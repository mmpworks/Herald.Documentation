# 07 — Olmstead University (Kognitos-lens)

*A multi-regulator higher-ed audit where a civil-rights threat letter motivated the chain deployment eleven months ago, two override-down decisions surface with the free-text rationale gone in Slate, and the framework's silences on coverage-boundary primitives become the litigation-defense exposure*

**Engagement:** Multi-framework higher-ed audit-readiness — DOE FERPA (with active OCR complaint) + FTC GLBA Safeguards + NIH research-integrity + HHS OCR informal advisory at the affiliated medical center + civil-rights litigation-defense addendum
**Client:** Olmstead University — large research university post-threat-letter; chain deployed under consent-to-resolve framework with a civil-rights firm
**Status:** AI-only chain instrumentation (eleven months live, ~840K screening inferences); everything else legacy (Banner SIS, Slate admissions, IRB SQL, Salesforce advancement, faculty-led research labs, affiliated medical center)
**Audit team lead:** Dawn
**Client liaisons:** Holland Berge, General Counsel; Inez Tilakaratne, Model Risk Management Chair; Wren Sumiyoshi, Privacy Officer / DPO; Cassius Okonkwo, Chief AI/ML Officer

**Audit team's framework:** Kognitos's 12-field schema. The team is now seven engagements in. This chapter introduces two new lens-stretching scenarios: (1) **a coverage-boundary gap that maps onto an active civil-rights threat letter** — the chain captures the structured override decision (reason code, reviewer ID, timestamp) but the human reviewer's free-text rationale prose lives one webhook away in Slate, where two of five sampled override-down cases have gone missing — both on applicants whose AI score would have admitted them; and (2) **a five-regulator partitioning problem** — the same audit produces five different regulator-shaped deliverables (FERPA, GLBA, NIH, HIPAA-informal, civil-rights addendum) and the framework has no primitive for partitioning the chain's claims by audience.

---

## 🌅 8:30 AM — Kickoff (Post-Threat-Letter Context)

Holland Berge — the General Counsel — opened with a printed §10.19 chain-coverage map. Eleven months ago, the university had received a civil-rights firm's threat letter naming a specific class of admissions decisions: override-down on applicants whose AI screening score would have admitted them. The chain deployment was the consent-to-resolve framework's principal defense.

"Three things on the table today," Holland said. "First, the AI-side chain that we deployed under consent-to-resolve — does it do what we said it does. Second, the gap I already know exists — the override-rationale free-text in Slate. Third, the partitioning. We have five regulator audiences. FERPA at OCR-Education. GLBA via FTC. NIH research-integrity. HHS OCR has an informal advisory on the medical center side. And the civil-rights firm has a litigation-defense addendum the rest of the universe doesn't see."

Dawn looked at the map. Four categories — chain-instrumented (admissions-AI screening), not-yet-instrumented (Banner SIS, IRB SQL, Salesforce advancement, faculty research labs), third-party-with-inspection (Slate admissions ledger), external-evidentiary (medical-center paper records, OMS-style work tickets).

"Under our framework — Kognitos's 12 fields — coverage-boundary is not a primitive. We can document boundaries in cover-memo prose. The reference spec your consent-to-resolve framework was anchored on does carry a §10.19 coverage-map primitive. We borrowed it at Mercator, Stelvio, Atrio, and Pacific Crescent. We will borrow it again here."

Holland nodded slowly.

"The threat letter names two override-down decisions specifically. If your reconciliation surfaces a rationale gap on either of those decisions — or any decision where the AI score would have admitted — the civil-rights firm will see it before the academic year is over. The chain has to support a defense the General Counsel can defend in deposition. The cover memo cannot carry the weight that the chain entries should carry."

Dawn wrote that down. *Coverage gap maps onto active threat-letter class. Reconciliation sample design needs to anchor on AI-would-admit / override-down combinations specifically. Note for the chapter.*

"Inez will walk you through MRM after the kickoff. Cassius will sit in for the ML lifecycle. Wren is here for FERPA. The civil-rights firm investigator is not in the room but will read the deliverable through Holland's filter."

---

## 🧬 9:30 AM — Admissions-AI Verifier (Field Walk)

