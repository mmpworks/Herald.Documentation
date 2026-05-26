# Comparative Analysis — Chapter 07 (Olmstead University)

*Side-by-side analysis of how the Kognitos 12-field framework and the TesseraSeal / FFIEC chain-of-custody v1.0b spec handle a **multi-regulator higher-ed audit** anchored on a civil-rights threat letter, with a deliverable that must partition across five regulator audiences. Honest assessment of where the chain captures the structured override and the framework's silences become the litigation-defense exposure on the free-text rationale gap.*

---

## The new research signal — multi-regulator partitioning and the structured-vs-prose gap

Chapter 07 surfaces two patterns the program has not directly named before:

1. **Multi-regulator partitioning** — the same engagement produces five distinct regulator-shaped deliverables (FERPA, GLBA, NIH research-integrity, HHS OCR informal, civil-rights litigation-defense addendum). The reference spec's §10.19 chain-coverage map is the partitioning tool — the same map answers each regulator's coverage question from a different read. Kognitos has no primitive for multi-audience partitioning of a single chain.

2. **Structured-capture vs prose-capture distinction** — the chain captures the structured override (reason code + reviewer ID + parent linkage); the human's prose rationale lives downstream in Slate, mutable, and was gone in 2/5 sampled suspect-class cases. Under Kognitos's Field 11, "human review" is satisfied — the decision and reviewer are captured. The framework has no row for the location, retention discipline, or recovery posture of the reviewer's prose reasoning. This is a new instance of under-reporting with a litigation-shaped consequence.

Both patterns are likely to recur — Chapter 13 (Saraswati Microfinance) and Chapter 18 (Argent Vector Defense) are likely candidates for multi-regulator partitioning; any engagement with human-reviewer prose-reasoning workflows (clinical override, lending decisions, defense-acquisition decisions) is a candidate for the structured-vs-prose under-reporting.

---

## Recurring from Chapters 01-06

| Recurring point | Earlier ref | Ch07 instance |
|---|---|---|
| Compositional security | Ch01 §4 | Admissions-AI chain (HMAC + Merkle + Ed25519 + HSM + §1.4) |
| Coverage-boundary primitive | Ch02 §A, Ch03, Ch06 | Four-category map; new dimension is multi-regulator partitioning |
| §1.2 epistemic-scope inarticulability | Ch05 §A, Ch06 §B | **Third instance — civil-rights litigation variant** |
| §1.1 Daubert four-factor mapping | Ch06 §C | Litigation-defense memo grounding |
| Deployment-intent capture | Ch02 §D, Ch05 §F | `production` with `policy_version=olm-admit-2025q4-consent` |
| OpenTelemetry GenAI naming | Ch02 §E | gen_ai.request/response.model on admissions screening |
| Pre-MAC redaction + disposition | Ch02 §G, Ch05 §E | FERPA `policy_id`/`policy_version` bound under MAC |
| Cross-vendor model-handover | Ch02 §K, Ch03 §H, Ch05 §I | Fairness-audit vendor contract triple (§10.21) |
| Three-name CC8.1 verifier citation | Ch05 §C | Recurring |
| Algorithm agility (long-retention) | Ch05 §D | Not exercised this engagement |
| Witness-mode (PASS-STRUCTURALLY) | Ch05 §B | Recurring; new context — federal-litigation discovery |
| Training-data retention floor | Ch01 §10 | 540-day floor (18-month deployment + 90-day buffer) |
| Entity succession | Ch01 §11, Ch04 | §10.17 dual-signatures with `entity_affiliation` |
| DR rejoin three-place tail | Ch06 §E | Recurring posture, not exercised in audit |
| §4.4.6 `audit.connector_source.*` family | Ch01 §6, Ch06 §H | **Slate webhook structural form; central to Phase 2 closure** |
| §10.18 runbook discipline | Ch04 §E, Ch06 | Recurring |

---

## New comparison points specific to Chapter 07

Nine new comparison points emerged from this engagement.

---

### A. §10.19 chain-coverage map as multi-regulator partitioning tool

**The audit-room question.** *"FERPA, GLBA, NIH, HIPAA-informal, civil-rights addendum — five regulator audiences read the same chain. How does the framework partition the deliverable so each audience reads only what concerns them?"*

