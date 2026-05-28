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

### What has landed so far

The first authored material targets Herald.OSS 0.10.2. Three
design-decision artifacts and one security posture ship as the
dual-register pattern: a structured record in `data/` and a
prose page in `prose/` for each one. The prose carries the
analogy and the community-publication voice; the record carries
the queryable facts.

- **The async-sink cross-tenant PII posture** — five-layer defense
  for `FastPathAsyncSink`, six new HERALD008–013 analyzer rules,
  the `[HeraldDrainSafe]` reviewed-suppression attribute. Prose:
  `prose/herald-oss/explanation/security/async-sink-cross-tenant-pii-posture.md`.
  Record: `data/herald-oss/security-postures/async-sink-cross-tenant-pii.json`.
- **The compact-path default-axes-only contract** — the 16-byte
  `LogPropertyCompact` carries default axes by construction; the
  full `LogProperty` path carries non-default axes; HERALD014
  analyzer rule enforces the line. Prose:
  `prose/herald-oss/explanation/design-decisions/compact-path-default-axes-only.md`.
  Record: `data/herald-oss/design-decisions/compact-path-default-axes-only.json`.
- **The Lever A async-default contract** — the new default
  `FastPathAsyncSink` async handoff uses a value-typed
  `AsyncEnvelope` on a per-connection channel; the engineering
  catalog of thirteen approaches is published as the
  due-diligence record. Prose:
  `prose/herald-oss/explanation/design-decisions/lever-a-async-default.md`.
  Record: `data/herald-oss/design-decisions/lever-a-async-default.json`.

The schema both design-decision records validate against is
`schemas/herald-oss/design-decision.schema.json`. The security
posture record validates against
`schemas/herald-oss/security-posture.schema.json`. Both schemas
were authored alongside their first records, on the rule that a
schema lands when the second instance of a fact shape arrives.

### The dual-register pattern

Each design-decision artifact ships in two registers. The
structured record under `data/` carries the queryable facts (the
decision, the contract, every alternative considered with its
verdict and evidence grade, the trust boundary, the honest
residual, the extension path, the cross-references). The prose
page under `prose/` carries the same content for a human reader
at roughly grade-10 reading level, anchored by an analogy and
written to invite the OSS community to push back or PR alternatives.
The pattern keeps the technical record auditable and the public
narrative readable without forcing either to compromise.

## License

Apache 2.0. See `LICENSE` and `NOTICE`.
