# 15 — Polaris Reinsurance × Lloyd's of London

> A Bermuda-domiciled reinsurer (Polaris Re Ltd., ~$8.4B gross written premium) and three of its largest cedents at Lloyd's of London (Syndicates 0314, 1218, 2847 — marine, aviation, and political-violence specialty lines respectively). **TesseraSeal in production for 14 months at Polaris on the cession-management and claim-adjudication path; in production for 9 months at the three Lloyd's syndicates on their cession-feed surface; chain extends across the cedent → reinsurer → retrocessionaire boundary.** A two-day pre-engagement readiness pass before the NAIC market-conduct examination wave that the reinsurance industry has been anticipating since the IAIS Basel sessions named multi-party claim-flow integrity as the next frontier. The team splits — Dawn, Mike, Diana, Tom in Hamilton, Bermuda; Raj, Elena, Luis, Chen at the syndicates' shared service-bureau in London. The audit confirms §10.43-§10.46 in production. The recusal protocol established at Northbridge is live for the first time; Mike authors the vendor-architecture sections.

## The team and the day

Eight travel; the team splits four-and-four. Dawn, Mike, Diana, Tom land in Hamilton on Sunday evening; Raj, Elena, Luis, Chen land at Heathrow Sunday morning and take the Heathrow Express into central London. Time-zone difference is 4 hours (Bermuda is AST, GMT-4; London is GMT in October). The engagement runs Monday-Tuesday; the team bridges by video twice a day during the overlap window (Hamilton 7-11 AM is London 11 AM-3 PM; Hamilton 1-5 PM is London 5-9 PM). The Tuesday close-out runs at Hamilton 11 AM / London 3 PM with all eight on the call.

Polaris's CRO is **Iyari Mendes-Webb**, mid-40s, ex-Aon, the reinsurance industry's reference voice on enterprise risk for the last decade. Lloyd's syndicate lead for the engagement is **Henry Latham**, the head of cession reporting for Syndicate 0314, coordinating across all three syndicates for the audit week. Polaris's CAE is **Alistair Quinn**.

## The drive-in monologue

```
6:50 AM Bermuda time. Dawn driving, Tom in the passenger seat. The road from
                          the Hamilton Princess to Polaris's offices in Pitts Bay.
                          Pink sand visible to the left through the casuarinas.
```

**Dawn:** "Fourteen prior engagements in the rear-view, in order. Northbridge twice — the original eighteen months ago, the M&A return two weeks back. Mercator. Stelvio. Atrio. Helmstad. Pacific Crescent. Olmstead. NetiVa. Sun-Won. Salt Pond. Eberhardt × Lumière. Hill Country. Saraswati. Northbridge return. And now — Polaris × Lloyd's."

**Tom:** "Different problem how?"

**Dawn:** "Three-party claim flow. Cedent — Lloyd's syndicate — emits a claim-state event when a covered loss is filed. Reinsurer — Polaris — picks it up under cession terms; they emit their own claim-state events for the reinsured share. If retrocession is in play the chain extends to a third reinsurer. Three independent chains, one logical claim, one regulator wanting the audit trail to be coherent across role boundaries. §10.43 normates the claim-state machine; §10.44 normates cession-cohort recursive subtree disclosure for the per-syndicate slice; §10.45 normates the independent third-party adjuster anchor; §10.46 normates bordereau integrity. All four shipped in TesseraSeal release N+1 nine months ago. Polaris and the three syndicates upgraded six months back."

**Tom:** "Recusal protocol live for the first time."

**Dawn:** "Mike authors the vendor-architecture sections; I moderate and author audit-procedure and reconciliation. Iyari and Alistair both received the engagement letter naming the authorship split. Henry got the same letter from his side."

**Tom:** "Polaris said anything about Steve?"

**Dawn:** "Iyari mentioned during the prep call that she'd been planning to invite a TesseraSeal vendor-side expert to Day 2 vendor-due-diligence. I redirected to the firm's recusal protocol. She said yes the way a senior CRO says yes — no follow-up, no surprise. She's seen our published methodology."

**Tom:** "Good."

A pause as Dawn takes the curve onto Pitts Bay Road. The Hamilton Princess is behind them; the Polaris office is a low limestone building two minutes ahead, between the harbor and the road.

**Dawn:** "Iyari also mentioned that Steve was in IAIS sessions in Basel in 2024. The reinsurance industry knew about the §10.43-§10.46 design points before the NAIC examination wave was announced."

**Tom:** "That checks the foresight pattern."

**Dawn:** "It checks the foresight pattern. Steve's working group spent two years on multi-party claim-flow integrity before this engagement was scheduled."

**Tom:** "Engagement in three minutes. We hold the line."

**Dawn:** "We hold the line. It never is."

**Tom:** "It never is."

## 7:30 AM Bermuda — Lobby, Polaris

The Polaris lobby. Limestone walls, a scale model of a 1950s Bermuda-rigged ketch behind glass at one end, a coffee station at the other. Iyari is already there, in a navy suit, with Alistair and a man in his early 40s — **Stuart Holm-Vance**, Polaris's Director of Cession Operations. The room smells of coffee and the faint salt of the harbor.

