# Comparative Analysis — Chapter 02 (Mercator Health System)

*Side-by-side analysis of how the Kognitos 12-field framework and the TesseraSeal / FFIEC chain-of-custody v1.0b spec handle each audit moment in Chapter 02. Companion document to the chapter file. Honest assessment of how much an auditor has to speculate when operating under each framework against a **bifurcated deployment** with strong AI-side capture and weak legacy-side controls.*

---

## How this chapter differs from Chapter 01

Chapter 01 (Northbridge) produced one research signal: the framework's shallowness when the bank exceeds it everywhere; speculation gaps dominated the report. Chapter 02 produces a different signal: the framework's shallowness **when the bank has a partial deployment**. The legacy zone produces real Findings against the bank; the framework gives the team clean per-system language for each Finding but **lacks a coverage-boundary primitive** to express the cross-zone narrative.

The Chapter 01 comparison points still apply on the AI side. For those, this document references the Chapter 01 comparison rather than restating in full. The Chapter 02 comparison focuses on **new comparison points that emerged from the bifurcation and from the healthcare-specific scenarios** (HIPAA + FDA SaMD + HITRUST).

### Quick map to Chapter 01 comparison points (recurring on the AI side)

These play out the same way under Kognitos as in Chapter 01. Severities unchanged:

| # | Area | Chapter 01 ref | Chapter 02 instance |
|---|---|---|---|
| 1 | Timestamp depth | Ch01 §1 | `ts: 2026-04-12T09:42:11.483Z` — millisecond UTC; same dual-timestamp story under §4.4 |
| 4 | Compositional security | Ch01 §4 | Same three-layer story on sepsis-CDS chain; framework records as one Field 12 Confirmation |
| 5 | IAM lifecycle (AI side) | Ch01 §5 | Same chain-driven IAM on AI side. **Legacy AD fails inversely** — see new point B below |
| 6 | Connector-source family | Ch01 §6 | Forward-looking — applies when CRM extension lands |
| 12 | Reference-verifier distribution | Ch01 §12 | FDA reviewer ran the Cosign-signed reference verifier independently. Same Kognitos blind spot. |
| 13 | Cross-key-rotation verification | Ch01 §13 | November 2025 retraining + key rotation verified. Same framework silence. |

---

## New comparison points specific to Chapter 02

Twelve distinct new comparison points emerged from this engagement.

---

### A. Coverage-boundary integrity propagation — the chapter's central new gap

**The audit-room question.** *"The chain is sound for the sepsis-CDS scope. The legacy systems have integrity gaps. How do we record the way those legacy gaps retroactively compromise the chain's evidentiary value?"*

**TesseraSeal.** §10.19 chain-coverage boundary documentation: every conformant institution publishes a chain-coverage map that names which systems are inside the integrity substrate and which are outside. For systems outside, §10.13 evidentiary-artifacts retention names the substitute discipline. The two together give the audit team a normative spine for a bifurcated assessment — green zone is the chain, red zone is the evidentiary substitute, and the institution's CC8.1 cross-references both per §10.18.

**Kognitos.** No concept of coverage scope. No notion of evidentiary substitute. The 12-field framework treats audit-trail capture as a single property — either the AI events satisfy each field or they don't. The framework cannot articulate "covered here, not covered there, and here's what stands in."

**Speculation gap.** Under Kognitos, the audit team can mark each system Pass / Fail against Field 12 independently, but has no framework anchor for the cross-zone narrative. The Mercator reconciliation test produced 5/5 inference, 4/5 backward (a source lab record was purged), 3/5 forward (two Epic notes were rewritten post-hoc). The chain side passed everything; the failures came from systems on either side of the chain. **The framework records the per-system failures but cannot articulate the way those failures retroactively compromise the chain's evidentiary value.**

The audit team has to write that argument in prose. The institution's CISO has to author the cross-zone evidentiary-substitute discipline independently of the framework.

**Structural reason for the gap.** Kognitos's framework is row-shaped — it lists what a single audit-trail row should contain. Cross-zone integrity propagation is a system-architecture property that operates across rows AND across systems. A row-list-as-schema framework cannot articulate cross-system architectural relationships without expanding its genre. The §10.19 coverage-map primitive is a spec-genre artifact (procedural + scope-bound); Kognitos is a checklist-genre artifact (per-row + scope-agnostic). The genres handle coverage differently because they exist for different purposes.

