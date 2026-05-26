---
kind: reference
sourced_from: E:\dev\MMP.Media\_assistant_drafts\wiki\market-research\2026-05-20-kognitos-12-field-audit-schema.md
---

# Kognitos's 12-field AI audit-trail schema — the audit team's working checklist

The audit team in this novel carries this checklist into every engagement room. They have no other framework. Their note-taking, finding taxonomy, and report structure all key off these twelve fields.

1. **Timestamp (NTP-synced, UTC).** Monotonic, NTP-synchronized timestamp in UTC, recorded at the moment the AI-influenced event occurred. Millisecond resolution expected. Anchored by EU AI Act Article 12(3)(a) for biometric ID, implied for general high-risk AI.
2. **Unique decision ID.** Globally-unique identifier (UUID or equivalent) threading through every downstream system the decision touches. Engineering implementation of EU AI Act Article 12(2) reconstruction-of-events.
3. **Authenticated human user identity (not just service account).** The verified SSO-authenticated user whose session triggered the work. Dual attribution required: log both the AI system identity and the authenticated human. HIPAA § 164.312(a)(2)(i) is the cleanest anchor.
4. **AI system identity and version.** Which AI platform made the decision, and its specific version at the time. COSO 2026 / EU AI Act Article 12 traceability.
5. **Model identity and version.** The specific model AND specific version. "GPT-4" is insufficient; "gpt-4-turbo-2024-04-09" is. Self-hosted: model weights hash. Fine-tuned: fine-tuning checkpoint identifier.
6. **Inputs received (with source attribution).** The data the AI acted on, plus where each piece came from. Source attribution is load-bearing. EU AI Act Article 12(3)(b) for biometric; SOX end-to-end transaction traceability.
7. **Specific policy, rule, or prompt invoked.** The exact decision logic that fired — policy text, rule definition, or prompt template with interpolated values. Version-controlled and inspectable. COSO 2026 explicit logging building block.
8. **Reasoning expressed in human-readable language.** Plain-language explanation of what factors drove the decision. Confidence scores ("94% confident") are NOT acceptable substitutes. GDPR Article 22(3), EU AI Act Article 86 (right to explanation), ECOA / Regulation B, CFPB Circular 2023-03.
9. **Output produced.** What the AI actually returned, verbatim. The exact text, classification, score, action, or recommendation.
10. **Action taken in downstream systems.** What changed in the system-of-record as a result. With identifiers tying back to the decision ID (Field 2). SOX end-to-end transaction traceability; COSO 2026 "output validation and exception handling."
11. **Human review or approval (if applicable), with reviewer identity.** Reviewer identity, timestamp, disposition (approved / rejected / modified / escalated). Override path documentation for clinical AI. SOX, FDA AI/SaMD, FFIEC, COSO 2026 Step 3 (right-sized human involvement). EU AI Act Article 14(5).
12. **Tamper-evident integrity proof (cryptographic hash or equivalent).** A cryptographic proof — hash chain, Merkle tree, digital signature, or append-only / WORM storage equivalent — that log entries have not been altered. PCAOB AS 1105 (2024) is the direct anchor.

## Important things the framework does NOT specify

The audit team in this novel will discover these silences operationally:

- **No multi-implementation conformance bar.** Field 12 asks for "tamper-evident integrity proof," but does not require that proof be verifiable by an independent reference implementation, nor that multiple implementations produce byte-identical output under a test-vector corpus.
- **No day-boundary semantics.** Field 1 asks for timestamps, but doesn't address how late-arriving events relate to prior daily seals (i.e., no notion of `late_binding=true` declaration).
- **No severity-classification normativity.** Fields are listed; sufficiency is unspecified. The team has no normative basis to refuse downgrading a finding.
- **No three-layer compositional security argument.** Field 12 covers integrity but doesn't require independent owning teams for the writer, the ingestion path, and the verifier.
- **No connector-source attribution family.** Field 6 asks for "inputs with source attribution" but doesn't enumerate the required attributes for SaaS-edge connectors (replay_id, commit_timestamp, lag_observed_ms, etc.).
- **No quantified-lag-bound requirement.** Field 1 asks for timestamps, but doesn't require institutions to publish median, 95th-percentile, alerting threshold, and RTO numbers for any connector. "Near real-time" wording would pass.
- **No prompt-store version-control discipline.** Field 7 says "version-controlled and inspectable" — but doesn't require the prompt store's hash to be bound under the audit trail's integrity proof.
- **No fork-detection responsibility for verifiers.** Field 12 covers integrity at the entry level but doesn't address duplicate (tenant_id, run_id) detection across files.
- **No Daubert / FRE 1001-1004 grounding.** Field 12 covers tamper-evidence but doesn't ground the framework in courtroom evidence rules.
- **No training-data retention floor.** No analogue to the deployment-window-plus-retention-horizon discipline.
- **No entity-succession discipline.** No analogue to how chain history transfers across M&A boundaries.

These silences are not Kognitos doing something wrong. They're the spaces a 12-row marketing checklist necessarily leaves between rows. The novel's job is to show what those silences feel like when an audit team is standing in them.
