---
title: What MMP.Licensing intentionally does not support at GA
slug: explanation/non-support-faq
category: explanation
audience: customers, sales, support, engineering
since: 2.0
status: published
last-reviewed: 2026-05-17
related:
  - explanation/how-licensing-works
related-records: []
related-external:
  - repo: mmpworks/MMP.Licensing
    path: doc/adr/0001-mmp-licensing-architecture.md
    label: ADR-0001, Explicit non-support at GA
---

# What MMP.Licensing intentionally does not support at GA

The "Explicit non-support at GA" section is essentially: "Here are
the things the product intentionally does NOT support at launch."

GA means: General Availability — the first real production
release customers can buy and rely on.

This section is actually very healthy engineering. It prevents:

- accidental promises
- sales overcommitting
- architecture ambiguity
- hidden assumptions
- "wait, I thought it supported…" disasters

The key thing to understand: **These are NOT bugs. They are
consciously deferred business/product/engineering decisions.**

This page translates the deferred items from
[ADR-0001](../../../../Modules/Herald.Licensing/doc/adr/0001-mmp-licensing-architecture.md)
into plain English. For every item you get four things: the
technical name from the ADR, what it means in everyday terms, why
we're saying "not yet," and what would trigger us to support it
later.

The page then closes with a second group — frequently asked side
questions that aren't about deferred features but come up in the
same conversations: dev licensing, environments, pricing,
security posture, and chain of custody.

If you want the mechanics of how the system works today, read
[how MMP.Licensing works](./how-licensing-works.md). This page is
the companion — it covers the edges we *haven't* built yet and
explains why.

> 💡 **The frame that matters most.** Pro and Enterprise are
> NOT trying to be unforkable. Someone can absolutely fork
> Herald.OSS and write their own loggers. They'll own the
> engineering, the bugs, the design decisions, the corner cases
> forever. Pro and Enterprise pay for **someone else owning that
> complexity for you.** That's the real moat — reliability,
> expertise, maintenance, support, operational confidence,
> long-term stewardship. Read every "not yet" answer below
> through that lens. We're not gatekeeping features; we're being
> honest about what's inside our support boundary today and
> what's outside it.

## What's on this page

**Deferred items from ADR-0001:**

