# Comparative Analysis — Chapter 09 (Sun-Won Cosmetics Group)

*Side-by-side analysis of how the Kognitos 12-field framework and the TesseraSeal / FFIEC chain-of-custody v1.0b spec handle a **multi-jurisdiction K-beauty audit with three regulators reading the same chain through four lenses, two HSMs across the Korea Strait, and a celebrity-controversy lookback litigation framing**. Honest assessment of where the institution drives normative spec evolution and where the framework can only record absences.*

---

## New research signal

Chapter 09 confirms the framework-can-grow vs framework-is-fixed contrast as a stable program-level pattern and introduces three new structural variants.

| New signal | Earlier reference | What is new in Chapter 09 |
|---|---|---|
| **Framework-grows reproducible across consecutive chapters** | Ch08 §10.17 (single instance) | Sun-Won drives TWO §12 change-log entries (§4.4 cross-border family + §4.4.1 sixth event type). NetiVa drove one. Two chapters, three spec sections. The reference spec's living-standard property is now a reproducible signal rather than a one-off. |
| **Cross-jurisdiction joint stakeholder statement** | Ch05 Helmstad joint CCO+CQD (single jurisdiction) | Min-seo (PIPA, Seoul) + Wei-ling (PDPA, Taipei) deliver one statement coordinated across two regulator regimes. Fifth voice pattern after direct boundary-setting, joint-leadership formal request, sharper-dimension addition, framework-substitution recommendation. |
| **Structural-proof vs policy-proof gap recurring** | Ch08 multi-tenant isolation (single instance) | Sun-Won's post-controversy redesign moved biometric-feature exclusion from model-layer policy to ingest-layer pre-MAC redaction. Cryptographic exclusion vs policy exclusion. Two consecutive chapters of structural-proof gaps; now a named pattern. |

This chapter's central novelty: the audit is no longer a one-time observation of framework limitation. The engagement actively *grows the reference spec* via the §12 change-log mechanism. The Kognitos framework, by contrast, sees the same findings but has no mechanism to absorb them.

---

## Recurring from earlier chapters

| Recurring point | Earlier ref | Ch 09 instance |
|---|---|---|
| Compositional security at 128-bit composite | Ch01, Ch06, Ch08 | §1.4 across the Korea Strait; each HSM independently FIPS-current and jurisdiction-blind |
| Field 12 collapses HMAC + Merkle + HSM | Ch01-08 | Now demonstrated across two HSMs in two countries with no per-HSM Kognitos vocabulary |
| §10.16 four-number lag-bound discipline | Ch04, Ch06, Ch07, Ch08 | TW CRM CDC mirror: median 18s / p95 SLO 90s / alert 150s / RTO 5min. **Fifth recurring instance — universal pattern.** |
| §4.4.6 connector_source attribution | Ch04, Ch06, Ch07, Ch08 | Salesforce CDC mirror for TW CRM; per-§4.4.6 attribute family |
| §1.2 epistemic-scope inarticulability | Ch05, Ch06, Ch07 | **New variant: pre-chain era §1.2 (c)** — chain begins on date D; pre-D source-data integrity is legacy-log dependency. Fourth variant of the §1.2 inarticulability. |
| §1.1 + §5.2 litigation-defense posture | Ch06, Ch07 | Celebrity-controversy lookback requires Daubert one-pager + FRE 1001-1004 best-evidence. **Third consecutive chapter with litigation-defense posture as load-bearing.** |
| §10.21 cross-vendor model-handover | Ch02, Ch03, Ch05 | Korean chatbot model from Seoul consultancy under contract triple; `contract_status` discriminator; plural `audit_report_languages` |
| §10.17 HSM partition-ceremony | Ch05, Ch08 (engagement-source) | Now applied across BOTH HSMs (Seoul Sangam-dong KISA-certified + Taipei Chunghwa Telecom CNS 27001 aligned) with `entity_affiliation` per |
| Cross-language CC8.1 discoverability | Ch04, Ch06, Ch08 (Hebrew) | **Korean + Mandarin variant.** Discoverability across two non-Latin scripts. |
| §10.22 pre-MAC redaction discipline | Ch02, Ch05, Ch08 | **Sharpened variant**: structural-proof vs policy-proof; biometric-feature exclusion at ingest, not at model layer |
| §10.15 multi-region invariants | Ch04, Ch08 | **Pattern A + Pattern B coexisting on one chain**. Per-jurisdiction tenants under B; cross-jurisdiction inventory under A. |
| §10.2 operational-events catalog | Ch07, Ch08 | `master_key.generated`, `chain.coverage_map_published`, `connector.lag_observation`, `chain.partition_ceremony_attended` across two HSMs |
| §10.1 IKM-registry uniqueness | Ch04, Ch08 | Daily key-fingerprint reconciliation against IKM registry across both HSMs |
| §10.13 evidentiary retention | Ch01, Ch06 | Standard evidentiary-floor compliance; no new variant this chapter |
| §10.26 reference-verifier distribution | Ch01, Ch05, Ch06, Ch08 | Three-name CC8.1 citation in both Korean and English audit-report languages |
| §10.25 run-resume + tail acquisition | Ch06, Ch08 | SQLite sidecar plus ledger rejoin; no incident-driven instance this engagement |
| §0.5.3 per-role reading paths | First named explicitly | Reference spec's per-role triage tool — four regulators reading four lenses on one chain |

