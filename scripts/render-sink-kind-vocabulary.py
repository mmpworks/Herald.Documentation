#!/usr/bin/env python
"""Validate and render the sink-kind vocabulary contract record.

The sink-kind vocabulary record pins the three names a sink's "kind"
carries across Herald layers and the rule for which name is canonical
at each boundary. It is a cross-cutting contract spec: one structured
record, one rendered prose view.

This script does two things, in order:
    1. Validate `data/herald-oss/sink-kind-vocabulary.json` against
       `schemas/herald-oss/sink-kind-vocabulary.schema.json`.
    2. Render the record to a markdown view at
       `rendered/herald-oss/sink-kind-vocabulary.md`.

The render is deterministic — same input, same output — so the PR diff
is reviewable. Re-run after editing the data file; never hand-edit the
rendered markdown (the edit would drift from the record on the next run).

Usage:
    python scripts/render-sink-kind-vocabulary.py            # validate + render
    python scripts/render-sink-kind-vocabulary.py --check    # validate + verify render is current; no write

Exit codes:
    0  validated and rendered (or --check: render is current)
    1  data file fails schema validation, or --check found stale render
    2  schema itself is malformed, or jsonschema not installed
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import json
except ImportError:  # pragma: no cover — json is stdlib
    print("error: json module unavailable", file=sys.stderr)
    sys.exit(2)

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("error: jsonschema not installed. Run: pip install jsonschema", file=sys.stderr)
    sys.exit(2)


# Path discipline — script lives in repo-root/scripts/, so repo root is one up.
REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schemas" / "herald-oss" / "sink-kind-vocabulary.schema.json"
DATA_PATH = REPO_ROOT / "data" / "herald-oss" / "sink-kind-vocabulary.json"
RENDER_PATH = REPO_ROOT / "rendered" / "herald-oss" / "sink-kind-vocabulary.md"


def _load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _strip_schema_pointer(payload: dict) -> dict:
    # The data file carries a `$schema` pointer for editor support; the
    # validator doesn't need it and shouldn't try to resolve the relative path.
    return {key: value for key, value in payload.items() if key != "$schema"}


def _validate(payload: dict) -> int:
    schema = _load_json(SCHEMA_PATH)
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # noqa: BLE001 — surface the schema problem.
        print(f"error: schema is malformed: {exc}", file=sys.stderr)
        return 2

    validator = Draft202012Validator(schema)
    errors = sorted(
        validator.iter_errors(payload),
        key=lambda err: list(err.absolute_path),
    )
    if errors:
        print(f"  FAIL  {DATA_PATH.relative_to(REPO_ROOT)}  ({len(errors)} error(s))")
        for err in errors:
            path = "/".join(str(segment) for segment in err.absolute_path) or "<root>"
            print(f"        {path}: {err.message}")
        return 1
    print(f"  OK  {DATA_PATH.relative_to(REPO_ROOT)}")
    return 0


def _render(payload: dict) -> str:
    """Render the record to the markdown view. Pure function of the payload."""
    vocab_by_id = {v["id"]: v for v in payload["vocabularies"]}
    lines: list[str] = []

    # Frontmatter — keeps the rendered page queryable alongside hand-authored prose.
    lines.append("---")
    lines.append(f"title: {payload['title']}")
    lines.append("slug: contracts/sink-kind-vocabulary")
    lines.append("category: reference")
    lines.append("audience: contributor")
    lines.append(f"last-reviewed: {payload['last_reviewed']}")
    lines.append("rendered-from: data/herald-oss/sink-kind-vocabulary.json")
    lines.append("generated: true")
    lines.append("---")
    lines.append("")
    lines.append("<!-- GENERATED FILE — do not hand-edit.")
    lines.append("     Edit data/herald-oss/sink-kind-vocabulary.json and re-run")
    lines.append("     scripts/render-sink-kind-vocabulary.py. -->")
    lines.append("")

    lines.append(f"# {payload['title']}")
    lines.append("")
    if payload.get("ratified_by"):
        lines.append(f"*Rule ratified by {payload['ratified_by']}. "
                     f"Last verified against the code on {payload['last_reviewed']}.*")
        lines.append("")

    # The rule first — it is the load-bearing sentence.
    lines.append("## The rule")
    lines.append("")
    lines.append(payload["rule"]["statement"])
    lines.append("")

    # The layer table — the layer-to-vocabulary mapping.
    lines.append("## Which layer speaks which name")
    lines.append("")
    lines.append("| Layer | Symbol | Speaks | Example |")
    lines.append("|---|---|---|---|")
    for layer in payload["layers"]:
        spoken = vocab_by_id[layer["speaks"]]["name"]
        lines.append(
            f"| {layer['layer']} | `{layer['symbol']}` | "
            f"**{spoken}** | `{layer['example']}` |"
        )
    lines.append("")

    # The three vocabularies, defined once each.
    lines.append("## The three names")
    lines.append("")
    for vocab in payload["vocabularies"]:
        examples = ", ".join(f"`{e}`" for e in vocab["examples"])
        lines.append(f"- **{vocab['name']}** — {vocab['definition']} "
                     f"Examples: {examples}.")
    lines.append("")

    # The callout analogy.
    if payload.get("analogy"):
        lines.append(f"> 💡 **Quick picture.** {payload['analogy']}")
        lines.append("")

    # The disposition of each vocabulary.
    lines.append("## Canonical, scoped, forbidden")
    lines.append("")
    lines.append(f"- **Canonical.** {payload['rule']['canonical']}")
    lines.append(f"- **Scoped.** {payload['rule']['scoped']}")
    lines.append(f"- **Forbidden.** {payload['rule']['forbidden']}")
    lines.append("")

    # Why it matters — the concrete consequence.
    lines.append("## Why it matters")
    lines.append("")
    lines.append(payload["consequence"]["summary"])
    lines.append("")
    lines.append(payload["consequence"]["detail"])
    lines.append("")

    # The do/don't a contributor reads first.
    lines.append("## Do / don't")
    lines.append("")
    lines.append(f"- **Do.** {payload['do_dont']['do']}")
    lines.append(f"- **Don't.** {payload['do_dont']['dont']}")
    lines.append("")

    # Source files — so the next reader can re-verify.
    if payload.get("source_files"):
        lines.append("## Verified against")
        lines.append("")
        for src in payload["source_files"]:
            lines.append(f"- `{src['repo']}` — `{src['path']}` ({src['role']})")
        lines.append("")

    return "\n".join(lines) + "\n"


def main() -> int:
    if not SCHEMA_PATH.is_file():
        print(f"error: schema not found at {SCHEMA_PATH}", file=sys.stderr)
        return 2
    if not DATA_PATH.is_file():
        print(f"error: data file not found at {DATA_PATH}", file=sys.stderr)
        return 1

    payload = _strip_schema_pointer(_load_json(DATA_PATH))

    code = _validate(payload)
    if code != 0:
        return code

    rendered = _render(payload)
    check_only = "--check" in sys.argv[1:]

    if check_only:
        current = RENDER_PATH.read_text(encoding="utf-8") if RENDER_PATH.is_file() else ""
        if current != rendered:
            print(f"  STALE  {RENDER_PATH.relative_to(REPO_ROOT)} — re-run without --check to update.")
            return 1
        print(f"  CURRENT  {RENDER_PATH.relative_to(REPO_ROOT)}")
        return 0

    RENDER_PATH.parent.mkdir(parents=True, exist_ok=True)
    RENDER_PATH.write_text(rendered, encoding="utf-8")
    print(f"  RENDERED  {RENDER_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
