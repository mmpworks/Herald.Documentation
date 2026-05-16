---
title: Herald.OSS Documentation Plan
slug: herald-oss-documentation-plan
status: draft
created: 2026-05-16
author: Heather (documentation agent)
related-repos:
  - Herald.OSS
  - Herald.Core
  - Herald.Documentation
last-reviewed: 2026-05-16
---

# Herald.OSS Documentation Plan

This plan describes the documentation we will build for Herald.OSS.
It does not contain the documentation itself. The deliverable is the
shape, the inventory, and the sequence. Authoring starts after the
user approves the shape.

The plan treats Herald.Documentation (this repo) as the source of
truth. Records and prose live here. The Herald.OSS repo, the public
doc site, and the marketing website all render from here. Edit once,
render many. That is the whole point of the layout the scaffold sets
up.

> Quick picture. Think of a print shop that prints the same poster in
> three sizes. The artwork file lives in one place. The shop has three
> presses, each set up for one size. When the artwork changes, you
> update the file, run all three presses, and the posters match. The
> moment you start editing each press's plates directly, the posters
> drift apart. Herald.Documentation is the artwork file. The
> renderers are the presses.

---

## 1. Audience and surface inventory

### Audiences

Four real readers, in rough order of size.

1. **New adopter.** Senior .NET engineer dropping into Herald for the
   first time. Wants a logger in their app inside ten minutes. Cares
   about cost: setup cost, runtime cost, AOT cost. Does not yet care
   about the kernel.

2. **Advanced user.** Already shipping with Herald. Tuning a pipeline,
   adding a custom sink, hot-reloading config, chasing a latency
   number. Cares about the contract of each piece and the operational
   surface. What fails, how it fails, how to recover.

3. **Plugin author.** Building a sink or processor against the
   Herald.OSS public surface. May ship to NuGet, may stay private.
   Cares about the sink contract, the capability metadata, the trust
   boundary, and how their plugin shows up in the registry.

4. **Contributor.** Working on Herald.OSS itself. Cares about how the
   code is laid out, how to run the benchmark suite, how the
   generators are wired, how the fork relates to Herald.Core.

A fifth reader. The evaluator who is choosing between Herald and
Serilog/NLog/ZLogger. Reads marketing copy on the website. That
audience is Dawn's surface, not ours. We feed her the benchmark
records and capability matrix; she shapes the pitch.

### The public surface

Walked from `E:/dev/Herald.OSS/src/` on 2026-05-16. Public types
exported by `MMP.Herald.OSS`:

- **Entry point.** `QuickLogBuilder` and its partials
  (`.With`, `.Mutations`, `.Diagnostics`, `.SerializerState`),
  `QuickLogResult`, `PipelineBuildResult`, `ValidationResult`. The
  `Quick/` namespace is where 95% of adopters land.
- **Logger contract.** `ILogger`, `ILogger<T>`, `TypedLogger`,
  `TypedLoggerFactory`, `LogCategory`, `LogEvent`, `LogEventBuffer`,
  `LogEventId`, `LogRenderContext`.
- **Pipeline.** `StructuredLogger`, `SwappableLogger`,
  `IPipelineStepHandler`, `ILogPipelineFactory`,
  `ILogPipelinePolicyFactory`, `EventCreationPreset`,
  `HeraldLogAttribute`, `LoggerComposition`,
  `IConfigurablePipelineDecorator`, `IComponentMetadata`,
  `IDescribable`, `LogMessage`, `SinkState`, `SinkHealthStatus`,
  `ISinkHealthReporter`, `CircuitBreakerOpenException`,
  `ICircuitBreakerRuntimeState`, `VendorInfo`, `PipelineStepNames`,
  the `Processors/` and `StepHandlers/` types.
- **Kernel.** `LogKernel`, `KernelCompiler`, `IKernelSink`,
  `GenSourceGatedSink`, `GenSourceGatedKernelSink`. (Most consumers
  never type these names; sink authors do.)
- **Sinks.** `HeraldSinkBase`, `INetworkSink`, `ILogSink`,
  `ILogSinkFactory`, `ILogSinkProvider`, `IConfigurableSinkProvider`,
  `ILogSinkRouterFactory`, `ISinkChainLevelIntrospection`,
  `ISinkWrapperFactory`, `LogSinkProviderRegistry`,
  `NoAutoRegisterAttribute`, `SinkWrapperRegistry`,
  `Routing/Loopback/`, `Routing/Providers/`.
- **Configuration.** `LogPipelinePolicy`, `AsyncLogPolicy`,
  `BatchingPolicy`, `DynamicLevelPolicy`, `FlightRecorderPolicy`,
  `FileSinkPolicy`, `PostFilteringPolicy`, `RetryPolicy`,
  `PipelineStrategy`, `ConfigDiff`, `ConfigDiffDetector`,
  `ConfigEnvInterpolator`, `ConfigurationFileWatcher`,
  `DefaultLoggingConfigurationMapper`, `HeraldJsonContext`,
  `KnownSink`, `LoggingHostAdapters`, `LoggingJsonSerializer`,
  `SinkChangeKind`, `ILoggingConfigurationMapper`, plus the
  `Configuration/Json/`, `Configuration/Runtime/`,
  `Configuration/Simple/`, `Configuration/Sinks/` subnamespaces.
- **Bootstrap.** `LoggingBootstrap`, `LoggingBootstrapResult`,
  `HotReloadableLoggingBootstrap`, `HotReloadOutcome`,
  `JsonConfiguredLoggingBootstrapFactory`, `OldResourceJanitor`,
  `LoggingRuntimeBootstrap`, `LoggingRuntimeBootstrapResult`.
- **Events / filtering / formatting / output / spans / time.** All
  named in `src/` subdirectories. These are reference material that
  most adopters never touch directly.
- **Diagnostics.** `HeraldRuntimeMessages` (new in 0.2.2. Runtime
  notice channel split from user sinks per the testbench finding).
- **Addons.** Every subdirectory under `src/Addons/` per `FORK_SCOPE.md`.
  Each addon is a documentation surface in its own right (Archive,
  BinarySerialization, Compliance, GameEnrichers, GamePerformance,
  Instrumentation, ManagementApi, MelAdapter, MetricExtraction,
  NetworkTransports, Observability, OtlpSinks, QualityChecks, Query,
  Reduction, Replay).