**Severities unchanged** for all recurring points.

---

## New comparison points specific to Chapter 09

### A. Cross-border-transfer attribute family (Finding-001) driven into reference spec

**The audit-room question.** *"The inventory tenant produces chain entries that cross the Korea Strait. Where does the cross-border transfer attribute appear on the entry?"*

**TesseraSeal.** Reference spec §4.4 envelope + §4.4.1 routing schema. Pre-engagement: cross-border attributes lived in routing as ad-hoc fields. Post-engagement: §12 change-log lifts six attributes to spec body — `contract_id`, `contract_version`, `contract_hash_sha256`, `source_jurisdiction`, `destination_jurisdiction`, `lawful_basis_type`. PIPA Section 28 + PDPA Article 8 + GDPR Chapter V all readable from one structured family. ETA Q3 2026.

**Kognitos.** Field 6 (inputs with source attribution) carries the inputs as a single field. It does not carry the lawful-basis-type attribute, nor the source/destination jurisdiction pair, nor the contract triple. Three regulators reading three regimes would each need prose footnotes.

**The under-reporting.** Reference spec captures cross-border-transfer as a six-attribute structured family at the entry level. Kognitos collapses to a single-field carry. The structured family is what makes per-regulator partitioned letters mechanical; absent the family, partitioning requires prose reconstruction per regulator.

**Speculation gap.** The auditor under Kognitos has to construct each regulator's letter from prose annotations. Under the reference spec, the per-§0.5.3 reading path produces partitioned letters mechanically from one chain artifact.

**Structural reason for the gap.** Cross-border discipline assumes attribute-family vocabulary at the chain-entry level. Kognitos's twelve-field schema was designed for single-jurisdiction AI decision recording.

**Honest assessment.** Severity: highest for multi-jurisdiction engagements; the reference spec absorbed the finding via §12 change-log within the audit cycle. Material impact: the institution drove normative spec evolution; under Kognitos, the same finding has no closure path.

---

### B. Chained classifier_output sixth event type (Finding-002) driven into reference spec

**The audit-room question.** *"Five samples. Three recoverable. Two gone. Where does the classifier rationale live in the chain?"*

**TesseraSeal.** Reference spec §4.4.1 routing schema. Pre-engagement: five event types. Post-engagement: §12 change-log adds `audit.routing.classifier_output` as a sixth event type, emitted *before* `audit.routing.attempt`, parent-linked via `parent_run_id` + `parent_seq`. Six new attributes: `classifier_name`, `classifier_version`, `classifier_input_hash`, `classifier_scores`, `classifier_decision`, `classifier_confidence`. The entire pipeline (classifier → router → model) becomes chain-bound. ETA Q3 2026.

**Kognitos.** Field 8 (reasoning) carries the model's reasoning. It does not carry prior-stage classifier scores or parent-linkage between event types. Multi-stage AI pipelines collapse to a single Field 8.

**The under-reporting.** Reference spec captures parent-linked event-type sequences. Kognitos's twelve fields are designed per-decision; the framework cannot represent upstream classifiers that route a decision to a model.

**Speculation gap.** Two of five samples beyond 90-day side-channel detector-log retention have routing rationale gone under any framework. Under the reference spec, the structural fix is chain-binding the classifier output. Under Kognitos, the rationale gap is invisible — Field 8 records the model's reasoning, not the upstream classifier's decision.

