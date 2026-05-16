---
title: Quickstart — Herald.OSS
slug: quickstart
category: landing
audience: new-adopter
since: 0.2.2
last-reviewed: 2026-05-16
related:
  - tutorials/first-pipeline
  - explanation/kernel-vs-chain
related-records: []
---

# Quickstart — Herald.OSS

You have a .NET 8 app. You want a logger that is fast, structured,
and stays out of your way. This page is the five-minute path.

## Install

```bash
dotnet add package MMP.Herald.OSS
```

That one package brings the logger, the source generators, and the
built-in console sink. No other dependencies are needed for the
first run.

## The smallest useful pipeline

```csharp
using MMP.Herald.OSS;
using MMP.Herald.OSS.Quick;

var result = QuickLogBuilder
    .Create()
    .WithConsoleSink()
    .Build();

var logger = result.Logger;

logger.Info(LogCategory.App, "Service started on port {Port}", 8080);
logger.Warn(LogCategory.App, "Slow request: {DurationMs} ms", 412);
```

Run the app. You will see two structured events on your console,
each with the property captured as a separate field.

> **Quick picture.** Think of `QuickLogBuilder` like a kettle. One
> button to fill it, one button to boil. You do not need to know
> how the heating element works to get tea. The kettle is the
> entry point; the kernel underneath is the heating element.

That is the whole "hello world." The logger does the right thing
by default — minimum-level filter at `Info`, structured properties,
zero allocations on the accept path for properties up to arity 8.

## Where to go next

Three places make sense from here.

**You want to walk one step at a time.** Read
[the first-pipeline tutorial](./tutorials/first-pipeline.md). It
takes the snippet above and shows you the build, the run, the
output, and one common pitfall.

**You want the mental model.** Read
[the kernel fast path explainer](./explanation/kernel-vs-chain.md).
It explains why two paths exist, when each one runs, and what the
cost difference actually buys you.

**You want a JSON-driven setup.** Most production apps drive the
pipeline from `herald.json` so operators can change levels without
a rebuild. The JSON-configured tutorial covers that path. (Coming
in the next docs wave.)

## What you do not need to do

A short list of things people assume they need to set up and do
not.

- **No DI registration is required** to use the logger. The
  builder returns a `Logger` you can hand to a service or hold in
  a field. DI integration exists for ASP.NET Core hosts; it is
  optional.
- **No `appsettings.json` is required.** The JSON path is for
  operators who want runtime reconfiguration. Pure-code setup
  works for tests, CLIs, and small services.
- **No async setup is required.** The default pipeline runs
  synchronously on the calling thread. If you need async dispatch
  for sinks that block (network sinks, file sinks under heavy
  load), the `AsyncLogPolicy` decorator opts you in.

The principle here is CUPID's *Predictable* — the default
pipeline is the one you can reason about without reading the docs.
You add a decorator when you have a reason. You don't pay for
behavior you didn't ask for.
