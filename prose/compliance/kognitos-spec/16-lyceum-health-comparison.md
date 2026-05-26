# 16 — Lyceum Health — Comparison

*Side-by-side reading: what the Kognitos twelve-field framework captures vs. what the FFIEC chain-of-custody v1.0b reference specification captures at the Lyceum Health System pre-Joint-Commission + HHS-OCR + FDA + five-state-DOH readiness engagement. First four-substrate composition in the program; third partial landing of the foresight-cluster §10.40 substrate-move pressure that opened at Ch12. First multi-state hospital-system engagement. Ninth settled voice-pattern variant introduced (personal-FDA-Sponsor-of-Record under SaMD post-market-surveillance accountability).*

---

## Per-walkthrough comparison

### Comparison A — §10.40 four-substrate composed variant (9:30 AM Day 1)

| Dimension | Kognitos 12-field | FFIEC reference spec |
|---|---|---|
| Quadrupled-timestamp at four-substrate seam | Field 1 singular; one of four timestamps recorded; three silently lost | §10.40 four-substrate variant binds four timestamps (Azure 14:17:08; Virginia on-prem 14:17:11; Hanover private cloud 14:17:14; Epic shared-services 14:17:21) as required attributes |
| Quadrupled-chain integrity across four substrates | Field 11 singular; one chain recorded; three chains + binding-hash silently lost | §10.40 four-substrate variant binds `audit.handover.substrate_chain[N]` with N=4 entries each carrying `chain_ref` + `merkle_root` + `seal_id` + `hsm_key_fingerprint` |
| Quad-HSM-rooted Ed25519 signatures | Field 12 singular; one signature recorded; three silently lost | §10.40 + §10.17 four-way HSM-root composition binds Azure HSM + Virginia HSM + Hanover HSM + Epic HSM signatures |
| Vendor-HSM attestation-doc cross-binding | No mechanism | §10.40 + §10.58 binds `vendor_hsm_attestation_doc_sha256` for the Epic-side substrate entry as published-attestation cross-reference |
| Verifier verdict — additional verifications array | Field 12 singular; the additional verifications array is invisible | §10.12 verdict object: exit code 0 + `additional_verifications: ['cross_cloud_seam_verified', 'multi_substrate_composition_verified', 'quad_hsm_signature_verified', 'vendor_cloud_co_anchor_verified']` (four additional verifications) |
| Recovery path | Speculation in cover memo: "the inference produced an action safely across systems" | Structural; reference spec carries four-substrate composition as a row-shape property |

The §10.40 four-substrate composed variant is the third partial landing of the foresight-cluster opener filed at Ch12. The compounding pattern: Ch14 cross-vendor variant (one substrate; one HSM root; one additional verification); Ch15 cross-cloud variant (two substrates; two HSM roots; two additional verifications); Ch16 four-substrate variant (four substrates; four HSM roots; four additional verifications). Each landing doubles the framework's structural losses at the seam.

### Comparison B — §10.55 FDA SaMD model-clearance attestation (11:30 AM Day 1)

| Dimension | Kognitos 12-field | FFIEC reference spec |
|---|---|---|
| FDA clearance provenance | Field 4 singular for model identity + version; FDA clearance number + pathway + clearance date not field-bearing | §10.55 binds `fda_clearance_number` (DEN240187) + `fda_clearance_pathway` (De Novo) + `clearance_date_utc` (2024-09-12) under MAC |
| Indications for Use SHA-256 + drift detection | No mechanism for IFU-drift detection | §10.55 binds `indications_for_use_sha256` with automatic detection of FDA-issued IFU drift via Letter to Industry; refusal-at-capture on hash mismatch |
| Sponsor-of-Record identity under MAC | Field 2 singular for human identity; FDA Sponsor accountability not field-bearing | §10.55 binds `sponsor_of_record_identity` (NPI under MAC) + `sponsor_of_record_attestation_chain_ref` (annual refresh chain row) |
| Indications-match refusal-at-capture | No mechanism | §10.55 + §10.22 SDK refusal-at-capture pattern halts inference when patient indication exceeds cleared scope |
| Deployed-model-artifact match | Field 4 records "version"; no slot for cleared-artifact byte-equal match | §10.55 binds `deployed_model_artifact_sha256` + `deployed_model_artifact_matches_cleared_artifact` boolean as runtime cleared-system verification |
| Post-market surveillance binding | No mechanism | §10.55 binds `adverse_event_subscription_active` + `post_market_surveillance_runbook_ref` |
| Recovery path | Speculation: "an FDA-cleared AI was used" | Structural; reference spec carries eight FDA regulatory-provenance attributes |