**Honest assessment.** For institutions with full deployments (no bifurcation), this gap is invisible — there's no cross-zone narrative to write. For institutions with partial deployments — which is most institutions adopting AI audit-trail discipline incrementally — the gap is structural. The auditor has to write prose where the framework should have a primitive. The institution has to author the budget-request argument independently of the framework that supposedly anchors the audit. **Severity: high for partial deployments; not applicable to full deployments.**

This is Chapter 02's most significant new finding. Combined with Chapter 01's compositional-security gap, this is the second time a Kognitos blind spot has produced a measurable difference in how the auditor has to construct the report.

---

### B. IAM lifecycle integrity — legacy zone failure mode

**The audit-room question.** *"The legacy Active Directory has 23 active temporary admins, oldest from 2019, and the audit log of grants/revocations is mutable by the AD admins themselves. Field 3 captures the human identity at the moment of access. Does the framework let us call this a Finding?"*

**TesseraSeal.** No specific section is required to elevate this to a Finding — under FFIEC v1.0b's IAM discipline (chain-captured IAM events tagged `event_class=iam`), an institution operating without IAM-lifecycle integrity is structurally non-conformant. The §10.19 coverage map names the IAM zone as either inside the chain or outside; if outside, §10.13 names the evidentiary substitute; if substitute is itself mutable, the institution is non-conformant.

**Kognitos.** Field 3: *"The verified identity of the human whose session triggered the work that led to the AI decision. Not a service account. Not an API key. The actual SSO-authenticated user."* The field is literally satisfied — the legacy AD captures the authenticated human at the moment of access. The framework does not specify that the IAM lifecycle producing that authentication must itself be audit-trail-captured with integrity.

**Speculation gap.** Under Kognitos, two engagement teams reviewing the same legacy AD posture can reach different conclusions:
- **Team A** reads Field 3 literally — the authenticated human is captured at access time. Field 3 ✓. The 23 active temporary admins and mutable audit log are recorded as Recommendations or Observations.
- **Team B** reads Field 3 in spirit — Field 3 implicitly requires that the human identity be trustworthy, and trustworthiness requires that the IAM lifecycle producing the identity is auditable. Field 3 ✗ for legacy AD. Elevated to Finding.

Neither team has done anything wrong relative to the framework. The framework's lack of severity-classification normativity (see Ch01 §3) compounds the lack of lifecycle-integrity wording in Field 3 itself.

**Honest assessment.** The Chapter 02 audit team chose Team B's reading and filed Finding-001. A less-rigorous engagement team operating under the same framework could downgrade this to a Recommendation. The bank's posture (23 active temporary admins, mutable audit log) would receive a Finding under FFIEC v1.0b's IAM discipline without engagement-team discretion. **This is structurally consequential**: institutions with weak legacy IAM can choose audit firms whose engagement teams read Field 3 literally, and pass the framework. Severity: high.

---

### C. Evidentiary substitute discipline — what stands in when there's no chain

**The audit-room question.** *"The CRM has PHI in free-text fields with field-history disabled. The lab pipeline has CloudTrail that's disable-able. The claims ETL has an editable checksum table. We're filing each as a Field 12 Finding. What do we say about the *interim* discipline the bank should adopt before chain extension lands?"*

**TesseraSeal.** §10.13 evidentiary-artifacts retention list specifies, for each evidentiary artifact, the retention floor and the substitute discipline when chain-of-custody is not yet operational. §10.22 pre-MAC redaction discipline names the PHI-handling pattern. §10.23 consumer-correlation index integrity names the checksum-table integrity discipline. §10.18 CC8.1 cross-referencing ties the institution's runbook to the relevant section.

**Kognitos.** No equivalent. The framework records per-field failures; it does not prescribe interim substitute discipline for systems failing those fields. An institution failing Field 12 has no framework guidance on what to do *until* chain coverage lands.

**Speculation gap.** Under Kognitos, the auditor can name the failure but not the interim remediation. The institution must author the interim discipline independently or borrow from an adjacent framework (HITRUST, HIPAA §164.312, ISO 27001).

