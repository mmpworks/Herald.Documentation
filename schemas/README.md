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

The first two Herald.OSS schemas have landed alongside their
first records. Both were authored on the "second appearance is
the signal" rule above.

- **`herald-oss/design-decision.schema.json`** — validates the
  records under `data/herald-oss/design-decisions/`. A
  design-decision record captures the decision, the contract it
  establishes, every alternative considered (with verdict and
  evidence grade), the trust boundary, the honest residual, the
  extension path, the cross-references, and the PR-back
  invitation to the OSS community. Two records validate against
  it today: `compact-path-default-axes-only.json` and
  `lever-a-async-default.json`.
- **`herald-oss/security-posture.schema.json`** — validates the
  records under `data/herald-oss/security-postures/`. A
  security-posture record captures the threat, the layered
  defense, the analyzer enforcement, the trust boundary, the
  twelve-claim threats-considered table, the test plan, and the
  honest residual. One record validates against it today:
  `async-sink-cross-tenant-pii.json`.

Two more schemas live elsewhere in this tree on the same rule:
`schemas/compliance/audit-trail-comparison.schema.json` and
`schemas/licensing/` (capability, preset, nag-template).

The renderers are still placeholders in `scripts/`. The Herald.OSS
plan in `prose/herald-oss/_planning/` enumerates the categories
that come next — sinks, methods, config keys, capability matrix,
glossary, performance claims — and each will land as a new schema
the same way these two did.

When you add a schema, name the corresponding renderer in this
README's tree so future readers can trace which renderer reads which
schema.
