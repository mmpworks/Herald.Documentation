---
title: Herald.Sinks Documentation Plan
slug: herald-sinks-documentation-plan
status: draft
created: 2026-05-16
author: Heather (documentation agent)
related-repos:
  - Herald.Sinks
  - Herald.OSS
  - Herald.Documentation
last-reviewed: 2026-05-16
---

# Herald.Sinks Documentation Plan

This plan describes the documentation we will build for Herald.Sinks.
It is the sibling of `documentation-guidance/herald-oss/herald-oss-documentation-plan.md`
and shares its model of the world. Records and prose live here; the
Herald.Sinks repo READMEs, the doc site, and the website's plugin
catalog all render from here.

The plan is intentionally shorter than the herald-oss plan. The
herald-oss plan does the heavy lifting on framework choices,
exemplar lessons, and harvest workflow. Herald.Sinks reuses every one
of those decisions. What changes is the inventory and the audience.

---

## 1. Lock-step with Herald.OSS

Herald.OSS and Herald.Sinks ship as one packaged release. A given
release of Herald is the OSS core plus the curated set of sinks the
release pulls in. Their documentation moves the same way. When we
publish a new OSS version, we publish a matching Sinks snapshot at
the same time, and the two doc surfaces cross-reference each other
freely.

The contract is simple. Per-product URL roots stand
(`/documentation/herald-oss/<slug>` and
`/documentation/herald-sinks/<slug>` per Richard's URL discipline),
but the prose is free to link across products with relative markdown
links. A Sinks page can write `[the kernel fast path](../../herald-oss/explanation/kernel-vs-chain.md)`
and the reader follows the link without thinking about which repo
authored the destination. An OSS page can write
`[picking a sink](../../herald-sinks/quickstart.md)` the same way.

That keeps each product's URL root predictable for SEO and
navigation, while keeping the prose honest about how the system
actually works — a Herald user reads across the seam because the
seam is a packaging detail, not a conceptual one.

> Quick picture. Think of a textbook and its problem set, published
> together. The textbook has chapters; the problem set has problems.
> They have their own page numbers, their own indexes, their own
> covers. But chapter 4 of the textbook says "see problems 4.7 and
> 4.8," and problem 4.7 says "see the proof in chapter 4." Neither
> can stand alone, and neither pretends to. Herald.OSS is the
> textbook. Herald.Sinks is the problem set.

---

## 2. Audience and surface inventory

### Audiences

Two real readers for Herald.Sinks docs, narrower than the OSS set.

1. **Operator picking a sink.** Has Herald.OSS running, needs to
   send events somewhere (Datadog, SignalFx, S3, Elasticsearch).
   Wants the capability matrix, the JSON config shape, the install
   line, and a working example. Often arrives from the OSS docs via
   the "where do my events go?" question.

2. **Sink author.** Building a new destination as a NuGet plugin.
   May be on the MMPWorks team adding to the curated set, or an
   outside contributor following the contributor guide. Cares about
   the `ILogSinkProvider` contract, `CAPABILITY.yaml`, the auto-
   registration pattern, and the test shape that ships in the
   `tests/` tree.

A third audience exists at the website level — the evaluator
choosing Herald over Serilog/NLog/ZLogger who wants to know "does it
have a sink for *X*?" That audience is Dawn's surface. We feed her
the rendered plugin catalog from `data/herald-sinks/sinks/`; she
shapes the marketing page.

### The public surface

The Herald.Sinks repo (`E:/dev/herald/Modules/Herald.Sinks/`) ships
one NuGet package per sink, each rooted at
`src/Herald.Sinks.<Name>/`. Surface per sink:

- **The provider type.** `<Name>LogSinkProvider` — implements
  `ILogSinkProvider` from Herald.OSS. The class consumers configure
  by name in JSON.
- **The sink type.** `<Name>LogSink` — the implementation. Some
  sinks also implement `IBatchedLogSink` or `IKernelSink`.
- **The registration shim.** `<Name>SinkRegistration` — the
  `[ModuleInitializer]` that auto-registers on assembly load.
- **The capability manifest.** `CAPABILITY.yaml` — the
  authoritative contract. Identity, JSON config shape, capabilities,
  limitations, edition, AOT compatibility, vendor, changelog.
- **The configuration form.** `configuration-<name>.mmpform` —
  embedded resource the Dashboard renders.
- **The README.** Auto-generated from `CAPABILITY.yaml` by
  `tools/generate-readmes.cjs`.

The repo currently ships ~80 sinks under `src/`. Every one of them
has a `CAPABILITY.yaml` and a per-sink README following the same
shape. That uniformity is what makes the docs tractable — one
schema, many instances.

---

## 3. Diátaxis mapping

The four-quadrant mapping for Herald.Sinks. Smaller than OSS
because most of the explanation lives in OSS docs and we
cross-reference rather than restate.

### Tutorials (learning-oriented)

One tutorial only. Sinks are not a learning surface in their own
right; OSS is. The tutorial here covers the one workflow specific
to Herald.Sinks: adding a destination beyond the built-in console.

- **`tutorials/your-first-sink-plugin.md`**. Operator picking
  Herald.Sinks.SignalFx, installing it, wiring the access token,
  seeing events land in SignalFx. Single sink, real config, end
  state visible in the destination dashboard.

### How-to guides (problem-oriented)

The how-to surface is mostly per-sink. Each sink's page is a how-to
in disguise. Plus a small set of cross-cutting recipes.

- **`howtos/pick-the-right-sink.md`**. Decision guide. Capability
  matrix as a flowchart. "I have logs from a high-volume API"
  → batched HTTP sinks. "I need long retention" → object-storage
  sinks. "I need correlation with metrics" → SignalFx, Datadog.
- **`howtos/configure-a-sink-from-json.md`**. The JSON shape the
  Sinks layer reads. Cross-references the OSS
  `reference/config/herald-json.md` for the surrounding
  configuration.
- **`howtos/wrap-a-sink-with-async-batching.md`**. The Async sink
  is itself a Herald.Sinks package. This page covers wrapping any
  other sink with the async decorator.
- **`howtos/contribute-a-new-sink.md`**. Lift from the existing
  `Herald.Sinks/CONTRIBUTING.md`. Adds the `CAPABILITY.yaml` walk-
  through and points sink authors at the migration pattern.
- **`howtos/troubleshoot-a-silent-sink.md`**. The Sinks-specific
  version of the OSS silent-events guide. Covers the auto-
  registration gotcha (the analyzers/dotnet/cs packaging rule),
  config-key typos, and per-vendor auth failures.

### Reference (information-oriented)

Reference is rendered from `data/herald-sinks/`. The biggest
single surface is the per-sink page set — one page per sink, all
emitted from `CAPABILITY.yaml`.

- **`reference/sinks/index.md`**. The capability matrix. One row
  per sink. Sortable by category (observability, storage, queue,
  alerting), by edition, by AOT compatibility.
- **`reference/sinks/<name>.md`**. One per sink. Rendered directly
  from `CAPABILITY.yaml`. Identity, vendor, install, capabilities,
  limitations, JSON config, examples.
- **`reference/capability-schema.md`**. The schema every
  `CAPABILITY.yaml` follows. Lift from the existing
  `Herald.Sinks/CAPABILITY-SCHEMA.md`.
- **`reference/sink-contract.md`**. The `ILogSinkProvider` /
  `ILogSink` / `IBatchedLogSink` / `IKernelSink` contract from the
  sink-author's point of view. Cross-references the OSS
  `reference/api/` for the type definitions; this page is the
  consumer-side explainer.

### Explanation (understanding-oriented)

Two pages. Both lean on OSS explainers via cross-reference rather
than restate.

- **`explanation/why-sinks-are-their-own-repo.md`**. The
  separation rationale. Sinks know transport; Core knows the event.
  Independent versioning, independent NuGet packages, no Core churn
  when a sink vendor changes their auth header. Names CUPID's
  *Unix philosophy* and the DRY win of one manifest schema across
  every destination.
- **`explanation/auto-registration-pattern.md`**. How
  `[ModuleInitializer]` + `analyzers/dotnet/cs/` packaging produce
  the `dotnet add package` ergonomics. Cross-references the OSS
  `explanation/source-gen-vs-runtime.md` for the generator side.

---

## 4. Canonical-data inventory

The Sinks layer has fewer record categories than OSS because most
records *already exist* — every sink ships a `CAPABILITY.yaml` in
its source tree. The renderer reads those files directly.

### Categories

- **`data/herald-sinks/sinks/`**. **Mirrored, not authored.** The
  renderer reads
  `E:/dev/herald/Modules/Herald.Sinks/src/Herald.Sinks.*/CAPABILITY.yaml`
  and treats each one as a first-class record. We do **not**
  re-author these in Herald.Documentation. The single source of
  truth is the file shipped with the sink's source.
- **`data/herald-sinks/categories/`**. One record per sink category
  (observability, storage, queue, alerting, file, network, chat).
  Description, when-to-use, related-sinks.
- **`data/herald-sinks/contributor-checklist/`**. One record per
  step in the sink-author workflow. Used by the renderer to emit a
  consistent checklist on the contributor page and inside the
  Herald.Sinks repo's CONTRIBUTING.

### Schema sketch

```
schemas/herald-sinks/
  capability.schema.json   : Mirrors Herald.Sinks/CAPABILITY-SCHEMA.md.
                              Used to validate the YAML files at render
                              time, not to author new records.
  category.schema.json     : Slug, name, description (md), when-to-use,
                              related-sinks[]
  contributor-step.schema.json
                            : Order, name, instruction (md), code-sample
```

The most important rule here: the `CAPABILITY.yaml` schema is owned
by the Herald.Sinks repo. Herald.Documentation mirrors it for
validation, not for authority. When the Sinks team changes the
schema (adds a field, deprecates one), the canonical edit happens
in `Herald.Sinks/CAPABILITY-SCHEMA.md` and the documentation
schema follows. This keeps the producer-consumer relationship clean.

---

## 5. Prose inventory

Pages under `prose/herald-sinks/`. Frontmatter shape matches the
OSS plan exactly. Same fields, same draft rule, same
last-reviewed expectation.

The full prose inventory is the page list in §3. Cross-cutting prose
that doesn't fit a quadrant:

- **`prose/herald-sinks/index.md`**. Landing page. Picks the
  reader's path (operator picking a sink / sink author).
- **`prose/herald-sinks/quickstart.md`**. The minimum-path
  quickstart. Already drafted as the alpha page in this round.
- **`prose/herald-sinks/CHANGELOG-rendered.md`**. Generated from
  per-sink `CAPABILITY.yaml` changelog blocks plus a top-level
  Herald.Sinks repo changelog.

---

## 6. Diagram inventory

Two diagrams up front. Mermaid only. The visual story for Sinks is
mostly "the auto-registration walk" and "the categorization tree" —
neither earns a hand-authored SVG yet.

| Page | Diagram | Level | Notes |
|---|---|---|---|
| `explanation/auto-registration-pattern.md` | `dotnet add package` → assembly load → `[ModuleInitializer]` → `LogSinkProviderRegistry.Default` | Mermaid sequence | Linear, four steps. Mermaid is the right fit. |
| `howtos/pick-the-right-sink.md` | Category decision tree | Mermaid flowchart | Five or six branches. Helps the reader skim. |

If a future explainer ("how a batched HTTP sink differs from a
kernel sink at the latency boundary") earns a hand-authored SVG,
match the OSS architecture-page SVG style for visual continuity.

---

## 7. Phased execution order

Two phases for Herald.Sinks. The OSS plan has five because OSS is
greenfield documentation. Herald.Sinks already has the
`CAPABILITY.yaml` corpus, the per-sink READMEs, and the
contributor guide. We are mostly wiring the existing assets into
the rendered surface.

### Phase 0. Pilot quickstart (this round)

Goal: prove the cross-product link contract end-to-end. One alpha
page lives at `prose/herald-sinks/quickstart.md`, links to the OSS
first-pipeline tutorial via relative markdown, and is ready for
Dawn to wire a `/documentation/herald-sinks/quickstart` route when
the website's sync script extends to `prose/herald-sinks/**`.

Output:
- `prose/herald-sinks/quickstart.md` (this round).
- This plan (this round).

No reference rendering yet, no `data/herald-sinks/` ingestion yet,
no diagrams yet. The pilot is one page that proves the lock-step
pattern works.

### Phase 1. Full reference (after OSS Phase 1 lands)

Goal: every sink that ships in `Herald.Sinks/src/` has a rendered
reference page at `/documentation/herald-sinks/reference/sinks/<name>`.
The capability matrix renders. The contributor page renders. The
quickstart's "next steps" links resolve.

Output:
- Sink ingestion renderer that reads
  `E:/dev/herald/Modules/Herald.Sinks/src/Herald.Sinks.*/CAPABILITY.yaml`
  and emits `rendered/herald-sinks/site/reference/sinks/<name>.md`.
- Capability matrix renderer.
- All how-to and explanation pages from §3 authored.
- Two Mermaid diagrams from §6 landed.
- Dawn handoff: `rendered/herald-sinks/website/plugin-catalog.ts`
  feeds the marketing surface's "supported sinks" page.

After Phase 1, the Herald.Sinks docs are a peer of the OSS docs —
same shape, same rendering pipeline, same lock-step release.

---

## 8. Open questions

Three decisions the user needs to make before Phase 1 begins. The
herald-oss plan has ten; we deliberately keep this list short
because most framework-level decisions there (doc site framework,
renderer language, rendered-output commit policy) are inherited
unchanged.

1. **`CAPABILITY.yaml` ingestion location.** The renderer reads
   the YAML files directly from `E:/dev/herald/Modules/Herald.Sinks/src/`.
   That works locally. For CI it needs a stable input — either a
   git submodule pointer (the Herald umbrella already has one) or a
   per-release tarball produced by the Sinks build. Recommendation:
   submodule pointer, matching the umbrella pattern. Decision
   unblocks Phase 1 CI.

2. **Per-sink page URL shape.** `/documentation/herald-sinks/reference/sinks/<name>`
   is the predictable shape. The alternative is to flatten —
   `/documentation/herald-sinks/<name>` — so the URL reads like
   "the SignalFx page" rather than "the SignalFx reference page."
   Stripe's pattern (one URL per operation) suggests flattening
   when each page stands alone. Recommendation: flatten, since
   `<name>` is unique and each sink page is self-contained.
   Decision unblocks the renderer's path scheme.

3. **Third-party sink listings.** The repo is self-curating —
   MMPWorks-authored sinks live in `Herald.Sinks/src/`, third-party
   sinks ship as their own NuGet packages elsewhere. The docs need
   a policy: do we maintain a curated "community sinks" index that
   links to outside packages, or do we stop at the
   MMPWorks-authored surface and rely on NuGet search?
   Recommendation: stop at the MMPWorks-authored surface for v1,
   revisit when three or more community sinks ship. Decision
   affects the contributor docs and the website's discoverability
   story.

---

## Closing note

Herald.Sinks docs are mostly a rendering exercise. The hard work —
the `CAPABILITY.yaml` schema, the per-sink manifests, the
contributor guide, the auto-registration ergonomics — is already
done in the Herald.Sinks repo. What we add here is the cross-
product wiring, the consumer-facing landing pages, and the
rendered reference surface.

The lock-step contract with Herald.OSS is the load-bearing decision.
A reader who lands on the SignalFx quickstart should be able to
follow a link to the OSS kernel explainer without a second thought,
and a reader on the OSS multi-tenancy explainer should be able to
follow a link to the SignalFx page without a second thought. That
crossing is the whole experience.