**Structural reason for the gap.** Kognitos is a checklist of what *should* be captured. It is not a prescriptive substitute discipline for systems that aren't capturing. The genre boundary is real: a 12-row schema cannot prescribe remediation patterns without becoming a different kind of artifact.

**Honest assessment.** For institutions where the audit produces a remediation roadmap, this gap matters. The Chapter 02 team had clean failure-naming under Kognitos and incomplete remediation guidance. The institution had to draw on HITRUST and HIPAA for the substitute discipline. **Severity: medium-high** for engagements where the audit is supposed to drive remediation planning; lower for compliance-confirmation engagements.

---

### D. Deployment-intent capture — production / canary / ab_test

**The audit-room question.** *"The model team rolled out v3.2.0 in February, observed elevated false-positive rate within 36 hours, and rolled back to v3.1.7. How does the audit trail capture the deployment posture during the canary window?"*

**TesseraSeal.** §4.4.2 deployment-intent capture: every model call carries `audit.deployment.intent` from an enumerated set (`production | canary | ab_test`), with `audit.deployment.policy_version` conditionally required whenever any `audit.deployment.*` attribute is present. The February v3.2.0→v3.1.7 rollback was a sealed canary chain entry with the rollback decision itself chained as a policy event. MRM committee can correlate any change-point with the policy in force at decision time.

**Kognitos.** No field for deployment intent. Field 4 (AI system identity) and Field 5 (model identity) capture the model version but do not address whether the model was operating in production, canary, A/B-test, or shadow mode.

**Speculation gap.** Under Kognitos, an institution silently flipping a production model with no audit-trail of the deployment posture satisfies Fields 4 and 5 identically to one operating disciplined canary/A-B discipline with the deployment intent chained per call. The auditor cannot distinguish.

**Structural reason for the gap.** Deployment intent is a model-operations property, not a per-event capture property. The 12-field schema is per-event; model-ops cadence sits outside the row.

**Honest assessment.** For institutions operating disciplined model-ops cycles (canary rollouts, A/B tests, rollback drills), the framework cannot record the discipline. For institutions operating "flip the flag in production" rollouts, the framework cannot detect the absence. Mercator handled the February rollback cleanly; the framework has no row to record how cleanly. **Severity: medium** — invisible to most audits; consequential when post-incident review needs to know what was in production at decision time.

---

### E. OpenTelemetry GenAI envelope naming — `gen_ai.request.model` / `gen_ai.response.model`

**The audit-room question.** *"You have both `gen_ai.request.model` and `gen_ai.response.model` populated. Why both? They're equal here."*

**TesseraSeal.** §4.4 makes both REQUIRED on any chain entry representing a model call. The two fields are normatively distinct because the framework spec contemplates **silent vendor-side rerouting** — an LLM provider returning responses from a different model than the one requested, without disclosing the substitution. The request-side captures what the institution asked for; the response-side captures what the model actually answered with. Equal values are evidence of no rerouting; divergent values are an investigatable event.

**Kognitos.** Field 4 (AI system identity and version) and Field 5 (model identity and version) capture the model identity but do not require the request/response distinction. An implementation logging a single `model_id` attribute satisfies both fields literally.

**Speculation gap.** Under Kognitos, an institution unaware of silent-vendor-rerouting attack class would log `model_id` once and satisfy the framework. The institution would have no detection capability if the vendor silently substituted a different model behind the API. **The framework's wording accepts implementations that cannot detect a known attack class.**

**Structural reason for the gap.** OpenTelemetry GenAI conventions are an industry-collaborative naming standard that emerged after Kognitos's framework was authored. The 12-field schema does not bind to any specific attribute namespace; it asks for the property and accepts any naming. Multi-implementation conformance via a shared namespace requires an authoritative standards body's blessing; Kognitos does not have that standing.

**Honest assessment.** For institutions using LLM APIs from external vendors (most institutions adopting AI today), silent-vendor-rerouting is a real attack vector. The OTel GenAI envelope is the emerging industry response. Kognitos's framework cannot anchor to it. **Severity: medium-high** for LLM-API consumers; lower for institutions running models in-house under their own version control.

---

### F. Override-record provenance — the human-review record's own integrity

**The audit-room question.** *"The clinician overrode the model 30% of the time. The override entry has the clinician ID, timestamp, override reason from a pick-list, and signature. Does Field 11 (human review) require the override record itself to be tamper-evident?"*

