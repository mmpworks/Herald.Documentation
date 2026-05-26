# 12 — Hill Country Federal Credit Union (Kognitos-lens)

*An engagement that closes clean on both sides — the chain reads as routine on AWS-only, the framework reads as routine on AWS-only, and the most consequential moment is a quiet engagement-file note Dawn writes for herself at five o'clock: "what happens when the substrate moves?"*

**Engagement:** Three-day pre-engagement readiness pass before NCUA AIRES examination opens in three weeks. Audiences: NCUA AIRES lead examiner (Day 2 afternoon arrival for workpaper composition) and CFPB consumer-protection examiner (§1033 personal-financial-data-rights cross-cut). Big-Four assurance reads downstream.
**Client:** Hill Country Federal Credit Union — ~$8B federally-insured multi-state FCU based in Austin, Texas; member-experience surface in production for eleven months under one chain on AWS `us-east-1` with replicas `us-east-2`. Six months ago Hill Country began a marketing-AI vendor handover — legacy Total Expert → HubSpot Marketing Hub plus an in-house ML scoring layer.
**Status:** Chain in production: eleven months. Single tenant `hillcountry`, four `service.name` values (`member-experience`, `marketing-scoring`, `credit-decision`, `disclosure-fulfillment`). §10.21 cross-vendor model-handover anchor placed at the handover-initiation moment twenty-three weeks ago — exactly when Herald released §10.21 in production. The anchor has not been audit-exercised end-to-end since placement. Today is the first.
**Audit team lead:** Dawn
**Client liaisons:** Tobias "Toby" Reinhardt (Chief Audit Executive — has carried anxiety about the vendor-handover boundary for six months); Beth-Anne Coker (Chief Marketing Officer — owned the handover); Stuart Maples (Chief Compliance Officer / ECOA counsel); Rajiv Khanna (Model Risk Management chair); Marcus Edenfield (Total Expert engineering, legacy vendor, on bridge from Minneapolis); Priya Subramanian (HubSpot Marketing Hub liaison, on bridge from Cambridge MA); Karen Yoo (in-house ML lead). **Regulator observers (Day 2 onward):** Linda Cantwell (NCUA AIRES lead examiner) and DeShawn Bradley (CFPB consumer-protection examiner).

**Audit team's framework:** Kognitos's 12-field schema. The team is now twelve engagements in. This is the first NCUA-supervised institution in the program and the first credit union. It is also the first engagement in the program where the §10.21 cross-vendor model-handover schema is exercised in its **single-substrate single-organization** form — one institution, one cloud, one HSM root, one vendor handover from legacy to new. Eberhardt × Lumière exercised §10.21 across an organizational boundary at Ch11; Hill Country exercises §10.21 across a vendor-handover boundary inside one institution. The contrast is what makes this engagement the foresight-cluster opener.

---

## 🌅 8:30 AM CT Day 1 — Kickoff (Austin operations center, second-floor conference room)

The audit team had landed at Austin-Bergstrom the night before. Dawn, Mike, Diana, Luis, Elena, and Chen took the second-floor conference room at Hill Country's operations center — a low-slung brick building four blocks east of South Congress, glass-walled along the courtyard side, with a whiteboard that ran the length of one wall. Coffee was Texas-strong by Austin standards. The bridge to Cambridge and Minneapolis opened at 8:15.

Toby Reinhardt opened from the head of the table. He was the Chief Audit Executive — quiet, slow-spoken, fifty-something, the kind of internal-audit head who had been at the institution long enough to remember when the chain was a roadmap item on a strategy deck. He had carried, by his own admission, anxiety about the marketing-AI vendor handover for six months. The handover moment had landed at the same week §10.21 shipped. The anchor was placed at handover initiation. The anchor had not been audit-exercised end-to-end since. Today was the day.

Beth-Anne Coker — the CMO — was beside him. She had owned the handover. The legacy stack was Total Expert; the new stack was HubSpot Marketing Hub plus an in-house ML scoring layer that Karen Yoo's team had built and shipped over six months. Stuart Maples — Chief Compliance Officer, ECOA counsel by training, the institution's load-bearing voice on credit-decision linkage — sat opposite. Rajiv Khanna — MRM chair — rounded out the in-person side.

Marcus Edenfield was on the bridge from Total Expert in Minneapolis, with permission and contractual cooperation for the §10.21 attestation. Priya Subramanian was on the bridge from HubSpot in Cambridge. Karen Yoo was in the room.

Dawn ran the three-day plan. Day 1 walked the §10.21 cross-vendor handover end-to-end and the auto-loan ECOA reconciliation. Day 2 walked the §10.69 per-customer disclosure across the vendor-boundary span and then the NCUA AIRES workpaper composition with Linda Cantwell. Day 3 closed the spec-section confirmation memo and the MRM-committee memo on cross-vendor model-card lineage.

*Note for the chapter. Eleven months chained. Anchor placed at handover initiation. Two vendors on the bridge cooperating in good faith. The CAE has been carrying the boundary anxiety for six months. Under the reference spec, the anchor is the structural feature that closes the anxiety. Under Kognitos, the question is what the framework records about that closure.*

> ### ✓ Confirmation #1 — Fields 1-4 satisfied across both vendor eras
> Eleven months of timestamps, actor identities, action descriptions, and tools/models used — all four fields satisfied in isolation on both sides of the handover. Legacy-vendor era reads clean. New-vendor era reads clean. The fields do not depend on the handover.