**TesseraSeal.** §10.19 chain-coverage map carries a cryptographic version anchor and per-section labels that bind to each regulatory audience. The same map answers FERPA's coverage question (admissions ledger + advancement + medical-center external-artifact bridge), GLBA's coverage question (Banner SIS + financial-aid stack), NIH's coverage question (per-lab enumeration), HIPAA's coverage question (medical-center hash-anchor only), and the civil-rights addendum's coverage question (override-rationale free-text boundary). One artifact, five reads.

**Kognitos.** No primitive for multi-audience partitioning. The 12 fields apply uniformly per chain entry; the framework cannot articulate which fields are load-bearing for which regulator.

**Speculation gap.** Under Kognitos, the auditor produces five separate deliverables by manual partitioning — restating the framework's results five times against five regulator-shaped lenses. The structural unification the §10.19 map provides is invented per engagement.

**Honest assessment.** For institutions facing concurrent multi-regulator audiences (universities, multi-jurisdiction financial institutions, healthcare systems with research arms, defense contractors), the partitioning primitive is operationally significant. The reference spec supplies one artifact-five-reads; Kognitos requires five-artifacts-restated. **Severity: high for multi-regulator institutions.**

---

### B. Structured override capture vs free-text rationale prose

**The audit-room question.** *"The chain captures `STRENGTH_OF_RECOMMENDATIONS` as the reason code for the override. The reviewer's prose explaining what about the recommendations was strong is in Slate, mutable. On 2/5 suspect-class samples the prose is gone. Field 11 says human review is satisfied. Where does the rationale-gap finding live?"*

**TesseraSeal.** §10.19 chain-coverage map names the free-text rationale field as an external-evidentiary boundary. §4.4.6 `audit.connector_source.*` family is the structural form to chain-capture the rationale via a Slate webhook with stable-`run_id` discipline tied to the Slate applicant record ID. §10.16 four-number lag posture (median / p95 SLO / alert / RTO) bounds the webhook capture latency. Together, the three sections give the institution the structural path to close the gap (Phase 2, 12 months) and the language to describe the gap until closed.

**Kognitos.** Field 11 (human review) is satisfied — the override decision, reviewer ID, and reason code are chain-bound. The framework has no row for the location of the prose rationale, its retention discipline, or its recovery posture. An institution with full §4.4.6 + §10.16 webhook capture and an institution with Slate-only rationale capture satisfy Field 11 identically.

**The under-reporting.** Under FFIEC, the rationale-gap is a §10.19 coverage-map Gap with a Phase 2 closure path. Under Kognitos, the finding is invisible — Field 11 records "human review" as satisfied because the structured override is captured. The institution catches this internally because they were on a consent-to-resolve framework that required the §10.19 discipline; under Kognitos as sole framework, the rationale-gap is unfileable.

**Litigation-shaped consequence.** The two gone-rationale cases were exactly the threat letter's suspect class — override-down on AI-would-admit applicants. The civil-rights firm will see the chain entries showing `reason_code=FIT_AND_CULTURE` and have no prose to interrogate. The institution's litigation defense relies on the reviewer's deposition reading of the structured reason code, not on the contemporaneous prose. Under Kognitos, this exposure is invisible.

**Honest assessment.** For institutions where the human-reviewer prose-reasoning is downstream of chain capture and load-bearing for litigation (lending decisions, clinical overrides, admissions overrides, defense-acquisition decisions), the structured-vs-prose distinction is operationally significant. The reference spec articulates the boundary; Kognitos does not. **Severity: highest for institutions with active civil-rights / litigation exposure on reviewer-prose dependencies; third under-reporting in the program.**

---

### C. §4.4.5 underwriting-features-by-analogy (`feature_vector_hash`, `feature_categories`, `protected_class_proxy_flags`)

**The audit-room question.** *"The chain emits feature_vector_hash, feature_categories (transcript / recommendations / essays / test-indicators), and protected_class_proxy_flags on every screening entry. How does the framework articulate this disparate-impact-prevention discipline?"*

**TesseraSeal.** §4.4.5 normates the underwriting-features-by-analogy attribute family for AI screening contexts where disparate-impact concerns apply. The attributes bind under per-event MAC. A downstream auditor can sample the chain and verify (a) the feature set categories are documented and unchanged across the deployment window, (b) the protected_class_proxy_flags posture is the institution's stated posture, and (c) the feature_vector_hash bounds the model's view of the application without leaking application content.

**Kognitos.** Field 6 (inputs with source attribution) addresses source attribution generically. The framework does not articulate feature-categorization or proxy-flag discipline.

