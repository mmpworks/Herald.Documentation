# Documentation Guidance

This directory holds the **meta-layer** of Herald.Documentation. It is
where decisions about how the documentation gets built are recorded, so
the next person who picks up the work can do so cold.

Nothing here ships to a reader. The reader-facing content lives in
`prose/` (narrative pages) and `data/` (structured records). This is
the planning and methodology corpus that sits behind both.

## What lives here

- **Documentation plans** — per-repo or per-release plans that name the
  pages we will build, the records we will populate, and the sequence
  we will ship them in. The Herald.OSS plan is the first example.
- **Sequencing notes** — phase orders, dependency calls, and "we
  agreed to ship X before Y" decisions.
- **Methodology notes** — rules of thumb for harvesting old fragments,
  IP-vs-SDK calls when adapting Modules/Core content, the diagram
  cadence used for a particular surface, the analogy bench (which
  callout-analogies have been used and where).
- **Exemplar studies** — when we read Stripe Docs, the Rust Book, or
  MDN and lifted a pattern, the study notes that produced the lift
  belong here so the rationale is preserved.
- **Audience inventories** — per-repo audience maps. Who reads what,
  in what order, on what kind of screen, with what prior knowledge.
- **Open-question logs** — architectural-ambiguity questions we
  surfaced to Richard, the disposition that came back, and the date.

## How this differs from the other top-level directories

```
data/                    structured records the renderers read
                         (API, sinks, config keys, capability matrices)

prose/                   narrative pages a reader actually reads
                         (tutorials, how-tos, explanations)

diagrams/                diagram sources (Mermaid, SVG, Excalidraw)
                         consumed by prose/ pages

schemas/                 JSON Schemas the records validate against

scripts/                 renderers that turn data/ + prose/ into output

documentation-guidance/  the "how we do docs here" meta-layer
                         (this directory)
```

The rule. If a file changes what the reader sees, it belongs under
`prose/`, `data/`, or `diagrams/`. If a file changes how we *decide*
what the reader sees, it belongs here.

## Layout

Mirrors the per-repo subtree shape used by `data/` and `prose/`:

```
documentation-guidance/
  herald-oss/      planning + methodology for Herald.OSS docs
  core/            Herald.Core
  compliance/      Herald.Compliance
  sci/             Herald.Sci
  server/          Herald.Server
  dashboard/       Herald.Dashboard
  lean/            Herald.Lean
  herald-py/       Herald.Py
  herald-sinks/    Herald.Sinks
```

Cross-repo guidance (e.g. ecosystem-wide voice rules, schema
conventions, renderer behavior) sits at the root of this directory.

## Lifecycle

A plan stays in `documentation-guidance/` for as long as it is
load-bearing. Once a phase ships and the plan's tracker is empty, the
plan moves to a `documentation-guidance/<repo>/archive/` folder with
the closing date in the filename. We do not delete plans. The trail
matters when a future contributor asks why a page exists in the shape
it does.
