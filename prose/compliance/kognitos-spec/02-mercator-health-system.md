# 02 — Mercator Health System (Kognitos-lens)

*A bifurcated audit under a framework that has no row for the boundary*

**Engagement:** HITRUST CSF v11 + HIPAA Security Rule + FDA SaMD Post-Market Combined Assessment
**Client:** Mercator Health System (top-20 US integrated health system — academic medical center, regional health-insurance carrier, multi-state physician group)
**Status:** AI audit-trail capture live for 90 days on one inference path (the FDA-cleared sepsis-prediction CDS in three ICUs); everything else is legacy
**Audit team lead:** Dawn
**Client liaison:** Dr. Patricia Okonkwo, system-wide CISO

**Audit team's framework:** Kognitos's 12-field AI audit-trail schema. The 12-row template is the only normative document in the room. No FFIEC v1.0b. No §10.19 chain-coverage map. No §1.2 epistemic-scope clause. No §10.13 evidentiary-artifacts retention list. The team carries the same printed template they brought to Northbridge Bank two weeks ago.

**Posture going in:** Patricia is asking the audit team to find and name the gaps so she can fund the remediation. The team's framework can do that — Kognitos has rows that fail when a system has no tamper-evidence, no authenticated user attribution, no model-version capture. What the team will discover is that the framework gives them clean language for the *failures* in the unchained zone, and almost no language for the *boundary* between the chained and unchained zones.

---

## 🌅 8:30 AM — Kickoff (and the Framework Meets Bifurcation)

Patricia's printed handout was a one-page system map with two colored zones. Green on the left: "AI audit-trail scope (sepsis-cds)." Red on the right: "Legacy scope (everything else)." No marketing language. Just a map of what was covered and what wasn't.

Dawn looked at it for a long moment.

The Kognitos 12-field template in her bag had no row for "coverage map." It assumed audit-trail capture was a single property — either the AI events were captured to the framework's depth or they weren't. The framework had no language for "captured for *this* set of decisions, not captured for *that* set," and the map Patricia had handed her was exactly that distinction made concrete.

She turned the map over and wrote, on the back: *Field coverage scope: sepsis-cds only. Legacy zone is everywhere Kognitos can't reach.*

Patricia did not pause for marketing. "I want you to find and name the gaps. The AI side has been live for 90 days. The legacy side has been live for 30 years. I want both assessed against whatever framework you brought. Whatever shape the report takes, I need it concrete enough to take to the board and ask for the budget to extend coverage."

Dawn put her coffee down. "Thank you for saying it out loud. It saves us a day."

She had a follow-up. The same Daubert question she had asked at Northbridge, because she wanted to see whether Mercator had the same shape of answer.

"The plaintiff bar is interested in sepsis. If a model-driven clinical error lands in court, what does your expert witness lay foundation on?"

Patricia did not pause. "Section 1.2 of our spec is on the wall above my desk. The chain proves what the model said at a specific time and that the record was not tampered after capture. Two things. The chain does NOT prove the model's clinical statement was accurate, that it complied with our AI Governance Committee policy, or that it was free of bias. We name the line clearly so the plaintiff's expert cannot drag our witness onto the truth foundation under cross-examination."

Dawn wrote that down. The wording was new to her — Patricia was citing a section number from a different spec, the same way Marcus had at Northbridge. Under the Kognitos framework, there was no comparable epistemic-scope clause. The framework asked what the audit trail should *contain*. It did not address what the audit trail *proves*. An institution operating under Kognitos would have to author its own epistemic-scope discipline; Mercator had borrowed one.

She made the kind of note auditors make when the framework is silent on a thing the institution has chosen to do well anyway: *◇ Mercator borrowed §1.2 epistemic-scope from the same spec we don't carry. The Kognitos framework has no row for it. The institution did the work the framework didn't ask for.*

"You said FFIEC v1.0b," she said.

"Yes. The reference spec for the chain substrate. The 12-field framework you're carrying is different — yours is the audit-trail-row schema; theirs is the integrity-substrate spec. They sit in different layers. The audit team I expected to walk in this morning would be carrying the audit-trail framework. That's you. We picked v1.0b for the substrate because the FDA reviewer has been working from a Cosign-signed reference verifier all year, and the public spec is what gives him something to verify against. Different problem, different artifact."

