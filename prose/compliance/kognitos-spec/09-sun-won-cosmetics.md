# 09 — Sun-Won Cosmetics Group (Kognitos-lens)

*An engagement where two halves of the audit team work the same chain across the Korea Strait on a video bridge, three regulators read the same artifact through four different lenses, and the institution drives two normative additions into the reference spec while the framework can only record what it lacks.*

**Engagement:** Coordinated annual review across PIPA Section 28 cross-border transfer (Korean PIPC), PDPA Article 8 explicit-consent (Taiwan PDPC), FSS BNPL credit-scoring supervision, Taiwan FSC listed-subsidiary disclosure, and a CPRA / GDPR sweep against the e-commerce platform — three regulators, two HSMs, one chain across the Korea Strait
**Client:** Sun-Won Cosmetics Group — Sangam-dong HQ (Seoul) + Xinyi District listed subsidiary (Taipei); 16 months in production across customer recommendation, inventory forecasting, multilingual chatbot, and BNPL credit-scoring; 8 tenants plus 1 cross-jurisdiction tenant for inventory; Korean HSM (Sangam-dong, KISA-certified) and Taipei HSM (Chunghwa Telecom, CNS 27001 aligned)
**Status:** Chain instrumentation in production sixteen months; deployed nine months ahead of the original roadmap after a celebrity-endorsement controversy alleged AI personalization had used facial and voice features from a celebrity's likeness without explicit consent — the chain is now the cryptographic-evidence backbone for that lookback litigation
**Audit team lead:** Dawn
**Client liaisons:** Hyun-jae Park (Sun-Won Group General Counsel, Seoul); Min-seo Kang (Privacy Officer / DPO for PIPA, Seoul); Joon-ho Lee (Chief AI / ML Officer, Seoul); Wei-ling Tsai (Privacy Officer for PDPA, Taipei); Yun-hsuan Lin (General Counsel, Taipei listed subsidiary); Cheng-hao Wu (M&A integration lead, Taipei)

**Audit team's framework:** Kognitos's 12-field schema. The team is now nine engagements in. This is the first multi-jurisdiction engagement in the program: three regulators reading the same chain through four lenses, two HSMs in two countries, and a split audit team on a video bridge. Dawn, Mike, and Chen took Seoul; Diana and Luis took Taipei. Two findings the engagement produced — cross-border-transfer attribute family and chained classifier_output sixth event type — landed as normative additions to the reference spec's §4.4 and §4.4.1 within the change-log mechanism. This makes Sun-Won the second consecutive chapter where the reference spec grew under audit pressure; under Kognitos, the same audit produces twelve fixed fields and two annotations the framework cannot file structurally.

---

## 🌅 8:30 AM Seoul / 7:30 AM Taipei — Dual Kickoff on the Bridge

The Sangam-dong conference room had four screens. Two showed Taipei. Dawn took the head of the Seoul table with Mike and Chen on her right. Hyun-jae Park, Min-seo Kang, and Joon-ho Lee sat across. On the Taipei side, Diana and Luis appeared on screen alongside Wei-ling Tsai, Yun-hsuan Lin, and Cheng-hao Wu.

Hyun-jae walked the opening. *We are sixteen months in. The chain was deployed nine months ahead of plan. You all know why — the celebrity-endorsement controversy last spring. The chain is now the evidentiary backbone for the lookback the firm is preparing on our behalf. Three regulators in two countries will read this audit. PIPC on the privacy side here. PDPC on the privacy side in Taipei. FSS on the BNPL credit-scoring supervision. FSC on the listed-subsidiary disclosure. Four lenses. One chain.*

Min-seo named the framework constraint. *We were asked to select a framework for the audit deliverable. We selected Kognitos for the cross-vendor comparability, as the customer-bank in the NetiVa engagement did last quarter — that paper has been circulating. We are prepared to revisit the choice if Day 1 surfaces things the framework cannot carry.*

Wei-ling spoke from Taipei. *The PDPA Article 8 explicit-consent regime reads the same artifact differently than PIPA. The cross-border attributes on the inventory tenant are what we need to see articulated cryptographically, not procedurally.*

