# Comparative Analysis — Chapter 10 (Salt Pond Toys)

*Side-by-side analysis of how the Kognitos 12-field framework and the TesseraSeal / FFIEC chain-of-custody v1.0b spec handle a **multi-location consumer-products recall-readiness audit** with four parallel audiences (CPSC + CBP CTPAT + Rhode Island AG + Target supplier-audit) reading the same chain across three time zones. Honest assessment of where multi-audience deliverable cost concentrates framework under-reportings into a linear multiplier and where chain-coverage boundary at the contract edge sits as a new inarticulability class.*

---

## New research signal — multi-audience deliverable cost

Salt Pond is the first engagement in the program where one chain produces four shaped deliverables in eleven consecutive days. The audience composition — CPSC (federal regulator), CBP CTPAT (federal customs revalidation), Rhode Island AG (state consumer protection), Target (private contractual retailer) — is the new dimension. Each audience asks a differently-shaped question; each framework under-reporting becomes a four-times-multiplied speculation cost.

| Dimension | Single-audience engagement (Ch01-Ch07 baseline) | Multi-audience engagement (Ch10 Salt Pond) |
|---|---|---|
| Under-reporting count | N per engagement | N per engagement (unchanged) |
| Speculation cost | 1 × N | 4 × N (one parallel cost per audience) |
| Deliverable shape | One shape | Four shapes from one chain |
| Auditor workload scaling | Engagement scope | Engagement scope × audience count |

What is new: framework under-reportings have an audience-count multiplier under multi-audience deliverable engagements. This is the third sharpening of the framework-substitution recommendation in the program (after Pankaj's first articulation and Min-seo + Wei-ling's cross-jurisdiction joint).

---

## Recurring from earlier chapters

| Recurring point | Earlier ref | Ch10 instance |
|---|---|---|
| §1.2 epistemic-scope inarticulability | Ch02, Ch05, Ch06 | Naomi's FRE 902(13)/(14) litigation-defense variant; 7th appearance |
| Compositional security (§1.4) | Ch01, Ch08 | HSM-rooted seals + Bureau Veritas PGP as independent third-party anchor; layered defense holds |
| Field 2 actor identity well-formed for the chain actor | Ch01 forward | Ling Wei named cleanly; the gap is at the boundary, not at the named actor |
| Field 12 well-formed for chain's own seal | Ch01 forward | 322 consecutive HSM-rooted daily seals; AWS CloudHSM `us-east-1`; clean |
| §10.18 CC8.1 runbook cross-referencing | Ch04, Ch08, Ch09 | Recall-trace validation runbook, Section 321 webhook runbook, CES-anchoring runbook all cross-reference §10.19 |
| §4.4.1 routing-schema controlled vocabulary | Ch03, Ch08, Ch09 | HTS broker-override `audit.routing.refusal_reason` under controlled vocabulary; classifier_output for HTS classification |
| §10.15 multi-region resilience (Pattern A / B) | Ch08, Ch09 | Pattern B per-region tenant boundaries — Newport / LA / Shenzhen each region-pinned |
| §10.16 SaaS-edge four-number lag | Ch08, Ch09 | Descartes broker-case webhook integration — four-number lag bounds |
| §4.4.6 SaaS-edge connector source attribution | Ch08, Ch09 | Descartes integration `audit.connector_source.*` |
| §7 + §10.12 verifier exit-code contract | Ch01 forward | PASS in 3-4 seconds across the sampled forecasts, QC dispositions, customs entries |
| §10.5 HSM custody + separation of duties | Ch01 forward | AWS CloudHSM `us-east-1`; CTO + security director separation of duties |
| §12 change-log spec growth | Ch08 (§10.17), Ch09 (§4.4, §4.4.1) | Fourth errata: §10.19 + `audit.external_artifact.*` driven into spec body from THIS engagement |
| Framework-grows-vs-fixed meta-property | Ch08, Ch09 | Third consecutive chapter; reproducibility now firm |
| Framework-substitution stakeholder recommendation | Ch08 (Pankaj), Ch09 (Min-seo + Wei-ling) | Patrick Cavanaugh + Naomi Briggs co-signed; multi-audience-cost-sharpened |
| Substrate-vs-policy / structural-proof-vs-policy-proof gap | Ch08 (cross-bank IKM); Ch09 (biometric pre-MAC exclusion) | Bureau Veritas independent institutional anchor as structural-proof analog |