- **Edition badge.** `HeraldEdition`. Informational only in OSS,
  read by downstream commercial wrappers. Documented as a seam, not
  as enforcement.
- **Source generators.** `[HeraldLog]` attribute,
  `TypedArgsOverloadGenerator`, `HeraldLogCategoryAnalyzer`,
  `HeraldLogLevelAnalyzer`, `HeraldStrategyAnalyzer`,
  `SinkAutoRegistrationGenerator`. These ship as analyzers in the
  same NuGet. Adopters get them by referencing Herald.OSS.

The four call shapes on the accept path are part of the SDK surface
and need explicit reference coverage: typed-args, `params
ReadOnlySpan<LogProperty>`, interpolated handler, level-bound
interpolated.

### Surface observations worth flagging

- **`Quick/` is large.** 29 public types in one namespace. Adopters
  who skim the namespace will see noise; the docs need to draw a
  sharp line between "the 4 types you use" (`QuickLogBuilder`,
  `QuickLogResult`, `HeraldHost`, `HeraldTenant`) and "the 25 types
  you almost never type by name."
- **`HeraldEdition` is back.** 0.2.0 stripped it. 0.2.1 restored it
  as the seam a downstream wrapper reads. The docs need to frame
  this honestly. It is *informational* in OSS, *enforced* in
  Herald.Core. Glossing this creates the same confusion FORK_SCOPE
  tries to clear.
- **`GenSourceGatedSink` ships in OSS.** OSS does not stamp
  `GenSource` by default and does not wrap any sink with the gate by
  default. The docs treat the gate as an opt-in composition pattern
  for multi-tenant routing. Not as a Pro feature gate.
- **`HeraldRuntimeMessages` is new (2026-05-16).** The 0.2.2 release
  split runtime notices off the user pipeline. The docs need to
  cover the subscribe pattern so consumers who relied on the old
  in-pipeline announcement know how to migrate.

---

## 2. Diátaxis mapping

Four modes, four reader needs, four shapes of writing. Herald.OSS
gets a page list per quadrant. Pages are named, not yet written.

### Tutorials (learning-oriented)

A tutorial walks one specific reader through one specific success.
Two tutorials only. More dilutes the learning path.

- **`tutorials/first-pipeline.md`**. New adopter, blank repo to
  working logger in 10 minutes. Console sink, one info call, one
  warn call. No JSON config yet, no DI. Ends with the reader seeing
  their event print to console.
- **`tutorials/json-configured-pipeline.md`**. New adopter, second
  step. Same logger, now driven from `herald.json`. Hot-reload
  enabled. Reader changes a level, sees behavior change without
  restart.

That is the tutorial set. Everything beyond those two is a how-to.

### How-to guides (problem-oriented)

A how-to is a recipe for a known problem. Numbered when the order
matters; un-numbered when the steps are linear.

- **`howtos/add-a-file-sink.md`**. Wire a built-in file sink.
- **`howtos/add-a-custom-sink.md`**. Implement `HeraldSinkBase` and
  ship the sink as a NuGet that auto-registers via assembly load.
- **`howtos/add-a-zero-alloc-sink.md`**. Implement `IKernelSink`
  when latency matters. Adopted from the existing
  `kernel-sink-pattern.md` guide.
- **`howtos/configure-async-batching.md`**. `AsyncLogPolicy` +
  `BatchingPolicy`, when to use which, what fails when the buffer
  fills.
- **`howtos/configure-hot-reload.md`**. `HotReloadableLoggingBootstrap`,
  the kernel-swap rule, watching `appsettings.json`.
- **`howtos/configure-redaction.md`**. Fast-path redactor,
  per-property rules, what the redactor does and does not see.
- **`howtos/structure-multi-tenant-pipelines.md`**. One builder per
  tenant. When to share sinks, when to isolate. Where the
  `GenSource` gate fits in if you want defense-in-depth.
- **`howtos/wire-up-mel-bridge.md`**. `MelAdapter` for ASP.NET Core
  hosts. The shape of the bridge, what gets lost, what is preserved.
- **`howtos/publish-aot.md`**. Native AOT publish against
  Herald.OSS. Adopted from `aot-and-trimming.md`.
- **`howtos/migrate-from-serilog.md`**. Serilog → Herald.OSS,
  fragment-by-fragment.
- **`howtos/migrate-from-nlog.md`**. NLog → Herald.OSS.
- **`howtos/migrate-from-mel.md`**. Microsoft.Extensions.Logging →
  Herald.OSS via the bridge.
- **`howtos/run-the-benchmarks.md`**. Reproduce the published
  numbers locally. Adopted from `benchmarks/HOWTO.md`.
- **`howtos/troubleshoot-silent-events.md`**. The "I'm calling
  `Info()` but nothing is appearing" path. Common causes: level
  filter, sink disabled, pipeline name mismatch, kernel-orphan after
  hot reload.
- **`howtos/subscribe-to-runtime-notices.md`**. Subscribe to
  `HeraldRuntimeMessages.OnNotice`. Migration target for users
  affected by the 0.2.2 channel split.

### Reference (information-oriented)

Reference is dense, dry, and complete. Most of it comes from
structured records, rendered into markdown. Hand-written prose only
where the structure does not capture intent.

- **`reference/api/`**. Auto-generated from XML-doc. One page per
  public type, grouped by namespace. The renderer reads `data/herald-oss/methods/*.json`
  and writes here. We do not hand-write under `reference/api/`.
- **`reference/sinks/index.md`**. Capability matrix rendered from
  `data/herald-oss/sinks/*.json`. One row per built-in sink.
- **`reference/config/herald-json.md`**. Full `herald.json` schema
  reference, rendered from the canonical JSON Schema in
  `schemas/herald-oss/herald-json.schema.json`.
- **`reference/config/env-vars.md`**. Environment variables Herald
  reads. Rendered from `data/herald-oss/env-vars/*.json`.
- **`reference/levels.md`**. The level model. Verbose / Debug / Info /
  Warn / Error / Fatal, what the level filter does, how
  `SwitchableLevelFilter` differs from `LevelFilter`.
- **`reference/event-model.md`**. `LogEvent`, `LogEventBuffer`,
  `LogCategory`, `LogProperty`, `LogPropertyCompact`, the four
  property-buffer shapes (`LogPropertyBuffer4`, etc.). Reference
  for sink authors.