> ### ✓ Confirmation #2 — Field 12 satisfied; one HSM root across eleven months
> Hill Country chain rooted in AWS CloudHSM `us-east-1` with replicas in `us-east-2`. Daily Ed25519 seals. FIPS 140-2 Level 3+. Tamper-evident integrity proof at every chain row across the eleven months. One substrate, one root, one institution.

## 🧬 9:30 AM Day 1 — §10.21 cross-vendor handover verifier exercise

Mike pulled the cross-vendor anchor entry. It sat on the new-vendor side, dated 2025-12-08, the day Hill Country took receipt of the legacy Total Expert export and sealed the hash into the new chain's daily Merkle seal.

The export itself was a 1.4-TB tar.gz: campaign history, member lists, A/B variant data, scoring artifacts, model cards, lineage metadata. Total Expert had produced the export under the §10.21 handover-cooperation clause. Hill Country had computed SHA-256 over the canonical-form bytes at the moment of receipt. The hash had been sealed into the new chain's daily Merkle seal that same day. Marcus Edenfield's countersigning attestation — a Total Expert engineering signature against the same hash, delivered through the §10.17 dual-signature pair — had landed in the chain three minutes after Hill Country's seal.

```json
{
  "entry_id": "hillcountry/marketing-scoring/2025-12-08#0001",
  "tenant": "hillcountry",
  "service": "marketing-scoring",
  "seq": 1,
  "ts": "2025-12-08T14:42:11.108Z",
  "model_id": "hc-marketing-scoring-v1.0",
  "model_version": "1.0.0-init",
  "gen_ai.request.model": "hillcountry-inhouse/marketing-scoring/v1.0",
  "gen_ai.response.model": "hillcountry-inhouse/marketing-scoring/v1.0",
  "audit.deployment.intent": "production",
  "audit.deployment.policy_version": "hc-prod-policy-v2.0",
  "audit.model_handover.source_party": "total-expert",
  "audit.model_handover.destination_party": "hillcountry-inhouse-ml + hubspot",
  "audit.model_handover.handover_kind": "vendor_replacement_within_substrate",
  "audit.model_handover.export_artifact_sha256": "8b41...c903",
  "audit.model_handover.export_size_bytes": 1503238553600,
  "audit.model_handover.source_attestation_sha256": "e2d7...a4f8",
  "audit.model_handover.dual_signature_pair_seq": 4,
  "audit.external_artifact.kind": "vendor_export_archive",
  "audit.external_artifact.identifier": "total-expert/hillcountry/export-2025-12-08",
  "audit.external_artifact.received_at_utc": "2025-12-08T14:11:03Z",
  "audit.external_artifact.evidentiary_role": "vendor_handover_baseline",
  "payload_hash": "...",
  "hmac": "...",
  "daily_seal_ref": "hillcountry/2025-12-08#seal"
}
```

```
$ herald-verify --tenant=hillcountry \
                --service=marketing-scoring \
                --date=2025-12-08 \
                --entry-id=1 \
                --strict \
                --cross-vendor-handover-walk
```

Nine minutes.

```
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified
        against public key fp:a4:c8:7d:...:11
        cross_vendor_handover_verified
        byte-equality between on-disk Total Expert backup
        (1,503,238,553,600 bytes) and anchored hash confirmed
        dual-signature pair (source attestation + Hill Country seal)
        validated under §10.17
Elapsed: 8m42s
```

Marcus Edenfield's voice came through the bridge speaker after the result resolved. He had run a parallel verification on the Total Expert side using the export's on-disk SHA-256. His number matched the chain's number byte-for-byte. The bridge went quiet for about three seconds.

Toby exhaled. *Six months of boundary anxiety closed in nine minutes of verifier walk*, Dawn wrote in the side margin of her notebook.

*Note for the chapter. The handover anchor is canonical: one institution, one substrate, two vendors, one byte-equal hash join across the vendor boundary. Under the reference spec this is §10.21 in its single-substrate single-organization form — the canonical reference shape for the cross-vendor anchor. Under Kognitos, the join is a Field 12 confirmation that names "the chain holds a proof" without articulating that the proof is the byte-equal hash join across two vendor-cooperation parties. The team has now seen this gap eleven engagements in. There is no new lens-stretch — only the recurrence.*

> ### ✓ Confirmation #3 — §10.21 cross-vendor model-handover anchor verified in single-substrate single-organization form
> The legacy Total Expert export (1.4 TB) was hash-anchored at the handover moment twenty-three weeks ago; the hash sealed into the new HubSpot+in-house-ML chain's daily Merkle seal; byte-equality between the on-disk backup and the anchored hash reproduces in under nine minutes; dual-signature pair (Marcus Edenfield's source attestation + Hill Country's seal) validated under §10.17. Operationally clean.

> ### ◇ Framework-Silent Observation #8 — Single-substrate single-organization §10.21 handover as canonical reference shape (vs cross-organizational variant from Ch11)
> The reference spec's §10.21 admits two structural shapes: (a) single-substrate single-organization vendor-replacement (Hill Country today — one institution, one cloud, one HSM root, two vendors cooperating under contract), and (b) cross-organizational partnership (Eberhardt × Lumière at Ch11 — two institutions, two clouds, two HSM roots, one §10.21 seam). Kognitos's Field 12 names "a proof exists" in both shapes without distinguishing them. The Field 12 row reads identically against today's chain and against Ch11's chain. The framework cannot articulate the structural difference between vendor-replacement-within-substrate and cross-organizational-partnership; the reference spec marks the two as distinct row-shape attributes (`handover_kind = "vendor_replacement_within_substrate"` vs `"cross_organizational_partnership"`).

## 🔧 11:00 AM Day 1 — Legacy-vendor handover review with Marcus Edenfield