**Severities unchanged.** No re-litigation of recurring points.

---

## New comparison points specific to this chapter

### A. Chain-coverage boundary at contract-defined edge

**The audit-room question.** *"The factory-floor operator under Ling Wei's supervision actually pulls the flagged unit off the line. Ling is the chain-of-record actor. Where in Kognitos do we say the operator is structurally outside the chain by design, with the quarterly contract-compliance review as the substitute audit procedure?"*

**TesseraSeal.** §10.19 (chain-coverage map; normative in v1.0b fourth errata) enumerates five categories of chain-coverage boundary; category 3 — "third-party systems under contractual inspection right" — fits the factory-floor operator handling under the supply-agreement §4.7 inspection clause. The boundary is documented as a chain row (`chain.coverage_map_published` operational event under §10.2). The substitute audit procedure (the Shenzhen office's quarterly contract-compliance review) is named in the same row.

**Kognitos.** Field 2 (actor identity) names Ling. There is no field that names a boundary. There is no field that names a substitute procedure.

**Inarticulability gap.** The framework has no row shape for "actor at this step is in someone else's access-control system; here is the contract clause; here is the substitute audit procedure." Speculating the operator into Field 2 with a `role: contractor` tag would falsify the structural relationship — the operator is not Salt Pond's actor under any reading. Speculating the boundary into Field 8 (reasoning/rationale) is a free-text annotation — works as a breadcrumb, fails as a structural label.

**Structural reason for the gap.** Kognitos's fixed-row architecture assumes the actor of every event is *in* the chain. The framework has no representation for "actor is by design out of the chain; the substitute is procedural, contractual, and audit-evidence-bearing in its own right." The reference spec needed a whole new normative section (§10.19, lifted to spec body in the fourth errata) to articulate this.

**Honest assessment.** Severity: highest for consumer-products manufacturers with contract-factory supply chains, multi-vendor logistics chains, or any operation where chain-coverage boundary lives at a contract edge; applies broadly to any audit with sub-contractor relationships.

### B. External-artifact hash anchoring as an attribute family

**The audit-room question.** *"The CES inspection notice is a signed PDF from CBP Los Angeles. We don't own it; CBP does. But CTPAT will ask us to verify it. Where in Kognitos do we hash-anchor the notice in the chain row?"*

**TesseraSeal.** `audit.external_artifact.*` attribute family (informative, advisory; canonical at §10.19 with Appendix A.14 lookup, lifted to spec body in fourth errata). Six attributes: `kind`, `identifier`, `sha256`, `received_at_utc`, `source_party`, `evidentiary_role`. One canonical row shape for any externally-signed third-party artifact hash-anchored alongside the chain entry. Worked examples in the spec: CES inspection notices, customs-broker case snapshots, factory access-log extracts, third-party signed PDFs, CPSIA certificates, bonded-carrier manifests, supply agreements.

**Kognitos.** None of the twelve fields. Field 4 (tools/models used) is wrong by structure — a CES notice is neither a tool nor a model. Field 12 (tamper-evident integrity proof) names the chain's own seal, not externally-signed third-party artifacts.

**The under-reporting.** Salt Pond has at least three distinct external-artifact kinds in active use — CES notice, supply agreement, CPSIA certificate. All three are hash-anchorable in `audit.external_artifact.*` under one canonical row shape. Under Kognitos, all three require speculation, and each speculation has to land somewhere different because the three kinds map differently when forced into Field 4 or Field 8.

**Speculation gap.** The CES notice speculates into Field 4. The supply agreement speculates into Field 8. The CPSIA certificate speculates into Field 11 (approval/oversight) — wrong by structure but the closest field by shape. Three different speculations for one structural pattern.

**Honest assessment.** Severity: highest for any institution with externally-signed third-party artifacts hash-anchored to chain rows — consumer products, customs, supply-chain finance, regulated manufacturing, pharmaceutical raw-materials sourcing, legal-evidence pipelines. The under-reporting is structural and the reference spec lifted the attribute family to the spec body from this engagement.

### C. `intermediate_state` boolean for long-running multi-step external interactions

**The audit-room question.** *"Section 321 broker manual-step takes 90 seconds to twelve minutes. The chain row has a broker-AI-completed timestamp and a broker-submitted-to-ABI timestamp. Between those two, Marisol is doing a manual visual review. How does Kognitos record that the chain row is not yet final?"*

**TesseraSeal.** `audit.external_artifact.intermediate_state` boolean — the worked example in the spec text. `intermediate_state: true` at broker-AI-completion; transitions to `intermediate_state: false` at ABI submission. The chain row's open-vs-closed status is structurally readable at any time.

**Kognitos.** No field articulates open-vs-closed state of a long-running multi-step external interaction. Field 7 (decisions made) carries the broker AI's initial classification. Field 11 (approval/oversight) is wrong by timing — approval is the closing event, not the intermediate state. Field 10 (errors/exceptions) is wrong by category — intermediate state is not an error.

**The under-reporting.** A CBP query during the intermediate state has to get a different answer than a CBP query after submission. The chain has to be readable to know which state is in scope. Without the boolean, the auditor cannot distinguish provisional from final.

**Speculation gap.** The auditor would have to invent a free-text annotation in Field 8 or stamp two separate Field 1 timestamps and let the reader infer which one is "still in flight." Both speculations leak operational state into rows that are not designed to carry it.

**Honest assessment.** Severity: highest for customs filings (Section 321 broker manual-steps are a high-volume case), high for any institution with long-running multi-step external interactions where the open-vs-closed status of a chain row is operationally consequential.

### D. Cross-vendor independent institutional anchor

**The audit-room question.** *"Bureau Veritas signed the CPSIA certificate with their PGP key. We have a SHA-256 of the certificate in the chain row. Two independent integrity proofs co-validate the same artifact. Where in Kognitos do we say that?"*

**TesseraSeal.** §10.21.1 (sample-based-attestation cross-anchor extending anti-counterfeit lot-level binding) and §10.60 (anti-counterfeit cross-anchor; independent third-party attestation reference). Bureau Veritas's PGP-signed CPSIA certificate is the canonical institutional analog the spec section names. Two independent integrity proofs reaching the same artifact from two unrelated institutional postures — Salt Pond's chain seal and Bureau Veritas's PGP signature.

**Kognitos.** Field 12 (tamper-evident integrity proof) names the chain's own seal. There is no field that names a second independent integrity path. Field 11 (approval/oversight) is wrong — Bureau Veritas is not Salt Pond's oversight body; Bureau Veritas is an independent third-party lab.

**The under-reporting.** The structural property — *two independent paths to the same artifact integrity* — is the litigation-defense backbone for the CPSIA certificate. If one institutional posture is challenged (key compromise, lab certification lapse), the other holds. Kognitos cannot articulate the redundancy.

**Speculation gap.** The auditor would have to speculate Bureau Veritas's PGP signature into a Field 12 free-text annotation, which would conflate two different integrity-proof institutional postures into one row.

**Honest assessment.** Severity: highest for consumer-products manufacturers (CPSIA-bound), pharmaceutical (FDA cGMP lot-binding), aerospace (AS6171/SHIELD anti-counterfeit), regulated manufacturing with third-party lab certifications. The cross-vendor anchor is a documented institutional pattern at scale; the reference spec catches it; Kognitos does not.

### E. Multi-audience deliverable cost as a framework property

**The audit-room question.** *"Four audiences in eleven days. CPSC, CBP CTPAT, RI AG, Target. Each asks differently-shaped questions of the same chain. The framework's under-reportings are read by all four. Where does the cost concentrate?"*

**TesseraSeal.** The reference spec's normative sections (§10.19 chain-coverage, `audit.external_artifact.*`, §10.21.1 cross-vendor anchor, §10.16 four-number lag, §4.4.6 connector-source) produce a *common substrate* readable by all four audiences. Each audience reads the same chain rows through its own lens — CPSC reads recall-trace; CBP reads CES notices and bonded-carrier handoffs; RI AG reads paperwork-completeness; Target reads 24-hour reconciliation window. The framework's structural completeness means each audience's question lands on rows that exist.

**Kognitos.** The twelve fixed fields produce the same rows for every audience. The under-reportings — chain-coverage boundary, external-artifact hash, intermediate_state, cross-vendor anchor — are the same for every audience. The speculation cost is read four times.

**The under-reporting.** Multi-audience deliverable cost is the audience-count multiplier on framework under-reportings. For Salt Pond, six framework gaps × four audiences = 24 parallel speculation lines in the deliverable. Each line has to be written four times, each time shaped for a different audience.

**Speculation gap.** The auditor writes the same gap four times in four shapes. CPSC's deliverable says one thing about the chain-coverage boundary; CBP says another; RI AG says another; Target's contractual reviewer asks the question yet differently. The framework cannot collapse the gap to one row.

**Structural reason for the gap.** Fixed-row frameworks scale their speculation cost linearly with audience count under multi-audience engagements. Reference-spec-style growable frameworks absorb the audience-count multiplier through structural completeness — each audience reads existing rows in its own way, but the rows exist.

**Honest assessment.** Severity: highest for any multi-audience engagement (federal + state regulator; federal + private contractual; multi-jurisdiction; multi-customer-side). The pattern recurs across consumer products, finance, healthcare, defense. Salt Pond is the first engagement in the program to make the audience-count multiplier explicit; it will not be the last.

### F. Multi-location operational dimension under Pattern B per-region tenant boundaries

**The audit-room question.** *"Three time zones on three video tiles. Newport ET, LA PT, Shenzhen CST. Eleven months of continuous operation. Where in Kognitos do we record that the chain is structurally region-pinned at Pattern B per-region tenant boundaries?"*

**TesseraSeal.** §10.15 (multi-region resilience). Pattern B per-region tenant boundaries — each region has its own SDK process, region-pinned, with independent daily Merkle seals reconciled at the tenant level. Newport, LA, and Shenzhen each have their own region-pinned process; the daily seals reconcile under the `saltpond` tenant.

**Kognitos.** No field articulates region pinning or multi-region tenant boundary architecture. Field 4 (tools/models used) can name the SDK; it cannot articulate the multi-region topology.

**The under-reporting.** Multi-region tenant boundary architecture is a structural property of the chain. Kognitos cannot articulate it.

**Honest assessment.** Severity: medium-high for global manufacturers, multi-region SaaS, multi-jurisdiction financial-services operations. Recurs from Ch08 (Pattern A multi-region) and Ch09 (Pattern A + B coexisting); Salt Pond is the first program instance of pure Pattern B per-region pinning.

### G. Cross-location cross-service recall reconciliation as a structural property

**The audit-room question.** *"Fourteen minutes from cold pick on lot 25-D-0492. Ninety-six chain rows resolved across three locations and four services. The 2024 inspector's distinction — recoverable vs producible — closed in fourteen minutes. Where in Kognitos do we record that this is a structural property of the chain?"*

**TesseraSeal.** §10.18 (CC8.1 runbook cross-referencing) + §10.19 (chain-coverage map) + §10.21.1 (cross-vendor anchor) + §4.4.6 (connector source) — the *combination* of these sections produces the 14-minute reconciliation as a reproducible operational outcome. The chain is structured such that cross-location cross-service joins resolve in operationally sensible windows.

**Kognitos.** No field aggregates across rows to articulate the structural property. The framework can record what happened in each of the 96 rows. It cannot say that those 96 rows are *structurally reconcilable in 14 minutes*.

**Speculation gap.** The auditor's deliverable to CPSC, Target, and RI AG would have to argue the 14-minute property as an editorial summary of per-row entries — narrating, not structurally evidencing. The 2024 inspector's "recoverable rather than producible" distinction lives precisely in this gap.

**Honest assessment.** Severity: highest for any institution with operationally consequential cross-location cross-service reconciliation windows — consumer-products recall, pharmaceutical supply chain, food safety, financial-services intraday settlement. The 14-minute property is a *structural property*; Kognitos's per-row architecture cannot articulate structural properties.

### H. FRE 902(13)/(14) litigation-defense posture as audience class

**The audit-room question.** *"Naomi needs the chain to self-authenticate as electronic record under FRE 902(13)(14). The chain self-authenticates as record; it does not self-authenticate as proof of physical truth. Where in Kognitos do we say so?"*

**TesseraSeal.** §1.2 (epistemic scope; chain proves what the AI said, not whether the lot was defect-free) + §5.2 (best-evidence under FRE 1001-1004) + §10.13 (evidentiary-artifacts retention list backing FRE 901(b)(9) authentication). The boundary is named structurally; the framework carries it in the chain row's design. Self-authentication-as-electronic-record is a property of the spec by construction.

**Kognitos.** §1.2 boundary is structurally inarticulable under Kognitos (recurring inarticulability, 7th appearance — variant: litigation-defense FRE posture). Field 6 (outputs) carries the AI's claim; no field distinguishes claim-vs-truth.

**Inarticulability gap.** For litigation-defense, the boundary must be in the framework, not in the closing argument. Naomi's litigation posture is structurally compromised under any framework that does not articulate the boundary structurally.

**Honest assessment.** Severity: highest for any institution with active litigation posture, state AG audit exposure, or contractual indemnification clauses triggered by documentation failure. Naomi's articulation is the first explicit FRE 902(13)/(14) framing in the program.

### I. Framework-cannot-grow meta-property — three consecutive engagements

**The audit-room question.** *"Three consecutive engagements have driven content into the reference spec body during or directly after the audit cycle — Netiva §10.17, Sun-Won §4.4 + §4.4.1, Salt Pond §10.19 + `audit.external_artifact.*`. The reference spec's change-log mechanism is doing structural work. Kognitos's twelve fields have produced zero growth. Where does the meta-pattern land?"*

**TesseraSeal.** §12 (change-log mechanism, normative) carries five engagement-source amendments across three chapters. The fourth errata explicitly names the Salt Pond engagement as the source for §10.19 and `audit.external_artifact.*`.

**Kognitos.** The twelve-field schema is fixed by design. There is no §12 analog. The framework cannot grow to meet the audit team's observations.

**The under-reporting.** The framework-cannot-grow meta-property is now reproducible across three consecutive engagements — the most stable signal in the program. Any institution selecting an audit-trail framework is implicitly selecting a growth posture: fixed-row (Kognitos) or change-log-mediated growth (reference spec).

**Honest assessment.** Severity: highest as a framework-selection meta-criterion. Recurs from Ch08 and Ch09; now firm.

---

## Summary table

| # | Area | TesseraSeal anchor | Kognitos anchor | Speculation gap | Material impact |
|---|---|---|---|---|---|
| A | Chain-coverage boundary at contract edge | §10.19 | No field | Inarticulability | Highest — recurring contract-factory pattern |
| B | External-artifact hash anchoring | `audit.external_artifact.*` | No field | Under-reporting | Highest — three distinct kinds in one engagement |
| C | `intermediate_state` boolean | `audit.external_artifact.intermediate_state` | No field | Under-reporting | Highest — Section 321 high volume |
| D | Cross-vendor independent anchor | §10.21.1 / §10.60 | Field 12 partial | Under-reporting | Highest — third-party lab certification scope |
| E | Multi-audience deliverable cost | Common substrate | No structural answer | Audience-count multiplier | Highest — pattern recurs |
| F | Pattern B per-region pinning | §10.15 | No field | Topology under-reporting | Medium-high — global manufacturers |
| G | Cross-location 14-min reconciliation | §10.18 + §10.19 + §10.21.1 + §4.4.6 combined | No structural-property aggregation | Editorial speculation | Highest — recall-readiness class |
| H | FRE 902(13)(14) litigation-defense posture | §1.2 + §5.2 + §10.13 | Inarticulable | Inarticulability variant | Highest — litigation exposure |
| I | Framework-cannot-grow meta | §12 | Fixed schema | Meta-property | Highest — framework-selection criterion |

**Plus recurring from Chapters 01-10:** 15 comparison points unchanged.
**Total comparison points exercised in Chapter 10:** 24.
**Of which inarticulabilities: 2 (chain-coverage boundary new; §1.2 litigation-defense variant).**
**Of which under-reportings: 4 (external-artifact attribute family; intermediate_state boolean; cross-vendor anchor; multi-audience cost concentration).**

---

## Honest assessment — engagement-scoped

### What Salt Pond uniquely contributes

Multi-audience deliverable cost as a framework property is the new dimension. Three prior engagements (Helmstad, Pacific Crescent, Netiva) had federal-regulator audiences with multi-stakeholder boards reading the deliverable, but each had one shaped deliverable. Salt Pond is the first with four shaped deliverables from one chain — CPSC, CBP CTPAT, RI AG, Target — in eleven consecutive days. The framework's under-reportings become four-times-multiplied speculation costs. Patrick Cavanaugh's framework-substitution statement sharpens Pankaj's (Ch08) and Min-seo/Wei-ling's (Ch09) by adding the audience-count multiplier.

Chain-coverage boundary at the contract edge is a new inarticulability class. Prior chapters' inarticulabilities sat at the §1.2 epistemic-scope boundary or the §1.4 substrate boundary. Salt Pond's sits at the *contract-coverage* boundary — where the chain ends and someone else's audit begins, with a named substitute procedure (the Shenzhen office's quarterly contract-compliance review under supply-agreement §4.7). Kognitos has no row shape for this. The reference spec needed a whole new normative section (§10.19) to articulate it.