**Iyari:** "Dawn, Mike, Diana, Tom. Welcome to Hamilton. Alistair runs internal audit; Stuart runs cession operations and is the institution's chain-deployment owner. The three syndicates' lead — Henry Latham — comes on the bridge at 11 AM our time, 3 PM London, for the joint kickoff."

**Dawn:** "Thank you for the welcome. Two-day engagement. Mike will walk the §10.43-§10.46 vendor-architecture sections — that authorship split is per the recusal-protocol language in our engagement letter. I'll moderate, run audit-procedure, and own the reconciliation memo. Tom partners with Alistair on the internal-audit side."

**Iyari:** "Acknowledged. The recusal posture is documented; we expected the language. Henry's syndicates received the same engagement letter."

**Alistair:** "I've read your prior eight engagement debriefs that the project has published. The Northbridge return is the one I keep coming back to."

**Tom:** "We're here to confirm operational fidelity in production. Polaris and the three syndicates are running §10.43 through §10.46 in production. We walk it cleanly, we file the spec-section confirmation memo, the institution becomes the canonical institutional reference for multi-party claim-flow integrity."

**Iyari:** "Good. Coffee. Then the architecture walk."

## 8:30 AM Bermuda / 12:30 PM London — Joint kickoff

The kickoff bridges Polaris and the London service-bureau. Henry Latham appears on the wall screen from the syndicates' shared facility on Lime Street. Raj, Elena, Luis, Chen are visible behind him in a glass-walled meeting room. The video is steady; the bridge audio is clean.

Iyari opens.

**Iyari:** "We're walking §10.43 claim-state, §10.44 cession-cohort subtree disclosure, §10.45 independent-adjuster anchor, §10.46 bordereau integrity. Each section is in production. The audit team confirms operational fidelity. The NAIC examination wave starts in eleven weeks; we'll have the spec-section confirmation memo for the New York DFS by close of business Tuesday."

**Henry** (London): "Three syndicates. 0314 marine, 1218 aviation, 2847 political-violence specialty. Each runs the cedent surface of §10.43 — claims open on our side, the chain entries flow to Polaris under cession terms, we receive Polaris's reinsured-share claim-state events back through the bordereau cycle. The §10.46 bordereau integrity sequencing is the part of the spec we exercise hardest."

**Mike:** "Walk me through the §10.43 lifecycle. The four canonical states — opened, pending, decided, closed — and the cross-role transitions."

**Stuart** (Polaris cession operations): "Cedent emits a `chain.claim_state.transition` event when the claim opens — `audit.claim_state.from` is empty because it's the first state, `audit.claim_state.to` is `opened`, the claim's reinsured-share metadata is bound under §10.46 bordereau attributes. The cedent's chain entry's MAC is computed under their tenant key. The chain entry references the cession contract by ID. Polaris, as reinsurer, receives the bordereau and emits its own `chain.claim_state.transition` on its chain — `audit.claim_state.from` is also empty on Polaris's side because it's the first state in Polaris's chain, `audit.claim_state.to` is `opened`, and a `cross_chain_anchor.cedent_chain_run_id` field binds the cedent's chain entry by run-id and SHA-256. The verifier walks both chains and confirms the cross-anchor."

**Mike:** "And the lifecycle?"

**Stuart:** "Per §10.43: opened → pending, opened → closed, pending → decided, pending → closed, decided → closed. Closed is terminal. Reflexive transitions are admitted in non-terminal states for institution-side substate moves; we use the substate dimension for the FNOL → reserve_set → adjuster_assigned cadence inside `pending`. The high-level state stays `pending` while the substates move."

**Mike:** "Show me a chain entry."

Stuart projects a JSON document.

```json
{
  "audit.claim_state.from": "pending",
  "audit.claim_state.to": "decided",
  "audit.claim_state.from_substate": "pending.adjuster_review",
  "audit.claim_state.to_substate": "decided.reserve_finalized",
  "audit.claim_state.transition_utc": "2026-09-14T10:42:18Z",
  "audit.claim_state.actor": "polaris-claim-handler-027",
  "audit.claim_state.rationale": "Adjuster's final report received and accepted; reserve finalized at $4.2M against the marine cargo total-loss claim per cession contract terms.",
  "audit.claim_state.authorizing_policy_id": "polaris-cession-policy-v3.2",
  "audit.claim_state.authorizing_policy_sha256": "7d3a...",
  "claim.id": "POL-2026-MAR-CARGO-04127",
  "cession.contract_ref": "lloyds-0314-mar-quota-2026",
  "cross_chain_anchor.cedent_chain_run_id": "lloyds-0314-2026-08-19-claim-04127",
  "cross_chain_anchor.cedent_chain_payload_sha256": "a2e1..."
}
```