- **`reference/source-generators.md`**. `[HeraldLog]`, the analyzer
  diagnostics (HERALDxxx), what each emits.
- **`reference/addons/`**. One page per `src/Addons/` subdirectory,
  pulled from the Herald.Core namespace docs we'll harvest in §6.
- **`reference/glossary.md`**. Rendered from
  `data/herald-oss/glossary/*.json`.
- **`reference/error-codes.md`**. Exception types thrown by the
  public surface, with the precondition that triggers each.

### Explanation (understanding-oriented)

Explanation builds the mental models the reader needs to make
decisions. This quadrant is where the "design primer" voice lives.

- **`explanation/architecture.md`**. The three concentric layers.
  Lifted and extended from the existing
  `Herald.OSS/docs/guides/architecture.md`.
- **`explanation/kernel-vs-chain.md`**. What the kernel fast path
  is, when the chain path runs, the cost difference, why both exist.
- **`explanation/quick-vs-bootstrap.md`**. `QuickLogBuilder` vs
  `LoggingBootstrap`. When Quick is enough. When the reader should
  step up to the Bootstrap pipeline. Added per the Stripe comparison
  pattern in §8. Two surfaces that overlap deserve a page that names
  the choice, not a paragraph buried in a longer explainer.
- **`explanation/hot-reload-mental-model.md`**. `SwappableLogger`,
  the kernel swap, why the kernel-delegate update is load-bearing.
- **`explanation/multi-tenancy.md`**. Structural isolation. One
  pipeline per tenant. Where the `GenSource` gate fits.
- **`explanation/sinks-stay-dumb.md`**. `ILogger.Log` is one-way.
  Sinks have no back-reference. Why this matters for plugin trust
  and for keeping the contract small.
- **`explanation/source-gen-vs-runtime.md`**. What
  `TypedArgsOverloadGenerator` produces, why it produces it, what
  changes if the consumer ships AOT vs JIT.
- **`explanation/cupid-in-herald.md`**. How CUPID and DRY show up
  in Herald.OSS choices. Worked examples. Not a CUPID tutorial. A
  reading guide for the codebase.
- **`explanation/fork-relationship.md`**. Herald.OSS vs
  Herald.Core. Reframed from `FORK_SCOPE.md` for an outside reader
  who has no insider history of the fork.
- **`explanation/performance-model.md`**. Where the numbers come
  from. What the accept-path cost actually measures. What
  zero-allocation buys you and what it does not.
- **`explanation/security-model.md`**. What the pipeline defends
  and what it does not. Adopted from the existing
  `security-overview.md`.

---

## 3. Canonical-data inventory

Records under `data/herald-oss/`. Each category gets a JSON Schema
under `schemas/herald-oss/`. Records are JSON files keyed by a stable
slug.

### Categories

- **`data/herald-oss/methods/`**. One record per public method on a
  public type. Signature, parameters, return, exceptions, remarks,
  example, related-methods. Renderer produces `reference/api/`.
- **`data/herald-oss/types/`**. One record per public type. Kind
  (class/record/interface/enum/struct), namespace, summary, since,
  related-types, deprecation. Renderer joins to methods.
- **`data/herald-oss/sinks/`**. One record per built-in sink. Name,
  display-name, kind-key, status (community / pro / enterprise per
  upstream Herald.Core, all available at source in OSS), zero-alloc
  (yes/no. Does it implement `IKernelSink`), thread-safety,
  buffering, retry-behavior, config-keys, NuGet-id, examples.
  Renderer produces the capability matrix in `reference/sinks/index.md`
  and feeds Dawn's plugin catalog on the website.
- **`data/herald-oss/config-keys/`**. One record per
  `herald.json` key. Path, type, default, allowed-values,
  description, since, examples. Renderer produces
  `reference/config/herald-json.md`.
- **`data/herald-oss/env-vars/`**. One record per environment
  variable. Name, type, default, description, since, examples.
- **`data/herald-oss/levels/`**. Six records (one per level). Name,
  numeric-value, semantics, when-to-use.
- **`data/herald-oss/addons/`**. One record per `src/Addons/`
  subdirectory. Name, summary, types-it-exposes, upstream-edition,
  threading-contract, since.
- **`data/herald-oss/glossary/`**. One record per term. Term,
  definition, also-known-as, related-terms, first-introduced-in
  (page slug), since.
- **`data/herald-oss/exceptions/`**. One record per exception type.
  Type, namespace, when-thrown, recovery-suggestion, since.
- **`data/herald-oss/performance-claims/`**. One record per
  benchmark headline (e.g. "27 ns 4-property accept, net10"). Claim,
  scenario, harness, run-date, reproduce-command. Feeds the README
  table, the performance page, and Dawn's marketing surface.
- **`data/herald-oss/source-gen-diagnostics/`**. One record per
  HERALDxxx analyzer code. Code, category, severity, message,
  example, fix.
- **`data/herald-oss/capability-matrix/`**. One document describing
  what OSS / Pro / Enterprise each provide. This is the "what's in
  what edition" table. Notes that gating is informational in OSS.

### Schema sketches

Each is one JSON file under `schemas/herald-oss/`. Sketched here
because the user wants the categories named, not the schemas finalized.

```
schemas/herald-oss/
  type.schema.json          : Name, namespace, kind, summary (md),
                               since, deprecated, related-types
  method.schema.json        : Type-slug, name, signature, params,
                               returns, exceptions, remarks (md),
                               examples, since, related-methods
  sink.schema.json          : Slug, display-name, kind-key,
                               upstream-edition, capabilities[],
                               config-keys[], nuget-id, examples,
                               since
  config-key.schema.json    : Path, type, default, allowed-values,
                               description (md), examples, since
  env-var.schema.json       : Name, type, default, description (md),
                               examples, since
  level.schema.json         : Name, numeric-value, semantics (md),
                               when-to-use (md)
  addon.schema.json         : Slug, summary (md), types[],
                               upstream-edition, threading-contract,
                               since
  glossary.schema.json      : Term, definition (md), aliases[],
                               related-terms[], first-introduced-in,
                               since
  exception.schema.json     : Type, namespace, when-thrown (md),
                               recovery (md), since
  performance-claim.schema.json
                            : Slug, claim, scenario, harness,
                               run-date, reproduce, source-data
  source-gen-diagnostic.schema.json
                            : Code, category, severity, message,
                               example, fix (md)
  capability-matrix.schema.json
                            : Rows[], columns[] (oss/pro/enterprise),
                               cells[][] with markdown notes
```

