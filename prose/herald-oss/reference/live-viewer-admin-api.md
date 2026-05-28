---
title: The Live Viewer admin API — the tenant-scoped surface the Dashboard speaks
slug: reference/live-viewer-admin-api
category: reference
subcategory: rest-api
audience: intermediate
since: 0.1.0-alpha.1
last-reviewed: 2026-05-28
status: implemented-fakeserver
related:
  - reference/demoapp-getting-started
  - explanation/planning/demoapp-jsx-server-api-gap
related-records:
  - data/herald-oss/rest-contracts/live-viewer-admin.json
mirrors:
  - Herald.RestApi.Contracts (ILiveViewerAdminApi, LiveViewer DTOs)
  - Herald.RestApi.FakeServer (the implementation the demo runs)
---

# The Live Viewer admin API

The Dashboard SPA does two things. It shows a live log feed, and it lets
you program the pipeline that produces the feed. The Live Viewer admin
API is the second half — the routes the SPA calls to read the pipeline's
shape and to change it.

Every route is scoped to one tenant and one pipeline. The path always
starts the same way:

```
/api/tenants/{tenantId}/pipelines/{pipelineId}/...
```

That scoping is the whole point. A request can only touch the tenant and
pipeline named in its own path. A principal scoped to a different tenant
gets a 403. The boundary is in the URL, so it is hard to get wrong.

> 💡 **Quick picture.** Think of a building with one master key per
> floor. The key opens every door on its floor and no door on any other.
> The tenant id in the path is that floor key. The Live Viewer routes
> hand you the rooms on your floor — your levels, your categories, your
> enrichers — and the lock checks your key on the way in.

## Read first, then write

The SPA starts with one read:

```
GET /api/tenants/{t}/pipelines/{p}/live-viewer
```

That returns a `LiveViewerState` — the whole panel state in one object.
Levels, categories, enrichers, the minimum-level floor, and the
flight-recorder setting all come back together. Each list also carries
an ETag, a version token for that list at the moment you read it.

The SPA hydrates its panels from this one response. It reads the same
route again later, when another tab changes something and the SPA needs
to catch up.

This is the route that was missing when the demo first 404'd. The JSX
SPA called `/live-viewer`, the server it talked to had never implemented
it, and the panels never filled. The fix was to point the demo at the
server that does implement it. The
[planning record](../explanation/planning/demoapp-jsx-server-api-gap.md)
walks that whole story.

## The mutation panels

Writes are split into three families — one per panel:

- **Levels** — style a level, set the minimum-visible floor, set the
  flight-recorder threshold, reorder the list, add a level, remove one.
- **Categories** — style, active toggle, add, remove.
- **Enrichers** — style, active toggle, add, remove, plus an opaque
  config PATCH for enricher-specific settings.

Each family is one job, so the routes read cleanly. Styling a level is
`PATCH .../levels/{levelId}/style`. Adding a category is
`POST .../categories`. The shape is the same across all three panels,
which means once you know one, you know the others. That is CUPID's
*Unix philosophy* property in practice — each route does one thing, and
the panels compose by URL, not by a tangle of special cases.

## What a 200 promises

Every PATCH on this surface carries one timing promise: a `200` means
the change is **accepted and queryable**. By the time the response lands,
a follow-up `GET /live-viewer` already reflects the change. You do not
poll. You do not wait for an event. The write is done.

That promise is what lets the SPA feel instant. It applies the change
locally, sends the PATCH, and trusts the `200`. If the server could not
keep the promise, the SPA's optimistic-update machinery would drift, so
every server that implements this contract has to honor it.

## ETags keep two editors honest

Reorder and delete carry an ETag. The idea is simple: the version you
saw when you read has to still be the current version when you write. If
someone else moved the list in between, your ETag is stale and the
server answers `409 Conflict`.

> 💡 **Quick picture.** Two people editing the same shared doc. You both
> opened version 5. You save first — now it's version 6. When the other
> person tries to save against version 5, the system says "this moved,
> reload and try again." The ETag is the version number. The 409 is the
> "this moved" message.

Style and active toggles do not carry an ETag. They change one row's
appearance, not the list's membership, so there is nothing to collide
on. Delete is opt-in: send an ETag for the safe check, or send a bodyless
DELETE for an unconditional remove. Deleting a level that is already gone
is a success, not an error — asking twice and getting the same answer is
the point.

## The SSE channel tells tabs to catch up

When you change something, other open tabs need to know. They find out
through a server-sent event on the per-tenant stream:

```
GET /api/tenants/{t}/events/stream
```

After every successful mutation the server publishes a `config-change`
event. The event is a **hint, not a payload**. It says "a level was
updated" or "a category was deleted" — enough for a tab to know which
panel to re-read. The tab then calls `GET /live-viewer` to get the real
state. The event never carries the new state itself, because the GET
against the canonical state is the one source of truth.

The tab that made the change does not need the hint. It already has the
authoritative state from its own PATCH-200. So the event carries an
`originToken` — the tab's own id, captured from the `X-Herald-Origin-Tab`
header. When a tab sees its own token come back, it drops the event
instead of re-reading. No echo, no wasted round-trip.

## Who implements this today

The contract types live in `Herald.RestApi.Contracts`. The wire shape is
what a client depends on; the package is just where the shape is written
down.

The implementation the public demo runs is the FakeServer
(`Herald.RestApi.FakeServer`). It honors the whole family end to end —
hydrate, mutate, re-hydrate, live feed. The reference host
(`Herald.RestApi.Host`) honors the route shapes too, but over an
in-memory store with no live pipeline behind it.

What does **not** exist yet is the production binding: this family hosted
over a real `Herald.Server` pipeline. The pipeline operations already
exist on `HeraldManagementApi`; the missing piece is the tenant-scoped
routing shell plus the `LiveViewerState` mapping. That work is tracked as
issue #38. The
[planning record](../explanation/planning/demoapp-jsx-server-api-gap.md)
has the full disposition.

The full route table, request and response shapes, and status codes live
in the structured record this page mirrors:
`data/herald-oss/rest-contracts/live-viewer-admin.json`.
