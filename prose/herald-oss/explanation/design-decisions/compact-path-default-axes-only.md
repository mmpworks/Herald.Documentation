---
title: The compact path is default-axes-only — a contract, not a limitation
slug: explanation/design-decisions/compact-path-default-axes-only
category: explanation
subcategory: design-decisions
audience: advanced
since: 0.10.2-planned
last-reviewed: 2026-05-27
status: decided-doc-pending-greenlight
related:
  - explanation/kernel-vs-chain
  - explanation/security/async-sink-cross-tenant-pii-posture
  - explanation/design-decisions/lever-a-async-default
related-records:
  - data/herald-oss/design-decisions/compact-path-default-axes-only.json
mirrors:
  - Herald.OSS (LogPropertyCompact, LogEventBuffer)
---

# The compact path is default-axes-only — a contract, not a limitation

Herald.OSS has two shapes a log property can take. The compact one,
`LogPropertyCompact`, is a 16-byte struct. The full one, `LogProperty`,
carries three optional axes — `CaptureMode`, `Format`, and `Visibility` —
that the chain-path decorators read.

This page documents the contract we are setting between them. The
compact path accepts properties whose three axes are at their
defaults. Properties that need non-default axes take the full
`LogProperty` path. The compact-path APIs do not accept a non-default
axis today, and a new analyzer rule — `HERALD014` — flags any attempt
to send one through.

The shape of this document is plain. We name the decision, the
contract, and the cost of the alternative we rejected. We name the
extension path for the case the contract excludes. Where the door
stays open for the community, we say so.

## 1. The decision

The compact path is default-axes-only **by construction**.

`LogPropertyCompact` exposes one constructor — `(string name, object?
value)` — and one factory — `From<T>(string name, T value)`. Neither
accepts a `CaptureMode`, a `Format`, or a `Visibility` parameter.
There is no public path that delivers a non-default-axis property
into a compact slot.

`LogPropertyCompact.ToLogProperty()` produces a `LogProperty` whose
three optional fields are at their defaults. The call signature drops
three nullable parameters, which is lossy *in shape*. The inputs
reaching the compact path are guaranteed to have those parameters at
their defaults, which is not lossy *in data*. Today, canonical
equivalence between the two shapes holds because the API surface
makes it hold.

> 💡 **Quick picture.** A postcard and an envelope carry the same kind
> of message, but they're built for different jobs. A postcard is
> open, fast, and small — perfect for a short note. An envelope is
> wider, takes a stamp, and carries the things you can't put on a
> postcard: a confidential letter, a folded check, anything that
> needs more than the postcard's surface allows. You don't slip a
> confidential letter under the postcard's address line. You reach
> for the envelope. The compact path is the postcard. The full
> `LogProperty` path is the envelope. The contract is that
> confidential letters — properties with non-default axes — take the
> envelope. The postcard can't carry them, and the rule says so out
> loud.

## 2. The contract

The contract, in plain words:

> The compact path is for properties whose only axes are the defaults.
> Properties with non-default axes take the full `LogProperty` path.
> This is a contract, not a limitation.

What the contract covers:

- `LogPropertyCompact(string, object?)` — the public constructor today
- `LogPropertyCompact.From<T>(string, T)` — the factory today
- `LogEventBuffer.ToLogEvent()` compact branch — emits the buffered
  compacts as `LogProperty` instances with default axes

What the contract excludes — these take the full `LogProperty` path:

- Properties marked `PiiSensitive` (force-eager to the full path
  before they reach a compact slot)
- Properties with non-default `CaptureMode` (for example, the
  forensic-`Silent` capture a downstream processor might want)
- Properties with a custom `Format`
- Properties with non-default `Visibility`

A consumer reading the XML doc on `LogPropertyCompact` sees the same
contract. The compiler enforces the constructor signatures. The
analyzer in section 4 catches the rare case where a consumer builds a
non-default `LogProperty` and tries to hand it to a compact-path API
by mistake.

## 3. Why this is the right shape

The compact path is the hot path. It is narrow because narrow is
fast. The question we asked is whether widening the compact struct —
adding three nullable axis fields so it could carry the full
`LogProperty` semantics losslessly — was worth the cost.

The cost is roughly 4% on the synchronous accept path at the
eight-property EPICS arity. That number wants context. On Jared's
bench rig, the noise band for those measurements is around 8
nanoseconds on 45-nanosecond numbers. The delta the widening would
add sits at about 3 nanoseconds — inside the noise. So the cost is
real on the struct-shape side (every event now carries three more
fields, every read pays the extra load) and unmeasurable on the
perf side (the regression vanishes into bench noise).

