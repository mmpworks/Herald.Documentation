---
title: Lever A is the default async handoff — the path we landed and the sketchbook of paths we did not
slug: explanation/design-decisions/lever-a-async-default
category: explanation
subcategory: design-decisions
audience: advanced
since: 0.10.2-planned
last-reviewed: 2026-05-27
status: decided-doc-pending-greenlight
related:
  - explanation/kernel-vs-chain
  - explanation/design-decisions/compact-path-default-axes-only
  - explanation/security/async-sink-cross-tenant-pii-posture
related-records:
  - data/herald-oss/design-decisions/lever-a-async-default.json
mirrors:
  - Herald.OSS (FastPathAsyncSink, AsyncEnvelope)
  - Modules/Core (byte-identical mirror)
---

# Lever A is the default async handoff — the path we landed and the sketchbook of paths we did not

Herald.OSS 0.10.2 ships a new default for the async sink. The shape is
called Lever A. The producer thread fills a value-typed envelope on its
own stack, copies it into a channel, and returns. The drain reads the
envelope out and either reconstitutes a small buffer on its own stack
(when the inner sink is kernel-eligible) or builds a heap `LogEvent`
at the boundary (when the inner sink is legacy).

The number that matters: at the cloud-native multi-tenant regime where
cores are oversubscribed four-to-ten times by container packing, Lever
A is strictly better on every axis we measured. Throughput doubles.
Allocation per event falls from 296 bytes to 0.3. Maximum pause drops
by 24.58 milliseconds.

