---
title: Async-sink cross-tenant PII — security posture
slug: explanation/security/async-sink-cross-tenant-pii-posture
category: explanation
subcategory: security
audience: advanced
since: 0.10.2-planned
last-reviewed: 2026-05-27
status: posture-published-fix-pending-greenlight
related:
  - explanation/kernel-vs-chain
  - explanation/design-decisions/compact-path-default-axes-only
  - explanation/design-decisions/lever-a-async-default
related-records:
  - data/herald-oss/security-postures/async-sink-cross-tenant-pii.json
mirrors:
  - Herald.OSS (FastPathAsyncSink, shipped)
  - Modules/Core (byte-identical mirror)
---

# Async-sink cross-tenant PII — security posture

This page describes a latent issue in `FastPathAsyncSink` — the
async-sink wrapper that ships in Herald.OSS and is mirrored
byte-for-byte in the commercial Core build — and the layered defense
we are landing against it. The fix is queued; the posture is set.

The shape of this document is honest defense-in-depth. We do not
claim a runtime check can detect every cross-tenant leak. We make the
safe thing the default, we force the unsafe thing to be flagged at
compile time, and we keep one runtime backstop for the subset a
backstop can actually catch. Where the defense ends, we say so.

## 1. The threat

`FastPathAsyncSink` accepts a log event on the producer thread,
enqueues it on a bounded channel, and returns. A background consumer
task drains the channel and forwards each event to the inner sink.
The producer and consumer run on different threads. They almost
always run under different ambient context.

Herald supports lazy property capture. A consumer writes:

```csharp
logger.Info(
    LogCategory.App,
    "User action — actor={Actor}",
    LogProperty.Lazy(() => CurrentTenant.ActorName));
```

`LogProperty.Lazy(...)` records the delegate, not the value. When the
property is serialized — on the consumer thread, inside the drain —
the delegate runs and reads `CurrentTenant.ActorName`. On the producer
thread that read returns tenant A's actor. On the consumer thread it
returns whatever the consumer thread's ambient state happens to hold:
tenant B's actor, an empty value, or, in the worst case, the actor of
whichever request most recently touched that thread.

The same shape repeats for any closure that reads from `AsyncLocal<T>`,
`HttpContext.Current`, `[ThreadStatic]` state, an `ILogScopeProvider`,
or a mutable reference whose contents change between enqueue and
drain. The bug is not in the closure. The bug is in deferring the
read past the boundary where the ambient context is valid.

> Quick picture. Imagine a coat-check at a theater. You hand the
> attendant a ticket and expect your coat back. Now imagine the
> attendant rewrote the ticket from memory at the moment you came to
> pick up. Most of the time the ticket would still be yours. Some of
> the time it would belong to whoever stood at the counter last.
> Lazy capture across an async boundary is the attendant rewriting
> the ticket. Eager capture is writing the ticket down at the moment
> you hand over the coat.

The issue is latent in shipped code — `FastPathAsyncSink` is present
from 0.4.0 onward in the OSS package, and byte-identical in the Core
build that wraps it. We have no evidence of exploitation. The fix
prevents exploitation rather than detects it.

## 2. The layered defense

Five layers. Each layer closes part of the problem. We name what
each one closes and what it does not.

### L1 — Default-eager capture

`LogProperty(...)` captures eagerly. The value reads on the producer
thread, while ambient context is still valid. `LogProperty.Lazy(...)`
is the explicit opt-in that defers the read.

What it closes: every property a consumer writes through the default
path. The producer-thread read happens before enqueue, so the value
the consumer reads on the drain is the value already captured.

What it does not close: explicit `LogProperty.Lazy(...)` calls,
closures embedded in scope values, and any path that builds the
`LogEvent` directly on the producer thread but defers some captured
field's resolution.

### L2 — Factory finalization scan