**Speculation gap.** Under Kognitos, an institution operating with full §4.4.5 attribution and one operating bare feature passthrough satisfy Field 6 identically. The disparate-impact-prevention posture is invisible.

**Honest assessment.** For institutions facing disparate-impact regulatory scrutiny (lending under ECOA, admissions under Title VI/VII, hiring under EEOC, housing under Fair Housing Act), §4.4.5 is the chain-bound discipline that anchors the defense. Kognitos does not articulate it. **Severity: high for disparate-impact-regulated institutions.**

---

### D. §10.11.1 ECOA adverse-action reasons schema bound under MAC

**The audit-room question.** *"The override decision carries reason_code from a controlled vocabulary — `STRENGTH_OF_RECOMMENDATIONS`, `FIT_AND_CULTURE`, `INCOMPLETE_APPLICATION`, etc. How does the framework articulate the controlled-vocabulary discipline?"*

**TesseraSeal.** §10.11.1 normates the ECOA adverse-action reasons schema applied by analogy to non-lending decisions. The controlled vocabulary is bound under per-event MAC; the institution documents the vocabulary in the §10.18 runbook. Downstream auditors verify that reason codes on the chain belong to the documented vocabulary and that the institution's reason-code distribution across protected-class proxies aligns with the disparate-impact posture stated in §4.4.5.

**Kognitos.** No field for adverse-action reasons schema or controlled-vocabulary discipline. The chain can carry a `reason` attribute on Field 10 or Field 11, but the framework does not normate the vocabulary discipline.

**Speculation gap.** Under Kognitos, an institution operating a documented controlled vocabulary and one operating free-form reason text satisfy the framework identically. The vocabulary-discipline posture is invisible.

**Honest assessment.** For institutions making adverse decisions under regulated frameworks (ECOA lending, ADA accommodations, EEOC hiring, FERPA admissions), the controlled-vocabulary discipline is the structural anchor for downstream forensic analysis. Kognitos does not articulate it. **Severity: high for adverse-decision regulated institutions.**

---

### E. §10.16 four-number lag posture (median / p95 SLO / alert / RTO)

**The audit-room question.** *"The Slate webhook lag posture has four numbers — median 4.2s, p95 SLO 30s, alert at 60s, RTO 15 minutes. How does the framework articulate the lag bound?"*

**TesseraSeal.** §10.16 normates the four-number lag posture for cross-system webhook capture. Each number bounds a different operational property — median is the steady-state; p95 SLO is the contractual bound; alert threshold is the operational-detection bound; RTO is the recovery-time bound. Together they give the institution a measurable contract with the webhook source and downstream verifiers a clean failure-mode framework.

**Kognitos.** No field for lag bounds, SLO posture, or RTO discipline. Field 12 (tamper-evident integrity proof) records that the integrity proof exists; the framework does not address the cadence or latency of the chain capture.

**Speculation gap.** Under Kognitos, an institution operating a 4-second median Slate webhook and one operating a 6-hour-delayed nightly batch satisfy Field 12 identically.

**Honest assessment.** For institutions with cross-system webhook capture (Slate webhook here; OMS work-order coupling at PCP; CIS/Salesforce at Atrio), the lag-bound discipline is operationally significant. The reference spec gives a four-number contract; Kognitos has no row. **Severity: medium-high for institutions with webhook-coupled chain capture.**

---

### F. §10.19 + `audit.external_artifact.*` cross-entity hash-anchor evidence

**The audit-room question.** *"The affiliated medical center has its own HIPAA-protected audit infrastructure. The university chain has no extension into the medical-center zone. How does the framework articulate cross-entity evidentiary linkage without consuming PHI?"*

**TesseraSeal.** §10.19 chain-coverage map extension via `audit.external_artifact.*` attributes: the university chain emits hash-anchor events that reference medical-center artifacts (by hash) without consuming PHI content. The medical center retains the artifacts in its own audit infrastructure; the university chain proves what hash was witnessed at what time. Downstream auditors can verify the linkage without crossing the PHI boundary.

**Kognitos.** No field for cross-entity hash-anchor evidence. Field 6 (inputs with source attribution) addresses source attribution per-event; the framework does not articulate hash-anchor evidence patterns that span affiliated entities.

**Speculation gap.** Under Kognitos, an institution with cross-entity hash-anchor discipline and one with bare "we work with the medical center" attribution satisfy Field 6 identically. The cross-entity evidentiary linkage is invisible.