1. [Serverless](#1-serverless)
2. [Dev containers on prod fleet token](#2-dev-containers-on-prod-fleet-token)
3. [Sidecar discount](#3-sidecar-discount)
4. [Multi-region active/passive discount](#4-multi-region-activepassive-discount)
5. [Batch fanout above cap](#5-batch-fanout-above-cap)
6. [K8s HPA above cap](#6-k8s-hpa-above-cap)
7. [Edge with 24h offline + online check-in](#7-edge-with-24h-offline--online-check-in)
8. [NFS multi-host air-gapped](#8-nfs-multi-host-air-gapped)
9. [Customer-of-customer multi-tenancy slot count](#9-customer-of-customer-multi-tenancy-slot-count)
10. [DR split-brain burst](#10-dr-split-brain-burst)
11. [Multi-user customer org self-service](#11-multi-user-customer-org-self-service)
12. [Self-revoke from customer portal](#12-self-revoke-from-customer-portal)
13. [Programmatic API key for token retrieval](#13-programmatic-api-key-for-token-retrieval)
14. [Third-party observability sinks for license telemetry](#14-third-party-observability-sinks-for-license-telemetry) — *now in GA scope*
15. [Per-tenant `tnt` slug validation](#15-per-tenant-tnt-slug-validation)
16. [Bundle-token wire format](#16-bundle-token-wire-format)
17. [In-process `LicenseRegistry.AddToken`](#17-in-process-licenseregistryaddtoken)
18. [Numbered env vars](#18-numbered-env-vars)

**Frequently asked side questions:**

19. [Are dev licenses free?](#19-are-dev-licenses-free)
20. [What environments do you recognize?](#20-what-environments-do-you-recognize)
21. [Why per-host pricing instead of per-event?](#21-why-per-host-pricing-instead-of-per-event)
22. [Where do the signing keys live? Who has access?](#22-where-do-the-signing-keys-live-who-has-access)
23. [Will my SAST scanner flag the embedded public key?](#23-will-my-sast-scanner-flag-the-embedded-public-key)
24. [Are you SOC 2 certified?](#24-are-you-soc-2-certified)

---

## 1. Serverless

**Plain English:** "If your app spins up thousands of tiny
short-lived cloud functions, our normal host-based licensing
model doesn't fit well."

**Why we're saying "not yet":** Your current model is: machines
claim slots, leases renew over time, stable identities matter.
Serverless breaks this because functions appear/disappear
constantly, there may be 1000 instances for 3 seconds, no stable
machine identity exists. So your stance is: "Use a different
pricing model for serverless."

**What would trigger support later:** When pricing decides to
ship a per-function-metering SKU.

---

## 2. Dev containers on prod fleet token

**Plain English:** "Dev work runs on a free dev license, not on
your production fleet token."

**Why we're saying "not yet":** Mixing the two means dev laptops,
CI runners, test containers, and local Docker images burn
production capacity unpredictably. We split the two so neither
side surprises you.

This is *not* a paywall on developer experience. **Professional
development seats are free.** Any company on Pro or Enterprise
gets free dev seats for their team, and any individual developer
can grab a personal free dev key from
[portal.mmpworks.com/dev](https://portal.mmpworks.com/dev). See
[#19](#19-are-dev-licenses-free) for the details.

**What would trigger support later:** When customers ask for a
unified dev/prod billing view that still keeps the environments
separate operationally.

---

## 3. Sidecar discount

**Plain English:** "If your architecture runs helper containers
beside the main app, those still count as licensed hosts."

**Why we're saying "not yet":** A pod might have: main app
container, logging sidecar, telemetry sidecar, auth sidecar. Some
customers may later argue: "Those shouldn't count." At launch
they DO count. But the schema is already designed so this can
change later (that's what `parent_lease_id` means).

**What would trigger support later:** When customers complain
about double-charging for sidecar patterns.

---

## 4. Multi-region active/passive discount

**Plain English:** "If you run a disaster recovery datacenter,
both sites count toward licensing."

**Why we're saying "not yet":** Example: East Coast primary, West
Coast standby. Customer expectation: "Standby shouldn't count."
Launch answer: "It does count." DR pricing gets messy fast.

**What would trigger support later:** When customers ask for
active/passive pricing.

---

## 5. Batch fanout above cap

**Plain English:** "Your bill stays predictable. If a batch job
tries to burst above your purchased capacity, the extra workers
stop instead of silently turning into a surprise invoice."

**Why we're saying "not yet":** A nightly analytics job might
burst to 500 workers. Elastic billing sounds friendly until the
invoice arrives. At GA, the cap you bought is the cap you pay
for — no overage charges, no auto-burst billing, no "your run
cost 4x what you expected." If you know you need batch capacity,
we'd rather you size for it deliberately.

**What would trigger support later:** When customers ask us for
a batch-hours SKU with documented overage pricing. We'd rather
ship that as its own clear product than bolt elastic billing onto
the per-host model.

---

## 6. K8s HPA above cap

**Plain English:** "Kubernetes can scale your app up to your
purchased cap. Pods that would push above the cap don't start,
so a runaway HPA can't quietly turn into a runaway bill."

**Why we're saying "not yet":** Auto-burst billing is the kind
of feature that sounds great until 3 a.m. on a holiday weekend
when an HPA misconfigures and you wake up to a five-figure
overage. At GA, we'd rather give you a cap you can reason about
than an elastic ceiling that punishes a bad HPA config. If your
fleet's real steady-state is above today's tier, the right
answer is to move to a tier that fits, not to pay overage rates
per pod-hour.

**What would trigger support later:** When customers tell us
their workload genuinely needs a burst tier, and we can design
one with documented per-host overage rates instead of surprise
math.

---

## 7. Edge with 24h offline + online check-in

**Plain English:** "We do not support occasionally-connected
edge devices yet."

**Why we're saying "not yet":** Examples: oil rigs, ships,
factory floors, retail edge appliances. We currently support
fully online OR fully air-gapped. But NOT
mostly-offline-with-intermittent-sync. That's actually a huge
product category. Very wise to defer.

**What would trigger support later:** When a true edge SKU is
requested.

---

## 8. NFS multi-host air-gapped

**Plain English:** "We do not support multiple disconnected
machines sharing a network drive for licensing."

**Why we're saying "not yet":** This becomes a nightmare because
NFS locking is unreliable, stale files happen, split-brain
occurs. We're wisely avoiding distributed consensus problems in
v1.

**What would trigger support later:** When a customer requires
shared-storage air-gap.

---

## 9. Customer-of-customer multi-tenancy slot count

**Plain English:** "If you host your own customers on top of
Herald, you pay for the hosts you run — full stop. We don't
meter your tenant count, your org count, or your account count."

**Why we're saying "not yet":** A SaaS platform with 10,000
tenants pays the same as a SaaS platform with 100, if they run
on the same number of hosts. That's deliberate. Per-tenant
pricing punishes growth and forces our billing system inside
your application's domain model — neither of those is something
we want to do at GA. Your tenant boundary is your business; our
boundary is the host. We expect this to stay this way unless a
clear customer case for per-tenant billing emerges with a
pricing shape we can actually defend.

**What would trigger support later:** When customers ask us for
per-tenant pricing and we can design one that doesn't penalize
growth or require us to crawl through their app's tenant model.

---

## 10. DR split-brain burst

**Plain English:** "If both disaster recovery regions
accidentally run simultaneously and double usage, we don't
handle that gracefully yet."

**Why we're saying "not yet":** Advanced enterprise edge case.
The schema column `burst_hosts_max` is already reserved —
meaning we anticipated it.

**What would trigger support later:** When a customer encounters
this during a DR drill.

---

## 11. Multi-user customer org self-service

**Plain English:** "Only one admin user per customer
organization at launch."

**Why we're saying "not yet":** No role systems, teams, org
permissions, or delegated admins yet.

**What would trigger support later:** v2.

---

## 12. Self-revoke from customer portal

**Plain English:** "Customers cannot revoke licenses themselves
yet."

**Why we're saying "not yet":** Support/operator must do it.
Good launch simplification — revoke is destructive.

**What would trigger support later:** v1.1.

---

## 13. Programmatic API key for token retrieval

**Plain English:** "Apps cannot automatically fetch tokens via
API yet."

**Why we're saying "not yet":** Currently humans provision
tokens. No CI/CD automation, automated provisioning, or secret
bootstrap APIs.

**What would trigger support later:** v2.

---

## 14. Third-party observability sinks for license telemetry

> ✅ **Now in GA scope as of 2026-05-17.** This item moved out
> of "not supported" and into the shipping plan. MMPWorks is
> fundamentally a logging company. Saying "we only support App
> Insights" was awkward when our own core product is structured
> logging that can sink anywhere. So we fixed it.

**Plain English:** "License telemetry shows up in whatever
observability tool your team already uses — Datadog, Logfire,
Splunk, OTLP collectors, or anything else Herald.OSS supports."

**How it works at GA — the two-channel design.** License
telemetry runs on two parallel channels:

- **The internal channel** is an HTTPS POST to the MMPWorks
  license server. This is what we use to make license decisions:
  renewals, capacity checks, denylist updates. It's authenticated,
  signed, and goes nowhere else. The internal channel is fixed
  and is not customer-configurable.
- **The customer-visible channel** mirrors those same events
  through a Herald.OSS sink. You point it at Datadog, Logfire,
  Splunk, an OTLP endpoint, an Elastic cluster, or any other
  sink Herald.OSS ships. Your existing dashboards see license
  events alongside the rest of your application telemetry.

The two channels carry the same facts; the mirror is for *your*
visibility, not for license enforcement. Enforcement always
flows through the internal channel.

**Why this matters:** You don't have to add yet another vendor
console to your on-call rotation. License health surfaces in the
same place as everything else you watch.

**What's still deferred:** Customer-controlled sampling and
filtering of the mirror channel — at GA, the mirror is on or off
per host, not per-event. Per-event filter rules are a v1.1
candidate if customers want them.

---

## 15. Per-tenant `tnt` slug validation

**Plain English:** "We trust manual coordination for tenant
naming right now."

**Why we're saying "not yet":** No automated namespace collision
checking yet.

**What would trigger support later:** v1.1.

---

## 16. Bundle-token wire format

**Plain English:** "One token only licenses one product."

**Why we're saying "not yet":** Instead, multiple token files in
a directory. Good simplification.

**What would trigger support later:** When customer pain demands
a single combined token.

---

## 17. In-process `LicenseRegistry.AddToken`

**Plain English:** "Apps cannot dynamically inject tokens through
code yet."

**Why we're saying "not yet":** Instead, filesystem/env-based
loading only. Smart security-wise for v1.

**What would trigger support later:** When a customer requires
programmatic load.

---

## 18. Numbered env vars

**Plain English:** "We are NOT supporting ugly env var systems
like `MMP_LICENSE_TOKEN_1`, `MMP_LICENSE_TOKEN_2`."

**Why we're saying "not yet":** Instead, directory-based token
loading. Cleaner operationally.

**What would trigger support later:** Never. Directory shape
dominates.

---

# Frequently asked side questions

The items above are deferred features. The items below are
recurring questions that come up in the same conversations.
They're not "not yet" answers — they're "here's our actual
stance" answers.

## 19. Are dev licenses free?

**Plain English:** "Yes. Professional development seats are
free. We don't charge engineers to write code against Herald."

**Two ways to get a dev seat:**

- **Company on Pro or Enterprise.** Free professional development
  seats for your team are included with your subscription. No
  separate purchase, no seat true-up, no surprise invoice.
- **Individual developer.** Any developer can grab a personal
  free dev key from
  [portal.mmpworks.com/dev](https://portal.mmpworks.com/dev) —
  no employer, no company purchase required. Use it on your
  laptop, your home lab, a side project.

**What's inside a dev token:** The token carries `flv: dev`,
`is_dev_host: true`, and `lim.hosts: 3` — meaning each dev key
covers up to 3 hosts (typically your laptop + a CI runner +
maybe a staging container). Production sinks reject any event
tagged from a dev-flavored token, so you can't accidentally let
dev traffic land in a production telemetry stream.

**The principle.** "Free for development" not "free for
hobbyists." A real engineer at a real company doing real work
against Herald should never feel like the license is in their
way. The paywall is at production, where the value lands.

## 20. What environments do you recognize?

**Plain English:** "Two environments at GA — dev and production.
A third — evaluation — is reserved for later."

The framework we design against:

| Environment | Status at GA | What it's for |
|---|---|---|
| **Dev** | Free, shipping | One developer's local box; CI runners; personal projects |
| **Production** | Paid, full SLA | Anything customer-facing, anything with a real on-call rotation |
| **Evaluation** | Reserved, future SKU | An organization trying Herald end-to-end before committing |

**Why "evaluation" isn't shipping at GA.** Org-trial mechanics
need their own permissioning, their own time-bounded enforcement,
and their own conversion path. Doing them right is a separate
shape than a personal dev key. We'd rather ship dev cleanly at
GA and add an evaluation SKU when the sales motion needs it,
than ship two half-baked things at once.

## 21. Why per-host pricing instead of per-event?

**Plain English:** "Per-event pricing punishes bad days. We
don't want to be in that business."

The day your application has a real incident is the day it
emits 10x its normal log volume. A per-event price model means
your worst day is also your most expensive day. That's a
perverse alignment — your logging vendor profits when you're in
pain.

We charge per host instead. Your bill is predictable. A bad day
costs you what a good day costs you. Your finance team can
forecast.

**The shape:** Volume discounts are encoded directly in your
token, and bundle tiers make the math obvious.

| Tier | Host count |
|---|---|
| Pro Team | ≤ 25 hosts |
| Pro Fleet | ≤ 100 hosts |
| Pro MSP | ≤ 500 hosts |
| Enterprise | Negotiated |

You buy a tier; the token enforces it. No metering pipeline, no
surprise overages, no incentive for either side to be unhappy
about a traffic spike.

## 22. Where do the signing keys live? Who has access?

**Plain English:** "Signing keys live in Azure Key Vault
Premium, HSM-backed and FIPS 140-2 Level 2 certified. No
employee has direct access."

The license server talks to Key Vault over an authenticated
channel and asks it to sign a payload. Key Vault produces the
signature and returns it. The private key bytes never leave the
HSM boundary. There is no `kv export-key` button, no break-glass
"give me the bytes" mode, no engineer with a copy.

This is a stronger claim than "we keep our keys safe." The HSM
is enforcing the access policy in hardware. Even if someone
compromised the license server itself, they could ask the HSM to
sign things while they had access — but they couldn't extract
the key and use it later from somewhere else. Recovery from a
server compromise is "rotate the Key Vault credentials." There
is no equivalent recovery cost for "we lost the key" because the
key never moved.

> 💡 **Quick picture.** Imagine a notary public who keeps the
> official seal locked inside a vault that opens only when the
> notary is physically present. You can hand the notary a
> document to stamp; you can never take the seal home. Even if
> someone broke into the notary's office, they couldn't steal
> the seal — only get a few stamps before the alarm tripped.
> Azure Key Vault Premium is that vault. The license server is
> the notary. The private key is the seal.

## 23. Will my SAST scanner flag the embedded public key?

**Plain English:** "Probably not — we've already pre-submitted
our public key bytes to the major scanners as trusted publisher
fingerprints. If yours still flags them, we ship a one-paste
suppression file."

The embedded public key in our SDK looks, to a naive scanner,
like "hardcoded cryptographic material" — which is normally a
security smell. But our public key is supposed to be embedded.
That's how the verifier checks signatures without phoning home.

We pre-registered the fingerprint with:

- Snyk
- Veracode
- SonarQube
- GitHub Code Scanning
- Semgrep

Those scanners recognize the bytes and don't flag them.

If your scanner isn't on that list, or your local policy still
trips on the pattern, drop our
[`.sast-suppress.yml`](https://portal.mmpworks.com/downloads/sast-suppress.yml)
into your repo. One paste, one commit. You don't need to chase
your security team for an exception — you can tell them the
vendor already documented the suppression.

**Why this matters.** A security flag from a scanner is a real
cost. It eats engineering time, it eats security-team review
cycles, and it tends to surface during a release window when
nobody wants to debate cryptography. Pre-registering the
fingerprint takes that whole conversation off your plate.

## 24. Are you SOC 2 certified?

**Plain English:** "Not today. We're transparent about that, we
have a published roadmap, and our cloud infrastructure already
runs on SOC 2-certified sub-processors."

The honest status:

- **MMPWorks is not SOC 2 certified at GA.**
- **We offer a vendor security questionnaire** — fill it out
  with us, share with your procurement team, get a real
  document on file.
- **Our published roadmap commits to SOC 2 Type I within 6
  months of GA, Type II within 18 months.** Those dates are
  internal commitments we'll publish externally once the audit
  schedule is firm.
- **Our cloud infrastructure runs on SOC 2-certified
  sub-processors.** Azure (license server, Key Vault,
  observability backend) and Stripe (billing) are both SOC 2
  certified. That doesn't make MMPWorks certified, but it does
  mean the layers beneath us already meet the standard your
  auditors care about.

**Why we're saying this out loud.** Some vendors fudge this
question, hoping the procurement team won't dig. We'd rather
tell you on day one that we're not certified yet, show you the
roadmap, and let you decide whether the questionnaire +
sub-processor evidence is enough to bridge the gap until the
Type I audit completes. It usually is.

---

## Big picture

This section is actually saying: "We intentionally chose
operational simplicity over feature completeness."

That is excellent engineering discipline.

Most teams hide these limitations. Our ADR explicitly says:
"Here is where the product boundary currently is."

That's extremely valuable because engineering knows scope, sales
knows scope, support knows scope, customers know scope, future
architects know scope.

The "v1.1 trigger" column means: "What real-world customer
pressure would justify building this?"

That's smart product thinking — we're not gold-plating
prematurely.

## See also

- [ADR-0001, the engineering rationale behind every item above](../../../../Modules/Herald.Licensing/doc/adr/0001-mmp-licensing-architecture.md)
- [How MMP.Licensing works](./how-licensing-works.md) — the mechanics
