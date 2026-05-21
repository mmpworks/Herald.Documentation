# 22 — Wasatch Payments Network

> A US payments network, ~$1.8T annual transaction volume, headquartered Salt Lake City. AI fraud-decisioning at sub-100ms decision time, billions of decisions per day. TesseraSeal in production for 8 months on the fraud-decisioning path. The team is on-site at the request of Wasatch's Chief Risk Officer ahead of a coordinated examination cycle: OCC + Federal Reserve, nine issuing-bank state examiners, and an FTC inquiry on a recently-publicized chargeback dispute. The engagement is two days. The story is structurally different from any of the prior 11 — Wasatch's clock runs faster than the spec's daily seal, and TesseraSeal's §10.27-§10.31 streaming-mode design points are exactly what the institution exercises in production.

## The team and the day

The full eight travel: Dawn, Raj, Elena, Mike, Diana, Luis, Chen, Tom. Salt Lake City field-office is in the engagement-letter copy; the actual day-one work happens in Wasatch's Operations Center (a hardened building in suburban West Valley City with biometric vestibules and a small museum-quality display of historic payment terminals at the lobby). The OCC + Fed examiner team will arrive Day 3; the team's job is the pre-engagement readiness pass plus the spec-section confirmation memo to Wasatch's CRO before the formal examination opens.

## The drive-in monologue

```
6:55 AM. Rental SUV, I-215 westbound from the Salt Lake City airport hotel. Dawn driving.
                          Raj in the passenger seat with his coffee.
```

**Dawn:** "Eleven prior engagements in the rear-view, in order. Northbridge was the high-water mark. Mercator was the bifurcation. Stelvio was the IT/OT split. Atrio was the multi-tenant proof. Helmstad was the biopharma maturity-bound. Pacific Crescent was the public-safety. Olmstead was the lawsuit-motivated. NetiVa was the nation-state. Sun-Won was the multi-jurisdiction. Salt Pond was the multi-location. Eberhardt × Lumière was the cross-vendor. And now Wasatch Payments — different problem."

**Raj:** "Different problem how?"

**Dawn:** "Sub-100ms decisions. Billions of them a day. Per-second seal."

**Raj:** "Ah. The clock."

**Dawn:** "The clock. The CRO's letter said it as plainly as I've ever read: *the regulators want our 11 AM transaction's evidence to be integrity-bound by 11:00:01 AM the same day, not by 4 AM tomorrow*. The spec normates configurable cadence per §10.27 — Wasatch runs `\"per_second\"`. Two-layer integrity from the moment of capture is exactly what §10.27 was designed to deliver."

**Raj:** "And the per-event MAC is real-time."

**Dawn:** "Real-time at capture, yes. Layer one. Layer two completes one second later when the cadence-interval seal record signs the Merkle root over that second's events under the HSM key. Two-layer integrity from the moment of capture for institutions on Wasatch's clock."

**Raj:** "What do we tell them?"

**Dawn:** "We tell them the §10.27 streaming-mode design is operational. The §10.29 streaming verifier consumes the live stream and produces incremental verdicts. The §10.30 trusted-time integration gives the clock the regulator-grade integrity claim. The §10.31 per-cohort subtree disclosure handles the nine issuing-bank slices. We confirm operational fidelity end-to-end."

**Raj:** "It never is."

**Dawn:** "It never is. But Wasatch exercises the streaming-mode design points at scale, in production, under live regulator review. The question is whether every section holds under operational reality."

## 7:45 AM — Lobby

The lobby smells of conference-center coffee and a faint disinfectant. The historic-terminals display has a 1970s magstripe imprinter, a 1990s VeriFone Tranz 330, a 2010s Square Reader, and a 2020s tap-to-pay terminal. The progression is the day in miniature.

The team checks in at security, gets badges with photo and a numeric escort code, and is shepherded into the executive briefing room by the CRO's chief of staff.

**The CRO** (introducing herself): "Marcia Endersby. I sent the engagement letter. The OCC team lands Wednesday. Nine issuing-bank state examiners — that's New York DFS, California, Texas, Massachusetts, North Carolina, Illinois, Pennsylvania, Florida, and Georgia — are reviewing concurrently. The FTC inquiry is on a particular dispute that surfaced in the press: the family from Provo whose teenager's tap-to-pay was AI-flagged at a stadium and the merchant retained the goods despite the cardholder's later confirmation."

