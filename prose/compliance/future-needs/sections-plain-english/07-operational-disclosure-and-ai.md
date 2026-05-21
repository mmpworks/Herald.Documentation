# Plain-English: §10.31–§10.55 — disclosure, edge attestation, training-phase, M&A continuity, GenAI

This cluster is where domain-specific extensions land — partial disclosure, per-device keys, training-phase integrity, edge attestation, late arrival, hierarchical Merkle, consent capture, M&A backfill, insurance bordereau, GenAI generation/grounding, post-quantum, decadal re-sealing, audit-target challenge-response.

---

## §10.31 Per-cohort subtree disclosure (normative)

**What.** RFC 6962 audit-path verification lets a verifier confirm a specific subset of chain entries against a signed Merkle root *without* accessing the full chain. Useful when only some cohort of entries (e.g., decisions about cardiology consults, decisions involving a specific consumer) needs to be disclosed.

**Witness-mode applicability** (per §7 table): both issuing-bank-side (institution's own disclosure key) and customer-side (per §10.69 disclosure key) are supported.

## §10.32 Per-device session-key derivation (normative when applicable)

**What.** Institutions whose chain extends to the device boundary (mobile tablets in field offices, federated-learning workers, point-of-sale terminals) derive per-device session keys: `info = HKDF_INFO_BASE || "|" || utf8(tenant_id) || "|" || utf8(device_id)`. Single-tenant-no-device institutions stay on §4.1's tenant-only base derivation.

**Why.** A chain entry under §10.32 has a session key no §4.1 verifier can re-derive without the device_id segment. The institution's CC8.1 names the device-identity scheme (UUID, MAC address, TPM identifier).

## §10.33 Model-update events (normative)

**What.** Schema for binding model-version transitions on the chain — institution updates its underwriting model from v1.4.2 to v1.4.3; a chain entry records the transition, the prior version, the new version, the activation timestamp.

## §10.34 Training-phase integrity (normative)

**What.** `audit.training.*` family for institutions operating training-phase-bearing AI: federated learning, in-house retraining, model-development pipelines. Training-data hash binding, gradient compute attestation, aggregation evidence, validation against held-out test sets, model-artifact production.

**Why.** Pre-PRD-4, training-phase integrity was institution-side-only (logs the SOC team consumed). §10.34 puts it on the chain.

## §10.35 Edge-attestation primitive (normative when applicable)

**What.** TEE-class attestation primitives (Android Keystore, Apple Secure Enclave, Intel SGX, ARM TrustZone) bound to chain entries. The chassis-level attestation document hashes onto the chain; the attestation chain validates against the platform-vendor's attestation root.

## §10.36 Late-arriving-entry seal discipline (normative)

**What.** Events captured but not delivered to the seal region before the day's seal closes are recorded with `ffiec.chain.late_binding = true` and included in the next day's seal. Original seal MUST NOT be altered. Verifier reports late-binding entries as `late-binding entries: N` PASS-with-anomaly line.

## §10.37 Hierarchical Merkle aggregation (normative when applicable)

**What.** For institutions with extreme event volumes, the daily Merkle tree composes with per-tenant-day sub-trees rather than a single tree per tenant per day. Multi-level aggregation with cross-anchor under the seal signature.

## §10.38 Consent capture (normative when applicable)

**What.** Four-event lifecycle for GDPR / DPDP / PIPL consent: `audit.consent.given`, `audit.consent.referenced`, `audit.consent.withdrawn`, `audit.consent.expired`. Plus `subject_id_hash` (NOT subject identifier) so consent integrity is provable without binding PII into the chain.

## §10.39 Institutional successor-attestation (normative when applicable)

**What.** Acquirer-side cryptographic inheritance of an acquired institution's pre-acquisition records. `chain.successor_attestation` event with `baseline_manifest_sha256` (now JCS-canonical sorted-array form per close-out), `baseline_manifest_kind` (closed enum: `prior_vendor_chain` / `prior_vendor_signed_pdfs` / `baseline_diary` / `mixed`), dual_signatures. Composes with §10.40 cross-vendor-merge cross-anchor and §10.42 backfill seal depending on `baseline_manifest_kind`.

## §10.40 Cross-vendor chain-merge cross-anchor (normative when applicable)

**What.** When the acquired institution operated a different vendor's chain, the acquirer's chain anchors the foreign-vendor roll-up artifacts using `audit.external_artifact.*` from §10.19. The acquirer's chain becomes the integrity-bound retrieval substrate even after the foreign vendor's service is decommissioned.

## §10.41 Chain-coverage-map M&A temporal-slice extension (normative when applicable)

**What.** During M&A cut-over windows, the chain-coverage map identifies three temporal partitions: pre-acquisition (acquirer's chain), cut-over window (target migrating onto acquirer's chain in tranches), post-cut-over (unified institution's chain). The `chain.coverage_map_published` event re-emits at each tranche.

## §10.42 Backfill seal discipline (normative when applicable)

**What.** When the acquired institution's pre-acquisition records are baseline-diary (not under any vendor's chain), the acquirer's HSM signs a one-time backfill seal at acquisition close. Seal record carries `seal.backfill_at_close = true`, `seal.backfill_window_start_utc`, `seal.backfill_window_end_utc`, `seal.backfill_baseline_manifest_sha256` (matching §10.39's `baseline_manifest_sha256`), `seal.backfill_companion_attestation_run_id` (cross-reference back to §10.39 event).