The admissions-AI screening service ran an ensemble model fed by transcript features, recommendation-letter NLP scores, application essays (NLP), and standardized-test indicators (where present). Each inference produced a screening score from 0 to 100. Decisions of 75 and above were "AI-recommend-admit"; 70-74 was "review"; below 70 was "AI-recommend-deny." Human reviewers could override in either direction.

Mike pulled a January 9 override — a score of 71 boosted to 78 with reason code `STRENGTH_OF_RECOMMENDATIONS`. The reviewer was logged. The override decision was a chain entry with parent_run_id linkage to the original screening inference.

```json
{
  "entry_id": "olm-admit-2026-01-09-7341428",
  "tenant": "olmstead-undergraduate-admissions",
  "service": "admissions-ai-screening",
  "seq": 7341428,
  "ts": "2026-01-09T15:22:41.207Z",
  "model_id": "olm/admit-screen-v4.2",
  "model_version": "v4.2.3-quarterly-2025q4",
  "gen_ai.request.model": "olm/admit-screen-v4.2",
  "gen_ai.response.model": "olm/admit-screen-v4.2",
  "prompt": {
    "feature_vector_hash": "sha256:...",
    "feature_categories": [
      "transcript", "recommendations", "essays", "test_indicators"
    ],
    "protected_class_proxy_flags": []
  },
  "response": {
    "score": 71,
    "recommendation": "review"
  },
  "override": {
    "parent_run_id": "olm-admit-2026-01-09-7341428",
    "new_score": 78,
    "reason_code": "STRENGTH_OF_RECOMMENDATIONS",
    "reviewer_id": "olm-admissions-reviewer-0114",
    "ts": "2026-01-09T16:08:33.491Z"
  },
  "audit.deployment.intent": "production",
  "audit.deployment.policy_version": "olm-admit-2025q4-consent",
  "audit.redaction.disposition": "redacted_at_sdk",
  "payload_hash": "...",
  "hmac": "...",
  "merkle_path": [...],
  "daily_seal_ref": "2026-01-09-d-seal-olm-admit"
}
```

The verifier ran in five seconds against the override entry.

```
$ herald-verify --tenant=olmstead-undergraduate-admissions \
                --service=admissions-ai-screening \
                --date=2026-01-09 \
                --entry-id=olm-admit-2026-01-09-7341428 \
                --strict
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified
        against public key olm-admit-prod-2025-q4
Elapsed: 5.2s
```

All twelve Kognitos fields satisfied. Field 11 (human review) carried depth — the override decision was chain-bound to the same parent_run_id as the original screening inference, with reviewer_id and reason_code stamped.

Mike paused on `protected_class_proxy_flags`. The array was empty for this entry. He noted: ◇ the chain emits per-entry attribution that downstream auditors can use to test the feature set against protected-class-proxy concerns. Under our framework, no field for proxy-flag discipline. *Note: §4.4.5 underwriting-features-by-analogy is the reference-spec anchor. Borrowing applies.*

> ### ✓ Confirmation #1 — All 12 fields satisfied on admissions-AI override entry (Field 11 chain-bound to parent screening)

A second test: Mike pointed the verifier at a February 2025 pre-chain decision — a record from before the chain went live. The verifier returned a structural error.

```
Status: STRUCTURAL ERROR
Step:   1
Reason: entry pre-dates chain genesis event 2025-03-15T00:00:00Z;
        no parent linkage possible; refused at structural-validation step
Elapsed: 0.4s
```

> ### ✓ Confirmation #2 — Chain refuses pre-chain retroactive entries; framework integrity preserved (Field 12)

Then witness-mode — no master-key supplied. The verifier returned `PASS-STRUCTURALLY` on a sampled override, useful for the federal-litigation-discovery posture where the civil-rights firm's expert witness would verify the chain without institutional credentials.

> ### ✓ Confirmation #3 — Witness-mode PASS-STRUCTURALLY for litigation discovery (recurring Ch05)

---

## 🚨 10:30 AM — Reconciliation Sample (Two Rationales Gone)

The team designed the reconciliation sample to anchor on the threat-letter class. Five admissions decisions chosen at random from the override-down population specifically — applicants whose AI score would have admitted them but who were overridden to deny.