**Dawn:** "We saw the news cycle."

**Marcia:** "The dispute itself we'll handle through normal channels. The press cycle and the FTC inquiry are about the *shape* of our audit trail — whether our AI's decision-record can be produced in hours, not days, with full integrity. That's the spec-section question. Tell me which spec sections TesseraSeal exercises and what each section gives us."

**Dawn:** "Two-day engagement. We'll walk the spec, sample the chain, do reconciliation on a slate of disputed transactions, and produce a spec-section confirmation memo Wednesday morning before the OCC arrives. Tom will partner with your Chief Audit Executive."

**Marcia:** "John Quan. He's already in the room."

A man in his late 50s, gray suit, half-rimmed reading glasses, steps forward and offers Tom his hand.

**John:** "I've read all eleven of your prior engagement debriefs that the project has published. Northbridge was instructive. Atrio was inspirational. Eberhardt × Lumière is the one I keep coming back to."

**Tom:** "We learn something every time."

**John:** "What we'll learn here is whether Wasatch's deployment exercises the streaming-mode design points cleanly across all five §10 sections."

**Dawn:** "It's structural. We're going to find that and document it."

## 9:00 AM — The fraud path walk-through

Wasatch's lead architect for fraud-decisioning — Anika Holzer, late 30s, sharp, ex-Google Pay — walks the team through the architecture. The fraud-decisioning system is a fan-out: every authorization request hits a routing layer that forwards to one of three model-serving regions (West Coast, Central, East Coast), each region runs an ensemble of three models (a baseline gradient-boosted-trees, a transformer-based sequence model, and a graph-neural-network for merchant-network analysis), and the ensemble's decision is returned within a 100ms budget.

The chain instruments the routing layer and each of the three model serves at every region. A single transaction generates one routing chain entry and three model-call chain entries, all within the same `run_id`. With billions of transactions per day, the chain volume is approximately twelve billion entries per day, peak rate roughly 250,000 entries per second.

**Mike** (the application-API specialist): "What's the SDK-side latency overhead?"

**Anika:** "About 0.4 milliseconds per chain entry, measured at the 99th percentile. Total budget for chain stamping per transaction is around 1.6 ms, which fits inside our 100ms decision budget comfortably."

**Mike:** "Where does the chain entry land?"

**Anika:** "Local SSD on the model-server host, fsync'd before the entry is treated as committed. Then a sidecar process ships entries to the central ledger over OTLP. End-to-end ledger-confirmed latency is 8-30 seconds depending on region and load."

**Mike:** "And the seal?"

**Anika:** "Daily, at 02:15 UTC, when traffic is lowest. The seal job runs across all three regions in coordinated reconciliation per spec §10.15."

**Mike:** "Which means a transaction at, say, 14:30 UTC today — its seal completes around 02:15 UTC tomorrow. Roughly twelve hours of integrity-claim asymmetry."

**Anika:** "Yes. That's the gap. The per-event MAC is integrity-bound at capture, but the seal is twelve to twenty-four hours behind."

**Dawn** (closing the morning): "Let me articulate it back so we agree. Today's chain provides one-layer integrity from the moment of capture — the per-event MAC. The second layer — the daily Merkle seal and HSM signature — completes by 04:00 UTC the following day. The institution wants both layers from the moment of capture. The regulator wants the same. The customer dispute response wants the same. The FTC's inquiry would like the same."

**Anika:** "Yes."

**Dawn:** "Good. Let's walk the streaming-mode design points: §10.27 cadence, §10.28 rotation discipline, §10.29 verifier, §10.30 trusted-time, §10.31 subtree disclosure. Each one is in production at Wasatch. The memo confirms the conformance for the OCC team."

## 10:30 AM — Per-event MAC sufficiency under FRE 902

The team adjourns to a smaller conference room. Mike, Diana, and Chen pull up specific transactions from the prior evening; Tom and John are at the end of the table. Dawn whiteboards.