Marcus opened from Minneapolis with the legacy-vendor lineage. Total Expert had retained the export's on-disk backup in escrow under a four-year contractual retention floor — past the §10.13 evidentiary-retention floor that NCUA AIRES expected. The escrow location was a separate AWS account under Total Expert's control, region `us-east-2`, with cross-account read-only audit access granted to Hill Country and to NCUA on request.

The §10.21 family had stamped the export's model cards individually. Three model cards. Each card carried a SHA-256 that matched its byte-for-byte on-disk file. Marcus's team had cooperated in good faith — every model card, every scoring artifact, every lineage metadata file had been cataloged and hash-anchored at the handover moment. The chain had every hash. The escrow had every byte.

Diana walked the §10.66 model-weight lineage DAG. Two of the legacy Total Expert scoring models had been retrained twice each over their production lifetimes — four retrain events across two model families, each anchored in the legacy chain with parent-model lineage. The DAG resolved cleanly from current-deployed model back through three retrain ancestors to the original 2024 launch model. Lineage exercise duration: under three minutes.

*Note for the chapter. The legacy vendor cooperated. The escrow holds the bytes. The chain holds the hashes. The lineage DAG resolves in three minutes. Under Kognitos, the lineage is a Field-4 "tools/models used" sequence; the DAG structure — parent-model lineage with retrain-event timestamps — collapses to free-text annotation. Field 4 names the model; nothing names that this model has three ancestors and which ones.*

> ### ✓ Confirmation #4 — §10.13 evidentiary-retention floor satisfied by Total Expert escrow
> Four-year escrow at Total Expert side; cross-account read-only audit access to Hill Country and NCUA on request; AWS `us-east-2` region. Exceeds the §10.13 NCUA AIRES expectation.

> ### ◇ Framework-Silent Observation #9 — Model-weight lineage DAG (§10.66) under vendor-replacement handover
> Three-minute resolution from current-deployed model back through three retrain ancestors to original 2024 launch model. Under reference spec, §10.66 carries the DAG structure as a row-attribute family (parent-model identifier + retrain-event timestamp + training-data-manifest hash). Under Kognitos, Field 4 (tools/models used) names the current model; nothing names the ancestors. The lineage walk would be editorial under Kognitos.

## 💳 1:00 PM Day 1 — Auto-loan ECOA adverse-action reconciliation (5 members)

After lunch, Stuart Maples walked the auto-loan reconciliation. He had selected five members for the trace; the load-bearing case was a member who had received a marketing offer in February — "you're pre-qualified for a $35,000 auto loan at 6.250%" — under the legacy Total Expert ML scoring weights, on a Tuesday, then applied for the loan three weeks later under the new in-house ML scoring weights, was AI-screened, and was approved at 6.625% on a slightly different term structure.

The CMO's question landed first: was the marketing-event-to-credit-decision linkage ECOA-defensible?

The audit answer landed in two parts. The marketing offer was in the chain as a model-inference event under the legacy-vendor era, with the legacy Total Expert ML model identified, the legacy scoring weights snapshotted by hash, and the legacy `audit.deployment.intent = "production"` stamp. The credit decision was in the chain three weeks later under the `audit.ecoa.adverse_action.*` family (§10.11.1) — adverse-action by spec terminology even though the outcome was approval, because the rate-and-term differed from the offer; the entry carried `prior_offer_run_id = "hillcountry/marketing-scoring/2026-02-04#3127"` and `prior_offer_seq = 3127`.

The parent-linkage was the structural feature. The credit-decision chain row referenced the prior-offer chain row by ID-and-seq under MAC; the legacy-vendor era's chain row was bound to the new-vendor era's chain row by cryptographic reference. Stuart's reconciliation tool walked the linkage. Five members, five linkages, all clean. The signature member's credit-decision chain row:

```json
{
  "entry_id": "hillcountry/credit-decision/2026-02-25#4218",
  "tenant": "hillcountry",
  "service": "credit-decision",
  "seq": 4218,
  "ts": "2026-02-25T15:11:47.302Z",
  "model_id": "hc-credit-scoring-v1.1",
  "model_version": "1.1.2-prod-pin-2026-02-19",
  "gen_ai.request.model": "hillcountry-inhouse/credit-scoring/v1.1",
  "gen_ai.response.model": "hillcountry-inhouse/credit-scoring/v1.1",
  "prompt": {
    "member_id_hash": "...",
    "loan_kind": "auto",
    "loan_amount_usd": 35000,
    "term_months_requested": 60
  },
  "response": {
    "decision": "approve",
    "rate_apr_offered": 6.625,
    "term_months_offered": 60,
    "rate_apr_basis_points_delta_vs_prior_offer": 37.5
  },
  "audit.deployment.intent": "production",
  "audit.deployment.policy_version": "hc-credit-policy-v3.2",
  "audit.ecoa.adverse_action.outcome_kind": "approval_with_rate_or_term_difference",
  "audit.ecoa.adverse_action.prior_offer_run_id":
      "hillcountry/marketing-scoring/2026-02-04#3127",
  "audit.ecoa.adverse_action.prior_offer_seq": 3127,
  "audit.ecoa.adverse_action.prior_offer_vendor_era": "legacy_total_expert",
  "audit.ecoa.adverse_action.current_offer_vendor_era": "new_inhouse_ml",
  "audit.ecoa.adverse_action.reason_codes": ["RA-08:rate-tier-shift-on-rescore"],
  "audit.redaction.disposition": "pre_mac_redacted",
  "payload_hash": "...",
  "hmac": "...",
  "daily_seal_ref": "hillcountry/2026-02-25#seal"
}
```