Chen ran the verifier across all five.

```
Sample 1 (2025-11-04, score 79 → reject):
  AI side:        PASS
  Reviewer side:  reviewer-0042 + reason_code "INCOMPLETE_APPLICATION"
  Rationale text: present in Slate (47-word entry)

Sample 2 (2025-12-18, score 76 → reject):
  AI side:        PASS
  Reviewer side:  reviewer-0117 + reason_code "STRENGTH_OF_RECOMMENDATIONS"
  Rationale text: present in Slate (62-word entry)

Sample 3 (2026-01-22, score 81 → reject):
  AI side:        PASS
  Reviewer side:  reviewer-0089 + reason_code "FIT_AND_CULTURE"
  Rationale text: present in Slate (35-word entry)

Sample 4 (2025-10-14, score 77 → reject):
  AI side:        PASS
  Reviewer side:  reviewer-0203 + reason_code "FIT_AND_CULTURE"
  Rationale text: NOT PRESENT in Slate; field-history shows
                  rationale field edited 2025-11-02, prior content not
                  retained per Slate default retention

Sample 5 (2026-02-08, score 80 → reject):
  AI side:        PASS
  Reviewer side:  reviewer-0114 + reason_code "STRENGTH_OF_RECOMMENDATIONS"
  Rationale text: NOT PRESENT in Slate; field-history disabled on this
                  account; no record of edit timing
```

Five for five on the AI side. Five for five on the structured override capture (reviewer_id + reason_code, chain-bound). Three for five on the free-text rationale.

Two for five missing — both override-down on AI-would-have-admitted applicants. Exactly the suspect class the threat letter named.

Dawn looked at Chen. Then at Holland, who had come back into the room.

"The chain has what we said it has. The structured override is captured. The reason code is captured. The reviewer ID is captured. The free-text rationale is not on the chain. It is in Slate, where the reviewer enters it, and Slate's default retention is not configured to preserve field-history for the rationale field on the schedule we need."

Holland: "How does our framework articulate this?"

"Under our framework — Field 11 (human review) is satisfied on all five samples. Reviewer ID, reason code, decision, timestamp — all present. The framework does not articulate the free-text rationale field. Under the reference spec, the §10.19 coverage map names the rationale field explicitly as an external-evidentiary boundary, and §4.4.6 is the structural form to close the gap via a Slate webhook with `audit.connector_source.*` attribution and stable-`run_id` discipline tied to the Slate applicant record ID. Phase 2 of your consent-to-resolve closes it on a 12-month plan. The reference spec carries the discipline. Our framework does not."

Holland's posture shifted.

"Tell me what I write to the General Counsel reading on Friday."

"Three sentences. First — the chain captures the structured override decision and reason code per the consent-to-resolve framework, and the AI-side verification is independent and reproducible. Second — the free-text rationale field is an external-evidentiary boundary identified per §10.19 coverage-map discipline; two of five sampled override-down decisions had this field unrecoverable from Slate. Third — Phase 2 closes the gap via §4.4.6 webhook capture; the litigation defense for the affected decisions relies on the reviewer's deposition reading of the structured reason code, not on the prose rationale at the moment of decision."

Holland wrote that down. He looked at it for a long moment.

> ### 🚨 Framework Under-Reporting #3 — Free-text rationale gap on 2/5 override-down samples (both on AI-would-admit applicants)
>
> The chain captures the structured override (reason code + reviewer + timestamp). Field 11 (human review) is satisfied. The free-text rationale prose lives in Slate, mutable, with selective field-history retention. Under FFIEC §10.19, this is a Gap in the chain-coverage map; under §4.4.6, the structural form to close it is the Slate webhook with stable-`run_id`. Under Kognitos, Field 11 records the review event with disposition; the framework has no row for the rationale-prose location or its retention discipline. **The two gone-rationale cases are the threat letter's suspect class verbatim.**

> ### ◇ Framework-Silent Observation #1 — Reconciliation-sample design anchored on suspect-class population
>
> The reference spec implicitly supports this via §10.18 runbook discipline (sample design is per-engagement). Under Kognitos, sample-design intent has no framework anchor; the auditor designs the sample by engagement judgment.

