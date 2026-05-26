# Comparative Analysis — Chapter 11 (Eberhardt Werkstoffe × Lumière AI)

*Side-by-side analysis of how the Kognitos 12-field framework and the TesseraSeal / FFIEC chain-of-custody v1.0b spec handle a **joint cross-vendor pre-audit ahead of EU AI Act enforcement** with five readers (EU AI Act conformity assessor + BSI/TISAX + LfDI/CNIL joint GDPR + OEM vendor-management + Big-Four assurance) reading two independent chains joined at a §10.21 cross-vendor model-handover seam across the Germany-France organizational boundary. Honest assessment of where cross-vendor zero-trust composition sits as the second substrate-class inarticulability and where the framework-grows-vs-fixed contrast becomes four-chapter-consecutive reproducible.*

---

## New research signal — cross-vendor zero-trust composition

Eberhardt × Lumière is the first engagement in the program where two independent companies operate two independent chains and the load-bearing structural feature is the byte-equal hash join at the cross-vendor seam between them. Each chain passes §7 verifier in isolation. The joint integrity claim — that the model deployed at Eberhardt was the model built by Lumière, that the model card was the model card at handover, that the fairness audit was the fairness audit at handover — is produced by *composition* of the two chains, not by either alone. Neither party has to trust the other; the byte-equal hash join is the trust-producing step.

| Dimension | Within-vendor composition (Ch08 NetiVa baseline) | Cross-vendor composition (Ch11 Eberhardt × Lumière) |
|---|---|---|
| Composition layers | Per-event HMAC + daily Merkle seal + HSM signature | All of NetiVa's + §10.21 cross-vendor anchor across organizational boundary |
| HSM roots | One (per-tenant) | Two (per-company, two jurisdictions) |
| Trust origin | Vendor's substrate trust | Byte-equal hash join (neither party trusts the other) |
| §1.4 articulation | Three-layer composite at 128 bits within one chain | Same composite extended across organizational boundary |
| Kognitos articulation | Field 12 names "proof exists" without the why | Field 12 names two separate proofs without the join or what it adds |

What is new: the byte-equal hash join at §10.21 produces trust where no chain alone produces it. This sharpens NetiVa's §1.4 substrate inarticulability from within-vendor into cross-vendor.

---

## Recurring from earlier chapters

| Recurring point | Earlier ref | Ch11 instance |
|---|---|---|
| §1.2 epistemic-scope inarticulability | Ch02, Ch05, Ch06, Ch07, Ch08, Ch09, Ch10 | Fairness-audit-vs-model-fairness variant; 8th appearance |
| §1.4 substrate-class inarticulability | Ch08 (NetiVa within-vendor) | First cross-vendor variant; 2nd substrate-class instance |
| Compositional security (§1.4) extended across boundary | Ch08 | Now extended across organizational boundary via §10.21 |
| §10.21 cross-vendor model-handover | Ch02, Ch03, Ch05, Ch09 | First explicit byte-equal-hash-join exercise; engagement-source amendment for plural-array `audit_report_languages` |
| Field 2 actor identity well-formed | Ch01 forward | Both chains; gap is at the seam, not at the named actor |
| Field 12 well-formed for chain's own seal | Ch01 forward | Two independent HSM-rooted daily seals; AWS Frankfurt + OVHcloud Roubaix |
| §10.18 CC8.1 + cross-language runbook discoverability | Ch04, Ch06, Ch08, Ch09, Ch10 | German + French + English; fourth cross-language variant |
| §10.15 multi-region resilience | Ch04, Ch06, Ch08, Ch09, Ch10 | Pattern A on each side; AWS Frankfurt + OVHcloud Roubaix region-pinned |
| §4.4.6 SaaS-edge connector source | Ch01, Ch06, Ch07, Ch08, Ch09, Ch10 | Recurring; not load-bearing here |
| §10.16 four-number lag | Ch04, Ch06, Ch07, Ch08, Ch09, Ch10 | Recurring; not the focal under-reporting |
| §4.4.1 cross-border-transfer attribute family | Ch08 (US↔IL), Ch09 (KR↔TW), Ch10 (KR↔TW image transfer) | First within-EU instance (DE↔FR SHOULD per §10.21 worked-example paragraph) |
| §12 change-log spec growth | Ch08 (§10.17), Ch09 (§4.4 + §4.4.1), Ch10 (§10.19 + `audit.external_artifact.*`) | Fourth consecutive chapter; Ch11 drives §10.20 + §10.21 amendments — 7 engagement-source amendments across 4 chapters |
| Framework-grows-vs-fixed meta-property | Ch08, Ch09, Ch10 | Now four-chapter-consecutive reproducible |
| Framework-substitution stakeholder recommendation | Ch08 (Pankaj), Ch09 (Min-seo + Wei-ling), Ch10 (Patrick + Naomi) | Heinrich + Sébastien cross-vendor partnership joint; fourth recommendation |
| Cross-location / cross-boundary multi-leg trace | Ch10 (14-min, 4 services, 1 institution) | Ch11 (~15-min, 7 legs across 2 institutions joined at §10.21 seam) |