`LogEventFactory.Create` and `DeferredLogEventFactory.Create` run a
finalization scan on every event they emit. The scan walks the
property list and either resolves any lazy closure on the spot (the
producer thread is still the right place to resolve) or, for
properties marked `PiiSensitive`, forces resolution and converts the
result to a string. Either way, no closure leaves the factory.

What it closes: events that travel through either factory, which is
every event built through the public surface — `logger.Info(...)`,
`logger.Log(LogEvent)`, and every other entry point that runs a
factory.

What it does not close: direct construction of a `LogEvent` that
skips the factory. That path is the documented residual in
section 7.

### L3 — Drain-entry assertion (defense-in-depth backstop)

`ConsumeAsync` runs an assertion at entry, before the first event is
pulled off the channel: the drain task is not running under any
named scope from the producer side. The assertion catches the shapes
of the leak that a runtime check *can* detect — the drain task
inheriting an `AsyncLocal` value, the drain task running inside an
`HttpContext`, the drain task seeing a `[ThreadStatic]` field set by
the producer's request.

**This layer is honest defense-in-depth. We do not overclaim it.**
The assertion catches the *shapes* of the mistake, not the
*liveness* of any object a closure may have captured. A closure that
captured a reference to a mutable tenant-context object, where the
object's fields are mutated after enqueue, is invisible to the
assertion. The check sees a closure with no AsyncLocal usage and
lets it through. The liveness problem is closed by L1 and L4 at the
producer side, not by L3 at the consumer side.

The right way to read this layer: L1 and L4 are the guarantee. The
factory scan in L2 enforces them. L3 catches a category of mistake
that survived the producer-side enforcement *and* the analyzer in
section 3 — the rare case where a consumer assembled a closure
through reflection, or constructed an event directly without the
factory, or otherwise bypassed every earlier layer. The assertion
fires loud when it sees one. It is a backstop, not the floor.

The L3 assertion sits at `ConsumeAsync` entry, which is a stable
entry point regardless of the channel-payload shape that rides
above it. The new
[Lever A async default](../design-decisions/lever-a-async-default.md)
changes the channel payload from a heap `LogEvent` to a value-typed
`AsyncEnvelope`, but it preserves the per-connection-drain topology
this posture relies on: each connection owns its own drain thread,
each drain runs the assertion at its own start, the multi-tenant
isolation closes the same way it did under the legacy payload. The
trust boundary L3 establishes composes cleanly across the
async-handoff redesign.

### L4 — `PiiSensitive` force-eager-to-string

Any property marked `PiiSensitive` (via attribute or builder call) is
resolved and serialized to a `string` on the producer thread before
enqueue. The consumer drains a `string`, not a closure, not a
reference to a tenant-scoped object. There is nothing for the drain
to evaluate.

What it closes: the cross-tenant leak vector for any data the
producer has marked as sensitive, including the transitive case
where a deferred `ToString()` on the drain would have re-entered
tenant scope. The string is computed on the producer thread; the
drain handles bytes.

What it does not close: data the producer did *not* mark sensitive.
That is the design intent — `PiiSensitive` is the explicit signal
that this field deserves the stricter handling.

### L5 — Fail-loud diagnostic instead of silent swallow

The pre-fix `ConsumeAsync` wrapped each inner-sink call in
`try { ... } catch { }`. That swallowed exceptions silently — the
producer never learned the drain rejected the event, and a drain
that threw on every event would simply lose the entire log stream
without a trace.

The fix replaces the swallow with a fail-loud diagnostic path. The
exception is routed to the configured failure sink (Herald's
diagnostic channel) and, if no failure sink is configured, the
event is re-attempted on the synchronous fallback the producer
configured at build time. The async sink never silently drops an
event whose drain threw.

What it closes: the "the drain ate every event and nobody noticed"
operational failure mode, and the more concerning case where the
exception itself encoded the cross-tenant slip and the swallow
hid the evidence.

What it does not close: the rare case where the failure sink itself
is misconfigured. That is documented in operational guidance.

## 3. The compile-time enforcement