**Mike:** "Good. The cross-chain anchor binds the cedent's chain entry to Polaris's chain entry. The verifier on Polaris's side walks the cession-side; the verifier on the cedent's side walks the cedent-side; the regulator's verifier can walk both and confirm the cross-anchor matches."

**Henry** (London): "And from our side, every claim's chain entries reference the same cession contract; the substate dimension carries syndicate-specific accounting milestones. Syndicate 0314 has substates around general average and salvage that are marine-specific; 1218 has aviation-specific damage-classification substates. The high-level state stays in the §10.43 enumeration; the substates are CC8.1-named per syndicate."

**Mike:** "Walk validation?"

**Stuart:** "The state-machine primitive in `_state_machine.py` runs `validate_walk` over each claim's transition sequence. The walk check enforces no history gaps and no transitions out of terminal states. Last verifier run on the production chain over a 90-day window produced clean walks for 14,300 claims at Polaris. The three syndicates produce clean walks on their side independently."

**Dawn:** "Good. Mike, the §10.44 conversation is yours to lead. I'll moderate."

## 10:00 AM Bermuda — §10.44 cession-cohort recursive subtree disclosure

Mike at the whiteboard.

**Mike:** "§10.44 normates that a Polaris-side seal record's Merkle tree is partitioned by cession-cohort — the group of risks reinsured under one cession contract or one program. Each cohort is a recursive subtree under the day's apex root. A cedent regulator can request the subtree corresponding to their syndicate; the §10.44 partial-disclosure mode produces the subtree, the audit path from the subtree's root to the apex, and the cohort metadata. The verifier validates the subtree against the apex under the seal's signature."

**Stuart:** "We organize by cession contract. Each cession contract is one cohort. Three syndicates with multiple cession contracts each — Polaris has 23 active cession contracts across the three syndicates. 23 cohorts, 23 subtrees, one apex root per day."

**Mike:** "How does the subtree get extracted?"

**Stuart:** "The seal job builds the day's Merkle tree with cession-contract grouping at the leaf level. Leaves within a cohort are siblings; cohort sub-roots aggregate into the apex. The §10.44 disclosure produces the per-cohort sub-root, the audit path to the apex, and the leaves under that sub-root. Henry's regulator at Lloyd's — the Prudential Regulation Authority — pulls Syndicate 0314's subtree directly. Each syndicate's regulator sees only the cohorts that pertain to that syndicate."

**Henry** (London): "And from Lloyd's side, our internal audit pulls our cohort subtree from Polaris's chain weekly. The subtree audit path verifies under Polaris's HSM signature. The cession-cohort metadata names the syndicate, the cession contract, the program year. We've verified 39 weekly subtree pulls over the past nine months; all 39 are clean."

**Mike:** "Run a fresh pull."

Stuart runs the §10.44 disclosure tool live on the Bermuda terminal. The output produces a subtree for Syndicate 0314's marine cohort for the prior week. The audit path includes 14 hash steps to the apex; the verifier confirms each step.

```
$ herald-disclose --cohort lloyds-0314-mar-quota-2026 --week 2026-W41 --json
{
  "cohort_id": "lloyds-0314-mar-quota-2026",
  "syndicate_id": "lloyds-0314",
  "leaves_in_cohort": 287,
  "subtree_root_sha256": "c4e8...",
  "audit_path_to_apex_steps": 14,
  "apex_root_sha256_per_seal": "9b21...",
  "seal_record_sha256": "a721...",
  "hsm_signature_verifies": true,
  "spec_section_dispatch_path": "§10.44 / PASS"
}
```

**Mike:** "Subtree clean. Run on Henry's side now."

Henry runs the verifier on the same disclosure from London. The verifier produces the same audit path, the same cohort root, the same apex root. The hashes match byte-for-byte.

**Mike:** "Cross-impl byte-equivalence between Polaris's emit and Lloyd's verify. §10.44 in production."

## 11:30 AM Bermuda — §10.45 independent third-party adjuster anchor

Diana drives the §10.45 review.

**Diana:** "§10.45 normates a dedicated `chain.adjuster_anchor` event family — distinct from §10.19 external-artifact anchors — for the bidirectional case where the SAME independent adjuster's activity is integrity-bound on multiple parties' chains simultaneously. Each affected party emits its own `chain.adjuster_anchor` event binding the adjuster identity, the activity-record SHA-256, the adjuster's signature over the activity record, and — load-bearingly — `peer_party_chain_entries`, a JCS-canonical array naming every other party's chain entry that anchors the same adjuster activity. That bidirectional cross-anchor mechanism is the feature §10.45 was authored for. §10.45 is the canonical instance of the §10.21.2 parallel-evaluator composition pattern — two independent evaluators (the primary insurer's adjuster and the cedent / reinsurer's chain) anchored at one shared target (the loss event)."