Tom — the visiting-team's internal-audit liaison — had already been on a call with Mercator's Chief Audit Executive the day before. "We agreed yesterday on the bifurcation framing. Two reports stapled together. The CAE is supportive."

"Two reports stapled together," Patricia repeated. "Yes. That is exactly right."

Dawn looked around the table. "Mornings is the AI side. Afternoons is the legacy side. We reconvene at three for a reconciliation test. Five-thirty debrief."

She added, mostly to herself but loud enough for Tom to hear:

"Tom — note in the cover memo. The framework we're operating under has no concept of coverage scope. We're going to write a bifurcated assessment by stapling two complete framework runs side by side. The boundary between them is going to be a thing we describe in prose, not something the framework can express."

Tom wrote.

He underlined "no concept of coverage scope."

---

## 🧩 9:15 AM — The AI Side (Sepsis CDS) — Fields Walk Cleanly

Mike and Chen went to the engineering floor. The lead clinical informaticist, Dr. Wei, was waiting with a laptop and no deck.

"You want to see a sealed inference," she said. "Pick a date. Pick a hospital."

Mike picked April 12. Memorial campus.

Dr. Wei pulled up `sep-2026-04-12-mem-00194` — a 67-year-old admitted overnight with pneumonia, model called at 09:42:11, sepsis probability 0.87, attending agreed with the prediction. The entry showed lab values, vitals, prompt, response, tool calls, and `clinician_override: null`.

Mike worked through his template.

- **Field 1 (Timestamp).** `ts: 2026-04-12T09:42:11.483Z`. RFC 3339 millisecond UTC. ✓
- **Field 2 (Decision ID).** `entry_id: sep-2026-04-12-mem-00194`. Unique per inference. ✓
- **Field 3 (Authenticated human identity).** The attending's clinician ID is captured on the override entry (when there is one); on this entry, override was null, so the field maps to the patient-record-access trail. The patient-context fetch carries an authenticated clinician identity. ✓
- **Field 4 (AI system identity and version).** `model_id: mercator/sepsis-pred-v3.2`, `model_version: v3.2.1-fda-cleared-2025-11`. ✓
- **Field 5 (Model identity and version).** Same fields, plus `gen_ai.request.model` and `gen_ai.response.model` both populated and equal. ✓
- **Field 6 (Inputs with source attribution).** Lab values (six values, each with source-lab-record-ID), vitals (four values, each with source-monitor-event-ID), patient context hash. ✓
- **Field 7 (Specific policy or prompt invoked).** Prompt content is in the entry; the policy version is in `audit.deployment.policy_version: mercator-mrm-2026q1`. ✓
- **Field 8 (Reasoning in human-readable language).** Feature attributions in the response payload. The model's reasoning — which inputs drove the prediction — is captured in structured form. Plain-language rendering is generated for the clinician via a separate inference and is itself captured as a chained entry. ✓
- **Field 9 (Output produced).** `sepsis_probability: 0.87, confidence: 0.92`, plus the feature_attributions vector. Verbatim. ✓
- **Field 10 (Action taken in downstream systems).** Linked to the clinician's downstream sepsis-bundle order via a `parent_run_id` reference on the bundle order entry. ✓
- **Field 11 (Human review).** Clinician override on this entry was null (attending agreed). A 30% override rate on the population. Override entries are themselves chain entries with clinician ID, override timestamp, override reason from a structured pick-list, and a signature linking back. ✓
- **Field 12 (Tamper-evident integrity proof).** HMAC-chained per entry, daily Merkle seal, Ed25519 signature, CloudHSM in `us-east-1` under FIPS 140-2 Level 3. ✓

All twelve fields satisfied on a single inference entry.

Mike asked Dr. Wei to run the verifier in front of him.

```
$ herald-verify --tenant=mercator-memorial \
                --service=sepsis-cds \
                --date=2026-04-12 \
                --entry-id=sep-2026-04-12-mem-00194 \
                --strict

Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified
        against public key sepsis-prod-2026-q2
```

> ### ✓ Confirmation #1 — All 12 fields satisfied on sepsis-CDS inference entry
>
> Every Kognitos field has clean evidence on the sepsis-CDS chain. Verifier returns PASS in under 1 second. No Mercator credentials required beyond read scope. Field 1-12 all satisfied.

Mike asked Dr. Wei to run the verifier on the day Mercator rotated the signing key — November 2025, model-retraining day. PASS. The verifier handled key rotation transparently.