The runtime layers are necessary but not sufficient. The strongest
position is to flag the unsafe shape before the code ever runs. The
analyzer that ships with Herald.OSS picks up six new rules for that.

The new rules extend the existing `HERALD0xx` analyzer family
(today: HERALD001–007, HERALD0410–0411) and ship additively in the
existing `MMP.Herald.OSS.Generators` assembly. No new analyzer
project, no new package.

| ID         | Severity | Detects                                                                                   |
|------------|----------|-------------------------------------------------------------------------------------------|
| HERALD008  | Warning  | A `LogProperty.Lazy(...)` closure captures an `AsyncLocal<T>` value.                      |
| HERALD009  | Warning  | A `LogProperty.Lazy(...)` closure captures `HttpContext.Current` or a request-scoped API. |
| HERALD010  | Warning  | A `LogProperty.Lazy(...)` closure reads a `[ThreadStatic]` field.                         |
| HERALD011  | Warning  | A `LogProperty.Lazy(...)` closure captures a mutable reference (non-`readonly` field).    |
| HERALD012  | Warning  | A `LogProperty.Lazy(...)` closure resolves through `ILogScopeProvider`.                   |
| HERALD013  | Info     | A `LogProperty.Lazy(...)` closure could be a local-eager capture (suggested rewrite).     |

Existing infrastructure handles the escalation: a consumer who sets
`<HeraldStrictMode>true</HeraldStrictMode>` in their csproj promotes
every Herald warning to an error (this is the existing HRLD0002
behavior — no new code). For a regulated build, strict mode is the
right default.

### The auditable suppression

When a consumer has reviewed a `LogProperty.Lazy(...)` site and
determined the closure is safe (for example, the captured value is
a request-scoped immutable copy that was already snapshotted), they
suppress the warning by attribute:

```csharp
[HeraldDrainSafe(Reason = "Captured immutable snapshot at request start; reviewed 2026-05-27 by alice@example.com.")]
public void LogActivity(...) { ... }
```

The `Reason` parameter is required — the analyzer rejects a
suppression without one. The build emits a count of `HeraldDrainSafe`
suppressions and writes them to the build output:

```
[Herald] HeraldDrainSafe: 14 reviewed exceptions with recorded reasons.
```

The count is the artifact. A clean build that reports
"0 warnings, 14 HeraldDrainSafe suppressions reviewed" is a stronger
posture than a clean build that reports "0 warnings" without
context. The audit trail is in the reasons, not in the silence.

### What the analyzer does not detect

The analyzer reads code shape. It does not measure object liveness.
Three specific cases stay out of reach:

- **Indirect ambient access.** A closure that calls a helper method
  that internally reads `AsyncLocal<T>` does not present an
  AsyncLocal token to the analyzer. The shape is invisible.
- **Reflection-assembled closures.** A `DynamicMethod` or
  `Expression.Compile()` closure built at runtime carries no
  syntactic shape for the analyzer to read.
- **Cross-assembly without the marker.** A closure that lives in a
  consumer's assembly and crosses into a Herald API without the
  `[HeraldDrainSafe]` attribute being applied cannot be detected by
  the analyzer in the Herald-OSS-side compilation unit.

These cases are caught by the runtime layers when they can be caught
(L1 + L4 close the producer-side, L3 catches the detectable subset
of drain-side surprises) and are named in the residual in
section 7.

## 4. The trust boundary

Four categories. A reader should be able to answer "where does this
defense fail?" in one read.

### Closed by construction — L1 + L4 + the factory scan

- Every property emitted through `LogProperty(...)` default path:
  eager capture on the producer thread.
- Every property marked `PiiSensitive`: resolved and string-ified
  on the producer thread.
- Every event passed through `LogEventFactory.Create` or
  `DeferredLogEventFactory.Create`: finalization scan resolves
  remaining lazies on the producer thread, stamps the frozen
  `LogEvent.TenantId` field, refuses to emit an event carrying a
  live closure.

A consumer who uses the documented entry points and does not call
`LogProperty.Lazy(...)` reaches this category by default.