**Severities unchanged.** No re-litigation.

---

## New comparison points specific to this chapter

### A. Cross-vendor zero-trust composition across organizational boundary (§1.4 variant)

**The audit-room question.** *"At noon we ran the byte-equal compare of three SHA-256s across two terminals — Eberhardt's chain row and Lumière's chain row. All three matched byte-for-byte. The joint integrity claim is produced by the composition. Where in Kognitos do we say that the composition is what produces trust?"*

**TesseraSeal.** §1.4 (compositional security) extended across §10.21 (cross-vendor model-handover schema). Per-event HMAC + daily Merkle seal + HSM signature on each side, plus the §10.21 byte-equal-hash-join across the organizational boundary, compose to a 128-bit composite integrity claim per NIST SP 800-175B. The composition is structural: neither party is the source of trust; the byte-equal hash join is the trust-producing step.

**Kognitos.** Field 12 (tamper-evident integrity proof) names one party's seal. There is no field that names the second party's seal in composition with the first. There is no field that names the join. There is no field that names what the join adds.

**Inarticulability gap.** The framework cannot articulate composition under any reading. Field 12 is per-event; it has no aggregation surface. Speculating the second chain's seal into a Field 8 (reasoning) annotation falsifies the structural relationship — the second seal is not the *reasoning* for the first seal; it is the second-half-of-the-composition that produces the joint integrity claim.

**Structural reason for the gap.** Kognitos's fixed-row architecture assumes the chain is the source of trust. The reference spec's compositional-security argument assumes the chain is *one component* of trust, with composition across cryptographic layers (within-vendor) or across organizational boundaries (cross-vendor) producing trust that no single component produces. Kognitos has no row shape for *composition*.

**Honest assessment.** Severity: highest for any institution where the load-bearing structural feature is a cross-vendor seam, supply-chain composition, multi-party integrity claim, or zero-trust architecture. Recurs from Ch08 (NetiVa within-vendor §1.4) and sharpens into cross-vendor variant. Second substrate-class inarticulability instance.

### B. Training-data retention floor bound to consuming-chain deployment window

**The audit-room question.** *"Lumière retains training data 90 days from training completion under GDPR Article 5(1)(c) minimization. Eberhardt deploys models 9-18 months in production before retrain cycle. At month 12 of deployment, the training corpus is gone. Where in Kognitos do we bind the retention floor to the consuming chain's deployment window?"*

