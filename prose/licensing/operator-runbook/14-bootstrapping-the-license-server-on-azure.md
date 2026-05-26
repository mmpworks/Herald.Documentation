---
title: Bootstrapping the license server on Azure
slug: operator-runbook/14-bootstrapping-the-license-server-on-azure
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: in-progress (Phase D — Azure server workstream)
last-reviewed: 2026-05-21
related:
  - prose/licensing/explanation/where-the-license-server-runs.md
  - prose/licensing/explanation/how-licensing-works.md
related-external:
  - repo: mmpworks/MMP.Azure.Env
    path: docs/container-apps-bootstrap-2026-05-20.md
    label: First-light deployment notes (source for this runbook)
  - repo: mmpworks/MMP.Azure.Env
    path: scripts/sql/grant-mi-sql-access.ps1
    label: Grant a Managed Identity a SQL user
  - repo: mmpworks/MMP.Azure.Env
    path: scripts/sql/sql-smoke.ps1
    label: Smoke-test a SQL connection over Entra
---

# Bootstrapping the license server on Azure

This is the operator companion to
[where the license server runs](../explanation/where-the-license-server-runs.md).
The explanation page covers the conceptual flow and the cost
picture. This page covers the order to stand things up in, the
four gotchas that will bite you the first time, and the
production-gap list that has to close before the first paying
customer hits the system.

The bootstrap was first proven end-to-end on 2026-05-20 using a
no-business-value test app. The full session notes live at
[`MMP.Azure.Env/docs/container-apps-bootstrap-2026-05-20.md`](../../../../MMP.Azure.Env/docs/container-apps-bootstrap-2026-05-20.md).
This runbook is the trimmed, repeatable version.

> :information_source: **Status — Phase D, work in progress.**
> The real license server is the Workstream D deliverable. The
> test app proved the foundation (compute + identity + SQL). This
> runbook will grow as Workstream D actually lands. Until then,
> treat this as the deployment shape we know works, with the
> known gaps called out below.

## The order to stand things up in

Each step is idempotent. Re-running a step that already
happened is safe.

1. **Register the resource providers** in the subscription. One
   time per subscription. Names:
   `Microsoft.ContainerRegistry`, `Microsoft.App`,
   `Microsoft.OperationalInsights`.
2. **Create the Azure Container Registry** — `mmpworksacr`,
   Basic SKU. Admin user stays disabled. This is the only
   always-on $5/mo line item.
3. **Cloud-build the image** with `az acr build`. Uploads the
   build context, builds inside ACR, pushes the result. A small
   .NET 8 app takes about 50 seconds.
4. **Create the Container Apps environment** — `mmpworks-cae`,
   central US, `--logs-destination none`. Provisioning takes
   two to three minutes.
5. **Create the Container App** with system-assigned identity
   AND registry pull via that same identity. The
   `--registry-identity system` flag does both in one shot, so
   the Managed Identity exists before the first image pull.
6. **Create a SQL user for the Managed Identity** on
   `mmpworks-db1`. Connect as the Entra admin, run
   `CREATE USER [<app-name>] FROM EXTERNAL PROVIDER;` and grant
   the minimum role (`db_datareader` at first, then exactly the
   write permissions the issuance ledger needs).

The scripts that automate steps 1, 3, and 6 live in
[`MMP.Azure.Env/scripts/`](../../../../MMP.Azure.Env/scripts/).

> :bulb: **Quick picture.** The whole bootstrap is "create the
> warehouse, hire the worker, give the worker a badge, write the
> badge into the database's guest list." Once those four
> things are done, the worker walks into the database and gets
> what it needs without ever showing a password.

## The four gotchas that will bite you

These are the things that go wrong the first time. Each one
looks like a different problem at first, so name-recognition
matters.

### 1. Alpine .NET runtime crashes the first SQL call

The symptom: the app starts fine, serves the health endpoint
fine, then throws `System.NotSupportedException: Globalization
Invariant Mode is not supported` the moment any code tries to
open a SQL connection.

The cause: the Alpine variant of the .NET runtime
(`mcr.microsoft.com/dotnet/aspnet:8.0-alpine`) does not ship
with ICU and enables globalization-invariant mode by default.
`Microsoft.Data.SqlClient` needs culture support and refuses to
run without it.

**Fix:** use the Debian-based image
`mcr.microsoft.com/dotnet/aspnet:8.0` instead. The image is
about 100 MB larger, which is the right trade for a system that
has to be reliable. If Alpine is required for some reason,
`aspnet:8.0-alpine-extra` ships with ICU pre-installed.

### 2. Revision rollout has a brief stale-routing window

The symptom: you just deployed a new image, and the first
request after the deploy returns the old behavior. The next
request returns the new behavior. Looks like a cache problem.

The cause: Container Apps creates a new revision when you
update the image. With single-revision mode (the default), the
new revision gets 100% traffic *as soon as it becomes healthy*,
but the load balancer can still route one or two requests to
the old revision while it drains.

