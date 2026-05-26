# 10 — Salt Pond Toys (Kognitos-lens)

*An engagement where four audiences with four deliverable shapes — CPSC cooperative-agreement, CBP CTPAT four-year revalidation, Rhode Island AG paperwork-only consumer-protection lookback, and Target supplier-recall-readiness — read the same chain across three time zones and force the audit team to articulate, four times in four shapes, what the framework cannot put into one row.*

**Engagement:** Multi-location consumer-products recall-readiness audit composing CPSC cooperative-agreement annual scope (closing a 2024 "recoverable rather than producible" inquiry on a false-alarm lead-paint scare), CBP CTPAT four-year revalidation due in nine months, Rhode Island AG paperwork-only consumer-protection lookback, and Target supplier-audit contractual 24-hour recall window.
**Client:** Salt Pond Toys — mid-size consumer-products manufacturer (~$320M revenue) — Newport HQ + Shenzhen QC office + Trans-Pacific Logistics LA + three Guangdong contract factories. Eleven months of chain instrumentation across four `service.name` values under one tenant: `qc-vision-shenzhen`, `customs-entry-la`, `demand-forecast-newport`, `recall-traceability`. Daily Ed25519 seals on AWS CloudHSM `us-east-1`.
**Status:** Chain in production eleven months. Four audiences arrive in eleven consecutive days starting Tuesday. The 2024 inspector's closing memo — *"best characterized as recoverable rather than producible"* — sits at the top of CPSC's open-file folder on Frances Whittaker's desk.
**Audit team lead:** Dawn
**Client liaison:** Patrick Cavanaugh (Chief Risk Officer); Naomi Briggs (General Counsel); Hugo Vinciguerra (Chief Technology Officer); Rajiv Mahadevan (AI/ML Officer); Audrey Saunders (VP Operations); Sophia Carmichael (Vendor Management); Ling Wei (QC Supervisor, Shenzhen); Tao Zheng (Shenzhen ML deployment lead); Marisol Reyes (LA customs broker liaison, Trans-Pacific Logistics); Frances Whittaker (CPSC inspector, observing combined engagement); Greer Pendleton (Rhode Island AG paperwork reviewer, arrives day three).