Paying real structural complexity for a perf cost you cannot
measure is the wrong trade. Especially on the hot path, where the
whole point of the narrow shape is that the cache line stays small,
the load stays predictable, and the events that don't need decorators
fly through.

The full `LogProperty` path is the right home for non-default-axis
properties. It pays the cost of the axes because its decorators read
them. The compact path was built for the events that don't need any
of that, and it is right to keep it for them.

This is CUPID's *Predictable* property in practice. The compact
path's behavior is the same the first time as the thousandth time
because the inputs that can reach it are the same kind every time.
Widening the struct would have introduced an axis-dependent branch
where today there is none, and the path would have lost the property
that makes it predictable.

## 4. The analyzer — `HERALD014`

The contract is enforced at three points.

**The API surface.** `LogPropertyCompact` accepts no axis parameters,
which closes the most common path by construction. There is no
constructor signature that takes a non-default `CaptureMode`.

**The XML doc.** `LogPropertyCompact` and `LogEventBuffer.ToLogEvent`
carry remarks naming the contract. A consumer reading IntelliSense
sees the rule before they call the API.

**The analyzer.** `HERALD014` catches the rare case where a consumer
builds a `LogProperty` with non-default axes — through one of the
full-path constructors — and then tries to pass it into a
compact-path API. The rule fires at build time.

| ID         | Severity | Detects                                                                                                                                                                |
|------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HERALD014  | Warning  | A `LogProperty` instance whose `CaptureMode`, `Format`, or `Visibility` is non-default is passed to a compact-path API (`LogPropertyCompact` factory or compact-slot). |

The diagnostic message names the contract directly: the compact path
is default-axes-only; route non-default-axis properties through the
full `LogProperty` path.

Consumers who want hard enforcement set
`<HeraldStrictMode>true</HeraldStrictMode>` in their csproj. That
escalates `HERALD014` (and every other Herald warning) to an error
through the existing HRLD0002 mechanism — no new escalation code.
For a regulated build, strict mode is the right default.

The analyzer reads code shape. It does not detect non-default axes
assigned through reflection or through a runtime-generated
`LogProperty` factory whose body the analyzer cannot read. Those
cases are the honest residual in section 6.

## 5. The trust boundary

A reader of this page should be able to answer "where does the
contract fail?" in one read. Four categories.

### True by construction

- Every property reachable through `LogPropertyCompact(string, object?)`
  carries default axes — the constructor accepts no axis parameters.
- Every property reachable through `LogPropertyCompact.From<T>(string, T)`
  carries default axes — the factory accepts no axis parameters.
- `LogPropertyCompact.ToLogProperty()` produces a `LogProperty` whose
  three optional fields are at their defaults, because the source
  struct has nowhere to carry non-default values.

### Enforced by the analyzer

- `HERALD014`: a non-default-axis `LogProperty` passed into a
  compact-path API is flagged at build time.
- `<HeraldStrictMode>true</>` escalates `HERALD014` to an error.

### Documented contract

- A consumer who builds a `LogProperty` with non-default axes uses
  the full `LogProperty` path. The compact-path APIs do not accept
  it; the analyzer flags the attempt at build time. The contract is
  the documented agreement.

### Out of scope

- Modification of Herald.OSS source to widen the compact struct or
  relax the analyzer rule. No library defense applies; the consumer's
  build provenance and package signing carry that risk.

## 6. The honest residual

The contract is total today because the API surface makes it total.
There is no public path that delivers a non-default-axis property
into a compact slot. `LogPropertyCompact.ToLogProperty()` is lossy in
shape but not in data, and that holds across every call site we
ship.

The honest part is what could change.

If a future API change exposed axes on the compact path — for
example, a new constructor overload — the contract would break the
moment that overload landed. The analyzer rule (`HERALD014`) lives
to catch the *consumer* side of that mistake; the *library* side is
a code-review discipline. A reviewer who sees an axis parameter
being added to `LogPropertyCompact` should reach for this page
before approving the change. The decision recorded here is part of
why the constructor signatures are what they are.

The analyzer also has its limits. It reads code shape. A consumer
who assigns non-default axes through reflection — `Activator`,
`MethodInfo.Invoke`, an `Expression.Compile`'d setter — does not
present a syntactic shape the analyzer can read. The runtime
behavior is the same as if the axes had been assigned directly: the
property has non-default axes, and the compact-path APIs still don't
accept it (the type system blocks the call). The reflection path
just doesn't get the build-time diagnostic.

