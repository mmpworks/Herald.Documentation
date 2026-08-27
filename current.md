# Current State
_as of 2026-08-12_

## What we're building right now
Herald.Documentation is the canonical "docs as a database" source for the Herald ecosystem (structured `data/`, prose `prose/`, `diagrams/`, `schemas/`, renderer `scripts/`) — READMEs, doc sites, and the public website all read from here. Two active threads right now: (1) the compliance auditor-story corpus under `prose/compliance/novel/` and its `synopsis/` mirror just landed chapter 24 ("Success Bank"), and (2) Herald.OSS technical docs (Live Viewer REST contract, DemoApp seed, 0.10.2 design-decision + security-posture artifacts) landed a few commits back. CI now notifies Herald.Website to rebuild whenever prose lands (`ci/notify-website`), so this repo drives the public site's content pipeline directly.

## Active decisions
- 2026-08-11: chapter 24 (Success Bank) added to the auditor-story novel corpus; synopsis mirror kept in lockstep (`prose/compliance/synopsis/24-success-bank.md`).
- 2026-08-xx (via PR #3): CI wired to notify Herald.Website on prose changes — prose landing here now triggers a website rebuild, so prose commits are effectively publish events, not just repo-internal edits.
- 2026-07-xx (via PR #2): FINRA Q&A companion doc added at `prose/compliance/q-and-a/finra.md` for the live Q&A surface.
- 2026-06-xx: `prose/compliance/novel/README.md`'s team roster and "read all twenty-three" framing predates chapter 24 — the count in that README is stale relative to what's actually in the directory (24 chapters now).
- Repo-wide: Apache 2.0 canonical-docs project; the "structured record vs. one-off prose" split (README's "docs as a database" section) governs where any new fact goes.

## Open questions
- `prose/compliance/novel/README.md` says "twenty-three" chapters; the directory has 24. Needs a wording pass (low-stakes, but visible to readers).
- Whether the auditor-story corpus has a target chapter count or is open-ended — no stop condition is recorded anywhere in the repo.
- Whether the Herald.OSS technical-docs thread (Live Viewer REST contract, 0.10.2 artifacts) has further planned entries, or is complete for the current OSS release — no open tracking doc found for it in this pass.

## Next action
Check `documentation-guidance/compliance/` for any in-flight chapter plan or story queue before writing a new chapter — if one exists, use it rather than guessing the next institution/scenario. If none exists, the next auditor-story chapter is an open creative choice, not a scripted one.

## Stop condition
Halt and return to Steve before: renaming or removing any published chapter (breaks the CI→website publish chain), changing the ADR numbering scheme, or altering `schemas/` in a way that would invalidate existing `data/` records.

## Needs approval
- Any change that triggers the website rebuild in a way visible to the public (this repo's prose IS the public content pipeline now, per the CI notify-website wiring) — normal prose additions are fine, but structural changes (renumbering chapters, restructuring `prose/compliance/`) should get a heads-up first.
- Agents can freely: write new auditor-story chapters/synopses following the established pattern, fix stale counts/wording, add structured `data/` records, run renderers.