All schemas allow markdown fragments in prose fields (`description`,
`remarks`, `summary`, `examples`). The renderer treats those as
markdown; everything else is structural.

> Quick picture. The schemas are like a kitchen's recipe cards.
> Each card has the same shape. Title, ingredients, steps, time.
> The cook can pull any card and know where to look for the
> information. The renderer is the printer that turns the cards
> into the menu, the cookbook, and the wall poster. Same cards,
> three audiences.

---

## 4. Prose inventory

Pages under `prose/herald-oss/`. Every page carries frontmatter so
the corpus is queryable (related-concepts, last-reviewed,
audience-tag). Frontmatter shape:

```yaml
---
title: ...
slug: ...
category: tutorial | howto | reference | explanation
audience: new-adopter | advanced | plugin-author | contributor
related: [other-slug, ...]
related-records: [data-path, ...]
last-reviewed: YYYY-MM-DD
since: 0.x.y
---
```

The full prose inventory is the page list in §2 (Diátaxis mapping).
Cross-cutting prose that doesn't fit a quadrant:

- **`prose/herald-oss/CHANGELOG-rendered.md`**. Generated from
  `data/herald-oss/changelog/*.json` (per-release record). The
  CHANGELOG that ships in the Herald.OSS repo is a render of this.
- **`prose/herald-oss/README-rendered.md`**. The Herald.OSS repo's
  root README is a render of structured records plus a short
  hand-written narrative section. The hand-written part lives here.
- **`prose/herald-oss/index.md`**. Landing page for the doc site.
  Picks the reader's path (new adopter / advanced / plugin author /
  contributor).

---

## 5. Diagram inventory

Six diagrams up front. Mermaid is the default; SVG when the visual
story needs it; no Excalidraw shipped to consumers.

| Page | Diagram | Level | Notes |
|---|---|---|---|
| `explanation/architecture.md` | three concentric layers (Quick / Pipeline / Kernel) | SVG | The lift target is the existing ASCII picture in `Herald.OSS/docs/guides/architecture.md`. Promote to SVG matching the herald-website style. Earns the cost because it's the page every new reader lands on. |
| `explanation/kernel-vs-chain.md` | kernel fast path vs chain path comparison | SVG | Two-panel comparison. Red panel = chain path (rich), blue panel = kernel path (fast). Matches the architecture-page SVG style on the herald-website. |
| `explanation/hot-reload-mental-model.md` | swap sequence (old pipeline + new pipeline + kernel delegate) | Mermaid sequence | Sequence diagram is enough. The swap is event-ordered. |
| `explanation/multi-tenancy.md` | two tenant pipelines, optional shared sink | Mermaid flowchart | Small and clear. |
| `explanation/source-gen-vs-runtime.md` | source-gen pipeline (Roslyn → emitted overloads) | Mermaid flowchart | Steps are linear; Mermaid handles it. |
| `tutorials/first-pipeline.md` | call shape (info call → buffer → console sink) | Mermaid sequence | One small picture as the tutorial's anchor. |

Cost rule: a diagram earns its space by saying something the prose
cannot. If a diagram would just restate the surrounding paragraph,
skip it. Two diagrams per page is the cap.

---

## 6. Old-fragment harvest plan

The user said there is "a lot of old architecture content in the main
Herald project and Modules/Core too." Walked those trees on
2026-05-16.

### Cross-reference rule

Herald.OSS was forked from Modules/Core at commit `98d23fd` and
squashed clean. Before lifting any fragment, check Modules/Core's git
history for the same file. Design rationale that exists in Core's
history was not carried into OSS's history, so we may need to harvest
the *reason* from Core even when the *file* is in OSS.

### Inventory of harvest candidates

Sources walked:
- `E:/dev/herald/docs/`
- `E:/dev/herald/Modules/Core/docs/`
- `E:/dev/herald/Herald/wiki/`

#### High-value lifts (clean adaptation expected)

| Source | What it documents | Target | Core-history check |
|---|---|---|---|
| `Modules/Core/docs/design-primer.md` | The "Kitchen" metaphor for the pipeline. Each station = one decorator. | `explanation/architecture.md` companion piece, or its own `explanation/why-it-thinks-like-this.md` | Author tone is unusual for the project (more literary). Check `git log -p` on Core to verify intent. Likely deliberate. Lift faithfully; do not flatten the voice. |
| `Modules/Core/docs/design-primer-condensed.md` | Condensed version of the primer. | Source for the short explainers on each page's "why" section. | Same check. |
| `Modules/Core/docs/kernel-fast-path-pattern.md` | The kernel fast-path discipline. What makes a sink kernel-eligible. | Merges into `explanation/kernel-vs-chain.md` and `howtos/add-a-zero-alloc-sink.md`. | Check Core history for the original design discussion. |
| `Modules/Core/docs/the-way-things-work.md` | End-to-end "what happens when you call `Info()`" narrative. | `explanation/architecture.md` (data-flow section). | Likely complete in Core; check for stripped Pro-only mechanics that should not lift. |
| `Modules/Core/docs/under-the-hood.md` | Lower-level mechanics commentary. | Source material for `explanation/performance-model.md`. | **Caution.** Likely contains IP-level mechanics. Read it carefully and surface only what is observable from the SDK; leave the rest behind per CLAUDE.md's IP-vs-SDK rule. |
| `Modules/Core/docs/the-loggers-speak.md` | Narrative tour of the logger interface. | `tutorials/first-pipeline.md`. Borrow the voice and structure for the tutorial intro. | Probably fine to lift. |
| `Modules/Core/docs/aot-readiness.md` | AOT and trimming notes from Core. | Cross-check against current `Herald.OSS/docs/guides/aot-and-trimming.md`; lift anything richer. | Check Core history for the AOT-readiness work that produced this. |
| `Modules/Core/docs/security.md` | Security overview. | Cross-check against `Herald.OSS/docs/guides/security-overview.md`; lift gaps. | Some content is Pro/Enterprise (provenance gate enforcement). Strip those before publishing. |
| `Modules/Core/docs/adding-sinks.md` | Sink-author walkthrough. | `howtos/add-a-custom-sink.md` and `howtos/add-a-zero-alloc-sink.md`. | Likely needs minor adjustment for OSS-only surface. |
| `Modules/Core/docs/principal-review.md` | Principal-reviewer takeaways on Herald.Core. | Source for `explanation/performance-model.md` framing and headline numbers. | **Caution.** Reviewers have no prior-iteration history per CLAUDE.md; lift the *current* claims, not the timeline of how they got there. |
| `Modules/Core/docs/allocation-reduction-design.md` | Allocation work rationale. | Source for `explanation/performance-model.md`. | **Caution.** This is IP-level rationale. Use as background; do not republish. |
| `Modules/Core/docs/wasm-filter-design.md` | WASM filter design document. | If shipping in OSS, becomes a how-to. Otherwise skip. | Verify whether WASM filter is in OSS. Probably not. Check `src/`. |
| `Modules/Core/docs/per-event-redaction-design.md` | Redaction design. | Background for `howtos/configure-redaction.md`. | Check for Pro-only redactor logic; strip it. |
| `Modules/Core/docs/log-event-security.md` | Event-level security discussion. | Source for `explanation/security-model.md`. | Check Core history for the threat-model framing. |
| `Modules/Core/docs/edition-strategy.md` | Edition machinery design. | Source for `explanation/fork-relationship.md`. | Lift the *current* split, not the iteration history. |
| `Modules/Core/docs/future-direction.md` | Forward-looking roadmap notes. | Do not publish as roadmap on OSS docs (speculation rule). Use as input to the open-questions list per release. | Skip for now. |