### Closed by the analyzer — HERALD008–HERALD013

- Every detectable unsafe shape inside `LogProperty.Lazy(...)`:
  AsyncLocal capture, HttpContext capture, ThreadStatic read,
  mutable-reference capture, scope-provider resolution, and the
  local-eager suggestion.

A consumer who builds with `<HeraldStrictMode>true</>` reaches this
category as a hard build error. A consumer who keeps strict mode
off sees warnings; a code-review process is the enforcement.

### Documented contract residual

- Direct construction of a `LogEvent` that bypasses both factories
  and is then passed to a chain-path `Log(LogEvent)` entry.
- Closures assembled through reflection (`DynamicMethod`,
  `Expression.Compile()`).
- Closures whose ambient access is wrapped behind a helper method
  the analyzer cannot read into.

These are documented in section 7. The contract is: callers who
take these paths take responsibility for the producer-thread
resolution of every captured value, or accept the L3 backstop's
detection limit.

### Interaction with the compact-path contract

The L4 `PiiSensitive` force-eager mechanism interacts cleanly with
the [compact-path default-axes-only contract](../design-decisions/compact-path-default-axes-only.md).
A property marked `PiiSensitive` is resolved and string-ified on the
producer thread before the property ever reaches a compact slot.
PII never rides the compact path. The trust boundary in this posture
and the trust boundary in the compact-path contract both close *by
construction* — the two arguments line up, and a consumer reading
either page should leave with the same mental model: Herald's hot
path is narrow on purpose, and the narrow shape is what makes the
security guarantee and the performance guarantee compatible.

### Explicitly out of scope — source modification

Bad actors who modify the Herald.OSS source — for example, removing
the L2 factory scan, removing the L3 assertion, or relaxing the
`HeraldDrainSafe` reason requirement — are out of scope for this
defense. No library can protect against modification of its own
source. Operationally, that risk is closed by the consumer's build
provenance, package signing, and dependency-pinning practice.

## 5. Threats considered

The threat model went through a hostile-expert review pass against
twelve claims. The table summarizes the status of each. Detail per
claim, including the mechanism and the test that covers it, lives in
the structured record at `data/herald-oss/security-postures/async-sink-cross-tenant-pii.json`.