---

## 🛡️ 11:30 AM — §1.2 Epistemic-Scope Walk for Litigation Defense

Holland came back with a yellow legal pad.

"Walk me through the §1.2 distinctions for the two gone-rationale cases. The civil-rights firm will ask the General Counsel five forensic questions in deposition. I need to know which questions the chain answers and which the chain does not."

Cassius — the Chief AI/ML Officer — took the §1.2 walk.

"§1.2 (a) — the chain proves what the screening system said. For sample 4, the AI score was 77 with feature_vector_hash bound to the chain. For sample 5, the AI score was 80 with feature_vector_hash bound. Mathematically defensible. We produce a witness for either."

"§1.2 (b)?"

"The record was not tampered after capture. HMAC plus Merkle plus Ed25519 plus §10.5 HSM custody plus §1.4 compositional security across the three layers."

"§1.2 (c)?"

"The chain does not prove the application's underlying data was authentic. We screen transcripts, recommendations, essays, and test indicators. The chain captures the AI's view of those inputs; it does not authenticate the upstream source. Under FERPA the institution does authenticate at the registrar layer; the chain is downstream."

"§1.2 (d)?"

"The chain does not prove the screening was the right screening. The model's accuracy and disparate-impact posture are separate audits — those live under §4.4.5 underwriting-features-by-analogy plus the quarterly fairness-audit vendor's §10.21 contract-triple binding. The chain captures what the model said, not whether what the model said was correct."

"§1.2 (e)?"

"The chain does not prove the override decision was the right decision. It captures the reason code — `FIT_AND_CULTURE` in both gone-rationale cases — and the reviewer ID. The chain does not adjudicate the reasoning. The free-text rationale was the reviewer's space to articulate that reasoning. In samples 4 and 5, the chain captures `FIT_AND_CULTURE` as the reason; the prose that elaborated it is gone."

Holland: "That last sentence is the litigation exposure. The civil-rights firm will read `FIT_AND_CULTURE` as a controlled-vocabulary reason code that maps to a category. Under ECOA-by-analogy via §10.11.1, that reason code is structurally bound under per-event MAC. But the prose that distinguishes 'fit' for sample 4 from 'fit' for sample 5 — the reviewer's actual reasoning — is unrecoverable. Two reviewers, two different applicants, same reason code, no rationale prose."

Dawn closed her notes.

She had what she needed for the Friday memo. Five §1.2 subclauses, five forensic-question answers, and the rationale gap framed as the litigation exposure rather than as a defect of the chain.

She wrote: *Under Kognitos, the §1.2 (a)-(e) distinctions are inarticulable. Every field satisfied; the framework cannot supply the litigation-defense one-pager. The Friday memo borrows §1.2 verbatim from the reference spec — same pattern as Pacific Crescent. **Framework Inarticulability #3 (third instance; civil-rights-litigation variant of Ch05's clinical and Ch06's public-safety inarticulabilities).***

> ### ⚠ Framework Inarticulability #3 — §1.2 epistemic-scope distinctions for civil-rights litigation defense
>
> Third instance in the program. Ch05 was clinical-quality CAPA; Ch06 was public-safety Daubert; Ch07 is civil-rights Title VI/VII litigation defense. The same framework gap (no epistemic-scope clause) produces materially different consequences depending on engagement stakes. Under Kognitos, every field satisfied on the AI-side override entries; the framework cannot articulate any of the five §1.2 subclauses for the Friday memo. Litigation-support file borrows §1.2 from the reference spec verbatim.

---

## 🔧 1:00 PM — Legacy Stack Walkthrough (Banner / IRB / IAM)

After lunch, Inez Tilakaratne — the MRM Chair — walked the team through the legacy stack. She was efficient.

"Banner SIS. 90-day audit-log retention. GLBA Safeguards Rule expects longer retention for security-event correlation; we have known about this for fourteen months. The renewal budget covers retention extension to 540 days."

Luis tagged ✗ Field 12 + ✗ Field 1 (Banner retention scope below GLBA expectations).

> ### 🚨 Finding-001 — Banner SIS 90-day audit retention below GLBA Safeguards expectation (Field 12 + Field 1)