**TesseraSeal.** §10.20 (training-data retention floor, lifted to normative spec body via fourth errata, naming Eberhardt × Lumière as the source engagement). Attribute `audit.training_data.retention_floor_days` propagates from the consuming chain's deployment-window discipline. The training-data manifest hash is anchored in chain; the retention floor is bound to the deployment window of the consuming chain via the §10.21 model-handover triple plus a `training_data_retention_floor_days` attribute. GDPR Article 6(1)(f) legitimate interest tied to EU AI Act Article 12 logging, with Article 35 DPIA, is the spec's worked-example resolution path.

**Kognitos.** No field carries retention-floor as a deployment-window function. Field 4 (tools/models used) names the model. Field 12 (integrity proof) carries the training-data manifest hash. Neither field articulates "this artifact's retention floor is set by a downstream chain's deployment-window discipline."

**The under-reporting.** A regulator inquiry at month 12 of deployment cannot reconstruct the training corpus because Lumière has deleted it at day 90. The reference spec catches this by binding the retention floor to the deployment window. Kognitos lets the gap exist silently.

**Speculation gap.** The auditor would have to speculate the retention-floor binding into a Field 8 (reasoning) annotation or into a Field 11 (oversight) note. Either choice produces a deliverable that does not match what an EU AI Act Article 12 regulator will ask for at month 12.

**Honest assessment.** Severity: highest for any joint-vendor engagement where the producing chain's privacy posture (retention minimization) is shorter than the consuming chain's deployment posture (operational continuity). Pattern recurs across automotive supply, pharmaceutical contract manufacturing, financial-services vendor models, healthcare ML vendors.

### C. Audit-document language coverage as chain attribute (plural-array discipline)

**The audit-room question.** *"Lumière's fairness-audit report is in French. The OEM reads English. Eberhardt reads German operationally. Three languages on one audit document. Where in Kognitos do we record which language coverages exist at handover and which are pending?"*

**TesseraSeal.** §10.21 plural-array `audit_report_languages` discipline (lifted to spec body via fourth errata as part of the worked-example paragraph). The attribute carries the language inventory as a row attribute: `["fr"]` for the current state, `["fr", "en"]` once English translation lands. Any reader can query which languages cover which audit artifacts.

**Kognitos.** Field 4 (tools/models used) names the model and possibly the audit author. No field carries audit-document language inventory. Field 8 (reasoning) is wrong by structure — language inventory is not reasoning; it is a structural property of the audit-document set.

**The under-reporting.** The five readers (EU AI Act, BSI, LfDI/CNIL, OEM, Big-Four) each have their own language expectation. The chain has to carry the inventory so each reader can verify the audit document exists in their reading language. Kognitos cannot carry the inventory.

**Honest assessment.** Severity: high for multi-language regulator audiences. Pattern recurs across any cross-border partnership engagement. Less severe than the §1.4 composition inarticulability but still structural.

### D. SDK refusal-at-capture as structural property (absence-bearing)

**The audit-room question.** *"Camille tried to commit a build entry with herself as both author and approver. The SDK refused at capture, before any chain row was produced. Build halted. The chain has no record of the attempted-and-refused event. Where in Kognitos do we record the discipline?"*

**TesseraSeal.** §10.22 + §10.21 + SDK-side §4.4 enforcement clause. The discipline is *absence-bearing* — events that violate the policy produce no chain row because the SDK refuses to seal them. The structural property is "wrongness cannot enter the chain because the SDK does not admit it." Audit posture: read the SDK enforcement clause and the audit-trail in conjunction; the chain's silence on the refused class of events is the evidence.

**Kognitos.** No field can articulate absence. Field 10 (errors/exceptions) is wrong by category — the refusal is not an error, it is enforced policy. Field 11 (approval/oversight) only fires when an event seals; refused events don't seal. The chain produced no row to file under any field.

**Structural reason for the gap.** Kognitos's row-shape requires an event to exist before the framework can describe it. Disciplines whose signature is *non-events* — the SDK refused, the policy held, the wrong class never entered the chain — are structurally invisible to a row-based framework.