**Honest assessment.** For institutions with affiliated entities under different regulatory regimes (universities + medical centers; banks + insurance affiliates; supply-chain with subsidiaries), the cross-entity hash-anchor pattern is the operative discipline. The reference spec gives it; Kognitos does not. **Severity: medium-high for institutions with affiliated-entity audit boundaries.**

---

### G. §4.4.1 routing schema with consent-to-resolve binding (single-provider; A/B forbidden)

**The audit-room question.** *"The consent-to-resolve framework forbids A/B testing on the admissions screening model — the civil-rights firm required single-provider single-version single-region throughout the consent window. How does the framework articulate the consent-binding?"*

**TesseraSeal.** §4.4.1 routing schema with deployment-intent enum (`production`) and a CC8.1 description that explicitly names "single-version single-region; A/B testing prohibited under consent-to-resolve framework with civil-rights firm." The schema is chain-bound — every screening entry carries `audit.deployment.intent=production` and `audit.deployment.policy_version=olm-admit-2025q4-consent`. The consent-framework binding is mechanically verifiable.

**Kognitos.** §4.4.2 deployment-intent enum is exercised (recurring from Ch02), but Kognitos has no field for routing-schema posture or for legal-framework binding to deployment-intent.

**Speculation gap.** Under Kognitos, an institution operating under a consent framework forbidding A/B and one operating with active A/B testing satisfy Field 5 (AI system identity / version) identically.

**Honest assessment.** For institutions operating under court orders, consent decrees, or regulatory consent agreements that constrain deployment posture, the framework-binding to deployment-intent is operationally significant. The reference spec gives it; Kognitos does not. **Severity: high for consent-constrained institutions.**

---

### H. §10.2 operational events (`chain.coverage_map_published`, `master_key.rotated`, `credential.rotated`)

**The audit-room question.** *"The chain emits operational events — coverage-map publication, master-key rotation, credential rotation. These are not inference events. How does the framework articulate operational-event chain capture?"*

**TesseraSeal.** §10.2 normates operational events that are chained alongside inference events. The events use the same chain substrate (HMAC + Merkle + signature) but carry operational metadata rather than inference content. Examples: `chain.coverage_map_published` (versioned coverage-map publication); `master_key.rotated` (HSM rotation); `credential.rotated` (per-tenant credential rotation). Downstream auditors verify the operational history via the chain.

**Kognitos.** No field for operational events outside the inference path. The 12 fields are inference-shaped.

**Speculation gap.** Under Kognitos, the institution's operational history (key rotations, coverage-map publications, credential rotations) lives in separate logs outside the chain. An auditor reconstructing operational history must trust multiple disjoint sources.

**Honest assessment.** For institutions with mature operational-discipline (PCI / SOC 2 / NIST 800-53 / FedRAMP audiences), chained operational events are the unified-source-of-truth pattern. The reference spec gives it; Kognitos does not. **Severity: medium-high for operationally-mature regulated institutions.**

---

### I. §10.23 Shape 1 consumer-correlation index (student-ID derived; chain-anchored)

**The audit-room question.** *"A student requests their own audit-trail subset under FERPA. The chain produces this via a student-ID derived correlation index. How does the framework articulate the consumer-disclosure protocol?"*

**TesseraSeal.** §10.23 Shape 1 consumer-correlation index: an institution-derived per-consumer hash (here, derived from student ID) is chain-anchored on a daily attestation event. When a student requests their subset, the institution produces the chain entries that hash-match the student's correlation index, with the daily attestation as integrity anchor. The protocol is FERPA-compliant (no PHI / FERPA-protected content in the correlation hash) and downstream-verifiable.

**Kognitos.** Recurring from Ch04 §H (§1033 per-customer disclosure). The framework has no field for consumer-disclosure protocols; the §10.23 Shape 1 pattern is the specific FERPA-shaped instance.

**Honest assessment.** Recurring from Ch04 with a new operational instance (FERPA student records rather than CFPB §1033 consumer financial data). The structural pattern is identical; the regulatory frame differs. **Severity: medium-high for institutions with consumer-disclosure-request workflows under any regulatory frame.**

---

## Summary table — Chapter 07 new comparison points