Same framework-silent observation Dawn had recorded at Northbridge. Kognitos doesn't ask whether Field 12 handles key rotation. Mercator handles it. Another ◇.

Mike asked about deployment-intent rollout. Dr. Wei pulled up February 2026: the team had attempted a v3.2.0 rollout, observed elevated false-positive rate within 36 hours, and rolled back to v3.1.7. The canary attempt was a sealed chain entry per the OpenTelemetry GenAI envelope's `audit.deployment.intent: canary` attribute. The rollback decision was a chained policy event.

Mike wrote in his Field 4 margin: *Deployment-intent capture — `audit.deployment.intent: production | canary | ab_test`. The bank carries the rollback as a sealed canary chain entry. Kognitos has no field for deployment intent. An institution silently flipping a production model with no audit-trail of the deployment posture would satisfy Field 4 (system identity) identically. The bank's discipline is invisible to the framework.* ◇.

> ### ◇ Framework-Silent Observation #1 — Deployment-intent capture
>
> The bank captures `audit.deployment.intent` (production / canary / ab_test) on every model call. The February 2026 v3.2.0→v3.1.7 rollback was a sealed canary chain entry. Kognitos has no field for deployment intent. An institution silently flipping a production model with no audit-trail of the deployment posture satisfies the framework identically.

> ### ◇ Framework-Silent Observation #2 — OpenTelemetry GenAI naming discipline
>
> The bank uses `gen_ai.request.model` and `gen_ai.response.model` from the OpenTelemetry GenAI envelope. The spec the bank conforms to (FFIEC v1.0b §4.4) makes both REQUIRED on any model-call entry. Kognitos's Fields 4 and 5 (AI system identity / model identity) accept any attribute name. Two institutions both satisfying Fields 4 and 5 could be using non-interoperable attribute schemas. No multi-implementation conformance bar.

Chen took the IAM side.

"Diana, you're up on the IAM split."

Diana walked into the engineering floor. The first thing she asked Dr. Wei was whether the sepsis-CDS service account had a separate identity from the platform's service identity.

"Yes. The sepsis-CDS service runs under `sepsis-cds-prod@mercator-memorial`. The patient-context fetcher is `patient-ctx@mercator-memorial`. Each inference's authenticated identity is the calling clinician's session token, threaded through. The service identities are themselves audit-trail-captured for every action."

Diana wrote a check on Field 3 for the AI side. The Kognitos field asked for the authenticated human user, not the service account, and Mercator threaded the clinician identity through the inference path. ✓.

She asked the question she had asked at Northbridge: "Walk me through how an engineer gets emergency write access to the AI-side chain."

"They don't. The chain table has INSERT-only roles for the service identities and SELECT-only roles for the analytics team. There is no role with UPDATE or DELETE in any environment. The role-creation role itself was retired after the deployment ceremony."

Same answer as Northbridge. Same framework-silent depth.

She had the same five-step ◇ chain to record. Plus a new one specific to clinical settings — the override entries themselves carry the structured pick-list reason and link back to the inference. The framework had no row for "the human review record's own provenance," and Mercator handled it cleanly.

> ### ✓ Confirmation #2 — Field 3 satisfied on AI side with chain-driven IAM
>
> All IAM events for the AI-side service identities are chain-captured. Override entries carry clinician identity, timestamp, structured-pick-list reason, and signature linking back to the inference entry. Auto-revocation is chain-driven. Same depth as observed at Northbridge.

Then Diana asked about the *legacy* side.

"Show me the Active Directory IAM history."

Patricia answered before Dr. Wei could. "It's in AD. We have it in a separate dashboard. I'll have Karen bring it up when we move to the legacy walkthrough this afternoon. The short version is — 23 active temporary admins, oldest from 2019. Twelve of them have no documented expiration. Four are former employees whose deactivation got missed in the offboarding workflow. Two are vendor accounts whose vendor contract ended in 2022. The dashboard exists. The audit trail of grants and revocations does not exist as a chain — it exists as the AD event log, which is mutable by the AD admins themselves."

Diana put her pen down.

"Twenty-three active temporary admins from as far back as 2019."

"Yes."

"And the audit trail of the IAM grants is mutable by the AD admins themselves."

"Yes."