**Stuart:** "Three large adjusters in our pool: Sedgwick, Crawford, McLarens. Each has an enterprise SLA with Polaris and a pre-registered adjuster role on our side. Their activity records come in PDF form signed under their digital signature; on receipt the activity record is hashed, the signature is preserved, and the chain entry is emitted carrying the adjuster identity, the activity-record SHA-256, the signature, and the peer-party chain-entry references that point back to the cedent syndicate's matching entry. Verifier dispatch path for §10.45: walk the `chain.adjuster_anchor` event, confirm `peer_party_chain_entries` is non-empty, and for each peer entry that the verifier can reach, confirm that peer's `chain.adjuster_anchor` references this party's entry back. Activity-record SHA-256s must match across all parties' entries."

**Diana:** "Show me an anchor entry."

```json
{
  "audit.adjuster_anchor.adjuster_id": "sedgwick-adj-2024-0817",
  "audit.adjuster_anchor.adjuster_legal_name": "Sedgwick Claims Management Services Ltd.",
  "audit.adjuster_anchor.adjuster_role": "loss_adjuster",
  "audit.adjuster_anchor.activity_record_sha256": "f3c1...",
  "audit.adjuster_anchor.activity_record_signature_b64": "MEUCIQDk2P...",
  "audit.adjuster_anchor.peer_party_chain_entries": [
    {
      "party_role": "cedent",
      "party_identifier": "lloyds-0314",
      "peer_run_id": "lloyds-0314-2026-09-08-claim-04127",
      "peer_seq": 4172
    }
  ],
  "audit.adjuster_anchor.activity_utc": "2026-09-08T14:22:00Z",
  "claim.id": "POL-2026-MAR-CARGO-04127"
}
```

**Diana:** "And the cession side?"

**Henry** (London): "Syndicate 0314 receives Sedgwick's report through the bordereau cycle as an attached artifact. We anchor it on our side as well — same SHA-256, same source party, same appointment-utc. Cross-anchor verification: cedent-side anchor SHA-256 matches reinsurer-side anchor SHA-256 byte-for-byte. The independent adjuster's report is bound on both sides of the cession boundary."

**Diana:** "Threat model?"

**Stuart:** "If a malicious party substitutes the adjuster's report between adjuster and reinsurer, the SHA-256 fails to match the appointment-letter binding. If a malicious party tampers with the appointment-letter, the appointment-letter SHA-256 stored in the chain entry fails to match the appointment-letter on file. Both checks are at chain-walk time."

**Diana:** "Last 90 days, anomalies?"

**Stuart:** "Zero. 142 independent-adjuster anchors across the three syndicates' cohorts; all 142 verify."

## 12:30 PM Bermuda — §10.46 bordereau integrity

Lunch is brought in. The team eats while Stuart walks the §10.46 bordereau lifecycle.

**Stuart:** "Bordereau is the spreadsheet — historically literal Excel — that the cedent sends the reinsurer listing the period's reinsured claims. §10.46 normates a four-event chain-bound lifecycle family: `audit.bordereau.published` (cedent publishes the bordereau for the period) → `audit.bordereau.received` (reinsurer receives, recomputing the hash) → `audit.bordereau.reconciled` (reinsurer completes reconciliation against its own claim records and emits `reconciliation_outcome` of `match` or `discrepancy`) → `audit.bordereau.discrepancy_resolved` (only emitted when reconciliation outcome is `discrepancy`). The bordereau itself is JCS-canonicalized at publish-time, hashed, and the `bordereau_sha256` is cross-bound across the `published`, `received`, and `reconciled` events."

**Mike:** "Show me the lifecycle for one bordereau."

Stuart projects the September 2026 bordereau for Syndicate 0314 marine cohort. The four §10.46 events in sequence:

```
2026-09-30T23:30:00Z  audit.bordereau.published        (Lloyd's-side, by Henry's team; bordereau_sha256 bound)
2026-09-30T23:33:14Z  audit.bordereau.received         (Polaris-side; recomputed bordereau_sha256 matches)
2026-10-02T11:42:00Z  audit.bordereau.reconciled       (Polaris-side; reconciliation_outcome = "match"
                                                        after 287-line reconciliation against claim state)
```

**Mike:** "Bordereau hash?"

**Stuart:** "Hash bound at publish-time. The bordereau is JCS-canonicalized — every claim ID, reinsured share, claim state, paid-to-date, reserved amount, all the structured fields in canonical order. The `bordereau_sha256` is bound in the `audit.bordereau.published` event. The reinsurer recomputes the SHA-256 on receipt — at the `audit.bordereau.received` event — and the same hash is then cross-bound at `audit.bordereau.reconciled`. If a single line item is different, the recomputed hash diverges, the verifier flags it as a chain-integrity anomaly, and the `reconciliation_outcome` records `discrepancy`."

**Henry** (London): "From our side: the bordereau is generated by an automated pipeline that pulls the period's claims from our cession-management system. The pipeline computes the JCS canonical form, hashes it, and emits the `audit.bordereau.published` event on our chain carrying `bordereau_id`, `period_start_utc`, `period_end_utc`, `bordereau_sha256`, `published_at_utc`, and `cedent_party_identifier`. The `audit.bordereau.received` event on Polaris's side cross-binds by `bordereau_sha256`. We've published 36 bordereaux across the nine months; 34 reconciled with `reconciliation_outcome = match`. Two surfaced `discrepancy` outcomes — the duplicated line item and the missing reserved amount — and both produced `audit.bordereau.discrepancy_resolved` events naming both parties as `resolving_parties` and binding the resolution-record SHA-256."