**Dawn** (writing on the whiteboard):

```
TRANSACTION 11:42:18.471 UTC, MERCHANT M, AMOUNT $X
  - run_id: r-a8f-...
  - seq=1: routing entry (which region, classifier_output)
  - seq=2: GBM model call
  - seq=3: transformer model call
  - seq=4: GNN model call
  - seq=5: ensemble decision (BLOCK or APPROVE)

EACH CHAIN ENTRY: per-event MAC under tenant session key
  → MAC verifies independently against IKM in HSM
  → fingerprint check at §7 step 8
  → MAC check at §7 step 9
  → ALL FIVE ENTRIES PASS individual MAC verification immediately

DAILY SEAL: covers all entries for the tenant-day, signed Ed25519 in HSM
  → Today's entries: seal not yet computed (at time of inspection)
```

**Dawn:** "FRE 902 self-authentication. The chain entry is a record of regularly conducted activity if the institution can demonstrate (1) the record was made at or near the time of the activity, (2) the institution's witness can lay the foundation for the integrity claim. The per-event MAC laid down at capture, with a `mac_computed_at_utc` field, satisfies (1). For (2), the institution's expert witness can describe the per-event MAC construction, the HKDF derivation, the FIPS-standardized primitives, the test-vector corpus."

**John:** "And the seal?"

**Dawn:** "The seal is the *cross-event* integrity claim — proving no events have been retroactively inserted, deleted, or reordered after the fact. For a single transaction's evidence, the seal is supportive but not dispositive — the per-event MAC alone is the within-event integrity claim. The seal becomes load-bearing when the production includes more than one event from the same tenant-day."

**John:** "Which is exactly what every multi-record dispute would want."

**Dawn:** "Yes. So for a single-transaction dispute response — the FTC's inquiry on the Provo-stadium dispute — the chain provides full per-event integrity at the moment of capture, and the seal completes the day-level cross-event integrity by tomorrow morning. That's defensible. But it's not what Wasatch wants."

**John:** "What does Wasatch want?"

**Dawn:** "Two-layer integrity from the moment of capture. The institution operates in a real-time decisioning regime. Daily seal is a posture mismatch."

**Anika:** "The §10.27 streaming cadence is what we run today."

**Dawn:** "And §10.27 is in the spec for exactly Wasatch's clock. Yes."

## 11:30 AM — The streaming-seal-cadence design conversation

The whiteboard fills with sketches.

**Anika:** "Could the spec support a configurable seal cadence — daily as default, but configurable down to per-second or even per-event?"

**Dawn:** "Per-event would defeat the cost benefit of Merkle aggregation. Per-second or per-minute is the realistic shape. The Merkle root over a per-second batch is meaningful; it gives a 1-second worst-case integrity-claim asymmetry."

**Chen** (data engineering): "Per-second batches at 250,000 entries per second peak — that's 250,000-leaf Merkle trees. Tractable. Per-minute would be 15M-leaf trees. Still tractable but the seal-record stream becomes large."

**Anika:** "Per-second is what we'd want. It puts our integrity-claim asymmetry at one second instead of twenty-four hours."

**Dawn:** "Then let's confirm what §10.27 says: spec normates cadence as a configurable parameter from per-second through weekly, with daily as the default. The cadence is recorded in every seal record's `cadence` field, bound under the §4.3 `sign_payload` form. Wasatch runs `\"per_second\"` and the verifier confirms continuity end-to-end. Test vector `020-streaming-seal-cadence-1s` is the byte-identical reference."