The §10.55 attestation is a new pattern in the program. Polaris's §10.51 cat-modeling ensemble was peer-model composition without regulator-clearance metadata; Lyceum's §10.55 is single-model with eight regulator-provenance attributes bound to personal Sponsor accountability. The two ensemble-vs-clearance shapes are structurally distinct AI-governance patterns at different points in the same regulatory landscape.

### Comparison C — §10.56 patient-safety clinical-decision-support boundary (1:30 PM Day 1)

| Dimension | Kognitos 12-field | FFIEC reference spec |
|---|---|---|
| Four-claim epistemic-scope partition | No concept of multi-claim epistemic-scope discipline | §10.56 partitions four claims: (a) what CDS said; (b) what surfaced to clinician; (c) what clinician did; (d) what happened to patient |
| Surfaced-to-clinician chain row | Field 6 records inputs; Field 8 records reasoning; no slot for bedside-presentation event | §10.56 + §10.11.1 ECOA-pattern reuse for bedside-presentation chain row with clinician_id receiving alert |
| Clinician-acted documented-override | Field 11 chain integrity per row; no slot for documented-override structural pivot | §10.56 + §10.11.1 ECOA-style structured-override pattern with `reason_code` + free-text rationale chain-bound under MAC; undocumented override structurally invisible |
| Patient-outcome out-of-chain boundary | No mechanism | §10.56 (d) explicit boundary — clinical outcomes are downstream; institution-side QI data is not chain |
| §1.1 Daubert four-factor mapping | No mechanism | §10.56 closure under §1.1 Daubert for Joint Commission Sentinel Event hearings |
| Recovery path | Speculation: "the AI was safe for the patient" | Structural; reference spec carries the four-claim partition under Daubert closure |

The §10.56 patient-safety boundary is the seventh §1.2 epistemic-scope variant in the program (after Helmstad post-enrollment correction; PCP sensor mutation; PCP dispatcher action; Olmstead civil-rights litigation; Sun-Won pre-chain era; Salt Pond FRE 902(13)/(14) litigation-defense). The new sharpening dimension: the boundary is structural at four claims simultaneously, not at one. Multi-claim epistemic-scope partition under a single regulatory framework (Joint Commission Sentinel Event Policy + §1.1 Daubert mapping) is a structurally new shape in the §1.2 family.

### Comparison D — §10.57 multi-state aggregated reporting partition (3:30 PM Day 1)

| Dimension | Kognitos 12-field | FFIEC reference spec |
|---|---|---|
| Jurisdictional partition of chain coverage | No concept of state-based partition | §10.57 enumerates five state partitions (MD/VA/DC/PA/DE) each with state-specific reporting requirements |
| State-specific reporting templates | No mechanism | §10.57 binds `subset_query` per partition with state-DOH reporting cycle (MD annual / VA quarterly / DC monthly / PA quarterly / DE biannual) |
| One-chain-many-deliverables structural property | Auditor produces parallel cover-memo speculations per audience | §10.57 + §10.19 chain-coverage map produces N deliverables from one chain artifact through deterministic partition queries |
| Recovery path | Speculation: "the chain meets each state's requirements" | Structural; reference spec carries jurisdictional partitioning as row-shape property |