#### Wiki namespace docs. The API-reference backbone

`E:/dev/herald/Herald/wiki/Herald.Core/namespaces/` has 57 files,
one per public namespace, ingested 2026-05-09. These are the closest
existing match to per-namespace API reference. They feed
`reference/api/` indirectly. The renderer's primary source is
XML-doc, but these files are the human-curated "what's in this
namespace and why" intro page.

Plan: harvest the intro paragraphs of each namespace doc into the
namespace's `data/herald-oss/types/<namespace>/_intro.md` slot. The
type listings underneath get re-rendered from `data/herald-oss/types/`,
not lifted.

#### Main `docs/` chapters

`E:/dev/herald/docs/chapter-01-tutorial.md` through `chapter-15-event-creation-presets.md`
plus standalone chapters (8, 10, 11, 12, 13, 14, 15). Each chapter is
~5-15KB of narrative.

| Chapter | Best target |
|---|---|
| chapter-01-tutorial.md | `tutorials/first-pipeline.md` (heavily adapt; strip Pro references) |
| chapter-02-capabilities.md | `explanation/architecture.md` (capability sketches) |
| chapter-03-configuration.md | `howtos/*` (split per concern: hot-reload, async, redaction) |
| chapter-04-patterns.md | `explanation/cupid-in-herald.md` + scattered |
| chapter-05-extensions.md | `howtos/add-a-custom-sink.md` |
| chapter-06-internals.md | Source for `explanation/kernel-vs-chain.md`. **caution: IP**, observe SDK-only |
| chapter-07-cookbook.md | Scatter across `howtos/*` |
| chapter-08-quicklogbuilder.md | `reference/api/quicklogbuilder.md` (rendered from records) + `tutorials/first-pipeline.md` |
| chapter-10-pipeline-inspection.md | `howtos/troubleshoot-silent-events.md` |
| chapter-11-stripe-patterns.md | Skip. Stripe-pattern material is more about Herald-the-product than OSS-the-library |
| chapter-12-herald-sdk.md | `explanation/architecture.md` (SDK shape) |
| chapter-13-logger-configurations.md | `howtos/configure-*.md` family |
| chapter-14-building-a-sink-plugin.md | `howtos/add-a-custom-sink.md` |
| chapter-15-event-creation-presets.md | `reference/event-model.md` + `howtos/*` |

#### What to leave behind

- `docs/herald-server-ingest-strategies.md`. Server territory, not OSS.
- `docs/dashboard-design.md` / `dashboard-wiring.md`. Dashboard territory.
- `docs/competitor-comparison.md` / `competitive-analysis.md`. Marketing surface (Dawn).
- `docs/medium-part1-one-interface.md` etc.. Already-published blog material (Dawn).
- `docs/scientific-*.md`. Herald.Sci territory.
- `docs/game-ideation.md` / `godot-*.md`. Game-specific; revisit when we have a Herald.Game audience.
- `docs/HMAC-SHA256-HKDF-upgrade.md`. Compliance territory.
- `docs/playbook-proposal.md`. Internal planning.
- Anything under `docs/_wip/` and `docs/research/`. Work-in-progress, not authoritative.
- `Modules/Core/docs/2026-04-23/`, `2026-04-24/` snapshots. Historical.

### Harvest workflow per fragment

For each fragment:

1. Read the source. Note IP-level material (per CLAUDE.md's
   IP-vs-SDK line). That gets left behind.
2. Run `git log --follow` on the file from `E:/dev/herald/Modules/Core/`
   to find prior versions and stripped rationale. If Core's history
   has a richer earlier version, lift the richer prose.
3. Land the lift under the target page in `prose/herald-oss/`.
   Frontmatter records the source: `source: Modules/Core/docs/<file>`
   plus `source-rationale: <commit-sha>` when Core history was
   consulted.
4. Update any structured records the lift implies (e.g. a sink
   description gets normalized into the sink record).
5. Mark the source fragment as harvested in a tracking table that
   lives in this plan's appendix. Once every fragment is harvested,
   the tracker tells us what to retire from the source repos.

---

## 7. Rendering targets

What gets produced from the canonical source, where it lands, who
reads it.