**Diana** (IAM, but she does threat-model analysis when she's not running access reviews): "What about the threat model? Streaming seal at one-second granularity exposes the seal-job process to compromise more frequently. The HSM partition would have to sign once per second instead of once per day. That's about 86,400 signing operations per day instead of 1."

**Dawn:** "The HSM throughput should support that. FIPS 140-2 Level 3 HSMs typically support tens of thousands of Ed25519 signatures per second. The threat-model question is the seal-job process compromise window — current is one-day, streaming would be one-second. Spec §1.2's fourth-class adversary (SDK-process compromise) becomes a tighter window for the seal-job too."

**Diana:** "And key rotation — the IKM rotation per §10.10 is designed for daily seal boundaries. Crossing a per-second seal boundary every second would be operationally awkward."

**Dawn:** "Right. §10.28 is the streaming-mode rotation discipline — extends §10.10 boundary-crossing to cadence-interval boundaries at sub-daily cadence. Wasatch's annual rotation passed under this section."

The whiteboard fills more.

## 12:30 PM — Lunch in the cafeteria

The cafeteria has a curved skylight and Wasatch Range views. The team takes a corner booth. John joins.

**Tom:** "The two confirmations so far — §10.27 configurable cadence, §10.28 streaming rotation discipline. What else does the day surface?"

**Mike:** "I want to check what the verifier looks like under streaming. Today's verifier batch-walks a tenant-day. A streaming verifier consumes a chain stream and produces incremental PASS/FAIL. That's a §7 question."

**John** (mid-sandwich): "The OCC examiner specifically asked us last cycle whether we could provide a real-time view of the chain — a live-feed of integrity-bound decisions. We said no. That was on us. The chain spec has an admin-SPA visibility surface but it's explicitly NOT integrity-bound per §4 ('In-process observation of partially-formed entries is NOT a spec-conformant view'). The real ask is a wire-bound streaming view that the verifier produces incrementally."

**Dawn:** "§10.29 is the streaming-mode verifier subprocedure. Each issuing-bank examiner runs the open-source verifier in streaming mode, consuming the live chain stream and producing incremental PASS/FAIL. The §10.12 exit-code contract extends to streaming-state codes (4/5/6). Wasatch's OCC team will exercise it Wednesday."

**Chen:** "And §10.14 trusted-time integration is informative right now. For streaming-mode operation at sub-second granularity, the trusted-time integration becomes load-bearing — the regulator wants to know the institution's clock isn't drifting and producing chain entries with timestamps that don't match real wall-clock."

**Dawn:** "§10.30 makes trusted-time integration normative at sub-daily cadence — institutions integrate a trusted-time source (NIST, USNO, GPS-disciplined, or RFC 3161 timestamp authority). Wasatch runs GPS-disciplined PTP across all three regions. The `clock.drift_detected` operational event in §10.2 has fired three times in eight months — each triggered a brief re-sync."

**John:** "What about the regulators? Each of the nine issuing-bank state examiners wants a per-issuer slice of the chain — only the transactions on their issued cards. Not the full Wasatch stream."

**Dawn:** "§10.31 is the per-cohort subtree disclosure — the institution selects leaves matching a cohort filter and produces a Merkle audit path showing those leaves are part of the sealed root. The verifier's partial-disclosure mode validates the cohort-bounded subtree against the seal's signed root. Wasatch's nine state examiners will each pull their issuing-bank subtree concurrently."

**John:** "All five sections become the spec-section confirmation memo for the OCC?"

**Dawn:** "All five. Plus we'll surface the timestamp precision question this afternoon — `mac_computed_at_utc` is currently RFC 3339, which goes to nanoseconds in principle but is implementation-defined in our spec. For sub-100ms decision events, sub-second precision becomes audit-relevant."

**John:** "OK. And tomorrow?"

**Dawn:** "Tomorrow, the reconciliation test, the §10.15 multi-region walk, and the spec-section confirmation memo. The OCC arrives Wednesday morning; we'll have the memo ready and a separate document for the institution-side discussion with the FTC."

## 2:30 PM — Reconciliation test

Ten transactions, picked from the prior evening, traced end-to-end.

The team divides:

- **Mike** runs the SDK-side capture trace.
- **Chen** runs the ledger-ingest trace.
- **Luis** runs the seal-job and HSM signature trace.
- **Diana** runs the IAM and access-review trace.
- **Raj** queries the database underlying the ledger.
- **Elena** correlates the ten transactions back to the CRM customer-record (for issuing-bank-side context).
- **Tom** observes and takes engagement-letter notes.
- **Dawn** moderates.

The ten transactions:

1. A tap-to-pay $48 grocery transaction in Memphis — APPROVE.
2. A $1,200 international hotel charge in Buenos Aires from a US card — BLOCK initially, then APPROVE on cardholder challenge response.
3. A $2.99 streaming-service recurring charge — APPROVE.
4. A $470 jewelry purchase in Las Vegas at 23:18 local — BLOCK, customer disputed and won.
5. The Provo-stadium tap-to-pay $89 (the FTC-inquiry transaction) — BLOCK.
6. A $35,000 wire-initiated commercial card transaction — APPROVE with manual review flag.
7. A $4.50 transit-system tap — APPROVE.
8. A $312 online retailer in a known fraud-prone merchant category — BLOCK.
9. A $0.99 vending machine tap — APPROVE.
10. A $1,750 luxury-goods purchase in Manhattan, repeat customer — APPROVE.

For all ten, the per-event MAC verifies in isolation (Mike confirms by re-running the verifier in single-entry mode against the SDK output). For transactions one through nine, the daily seal (from yesterday) covers the chain entries. For transaction five (the FTC-inquiry transaction from this morning at 11:42 UTC), the seal will not be computed until tomorrow at 02:15 UTC.

**Dawn** (to Marcia, who has rejoined): "Transaction 5 — the Provo-stadium one — has full per-event MAC integrity right now. The seal will be tomorrow morning. If you want to produce sealed evidence to the FTC today, you can't. If you produce per-event-MAC-only evidence to the FTC today, you can."

**Marcia:** "And the FTC will say — what did we know about the integrity at 3 PM today?"

**Dawn:** "Per-event MAC at capture, verifying. Seal pending. The institution's expert witness lays the foundation in the same way: FIPS 198-1, RFC 5869, RFC 8785, this institution's HSM-held IKM. The integrity claim at the per-event level is unimpeachable. The seal is the additional cross-event claim that closes by tomorrow morning."

**Marcia:** "OK. That gets us through this dispute. But Wishlist item 1 — configurable seal cadence — is what we want the OCC and the FTC to know is the structural answer."

**Dawn:** "It is."

## 4:30 PM — The CRO question

Marcia in her office. Floor-to-ceiling windows facing the Wasatch Range. Sun lowering.

**Marcia:** "Can we tell the OCC that mid-day evidence is integrity-bound?"

**Dawn:** "Yes. The per-event MAC is integrity-bound at the moment of capture. The chain entry verifies in isolation. The institution's expert witness lays the foundation."

**Marcia:** "Can we tell them the seal is integrity-bound?"

**Dawn:** "By 02:15 UTC tomorrow, yes."

**Marcia:** "And the spec sections?"

**Dawn:** "Five sections, all currently exercised. §10.27 configurable seal cadence (the headline — Wasatch runs per-second). §10.28 streaming rotation discipline (last June's rotation). §10.29 streaming-mode verifier (OCC team will exercise Wednesday). §10.30 trusted-time integration normative (GPS-disciplined PTP). §10.31 per-cohort subtree disclosure (nine issuing-bank slices)."

**Marcia:** "And the spec covers all five?"

**Dawn:** "All five are normative in the current spec. None breaks wire-format compatibility — additive within the `'v1'` wire-format identifier. Wasatch's deployment is the canonical institutional reference. And one more for the Fed side of the room — §10.71 normates `audit.wire.fedwire_originated`, `audit.wire.fedwire_received`, `audit.ach.originated`, and `audit.ach.received` event kinds with cross-institution registry-discovery cross-anchor binding (`cross_anchor_state` ∈ {`bound`, `unbound`, `published-pending-counterpart`}) at typically-90-second post-settlement publication; Wasatch operating between issuing banks and merchants on Fedwire and ACH rails is the natural canonical-adjacent reference for that section's cross-institution chain integrity."

**Marcia:** "And our message to the OCC on Wednesday?"

**Dawn:** "Today the chain gives you per-event integrity at capture and per-second cross-event integrity. We meet the FFIEC handbook's logging-integrity bar. We meet SR 26-2's audit-trail expectations for AI-based models. The §10.27-§10.31 streaming-mode design points are exercised end-to-end; the OCC team can run their own streaming-mode verifier against our live chain stream and produce byte-identical incremental verdicts. For the executive-level orientation — what the chain captures, how it's sealed, how a third party verifies it — point each examiner at §0.5.1 ('The chain in three paragraphs'). It is the spec's own three-paragraph summary, written for exactly this hand-off."

**Marcia:** "Good. That's defensible. That's the message I wanted."

**Dawn** (rising): "Tomorrow's reconciliation continues at nine. Memo to you Wednesday morning at six."

**Marcia:** "I'll be in the office at five. Coffee is in the executive kitchen."

## 6:30 PM — Hotel, Sandy, Utah

The team gathers in the hotel restaurant. Tom has the spec-section confirmation memo notebook open.

**Tom:** "Five sections. All exercised in production at Wasatch."

**Dawn:** "Yes."

**Raj:** "What's the OCC team going to say?"

**Dawn:** "I think they'll cite Wasatch's deployment as the canonical streaming-mode reference. §10.27 cadence at per-second is the headline. §10.29 streaming verifier is what they'll exercise themselves. §10.30 trusted-time integration is what gives Wasatch's clock the regulator-grade integrity claim. §10.28 rotation discipline and §10.31 subtree disclosure handle the operational and per-cohort edges."

**Tom:** "Quote for the engagement debrief?"

**Dawn:** "The spec was forward-thinking enough to anticipate institutions on Wasatch's clock. §10.27's configurable cadence, §10.29's streaming-mode verifier, §10.30's normative trusted-time integration — these are the design points TesseraSeal carried into the field for institutions whose clocks don't match the calendar. Wasatch operates them all in production."

**Tom** (writing): "*From the moment of capture.* Good."

**Mike:** "Dinner."

**Dawn:** "Dinner. Tomorrow we run the §10.15 multi-region walk and finalize the memo."

## Day 2

The §10.15 multi-region reconciliation walk goes cleanly. Three regions, one Merkle root per region, coordinated reconciliation per the spec's invariant 5. The seal-region produces the daily aggregate; the per-region partitions reconcile against the seal-region's expected count.

The spec-section confirmation memo finalizes by 4 PM.

The team flies home. Wednesday morning the OCC + Federal Reserve + nine state examiners + FTC inquiry team begin work; Wasatch's CRO has the memo, John's CAE team supports the examiners, and the engagement closes from the team's side.

## TesseraSeal forward-thinking design points Wasatch exercises

Wasatch's deployment exercises five spec sections that TesseraSeal's design anticipated for real-time decisioning institutions. Each is articulated below with what Wasatch operates and which spec section the institution is conformant against.

### Section 1 — Configurable seal cadence (§10.27)

**What Wasatch operates.** 1-second seal cadence in production across all three regions. Per-second Merkle aggregation across ~250,000-leaf trees at peak; HSM signing on AWS CloudHSM `us-east-1` with co-signing replicas in `us-west-2` and `us-east-2`; ~86,400 Ed25519 signatures per day per region. Two-layer integrity (per-event MAC plus signed Merkle root) reaches every chain entry within one second of capture. The institution's CC8.1 names the cadence and the change-management procedure. Verifier confirms cadence-record continuity end-to-end.

**Why TesseraSeal designed for this.** §10.27 normates cadence as a configurable parameter from per-second through weekly precisely so payments networks, real-time fraud-decisioning, and other sub-second-clock institutions are not asymmetric on the cadence axis. Daily-cadence institutions remain the default; streaming-mode institutions opt in.

### Section 2 — Streaming-mode IKM rotation discipline (§10.28)

**What Wasatch operates.** Annual IKM rotation per §10.10 (boundary-crossing rotation), with the streaming-mode extension at §10.28 governing cadence-interval boundaries. The rotation completed June 14, 2025 — at 03:14 UTC — across all three regions. Per §10.28 the cadence-interval crossing the rotation event was sealed under both prior and new key generations; the seal records covering that one-second interval listed `key_versions: [4, 5]`. The verifier dispatched per-entry `key_version` lookup at §7 step 7 across the rotation interval; both key generations remain valid for the chain entries they signed.

**Why TesseraSeal designed for this.** §10.28 extends the §10.10 boundary-crossing discipline to cadence-interval boundaries at sub-daily cadence. Wasatch's rotation was one second of two-key-version sealing; the verifier handles it as a normal multi-key-version interval.

### Section 3 — Streaming-mode verifier (§10.29)

**What Wasatch operates.** Each issuing-bank examiner runs the open-source verifier in streaming mode, consuming the live chain stream and producing incremental PASS/FAIL. The OCC team runs streaming-mode verification on the production stream concurrent with their on-site visit. Exit code 4 (streaming, all-pass-so-far) is observed throughout the audit period; no exit code 5 (anomaly-detected) events occurred.

**Why TesseraSeal designed for this.** §10.29 normates the streaming subprocedure of §7. Live-sample examination becomes tractable: regulators consume the same wire stream the institution produces, in real time, with byte-identical incremental verdicts.

### Section 4 — Trusted-time integration normative for streaming-mode (§10.30)

**What Wasatch operates.** Each region has a GPS-disciplined master clock with NIST-traceable network time fanned out via PTP (IEEE 1588) to all model-serving hosts. Median clock drift across the fleet is 18 microseconds; alerting threshold is 100 milliseconds; a `clock.drift_detected` event has fired three times in eight months — each triggered a brief (<2 minute) re-sync. The institution's CC8.1 names the trusted-time architecture.

**Why TesseraSeal designed for this.** §10.30 makes trusted-time integration normative at sub-daily cadence because clock drift becomes load-bearing for the integrity-claim asymmetry argument. The `clock.drift_detected` operational event in §10.2 gives the streaming-mode verifier the per-entry temporal context it needs.

### Section 5 — Per-cohort subtree disclosure (§10.31)

**What Wasatch operates.** Each issuing-bank state examiner pulls a per-issuer subtree disclosure for their day's chain entries. The verifier's partial-disclosure mode validates the cohort-bounded subtree against the seal's signed root. Nine state examiners pull their nine subtrees concurrently during the audit week; each examiner sees only their bank's transactions but each examiner's subtree verifies under the same single signed Merkle root.

**Why TesseraSeal designed for this.** §10.31 normates Merkle subtree extraction for cohort-bounded examination. Multi-tenant SaaS, payments networks, and any institution serving multiple downstream regulator-jurisdictions get per-cohort visibility without compromising single-Merkle-root integrity.

## Engagement debrief — Dawn's voice

> "It never is. But Wasatch's deployment is the most complete exercise of the spec's streaming-mode design points I've seen in eight months. Per-second cadence. Streaming-mode verifier under live regulator review. GPS-disciplined trusted-time integration with clock-drift events firing exactly when we'd expect them. Per-issuer subtree disclosure for the nine state examiners — same single signed Merkle root, nine independent partial-disclosure verifications, all PASS.
>
> "TesseraSeal's design anticipated payments-network operators years before this engagement. §10.27 through §10.31 are why we walked into a coordinated examination with OCC + Fed + nine state examiners + an FTC inquiry and watched every part of the integrity story hold under live observation. Marcia gets to send the OCC team home with sealed evidence at 1-second integrity-claim asymmetry; John's CAE team will be quoting §10.29's streaming-mode verifier exit codes for the next decade.
>
> "The next time we visit a real-time decisioning institution, this engagement is the canonical reference. Wasatch ran it the way the spec normates."

## Cross-references

- **Spec impact**: §4.2 (cadence), §7 (streaming-mode subprocedure), §10.2 (operational events for clock drift), §10.28 (streaming rotation discipline), §10.12 (verifier exit codes 0-3 plus streaming codes 4-6 per §10.29), §10.30 (trusted-time normative for streaming-mode).
- **Test-vector references**: vectors 020-023 referenced by the spec sections above.
- **Stakeholder navigation**: §13 stakeholder for "real-time-decisioning institution" — a new candidate stakeholder for spec §13.
- **Auditor stories**: this story's spec-section confirmation contrasts with Story 04 Atrio (multi-tenant, daily-cadence, full coverage) and Story 06 Pacific Crescent (utility, post-incident, daily-cadence). Wasatch is the canonical streaming-mode reference institution.

The spec-section confirmation memo and engagement debrief are filed under Wasatch's compliance-track records, with the §10.27-§10.31 spec-section confirmations cited in the institution's CC8.1 control description.