Diana wrote in her Field 3 row for the legacy side: *Field 3 FAILED for legacy AD scope. Authenticated human identity exists but its audit trail is itself mutable by the admins whose grants it records. 23 active temporary admins, oldest from 2019. The framework's Field 3 wording — "the verified identity of the human" — is satisfied at the moment of access, but the lifecycle integrity is gone.*

She added: *This is a real Finding against the bank. Not a framework Gap. The bank's legacy AD is operating without integrity discipline on its own audit trail.*

She marked it 🚨 Finding-001.

> ### 🚨 Finding-001 — Legacy AD audit trail is mutable by its own admins (Field 3 partially failed; lifecycle integrity absent)
>
> Mercator's legacy Active Directory carries authenticated human identity for access events, satisfying Field 3 at the moment of access. The IAM lifecycle audit trail (grants, revocations, elevations) is held in the AD event log, which is mutable by the AD admins themselves. 23 active temporary admins, oldest from 2019, 12 with no documented expiration. **For the legacy zone, Field 3 is structurally compromised.** Remediation requires either extending the chain-of-custody substrate to AD lifecycle events or implementing equivalent immutable IAM-lifecycle logging.

Diana noted: this is the first real Finding the team has filed against a bank under the Kognitos framework. It exists because the framework's Field 3 wording is implicit about lifecycle integrity, and an institution operating without lifecycle integrity is detectable under the framework's spirit even if the literal wording is satisfied.

The 23 active temporary admins were not, on their own, a Kognitos Field 3 violation. The audit trail being mutable by its own admins was. The two together produced the finding.

---

## 🧬 1:00 PM — The Legacy Side (CRM, Mulesoft, Lab Pipeline, Claims ETL, Epic)

Lunch was sandwiches in the conference room. Patricia stepped out. Tom closed the door.

"Dawn, where are we at noon?"

"AI side is clean. All 12 fields satisfied, plus eight or nine framework-silent observations for depth — deployment-intent capture, gen_ai.request/response naming, three-layer compositional security on the chained side, override-record provenance. One Finding-001 against the legacy AD."

"And the legacy walkthrough?"

"I'm expecting more Findings. Patricia handed us the map this morning. She knows the legacy side has gaps. She wants them named with the framework's language so the budget request reads cleanly."

The team split. Elena took the CRM. Luis took the lab pipeline and the claims ETL. Raj took Mulesoft. Mike took the Epic boundary.

---

### Elena — Salesforce CRM (PHI in Unaudited Free-Text)

Elena pulled up the Salesforce architecture page. Two business lines on one Salesforce footprint — member-services for the insurance arm and patient-outreach for the physician group. No connector to any chain. Field-history disabled for storage-cost reasons, HITRUST Partial renewed three cycles unfunded.

She opened a member-services case at random. The case description field had clinical notes — PHI — written by a CSA who had taken a member's phone call about a denied claim.

"This is PHI in a free-text field with field history disabled."

Patricia, who had come back into the room, said: "Yes. We know. The HITRUST Partial has been renewed three cycles. The funding to fix it has been deferred each year for storage-cost reasons. The PHI is in the free-text because the CSA needed to capture what the member said, and Salesforce was the system in front of her. We do not have an audit trail of what she wrote, when she wrote it, who else read it, or what was changed. We have backups, but the backup retention is 30 days."

Elena went through her template.

- **Field 1 (Timestamp).** The case has a `LastModifiedDate` but field-history is disabled, so prior modifications are not preserved. Field 1 ✗ — the timestamp on the current version of the field exists; the timestamps of prior modifications do not.
- **Field 6 (Inputs with source attribution).** No source attribution beyond "CSA typed this." No structured field for what the member actually said vs. the CSA's paraphrase. ✗ — Field 6 fails.
- **Field 9 (Output produced).** Not applicable; the CRM is not the AI side. But the free-text field is information that *feeds* downstream AI decisions when the CRM data is reused. The provenance gap propagates. ⚠ — concern noted.
- **Field 12 (Tamper-evident integrity proof).** None. Salesforce field-history disabled, backups deletable by IT, no append-only enforcement at the storage tier. ✗ — Field 12 fails decisively.

Elena marked four field failures on the legacy CRM. Three failed fields constituted a Finding under most engagement-framework conventions; the team's firm had a policy that two failed fields on a single system was a Material Finding.

