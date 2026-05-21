# Plain-English: §10.56–§10.71 — wave (hardware, frontier AI, banking institutional)

The wave is the spec's most recent expansion, covering three story arcs:
- **Story 18 (§10.56–§10.62)** — hardware bill of materials, firmware attestation, component cryptographic identity, RMA, anti-counterfeit, CMMC overlay, red/black separation
- **Story 19 (§10.63–§10.68)** — frontier AI training-corpus, training-run, fleet attestation, model-weight lineage, evaluation chain, AISI overlay
- **Story 20 (§10.69–§10.71)** — banking institutional: customer-disclosure subset, BSA SAR / privileged investigation, cross-institution Fedwire/ACH

---

## §10.56 Hardware bill-of-materials (HBOM) chain integrity (normative when applicable)

**What.** `audit.hbom.*` family for institutions operating chain-of-custody coverage that includes physical hardware components (defense electronics, automotive, industrial control, datacenter hardware). Per-component lifecycle: incoming-test → integration → field deployment → return → disposition. Composes with §10.58 cryptographic identity for binding-walk and challenge-walk verification.

**Why.** Counterfeit components, supply-chain attacks, sustainment ambiguity — all addressable by a per-component chain anchored from incoming-test.

## §10.57 Firmware-attestation chain across supplier tiers (normative when applicable)

**What.** Two paths: internal-build (`audit.firmware.build` + `audit.firmware.activate` events on the institution's own chain) and cross-supplier-build (institution cross-anchors the supplier's signed attestation document via §10.21).

## §10.58 Component cryptographic identity primitive (normative when applicable) — *substantive*

**What.** Four identity-kinds for binding hardware components:
- `puf-response` — Physically Unclonable Function challenge-response
- `seal-chiplet-attestation` — DARPA SHIELD program chiplet attestation
- `factory-provisioned-key` — manufacturer-provisioned key with public CA chain
- `serial-lot-hash` — fallback for components without on-die identity

**Two verifier modes:**
- **Binding-walk** — verifier confirms binding-hash structurally (component need not be in-hand). PASS marker: `'component_identity_binding_walk_verified'`.
- **Challenge-walk** — verifier challenges component directly (component must be in-hand). PASS marker: `'component_identity_challenge_walk_verified'`. Available for `puf-response` (always) and `factory-provisioned-key` (when CA online).

**Binding-hash construction:** `binding_hash = SHA-256(JCS(canonical_binding_input))` where `canonical_binding_input` is a JSON object with `identity_kind` plus per-kind payload fields. The JCS-based construction (replacing the original pipe-delimited form) closes the boundary-confusion vulnerability cryptographic reviewers would have caught at public comment.

## §10.59 RMA / sustainment chain re-entry discipline (normative when applicable)

**What.** Hardware components removed from deployed systems re-enter the chain. `audit.rma.*` events for depot-return, repair-completion, cannibalization (parent-children pattern), scrap, RMA-disposition. Duplicate-binding anomaly fires when the same `cryptographic_identity` is bound to multiple incoming-test entries under different serials.

## §10.60 Anti-counterfeit cross-anchor (normative when applicable — extends §10.21.1)

**What.** When §10.59's duplicate-binding anomaly fires, the institution refers the suspect lot to an AS6171 laboratory. The resulting attestation lands as an `audit.rma.disposition` event referencing the §10.60 cross-anchor.

## §10.61 CMMC 2.0 / NIST 800-171 / NIST 800-161 regulator-pack overlay framework (normative when applicable)

**What.** Defense-electronics primes operate under Cybersecurity Maturity Model Certification 2.0. §10.61 maps the chain primitives onto specific control items in CMMC 2.0 + NIST 800-171 + NIST 800-161. Versioned overlay: §10.61.1 for CMMC 2.0, §10.61.2 for the next CMMC release.

## §10.62 Red/black separation chain integrity (normative when applicable) — *substantive*

**What.** Cleared-environment systems maintain red/black separation between plaintext-classified ("red") and encrypted-or-unclassified ("black") subsystems. AI-bearing systems whose inference happens on red and whose outputs traverse to black via a Type-1 cross-domain crypto module need the chain to respect the separation.

**§10.62 introduces a new top-level wire-format kind:** `cross_domain_transition`. Schema (with `audit.cross_domain_transition.*` namespace prefix per close-out):
- `red_chain_entry_id` — source red-side chain entry
- `releasable_hash` — deterministic releasable-form projection
- `releasability_filter_version` — institution-named filter version
- `cross_domain_module_attestation` — §10.21 cross-anchor to NSA-issued evaluation
- `red_to_black_transition_at_utc` — RFC 3339 UTC
- `black_chain_entry_id` — counterpart on black side (when applicable)

**Two verifier modes:**
- **Red-side full walk** — operated inside the cleared area with full red-side IKM access. PASS marker: `'red_black_red_side_full_walk_verified'`.
- **Black-side hash-equivalence walk** — operated outside the cleared area with no red-side IKM. PASS marker: `'red_black_black_side_hash_equivalence_verified'`.

**Failure paths:** three named anomaly lines for releasable-hash projection divergence, cross-domain attestation invalid, red-black hash-equivalence broken.

### §10.62.1 Red/black-aware chain entry tagging

`audit.color_classification.side` enum (`red` / `black` / `cross-domain`); `audit.color_classification.classification_level` (institution-named: `secret` / `top-secret` / `unclassified-cui` / `unclassified`).

### §10.62.2 Releasability-projection contract framework

The releasable-hash projection's contract (normative): determinism, no red-side content leakage, versioning, test-vector grounding (each filter MUST ship with at least one byte-identical test vector). Reference projection: TALON-X program filter, vector `063-red-black-projection-talon-x` (Phase 12 budget).

