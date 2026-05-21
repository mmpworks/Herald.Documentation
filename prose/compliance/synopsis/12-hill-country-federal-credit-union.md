# Story 12 — Hill Country Federal Credit Union (multi-state FCU under NCUA AIRES + CFPB §1033, marketing-AI vendor handover)

**Story file:** `docs/auditor-stories/12-hill-country-federal-credit-union.md`
**Engagement type:** Three-day pre-engagement readiness pass before NCUA AIRES examination three weeks out
**Posture going in:** Chained in production for 11 months across the full member-experience surface; AWS-resident; Herald.Core.Aws runs the chain on `us-east-1` with replicas in `us-east-2`; §10.21 (cross-vendor model-handover) shipped in a Herald release seven months ago — exactly when the FCU began the marketing-AI vendor transition
**Outcome posture:** Confirmation; foresight-cluster opener for Stories 12-17; the cross-vendor anchor primitive operates cleanly in its single-substrate AWS-only form and the lead auditor files a deliberate engagement-file note about the substrate axis

## Type of audit
Three-day engagement at Hill Country's Austin operations center before NCUA's AIRES examination opens in three weeks. The institution is a ~$8B federally-insured multi-state FCU with a Texas-plus-neighboring-states footprint. Six months ago it began a marketing-AI vendor handover — legacy Total Expert → HubSpot Marketing Hub plus an in-house ML scoring layer. The cross-vendor anchor was placed at handover initiation; the engagement confirms the §10.21 cross-vendor model-handover surface operated cleanly across the transition and is examinable by NCUA AIRES workpaper conventions. CFPB §1033 personal financial data rights are in scope as a cross-cut: every member-disclosure packet must remain producible across the vendor handover. ECOA / Reg B is the policy-vs-implementation surface where marketing-AI data first becomes load-bearing audit content — an auto-loan adverse-action linkage is the day's signature reconciliation.

## Interested parties (spec readers)
- **NCUA AIRES examiner** — Lead supervisor; consumes the spec-section confirmation memo first; runs the cross-vendor anchor verifier against the legacy Total Expert export and the new HubSpot + in-house ML chain
- **CFPB consumer-protection examiner** — §1033 personal financial data rights examiner; consumes §10.69 per-customer audit-trail subset disclosure across the vendor-boundary span
- **FCU Chief Audit Executive** — Has carried anxiety about the vendor-handover boundary for six months; consumes the §10.21 confirmation as the headline assurance
- **FCU Chief Marketing Officer** — Owns the handover; produces the legacy-vendor model card and the new in-house ML model card; cosigns the cross-vendor anchor attestation
- **FCU Chief Compliance Officer / ECOA counsel** — Marketing-to-credit-decision linkage; the auto-loan ECOA adverse-action case is the load-bearing example
- **Model Risk Management chair** — SR 11-7 substrate; legacy vs new ML scoring model risk; cross-vendor model-card lineage under the chain
- **Marketing-AI vendor (legacy)** — Total Expert engineering; produces the byte-identical handover dump and cooperates in §10.21 attestation
- **Marketing-AI vendor (new)** — HubSpot Marketing Hub + in-house ML team; receives the cross-vendor anchor and produces forward chain entries
- **Standards-body reviewer** — Single-substrate cross-vendor anchor is the canonical-reference shape for §10.21; the lead auditor's engagement-file note ("works on one substrate. what happens when the substrate moves?") becomes the seed wishlist memo for §10.40's cross-cloud extension
- **SDK implementer** — Cross-vendor handover SDK path on the new in-house ML side; chain entry emission across the boundary
- **Verifier implementer** — `audit.model_handover.*` dispatch on the legacy-vendor leaf and the byte-equality reconciliation against the anchored dump; `cross_vendor_handover_verified` marker emission per §10.12