**Audit team's framework:** Kognitos's 12-field schema. The team is now ten engagements in. Multi-location is new — three time zones live on video tiles in the same room. Multi-audience is new at this density — four deliverable shapes from one chain. The chain-coverage boundary question (where does the chain end and where does someone else's audit begin?) is going to land squarely on a Field-2 actor-identity row and bend it.

---

## 🌅 8:30 AM ET — Kickoff (Newport HQ + LA tile + Shenzhen tile)

The audit team arrived at Salt Pond's Newport HQ at quarter past eight on Tuesday. The team split before the kickoff: Dawn, Mike, Chen, and Elena took the Newport room; Diana joined on the LA video tile from Trans-Pacific Logistics' broker office in Long Beach; Luis joined on the Shenzhen tile from Salt Pond's QC office in Futian. The LA tile showed Marisol Reyes already at her customs desk, mug in hand, eight hours into her shift. The Shenzhen tile showed Ling Wei and Tao Zheng — eight-thirty PM their time, an unusual courtesy.

Patrick Cavanaugh opened. The four-audience engagement was unusual — CPSC's annual cooperative-agreement review starting the following Tuesday, CBP CTPAT four-year revalidation in nine months, Rhode Island AG's paperwork-only lookback opening day three, and Target's supplier-audit reviewer reading the deliverable as soon as it landed. One chain, four deliverable shapes, eleven days. Frances Whittaker — CPSC's inspector — was sitting in to observe how Salt Pond's chain instrumentation answered her predecessor's 2024 closing memo. The phrase *"recoverable rather than producible"* had a specific meaning in CPSC parlance and a specific cost: the 2024 inquiry had cost Salt Pond eighteen months and a seven-figure outside-counsel bill on a false-alarm lead-paint scare that the chain — had it existed — would have closed in an afternoon. The chain existed now. Frances would watch them prove it.

Naomi Briggs added the litigation-defense layer. Two FRE 902(13) and (14) self-authentication postures sat behind the engagement: the Rhode Island AG paperwork-only lookback could, on its own findings, escalate to a consumer-protection action, and Target's supplier-agreement carried a contractual indemnification clause that triggered on documentation failures in the 24-hour recall window. Naomi wanted both backed by the engagement deliverable. Dawn nodded — best-evidence posture under federal evidence rules was a strict reading of what the chain had to do, not just what the framework labeled it.

Rajiv Mahadevan walked the four chain instruments. The QC vision model — in-house, trained on internal defect labels across forty-two SKU families — flagged plush-bear units at the Dongguan contract factory under Ling Wei's supervision. The customs-entry pipeline — a third-party broker AI handling HTS classification for Trans-Pacific's filings — ran under Marisol's review at LA. The demand-forecast model — a Newport-side in-house model on six-month rolling actuals — ran daily. The recall-traceability tool walked the chain when called. Eleven months of operation. Daily HSM seals at the eastern close. *Note for the chapter. Four services, three locations, four audiences, one chain. The team has not yet seen a row that named where the chain ended and someone else's audit began. They are going to see one before lunch.*

> ### ✓ Confirmation #1 — Field 1, 2, 3, 4 satisfied across the four chain instruments under one tenant boundary
> The kickoff walked deployment-intent, model identification, and policy versioning across all four `service.name` values under the `saltpond` tenant. Production intent on every instrument, version pins on every model, eleven months of operational continuity. Kognitos Fields 1-4 are answerable for every entry the chain produced.

> ### ✓ Confirmation #2 — Field 12 satisfied; HSM-rooted daily seals on AWS CloudHSM `us-east-1` for 322 consecutive daily seals
> Mike pulled the daily-seal index. The chain has produced 322 consecutive daily seals across eleven months with zero rotation events and zero algorithm changes. Tamper-evident integrity proof is straightforwardly demonstrable.

## 🧬 9:30 AM — Plush-bear demand-forecast verifier exercise

Mike pulled a March 21 demand-forecast for the plush-bear SKU family — six months of rolling actuals fed into the Newport-side forecast model, output a re-order recommendation for the Dongguan contract factory.

```json
{
  "entry_id": "saltpond/demand-forecast-newport/2026-03-21#147",
  "tenant": "saltpond",
  "service": "demand-forecast-newport",
  "seq": 147,
  "ts": "2026-03-21T16:42:08.137Z",
  "model_id": "forecast-plush-v3.2",
  "model_version": "3.2.0-prod-pin-2026-01-14",
  "gen_ai.request.model": "internal/forecast-plush-v3.2",
  "gen_ai.response.model": "internal/forecast-plush-v3.2",
  "prompt": {
    "sku_family": "plush-bear-12in",
    "window_actuals_180d": "...redacted...",
    "seasonality_index": "Q2-spring",
    "retailer_demand_signals": "..."
  },
  "response": {
    "recommendation": "reorder_31000_units_dongguan_factory_3",
    "confidence_band": "p50=31000; p10=24500; p90=39200",
    "lead_time_assumed_days": 32
  },
  "audit.deployment.intent": "production",
  "audit.deployment.policy_version": "demand-forecast-policy-v2.1",
  "payload_hash": "0a8f...c421",
  "hmac": "d5...e7",
  "merkle_path": ["...", "..."],
  "daily_seal_ref": "saltpond/2026-03-21#seal"
}
```

Mike ran the verifier:

```
$ herald-verify --tenant=saltpond \
                --service=demand-forecast-newport \
                --date=2026-03-21 \
                --entry-id=147 \
                --strict
```

Four seconds.

```
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified
        against public key fp:b4:e9:...:71
Elapsed: 4.1s
```

Frances Whittaker watched the verifier output. The forecast had recommended 31,000 plush bears. The Dongguan factory had run that day and produced exactly 31,000. The chain held a structural record of what the forecast said. *Note. Field 6 (output) carries the recommendation; Field 7 (decision) carries the auto-acceptance disposition. Field 11 (approval) is the lead-time gate review by Audrey. The framework can answer "what did the AI say on March 21?" cleanly.*

> ### ✓ Confirmation #3 — Field 5, 6, 7, 8 satisfied on the demand-forecast walk; the auditor can reconstruct the AI's claim
> One forecast, one factory, one production run, one chain row. The framework can answer the simple question: what did the AI recommend, and what was the human disposition? Both rows are present. The chain row backs the answer.

## 🚨 10:30 AM — The factory-floor operator question

Frances raised her pen. She had a question about Field 2 — actor identity.

The chain entry for the QC vision model named Ling Wei as the supervising actor for the Dongguan flagged-unit dispositions. Frances had a follow-up: the operator on the factory floor who actually pulled the flagged unit off the line and routed it to rework or scrap — who was that, and where did Kognitos record it?

Luis, on the Shenzhen tile, walked the answer carefully. Ling supervised the QC vision workflow remotely from the Shenzhen office — she received the model's flags, reviewed them on her dashboard, and assigned dispositions. Each flagged unit was then handled by an operator on the contract factory's floor, under the factory's separate badge-and-access-control system. Salt Pond did not own or operate the factory; it had a contract relationship with Dongguan Factory 3, which had its own access controls, its own personnel records, and its own internal audit.

So the actor-of-record in the chain is Ling. The factory-floor operator is in someone else's system.

Frances asked the obvious question: how does CPSC know the floor operator actually did what Ling assigned? Audrey Saunders fielded it. The contract included an inspection-rights clause and a quarterly contract-compliance review run by the Shenzhen office staff. The floor operator's badge log lived in the factory's access-control system, and the contract gave Salt Pond pull-access on request.

Frances looked at Dawn. Dawn looked at Chen. Chen had been quiet most of the morning. *Note for the chapter. Field 2 has a name on it — Ling. The actor it does NOT have a name on is the floor operator. The contract-clause review and the inspection right are the substitute, but Kognitos Field 2 has no row for "actor is structurally outside the chain by design, here is the substitute audit procedure that takes its place." There is no field that can carry the boundary itself. There is no field that can carry the contract-inspection right that substitutes for it.*

> ### ⚠ Framework Inarticulability #6 — Chain-coverage boundary cannot be filed under any Kognitos field
> The factory-floor operator is structurally outside the chain by design. The Shenzhen office's quarterly contract-compliance review is the substitute audit procedure. Kognitos Field 2 (actor identity) names Ling Wei as the supervising actor. There is no field that can carry the boundary itself — the row that says "actor at this step is in the contract factory's separate access-control system; the substitute audit procedure is the quarterly contract-compliance review under inspection clause §4.7 of the supply agreement." Speculating the operator into Field 2 with a fabricated "role: contractor" tag would falsify the structural relationship. Speculating a free-text rationale into Field 8 would leak the boundary into the wrong field. The framework cannot articulate where the chain ends and someone else's audit begins.

Chen wrote it on the back of his notepad. *No field for chain-coverage boundary. No field for substitute audit procedure. No field for contract-inspection right.*

## 🛡️ 11:00 AM — Naomi's §1.2 boundary

Naomi stepped into the silence with a question that Dawn had been waiting for since the kickoff.

She wanted to understand exactly what the chain proved. The Rhode Island AG lookback was paperwork-only — no enforcement action open, no consumer complaint pending — but if a complaint did open and escalated, Naomi wanted to know the limits of what the deliverable could say. Specifically: did the chain prove that lot 25-D-0492 was defect-free, or did it prove that the QC vision model said the units it sampled passed?

Dawn answered directly. The chain proved what the AI said. The chain held a structural record of every flagged unit and every disposition. It did not, on its own, prove that the un-flagged units were defect-free; that proof would require additional physical evidence — destructive testing, lab analysis, the CPSIA certificate from Bureau Veritas. The chain proved the AI's claim. Other evidence proved the physical state.

Naomi nodded slowly. That was exactly the boundary she needed for the FRE 902(13) and (14) self-authentication posture. The chain self-authenticated as an electronic record of what the AI said. It did not self-authenticate as proof of ground truth. *Note for the chapter. The team has had this conversation three times now under three different stakes shapes — Helmstad's clinical-validation stakes, Pacific Crescent's public-safety stakes, and now Salt Pond's consumer-products litigation-defense stakes. Each time the framework leaves the boundary unstated. Each time the stakeholder has to articulate it herself, in her own words, for the specific posture she is defending.*

> ### ⚠ Framework Inarticulability #7 — Epistemic-scope boundary (variant: litigation-defense / FRE 902(13)(14) posture)
> The chain proves what the AI said about lot 25-D-0492; it does not prove the lot was defect-free. This boundary is the structural meaning of FRE 902(13) self-authentication — the electronic record self-authenticates as record; the underlying truth requires other proof. Kognitos has no field that articulates this boundary. The auditor is left with Field 6 (outputs) carrying the AI's claim and no structural label distinguishing "what the AI said" from "what is true." For litigation-defense framing, this is the boundary the General Counsel needs in writing. The framework cannot put it there.

## ⚡ 11:30 AM — CES inspection notice gap

Diana, from the LA tile, pulled a March 27 customs entry summary for a Trans-Pacific shipment of plush bears and pulled a thread.

She walked the verifier on the HTS classification entry — a broker AI had classified the line under HTS 9503.00.00 and Marisol had overridden it to 9504.40.00 per a CBP ruling letter from 2023. The verifier produced PASS in three seconds; the override was a chain row with the override rationale ("CBP HQ ruling #H312045") in the chain entry, the classifier_output flag set, and Marisol's actor identity present.

Diana then asked about the customs handoff in the Yantian port leg. The maritime leg from Yantian to LA was on a bonded carrier — a CBP-supervised chain — and the chain ended at the Yantian gate-out event and resumed at the LA receipt event. The CES inspection notice (Container Examination Station notice from CBP Los Angeles) was a paper artifact (well, a signed PDF) that documented any inspection event during the LA leg. Marisol kept the PDFs in a Descartes-managed broker filing system.

Diana asked the question: where in the chain row was the CES notice anchored?

Marisol paused. The answer was — nowhere. The CES notice lived in the Descartes filing. The chain row for the customs entry summary did not carry a hash of the CES notice. If CBP CTPAT came and asked to verify the bonded-carrier handoff under sealed inspection, the auditor would have to retrieve the CES notice from Descartes, compute its hash, and verbally vouch that it was the one that applied to the chain row in question.

Dawn looked at Chen. Chen wrote on his notepad. *No field for external-artifact hash anchor. No field for "received_at_utc" of the external artifact. No field for "source_party = CBP_LA." No field for evidentiary_role = "chain_of_custody_handoff."* The closest Kognitos field was Field 4 (tools/models used) — but the CES notice was neither a tool nor a model. The next closest was Field 12 (integrity proof) — but Field 12 named the chain's own seal, not an externally-signed third-party artifact hash-anchored into the chain.

> ### 🚨 Framework Under-Reporting #8 — External-artifact hash anchoring has no Kognitos field
> Reference spec attribute family `audit.external_artifact.*` (six attributes: kind, identifier, sha256, received_at_utc, source_party, evidentiary_role) carries the CES inspection notice as a hash-anchored row alongside the chain entry. Kognitos has no field that does this. The auditor must speculate the notice into Field 4 (tools/models) — a falsification — or invent a free-text rationale in Field 8 (reasoning). Either choice produces a deliverable that does not match what CBP CTPAT will ask for at revalidation. The reference spec drove this attribute family into the spec body as a worked example from this engagement; Kognitos cannot grow to meet the same need.

## 🔧 1:00 PM — Shenzhen tile: contract-compliance review walkthrough

After the lunch break, Luis walked the Shenzhen quarterly contract-compliance review with Ling and Tao. The review ran every quarter — Salt Pond's Shenzhen office staff (six people, all under the office director) visited each of the three Guangdong contract factories on a rotating schedule, audited the factory's access-control logs against the chain's flagged-unit dispositions, sampled factory operator badge swipes against expected handling timestamps, and produced a quarterly memo signed by the office director and counter-signed by the factory's QA manager.

The 23 credential rotations across eleven months were all in scope of the quarterly review. The factory-floor operator badge boundary was structurally documented in the contract — clause §4.7 of the supply agreement, naming the inspection right, the quarterly cadence, and the substitute audit procedure. The contract itself was a document, not a chain row. The contract reference was in the chain entry as a free-text annotation: `audit.note = "see supply-agreement §4.7 for chain-coverage boundary at factory-floor handling"`.

Dawn watched. The contract reference was carried as a free-text Field 8 (rationale) annotation. That worked for now — the auditor reading the chain could follow the breadcrumb — but it was a structurally weak anchor. The contract document itself was not hash-anchored. If the contract was amended (which had happened twice in the eleven-month window), the chain rows that referenced it did not get updated.

> ### 🚨 Finding-001 — Contract reference for chain-coverage boundary is a free-text Field 8 annotation with no hash anchor
> The supply agreement §4.7 — the document naming the chain-coverage boundary, the inspection right, and the substitute audit procedure — is referenced by free-text annotation in chain entries. The reference spec would carry this under `audit.external_artifact.kind = "supply_agreement"` with `sha256` and `received_at_utc` attributes, version-stamped and re-anchored when the contract amends. Kognitos's free-text annotation in Field 8 cannot version-stamp and cannot re-anchor on amendment. The Field 8 annotation is at risk of stale reference whenever the contract amends.

> ### ✓ Confirmation #4 — Substitute audit procedure is operationally sound; the gap is documentary, not procedural
> The quarterly contract-compliance review is operationally well-executed. Eleven months of quarterly memos, all signed and counter-signed, all sampling the right scope. The procedural substance is there. What is missing is the structural label that names the substitute procedure in the chain. The work is being done; the framework cannot articulate that it is being done as a substitute for what would otherwise be a chain-coverage row.

## 🔧 2:30 PM — Bureau Veritas CPSIA cross-vendor anchor walk

Sophia Carmichael walked the Bureau Veritas anchor with Dawn and Mike in the Newport room. Every Salt Pond SKU shipped to retail required a CPSIA Section 102 testing certificate from a CPSC-accredited third-party lab. Salt Pond used Bureau Veritas as its primary lab. Each CPSIA certificate was a signed PDF (Bureau Veritas PGP signature) plus a chain row in the `recall-traceability` service that hash-anchored the certificate's SHA-256 alongside the lot identifier.

The auditor walked one certificate end-to-end — a CPSIA cert for lot 25-D-0492 (the plush-bear lot that would feature in the recall-readiness exercise that afternoon). The PGP signature verified against Bureau Veritas's published key. The SHA-256 in the chain row matched the SHA-256 of the signed PDF byte-for-byte. Two independent integrity proofs co-validated the certificate.

Mike asked the structural question. The Bureau Veritas anchor was an *independent third-party institutional anchor* — Bureau Veritas was not under Salt Pond's tenant, was not party to the chain, and provided integrity proof through its own institutional cryptographic posture. The chain held a hash that pointed to the same artifact Bureau Veritas pointed to. Two independent paths to the same artifact.

Where, in Kognitos, did this co-anchoring live?

Chen wrote on the notepad. Field 12 (tamper-evident integrity proof) named the chain's own seal. There was no Kognitos field that named an independent third-party institutional anchor co-validating a hash. Field 4 (tools/models used) was wrong by structure — Bureau Veritas was not a tool. Field 11 (approval/oversight) was close but wrong — Bureau Veritas was not Salt Pond's oversight body; it was an independent lab.

> ### 🚨 Framework Under-Reporting #9 — Cross-vendor independent institutional anchor has no Kognitos field
> The reference spec carries this under §10.21.1 (anti-counterfeit sample-based-attestation extended to institutional analogs) and §10.60 (anti-counterfeit cross-anchor). Bureau Veritas's CPSIA-cert PGP signature is the canonical institutional analog for the spec section. The cross-vendor anchor is a structural property — two independent integrity proofs reaching the same artifact from two unrelated institutional postures. Kognitos Field 12 names one. There is no field that names the second.

## ⚡ 3:30 PM — Section 321 broker manual-step pull

Diana, from the LA tile, surfaced the harder one.

Section 321 de-minimis filings — the under-$800 shipment exemption — went through a broker manual-step that took anywhere from 90 seconds to twelve minutes to clear. Marisol's broker workflow was: she received the shipment manifest, ran the broker AI for the initial classification, saved an intermediate state in Descartes, walked the manifest visually for any anomalies, and then submitted the final ABI (Automated Broker Interface) filing to CBP.

The chain entry for a Section 321 manual-step disposition had two timestamps: `intermediate_at` (when the broker AI completed and Marisol saved) and `submitted_at` (when Marisol submitted to ABI). The disposition between those two timestamps was a manual visual review — not in the chain.

Diana asked the question: how does Kognitos record that the chain row is *not yet complete* — that there's a known manual step between two timestamps where the auditor cannot speak to what happened?

Chen wrote on the notepad. Field 7 (decisions made) carried the broker AI's initial classification. Field 7 did not carry an `intermediate_state` boolean — there was no row in Kognitos that distinguished "the AI completed and the human is still working" from "the AI completed and the human is done." Field 11 (approval/oversight) was wrong by timing — the human's approval was the *closing event*, not the *intermediate state*. Field 10 (errors/exceptions) was wrong by category — this wasn't an error.

> ### 🚨 Framework Under-Reporting #10 — `intermediate_state` boolean for long-running multi-step external interactions has no Kognitos field
> Reference spec carries `audit.external_artifact.intermediate_state = true` as a boolean attribute distinguishing a broker-saves-at-T1 state from a broker-submits-final-ABI-at-T2 state. The two-state distinction is the worked example for the spec section. Kognitos has no field that articulates the open-vs-closed state of a long-running multi-step external interaction. The auditor reading a Section 321 entry without the intermediate_state flag cannot tell whether the row is provisional or final.

Marisol added the operational dimension. The 90-second-to-twelve-minute window mattered for the customs filing — if CBP queried during the intermediate state, the broker's answer was different from the answer during the final state. The chain had to be readable to know which state was in scope at query time.

## 💳 4:30 PM — Recall-readiness exercise on lot 25-D-0492

Audrey Saunders started the recall-readiness exercise from a cold pick. The lot identifier — 25-D-0492 — was drawn from Audrey's hat (literally, a small bowl of paper slips). Three thousand eight hundred and forty units. Forty-seven retailers. The Target supplier-agreement contractual window was 24 hours from notification to delivery of a complete reconciliation.

Audrey hit the timer.

Mike ran the recall-trace tool against the `recall-traceability` service. The tool walked:
- Newport demand-forecast entry that authorized the production run (1 chain row)
- Shenzhen QC vision flagged-unit dispositions (47 flagged units across the lot — 43 rework, 4 SCRAP_EYE_ATTACHMENT)
- Dongguan factory production manifest cross-anchored to the QC dispositions
- LA customs entry summary for the import (1 chain row + Bureau Veritas CPSIA cross-anchor)
- Newport receipt and retailer distribution split (47 retailer routings, each its own chain row)

Total chain rows: 96. Verifier produced PASS across all 96 in 22 seconds. The recall-trace tool produced a complete cross-location, cross-service trace with retailer-level resolution.

Audrey stopped the timer. Fourteen minutes from cold pick.

The 2024 inspector's closing memo — *"best characterized as recoverable rather than producible"* — had named the structural failure. In 2024 Salt Pond had been *recoverable* (could, given enough lawyer-hours, reconstruct the chain of evidence from paper records and ERP logs) but not *producible* (could not, in any operationally sensible window, produce that chain). The 2026 chain test produced the trace in fourteen minutes. The structural distinction had closed.

Frances watched the exercise. She did not speak for a long beat. Then she asked Dawn a question.

She asked how Kognitos articulated the fourteen-minute property. Was there a field that recorded "produced cross-location cross-service reconciliation in 14 minutes"? Was there a field that captured the operational property the 2024 inspector had been asking for?

Dawn answered honestly. Kognitos's twelve fields were per-event. None of the twelve fields aggregated across a lot to record a cross-location reconciliation property. The fourteen-minute property was a *structural property of the chain* — that the chain rows were sequenced, hashable, verifier-walkable in cross-service joins, and reconcilable at lot resolution. Kognitos could record each individual event in each individual chain row but could not articulate the *structural property* that made the fourteen-minute reconciliation possible.

> ### ◇ Framework-Silent Observation #4 — Cross-location cross-service recall reconciliation as a structural property
> The reference spec carries the structural property through §10.19 (chain-coverage map), §10.18 (CC8.1 runbook cross-referencing), §10.21.1 (cross-vendor anchor), and §4.4.6 (connector-source attribution) — the *combination* of these sections makes the 14-minute property a reproducible operational outcome. Kognitos can record what happened in each row. It cannot articulate the structural property that produced the 14-minute outcome across all rows. The 2024 inspector's "recoverable rather than producible" distinction lives precisely in this gap.

Frances wrote in her notepad. Dawn watched her write. *Note for the chapter. The 2024 inspector's phrase closed today, in fourteen minutes, under the chain. Under the Kognitos framework alone, the closing would have to be argued out as an editorial summary of per-row entries — not produced as a structural property. The deliverable shape is different.*

## 🌆 5:00 PM — Auditor debrief

Dawn pulled the team to the whiteboard.

```
KOGNITOS 12-FIELD ASSESSMENT — SALT POND TOYS (4 AUDIENCES / 3 LOCATIONS / 11 DAYS / 1 CHAIN)

AI SIDE — DEMAND-FORECAST + QC-VISION + CUSTOMS-ENTRY + RECALL-TRACEABILITY:
  Confirmations:                  4 (Fields 1-4, 5-8, 12, substitute-procedure operational soundness)
  Operational demonstration:      1 (14-min cross-location recall reconciliation on lot 25-D-0492)
  Partials:                       0
  Findings against bank:          1 (free-text supply-agreement reference w/ no hash anchor)
  Nits:                           0 (under Kognitos; reference spec records 0)
  Framework-silent observations:  1 (14-min recall reconciliation structural property)

CHAIN-COVERAGE / EXTERNAL-ARTIFACT SIDE:
  Framework Inarticulability:     1 (chain-coverage boundary at factory-floor operator handling)
  Framework Under-Reporting:      3 (external_artifact hash anchor; cross-vendor independent anchor; intermediate_state boolean)

EPISTEMIC-SCOPE SIDE:
  Framework Inarticulability:     1 (§1.2 boundary variant: litigation-defense FRE 902(13)(14) posture)

CROSS-AUDIENCE / FRAMEWORK-SIDE:
  Multi-audience deliverable cost: 4 parallel speculation costs (CPSC + CBP + RI AG + Target)
```

The team sat with it.

Dawn ran the framework-side observations:

1. **Chain-coverage boundary is structurally inarticulable.** The factory-floor operator under Ling Wei's supervision is outside the chain by contract design. Kognitos Field 2 has no row for "actor is structurally outside the chain; here is the substitute audit procedure." The contract-clause reference works as a free-text annotation but cannot version-stamp.

2. **External-artifact hash anchoring is structurally missing.** Three distinct cases — the CES inspection notice from CBP, the supply agreement document, the Bureau Veritas CPSIA certificate. None of these have a Kognitos field. The reference spec's `audit.external_artifact.*` attribute family folds all three under one canonical row shape. Kognitos auditor must speculate into Field 4 or Field 8 — both falsifications.

3. **Cross-vendor independent institutional anchor is structurally missing.** Bureau Veritas's PGP signature plus the chain hash is two independent integrity proofs co-validating one artifact. Field 12 names one path. There is no field for the second.

4. **Intermediate-state boolean for long-running multi-step external interactions is structurally missing.** Section 321 broker manual-step is a 90-second-to-twelve-minute window with a chain row that may be provisional or final. Kognitos has no field that articulates the open-vs-closed state.

5. **Cross-location cross-service recall reconciliation is a structural property the framework cannot articulate.** Fourteen minutes from cold pick on lot 25-D-0492. Kognitos can record each row; it cannot articulate the structural property that made the fourteen-minute reconciliation possible.

6. **Multi-audience deliverable cost is concentrated by under-reporting.** Four audiences (CPSC, CBP, RI AG, Target) each ask different shaped questions of the same chain. Each framework under-reporting becomes four parallel speculation costs — one per audience deliverable. The auditor's workload scales with the audience count, not with the engagement scope.

Chen added one more, quietly. The reference spec drove §10.19 (chain-coverage map) and `audit.external_artifact.*` into the spec body in the fourth errata. This is now the third consecutive engagement in the team's notes where the reference spec grew during or directly after the audit. The spec's change-log mechanism produced the growth. Kognitos's twelve fields produced no growth. The framework's fixed-row architecture is at this point a documented design choice that the audit team has observed three times in three consecutive engagements.

## Stakeholder statement — Patrick Cavanaugh, co-signed by Naomi Briggs

Patrick came back into the room at six-fifteen, after he had read the whiteboard. Naomi followed him in five minutes later, after she had read the same whiteboard and Patrick's note on top of it.

Patrick spoke first. He wanted to put a sharper dimension on the framework-substitution conversation that he had been told the team had been having across prior engagements. He had read Pankaj Iyengar's statement from the Netiva engagement notes and Min-seo Kang's joint statement from the Sun-Won engagement notes — both of which sat in the cross-vendor reference file that Sophia Carmichael's vendor-management group maintained. He wanted to add the dimension that the Salt Pond engagement uniquely surfaced.

The Salt Pond engagement was four audiences in eleven days. Each audience read the same chain. Each audience asked differently-shaped questions. Under a framework that under-reports — that has six structural gaps the auditor has to speculate around — each gap multiplies by four. Salt Pond did not pay one speculation cost; Salt Pond paid four parallel speculation costs, one per audience deliverable. The deliverable for CPSC was not the deliverable for CBP CTPAT; the deliverable for RI AG was not the deliverable for Target. Each audience needed a separately-shaped answer to questions the framework could not file under any structural row. Each speculation was four-times-multiplied.

Patrick was speaking on the record. *On the record:* Salt Pond would not migrate from the reference spec to Kognitos as the chain-of-custody framework. The reason was not technical preference. The reason was multi-audience deliverable cost. A consumer-products manufacturer of Salt Pond's scope — four audiences (federal regulator, customs revalidation, state AG, contractual retailer) — could not absorb the four-times-multiplied speculation cost that comes with a fixed-row framework that under-reports chain-coverage, external-artifact, cross-vendor-anchor, and intermediate-state structural properties. Patrick wanted the statement filed alongside Pankaj's and Min-seo's. The framework-substitution recommendation, in his frame, was multi-audience-cost-sharpened.

Naomi spoke second. Her dimension was litigation-defense-shaped. The FRE 902(13) and (14) self-authentication posture required the chain to self-authenticate as an electronic record. The chain did that. What the chain also had to do — and what Kognitos's framework could not do under any reading — was carry the epistemic-scope boundary cleanly. The chain proved what the AI said about lot 25-D-0492; it did not prove the lot was defect-free. Under the reference spec, §1.2 named this boundary. Under Kognitos, the boundary was structurally inarticulable. If RI AG opened a consumer-protection action that turned on the AI's claim being treated as proof of physical state, Naomi could not let her best-evidence chain be backed by a framework that had no structural label distinguishing claim-vs-truth. The litigation-defense posture required the boundary in the framework, not in the closing argument.

Both signed.

Dawn replied: *"On the record."*

## 🧾 Final Assessment Theme

> "Salt Pond Toys produced a clean four-audience deliverable on the chain side — four service instruments, eleven months of operation, fourteen-minute cross-location recall reconciliation on a cold-pick lot, daily HSM seals across three time zones, Bureau Veritas cross-vendor anchor verified end-to-end. Under Kognitos, the deliverable carried one Finding (free-text contract reference with no hash anchor), three Framework Under-Reportings (external-artifact hash, cross-vendor independent anchor, intermediate_state boolean), two Framework Inarticulabilities (chain-coverage boundary, §1.2 litigation-defense variant), and one Framework-Silent Observation (14-minute reconciliation as a structural property). Patrick Cavanaugh and Naomi Briggs co-signed the third framework-substitution recommendation in the program, multi-audience-cost-sharpened: a fixed-row framework that under-reports four structural properties multiplies its speculation cost by the audience count. Reference spec's fourth errata — §10.19 chain-coverage map and `audit.external_artifact.*` attribute family — was driven into the spec body as a direct outcome of this engagement. The framework grew. The framework with twelve fixed fields did not."

## Research takeaway

Salt Pond Toys is the third consecutive engagement to drive content into the reference spec body during or directly after the audit cycle. Netiva drove §10.17 (HSM partition-ceremony attestation). Sun-Won drove §4.4 (cross-border-transfer attribute family) and §4.4.1 (sixth event type `audit.routing.classifier_output`). Salt Pond drove §10.19 (chain-coverage map) and `audit.external_artifact.*` (six-attribute family for hash-anchored external artifacts). Five engagement-source amendments in three consecutive chapters. The framework-grows-vs-fixed contrast is now the most reproducible signal in the program.

The new dimensions Salt Pond contributes:

- **Multi-audience deliverable cost** as a sharpening of the framework-substitution recommendation. Pankaj (Netiva) named the recommendation. Min-seo and Wei-ling (Sun-Won) cross-jurisdicted it. Patrick (Salt Pond) added the multi-audience multiplier: speculation cost scales linearly with audience count under fixed-row frameworks.
- **Chain-coverage boundary** as a new inarticulability class. Where prior chapters' inarticulabilities sat at the §1.2 epistemic-scope boundary (what the AI said vs what is true) or the §1.4 substrate boundary (compositional security in cryptographic terms), Salt Pond's inarticulability sits at the *contract-coverage* boundary: where the chain ends and someone else's audit begins, with a named substitute procedure.
- **External-artifact hash anchoring** as a new under-reporting class — generalizing across three distinct external-artifact kinds (CES notice, supply agreement, CPSIA certificate). Kognitos cannot file any of the three under any row.
- **Cross-vendor independent institutional anchor** as a sharper variant of the integrity-proof gap. Bureau Veritas PGP plus chain hash is the canonical institutional analog driven into §10.21.1 / §10.60 from this engagement.
- **Operational property: 14-minute recall reconciliation** as a structural-property-of-the-chain observation. The 2024 "recoverable rather than producible" distinction lives in exactly this gap.
- **Multi-location operational dimension** — three time zones on three video tiles, eleven months of continuous operation. New for the program. Pattern B per-region tenant boundaries (Newport / LA / Shenzhen each region-pinned) is the architectural shape.
- **FRE 902(13)/(14) litigation-defense posture** as a new audience class. Best-evidence under federal evidence rules requires the chain to carry the §1.2 boundary in the framework, not in the closing argument.

---

*Running counts and program-level signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
