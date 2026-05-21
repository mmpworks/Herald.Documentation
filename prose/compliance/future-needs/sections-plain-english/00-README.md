# Plain-English spec walkthrough

> **What this is.** A working set of plain-English explanations of the chain-of-custody spec, section by section. The official spec is the authoritative document; these files exist to help readers (implementers, examiners, MRM committee members, executives, lawyers) build mental models of what each section does and why.
>
> **Status.** Forward-looking working notes; lives in `docs/future-needs/` (gitignored). Not part of the published artifact set.
>
> **Convention.** Each file covers one or more spec sections. For each section: (1) what the section says in everyday terms, (2) why it exists / what problem it solves, (3) common reader questions, (4) edge cases / gotchas. The aim is a reader can come to the official spec text already knowing the shape of what they're about to read.

## Files

| File | Spec coverage |
|---|---|
| [01-scope-and-overview.md](01-scope-and-overview.md) | §0 (version policy, how to read), §1 (scope), §2 (out of scope), §3 (definitions) |
| [02-the-four-primitives.md](02-the-four-primitives.md) | §4 (the four primitives) — HMAC chain, daily Merkle seal, HSM-rooted root signature, OpenTelemetry-native wire |
| [03-wire-storage-verification.md](03-wire-storage-verification.md) | §5 (wire format), §6 (storage), §7 (verification procedure) |
| [04-conformance-and-security.md](04-conformance-and-security.md) | §8 (test vectors), §9 (security considerations) |
| [05-operational-foundational.md](05-operational-foundational.md) | §10.1–§10.18 (key fingerprints, operational events, append-only, time, HSM, IKM, software-key adapter, constant-time, IKM registry retention, rotation crossing seal boundaries, ECOA/FCRA translation, verifier exit codes, evidentiary artifacts, trusted-time, multi-region, SaaS-edge, partition ceremony, CC8.1 cross-referencing) |
| [06-operational-md-and-resilience.md](06-operational-md-and-resilience.md) | §10.19–§10.30 (chain coverage map, training-data retention, cross-vendor handover, redaction discipline, consumer-correlation index, entity succession, run resume, reference verifier, configurable cadence, streaming mode, IKM rotation, trusted time for streaming) |
| [07-operational-disclosure-and-ai.md](07-operational-disclosure-and-ai.md) | §10.31–§10.55 (cohort subtree disclosure, per-device keys, model updates, training-phase, edge attestation, late arrival, hierarchical Merkle, consent, succession, cross-vendor merge, M&A temporal slice, backfill seal, claims, cessions, adjusters, bordereau, GenAI generation, stochasticity, retrieval, output grounding, public transparency, model card, post-quantum, decadal re-sealing, challenge-response) |
| [08-operational-prd4-wave.md](08-operational-prd4-wave.md) | §10.56–§10.71 (hardware bill of materials, firmware attestation, component cryptographic identity, RMA, anti-counterfeit, CMMC, red/black separation, training corpus, training run, fleet attestation, model-weight lineage, evaluation chain, AISI overlay, customer disclosure, BSA SAR, cross-institution Fedwire/ACH) |
| [09-references-changelog-stakeholders.md](09-references-changelog-stakeholders.md) | §11, §12, §13, Appendix A |

## Reading paths

- **First-time spec reader**: 01 → 02 → 03 → 04. That gives you the mental model. §10 sections you can read on demand once you know what the four primitives are.
- **Implementer**: 02 → 03 → 04 → §10.x sections relevant to the features you're implementing.
- **Examiner / auditor**: 01 → 02 → 04 (security model) → §13 stakeholder navigation in the official spec → relevant §10.x.
- **MRM committee / risk / compliance**: 01 → §1.1 + §1.2 in the official spec (Daubert + epistemic scope) → relevant §10.x for AI-specific concerns (§10.34, §10.47–§10.50, §10.66).
- **Lawyer / litigation support**: 01 → §1.1 + §1.2 + §10.13 + §10.14 + §10.24 + §10.42 + the litigation-support docs.

## How to use these notes

These files are *informative companions* to the spec, not the spec itself. When the spec text and a plain-English explanation diverge, the spec wins. The plain-English layer exists to make the spec less intimidating, not to compete with it.

Spec line numbers can shift as the spec is amended. Plain-English explanations cite section numbers and section names rather than line numbers.
