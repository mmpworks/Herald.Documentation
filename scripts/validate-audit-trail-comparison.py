#!/usr/bin/env python
"""Validate every audit-trail-comparison data file against its schema.

The audit-trail-comparison subtree carries point-by-point comparisons
between an external AI-audit-trail checklist and the Herald PRD
chain-of-custody specification. Every data file under
`data/compliance/audit-trail-comparison/` must validate against
`schemas/compliance/audit-trail-comparison.schema.json`.

Usage:
    python scripts/validate-audit-trail-comparison.py

Exit codes:
    0  every data file validates
    1  at least one data file fails schema validation
    2  schema itself is malformed

This is the first concrete validator in the repo. Future validators
follow the same shape — load schema, glob data files, validate, report.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("error: jsonschema not installed. Run: pip install jsonschema", file=sys.stderr)
    sys.exit(2)


# Path discipline — script lives in repo-root/scripts/, so repo root is one up.
REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "schemas" / "compliance" / "audit-trail-comparison.schema.json"
DATA_GLOB = REPO_ROOT / "data" / "compliance" / "audit-trail-comparison"


def _load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _strip_schema_pointer(payload: dict) -> dict:
    # The data file carries a `$schema` pointer for editor support; the
    # validator doesn't need it and shouldn't try to resolve the relative path.
    return {key: value for key, value in payload.items() if key != "$schema"}


def main() -> int:
    if not SCHEMA_PATH.is_file():
        print(f"error: schema not found at {SCHEMA_PATH}", file=sys.stderr)
        return 2

    schema = _load_json(SCHEMA_PATH)
    try:
        Draft202012Validator.check_schema(schema)
    except Exception as exc:  # noqa: BLE001 — surface the schema problem.
        print(f"error: schema is malformed: {exc}", file=sys.stderr)
        return 2

    validator = Draft202012Validator(schema)
    data_files = sorted(DATA_GLOB.glob("*.json"))
    if not data_files:
        print(f"warning: no data files found under {DATA_GLOB}")
        return 0

    failed = 0
    for data_path in data_files:
        payload = _strip_schema_pointer(_load_json(data_path))
        errors = sorted(
            validator.iter_errors(payload),
            key=lambda err: list(err.absolute_path),
        )
        rel = data_path.relative_to(REPO_ROOT)
        if not errors:
            row_count = len(payload.get("rows", []))
            print(f"  OK  {rel}  ({row_count} rows)")
            continue
        failed += 1
        print(f"  FAIL  {rel}  ({len(errors)} error(s))")
        for err in errors:
            path = "/".join(str(segment) for segment in err.absolute_path) or "<root>"
            print(f"        {path}: {err.message}")

    if failed:
        print(f"\n{failed} file(s) failed schema validation.")
        return 1

    print(f"\nAll {len(data_files)} audit-trail-comparison file(s) valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