| Target | Renderer | Output path | Consumer |
|---|---|---|---|
| Herald.OSS repo `README.md` | renderer pulls the headline table from `data/herald-oss/performance-claims/`, the "what's in v0.x" list from `data/herald-oss/changelog/`, the getting-started block from `prose/herald-oss/README-rendered.md` | rendered to `rendered/herald-oss/README.md`, copied into `E:/dev/Herald.OSS/README.md` as a build step | Anyone landing on the GitHub repo |
| Herald.OSS `CHANGELOG.md` | renderer reads `data/herald-oss/changelog/*.json` | rendered to `rendered/herald-oss/CHANGELOG.md`, copied into `E:/dev/Herald.OSS/CHANGELOG.md` | Adopters tracking releases |
| mkdocs site (proposed `docs.herald.dev`) | mkdocs reads `prose/herald-oss/` plus `rendered/herald-oss/site/` (where the structured-data renders land) | `rendered/herald-oss/site/` then deployed | All four audiences |
| API reference pages | renderer reads `data/herald-oss/methods/` + `data/herald-oss/types/`, joins, emits one markdown per type | `rendered/herald-oss/site/reference/api/` | Advanced users, plugin authors |
| Sink capability matrix | renderer reads `data/herald-oss/sinks/` | `rendered/herald-oss/site/reference/sinks/index.md` | All audiences |
| Config-key reference | renderer reads `schemas/herald-oss/herald-json.schema.json` plus `data/herald-oss/config-keys/` | `rendered/herald-oss/site/reference/config/herald-json.md` | Advanced users |
| Website plugin catalog | renderer reads `data/herald-oss/sinks/` plus `data/herald-sinks/*` and produces a TypeScript module Dawn imports | `rendered/herald-oss/website/plugin-catalog.ts` then handed to Dawn | herald-website readers |
| Website architecture-page records | renderer reads `data/herald-oss/performance-claims/` | TypeScript module Dawn imports | herald-website readers |

The mkdocs choice is provisional. Docusaurus and Hugo are both viable;
the user needs to choose. The renderer pipeline is tool-agnostic
because the canonical source is markdown + structured data.

---

## 8. Exemplar lessons applied

Three exemplars studied. Each lesson is a specific page or page-shape
choice in the Herald.OSS plan above.

### Stripe Docs. Task-oriented landing + sidecar code

Stripe's docs land you on "what do you want to do?" not "here are
all our APIs." Every page has working code on the right side that
matches the prose on the left. The reader copies, pastes, adapts.

Studied 2026-05-16: `docs.stripe.com/`, `/api`, `/api/charges/create`,
`/payments`, plus the full sitemap (~13K URLs). The second pass added
six concrete design choices the first pass missed.

Applied (first pass):
- **`prose/herald-oss/index.md`** opens with four reader-path
  buttons (new adopter / advanced / plugin author / contributor),
  not a topic tree.
- Every `howtos/*.md` page closes with a copy-pasteable example
  block. The example is one piece, not eight fragments the reader
  must assemble.
- `tutorials/first-pipeline.md` has a code-on-the-right layout
  pattern: the prose on the left explains, the code panel on the
  right grows step by step.

Applied (second pass, after the deeper Stripe study):

- **One page per operation.** Stripe gives every operation on a
  resource its own URL. `/api/accounts/create`,
  `/api/accounts/retrieve`, `/api/accounts/update`,
  `/api/accounts/list`, `/api/accounts/delete`, plus
  `/api/accounts/object` for the response shape. Apply: the renderer
  that reads `data/herald-oss/methods/` emits one markdown page per
  public method, not one mega-page per type. The type's `object`
  shape (its public properties) gets its own page, matching Stripe's
  convention. Every method ends up with a copy-pasteable URL.

- **`/quickstart` is a reserved slug.** Every Stripe product publishes
  its quickstart at the same predictable path. `/checkout/quickstart`,
  `/billing/quickstart`, `/connect/marketplace/quickstart`. Apply:
  `tutorials/first-pipeline.md` lives at `/quickstart/` on the docs
  site, with redirects from any reasonable guess (`/getting-started`,
  `/start`, `/intro`). A Herald reader who types *quickstart* in the
  URL bar reaches the ten-minute success path.

- **Comparison pages get their own URL.** When two Stripe surfaces
  overlap, Stripe ships a dedicated page for the choice. A real
  example: `/payments/checkout-sessions-and-payment-intents-comparison`.
  The page exists because the choice matters and burying it in a
  section header costs readers. Apply: when two Herald surfaces
  overlap, give the choice its own page. The three candidates we
  already know about: `explanation/quick-vs-bootstrap.md`
  (`QuickLogBuilder` vs `LoggingBootstrap`),
  `explanation/kernel-vs-chain.md` (already in the plan), and
  `explanation/sync-vs-async-policy.md`. The first one was missing
  from §2 and has been added.

- **Changelog entries are per-record, grouped by release codename.**
  Stripe's URL shape is `/changelog/acacia/2025-01-27/...`. Every
  change has its own page. Readers can browse by date or by codename
  (acacia, basil, clover, dahlia, …). Apply: `data/herald-oss/changelog/`
  holds one record per change, not one giant markdown file. The
  renderer groups by Herald.OSS release (`0.2.1`, `0.2.2`, …) and
  emits both a flat chronological feed and a per-release view. Each
  entry is linkable on its own URL.

- **The version is always on screen.** Every Stripe reference page
  carries the current API version in the right-rail and in the auth
  token banner. The reader never has to ask "which version is this?"
  Apply: every `reference/api/` page reads the Herald.OSS version
  (`0.2.2` today) from frontmatter and surfaces it as a corner badge.
  The `since:` field on each record tells the reader when a feature
  appeared. The page badge tells them which library version the page
  was written against. Two different questions, two different answers,
  both visible.

- **Right-rail code panel with a switcher (the "sidecar code"
  pattern).** Stripe's `/api/*` pages put curl, Node, Python, Ruby,
  Go, .NET, and PHP on a switchable panel that scrolls with the
  prose. Apply: Herald.OSS is C# only at the language level, so the
  language switcher doesn't carry over. But the panel shape works
  for *call-shape* switching. The reference page for `Info()` shows
  the four shapes (typed-args, span, interpolated handler,
  level-bound interpolated) on a switchable right-rail panel that
  scrolls with the prose. The reader picks the shape they prefer and
  sees it inline. The renderer reads
  `data/herald-oss/methods/*.json`'s `call-shapes[]` array and emits
  the panel.

The first pass said "every how-to ends with a copy-pasteable example
block." The second pass made the pattern more specific. Three
concrete examples from the Stripe study:

