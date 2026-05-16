# scripts/

Renderers that read the canonical source (`data/`, `prose/`, `diagrams/`)
and produce the markdown, HTML, and SVG that consumer surfaces read.

This directory is a placeholder. The renderer pipeline lands as the
first authoring phase needs it — start with the smallest renderer that
turns one structured record category into one rendered artifact, then
grow from there. Resist the urge to scaffold a full framework before
the first real consumer exists.

## Shape we're aiming at

A renderer is a small, deterministic script. Given the same inputs it
produces the same output. That makes the rendered diff reviewable in a
pull request.

Each renderer:

1. Reads one or more files under `data/` (JSON validated against a
   schema in `schemas/`) and optionally pulls prose fragments from
   `prose/`.
2. Walks the records and produces markdown, HTML, or SVG.
3. Writes the output to `rendered/<consumer>/<path>`.
4. Reports what it wrote.

## Conventions

- **Determinism.** Renderers sort records by a stable key before
  iteration. No timestamps, no random ordering, no environment-dependent
  output. The same input must produce the same output every run.
- **One renderer, one output category.** A renderer that produces both
  a README section and an mkdocs page is doing two jobs. Split it.
- **No mutation of inputs.** Renderers read only. They never write
  back to `data/`, `prose/`, or `diagrams/`.
- **Errors surface loud.** Schema validation failures, missing records,
  unresolved cross-references all stop the build with a clear message.

## What lives here

Until the first real renderer ships, this directory is empty except
for this README. The renderer language is not yet decided — Node,
Python, and a .NET console app are all candidates. The decision sits
with the user.

The first concrete renderer will likely be the Herald.OSS README
section assembler, since that's the first consumer surface the plan
calls out. See `prose/herald-oss/_planning/` for the plan.