Dawn confirmed the lens. *We walk the engagement under Kognitos. Running notes flag what the framework cannot carry. Same shape as NetiVa, with the added dimension that this engagement has a fifth audience — the firm that is preparing the celebrity-controversy lookback litigation will read the cover memo. The §1.2 and §5.2 best-evidence posture under FRE 1001-1004 will need to be articulable.*

Hyun-jae nodded slowly. *Begin.*

*Note for the chapter. Four regulator audiences plus a litigation audience. That is five lenses on one chain. The framework has twelve fields. The shape of the deliverable will not match the shape of the question.*

---

## 🧬 9:30 AM Seoul — The April 4 BNPL Declination

Mike pulled an entry from the BNPL credit-scoring chain. April 4, conditional decline at score 689, override to approved by reviewer kr-rv-014. The override answered the FSS 2024-Q2 supervisory letter on reviewer-override capture.

Mike ran the verifier:

```
$ herald-verify --tenant=sunwon-bnpl-kr \
                --service=bnpl-credit-scoring \
                --date=2026-04-04 \
                --entry-id=entry_bnpl_kr_20260404_1428_0331 \
                --strict
```

Four point six seconds.

```
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified
        against public key a1:7f:23:c4:b8:0e:91:d6
Elapsed: 4.6s
```

Mike ran the bulk verifier across the entire BNPL chain for the last 365 days.

```
$ herald-verify --tenant=sunwon-bnpl-kr \
                --service=bnpl-credit-scoring \
                --date-range=2025-04-04..2026-04-03 \
                --strict --bulk
```

Twenty-two seconds.

```
Status: PASS
Entries verified: 18,442
Steps:   12 (per entry)
Reason: chain integrity verified across 365 days;
        no JCS self-test failures; no chain breaks;
        all overrides parent-linked
Elapsed: 22.0s
```

Joon-ho watched. *Three hundred sixty-five days, 18,442 entries, twelve steps each, strict mode, JCS self-test pre-flight on every one.*

> ### ✓ Confirmation #1 — 365-day strict-mode PASS over 18,442 BNPL entries
> Entry-level verification scaled across a year. Override parent-linkage on the 689-score case was answerable to the FSS 2024-Q2 letter. Kognitos Field 11 (human review) records the override; the parent-linkage and the bulk-verification posture do not have framework slots.

Chen wrote in her notebook: *Bulk-verifier posture has no Kognitos representation. The framework records entries one at a time; the institution's evidentiary posture across 365 days is a property of the chain as a whole.*

*Note for the chapter. Kognitos records that an entry has Field 12. It does not record that 18,442 entries verified strict-mode in 22 seconds. That second number is what the FSS will ask about.*

---

## ⚡ 10:30 AM — §10.15 Pattern A and Pattern B Coexisting on One Chain

Joon-ho and Cheng-hao walked the team through the multi-region architecture from both sides.

The KR + TW recommendation tenants ran under §10.15 Pattern B: per-jurisdiction `tenant_id`, separate HSMs, separate IKMs, separate seal cadences. No co-mingling of key material between parent and subsidiary. FSC and PIPC both wanted this explicitly.

The `sunwon-cross-inventory` tenant ran under §10.15 Pattern A: single seal region (Seoul) with synchronous-read freshness on `master.cross_region_replication_completed`. The cross-jurisdiction inventory tenant existed because the supply-chain optimizer needed both warehouses' counts.

Diana walked the cross-region reconciliation from Taipei.

```
$ herald-verify --tenant=sunwon-cross-inventory \
                --service=inventory-forecasting \
                --date=2026-05-21 \
                --region-reconcile --strict
```

```
Status: PASS
Per-region count (KR): 1,832
Per-region count (TW): 362
Sum: 2,194
Seal-region count (Seoul): 2,194  ← MATCH
Reason: §10.15 Pattern A freshness rule honored;
        master.cross_region_replication_completed
        synchronous-read at emission
Elapsed: 3.8s
```

> ### ✓ Confirmation #2 — Pattern A reconciliation on `sunwon-cross-inventory` (KR + TW = seal-region)
> Cross-jurisdiction count integrity holds across the strait. The Pattern A freshness rule held under live conditions.