## Top spec sections used
- **§10.21** — Cross-vendor model-handover (the headline; production for seven months; exercised end-to-end in the byte-equality demonstration on Day 1 afternoon)
- **§10.40** — Cross-vendor chain-merge anchor in single-substrate form; legacy Total Expert export hashed at handover, anchored inside the new HubSpot+ML chain, byte-equal verification
- **§10.69** — Per-customer audit-trail subset disclosure; CFPB §1033 right; member-disclosure packets that span the vendor handover
- **§10.11.1** — `audit.ecoa.adverse_action.*` family; the auto-loan adverse-action linkage where a marketing-AI event under the legacy vendor's scoring informs a credit decision under the new vendor's scoring; `prior_offer_run_id` / `prior_offer_seq` parent-linkage fields bind the prior marketing inference to the credit-decision entry
- **§10.19** — `audit.external_artifact.*` family that §10.40 reuses for the legacy-vendor export
- **§10.22** — Redaction discipline; PII redaction in member-disclosure packets that crossed the vendor boundary
- **§7** — Twelve-step verifier procedure; the cross-vendor-handover dispatch path

## All cited spec sections
- **§0.5.1** — Three-paragraph elevator pitch for NCUA-side executive orientation
- **§1.1** — Daubert four-factor grounding referenced in the ECOA-adverse-action subsection
- **§1.2** — Epistemic scope
- **§4** — Four primitives; per-event MAC, per-day Merkle seal, HSM-rooted root signature, in-process observation not spec-conformant
- **§4.1** — Per-tenant HKDF binding the cross-vendor anchor extends across the handover
- **§4.2** — Daily Merkle seal default cadence; production cadence on AWS CloudHSM `us-east-1`
- **§4.3** — HSM-rooted root signature; key fingerprint declared on both sides of the handover
- **§7** — Twelve-step verifier procedure including the §10.21 cross-vendor dispatch
- **§10** — Operational requirements
- **§10.5** — HSM custody at FIPS 140-2 Level 3+; AWS CloudHSM partition attestation
- **§10.11.1** — `audit.ecoa.adverse_action.*` family
- **§10.13** — Evidentiary artifacts composing with NCUA AIRES workpaper model
- **§10.17** — Partition-ceremony attestation; the §10.21 dual-signature pair (legacy vendor + new vendor) structurally identical to the §10.39/§10.42 dual-signature pair used in Story 14
- **§10.19** — `audit.external_artifact.*` for the legacy Total Expert export
- **§10.21** — Cross-vendor model-handover; the canonical single-substrate reference
- **§10.22** — Redaction discipline
- **§10.40** — Cross-vendor chain-merge anchor; this engagement exercises the single-substrate AWS-only form. The standards-body reviewer's open question (does §10.40 generalize across substrates) becomes the wishlist seed that PRD-1's cross-cloud extension answers
- **§10.69** — Per-customer audit-trail subset disclosure for the CFPB §1033 cross-cut
- **§13** — Stakeholder navigation; "credit union under NCUA AIRES + CFPB §1033" becomes a canonical stakeholder entry alongside the existing community-bank entries

## Synopsis

### Audit activity
Day 1 morning walks the §10.21 cross-vendor model-handover surface: the legacy Total Expert export (a 1.4-TB tar.gz of campaign history, member lists, A/B variant data, scoring artifacts, model cards, lineage metadata) was hash-anchored at the handover moment 23 weeks earlier; the hash was sealed into the new HubSpot+in-house-ML chain in the same daily Merkle seal that covers the first new-vendor chain entries. The verifier emits `cross_vendor_handover_verified` alongside exit code 0 on the legacy-vendor leaf; byte-equality between the on-disk Total Expert backup and the anchored hash reproduces in nine minutes.