The `prior_offer_run_id` field bound the credit-decision row's MAC to the prior marketing-scoring row's chain ID; the `prior_offer_seq = 3127` matched the marketing-scoring row's sequence number; the `prior_offer_vendor_era = "legacy_total_expert"` and `current_offer_vendor_era = "new_inhouse_ml"` recorded the vendor-era taxonomy explicitly. Stuart's reconciliation tool walked the linkage by resolving the parent chain ID; the verifier confirmed the cross-era binding under MAC.

```
$ herald-verify --tenant=hillcountry \
                --service=credit-decision \
                --date=2026-02-25 \
                --entry-id=4218 \
                --strict \
                --ecoa-prior-offer-trace
```

Six seconds.

```
Status: PASS
Step:   12
Reason: chain integrity verified, prior-offer parent-linkage resolved,
        prior_offer_run_id chain row located in legacy-vendor era,
        prior_offer_seq matches parent row,
        cross-era linkage integrity verified
Elapsed: 6.2s
```

Beth-Anne asked the second question. Whether the policy is fair — whether a 6.250% offer becoming a 6.625% approval is fair, in the ECOA sense — is a different question. The audit answer was the boundary that landed at the §1.2 conversation later, but Stuart already knew it: the chain proves what the AI said about this member, at this time, under this scoring policy. The chain does not, on its own, prove the scoring policy was fair. Fair-lending posture is the institution's CECL and ECOA committees, with the chain providing the data.

Beth-Anne nodded. Rajiv Khanna — MRM chair — wrote in his notebook.

*Note for the chapter. The parent-linkage chain pivot is structural. The marketing-event-to-credit-decision linkage crosses the vendor handover via the prior_offer_run_id / prior_offer_seq fields under MAC. Under the reference spec, the linkage is structural — §10.11.1 carries it. Under Kognitos, the two events would be in the chain as two independent rows; the linkage between them, which is the load-bearing ECOA defense, would be unarticulated. Field 8 (reasoning) could carry the linkage as free-text annotation; the cryptographic binding under MAC would not survive into the framework deliverable.*

> ### ✓ Confirmation #5 — §10.11.1 ECOA adverse-action linkage with prior-offer parent-linkage verified across vendor handover
> Five members traced; signature case ($35K auto-loan at 6.625% vs $35K marketing offer at 6.250%); parent-linkage chain pivot from new-vendor era credit decision to legacy-vendor era marketing offer; cryptographic binding under MAC.

> ### ◇ Framework-Silent Observation #10 — Marketing-event-to-credit-decision parent-linkage chain pivot across vendor handover
> Reference spec §10.11.1 binds the prior-offer chain row to the credit-decision chain row via `prior_offer_run_id` + `prior_offer_seq` under MAC; the linkage spans the vendor handover. Under Kognitos, the two chain rows would file as two independent Field-12 confirmations; the linkage between them — cryptographic, parent-binding, ECOA-load-bearing — would be free-text under Field 8 (reasoning). The chain pivot is structural; the framework's per-row architecture cannot carry it.

## 🛡️ 3:00 PM Day 1 — §10.69 per-customer disclosure across vendor-boundary span

Diana had been preparing the §10.69 disclosure exercises since morning. Three CFPB §1033 personal-financial-data-rights disclosure requests were on the schedule. Each spanned the vendor-handover boundary — each request asked for one unified per-member audit trail covering both the legacy Total Expert era and the new HubSpot + in-house ML era.

The first member's disclosure was for "all AI-influenced communications and credit interactions during 2025-2026 calendar period." The chain had eleven months of entries against this member — ~9,400 chain rows spanning the vendor handover.

```
$ herald-verify --tenant=hillcountry \
                --service=disclosure-fulfillment \
                --customer-anchor=mbr-91842 \
                --start=2025-06-15 \
                --end=2026-05-22 \
                --1033-disclosure \
                --strict
```

Fourteen seconds.

```
Status: PASS
Step:   12
Reason: chain integrity verified across customer subtree
        9,403 chain rows spanning vendor-handover boundary
        customer_disclosure_subtree_verified
        customer_disclosure_key_derivation_verified
        per-customer Merkle subtree resolved across both vendor eras
Elapsed: 14.1s
```

The other two members verified in 13.8 and 14.4 seconds against ~9,100 and ~9,700 chain rows respectively. The disclosure subtree spanned the cross-vendor anchor leaf cleanly — the legacy-vendor era's chain entries were members of the same per-member Merkle subtree as the new-vendor era's entries, because the anchor bound them under one tenant-day Merkle seal.

*Note for the chapter. The structural property — one §1033 disclosure returns one unified per-member audit trail across two vendor eras — is the §10.69 + §10.21 + §4.2 composition. Under Kognitos, the disclosure would have to be argued out as the union of two independent twelve-field deliverables; the unified-subtree property would be editorial. The framework's per-row architecture cannot carry the "one disclosure, one subtree, two vendor eras" structural property as a single deliverable.*

> ### ✓ Confirmation #6 — §10.69 per-customer disclosure subtree spans vendor-boundary cleanly
> Three §1033 disclosure requests; ~13-14 seconds against ~9,100-9,700 chain rows each; the per-member Merkle subtree resolves across both vendor eras in a single verifier walk.

> ### ◇ Framework-Silent Observation #11 — §10.69 disclosure subtree spanning §10.21 cross-vendor anchor leaf
> Reference spec §10.69 + §10.21 + §4.2 compose to produce "one §1033 disclosure returns one unified per-member audit trail across both vendor eras" as a structural property of the chain. Kognitos's per-row architecture cannot articulate the unified-subtree property; the disclosure would be editorial across two independent twelve-field deliverables.

