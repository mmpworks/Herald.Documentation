# FAQ migration handoff (2026-05-19)

Dawn handing off the Herald.OSS FAQ migration to Heather per Steve's
direction.

## What landed

1. **Schema** at `schemas/faq.schema.json` (draft).
   - One document per surface (e.g. `herald-oss.json`).
   - `surface` + `version` + `title` + `lead` at the top level.
   - `sections[]` — each section has `id`, `title`, optional `lead`,
     and `items[]`.
   - Each item has `id`, `question`, and `answer_html`. The website
     consumer renders `answer_html` verbatim into a `v-html` target.
   - Sections render in array order; items inside a section render
     in array order.

2. **Migrated content** at `data/herald-oss/faq.json`.
   - **Lossless 1:1 migration** of all 8 panels from
     `web/src/pages/FaqPage.vue` (sha 99231d8 on
     `feat/herald-style-refresh-2026-05-18`).
   - Current grouping: one section per original panel, one item per
     section.
   - The sinks table was inlined as an HTML `<table>` inside the
     sink-catalog item's `answer_html`. The data came from the
     `SINKS` const in `FaqPage.vue`.

## What's yours to decide

- **Schema ratification or refinement.** Look at `schemas/faq.schema.json`.
  If the shape doesn't fit how you want to author docs (e.g. you'd
  rather split tables out as structured data rather than HTML strings,
  or you want a richer `answer_blocks[]` shape with typed block kinds),
  refine the schema and re-migrate the content. The website-side
  consumer doesn't exist yet, so we can iterate on shape without
  breaking anything live.

- **Grouping.** Steve's direction is that you own the section
  structure. The 8 panels in `faq.json` are placeholder sections so
  no content was dropped during the migration. Re-group as the docs
  author: cluster license + signed-binaries together, split migration
  by source logger, surface pricing + support under one "commercial"
  section — whatever serves the reader. Keep every question; that's
  the only hard constraint Steve set.

- **Voice.** Content is verbatim from the website today. If your
  documentation voice differs from the website's marketing voice,
  feel free to rephrase the question slugs and answer prose. The
  consumer treats `answer_html` as opaque content.

## Consumption contract (for context)

The website-side fetch happens via
`web/scripts/fetch-herald-docs-if-missing.cjs`, which clones
Herald.Documentation into a temp location and copies the relevant
data into `web/public/herald-docs/`. The plan is:

1. Add `data/herald-oss/faq.json` to the manifest the fetch script
   reads.
2. At build time, validate `faq.json` against `schemas/faq.schema.json`
   with `ajv`.
3. The FaqPage component (W2/W3 of the migration, not landed yet)
   does `fetch('/herald-docs/faq/herald-oss.json')` and renders the
   sections as `v-expansion-panels`.

Steve's instruction: don't touch the website-side consumer rewrite
yet. Wait for Heather's schema ratification + content commit, then
Dawn picks up the consumer wire-in.

## Action requested

1. Ratify or refine `schemas/faq.schema.json`. If you refine,
   re-migrate `data/herald-oss/faq.json` to match.
2. Re-group the sections as you see fit (preserve all questions).
3. Commit + push to `mmpworks/Herald.Documentation` on `main`.
4. Report the commit SHA back to Steve so Dawn can wire up the
   consumer fetch.

— Dawn (herald-website-maintainer)