Day 1 afternoon walks the ECOA reconciliation. Five members traced end-to-end; the load-bearing case is a member who received a "you're pre-qualified for a $35,000 auto loan at 6.250%" marketing offer under the legacy Total Expert ML scoring weights on a Tuesday in February, then applied for the loan under the new in-house ML scoring weights three weeks later, was AI-screened, and was approved at 6.625% on a slightly different term structure. The CMO asks whether the marketing-event-to-credit-decision linkage is ECOA-defensible. The audit answer: the marketing offer is in the chain as a model-inference event under the legacy §10.21 model-handover; the credit decision is in the chain under §10.11.1's `audit.ecoa.adverse_action.*` family; the linkage between them is bound via §10.11.1's `prior_offer_run_id` and `prior_offer_seq` parent-linkage fields on the credit-decision chain entry — the same parent-linkage pattern §10.11 already establishes for translation→decision, reused here for the prior-offer→decision pivot. Whether the policy is fair is a different question — but the institution can answer it now, with data, against an examiner's exact prompt.

Day 2 morning walks §10.69 per-customer disclosure across the vendor-boundary span: a CFPB §1033 disclosure request that spans the handover boundary must produce one unified per-member audit trail covering both the legacy-vendor era and the new-vendor era. Three §1033 disclosures are walked; each verifies in ~14 seconds against ~9,400 chain entries spanning 11 months. The verifier emits `customer_disclosure_subtree_verified` and `customer_disclosure_key_derivation_verified` on PASS. The disclosure subtree spans the cross-vendor anchor leaf cleanly — the legacy-vendor era's chain entries are members of the same subtree as the new-vendor era's entries, because the anchor binds them under one tenant-day Merkle seal.

Day 2 afternoon walks the NCUA AIRES workpaper composition: the spec-section confirmation memo on §10.21, §10.40 (single-substrate form), §10.69, and §10.11.1 is drafted under the AIRES workpaper conventions. The CAE drafts the AIRES references; the audit team signs the technical reproduction. Day 3 closes the engagement with the spec-section confirmation memo handed to the CAE for NCUA delivery, the MRM-committee memo on cross-vendor model-card lineage, and a quiet engagement-file note: *"§10.40 anchor reads as routine on AWS-only. Open question for the next pass: what happens when the substrate moves?"*

### How the spec was used
- **§10.21** — Production for seven months at the time of the engagement; the legacy Total Expert handover walks the canonical single-substrate cross-vendor reference end-to-end. Dual-signature pair from §10.17 (legacy CTO + new-vendor CTO) bound into the seal
- **§10.40** — Single-substrate form; the legacy export's hash is computed at handover, anchored inside the new chain's daily Merkle seal, and verified byte-equal at audit time. The §10.40 wishlist seed for cross-cloud generalization is identified
- **§10.69** — Disclosure subtree spans the cross-vendor anchor; one CFPB §1033 request returns one unified audit trail across both vendor eras
- **§10.11.1** — ECOA adverse-action linkage chain entry references the prior marketing-offer hash; the marketing-event-to-credit-decision chain pivot is in the chain
- **§10.22** — Member PII redacted in disclosure packets per policy; `redacted_per_§10.22` markers carry through
- **§10.13** — Chain artifacts compose with the NCUA AIRES workpaper model; the spec-section confirmation memo cites AIRES workpaper references alongside spec sections

### Results
Four spec-section confirmations land in production at a federally-insured FCU: §10.21 cross-vendor model-handover, §10.40 single-substrate cross-vendor anchor, §10.69 per-customer disclosure across the vendor boundary, §10.11.1 ECOA adverse-action linkage. Hill Country becomes the canonical credit-union institutional reference for §10.21 — first credit union in the corpus and first NCUA-supervised institution to exercise the cross-vendor anchor in production. The engagement-file note about cross-substrate behavior is filed quietly; it carries no public weight at the time and becomes the wishlist seed that §10.40's cross-cloud extension answers two engagements later. No findings; engagement closes 22% under budget. AIRES examination opens three weeks later with the spec-section confirmation memo on the examiner's desk before the entrance meeting.