## ⚡ 4:30 PM Day 1 — §10.22 PII redaction across vendor-boundary disclosure packets

Luis ran the §10.22 redaction discipline on the disclosure packets. Member PII — SSN, account numbers, raw scoring features — was pre-MAC redacted at the SDK boundary on the marketing-scoring side per Hill Country's privacy policy. The `redacted_per_§10.22` markers carried through the disclosure packets. The redaction discipline survived the vendor handover — Total Expert's pre-handover redaction rules and Hill Country's post-handover redaction rules were both bound under MAC, with the disposition recorded in the chain as `audit.redaction.disposition = pre_mac_excluded` on the marketing-scoring side and `pre_mac_redacted` on the credit-decision side.

Stuart confirmed the rules: marketing-scoring excluded the PII entirely; credit-decision redacted it with the disposition marker bound under MAC for ECOA evidentiary linkage.

*Note for the chapter. The redaction discipline is per-vendor-era under different operational defaults but both vendor eras' dispositions are MAC-bound. Under Kognitos, the dispositions would file as Field-7 (data sources/security context) annotations; the disposition-enum bound under MAC is a reference-spec structural property the framework cannot carry as a discriminator.*

> ### ✓ Confirmation #7 — §10.22 redaction discipline survives vendor handover with disposition-enum bound under MAC
> Marketing-scoring side: `audit.redaction.disposition = pre_mac_excluded`. Credit-decision side: `pre_mac_redacted`. Both dispositions bound under MAC; disclosure packets carry the markers through.

## 🌆 5:00 PM Day 1 — Auditor debrief + engagement-file note

Both rooms reconverged. Dawn wrote the day-one tally on the whiteboard:

```
KOGNITOS 12-FIELD ASSESSMENT — HILL COUNTRY FCU
(NCUA AIRES + CFPB §1033 + FCU INTERNAL AUDIT + BIG-FOUR ASSURANCE DOWNSTREAM)
(SINGLE-SUBSTRATE / SINGLE-ORGANIZATION / VENDOR-REPLACEMENT WITHIN AWS)

AI SIDE — MARKETING-SCORING (5 MONTHS NEW, 6 MONTHS LEGACY):
  Confirmations:                  4 (Fields 1-4, 5-8, 11, 12)
  Partials:                       0
  Findings:                       0
  Nits (under Kognitos):          0
  Framework-silent observations:  4 (handover-kind discriminator;
                                     model-weight lineage DAG;
                                     prior-offer parent-linkage;
                                     disclosure subtree across anchor)

LEGACY-VENDOR SIDE — TOTAL EXPERT HANDOVER:
  Confirmations:                  2 (§10.13 escrow; §10.21 cooperation + dual-signature)
  Partials:                       0
  Findings:                       0

CFPB §1033 SIDE — DISCLOSURE-FULFILLMENT:
  Confirmations:                  1 (subtree spans vendor boundary)
  Partials:                       0
  Findings:                       0

CROSS-VENDOR ANCHOR LEAF:
  Confirmations:                  1 (byte-equal hash join in 9 minutes;
                                     dual-signature pair validated)
  Partials:                       0
  Findings:                       0

FRAMEWORK-SIDE:
  Framework Inarticulability:     0 NEW (recurring §1.4 from Ch08/Ch11
                                          and §1.2 from earlier chapters)
  Framework Under-Reporting:      0 NEW
  Framework-Silent Observation:   4 NEW (single-substrate §10.21 form;
                                          §10.66 lineage DAG;
                                          §10.11.1 prior-offer parent-linkage;
                                          §10.69 + §10.21 subtree composition)

CROSS-CHAPTER META:
  §12 engagement-source amendments this engagement: 0 (clean confirmation)
  §12 amendments in last 4 chapters: 7 (carried forward from Ch11)
  Confirmation-posture engagement (no Findings, no Partials, no new
  Framework Inarticulabilities, no new Framework Under-Reportings):
  first occurrence since Ch03
```

Dawn ran the framework-side observations:

1. **The framework records eleven months cleanly when there are no new gaps to record.** Hill Country's chain operated for eleven months under the reference spec's discipline; the framework's twelve fields are individually satisfied row-by-row across the eleven months; no new Inarticulability surfaces because no novel structural feature pressed against the framework's per-row architecture. This is the first chapter since Ch03 with this posture.

2. **The §10.21 cross-vendor anchor exercises in its single-substrate single-organization form for the first time.** Eberhardt × Lumière at Ch11 exercised §10.21 across an organizational boundary at two HSM roots in two jurisdictions; Hill Country exercises §10.21 across a vendor-replacement boundary within one AWS substrate. The reference spec admits both shapes via the `handover_kind` attribute. The framework's Field 12 reads identically against both — neither shape distinguishes itself under Kognitos's row.

3. **Model-weight lineage DAG resolves in under three minutes.** §10.66 carries the parent-model lineage with retrain-event timestamps as row-attribute structure. Field 4 names the current model; the ancestors are not field-bearing.

4. **The ECOA marketing-event-to-credit-decision parent-linkage chain pivot is structural.** §10.11.1's `prior_offer_run_id` + `prior_offer_seq` fields under MAC bind the legacy-vendor era's marketing offer to the new-vendor era's credit decision. The linkage spans the vendor handover; the binding is cryptographic; the ECOA defense rests on the binding. Field 8 (reasoning) could carry the linkage as free-text; nothing in Kognitos carries the cryptographic parent-binding.