§10.57 is the jurisdictional sibling of Ch14's §10.41 temporal-slice partitioning. Both extend §10.19 chain-coverage map (Salt Pond Ch10) — temporal extension at Northbridge for M&A; jurisdictional extension at Lyceum for multi-state regulatory overlay. The §10.19 family is now three-extension (spatial / temporal / jurisdictional) and predicts further extensions for engagement classes with novel partitioning shapes.

### Comparison E — §10.58 EHR-vendor co-anchor cross-tenant hash binding (9:00 AM Day 2)

| Dimension | Kognitos 12-field | FFIEC reference spec |
|---|---|---|
| Ongoing operational cross-vendor composition | Ch11 introduced one-time handover composition; ongoing composition has no analog under Kognitos | §10.58 binds daily cross-tenant anchor row carrying vendor seal SHA-256 + HSM attestation hash + freshness window + staleness threshold + refresh timestamps |
| Freshness-as-state property | No concept | §10.58 + §10.13 binds `cross_tenant_freshness_window_hours` + `staleness_alert_threshold_hours` + `last_refreshed_utc` + `vendor_seal_published_to_lyceum_at_utc` |
| Cross-tenant anchor row pattern | Field 6 partial-fits each refresh row as discrete source-attribution event | §10.58 binds the ongoing composition as a structural property across thirteen months operational history with zero stale-window incidents |
| Recovery path | Speculation: "Epic and Lyceum are connected" | Structural; reference spec carries ongoing operational composition with freshness contract |

The §10.58 cross-tenant pattern extends two prior patterns:
- Ch11 cross-vendor zero-trust composition (one-time handover at §10.21 seam — byte-equal SHA-256 join produces joint integrity claim)
- Ch13 consent-lifecycle-as-state (Saraswati DPDP Act §6 four-state lifecycle queryable across 184,712 referencing decisions)

§10.58 composes the two: cross-vendor composition (Ch11) + lifecycle-as-state-but-for-cross-vendor-binding-freshness (Ch13 analog). The compounded shape is a new structural primitive predicting future engagements with ongoing cross-vendor chain composition under freshness contract.

---

## Aggregate Comparison F — Multi-axis verdict mechanism compounded (program-level trajectory)

| Engagement | Substrate count at seam | Additional verifications landed | Kognitos Field 12 capture |
|---|---|---|---|
| Ch14 Northbridge Return | 1 substrate (within-AWS cross-vendor) | 1 (`backfill_seal_verified`) | "✓" + speculation that additional axis exists |
| Ch15 Polaris Reinsurance Lloyd's | 2 substrates (AWS + Azure) | 2 (`cross_cloud_seam_verified`, `dual_hsm_signature_verified`) | "✓" + speculation that two additional axes exist |
| Ch16 Lyceum Health | 4 substrates (on-prem + private cloud + Azure + Epic vendor cloud) | 4 (`cross_cloud_seam_verified`, `multi_substrate_composition_verified`, `quad_hsm_signature_verified`, `vendor_cloud_co_anchor_verified`) | "✓" + speculation that four additional axes exist |
| Ch17 Helvetian Tax Authority (forecast) | 2-3 substrates + cross-jurisdictional | 3-5 (forecast includes `cross_jurisdictional_seam_verified` + possible PQ-signature variant) | "✓" + speculation that 3-5 additional axes exist |

The compounding rate is structural — verdict-object additional-verifications grow with the spec; Kognitos's Field 12 stays singular. At Ch16 the framework records one of five total verification axes per four-substrate seam (one base proof + four additional verifications). The framework-grows-vs-fixed contrast appears directly in the verdict object at every engagement.

---

## Recurring lines (carried forward, not restated)

