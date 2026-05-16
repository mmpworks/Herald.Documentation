# Herald.Documentation

Canonical documentation source for the Herald ecosystem. Apache 2.0.

This repo is the single place where Herald's facts live. READMEs, doc
sites, API references, and the public website all read from here.
Editing in one place keeps every consumer surface in sync.

## The idea — docs as a database

Most documentation drifts because the same fact lives in three files
and only one gets updated. We fix that by treating documentation like
a database:

- **Structured records** hold the facts that show up in more than one
  place. API signatures, configuration keys, sink catalogs, capability
  matrices, benchmark numbers.
- **Prose with frontmatter** holds the narrative pages. Tutorials,
  architecture explainers, migration guides.
- **Diagrams** sit alongside the prose. Mermaid by default, hand-authored
  SVG for richer storytelling, Excalidraw for early sketches.
- **Renderers** turn the structured records into the markdown the
  README and the doc site read. Run the renderers, and every consumer
  surface is consistent.

The line between structured and prose is simple. If the same fact
appears in more than one rendered place, it belongs in a record. If a
page is a one-off narrative, it stays as prose.

## Layout

```
data/                    structured records, organized by source repo
prose/                   markdown with frontmatter, mirrored layout
diagrams/                Mermaid sources, hand-authored SVG, Excalidraw JSON
schemas/                 JSON Schemas the records validate against
scripts/                 renderers that read data/ + prose/ and produce output
rendered/                build artifacts (gitignored)
documentation-guidance/  the "how we do docs here" meta-layer
                         (plans, sequencing, methodology, exemplar studies)
```

Inside `data/`, `prose/`, `diagrams/`, and `documentation-guidance/`,
the same nine subtrees mirror the source repos:

- `herald-oss/` — the Apache 2.0 upstream
- `core/` — the commercial Herald.Core wrapper
- `compliance/` — Herald.Compliance
- `sci/` — Herald.Sci
- `server/` — Herald.Server
- `dashboard/` — Herald.Dashboard
- `lean/` — Herald.Lean
- `herald-py/` — the Python implementation
- `herald-sinks/` — the sink curation monorepo

A doc that crosses repos (e.g. an ecosystem overview) goes wherever
its primary anchor lives, with cross-links.

## Contributing

Apache 2.0 inbound equals outbound. No CLA today. We defer the CLA
question and follow whatever pattern Herald.Sinks settles on for
externally-authored material. Consult sibling repos before adding a
CLA workflow here.

Pull requests that change structured records should run the renderers
locally before pushing, so the diff includes the rendered output the
PR reviewer needs to see. Pull requests that change prose only do
not need to re-render.

## Status

Repo scaffold landed 2026-05-16. First documentation plan is for
Herald.OSS — see `documentation-guidance/herald-oss/herald-oss-documentation-plan.md`.

## License

Apache 2.0. See `LICENSE` and `NOTICE`.