Verifier marker: `'backfill_seal_verified'` (lowercase per §10.12 marker convention).

**Why.** Pre-acquisition baseline-diary records were under no chain at all; §10.42 produces a chain-shaped integrity envelope retroactively over the inherited records.

## §10.43 Claim-state-machine chain entries (normative when applicable)

**What.** Insurance claim lifecycle on the chain: claim-opened → claim-noticed → claim-investigated → claim-disposed. State-machine transitions integrity-bound; out-of-order transitions are anomalies.

## §10.44 Cession-cohort recursive subtree disclosure (normative when applicable)

**What.** Recursive RFC 6962 audit paths for reinsurance cession disclosure. Lets a reinsurer audit only the cohort of policies assigned to its treaty without accessing the cedent's full claims chain.

## §10.45 Independent third-party adjuster anchor (normative when applicable)

**What.** Insurance-adjuster cross-anchor via §10.21.2 parallel-evaluator pattern. The adjuster's chain entries cross-anchor to the institution's claim-state-machine entries; both sides' verifiers walk the cross-anchor independently.

## §10.46 Bordereau integrity (normative when applicable)

**What.** Reinsurance bordereau (the per-period premium and loss summary the cedent sends the reinsurer) integrity-bound on the chain. `audit.bordereau.*` family with `bordereau_period`, `cedent_signature`, `reinsurer_acknowledgment`.

## §10.47 Generation prompt/output four-tuple binding (normative when applicable)

**What.** GenAI-specific: a chain entry for a model call binds (prompt, output, model_id, sampling parameters) as a four-tuple under the per-event MAC. `audit.generation.*` family with `model_weights_hash`, `prompt_hash`, `output_hash`, parameters.

**Why.** Without the four-tuple binding, an examiner asking "what produced this output?" can't answer from the chain alone — model identifier alone doesn't determine the output (sampling parameters matter).

## §10.48 Stochasticity attestation (normative when applicable — §10.47 extension)

**What.** Sampling parameters bound on the chain so a regulator running the same model with the same seed + parameters + weight bundle obtains the same output up to floating-point determinism per institution-named numerics-determinism posture.

## §10.49 Retrieval-source integrity (normative when applicable)

**What.** RAG (Retrieval-Augmented Generation) systems retrieve documents at inference time. §10.49 normates two integrity surfaces: a retrieval-set Merkle root bound on the §10.47 generation event, AND per-document anchor events emitted alongside.

**close-out:** retrieval-set Merkle leaves ordered lexicographically ascending by `document_sha256` (not by retrieval-relevance ranking). Ranking is preserved on per-document anchor events instead. Two implementations reconstructing the same retrieval set produce byte-identical Merkle root.

## §10.50 Output-grounding event family (normative when applicable)

**What.** Clinical-decision-support and regulator-supervised AI: `audit.grounding.*` family binding output to source documents. Composes with §10.49 retrieval and §10.21.2 parallel-evaluator (when an external clinical observer like Cleveland Clinic runs a parallel chain).

## §10.51 Public-transparency overlay (normative when applicable)

**What.** Differential-privacy aggregate publication primitive. `audit.public_transparency.*` family with DP noise seed bound on the chain so a regulator can verify the published aggregate matches the noise-seed-determined output.

## §10.52 Public model-card binding (normative when applicable)

**What.** The model card document published publicly (typical: institution's website) is hash-bound on the chain. A regulator reading the published model card and the chain entry can confirm they match.

## §10.53 Hybrid post-quantum seal mandate (normative when applicable)

**What.** For long-retention institutions (insurance with 25-year horizons, legal-hold archives), dual-algorithm seals (Ed25519 + ML-DSA-65 or similar) are mandated by 2030-01-01. TesseraSeal posture (TCCP axis 1) ships hybrid early; the spec mandate is 2030.

## §10.54 Decadal re-sealing discipline (normative when applicable)

**What.** Every 10 years, the institution re-seals the prior decade's chain anchor under the current cryptographic primitives. Composes with §10.53 PQ posture so cryptographic-agility migration happens at decadal boundaries rather than emergency-patch SLAs.

## §10.55 Audit-target challenge-response procedure (normative when applicable)

**What.** When a regulator wants to challenge a specific chain entry's integrity (e.g., during a DOJ subpoena), the institution executes a documented challenge-response producing a structured disposition the regulator can act on.

---

## What §10.31–§10.55 buys you

The middle cluster carries domain-specific operational extensions: per-device key derivation for edge / federated learning; training-phase integrity for in-house ML; edge-attestation for tablets and TEEs; late-arrival discipline for replication-loss tolerance; hierarchical Merkle for extreme-volume tenants; consent capture for GDPR/DPDP; M&A backfill + cross-vendor merge for acquisitions; insurance lifecycle (claim, cession, bordereau, adjuster); GenAI generation + grounding + retrieval + transparency + model-card binding; post-quantum + decadal re-sealing for long-retention regimes; audit-target challenge-response for regulator-initiated integrity tests.

Most institutions adopt only the §10.x extensions that match what they do — a community bank running underwriting AI doesn't operate a §10.62 red/black boundary; a frontier-AI training institution doesn't operate §10.46 bordereau integrity. The "(normative when applicable)" pattern lets institutions select their conformance surface per CC8.1.
