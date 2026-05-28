---
title: Why the demo is the FakeServer, and what's still open behind it
slug: explanation/planning/demoapp-jsx-server-api-gap
category: explanation
subcategory: planning
audience: contributor
since: 0.1.0-alpha.1
last-reviewed: 2026-05-28
status: decided-open-followups
related:
  - reference/live-viewer-admin-api
  - reference/demoapp-getting-started
related-records:
  - data/herald-oss/planning/demoapp-jsx-server-api-gap.json
mirrors:
  - Herald.RestApi.FakeServer (samples/DemoApp — the demo)
  - Modules/Server (Herald.Server — the legacy flat API)
  - Herald.RestApi.Host (the reference host)
---

# Why the demo is the FakeServer, and what's still open behind it

The public demo had a 404. Someone would install `Herald.DemoApp`, run
`herald-demo`, open the browser, and watch the panels fail to fill. The
SPA was calling an API the server had never built.

This page is the record of how that got resolved, the two traps that made
it confusing, and the one piece of work that is still planned and not
done. If you are picking up the demo cold, read this before you touch the
packaging.

## Two server stacks that do not speak the same language

Herald has two REST servers, and they answer different APIs. That is the
root of the confusion.

- **Herald.Server** (`Modules/Server`) speaks the **legacy flat API** —
  `/api/config/...`, `/api/pipeline/{name}/...`, `/api/levels`. It runs a
  real pipeline and serves the SPA, but it never registered the
  tenant-scoped Live Viewer routes.
- **Herald.RestApi.Host** speaks the **tenant-scoped Live Viewer API**
  the SPA actually depends on — `/api/tenants/{t}/pipelines/{p}/...`. But
  it is in-memory: no live pipeline, no SPA, no demo seed.

The JSX SPA was built against the tenant-scoped family. So it works
against the reference host's API shape but the reference host has nothing
real behind it — and it 404s against Herald.Server, which has a real
pipeline but the wrong API.

Neither server, by itself, is the demo.

> 💡 **Quick picture.** Two help desks. One has the right forms but no
> staff behind the counter. The other has staff but only accepts the old
> forms. The customer fills out the new form and gets turned away at both.
> You need one desk with the new forms *and* the staff.

## The FakeServer is the one desk with both

The FakeServer (`Herald.RestApi.FakeServer`) is the server that satisfies
every demo promise at once. It serves the JSX SPA, seeds a tenant, runs a
real Herald.OSS pipeline over synthetic events, and answers the
tenant-scoped Live Viewer API the SPA calls. The sample at
`samples/DemoApp` packages it as `Herald.DemoApp`, version
`0.1.0-alpha.1`.

So the decision, made 2026-05-28: **the public `herald-demo` is the
FakeServer sample.** Not the umbrella `Modules/DemoApp`.

## Trap one — two packages named like the demo

There are two things that look like "the DemoApp," and only one is.

- `Modules/DemoApp` — the umbrella package that wraps Herald.Server. This
  is the one that 404s.
- `samples/DemoApp` in the FakeServer repo — PackageId `Herald.DemoApp`,
  v0.1.0-alpha.1. This is the demo.

Repack or publish the wrong one and you ship a broken first impression.
The names are close enough that this is easy to get wrong, which is
exactly why it is written down here.

## Trap two — "just point it at the host that has the right API"

The reference host speaks the right API. It is tempting to point the demo
at it and call the 404 fixed. Don't. The reference host has no live
pipeline, no SPA, and no seed. You would trade a 404 for empty panels —
and the whole reason the demo exists is to let someone watch a *real*
Herald pipeline move events. Empty data breaks that promise more quietly
than a 404 does, which makes it worse.

## What's already fixed

Two edits already landed, and both are safe no matter how the open work
resolves:

- The primary demo pipeline in `Modules/Server/Program.cs` was renamed
  from `code-built-pipeline` to `default`. The OSS dashboard targets the
  pipeline named `default`, so this is correct under any path. The
  pipeline now registers as `default/default` and `/health` returns 200.
- The shipped JSX was repacked so its default scope is `default`/`default`
  rather than a stale `acme` value baked into an older build.

## What's still open — the production binding

Here is the honest gap. The Live Viewer API works against the FakeServer
and against the in-memory reference host. It is **not** yet bound to a
real `Herald.Server` pipeline. That binding is issue **#38** (Glenn D3).

The good news: the hard part already exists. The pipeline operations the
binding needs are already on `HeraldManagementApi` — get level styles,
get category styles, get custom levels, set minimum level, set the flight
recorder, add and remove enrichers. What is missing is the tenant-scoped
routing shell and the mapping from those operations into a
`LiveViewerState`. The route-mapping glue and the interface implementation
are both portable; they move, they do not get rewritten.

Two layered options are on the table:

- **A — the minimal first-impression fix.** Implement just
  `GET /live-viewer` over the existing `HeraldManagementApi` getters. The
  error banner clears, the panels hydrate, and live logs flow. Style edits
  and CRUD still 404, so it is a degraded surface — but "open the browser,
  watch a real pipeline" works. Small and low-risk.
- **B — the full production binding (issue #38).** Implement the whole
  `ILiveViewerAdminApi` over the real pipeline and host the entire
  tenant-scoped family. Everything in the SPA works. Larger, and it
  warrants an architecture review with Richard, a plan, code review, and
  tests before it lands.

One more thing that is *not* part of this: the Vue SPA deprecation. The
DemoApp already ships and serves the JSX SPA. The Vue port is a separate,
deprecated parallel client. Removing it fixes none of the API-gap issues
— it is independent cleanup.

The full option matrix and the issue tracking live in the structured
record this page mirrors:
`data/herald-oss/planning/demoapp-jsx-server-api-gap.json`.