These are the same residuals every Roslyn analyzer carries. Naming
them is the honest position.

## 7. The extension path

If a real shipping need arrives for non-default axes on compact —
the canonical case is a downstream processor wanting forensic-Silent
capture on a compact buffer — the extension is **Option 7a**: a
per-event sparse-optional axes-override sidecar on
`LogEventBuffer`, mirroring the existing `EventId` and `GenSource`
precedent.

The shape: most events allocate nothing in the sidecar. The rare
event that needs non-default axes pays a small per-event sparse
cost. The compact struct itself stays a 16-byte struct. The hot
path stays the hot path. The widening that Option 7a avoids is the
widening of `LogPropertyCompact`; the sidecar lives one level up,
on the buffer.

This is the same shape `EventId` and `GenSource` already use to
attach sparse-optional state without paying for it on every event.
Option 7a inherits that precedent's perf envelope, which is the
strongest evidence the shape works.

We are not building Option 7a today. The need has not surfaced. The
extension is documented now so a future reader — and a future
contributor — knows the team has thought about it. If the need
surfaces, the prior work is here.

## 8. Interactions with adjacent contracts

### The PII posture

This contract closes in the same direction as the
[async-sink cross-tenant PII posture](../security/async-sink-cross-tenant-pii-posture.md).
Properties marked `PiiSensitive` are force-eager — resolved and
serialized to a `string` on the producer thread before they ever
reach a compact slot. PII never rides the compact path. The trust
boundary in the PII posture and the contract here both close *by
construction*; the two arguments line up.

A consumer who reads both pages should leave with the same mental
model: Herald's hot path is narrow on purpose, and the narrow shape
is what makes the security and the performance guarantees compatible.
Widening the path to carry more semantics would have weakened both.

### The Lever A async-default contract

The compact path's 16-byte `LogPropertyCompact` and its default-axes
invariant are also exactly what makes the new async default —
[Lever A's value-typed `AsyncEnvelope`](lever-a-async-default.md) —
fit in a stack-allocated envelope without overflow on the common
case. `AsyncEnvelope` carries an `[InlineArray(8)]` slot buffer
that the compact struct rides inside; the slot count is sized for
the common-case event arity, and the compact struct's narrow shape
is what keeps the slot buffer small enough to live inside a value
type. The canonical-equivalence claim this page makes — compact and
full paths produce equivalent `LogEvent` outputs by construction —
continues to hold across the new async default. The envelope's
lossless compact slot is the construction that lets ingress-equals-
output continue to hold when an event takes the inline async route.
The two designs were authored as one piece of work.

## 9. The community door is open

Herald.OSS is open source. This page is the team's reasoning today,
not the team's verdict for all time.

If a contributor finds a way to make the compact path carry
non-default axes losslessly — without the accept-path cost we
measured, or with evidence that the cost we measured is genuinely
zero on real hardware and the bench noise hid a real signal — they
are welcome to open a PR. Show the measurement. Show the shape. We
evaluate.

If a contributor sees a third path the team missed — neither
"widen the struct" nor "sidecar on the buffer" but something the
team did not enumerate — same invitation. The honest position is
that we picked the best shape from the angles we considered.
Another angle is welcome.

The contract is what we ship today. The door is not closed.

## 10. What ships, when

The decision is recorded. The implementation sequence:

1. Steve greenlights the doc.
2. Glenn lands the XML doc, the `HERALD014` analyzer rule, the
   analyzer tests, and the CHANGELOG entry.
3. The release version bumps to 0.10.2 and ships the CHANGELOG
   entry that points back to this page.

Until the greenlight, the contract holds by API surface (the
constructor signatures already enforce it); the XML doc and the
analyzer make it explicit and enforced.

## 11. Read next

- The structured record: `data/herald-oss/design-decisions/compact-path-default-axes-only.json`
- The kernel-vs-chain explainer: `prose/herald-oss/explanation/kernel-vs-chain.md` — why the hot path exists, and why "narrow" is what makes it fast
- The PII posture: `prose/herald-oss/explanation/security/async-sink-cross-tenant-pii-posture.md` — the same "by construction" argument in the security domain
- The Lever A async-default contract: `prose/herald-oss/explanation/design-decisions/lever-a-async-default.md` — the new default async handoff that carries this compact path inside its inline envelope
- The diagnostic-codes reference in Herald.OSS: `docs/diagnostics/HRLD-codes.md` (HERALD014 lands alongside the existing family)