**Mike:** "How does the verifier walk the lifecycle?"

**Stuart:** "Four checks under §10.46. First, every `received` event must follow a `published` for the same `bordereau_id`. Second, every `reconciled` event must follow a `received` for the same party. Third, when `reconciliation_outcome` is `discrepancy`, a `discrepancy_resolved` event must eventually appear for the same `bordereau_id`. Fourth — load-bearingly — `bordereau_sha256` must be consistent across `published`, `received`, and `reconciled`; every party hashes the same canonical bordereau document. Mismatch on the hash cross-binding is a chain-integrity anomaly."

**Diana:** "Cross-binding to claims?"

**Stuart:** "Per §10.46's `audit.claim_state.bordereau_id` cross-binding attribute, each claim referenced in a bordereau carries a `chain.claim_state.transition` event naming the bordereau the transition was reflected in. NAIC market-conduct examiners trace from the bordereau back to the per-claim transitions that produced it; the cedent emits the cross-binding on the cession-recording transition and Polaris emits it on the inclusion-recording transition."

**Mike:** "Run a verification."

Stuart runs the verifier on a closed bordereau from August.

```
$ herald-verify --bordereau-id lloyds-0314-mar-aug-2026 --json
{
  "bordereau_lifecycle_walk": "published -> received -> reconciled",
  "lifecycle_walk_valid": true,
  "bordereau_sha256_cross_binding_match": true,
  "reconciliation_outcome": "match",
  "cedent_party_identifier": "lloyds-0314",
  "receiving_party_identifier": "polaris-re",
  "reconciling_party_identifier": "polaris-re",
  "spec_section_dispatch_path": "§10.46 / PASS",
  "exit_code": 0
}
```

**Mike:** "Bordereau integrity confirmed. §10.46 in production."

## 1:30 PM Bermuda / 5:30 PM London — Reconciliation test

The reconciliation test for the engagement is a 1,400-claim trace across the cedent → reinsurer boundary, sampled from the prior 90-day cession period. 1,000 claims from Syndicate 0314 (marine), 250 from 1218 (aviation), 150 from 2847 (political-violence specialty).

The team divides:

- **Mike** runs the §10.43 claim-state walk on Polaris's side.
- **Stuart** runs the §10.43 walk on the syndicate side, by syndicate.
- **Diana** runs the §10.44 cohort subtree extraction for each syndicate's cohorts.
- **Chen** (London) runs the bordereau reconciliation against the claim-state records for each cession period.
- **Luis** (London) runs the §10.45 adjuster-anchor verification on the 142 anchored reports.
- **Raj** (London) queries the cession-management database for the cohort metadata.
- **Elena** (London) correlates the claims back to the syndicate's underwriting records.
- **Tom** observes the audit-procedure across both sites.
- **Dawn** moderates from Bermuda.

The reconciliation runs through the afternoon. Hamilton 1:30 to 5:30 PM is London 5:30 to 9:30 PM; the London team works through their evening to keep parallel pace. Status check at Hamilton 3 PM / London 7 PM: Mike has cleared 800 claims; Diana has extracted 12 of 23 cohort subtrees; Chen has reconciled 14 bordereau periods; Luis has verified 87 of 142 adjuster anchors. By Hamilton 5 PM the team is at 1,200 claims cleared, 23 subtrees extracted, 22 bordereau periods reconciled, 142 adjuster anchors verified.

The remaining 200 claims and the four open subtrees go to Tuesday morning.

## 4:30 PM Bermuda — The CRO question

Iyari in her office. Floor-to-ceiling glass on three sides, harbor view, sailboats anchored against the late-afternoon light. Dawn sitting across from her. Tom at the end of the room watching, not speaking.

**Iyari:** "I've been waiting to ask this. The §10.43 claim-state-machine — there's a subtle question about reflexive transitions and substate semantics that I'd like a vendor-side read on. The spec normates reflexive transitions in non-terminal states; we exercise it for substate moves. But the §10.43 normative text doesn't fully specify whether the substate dimension is bound to the high-level state or attestable independently. The OCC examiner I expect on Day 3 will press on this."

**Dawn:** "I have the read. But this is the kind of question where my firm's recusal protocol normally has me defer to vendor-side technical testimony. I want to give you the recusal-protocol-clean answer, then confirm with Mike. I will not contact Steve directly on this; Mike or Chen will, if needed, through the firm's recusal-cleared escalation path."

**Iyari:** "Acknowledged."

**Dawn:** "My read: the §10.43 substate dimension is a CC8.1 institutional concern. The spec normates the high-level enumeration (opened / pending / decided / closed) and the transitions; the substates are institution-named under CC8.1, not normative. The verifier dispatches on the high-level state only; the substates appear in the chain entry as additional attributes but they're institution-side semantics. The OCC examiner can audit your CC8.1 control description for the substate naming and the institution's procedure for substate moves; the chain doesn't claim normative semantics for the substate."