> ### 🚨 Finding-002 — Salesforce CRM legacy scope fails Fields 1, 6, 12 (Material Finding)
>
> Member-services and patient-outreach Salesforce instance carries PHI in free-text case description fields with field-history disabled and 30-day backup retention. No tamper-evident audit trail of who wrote what, when, or whether content was modified. Fields 1 (timestamp completeness), 6 (input source attribution), and 12 (tamper-evident integrity proof) all fail. **Material Finding.** Remediation requires either (a) extending the chain substrate to the CRM with a SaaS-edge connector (the bank's preferred direction per the budget request), or (b) enabling Salesforce field history, native auditing, and immutable backup retention as an interim discipline.

Elena added in her margin: *The framework has clean language for the failures. What it doesn't have is language for what the bank should do with the PHI gap in the interim. §10.22 pre-MAC redaction discipline (which is what the bank would adopt under the FFIEC substrate) is invisible to Kognitos. The bank can adopt it without the framework asking; the framework can't recommend it.*

### Luis — Lab Pipeline + Claims ETL

Luis walked through the lab pipeline. Three-day Dead Letter Queue. S3 with CloudTrail logging — but CloudTrail itself was *disable-able* by a privileged storage-account principal. He found the audit log for CloudTrail enablement state and noted that it had been disabled twice in 2024 during maintenance windows. Both times re-enabled. But the gaps in CloudTrail during those windows meant that any S3-side changes to lab archives during those hours were not retained.

He marked Field 12 ✗ for the lab pipeline.

He moved to the claims ETL. The checksum table for downstream reconciliation was a DynamoDB table with no immutability. Edits to the checksum table were allowed by the engineering team's normal IAM principals.

He marked Field 12 ✗ for the claims ETL.

> ### 🚨 Finding-003 — Lab pipeline fails Field 12 (CloudTrail disable-able, S3 not in compliance mode)
> 
> Lab results pipeline uses S3 storage with CloudTrail logging that is itself disable-able by storage-account principals. CloudTrail was disabled twice in 2024 during maintenance windows. During those windows, S3-side changes are not retained. Field 12 fails for lab archive integrity.

> ### 🚨 Finding-004 — Claims ETL fails Field 12 (editable checksum table)
>
> Claims ETL maintains a DynamoDB checksum table for downstream reconciliation. The table accepts UPDATE operations from normal engineering principals. The checksum that is supposed to detect tampering can itself be tampered with. Field 12 fails.

Luis noted in his cover memo: *The framework's Field 12 has clean language for both failures. What it doesn't have is the cross-cutting language for "the integrity of the integrity-detection mechanism." The claims ETL fails because the checksum table that detects tampering is itself tamperable. Field 12 records this as "no tamper-evident integrity proof"; under the bank's reference spec, §10.23 consumer-correlation index integrity is the named primitive. Kognitos's failure code is adequate; the diagnostic language for what specifically fails is missing.* ◇.

### Raj — Mulesoft Boundary

Raj walked through the Mulesoft Epic-billing handoff. 6-week retention dial controlled by eight engineers. Any of the eight could shorten retention.

He marked Field 12 ⚠ Partial — the retention is short relative to the 90-day FDA SaMD post-market window, and the retention itself is mutable by the engineers who run the integration.

He added: under FFIEC v1.0b's §10.13 evidentiary-artifacts retention list, the institution's CC8.1 control description would name the retention duration explicitly and tie retention shortening to a sealed chain event. Kognitos has no field for retention discipline. The bank's posture (engineering-team mutable, 6 weeks, no audit-trail of retention changes) satisfies Kognitos's Field 12 *at the time of audit* — entries within the 6-week window are present — but produces a structural blind spot whenever the audit window exceeds 6 weeks, or whenever retention is shortened without notice.

> ### ⚠ Partial #1 — Mulesoft Epic-billing handoff retention discipline
>
> 6-week retention dial controlled by eight engineering principals. Field 12 is satisfied at the moment of audit but the retention discipline itself is not auditable. The framework has no row for retention-control integrity. Filed as Partial pending remediation through the planned chain extension.

### Mike — Epic Boundary (Mutable Notes Post-Hoc)

Mike asked Dr. Wei to walk him through what happens when a clinician's note is edited in Epic after the sepsis-CDS prediction was recorded.

"Epic supports note edits within a 90-day window with an Epic-side audit trail. After 90 days, the note is locked. The Epic audit trail is held in Epic's own audit-log schema and is mutable by Epic database administrators with sufficient privilege."

Mike picked one of the reconciliation-test alerts. The forward-reconciliation step (chain → Epic note) revealed that two of the five tested alerts had their downstream Epic notes rewritten post-hoc within the 90-day window. The chain captured what the model said; Epic captured what the clinician wrote. The two were not the same any more, and the Epic side had no chain-of-custody integrity.

He marked Field 10 (downstream action) ⚠ Partial. The action was recorded in Epic but Epic's recording was itself mutable.

> ### ⚠ Partial #2 — Epic clinical note post-hoc edits compromise downstream-action integrity (Field 10)
>
> 5-alert reconciliation test produced 3/5 forward-reconciliation matches between chain entries and downstream Epic notes. Two failures were post-hoc note edits within Epic's 90-day window. Field 10 is satisfied at the moment of recording but the recording is itself mutable. The framework has no row for "downstream-system action immutability." Remediation requires either chain extension to Epic boundary events or a §10.21 cross-vendor model-handover schema applied to EHR write-back.

---

## 📊 3:00 PM — Reconciliation Test

Dawn ran her usual reconciliation test, scoped this time to a 5-alert sample.

```
5 alerts selected — sepsis predictions from April 10-12, three hospitals, four model versions.

Inference reconciliation (chain → operational AI-side view):
  5/5 PASS

Backward reconciliation (chain → source lab record):
  4/5 PASS
  1/5 FAIL — source lab record purged 60 days ago by a retention job
            that has since been disabled. Lab archive S3 had CloudTrail
            disabled during the relevant maintenance window.

Forward reconciliation (chain → downstream Epic clinical note):
  3/5 PASS
  2/5 FAIL — Epic clinical notes were rewritten post-hoc within Epic's
            90-day editable window. Chain captured what the model said;
            Epic captured a different clinical note.
```

Three forward failures. The chain side passed every test. The legacy side failed three of the cross-system reconciliations.

Dawn looked at the result.

The framework had clean language for the chain-side passes. It had clean language for the legacy-side failures of Field 12 (CloudTrail disable, mutable checksum) and Field 10 (Epic post-hoc edits). It had **no language for the relationship between the two zones** — the way the chain's integrity ended at the boundary of its coverage, and the legacy zone's vulnerabilities propagated backward across that boundary to compromise the value of the chain.

She wrote in her cover-memo notes: *The chain-side integrity is sound. The legacy-side failures are real. What the framework cannot articulate is that the legacy-side failures compromise the chain's evidentiary value retroactively. The chain captured the model's prediction byte-for-byte; the source lab record that justified the prediction has been purged. The chain is intact; the audit story isn't. Under the bank's reference spec (§10.19 chain-coverage boundary + §10.13 evidentiary-artifacts retention), this is captured as a coverage-map property — the green zone's evidentiary value depends on the red zone's substitute discipline. The framework has neither.*

> ### ✗ Gap (Framework) — No primitive for coverage-boundary integrity propagation
>
> The framework treats the audit trail as a per-event row schema. It has no language for the property that an audit trail's evidentiary value depends on the integrity of the systems it references — the source data, the downstream actions, the IAM substrate. When the chain-side is sound but the legacy-side has integrity failures, the framework records the legacy failures as Field-specific Findings (Field 10, Field 12) but cannot record the way those failures retroactively compromise the chain's evidentiary value. **The §10.19 chain-coverage map and §10.13 evidentiary-artifacts retention list together would handle this in the bank's reference spec. Kognitos has neither.** Filed as a Framework Gap distinct from any bank finding.

---

## 🌆 5:30 PM — Debrief

The team gathered in the engagement room. Patricia stepped out.

Dawn wrote on the whiteboard.

```
KOGNITOS 12-FIELD ASSESSMENT — MERCATOR HEALTH SYSTEM

AI SIDE (sepsis-CDS, chained, 90 days live):
  Confirmations:                  12   (Fields 1-12 satisfied on inference entries;
                                        Field 3 satisfied with chain-driven IAM)
  Partials:                        0
  Findings against bank:           0
  Framework-silent observations:  9    (deployment-intent, gen_ai.* naming,
                                        compositional security, override provenance,
                                        key-rotation transparency, others)

LEGACY SIDE (everything else):
  Findings against bank:           4   (Finding-001 legacy AD;
                                        Finding-002 CRM PHI free-text;
                                        Finding-003 lab pipeline CloudTrail;
                                        Finding-004 claims ETL checksum)
  Partials against bank:           2   (Mulesoft retention; Epic post-hoc edits)
  Confirmations:                   0   (no system in the legacy zone passes Field 12)

CROSS-ZONE:
  Framework Gap:                  1   (coverage-boundary integrity propagation)

  Reconciliation test:
    5/5 inference (PASS)
    4/5 backward (1 source lab record purged; lab CloudTrail disable-able)
    3/5 forward  (2 Epic notes rewritten post-hoc)
```

Underneath, she wrote:

```
ENGAGEMENT-TEAM OBSERVATIONS ON FRAMEWORK SELECTION:

1. The Kognitos 12-field framework gives the team clean language for the AI-side
   confirmations and the legacy-side Findings. The cross-zone integrity-propagation
   issue — where legacy failures retroactively compromise chain evidentiary value —
   has no framework anchor. The team must describe it in prose.

2. The framework has no concept of "coverage scope" or "evidentiary substitute."
   The bank's reference spec carries §10.19 (chain-coverage map) and §10.13
   (evidentiary-artifacts retention) — these handle bifurcated assessment natively.
   Under our framework, bifurcation is bolted together by stapling two complete
   framework runs and writing the boundary in prose.

3. Finding-001 (legacy AD audit-trail mutability) is filed against the bank
   under Field 3's spirit, not its literal wording. The framework's Field 3 asks
   for "the verified identity of the human"; it does not normate that the human's
   identity-grant lifecycle must itself be audit-trail-captured with integrity.
   The team made a judgment call to elevate this to a Finding because the legacy
   posture (23 active temporary admins, mutable audit log) fails Field 3's spirit.
   A less-rigorous engagement team could downgrade this to a Recommendation under
   the same framework wording.

4. The bank's budget request to extend the chain to the legacy zone is grounded
   in this report. The Findings against the legacy systems are real; the
   remediation (extending the chain substrate) is well-defined; the operational
   value is concrete. Patricia has the documentation she needs.
```

She turned around.

Mike said: "The 12 fields walked cleanly on the AI side. Same depth as Northbridge. The legacy side is the part that took the day."

Diana said: "Finding-001 on the legacy AD was the call I made. The framework's Field 3 wording could go either way. I went with Finding."

Elena said: "The PHI in CRM free-text was the easiest finding I've written this year. Field 1, 6, and 12 all fail cleanly. Material Finding under any framework convention."

Luis said: "Field 12 failed twice in the legacy zone — lab pipeline and claims ETL. Both are storage-tier integrity failures. The framework gave me clean language for the diagnosis but not for the specific remediation discipline. The bank's reference spec has §10.23 consumer-correlation index integrity for the claims ETL case; ours doesn't."

Raj said: "Mulesoft was a Partial. Six-week retention with eight engineers controlling the dial. The framework records it as Partial; under the bank's spec it would be a Finding because §10.13 retention discipline would name the duration explicitly and tie shortening to a chain event. The framework gives the engagement team more discretion."

Chen said: "The reconciliation test was the cleanest illustration of the coverage-boundary gap. 5/5 inference, 4/5 backward, 3/5 forward. The chain captured what the model said. The systems on either side of the chain mutated the source and the downstream. The framework can name each system's failure; it cannot name the way those failures compromise the chain's value."

Tom finished writing. He had a question for Dawn.

"If we were under FFIEC v1.0b today, what would the legacy-side report look like?"

Dawn took her time.

"Probably the same four Findings against the bank, plus two Partials, plus the chain-coverage-boundary discussion would have a normative spine — §10.19 plus §10.13 — instead of being something we describe in prose. The bank would have the same budget request to fund. The remediation work would be the same. The framework lets us mark the gaps; the spec would let us mark them and also articulate the boundary discipline they sit inside."

"So the report changes shape but the operational outcome converges."

"At an institution like Mercator, where the CISO asked for the gaps to be found and named, the outcome converges. At an institution that wanted to minimize the report's bite, the framework's silence on coverage discipline would let the engagement team write a thinner cover memo. The bank's culture is doing the work the framework isn't again, just like at Northbridge."

Tom wrote that down.

Dawn was quiet for a moment.

"Patricia knew the chain didn't reach the legacy systems. She knew the legacy systems had integrity gaps. She knew the report was going to name them. What she wanted from us was the documentation she could take to the board. The framework gave her exactly that for the AI side and for each legacy system individually. The cross-zone story — the way the AI side's evidentiary value depends on the legacy side's substitute discipline — is the part the framework cannot articulate, and the part the budget request actually needs to argue. Patricia is going to have to write that part herself."

She paused.

"Tom, in the cover memo: note that the bank's CISO will need to author the cross-zone evidentiary-substitute argument independently. The framework cannot supply it."

Tom wrote.

He underlined "cross-zone evidentiary-substitute argument."

Patricia came back into the room with coffee. She read the whiteboard.

"Four Findings on the legacy side. Two Partials. One Finding on legacy AD. Zero on the AI side. That is the report I asked for. The cross-zone framework gap — that is the part I expected your firm not to have language for. We've been working with the bank's reference spec for nine months; the §10.19 coverage-map language gave us the conceptual spine for the budget request. I'll author that part. Your report names the gaps; my budget argument frames the gaps."

Dawn nodded.

"That is the right division of labor."

Patricia almost smiled. "It is the only division of labor that works. The auditor names what they can see in their framework. The institution authors what the framework can't articulate. We have done it for HITRUST, for HIPAA, for FDA SaMD. We will do it for Kognitos. The framework you brought is younger than my CISO tenure; I do not expect it to carry everything."

She picked up the report draft. She turned to leave.

She stopped at the door.

"Dawn."

"Mm."

"Thank you for not softening the legacy findings. The board needs the bite. The budget request needs four real Findings and two real Partials with concrete remediation paths, not a recommendation memo."

"That was the assignment."

"Yes. And the framework you brought gave you exactly enough language to do it. The cross-zone gap was the part I expected. You named it; that's enough."

She walked out.

---

## ❌ What They Expected vs ✅ What They Found — and What Their Framework Could Record

**❌ What They Expected:**

- AI side might have field-level gaps where the chain didn't reach a specific Kognitos requirement.
- Legacy side might have *some* findings the team would have to wrestle with.
- The 12-field framework would be enough to write a bifurcated assessment without prose stapling.

**✅ What They Found:**

- AI side cleared all 12 Kognitos fields plus 9 framework-silent depth observations.
- Legacy side produced 4 Findings (legacy AD, CRM PHI, lab pipeline CloudTrail, claims ETL checksum), 2 Partials (Mulesoft retention, Epic post-hoc edits), and 0 Confirmations across the legacy zone.
- The 12-field framework has clean per-system language but no coverage-boundary primitive. Bifurcated assessment requires prose stapling.

**⚠ What Their Framework Could Not Record:**

- Coverage-boundary integrity propagation (the way legacy-side failures compromise chain-side evidentiary value retroactively).
- Evidentiary-substitute discipline for unchained systems.
- Cross-vendor model-handover schema for the planned EHR write-back extension.
- The bank's voluntary §10.20 training-data retention floor (pre-launch backfill 18-day overlap).
- The bank's three-layer compositional security on the chain side.

---

## 🧾 Final Assessment Theme

> "The organization operates a partial chain-of-custody deployment with strong integrity on the AI-side scope and material integrity gaps on the legacy scope. The Kognitos 12-field framework records the AI-side as twelve clean Confirmations and the legacy-side as four Findings and two Partials, with one Framework Gap on the boundary itself. The institution is funded to remediate; the framework supports the diagnosis but not the cross-zone evidentiary-substitute argument the budget request requires. The institution's CISO authors that argument independently of the framework."

---

## Research takeaway

Chapter 02 produces a different research signal from Chapter 01. Chapter 01 showed the framework's shallowness when the bank exceeds it everywhere; speculation gaps dominated the report and the bank's culture made the operational outcome converge. Chapter 02 shows the framework's shallowness in a different way: when the bank has a *partial* deployment, the framework lacks a coverage-map primitive to express the boundary cleanly. Per-system findings are clean; per-zone narrative requires the institution to author it independently.

Combined, Chapter 01 and Chapter 02 show that the Kognitos framework's row-list-as-schema genre handles two scenarios differently:
- **Full deep deployment:** speculation gaps dominate; institution culture covers them.
- **Partial deployment:** per-system findings are tractable; cross-zone narrative is not.

Both scenarios produce reports that satisfy the framework. Both rely on institution-side culture to do the work the framework cannot articulate. The convergence on operational outcome is conditional on that culture being present.