**Honest assessment.** Severity: medium for engagements where the structural discipline is enforce-at-capture rather than detect-after-the-fact. Recurs across any SDK-enforced discipline (Ch05 Helmstad pre-MAC redaction; Ch08 NetiVa cross-bank IKM refusal; Ch09 Sun-Won biometric pre-MAC exclusion). Eberhardt × Lumière adds the author-approver instance.

### E. Cross-vendor seven-leg end-to-end trace across organizational boundary

**The audit-room question.** *"Fourteen minutes forty-eight seconds. Eleven chain rows. Three byte-equal hash matches at three §10.21 anchors. Vehicle telemetry to training-data per-shard reconciliation, across two companies, two jurisdictions, two HSM roots. Where in Kognitos do we say the structural property is reproducible?"*

**TesseraSeal.** §10.21 (model-handover) + §7 (verifier) + §5 (RFC 8785 JCS canonicalization) + §8 (conformance test vectors enabling cross-vendor byte equality). The combination produces the seven-leg trace as a reproducible operational outcome — the chains are *designed* such that cross-organizational-boundary joins resolve in operationally sensible windows under deterministic canonicalization.

**Kognitos.** No field aggregates across rows or chains to articulate the structural property. The framework can record what happened in each of the 11 rows. It cannot say that those 11 rows are *structurally joinable* in under fifteen minutes across an organizational boundary.

**Speculation gap.** Under Kognitos, the trace would have to be argued out as an editorial summary across two independent twelve-field deliverables — the cross-vendor join itself unarticulated, the byte-equal hash matches narrated as auditor commentary rather than evidenced as structural property.

**Honest assessment.** Severity: highest for any cross-vendor partnership engagement where joint reconciliation across an organizational boundary is operationally consequential — automotive supply, contract manufacturing, financial-services vendor models, joint-data-product partnerships. Extends Salt Pond's 14-minute cross-location reconciliation into the cross-organizational-boundary case.

### F. §1.2 fairness-audit-vs-model-fairness boundary (variant)

**The audit-room question.** *"Lumière's fairness-audit report is hash-anchored at handover. The chain proves the audit existed at handover and has not been mutated since. Does the chain prove the audit's conclusions are correct, or that the model is unbiased?"*

**TesseraSeal.** §1.2 epistemic scope. The chain proves what was deployed and what was handed over. The chain does not prove the audit's conclusions are correct or the model is unbiased. The fairness-audit-document-vs-model-fairness boundary sits inside §1.2 as the EU-AI-Act-bias-conformity-assessment variant.

**Kognitos.** §1.2 boundary is structurally inarticulable. Field 8 (reasoning/rationale) carries the fairness-audit hash; Field 12 (integrity proof) carries the seal. No field distinguishes "the audit document exists" from "the audit's conclusions are correct."

**Inarticulability gap.** Fifth §1.2 variant in the program after Helmstad (post-enrollment correction), PCP (sensor mutation), Olmstead (civil-rights litigation), Sun-Won (pre-chain era), Salt Pond (FRE 902(13)(14) litigation-defense). Eberhardt × Lumière adds: fairness-audit-document-vs-model-fairness.

**Honest assessment.** Severity: highest for EU AI Act conformity-assessment engagements where the fairness audit is a deliverable. Pattern recurs across any model-deployment engagement where third-party bias audit is hash-anchored in chain.

### G. Within-EU cross-border-transfer attribute emission as SHOULD-by-default operational reading

**The audit-room question.** *"Geneviève said: GDPR Article 30 record-of-processing still requires the within-EU transfer to be attribute-bearing. The §10.21 worked-example paragraph says SHOULD. The operational reading is emit-by-default. Where in Kognitos do we record the SHOULD-vs-MUST distinction at the attribute level?"*

**TesseraSeal.** §4.4.1 `audit.cross_border_transfer.*` family. The worked-example paragraph at §10.21 specifies SHOULD for within-EU transfers; the GDPR Article 30 reading converts SHOULD to emit-by-default. The chain carries the attribute family on every cross-border entry.