"IRB SQL. The institutional review board's protocol database. Update-by-DBA permitted on three IRB administrators; no MFA on the database side; database-side audit log is editable by the same three DBAs. Same shape as iFIX at Pacific Crescent."

Diana: ✗ Field 3 + ✗ Field 12.

> ### 🚨 Finding-002 — IRB SQL DBA UPDATE with mutable audit log (Field 3 + Field 12)

"Four-column IAM. Admissions / Banner / IRB / Salesforce. Each column has its own identity authority. There is no cross-column reconciliation today; an admissions reviewer rotated off in February 2025 still has a row in Banner that nobody closed. We have a remediation ticket from the IT security team that's eleven months old."

Diana: ✗ Field 3.

> ### 🚨 Finding-003 — Four-column IAM with no cross-column reconciliation (Field 3)

"Shared `aid_admin` account in financial aid during peak season. Six staff use one account from October through January. No MFA. Same pattern as the Stelvio Plant_Engineer and the Pacific Crescent dispatch HMI."

Diana: ✗ Field 3.

> ### 🚨 Finding-004 — Shared `aid_admin` peak-season account (Field 3; recurring pattern)

"Paper access reviews. Twice-yearly access certification produces a paper record signed by the column owner. The paper record is the audit artifact. There is no chain entry for the certification event; the §10.2 operational-events discipline would capture this as a chained event but the institution has not implemented the connector."

Chen: ⚠ Partial — Field 3 + Field 11 (paper certification; no chain capture).

> ### ⚠ Partial #1 — Paper-based access certification not chain-captured (Field 3 + Field 11)

By 2 PM the legacy column had four Findings + one Partial.

---

## 🔬 2:30 PM — Research-Computing Tour (Two Lab Visits)

NIH research-integrity expected per-lab discipline. The team toured two labs.

**Lab 1 — Computational Biology.** Principal investigator with mature data-management plan. Chained ELN (electronic lab notebook) entries via vendor-supplied connector emitting `audit.connector_source.*` attribution and contributing to a per-PI chain rolled into the institution's IKM registry. The PI walked through three random ELN entries — verifier returned PASS in 3.8 seconds for each.

> ### ✓ Confirmation #4 — Lab 1 ELN chain integrity (3 random entries; PASS in <4s each)

**Lab 2 — Quantitative Finance.** Principal investigator at an econ-CS joint appointment. ELN was a shared Google Doc with version history disabled selectively; raw data on a lab-managed S3 bucket with no audit-log retention configured. The PI explained that the lab's research output was modeled as "publication artifacts" and the audit trail was the publication record. NIH research-integrity expectations include reproducibility from raw data through analysis; the lab's posture did not meet the expectation.

Chen: ✗ Field 6 + ✗ Field 12 (lab-level retention and source attribution).

> ### 🚨 Finding-005 — Lab 2 quantitative-finance lab does not meet NIH research-integrity expectations (Field 6 + Field 12)

The framework's silence on per-lab discipline produced an interesting structural note. Under Kognitos, the institution either gets a Confirmation across all labs (if a sampled lab passes) or a Finding (if a sampled lab fails). There is no framework-supplied vocabulary for the per-lab variance or for the institution's enforcement posture across the lab population. Under the reference spec, §10.19 chain-coverage map names the lab enumeration explicitly; the institution can document per-lab posture in the map.

> ### ◇ Framework-Silent Observation #2 — Per-lab variance and institution-level enforcement posture
>
> The reference spec supports per-lab enumeration via §10.19. Under Kognitos, lab-population variance has no framework anchor; sampled findings cannot be cleanly attributed to per-lab vs. institution-level enforcement.

---

## 🏥 3:30 PM — Medical-Center Hallway Tour (HIPAA Informal Advisory)

HHS OCR was not auditing today but had requested an informal advisory pass at the affiliated medical center. Wren Sumiyoshi walked the team across the connector to the medical center's HIPAA-protected zone.

The medical center had its own audit-trail infrastructure (legacy, paper-heavy). The chain on the university side had no extension into the medical-center zone. The reference spec supports cross-entity anchoring via `audit.external_artifact.*` attributes — the university chain can hash-anchor medical-center evidentiary artifacts without consuming PHI, via §10.19 chain-coverage map extension.