The team explored twelve other shapes before landing here. This page
records the decision, the contract that ships with it, and a short
tour of the sketchbook — the paths we considered and the reasons each
one did not become the default. The full engineering analysis lives
in the [companion catalog](#read-next); the prose here is the version
intended for the wider OSS audience.

## 1. The decision

Lever A is the default `FastPathAsyncSink` async handoff as of
Herald.OSS 0.10.2. The alternatives in this document — thirteen
shapes in all — were explored as due diligence before the team
committed.

The shape, in one breath: the producer constructs an `AsyncEnvelope`
value type on its stack. The envelope carries header scalars and an
inline-array slot buffer. The producer copies the envelope into a
`Channel<AsyncEnvelope>` slot and returns. No heap allocation on the
producer side. The drain reads the envelope back out and routes it
either to a kernel-eligible inner sink (zero allocation, full path)
or to a legacy inner sink (one allocation on the consumer thread,
backward compatible).

The alternative we shipped before this — a heap `LogEvent`
materialized on the producer thread and carried on
`Channel<LogEvent>` — stays in the code as a fallback for the legacy
inner-sink case. It is no longer the default for kernel-eligible
inner sinks.

> 💡 **Quick picture.** An architect's sketchbook holds the buildings
> that did not get built. The one you walk into is the one that got
> selected, but the sketchbook records the alternatives — the
> facade with the wrong load on the south wall, the floor plan with
> the corridor that became a bottleneck, the elevation that worked
> on paper but lost the morning light. The sketches are not waste.
> They are the record of due diligence — proof that the building you
> see was chosen against real alternatives, not by default. This page
> is the sketchbook. The default that ships is Lever A. The other
> twelve sketches are here so a reader can see what the choice cost
> and what the choice ruled out.

## 2. The contract

The contract that ships with Lever A, in plain words:

> `FastPathAsyncSink` accepts a log event on the producer thread,
> places it on a per-connection channel without allocating on the
> heap, and returns. A per-connection drain reads events off the
> channel and forwards them to the inner sink. Each connection
> owns its channel and its drain — no shared work, no cross-tenant
> interference. When the inner sink is kernel-eligible, the whole
> pipeline runs at zero allocations per event in steady state.

What the contract covers:

- `FastPathAsyncSink.Log(LogEventBuffer)` — the public entry point
  on the producer thread
- `Channel<AsyncEnvelope>` — the per-connection channel, value-type
  payload, no heap object per event
- `ConsumeAsync` — the per-connection drain that reads envelopes
  and routes them to the inner sink
- The kernel-eligible inner-sink path — zero allocation in steady
  state
- The legacy inner-sink path — one allocation on the consumer
  thread per drained event, on the cold side of the channel

What the contract does not cover:

- The 100 KHz/connection design ceiling is a target, not a
  representative current-customer rate. Most production workloads
  today are well below that. We optimize for the headroom.
- Workloads whose service-level objective requires a maximum pause
  tighter than two to three milliseconds in the paced regime. The
  inline path carries a small per-event-stable cost on quiet
  reps; operators with tight pause budgets opt out via the future
  M-5 seam (see [section 6](#6-the-extension-path)).
- Events whose property count routinely exceeds the eight-slot
  inline buffer. Overflow events fall back to an array allocation
  and lose part of the inline win. The team has not measured the
  overflow rate on production-shaped workloads at scale; the
  twenty-four-hour soak is the surface where that number lands.

## 3. The numbers

Two regimes were measured. The numbers below are reproducible from
the test rig in `Modules/Core/soak-tests/Herald.MultiSourceLoadTest/`
with the `--corrected` flag.

### Oversubscribed regime — 96 connections on 24 cores, flat out

The regime where cores are packed four times denser than the worker
count. This is the cloud-native default deployment shape, not an
edge case. Container schedulers regularly place eight to sixteen
microservices on a four-core node; each microservice has its own
logging pipeline; the result is four-to-ten times core
oversubscription as the baseline.

| Path | Throughput | Bytes per event | Maximum pause |
|---|---|---|---|
| Heap (today's default) | 39.3 million events/s | 296 | 30.4 ms |
| Inline (Lever A) | 78.7 million events/s | 0.3 | 5.8 ms |

The inline path doubles throughput, drops allocation per event by
roughly three orders of magnitude, and cuts maximum pause by almost
twenty-five milliseconds. There is no axis on which the heap path
wins in this regime.

### Paced regime — 24 connections, 100 KHz per connection, three reps

The regime where each producer is rate-limited to 100,000 events
per second. The pacing cap means total throughput is locked to
roughly 2.4 million events per second on both paths — the question
is what happens to allocation rate, garbage-collection pressure,
and tail pause.

| Metric | Heap (mean of 3) | Inline (mean of 3) | Delta |
|---|---|---|---|
| Throughput | 2,399,599 events/s | 2,399,798 events/s | pacing-locked |
| Bytes per event | 342.8 | 51.2 | 6.7× lower |
| Gen-0 collections per 15 s | ~1,194 | ~210 | 5.7× lower |
| Gen-1 collections per 15 s | ~114 | ~6 | 19× lower |
| Maximum pause (mean) | 21.81 ms | 9.59 ms | 12.22 ms lower |

The maximum-pause line carries a story. On quiet reps one and two,
the inline path was about 1.5 milliseconds *slower* on max pause —
a small per-event-stable cost that lands when the GC has no tail
event to grapple with. On rep three, the heap path took a single
61-millisecond tail pause from a gen-2 collection; the inline path
stayed under 22 milliseconds during the same rep. The heap path's
maximum-pause distribution is wider than the inline path's, and
the wide tail is what the mean reflects.

The honest reading of the paced numbers: the inline path is
slightly worse on quiet reps and substantially better when the GC
takes a hard moment. The mean comes out twelve milliseconds in
inline's favor, but the right way to interpret the result is that
the inline path's maximum-pause distribution is narrower, not
that the per-event-stable cost has vanished. Operators whose
service-level objective is tighter than two to three milliseconds
of paced-regime pause should opt out through the future M-5 seam.

### What N=3 does not prove

The paced-regime numbers come from three reps at 15 seconds each.
That is enough to characterize the directional shape of the
distribution. It is not enough to claim a statistical confidence
interval on the tail. A 30-rep run is the right way to characterize
the tail. The 24-hour soak — queued as joint work between Max and
Jared — is the right surface for production-shaped tail behaviors
the synthetic harness understates. Both runs are planned. Neither
is required to land the default change, because the oversubscribed
regime is decisive on its own.

## 4. The sketchbook — twelve paths we did not take

Each entry below names the shape, the evidence grade behind the
verdict, and the reason the path did not become the default. The
[companion catalog](#read-next) carries the full rationale per
entry; this page summarizes.

The evidence grades use a five-level scale: **measured** (we ran
the code), **projected from direct microbenchmark** (we measured the
component primitive and did the arithmetic), **projected from
analogous measurement** (we measured a related shape and reasoned
the analogy), **designed-only** (design analysis, no measurement),
and **first-principles estimate** (computed from published
constants).

| # | Shape | Evidence | Why not the default |
|---|---|---|---|
| 1 | SPSC Disruptor-proper ring per connection | Projected from analogous measurement | The Disruptor literature's famous 10× win is a JVM-and-Unsafe story; in .NET it is closer to 1.5–3× over `Channel<T>` because the JIT emits conservative memory fences the JVM can opt out of. A substantial code surface for a small win. |
| 2 | Off-heap unmanaged byte ring | Designed-only | The producer pays per-event byte encoding (200–500 ns) to save the channel-side allocation. Wrong trade in-process — you lose throughput to save allocation rate. |
| 3 | Per-thread batched handoff | Designed-only | Reintroduces the cross-tenant fairness problem the per-connection-drain topology exists to prevent. A slow tenant's batch holds up a fast tenant's batch in the same lane. |
| 4 | Pre-render to bytes on the producer | Designed-only | Same shape as #2 from a different angle. Requires the sink interface to accept bytes, not events, which forces a re-architecture of every sink in the ecosystem for a tail-case win. |
| 5 / M-2 | Kernel-inner-direct-to-sink bypass (runtime and compile-time variants) | Designed-only | Removes the async handoff entirely when the inner sink claims kernel eligibility. The handoff is the latency firewall — without it, a sink with a 50 ms first-call pause blocks every producer thread. The compile-time variant proves the sink type, not the latency profile of the sink's `Log` body. Operator footgun. |
| 6 | Producer-side fixed-arena allocator with epoch reset | Designed-only | The cross-thread free coordination costs more than the allocation it saves. Arena allocators work for request-scoped allocation; they do not work when the consumer is async and the producer doesn't know when reset is safe. |
| 7 | Native AOT-specific path | First-principles estimate | The JIT optimizations that matter for the async handoff are present in AOT mode today. No measurable AOT-specific win to bet on. |
| 8 / O-1 | Ref-struct channel hybrids | First-principles estimate | Possible only if you redefine "channel" to break the async-decoupling property. Generic `Channel<T>` cannot carry `ref struct` without the `allows ref struct` constraint, which is a research feature in .NET 10. |
| M-1 | Vyukov MPSC linked-list queue | Projected from analogous measurement | Trades the per-enqueue sequence write for a CAS. Net win is workload-dependent and may invert under high contention. Orthogonal to Lever A — could combine with it in a future revision. |
| M-3-A | Pooled mutable `LogEvent` (SemVer-major break) | Designed-only | Breaks the public-API value-equality contract. The pool must be lock-free MPSC, and pooled instances tenure into gen-2 quickly, where they hold references to short-lived strings — the unfavourable side of the same generational-distribution shift that Lever A's inline path lands on the favourable side of. |
| M-3-B | Pooled mutable carrier, public `LogEvent` materialized at sink boundary | Designed-only | Preserves the public API. Producer-side wins comparable to Lever A. Consumer pays one allocation per drained event on the cold path. Same gen-2 caveat as M-3-A for the carrier. A credible alternative; the maintenance cost of pool discipline tipped the decision toward Lever A's value-type shape. |
| M-4 | SPSC fan-in via single drainer thread | Designed-only | Concentrates throughput at one drainer thread. The ceiling is roughly one core's event-processing capacity; cannot reach the 78 million events per second the oversubscribed-regime Lever A measurement showed. Inverts the per-connection-drain topology's load distribution. |

Lever A is entry #13 (entry **A** in the catalog table). It is the
only measured entry. The other twelve are designed-only,
projected, or estimated. The team did not pre-measure every
designed-only entry as a precondition for shipping — that path
leads to forever-pending research. The catalog states each
evidence grade honestly so a reader can judge which entries
deserve follow-up measurement.

## 5. The honest residual

Three things this decision does not solve.

**Paced-regime per-event-stable cost.** On quiet reps in the
100 KHz paced regime, the inline path carries roughly 1.5
milliseconds more maximum pause than the heap path. This is a
real per-event-stable cost, reproducible across reps when the GC
has no tail event to dominate the measurement. Operators whose
service-level objective is tighter than two to three milliseconds
of paced-regime pause cannot tolerate the default. They need an
opt-out.

**Overflow events.** The inline `AsyncEnvelope` carries an
eight-slot buffer. Events with more than eight properties overflow
to a heap-allocated array and lose part of the inline win. The
synthetic harness uses four-property events; production workloads
range from eight to fifteen properties with mixed scalar, nested
object, and string-of-arbitrary-length content. The exact rate at
which production events overflow the eight-slot buffer has not
been measured. The 24-hour soak is the surface where that number
lands. If it turns out a substantial fraction of production events
overflow, raising the inline slot count is a contained tune.

**Statistical confidence on the tail distribution.** Three reps at
15 seconds each is enough to show the inline path's maximum-pause
distribution is narrower than the heap path's. It is not enough to
claim a confidence interval on the tail. A 30-rep run and a
24-hour soak are the right ways to land the tail claim with the
rigor an SRE evaluating the default will want. Both are queued.

These residuals are documented so a future reader — and a future
contributor — knows the team has thought about them. They are not
hidden behind smooth prose.

## 6. The extension path

The contingency is **M-5** — the `IAsyncHandoff` interface seam.

The shape: extract the async handoff into a public interface; ship
the default `ChannelBasedAsyncHandoff` (Lever A's shape); allow
operators to register an alternative implementation
(`SpscDisruptorAsyncHandoff`, `BatchedAsyncHandoff`, or any other
shape a future workload reveals as the right fit).

The cost: roughly three to five nanoseconds per event of
devirtualization overhead, because the JIT can no longer inline
across the seam unless guarded devirtualization fires (which it
does when a single implementation is registered per pipeline). At
2.4 million events per second the overhead is about 7 to 12
milliseconds per second of CPU — about 2% of one core.

The reason M-5 is deferred, not shipped today: the seam costs
every operator the small interface tax in exchange for a
flexibility most operators will never use. The right time to add
the seam is when an operator demonstrates a workload where opting
out matters. The 24-hour soak and the early adopter feedback
window are exactly where that demonstration will happen. Until
then, the interface tax is a real cost paid by everyone for a
flexibility nobody is using.

**The contingency contract:** if the 24-hour soak surfaces a
workload where Lever A's paced-regime cost is intolerable AND the
affected customer cannot be served by tuning channel capacity or
the per-connection-drain shape, the team commits to landing the
M-5 seam as a follow-on without forcing the operator to wait for
a major-version cycle. The default ships now; the safety valve
ships when the need arrives.

This is the same shape every responsible default carries. We pick
the shape that wins for the common case. We document the path out
for the case the default doesn't fit. We do not pretend the
common-case shape is universal.

## 7. The trust boundary

Four categories. A reader of this page should be able to answer
"where does this design hold and where does it stop?" in one read.

### True by construction

- `AsyncEnvelope` is a value type. It has no heap presence. There
  is no `Return()` discipline to enforce, no pool to manage, no
  tenuring story to monitor.
- Each connection owns its channel and its drain. There is no
  shared mutable state between connections. Cross-tenant
  interference at the channel layer is structurally impossible.
- The kernel-eligible inner-sink path runs the drain entirely on
  the consumer thread without allocating on the producer thread.
  The producer-side allocation count is zero by construction, not
  by enforcement.

### Documented contract

- Operators whose service-level objective is tighter than the
  inline path's quiet-rep per-event-stable cost (about 1.5 ms on
  the harness, likely different in production) opt out through
  the M-5 seam when it ships.
- Events whose property count exceeds the eight-slot inline
  buffer overflow to a heap-allocated array and pay a partial
  inline win. The contract is documented; the tune (raising the
  slot count) is contained.

### Out of scope

- Workloads at the 100 KHz/connection design ceiling are a target,
  not a representative current-customer rate. The optimization
  analysis is forward-looking. A reviewer who asks "show me the
  customer producing that rate today" hears "we are optimizing
  for the headroom, not for present demand."
- Bad-actor source modification of Herald.OSS itself — for
  example, removing the per-connection-drain topology — is out
  of scope. No library defense applies; the consumer's build
  provenance and package signing carry that risk.

### Interaction with adjacent contracts

The Lever A default does not exist in isolation. It composes
cleanly with two other shipped contracts:

- [The compact-path default-axes-only contract](compact-path-default-axes-only.md)
  defines the data shape that rides inside `AsyncEnvelope`'s inline
  slot buffer. The compact struct's 16-byte size and default-axes
  invariant are exactly what makes the inline envelope's slot
  buffer fit in a value type without overflow on common-case
  events. The two designs were authored as one.
- [The async-sink cross-tenant PII posture](../security/async-sink-cross-tenant-pii-posture.md)
  defines the L3 drain-entry assertion that fires on detectable
  ambient-context shapes. The assertion sits at the drain's
  `ConsumeAsync` entry, which is a stable entry point regardless
  of which channel-payload shape rides above it. Lever A's
  per-connection-drain topology preserves the assertion's
  contract — each drain is its own thread, each drain runs the
  assertion at its own start, the multi-tenant isolation the
  posture relies on is structurally intact.

## 8. The community door is open

Herald.OSS is open source. This page is the team's reasoning
today, not the team's verdict for all time. The catalog enumerates
thirteen approaches we considered, with honest evidence grades.
The community will know of approaches we did not consider.

**Pushback on the constraints.** We held four constraints fixed:
multi-connection mandatory, 100 KHz/connection design ceiling,
per-connection-drain topology, public-API discipline. If you have
a reason to relax any of them — a workload shape we did not
anticipate, a deployment model where multi-connection is wrong,
an operator profile we missed — we want the conversation. Open an
issue, name the constraint, name the workload.

**Measurements of the designed-only entries.** Twelve of the
thirteen entries in the catalog are designed-only or projected.
Anyone who can stand up a credible .NET SPSC Disruptor (entry #1),
a Vyukov MPSC queue (entry M-1), or a pooled-carrier prototype
(entry M-3-B) against the corrected harness and produce numbers —
we will incorporate the result. The catalog entry moves up the
evidence-grade column and credits the contributor.

**New shapes we missed.** This catalog has thirteen entries. If
you see an approach the team did not enumerate, submit it with
the same shape — evidence grade, one-line verdict, tradeoff
section — and we land it in the catalog. The catalog is a living
record of the design space, not a frozen claim of completeness.

**Customer workload data.** The 100 KHz/connection design ceiling
is honest about being a target, not a representative current rate.
If your deployment is at or above that rate today, we want the
data — both for catalog validation and for the M-5
contingency-trigger discussion. The team will use the data, name
the source, and credit the contributor.

If the catalog itself is wrong somewhere — if a verdict is
overstated, an evidence grade is misclassified, an alternative is
mislabeled — the same invitation applies. Open the PR. Show the
work. We evaluate.

The default ships now. The catalog is the record of how we got
here. The door is open for the catalog to be wrong.

## 9. What ships, when

The decision is recorded. The implementation sequence:

1. Steve greenlights the doc.
2. Glenn lands the Lever A implementation, the XML doc on the new
   `AsyncEnvelope` shape, and the CHANGELOG entry. The
   per-connection-drain topology is the existing shape; Lever A
   changes the channel payload from `LogEvent` to `AsyncEnvelope`
   and adds the kernel-eligible inner-sink path that returns
   zero allocations.
3. The release version bumps to 0.10.2 and ships the CHANGELOG
   entry that points back to this page and to the catalog.
4. The 24-hour soak runs as queued joint work between Max and
   Jared. The soak's findings update this page's residual section
   and trigger the M-5 seam discussion if needed.
5. Rick announces the catalog and the publication to the OSS
   community across the standard outreach channels, after Steve
   approves the announcement copy.

The default ships in 0.10.2. The catalog ships alongside it. The
M-5 seam is queued as the contingency the team commits to if the
soak or the early adopter feedback surfaces the need.

## 10. Read next

- The structured record: `data/herald-oss/design-decisions/lever-a-async-default.json`
- The engineering catalog (Jared's source-of-truth analysis):
  `docs/_wip/lever-a-paced-remeasure-2026-05-27/async-handoff-design-space-catalog.md`
  in the Herald.OSS repo
- The paced-regime re-measure report:
  `docs/_wip/lever-a-paced-remeasure-2026-05-27/paced-regime-remeasure-report.md`
- The compact-path contract: `prose/herald-oss/explanation/design-decisions/compact-path-default-axes-only.md`
  — the data shape that rides inside the inline envelope
- The async-sink PII posture: `prose/herald-oss/explanation/security/async-sink-cross-tenant-pii-posture.md`
  — the L3 assertion that composes with the per-connection-drain topology
- The kernel-vs-chain explanation: `prose/herald-oss/explanation/kernel-vs-chain.md`
  — why the hot path exists and why "narrow" is what makes it fast