**Kognitos.** Field 5 (inputs) carries the data flow. No field articulates per-jurisdiction emission policy (SHOULD vs MUST vs MAY).

**The under-reporting.** Within-EU partnerships often default to under-emitting attribute families on the basis that within-EU is structurally lower-risk. This produces a gap at the GDPR Article 30 reading where the regulator expects records of all transfers, EU or non-EU.

**Honest assessment.** Severity: medium-high for any EU-internal partnership engagement; lower where the data flow is entirely intra-jurisdiction.

### H. Cross-vendor partnership joint stakeholder statement (seventh voice pattern)

**The audit-room question.** *"Heinrich Becker (Eberhardt CTO) and Sébastien Aubert (Lumière CEO) co-signed the framework-substitution recommendation across the partnership boundary. This is not Helmstad-style (same dimension, same institution), not Sun-Won-style (same dimension, two jurisdictions, same institution), not Salt Pond-style (two dimensions, two roles, same institution). Where does the new variant land?"*

**TesseraSeal.** Not applicable — this is a program-level meta-observation about stakeholder voice patterns under the Kognitos lens, not a spec-section comparison.

**Honest assessment.** Severity: program-level observation. The seventh voice pattern in the program is two-executive joint across an organizational boundary — cross-vendor partnership joint. Distinct from all prior six variants. Predicts future cross-vendor partnership engagements will produce similar patterns.

### I. Framework-cannot-grow meta-property — four-chapter-consecutive

**The audit-room question.** *"Four consecutive engagements have driven content into the reference spec body during or directly after the audit cycle — NetiVa §10.17, Sun-Won §4.4 + §4.4.1, Salt Pond §10.19 + `audit.external_artifact.*`, Eberhardt × Lumière §10.20 + §10.21. Seven engagement-source amendments in four chapters. Where does the meta-pattern land?"*

**TesseraSeal.** §12 (change-log mechanism, normative) carries seven engagement-source amendments across four chapters. Fourth errata names Eberhardt × Lumière as the source for §10.20 and §10.21 (plural-array discipline + training-data retention floor + within-EU cross-border-composition note).

**Kognitos.** The twelve-field schema is fixed by design. No §12 analog. Framework cannot grow to meet the audit team's observations across four consecutive chapters.

**The under-reporting.** The framework-cannot-grow meta-property is now reproducible across four consecutive engagements — the most stable signal in the program. Any institution selecting an audit-trail framework is implicitly selecting a growth posture: fixed-row (Kognitos) or change-log-mediated growth (reference spec).

**Honest assessment.** Severity: highest as a framework-selection meta-criterion. Recurs from Ch08 / Ch09 / Ch10; now firm at four chapters.

---

## Summary table

| # | Area | TesseraSeal anchor | Kognitos anchor | Speculation gap | Material impact |
|---|---|---|---|---|---|
| A | Cross-vendor zero-trust composition (§1.4 variant) | §1.4 + §10.21 | Field 12 partial | Inarticulability | Highest — 2nd substrate-class instance |
| B | Training-data retention floor binding | §10.20 (engagement-source) | No field | Under-reporting | Highest — joint-vendor pattern |
| C | Audit-document language coverage | §10.21 plural-array (engagement-source) | No field | Under-reporting | High — multi-language regulator audience |
| D | SDK refusal-at-capture absence-bearing | §10.22 + §10.21 + §4.4 | Inarticulable absence | Framework-silent | Medium |
| E | Cross-vendor 15-min seven-leg trace | §10.21 + §7 + §5 + §8 combined | No structural-property aggregation | Editorial speculation | Highest — cross-vendor pattern |
| F | §1.2 fairness-audit-vs-model-fairness | §1.2 | Inarticulable | Inarticulability variant | Highest — EU AI Act conformity |
| G | Within-EU cross-border-transfer SHOULD-by-default | §4.4.1 + §10.21 | No field | Per-jurisdiction emission | Medium-high |
| H | Cross-vendor partnership joint stakeholder | n/a (program-level) | n/a | Voice-pattern observation | Program-level signal |
| I | Framework-cannot-grow meta (4-chapter-consecutive) | §12 | Fixed schema | Meta-property | Highest — framework-selection criterion |

