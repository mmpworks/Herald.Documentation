---
title: Chain-of-custody crypto design — plain-English walkthrough
slug: compliance/reference/crypto-design
category: reference
audience: implementer, examiner, MRM-committee, legal, executive
reading-level: high-school (target = "spec less intimidating, not dumbed down")
status: published
last-reviewed: 2026-06-02
source-of-truth: E:\dev\ffiec-public\spec\chain-of-custody-DRAFT-0.2.0.md
citation-map: E:\dev\_oss-rollout-plan\ffiec-crypto-boundary-and-citation-map.md
---

# Chain-of-custody crypto design — plain-English walkthrough

The FFIEC chain-of-custody spec is the cryptographic heart of
TesseraSeal. This is a plain-English walkthrough of the **ratified
crypto design** — the four primitives, the wire format, the storage
rules, the verification procedure, and the operational floor every
institution needs.

The official spec is the authority. These pages exist to help a reader
build the mental model before they open the spec text. Every crypto
passage here carries an FFIEC `§ref` citation, so a reader can trace
each statement back to the section it explains.

> **What's here and what isn't.** This walkthrough covers the ratified,
> publish-safe crypto design. The forward-design extensions — the
> not-yet-ratified, candidate-normative spec waves — are tracked
> internally and are not part of this published surface. The line is
> simple: a passage that maps to a ratified, cited section ships here;
> candidate-normative material does not.

## The pages

| File | Spec coverage |
|---|---|
| [01-scope-and-overview.md](01-scope-and-overview.md) | §0–§3 — version policy, how to read, scope, definitions |
| [02-the-four-primitives.md](02-the-four-primitives.md) | §4 — HMAC chain, daily Merkle seal, HSM-rooted root signature, OpenTelemetry-native wire |
| [03-wire-storage-verification.md](03-wire-storage-verification.md) | §5 wire format, §6 storage, §7 verification procedure |
| [04-conformance-and-security.md](04-conformance-and-security.md) | §8 test vectors, §9 security considerations |
| [05-operational-foundational.md](05-operational-foundational.md) | §10.1–§10.18 — the operational floor (key custody, HSM, entropy, append-only, constant-time, multi-region) |
| [09-references-changelog-stakeholders.md](09-references-changelog-stakeholders.md) | §11–§13 + Appendix A — references, change log, stakeholder reading paths, schema reference |

## Reading paths

- **First-time spec reader**: 01 → 02 → 03 → 04. That gives you the
  mental model. The §10 operational sections you read on demand once
  you know the four primitives.
- **Implementer**: 02 → 03 → 04 → the §10.x sections your features
  touch.
- **Examiner / auditor**: 01 → 02 → 04 (security model) → the
  stakeholder navigation in 09 → the §10.x sections that matter to you.
- **Cryptographic reviewer**: 02 → 03 → 04 → §10.6/§10.7/§10.8 in 05.

## How to use these notes

These are informative companions to the spec, not the spec itself. When
the spec text and a plain-English explanation diverge, the spec wins.
The plain-English layer makes the spec less intimidating; it does not
compete with it.

Spec line numbers shift as the spec is amended. These pages cite
section numbers and section names, not line numbers.