1. The reference spec is structurally as wide as the institution's architecture; the framework is row-shaped.
2. Field 12's tamper-evident-proof singular wording compounds losses at multi-substrate seams (quadrupled timestamps + chains + signatures at Ch16).
3. Stakeholder explicit-attribution: Dr. Yuki Takeda + Dr. Cyrus Patel deliver a joint statement composing the ninth settled voice-pattern variant (personal-FDA-Sponsor-of-Record under SaMD post-market-surveillance accountability) with the cross-functional executive joint pattern (board-level patient-safety under Joint Commission Sentinel Event Policy). Streak count advances to 11-in-16.
4. Cross-entity parent-linkage family extends: Ch07 external-artifact (documents) + Ch12 ECOA prior-offer (credit decisions) + Ch15 premium-allocation (money movement) + Ch16 §10.58 EHR-vendor cross-tenant ongoing composition. Four chapter-classes within the same structural pattern.
5. Composed-prior-amendments framework-growth signal continues: Lyceum's §10.40 four-substrate variant composes Ch15 §10.40 cross-cloud + Ch08 §10.17 dual-HSM-root + Ch10 `audit.external_artifact.*` (for the Epic vendor HSM attestation cross-binding); §10.58 composes Ch11 cross-vendor zero-trust + Ch13 lifecycle-as-state.
6. The §10.17 dual-HSM root discipline scales monotonically: within-vendor multi-region (NetiVa Ch08) → cross-cloud-within-jurisdiction (Polaris Ch15) → four-substrate-within-jurisdiction (Lyceum Ch16) → (forecast) cross-jurisdictional-cross-cloud (Ch17 Helvetian).
7. The framework's twelve-row schema has not moved in twenty months; the reference spec has absorbed nine engagement-source amendments + the v1.0b errata stream including §10.40 cross-cloud variant + §10.51-§10.54 Polaris wave + §10.55-§10.58 Lyceum wave.
8. Seven framework-substitution recommendations now exist in the program: Pankaj Ch08; Min-seo+Wei-ling Ch09; Patrick+Naomi Ch10; Heinrich+Sébastien Ch11; Aparna Ch13 (compose-rather-than-substitute variant); Maya Ch15; Yuki+Cyrus Ch16. Veronika's Ch04 statement remains the framing-pattern predecessor.

---

## Research signal

**Foresight cluster — third partial landing at Ch16.** The Ch12 whiteboard opener ("what happens when the substrate moves?") has now landed in three increments: Ch14 cross-vendor variant (within-substrate, cross-vendor-target M&A); Ch15 cross-cloud variant (two substrates, within-jurisdiction-UK + dual-HSM-root); Ch16 four-substrate variant (on-prem + private cloud + public cloud + EHR-vendor cloud composition, within-jurisdiction-multi-state + four-way HSM-root composition). The cross-jurisdictional-cross-cloud variant remains pending; Ch17 Helvetian Tax Authority is positioned as the cluster-closer with Swiss sovereign-data hard edge + extraterritorial OECD pillars producing the strongest variant of the substrate-move pressure.

**Compounding rate of multi-axis verdict mechanism.** Ch14 landed one additional verification per verifier invocation; Ch15 landed two; Ch16 landed four. The doubling pattern is not coincidental — each foresight-cluster landing adds one structural dimension to the verdict object's additional-verifications array. Ch17 cluster-closure may produce 5-6 additional verifications at the cross-jurisdictional-cross-cloud seam (forecast: cross_cloud + multi_substrate + quad-or-N-HSM + vendor_co_anchor + cross_jurisdictional + possible PQ-signature). The framework-grows-vs-fixed contrast appears in the verdict object's growth rate directly.

**Ninth settled voice-pattern variant: personal-FDA-Sponsor-of-Record under SaMD post-market-surveillance accountability.** Dr. Yuki Takeda's statement composes Maya Hartwell's eighth-variant personal-regulatory-exposure pattern (Ch15) with a structurally distinct register: FDA Sponsor of Record registration for DEN240187 is product-specific, while PRA SM&CR SMF26 is institutional-management-wide. The two patterns share shape (personal-register-named accountability) but operate on different registers (product-specific vs. management-wide). The voice-pattern catalog reaches 9 settled variants plus 1 candidate tenth (Ch14 return-engagement institutional-memory observation, still provisional pending second-instance reproduction at any future return engagement; Ch20 Mission Plaza Bank candidate).