- `/checkout/quickstart` ends with a runnable Node block that reads
  `STRIPE_SECRET_KEY` inline, defines the Express route, and points
  at the success-redirect URL. One paste, one working app.
- `/billing/quickstart` ends with a Stripe CLI command
  (`stripe trigger payment_intent.succeeded`) so the reader can
  exercise the integration without putting through a real charge.
- `/api/charges/create` places the closing example beside the
  parameter table, not at the bottom of the page. The example grows
  as the reader works down the parameters.

Apply to Herald.OSS how-tos. The closing block is a complete,
runnable program. Not a fragment. Where a CLI command or a benchmark
invocation can sanity-check the result, include it.
`howtos/run-the-benchmarks.md` and `howtos/add-a-custom-sink.md`
land this discipline first.

### Rust Book. Progressive disclosure with a strong spine

Chapters build. Chapter 4 (ownership) assumes Chapter 3 (variables).
The book never makes the reader scroll back; it makes the reader
trust that the next thing they need is one chapter ahead.

Applied:
- **The two tutorials are sequenced.** `first-pipeline.md` is
  Chapter 1. `json-configured-pipeline.md` is Chapter 2. No skipping.
- **`explanation/*.md` is the spine.** A reader who reads
  `architecture.md` → `kernel-vs-chain.md` → `hot-reload-mental-model.md`
  in order learns Herald the way the Rust Book teaches Rust. Each
  page assumes the prior.
- **Diagrams are the chapter-image equivalent.** One diagram per
  spine page, no more, anchored to the concept being introduced.

### MDN Web Docs. Reference quality

MDN's reference pages have predictable shape: signature, parameters,
return, examples, exceptions, related, since. The reader does not
need to learn a new layout per page.

Applied:
- **`reference/api/` is rendered, not hand-written.** Records under
  `data/herald-oss/methods/` and `data/herald-oss/types/` carry the
  fields; the renderer produces the markdown. Every reference page
  has the same shape. No drift.
- **The renderer enforces the "since" field.** A method without a
  `since:` is a schema-validation error. The reader can always trust
  the "since when?" answer is present.
- **Examples are records, not body text.** Each method's
  `examples[]` is structured. Title, code, language, expected output.
  That means the same example can render to the API reference page
  *and* to the tutorial where it's introduced.

A fourth pattern worth naming, drawn from all three: **strong
information scent.** Every page tells you where you are
(breadcrumb / category badge), what category it is (tutorial /
how-to / reference / explanation), and what to read next. The
mkdocs site theme handles breadcrumb + category badge; the
"what to read next" lives in each page's frontmatter
(`related:` field) and renders into the page footer.

---

## 9. Phased execution order

A documentation surface ships in layers. The goal of phase 1 is a
**usable narrow surface**, not a comprehensive empty one.

### Phase 1. Skeleton + first reader path (week 1)

Goal: a new adopter can land on the doc site and walk
`first-pipeline.md` to success.

- Schemas for `type`, `method`, `sink`, `config-key`, `glossary`.
- Records: enough sinks (console, channel, audit) and methods
  (`QuickLogBuilder.Create`, `.WithConsoleSink`, `.BuildAndCommit`,
  `.Info`) to back the tutorial.
- Renderer: README assembler + one API-reference renderer (types
  only, no joins yet).
- Prose: `index.md`, `tutorials/first-pipeline.md`,
  `explanation/architecture.md` (lift + reshape from
  `Herald.OSS/docs/guides/architecture.md`).
- Diagram: the three-layer SVG.
- Rendered output: Herald.OSS `README.md`, the doc site's landing +
  tutorial + architecture page.

Nothing else. The site has gaps, and that's correct. The gaps point
the reader at the GitHub repo for now.

### Phase 2. Cover the how-to surface (weeks 2-3)

Goal: an advanced user can solve a real problem.

- Schemas: `addon`, `env-var`, `level`, `performance-claim`,
  `exception`, `source-gen-diagnostic`.
- Records: all built-in sinks, all `herald.json` keys, all six
  levels, the headline performance claims.
- Renderer: capability matrix, config-key reference, performance
  page.
- Prose: all 15 how-to pages from §2, sequenced.
- Diagrams: kernel-vs-chain SVG, hot-reload sequence Mermaid,
  multi-tenancy Mermaid.

### Phase 3. Reference completeness + explanation spine (weeks 4-5)

Goal: a plugin author can build a sink from the reference alone.

- Records: every public type + method. The XML-doc → record
  pipeline is the load-bearing piece here. See open questions.
- Renderer: full API reference, glossary, source-gen diagnostics.
- Prose: all `explanation/*.md` pages.
- Diagrams: source-gen flowchart Mermaid, tutorial sequence Mermaid.
- Old-fragment harvest from §6 (highest-value lifts first:
  design-primer, kernel-fast-path-pattern, the-way-things-work).

### Phase 4. Polish, search, and the website handoff (week 6)

- Search across the doc site (mkdocs has it built in; verify it
  surfaces structured-record content).
- Cross-link audit: every page has `related:` frontmatter that
  resolves.
- Last-reviewed date audit: every page newer than 90 days.
- Dawn handoff: the plugin catalog and architecture-page records
  are flowing into `herald-website` cleanly.

### Phase 5. Contributor + migration (week 7+)

- Contributor pages (`how-to-build`, `how-to-run-tests`,
  `how-to-run-benchmarks`, `repo-layout`).
- Migration guides (Serilog / NLog / MEL → Herald.OSS).
- Old-fragment retirement: source fragments harvested in §6 get
  marked deprecated in their original repos with a pointer here.

---

## 10. Open questions

Decisions the user needs to make before authoring begins. None of
these blocks the scaffold or the plan; they block specific phases.

1. **Doc site framework.** Mkdocs, Docusaurus, or Hugo. Default
   recommendation: mkdocs (Material theme). Stripe-quality search
   out of the box, low-friction markdown ingest, plays well with
   structured-data renders. Decision unblocks Phase 1 deployment.

2. **Doc site domain.** `docs.herald.dev`? `docs.mmpworks.com/herald`?
   Something else? Decision unblocks any absolute-URL renders and
   the website cross-linking.

3. **API reference source.** XML-doc → records is the cleanest path.
   The DocFX toolchain has the XML-doc parser; we can shell out to
   it during render. Alternative: write a small Roslyn-based
   extractor inside `scripts/`. Decision unblocks Phase 3.

