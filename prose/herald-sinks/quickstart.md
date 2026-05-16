---
title: Quickstart — Herald.Sinks
slug: quickstart
category: landing
audience: new-adopter
since: 1.0.0
last-reviewed: 2026-05-16
related:
  - reference/sinks/signalfx
  - howtos/pick-the-right-sink
related-records:
  - data/herald-sinks/sinks/signalfx.yaml
---

# Quickstart — Herald.Sinks

You have a Herald.OSS pipeline running. Your events are going to
the console. Now you want them in a real destination: SignalFx,
Datadog, S3, Elasticsearch, somewhere operators can search and
alert on. This page is the five-minute path.

The running example is the SignalFx sink. Every other sink in the
catalog follows the same four steps: pick the package, install it,
point it at the destination, send events. Swap in the package name
and the connection details for whatever destination you actually
use.

If you have not built a Herald pipeline yet, start with
[the Herald.OSS first-pipeline tutorial](../herald-oss/tutorials/first-pipeline.md)
and come back here when your console sink is working.

## Install

```bash
dotnet add package Herald.Sinks.SignalFx
```

That one package brings the sink, its provider, and the
auto-registration shim. No `RegisterAll(...)` call is required.
The package's `[ModuleInitializer]` adds itself to
`LogSinkProviderRegistry.Default` the moment the assembly loads.

## Point the pipeline at the sink

```csharp
using MMP.Herald.OSS;
using MMP.Herald.OSS.Quick;

var result = QuickLogBuilder
    .Create()
    .WithSink("signalfx", new
    {
        host  = "us0",                 // realm; or set `uri` for self-hosted
        alias = "${SIGNALFX_TOKEN}"    // X-SF-Token, read from env
    })
    .Build();

var logger = result.Logger;

logger.Info(LogCategory.App, "Order placed: {OrderId}", "ord_7421");
logger.Warn(LogCategory.App, "Slow checkout: {DurationMs} ms", 1203);
```

Set the `SIGNALFX_TOKEN` environment variable to your access token
and run the app. Two events land in SignalFx, each with its
properties as searchable fields and the message as the event text.

> **Quick picture.** Think of Herald.Sinks like power adapters in
> a travel kit. The logger is your laptop. It speaks one shape of
> output. The destination is the wall socket, and every country
> wired the socket a little differently. The sink is the adapter
> that bridges the two. You do not rewire the laptop and you do
> not rewire the socket. You pick the adapter that matches the
> room. Add a new destination, swap in a new adapter.

## Why sinks are their own thing

Herald.OSS knows what an event is. It does not know how SignalFx
authenticates, how Datadog batches, or how S3 names objects.
Putting transport knowledge inside the core would couple every
destination upgrade to a Herald.OSS release. So each sink is its
own NuGet package, with its own version, its own changelog, and
its own `CAPABILITY.yaml` manifest.

That is CUPID's *Unix philosophy* applied to a logging library.
Each piece does one job, and the pieces compose. And it is a DRY
win on top of that: the contract every destination implements
(`ILogSinkProvider`) lives in one place, and every sink in the
catalog uses the same `CAPABILITY.yaml` schema, so the docs, the
Dashboard form, and the release pipeline all read the same
description without us writing it three times.

## Where to go next

**You want to find the right destination.** Open the
[capability matrix](./reference/sinks/index.md). One row per sink,
sortable by category, edition, and AOT compatibility.

**You want to build a custom sink.** Read
[contribute a new sink](./howtos/contribute-a-new-sink.md). It walks
the `ILogSinkProvider` contract, the `CAPABILITY.yaml` shape, and
the test pattern every existing sink follows.

**You want to understand the auto-registration.** Read
[the auto-registration pattern](./explanation/auto-registration-pattern.md).
It explains how `dotnet add package` is the whole workflow, and
what the `analyzers/dotnet/cs/` packaging rule prevents.

## What you do not need to do

- **No manual registration call.** The sink registers itself on
  assembly load. If you find yourself writing
  `RegisterAll(...)` or `WithSinkProvider(new SignalFxLogSinkProvider())`,
  the sink package was probably built without the
  `analyzers/dotnet/cs/` packaging rule and the
  `[ModuleInitializer]` never fired. Check the package contents.
- **No core upgrade for a sink upgrade.** A new SignalFx package
  ships independently. `dotnet update package Herald.Sinks.SignalFx`
  is the whole change.
- **No custom serialization.** The sink reads the `LogEvent` Herald
  already produced. Per-event properties land at the destination's
  preferred shape (payload root for SignalFx, structured fields for
  Datadog, columns for SQL sinks). The mapping is the sink's job,
  not the application's.

The pattern Herald.Sinks enforces is small on purpose. One package
per destination. One manifest per package. One registration shim
per package. The catalog grows by adding new packages, not by
editing old ones.