**Cross-functional executive joint pattern reproduces with new dimension.** Dr. Cyrus Patel's co-signed statement reproduces the cross-functional executive joint pattern from Patrick + Naomi Ch10 (Salt Pond CRO + GC) with the new sharper dimension of board-level patient-safety accountability under Joint Commission Sentinel Event Policy. Cross-functional executive joint is now two-instance reproducible; the dimension-addition mechanism (Soren Ch06 / Holland Ch07 / Patel Ch16) is now four-instance reproducible across engagement classes.

**Diversity sample clean-fit rate trajectory.** Ch15 Polaris produced 0% clean-fit (zero of 10 records cleanly fit the Kognitos twelve-row template; all 10 verified under reference spec). Ch16 Lyceum produces 10% clean-fit (one record — clinical-trial screening on private cloud — partial-fits; nine of ten produce inarticulability or governance-ceremony silence or form-mismatch). The pattern: multi-substrate composed-architecture engagements where at least one surface preserves clean AI-decision mental model (clinical research; revenue cycle; back-office ML) show modest clean-fit rates while composed-architecture surfaces (clinical CDS pipeline; multi-state aggregated reporting; cross-vendor co-anchor) produce zero clean-fit. Future engagements with similar mixed-surface composition (Ch19 Aerolith hyperscale compute is candidate) may reproduce the 10%-or-less clean-fit signature.

**§12 amendment streak still broken — four consecutive chapters.** Ch12 (no amendment); Ch13 (structural-vocabulary gaps); Ch14 (structural-vocabulary gaps, M&A integration); Ch15 (structural-vocabulary gaps, cross-cloud composition); Ch16 (structural-vocabulary gaps, four-substrate composition). The §10.55-§10.58 sections that Lyceum exercises shipped in the spec's sixth errata seven weeks before the engagement opened — Lyceum is the first *production exercise* of these sections, not the engagement that produced them. Ch17 Helvetian Tax Authority is positioned to restart the §12 streak with the cross-jurisdictional-cross-cloud cluster-closing amendment that closes the foresight cluster filed at Ch12.

**Patient-safety / clinical-AI chapter-class introduced.** Lyceum is the first multi-state hospital system engagement; the first FDA SaMD post-market-surveillance pressure; the first clinical-decision-support boundary discipline production exercise. The chapter-class is structurally characterized by: (1) multi-substrate composition including on-prem; (2) FDA SaMD attestation with Sponsor-of-Record accountability; (3) §10.56 four-claim epistemic-scope boundary under Joint Commission Sentinel Event Policy + §1.1 Daubert; (4) multi-state regulatory partition; (5) EHR-vendor co-anchor cross-tenant ongoing composition. Predicts second instance at any multi-state hospital / health system engagement; possible signal for future Ch20 (Mission Plaza Bank — if architecture surfaces analogous multi-jurisdiction-multi-substrate composition for federal banking).

**Composed-amendment compounding signal extends.** Polaris Ch15's §10.54 retrocession ladder closed structurally through composed reuse of three prior engagement-source amendments. Lyceum Ch16's §10.40 four-substrate variant composes Ch15 §10.40 cross-cloud variant + Ch08 §10.17 dual-HSM-root + Ch10 `audit.external_artifact.*`; Lyceum's §10.58 composes Ch11 cross-vendor zero-trust + Ch13 lifecycle-as-state. The accumulated-amendments-composition signal is now reproducible across two consecutive chapters (Ch15 + Ch16); the framework-grows-vs-fixed contrast's second growth signature is established as a stable pattern.
