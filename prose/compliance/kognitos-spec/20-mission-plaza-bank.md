# 20 — Mission Plaza Bank — Kognitos-lens

*The second return engagement. Dawn back at Mission Plaza Bank's San Francisco headquarters sixteen months after the original clean baseline engagement; seven months after FDIC-assisted Purchase and Assumption of Argosy Pacific Bank, N.A. The chain in production fifty-one months on the original Mission Plaza perimeter; seven months on the inherited Argosy Pacific perimeter under FDIC-resolution receivership discipline. Five FDIC-receivership-specific reference-spec sections (§10.73 bridge-bank receivership chain inheritance + §10.74 FDIC-attestation chain-anchor + §10.75 loss-share agreement chain-anchor + §10.76 uninsured-depositor DIF reconciliation chain + §10.77 receivership-window temporal-slice with regulatory bridge-state binding) exercised in production at one institution for the first time in the program. Confirmation-posture engagement — the third in the program after Ch12 (Hill Country FCU) and Ch14 (Northbridge return). Five Framework Inarticulabilities surface in the FDIC-resolution shape; no on-the-record framework-substitution recommendation; institutional-memory closing observation from CAE Linda Marchetti lands as cover-memo prose rather than formal recommendation — second-instance reproduction of the Ch14 Marcus Tan pattern, settling the candidate fourteenth voice-pattern variant.*