**Structural reason for the gap.** Multi-stage AI pipelines are increasingly common (classifier + router + model + post-processor). The reference spec's chained-event-type discipline scales monotonically with pipeline depth. Kognitos's per-decision row-shape does not.

**Honest assessment.** Severity: highest for multi-stage pipelines (any classifier-router-model architecture). Material impact: second §12 change-log entry from this engagement; the reference spec absorbed both findings within the audit cycle.

---

### C. Structural proof vs policy proof: biometric-feature exclusion at ingest

**The audit-room question.** *"Pre-controversy: model-layer feature filter as policy. Post-controversy: ingest-layer pre-MAC redaction as cryptographic exclusion. Where does the structural-proof discipline file?"*

**TesseraSeal.** Reference spec §10.22 pre-MAC SDK redaction + `audit.redaction.disposition` attribute. The redaction happens BEFORE MAC computation. Biometric features (facial features from photographs; voice features from audio) cannot enter the feature pipeline because the redaction is cryptographically anchored at ingest. The MAC integrity of the chain entry is the structural proof that the features were excluded. The institution can defend "feature X cannot enter" as a property of the chain, not as a policy claim.

**Kognitos.** Field 6 (inputs with source attribution) carries the inputs *after* redaction. The framework records what entered the feature pipeline. The framework does not record what was *cryptographically prevented* from entering. The structural-proof property has no slot.

**The under-reporting.** Reference spec captures the discipline that moves exclusion from model-layer policy to ingest-layer cryptography. Kognitos's twelve fields record only what made it through.

**Speculation gap.** For the celebrity-controversy lookback litigation, the defense rests on "the model could not have used biometric features because they were structurally excluded at ingest." Under Kognitos, that defense is a prose claim. Under the reference spec, that defense is a chain property.

**Structural reason for the gap.** The framework's design center is the AI decision (what the model said). Cryptographic exclusion at ingest is a property of the chain mechanism, not of any single decision. Kognitos's row-shape does not admit chain-mechanism properties.

**Honest assessment.** Severity: highest for engagements where institutional discipline has shifted from policy enforcement to cryptographic enforcement. This is the second consecutive chapter where the structural-proof gap surfaces (NetiVa Ch08 on multi-tenant isolation; Sun-Won Ch09 on biometric-feature exclusion). Now a named pattern.

---

### D. Pre-chain era as §1.2 (c) variant

**The audit-room question.** *"The chain begins in March 2025. The litigation lookback covers events before then. Where does Kognitos articulate the chain's start date as an epistemic-scope boundary?"*

