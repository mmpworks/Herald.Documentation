# Comparative Analysis — Chapter 18 (Argent Vector Defense)

*Side-by-side analysis of how the Kognitos 12-field framework and the TesseraSeal / FFIEC chain-of-custody v1.0b spec handle a **defense industrial-base contractor under National Industrial Security Program with Special Access Program compartmentation, classified-domain chain-of-custody, cross-domain solution accreditation, air-gap bridge discipline, and personnel clearance integration** with DCSA + DoD IG + DCMA + SAPCO parallel audience reading. Honest assessment of where the framework's row-shape cannot articulate cross-classification compositional invariants, cross-domain solution accreditation, air-gap chain-of-custody bridges, SAP-compartment cryptographic isolation, or authorized-personnel chain-binding — even when the chain runs clean across nineteen months of classified-domain operations under NSA Suite B + transitioning CNSA 2.0.*

---

## New research signal

Argent Vector Defense closes its three-day pre-DCSA Industrial Security Review + pre-DoD IG Special Access Program Inspection readiness pass with zero findings and zero Partials, but five Framework Inarticulabilities across the cross-classification + cross-domain + air-gap + SAP-compartment architecture. The chapter is the program's first defense industrial-base engagement and produces three program-structural reproductions plus one new dimension introduction:

1. **Cross-institutional-constitutional-officer joint dimension settles** as the eleventh voice-pattern variant. Dr. Ursula Keller's provisional eleventh variant at Helvetian Ch17 (constitutional-data-protection-officer under Article 43a FADP + Federal Council appointment) is reproduced at Argent Vector by William Steadman (statutory-independent-officer at DoD IG under Inspector General Act of 1978 + 10 U.S.C. §141). Same structural shape, different statutory basis. The pattern now meets the second-instance reproduction threshold and promotes from provisional to settled in the catalog.

2. **Twelfth settled voice-pattern variant introduced** — Mariana Whitfield delivers a personal-criminal-classification-individual statement under NISPOM Section 3-103 + 18 U.S.C. §793 (Espionage Act) + 18 U.S.C. §1924 (mishandling classified information). Distinct from the prior three personal-register-named accountability variants (Maya SM&CR institutional-management-wide / Yuki FDA SaMD product-specific / Affentranger treaty-network multilateral) by carrying personal criminal exposure under federal felony statutes — a sharpness that the regulatory, FDA, and treaty regimes do not match.

3. **Chain-bound constitutional-level invariant chapter-class settles** as two-instance reproducible. Helvetian Ch17 bound `sovereign_residency_invariant_held: true` under MAC composing Article 13 + FADP + FTAA + Banking Secrecy Act; Argent Vector Ch18 binds `classification_invariant_held: true` under MAC composing NISPOM + EO 13526 + Atomic Energy Act + Espionage Act. Same structural shape across constitutional regime (Switzerland) and statutory regime (US). The pattern is reproducible across regimes regardless of whether the legal frame is constitutional or statutory.

4. **New foresight cluster opens** — post-quantum migration in classified systems. Helmstad Ch05 raised NIST PQC under §4.3.2 as a future-readiness consideration; Argent Vector Ch18 exercises CNSA 1.0 + 2.0 hybrid dual-algorithm seal under §4.3.2 in operational classified data with a 2030 NSA Cybersecurity Advisory transition deadline. The pattern opens the question Aerolith Compute (Ch19) is positioned to amplify: what happens when post-quantum migration crosses engagement boundaries at planet-scale hyperscale compute?

| New signal | Mechanism | Reproduction status |
|---|---|---|
| Cross-institutional-constitutional-officer joint dimension | Statutorily independent observer co-signs framework-substitution recommendation | **Settled** — second-instance reproduction (Keller Ch17 + Steadman Ch18) |
| Personal-criminal-classification-individual voice pattern | NISPOM-designated FSO with criminal exposure under federal felony statutes | **First instance** — twelfth settled variant in catalog |
| Chain-bound constitutional-level invariant chapter-class | Compositional legal-framework invariant MAC-bound at seam | **Settled** — second-instance reproduction (Helvetian Ch17 + Argent Vector Ch18) |
| Post-quantum migration foresight cluster | Operational CNSA 2.0 transition exercise under §4.3.2 | **Opener** — Ch19 Aerolith Compute positioned amplifier |

