---
title: What the demo seeds — the tenant, pipeline, levels, enrichers, and sinks you see on first run
slug: tutorials/running-the-demo/what-the-demo-seeds
category: reference
audience: new-adopter
since: 0.1.0-alpha.1
status: current
created: 2026-05-28
last-reviewed: 2026-05-28
author: Heather (documentation agent)
related:
  - tutorials/running-the-demo
  - reference/live-viewer-admin-api
  - explanation/planning/demoapp-jsx-server-api-gap
related-records:
  - data/herald-oss/demo/demoapp-fakeserver-seed.json
mirrors:
  - Herald.RestApi.FakeServer (DemoSeeder.cs, DemoOptions.cs)
---

# What the demo seeds

When you run `herald-demo` with no flags, the tool seeds a working
pipeline and starts feeding it events. This page is the inventory of
what lands — so when you open the Live Viewer and see six levels, no
categories, and four active enrichers, you know exactly what you are
looking at and why.

The demo is the FakeServer sample, packaged as `Herald.DemoApp`
(v0.1.0-alpha.1). It is not a mock. A real Herald.OSS pipeline runs
inside the tool, and everything below is real seeded state.

## The tenant and pipeline

The seeder creates a tenant called `acme` (display name "Acme Corp") so
the demo carries a realistic-looking name. It also creates a `default`
tenant alongside it. That second one is not decoration — the SPA defaults
its scope to `default`/`default`, so that tenant has to exist for the
panels to hydrate.

Under the tenant sits one pipeline, id `default`, display "Default
Pipeline", status Running. It uses a memory buffer with capacity 1024 and
a minimum-level floor of Warning.

The pipeline's shape is a plain JSON bootstrap — the same document
`QuickLogBuilder` produces. You can see it on the Pipeline JSON tab. The
bootstrap stores **names**, never slugs or priority numbers, for levels,
categories, and enrichers. Hand-edit that JSON and restart, and you have
reconfigured the pipeline.

## Six levels — Serilog's set, nothing custom

Herald.OSS ships exactly six levels. They are Serilog's level set and
nothing else — Herald.OSS adds no custom level. The name is the identity,
so the feed's emitted severities match the panel names exactly.

| Level | Priority | Color |
|-------|----------|-------|
| Fatal | 1 | `#FF4D4D` (bold) |
| Error | 2 | `#FF6B6B` |
| Warning | 3 | `#FFD166` |
| Information | 4 | `#7DD3FC` |
| Debug | 5 | `#A3A3A3` |
| Verbose | 6 | `#6B7280` (italic) |

The minimum floor seeds to Warning, priority 3. The flight recorder is
**not** armed — the bootstrap ships no flight-recorder entry, and that
entry is the only source of truth for whether the recorder is present.
You add it from the catalog before there is anything to arm.

## Zero categories — by design

The Categories panel is empty on first run. That is correct. Herald.OSS
ships no categories.

A category is a topic field your application chooses. Herald.OSS passes
it through; it does not invent a starter list. So the panel fills from
whatever categories actually arrive on the feed. You see the real topics
in your own stream, not a fabricated demo set.

## Seven enricher classes, shown as their fields

The bootstrap lists seven Core enricher **classes**:

`ServiceIdentityEnricher`, `CorrelationIdEnricher`, `ActivityEnricher`,
`MachineNameLogEnricher`, `ProcessIdLogEnricher`, `ThreadIdLogEnricher`,
and `ExceptionDetailEnricher`.

But the panel does not show class names. It shows the **fields** those
classes emit, keyed by the snake-case field name. The reason is that one
class can emit several fields.

> 💡 **Quick picture.** Think of a form-letter mail merge. One template
> field, "address," expands into street, city, state, and zip on the
> printed page. The enricher class is the template field; the panel rows
> are the printed lines. `ServiceIdentityEnricher` is one class, but it
> prints four fields. `ProcessIdLogEnricher` prints two — `process_id`
> and `process_name`. The panel keys on what gets printed, because that
> is what you actually style and toggle.

That snake field-name is one id all the way through: it is the panel id,
the SSE envelope key, and the SPA's tint-match id. No translation, no
drift.

Four fields default to active because they produce real values on the
synthetic feed: `machine_name`, `process_id`, `thread_id`, and
`correlation_id`. The rest — `process_name`, `is_thread_pool_thread`,
`trace_id`, `span_id`, and the `service_*` fields — default inactive.
They have no honest value on the demo feed and would render blank, so you
turn them on once your own app supplies the context.

One class, `ExceptionDetailEnricher`, emits no panel field. It writes
`exception.*` properties only when there is an exception, so it is in the
bootstrap class list but not in the panel.

## Two sinks wired, five loaded, eighty more advertised

The seed pipeline wires two sink **instances**:

- `console` (`herald.console`) — the human-readable stream in the
  terminal where `herald-demo` runs.
- `live-feed` (`http_json`) — the honest source of the browser view. It
  POSTs each rendered event to a loopback endpoint so the browser sees
  the same stream the console does. It is a real sink with an editable
  target URL, visible in the Sinks tab. Disable it and the live view goes
  dark — which tells you it is doing real work.

Behind those instances, the host **loads** five sink kinds it can build:

| Kind | Display | Package |
|------|---------|---------|
| `herald.console` | Console | Herald.OSS |
| `herald.text-file` | Text File | Herald.Sinks.File |
| `herald.json-file` | JSON File | Herald.Sinks.File |
| `herald.otlp` | OTLP Exporter | Herald.Sinks.Otlp |
| `http_json` | HTTP JSON | Herald.Sinks.HttpJson |

Beyond the loaded five, the host **advertises** the other eighty-plus
sinks from a CI-validated manifest. Advertised sinks have no shipped
provider — they give the install dialog a target. Loading a sink and
using it are two different jobs: downloading the package makes a kind
available; configuring it and adding it to a pipeline is the separate act
of putting it to work.

## The feed is real, and you can feed it yourself

A source emits synthetic events at roughly one to ten per second through
the canonical Default pipeline strategy. The pipeline fans out to the two
sinks, and the browser watches the same stream the console does. When you
change the pipeline from the Live Viewer, it rebuilds and the change
shows on the next event.

Want your own events? POST newline-delimited JSON log envelopes to
`/api/logs/incoming`. The synthetic feed steps aside while a real producer
is active, so your events flow through the exact pipeline you see on
screen.

The full set of seeded values — every level color, every enricher field,
the sink package ids — lives in the structured record this page mirrors:
`data/herald-oss/demo/demoapp-fakeserver-seed.json`.