**Plus recurring from Chapters 01-11:** 16 comparison points unchanged.
**Total comparison points exercised in Chapter 11:** 25.
**Of which inarticulabilities: 2 (§1.4 cross-vendor variant; §1.2 fairness-audit-vs-model-fairness variant).**
**Of which under-reportings: 2 (training-data retention floor; audit-document language coverage).**

---

## Honest assessment — engagement-scoped

### What Eberhardt × Lumière uniquely contributes

Cross-vendor zero-trust composition is the new dimension. Prior chapters' inarticulabilities sat within one institution — Helmstad's epistemic-scope boundary, NetiVa's substrate boundary, Salt Pond's contract-coverage boundary. Eberhardt × Lumière's sits at the *organizational boundary* — two companies, two HSM roots, two jurisdictions, two chains, joined at a §10.21 cross-vendor seam by byte-equal hash. The composition is the trust-producing step; Kognitos cannot articulate composition.

Training-data retention floor bound to consuming-chain deployment window is a new under-reporting class. §10.20 absorbs the binding into the spec body; Kognitos has no field for retention-floor as a deployment-window function. The reference spec names Eberhardt × Lumière as the worked-example source.

Audit-document language coverage via plural-array `audit_report_languages` is a new under-reporting class. §10.21 plural-array discipline lifts to spec body from this engagement. Multi-language regulator audiences require the language inventory as a chain row attribute; Kognitos has no field.

The 15-minute seven-leg cross-vendor end-to-end trace closes the OEM's three-questions test in under fifteen minutes across the partnership boundary. Extends Salt Pond's 14-minute cross-location reconciliation into the cross-organizational-boundary case. Under Kognitos the trace would be editorial across two independent deliverables; under the reference spec the trace is structural.

### Heinrich Becker and Sébastien Aubert — cross-vendor partnership joint statement

Heinrich, on the record: *"The framework records each chain in isolation cleanly. It does not record the cross-vendor seam — neither the byte-equal hash join that produces our joint integrity claim, nor the §10.21 model-handover schema that lets two independent companies compose trust without either trusting the other. Eberhardt co-signs the framework-substitution recommendation, with the new sharpening dimension that our engagement adds: cross-vendor partnership composition across an organizational boundary."*

Sébastien, on the record: *"The byte-equal hash join at our handover with Eberhardt produced what I hoped it would produce: a joint integrity claim that did not require either of us to trust the other. The composition is the trust-producing step. Under Kognitos, neither side's deliverable can articulate what the composition adds, because the composition is the *interaction* between two chains, and the framework has no row for interaction. The cross-vendor partnership joint is the seventh voice pattern in our auditor's running notebook, and we want our names against it."*

Both signed. Dawn replied: *"On the record."*

### Engagement-specific consequences

- Fourth errata absorbs §10.20 (training-data retention floor) and §10.21 (plural-array `audit_report_languages` + within-EU cross-border-composition note) into spec body, naming Eberhardt × Lumière as source.
- Seven engagement-source amendments in four consecutive chapters (NetiVa 1 + Sun-Won 2 + Salt Pond 2 + Eberhardt × Lumière 2).
- 24-month training-data retention as permanent line in model-supply DPA; CAPA in flight; English fairness-audit translation in four weeks.
- Bilingual or trilingual audit bodies as standing practice across Lumière engagements going forward.
- Eberhardt × Lumière partnership now operates under the reference spec for all future EU AI Act conformity-assessment files; Kognitos retained only as cross-vendor comparison summary on cover.

---

*Program-level running tally and editorial signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