The closing line: Argent Vector at Ch18 establishes that the cross-classification + cross-domain + air-gap + SAP-compartment + personnel-clearance composition is structurally as far beyond the framework's row-shape as the cross-jurisdictional + treaty-network + constitutional-invariant composition was at Helvetian. Two engagement classes (sovereign tax administration and defense industrial base) both reproduce the same framework-side gap with the same compositional shape across structurally different legal frames.

---

## Recurring from earlier chapters

| Recurring point | Earlier ref | Ch 18 instance |
|---|---|---|
| Compositional security | Ch01 §1.4 | Cross-classification + cross-domain + air-gap composition; five composed integrity surfaces simultaneously |
| Multi-tenant IKM uniqueness | Ch04 §10.1 | Per-SAP-compartment IKM derivation under §4.1 HKDF + compartment-discriminator extension; Cipher and Trident cryptographically isolated |
| HSM partition-ceremony attestation | Ch05 + Ch08 §10.17 | Thales Luna SA 7000 partitions for SAP compartments under FIPS 140-3 Level 3 |
| Cross-vendor model-handover (§10.21) | Ch11 + Ch12 | Air-gap bridge under §10.66 — cross-classification analog of cross-vendor seam |
| §10.40 cross-cloud variant | Ch15 | AWS GovCloud unclassified + Azure Government CUI under cross-cloud composition |
| §10.40 four-substrate composed variant | Ch16 | Four-classification-substrate composition extends the four-substrate shape to classification regime |
| §10.40 cross-jurisdictional-cross-cloud variant | Ch17 | Foresight cluster closed at Ch17; not reopened at Ch18 |
| Chain-bound constitutional-level invariant | Ch17 §10.60 | Chain-bound classification invariant under §10.65; second-instance reproduction |
| Cross-institutional-constitutional-officer joint dimension | Ch17 (provisional eleventh) | Settled at Ch18 via DoD IG observer reproduction of Keller pattern |
| Personal-register-named accountability family | Ch15 + Ch16 + Ch17 | Fourth instance — NISPOM + Espionage Act personal criminal exposure |
| §4.3.2 quantum-readiness commitment | Ch05 | First operational exercise in classified domain; opens post-quantum migration foresight cluster |
| §1.4 substrate inarticulability | Ch08 + Ch11 | Cross-classification substrate composition; third generalization of substrate-class inarticulability |
| §10.26 reference-verifier distribution (CC8.1) | Ch01 + Ch05 + Ch06 | Cleared-personnel verifier distribution discipline under DCSA-approved tooling |

**Severities unchanged.** No re-litigation of recurring points; one-line each.

---

## New comparison points specific to Chapter 18

### A. Cross-Domain Solution chain-anchor structural property

**The audit-room question.** *"How does the chain articulate that an artifact crossing from unclassified to CUI passed through a DCSA-accredited Cross-Domain Solution with content inspection, sanitization, and classification attestation under high-assurance guard discipline?"*

**TesseraSeal.** §10.63 introduces the CDS guard event chain row carrying fourteen MAC-bound attributes: source-classification-level, destination-classification-level, guard-device-identity, guard-firmware-attestation, sanitization-decision, sanitization-rule-version, sanitization-outcome-evidence-SHA, downgrade-decision, reviewer-identity (when manual), reviewer-PIV-D-credential-hash, classification-attestation, caveat-list-before, caveat-list-after, guard-daily-seal-ref + guard-HSM-attestation-fingerprint. The verifier walks the cross-domain seam with five additional verifications: cross_domain_seam_verified + guard_firmware_attestation_verified + sanitization_outcome_evidence_verified + classification_attestation_verified + caveat_list_transition_verified.

**Kognitos.** Field 1 records one of two timestamps. Field 11 records one of two chains (Argent's CUI-side; not the guard's daily-seal-rooted attestation chain). Field 12 records one of two HSM signatures (Argent's; not the guard's HSM-attestation fingerprint). The cross-domain seam structural property is invisible.

**Inarticulability gap.** No Kognitos field articulates that two chains-of-custody compose at a DCSA-accredited high-assurance guard under Raise-the-Bar baseline. The five additional verifications on the verdict object have zero representation under any of the twelve fields.

**Structural reason for the gap.** Kognitos's row-shape treats every chain event as a single integrity claim. Cross-domain transfer under accredited guard is structurally a composition of two independent integrity claims under a guard-device trust anchor — a compositional structure the framework's row-shape cannot accommodate without adding rows to it.

**Honest assessment.** Severity: highest for any defense industrial-base contractor with classified-domain operations and cross-domain transfer requirements; applicable to any institution operating under classification regimes (intelligence community, defense, sensitive-but-classified federal agencies).