**Engagement:** Two-day spec-section confirmation pass on the FDIC-assisted Purchase and Assumption integration before the OCC's post-failure-acquisition examination opens (four weeks out). Mission Plaza Bank has completed its FDIC-assisted P&A acquisition of Argosy Pacific Bank, N.A. — an $8.1B OCC-supervised national bank headquartered in Long Beach, California, placed into receivership by the OCC and FDIC on Friday 2025-10-17 at 17:00 PT after a deposit run triggered by examiner-ordered MOU disclosure. FDIC operated Argosy as a bridge bank for nine days (2025-10-17 through 2025-10-26) under the Division of Resolutions and Receiverships. Mission Plaza won the closed P&A bid and assumed deposits and selected assets at the 2025-10-26 17:00 PT close. The bridge-bank operating period was end-to-end chain-bound under FDIC's receivership-attestation discipline. Mission Plaza is now seven months past close. The institution upgraded to a release that shipped §10.73 through §10.77 four weeks before close. The audit firm received a request from Linda Marchetti for a spec-section confirmation pass before the OCC team arrives.
**Client:** Mission Plaza Bank — same institution from the audit firm's engagement archive sixteen months prior (clean baseline, not depicted; referenced as engagement-archive entry MPB-2024-Q4). ~$72B consolidated assets pre-acquisition; ~$78B post-P&A (Argosy Pacific added ~$6.1B in retained deposits + ~$1.2B in loss-share-covered commercial-real-estate loans; ~$800M in non-acquired assets resolved through DIF). OCC-supervised national bank, FDIC-insured. San Francisco Financial District HQ.
**Status:** Chain in production: fifty-one months on the original Mission Plaza perimeter (started fifteen months before the firm's MPB-2024-Q4 engagement). Seven months on the inherited Argosy Pacific perimeter under §10.73 FDIC bridge-bank receivership chain inheritance + §10.74 FDIC-attestation chain-anchor + §10.75 loss-share agreement chain-anchor + §10.76 uninsured-depositor DIF reconciliation + §10.77 receivership-window temporal-slice. Pre-failure baseline on the Argosy side: 4,317 daily seals on the original Argosy chain (vendor-equivalent to Mission Plaza's chain stack but a different HSM root + different IKM family + different tenant_id space) from 2022-08-12 through 2025-10-17 17:00 PT. Bridge-bank-period operations: 174 chain rows across nine days under FDIC-receivership attestation. Total inherited baseline: 4,317 daily seals + 174 bridge-bank rows cross-anchored under §10.74 FDIC-attestation chain-anchor.
**Audit team lead:** Dawn
**Returning audit team:** Mike (verifier operator); Diana (IAM & access control — relevant because the FDIC operated Argosy under bridge-bank credentials that were distinct from both the original Argosy IAM and the acquirer's IAM); Luis (retention & evidentiary floor — relevant because FDIC receivership records carry a thirty-year retention floor under 12 U.S.C. §1823(e)); Chen (template / framework-fit specialist). Elena and Tom not on this trip — the engagement shape does not exercise customer-side stacks materially, and the M&A integration office is sufficient without internal-audit-liaison support. The team is now twenty months past Ch14 and twenty engagements deep into Kognitos-checklist usage.
**Client liaisons:** Linda Marchetti (Chief Audit Executive — same CAE from the firm's MPB-2024-Q4 baseline engagement; calm, sixteen-month working relationship); Brad Killian (VP Strategic Integrations — acquirer); Carmen Lo (Acquired-entity transition lead, retained from Argosy Pacific's pre-failure management team after the 2025-10-17 receivership for the seven-month transition); Walter Singh (General Counsel — receivership evidentiary defensibility under 12 CFR Part 360 and 12 U.S.C. §1823); Gabriela Estrada (FDIC Division of Resolutions and Receiverships, retained through 24-month transition window for loss-share administration); Olivia Wendt-Park (Audit Committee chair, joining for Day 2 closing — former FDIC Office of Inspector General Deputy IG before joining Mission Plaza's board three years ago).

**Audit team's framework:** Kognitos's 12-field schema. Same printed twelve-row template Dawn has been using since Ch01. After twenty engagements the firm has accumulated a parallel internal-knowledge-base of framework-silent observations — roughly one hundred entries across all engagements, indexed by engagement and by spec-section. Dawn carries the relevant subset for return engagements: the firm's MPB-2024-Q4 margin notes against the original Mission Plaza architecture, plus the Ch14 Northbridge entries on the §10.24/§10.39/§10.40/§10.42 wave (the most analogous prior wave to the §10.73-§10.77 wave). The team walks in expecting a clean confirmation pass on the original perimeter and the FDIC-resolution surface — but they have not seen the §10.73-§10.77 wave's production exercise before. This is the first chapter where the FDIC-resolution-specific sections meet a real OCC-bound audit.

---

## 🌅 8:30 AM — Day 1 — Kickoff at Mission Plaza HQ, San Francisco

Dawn walked into the engagement room on the 41st floor of Mission Plaza Tower. Same view of the Bay Bridge she remembered from sixteen months ago. The same long walnut table. The same projector. The coffee station was new — Linda had moved it from the corner to the table-end after the firm's prior engagement had run long into the afternoon and the team had kept pouring from the wrong side of the room.

The intervening sixteen months had been twenty engagements across eleven countries. Dawn's printed twelve-row Kognitos template was the same one she had brought to the MPB-2024-Q4 baseline engagement. The firm's parallel knowledge-base had grown alongside it — indexed by engagement and by spec section.

Linda Marchetti walked in at 8:33 with the same calm. Late fifties, navy blazer, coffee in her left hand. She had been calm at the MPB-2024-Q4 baseline; she was calm now.

"Dawn. Welcome back."

Dawn shook her hand. "Linda. Same room."

"Same room. The coffee moved."

Linda introduced Brad Killian, who was the M&A integration lead — early forties, formerly with the FDIC's Closed Bank Operations group before joining Mission Plaza three years ago. Brad had spent the past seven months on the Argosy Pacific P&A from bid through close to the seven-month post-close evidentiary stabilization.

Carmen Lo, the Argosy Pacific transition lead, joined from a teleconference bridge. Carmen was based in Long Beach — the original Argosy Pacific HQ — and had been Argosy's Chief Risk Officer before the 2025-10-17 receivership. The FDIC had retained her through the bridge-bank period and Mission Plaza had retained her through the seven-month transition. She was the institutional memory on the Argosy side and the one who had cooperated with the bridge-bank attestation ceremonies during the nine-day FDIC operating period.

Walter Singh — Mission Plaza's General Counsel — joined briefly to greet the team and clarify that he would be available throughout the engagement for any §1.2 epistemic-scope or 12 U.S.C. §1823 receivership evidentiary-defensibility questions that surfaced during the audit. Walter would be the one to read the cover memo against OCC's likely post-failure-acquisition examination questions.

Gabriela Estrada from the FDIC Division of Resolutions and Receiverships joined by teleconference from Dallas. Gabriela was the FDIC liaison retained for the 24-month loss-share administration window — twenty years at the FDIC, eight at DOLR. She would not direct the engagement; her role was observer-with-standing-to-comment-on-§10.74-attestation-chain-anchor authenticity if any FDIC-attestation chain row surfaced as a question.

Linda opened.

"Two-day spec-section confirmation pass before the OCC post-failure-acquisition examination opens. The OCC team arrives in four weeks. I want a clean spec-section confirmation memo from your team that names what the chain demonstrates on the inherited Argosy Pacific perimeter and how the receivership-resolution sections behaved against the nine-day bridge-bank period and the seven-month post-close stabilization. The chain has been running on the original Mission Plaza perimeter for fifty-one months — including the sixteen months since you last visited. The chain has been running on the inherited Argosy Pacific perimeter for seven months. We exercise five FDIC-resolution-specific spec sections this week: §10.73 bridge-bank receivership chain inheritance; §10.74 FDIC-attestation chain-anchor for the receivership-period rows; §10.75 loss-share agreement chain-anchor for the $1.2B CRE loan portfolio under FDIC indemnification; §10.76 uninsured-depositor reconciliation chain witnessing the DIF transfer for the $312M uninsured deposit balance; §10.77 receivership-window temporal-slice with regulatory bridge-state binding."

Dawn nodded. She had not heard those five section numbers before in any of the firm's engagement archive. They were new to her under Kognitos's lens.

She uncapped her pen.

"Same twelve-row template," she said. "I'll walk what the framework can confirm. We'll mark the rest in the firm's parallel observations."

Linda nodded. She had heard the phrase "parallel observations" from her before. At MPB-2024-Q4 she had used it once, at the closing, to describe what the cover memo had to carry. Sixteen months later she was using it again, and Linda heard the change in usage. It was no longer a placeholder for one-off cover-memo prose; it had become an internal corpus.

"Same drill," she said. "I look forward to reading both."

*Note for the chapter. Second return engagement in the program. The audit team and the institution have prior history; the framework does not. The Kognitos twelve-row template Dawn carries today is byte-equal to the one she carried to MPB-2024-Q4; the framework has not moved in sixteen months. The reference spec has absorbed engagement-source amendments from Helvetian (Ch17 — seventh errata; §10.40 cross-jurisdictional-cross-cloud + §10.59 OECD CRS) + Argent Vector (Ch18 — eighth errata; §10.63 CDS + §10.66 air-gap bridge) + Aerolith Compute (Ch19 — ninth errata; §10.68 dual-algorithm seal + §10.69 substrate downstream-reference graph) since Linda last saw the firm. The framework-grows-vs-fixed contrast that Sun-Won named on the record in Ch09 has continued unbroken since. Three consecutive errata cycles with two engagement-source amendments each is the strongest sustained §12 amendment cadence in the program — and the framework's twelve rows are still the same twelve rows.*

## 🏛 9:30 AM — Day 1 — §10.73 bridge-bank receivership chain inheritance walkthrough

Brad took the projector. He brought up the §10.73 bridge-bank chain inheritance record from the 2025-10-26 P&A close — a single chain entry produced at 17:00:02 PT, the moment Mission Plaza assumed control of the bridge-bank chain rows.

```json
{
  "entry_id": "missionplaza/institutional-events/2025-10-26#bridge-inheritance-001",
  "tenant": "missionplaza",
  "service": "institutional-events",
  "event_class": "iam",
  "audit.receivership.kind": "bridge_bank_pa_acquisition",
  "audit.receivership.failed_institution_legal_name": "Argosy Pacific Bank, N.A.",
  "audit.receivership.failed_institution_lei": "549300APBNA2022B6",
  "audit.receivership.failed_institution_charter_number": "OCC-24817",
  "audit.receivership.receivership_open_utc": "2025-10-17T17:00:00.000-07:00",
  "audit.receivership.receivership_open_authority": "OCC-FDIC-joint-action",
  "audit.receivership.bridge_bank_operator": "FDIC-DOLR",
  "audit.receivership.bridge_bank_period_start_utc": "2025-10-17T17:00:00.000-07:00",
  "audit.receivership.bridge_bank_period_end_utc": "2025-10-26T17:00:00.000-07:00",
  "audit.receivership.bridge_bank_row_count": 174,
  "audit.receivership.acquirer_legal_name": "Mission Plaza Bank",
  "audit.receivership.acquirer_lei": "549300MPB2021A3",
  "audit.receivership.acquirer_hsm_key_fingerprint": "7d:91:a4:c8:35:e2:1b:..." ,
  "audit.receivership.pa_close_utc": "2025-10-26T17:00:00.000-07:00",
  "audit.receivership.pa_agreement_sha256": "c4f1...a82d",
  "audit.receivership.fdic_attestation_chain_anchor_ref": "fdic-dolr/2025-10-26#attestation-argosy-pa",
  "audit.receivership.loss_share_agreement_chain_anchor_ref": "missionplaza/loss-share/2025-10-26#agreement-001",
  "audit.receivership.dif_reconciliation_chain_anchor_ref": "missionplaza/dif-reconciliation/2025-10-26#reconciliation-001",
  "audit.receivership.companion_backfill_seal_run_id": "missionplaza/seals/backfill/2025-10-26#bf001",
  "audit.receivership.tri_signatures": {
    "receiver": {
      "signer_role": "FDIC DOLR Resolution Officer",
      "signer_identity": "fdic-dolr:G-Estrada-2025-10-26",
      "hsm_key_fingerprint": "3a:8e:2c:f1:...",
      "ts": "2025-10-26T16:58:42.117-07:00"
    },
    "failed_entity_retained_officer": {
      "signer_role": "Argosy Pacific CRO (retained through transition)",
      "signer_identity": "argosy-cro:C-Lo-2025-10-26",
      "hsm_key_fingerprint": "5d:7b:09:a3:...",
      "ts": "2025-10-26T16:59:11.482-07:00"
    },
    "acquirer": {
      "signer_role": "Mission Plaza CFO",
      "signer_identity": "mpb-cfo:M-Salazar-2025-10-26",
      "hsm_key_fingerprint": "7d:91:a4:c8:...",
      "ts": "2025-10-26T17:00:01.293-07:00"
    }
  },
  "hmac": "...",
  "merkle_path": [...],
  "daily_seal_ref": "missionplaza/2025-10-26#seal"
}
```

Brad walked the fields aloud. Failed-institution legal name + LEI + OCC charter number (validated against the OCC chartered-bank registry at close). Receivership-open authority `OCC-FDIC-joint-action` — the OCC closed the bank; the FDIC was appointed receiver under 12 U.S.C. §1821(c). Bridge-bank operator `FDIC-DOLR` for the nine-day period during which the FDIC's Division of Resolutions and Receiverships ran Argosy as a bridge bank. Bridge-bank row count: 174 chain entries produced under FDIC operating authority across the nine days. P&A agreement SHA-256 over the JCS-canonicalized purchase-and-assumption agreement. Four bidirectional cross-references to companion chain anchors: §10.74 FDIC-attestation, §10.75 loss-share, §10.76 DIF reconciliation, plus the companion backfill seal.

The structurally novel part was the tri-signature pair. Where §10.39 (Northbridge Ch14) bound dual-signatures (from-entity CFO + to-entity CFO), §10.73 bound three: the FDIC DOLR Resolution Officer as receiver, the failed-entity's retained CRO as the institutional-memory signer for the bridge-bank period operating record, and the acquirer's CFO. Three HSM keys; three signatures; three structurally distinct roles bound under one entity-succession event.

The verifier ran in strict mode and returned:

```
$ herald-verify --tenant=missionplaza \
                --service=institutional-events \
                --entry-id="2025-10-26#bridge-inheritance-001" \
                --strict

[OK] entry hash matches
[OK] HMAC valid (IKM:missionplaza-base, derived for tenant=missionplaza)
[OK] tri_signatures.receiver verified against FDIC DOLR-published HSM key
[OK] tri_signatures.failed_entity_retained_officer verified against
     archived Argosy HSM key (released to receiver by OCC at 2025-10-17 17:00 PT)
[OK] tri_signatures.acquirer verified against Mission Plaza acquirer-side HSM key
[OK] pa_agreement_sha256 cross-binds against §10.75 loss-share anchor
[OK] fdic_attestation_chain_anchor_ref resolves to fdic-dolr/2025-10-26#attestation-argosy-pa
[OK] dif_reconciliation_chain_anchor_ref resolves
[OK] companion_backfill_seal_run_id resolves to missionplaza/seals/backfill/2025-10-26#bf001
[OK] daily seal chain integrity through 2025-10-26#seal
[OK] additional_verifications: ['bridge_bank_inheritance_verified',
                                  'tri_signature_pair_verified',
                                  'fdic_attestation_anchor_resolved',
                                  'pa_agreement_sha_cross_bound',
                                  'loss_share_anchor_resolved',
                                  'dif_reconciliation_anchor_resolved']
[OK] exit code: 0
```

Six additional verifications. Eleven steps. Verifier returned in 2.4 seconds.

Dawn walked the Kognitos checklist against the §10.73 row. Field 1 (timestamp) matched. Field 11 (hash chain) matched. Field 12 (tamper-evident proof) matched in the sense that the hash chain and HMAC and HSM signatures were all defensible — but Field 12's singular wording could not articulate that the verifier returned *six additional verifications alongside* the exit code; the multi-axis verdict mechanism from §10.12 was again the surface that produced the gap, the same gap surfaced at Ch14 with one additional verification, Ch15 with two, Ch16 with four, Ch17 with six (cluster-closing), Ch18 with five, Ch19 with six. At Ch20, six again. The framework's twelve rows could not file the structure of a verdict object that carried `additional_verifications: ['bridge_bank_inheritance_verified', ...]` — under any reading.

Field 2 (actor identity) form-mismatched. Kognitos's mental model was a session-authenticating actor running a single AI inference. A tri-signature pair under HSM-rooted attestation by three structurally distinct roles — one receiver, one retained officer of a failed entity, one acquirer's CFO — was not a session identity. The framework had no slot for a three-role institutional-succession event under federal banking receivership authority.

She wrote in the parallel observations: *§10.73 bridge-bank receivership chain inheritance: structurally a three-role institutional-succession event composing §10.74 FDIC-attestation chain-anchor + §10.75 loss-share agreement + §10.76 DIF reconciliation + §10.42 (Ch14) backfill seal pattern. Field 2 form-mismatches against tri-signature pair. Field 12 form-mismatches against six-axis verdict object. The framework's mental model for entity-succession was authored at Northbridge Ch14 around dual-signatures from-entity + to-entity; FDIC-resolution receivership adds the receiver as a third role bound under HSM-rooted attestation, and the receiver's HSM is operated under federal-receivership authority rather than commercial M&A authority.*

> ### ⚠ Framework Inarticulability #1 — §10.73 bridge-bank receivership chain inheritance
> Kognitos's twelve-row schema has no concept of FDIC-receivership entity-succession discipline. The §10.73 row binds three signatures under HSM-rooted attestation by three structurally distinct roles (FDIC DOLR Resolution Officer as receiver + failed-entity's retained officer + acquirer's CFO) where Ch14's §10.39 dual-signature pattern bound only two. The framework's row-shape for entity-succession admits at most one acquirer-side actor identity under Field 2; the tri-signature pair under federal-receivership authority is structurally invisible.

## 🏛 11:00 AM — Day 1 — §10.74 FDIC-attestation chain-anchor walkthrough

Brad and Gabriela walked the §10.74 FDIC-attestation chain-anchor. This was the chain anchor that bound the 174 chain rows produced under FDIC bridge-bank operating authority during the nine-day receivership period (2025-10-17 17:00 PT through 2025-10-26 17:00 PT).

The structurally novel part of §10.74 was that the chain rows had been produced under an HSM key controlled by the FDIC, not by Argosy Pacific or Mission Plaza. During the bridge-bank period, the FDIC DOLR Resolution Officer (Gabriela Estrada, on-site at Argosy's Long Beach HQ from 2025-10-17 through 2025-10-26) had operated Argosy's chain SDK under a FDIC-published bridge-bank HSM key (`3a:8e:2c:f1:...`) for institutional-events and customer-facing transactions. Argosy's original chain HSM keys had been released to FDIC custody at 2025-10-17 17:00 PT under OCC-supervised key-transfer ceremony.

The 174 bridge-bank rows broke down:
- 31 customer-facing transaction rows (depositor withdrawals at the eight largest branches; the rest of Argosy's deposit base had been frozen on Saturday morning)
- 47 institutional-events rows (FDIC closing inventory, asset-disposition decisions, employee-retention attestations)
- 96 reconciliation rows (legacy Argosy systems verified against bridge-bank state for the P&A bid process)

Each of the 174 rows carried `audit.bridge_bank.operator = "FDIC-DOLR"` + `audit.bridge_bank.operating_period_id = "argosy-pa-2025-10"` + `audit.bridge_bank.receiver_hsm_key_fingerprint = "3a:8e:2c:f1:..."` MAC-bound at capture. The §10.74 anchor row produced at 2025-10-26 17:00 PT — alongside the §10.73 bridge-bank inheritance row — bound all 174 row hashes under one Merkle root cross-signed by the FDIC DOLR Resolution Officer and the Mission Plaza CFO.

```json
{
  "entry_id": "fdic-dolr/2025-10-26#attestation-argosy-pa",
  "tenant": "fdic-dolr",
  "service": "receivership-attestation",
  "event_class": "iam",
  "audit.fdic_attestation.kind": "bridge_bank_period_close_attestation",
  "audit.fdic_attestation.failed_institution_charter_number": "OCC-24817",
  "audit.fdic_attestation.operating_period_id": "argosy-pa-2025-10",
  "audit.fdic_attestation.bridge_bank_row_count": 174,
  "audit.fdic_attestation.bridge_bank_merkle_root_sha256": "8e4f...2b91",
  "audit.fdic_attestation.dolr_resolution_officer_signature": {
    "signer_identity": "fdic-dolr:G-Estrada-2025-10-26",
    "hsm_key_fingerprint": "3a:8e:2c:f1:...",
    "ts": "2025-10-26T16:55:08.392-07:00"
  },
  "audit.fdic_attestation.acquirer_cross_signature": {
    "signer_identity": "mpb-cfo:M-Salazar-2025-10-26",
    "hsm_key_fingerprint": "7d:91:a4:c8:...",
    "ts": "2025-10-26T17:00:33.819-07:00"
  },
  "audit.fdic_attestation.federal_register_publication_ref": "FR-90-FR-26417",
  "audit.fdic_attestation.dolr_internal_case_ref": "DOLR-2025-CA-0817",
  "hmac": "...",
  "merkle_path": [...],
  "daily_seal_ref": "fdic-dolr/2025-10-26#seal"
}
```

Gabriela walked the row aloud. The structural property she named was that the FDIC's HSM key was published in the Federal Register at FR-90-FR-26417 with a publication date of 2025-10-30 and that the key was time-bounded — its validity window was exactly the nine-day bridge-bank operating period. The §10.74 attestation row carried the Federal Register publication reference under MAC. Any verifier walking the 174 bridge-bank rows would resolve the FDIC HSM key from the Federal Register entry, validate that the row's timestamp fell within the published validity window, and validate the signature. After 2025-10-26 17:00 PT, the FDIC HSM key was structurally invalid for new chain rows; the key remained valid for verification of the 174 already-produced rows in perpetuity.

Mike walked the verifier through all 174 rows. The verifier resolved the FDIC HSM key from the published Federal Register entry. Each row's timestamp fell within the published validity window. Each row's signature validated. The Merkle root computed from the 174 row hashes matched the `bridge_bank_merkle_root_sha256` in the §10.74 anchor row byte-for-byte. The verifier completed in 4.7 seconds across all 174 rows.

Dawn walked the §10.74 anchor against the Kognitos checklist. The framework had no field for *a chain row whose signing authority is published in the Federal Register and is time-bounded to a specific receivership operating period*. Field 2 (actor identity) admitted at most one institution-side identity; the FDIC DOLR Resolution Officer operating under federal-receivership authority during a nine-day window was a structurally distinct identity kind. Field 6 (source attribution) admitted free text but had no slot for the Federal Register publication reference under MAC. Field 12 (tamper-evident proof) could not articulate the time-bounded validity window property.

She wrote in the parallel observations: *§10.74 FDIC-attestation chain-anchor introduces federal-receivership-signing-authority as a chain-bound concept. The signing authority is published in the Federal Register, time-bounded to the bridge-bank operating period, and structurally distinct from both the failed institution's pre-failure signing authority and the acquirer's post-close signing authority. The receivership-attestation chain row is the institutional witness for the bridge-bank period; without it, the 174 rows produced under FDIC operating authority would have no defensible signing-authority binding in evidence.*

> ### ⚠ Framework Inarticulability #2 — §10.74 FDIC-attestation chain-anchor (federal-receivership-signing-authority binding)
> Kognitos's row-shape admits one actor-identity per chain row under Field 2. The §10.74 anchor binds *federal-receivership-signing-authority* as a third structurally distinct identity kind — distinct from pre-failure institutional identity and post-close acquirer identity — published in the Federal Register and time-bounded to a nine-day bridge-bank operating window. The framework has no slot for federal-receivership-signing-authority as a chain-bound concept; the auditor speculates that the bridge-bank rows are "covered" without structural footing for the receivership-attestation binding.

## 🏛 1:30 PM — Day 1 — §10.75 loss-share agreement chain-anchor walkthrough

After lunch, Brad and Gabriela walked the §10.75 loss-share agreement chain-anchor. The structural feature was the FDIC's indemnification of $1.2B of acquired commercial-real-estate loans under a 24-month loss-share agreement — a standard FDIC P&A clause designed to transfer credit-risk on the failed bank's distressed asset portfolio to the acquirer's books while keeping FDIC on the hook for loss-share-covered losses.

The loss-share agreement chain anchor bound:
- The $1.2B portfolio identifier (227 individual CRE loans)
- The per-loan SHA-256 of each loan's underwriting file (227 hashes)
- The Merkle root across all 227 loan files
- The FDIC loss-share-coverage percentages by tranche (80% on Tranche A first-loss; 95% on Tranche B catastrophic-loss)
- The reserve-account chain-anchor reference (the segregated reserve account where Mission Plaza held the FDIC's contingent reimbursement obligation)
- The cross-entity settlement reference to FDIC's internal claims-administration anchor
- Tri-signatures (FDIC DOLR + Mission Plaza CFO + Mission Plaza CRO)

The structurally novel part was the deterministic-arithmetic indemnification clause. Each chargeoff event against a loss-share-covered loan would produce a chain row carrying the chargeoff amount + the tranche identifier + the deterministic-arithmetic indemnification calculation (e.g., chargeoff $4.7M on Tranche A → FDIC reimbursement $3.76M = 80% × $4.7M). The chargeoff chain row would parent-link to the §10.75 anchor row under MAC, and the FDIC claims-administration would walk the chain-bound reference graph at quarterly settlement.

Gabriela walked the row. She had administered ninety-four prior FDIC loss-share agreements during her DOLR tenure. The §10.75 anchor was the first one she had administered where the deterministic-arithmetic indemnification clause was chain-bound rather than spreadsheet-derived. The FDIC's claims-administration office had piloted chain-bound loss-share administration on the Argosy Pacific resolution because Mission Plaza had been running the chain stack for fifty-one months and the bridge-bank period had already been chain-bound. The pilot had received approval from the FDIC's Chief Financial Officer two weeks before close.

Dawn walked the §10.75 anchor against the Kognitos checklist. The chain-as-input pattern from Polaris Ch15 (component_chain_refs as inputs to aggregation row) appeared again — the §10.75 anchor referenced 227 per-loan chain rows as the input set, and the chargeoff chain rows referenced the §10.75 anchor as parent. The framework's mental model for chain rows admitted hash-chain integrity (Field 11) and parent-event linkage (Field 8) at one-level depth; the deterministic-arithmetic indemnification rule binding chargeoff-amount and FDIC-reimbursement-amount under MAC was structurally invisible to Field 8.

> ### ⚠ Framework Inarticulability #3 — §10.75 loss-share agreement chain-anchor (deterministic-arithmetic indemnification under MAC)
> Kognitos's Field 8 (decision rationale) admits free text. The §10.75 anchor binds *deterministic-arithmetic indemnification* as a chain-bound calculation rule (e.g., 80% × chargeoff_amount for Tranche A; 95% × chargeoff_amount for Tranche B) MAC-bound at capture and walked by FDIC claims-administration at quarterly settlement. The framework has no slot for chain-bound arithmetic indemnification calculation; the FDIC pilot's chain-bound loss-share administration is structurally invisible to Kognitos.

## 🏛 3:30 PM — Day 1 — §10.76 uninsured-depositor DIF reconciliation chain walkthrough

The §10.76 anchor was the chain witness for the FDIC's reconciliation of Argosy Pacific's uninsured deposit balance through the Deposit Insurance Fund. At 2025-10-17 17:00 PT, Argosy had $312M in uninsured deposits across 47 accounts (mostly large commercial customers; a few high-net-worth households). Under the standard P&A structure, FDIC had paid the insured portion ($250K per depositor) immediately on Monday 2025-10-20 from the DIF. The uninsured portion had been resolved through the receivership claims process — uninsured depositors received pro-rata distributions as Argosy's non-acquired assets were liquidated.

The §10.76 anchor bound:
- The 47 uninsured-depositor records (each with depositor identifier + uninsured balance + claim sequence number)
- The DIF transfer transaction reference (the FDIC's claims-administration entry that recorded the DIF disbursement)
- The pro-rata distribution schedule (initial 35% at close; subsequent 28% at 90 days; final 12% at 180 days from non-acquired asset liquidation; remaining 25% loss to depositors as final pro-rata claim)
- The cross-entity settlement reference to FDIC's claims-administration anchor
- Tri-signatures (FDIC DOLR + FDIC Claims Administration Officer + Mission Plaza CFO)

The structurally novel part was the **multi-installment-disbursement structure with terminal-loss recognition**. Where the §10.75 loss-share row tracked open-ended chargeoff-and-reimbursement events, the §10.76 row tracked a closed schedule of three pro-rata distributions plus terminal-loss recognition for the remaining 25%. Each distribution chain row parent-linked to the §10.76 anchor under MAC; the terminal-loss chain row carried `terminal_loss_amount_held: true` MAC-bound at capture.

Mike walked the verifier through the seven chain rows that had already produced under §10.76 in the seven months since close — the close-day initial disbursement, the 90-day-mark second disbursement (still pending settlement at the time of the audit), and five reconciliation rows from the asset-liquidation pipeline. The verifier resolved all seven references and produced exit code 0 + three additional verifications (`pro_rata_distribution_held`, `cross_entity_settlement_resolved`, `terminal_loss_not_yet_recognized`).

Dawn walked the row. The Kognitos framework had no concept of *a closed-schedule multi-installment cross-entity disbursement with terminal-loss recognition under MAC*. Field 6 (source attribution) and Field 8 (decision rationale) admitted free text; neither slot could carry the structured disbursement-schedule binding. Field 11 (hash chain) admitted parent-event linkage; the cross-entity settlement reference to the FDIC claims-administration anchor was a structurally distinct linkage kind from intra-institution parent-event linkage.

> ### ⚠ Framework Inarticulability #4 — §10.76 uninsured-depositor DIF reconciliation chain (multi-installment cross-entity disbursement with terminal-loss recognition under MAC)
> Kognitos has no field for a closed-schedule multi-installment cross-entity disbursement under federal-receivership claims administration. The §10.76 anchor binds three structured pro-rata distributions + one terminal-loss recognition event under MAC, with each disbursement chain row parent-linking to the anchor and cross-entity settlement references to FDIC claims administration. The framework's Field 8 free-text rationale slot cannot articulate the structured disbursement-schedule binding; the cross-entity settlement reference is structurally invisible.

## 🏛 4:30 PM — Day 1 — End-of-day whiteboard

Dawn walked to the whiteboard with one marker. Day 1 had exercised §10.73 (bridge-bank inheritance) + §10.74 (FDIC-attestation) + §10.75 (loss-share agreement) + §10.76 (DIF reconciliation). Day 2 would walk §10.77 (receivership-window temporal-slice). Ten records traced end-to-end through the receivership-window and post-close partitions after lunch. Closing memo at noon. Same drill.

She wrote on the whiteboard:

```
Mission Plaza Bank — Argosy Pacific FDIC P&A
Day 1 close:
  §10.73 ✓  bridge-bank receivership chain inheritance
  §10.74 ✓  FDIC-attestation chain-anchor (federal-receivership-signing-authority)
  §10.75 ✓  loss-share agreement chain-anchor (deterministic-arithmetic indemnification)
  §10.76 ✓  uninsured-depositor DIF reconciliation chain
  §10.77 ⧗  receivership-window temporal-slice (Day 2)

Kognitos:
  Field 1 ✓  timestamp
  Field 6 partial  source attribution (174 bridge-bank rows partially)
  Field 11 ✓  hash chain
  Field 12 ✓  tamper-evident proof (but multi-axis verdict mechanism partial)

Framework Inarticulabilities (Day 1): 4
  #1 §10.73 tri-signature pair (federal-receivership entity-succession)
  #2 §10.74 federal-receivership-signing-authority binding
  #3 §10.75 deterministic-arithmetic indemnification under MAC
  #4 §10.76 multi-installment cross-entity disbursement with terminal-loss recognition

Framework-Silent Observations (Day 1): 5
  - Federal Register publication of receiver HSM key, time-bounded validity
  - Chain-as-input + chain-as-parent reuse from Polaris Ch15
  - Three-role tri-signature extending Ch14 dual-signature pattern
  - FDIC chain-bound loss-share administration pilot
  - Three-instance chain-bound constitutional-level invariant precedent from Ch17-Ch19
```

Linda walked back in at 4:40 PM. She read the whiteboard quietly. She did not interrupt Dawn.

Brad pulled up the firm's MPB-2024-Q4 engagement file on the projector. The original engagement had landed five Framework Confirmations and one Framework Partial (a runbook cross-reference Nit). Today Day 1 had landed four Framework Inarticulabilities. The architectural reach of Mission Plaza's chain had grown materially in sixteen months. The Kognitos framework had not.

Dawn capped her pen.

"Same shape we've seen at twenty other engagements. The chain runs clean — the framework records partial. The architectural depth of why the chain runs clean — the four FDIC-resolution sections walked today, the §10.77 walk tomorrow — sits in the parallel observations. Chen, can you pull the firm's M&A-receivership archive against §10.73 from Ch14?"

Chen flipped through her laptop.

"Ch14 (Northbridge Federal Savings return — Cumberland Heritage M&A) is the closest prior chapter to §10.73 in structural shape. At Northbridge, §10.39 successor-attestation envelope bound a dual-signature pair (from-entity CFO + to-entity CFO) for a planned-M&A close. §10.73 extends the entity-succession family by adding a third signature — the receiver (FDIC DOLR Resolution Officer in this case) — for FDIC-resolution receiverships. The structural distinction is sharp: planned M&A is a two-party transaction; FDIC resolution is a three-party transaction with the receiver as a structurally distinct role bound under federal-receivership authority during a published time-bounded operating window."

"And the composition with §10.74 / §10.75 / §10.76?"

Chen: "Composes through bidirectional cross-references like the Ch14 wave (§10.39 envelope ↔ §10.42 backfill seal). At Ch20 the bridge-bank-inheritance row (§10.73) cross-references the FDIC-attestation anchor (§10.74) bidirectionally; the §10.75 loss-share agreement and §10.76 DIF reconciliation each carry their own anchor rows bidirectionally cross-referenced from the §10.73 row. Five sections, four bidirectional cross-references through the §10.73 hub. Pre-mortem rejected hub-and-spoke without bidirectional cross-references because that would have allowed a chain row to claim membership in the receivership-wave without the wave-hub row witnessing it back."

Dawn wrote on the whiteboard: *§10.73-§10.77 wave bidirectional cross-reference discipline exercised at Day 1 walkthroughs; §10.77 walkthrough Day 2 9:00 AM.*

She turned to the team.

"Day 2 we walk §10.77 receivership-window temporal-slice in the morning. Ten records traced end-to-end through the receivership-window and post-close partitions after lunch. Linda, Brad, Carmen, Gabriela all join for the closing memo at noon. Olivia Wendt-Park — the Audit Committee chair — sits in for the close. Walter Singh on standby for any §1.2 questions that surface. We'll close before 1:00 PM. Same drill."

Mike picked up his coat.

"Linda said 'same drill, the coffee moved' at kickoff. She wasn't wrong. The framework's row-shape hasn't changed in sixteen months. The chain's structural reach has."

*Note for the chapter. Day 1 closed with four Framework Inarticulabilities (one pending on §10.77 receivership-window temporal-slice Day 2) and four Framework Confirmations. The audit-team-side accumulated knowledge — one-hundred-ish observations indexed by engagement and spec section across twenty engagements — read the FDIC-resolution wave in four hours and named what the framework could not. Sixteen months is enough operational time at one institution to test whether the parallel-observations discipline reproduces across a return engagement with a structurally distinct M&A wave. It does. The framework itself is unchanged. The reference spec is wider by nine engagement-source amendments since Ch11 (the most recent two-amendment errata pair before this engagement). Same drill. Different shape.*

## 📋 9:00 AM — Day 2 — §10.77 receivership-window temporal-slice walkthrough

Brad opened Day 2 with the §10.77 walk. The receivership-window temporal-slice was the spec section that extended §10.41's M&A temporal-slice (Northbridge Ch14) to FDIC-resolution receiverships, adding a fourth named partition: **bridge-bank-period**.

§10.41 (Ch14) had named three partitions: pre-acquisition / cut-over-window / post-cut-over. §10.77 named four: **pre-failure** (failed institution's chain rows under its own signing authority, from chain inception through receivership-open at 2025-10-17 17:00 PT) + **bridge-bank-period** (174 rows under FDIC operating authority across 2025-10-17 through 2025-10-26) + **cut-over-window** (acquirer's first 72 hours under the chain, 2025-10-26 17:00 PT through 2025-10-29 17:00 PT) + **post-cut-over** (acquirer-side ongoing chain).

The structurally novel partition was the bridge-bank-period — a temporally-bounded interval where the chain rows were produced under federal-receivership authority rather than commercial-institution authority. Under §10.77, every chain row's partition assignment was derivable deterministically from the row's timestamp and the bridge-bank operating window. Cross-partition queries (e.g., "which Argosy CRE loans were re-underwritten between pre-failure and post-cut-over?") walked the §10.77 partition assignments deterministically without ambiguity.

Brad explained the design choice. The pre-mortem had rejected three alternatives. First, treating the bridge-bank-period as a sub-partition of cut-over-window — rejected because the bridge-bank-period was structurally distinct from cut-over-window (different signing authority, different operating institution, different regulatory framing). Second, omitting the bridge-bank-period as a named partition and letting verifiers infer it from the FDIC-attestation anchor — rejected because partition assignment needed to be deterministic without requiring resolution of the anchor reference. Third, adding more than four partitions (e.g., "OCC enforcement period" before pre-failure or "loss-share administration period" after post-cut-over) — rejected because four partitions covered the structurally distinct receivership-resolution shapes and additional partitions would have fragmented the temporal-slice mental model.

Four partitions as the canonical structure for FDIC-resolution temporal-slicing.

Dawn walked the amendment against the Kognitos checklist. The framework had no concept of partition assignment at all. The Northbridge Ch14 §10.41 three-partition discipline had been structurally invisible to Kognitos; the §10.77 four-partition extension was equally structurally invisible. The framework's mental model had been authored for *one institution capturing one row at one timestamp under one signing authority*; it had no slot for temporal partitioning across signing-authority transitions.

She wrote in the parallel observations: *§10.77 receivership-window temporal-slice extends §10.41 from three partitions to four by adding the bridge-bank-period partition. The bridge-bank-period is the structurally novel temporal interval — chain rows produced under federal-receivership operating authority during a published time-bounded window. Under the reference spec, every row's partition assignment is deterministic from the row's timestamp plus the receivership operating window. Under Kognitos, partition assignment is not a concept; cross-partition queries are not articulable.*

> ### ⚠ Framework Inarticulability #5 — §10.77 receivership-window temporal-slice (four-partition discipline with bridge-bank-period)
> Kognitos's row-shape has no concept of partition assignment. The §10.77 four-partition discipline (pre-failure + bridge-bank-period + cut-over-window + post-cut-over) extends Ch14's §10.41 three-partition shape by adding bridge-bank-period as a structurally distinct temporal interval under federal-receivership signing authority. The framework has no slot for partition assignment derived from timestamp + signing-authority window; cross-partition queries that the institution uses to answer OCC examination questions (e.g., "which pre-failure CRE loans were re-underwritten in post-cut-over?") are structurally invisible.

## 🔧 11:00 AM — Day 2 — Ten records traced through the four partitions

After the §10.77 walk, Mike and Diana took the diversity-sample exercise. Brad had pre-pulled ten records spanning the four partitions:

1. **Pre-failure, 2023-04-12** — Argosy Pacific commercial-real-estate underwriting decision; signed by Argosy CRO under Argosy's pre-failure HSM key; chain row hash anchored under §10.74 FDIC-attestation seal at receivership close (chain row produced under Argosy's authority but transferred to FDIC custody during bridge-bank period).

2. **Pre-failure, 2024-09-30** — Argosy Pacific consumer credit-decision (subprime auto); SHA-256 verified against archive contents in 0.6s; one of the 4,317 daily seals; bound under §10.74 attestation anchor.

3. **Pre-failure, 2025-10-15** — Argosy Pacific deposit-account update (two days before receivership); SHA-256 verified; bound under §10.74.

4. **Bridge-bank-period, 2025-10-19 14:23 PT** — branch deposit withdrawal at Argosy's Pasadena branch on the Sunday after receivership; chain row produced under FDIC DOLR operating authority; signed under FDIC HSM key (`3a:8e:2c:f1:...`); bound under §10.74 with `audit.bridge_bank.operator = "FDIC-DOLR"` MAC-bound at capture.

5. **Bridge-bank-period, 2025-10-23 09:11 PT** — FDIC closing-inventory reconciliation row for Argosy's Tustin commercial branch; produced under FDIC operating authority; bound under §10.74.

6. **Cut-over-window, 2025-10-27 09:42 PT** — first chain row produced under Mission Plaza's HSM key for the inherited Argosy perimeter (Long Beach branch deposit withdrawal); cross-references §10.73 bridge-bank inheritance row.

7. **Cut-over-window, 2025-10-28 11:08 PT** — Mission Plaza-side CRE loan re-underwriting attestation for one of the $1.2B loss-share-covered loans; chain row references §10.75 loss-share agreement anchor under MAC; verifier returns PASS in 1.2s.

8. **Post-cut-over, 2025-12-15** — Mission Plaza-side CRE loan chargeoff event (first chargeoff under loss-share); $4.7M chargeoff on Tranche A; deterministic-arithmetic indemnification calculation $3.76M = 80% × $4.7M; bound under §10.75; FDIC claims-administration walked the chain reference at 2026-Q1 quarterly settlement.

9. **Post-cut-over, 2026-01-22** — Mission Plaza-side uninsured-depositor pro-rata distribution row (the 90-day-mark second disbursement; $87.4M = 28% × $312M); bound under §10.76; cross-entity settlement reference to FDIC claims-administration anchor.

10. **Post-cut-over, 2026-05-12** — Mission Plaza-side ongoing operational chain row (Long Beach branch credit-decision under post-close chain SDK); full twelve-field row; verifier PASS in 1.0s.

Ten records traced end-to-end through the four partitions. Ten for ten verified.

For records 1-3 (pre-failure), the verifier returned `additional_verifications: ['fdic_attestation_anchor_resolved', 'pre_failure_partition_verified']` alongside exit code 0. For records 4-5 (bridge-bank-period), the verifier returned exit code 0 with the FDIC HSM key resolved from the Federal Register publication reference; `additional_verifications: ['federal_register_key_resolution_verified', 'bridge_bank_partition_verified', 'fdic_operating_authority_binding_verified']`. For record 6 (cut-over-window), the verifier returned exit code 0 + `bridge_bank_inheritance_resolved` + `cut_over_partition_verified`. For record 7, additionally `loss_share_anchor_resolved`. For record 8 (post-cut-over chargeoff), the verifier returned exit code 0 + `deterministic_arithmetic_indemnification_verified` + `loss_share_quarterly_settlement_ref_resolved`. For record 9, `pro_rata_distribution_held` + `cross_entity_settlement_resolved`. For record 10, `post_cut_over_partition_verified`. Six additional verifications across the ten records under the §10.77 four-partition discipline.

Dawn ran the Kognitos twelve-row template against each. Records 1-3 partially satisfied Field 6 (source attribution) and Field 12 (tamper-evident proof) but were silent on the §10.74 federal-receivership-signing-authority binding. Records 4-5 partially satisfied Field 6 but the structural distinction that the signing authority was FDIC-DOLR operating under a published time-bounded validity window was structurally invisible. Records 6-7 partially satisfied Fields 1, 11, 12; the bidirectional cross-reference discipline was unrepresented. Record 8 satisfied Fields 1, 6, 11, 12 but the deterministic-arithmetic indemnification calculation was structurally invisible. Record 9 partially satisfied Fields 1, 11, 12; the multi-installment cross-entity disbursement structure was structurally invisible. Record 10 satisfied all twelve fields cleanly under Kognitos's mental model.

Four distinct patterns of framework-fit emerged. Records 1-3: framework partial-fit (pre-failure rows under §10.74 attestation are partially readable but the federal-receivership-signing-authority binding is invisible). Records 4-5: framework form-mismatch (bridge-bank-period under FDIC operating authority is structurally invisible). Records 6-9: framework form-mismatch (FDIC-resolution-specific structures — bidirectional cross-reference, deterministic-arithmetic indemnification, multi-installment cross-entity disbursement — are structurally invisible). Record 10: framework clean-fit.

Dawn wrote in the parallel observations: *Ten records traced; ten for ten verified under the reference spec; four distinct patterns of Kognitos framework-fit across the FDIC-resolution integration. The framework reads Record 10 cleanly because the post-cut-over surface is what Kognitos was authored for; Records 1-3 partially because the pre-failure rows predate the §10.74 attestation binding and the federal-receivership-signing-authority discipline; Records 4-5 form-mismatched because bridge-bank-period under FDIC operating authority is structurally a third signing-authority kind; Records 6-9 form-mismatched because the FDIC-resolution-specific structures are structurally invisible. The institution's claim — that all ten records are equally defensible under one continuous evidentiary trail across four partitions — is the structural property of §10.77's four-partition temporal-slice; the framework cannot articulate the property.*

## 🌆 12:00 PM — Day 2 — Closing memo composition + engagement close

Linda, Brad, Carmen, Gabriela, Walter Singh, and Olivia Wendt-Park all joined the closing at noon. Olivia was the Audit Committee chair — late fifties, former Deputy Inspector General at the FDIC Office of Inspector General, on Mission Plaza's board three years. She would read the cover memo against the audit committee's FDIC P&A integrity charter and against her own institutional memory of how FDIC IG read receivership audit-trails.

Dawn walked the cover memo:

> **Spec-section confirmation pass — Mission Plaza Bank — Argosy Pacific FDIC-assisted P&A integration**
>
> The audit team confirms, under the FFIEC chain-of-custody v1.0b reference specification (ninth errata current), that the following five FDIC-resolution-specific sections were exercised in production at the post-P&A institution and verify cleanly:
>
> - **§10.73** — Bridge-bank receivership chain inheritance; tri-signature pair (FDIC DOLR Resolution Officer + failed-entity retained CRO + acquirer CFO) validated under HSM-rooted attestation; bidirectional cross-references to §10.74, §10.75, §10.76 anchors resolve; verifier PASS in 2.4s with six additional verifications.
> - **§10.74** — FDIC-attestation chain-anchor for the 174 bridge-bank-period rows; Federal Register publication reference (FR-90-FR-26417) under MAC binds the time-bounded validity window for the receiver HSM key; verifier walks all 174 rows in 4.7s; Merkle root cross-binds to the §10.74 anchor byte-for-byte.
> - **§10.75** — Loss-share agreement chain-anchor for $1.2B CRE portfolio under FDIC indemnification; 227 per-loan SHA-256 hashes Merkle-bound; deterministic-arithmetic indemnification rule (80% Tranche A; 95% Tranche B) chain-bound at capture; first FDIC chain-bound loss-share pilot under CFO approval.
> - **§10.76** — Uninsured-depositor DIF reconciliation chain; $312M across 47 accounts; closed-schedule three-installment pro-rata distribution (35% / 28% / 12%) + 25% terminal-loss recognition under MAC; cross-entity settlement references to FDIC claims-administration anchor resolve.
> - **§10.77** — Receivership-window temporal-slice with four-partition discipline (pre-failure + bridge-bank-period + cut-over-window + post-cut-over); partition assignment deterministic from timestamp + signing-authority operating window; extends Ch14 §10.41 three-partition shape to FDIC-resolution receiverships.
>
> Under the Kognitos twelve-field AI audit-trail framework: 4 Framework Confirmations (Field 1 timestamp; Field 6 source attribution partially against the 174 bridge-bank rows; Field 11 hash chain; Field 12 tamper-evident proof). 5 Framework Inarticulabilities documented in the firm's parallel observations: §10.73 tri-signature pair; §10.74 federal-receivership-signing-authority binding; §10.75 deterministic-arithmetic indemnification under MAC; §10.76 multi-installment cross-entity disbursement with terminal-loss recognition; §10.77 four-partition temporal-slice with bridge-bank-period. 5 Framework-Silent Observations: Federal Register key publication with time-bounded validity; chain-as-input + chain-as-parent reuse from Polaris Ch15 extending to FDIC claims-administration; three-role tri-signature extending Ch14 dual-signature pattern; FDIC chain-bound loss-share administration pilot under CFO approval; four-partition temporal-slice extending Ch14's three-partition shape.
>
> The institution's audit-trail discipline as exercised under the reference specification is defensible against the OCC's post-failure-acquisition examination scope. The Kognitos checklist records the four Confirmations cleanly; the five Inarticulabilities are documented in the firm's parallel observations and are appended to this cover memo as a reading aid for the OCC examination team.

Olivia read the memo. She handed it to Walter, who skimmed the §1.2 epistemic-scope notes at the appendix and nodded. Gabriela read it next and noted the §10.74 anchor row's Federal Register cross-reference for her DOLR case file. Linda read it last.

Linda closed her folder.

"Sixteen months ago at MPB-2024-Q4, you walked in here and named what the framework could not carry against our baseline architecture. Today, you walked in, named the five FDIC-resolution sections from the cover memo before lunch on Day 1, and walked through them against what the chain demonstrates across the four-partition discipline. The framework still doesn't carry it. Your team's parallel observations have carried it for fourteen engagements that have produced cover memos that crossed my desk through industry channels since you last visited — and you've carried it here today."

She paused.

"I read Marcus Tan's Northbridge return cover memo when it became public through the OCC examiner network channels about a year and a half ago — that was the cover memo I lifted my own engagement template from for this audit. I read Maya Hartwell's Polaris cover memo when it came through the PRA-FRB bilateral coordination channel six months ago. I read Yuki Takeda's Lyceum cover memo when it landed through the FDA-FRB healthcare-oversight liaison three months ago. I read Lukas Affentranger's Helvetian cover memo when it landed through the OECD CRS liaison two months ago. I read Mariana Whitfield's Argent Vector cover memo when it landed through the DCSA industrial-security commercial-sector channel one month ago. I read Hyo-jin Park's Aerolith cover memo two weeks ago when it landed through the NIST CMVP cryptographic-officer industry channel. The firm's parallel observations are part of the federal-banking-regulator working canon now. I will not ask for an on-the-record framework-substitution recommendation today, because the firm's parallel observations have done that work seven times in seven prior cover memos already, and the OCC examination team will read both side by side. I want what you wrote in the memo, and the appendix, and the parallel observations from the prior seven engagements, in one packet for the OCC team. The audit committee chair has read the memo. The general counsel has read the memo. The FDIC liaison has read the memo. I'm signing the receipt now. Same drill, the coffee moved, and the next time you come back — and you will, because the chain keeps getting wider — I'll see you here."

She signed.

The engagement closed at 12:21 PM.

*Note for the chapter. Second-instance reproduction of Ch14's return-engagement institutional-memory observation. Linda Marchetti's closing remarks structurally reproduce Marcus Tan's pattern from Ch14: read prior cover memos from sister institutions through industry channels; decline to make an on-the-record framework-substitution recommendation; defer to the parallel-observations corpus as having done the work already; sign the receipt and close. The pattern is now two-instance reproducible and settles as the **fourteenth voice-pattern variant** in the catalog. The return-engagement chapter-class is two-instance reproducible (Ch14 M&A planned-close; Ch20 FDIC-resolution receivership). Both chapters closed confirmation-posture without on-the-record stakeholder statement; both CAEs produced cover-memo-prose institutional-memory observations referencing the firm's prior cover memos through industry channels. The structural distinction across the two instances: Ch14 Marcus Tan referenced six prior cover memos (Atrio, Helmstad, Pacific Crescent, Salt Pond, Eberhardt × Lumière, Hill Country, Saraswati — seven if all counted); Ch20 Linda Marchetti referenced seven cover memos (Northbridge return, Polaris, Lyceum, Helvetian, Argent Vector, Aerolith, plus implicit awareness of intervening chapters through federal-banking-regulator working canon). The institutional-memory observation grows materially in scope as the program advances — Marcus Tan's catalog of cover memos in his industry channel was seven institutions across thirteen prior engagements; Linda Marchetti's catalog seventeen months later spans seven explicit references across nineteen prior engagements. The cover-memo corpus is now part of the federal-banking-regulator working canon by Linda's account.*

---

## Day 1 + Day 2 close — five Framework Inarticulabilities + five Framework-Silent Observations under the ninth-errata reference spec

5 Framework Inarticulabilities (all structural-vocabulary gaps in the §10.73-§10.77 wave). 5 Framework-Silent Observations (Federal Register key publication + chain-as-input/parent reuse + three-role tri-signature + FDIC chain-bound loss-share pilot + four-partition temporal-slice extension). 4 Framework Confirmations. Engagement closes 12:21 PM Day 2.

**Second-instance reproduction of the Ch14 return-engagement institutional-memory observation pattern; voice-pattern catalog advances to fourteen settled variants.**