The team produced two informal observations consistent with prior healthcare audits — selective field-history on EHR access logs (recurring shape from Mercator); 60-day rolling backup retention on the medical-center HIE bridge (below HIPAA-Security expectations).

> ### 🚨 Findings 006-007 — Medical-center informal advisory (selective EHR field-history; 60-day HIE backup retention)

Under Kognitos, the cross-entity-anchor pattern has no field. Field 6 (inputs with source attribution) is generic; the framework does not articulate hash-anchor evidence across affiliated entities.

> ### ◇ Framework-Silent Observation #3 — Cross-entity hash-anchor evidence pattern
>
> Reference spec: §10.19 + §audit.external_artifact.*. Under Kognitos, cross-entity evidentiary linkage has no framework anchor.

---

## 💳 4:00 PM — Salesforce Advancement (FERPA + Donor)

Elena walked the advancement stack. Salesforce held alumni / donor records and student-facing communications (FERPA-protected for current students; relaxed for alumni). Field-history was selectively enabled — donor-facing fields had history; student-facing communication fields had history disabled on accounts older than 24 months.

> ### 🚨 Finding-008 — Salesforce selective field-history; student-facing fields age-disabled at 24 months (Field 12)

> ### ⚠ Partial #2 — Salesforce advancement retention discrepancy between donor and student fields

---

## 🌆 5:00 PM — Auditor Debrief

The team gathered. Dawn wrote on the whiteboard.

```
KOGNITOS 12-FIELD ASSESSMENT — OLMSTEAD UNIVERSITY (POST-THREAT-LETTER)

AI SIDE — ADMISSIONS SCREENING:
  Confirmations:                  4 (override entry; pre-chain refusal;
                                     witness-mode; Lab 1 ELN)
  Partials:                       0
  Findings against bank:          0 on AI side directly
  Framework Under-Reporting:      1 (rationale gap; 2/5 suspect-class samples)
  Framework-silent observations:  3 (suspect-class sample design;
                                     per-lab variance; cross-entity anchor)

LEGACY STACK — BANNER / IRB / IAM:
  Findings against bank:          4  (Banner 90-day; IRB DBA;
                                       four-column IAM; shared aid_admin)
  Partials against bank:          1  (paper access certification)

RESEARCH-COMPUTING:
  Findings against bank:          1  (Lab 2 quant-finance)

MEDICAL-CENTER INFORMAL:
  Findings (advisory):            2  (EHR selective field-history;
                                       HIE backup retention)

ADVANCEMENT — SALESFORCE:
  Findings against bank:          1
  Partials against bank:          1

CROSS-ZONE / FRAMEWORK-SIDE:
  Framework Inarticulability:     1 (§1.2 (a)-(e) for litigation-defense memo;
                                     third instance — civil-rights variant)
  Framework Under-Reporting:      1 (rationale-gap; §10.19 + §4.4.6 invisible)
  Framework Gap (recurring):      1 (coverage-boundary primitive; recurring
                                     across Ch01-06)
```

Underneath, she wrote:

```
ENGAGEMENT-TEAM OBSERVATIONS ON FRAMEWORK SELECTION:

1. The reconciliation sample anchored on the suspect-class population
   (override-down on AI-would-admit). Under our framework, sample-design
   intent has no anchor. The two gone-rationale cases are exactly the
   threat letter's named class. The institution's reference spec gives
   the rationale-gap finding §10.19 + §4.4.6 articulation; our framework
   records Field 11 satisfied across all five samples.

2. The §1.2 (a)-(e) walk for the Friday memo is inarticulable under our
   framework. Same pattern as Pacific Crescent. The reference spec
   carries the five subclauses; the framework supplies none. The Friday
   memo borrows §1.2 from the reference spec verbatim.

3. Five-regulator partitioning of the deliverable is not a Kognitos
   primitive. FERPA, GLBA, NIH, HIPAA-informal, civil-rights addendum —
   the institution will produce five regulator-shaped deliverables and
   the framework offers no partitioning vocabulary. The reference spec
   §10.19 chain-coverage map is the partitioning tool.

4. The §4.4.5 underwriting-features-by-analogy attribution
   (feature_vector_hash, feature_categories, protected_class_proxy_flags)
   is the chain-bound disparate-impact-prevention discipline. Under our
   framework, no field for feature-categorization or proxy-flag posture.

5. ECOA adverse-action-reasons schema bound under MAC (§10.11.1) anchors
   the structured override defense. Under our framework, controlled-
   vocabulary reason-code discipline has no row.
```