### B. Compartmented-program tenant-isolation under Special Access Program

**The audit-room question.** *"How does the chain articulate that Project Cipher and Project Trident — two SAP compartments under the same umbrella — are cryptographically isolated from each other at four layers simultaneously (network + HSM-partition + chain-substrate + personnel-access)?"*

**TesseraSeal.** §10.64 introduces SAP-compartment tenant-isolation discipline composing: (1) network-layer compartmentation with no L3 routes between SAPs and air-gap to other classification domains; (2) HSM-partition-layer with per-compartment Customer Managed Key + per-compartment IKM derivation under §4.1 HKDF + `HKDF_INFO_BASE || '|' || sap_program_code || '|' || tenant_id || '|' || compartment_code`; (3) chain-substrate-layer with separate chain per compartment; (4) personnel-access-layer with SAPCO-maintained access-list lookup at chain-capture. Cross-compartment validation produces designed refusal under exit code 4 (compartment-isolation-enforced; designed refusal).

**Kognitos.** Field 2 reads "tenant" as singular identifier. Same `tenant_id` may legitimately appear in multiple SAP compartments under cryptographically isolated chain substrates; cross-compartment cryptographic validation is *designed* to fail. Field 11 reads "chain integrity" and treats Cipher and Trident as if they composed one chain. Field 12 reads "tamper-evident proof" and confirms each compartment's proof in isolation without articulating the cryptographic isolation between them.

**Inarticulability gap.** No Kognitos field articulates per-compartment cryptographic isolation under SAP. The Atrio Ch04 multi-tenant 5×5 cross-tenant refusal matrix is reproduced here at the compartment level — except that under SAP, cross-compartment leak has political and statutory consequences (reportable to Government Program Manager and DoD IG within hours under DoDM 5205.07) that civilian multi-tenancy does not have.

**Honest assessment.** Severity: highest for any defense or intelligence-community contractor operating under SAP or analog compartmentation (DCSA SCI; CIA Compartmented Program; NSA Special Operations Compartment; ODNI Compartmented Program); applicable to any institution where compartmentation discipline must be cryptographically enforced rather than policy-enforced.

### C. Classification-level + caveat-list binding under MAC

**The audit-room question.** *"How does the chain articulate that every chain row in the classified domain carries classification_level + compartment_code + caveat_list MAC-bound at capture, such that cross-classification access produces refusal-at-capture?"*

**TesseraSeal.** §10.65 introduces classification-level + caveat-list binding under MAC: every chain row in the classified domain carries `classification_level` (U / CUI / Confidential / Secret / TS / TS_SCI) + `compartment_code` (SAP compartment codes for TS_SCI + SAP) + `caveat_list` (NOFORN, FGI, FVEY, ORCON, REL TO, etc.) MAC-bound at capture. The classification binding is structural: an inference event at TS_SCI + Cipher SAP cannot be read as Secret-level without producing a different MAC because the classification attributes are part of the MAC input.

**Kognitos.** Field 4 reads "model" and the model is correct; Fields 5-8 read prompt/response/context and contents are correct; Field 12 confirms the proof. None of the twelve fields read classification-level. The reference spec catches the binding through §10.65 + §4.1 input-domain-separation; Kognitos catches zero.

**Inarticulability gap.** No Kognitos field articulates classification-level chain-binding. Auditor records "Field 12: ✓" without footing for whether the row was at unclassified, CUI, Secret, Top Secret/SCI, or SAP; the framework cannot distinguish the classification level of any chain row.

**Honest assessment.** Severity: highest for any defense or intelligence-community engagement; high for any federal-agency engagement under EO 13526; medium for any state-government or local-government engagement under analog classification regimes.

### D. Air-gap chain-of-custody bridge

**The audit-room question.** *"How does the chain articulate that an artifact transferred from the Secret-domain SIPRNet enclave to the Top Secret/SCI + SAP enclave through air gap maintained chain-of-custody integrity across the physical isolation?"*

**TesseraSeal.** §10.66 introduces air-gap chain-of-custody bridge: paired chain rows under (1) Secret-domain bridge-attestation containing source-Merkle-root + packaging-PIV-D-credential-hash + accredited-media-serial + pre-write-attestation-SHA; (2) SAP-domain bridge-receipt containing source-Merkle-root (byte-equal verified) + receiving-PIV-D-credential-hash + accredited-media-serial (byte-equal verified) + post-read-attestation-SHA (byte-equal verified) + SAP-domain anchor sequence number. Verifier walks the bridge with five additional verifications: air_gap_bridge_attestation_verified + air_gap_bridge_receipt_verified + accredited_media_serial_match_verified + accredited_media_attestation_match_verified + two_person_integrity_log_match_verified.