Wei-ling asked the question that produced the first finding.

*The inventory tenant produces chain entries that cross the Korea Strait. Where does the cross-border transfer attribute appear on the entry?*

Joon-ho paused. The cross-border transfer information was recorded — but it lived in the routing schema as ad-hoc attributes, not as a normative attribute family. The spec body (§4.4) named transfer envelopes but did not have a formal attribute family for cross-border-specific data.

Chen wrote down the gap.

> ### 🚨 Finding-001 — Cross-border-transfer attribute family is not yet in reference spec body
> The institution carries the cross-border attributes (`contract_id`, `contract_version`, `contract_hash_sha256`, `source_jurisdiction`, `destination_jurisdiction`, `lawful_basis_type`) in the chain entries today as ad-hoc routing attributes. Reference spec §4.4 envelope and §4.4.1 routing schema do not yet name this attribute family normatively. The institution will be filing the gap with the standards-body reviewer as a §12 change-log entry. Closure path: spec amendment lifting the six attributes to spec body. ETA: Q3 2026.
>
> Kognitos: Field 6 (inputs with source attribution) carries the inputs; it does not carry the lawful-basis-type attribute or the source/destination jurisdiction pair as a structured cross-border family. The PIPA Section 28 + PDPA Article 8 + GDPR Chapter V audiences each need to read the attribute family; under the framework, the auditor carries the six attributes in a prose footnote per regulator.

*Note for the chapter. The first finding of the day is one the institution will be using to grow the reference spec. The reference spec absorbs the finding via §12 change-log governance. Kognitos's twelve fields are fixed. The institution can drive spec evolution; under the framework, the institution can only record the absence.*

---

## 🛡️ 11:30 AM — Celebrity-Controversy Lookback Framing: §1.2 + §5.2 + §1.1

Hyun-jae stood and walked to the screen. The case was on the room's mind from the kickoff. The chain had been deployed nine months ahead of plan in March 2025, immediately after the controversy broke. The allegation was that the recommendation engine had used the celebrity's facial features from photographs and voice features from interview audio without explicit consent.

The chain — sixteen months in — covered everything from the deployment forward. The pre-chain era was the litigation lookback window.

Hyun-jae walked the §1.2 epistemic-scope line.

*The chain proves what the model said. The chain proves the record was not tampered with. The chain does NOT prove that the inputs the model used were sourced under explicit consent. That is a separate provenance question. For the post-March-2025 period, the chain demonstrates structurally — via §10.22 pre-MAC redaction — that facial features and voice features cannot enter the feature pipeline. For the pre-chain era, the institution depends on legacy logs at the ingestion-system layer.*

Dawn asked the framework question.

*Where does Kognitos articulate the §1.2 (c) line that the chain does not prove input authenticity?*

Chen flipped pages slowly. Field 6 (inputs with source attribution) was the closest field. But Field 6 records what the model SAID was its input, not what was actually the case at the ingestion-system layer pre-chain.

> ### ⚠ Framework Inarticulability #5 — §1.2 (c) chain-clean / source-pre-chain has no Kognitos slot
> This is the third instance of the §1.2 epistemic-scope inarticulability in the program. Helmstad (Ch05) had the post-enrollment correction variant; Pacific Crescent (Ch06) had the sensor-mutation variant; Olmstead (Ch07) had the civil-rights litigation variant. Sun-Won introduces the pre-chain-era variant: the chain begins on a date; before that date, source-data integrity is a property of legacy logs at the ingestion layer. Kognitos has no slot for the chain's start-date as an epistemic-scope boundary. Reference spec §1.2 + §10.19 + §12 articulate the boundary honestly.

Hyun-jae continued. *The firm preparing the lookback will need a Daubert one-pager. They will need the §5.2 best-evidence posture under FRE 1001-1004 articulated. They will need the §1.1 four-factor mapping — testability, peer review, error rate, general acceptance.*