| Claim | Status                | Mechanism                                                                                                                     |
|-------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------|
| A     | Closed                | Direct AsyncLocal capture in `LogProperty.Lazy(...)` — L1 default-eager + HERALD008 analyzer warning                          |
| B     | Closed                | HttpContext capture in lazy closure — L1 + HERALD009                                                                          |
| C     | Closed                | ThreadStatic field read in lazy closure — L1 + HERALD010                                                                      |
| D     | Closed                | Mutable-reference capture (closure observes post-enqueue mutation) — L1 + HERALD011 + L4 force-eager-to-string for PII fields |
| E     | Closed                | `ILogScopeProvider` resolution in lazy closure — L1 + HERALD012                                                               |
| F     | Closed                | Local-variable that could have been captured eagerly — HERALD013 (Info, suggestion)                                           |
| G     | Closed                | Transitive `ToString()` on the drain re-entering tenant scope — L4 force-eager-to-string at producer (Richard's red-team find) |
| H     | Closed                | Silent exception swallow hiding the slip — L5 fail-loud diagnostic                                                            |
| I     | Closed (defense-in-depth) | Drain task inheriting AsyncLocal from the construction site — L3 assertion at drain entry (caught when the shape is present) |
| J     | Closed (documented residual) | Direct `LogEvent` construction bypassing factories — chain-path contract documented in section 7                          |
| K     | Closed (documented residual) | Reflection-assembled closures invisible to the analyzer — caught by L3 when the shape resolves, otherwise documented      |
| L     | Out of scope          | Source modification of Herald.OSS itself — no library defense applies                                                         |

The pattern: nine of the twelve are closed by L1/L2/L4 plus the
analyzer (the producer-side guarantee). One (G) is closed by a
purpose-built layer that emerged from the red-team pass. One (I) is
the honest defense-in-depth backstop the L3 assertion provides for
the detectable subset. Two (J, K) are residual contracts shared by
every logging framework — they are documented, not hidden.

## 6. Test evidence

Twenty tests cover the layers. Echo owns the test plan; the shape
of the coverage is summarized here so a reader of the posture knows
what is and is not measured.

Ten regression tests (RT-01 through RT-10) sit against the bug. The
first seven reproduce the original cross-tenant slip across each of
the unsafe shapes the analyzer detects — they fail on shipped code
and pass once the fix lands. The last three (RT-08, RT-09, RT-10)
are new tests added during the security pass: one covers the
transitive `ToString()` vector that L4 closes, one covers the
fail-loud diagnostic path that L5 establishes, and one covers the
factory finalization scan in the deferred-factory case.

Ten analyzer tests (ANA-001 through ANA-010) cover HERALD008
through HERALD013, plus three coverage tests for `HeraldDrainSafe`:
that suppression without a reason fails, that suppression with a
reason silences the warning, and that the build output reports the
suppression count.

A passing build of Herald.OSS produces a clean RT run and a clean
ANA run. A consumer who introduces a new `LogProperty.Lazy(...)`
site that captures `AsyncLocal<T>` produces a HERALD008 warning,
which strict-mode consumers treat as an error.

## 7. The honest residual

Three paths remain where a determined caller can still construct a
cross-tenant slip:

**Direct `LogEvent` construction without the factory.** The
chain-path `Log(LogEvent)` entry accepts a pre-built `LogEvent`. A
caller who builds the event manually, embeds a closure in a property
without running the property through `LogProperty(...)`, and passes
the result to the chain-path entry has bypassed the factory and the
factory's finalization scan. The contract for this path is: callers
who construct directly take responsibility for producer-thread
resolution. The path exists because some advanced consumers
construct events in batch and need the chain-path entry to remain
open; we did not remove it.

**Reflection-assembled closures.** A consumer who builds a closure
through `Expression.Compile()` or `DynamicMethod` and passes it into
`LogProperty.Lazy(...)` does not present a syntactic shape the
analyzer can read. The L3 assertion catches the shapes that resolve
to detectable ambient access. Closures that read through a
runtime-generated helper are outside the assertion's reach.

**Arbitrary mutable objects in scope values.** A consumer who
attaches a mutable object to a logging scope and then mutates the
object between enqueue and drain has constructed the same liveness
problem the lazy closure does, by a different mechanism. The fix
discourages this pattern by marking the relevant `ILogScope`
contract as snapshot-on-attach, but the contract is contract — not
enforcement.

This is the same residual every logging framework carries.
Serilog's documentation names the same shapes; NLog's does as well;
the .NET BCL `ILogger` documentation calls out the lazy-state
contract directly. Naming the residual is not negligence — it is
the honest position.

## 8. What ships, when

The posture is published with the fix queued. The implementation
sequence:

1. Steve greenlights the change.
2. Glenn lands the five-layer fix and the analyzer rules in
   Herald.OSS, with the mirrored change in Modules/Core.
3. Echo lands the twenty tests.
4. The release version bumps to 0.10.2 and ships the CHANGELOG entry
   that points back to this posture.

Until the greenlight, the shipped code carries the latent issue and
this posture carries the honest description of it. The structured
record under `data/herald-oss/security-postures/` is the queryable
form of the same content; future renders (a security-postures index
page on the documentation site, a status badge on the OSS README)
read from there.

## 9. Read next

- The structured record: `data/herald-oss/security-postures/async-sink-cross-tenant-pii.json`
- The kernel-vs-chain explanation: `prose/herald-oss/explanation/kernel-vs-chain.md`
- The diagnostic-codes reference in Herald.OSS: `docs/diagnostics/HRLD-codes.md` (HERALD008–HERALD013 land alongside the existing family)