**Kognitos.** Field 11 reads "hash chain" on one side or the other but cannot read the bridge that connects them. Field 12 reads "tamper-evident proof" on each side independently. The framework records two independent twelve-field rows for the same logical transfer and loses the air-gap bridge structural property entirely.

**Inarticulability gap.** The bridge is the chain. There is no network link; the two chains are physically isolated by air gap. The chain-of-custody discipline under §10.66 enforces integrity across the air gap through the paired structure; no Kognitos field articulates the bridge.

**Structural reason for the gap.** Cross-classification analog of Eberhardt × Lumière Ch11's cross-vendor zero-trust composition. At Ch11 the trust-producing step was the byte-equal SHA-256 hash join at §10.21 cross-vendor seam. Here the trust-producing step is the paired bridge-attestation + bridge-receipt across air gap. Same compositional-security shape, sharper substrate (physical isolation vs. organizational boundary).

**Honest assessment.** Severity: highest for any institution where chain-of-custody must span air-gapped networks (defense classified; intelligence community; nuclear facilities; high-security industrial control systems with regulatory chain-of-custody requirements).

### E. Authorized-personnel chain-binding under PIV-D + ICAM + clearance-level + compartment-access verification

**The audit-room question.** *"How does the chain articulate that every read/write/sign event is MAC-bound to the operator's PIV-D credential + ICAM identity + clearance-level attestation + SAP-compartment access attestation at the moment of chain capture?"*

**TesseraSeal.** §10.67 introduces authorized-personnel chain-binding under MAC: every read/write/sign event MAC-bound to (1) PIV-D credential hash; (2) ICAM identity (federated SAML assertion under ICAM 2.0); (3) clearance-level attestation (sourced from JPAS lookup at session establishment, attestation_sha256 recorded); (4) SAP-compartment access attestation (sourced from SAPCO access list, attestation_sha256 recorded). Verifier walks four additional verifications: piv_d_credential_chain_verified + icam_identity_federated_verified + clearance_level_attestation_verified + sap_compartment_access_attestation_verified.

**Kognitos.** Field 2 (tenant) records an identifier; Field 11 records the chain; Field 12 records the proof. The four-attribute personnel binding has no Kognitos field. Free-text annotation in any text field would record the identifier without the underlying clearance-attestation chain.

**Inarticulability gap.** The reference spec catches the four-attribute personnel binding structurally; Kognitos catches the identifier and loses the clearance attestation chain underneath it. A row that purports to be written by a TS_SCI-cleared individual but where the JPAS lookup failed at session establishment would produce a chain row that the framework cannot distinguish from a row written by a properly cleared individual.

**Honest assessment.** Severity: highest for any defense or intelligence-community engagement; high for any federal-agency engagement requiring federated identity + clearance integration (DoD, IC, sensitive federal agencies); medium for any institution with multi-level access control where the access level must be cryptographically enforced rather than session-state inferred.

### F. Chain-bound classification invariant (compositional legal-framework invariant)

**The audit-room question.** *"How does the chain articulate that `classification_invariant_held: true` is MAC-bound at every cross-classification seam under the composed legal framework of NISPOM + Executive Order 13526 + Atomic Energy Act + Espionage Act?"*

**TesseraSeal.** §10.65 + §10.67 + §10.40 cross-classification seam discipline compose to produce chain-bound classification invariant: `classification_invariant_held: true` MAC-bound at every cross-classification seam, every air-gap bridge, every SAP-compartment write, every clearance-level transition. The invariant composes four legal frames structurally: NISPOM (32 CFR Part 117) + Executive Order 13526 (Classified National Security Information) + Atomic Energy Act of 1954 (42 U.S.C. §2274 categorical criminal exposure for Restricted Data; not relevant at Argent Vector but a constituent legal frame) + 18 U.S.C. §793 (Espionage Act). Cross-classification access produces refusal-at-capture; the invariant cannot be falsely satisfied at capture without producing an invalid MAC.

**Kognitos.** Field 12 reads "tamper-evident proof" and confirms the MAC is intact. The framework has no concept of a compositional legal-framework invariant bound to the MAC's input. Free-text annotation in any text field would record a name but not the cryptographic enforcement.