External-artifact hash anchoring as an attribute family is a new under-reporting class. Three distinct external-artifact kinds in one engagement (CES notice, supply agreement, CPSIA certificate) all fold under one canonical row shape under `audit.external_artifact.*`; under Kognitos, all three require speculation, and each speculation lands in a different wrong field. The reference spec drove this attribute family into the spec body in fourth errata from this engagement.

The 14-minute cross-location cross-service recall reconciliation on lot 25-D-0492 closes the 2024 inspector's "recoverable rather than producible" distinction. Under Kognitos, the closure would have to be editorial — narrating per-row content. Under the reference spec, the closure is structural — the chain is *designed* such that 14-minute cross-location reconciliation is a reproducible operational property.

### Patrick Cavanaugh and Naomi Briggs — joint on-the-record statement

Patrick spoke for multi-audience-cost: *Salt Pond will not migrate from the reference spec to Kognitos as the chain-of-custody framework. The reason is not technical preference. The reason is multi-audience deliverable cost. A consumer-products manufacturer of Salt Pond's scope — four audiences (federal regulator, customs revalidation, state AG, contractual retailer) — cannot absorb the four-times-multiplied speculation cost that comes with a fixed-row framework that under-reports chain-coverage, external-artifact, cross-vendor-anchor, and intermediate-state structural properties.*

Naomi spoke for litigation-defense: *Under the reference spec, §1.2 names the boundary between what the AI said and what is physically true. Under Kognitos, the boundary is structurally inarticulable. If RI AG opened a consumer-protection action that turned on the AI's claim being treated as proof of physical state, I could not let my best-evidence chain be backed by a framework that had no structural label distinguishing claim-vs-truth. The litigation-defense posture requires the boundary in the framework, not in the closing argument.*

Both signed. Dawn replied: *"On the record."*

### Engagement-specific consequences

- Fourth errata lifts §10.19 and `audit.external_artifact.*` to spec body, naming Salt Pond as the source engagement.
- Bureau Veritas CPSIA cross-vendor anchor establishes the canonical institutional analog for §10.21.1 / §10.60.
- The 2024 "recoverable rather than producible" distinction now has a structural closure — 14 minutes on a cold-pick lot.
- Phase 2 (by July 1): Descartes webhook + CES-notice anchoring + Yantian gate-out / LA receipt rename + Bureau Veritas rename + Shenzhen-Newport image-transfer cross-border attribute.
- Phase 3 (12-18 months): supplier-risk model under §10.21 + §10.24 entity-succession runbook for the family-trust generational transition.

---

*Program-level running tally and editorial signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
