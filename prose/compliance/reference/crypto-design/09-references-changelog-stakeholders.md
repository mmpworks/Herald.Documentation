# Plain-English: §11–§13 + Appendix A — references, change log, stakeholders, schema reference

The closing material. Reference standards, the spec's evolution history, role-by-role reading paths, and a consolidated schema reference.

---

## §11 References

**What.** Two lists.

**Normative references** — standards the spec depends on for cryptographic constructions and wire format:
- RFC 2119 / RFC 8174 — conformance keywords (MUST / SHOULD / MAY)
- RFC 6962 — Certificate Transparency Merkle tree (the §4.2 daily seal substrate)
- RFC 8785 — JCS (the canonicalization for hash inputs)
- RFC 5869 — HKDF (the §4.1 session-key derivation)
- RFC 2104 — HMAC
- RFC 4868 — HMAC-SHA-256 keying recommendations (32-byte key minimum drives FFIEC chain-of-custody spec §10.6's IKM minimum)
- RFC 3339 — date and time formatting
- FIPS 140-2 / FIPS 140-3 — HSM protection levels
- FIPS 180-4 — SHA-2 family
- FIPS 186-5 — Ed25519
- FIPS 198-1 — HMAC
- OpenTelemetry Specification, OTLP, GenAI Semantic Conventions
- RFC 9101 — Legal Entity Identifier (LEI), per ISO 17442

**Reference verifier (per §10.26).** The reference verifier ships under Apache 2.0 in a separate repository. Pinned reference-verifier version for spec v1.0b is the `v1.0b-verifier` release tag, Cosign-signed, reproducible build, per-platform binaries with SHA-256/SHA-512 manifests and CycloneDX SBOM.

**Cryptographic-agility roadmap (GAP-6 closure).** `docs/cryptographic-agility-roadmap.md` is normative-when-applicable per §10.53 — institutions in long-retention regimes MUST track NIST PQC migration timelines, dual-algorithm transition windows, algorithm-retirement procedures.

**Informative references:**
- FFIEC IT Examination Handbook — Information Security booklet (Sept 2016)
- FFIEC IT Examination Handbook — Architecture, Infrastructure, and Operations booklet (June 2021)
- Federal Reserve SR 11-7 — Model Risk Management (2011)
- OCC Bulletin 2011-12 — Sound Practices for Model Risk Management
- **OCC Bulletin 2026-13** — Joint OCC / Federal Reserve / FDIC update to model-risk-management guidance (the consolidated 2026 update of SR 11-7 and OCC 2011-12); counterpart Federal Reserve / FDIC issuances tracked alongside as those agencies publish
- U.S. Treasury Financial Services AI Risk Management Framework (Feb 2026)

---

## §12 Change log

**What.** Every spec amendment recorded with date + scope. The change log is verbose by design — a clean-room implementer reading the spec at a moment in time can reconstruct what changed when.

**Key entries:**
- **v1.0-draft** (2026-05-06) — initial draft. Four primitives defined. Wire format normative.
- **v1.0-rework** (2026-05-06, same day) — substantive in-place rework anchored on the Herald HMAC-SHA-256 + HKDF audit-chain construction. Resolved through three Auditor rounds.
- **v1.0-final** (2026-05-15) — polished form after subsequent reviewer rounds. Added §4.1.1 session-key handshake security floor, §4.2.1 cadence, §4.3.1 HSM unavailability, §4.3.2 algorithm rotation + quantum-readiness, §10 operational requirements, §13 stakeholder navigation.
- **v1.0-final-amendment** (2026-05-07) — same-day close-out of three reviewer waves plus user-directed scope additions. Locked canonical wire form: 10-line `sign_payload` with `sign_payload_version = "v1.0a"`. Wave-1 / Wave-2 / Wave-3 / Wave-4 / Wave-5 / Wave-6 close-outs all in this row.
- **v1.0b** (2026-05-07) — cryptographic close-out (NIST cryptographic reviewer). Wire-form extension #3: `sign_payload` extended from 10-line v1.0a to 12-line v1.0b binding `key_versions_canon` and `hex(kms_handle_uris_digest)`. Closes (`kms_handle_uri` provenance-only at v1.0a) and (`key_versions` cross-checked but not signed at v1.0a).

**Pattern.** Each row records what changed, why (which round, which reviewer), and what test-vector regeneration was required. The change log is the audit trail for the spec text itself.

---

## §13 Stakeholder navigation

**What.** Role-by-role reading paths plus pointers to companion docs. The chain-of-custody documentation corpus is comprehensive (50+ documents); §13 tells each reader where to start.

**Stakeholder rows:**

| Stakeholder | Time | Sections to read | Companion doc |
|---|---|---|---|
| **Bank executive (CEO)** | 5-10 min | §0.5.4 + §1 | `docs/management-summary.md` |
| **Bank Audit Committee chair** | 30 min | §0.5.4 + §1 + §10.13 + §10.14 | `docs/audit-committee-summary.md` |
| **Bank MRM committee chair** | 45 min | §1.2 + §10.20 + §10.33 + §10.34 + §10.37 | `docs/MRM-COMMITTEE-BRIEF.md` |
| **Bank chain-operations team** | 90 min | §4 + §6 + §7 + §10 | `docs/operator-guide.md` |
| **Bank chain adopter** | 60 min | §0.5.4 + §1 + §10.1-§10.18 | `docs/first-engagement-guide.md` |
| **Bank vendor-management team** | 60 min | §10.21 + §10.39 + §10.40 + §10.21.2 | `docs/vendor-hosted-controls.md` |
| **Bank privacy / GDPR team** | 60 min | §10.22 + §10.23 + §10.38 | `docs/privacy-by-design.md` |
| **Bank Legal / IR team** | 90 min | §1.1 + §1.2 + §10.13 + §10.14 + §10.24 + §10.42 | `docs/litigation-support.md` |
| **Internal audit team** | 90 min | §7 + §10 + audit-procedures | `docs/audit-procedures.md` |
| **SOC 1 / SOC 2 engagement team** | 90 min | §10 + control-map | `docs/soc-pack/` |
| **FFIEC IT Examiner** | 45 min | §1, §1.1, §4, §7, §10.12 | `docs/regulator-pack/fdic-occ-examination-overlay.md` |
| **FFIEC Cybersecurity Specialist Examiner** | 45 min | §4 + §10 + threat model | `docs/regulator-pack/dora-articulation-overlay.md` |
| **FFIEC Examiner-in-Charge (EIC)** | 30 min | §0.5.4 + §1 + §10 | `docs/regulator-pack/fdic-occ-examination-overlay.md` |
| **FFIEC consumer-protection / CFPB examiner** | 60 min | §10.11 + §10.11.1 + §10.11.2 + §10.22 + §10.23 + §10.69 | `docs/regulator-pack/cfpb-overlay.md` |
| **State insurance department market-conduct examiner** | 60 min | §10.11 + §10.43-§10.46 + §4.4.5 | regulator pack |
| **Acquirer-side IT due-diligence** | 90 min | §10.21 + §10.24 + §10.39 + §10.40 + §10.41 + §10.42 | `docs/m-and-a-handoff.md` |
| **Cryptographic expert (witness, advisory)** | 2+ hours | §1.3 + §1.4 + §4 + §5 + §7 + §10.6 + §10.6.1 + §10.7 + §10.8 + §10.53 | `docs/cryptographic-agility-roadmap.md` |
| **Implementer (SDK, ledger, verifier)** | 4+ hours | full spec + test vectors + design docs | `docs/design/` |

**Why this exists.** Different audiences need different entry points. §13 is the wayfinder.

---

## Appendix A — Consolidated chain envelope schema reference (informative)

**What.** A single-page schema lookup across every `ffiec.chain.*`, `audit.*`, `service.*`, `chain.*`, `seal.*`, `consumer_index.*`, `gen_ai.*`, `tool.*`, and `herald.*` attribute defined throughout the spec. Useful for an implementer who needs the full attribute roster in one place rather than scattered across §4, §10, and the regulator pack.

**Sub-sections (A.1 through A.17):** chain envelope, OTel GenAI envelope, audit-routing family, cross-border transfer family, deployment-intent family, underwriting-feature family, disparate-impact family, connector-source family, ECOA/FCRA families, redaction family, consumer-correlation index, entity succession, HSM partition ceremony, external artifact + model handover, service identity + posture, vendor-namespaced attributes, reading order.

**Why this exists.** The schema is dispersed across many sections by design (each attribute family lives next to its semantic context). The appendix consolidates for fast lookup. A clean-room implementer building an OTLP wire encoder reads Appendix A; a spec-text reader doesn't usually need it.

---

## What §11–§13 + Appendix A buys you

The closing material is the wayfinding layer. References tell you what standards the spec depends on and where the reference verifier lives. The change log tells you what's been amended and why. Stakeholder navigation tells each reader where to start. The schema appendix consolidates attribute lookup for implementers.

A reader who finishes this published walkthrough has covered the
ratified crypto design end to end:
- §0–§3 — orientation, scope, definitions (`01-scope-and-overview.md`)
- §4 — the four primitives (`02-the-four-primitives.md`)
- §5–§7 — wire, storage, verification (`03-wire-storage-verification.md`)
- §8–§9 — conformance + security (`04-conformance-and-security.md`)
- §10.1–§10.18 — operational foundational (`05-operational-foundational.md`)
- §11–§13 + Appendix A — references, change log, stakeholders, schema reference (this file)

The §10.19 and later operational waves — chain-coverage, M&A and
run-resume, edge attestation, GenAI disclosure, the hardware and
frontier-AI extensions — are situational, candidate-normative
forward-design. They are tracked separately and are not part of this
published surface.

That's the ratified spec, in plain English. The official spec is the
authority — these notes are the onramp.