**Fix:** retry once. The window is seconds. If the second
request also returns stale behavior, then it's a real bug, not
the rollout.

### 3. Azure SQL serverless cold-resume looks like a hard failure

The symptom: the database has been idle for a while. A
connection attempt fails with `Database '...' is not currently
available. Please retry the connection later.` It looks like
the database is down.

The cause: the database auto-paused after 60 seconds of idle
(that's the free-tier SKU's behavior). When the first connection
arrives, the SQL gateway sometimes returns the
"not currently available" error instead of waiting for the
database to resume. SqlClient's built-in `ConnectRetryCount` and
`ConnectRetryInterval` parameters do *not* help here — they
handle network-level retries, not server-side "not yet ready"
rejections.

**Fix:** wrap `OpenAsync` in an application-level retry. Polly
is the standard choice in .NET. Three retries with exponential
backoff (1s, 2s, 5s) absorbs every cold-resume we've measured
so far (30 to 90 seconds in the worst case). The license server
must have this from day one — a customer activation that times
out at 3 a.m. is a refund-or-worse outcome.

### 4. Container Apps consumption has a shared outbound IP pool

The symptom: you try to lock down the SQL firewall by adding
each of the Container App's outbound IPs as a firewall rule.
The list returned by `az containerapp show` is about 160 IP
addresses, and that doesn't even fit.

The cause: Container Apps consumption tier shares a regional
outbound IP pool across many tenants. Those 160 addresses are
the pool, not "your app's IPs." Restricting the SQL firewall to
that pool would let every other consumption-tier tenant in the
region reach the database.

**Fix:** use the SQL firewall rule `AllowAllWindowsAzureIps`
(already enabled on `mmpworks-db1`) and rely on **Entra
authentication** for actual access control. The Managed Identity
plus the SQL user grant is the access boundary. The firewall
just enforces "must come from Azure," which is a weak signal —
the real signal is the identity.

## What needs to close before the first paying customer

The current deployment is dev-grade. These gaps must close
before real cash starts flowing through the system. Each one is
named with its monthly cost delta because the
[$200/mo budget envelope](../../../../herald/.claude/projects/E--dev-herald/memory/project_mmpworks_azure_account_budget_posture.md)
is real.

| Gap | What it is | Cost to close |
|---|---|---|
| **Cold-start latency** | DB auto-pauses; cold-resume is 30–90s | Drop auto-pause OR move to provisioned: ~$15–30/mo |
| **Zone redundancy + geo-failover** | DB is local-redundant central-US only; the issuance ledger needs to survive a regional outage | ~$30–60/mo on the DB tier |
| **Admin identity** | Admin is a personal MSA (`mmpworks2026@outlook.com`); limits group-RBAC ergonomics | $0 mechanical, but coordinate with Steve before moving |
| **Entra-only auth** | `azureADOnlyAuthentication: false` today; SQL auth is still enabled alongside Entra | $0; flip the flag after app accounts are sorted |
| **Separate dev DB** | This instance currently doubles as the sandbox; not safe once real keys are in it | New free-tier DB: $0; the dev DB stays free |
| **Audit + threat detection** | SQL auditing + Defender for SQL not turned on; issuance/revocation needs an append-only trail | Defender for SQL: ~$15/mo per server |
| **Tamper-evident issuance schema** | The ledger should be signed-chain consistent with TesseraSeal patterns | $0 storage delta; engineering work to design + apply |
| **App-level retry around DB open** | See gotcha #3; required for survivable activation calls | $0 |
| **Webhook ack speed under cold-start** | Container Apps cold-start + SQL resume can exceed Stripe's 10s webhook timeout | Keep `--min-replicas 1` (~$0.50/mo) OR ack fast + process async with a queue + worker |

Closing every line is roughly **$60 to $110/mo on top of the
~$5/mo bootstrap baseline**, depending on which DB tier we end
up on. That's the honest production cost picture.

> :bulb: **Quick picture.** Today the system is a card table in
> a garage. It works. Real customers need a desk in a room with
> a roof and a locked door. The numbers above are what the desk
> and the room and the door cost.

## What this runbook does not cover

- **Standing up Stripe.** The webhook side of the license
  server depends on Stripe being configured with the right
  signing secret and the right event subscription. That has its
  own runbook (forthcoming with Workstream E).
- **Minting the first test license.** That's a Workstream A +
  Workstream D handshake — `HeraldLicenseMinter` is already
  shipped on the engine side; the server-side endpoint that
  invokes it is what Workstream D adds.
- **The customer-facing install path.** When the customer pastes
  the key into their app, the verifier inside their app does the
  work. That's the
  [explanation page](../explanation/how-licensing-works.md)'s
  story, not this one.

## When something here is wrong

If a step in this article doesn't match what you see in Azure,
flag it in the `#licensing-ops` channel. The runbook follows the
deployment; when they drift, we fix the runbook.