## §10.63 Training-corpus provenance chain (normative when applicable)

**What.** Frontier AI training corpus integrity. `audit.training_corpus.*` events at build time chain corpus shards, dataset versions, copyright-clearance attestations. The chain becomes the integrity substrate for the corpus claim.

## §10.64 Training-run code-and-config chain with per-step Merkle aggregation (normative when applicable)

**What.** `audit.training_run.*` family. Per-step Merkle aggregation: each training step produces a chain entry; per-step entries roll up into `aggregation_proof_hash`. Cross-anchor to §10.63 corpus and §10.65 fleet attestation.

## §10.65 Hyperscale GPU-fleet attestation (normative when applicable)

**What.** Chassis-level TPM as the institution's §10.58 component-cryptographic-identity primitive applied at chassis granularity. Per-GPU TEEs (when present in next-generation fleets) extend §10.58 to per-GPU.

### §10.65.1 + §10.65.2 Expected-state-evolution profile schema

Hardware whose chain entries carry §10.35 edge-attestation primitives (TPM PCR state) experience PCR evolution as firmware activates. The expected-state-evolution profile names the institution's expected PCR-state evolution per chassis class. `drift_seen` boolean discriminates routine kernel updates (operational, not anomaly) from unauthorized updates (control-completeness anomaly). The profile event is **chain-published** (not CC8.1-only) so public verifiers can perform `drift_seen` discrimination by walking the chain — institutions cannot retroactively claim a different "expected" profile.

## §10.66 Model-weight lineage across multi-month runs (normative when applicable)

**What.** Frontier models go through multi-stage life: pre-training → SFT → RLHF/DPO → evaluation → deployment. `audit.model_weights.*` family captures every weight transition as a directed acyclic graph (DAG) with per-transition cross-anchor to §10.64 producing runs.

**Lineage Merkle construction:** `lineage_root_hash = SHA-256(JCS(canonical_binding_input))` over leaves where each leaf is the SHA-256 of JCS-canonical bytes of one transition event's payload. Within each leaf, `parent_weights_hashes` sorted lexicographically; across leaves, sorted by `child_weights_hash`.

PASS marker: `'model_weight_lineage_verified'`.

## §10.67 Pre-deployment evaluation chain (normative when applicable)

**What.** `audit.evaluation.*` family. Composes with §10.21.2 parallel-evaluator (e.g., lab + AISI run parallel evaluation chains anchored at the target-model-weights chain entry).

## §10.68 AI Safety Institute Reference Evaluation Program regulator-pack overlay (normative when applicable)

**What.** Versioned regulator-pack overlay for institutions participating in the AISI Reference Evaluation Program. Maps the chain primitives onto AISI-specific evaluation requirements.

## §10.69 Per-customer audit-trail subset disclosure (normative when applicable) — *substantive*

**What.** A customer demanding their own chain-of-custody record receives a per-customer subset packet. The packet:
- Includes only chain entries belonging to that customer
- Is integrity-verifiable by the customer using a §10.69-derived disclosure key (NOT the institution's IKM)
- Documents exclusions (typically `sar`, `litigation_hold`, `privileged_investigation`)

The customer-disclosure verifier mode is the third verifier mode (alongside strict and witness; per §7 amendment). Output: `Status: PASS-CUSTOMER-DISCLOSURE, institution-IKM verification skipped`.

**§1.2 fifth epistemic non-claim** (added 2026-05-09): the chain proves what was disclosed, not what was withheld. A customer cannot detect institution mis-categorization of a withheld entry as `litigation_hold` from the chain alone. The §10.70 access-trail backs this post-hoc.

## §10.70 Bank Secrecy Act SAR / privileged-investigation overlay (normative when applicable)

**What.** Two verifier outputs for entries under privileged-investigation flags:
- **Cleared mode** — full content returned (regulator with appropriate clearance)
- **Non-cleared redacted-with-existence-attestation** — entry content withheld, but existence cryptographically attested (a non-cleared regulator can confirm "an entry exists for this consumer at this time" without seeing content)

`audit.privileged_investigation_access` events form the access-trail that backs §10.69's customer-disclosure non-disclosure claim post-hoc.

## §10.71 Cross-institution Fedwire / ACH chain integrity (normative when applicable)

**What.** When an institution originates a Fedwire or ACH transaction, the chain entries on the originating side benefit from cross-institution integrity binding to the receiving institution's chain. Uses §10.21.3 registry-discovery pattern via the Federal Reserve's voluntary cross-institution-anchor registry.

`audit.wire.*` and `audit.ach.*` event families. Verifier marker: `'cross_institution_chain_verified'` on bound; `'cross_anchor_unbound'` when receiving institution non-participating.

---

## What §10.56–§10.71 buys you

The wave covers three institutional surfaces the v1.0a/v1.0b base didn't reach:
- **Hardware supply chain** (Story 18) — defense electronics, datacenter hardware, automotive, industrial control benefit from per-component chain anchoring + cryptographic identity + red/black separation.
- **Frontier AI training** (Story 19) — institutions building large models get training-corpus + training-run + fleet + weight-lineage + pre-deployment-evaluation primitives + the AISI overlay.
- **Banking institutional** (Story 20) — per-customer disclosure with bounded session-key derivation + BSA SAR access-trail backing + cross-institution Fedwire/ACH integrity binding.

Each of these is a "(normative when applicable)" — institutions adopt only what their use cases require. A community bank running AI underwriting doesn't operate any of §10.56–§10.71; a tier-1 institution operating frontier-AI training in defense-cleared environments operates most of them.