5. **§10.69 disclosure subtree spanning §10.21 cross-vendor anchor leaf is structural.** The reference spec composes §10.69 + §10.21 + §4.2 to produce "one §1033 disclosure returns one unified per-member audit trail across both vendor eras" as a structural property; Kognitos's per-row architecture cannot articulate the property.

Chen wrote one line on his side of the whiteboard before they wrapped: *"§10.40 anchor reads as routine on AWS-only. Open question for the next pass: what happens when the substrate moves?"*

Dawn copied it into the engagement file. It went in as a quiet note — not a finding, not a recommendation, not anything that would land on the NCUA examiner's desk in three weeks. Just a note for herself. The §10.40 cross-vendor anchor — the single-substrate form, the canonical reference shape — had read clean on AWS-only. What happened when the institution's chain spanned two clouds, or when a vendor moved from AWS to Azure mid-handover, or when a chain at one institution had to compose with a chain at another institution across substrate boundaries? She didn't know yet. The chapter would not know yet. Two engagements out — maybe three — that question would be the load-bearing structural feature on someone else's chain, and she would remember this evening.

*Note for the chapter. This is the foresight-cluster opener. The chapter closes clean and the only signal is the question filed quietly for later. The framework has nothing to say about the question — the framework cannot articulate substrate-move under any reading — and the reference spec's §10.40 has the answer waiting in its single-substrate worked-example paragraph. The two engagements after this one will press on the question, and the next-next engagement after those will press on it harder. For now, the note goes in the engagement file and the team goes to dinner.*

## 📋 9:00 AM Day 2 — NCUA AIRES workpaper composition with Linda Cantwell

Linda Cantwell arrived at the operations center at 9:00 Wednesday morning. Lead NCUA AIRES examiner — twenty years at NCUA, last six in the FCU large-credit-union team. Texan, mid-fifties, soft-spoken in the way that career federal examiners tend to be when they have already read most of what they want to read before the entrance meeting. She wanted the spec-section confirmation memo on her desk before her entrance meeting in three weeks, and she wanted to read the audit team's running notes alongside the chain artifacts before she signed for it.

The morning composition session ran two hours and ten minutes. Dawn walked the §10.21 confirmation first — the byte-equal hash join, the dual-signature pair, the Total Expert escrow at four-year retention. Linda asked three questions on §10.21. Where was the source attestation signed; what was Total Expert's contractual cooperation duration; what happened to the escrow if Total Expert was acquired or wound down. Toby Reinhardt fielded the last one — Hill Country had a perpetual-license clause on the escrow contents under any vendor-succession scenario. Linda wrote that down.

Dawn walked the §10.40 single-substrate cross-vendor anchor next. Linda asked one question — whether the AIRES workpaper would distinguish single-substrate handover from cross-substrate handover. Dawn answered honestly: the spec marks the distinction via the `handover_kind` row-attribute discriminator, and the engagement-file note from Day 1 captures the open question about substrate-move for the next-pass audit. Linda asked her to copy the engagement-file note into the workpaper as a forward-looking annotation. Dawn agreed.

§10.69 came next — the disclosure subtree spanning the cross-vendor anchor leaf. Linda's question was operational: could a member's disclosure request, filed under CFPB §1033, return a unified per-member audit trail across both vendor eras in production-realistic time? Diana walked the verifier output from Day 1 — three §1033 disclosures, ~13-14 seconds each, ~9,100-9,700 chain rows per member. Linda asked whether the disclosure scaled if a member's chain-row count went to ~50,000. Mike fielded it — verifier walk time scales sub-linearly with chain-row count because the Merkle subtree resolution depends on tree depth, not leaf count. Linda wrote that down too.

§10.11.1 closed the morning. Stuart Maples walked the ECOA marketing-event-to-credit-decision parent-linkage with the signature case from Day 1. Linda asked whether the parent-linkage held across a hypothetical second vendor handover — if Hill Country replaced the new in-house ML scoring layer with a third vendor in twelve months, would the prior-offer linkage from the legacy Total Expert era still resolve? Karen Yoo answered — the linkage was MAC-bound at row-creation time; subsequent handovers would not invalidate the binding because the binding lived in the chain row, not in the vendor. Linda nodded.

Twelve questions across two hours. Audit team answered all twelve from the chain. The AIRES workpaper conventions translated cleanly from the spec-section references — §10.21 mapped to AIRES Module 5 (vendor management); §10.69 mapped to AIRES Module 7 (consumer protection / §1033 cross-cut); §10.11.1 mapped to AIRES Module 6 (lending fair-lending review); §10.66 mapped to AIRES Module 8 (model risk management). Linda signed for the composition session at 11:15.

*Note for the chapter. The composition session was the audit team's first NCUA AIRES workpaper composition in the program. The translation from spec-section references to AIRES module references worked because the reference spec composes with the NCUA AIRES workpaper model at §10.13. Under Kognitos alone, the translation would have been editorial — the framework's twelve fields do not compose with AIRES modules in any structural way. The chapter's confirmation-posture outcome is partly a function of this structural composability: when the reference spec's section taxonomy lines up with the regulator's workpaper module taxonomy, the audit team's job is to walk the crosswalk, not to invent it.*

## 🛡️ 11:30 AM Day 2 — CFPB §1033 witness-mode walk with DeShawn Bradley

DeShawn Bradley arrived at 11:30. CFPB consumer-protection examiner — six years at the Bureau, last three on §1033 personal-financial-data-rights enforcement, joined the engagement on the §1033 cross-cut because Hill Country was one of the first NCUA-supervised FCUs to bring its §1033 disclosure infrastructure under chain instrumentation. He carried his own laptop.

