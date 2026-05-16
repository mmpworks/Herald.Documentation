---
title: The kernel fast path — what it is and why it exists
slug: explanation/kernel-vs-chain
category: explanation
audience: advanced
since: 0.2.2
last-reviewed: 2026-05-16
related:
  - quickstart
  - tutorials/first-pipeline
related-records: []
---

# The kernel fast path — what it is and why it exists

Herald.OSS has two paths an event can take from your call site to a
sink. The fast one is the *kernel path*. The flexible one is the
*chain path*. They share a builder and a logger interface, but the
runtime cost shape is very different. This page explains what each
one is, when each one runs, and why both exist.

If you skim only one section, make it the diagram further down.
The picture is the whole point.

## Two paths, one call

You make the same call either way:

```csharp
logger.Info(LogCategory.App, "User {Id} logged in", userId);
```

The pipeline you built decides which path the event takes. A
minimal pipeline — a builder, a console sink, nothing else — uses
the kernel path. A pipeline with decorators (async dispatch,
batching, redaction, fan-out) uses the chain path.

The choice is made at `Build()` time, once, and frozen into the
delegate the logger holds. Your call site does not check anything
at runtime to pick a path. It just calls the logger.

![Kernel path vs chain path](../diagrams/herald-oss/kernel-vs-chain.svg)

## The kernel path

The kernel path is what runs when your pipeline has nothing
between the call site and the sinks. It does three things:

1. **Check the minimum level.** If the level is below the floor,
   return. Nothing else happens.
2. **Stack-allocate a `LogEventBuffer`.** The buffer is a
   value-type struct sized to hold up to eight properties without
   touching the heap. The properties go into the buffer, the
   timestamp goes in, the template stays as a string reference.
3. **Invoke the kernel delegate.** The delegate is one compiled
   method, captured at build time, that walks the sinks and hands
   each one the buffer.

Sinks that implement `IKernelSink` receive the buffer directly. No
boxing. No copy. Sinks that don't implement `IKernelSink` pay one
allocation at the boundary — the kernel builds a heap event for
them so they get the `ILogSink.Write(LogEvent)` shape they expect.

The whole accept path runs in about 27 nanoseconds for a four-property
event on .NET 10, with zero heap allocations when every sink in
the pipeline is an `IKernelSink`. That number includes the level
check, the buffer construction, the kernel delegate, and the write
into a console-shaped sink.

> **Quick picture.** Imagine a security checkpoint at an airport.
> Most travelers walk through the metal detector and continue —
> fast, no fuss. Only a few get pulled aside for the full bag
> search. The kernel path is the metal detector. The chain path
> is the bag-search lane. The metal detector is fast because it
> does one thing in one place; the bag-search lane is slower
> because it does several things in series. Both lanes exist for
> a reason; the airport puts most travelers through the fast one.

## The chain path

The chain path runs when your pipeline has decorators. You opted in
because you needed a behavior the kernel path does not provide —
async dispatch to a network sink, batching to amortise an HTTP
round trip, redaction of PII before any sink sees the event,
post-filtering for category-based routing.

Each decorator is a step in a chain. The strategy composer wires
them in a defined order at build time. The chain hands the event
from one step to the next, and the last step hands it to the
sinks.

The cost depends on which decorators you composed. Async dispatch
trades latency at the call site for back-pressure tolerance.
Batching trades per-event cost for amortised throughput. Redaction
trades a small amount of CPU for a security property the kernel
path can't enforce.

The chain path is not the slow path — it is the path that gives
you decorator behaviors the kernel can't do alone. If you need
those behaviors, the chain path is the right path. If you don't,
the kernel path is right.

## Why both paths exist

Two reasons, one principled, one practical.

**Practical.** Most apps that adopt Herald.OSS are not running
network sinks on the hot path. They write to console in
development, to a file in production, occasionally to a structured
sink that already has its own batching. For those apps, the chain
path's machinery is overhead they don't need. The kernel path
removes that overhead by removing the machinery.

**Principled.** Bundling async, batching, filtering, and rendering
into one monolithic logger would be a DRY violation dressed as
ergonomics. The decorator chain pattern lets each behavior live in
its own decorator, opted into independently. The kernel path is
the extreme case where the opt-in set is empty.

The CUPID property at work here is *Predictable*. The same
`logger.Info(...)` call has the same shape from the caller's point
of view whichever path runs. The path is a property of the
pipeline, not of the call. The call site reads identically in a
high-throughput service and in a debug script.

The second CUPID property is *Composable*. You compose the
pipeline you need by adding decorators. You do not subclass a
logger, you do not wrap it in your own facade, you do not edit a
config file with twenty optional sections. You add the decorator,
or you don't. The kernel path is what you get when you compose
nothing.

## Choosing a path for your pipeline

You almost never choose the path directly. You choose the
behaviors you need, and the path follows.

- **Console sink, file sink, in-process structured sink, no async.**
  Kernel path. No work needed.
- **Network sink (Loki, Splunk, Elastic, Seq).** Add the
  `AsyncLogPolicy` decorator. You are now on the chain path,
  because async dispatch is one of the decorators.
- **PII redaction required.** Add the redaction decorator. Chain
  path.
- **High-throughput service, batching matters.** Add
  `BatchingPolicy`. Chain path.
- **Mixed — kernel sinks plus one network sink that needs async.**
  The pipeline can use the chain path for the async-wrapped sink
  and the kernel path for everything else. The composer figures
  out the seam.

In short: build the pipeline that does what you need. The path is
the consequence, not the input.

## What this is not

A few things this page is not claiming, because the framing matters.

- This is not a "two products" story. Herald.OSS ships one
  logger, one builder, one event shape. The kernel path and the
  chain path are two routes through the same pipeline machinery.
- This is not a feature gate. Both paths ship in the same NuGet,
  in the same edition. You do not pay more for the kernel path.
- This is not a "go fast at the cost of correctness" mode. The
  kernel path runs the same level check, builds the same event
  shape, and writes to the same sinks as the chain path. It just
  does so without machinery you didn't ask for.

If you want to see the kernel path running on your machine, the
[first-pipeline tutorial](../tutorials/first-pipeline.md) builds a
pipeline with no decorators. Every event in that tutorial takes
the kernel path.