**Iyari:** "And if the OCC examiner asks: 'how do we know the substate isn't a covert way to mask a pending → closed transition that should have been pending → decided?'"

**Dawn:** "Two answers. First, the high-level transition (pending → closed vs pending → decided → closed) is what the chain binds and the verifier checks; if the institution emits pending → closed, that's the chain claim, and CC8.1 has to justify why decided was skipped. Second, the substate dimension does not have authority to skip a high-level transition. The substate moves are reflexive at the high-level state; a high-level transition requires a from / to pair across two distinct high-level states. The verifier enforces this at the §1.5 / GAP-2 substrate level."

**Iyari:** "And the ambiguity in the spec text?"

**Dawn:** "Mike will confirm the vendor-side read with his counterpart. If the spec text needs an editorial pass to disambiguate, that's an issue we surface in our memo and the spec working group decides. My firm's recusal protocol means I do not consult the principal designer directly on questions where his read would be load-bearing testimony for your regulatory engagement. Mike does."

**Iyari:** "Understood. Send the read in writing tomorrow."

**Dawn:** "By close of business tomorrow."

**Iyari** (after a pause): "I noticed the recusal language in your engagement letter. I haven't asked. I won't ask. The methodology is sound; the audit work today is clean; I expect the same tomorrow. If the spec text needs sharpening, Polaris will support the working group on it."

**Dawn:** "Thank you."

**Tom** (from the corner of the room): "We'll have the working-group note prepared as part of the memo's appendix."

**Iyari** (rising): "Good. See you tomorrow."

## 6:30 PM Bermuda — Hamilton Princess terrace

The Bermuda evening. Pink sand glowing across the harbor; the team scattered. Mike, Diana at the bar with Tom; Dawn alone on the terrace, her phone in her hand.