**TesseraSeal.** Reference spec §1.2 (c) (chain does not prove input authenticity) + §10.19 (chain-coverage map names the chain's start date) + §12 (change-log records spec evolution). Together: chain begins on date D; pre-D source-data integrity is a property of legacy logs at the ingestion layer; the lookback firm reconstructs pre-D provenance via those legacy logs, not via the chain. Honest scoping in writing.

**Kognitos.** Field 1 (timestamp) on every entry. The framework records that each entry was made at time T. The framework does not articulate "the chain begins on date D" as a structured property of the chain itself.

**Inarticulability gap.** No field, under any reading, articulates the chain's start date as an epistemic-scope boundary. The honest pre-chain framing requires cover-memo prose.

**Speculation gap.** The lookback firm asks: "what does the audit say about events before March 2025?" The auditor's framework-scoped answer is: "the framework has timestamps; it has no slot for the chain's start date as a structural boundary." Reference-spec-borrowing language goes into the cover memo.

**Structural reason for the gap.** The framework was designed at the layer of AI-decision recording, assuming the chain exists. The chain's own bootstrap event — the date it begins — is a meta-property the framework does not model.

**Honest assessment.** Severity: high for any engagement with active litigation lookback to the pre-chain era. Fourth instance of the §1.2 inarticulability (Helmstad post-enrollment correction; PCP sensor mutation; Olmstead civil-rights; Sun-Won pre-chain era).

---

### E. Cross-jurisdiction joint stakeholder statement variant

**The audit-room question.** *"PIPA + PDPA across two countries. Who delivers the on-the-record statement?"*

**TesseraSeal.** Reference spec §0.5.3 per-role reading paths support multi-jurisdiction partitioned letters from one chain. The institution's privacy officers in each jurisdiction can deliver coordinated statements without needing institutional re-coordination.

**Kognitos.** Twelve fields. No per-jurisdiction reading path; each jurisdiction's letter requires prose reconstruction. The framework does not impede joint statements but does not enable them structurally either.

**Speculation gap.** Min-seo (Seoul) + Wei-ling (Taipei) coordinated their statement across the bridge. The joint cross-jurisdiction shape is the new variant. Under Kognitos, the joint statement would carry prose footnotes per regulator regime.

**Structural reason for the gap.** This is not a framework gap per se; it is a stakeholder-pattern observation. The framework does not prevent joint statements; the engagement shape produces them when two privacy regimes read the same chain.

**Honest assessment.** Severity: low for the framework directly; this is a voice-pattern enrichment rather than a coverage gap. Material impact: the program now has five voice patterns (direct, joint-single-jurisdiction, sharper-dimension, framework-substitution, cross-jurisdiction-joint).

---

### F. Pattern A and Pattern B coexisting on one chain

**The audit-room question.** *"How does the chain enforce per-jurisdiction isolation for KR + TW recommendations *and* cross-jurisdiction inventory reconciliation on the same artifact?"*

**TesseraSeal.** Reference spec §10.15 carries five multi-region invariants. Pattern B (per-jurisdiction `tenant_id`, separate HSMs, separate IKMs, separate seal cadences) for the KR + TW recommendation tenants; no co-mingling of key material. Pattern A (single seal region with synchronous-read freshness on `master.cross_region_replication_completed`) for the `sunwon-cross-inventory` tenant. The two patterns coexist because the tenants are different — recommendation tenants are bank-isolated; inventory tenant is shared by design.

**Kognitos.** Field 4 (AI system identity) and Field 6 (inputs). No representation of multi-region invariants. No way to articulate that one tenant's chain entries are isolated by HSM separation while another tenant's chain entries are reconciled across regions under freshness rule.

**Speculation gap.** The auditor under Kognitos reports per-tenant Field 12 PASS without articulating the cross-tenant multi-region discipline that justifies the architecture.

**Structural reason for the gap.** The framework's design center is the decision. Multi-region invariants are properties of the chain-mechanism layer that the framework does not model.

**Honest assessment.** Severity: medium-high for any multi-region engagement; severity: highest where Pattern A and Pattern B coexist (common in multi-jurisdiction SaaS).

---

### G. Lookback-litigation defense file (§1.1 + §1.2 + §5.2)

**The audit-room question.** *"The firm preparing the celebrity-controversy lookback litigation has asked for a Daubert one-pager. Where does Kognitos articulate any of §1.1 (a)-(d)?"*

**TesseraSeal.** Reference spec §1.1 (testability, peer review, known error rate, general acceptance) + §1.2 (epistemic-scope clauses) + §5.2 (best-evidence under FRE 1001-1004). All three articulate the chain's evidentiary posture for litigation. Reference spec is litigation-readable.

**Kognitos.** Twelve fields. Field 12 records "tamper-evident integrity proof exists." The framework has no slot for Daubert four-factor mapping, no slot for best-evidence-under-FRE framing, no slot for the §1.2 epistemic-scope clauses.

**Inarticulability gap.** No field, under any reading. The litigation file requires verbatim borrowing of reference-spec language.

**Speculation gap.** The Daubert one-pager and best-evidence posture have to be reconstructed from prose by an auditor familiar with reference-spec language. The framework cannot supply the litigation file.

**Structural reason for the gap.** The framework was authored for AI-decision recording, not for evidentiary-claim articulation. Daubert and FRE 1001-1004 are evidentiary-claim structures.

**Honest assessment.** Severity: highest for any engagement with active or anticipated litigation. Third consecutive chapter (Ch07 civil-rights / Ch08 nation-state threat coordination / Ch09 celebrity-controversy lookback) where litigation-defense posture is load-bearing.

---

### H. §0.5.3 per-role reading paths from one chain artifact

**The audit-room question.** *"Four regulators (PIPC, PDPC, FSS, FSC) read this audit through four lenses. Where does each one's reading path live?"*

**TesseraSeal.** Reference spec §0.5.3 per-role reading-paths-by-role table. Each role has a designated entry path through the spec's normative material. The same chain artifact produces four partitioned letters because the reading paths route differently.

**Kognitos.** No per-role reading path. Twelve fields read the same way for everyone. Per-regulator letters are reconstructed from prose.

**Speculation gap.** Four regulator letters from one chain requires prose-reconstruction per regulator under Kognitos. Under the reference spec, the partitioning is mechanical.

**Structural reason for the gap.** Per-role reading is a property of the spec's organization, not of the chain entries. Kognitos has no document-organization vocabulary because the framework is not a spec.

**Honest assessment.** Severity: high for multi-regulator engagements (3+ audiences); manifests as auditor labor under Kognitos that is absent under the reference spec.

---

### I. Spec moves to meet posture: second consecutive chapter

**The audit-room question.** *"The reference spec absorbed §10.17 from NetiVa last quarter. It absorbed §4.4 + §4.4.1 from Sun-Won this quarter. What does Kognitos absorb?"*

**TesseraSeal.** Reference spec §12 change-log mechanism. Two consecutive chapters of engagement-source amendments (NetiVa §10.17; Sun-Won §4.4 + §4.4.1). The reference spec is now demonstrably a living standard. The §12 mechanism is the structural feature that enables it.

**Kognitos.** Twelve fields, fixed by framework author. No change-log mechanism. No engagement-source attribution clause. The framework cannot grow under audit pressure.

**Inarticulability gap (meta-shape).** Same shape as Ch08 framework-cannot-grow point, now reproduced across two consecutive chapters. The reproducibility makes the meta-property a stable program-level signal.

**Speculation gap.** Institutions on the leading edge of audit-trail design produce findings that change normative standards. Under Kognitos, those findings have no closure path. The institution either operates under both (Kognitos for cross-vendor; reference spec for substance) or migrates entirely.

**Structural reason for the gap.** A living standard requires governance mechanism for evolution. The reference spec has §12. Kognitos has none.

**Honest assessment.** Severity: highest for any institution operating at the leading edge of audit-trail architecture. Material impact: the structural difference predicts that the reference spec will continue to evolve while the Kognitos framework remains at twelve fixed fields.

---

## Summary table

| # | Area | TesseraSeal anchor | Kognitos anchor | Speculation gap | Material impact |
|---|---|---|---|---|---|
| A | Cross-border-transfer attribute family | §4.4 + §4.4.1 (post-engagement) + §12 | Field 6 single carry | Under-reporting (highest) | Engagement drove spec amendment; framework records absence |
| B | Chained classifier_output sixth event type | §4.4.1 (post-engagement) + §12 + parent-linkage | Field 8 collapses pipeline | Under-reporting (highest) | Second §12 entry from this engagement |
| C | Structural-proof biometric-feature exclusion | §10.22 pre-MAC + `audit.redaction.disposition` | Field 6 records what entered | Under-reporting (highest) | Lookback defense rests on cryptographic exclusion |
| D | Pre-chain era §1.2 (c) variant | §1.2 (c) + §10.19 + §12 | Field 1 timestamp inadequate | Inarticulability | Fourth §1.2 variant; honest scoping requires prose |
| E | Cross-jurisdiction joint statement variant | §0.5.3 per-role reading paths | None (voice-pattern observation) | Voice-pattern enrichment | Fifth stakeholder voice pattern in program |
| F | Pattern A + Pattern B coexisting | §10.15 invariants + freshness rule | Field 4 + Field 6 inadequate | Speculation | Multi-region discipline invisible |
| G | Lookback-litigation defense file | §1.1 + §1.2 + §5.2 + FRE 1001-1004 | Field 12 inadequate | Inarticulability (highest) | Third consecutive litigation-defense gap |
| H | Per-role reading paths from one chain | §0.5.3 + per-regulator partitioning | No per-role reading | Speculation | Auditor labor under Kognitos absent under spec |
| I | Spec moves to meet posture (2 consecutive chapters) | §12 change-log mechanism | Framework cannot grow | Inarticulability (meta, reproducible) | Reference spec is living standard; framework is not |

**Plus recurring from Chapters 01-08:** 17 comparison points unchanged.

**Total comparison points exercised in Chapter 09:** 26 (9 new + 17 recurring).

**Of which inarticulabilities (new this chapter):** 1 (point D — pre-chain era §1.2 variant; reproducible meta-shape in I; litigation-defense in G).

**Of which under-reportings (new this chapter):** 2 (point A cross-border attribute family; point B classifier_output event type) — both elevated to spec body via §12 change-log within the audit cycle.

---

## Honest assessment — engagement-scoped only

### What Sun-Won uniquely contributes

The engagement is the first multi-jurisdiction audit in the program — three regulators reading the same chain through four lenses, two HSMs in two countries, a split audit team on a video bridge. Three structurally new contributions: the framework-grows-vs-fixed contrast is now reproducible across consecutive chapters (NetiVa + Sun-Won = three spec amendments); the cross-jurisdiction joint stakeholder-statement variant adds a fifth voice pattern to the program; the structural-proof-vs-policy-proof gap is now a named pattern after two consecutive instances.

### The two §12 change-log entries

This engagement drove two normative additions to the reference spec. The cross-border-transfer attribute family lifts to §4.4 spec body — `contract_id`, `contract_version`, `contract_hash_sha256`, `source_jurisdiction`, `destination_jurisdiction`, `lawful_basis_type`. The chained classifier_output sixth event type lifts to §4.4.1 spec body — `classifier_name`, `classifier_version`, `classifier_input_hash`, `classifier_scores`, `classifier_decision`, `classifier_confidence`, parent-linked to `audit.routing.attempt` via `parent_run_id` + `parent_seq`. Both land before end of Q3 2026 alongside six-week legal review and two-week chain-config remediation. The institution drove spec evolution; the framework recorded two findings it could not file.

### Stakeholder statement: Min-seo Kang + Wei-ling Tsai (joint cross-jurisdiction)

> *We are the privacy officers for Sun-Won Cosmetics Group across two jurisdictions. We have selected the Kognitos framework for cross-vendor comparability on the audit-deliverable cover, and we have heard the audit team walk the engagement under that framework with discipline. We have also heard, in their running notes, that the framework cannot carry the cross-border-transfer attribute family in a structured way; that it cannot carry the chained classifier_output event type in a structured way; that it cannot carry the §1.2 (c) pre-chain era boundary that the lookback litigation depends on; that it cannot carry the §1.1 Daubert four-factor mapping that the firm preparing the litigation has asked for in writing.*
>
> *Our institution has surfaced two findings in this engagement that the reference specification will be absorbing into normative spec body via the §12 change-log mechanism. The cross-border-transfer attribute family lifts to §4.4 spec body. The chained classifier_output sixth event type lifts to §4.4.1 spec body. Both land before the end of Q3, alongside our six-week legal review of the contract bindings and two-week chain-config remediation. The reference spec is moving to meet our posture. The Kognitos framework cannot move. We want that distinction on the record.*
>
> *We are asking the standards-body reviewer to credit Sun-Won Cosmetics Group as the engagement source for both §4.4 and §4.4.1 amendments per the §12 change-log practice. We are asking our audit team to name, in the cover memo, that the framework we selected for cross-vendor comparability did not carry the engagement's most consequential findings. We will recommend that future multi-jurisdiction privacy audits across PIPA, PDPA, GDPR, and any analog regime be delivered against the reference specification, with Kognitos retained only for the cross-vendor comparison summary table. The audit team's running notes will be the record of what the framework missed. On the record. Both jurisdictions.*

This is the fifth-and-sixth on-the-record statements counted by speaker, but the *fifth statement* counted by occasion. It introduces a new voice pattern (cross-jurisdiction joint) and is the second framework-substitution recommendation (after Pankaj at NetiVa), now applied to multi-jurisdiction privacy audits as an engagement class.

### Engagement-specific consequences

For Sun-Won: ten Confirmations + the pre-chain era confirmation-by-spec; two Findings driven into spec body via §12; one tracking Finding closed by the second engagement-source amendment; bundle remediation Q3 2026 (six weeks legal + two weeks chain config).

For the lookback litigation firm: the §1.2 + §10.19 + §12 pre-chain era framing arrives in writing; the §10.22 pre-MAC structural-proof argument is the post-controversy defense backbone; the §1.1 + §5.2 Daubert + best-evidence file is reference-spec-borrowed in the cover memo.

For the standards-body reviewer: two §12 change-log entries credited to Sun-Won Cosmetics Group. Reference spec moves from PRD-1 to PRD-1 + Sun-Won amendments by end of Q3 2026.

For the four regulators: PIPC, PDPC, FSS, FSC each receive a per-regulator partitioned letter from one chain via §0.5.3 reading paths. Same answers framed for each lens.

---

*Program-level running tally and editorial signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