Dawn walked the framework's answer honestly. *Under Kognitos, the litigation file consists of Field 12 marked "tamper-evident integrity proof exists" plus twelve rows per entry. The framework has no slot for Daubert factors, no slot for FRE 1001-1004 best-evidence framing, no slot for §1.1 mapping. We will be borrowing the reference-spec language for the cover memo.*

> ### ◇ Framework-Silent Observation #13 — Litigation-defense posture for celebrity-controversy lookback
> The lookback litigation requires a Daubert one-pager + §5.2 best-evidence posture + §1.1 four-factor mapping. Reference spec articulates all three. Kognitos's twelve fields articulate none.

*Note for the chapter. This is the second engagement in two chapters (after Olmstead's civil-rights variant) where the litigation-defense posture is a primary deliverable. The pattern is firming: at any engagement with active or anticipated litigation, the framework's edges around §1.1 / §1.2 / §5.2 become load-bearing — and Kognitos has no slot for any of them.*

---

## 🔧 1:00 PM — Pre-MAC Redaction as Structural Proof, Not Policy Proof

After lunch, Joon-ho walked the post-controversy redesign. The pre-controversy AI pipeline had policy-level guardrails: feature filters at the model layer, with a runtime check that excluded facial features and voice features from the recommendation engine's inputs. The controversy alleged that the runtime check had been bypassed in one or more cases. The institution had no cryptographic proof of feature-exclusion.

The redesign moved feature exclusion to ingest. The §10.22 pre-MAC redaction at the SDK boundary now ensures that any photograph or audio input is processed for *non-biometric* features only — color palette, garment styling, scene composition for photographs; cadence, pacing, tone-class for audio — before the MAC computation. The biometric features cannot enter the feature pipeline because they are redacted before the chain entry's MAC is computed.

Joon-ho's framing: *Under the old design, "the model does not use facial features" was a policy claim. Under the redesign, "facial features cannot enter the feature pipeline" is a cryptographic claim. The chain entry's MAC integrity is the structural proof.*

Mike ran a verifier exercise on a sample recommendation entry. PASS. Chen examined the `audit.redaction.disposition` attribute on the entry: `pre_mac_excluded`. Reason: `biometric_features_excluded_at_ingest_per_post_controversy_design`.

> ### ✓ Confirmation #3 — §10.22 pre-MAC redaction operationalized as cryptographic proof
> The redaction disposition attribute, bound under MAC, makes the feature-exclusion structurally verifiable rather than policy-verifiable. Reference spec catches this discipline; the institution's post-controversy redesign sits on this spec section.
>
> Kognitos: Field 6 (inputs with source attribution) carries the inputs after redaction. The framework records what entered the pipeline. The framework does not record that something cryptographically *could not* enter the pipeline. The structural proof has no Kognitos representation.

> ### 🚨 Framework Under-Reporting #6 — Structural proof of feature-exclusion vs policy proof
> Reference spec §10.22 + `audit.redaction.disposition` enables the discipline where features are excluded *before* MAC computation, making exclusion cryptographically verifiable. The institution can defend "feature X cannot enter" as a chain property. Kognitos's twelve fields record what Field 6 saw; they cannot record what was structurally prevented from being seen. For the lookback litigation, this is the difference between defending the AI on policy claim and defending the AI on cryptographic claim.

*Note for the chapter. This is the second consecutive chapter to surface a structural-proof-vs-policy-proof gap. Ch08 had it on cross-bank cryptographic isolation. Ch09 has it on biometric-feature exclusion. The framework records what happened; it cannot record what was structurally prevented from happening. The under-reporting count is now six.*

---

## ⚡ 2:00 PM — The Chatbot Routing-Rationale Gap: Finding-002

Joon-ho pulled the chatbot chain. The multilingual chatbot served Korean, Mandarin, English, Japanese, and Indonesian. Routing decisions — which language path to take — were made by a language-detection classifier before the LLM was invoked.

Dawn asked for a five-sample reconciliation: pull five recent ambiguous-language routing decisions; reconstruct from the chain why each was routed where.

Three of five samples were recoverable: the language-detection classifier had emitted scores to a separate 90-day detector-log table. From the detector log + chain entry, the routing rationale was traceable.

Two of five were gone. The 90-day window had rolled. The chain entry recorded the routing decision but not the classifier scores that informed it. The routing was correct; the rationale was not chain-bound.

Chen worked the gap with Joon-ho.

The structural fix: emit `audit.routing.classifier_output` as a sixth event type, *before* the `audit.routing.attempt` event it informs, parent-linked via `parent_run_id` and `parent_seq`. The classifier_output event would carry `classifier_name`, `classifier_version`, `classifier_input_hash`, `classifier_scores`, `classifier_decision`, `classifier_confidence`. Bind the whole sequence under MAC. The rationale becomes chain-bound rather than dependent on a side-channel log with a 90-day retention.

The standards-body reviewer in the room (Joon-ho dialed in another participant from the AI/ML side) agreed the gap was structural and would file the change-log entry. ETA Q3 2026 alongside the cross-border attribute family.

> ### 🚨 Finding-002 — Chained `audit.routing.classifier_output` sixth event type not yet in reference spec body
> The institution's chatbot routing rationale depends on a side-channel detector-log table with 90-day retention. For ambiguous-language samples older than 90 days, the rationale is not chain-bound. The institution will file the gap with the standards-body reviewer as a sixth event type: `audit.routing.classifier_output` parent-linked to `audit.routing.attempt` via `parent_run_id` + `parent_seq`. Six new attributes. Spec ETA Q3 2026.
>
> Kognitos: Field 8 (reasoning) is the closest field. Field 8 captures the model's reasoning narrative; it does not capture the prior-classifier scores that determined which model was invoked. The chained event-type sequence — parent-linkage between a classifier and the model invocation it routed to — has no Kognitos slot.

> ### 🚨 Framework Under-Reporting #7 — Parent-linked event-type sequences
> Reference spec §4.4.1 enables chained events with parent-linkage discipline. The classifier_output → routing.attempt sequence makes the rationale structurally part of the chain. Kognitos's twelve fields are designed per-decision; the framework does not have parent-linkage between event types. For multi-stage AI pipelines (classifier → router → model → post-processor), the upstream stages disappear from the framework's representation.

> ### 🚨 Finding-003 — Chatbot reconciliation 3-of-5 routing rationale recoverable
> Tracking finding. Two samples beyond 90-day window have routing decisions chain-bound but classifier scores gone. Closure path: Finding-002 remediation lands the sixth event type into spec body and into NetiVa, Sun-Won, and any other multi-classifier implementations. ETA Q3 2026.

*Note for the chapter. Two findings the engagement drove into the spec, plus one tracking finding closed by the second one. The reference spec absorbs both via §12 change-log governance. The Kognitos framework records seven row-violations: three for the cross-border attributes (Finding-001 instance per regulator), two for the missing classifier-scores (Finding-003 instance), two for the under-reporting category. The spec moves to meet the posture. The framework stays where it was.*

---

## 💳 3:30 PM Taipei — Salesforce CDC Mirror Walk

Diana pulled the Taiwan CRM Salesforce CDC mirror. The §10.16 lag posture: median 18 seconds, p95 SLO 90 seconds, alert threshold 150 seconds, RTO 5 minutes. Steady-state actuals well under SLOs. Zero alert-threshold breaches in 12 months.

Diana ran the verifier on a CDC-sourced recommendation entry.

```
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified;
        connector_source attribution per §4.4.6
Elapsed: 4.9s
```

> ### ✓ Confirmation #4 — §10.16 four-number lag-bound discipline on TW CRM CDC mirror
> Median 18s, p95 90s, alert 150s, RTO 5min. Steady-state well under SLOs. Recurring instance from Ch04, Ch06, Ch07, Ch08. The framework has Field 6 source attribution; it does not have the temporal envelope around it.

*Note for the chapter. Fifth recurring instance of the four-number lag posture observation. The pattern is now stable across five engagements with different industries — banking, healthcare, utility, university, vendor evaluation, K-beauty multi-jurisdiction. The framework gap on temporal-envelope-of-source is universal.*

---

## ⚡ 4:00 PM — §10.21 Cross-Vendor Handover: The Seoul Consultancy Chatbot

Joon-ho walked the chatbot model's lineage. The base model was authored by a Seoul AI consultancy under a written contract; Sun-Won took possession of the model artifact, the training-data hash manifest, and the audit-report citation set. The handover was integrity-bound under §10.21: `contract_status` discriminator on the chain entry's vendor-handover attribute family; `audit_report_languages` array carrying both Korean and English audit-report citations.

Mike examined an entry: `vendor_handover.contract_status = closed; audit_report_languages = ["ko", "en"]`.

> ### ✓ Confirmation #5 — §10.21 cross-vendor model-handover with contract binding
> Korean chatbot model handover from Seoul consultancy. Contract triple bound under MAC. Plural `audit_report_languages` covers Korean and English audit-report citations. Recurring from Ch02, Ch03, Ch05.

---

## ⚡ 4:30 PM — Pre-chain Era Honest Framing: §1.2 + §10.19 + §12

Chen had been working a separate thread for an hour. The chain started in March 2025. The pre-chain era — for which the firm preparing the lookback would need to construct a separate provenance case — was an ingestion-layer legacy-log question, not a chain question.

Chen walked the framing with Min-seo and Wei-ling.

The §1.2 epistemic-scope line says the chain proves what the model said. The §10.19 chain-coverage map says where the chain begins. The §12 change-log records the spec's evolution. Together, the three sections articulate honestly: the chain begins on date D; before date D, source-data integrity is a property of legacy logs at the ingestion layer; the lookback firm will reconstruct pre-D provenance via those legacy logs, not via the chain.

> ### ✓ Confirmation #6 — Pre-chain era honest framing via §1.2 + §10.19 + §12
> The institution carries a §10.19 chain-coverage map that names the chain's start date and acknowledges the pre-chain era as institution-side legacy-log dependency. The firm preparing the lookback gets the framing in writing. Reference spec is honest about epistemic-scope-by-date.
>
> Kognitos: Field 1 (timestamp) on every entry. The framework records that an entry was made at time T. The framework does not articulate "the chain begins on date D" as a structured property of the chain itself. The honest framing requires prose annotation in the cover memo.

---

## 🌆 5:00 PM Seoul / 4:00 PM Taipei — Joint Debrief

Dawn went to the whiteboard. Diana and Luis dialed in for the debrief. The screens showed both sides of the room.

```
KOGNITOS 12-FIELD ASSESSMENT — SUN-WON COSMETICS GROUP
(MULTI-JURISDICTION KR + TW; 4 REGULATORS; LOOKBACK LITIGATION AUDIENCE)

AI SIDE — BNPL + RECOMMENDATION + INVENTORY + CHATBOT:
  Confirmations:                  6 (BNPL bulk verify; Pattern A reconcile;
                                     pre-MAC structural proof; CDC lag;
                                     cross-vendor handover; pre-chain framing)
  Findings (drove into spec):     3 (Finding-001 cross-border family;
                                     Finding-002 classifier_output event type;
                                     Finding-003 tracking — closes with -002)
  Partials:                       0
  Framework-silent observations:  1 (litigation-defense posture for lookback)

CROSS-JURISDICTION SUBSTRATE:
  §10.15 Pattern A + Pattern B coexisting: 1 framework-thin row per pattern
  PIPA Section 28 + PDPA Article 8 + GDPR Chapter V: prose carry per regulator
  Korean + Mandarin runbooks (cross-language CC8.1): no framework slot

LITIGATION SUBSTRATE:
  Daubert one-pager (§1.1): NOT REPRESENTABLE in framework
  Best-evidence posture (§5.2 / FRE 1001-1004): NOT REPRESENTABLE in framework
  Pre-chain era boundary (§1.2 (c) variant): no framework slot

CROSS-ZONE / FRAMEWORK-SIDE:
  Framework Inarticulability:     1 (pre-chain era §1.2 (c) variant)
  Framework Under-Reporting:      2 (structural-proof feature-exclusion;
                                     parent-linked event-type sequence)
  Spec moved to meet posture:     2 sections this engagement
                                  (§4.4 + §4.4.1 via §12 change-log)
```

Dawn drew a box around "Spec moved to meet posture" and underlined "2 sections this engagement."

**ENGAGEMENT-TEAM OBSERVATIONS ON FRAMEWORK SELECTION:**

1. The reference spec absorbed two findings this engagement produced. Under Kognitos, those same findings would be unfilable observations. Two consecutive chapters (NetiVa, Sun-Won) have now demonstrated that the reference spec is a living standard while the Kognitos framework is a fixed catalog. The §12 change-log mechanism is the structural difference.
2. Four regulators read the same chain through four lenses. The reference spec's per-role reading paths (§0.5.3) make partitioned letters from one chain artifact natural. Kognitos has no per-role reading discipline; each regulator letter requires reconstruction from prose.
3. The post-controversy redesign moved feature exclusion to ingest. The discipline is now cryptographic, not policy. Reference spec §10.22 catches the discipline; Kognitos's Field 6 records what entered, not what was structurally prevented from entering. For the lookback litigation, this is the difference between defending on policy and defending on cryptographic proof.
4. The chatbot multi-stage pipeline (classifier → router → model) is invisible under Kognitos. The reference spec's chained event types with parent-linkage make the pipeline structurally observable. Kognitos's twelve fields are per-decision; pipelines collapse to a single Field 8.
5. The lookback litigation requires §1.1 + §1.2 + §5.2 articulation. Reference spec carries all three. Kognitos carries none. The cover memo will borrow reference-spec language verbatim.
6. Two HSMs, two countries, two languages, cross-language CC8.1 discoverability — none have framework slots. The cross-language Hebrew variant from NetiVa is now joined by the Korean + Mandarin variant here. Pattern is stabilizing.

The Taipei side stayed quiet for a beat. Wei-ling spoke.

*The PDPA Article 8 letter we owe in three weeks will read this audit. The cross-border attribute family is the centerpiece of that letter. Under Kognitos as the sole framework, the centerpiece would be prose. The reference spec moving to meet our posture means the centerpiece is structurally cryptographic by Q3.*

Hyun-jae picked it up from Seoul. *We will request the joint statement.*

---

## 🧾 Stakeholder On-the-Record Statement — Min-seo Kang + Wei-ling Tsai (Joint Cross-Jurisdiction)

Min-seo led from Seoul. Wei-ling joined from Taipei on the bridge. Both DPOs spoke for their respective regulator regimes — PIPA / PIPC on the Korean side; PDPA / PDPC on the Taiwanese side. The cover-memo destination was the standards-body reviewer who would file the §12 change-log entries.

Min-seo opened, in English with formal cadence.

*We are the privacy officers for Sun-Won Cosmetics Group across two jurisdictions. We have selected the Kognitos framework for cross-vendor comparability on the audit-deliverable cover, and we have heard the audit team walk the engagement under that framework with discipline. We have also heard, in their running notes, that the framework cannot carry the cross-border-transfer attribute family in a structured way; that it cannot carry the chained classifier_output event type in a structured way; that it cannot carry the §1.2 (c) pre-chain era boundary that the lookback litigation depends on; that it cannot carry the §1.1 Daubert four-factor mapping that the firm preparing the litigation has asked for in writing.*

Wei-ling continued from Taipei.

*Our institution has surfaced two findings in this engagement that the reference specification will be absorbing into normative spec body via the §12 change-log mechanism. The cross-border-transfer attribute family lifts to §4.4 spec body. The chained classifier_output sixth event type lifts to §4.4.1 spec body. Both land before the end of Q3, alongside our six-week legal review of the contract bindings and two-week chain-config remediation. The reference spec is moving to meet our posture. The Kognitos framework cannot move. We want that distinction on the record.*

Min-seo closed.

*We are asking the standards-body reviewer to credit Sun-Won Cosmetics Group as the engagement source for both §4.4 and §4.4.1 amendments per the §12 change-log practice. We are asking our audit team to name, in the cover memo, that the framework we selected for cross-vendor comparability did not carry the engagement's most consequential findings. We will recommend that future multi-jurisdiction privacy audits across PIPA, PDPA, GDPR, and any analog regime be delivered against the reference specification, with Kognitos retained only for the cross-vendor comparison summary table. The audit team's running notes will be the record of what the framework missed. On the record. Both jurisdictions.*

Dawn waited. *On the record. Both jurisdictions.*

*Note for the chapter. Fifth-and-sixth on-the-record stakeholders — Min-seo Kang + Wei-ling Tsai jointly across two regulator regimes. This is the first cross-jurisdiction joint statement in the program. It is also the second framework-substitution recommendation (after Pankaj at NetiVa), now applied to a different engagement class: multi-jurisdiction privacy audits. The pattern is firming: at every engagement where the framework's silences cost the institution materially AND the spec moves to meet the institution's posture, the stakeholder requests framework substitution rather than annotation.*

---

## 🧾 Final Assessment Theme

> "Sun-Won Cosmetics Group is the second consecutive engagement where the reference spec absorbed findings into normative spec body during the audit cycle. Two §12 change-log entries — §4.4 cross-border-transfer attribute family and §4.4.1 chained classifier_output sixth event type — land before Q3 2026. Under the Kognitos lens, the same engagement reads as ten Confirmations on the AI side, two findings the framework cannot file structurally, one framework inarticulability on the pre-chain era §1.2 (c) variant, two framework under-reportings (structural-proof feature exclusion; parent-linked event-type sequence), and one framework-silent observation on litigation-defense posture for the lookback. The Korean + Taiwanese DPOs delivered a joint cross-jurisdiction on-the-record statement, the first of its kind in the program, recommending framework substitution for multi-jurisdiction privacy audits with the standards-body reviewer credited for the §12 change-log entries. The reference spec moves to meet the posture. The framework records what the posture lacks."

---

## Research takeaway

Chapter 09 introduces three structurally new observations and sharpens two existing ones. First — and most importantly — the engagement demonstrates that the framework-can-grow vs framework-is-fixed contrast is now reproducible across consecutive chapters. NetiVa drove §10.17 via §12 change-log. Sun-Won drove §4.4 + §4.4.1 via §12 change-log. Two chapters, three spec sections, one mechanism. The meta-property is now a stable program-level signal rather than a one-off observation.

Second, the cross-jurisdiction joint statement variant adds a fifth voice pattern (after direct boundary-setting, joint-leadership formal request, sharper-dimension addition, and framework-substitution recommendation): the *cross-jurisdiction joint stakeholder statement*, where representatives of two regulator regimes coordinate their request. Min-seo + Wei-ling delivering one statement across two countries is a new variant predicting future multi-national engagements will produce similar coordination.

Third, the structural-proof-vs-policy-proof gap surfaced in two consecutive chapters: NetiVa on multi-tenant cryptographic isolation; Sun-Won on biometric-feature exclusion at ingest. This is now a named program-level pattern: at any engagement where institutional discipline has moved from policy enforcement to cryptographic enforcement, the framework's row-shape (records what happened) cannot capture the discipline shift (records what is structurally prevented from happening).

- Compared to Ch08 (NetiVa), the spec-moves-to-meet-posture observation is now a two-chapter pattern. Predicts that any future engagement where the institution is on the leading edge of audit-trail design will produce §12 change-log entries that the framework cannot match.
- Compared to Ch07 (Olmstead), the multi-regulator partitioning observation deepens — Olmstead had five regulator audiences from one chain; Sun-Won has four regulator audiences across two countries. The cross-jurisdiction dimension is the new sharpening.
- Compared to Ch05 (Helmstad), the litigation-defense posture is now invoked in three consecutive chapters (Ch07 civil-rights, Ch08 nation-state threat coordination, Ch09 celebrity-controversy lookback). The §1.1 / §1.2 / §5.2 framework gap is consistently load-bearing.

The pattern is consolidating: the framework's edges around growth, structural-proof, litigation-defense, and cross-jurisdiction coordination are systematically inadequate. Two consecutive framework-substitution recommendations across two different engagement classes (nation-state threat at NetiVa; multi-jurisdiction privacy at Sun-Won) suggest the program will produce more substitution recommendations rather than fewer.

---

*Running counts and program-level signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
