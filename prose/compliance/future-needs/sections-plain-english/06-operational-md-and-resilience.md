# Plain-English: §10.19–§10.30 — chain coverage, M&A continuity, run resume, streaming

This cluster covers the operational requirements that span chain-coverage governance, model-handover, redaction, consumer-correlation, M&A continuity, run resume, reference-verifier distribution, configurable cadence, and streaming-mode operations.

---

## §10.19 Chain-coverage boundary documentation (normative)

**What.** The institution's CC8.1 names a *chain-coverage map* — five categories: chain-instrumented institutional, institutional-not-yet-instrumented, third-party-under-contractual-inspection, third-party-out-of-reach, external-evidentiary-artifacts-hash-anchored. Plus the `audit.external_artifact.*` family for binding hashes of artifacts the chain reaches by reference (CES inspection notices, broker case-management snapshots, factory access-log extracts).

**Why.** "What does the chain cover?" is the first question every examiner asks. §10.19 normates a written answer.

## §10.20 Training-data retention vs deployment-window discipline (normative)

**What.** Training-data shard retention MUST be at least as long as the longest active deployment window of any model trained on the data, plus a 60-90-day investigation buffer. GDPR Article 5(1)(c) data-minimization tension is resolved through Article 6(1)(f) legitimate-interests determination tied to EU AI Act Article 12 logging obligations.

**Why.** Without this floor, a model deployed for 18 months whose training shards retained for only 90 days has unreproducible decisions in the back half of its deployment.

## §10.21 Cross-vendor model-handover schema (normative when applicable) — *substantive*

**What.** When a model is delivered from one party to another (vendor → deployer; in-house ML platform → business unit), the deployer's chain MUST include a model-handover entry binding the delivered artifact to the provider's chain.

**Schema (`audit.model_handover.*`):**
- `provider`, `model_id`, `model_version` — basic identification
- `model_artifact_sha256` — SHA-256 of the canonicalized model artifact
- `model_card_sha256` — SHA-256 of the model card
- `fairness_audit_report_sha256` — required for high-risk AI under EU AI Act
- `audit_report_languages` — array of language codes (multilingual reports common when crossing jurisdictions)
- `provider_chain_entry_id` — cross-reference to provider's chain
- `training_data_retention_floor_days` — provider's commitment per §10.20
- `training_shard_manifest_sha256` —: hash of provider's canonical shard list (lets post-close auditor recompute manifest)
- `contract_id` / `contract_version` / `contract_hash_sha256` —: bind which contract version governed each delivery
- `contract_status` — (added 2026-05-09): closed-enum discriminator (`external_contract_bound` / `internal_no_external_contract` / institution-named) integrity-binding the absence of contract attributes

### §10.21.1 Sample-based-attestation cross-anchor pattern

For destructive/sample-based testing (AS6171, DARPA SHIELD, lot-acceptance). Schema additions: `lot_identifier`, `sample_size`, `lot_population`, `sample_disposition` enum, `attestation_authority`. Verifier marker: `'sample_based_attestation_via_lot_verified'`.

### §10.21.2 Independent-evaluator parallel-chain composition

Multiple independent parties evaluate the same subject (cedent + reinsurer; lab + AISI; institution + third-party adjuster; institutional clinical chain + Cleveland Clinic observer). Schema additions: `evaluator_identity`, `evaluator_role` (enum), `target_anchor_chain_entry_id`, `evaluator_chain_entry_id`, `cardinality` (REQUIRED — integer or `"dynamic"` per close-out). Verifier marker: `'parallel_evaluator_anchor_verified'`. Plus failure-path normation (target unresolved, hash-binding mismatch).

### §10.21.3 Registry-discovery pattern for cross-institution cross-anchors

Cross-anchors mediated by a third-party registry (Federal Reserve Fedwire/ACH registry, SWIFT, FedNow, FINRA, CCP, credit bureau). Schema additions: `registry_identity`, `registry_publication_id`, `registry_publication_at_utc`, `counterpart_institution`, `cross_anchor_state` enum (`published-pending-counterpart` / `bound` / `unbound`). Verifier markers: `'registry_cross_anchor_verified'` (bound), `'cross_anchor_unbound'` (unbound).

## §10.22 Redaction discipline (normative)

**What.** Redaction MUST happen pre-MAC at the SDK boundary. A chain entry's canonical bytes (which the per-event MAC covers) are the redacted content. Post-MAC sidecar redaction is non-conformant unless the sidecar is itself a separate chain pointing to a parent unredacted chain via cross-anchor.

**`audit.redaction.*` family:** `policy_id`, `policy_version`, `redacted_field_paths` (JSONPath array), `redaction_method` (closed enum: `sha256_hash` / `deterministic_token` / `length_preserving_pad` / `static_replacement` / `format_preserving_encryption` or institution-named), `disposition`.

