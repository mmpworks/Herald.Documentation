# schemas/

JSON Schemas that the structured records in `data/` validate against.

Schemas are the contract between the records and the renderers. If a
record drifts away from the schema, the renderer fails. That's the
whole point — the failure is loud, the fix is local.

## When you add a schema

Add a schema the second time a fact appears in more than one place. The
first appearance is a free-form prose page. The second appearance is
the signal that the fact has earned a structured home. Promote it
then, not before — premature schema-shaping creates ceremony without
payoff.

## Schema discipline

- **One concept per schema.** A `sink.schema.json` describes one sink
  record. A `capability-matrix.schema.json` describes one matrix
  document. Don't bundle unrelated concepts.
- **`$id` is the path.** A schema at `schemas/herald-oss/sink.schema.json`
  carries `"$id": "https://herald.dev/schemas/herald-oss/sink.schema.json"`
  (the URL is informational; validators key off the file path locally).
- **Required fields are honest.** Mark a field required only if every
  record genuinely needs it. Optional fields take a `default` when
  the renderer needs one.
- **Markdown fragments are first-class.** A schema field can carry
  markdown prose. Mark such fields with a `"contentMediaType": "text/markdown"`
  hint so editors know not to wrap quotes around it.
- **Cross-references are explicit.** A field that references another
  record (e.g. a sink referencing a capability) carries the target
  schema's `$id` in its `"$ref"` or a `"x-references"` annotation the
  renderer reads.

## What lives here

This directory is empty until the first structured-record category
lands. The Herald.OSS plan in `prose/herald-oss/_planning/` enumerates
the categories the schemas will need to cover — sinks, methods, config
keys, capability matrix, glossary, performance claims.

When you add a schema, name the corresponding renderer in this
README's tree so future readers can trace which renderer reads which
schema.
