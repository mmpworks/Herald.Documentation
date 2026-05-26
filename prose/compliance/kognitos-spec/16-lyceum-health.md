# 16 — Lyceum Health — Kognitos-lens

*Multi-state non-profit hospital system audit; first four-substrate composition in the program (on-prem Epic at hospital data centers + hospital-system-owned private cloud for clinical research + Microsoft Azure Mid-Atlantic public cloud for ML inference + Epic shared-services vendor-managed cloud for cross-hospital data aggregation); third partial landing of the foresight-cluster §10.40 substrate-move pressure that opened at Ch12 (after Ch14 cross-vendor variant + Ch15 cross-cloud variant; Ch16 lands the on-prem-plus-cloud composed-four-substrate variant); ninth settled voice-pattern variant introduced — personal-FDA-Sponsor-of-record statement under SaMD post-market-surveillance accountability — distinct from Ch15's SM&CR variant because FDA registration is product-specific not institutional-management. Five Framework Inarticulabilities surface: §10.40 four-substrate composed variant; §10.55 FDA SaMD model-clearance attestation; §10.56 patient-safety clinical-decision-support boundary; §10.57 multi-state aggregated reporting partition; §10.58 EHR-vendor co-anchor cross-tenant hash binding.*

**Engagement:** Three-day pre-Joint-Commission triennial survey + HHS Office for Civil Rights HIPAA readiness pass at Lyceum Health System's Baltimore headquarters. Joint Commission triennial opens in five weeks; HHS OCR routine compliance audit window opens in eight weeks; FDA post-market surveillance review of the radiology AI ensemble's 510(k) clearance opens in seven weeks. Six parallel regulator audiences read the chain: Joint Commission (accreditation); HHS Office for Civil Rights (HIPAA Security Rule + Privacy Rule + Enforcement Rule); CMS (Conditions of Participation; Medicare Promoting Interoperability Program); FDA (post-market surveillance under 21 CFR §807 + §820 against the radiology AI's De Novo clearance); five state Departments of Health (Maryland DHMH; Virginia VDH; DC DOH; Pennsylvania DOH; Delaware DPH — each with state-specific reporting cycles partitioned from the chain coverage map).
**Client:** Lyceum Health System — five-state Mid-Atlantic non-profit health system based in Baltimore. ~$8.4B annual revenue; 19 acute-care hospitals across MD/VA/DC/PA/DE; 187 ambulatory clinics; ~73,000 employees; ~6,400 affiliated clinicians; ~610,000 inpatient admissions per year; ~12.4M outpatient visits per year. Clinical AI inference paths: sepsis early-warning ML, ED triage acuity model, radiology AI ensemble (cleared under FDA De Novo pathway DEN240187 in 2024-Q3 for chest CT pulmonary embolism screening), revenue-cycle ML.
**Status:** Chain in production: thirteen months across on-prem Epic instances at hospital data centers (per-event MAC + daily Merkle seal + Ed25519 signature under hospital-data-center HSMs at five regional roots); thirteen months across Lyceum-owned private cloud in Hanover Maryland data center for 21 CFR Part 11 clinical-research workloads (per-event MAC + daily Merkle seal under Lyceum private-cloud HSM); thirteen months across Microsoft Azure Mid-Atlantic public cloud for ML inference paths (per-event MAC + daily Merkle seal under Azure Dedicated HSM East US 2); eight months across Epic shared-services vendor-managed cloud cross-hospital data aggregation (per-event MAC at Epic's seal; co-anchor hash-binding to Lyceum's chain under §10.58 cross-tenant anchor framework shipped seven weeks ago in the spec's sixth errata).
**Audit team lead:** Dawn
**Audit team:** Mike (application/API layer); Elena (clinical-workflow systems); Chen (data engineering / ML inference paths); Diana (IAM & multi-substrate access control across five state HSM roots); Luis (DevOps / hybrid substrate substrate); Raj (database / cross-substrate replication discipline including Epic shared-services cloud); Tom (audit liaison).
**Client liaisons:** Dr. Amelia Hartmann (Chief Medical Information Officer — clinical AI governance and inference-path operational oversight); Dr. Cyrus Patel (Chief Quality Officer — board-level patient-safety governance under Joint Commission requirements; reports directly to the Board of Trustees Quality Committee); Patricia Donovan (Chief Compliance Officer — HIPAA, CMS, state DOH, Joint Commission portfolio); Marcus Sieber (Chief Information Security Officer); Dr. Yuki Takeda (Chief Radiologist and Sponsor of Record for the radiology AI 510(k) clearance DEN240187; personally accountable under FDA 21 CFR §807.81 + §820.198 for post-market surveillance and adverse-event reporting); Greg Holloway (VP IT / SRE); Dorothy Brennan (General Counsel); Sarah Connaughton (Board of Trustees Chair; joining Day 2 for closing).

**Audit team's framework:** Kognitos's 12-field schema. Same printed twelve-row template Dawn has carried since Ch01. After fifteen engagements the firm's parallel observations corpus is approximately ninety-five entries indexed by engagement and spec section. Dawn carries the relevant subset for Lyceum: Mercator's two-zone HIPAA-vs-research coverage-boundary primitive from Ch02 (a near analog for Lyceum's four-substrate composition); Helmstad's CCO+CQD joint clinical-readiness pattern from Ch05 (CMIO + CQO joint pattern likely to recur); Pacific Crescent's §1.2 (a)-(e) public-safety inarticulability cluster from Ch06 (the clinical-decision-support boundary is the patient-safety variant); NetiVa's §10.17 dual-HSM-root discipline from Ch08 (the four-substrate composition reuses §10.17 at five different boundary types simultaneously); Polaris's §10.40 cross-cloud variant from Ch15 (the immediately preceding partial-landing of the foresight cluster). The team walks in expecting a clean confirmation pass on the on-prem Epic + Lyceum-private-cloud surfaces — but has not seen the §10.55-§10.58 wave's production exercise before. This is the first chapter where the FDA SaMD attestation + patient-safety clinical-decision-support boundary + multi-state aggregated reporting + EHR-vendor co-anchor sections meet a real multi-regulator-audience audit.

---

## 🌅 8:30 AM — Day 1 — Kickoff at Lyceum Health System HQ, Baltimore

Dawn walked into Lyceum Health System's headquarters on Pratt Street in Baltimore. The system's executive floor — twentieth — looked out over the Inner Harbor. The engagement room was the Board of Trustees meeting room itself, by Sarah Connaughton's request — she wanted the Board to be able to walk in on Day 2 closing without anyone having to relocate.

Dr. Amelia Hartmann met her at the door at 8:33. Mid-fifties, white coat over business attire, a stethoscope still slung around her neck from her morning patient rounds at Lyceum Baltimore Medical Center two blocks east. Dr. Hartmann had been CMIO at Lyceum for eleven years. She had been the executive sponsor of the chain-of-custody program when it stood up thirteen months ago.

"Dawn. Tom. Coffee's by the window. Let me introduce the team."

The audit team filed in. Dr. Cyrus Patel (CQO) was already seated, reading the morning's overnight inpatient incident report on a tablet. Dr. Yuki Takeda (Chief Radiologist + FDA SaMD Sponsor of Record) sat at the far end of the table with a printed copy of the DEN240187 510(k) clearance letter and the FDA's most recent post-market surveillance correspondence. Patricia Donovan (CCO), Marcus Sieber (CISO), Greg Holloway (VP IT), and Dorothy Brennan (GC) filled the remaining seats. Sarah Connaughton would join Day 2.

Dr. Hartmann opened.

"Three days. Joint Commission triennial in five weeks. HHS OCR routine in eight. FDA post-market surveillance of the radiology AI clearance in seven. Five state DOH reporting cycles overlap on the same chain in the next four months. The chain has been running thirteen months across four substrates — on-prem Epic at each hospital data center; our own private cloud in Hanover for clinical research workloads under 21 CFR Part 11; Azure Mid-Atlantic for the ML inference paths; and Epic shared-services vendor-managed cloud for cross-hospital data aggregation since eight months ago, under the §10.58 cross-tenant anchor framework that shipped in the sixth errata seven weeks ago.

"We need a spec-section confirmation pass on five sections: §10.40 four-substrate composed variant; §10.55 FDA SaMD model-clearance attestation; §10.56 patient-safety clinical-decision-support boundary; §10.57 multi-state aggregated reporting partition; §10.58 EHR-vendor co-anchor cross-tenant hash binding. Dr. Takeda will personally walk you through §10.55 because her name is on the FDA Sponsor registration for DEN240187. Dr. Patel will personally walk you through §10.56 because the patient-safety boundary is his board-level accountability under Joint Commission's Sentinel Event Policy."

Dawn uncapped her pen.

"Same twelve-row template I've carried since the program began. I'll walk what the framework can confirm. The rest goes in the firm's parallel observations as we go."

Dr. Patel looked up from the inpatient report.

"I want the parallel observations bound into the closing memo for both the Joint Commission packet and the FDA post-market surveillance correspondence. Sarah will read both at close on Day 2 in her Board Quality Committee chair role. I'll explain at close why."

*Note for the chapter. First multi-state hospital-system engagement; first four-substrate composition in the program; ninth settled voice-pattern variant arriving via FDA SaMD Sponsor-of-record + CQO joint statement. The framework has not moved in twenty months; the reference spec has absorbed nine engagement-source amendments in that window plus the §10.40 cross-cloud variant + §10.51-§10.54 Polaris wave + §10.55-§10.58 Lyceum wave shipped in the fifth and sixth errata streams; the Kognitos checklist Dawn carries is byte-equal to Ch01's.*

## 🌐 9:30 AM — Day 1 — §10.40 four-substrate composed variant walkthrough

Greg Holloway took the projector. He brought up the four-substrate architecture diagram.

The on-prem Epic perimeter ran at each of the 19 hospital data centers, each with its own HSM root. To keep cryptographic boundaries clean, the five state DOH territories had been organized into five regional roots — Maryland HSM Cluster, Virginia HSM Cluster, DC HSM Cluster, Pennsylvania HSM Cluster, Delaware HSM Cluster — with each hospital binding to the cluster in its state. Per-event MAC at capture; daily Merkle seal at 23:59 ET; Ed25519 signature under the state-regional HSM root.

The Lyceum-owned private cloud in Hanover Maryland served the 21 CFR Part 11 clinical-research workloads. Per-event MAC at capture; daily Merkle seal under Lyceum private-cloud HSM in the Hanover data center.

The Microsoft Azure Mid-Atlantic public cloud served the four ML inference paths — sepsis early-warning ML, ED triage acuity model, radiology AI ensemble (DEN240187), revenue-cycle ML. Per-event MAC at capture; daily Merkle seal under Azure Dedicated HSM East US 2.

The Epic shared-services vendor-managed cloud was the cross-hospital data aggregation surface — Epic's own audit trail discipline ran the chain there, with Lyceum's chain hash-anchoring Epic's seals through the §10.58 cross-tenant anchor framework.

Greg brought up an example record from a sepsis-ML alert that fired on 2026-04-22 at 14:17 ET at Lyceum Virginia Medical Center in Arlington.

```json
{
  "entry_id": "lyceum/cross-substrate-seam/2026-04-22#cs-04222",
  "tenant": "lyceum",
  "service": "cross-substrate-anchor",
  "event_class": "clinical_inference_to_action",
  "audit.handover.substrate_chain": [
    {
      "substrate": "azure-mid-atlantic-east-us-2",
      "kind": "public_cloud_inference",
      "chain_ref": {
        "tenant": "lyceum-ml",
        "service": "sepsis-early-warning",
        "entry_id": "lyceum-ml/2026-04-22#sep-1417-VA-MED-ARL",
        "merkle_root": "8a3c...4e91",
        "seal_id": "lyceum-ml/seals/2026-04-22#azhsm",
        "hsm_key_fingerprint": "5d:2c:9a:7f:..."
      }
    },
    {
      "substrate": "on-prem-epic-virginia-cluster",
      "kind": "on_prem_clinical_workflow",
      "chain_ref": {
        "tenant": "lyceum-epic-va",
        "service": "clinical-workflow",
        "entry_id": "lyceum-epic-va/2026-04-22#cdsf-1417-VA-MED-ARL",
        "merkle_root": "9c7e...3a12",
        "seal_id": "lyceum-epic-va/seals/2026-04-22#va-hsm",
        "hsm_key_fingerprint": "3b:8e:11:2a:..."
      }
    },
    {
      "substrate": "lyceum-private-cloud-hanover",
      "kind": "private_cloud_research_link",
      "chain_ref": {
        "tenant": "lyceum-research",
        "service": "sepsis-validation-cohort",
        "entry_id": "lyceum-research/2026-04-22#cohort-1417-VA-MED-ARL",
        "merkle_root": "1f4d...8b23",
        "seal_id": "lyceum-research/seals/2026-04-22#hanover-hsm",
        "hsm_key_fingerprint": "7e:4c:6f:91:..."
      }
    },
    {
      "substrate": "epic-shared-services-vendor-cloud",
      "kind": "ehr_vendor_managed_cloud",
      "chain_ref": {
        "tenant": "epic-shared-services-lyceum-tenant",
        "service": "cross-hospital-aggregation",
        "entry_id": "epic-shared/2026-04-22#agg-1417-VA-MED-ARL",
        "merkle_root": "6b2a...5d40",
        "seal_id": "epic-shared/seals/2026-04-22#epic-hsm",
        "hsm_key_fingerprint": "2f:9d:c4:88:...",
        "vendor_hsm_attestation_doc_sha256": "a5...3e"
      }
    }
  ],
  "audit.handover.payload_sha256": "d7e2...1c5b",
  "audit.handover.composed_signature_set": {
    "azure_hsm_signature": "...",
    "virginia_hsm_signature": "...",
    "hanover_hsm_signature": "...",
    "epic_hsm_signature": "..."
  },
  "hmac": "...",
  "merkle_path_azure": [...],
  "merkle_path_virginia": [...],
  "merkle_path_hanover": [...],
  "merkle_path_epic_shared": [...],
  "spec_section_reference": "§10.40 (four-substrate) + §10.17 + §10.58 + §10.5"
}
```

Greg walked the structure aloud. The four-substrate seam was not one chain entry — it was a paired-quadruple chain entry that lived simultaneously in four substrates. The Azure-side sepsis-ML inference produced the loss-score output at 14:17:08 ET; the same payload's SHA-256 was committed to the on-prem Epic Virginia chain when the clinical-decision-support flag fired at the bedside (14:17:11 ET); the same payload was committed to the Lyceum-private-cloud chain for the research-validation cohort linkage (14:17:14 ET, within the four-second multi-substrate-window contract); and the same payload was committed to the Epic shared-services vendor cloud for cross-hospital aggregation (14:17:21 ET). Four chain entries; one payload SHA-256 binding them; four HSM-rooted Ed25519 signatures under §10.17 four-way composition.

Mike ran the verifier in strict mode against the four-substrate seam:

```
$ herald-verify --tenant=lyceum \
                --entry-id="2026-04-22#cs-04222" \
                --strict --multi-substrate

Status: PASS
Exit code: 0
Step: 11 (§10.40 four-substrate dispatch complete)
additional_verifications: ['cross_cloud_seam_verified',
                           'multi_substrate_composition_verified',
                           'quad_hsm_signature_verified',
                           'vendor_cloud_co_anchor_verified']

Reason:
  step 1: read seam record; identified four-substrate variant
  step 2: Azure-side chain entry resolved; merkle_root recomputed; HSM 5d:2c:9a:7f:... verified
  step 3: Virginia on-prem chain entry resolved; merkle_root recomputed; HSM 3b:8e:11:2a:... verified
  step 4: Hanover private-cloud chain entry resolved; merkle_root recomputed; HSM 7e:4c:6f:91:... verified
  step 5: Epic shared-services co-anchor entry resolved; merkle_root recomputed; HSM 2f:9d:c4:88:... verified
  step 6: vendor-HSM attestation doc verified against Epic-published attestation registry
  step 7: payload_sha256 (d7e2...1c5b) byte-equal across all four sides
  step 8: Azure HSM signature verified
  step 9: Virginia HSM signature verified
  step 10: Hanover HSM signature verified
  step 11: Epic HSM signature verified

Elapsed: 4.1s
```

Mike walked the verdict object aloud. The verifier landed *four* additional verifications alongside exit code 0: `cross_cloud_seam_verified` (Polaris pattern Ch15), `multi_substrate_composition_verified` (new at Ch16), `quad_hsm_signature_verified` (new at Ch16 — four-way extension of §10.17), and `vendor_cloud_co_anchor_verified` (§10.58 new at Ch16).

Dawn walked the four-substrate seam against the Kognitos checklist.

Field 1 (timestamp). The seam carried *four* timestamps — Azure-side 14:17:08; Virginia on-prem 14:17:11; Hanover private cloud 14:17:14; Epic shared-services 14:17:21. The field's singular wording could record one. Three were lost.

Field 11 (hash chain). The framework had a place for one hash chain. The seam involved four hash chains, all bound by the byte-equal payload SHA-256. Three were unrepresented.

Field 12 (tamper-evident proof). The seam carried four Ed25519 signatures under four HSM roots. The singular field could record one. Three were lost.

The verdict object landed four additional verifications. Field 12's singular wording could record neither the second nor the third nor the fourth.

Dawn wrote in the parallel observations: *The §10.40 four-substrate composed variant is the structural answer to the program's question filed at Ch12 — what happens when the substrate moves? — extended to its compound limit. Polaris answered with two substrates. Lyceum answers with four. The framework's singular-axis losses compound by a factor of four at every Field per seam: paired timestamps become quadrupled; paired chains become quadrupled; paired signatures become quadrupled. The verifier verdict object lands four additional verifications alongside exit code 0; under Kognitos's Field 12 only the base proof can land, and the four additional axes are structurally lost.*

> ### ⚠ Framework Inarticulability #1 — §10.40 four-substrate composed variant
> Kognitos's twelve-row schema has no concept of N-substrate composed chain entries. The §10.40 four-substrate composed variant binds a single inference-to-action event simultaneously into four chains — Azure Mid-Atlantic public cloud (ML inference) + Virginia on-prem Epic (clinical-workflow action) + Hanover Lyceum private cloud (research-validation linkage) + Epic shared-services vendor-managed cloud (cross-hospital aggregation) — under §10.17 four-way HSM-root composition. The verifier returns exit code 0 + four additional verifications (`cross_cloud_seam_verified` + `multi_substrate_composition_verified` + `quad_hsm_signature_verified` + `vendor_cloud_co_anchor_verified`). Field 1 records one of four timestamps; Field 11 records one of four chains; Field 12 records one of four signatures and zero of four additional verifications. The auditor speculates that "the inference produced an action safely across systems" without structural footing for the four-substrate composition.

## 🩺 11:30 AM — Day 1 — §10.55 FDA SaMD model-clearance attestation walkthrough

After a coffee break, Dr. Yuki Takeda took the projector. She placed her physical copy of the DEN240187 510(k) De Novo clearance letter on the table — six pages, FDA letterhead, dated 2024-09-12, signed by the Director of CDRH Office of Radiological Health.

"I am the Sponsor of Record for the radiology AI ensemble's clearance," she said. "FDA 21 CFR §807.81 makes me personally accountable for post-market surveillance under §820.198. The §10.55 model-clearance attestation is the chain's structural binding to my Sponsor accountability — it carries the FDA-issued clearance number, the Indications for Use, the manufacturer-of-record, the clinical-evidence summary hash, and my Sponsor-of-Record identification under MAC in every chain entry the radiology AI ensemble produces. If the FDA opens a post-market action against deficient adverse-event reporting, the chain is what defends my Sponsor status."

She brought up a representative chain entry from a radiology AI inference produced on 2026-04-15:

```json
{
  "entry_id": "lyceum-ml/2026-04-15#rad-1247-MD-MED-BAL",
  "tenant": "lyceum-ml",
  "service": "radiology-ai-ensemble",
  "event_class": "samd_inference",
  "audit.samd.fda_clearance_number": "DEN240187",
  "audit.samd.fda_clearance_pathway": "De Novo",
  "audit.samd.clearance_date_utc": "2024-09-12",
  "audit.samd.indications_for_use_sha256": "a3f1...8b29",
  "audit.samd.manufacturer_of_record": "Radial Diagnostics Inc.",
  "audit.samd.manufacturer_uri": "https://radialdiagnostics.example",
  "audit.samd.clinical_evidence_summary_sha256": "c7d2...4f08",
  "audit.samd.sponsor_of_record_identity": "fda-sponsor:Yuki-Takeda-MD:NPI-1234567890",
  "audit.samd.sponsor_of_record_attestation_chain_ref": "lyceum-ml/samd-governance/2024-09-15#sponsor-of-record-takeda",
  "audit.samd.indications_match_check": "indication_within_clearance_scope",
  "audit.samd.deployed_model_artifact_sha256": "8e5b...1c7a",
  "audit.samd.deployed_model_artifact_matches_cleared_artifact": true,
  "audit.samd.adverse_event_subscription_active": true,
  "audit.samd.post_market_surveillance_runbook_ref": "lyceum-ml/runbooks/samd-pms-2024-Q4",
  "hmac": "...",
  "merkle_path": [...],
  "daily_seal_ref": "lyceum-ml/seals/2026-04-15#azhsm"
}
```

Dr. Takeda walked the eight FDA-specific attributes aloud. The clearance number plus pathway plus clearance date bound the regulatory provenance under MAC. The Indications for Use SHA-256 bound the FDA-issued IFU document — if the FDA published an updated IFU through a Letter to Industry, the IFU hash would change and the §10.55 attestation chain row's hash would no longer match — automatic detection of deployed-system drift from cleared-system. The manufacturer-of-record + manufacturer URI bound the cleared device's manufacturer (Radial Diagnostics Inc., the third-party AI vendor whose product Lyceum licensed under FDA SaMD framework). The clinical-evidence summary hash bound the 510(k) submission's clinical-evidence section. The Sponsor-of-Record identity bound Yuki's NPI and her FDA Sponsor-of-Record attestation under MAC. The indications-match check was a chain-bound verification that the inference's actual patient indication fell within the cleared scope (Lyceum's CDS layer enforced that the radiology AI was only invoked for chest CT pulmonary embolism screening; any other indication produced a refused-inference chain row under SDK refusal-at-capture pattern from Ch11). The deployed-model-artifact hash plus the cleared-artifact-match boolean bound that the running model artifact was byte-equal to the cleared artifact (no field-update / no shadow-deployment / no hot-patch). The adverse-event subscription status plus the post-market-surveillance runbook reference bound the operational compliance posture.

Dawn walked the §10.55 entry against the Kognitos checklist.

Field 4 (the AI model used + version). The Kognitos field expected one model identity plus version. The §10.55 entry carried a much wider provenance — clearance number, pathway, clearance date, IFU hash, manufacturer-of-record, clinical-evidence summary hash, Sponsor-of-Record identity. Field 4 could carry one or two of these eight; the rest had no slot.

Field 8 (reasoning behind the decision). The reasoning was the radiology AI's output — a probability score for pulmonary embolism. Field 8 could carry the output. But the *Sponsor-of-Record FDA accountability* binding that established Yuki's personal regulatory exposure was not "reasoning behind the decision" — it was regulatory provenance metadata.

Field 11 + Field 12. Verified.

The FDA SaMD model-clearance attestation as a structural binding to Sponsor-of-Record accountability was unrepresented.

Dr. Takeda watched Dawn write. She had read Maya Hartwell's Polaris cover memo through industry channels three weeks ago — Lloyd's market disclosures and Maya's PRA SM&CR statement had landed on Yuki's desk the week the cover memo became public. She had seen the personal-regulatory-exposure-individual voice pattern. Yuki's FDA accountability was structurally analogous — same shape, different register.

She didn't speak yet. She would speak at the close.

Dawn wrote in the parallel observations: *The §10.55 FDA SaMD attestation binds eight regulatory-provenance attributes under MAC in every radiology AI inference chain entry. The Sponsor-of-Record identity is the binding to Yuki Takeda's personal FDA accountability under 21 CFR §807.81 + §820.198. Under Kognitos, Field 4 is singular and Field 8 is reasoning text; the regulatory provenance has no slot. The auditor records "the AI used was the radiology ensemble" without structural footing for the Sponsor-of-Record accountability.*

> ### ⚠ Framework Inarticulability #2 — §10.55 FDA SaMD model-clearance attestation
> Kognitos's Field 4 (AI model + version) is singular. The §10.55 FDA SaMD attestation pattern binds eight regulatory-provenance attributes under MAC in every SaMD-class inference chain entry: clearance number (DEN240187); clearance pathway (De Novo); clearance date (2024-09-12); Indications for Use SHA-256 (with automatic detection of FDA-issued IFU drift); manufacturer-of-record + manufacturer URI; clinical-evidence summary SHA-256; Sponsor-of-Record identity (Yuki Takeda's NPI under MAC); indications-match check (refusal-at-capture if patient indication exceeds cleared scope); deployed-model-artifact hash + cleared-artifact-match boolean; adverse-event subscription status; post-market-surveillance runbook reference. Field 4 cannot record the regulatory provenance. Field 8 (reasoning) cannot carry Sponsor-of-Record accountability as structural metadata. The auditor speculates that "an FDA-cleared AI was used" without structural footing for the eight-attribute binding to personal Sponsor accountability under 21 CFR §807.81 + §820.198.

## 🏥 1:30 PM — Day 1 — §10.56 patient-safety clinical-decision-support boundary walkthrough

After lunch in the Board of Trustees dining room, Dr. Cyrus Patel took the projector. He brought up the §10.56 patient-safety boundary discipline.

"Joint Commission's Sentinel Event Policy makes me personally accountable for the institution's patient-safety reporting," he said. "I have to be able to answer, in a hearing-room setting, whether a patient harm was caused by an AI failure, by a clinician failure, by a system failure, or by no failure at all. The chain has to draw those lines structurally. §10.56 is the patient-safety variant of the §1.2 epistemic-scope boundary."

He walked the discipline aloud. The chain's patient-safety boundary distinguished four operational claims:

```
§10.56 patient-safety clinical-decision-support boundary claims:

(a) The chain proves what the CDS system said.
    -- HMAC-bound model output; cryptographically defensible.

(b) The chain proves the CDS output was surfaced to the clinician.
    -- §10.11.1 ECOA-pattern bedside-presentation chain row; clinician_id
       receiving the alert; alert_acknowledgement_required boolean; the
       acknowledgement chain row if acknowledged or unacknowledged.

(c) The chain does NOT prove the clinician acted on the CDS output.
    -- Clinical-judgment exception is structurally chain-bound only when
       the clinician documents the override under §10.11.1 ECOA-style
       structured-override pattern with reason_code + free_text rationale.
       Undocumented override is structurally invisible.

(d) The chain does NOT prove patient harm or absence of patient harm.
    -- Clinical outcomes are downstream of CDS use; downstream outcomes
       are not in the chain; clinical-outcome correlation requires the
       institution's own quality-improvement data outside the chain.
```

The four-claim boundary closed under §1.1 Daubert four-factor mapping for sentinel-event hearings — Patel had used the boundary in two sentinel-event hearings in the prior eighteen months and survived legal cross-examination both times because the boundary was *structural*, not editorial.

Dawn walked the §10.56 discipline against the Kognitos checklist.

Field 11 (hash chain). The chain's integrity proofs for the CDS output + the bedside-presentation row + the documented-override row + the patient-outcome-correlation row were all cryptographic. Field 11 confirmed.

Field 12 (tamper-evident proof). Confirmed.

But the *four-claim epistemic-scope boundary* itself — the structural distinction between (a) what the CDS said, (b) what the clinician saw, (c) what the clinician did, and (d) what happened to the patient — was unrepresented. The framework had no concept of epistemic-scope partitioning across the CDS-to-clinician-to-patient pipeline.

Dawn wrote in the parallel observations: *The §10.56 patient-safety CDS boundary is the §1.2 epistemic-scope discipline's seventh variant in the program (after Helmstad post-enrollment correction; PCP sensor mutation; PCP dispatcher action; Olmstead civil-rights litigation; Sun-Won pre-chain era; Salt Pond FRE 902(13)/(14) litigation-defense) — but the first variant where the boundary is structural at four claims simultaneously rather than at one. Under Kognitos, the four-claim boundary collapses to "Field 12 PASS" and the auditor speculates that "the AI used was safe for the patient" without structural footing for the epistemic-scope partitioning. The framework cannot supply the Joint Commission Sentinel Event hearing's §1.1 Daubert mapping for clinical AI.*

> ### ⚠ Framework Inarticulability #3 — §10.56 patient-safety clinical-decision-support boundary
> Kognitos has no concept of multi-claim epistemic-scope boundary discipline. The §10.56 patient-safety CDS boundary partitions four claims: (a) what the CDS said (HMAC-bound; defensible); (b) what was surfaced to the clinician (§10.11.1 ECOA-pattern chain-bound); (c) what the clinician did (chain-bound only under documented-override discipline; undocumented override is structurally invisible); (d) what happened to the patient (outside the chain; quality-improvement data is institution-side). The four-claim partition closes under §1.1 Daubert four-factor mapping for sentinel-event hearings. Field 11 + Field 12 verify the chain integrity for each row in isolation; the four-claim boundary itself has no structural representation. The auditor speculates that "the AI was safe for the patient" without footing for the epistemic-scope partitioning.

## 📋 3:30 PM — Day 1 — §10.57 multi-state aggregated reporting partition walkthrough

Patricia Donovan (CCO) took the projector for the §10.57 walk. She brought up the chain coverage map's state-partition extension.

"Five state DOH reporting cycles overlap on the same chain in the next four months. Each state has different mandatory reporting requirements. Maryland requires annual quality-of-care reporting under MD Health-General §19-308.2. Virginia requires sentinel-event reporting under 12 VAC 5-410-490. DC requires CMS-aligned reporting under DCMR 22-A. Pennsylvania requires PA-29 reporting under Patient Safety Authority. Delaware requires DPH-aligned reporting under Title 16 Del. Admin. Code. Five chain-coverage map partitions; five different chain-row subset queries; one chain."

The §10.57 multi-state aggregated reporting partition was an extension of §10.19 chain-coverage map (Salt Pond Ch10) but partitioned by *state* rather than by *contractual zone*:

```
§10.57 chain-coverage map state partitions:

Partition MD (Maryland): hospital_ids in maryland_cluster
  - reporting requirements: MD Health-General §19-308.2 annual QoC
  - chain rows: all maryland_cluster Epic instances + Hanover private cloud
                + Azure inference paths producing inferences for MD patients
  - subset query: ChainSubsetByStatePartition("MD")
  - audit-deliverable shape: MDH-QoC-2026-annual.pdf

Partition VA (Virginia): hospital_ids in virginia_cluster
  - reporting requirements: 12 VAC 5-410-490 sentinel-event quarterly
  - chain rows: all virginia_cluster Epic instances + applicable inference paths
  - subset query: ChainSubsetByStatePartition("VA")
  - audit-deliverable shape: VDH-Sentinel-2026-Q2.pdf

Partition DC (District of Columbia): hospital_ids in dc_cluster
  - reporting requirements: DCMR 22-A CMS-aligned monthly
  - chain rows: all dc_cluster Epic instances + applicable inference paths
  - subset query: ChainSubsetByStatePartition("DC")

Partition PA (Pennsylvania): hospital_ids in pennsylvania_cluster
  - reporting requirements: PA-29 Patient Safety Authority quarterly
  - chain rows: all pennsylvania_cluster Epic instances + applicable inference paths
  - subset query: ChainSubsetByStatePartition("PA")

Partition DE (Delaware): hospital_ids in delaware_cluster
  - reporting requirements: Title 16 Del. Admin. Code biannual
  - chain rows: all delaware_cluster Epic instances + applicable inference paths
  - subset query: ChainSubsetByStatePartition("DE")
```

Each partition was a deterministic-arithmetic subset query against the chain — hospital_ids enumerated for the state cluster; chain rows filtered to those hospitals; inference paths filtered to those rows' patient-records; state-specific reporting templates produced from the filtered subsets. Five deliverables; one chain artifact; five distinct shapes determined by the state DOH's required template.

Dawn walked the §10.57 partitioning against the Kognitos checklist.

There was no field for state-based partition discipline. The Kognitos twelve-row schema had no concept of *jurisdictional partitions* across the chain — analogous to the framework's silence on §10.41's temporal-slice partitioning from Ch14, but jurisdictional rather than temporal.

Field 11 verified each row's integrity individually within whichever partition it belonged to.

The structural property — that one chain artifact produced five state-DOH deliverables through deterministic partition queries — was unrepresented.

Dawn wrote in the parallel observations: *§10.57 multi-state aggregated reporting partition is the jurisdictional sibling of Ch14's §10.41 temporal-slice partitioning. Five state partitions; five reporting cycles; five audit deliverables; one chain. The framework has no concept of jurisdictional partitioning — each row reads as a discrete event with no field for which-state-cluster-it-belongs-to. Under Kognitos, the multi-state aggregated reporting collapses to "twelve fields per row" and the five state-DOH deliverables become five parallel cover-memo speculations.*

> ### ⚠ Framework Inarticulability #4 — §10.57 multi-state aggregated reporting partition
> Kognitos has no concept of jurisdictional partitioning of chain coverage. The §10.57 partition extension to §10.19 chain-coverage map enumerates five state partitions (MD/VA/DC/PA/DE) each with state-specific reporting requirements (MD Health-General §19-308.2 annual; 12 VAC 5-410-490 sentinel-event quarterly; DCMR 22-A monthly; PA-29 quarterly; Title 16 Del. Admin. Code biannual) and produces five deliverables through deterministic partition queries against the same chain artifact. Field 11 verifies each row's integrity within whichever partition it belongs to; the five-partition discipline has no structural representation. The auditor records each row in isolation; the five-state aggregated reporting is paid as five parallel cover-memo speculations.

## 🌆 5:00 PM — Day 1 — Auditor debrief whiteboard

Dawn pulled the team into the room at end of Day 1. The whiteboard tally:

- **Framework Confirmations**: 4 partial (Field 1 partial under quadrupled-timestamp; Field 11 partial across chain integrity; Field 12 partial under singular-axis verdict; Field 6 partial against clinical inputs)
- **Framework Inarticulabilities** (so far): 4
  - §10.40 four-substrate composed variant (quadrupled-timestamp, quadrupled-chain, quadrupled-HSM-signature; four additional verifications on verdict object)
  - §10.55 FDA SaMD model-clearance attestation (eight regulatory-provenance attributes; Sponsor-of-Record accountability)
  - §10.56 patient-safety clinical-decision-support boundary (four-claim epistemic-scope partition under §1.1 Daubert)
  - §10.57 multi-state aggregated reporting partition (jurisdictional sibling of Ch14 temporal-slice)
- **Framework-Silent Observations** (so far): 2
  - Four-way §10.17 dual-HSM-root composition extension across Azure + Virginia on-prem + Hanover private cloud + Epic shared-services vendor cloud
  - SDK refusal-at-capture for radiology AI ensemble outside the cleared IFU scope (analog to Eberhardt × Lumière Ch11; chain row produced only when patient indication falls within cleared scope)

Dawn capped her pen.

"§10.58 EHR-vendor co-anchor walk tomorrow at 9. Diversity sample at 11. Sarah Connaughton — the Board Chair — joins for closing at noon. Drs. Patel and Takeda will close jointly per Hartmann's note at kickoff."

Elena packed her laptop. "Dr. Takeda has been quiet through the §10.55 walk. She'll deliver tomorrow."

Mike added, "The four-substrate seam took 4.1 seconds. The verdict object lands four additional verifications. Kognitos's Field 12 records one of five total verification axes. Compounding rate just stepped up — Ch15 was one base proof plus two additionals; Ch16 is one base proof plus four additionals."

Tom rolled the projector cart out. "Same shape, deeper compound. Same drill, different substrate count."

*Note for the chapter. Day 1 closed with four Framework Inarticulabilities + four Framework Confirmations partial. The four-substrate composed variant is the third partial landing of the foresight-cluster substrate-move pressure that opened at Ch12 (after Ch14 cross-vendor + Ch15 cross-cloud); the cross-jurisdictional-cross-cloud variant remains pending for Ch17 Helvetian Tax Authority cluster-closure. The compounding factor on Field 12 multi-axis verdict mechanism stepped from one additional (Ch14) to two (Ch15) to four (Ch16). Yuki Takeda has been silent; Cyrus Patel has been silent; they will deliver Day 2.*

## 🔗 9:00 AM — Day 2 — §10.58 EHR-vendor co-anchor cross-tenant hash binding walkthrough

Raj walked the §10.58 EHR-vendor co-anchor framework on Day 2 morning. The Epic shared-services vendor-managed cloud was Epic's own audit-trail discipline running in Epic's environment under Epic's HSM root; Lyceum's chain hash-anchored Epic's seals through cross-tenant hash binding.

The §10.58 cross-tenant anchor structure was structurally distinct from Ch11's cross-vendor zero-trust composition (one-time model handover with byte-equal SHA-256 join at §10.21 seam) — §10.58 was *ongoing* operational composition with daily cross-anchor refresh under §10.58 cross-tenant freshness contract.

Raj brought up the daily cross-tenant anchor record:

```json
{
  "anchor_id": "lyceum/cross-tenant-anchors/2026-04-22#epic-shared-services",
  "tenant": "lyceum",
  "event_class": "ehr_vendor_co_anchor",
  "audit.co_anchor.vendor_name": "Epic Systems Corporation",
  "audit.co_anchor.vendor_tenant_id": "epic-shared-services-lyceum",
  "audit.co_anchor.vendor_seal_id": "epic-shared/seals/2026-04-22#epic-hsm",
  "audit.co_anchor.vendor_seal_sha256": "f8a3...2e91",
  "audit.co_anchor.vendor_hsm_attestation_doc_sha256": "a5d7...3e44",
  "audit.co_anchor.cross_tenant_freshness_window_hours": 26,
  "audit.co_anchor.last_refreshed_utc": "2026-04-22T23:59:00Z",
  "audit.co_anchor.staleness_alert_threshold_hours": 30,
  "audit.co_anchor.vendor_seal_published_to_lyceum_at_utc": "2026-04-23T00:14:00Z",
  "audit.co_anchor.lyceum_anchor_signature": "...",
  "hmac": "...",
  "merkle_path": [...]
}
```

Raj walked the structure aloud. Epic produced its own daily seal under Epic's HSM at 23:59 UTC. Epic published the seal's SHA-256 plus HSM attestation document to Lyceum within the 26-hour freshness window required by the §10.58 cross-tenant freshness contract (Epic's runbook required publication within 6 hours; Lyceum's runbook required reception within 30 hours; the operational margin was substantial). Lyceum's chain produced a daily co-anchor row that bound Epic's seal SHA-256 + Epic's HSM attestation hash under Lyceum's MAC + Lyceum's HSM signature. The cross-tenant anchor row was Lyceum's structural representation of Epic's chain — Lyceum did not have Epic's individual chain rows, but Lyceum's chain bound Epic's *seal hash* under MAC and could verify that Epic's chain had not been retroactively modified.

The §10.58 staleness contract was load-bearing — if Epic's seal failed to publish within the freshness window, Lyceum's chain produced an alert chain row and Epic's data was treated as stale until reconciliation. The thirteen-month operational history showed zero stale-window incidents across both Lyceum and Epic; the freshness contract was operating well within margin.

Dawn walked the §10.58 against the Kognitos checklist.

Field 6 (input data + source attribution). The vendor's name + tenant ID + seal ID + seal hash were source-attribution metadata. Field 6 partially applied. The cross-tenant freshness contract was structural metadata about the binding's freshness — no field for freshness-as-state.

Field 11 + Field 12. Verified.

The cross-tenant ongoing-composition property — that Lyceum's chain bound Epic's chain through daily refresh under a freshness contract — was unrepresented. Field 6 read each refresh row as a discrete source-attribution event; the ongoing composition was the structural property the framework could not articulate.

Dawn wrote in the parallel observations: *§10.58 EHR-vendor co-anchor cross-tenant hash binding is the ongoing operational composition variant of Ch11's cross-vendor zero-trust composition. Ch11 was one-time handover at §10.21 seam; §10.58 is daily refresh under freshness contract. The freshness-as-state property — that the cross-tenant anchor is current within a defined window or alerts as stale — is structurally analogous to Ch13's consent-lifecycle-as-state (Saraswati) but for cross-vendor chain composition. Under Kognitos, Field 6 partial-fits per refresh row; the ongoing composition with freshness-as-state is invisible.*

> ### ⚠ Framework Inarticulability #5 — §10.58 EHR-vendor co-anchor cross-tenant hash binding
> Kognitos has no concept of ongoing operational cross-vendor chain composition under freshness contract. The §10.58 EHR-vendor co-anchor pattern produces a daily cross-tenant anchor row binding the vendor's seal SHA-256 + vendor HSM attestation hash + cross-tenant freshness window hours + staleness-alert threshold + last-refreshed UTC + vendor-seal-published timestamp + Lyceum anchor signature. The freshness-as-state property is structurally analogous to Ch13 consent-lifecycle-as-state but for cross-vendor chain composition. Field 6 partial-fits each refresh row as discrete source-attribution event; the ongoing composition with freshness-as-state under contractual binding is structurally invisible. The auditor speculates that "Epic and Lyceum are connected" without structural footing for the cross-tenant ongoing composition.

## 🔧 11:00 AM — Day 2 — Diversity sample trace across the four-substrate architecture

Mike and Diana walked the diversity sample after morning tea. Ten records spanning the architecture across all four substrates and across all five state clusters:

1. **2026-04-22 sepsis-ML inference to bedside CDS at Virginia Medical Center Arlington** — four-substrate paired-quadruple chain entry (§10.40 walk). Verifier PASS in 4.1s with four additional verifications.

2. **2026-04-15 radiology AI ensemble inference at Maryland Medical Center Baltimore** — §10.55 FDA SaMD attestation row. Verifier PASS in 1.6s.

3. **2026-03-08 documented-override at Pennsylvania Medical Center Pittsburgh** — clinician acknowledged sepsis-ML alert but documented override (`reason_code: "clinical_judgment_alternative_diagnosis_pneumonia"` + free-text rationale) — §10.56 (c) documented-override chain pivot. Verifier PASS in 1.1s.

4. **2026-02-14 §10.55 IFU-drift detection at DC Medical Center** — FDA published Letter to Industry updating DEN240187 IFU; chain detected the IFU hash mismatch at next inference; refusal-at-capture pattern halted radiology AI inferences pending Lyceum's reauthorization-of-deployed-IFU runbook step. Verifier PASS in 1.4s on the alert chain row; no inference rows produced during the 7-hour reauthorization window.

5. **2026-01-22 21 CFR Part 11 clinical-trial subject screening at Lyceum-private-cloud Hanover** — chain row for the screening event including subject ID, consent record reference, eligibility-criteria check. Verifier PASS in 1.0s.

6. **2026-04-22 Epic shared-services daily co-anchor refresh** — §10.58 cross-tenant anchor (today's diversity-sample-day refresh). Verifier PASS in 1.2s.

7. **2026-03-31 Q1 2026 cross-state MD/VA/DC/PA/DE aggregated reporting** — five state-partition deliverables produced from the chain artifact through §10.57 partition queries. Each verifier PASS in 1.3-1.5s.

8. **2025-12-04 FDA Sponsor-of-Record attestation chain row** — Dr. Yuki Takeda's NPI bound under MAC as Sponsor-of-Record for DEN240187 (post-clearance attestation; refreshed annually under §10.55 attestation refresh cycle). Verifier PASS in 1.0s.

9. **2026-04-01 Maryland DHMH annual QoC reporting deliverable** — Patricia Donovan filed the MD Health-General §19-308.2 annual report from a §10.57 MD-partition query; verifier PASS in 1.3s with state-partition cross-reference.

10. **2026-04-20 Joint Commission sentinel-event preparatory chain row** — Dr. Cyrus Patel prepared a sentinel-event hearing brief for a 2025-Q4 case using §10.56 four-claim partition; chain row bound the brief's structural-evidence anchors under MAC. Verifier PASS in 1.2s.

Ten records traced end-to-end. Ten for ten verified under the reference spec.

Dawn ran the Kognitos twelve-row template against each. Records 1 (four-substrate seam), 2 (§10.55 SaMD), 3 (§10.56 documented-override), 4 (IFU-drift refusal-at-capture), 6 (§10.58 co-anchor), 7 (multi-state partitioning), 8 (Sponsor-of-Record attestation), 9 (state DOH deliverable), and 10 (sentinel-event brief) all triggered Framework Inarticulabilities documented above. Record 5 (clinical-trial screening on Lyceum-private-cloud) was the closest to a clean-fit — the chain row carried clinical-decision metadata that Kognitos's twelve fields could partially recognize, though Fields 4 + 8 still form-mismatched against the eligibility-criteria-check structure.

The diversity sample's framework-fit distribution: ten for ten under the reference spec; under Kognitos, nine of ten produced inarticulability or governance-ceremony silence or form-mismatch, and one (record 5 clinical-trial screening) produced partial-fit. Approximate 10% clean-fit rate is a slight increase from Polaris's 0% — the multi-substrate architecture compounds losses across substrates but the clinical-research surface preserves enough of the AI-decision mental model that one record can partial-fit.

Dawn wrote in the parallel observations: *Lyceum's diversity sample produces 1-of-10 partial-fit + 9-of-10 inarticulability/silence/form-mismatch under Kognitos. The clean-fit rate is approximately ten percent — higher than Polaris's zero percent (which had no AI-decision surface clean enough to fit the framework) but well below the multi-substrate architecture's reference-spec coverage (which records all ten cleanly). The pattern predicts that multi-substrate composed-architecture engagements where one surface preserves clean AI-decision mental model (clinical research; revenue cycle; back-office ML) will show modest clean-fit rates against Kognitos while the composed-architecture surfaces (clinical CDS pipeline; multi-state aggregated reporting; cross-vendor co-anchor) produce zero clean-fit.*

## 🌆 12:00 PM — Day 2 — Closing memo composition + Takeda + Patel joint statement

Sarah Connaughton joined the close at noon. Mid-sixties, navy suit, Board Chair for seven years, former CEO of a regional payer organization. She sat at the head of the Board of Trustees table. Dr. Hartmann, Dr. Patel, Dr. Takeda, Patricia Donovan, Marcus Sieber, Greg Holloway, Dorothy Brennan filled the remaining seats.

Dawn walked the cover memo:

> **Spec-section confirmation pass — Lyceum Health System — pre-Joint Commission + HHS OCR + FDA post-market surveillance + five state DOH readiness**
>
> The audit team confirms, under the FFIEC chain-of-custody v1.0b reference specification, that the following five sections were exercised in production at Lyceum Health System and verify cleanly:
>
> - **§10.40 four-substrate composed variant** — first four-substrate composition in the program; on-prem Epic (five state HSM clusters) + Lyceum-owned private cloud Hanover + Microsoft Azure Mid-Atlantic public cloud + Epic shared-services vendor-managed cloud; §10.17 four-way HSM-root composition; 4.1s verifier PASS with four additional verifications.
> - **§10.55 FDA SaMD model-clearance attestation** — eight regulatory-provenance attributes bound under MAC including FDA clearance number DEN240187 + Sponsor-of-Record identity (Dr. Yuki Takeda NPI) + IFU SHA-256 + indications-match check + deployed-model-artifact match boolean + adverse-event subscription status; IFU-drift detection demonstrated on the 2026-02-14 FDA Letter to Industry response.
> - **§10.56 patient-safety clinical-decision-support boundary** — four-claim epistemic-scope partition (CDS-said / surfaced-to-clinician / clinician-acted / patient-outcome); §1.1 Daubert four-factor mapping closure for Joint Commission Sentinel Event hearings; two prior sentinel-event hearings closed under structural boundary in eighteen months.
> - **§10.57 multi-state aggregated reporting partition** — five-state partitioning (MD/VA/DC/PA/DE) with state-specific reporting templates (MD §19-308.2 annual; VA 12 VAC 5-410-490 sentinel quarterly; DC DCMR 22-A monthly; PA-29 PSA quarterly; Title 16 Del. Admin. Code biannual); five deliverables from one chain artifact via deterministic partition queries.
> - **§10.58 EHR-vendor co-anchor cross-tenant hash binding** — daily cross-tenant anchor binding Epic shared-services seal SHA-256 + Epic HSM attestation hash under Lyceum MAC; freshness contract 26-hour window / 30-hour staleness threshold; thirteen-month operational history with zero stale-window incidents.
>
> Under the Kognitos twelve-field AI audit-trail framework: 4 Framework Confirmations partial (Fields 1, 6, 11, 12 under singular-axis mental model). 5 Framework Inarticulabilities documented in the firm's parallel observations: §10.40 four-substrate composed; §10.55 FDA SaMD attestation; §10.56 patient-safety CDS boundary; §10.57 multi-state partitioning; §10.58 cross-tenant ongoing composition. 2 Framework-Silent Observations: four-way §10.17 dual-HSM-root composition extension; SDK refusal-at-capture for IFU-out-of-scope inferences.
>
> Diversity sample (10 records): 10 for 10 verified under reference spec. 1 of 10 partial-fit under Kognitos (clinical-trial screening on private cloud); 9 of 10 produce inarticulability, governance-ceremony silence, or form-mismatch.

Sarah Connaughton read the memo. She passed it to Dorothy Brennan; Dorothy skimmed the §1.2 + §1.1 Daubert appendix and nodded. Sarah placed the memo down and looked at Drs. Patel and Takeda.

"You said at the kickoff yesterday that you'd close jointly. Cyrus first?"

Dr. Patel uncapped his pen, looked at his tablet, and looked up.

"I'm the Chief Quality Officer of Lyceum Health System. The Joint Commission's Sentinel Event Policy makes me personally accountable to the Board's Quality Committee for any sentinel event that involves an AI system. The Board has a fiduciary duty to ensure that the institution's audit-trail discipline can defend a sentinel-event hearing structurally — not editorially. The §10.56 four-claim boundary is what gives that defense. The framework you brought today carries Field 12 as a singular verdict. The boundary I have to defend is four claims, with four different evidentiary frames, under §1.1 Daubert four-factor mapping. The framework cannot supply the boundary.

"I have read the cover memos from Maya Hartwell at Polaris three weeks ago; from Aparna Desai at Saraswati six months ago; from Heinrich Becker and Sébastien Aubert at Eberhardt × Lumière a year ago; from Pankaj Iyengar at NetiVa two years ago. The framework has not carried any of their engagements either. The pattern is the program's running observation. On the record: the Kognitos twelve-field framework is acceptable as a vendor-facing summary of an AI-decision audit-trail. It is not acceptable as the only assessment artifact for a hospital system where any clinical AI inference is one chain row away from a Joint Commission sentinel-event hearing. The patient-safety boundary requires structural representation in the chain — the four-claim epistemic-scope partition cannot be reconstructed editorially after a sentinel-event hearing has opened.

"Sarah, you've heard me. The cover memo's appendix carries my statement. The Board Quality Committee's quarterly review packet will name the framework-substitution recommendation. On the record."

Dr. Takeda spoke next, deliberately.

"My name is on the FDA Sponsor of Record registration for DEN240187. 21 CFR §807.81 makes me personally accountable for the radiology AI ensemble's post-market performance. 21 CFR §820.198 makes me personally accountable for adverse-event reporting. If a patient experiences a missed pulmonary embolism diagnosis because the radiology AI failed to flag the embolism and the failure was a known device defect, the FDA's enforcement action against deficient post-market surveillance names *me* as Sponsor — not Radial Diagnostics Inc. as manufacturer, not Lyceum Health System as institution. The FDA register entry is in my name.

"I have read Maya Hartwell's PRA SM&CR statement from Polaris three weeks ago. Same shape, different register. Maya's accountability flows through the PRA register entry for SMF26; mine flows through the FDA Sponsor of Record registration for DEN240187. The structural distinction is sharp — Maya carries ongoing-institutional-management accountability under a Senior Manager regime; I carry specific-product-post-market-surveillance accountability under a SaMD device clearance. Both are individual-register-named accountability. Maya's framework-substitution recommendation reads structurally identical to what I'm about to file.

"On the record: the Kognitos twelve-field framework is acceptable as a vendor-facing summary. It is not acceptable as the only assessment artifact for any FDA-cleared AI/ML SaMD device in active clinical use where a named Sponsor of Record carries personal accountability under 21 CFR §807.81 + §820.198. The framework cannot articulate the eight regulatory-provenance attributes of the §10.55 attestation; it cannot articulate the IFU-drift detection; it cannot articulate the indications-match refusal-at-capture; it cannot articulate Sponsor-of-Record identity under MAC binding. The framework records 'Field 4: radiology AI v23.2' and loses the seven other binding attributes that make the device legally deployable.

"Cyrus and I are co-signing the framework-substitution recommendation under our respective personal-register-named accountabilities — his under Joint Commission Sentinel Event Policy / board fiduciary, mine under FDA SaMD Sponsor of Record. Different registers. Same shape. The cover memo carries both. The FDA post-market surveillance packet, the Joint Commission triennial packet, the HHS OCR routine packet, the CMS Promoting Interoperability packet, and the five state DOH cycle deliverables all carry both statements. On the record."

Sarah Connaughton wrote a short note in her own notebook — the Board Quality Committee's continuous-oversight discipline would absorb both statements as institution-wide signals. She looked at Dawn.

"You'll have both in the cover memo's appendix?"

"Both. Head of the reading-order, before the spec-section confirmation pass."

Sarah signed the receipt at 12:46 PM.

The engagement closed at 12:48 PM.

*Note for the chapter. Ninth settled voice-pattern variant introduced: personal-FDA-Sponsor-of-Record statement under SaMD post-market-surveillance accountability (Dr. Yuki Takeda). Distinct from Maya Hartwell's eighth-variant SM&CR statement because FDA Sponsor registration is product-specific not institutional-management-wide. Co-signed with cross-functional-executive joint dimension (Dr. Cyrus Patel CQO under Joint Commission Sentinel Event Policy / board fiduciary accountability) — Patel's statement reproduces the cross-functional executive joint pattern from Patrick + Naomi Ch10 with the new sharper dimension of board-level patient-safety accountability under Joint Commission's Sentinel Event Policy. Stakeholder explicit-attribution streak extends to 11-in-16 chapters. Voice-pattern catalog reaches 9 settled variants plus 1 candidate tenth (Ch14 return-engagement institutional-memory observation; still provisional pending second-instance reproduction). Foresight-cluster §10.40 substrate-move pressure lands third partial increment at Ch16 (four-substrate composed variant on-prem + private cloud + public cloud + EHR-vendor cloud within five-state-cluster discipline); cross-jurisdictional-cross-cloud variant remains pending for Ch17 Helvetian Tax Authority cluster-closer. §12 amendment streak remains broken from Ch12 — Polaris's §10.40 cross-cloud + §10.51-§10.54 shipped in the fifth errata; Lyceum's §10.40 four-substrate + §10.55-§10.58 shipped in the sixth errata; Ch17 is positioned to restart the §12 streak with the cross-jurisdictional-cross-cloud cluster-closing amendment. Engagement closes within budget.*