**TesseraSeal.** Override entries are themselves chain entries with `parent_run_id` / `parent_seq` linking back to the inference entry. The override carries the structured pick-list reason and the clinician's signature. The override entry is MAC-bound and Merkle-sealed identically to the inference entry. Post-hoc edits to the override are detectable.

**Kognitos.** Field 11: *"When a human reviewed or approved the AI's output before action, the reviewer's identity, timestamp, and disposition (approved / rejected / modified / escalated). Includes override path documentation for clinical-decision-support style systems where the human chose to deviate from the AI recommendation."* The field requires the override record's content but does not normate the override record's own tamper-evidence.

**Speculation gap.** Under Kognitos, an institution recording overrides in a mutable system (an EHR free-text field, a mutable database row) satisfies Field 11 literally. The institution with chain-bound override records satisfies it identically. The framework cannot distinguish whether the human-review evidence is itself trustworthy.

**Structural reason for the gap.** Field 11's wording is *what to capture*. Field 12 covers integrity. The relationship between them — that the human-review evidence must itself satisfy Field 12 — is implicit but not explicit. An institution operating Field 11 in a mutable substrate and Field 12 only on the AI inference would pass both fields independently while having no integrity protection on the human-review evidence.

**Honest assessment.** For clinical decision support (Chapter 02's domain), the override record is often the most legally consequential artifact — it's the document plaintiff's counsel will request when a model-driven clinical error lands in court. Mercator's chain-bound override discipline is materially stronger than a mutable-EHR override record; Kognitos cannot distinguish them. **Severity: medium-high** for clinical AI; medium for other CDS contexts.

---

### G. PHI redaction discipline — pre-MAC redaction vs post-hoc obscuring

**The audit-room question.** *"The CRM case description contains PHI written by a CSA who took a member's call. The case description is free-text. How does the audit trail handle PHI?"*

**TesseraSeal.** §10.22 pre-MAC redaction discipline names the pattern: PHI is redacted *before* the per-event MAC is computed, so the canonical bytes the MAC covers do not contain PHI. The institution's redaction policy version is bound under the MAC. The post-redaction view is what the chain captures; the pre-redaction view is held outside the chain under PHI access controls.

**Kognitos.** No field for redaction discipline. Field 6 (inputs with source attribution) names the input but does not address PHI handling.

**Speculation gap.** Under Kognitos, an institution capturing PHI directly into a free-text field with no redaction discipline satisfies the framework if Field 6 has source attribution. An institution doing pre-MAC redaction satisfies the same field. The framework cannot distinguish.

**Structural reason for the gap.** PHI discipline is a regulatory crossover concern (HIPAA, HITRUST, GDPR). A cross-regulator marketing-grade synthesis must avoid prescribing regulator-specific patterns or it loses generality. Kognitos's framework explicitly punts PHI handling to the per-regulator framework. The pre-MAC redaction pattern lives in FFIEC v1.0b's §10.22 because the spec is designed to be regulator-anchored.

**Honest assessment.** For healthcare institutions, PHI redaction is operative. Mercator's CRM legacy posture (PHI in free-text, no redaction discipline) is a HIPAA exposure; Kognitos cannot detect it because the framework is regulator-agnostic. The Chapter 02 team filed Finding-002 against the CRM under the spirit of Fields 1, 6, and 12 combined, but the specific PHI-redaction recommendation came from HIPAA, not from Kognitos. **Severity: high** for healthcare; not applicable in non-PHI contexts.

---

### H. Consumer-correlation index integrity — claims ETL editable checksum

**The audit-room question.** *"The claims ETL maintains a DynamoDB checksum table for downstream reconciliation. The table is editable by engineering principals. Field 12 fails for the claims ETL — but what specifically is the failure?"*

**TesseraSeal.** §10.23 consumer-correlation index integrity: any reconciliation index, checksum table, or correlation key that is referenced by downstream auditing must itself be tamper-evident. The reconciliation table is a chain entry; updates to the table are chain events; the integrity of the table is bound under the same per-tenant MAC as the data it references.

**Kognitos.** Field 12: tamper-evident integrity proof. The field correctly fails for the claims ETL's editable checksum table — the integrity proof is itself tamperable. The diagnostic language Kognitos provides: "Field 12 fails." That's adequate for naming the failure.

**Speculation gap.** Under Kognitos, the auditor knows the failure but does not have specific remediation language. The claims ETL fails because the checksum that detects tampering can itself be tampered with — that's a specific failure mode (the integrity of the integrity-detection mechanism) that §10.23 names directly. Kognitos records it generically.

**Honest assessment.** For institutions building remediation roadmaps, the specific failure-mode language matters. "The checksum table that detects tampering can itself be tampered with — fix the integrity of the integrity-detection mechanism" is the remediation. Kognitos says "Field 12 fails — implement tamper-evident integrity proof." The institution has to translate the failure into the specific remediation. **Severity: medium** — failure-naming is clean; specific-remediation-language is missing.

---

### I. Storage-tier integrity vs convention — CloudTrail disable-able S3

**The audit-room question.** *"The lab pipeline uses S3 with CloudTrail logging. CloudTrail is itself disable-able by storage-account principals. It was disabled twice in 2024 during maintenance windows. Field 12 fails — but how do we characterize the specific architectural failure?"*

**TesseraSeal.** §10.3 + §10.5 + §10.13: storage-tier integrity must be enforced by the storage tier itself (object lock in compliance mode), in a separate trust boundary from the application account. CloudTrail-disable-able S3 is structurally inadequate — the integrity proof depends on a logging mechanism that can be turned off by privileged storage-account principals.

**Kognitos.** Field 12: tamper-evident. The "or WORM equivalent" wording accepts CloudTrail-logged S3 as one possible implementation. An institution using CloudTrail-logged S3 with CloudTrail disable-able satisfies Field 12 at the time of audit *if CloudTrail was enabled during the audit window*. The framework cannot detect the disable-during-maintenance attack window.

**Speculation gap.** Under Kognitos, the auditor inspecting an audit-window-complete CloudTrail trail concludes Field 12 ✓. The auditor who happens to ask "is CloudTrail itself protected from disablement?" can elevate to Finding. The framework does not require the question.

**Honest assessment.** For storage-tier integrity, "by storage policy" vs "by IAM convention" is the operative distinction. Compliance-mode object-lock in a separate trust boundary is materially stronger than CloudTrail-logged S3 that can be disabled by privileged principals during maintenance windows. Kognitos's framework accepts both implementations identically. **Severity: medium-high** for insider-with-privilege threat models; this is the Ch01 §11 (separate trust boundary) point exercised in a specific failure mode.

---

### J. Retention-control discipline — Mulesoft 6-week dial controlled by 8 engineers

**The audit-room question.** *"The Mulesoft Epic-billing handoff has a 6-week retention dial controlled by 8 engineers. Any of the 8 can shorten retention without an audit trail of the change. The 90-day FDA SaMD post-market window exceeds the retention. Is this a Field 12 Finding or a Partial?"*

**TesseraSeal.** §10.13 evidentiary-artifacts retention list: the institution's CC8.1 control description names the retention duration explicitly per artifact category. §10.18 ties the retention specification to a chain event — any change to retention is itself a sealed chain entry with the role that requested the change, the prior policy, the new policy, and the time-to-effect. Retention shortening is detectable; the dial-control discipline is auditable.

**Kognitos.** No field for retention discipline. Field 12 covers tamper-evidence on the data; the framework does not address retention duration or retention-change auditability.

**Speculation gap.** Under Kognitos, an institution with a 1-day retention or a 10-year retention satisfies Field 12 identically if the data within retention is tamper-evident. The audit team's only language for retention concerns is to elevate to Partial or Finding based on engagement judgment — but the framework has no row to anchor the elevation. The Chapter 02 team filed Mulesoft as Partial because the 6-week retention is shorter than the 90-day FDA window but the data within retention is tamper-evident enough to satisfy Field 12 literally.

**Honest assessment.** Retention duration is operative for any audit that operates over a window longer than the institution's retention. For FDA SaMD post-market surveillance (90-day window), Mulesoft's 6-week retention is structurally inadequate. Kognitos's framework cannot articulate this. The engagement team's Partial filing was a judgment call — under FFIEC v1.0b's §10.13, this would be a Finding without discretion because the institution's stated retention is shorter than the cited regulatory window. **Severity: medium-high** for institutions with regulatory windows; lower for shorter-cycle audits.

---

### K. Cross-vendor model-handover schema — EHR write-back extension pattern

**The audit-room question.** *"The chain captures the model's prediction. The clinician's action lands in Epic. The Epic note can be edited within 90 days. The 2/5 forward-reconciliation failures are post-hoc Epic edits. When the chain extends to the EHR boundary, what schema does the handover use?"*

**TesseraSeal.** §10.21 cross-vendor model-handover schema names the attribute family for chain entries that span a vendor boundary (Epic write-back, Cerner export, third-party EHR integration). Schema includes model card reference, training-data summary reference, evaluation outputs reference, hashes for each. The handover event lands as a chain entry with the §10.21 attribute family. Bidirectional integrity is established across the vendor boundary.

**Kognitos.** No field for cross-vendor model-handover discipline. Field 10 (downstream action) records that an action occurred; it does not address the schema for crossing vendor boundaries.

**Speculation gap.** Under Kognitos, an institution extending chain coverage to a third-party system has no framework anchor for the schema. The institution must invent the handover discipline or borrow from another framework.

**Honest assessment.** For institutions planning chain extension across vendor boundaries (Mercator's planned EHR write-back is the example), the framework cannot supply the schema. The bank's reference spec gives them a starting point; Kognitos cannot. **Severity: medium** — only relevant to extension planning, not to point-in-time audits.

---

### L. Pre-launch backfill discipline — 18-day training-data overlap

**The audit-room question.** *"The sepsis-CDS model was trained on data through the launch date plus 18 days of pre-launch validation. The training-data overlap with the deployment window is itself audit-trail-captured. How does the framework treat this?"*

**TesseraSeal.** §10.20 training-data retention vs deployment-window discipline. The pre-launch backfill 18-day overlap is itself documented in the chain — the model card hash, training-data summary, and evaluation outputs are sealed chain entries. The retention floor (deployment-window + chain-retention horizon) covers post-deployment challenge windows.

**Kognitos.** No field for training-data retention vs deployment-window discipline. Field 5 (model identity and version) records the model version but not the training-data timeline relative to deployment.

**Speculation gap.** Under Kognitos, an institution with disciplined pre-launch backfill (Mercator's pattern) and an institution with no training-data documentation satisfy Field 5 identically if both record the model version. The framework cannot distinguish.

**Honest assessment.** Already covered in Ch01 §10. Mercator's pre-launch backfill is a clean instance of the discipline; Kognitos cannot record it. Severity: medium.

---

## Summary table — Chapter 02 new comparison points

| # | Area | TesseraSeal anchor | Kognitos anchor | Speculation gap | Material impact |
|---|---|---|---|---|---|
| A | Coverage-boundary integrity propagation | §10.19 + §10.13 | No primitive | High | Bifurcated assessment requires prose stapling |
| B | IAM lifecycle integrity (legacy zone) | event_class=iam + §1.4 | Field 3 — identity only | High | Engagement teams may downgrade or elevate based on reading |
| C | Evidentiary substitute discipline | §10.13 + §10.18 | No prescriptive language | Medium-High | Interim remediation guidance missing |
| D | Deployment-intent capture | §4.4.2 | No field | Medium | Canary / rollback discipline invisible |
| E | OpenTelemetry GenAI naming | §4.4 require both gen_ai.request/response.model | Fields 4 + 5 any naming | Medium-High | Silent vendor rerouting undetectable |
| F | Override-record provenance | Chain-bound override entries | Field 11 — disposition only | Medium-High | Override-record tamper-evidence not required |
| G | PHI redaction discipline | §10.22 pre-MAC redaction | No field | High (in healthcare) | HIPAA exposure undetectable |
| H | Consumer-correlation index integrity | §10.23 | Field 12 — generic failure | Medium | Specific remediation language missing |
| I | Storage-tier integrity vs convention | §10.3 + §10.5 | Field 12 — "or WORM equivalent" | Medium-High | CloudTrail-disable-able vs compliance-mode object-lock indistinguishable |
| J | Retention-control discipline | §10.13 + §10.18 | No field | Medium-High | Retention shortening not auditable |
| K | Cross-vendor model-handover schema | §10.21 | No field | Medium | Chain extension across vendors has no schema |
| L | Pre-launch backfill / training-data retention floor | §10.20 | No field | Medium | Same as Ch01 §10 |

**Recurring from Chapter 01 (AI side):** 6 comparison points (timestamp depth, compositional security, IAM lifecycle AI-side, connector-source family forward-looking, reference-verifier distribution, key-rotation) — same severities as Chapter 01.

**New for Chapter 02:** 12 comparison points (A through L above).

**Total comparison points exercised in Chapter 02:** 18.

---

## Bifurcation-specific honest assessment

### What the framework handled adequately

The Kognitos 12-field framework gave the Chapter 02 audit team clean per-system language for every legacy-side failure. Four Findings (legacy AD, CRM, lab pipeline, claims ETL) and two Partials (Mulesoft, Epic) were filed without engagement-team improvisation. The framework's row-list-as-schema genre **is** adequate when the question is "does this specific system pass Field N?" — and the team got concrete diagnostic language for each system the bank operates outside its chain.

### What the framework could not handle

The cross-zone narrative. The way the chain's evidentiary value depends on the integrity of the systems on either side of it. The reconciliation test's 5/5 inference, 4/5 backward, 3/5 forward results are concrete evidence that the chain integrity is sound but the chain's evidentiary value is compromised by the legacy zone's integrity gaps. The framework cannot articulate that compromise. The institution's CISO has to author the cross-zone evidentiary-substitute argument independently.

For a bifurcated deployment, this is a structural limit. The framework provides per-system findings; the institution provides the cross-zone narrative. The two together produce a usable budget request.

### How much speculation the auditor performs

Tallying the new comparison points: 18 points exercised in Chapter 02, of which:
- **6** are recurring from Chapter 01 (AI-side, same severities)
- **12** are new — surfaced specifically by the bifurcation, the healthcare-specific scenarios, and the legacy-side failures

For each new point, the auditor speculates or borrows on top of the framework. The borrowing is from adjacent frameworks (HITRUST for CRM, HIPAA for PHI redaction, FDA SaMD for retention windows). The framework Kognitos provides is a baseline; the auditor's actual report is the framework plus the borrowed remediation discipline plus the prose-stapled cross-zone narrative.

Under FFIEC v1.0b, the equivalent audit would have **zero** speculation points — the spec carries §10.19 coverage maps, §10.13 evidentiary retention, §10.21 cross-vendor handover, §10.22 PHI redaction, and §10.23 correlation-index integrity. Each Chapter 02 finding maps to a specific §-numbered control, and the cross-zone narrative is anchored by §10.19 with prose-stapling avoided.

**Honest measurement: 12 new speculation anchors invented in Chapter 02 vs. zero under the bank's reference spec.** Combined with Chapter 01's 14, the running tally across two chapters is **26 invented anchors** under Kognitos vs. **zero** under the reference spec.

### Convergence on operational outcome

Mercator's CISO knew the legacy zone had integrity gaps; that's why she scoped the engagement. The framework's role was to produce documentation that supports the budget request. Under both frameworks, Patricia gets a usable report — but under Kognitos, she has to write the cross-zone narrative herself. The institution's culture (treating the audit as a budget-supporting artifact, not a compliance-confirmation artifact) is what makes the operational outcomes converge.

The recurring theme across Chapters 01 and 02 is that institutional culture is the load-bearing variable that prevents Kognitos's silences from producing materially weaker operational outcomes. **At an institution without that culture, the framework's silences would produce materially weaker reports.** Kognitos cannot distinguish between these institutions.

---

## Methodological note — building the comparison artifact across chapters

The Chapter 02 comparison file references the Chapter 01 file for recurring comparison points rather than restating in full. This pattern is intended to scale: each subsequent chapter's comparison file should:

1. Reference earlier chapters' comparisons for recurring points (with cross-chapter severity continuity)
2. Identify new comparison points specific to the chapter's scenarios
3. Highlight any new research signals (Chapter 01: deep deployment / speculation gap; Chapter 02: partial deployment / coverage-boundary gap)
4. Maintain the running tally of speculation anchors

By Chapter 22, the expected pattern: approximately 50-80 distinct comparison points across the program, with each chapter contributing 5-15 new points and recurring the rest. The running tally of speculation anchors is the program-level honest signal of framework completeness.