**Why.** Without redaction posture normation, an examiner can't tell whether the institution redacted at the SDK boundary (the `redacted` form is what the chain proves was captured) or post-hoc on a sidecar (the chain doesn't bind the sidecar).

## §10.23 Consumer-correlation index integrity (normative)

**What.** Two acceptable shapes for the institution's consumer-correlation index (CUEC). Shape 1: chain-anchored index where each CUEC entry is a chain entry under `chain_kind = "operational"`. Shape 2: daily `consumer_index.attestation` operational event carrying snapshot hash + consumer count + period.

**Why.** A CFPB Civil Investigative Demand asks for "all adverse-action decisions for consumers in [ZIP X] during Q1 2026." Without integrity-bound CUEC, the institution could regenerate the index at production time and quietly omit consumers it would rather not surface. Shape 1 makes omission cryptographically detectable; Shape 2 makes it detectable at sample-comparison time.

## §10.24 Entity succession (normative)

**What.** When the legal entity changes (merger, acquisition, divestiture, rename, subsidiary transfer), the chain emits `chain.entity_succession` with `from_entity_legal_name`, `to_entity_legal_name`, optional LEI fields per RFC 9101, `effective_utc`, `kind` enum, REQUIRED `dual_signatures` (from-entity + to-entity authorized signers).

**Why.** Without this, an acquirer's post-close chain has a discontinuity at the legal-entity boundary that no single signature could span. Dual signatures bind both sides' acceptance of the integrity claim.

## §10.25 Run resume and chain-tail acquisition (normative)

**What.** SDK restart discipline for picking up an in-flight run without breaking the chain. Three-place tail lookup: in-memory state, local persistence sidecar, ledger query rejoin path. Single-writer-per-run rule enforced through file or row locks. Ledger ingestion cross-checks `(prev_hash, seq)` monotonicity. Genesis-form anti-spoof (a `prev_hash = 32 zero bytes` at `seq > 1` is a tampering signal). DR rejoin discipline refuses-to-emit when both local persistence and ledger reachability are lost.

**Why.** Without run-resume discipline, a process crash can cause silent fork attacks (an attacker silently begins a new chain at `seq = 1` for a run that already exists).

## §10.26 Reference verifier distribution (normative)

**What.** The reference verifier ships in a separate repository under Apache 2.0. Reproducible builds, Cosign-signed release artifacts, per-platform binaries, SHA-256/SHA-512 manifests, CycloneDX SBOM. Spec-version pinning: the reference-verifier release tag for spec v1.0b is `v1.0b-verifier`. Institutions cite the verifier in CC8.1 by implementation name + version + verification key.

**Why.** "Which verifier did the examiner use?" is a load-bearing question. Without pinned reference-verifier discipline, the answer drifts.

## §10.27 Configurable seal cadence (normative)

**What.** Default cadence is daily. Hourly and weekly are conformant. The seal record carries `cadence` in its `sign_payload` (signed under HSM since v1.0a).

**Why.** A 1-second-decision-rate trading desk needs hourly seals to bound the per-seal event count. A low-volume long-retention institution can use weekly. The cadence flexibility composes with §10.28 streaming-mode IKM rotation.

## §10.28 Streaming-mode IKM rotation discipline (normative)

**What.** Sub-second rotation crossing semantics. The streaming verifier observes a rotation event and transitions through `STREAMING_KEY_ROTATION_PENDING_CONFIRMATION` (exit code 6) until the next seal under the new key validates.

## §10.29 Streaming-mode verifier procedure (normative)

**What.** A continuous verifier walking a chain stream incrementally rather than file-by-file. Three streaming-state exit codes:
- `4` STREAMING_ALL_PASS_SO_FAR
- `5` STREAMING_ANOMALY_DETECTED
- `6` STREAMING_KEY_ROTATION_PENDING_CONFIRMATION

These are non-terminal states. Terminal states (PASS / FAIL) come at end-of-stream. The §10.12 `additional_verifications` discipline is unchanged; codes 4-6 signal state, not bonus verifications.

## §10.30 Trusted-time integration normative for streaming-mode (normative)

**What.** Streaming-mode chains DETECT clock drift at 100ms thresholds via `clock.drift_detected` events. The §10.30 byte form composes with §10.28 rotation events.

---

## What §10.19–§10.30 buys you

The cluster gives you operational discipline that a real institution actually uses day-to-day: documented chain coverage; cross-vendor handover with contract binding; redaction discipline; consumer-correlation integrity; M&A entity succession; run resume + fork prevention; pinned reference verifier; configurable cadence + streaming-mode primitives.

Most of these compose with §10.31+ extensions — institutional clinical chains compose with §10.50 output-grounding; multi-vendor handover composes with §10.45 adjuster anchors; M&A entity succession composes with §10.39 successor attestation and §10.42 backfill seal.