Diana set up the witness-mode walk. Witness-mode in §10.12 was the verifier path where the examining party ran the verifier on their own laptop, against the chain artifacts the audit team handed over, and read the verdict in the witness-mode discriminator — `PASS-STRUCTURALLY` rather than `PASS`. The discriminator meant that the chain integrity verified structurally against the artifacts presented, but the examiner had not personally observed the HSM signing operation and did not warrant the substrate-trust assumption beyond what the artifacts could carry. The §10.12 exit-code contract made the distinction explicit.

DeShawn pulled the disclosure-subtree verifier and ran it against the first §1033 disclosure from Day 1 (member `mbr-91842`, ~9,400 chain rows spanning the vendor handover):

```
$ herald-verify --tenant=hillcountry \
                --service=disclosure-fulfillment \
                --customer-anchor=mbr-91842 \
                --start=2025-06-15 \
                --end=2026-05-22 \
                --1033-disclosure \
                --witness-mode \
                --strict
```

```
Status: PASS-STRUCTURALLY
Step:   12
Reason: chain integrity verified against artifacts presented;
        substrate-trust assumption read from §10.5 attestation
        and §10.17 HSM partition-ceremony record;
        examiner-side verification of HSM signing operation
        deferred to artifact-based attestation
Elapsed: 14.6s
```

DeShawn nodded once. He ran the second and third §1033 disclosures on his own laptop — 14.2s and 14.9s respectively. All three returned PASS-STRUCTURALLY. He wrote three lines in his notebook and looked up at Diana.

The witness-mode walk closed the §1033 cross-cut for the engagement. DeShawn's pre-engagement file would carry the three PASS-STRUCTURALLY verdicts; his entrance meeting at the same three-week mark as NCUA's would not need a re-verification step.

*Note for the chapter. The §10.12 witness-mode discriminator is the structural feature that lets a regulator run their own verification without depending on the audit team's chain access. Under Kognitos, the framework has no exit-code contract — Field 12 (integrity proof) is a binary assertion. The witness-mode-vs-confirmed-mode distinction is invisible to Kognitos; under §10.12 it is a row-attribute discriminator on the verifier output.*

> ### ✓ Confirmation #8 — §10.12 witness-mode PASS-STRUCTURALLY discriminator exercised by CFPB §1033 examiner
> Three §1033 disclosures verified by DeShawn Bradley on his own laptop in witness-mode; 14.2-14.9 seconds each; PASS-STRUCTURALLY discriminator distinguishes structural-verification-of-artifacts from substrate-trust-from-direct-HSM-observation.

## 🔧 2:00 PM Day 2 — MRM-committee memo on cross-vendor model-card lineage

After lunch on Wednesday, Rajiv Khanna walked the MRM-committee memo with Karen Yoo. The committee meeting was the following Tuesday; the memo needed to land on the chain as `chain.coverage_map_published` with the AIRES Module 8 crosswalk attached.

The memo walked the §10.66 model-weight lineage DAG for both the marketing-scoring and credit-scoring model families. Marketing-scoring had three legacy Total Expert ancestors and one new in-house ML descendant; credit-scoring had two legacy ancestors and one new descendant. Six retrain events across the two families; each retrain event in the chain with parent-model linkage, retrain-event timestamp, and training-data-manifest hash.

Rajiv added the MRM committee's standing question — whether the in-house ML scoring layer's training data contained any features derived from the legacy Total Expert model's output predictions, which would create a model-on-model dependency that complicated risk-attribution. Karen confirmed it did not — the in-house ML scoring layer trained from first-party Hill Country member data and a fresh set of derived features built from raw transaction history; no Total Expert prediction outputs fed the training set. The chain's training-data manifest hashes confirmed this from the training-data manifest side; the lineage DAG confirmed it from the model side.

The memo went into the chain at 2:48 PM as `chain.coverage_map_published` event under §10.2 operational events, with the AIRES Module 8 crosswalk attached as an `audit.external_artifact.*` reference.

*Note for the chapter. The MRM-committee memo is one of the engagement deliverables that lands in the chain itself as an operational event under §10.2. Under Kognitos, the memo would be out-of-chain documentation; the operational-event chain inscription is structural-property of the reference spec that Kognitos cannot carry.*

## 🌆 5:30 PM Day 3 — Engagement close

Thursday morning had been the close-out session with Toby Reinhardt and Beth-Anne Coker — internal-audit sign-off on the spec-section confirmation memos, Toby's countersignature on the AIRES workpaper composition, Beth-Anne's countersignature on the §10.21 vendor-handover memo. Marcus Edenfield had emailed his final Total Expert cooperation attestation at 11:48 AM CT, with the four-year escrow access credentials renewed and the dual-signature pair index from §10.17 written through to the chain.

By 4:30 PM Thursday the three days had closed at 22% under budget. The MRM-committee memo had landed in the chain on Wednesday afternoon as `chain.coverage_map_published`; the §10.21 confirmation memo had gone into Linda Cantwell's pre-engagement file Wednesday morning; the §10.69 confirmation memo had gone to DeShawn Bradley after the Wednesday witness-mode walk; the §10.11.1 ECOA confirmation memo had gone to Stuart Maples at 3:15 PM Thursday for the next CCO-committee packet. Toby Reinhardt countersigned the engagement-summary memo at 4:42 PM, sliding it across the conference table to Dawn with no words and a small nod. The CAE's six-month boundary anxiety closed in that nod.

