# 05 — Helmstad BioSciences (Kognitos-lens)

*A clinical-trial readiness audit where the chain works perfectly and the framework still cannot articulate the finding that matters*

**Engagement:** FDA Bioresearch Monitoring (BIMO) pre-inspection readiness audit
**Client:** Helmstad BioSciences — mid-size oncology biopharma; AI clinical-trial-eligibility classifier on Phase II NSCLC trial; chain live for 4 months
**Status:** FDA inspectors arrive in 6 weeks; the engagement is explicitly "run readiness like the inspector will run it"
**Audit team lead:** Dawn
**Client liaison:** Dr. Henrik Bjornsson, Chief Compliance Officer; Dr. Mona Acharya, Clinical Quality Director

**Audit team's framework:** Kognitos's 12-field schema. This is the fourth bifurcated engagement (after Mercator, Stelvio, and Atrio's multi-tenant variant). The team has practiced the pattern: staple framework runs, write coverage-boundary prose, file under-reportings when the reference spec catches findings the framework can't articulate. Helmstad introduces a new scenario the team has not yet encountered — a **chain-integrity-clean / source-data-wrong** finding that does not fit any Kognitos field.

---

## 🌅 8:30 AM — Kickoff (Six Weeks Before BIMO)

Henrik walked into the engagement room with the printed §10.19 coverage map. Five categories. Green: the nsclc-phase2 eligibility classifier (4 months live, all eligibility decisions chained). Red: legacy regulatory and clinical-ops platforms, EDC, CRO data feeds, lab/LIMS, email/SharePoint.

"The FDA inspector arrives in six weeks. We're asking you to run readiness like the inspector will run it. BIMO methodology. Witness-mode verification on a laptop the inspector brings. Seven-artifact evidence pack as the inspection-day playbook."

Dawn looked at the map.

"You've handed us the coverage map. Under our framework — the Kognitos 12-field schema — we don't have a row for it. We've run three bifurcated engagements; the pattern by now is to staple two framework runs and write the boundary in prose. Your inspector is going to expect §1.2 (c) language for any chain-integrity-versus-process-design distinction. We need to know how to map that distinction into our framework."

Henrik nodded.

"Mona's the right person to walk you through the eligibility classifier. The clinical-quality side is where she lives. Let me also flag — we have one open clinical-quality finding from a five-decision reconciliation we ran internally last week. The classifier worked correctly. The chain captured what the classifier saw. The EHR was corrected after the classifier saw it. We need your framework to record this honestly; we don't want the inspector reading a finding-against-the-chain when the chain did exactly what it was supposed to."

Dawn put her coffee down.

"That's the April 15 patient?"

"That's the April 15 patient. T3N2M0 staging at the time the classifier saw the record. Corrected to T3N2M1 two days after enrollment. M1 disease excludes from this trial. The classifier recommended enrollment based on the staging it saw; the staging was wrong; the patient enrolled; medical-monitor follow-up was initiated when we caught the correction. The chain captured everything — what the classifier saw, what it said, what got enrolled. The finding is about the upstream staging correction not back-feeding to the screening pipeline, not about the chain."

Dawn wrote in her template: *◇ The April 15 patient. Chain-integrity clean. Source-data wrong. Process-design CAPA, not chain-integrity finding. Under the bank's reference spec, §1.2 (c) handles this — chain proves what the model said about the input it was given; input authenticity is governed by upstream storage controls. Under our framework, there is no field for this distinction. We will need to write the finding in cover-memo prose and explicitly note that no Kognitos field fails.*

She wrote a second note: *Witness mode. Inspector runs verifier without IKM access. Output is `PASS-STRUCTURALLY` rather than `PASS`. Kognitos has no concept of witness mode. The inspector trying to verify under Kognitos would need IKM access or would need to trust the institution. The bank's reference spec gives the inspector a workable path; the framework does not.*

---

## 🧬 9:30 AM — The Eligibility Classifier (Field Walk)

Mona pulled up the eligibility classifier. The model classified incoming candidates into one of five eligibility buckets: clear-eligible, eligible-with-monitoring, ineligible-by-stage, ineligible-by-comorbidity, escalate-to-medical-monitor. Each classification was a chain entry.

She picked a March 22 classification. The entry had:

```json
{
  "entry_id": "elig-2026-03-22-helmstad-04417",
  "tenant": "helmstad-clinical-trials",
  "service": "nsclc-phase2-eligibility",
  "seq": 4417,
  "ts": "2026-03-22T11:23:47.812Z",
  "model_id": "helmstad/nsclc-eligibility-v2.3",
  "model_version": "v2.3.1-validated-2025-12",
  "gen_ai.request.model": "helmstad/nsclc-eligibility-v2.3",
  "gen_ai.response.model": "helmstad/nsclc-eligibility-v2.3",
  "prompt": {
    "staging": "T3N2M0",
    "egfr_mutation": "L858R",
    "alk_translocation": "negative",
    "ecog_status": 1,
    "prior_systemic_therapy": "none",
    "comorbidity_score": 4,
    "input_source_pointer_hash": "sha256:..."
  },
  "response": {
    "eligibility_bucket": "eligible-with-monitoring",
    "confidence": 0.91,
    "monitoring_flags": ["ecog_borderline_within_screening_window"]
  },
  "audit.deployment.intent": "production",
  "audit.deployment.policy_version": "helmstad-mrm-2026q1",
  "audit.redaction.disposition": "redacted_at_sdk",
  "payload_hash": "...",
  "payload_hash_alt": "...",
  "hmac": "...",
  "merkle_path": [...],
  "daily_seal_ref": "2026-03-22-d-seal-helmstad-clinical-trials"
}
```

Mike worked his template:
- Field 1 (Timestamp) — RFC 3339 millisecond UTC. ✓
- Field 2 (Decision ID) — `entry_id` per classification. ✓
- Field 3 (Authenticated human identity) — the screening coordinator's identity on the chain entry that triggered the classification. ✓
- Fields 4-5 (System / Model identity) — `model_id`, `model_version`, `gen_ai.request/response.model`. ✓
- Field 6 (Inputs) — staging, mutations, ECOG, comorbidity, with `input_source_pointer_hash` linking to the source EHR record. ✓
- Field 7 (Policy/prompt) — `audit.deployment.policy_version` = `helmstad-mrm-2026q1`. ✓
- Field 8 (Reasoning) — monitoring_flags + confidence give the human-readable reasoning. ✓
- Field 9 (Output) — eligibility bucket and confidence verbatim. ✓
- Field 10 (Downstream action) — linked to the screening-decision record via parent_run_id. ✓
- Field 11 (Human review) — if the bucket is `escalate-to-medical-monitor`, the medical monitor's review is chained. Not applicable on this entry. ✓
- Field 12 (Integrity proof) — HMAC + Merkle + Ed25519 + CloudHSM. ✓

Plus he noticed `payload_hash_alt`.

"What's `payload_hash_alt`?"

Mona: "Per §4.1.3 per-event MAC algorithm agility. The primary MAC is HMAC-SHA-256; the alternate is HMAC-SHA-3-256. We emit both as a 25-year retention safety margin in case HMAC-SHA-256's security degrades over the retention horizon. The verifier today only checks the primary; if SHA-256 is ever deprecated, the verifier can dispatch on the alternate."

Mike wrote that down. Kognitos has no field for algorithm agility. ◇.

Plus the `audit.redaction.disposition = "redacted_at_sdk"` attribute. Mona explained: pre-MAC redaction discipline per §10.22. The SDK redacts PHI before computing the per-event MAC, so the canonical bytes the MAC covers do not contain raw PHI. The disposition attribute makes the redaction policy mechanical for an inspector reading any chain entry.

> ### ✓ Confirmation #1 — All 12 fields satisfied on eligibility classification entry
>
> Field 1-12 cleanly satisfied. `payload_hash_alt` adds algorithm-agility depth (framework-silent). `audit.redaction.disposition` makes redaction mechanical (framework-silent). The `audit.deployment.intent` enum is richer than Ch02's set: `production / validation / regulatory_sandbox` for clinical workflows (framework-silent).

> ### ◇ Framework-Silent Observations #1-3 — Algorithm agility, pre-MAC redaction disposition, clinical-context deployment-intent

---

## 🔍 10:30 AM — Witness Mode

Dawn wanted to see witness mode operationally. Henrik had said the FDA inspector would run the verifier on a laptop the inspector brought. The inspector would not have IKM access.

```
$ herald-verify --tenant=helmstad-clinical-trials \
                --service=nsclc-phase2-eligibility \
                --date=2026-03-22 \
                --entry-id=elig-2026-03-22-helmstad-04417 \
                --witness-mode \
                --strict
```

```
Status: PASS-STRUCTURALLY
Step:   12 (steps 7-9 skipped under witness-mode)
Reason: chain structure verified, Merkle path resolved,
        signature verified against public key
        helmstad-clinical-prod-2026-q1.
        Per-event MAC recompute not performed
        (IKM access not available in witness mode).
```

Dawn read the output twice.

"`PASS-STRUCTURALLY` is a distinct verdict from `PASS`. The inspector gets structural integrity but does not get per-event MAC verification. The framework you operate under makes this an explicit verdict in the exit-code contract; under our framework, there's no language for partial-verification verdicts."

Mona: "§10.12 names the verdicts: `PASS`, `PASS-STRUCTURALLY`, `FAIL`, exit codes 0, 0-with-flag, 1/2/3. The witness-mode verdict is distinct so a downstream inspector or auditor can record the level of trust they have. Per-event MAC recompute requires IKM; structural verification doesn't. An inspector arriving with a laptop they bring runs witness-mode and gets verifier output that is honest about what was and was not verified."

Dawn wrote that down.

The Kognitos framework has no concept of witness mode. An inspector under Kognitos would either:
- Be given IKM access (compromises the cryptographic isolation)
- Trust the institution's own verifier output (compromises independent verification)
- Run a partial verification with no framework-supplied vocabulary for what was verified vs. what was not

Each option weakens the audit. The bank's reference spec provides a fourth: witness-mode verification with an explicit verdict. The framework does not.

> ### ◇ Framework-Silent Observation #4 — Witness-mode verification verdict
>
> The bank's reference spec gives downstream inspectors a workable verification path that does not require institutional credentials and that produces an honest, framework-articulated verdict (`PASS-STRUCTURALLY`) when per-event MAC recompute is not possible. The Kognitos framework has no equivalent. Inspectors operating under Kognitos either compromise on IAM or compromise on independence.

---

## 🔐 11:30 AM — IAM Split

Diana ran the IAM walkthrough. Chained AI service-account discipline on the green side; 12 DBAs with UPDATE permission on the legacy clinical-ops databases.

The AI side: `nsclc-eligibility-prod@helmstad-clinical-trials` service identity, chain-driven IAM, no break-glass account. ✓ Field 3 satisfied with the same chain-driven depth recorded in Chapters 01-04.

The legacy side: 12 DBAs with table-level UPDATE permission across the clinical-ops databases. The access review attests group membership (yes/no, is the person in the DBA group), not table-level modification (what they actually did with the access). Diana wrote: ✗ Field 3 partially failed for legacy clinical-ops — identity is captured at access; lifecycle integrity is not.

> ### 🚨 Finding-001 — Legacy clinical-ops 12-DBA UPDATE access; access review attests group membership not table-level activity (Field 3 partial fail)
>
> Twelve DBAs hold table-level UPDATE permission across legacy clinical-ops databases. Access reviews confirm group membership but do not capture row-level modifications. Field 3 (authenticated human identity) is satisfied at the moment of access but lifecycle integrity is gone. **Finding against bank.** Phase 2 remediation extends chain-driven IAM discipline to clinical-ops.

---

## 🩺 1:00 PM — The April 15 Patient (Where The Framework Stops Articulating The Finding)

After lunch, Mona walked the team through the April 15 patient. This was Chapter 05's lens-stretching scenario.

She pulled up the chain entry for the classification.

```
elig-2026-04-15-helmstad-04823
ts:      2026-04-15T09:47:11.234Z
input:   staging=T3N2M0, egfr=L858R, ecog=1, comorbidity=4
output:  eligibility_bucket=eligible-with-monitoring
         confidence=0.94
         monitoring_flags=["ecog_borderline_within_screening_window"]
```

Then she pulled up the screening-to-enrollment chain entry from the same day.

```
screening-2026-04-15-helmstad-04823
ts:      2026-04-15T14:11:38.491Z
decision: enrolled
basis:    elig-2026-04-15-helmstad-04823
enrolled_by: dr_kim (screening coordinator)
```

Then she pulled up the EHR-correction record from two days later.

```
ehr-correction-2026-04-17-helmstad
ts:                 2026-04-17T16:23:09.000Z
patient:            (redacted; subject-keyed reference)
field_corrected:    staging
original_value:     T3N2M0
corrected_value:    T3N2M1
correction_reason:  "Bone scan re-read after enrollment;
                    metastatic lesion confirmed L3 vertebral body"
correction_by:      dr_alvarez (oncology fellow)
```

Mona: "The classifier saw T3N2M0 and said `eligible-with-monitoring`. The classifier worked correctly on the input it was given. The staging was corrected two days after enrollment — the bone scan was re-read, an L3 metastatic lesion was found, and the staging was changed from M0 to M1. M1 disease excludes from this trial. The patient enrolled; medical-monitor follow-up was initiated when we caught the correction last week."

She paused.

"Under our reference spec, this distinction is §1.2 (c) — the chain proves what the model said about the input it was given; input authenticity is governed by upstream storage controls. The chain finding here is: the chain captured the classifier's decision correctly. The process finding here is: the upstream EHR's late staging correction did not back-feed to the screening pipeline. Two different findings. One chain-integrity-clean. One process-design-CAPA."

Mike worked his template.

- **Field 1 (Timestamp).** The classification timestamp is correct. ✓
- **Field 2 (Decision ID).** Unique per classification. ✓
- **Field 3 (Authenticated human identity).** The screening coordinator's identity is captured. ✓
- **Field 4 (AI system identity).** Correct. ✓
- **Field 5 (Model identity).** Correct. ✓
- **Field 6 (Inputs received with source attribution).** Staging=T3N2M0 was the input. The `input_source_pointer_hash` references the source EHR record AS IT WAS at classification time. ✓ — the input was captured accurately with attribution.
- **Field 7 (Policy/prompt).** Correct. ✓
- **Field 8 (Reasoning).** The model's reasoning given the input was sound. ✓
- **Field 9 (Output).** `eligible-with-monitoring` was what the model returned. ✓
- **Field 10 (Downstream action).** The patient was enrolled. The enrollment record links back to the classification. ✓
- **Field 11 (Human review).** The screening coordinator reviewed the classification. ✓
- **Field 12 (Integrity proof).** The chain integrity is sound. ✓

**Every Kognitos field is satisfied.**

Mike paused his pen.

"Under our framework, this entry passes every field. But there's a finding here — the patient enrolled on an M0 staging that was later corrected to M1, and the correction did not propagate back to the screening pipeline. The framework cannot record this. The bank's reference spec records it as a process-design CAPA under §1.2 (c) — chain-integrity clean, source-data wrong."

He turned to Dawn.

"Where does this finding go?"

Dawn took her time.

"It doesn't have a Kognitos field. The framework's Field 6 asks for inputs with source attribution; the input was captured with attribution at the time the model saw it. The framework doesn't address what happens when the input is later corrected upstream and the correction doesn't back-feed. The framework treats the per-event row as the unit of analysis; the finding here is about upstream-source-data lifecycle across multiple events, which is not a row property."

She continued.

"This goes in the cover memo. We write it as a process-design finding, not a chain-integrity finding. We cite §1.2 (c) from the bank's reference spec as the conceptual frame even though we're operating under our framework. We explicitly note that no Kognitos field fails — the chain did exactly what it was supposed to do — and that the finding is detectable only because the institution ran the cross-event reconciliation and saw the M0-to-M1 correction. Under our framework alone, an institution that did not run that reconciliation would never surface this finding."

Mike wrote.

She added: "This is the third category of framework-side issue, after speculation and under-reporting. **Framework cannot articulate the finding shape.** Speculation = auditor invents anchors. Under-reporting = framework misses findings the reference spec catches. **Inarticulable** = the finding exists, the reference spec has language for it, the framework has no row that could be used to file it under any reasonable reading."

> ### 🚨 Process-design CAPA (NOT chain-integrity Finding) — April 15 patient enrollment on M0 staging later corrected to M1
>
> The eligibility classifier received T3N2M0 staging on April 15, classified the patient as eligible-with-monitoring, and the patient enrolled. The staging was corrected to T3N2M1 (M1 = excludes from trial) two days after enrollment. The correction did not back-feed to the screening pipeline. **Every Kognitos field is satisfied — the chain did exactly what it was supposed to do.** This is filed as a process-design CAPA, citing the bank's reference spec §1.2 (c) (chain proves what the model said about the input it was given; input authenticity is governed by upstream storage controls). Medical-monitor follow-up was initiated last week.

> ### ◇ Framework Inarticulability #1 — Cross-event upstream-source-data lifecycle finding
>
> The framework's Field 6 captures input at classification time. The framework does not have a row for "upstream source-data later corrected; correction did not back-feed." This finding is detectable only because the institution ran cross-event reconciliation. Under Kognitos alone, the finding would be invisible.

---

## 🧪 2:30 PM — Five-Decision Reconciliation Test

Dawn ran her standard reconciliation. Five random eligibility decisions across the 4-month operational window.

```
5 decisions selected — eligibility classifications from Jan-Apr 2026.

Inference reconciliation (chain → operational decision view):
  5/5 PASS

Backward reconciliation (chain → source EHR record):
  2/5 clean
  1/5 corrected-source discrepancy (the April 15 patient; T3N2M0 → T3N2M1)
  2/5 blocked by CRO retention window (CRO retains source data 30 days only;
      audit window exceeds CRO retention)

Forward reconciliation (chain → enrollment/medical-monitor records):
  5/5 PASS (all classifications produced downstream actions that matched
            the chain entry)
```

The 2/5 blocked-by-CRO-retention failures were a new pattern. The CRO (contract research organization) retained source data for 30 days only; the audit window for older decisions exceeded the CRO's retention.

Mona explained the contract reframing. The internal friction at Helmstad over extending the chain to the CRO had been recurring for 18 months. The five-decision reconciliation crystallized the issue: 2 of 5 backward reconciliations were blocked not because the chain failed but because the upstream source was no longer available. The next CRO contract renewal would include a §10.21 cross-vendor model-handover clause requiring the CRO to retain source data for the deployment-window + investigation-buffer floor.

> ### 🚨 Finding-002 — CRO source-data retention shorter than audit window (Field 6 + §10.20-style retention floor failure)
>
> CRO retains source EHR data for 30 days; the audit window for older eligibility decisions exceeds CRO retention. Backward reconciliation is blocked for 2 of 5 sampled decisions. Field 6 (inputs with source attribution) is satisfied at the chain entry but the source data attribution becomes unverifiable beyond 30 days. Remediation: §10.21 cross-vendor model-handover clause in next CRO contract renewal, requiring CRO to retain source data for the deployment-window + investigation-buffer floor (540 days equivalent).

---

## 📋 3:30 PM — Legacy Walkthrough

Diana walked the legacy systems quickly because by now the patterns were familiar.

- **Legacy DBA UPDATE permission** — §10.3 architectural target. Finding (Field 3 / Field 12 partial). Already filed as Finding-001.
- **LIMS same shape** — DBA UPDATE on lab data. Same finding pattern; second instance.
- **CTMS Visit Summary field history disabled** — §10.22 / §4.4.6. Finding (Field 1 / Field 6 / Field 12).
- **EDC extract has no chain (§4.4.6 forward-readiness)** — Partial. The EDC delivers files daily; the bank's reference spec normates a streaming change-stream mirror under §4.4.6 + §10.16 for the next phase.
- **CTMS overwrite-able (§10.22 redaction)** — Finding (Field 12).
- **Late-Effective-Date filter discoverability (§10.18)** — under the reference spec this would be a Nit; under Kognitos no field. Framework Under-Reporting.
- **Legacy access review attests group membership not table-level modification** — already part of Finding-001.

> ### 🚨 Findings-003 through -005 — Legacy CTMS, LIMS, EDC failures (Fields 1, 6, 12 fail)

> ### ⚠ Framework Under-Reporting #1 — Late-Effective-Date filter discoverability (§10.18 Nit; no Kognitos field)

---

## 📦 4:30 PM — The Seven-Artifact Evidence Pack

Henrik walked them through the inspection-day evidence pack. Seven artifacts the FDA inspector would receive on arrival:

1. **The chain-coverage map** with `coverage_map_version`, `effective_utc`, `coverage_map_sha256`, and the most recent `chain.coverage_map_published` chain event.
2. **The deployment-intent enum documentation** — `production`, `validation`, `regulatory_sandbox` — with the most recent intent-change chain events.
3. **The reference-verifier package** with implementation, version, verification-key three-name CC8.1 citation (§10.26).
4. **The HSM partition-ceremony attestation chain entry** (§10.17) with `entity_affiliation` and the institutional CloudHSM IQ/OQ document.
5. **The pre-MAC redaction policy** (§10.22) with the most recent policy-version chain event and the `audit.redaction.disposition` mapping table.
6. **The §10.13 evidentiary-artifacts retention table** with cross-reference to FRE 901(b)(9) authentication-of-the-process foundation.
7. **The §1.2 epistemic-scope clause** verbatim, plus the April 15 patient finding written as a process-design CAPA citing §1.2 (c).

Dawn looked at the pack.

The Kognitos framework had no concept of evidence pack. The 12 rows of the framework do not bind to specific inspection-day artifacts; the framework records what should be captured in each row, not what artifacts an inspector should receive.

She wrote: *◇ Inspection-day evidence pack. Seven artifacts. Kognitos has no concept of inspection-day evidence pack. The bank's reference spec produces a deterministic seven-artifact pack from the §-numbered controls; our framework cannot.*

> ### ◇ Framework-Silent Observation #5 — Inspection-day evidence pack discipline

---

## 🌆 5:30 PM — Auditor Debrief

The team gathered. Mona stepped out.

Dawn wrote on the whiteboard.

```
KOGNITOS 12-FIELD ASSESSMENT — HELMSTAD BIOSCIENCES (BIMO PRE-INSPECTION)

GREEN ZONE — NSCLC ELIGIBILITY CLASSIFIER (4 months live):
  Confirmations:                  12 (all fields)
  Partials:                        0
  Findings against bank:           0
  Framework-silent observations:  5  (algorithm agility, pre-MAC redaction
                                     disposition, clinical deployment-intent,
                                     witness mode, evidence pack discipline)

RED ZONE — LEGACY CLINICAL-OPS & EDC/CRO/LIMS:
  Findings against bank:           5  (legacy DBA UPDATE; CRO retention;
                                       CTMS Visit Summary; LIMS DBA UPDATE;
                                       CTMS overwrite)
  Partials against bank:           2  (EDC streaming-readiness; access review)

CROSS-ZONE:
  Process-design CAPA (NOT chain-finding): 1  (April 15 patient — chain-integrity
                                               clean, source-data wrong)
  Framework Inarticulability:           1  (cross-event upstream-source-data
                                            lifecycle finding shape — Kognitos
                                            has no row for this finding kind)
  Framework Under-Reporting:            1  (§10.18 runbook Nit; no field)
  Framework Gap (recurring):            1  (coverage-boundary primitive)

Reconciliation test (5 random eligibility decisions):
  5/5 inference PASS
  2/5 backward clean; 1/5 corrected-source discrepancy; 2/5 CRO-retention blocked
  5/5 forward PASS
```

Underneath, she wrote:

```
ENGAGEMENT-TEAM OBSERVATIONS ON FRAMEWORK SELECTION:

1. The April 15 patient finding is the most consequential discovery of the engagement
   and is invisible to our framework. The chain captured the model's decision
   correctly; the upstream source data was wrong; the correction did not back-feed.
   No Kognitos field fails. The bank's reference spec records this under §1.2 (c)
   as a process-design CAPA cleanly. Under our framework, the finding can only be
   recorded in cover-memo prose.

2. This introduces a third framework-side issue category: FRAMEWORK INARTICULABILITY.
     - Speculation (Chapters 01-03): auditor invents anchors to fill silences.
     - Under-reporting (Chapter 04): framework misses findings reference spec catches.
     - Inarticulability (Chapter 05): finding exists, reference spec has language
                                      for it, framework has no row that could file it.

3. Witness mode is the second major engagement-relevant gap. The FDA inspector
   arriving in six weeks will run the verifier on a laptop they bring, with no IKM
   access. The bank's reference spec gives them an explicit verdict
   (PASS-STRUCTURALLY) honest about what was verified. Under our framework alone,
   no equivalent verdict; an inspector reading our framework would either need IKM
   access or would have to trust institutional verifier output.

4. The seven-artifact inspection-day evidence pack is produced deterministically
   from the bank's spec sections. Our framework has no equivalent — auditors and
   institutions invent the inspection-day artifact set per engagement.

5. The CRO source-data retention finding (2/5 backward reconciliation blocked) is
   filed against Field 6 with the bank's §10.21 cross-vendor model-handover clause
   as the remediation pattern. The remediation path is sound under both frameworks;
   the discipline language for the clause is in the reference spec.
```

She turned around.

Henrik came back into the room. Mona was with him. The Clinical Quality Director who had walked them through the April 15 patient.

Mona read the whiteboard.

"You filed the April 15 patient as a process-design CAPA citing §1.2 (c) from our reference spec. Even though you operate under the other framework."

Dawn nodded. "We had no Kognitos row to file it against. Every field passes for that entry. The chain did its job. The finding is real — it's a process-design issue about source-data lifecycle. We borrowed §1.2 (c) language because your reference spec has it and our framework doesn't. The cover memo explicitly notes that no Kognitos field fails and that the finding is detectable only because you ran the cross-event reconciliation."

Mona almost smiled.

"Six weeks ago I would have said the framework you brought was good enough for a clinical-trial readiness audit. I would have been wrong. The April 15 patient is the kind of finding that surfaces in a clinical-trial context — chain works, source-data is wrong, downstream patient impact follows. If we had been operating under your framework only, we would have caught the M0-to-M1 correction internally via our weekly QC review — but the audit deliverable would have shown zero findings. The FDA inspector would have read a report that said the chain works, the model performed correctly, the patient was enrolled per the chain. And the inspector would have asked us why we didn't catch the correction. We would have looked unprepared."

She paused.

"With your cover-memo note citing §1.2 (c) and the process-design CAPA framing, the inspector reads a report that names exactly what's going on. The chain did its job. The process didn't. Two different findings. Two different remediations. The framework you carry has no row for that. The reference spec we operate under has §1.2 (c)."

Dawn nodded.

"That's why we wrote it this way."

Henrik: "When the inspector arrives in six weeks, the cover memo travels with the report. The §1.2 (c) framing is what they'll read first."

Tom finished writing.

He had one question for Dawn.

"Inarticulability. That's a new category. We're going to want a definition we can reuse in the program-level write-up."

Dawn took her time.

"A finding is inarticulable when (a) the finding is real and operationally consequential, (b) the bank's reference spec has explicit language for it, and (c) the framework has no field that could be used to file it under any reasonable reading. Inarticulability differs from speculation in that no creative re-reading of any Kognitos field surfaces the finding. It differs from under-reporting in that the finding doesn't fail any field — the chain does exactly what it's supposed to do; the issue is at a layer the framework doesn't address."

"And the April 15 patient is the example."

"And the April 15 patient is the example."

Tom wrote.

Henrik picked up the draft.

"Six weeks. We have six weeks. Your cover memo gives us the framing. The seven-artifact pack is in good shape. The CRO retention finding is in the next contract renewal. The legacy clinical-ops findings are funded for Phase 2. We're going into the inspection with documentation."

He turned to leave.

He paused.

"One more thing. Dr. Acharya wants the framework you brought named in the cover memo. Not anonymized. The framework was inadequate to articulate the most consequential finding of this engagement, and we want that in the record. Under our reference spec, we caught the finding; under your framework, we would have shipped a clean report and the inspector would have asked us hard questions about why we didn't see it. The framework's silence almost cost us the inspection. We want that documented."

Dawn nodded.

"On the record."

---

## ❌ What They Expected vs ✅ What They Found

**❌ What They Expected:**

- The eligibility classifier would pass the 12 fields cleanly.
- The legacy systems would produce some Findings.
- The framework would have language for the chain-integrity-versus-process-design distinction.

**✅ What They Found:**

- AI side cleared all 12 fields with 5 framework-silent depth observations.
- Legacy side produced 5 Findings + 2 Partials (familiar pattern).
- **The framework had no language for the April 15 patient finding** — a real, operationally consequential, source-data-lifecycle issue that does not fail any Kognitos field but does require a CAPA.

**⚠ What Their Framework Could Not Record:**

- The April 15 patient (chain-integrity-clean / source-data-wrong) — new "inarticulability" category.
- Witness mode for FDA inspector verification (recurring shape, new instance).
- Seven-artifact inspection-day evidence pack.
- §1.2 (c) epistemic-scope distinction.
- Algorithm agility (`payload_hash_alt`).
- Pre-MAC redaction disposition (`audit.redaction.disposition="redacted_at_sdk"`).
- Clinical deployment-intent enum (`validation`, `regulatory_sandbox`).
- Quantum-readiness commitment (§4.3.2).

---

## 🧾 Final Assessment Theme

> "The organization satisfies all twelve fields of the Kognitos framework on the AI-side scope, with material integrity gaps on the legacy clinical-ops side. The most consequential finding of the engagement — the April 15 patient enrolled on a staging that was corrected post-enrollment — does not fail any Kognitos field and is invisible to the framework. The bank's reference spec records the finding cleanly under §1.2 (c) as a process-design CAPA distinct from chain-integrity. Under the framework alone, an institution operating without the internal discipline to catch this finding via cross-event reconciliation would ship a clean audit report and surprise the FDA inspector. **The framework was inadequate to articulate the most consequential finding of this engagement.** The institution's Chief Compliance Officer and Clinical Quality Director jointly requested on-the-record attribution of this observation in the cover memo."

---

## Research takeaway

Chapter 05 introduces **framework inarticulability** as the third category of framework-side issue:

| Category | Definition | Earliest chapter |
|---|---|---|
| **Speculation** | Auditor invents anchors to fill framework silences | Ch01 |
| **Under-reporting** | Framework misses findings reference spec catches | Ch04 |
| **Inarticulability** | Finding exists; reference spec has language; framework has no row that could file it under any reasonable reading | Ch05 |

The April 15 patient is the canonical example: chain-integrity perfect, every Kognitos field satisfied, but a real operationally-consequential finding the bank's reference spec records under §1.2 (c) as a process-design CAPA. The framework has no row for the finding kind.

**Inarticulability is the most consequential of the three categories** because no creative re-reading of any Kognitos field will produce the finding. The auditor cannot speculate their way to it. The framework cannot under-report it because the finding isn't a field failure — it's an architectural-layer issue the framework doesn't address.

Running tally across five chapters:
- 43 speculation anchors
- 2 under-reportings
- **1 inarticulability** (new category)

The inarticulability count will likely grow at engagements with rich cross-event scenarios: clinical trials with post-enrollment corrections, financial-services with after-the-fact data reclassification, manufacturing with quality-correction propagation, regulatory submissions with source-document-corrected scenarios. Each such scenario is structurally similar to the April 15 patient: the chain works; the source-data lifecycle is the issue; no field fails.

The institution's joint request for on-the-record attribution (Helmstad's CCO + Clinical Quality Director) is the second such request in the program, after Atrio's Veronika in Chapter 04. The pattern is stakeholders explicitly asking auditors to document the framework's limits.
