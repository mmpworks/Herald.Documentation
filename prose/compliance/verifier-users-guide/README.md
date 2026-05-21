---
title: TesseraSeal Verifier User's Guide — index
slug: verifier-users-guide-index
surface: compliance
category: verifier-users-guide
audience: auditor-or-it-operator
version: 2026-05-21
last-reviewed: 2026-05-21
status: phase-1-in-progress
---

# TesseraSeal Verifier User's Guide

The user's guide for the TesseraSeal Verifier. Implementation-agnostic
across the three references: Verus (Go), Herald.Compliance (.NET), and
Visus (Python). All three produce the same verdict surface against the
same chain format. The reader audience is auditors, IT operators, and
compliance officers; engineers setting up the verifier in their
pipelines are the secondary audience.

Companion content:

- `ffiec/docs/examiner-quickstart.md` — 5-minute orientation for
  examiners who have never run the verifier
- `ffiec/docs/runbook-verus.md` — operator-mechanic deep-dive
  runbook for Verus (Jared, Commit 6)
- `ffiec/docs/auditor-stories/` — plain-spoken narrative companions
  showing the verifier in actual engagements
- `ffiec-public/spec/chain-of-custody-DRAFT-0.2.0.md` — normative
  specification (§7 verification procedure, §10.12 exit-code
  contract)

## Sections

| § | Title | Status |
|---|---|---|
| 1 | What the verifier is | **Drafted** |
| 2 | What the verifier proves (and what it does not) | Phase 2 |
| 3 | The four primitives in plain English | Phase 2 |
| 4 | Choosing an implementation | Phase 3 |
| 5 | Invoking the verifier | Phase 3 |
| 6 | Reading the verdict | Phase 2 |
| 7 | When verification fails | Phase 3 |
| 8 | The bundle and re-verification | Phase 4 |
| 9 | Version policy and additional verifications | Phase 4 |
| 10 | Where to go next | Phase 4 |

## How the guide is built

This is one example of the Herald.Documentation docs-as-database
discipline. The narrative sections live here as markdown with
frontmatter. The catalog-shaped material (exit codes, output fields,
CLI flags, failure modes, additional-verifications enumeration) lives
in `data/compliance/verifier-users-guide/` as structured records that
the renderer assembles into reference tables. One edit per fact;
multiple consumer surfaces stay in sync.

The plan, audience-and-voice manifesto, diagram inventory, and
sequencing live in
`documentation-guidance/compliance/verifier-users-guide-plan.md`.