No public statement. No on-the-record demand. No press release. Just the memo handed across the conference table, a brief paragraph of internal-audit-committee text for the next-quarterly board packet, and the engagement-file note about substrate-move sitting quietly in Dawn's engagement file for the engagements that would follow.

The audit team flew back to Austin-Bergstrom Friday morning. The chapter is the first since Ch03 to close without an explicit framework-substitution demand or sharper-dimension addition. The engagement-file note about substrate-move is the chapter's only forward-looking signal; it sits in Dawn's engagement file under the timestamp 17:02 CT, Day 1.

## 🧾 Final Assessment Theme

> "Hill Country Federal Credit Union produced the cleanest deliverable in the program so far — eleven months chained, four `service.name` values, single AWS substrate, single HSM root, vendor handover from Total Expert to HubSpot + in-house ML at twenty-three weeks, byte-equal hash join across the handover boundary reproducing in under nine minutes, ECOA marketing-event-to-credit-decision parent-linkage chain pivot verified across five members, §10.69 per-customer disclosure subtree spanning the cross-vendor anchor leaf in under fifteen seconds, NCUA AIRES workpaper composition translating cleanly from spec-section references, CFPB §1033 witness-mode PASS-STRUCTURALLY verification in under fifteen seconds, no findings, no partials, no new framework inarticulabilities, no new framework under-reportings. Under Kognitos the deliverable carried four new Framework-Silent Observations — single-substrate single-organization §10.21 form as canonical reference shape (vs Ch11's cross-organizational variant); §10.66 model-weight lineage DAG; §10.11.1 ECOA prior-offer parent-linkage chain pivot across vendor handover; §10.69 + §10.21 disclosure subtree composition — none of which produce framework-substitution demands because the engagement closed clean on the chain side. CAE Tobias Reinhardt's six-month boundary anxiety closed quietly. The chapter's only forward-looking signal is the engagement-file note that lead auditor Dawn wrote for herself at five o'clock on Day 1: '§10.40 anchor reads as routine on AWS-only. Open question for the next pass: what happens when the substrate moves?' This is the foresight-cluster opener for the engagement chain that follows; the note carries no public weight at the time of filing."

## Research takeaway

Hill Country FCU is the first **confirmation-posture engagement** in the program since Ch03 — the chain closes clean, the framework closes clean, no Findings, no Partials, no new Framework Inarticulabilities, no new Framework Under-Reportings, no on-the-record framework-substitution recommendation. Under the four-chapter framework-grows-vs-fixed pattern from Ch08-Ch11, this chapter breaks the consecutive §12 amendment streak: no engagement-source amendments land. The §12 streak ends at four (seven engagement-source amendments across NetiVa + Sun-Won + Salt Pond + Eberhardt × Lumière); Hill Country is the first chapter where the chain runs cleanly enough that no spec-body amendment surfaces.

The new dimensions Hill Country contributes:

- **Single-substrate single-organization §10.21 cross-vendor model-handover** as the canonical reference shape, contrasting with Ch11's cross-organizational variant. Both shapes are admissible under §10.21; the reference spec distinguishes them via the `handover_kind` attribute (`vendor_replacement_within_substrate` vs `cross_organizational_partnership`); Kognitos's Field 12 reads identically against both shapes. This sharpens the §10.21 family's structural taxonomy — the engagement is the canonical "vendor-replacement within one institution's substrate" reference.
- **ECOA marketing-event-to-credit-decision parent-linkage chain pivot** as a new Framework-Silent Observation. §10.11.1's `prior_offer_run_id` + `prior_offer_seq` bind the legacy-vendor era's marketing offer to the new-vendor era's credit decision under MAC; the binding spans the vendor handover; the ECOA defense rests on the binding; Kognitos's per-row architecture cannot carry the cryptographic parent-binding.
- **§10.69 disclosure subtree spanning §10.21 cross-vendor anchor leaf** as a new Framework-Silent Observation. One §1033 disclosure returns one unified per-member audit trail across both vendor eras; the structural property is the §10.69 + §10.21 + §4.2 composition; Kognitos cannot articulate the unified-subtree property as a single deliverable.
- **Model-weight lineage DAG resolution under §10.66** as a new Framework-Silent Observation. Three-minute lineage walk back through three retrain ancestors to the original 2024 launch model; the DAG is row-attribute-structured under §10.66; Field 4 names the current model and nothing names the ancestors.
- **Confirmation-posture-without-stakeholder-statement** as a new chapter-class. Eight prior chapters from Ch04 onward produced explicit on-the-record stakeholder statements; Hill Country closes without one. The CAE's boundary anxiety closed quietly. This is the first chapter since Ch03 without a formal stakeholder voice; future confirmation-posture engagements may produce similar patterns.
- **Foresight-cluster opener** as a new chapter-role. Dawn's engagement-file note ("§10.40 anchor reads as routine on AWS-only. Open question for the next pass: what happens when the substrate moves?") is filed quietly and carries no public weight at the time of writing. The question becomes the wishlist seed for §10.40's cross-cloud extension that lands a few engagements later. The chapter's only forward-looking signal is the note; the chapter operates as the structural opener of the foresight cluster (Stories 12-17).

The program-level pattern this chapter establishes: not every engagement produces a framework-substitution demand. When the chain runs clean on a single substrate within a cooperative vendor-replacement handover, the framework records clean too. The cost of the framework is not zero — four new Framework-Silent Observations land — but the cost does not rise to the level of an on-the-record stakeholder demand. The chapter sets up the comparison axis: confirmation-posture engagements vs the seven prior framework-substitution-demand engagements. Foresight-cluster engagements that follow may press the question Dawn filed quietly today.

---

*Running counts and program-level signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