She turned around.

Holland came back into the room. He had read the rationale-gap analysis.

"Add this to the cover memo. On the record."

He read from his notes.

"Olmstead's chain captures the structured override decision and reason code per the consent-to-resolve framework with the civil-rights firm; the AI-side verification is independent and reproducible. The free-text rationale field in Slate is an external-evidentiary boundary identified per the reference spec's §10.19 chain-coverage-map discipline; on the engagement-day reconciliation sample, two of five override-down decisions on applicants whose AI score would have admitted had the rationale field unrecoverable. Phase 2 of the consent-to-resolve framework closes this gap via §4.4.6 webhook capture in the next twelve months. Until then, the litigation defense for the affected decisions relies on the reviewer's deposition reading of the structured reason code, not on the prose rationale at the moment of decision."

He paused.

"Tell your firm. The 12-field framework is acceptable as a vendor-facing summary. It is not acceptable as the only assessment artifact for any institution operating under a consent-to-resolve framework with active civil-rights litigation exposure. The framework cannot articulate the rationale-gap finding; it cannot supply the §1.2 litigation-defense memo; it cannot partition the deliverable across five regulator audiences. We've been operating under the reference spec for eleven months because the framework you brought cannot articulate the distinction between the structured override and the prose rationale. Under disparate-impact law, that distinction is the difference between defending the reviewer and not. On the record."

Dawn nodded.

"On the record."

---

## 🧾 Final Assessment Theme

> "The admissions-AI chain passes 12 Kognitos fields across four reconciliation Confirmations including the override entry, pre-chain refusal, witness-mode for federal litigation discovery, and Lab 1 ELN integrity. The reconciliation sample anchored on the threat-letter's suspect class produces two gone-rationale cases on AI-would-admit applicants — the chain captures the structured override; the prose rationale is gone in Slate. Under our framework, Field 11 (human review) is satisfied on all five samples; under the reference spec, this is a §10.19 chain-coverage-map Gap closed by §4.4.6 Phase 2 webhook capture. The §1.2 (a)-(e) epistemic-scope distinctions the General Counsel needs for the Friday memo are inarticulable under the framework — third inarticulability instance in the program. Five-regulator partitioning of the deliverable (FERPA / GLBA / NIH / HIPAA-informal / civil-rights addendum) requires the §10.19 chain-coverage map as the partitioning tool; our framework offers no equivalent. The General Counsel requested on-the-record attribution of the framework's inadequacy for any institution under consent-to-resolve framework with active civil-rights litigation exposure."

---

## Research takeaway

Chapter 07 produces the third inarticulability instance — civil-rights-litigation variant of the §1.2 epistemic-scope distinction that drove Ch05 (clinical-quality CAPA) and Ch06 (public-safety Daubert). The progression is consolidating into a regularity: at every engagement where stakes scale beyond compliance-confirmation, the §1.2 distinctions become the load-bearing litigation defense and the framework cannot supply them.

Chapter 07 also produces the third framework under-reporting — the free-text rationale gap on 2/5 sampled override-down decisions, both on AI-would-admit applicants exactly matching the threat letter's named class. The reference spec catches this via §10.19 chain-coverage-map discipline; the framework's Field 11 records "human review" as satisfied because the structured override decision IS captured; the gap between structured-capture and prose-capture is invisible.

The chapter also introduces three new operational properties the framework cannot articulate: (1) reconciliation-sample design intent anchored on a regulator-named suspect class; (2) per-lab variance and institution-level enforcement posture across a research-computing population; (3) cross-entity hash-anchor evidence patterns linking an affiliated medical center to the university's chain via `audit.external_artifact.*` without consuming PHI.

---

*Running counts and program-level signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