The text from her, to Steve in California (where it's 2:30 PM):

> *"Engagement is clean. §10.43-§10.46 holding. Iyari surfaced a substate-semantics question this afternoon — Mike has the action item to walk it with his counterpart through the firm's recusal-cleared path tomorrow. Recusal protocol working as designed. Tomorrow morning we close out the remaining 200 claims and four cohort subtrees. Memo by 4 PM Bermuda. Thinking of you."*

His response three minutes later (he was probably in a meeting):

> *"Glad it's holding. The substate question was on the working-group draft list for editorial pass — the §10.43 normative text could be clearer. Mike's counterpart this cycle is Akshara on our side; I'll make sure she's reachable through the protocol. Thinking of you too."*

She reads it twice.

She does not reply for a while.

Mike, walking past with Diana toward the bar, sees Dawn's expression and says nothing.

## Day 2

### 8:30 AM Bermuda — Closing the trace

The remaining 200 claims clear by 10:30 AM Bermuda. The four open cohort subtrees extract by 10:45. Mike emails Akshara at TesseraSeal at 9:15 AM Bermuda (5:15 AM Pacific) on the substate-semantics question, copying Tom and the firm's general counsel per the recusal protocol; Akshara responds at 11:30 AM Bermuda (7:30 AM Pacific) confirming the read Dawn delivered to Iyari yesterday and naming the working-group editorial-pass action item already on the December agenda. Mike includes Akshara's response in the spec-section confirmation memo's appendix.

### 11:00 AM Bermuda / 3:00 PM London — Joint close-out

The full team on the bridge. Iyari, Alistair, Stuart in Bermuda; Henry on the London side. Mike delivers the vendor-architecture sections of the memo; Dawn delivers the audit-procedure and reconciliation sections.

**Mike:** "Four spec-section confirmations, in production at Polaris × Lloyd's. §10.43 claim-state-machine: 14,300 claims walked clean over 90 days at Polaris; 8,400 claims walked clean across the three syndicates. Cross-chain anchors verify between cedent and reinsurer chains. §10.44 cession-cohort subtree disclosure: 23 cohorts at Polaris organized by cession contract; weekly subtree pulls verify byte-for-byte between Polaris emit and Lloyd's verify across 39 pull cycles. §10.45 independent-adjuster anchor: 142 `chain.adjuster_anchor` events across three large adjusters; bidirectional `peer_party_chain_entries` cross-references verify in both directions; activity-record SHA-256s match across cedent-side and reinsurer-side entries. §10.46 bordereau integrity: 36 bordereaux published across nine months; 34 with `reconciliation_outcome = match`, 2 with `discrepancy` resolved through `audit.bordereau.discrepancy_resolved` events; `bordereau_sha256` cross-binding verifies across `published`, `received`, and `reconciled` events on every bordereau. The substate-semantics question Iyari raised is in the spec working group's December editorial-pass agenda; institutional-side CC8.1 governs the substate dimension."

**Dawn:** "Audit-procedure: 1,400-claim trace across cedent → reinsurer boundary; reconciliation against bordereau lifecycle; cohort subtree verification on both sides; adjuster-anchor SHA-256 verification on both sides. Polaris × Lloyd's becomes the canonical institutional reference for multi-party claim-flow integrity. The NAIC examination wave can be answered with the chain output; New York DFS, Bermuda Monetary Authority, and the PRA each get their respective subtree disclosures with byte-for-byte verifiability."

**Iyari:** "And the structural answer for the wave?"

**Dawn:** "Multi-party claim flow under TesseraSeal looks like this: each party runs their own chain on their tenant key; cross-chain anchors at cession boundaries bind the role-handoffs; cohort-subtree disclosure gives each regulator their slice of the visibility; bordereau integrity binds the periodic reconciliation. The NAIC wave's structural question — 'how do we audit a claim that crosses three parties?' — is answered by the cross-chain anchors and the §10.44 cohort subtrees together."

**Henry** (London): "And from Lloyd's side, our internal-audit attestation will reference Polaris's chain output with cross-walk verification. The PRA will see a coherent audit trail across cedent and reinsurer."

**Iyari:** "Memo by close of business?"

**Dawn:** "By 4 PM Bermuda, 8 PM London."

**Iyari:** "Thank you. You handled the recusal protocol exactly as I'd want a senior firm to handle it. The audit-procedure and the substate-semantics escalation both went through the channels your engagement letter named. There's no daylight between the methodology and the execution."

**Dawn:** "Thank you, Iyari."

The bridge closes. The London team starts shutting down for the day; the Bermuda team finishes the memo.

### 8:00 PM Bermuda — Dinner

The Hamilton Princess restaurant. Mike, Diana, Tom, Dawn. The London team is on a separate dinner clock at the syndicates' usual pub near Lime Street, four hours ahead.

Tom raises his glass.

**Tom:** "Twenty-six years of doing this together, Dawn. You handled it the way I'd want my daughter to handle it."

Dawn doesn't say anything for a moment.

Then: "Thank you, Tom."

The table is quiet for a long second.

**Mike:** "Recusal protocol live for the first time. It worked the way the firm wrote it."

**Diana:** "Akshara's response cleared in two hours. The escalation path is operational."

**Tom:** "The protocol is the protocol because we wrote it for cases like this. It worked."

**Mike** (raising his glass too): "To the engagement."

The team drinks. The Hamilton harbor outside the window is dark. Across the Atlantic, the London team is wrapping their pints and heading to the hotel.

## TesseraSeal forward-thinking design points Polaris × Lloyd's exercises

Polaris × Lloyd's exercises four spec sections that TesseraSeal's design anticipated for multi-party claim-flow integrity in the reinsurance industry. Each is articulated below.

### Section 1 — Claim-state-machine chain entries (§10.43)

**What Polaris × Lloyd's operates.** The four canonical states — opened / pending / decided / closed — are emitted as `audit.claim_state.transition` chain entries on each party's tenant chain. Cross-chain anchors at cession boundaries bind cedent-side and reinsurer-side claim-state events by run-id and SHA-256. Polaris emits 14,300 transitions in a 90-day window across 23 cession cohorts; the three syndicates emit 8,400 transitions on their respective sides. Reflexive transitions in non-terminal states carry institution-named substates (CC8.1 governed) for marine/aviation/political-violence-specific milestones.

**Why TesseraSeal designed for this.** §10.43 lifts the §1.5 / GAP-2 state-machine substrate to the claim-adjudication domain. Multi-party claim flow needed a normative high-level enumeration so cross-jurisdiction regulators can audit claim flow without each regulator having to learn each institution's substate semantics.

### Section 2 — Cession-cohort recursive subtree disclosure (§10.44)

**What Polaris × Lloyd's operates.** Polaris organizes the daily Merkle tree by cession-cohort grouping; each of 23 cohorts is a recursive subtree under the apex root. Per-cohort subtree disclosure produces the cohort's sub-root, the audit path to the apex, and the leaves under that sub-root. Lloyd's syndicates and the New York DFS each pull their respective cohort subtrees with byte-for-byte verifiability against Polaris's HSM-signed apex.

**Why TesseraSeal designed for this.** §10.44 generalizes §10.31 per-cohort subtree disclosure to the recursive structure cession contracts produce naturally — a cession contract is a cohort, and a cohort is a sub-root. Each regulator sees only their slice; the institution doesn't expose cross-syndicate visibility to any one regulator.

### Section 3 — Independent third-party adjuster anchor (§10.45)

**What Polaris × Lloyd's operates.** 142 independent-adjuster activity records across the three large adjusters (Sedgwick, Crawford, McLarens) anchored as `chain.adjuster_anchor` events on both Polaris's and the cedent syndicates' chains. Each anchor binds adjuster identity, adjuster legal name, adjuster role, activity-record SHA-256, the adjuster's signature over the activity record, peer-party chain-entry references that name every other party's matching chain entry, and the activity-utc. Bidirectional cross-anchor verification: every cedent-side entry references the matching reinsurer-side entry and vice versa via `peer_party_chain_entries`; activity-record SHA-256s match byte-for-byte across all parties' entries.

**Why TesseraSeal designed for this.** §10.45 normates a dedicated bidirectional-anchor event family because §10.19 (one-way external-artifact anchoring) and §10.40 (one-way chain-merge inheritance) do not cover the multi-party simultaneous case. The integrity claim is structural: a malicious party cannot substitute the adjuster's activity record between adjuster and reinsurer because the activity-record SHA-256 must match across all parties' `chain.adjuster_anchor` entries, and the bidirectional `peer_party_chain_entries` references make a unilateral anchor without peer reciprocation a control-completeness anomaly the verifier surfaces.

### Section 4 — Bordereau integrity (§10.46)

**What Polaris × Lloyd's operates.** Bordereau lifecycle as a four-event chain-bound family: `audit.bordereau.published` → `audit.bordereau.received` → `audit.bordereau.reconciled` → `audit.bordereau.discrepancy_resolved` (the fourth emitted only when `reconciliation_outcome` is `discrepancy`). The bordereau is JCS-canonicalized at publish-time; `bordereau_sha256` is bound at `published` and cross-bound at `received` and `reconciled`. Verifier confirms (a) `received` follows `published` for the same `bordereau_id`, (b) `reconciled` follows `received` for the same party, (c) every `discrepancy` outcome eventually produces a `discrepancy_resolved` event, (d) `bordereau_sha256` is consistent across all three lifecycle events.

**Why TesseraSeal designed for this.** §10.46 normates the bordereau lifecycle as a chain-bound process so the periodic reconciliation that defines reinsurance accounting is integrity-bound. Two surfaced discrepancies at Polaris × Lloyd's over nine months produced `audit.bordereau.reconciled` events with `reconciliation_outcome = "discrepancy"` followed by `audit.bordereau.discrepancy_resolved` events binding the resolution-record SHA-256 and the resolving-parties array; the chain has the full four-event sequence recorded.

## Engagement debrief — Dawn's voice

> "It never is. But Polaris × Lloyd's runs the §10.43 through §10.46 multi-party claim-flow integrity sections cleanly across cedent → reinsurer boundary; the recusal protocol our firm wrote at Northbridge worked as designed at its first test. Mike authored the vendor-architecture sections; I moderated and authored audit-procedure; Iyari surfaced a substate-semantics question and the answer escalated through the firm's protocol path to TesseraSeal's working-group escalation contact, returning a clean confirmation in two hours.
>
> "TesseraSeal's design anticipated multi-party reinsurance flows two years before the NAIC market-conduct examination wave was scheduled. Steve was at the IAIS sessions in Basel in 2024; the §10.43 through §10.46 design points landed in TesseraSeal release N+1 nine months ago. Polaris and the three syndicates upgraded six months ago. The 1,400-claim trace across cedent → reinsurer boundary verifies byte-for-byte; the §10.44 cohort subtree disclosure gives each regulator their slice; the §10.46 bordereau integrity binds the periodic reconciliation; the §10.45 independent-adjuster anchor cross-binds across the cession boundary.
>
> "The work is the work."

## Cross-references

- **Spec impact**: §10.43 (claim-state-machine, lifts §1.5 / GAP-2 substrate), §10.44 (cession-cohort recursive subtree disclosure, generalizes §10.31), §10.45 (independent third-party adjuster anchor, dedicated `chain.adjuster_anchor` event family with bidirectional `peer_party_chain_entries`; canonical instance of the §10.21.2 parallel-evaluator composition pattern), §10.46 (bordereau integrity, four-event lifecycle family `published → received → reconciled → discrepancy_resolved` keyed on `bordereau_id` and `bordereau_sha256`). §10.43 substate-semantics editorial pass on December working-group agenda.
- **Test-vector references**: vectors 037 (state-machine transition validator — the §1.5 / GAP-2 primitive), 038 (claim-state lifecycle — §10.43), 039 (adjuster-anchor bidirectional cross-binding — §10.45), 040 (bordereau lifecycle — §10.46). §10.44 cession-cohort recursive subtree disclosure generalizes the §10.31 per-cohort subtree primitive; no dedicated Phase-6 vector.
- **Stakeholder navigation**: §13 stakeholder for "reinsurance market-conduct examiner" — Polaris × Lloyd's becomes the canonical institutional reference; the docs/regulator-pack/reinsurance-multi-party-overlay.md operational supplement names the cross-chain-anchor pattern and the bordereau-integrity dispatch path.
- **Auditor stories**: this story is the first-test of the recusal protocol introduced in Story 14. Mike's authorship of the vendor-architecture sections, the firm-cleared escalation path to TesseraSeal's Akshara, and Iyari's "no daylight between methodology and execution" close are the pattern Stories 16 and 17 will follow.

The spec-section confirmation memo and engagement debrief are filed under Polaris's compliance-track records, with the §10.43-§10.46 spec-section confirmations cited in the institution's CC8.1 control description and Lloyd's syndicates' internal-audit attestations.
