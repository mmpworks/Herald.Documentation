---
title: Verifier User's Guide — Phase 1 plan
slug: verifier-users-guide-plan
surface: compliance
category: planning
audience: doc-team-internal
version: 2026-05-21
last-reviewed: 2026-05-21
owner: heather
collaborators:
  - tom (diagrams)
  - jared (verifier implementation, Go)
  - richard (spec ambiguity cross-consults)
---

# Verifier User's Guide — Phase 1 plan

This file is the methodology + outline + diagram inventory + sequencing
for the TesseraSeal Verifier User's Guide. It is not the guide itself.
The guide proper lives in `prose/compliance/verifier-users-guide/`.

## Why this guide exists

The verifier is the artifact auditors run, regulators read, and
customers depend on as the integrity-proof primitive. Three reference
implementations exist or are under construction:

- **Herald.Compliance** — the .NET reference (shipped)
- **Visus** — the Python reference (shipped; renamed from Vidimus
  2026-05-21 per Laura's brand-family round)
- **The Go reference** (Jared, Commit 1 in progress; the
  `ffiec/verifier` repo path today). Product-name pick paused
  2026-05-21 — Pearl's collision sweep ruled out the round-1
  candidate (literal CLI conflict with `verus-lang/verus`, CMU's
  Rust formal verifier); Steve revisiting from Laura's round-2
  runners-up.

The user's guide is implementation-agnostic. Auditors do not care which
binary they run; they care about the verdict. The guide explains what
the verifier proves, how to invoke it, what each output field means,
and what to do when verification fails. The runbook
(`ffiec/docs/runbook-verifier.md`, Jared Commit 6 — filename will
rename when the Go product name locks) is the operator deep-dive
companion. This guide is the front door.

## Source-of-truth decision

Canonical home: this repo, under three sibling subtrees:

```
prose/compliance/verifier-users-guide/        narrative + frontmatter
data/compliance/verifier-users-guide/         structured records
diagrams/compliance/verifier-users-guide/     Tom's diagram sources
schemas/compliance/                           JSON Schemas for the records
```

**What is structured-record-shaped (data/):**

- `exit-codes.json` — the §10.12 four-code contract, plus
  examiner-harness branching guidance. The schema is shared across
  the .NET, Python, and Go implementations; the record is one
  rendered fact that ends up in the user's guide, the runbook, the
  conformance test plan, and the herald-website MRM section.
- `output-fields.json` — the Status / Step / Reason / Verdict-Object
  surface. Same multi-render shape as exit codes.
- `cli-flags.json` — implementation-neutral flag catalog. Per-impl
  divergence (the Go `--strict` flag versus the .NET equivalent) is
  carried in the same record as a `per-implementation` map.
- `failure-modes.json` — the step-by-step failure catalog already
  partially expressed in `ffiec/docs/examiner-quickstart.md`'s table.
  Promoting it to a record means the table renders in this guide,
  the quickstart, the runbook, and the IR-scenario corpus from one
  source.
- `additional-verifications.json` — the §10.12 closed enumeration
  (currently 20 markers). Lifted directly from the spec table; one
  edit per amendment cycle, many renders.

**What is prose-shaped (prose/):**

- The conceptual walkthrough of what the verifier proves
- The "what each primitive actually checks" narrative (chain linkage,
  Merkle root, seal signature, per-event MAC)
- The "what to do when it fails" decision flow
- The migration / version policy narrative
- The implementation-choice guidance (Go vs .NET vs Python — when to
  pick which)

**Render targets (Phase 2+):**

| Target | Audience | Render mechanism |
|---|---|---|
| `ffiec/docs/verifier-users-guide.md` | Go contributors / co-located reader | New render script in `Herald.Documentation/scripts/` |
| `herald-website` MRM compliance section | Public audit firms, prospects | Extend `sync-mrm-spec.cjs` pattern or a sibling script Dawn owns |
| Standalone PDF (eventually) | Regulators reading off-network | Pandoc render from the canonical markdown |

The herald-website render is Dawn's placement decision. Heather
produces the canonical material; Dawn places it on the website.

## Audience-and-voice manifesto

The guide is written for **auditors, IT operators, and compliance
officers** as primary readers. Engineers setting up the verifier in
their pipelines are the secondary audience. The guide does NOT
assume cryptographic literacy. It does NOT assume Go, .NET, or Python
fluency. It DOES assume the reader knows what a hash is, what a
digital signature is at the consumer level (you sign a document, the
recipient verifies it), and what a command-line invocation looks like.

**Reading-level target: grades 9-10.** Short sentences. Common words.
One idea per sentence. Active voice. Define every term the first time
it appears.

**Tone:** plainspoken, practical, confident, grounded. Same voice as
the existing auditor stories and the audit-trail-comparison closing.
The reader is a tired professional reading on a phone between
meetings — every sentence respects that.

**Callout analogies pair with every hard concept.** Merkle trees, HMAC
chains, HSM signatures, structural-only versus full verification —
each gets a callout box anchoring the concept in a concrete picture
(the notary's bound ledger, the wax seal, the magnifying glass, the
master ribbon). One analogy per major section is the cap.

**CUPID/DRY surfacing:** every design choice that's shaped by CUPID
or DRY discipline gets one sentence naming the principle. Examples:

- "The verifier's offline posture is one example of CUPID's
  *Predictable* property — same ledger plus same public key produces
  the same verdict on a coffee shop's wifi as it does in the bank's
  data centre."
- "The four-code §10.12 contract is what saves the verdict surface
  from combinatorial blow-up across additional verifications — a
  textbook DRY discipline, and the integrator's 0-vs-non-zero
  contract is preserved as new spec sections land."

The reader learns the vocabulary from the prose. No lecturing.

**What the guide does NOT do:**

- Does not duplicate the §7 verification procedure normative text.
  It explains what the procedure does in plain English; the spec is
  the normative source.
- Does not duplicate `runbook-verifier.md`. The runbook is the
  operator deep-dive; this guide is the front door.
- Does not duplicate `examiner-quickstart.md`. The quickstart is a
  5-minute orientation for examiners who have never run the
  verifier; this guide is the longer "I want to understand what's
  going on" reference.
- Does not narrate any cryptographic algorithm implementation
  details. The verifier handles all that; the reader reads the
  verdict.
- Does not pretend the .NET / Python / Go implementations are byte-
  identical. Where they differ, the guide names the difference.

## Outline

The guide is structured as a Diátaxis **explanation + reference**
hybrid. It is not a tutorial (the quickstart fills that slot) and
not a how-to (the runbook fills that slot).

| § | Section | Type | Phase |
|---|---|---|---|
| 1 | What the verifier is | Explanation | Phase 1 (drafted below) |
| 2 | What the verifier proves (and what it does not) | Explanation | Phase 2 |
| 3 | The four primitives in plain English | Explanation + Reference | Phase 2 |
| 4 | Choosing an implementation | Reference | Phase 3 |
| 5 | Invoking the verifier | Reference | Phase 3 |
| 6 | Reading the verdict | Reference | Phase 2 |
| 7 | When verification fails | Explanation + Reference | Phase 3 |
| 8 | The bundle and re-verification | Explanation | Phase 4 |
| 9 | Version policy and additional verifications | Reference | Phase 4 |
| 10 | Where to go next | Navigation | Phase 4 |

One-sentence descriptions per section:

1. **What the verifier is.** A standalone offline binary that
   reads a chain file plus a verifier config and produces a verdict.
2. **What the verifier proves.** Integrity (the record was not
   tampered with) — not correctness (whether the AI's underlying
   decision was right).
3. **The four primitives.** Plain-English walkthrough of HMAC chain,
   Merkle root, HSM-rooted root signature, OpenTelemetry-native wire.
4. **Choosing an implementation.** The Go reference for examiner
   laptops and air-gapped deployments; Herald.Compliance (.NET) for
   in-process verification inside Herald pipelines; Visus (Python)
   for Python-based Herald consumers.
5. **Invoking the verifier.** The implementation-neutral flag catalog
   plus per-impl invocation examples.
6. **Reading the verdict.** The Status / Step / Reason / Verdict-Object
   surface; the §10.12 exit codes; the `additional_verifications`
   array.
7. **When verification fails.** The failure-mode catalog mapped to
   examination response actions; severity calibration; the path from
   a failure record to a documented response.
8. **The bundle and re-verification.** What's in the bundle, who can
   re-run it, how the bundle is the working-paper artifact.
9. **Version policy.** How the §10.12 enumeration evolves; how
   examiners handle verifier-version skew; the "obtain newer
   verifier" path.
10. **Where to go next.** Pointers to the quickstart, the runbook,
    the auditor stories, the spec, the regulator pack.

## Diagram inventory (for Tom)

Tom is working the visual side in parallel. The diagrams the guide
needs, with scope, level (per Heather's diagram-discipline section in
her agent definition), and target section:

| # | Title | Level | Target § | Scope |
|---|---|---|---|---|
| D1 | What the verifier is — the input/output story | SVG | §1 | Three-panel SVG: inputs (ledger + public key + optional IKM) flow into the verifier (the binary in the middle), out come the verdict (Status/Step/Reason) and optional bundle. Reference style: herald-website architecture q-svgs. Color: blue Herald path, green terminal verdict, yellow for the optional IKM path. |
| D2 | Integrity vs correctness — what the verifier proves | SVG | §2 | Two-panel comparison: left panel "what the chain proves" (integrity boundary in blue around capture-to-verify), right panel "what stays outside" (the AI's underlying decision quality in grey, with a dashed boundary). Anchors the §1.2 epistemic-scope distinction visually. |
| D3 | The notary's bound ledger | SVG | §3 intro | Single hero illustration borrowed from the verifier README's analogy: a bound book on a desk, a wax seal across the day's pages, a magnifying glass over one page. This is the anchor analogy the four primitive walk-throughs return to. |
| D4 | HMAC chain linkage | Mermaid (or SVG if Tom prefers) | §3.1 | Sequence/flow showing three chain entries with prev_hash arrows; one entry tampered, showing how the next entry's prev_hash mismatch cascades. |
| D5 | Merkle root construction | Mermaid | §3.2 | RFC 6962 tree with 4 leaves, showing the 0x00/0x01 domain-separation prefixes at one leaf and one internal node. Single-byte tamper on a leaf flips the root. |
| D6 | HSM-rooted root signature | SVG | §3.3 | The "signet pattern published on the wall" analogy: HSM as a safe, private key inside, public key fingerprint posted publicly, verifier comparing the seal's signet against the published fingerprint. |
| D7 | Structural-only vs full verification | SVG | §3.4 | Side-by-side: structural (3 checks running, MAC pass marked "skipped") versus full (4 checks running, all green). Same visual frame, only the MAC pass differs. Reinforces the load-bearing distinction. |
| D8 | The verdict-reading decision tree | SVG | §6 | Decision-tree SVG: exit code 0 → "what additional_verifications carries"; exit code 1 → "which step fired, what to do"; exit code 2 → "deployment / artifact problem"; exit code 3 → "invocation defect, fix the command". Color: green PASS path, red FAIL path, yellow structural-error, orange config-error. |
| D9 | The bundle as working-paper | SVG | §8 | The bundle's contents (report.pdf, report.json, verifier.sha256, ledger.sha256, public_key.pem, metadata.json) as a labeled package; an arrow from "Examiner A produces" to "Examiner B re-runs"; the institution out of frame, emphasizing bundle sufficiency. |

**Diagram cadence per the agent guidelines:** 9 diagrams across 10
sections is on the higher end, but the guide is dense regulatory
material aimed at non-engineer readers — every primitive needs an
anchor. Tom can downgrade D4/D5 to inline Mermaid (cheaper) and
focus polish budget on D1, D2, D3, D7, D8 (the load-bearing visual
arguments). The diagram source style is the herald-website
architecture q-svg vocabulary (Cascadia Code monospace, blue/red/
green/yellow color semantics, 75 px tall rounded rectangles,
context-stroke arrowheads).

**Where Tom delivers:** `diagrams/compliance/verifier-users-guide/`
in this repo. File-naming convention: `D<#>-<descriptive-slug>.svg`
or `.mmd`. Each diagram source carries a leading comment block with
its target section and scope (one sentence) so a future reader can
trace which diagram lives where.

## Sequencing

**Phase 1 (this dispatch).** Plan + manifesto + outline + diagram
inventory + section 1 drafted. Lands today.

**Phase 2.** Sections 2, 3, 6 drafted. These are the conceptual core:
what the verifier proves, what each primitive checks, how to read the
verdict. The `exit-codes.json`, `output-fields.json`, and
`additional-verifications.json` structured records land in Phase 2
because §6 renders from them.

**Phase 3.** Sections 4, 5, 7 drafted. These are the operator-facing
reference material: which implementation to choose, how to invoke,
what to do when it fails. The `cli-flags.json` and
`failure-modes.json` records land in Phase 3.

**Phase 4.** Sections 8, 9, 10 drafted. These are the bundle /
version-policy / navigation pages. Phase 4 also stands up the render
script that produces `ffiec/docs/verifier-users-guide.md` and (with
Dawn) the website mirror.

Each phase lands one PR-ready commit set. Steve reviews in place;
Jared reviews where the guide describes the Go implementation's
shape; Richard reviews if spec ambiguities surface.

## Open coordination

- **Tom.** Diagram inventory is the work list. Cross-consult Laura
  on visual register if uncertain — golden-age sci-fi is the
  MMPWorks default but the verifier guide is sober regulatory
  documentation; the herald-website architecture-page SVG vocabulary
  is the right anchor.
- **Jared.** Section 5 (invocation) draws on the Go reference's flag
  surface. The current `ffiec/verifier/README.md` is the source of
  truth for the Go side until Commit 1 lands. The repository path
  and any name-bearing prose will land cleanly once Steve picks the
  Go product name (Pearl's round-1 collision rejection paused the
  pick 2026-05-21). Heather will read the Commit 1 surface when it
  ships and update the prose if anything diverges from the README.
- **Richard.** Any spec ambiguity Heather encounters surfaces to
  Richard via the standard architecture-designer dispatch, with a
  note that the disposition feeds PRD-3 amendments.
- **Dawn.** Phase 4 includes the website-mirror render. Dawn places
  copy on the website; Heather produces the canonical material.
  Heather does not push to herald-website.