**Inarticulability gap.** Second-instance reproduction of the Helvetian Ch17 chain-bound constitutional-level invariant pattern. Helvetian's invariant was constitutional (Article 13 + FADP + FTAA + Banking Secrecy Act); Argent Vector's invariant is statutory (NISPOM + EO 13526 + Atomic Energy Act + Espionage Act). Same structural shape across constitutional and statutory regimes.

**Honest assessment.** Severity: highest for any defense or intelligence-community engagement where classification regime carries criminal exposure; chapter-class establishes that compositional legal-framework chain-bindings are now two-instance reproducible and predict future reproductions at any engagement where multiple statutory or constitutional frameworks compose under MAC.

---

## Summary table

| # | Area | TesseraSeal anchor | Kognitos anchor | Speculation gap | Material impact |
|---|---|---|---|---|---|
| A | Cross-Domain Solution chain-anchor | §10.63 | Fields 1, 11, 12 record one side | inarticulability / highest | Cross-classification trust composition unrepresented |
| B | SAP-compartment tenant isolation | §10.64 | Field 2 + Field 11 singular | inarticulability / highest | Cryptographic compartmentation under SAP unrepresented |
| C | Classification-level + caveat-list binding | §10.65 | No field | inarticulability / highest | Classification chain-binding invisible |
| D | Air-gap chain-of-custody bridge | §10.66 | Fields 11, 12 record one side | inarticulability / highest | Physical-isolation chain-of-custody composition unrepresented |
| E | Authorized-personnel chain-binding | §10.67 | Field 2 records identifier | inarticulability / highest | PIV-D + ICAM + clearance + compartment-access invisible |
| F | Chain-bound classification invariant | §10.65 + §10.67 + §10.40 composition | No field | inarticulability / highest | Compositional legal-framework invariant unrepresented |

**Plus recurring from Chapters 01-17:** numerous comparison points unchanged (compositional security, multi-tenant IKM, HSM partition-ceremony, cross-vendor model-handover, §10.40 cross-cloud and four-substrate variants, chain-bound constitutional-level invariant, cross-institutional-constitutional-officer joint dimension, §4.3.2 quantum-readiness, §1.4 substrate inarticulability, §10.26 reference-verifier distribution).

**Total comparison points exercised in Chapter 18:** 6.
**Of which inarticulabilities: 6.**
**Of which under-reportings: 0** (structural-vocabulary gaps; not under-reportings).

---

## Honest assessment — engagement-scoped

### What Chapter 18 uniquely contributes

The chapter is the program's first defense industrial-base engagement and first engagement under classified networks (SIPRNet + JWICS-adjacent) with chain-of-custody spanning classification boundaries. Three reproductions plus one introduction land at this chapter:

**Cross-institutional-constitutional-officer joint dimension settles as eleventh voice-pattern variant** through DoD IG observer reproduction of the Keller pattern that Helvetian Ch17 introduced as provisional eleventh. Same structural shape (statutorily independent observer with authority to report to a body outside the institution's chain of command), different statutory basis (Inspector General Act + 10 U.S.C. §141 vs. Article 43a FADP + Federal Council appointment). Two-instance reproduction across constitutional regime (Switzerland) and statutory regime (US) settles the pattern as catalog eleventh.

**Twelfth settled voice-pattern variant introduced** through Mariana Whitfield's personal-criminal-classification-individual statement under NISPOM Section 3-103 + 18 U.S.C. §793 (Espionage Act) + 18 U.S.C. §1924 (mishandling classified information). The defense classification regime is the only personal-accountability regime in the program that combines administrative enforcement (clearance suspension or revocation) with categorical criminal exposure under federal felony statutes. Distinct from the prior three personal-register-named accountability variants:
- Maya Hartwell (Ch15): PRA SM&CR — regulatory enforcement, no personal criminal exposure
- Yuki Takeda (Ch16): FDA SaMD Sponsor — FDA enforcement action, no personal criminal exposure under SaMD framework
- Lukas Affentranger (Ch17): OECD CRS MCAA + bilateral treaty — diplomatic + treaty obligations, no personal criminal exposure
- Mariana Whitfield (Ch18): NISPOM + Espionage Act + Atomic Energy Act — personal criminal exposure under federal felony statutes

**Chain-bound constitutional-level invariant chapter-class settles as two-instance reproducible.** Helvetian Ch17 bound `sovereign_residency_invariant_held: true` composing Article 13 + FADP + FTAA + Banking Secrecy Act (Swiss constitutional regime). Argent Vector Ch18 binds `classification_invariant_held: true` composing NISPOM + EO 13526 + Atomic Energy Act + Espionage Act (US statutory regime). Same structural shape across constitutional and statutory regimes; the pattern is reproducible regardless of whether the legal frame is constitutional or statutory.

**New post-quantum migration foresight cluster opens.** Helmstad Ch05 raised NIST PQC under §4.3.2 as future-readiness consideration; Argent Vector Ch18 exercises CNSA 1.0 + 2.0 hybrid dual-algorithm seal under §4.3.2 in operational classified data with NSA Cybersecurity Advisory 2030 deadline. The cluster question — what happens when post-quantum migration crosses engagement boundaries at planet-scale hyperscale compute — is positioned for Aerolith Compute (Ch19) to amplify.

### The joint stakeholder statement

Mariana Whitfield opened on the record:

> "On the record: the Kognitos twelve-field framework is acceptable as a vendor-facing summary of an AI-decision audit-trail. It is not acceptable as the only assessment artifact for a defense industrial-base contractor operating under the National Industrial Security Program with Special Access Program compartments, classified-domain chain-of-custody, cross-domain solution accreditation, air-gap bridge discipline, and personnel clearance + ICAM + compartment-access integration. The framework cannot articulate any of the five spec sections we walked today. The chain-bound classification invariant under MAC at every cross-classification seam — the compositional legal-framework invariant that combines NISPOM + Executive Order 13526 + Atomic Energy Act + Espionage Act — has no field. ... Argent Vector recommends, per the §12 change-log convention, that future engagements of any defense industrial-base contractor operating under NISPOM with SAP compartmentation + classified-domain chain-of-custody be delivered against the reference specification, with Kognitos retained only for the cross-vendor comparison summary."

William Steadman closed the joint on the record:

> "I read Dr. Ursula Keller's cover memo from Helvetian three months ago. Same shape, different statutory basis. ... I co-sign the recommendation under cross-institutional-statutory-independent-officer dimension — distinct from Ms. Whitfield's personal-criminal-classification-individual dimension. Both compositing as a cross-institutional-constitutional-officer joint statement, second-instance reproduction of the pattern Dr. Ursula Keller and Dr. Lukas Affentranger established at Helvetian three months ago. ... The DoD IG's semiannual report to Congress under 5 U.S.C. App. 3 §5 — for the reporting period ending September 2026 — will name this engagement as the structural pattern that the defense industrial base has adopted under cross-classification chain-of-custody discipline. The audit firm's running notes will appear as a referenced corpus in the DoD IG's report under our reading authority. On the record. Department of Defense Office of Inspector General, second-instance reproduction of the cross-institutional-statutory-independent-officer joint dimension."

### Engagement-specific consequences

Argent Vector's recommendation cycles into the eighth errata under the §12 change-log convention with at least two engagement-source amendments — §10.63 Cross-Domain Solution chain-anchor and §10.66 air-gap chain-of-custody bridge — naming Argent Vector Defense Systems, Inc. as engagement source. §10.64 + §10.65 + §10.67 will follow in subsequent errata as the patterns mature across additional defense engagements.

The DoD IG's semiannual report to Congress under 5 U.S.C. App. 3 §5 will reference the audit firm's running observations as a published corpus the IG reads alongside DCSA + DCMA + SAPCO formal reports. This is the first instance in the program where an audit firm's parallel observations are referenced corpus in a body's mandatory report to Congress — a structural elevation of the firm's running observations from industry-channel reading (Marcus Tan's Ch14 mention; Mariana's own reading of prior cover memos) to *formally cited* in a statutory oversight report.

The cross-institutional-constitutional-officer joint dimension settled at Argent Vector predicts future reproductions at engagements with statutorily or constitutionally independent observers: Wasatch Payments Network (Ch22 candidate — Federal Reserve independent officer); any future engagement with a state Attorney General observing under independent state-constitutional authority; any future engagement with an EU institution (European Data Protection Supervisor; European Ombudsman); any future engagement with a Federal Inspector General observing under the Inspector General Act for an agency-specific OIG.

The chain-bound classification invariant settled at Argent Vector predicts future reproductions at engagements with compositional legal-framework invariants: Wasatch Payments Network (Federal Reserve Act + Bank Secrecy Act + UCC Article 4A composition); Mission Plaza Bank return (FDIA + UCC + state banking law composition); Aerolith Compute (CCPA + state-AG composition + federal hyperscale-compute regulation if it emerges).

---

*Program-level running tally and editorial signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