4. **CLA for Herald.Documentation.** README says no CLA, deferred.
   Confirm. If we later want a CLA matching the other Herald repos,
   we follow the Herald.Sinks DCO pattern (per memory note
   `feedback_herald_sinks_dco`) rather than the
   `mmpworks/cla-signatures` CLA workflow.

5. **Website-bound records. Committed here or in herald-website?**
   The plugin catalog TypeScript module is generated. It can live in
   `rendered/herald-oss/website/` here (gitignored) and Dawn pulls
   on build, or it can be committed into `herald-website/` directly.
   Decision affects who runs the renderer when records change.

6. **Renderer language.** Node, Python, or .NET console. Default
   recommendation: Node. Fastest path to a working renderer given
   the markdown + JSON Schema ecosystem. Decision unblocks scripts/.

7. **Rendered output commit policy.** Do we commit
   `rendered/herald-oss/README.md` into the Herald.OSS repo, or
   only the source records, with CI doing the render at release?
   Default recommendation: commit the rendered README so a GitHub
   visitor with no docs site sees the current copy. Decision shapes
   the release workflow.

8. **Excalidraw use.** The scaffold leaves room for Excalidraw under
   `diagrams/`. The plan above ships zero Excalidraw to consumers.
   Confirm Excalidraw stays internal-only.

9. **Versioning strategy.** Herald.OSS is at 0.2.2. Docs version
   1-to-1 with the library? Versioned site with version switcher?
   Single-version "latest" until 1.0? Default recommendation:
   single-version "latest" until 1.0, then switch to versioned. The
   `since:` field on every record records when a feature appeared,
   which gives the reader version awareness without needing a
   version switcher pre-1.0.

10. **`HeraldEdition` framing.** The plan documents it as
    "informational in OSS, enforced in Herald.Core." Confirm the
    framing. This is the kind of architectural-disposition question
    that benefits from a Richard pass at authoring time, but the
    framing decision is the user's.

---

## Appendix A. Harvest tracker (initialized)

One row per source fragment. The tracker grows during Phase 3 as we
walk each fragment. Status values: `pending`, `lifted`, `partial`,
`skipped`, `retired-at-source`.

| Source | Target | Status | Notes |
|---|---|---|---|
| `Modules/Core/docs/design-primer.md` | `explanation/why-it-thinks-like-this.md` | pending | Lift the "Kitchen" framing; preserve voice. |
| `Modules/Core/docs/design-primer-condensed.md` | scattered | pending | Mine for one-paragraph explainers. |
| `Modules/Core/docs/kernel-fast-path-pattern.md` | `explanation/kernel-vs-chain.md` + `howtos/add-a-zero-alloc-sink.md` | pending | Check Core git history for design rationale. |
| `Modules/Core/docs/the-way-things-work.md` | `explanation/architecture.md` (data-flow) | pending | Strip Pro-only mechanics if any. |
| `Modules/Core/docs/under-the-hood.md` | `explanation/performance-model.md` | pending | **Caution: IP**. SDK-only lift. |
| `Modules/Core/docs/the-loggers-speak.md` | `tutorials/first-pipeline.md` (voice) | pending | |
| `Modules/Core/docs/aot-readiness.md` | merge into `howtos/publish-aot.md` | pending | |
| `Modules/Core/docs/security.md` | `explanation/security-model.md` | pending | Strip provenance-gate enforcement details. |
| `Modules/Core/docs/adding-sinks.md` | `howtos/add-a-custom-sink.md` | pending | |
| `Modules/Core/docs/principal-review.md` | `explanation/performance-model.md` | pending | Lift current claims, not the timeline. |
| `Modules/Core/docs/allocation-reduction-design.md` | background only | pending | **IP**. Do not republish. |
| `Modules/Core/docs/wasm-filter-design.md` | TBD | pending | Verify if WASM filter ships in OSS. |
| `Modules/Core/docs/per-event-redaction-design.md` | `howtos/configure-redaction.md` | pending | Strip Pro-only redactor logic. |
| `Modules/Core/docs/log-event-security.md` | `explanation/security-model.md` | pending | |
| `Modules/Core/docs/edition-strategy.md` | `explanation/fork-relationship.md` | pending | Lift current shape only. |
| `Herald/wiki/Herald.Core/namespaces/MMP-Herald-*.md` (57 files) | per-namespace `_intro.md` slots | pending | The intro paragraph of each is the harvest target. |
| `docs/chapter-01-tutorial.md` | `tutorials/first-pipeline.md` | pending | Strip Pro references. |
| `docs/chapter-02-capabilities.md` | `explanation/architecture.md` | pending | |
| `docs/chapter-03-configuration.md` | `howtos/configure-*.md` (split) | pending | |
| `docs/chapter-04-patterns.md` | `explanation/cupid-in-herald.md` + scattered | pending | |
| `docs/chapter-05-extensions.md` | `howtos/add-a-custom-sink.md` | pending | |
| `docs/chapter-06-internals.md` | `explanation/kernel-vs-chain.md` | pending | **Caution: IP**. Observe SDK-only. |
| `docs/chapter-07-cookbook.md` | scatter to `howtos/*` | pending | |
| `docs/chapter-08-quicklogbuilder.md` | `reference/api/quicklogbuilder.md` + tutorial | pending | |
| `docs/chapter-10-pipeline-inspection.md` | `howtos/troubleshoot-silent-events.md` | pending | |
| `docs/chapter-12-herald-sdk.md` | `explanation/architecture.md` | pending | |
| `docs/chapter-13-logger-configurations.md` | `howtos/configure-*.md` family | pending | |
| `docs/chapter-14-building-a-sink-plugin.md` | `howtos/add-a-custom-sink.md` | pending | |
| `docs/chapter-15-event-creation-presets.md` | `reference/event-model.md` + `howtos/*` | pending | |

This appendix becomes the working list for Phase 3.

---

## Closing note

The plan is intentionally long because every page named here is a
specific writing job with a specific source. Authoring is a series of
small lifts, not one large rewrite. The scaffold and the plan
together give the user something inspectable before any prose ships.

When authoring starts, each page comes through this plan's
inventory. The reader who picks up Herald.OSS docs cold reaches
success in the first ten minutes because we sequenced the spine
before we wrote it.