| # | Area | TesseraSeal anchor | Kognitos anchor | Speculation gap | Material impact |
|---|---|---|---|---|---|
| A | §10.19 chain-coverage map as multi-regulator partitioning tool | §10.19 | No primitive | High (multi-regulator) | Five-deliverable manual restating |
| B | **Structured override vs free-text rationale — under-reporting** | §10.19 + §4.4.6 + §10.16 | **Field 11 satisfied; no row for prose** | **Under-reporting** | Threat-letter suspect-class rationale gap invisible |
| C | §4.4.5 underwriting-features-by-analogy | §4.4.5 | Field 6 generic | High (disparate-impact) | Proxy-flag posture invisible |
| D | §10.11.1 ECOA adverse-action reasons under MAC | §10.11.1 | No field | High (adverse-decision regulated) | Controlled-vocabulary discipline invisible |
| E | §10.16 four-number lag posture | §10.16 | No field | Medium-High | Webhook lag bounds invisible |
| F | §10.19 + `audit.external_artifact.*` cross-entity anchor | §10.19 extension | No field | Medium-High | Affiliated-entity linkage invisible |
| G | §4.4.1 routing schema + consent-framework binding | §4.4.1 + §4.4.2 | No field | High (consent-constrained) | Court-order binding to deployment invisible |
| H | §10.2 operational events on the chain | §10.2 | No field | Medium-High | Operational history disjoint |
| I | §10.23 Shape 1 student-ID consumer-correlation index | §10.23 | No field | Medium-High | Recurring (FERPA variant of Ch04 §1033) |

**Plus recurring from Chapters 01-06:** 16 comparison points unchanged.

**Total comparison points exercised in Chapter 07:** 25.

**Of which inarticulabilities: 1** (§1.2 (a)-(e) for Friday memo; third instance — civil-rights litigation variant).
**Of which under-reportings: 1** (structured override vs prose rationale; third instance).

---

## Honest assessment — Chapter 07's unique contribution

### Multi-regulator partitioning is a structural primitive the framework lacks

Olmstead's engagement produced five distinct regulator-shaped deliverables from one chain. The reference spec's §10.19 chain-coverage map carried the partitioning load — one map, five reads, each regulator's coverage question answered from the same artifact. Under Kognitos, the partitioning is done by hand. The framework provides no vocabulary for "this section of the chain is FERPA-load-bearing; this section is GLBA-load-bearing; this is the civil-rights addendum."

This is the first chapter where a single chain had to answer five concurrent regulatory audiences. Future chapters with similar multi-regulator shape (defense + commercial; tax + financial; multi-jurisdiction fintech) will likely reinforce the pattern.

### The structured-vs-prose under-reporting is the litigation exposure

The two gone-rationale cases are the most operationally consequential under-reporting the program has surfaced. The threat letter named override-down decisions on applicants whose AI score would have admitted them. The reconciliation sample anchored on exactly that class. Two of five had the reviewer's prose rationale unrecoverable in Slate.

Under Kognitos, Field 11 is satisfied for all five samples — the structured override (reason code + reviewer + parent linkage) is on the chain. The framework cannot articulate that the prose rationale is downstream and mutable. An institution operating under Kognitos as sole framework, without the consent-to-resolve discipline that drove the §10.19 map, would have shipped the audit deliverable showing zero findings against the suspect-class decisions.

The civil-rights firm would have read that deliverable, requested the prose rationales, and learned in discovery that two were unrecoverable. The litigation defense would have collapsed in the courtroom rather than in the audit room.

### The General Counsel's on-the-record statement

Holland Berge added a fourth dimension to the explicit-attribution pattern: institutions operating under consent-to-resolve frameworks with active civil-rights litigation exposure. The cumulative pattern across chapters is now:

- **Ch04 (Veronika, Atrio CISO)** — multi-tenant BaaS platforms
- **Ch05 (Helmstad CCO + CQD jointly)** — clinical-trial readiness pre-FDA-inspection
- **Ch06 (Soren Kovach, PCP CISO)** — any utility with public-safety stakes
- **Ch07 (Holland Berge, Olmstead GC)** — any institution under consent-to-resolve framework with active civil-rights litigation exposure

Four CISO-or-equivalent statements across four consecutive chapters. The cadence is engagement-driven; the stakes are different each time; the framework's silences are structurally the same.

### What this changes about the program-level argument

By Chapter 07, the pattern is no longer just "the framework is shallow." It is: **the framework's row-shape is structurally inadequate for any engagement where (a) multiple regulators read the same chain, (b) human-reviewer prose-reasoning is load-bearing for litigation defense, or (c) coverage boundaries map onto regulator-named suspect classes.** Each of these is a recurring engagement class in the program; each one produces framework-side findings that the institution can only recover via cover-memo borrowing from the reference spec.

---

*Running counts and program-level signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
