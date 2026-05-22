# 21 — Brazos Federal Bancshares × Mission Plaza Bank

> Brazos Federal Bancshares — a Houston-HQ Texas regional bank, ~$45B consolidated assets, Texas + Oklahoma footprint, OCC-supervised. TesseraSeal in production for 15 months across all customer-facing surfaces on Azure (Herald.Enterprise.Azure, multi-region resilience per §10.15; Azure Key Vault Managed HSM for the root signature). Mission Plaza Bank — San Antonio-HQ Texas community bank, ~$3.2B assets at close, acquired by Brazos in a $269M cash-and-stock deal that closed Feb 1, 2026; partial TesseraSeal for six months pre-close on AWS (Herald.Enterprise.Aws, AI-decisioning surface plus the Phase-A marketing surface stood up in the six months pre-close). Three-day post-close integration audit at Brazos's Houston operations center, mid-September 2027, ~19 months post-close, ~6 weeks before full operational integration to the Brazos brand in November 2027. The cross-vendor anchor was placed at close at 00:00:01 UTC Feb 1, 2026 binding Mission Plaza's full pre-close chain into Brazos's Azure chain. Marketing-stack handover Insider + Yello → Salesforce Marketing Cloud + Marketo Engage in progress. Regulators in scope: OCC (lead, both legacy and acquired charters), CFPB (UDAAP on rebrand-period communications + §1033 disclosure across the merger boundary), Texas Department of Banking (Mission Plaza legacy state charter). First MMPWorks-vendor-side appearance for Dawn as lead TesseraSeal liaison; first engagement where the §10.40 substrate-agnostic clarifier is exercised live in production.

## The team and the day

The full eight travel: Raj, Elena, Mike, Diana, Luis, Chen, Tom, Sonya. Raj has been Lead Auditor for ten months. The drive-in pairing today is Raj and Diana; Raj has been rotating the right-seat through the team since taking the chair, and Diana's turn came up in May. Tom is internal-audit liaison specialist for the engagement, running the standard four questions as he has done for nineteen of the firm's last twenty engagements.

Dawn is on the schedule separately. The engagement letter names her as MMPWorks lead TesseraSeal liaison, joining at noon on Day 1 at the joint invitation of Brazos's CMO and the audit team. The spousal-disclosure paragraph of the firm's conflict-of-interest protocol governs her appearance; Tom logged the engagement-letter language with the firm's General Counsel three weeks before the on-site.

Brazos's Houston operations center is on the west side of downtown, off Allen Parkway, a fourteen-story glass building with a covered drop-off and a lobby that opens onto a courtyard with a small fountain and three live oaks. The drive in from the hotel — the team is at a Hyatt on Smith Street — is six minutes on a clear morning.

Brazos's Chief Audit Executive is **Margarethe Sundberg-Vallejo**, early-50s, integration veteran. Brazos's third acquisition under her tenure; she was CAE during the 2022 acquisition of a small East Texas thrift and the 2024 acquisition of an Oklahoma City community bank. Calm. Knows the chain. Mission Plaza's legacy CAE — now reporting to Margarethe under the integration — is **Donovan Eastlake-Boudreaux**, late-40s, two years in the role at Mission Plaza, the institutional sponsor of the partial deployment Story 20 audited.

Brazos's CMO is **Renata Whitley-Aguilar**, early-50s, hired four years ago from a national grocery chain's loyalty group; she is the one who called MMPWorks 60 days before close, asked for an integration plan, got one. Mission Plaza's legacy CMO — now Director of Brand Transition for the integration period — is **Easton Wadsworth** (the same Easton from Story 20, who signed the Phase A budget Day 3 afternoon at San Antonio in November 2026; the post-close arc kept him in the marketing seat through the brand-transition window, scheduled to roll off in November 2027 with the integration close).

Brazos's M&A integration program lead is **Hollis Trent-Mosley**, late-50s, on staff for nineteen years, has run all three of Margarethe's integrations from the program-management side. The General Counsel is **Adelaide Carrowmore-Finch**, early-60s, on staff for twenty-two years. The CFPB UDAAP attorney handling the February 4 rebrand-campaign settlement is **Yusuf Adekunle-Mensah** of the firm's regulatory practice in DC, joining by video bridge as needed.

The Federal Reserve Bank of Dallas — Wholesale Payments Office — operates the §10.21.3 voluntary cross-institution-anchor registry referenced under §10.71. The registry observer for Day 3's wire walk is **Magdalena Forsberg-Aliyev**, eighteen years at the Fed of Dallas, second career; her predecessor in the chair attended the §10.21.3 working-group sub-track at the spec body two years ago.

## The drive-in monologue

```
6:50 AM CDT. Rental SUV from the Hyatt downtown to the Brazos operations
                          center off Allen Parkway. Raj driving. Diana in the
                          passenger seat for her fourth turn in the right seat
                          since Raj took the Lead chair.
```

**Raj:** "Engagement count. Where are we."

**Diana:** "Twenty-three for the firm with you in the Lead seat; thirty-one for the team since the firm has been on TesseraSeal engagements; the Brazos × Mission Plaza engagement is the firm's third post-merger integration audit since the Atrio multi-bank platform pass three years ago."

**Raj:** "And the slot."

**Diana:** "Post-merger integration. Marketing data load-bearing. Cross-cloud anchor at the close boundary. AWS to Azure. Closest precedent in the firm's bench is Atrio's coordinated-examiner-room — but here the chain crosses a vendor-merger boundary inside the acquiring bank itself and crosses two cloud substrates inside the audit window. The §10.40 substrate-agnostic clarifier is the operative spec text."

**Raj:** "Twelve prior contexts in the rear-view. — Northbridge was the high-water mark. Mercator was the bifurcation. Atrio was the multi-bank platform first. The European arc through six countries. Hill Country was the marketing-AI vendor swap. Saraswati was the edge-AI federated work. The Northbridge return was the M&A pattern proper. Polaris × Lloyd's was the reinsurance horizon. Lyceum was the FDA-enforcement foresight. Helvetian was the parliamentary scale. Argent Vector + Aerolith was the defense-electronics + frontier-AI cluster. Mission Plaza was the community-bank scale and the bench transition. — Brazos × Mission Plaza is post-merger integration with marketing-data as load-bearing. Cross-cloud anchor at the close boundary. Closest precedent is Atrio's coordinated-examiner-room, but here the chain crosses a vendor-merger boundary inside the acquiring bank itself and crosses two cloud substrates inside the audit window."

**Diana:** "And the cross-cloud framing."

**Raj:** "Routine. — That's the discipline today. The team treats cross-cloud as just another anchor type. The verifier dispatches against the §10.40 substrate-agnostic path; the byte-equality demonstration reads as routine; the room reads our calm familiarity as a form of evidence. — We do not narrate the operation as a heroic technical climax. The chain doesn't care which cloud the artifacts live on. The substrate-trust boundary is just another anchor."

**Diana:** "And Dawn."

**Raj:** "Dawn arrives at noon. Vendor-side, lead TesseraSeal liaison from MMPWorks. The engagement letter names her appearance, the spousal-disclosure paragraph governs, Tom logged the language three weeks ago with GC. Margarethe has met her in vendor capacity twice in the last quarter; Renata Whitley-Aguilar invited her in March; this isn't anyone's first meeting. The conversation at lunch is brief — Tom asks after Steve, asks about the house, and then everyone moves on. The work is the work."

**Diana:** "And the room reads it that way."

**Raj:** "The room reads it the way the team reads it. The seat change happened ten months ago. The work compounded across the seat change. Today is the engagement where the chain crosses two clouds inside one audit window; Dawn is the technical lead on the architecture from the vendor side; the audit confirms the architecture from the firm side. — Off the highway, next exit."

The SUV turns off Allen Parkway. The Brazos operations center comes into view — the fourteen stories of glass, the live oaks in the courtyard, the U.S. flag and the Texas flag flying on twin poles at the entrance, both at the same height.

**Diana** (looking at the building): "And the §10.40 question."

**Raj:** "Today's the day. Dawn filed the engagement-file note at Hill Country three years ago. The §10.40 substrate-agnostic clarifier extension shipped in a Herald release nine months ago — three months after she joined MMPWorks. Brazos × Mission Plaza is the first production engagement where the extension is exercised live. The byte-equality demonstration on the cross-cloud chain is the headline. — That's the engagement."

Raj parks the SUV in the visitor lot. They walk to the lobby.

## 7:15 AM — Lobby

The Brazos lobby is large, well-lit, and built for people in suits and for people in hard hats moving between the engineering wing and the executive wing without crossing one another's badge zones. A receptionist named Beulah greets the team by name; she has the badges printed and the photos already loaded. Margarethe is at the badge desk in a navy suit with a Texas-flag pin on the lapel. Donovan Eastlake-Boudreaux is next to her in a gray suit; he flew in from San Antonio yesterday afternoon and stayed at the same Hyatt. Hollis Trent-Mosley arrives from the elevator bay thirty seconds after the team clears security.

**Margarethe:** "Raj. Welcome to Houston."

**Raj:** "Margarethe. Donovan. Hollis. — Good to be on the ground."

**Margarethe:** "Renata is in the engagement room. Easton drove up from San Antonio last night; he's with her. The Insider-side and Yello-side counterparts joined by Teams at six this morning to confirm the pre-engagement integration prep was clean; they'll be on the bridge for Day 1 afternoon. Adelaide will be in and out across the three days. Yusuf from the regulatory practice in DC is on call from the §10.69 walk forward. — Tom, you and Donovan have the internal-audit partner walk at seven-thirty; Brigitte from Mission Plaza's IA team is joining by video."

**Tom:** "Engagement letter has it. We'll walk."

**Donovan** (to the team, briefly, his accent more East Texas than San Antonio): "Welcome. The Mission Plaza side — what's left of it under the integration — is grateful you came. Some of what you'll see today was built by Reyna Calderón-Esquivel before I took her seat; the rest is what we built across the seven months since close. The chain held. We're here to walk it together."

**Margarethe** (briefly, to Raj, in the elevator): "And Dawn — noon, the engagement letter names the appearance, Renata invited her, I countersigned. Yusuf from regulatory has cleared the spousal-disclosure paragraph language against the CFPB UDAAP settlement file from March. The frame is clean."

**Raj:** "Thank you for handling it cleanly."

**Margarethe:** "It's the right call. — I've read the Mission Plaza Story-20 engagement debrief Reyna sent me when we acquired. The recusal-protocol language has gotten cleaner each engagement; the spousal-disclosure paragraph reads as the natural next state. Brazos has nothing to hide from the regulators about Dawn being on the bridge today; everything that matters is in the engagement letter."

The elevator opens on the fifth floor. The engagement room is large, well-lit, set for a multi-day pass. Coffee carafes, sandwiches under cover for later, a single-page diagram on each chair: the §10.41 three-partition chain-coverage map with the pre-acquisition partition in pale gray, the cut-over window in pale blue (a thin band labeled `00:00:00 UTC Feb 1, 2026 ± 30 seconds`), the post-cut-over partition in green, and the November 2027 full-integration cut-over boundary indicated by a dashed line near the right edge of the map. The diagram is annotated with the spec-section labels — §10.39 (successor-attestation envelope) at the cut-over band, §10.40 (cross-vendor chain-merge anchor, substrate-agnostic) at the partition seam, §10.42 (backfill seal at close) at the band's left edge, §10.41 (partition closure boundary) at the November dashed line.

Sonya picks up the diagram. She looks at Tom. Tom nods once.

**Sonya** (quietly, to Raj): "The §10.41 map is the audit. The partitions are named; the boundaries are dated; the spec sections are labeled. The map is the architecture and the audit plan at the same time."

**Raj:** "Margarethe and Donovan stood it up at the cut-over ceremony seven months ago. Hollis ran the program. The map has been on the operations-center wall since February."

**Sonya:** "Pattern recognition. — The same kind of map Reyna handed out at Mission Plaza in November under §10.19; the same kind of map every well-run M&A integration produces under §10.41."

**Raj:** "Same discipline; different spec-section family. — That's the audit."

## 8:00 AM — Tom's four questions, both CAEs in the room

The room reassembles at 8:00 with both CAEs seated, Hollis on Margarethe's right, the M&A program register open on his laptop. Renata Whitley-Aguilar is at the back of the table with a tablet. Easton Wadsworth is next to her with the same notebook he carried at Mission Plaza in November.

Tom opens at the head of the table with his notebook and a pen.

**Tom:** "Engagement 31 for the team since the firm has been on TesseraSeal engagements; engagement 23 for Raj in the Lead seat; engagement 3 for the firm on a post-merger integration audit. — Four questions. — Margarethe, Donovan, in your own words."

He looks at Margarethe first.

**Tom:** "Question one. What does Brazos need from this audit?"

**Margarethe:** "Three things. — One: a confirmation memo we can put in front of the OCC post-merger examiner. The OCC examination opens 60 days after this engagement and consumes the spec-section confirmation memo as the first read on the cross-cloud and cross-vendor anchors. — Two: the cross-cloud byte-equality demonstration. Brazos's GC needs the demonstration on the firm's record because pre-merger marketing promises will land in pre-trial discovery for any next-three-years consumer suit naming the rebrand period; the cross-cloud byte-equality reproduction in court is the discipline Adelaide wants on file. — Three: the §10.41 partition closure memo for the November 2027 full-integration cut-over. Hollis owns the cut-over; the partition map closes cleanly under the same composition we used at the Feb 1 close; the memo gives Hollis his closure-discipline language in writing."

**Tom:** "Question two. What does Mission Plaza — Donovan — need from this audit?"

**Donovan:** "Two things. — One: confirmation that the partial deployment Reyna stood up before close held cleanly across the cross-cloud anchor at close. Reyna and I built the pre-close partial under §10.19's `pattern_2_partial_coverage_with_named_scope` declaration; the Phase A marketing-surface extension she signed Easton's budget on landed three weeks before close; the cross-cloud anchor at close was supposed to bind the entire pre-close chain into Brazos's Azure chain without losing the partial-deployment-era discipline. Today's audit is whether that held. — Two: the §10.69 per-customer disclosure across the merger boundary. The Mission Plaza legacy charter is a Texas state charter; the Texas Department of Banking examiner will ask for one cross-merger §1033 disclosure on the next exam cycle; the audit walks the disclosure today so we know the shape the Texas examiner will see."

**Tom:** "Question three. What does Renata need from this audit?"

**Renata:** "The cross-vendor marketing-stack handover under §10.21. The Insider footprint that ran Mission Plaza's cross-channel marketing automation and the Yello footprint that ran the account-opening journey both retired at close; the Salesforce Marketing Cloud + Marketo Engage stack on the Brazos side absorbed both customer-journey threads under §10.21 cross-vendor model-handover. The pre-merger HELOC pre-qualification offer that pivoted to a post-merger HELOC approval under a different product structure is the load-bearing reconciliation case; the chain has to span the marketing-data boundary because the chain says it does, and Brazos built it that way because the regulators are going to ask. — The other thing I need is the cross-vendor model-handover for the AI-decisioning surface itself. Mission Plaza ran its credit-decisioning model under the §10.21 Yello-to-underwriting boundary; Brazos runs its credit-decisioning model under Salesforce FSC + Brazos's own underwriting. The handover at close composed the two surfaces under one customer-journey trail; today's audit walks the composition."

**Tom:** "Question four. What does Hollis need from this audit?"

**Hollis Trent-Mosley** (M&A integration lead): "The November 2027 partition closure boundary. — The §10.41 map has three partitions today: pre-acquisition, cut-over window, post-cut-over. The November cut-over closes the partition map into a single coverage region under §10.41's partition closure attestation. The audit gives me the closure-discipline language in writing — the same composition we used at the Feb 1 close (§10.39 + §10.42), now scheduled for the November cut-over (§10.41 partition closure + §10.39 successor-attestation envelope's final-form revision). I want the language clean; the OCC and the Texas Department of Banking will both read the partition closure memo at next year's exam cycle."

Tom writes for ninety seconds without speaking. The room waits.

He looks up. He looks at Donovan.

**Tom:** "One follow-up to question two. — The cross-charter retention policy. Mission Plaza is a Texas state charter; Brazos is a federally-chartered national bank under OCC supervision. The Mission Plaza retention policy at close was the Texas Department of Banking's seven-year floor on customer records plus the FFIEC IT Handbook five-year floor on AI-decisioning chain entries. The Brazos retention policy is the OCC's seven-year floor plus the FFIEC five-year floor. The two policies overlap, but the chain entries on the Mission Plaza side at close were sealed under the Texas-charter retention discipline. — When the cross-cloud anchor binds Mission Plaza's chain into Brazos's chain, what's the operative retention policy for the legacy-side chain entries going forward?"

Donovan pauses.

**Donovan:** "The operative retention policy for the legacy-side chain entries going forward is — I want to walk through this carefully because I don't want to give you a partial answer. — The chain entries themselves are byte-identical pre-close and post-close; the cross-cloud anchor doesn't mutate the legacy bytes. The retention obligation on those bytes is the obligation Mission Plaza carried at the moment of sealing, plus any inheritance under the OCC's post-merger framework that applies to acquired institutional records. — My honest answer is I have not stress-tested the cross-charter inheritance language against the OCC's post-merger framework at the level you're asking. Adelaide on the GC side may have; I don't know that we've documented it in a way that holds up to a focused question at next year's exam."

Tom writes for thirty seconds. He looks at Margarethe.

**Margarethe:** "Adelaide and I walked the cross-charter retention question in March, after the CFPB settlement closed. The conversation was that the Brazos retention policy on legacy Mission Plaza records would be the more-conservative of the two — that is, where Brazos's policy is more conservative than Texas's, Brazos's applies; where Texas's was more conservative, Texas's continues to apply to the pre-close records under the inheritance discipline. Adelaide drafted a one-page policy note. — Donovan is right that we have not stress-tested the language against the OCC post-merger framework at the level Tom's asking. We have the policy note; we don't have the framework-fit memo."

**Tom** (writing): "*Cross-charter retention policy: Brazos applies more-conservative of Texas-charter + OCC-charter on a per-record basis; policy note drafted March 2026 by GC; framework-fit memo against OCC post-merger framework not yet produced. — Note logged. Not a Gap; not a Partial; documented for the close-out memo as a Nit-class observation with a remediation pathway named.*"

He looks up.

**Tom:** "Logged as a Nit. — Adelaide can produce the framework-fit memo before the OCC examination opens in 60 days; the remediation pathway is named; the institution carries the policy note in the interim. — Margarethe, Donovan, the four questions are answered. The audit shape for three days is clear: Day 1 morning cross-cloud anchor end-to-end, Day 1 afternoon marketing-stack handover with the HELOC pivot, Day 2 morning the rebrand-period UDAAP scene, Day 2 afternoon §10.69 + §10.70, Day 3 morning §10.71 with the Fed of Dallas on bridge, Day 3 afternoon the §10.41 partition closure memo and the Steve-by-video moment. — Raj?"

**Raj:** "Acknowledged. — Chen, you have the cross-cloud anchor walk at nine. Mike has the credit-decisioning composition at ten-thirty. Elena has the marketing-stack handover at eleven-fifteen. Coffee, then we walk."

Sonya catches Tom's eye across the table. Tom gives her the small nod he gave Dawn at Mission Plaza in November — the *one Nit, logged clean, no surprise* nod. The Mission Plaza pattern carries; Donovan's pause on the fourth question is the same kind of pause Reyna had on the fourth question at Mission Plaza ten months ago. The team registers it without comment.

## 9:00 AM — The §10.40 cross-cloud anchor walk

The Brazos engineering bench is on the seventh floor. Hollis takes the team up. The chain-of-custody operations lead is **Cyrille Beaumont-Whitlock**, mid-30s, ex-Microsoft Azure infrastructure-platform-team, six years at Brazos. He has the cross-cloud anchor on the projector when the team walks in.

**Cyrille:** "Chen, Mike, Raj — morning. The cross-cloud anchor. — Mission Plaza's last pre-close Merkle seal was sealed at 23:59:30 UTC Jan 31 under AWS CloudHSM in `us-east-1` against tenant `mission-plaza-bank-prod`. Brazos's first post-close seal was sealed at 00:00:01 UTC Feb 1 under Azure Key Vault Managed HSM in `eastus2` against tenant `brazos-federal-prod`. The cross-anchor binds the two roots in a single attestation envelope. — Walk?"

**Chen:** "Walk."

Cyrille opens a terminal. The cross-anchor envelope appears on the projector — a single JSON document with the §10.39 successor-attestation envelope at the top, the §10.40 cross-vendor chain-merge anchor in the middle, the §10.42 backfill seal at the bottom, and the dual-signature pair (Mission Plaza CFO + Brazos CFO) attested at the §10.17 partition-ceremony attestation level.

```json
{
  "ffiec.chain.spec": "v1.0",
  "ffiec.chain.format_version": "v1",
  "ffiec.chain.chain_kind": "audit",
  "ffiec.chain.run_id": "brazos-mission-plaza-cross-cloud-anchor-2026-02-01",
  "ffiec.chain.tenant_id": "brazos-federal-prod",
  "ffiec.chain.captured_at": "2026-02-01T00:00:01.000000000Z",
  "ffiec.chain.seq": 1,
  "ffiec.chain.payload_hash": "9e4c8b1f3a7d6e2c5b0a4f8d1c3e6b9a7d2f5c8e1b4a7d0c3f6b9e2a5d8c1f4b",
  "ffiec.chain.prev_hash":    "0000000000000000000000000000000000000000000000000000000000000000",
  "ffiec.chain.key_version": 7,
  "ffiec.chain.key_fingerprint": "a3d8f2c5b9e4a1c6f0d3b7e2a5c8f1b4",
  "ffiec.chain.mac_computed_at_utc": "2026-02-01T00:00:01.488Z",
  "ffiec.chain.kms_handle_uri": "azure-akv-mhsm:vault/brazos-prod-mhsm/key/k-brazos-cross-anchor-2026q1",
  "ffiec.chain.canonical_encoding": "rfc8785-jcs",
  "ffiec.chain.region": "eastus2",
  "event": "cross_vendor_chain_merge_anchor.placed",

  "audit.successor_attestation.acquirer_institution": "brazos-federal-bancshares",
  "audit.successor_attestation.acquired_institution": "mission-plaza-bank",
  "audit.successor_attestation.acquirer_charter_type": "occ-national-bank",
  "audit.successor_attestation.acquired_charter_type": "texas-state-bank",
  "audit.successor_attestation.close_timestamp_utc": "2026-02-01T00:00:00.000Z",
  "audit.successor_attestation.acquirer_hsm_key_fingerprint": "a3d8f2c5b9e4a1c6f0d3b7e2a5c8f1b4",
  "audit.successor_attestation.acquirer_hsm_substrate": "azure-key-vault-managed-hsm",
  "audit.successor_attestation.acquired_hsm_key_fingerprint": "7c2e9b4f1a8d6e3c0f5b8a2e7d1c4f9b",
  "audit.successor_attestation.acquired_hsm_substrate": "aws-cloudhsm",
  "audit.successor_attestation.acquirer_cfo_signature_ref": "brazos-cfo-2026q1-sig-001",
  "audit.successor_attestation.acquired_cfo_signature_ref": "mission-plaza-cfo-2026q1-sig-final",

  "audit.cross_vendor_chain_merge.acquired_chain_terminal_seal_id": "seal-mission-plaza-bank-prod-2026-01-31",
  "audit.cross_vendor_chain_merge.acquired_chain_terminal_merkle_root": "5f8a2c1e9b4d7f0c3a6e9b2d5f8a1c4e7b0d3f6a9c2e5b8d1a4f7c0e3b6d9f2a",
  "audit.cross_vendor_chain_merge.acquired_chain_terminal_seal_at_utc": "2026-01-31T23:59:30.000Z",
  "audit.cross_vendor_chain_merge.acquired_chain_entry_count_total": 4892346,
  "audit.cross_vendor_chain_merge.substrate_agnostic_clarifier_applied": true,
  "audit.cross_vendor_chain_merge.cross_substrate_pair": "aws-s3-aws-cloudhsm__azure-blob-azure-akv-mhsm",
  "audit.cross_vendor_chain_merge.byte_equality_method": "rfc8785-jcs-sha256",

  "audit.backfill_seal.applied": true,
  "audit.backfill_seal.scope": "mission-plaza-bank-prod-pre-close-baseline",
  "audit.backfill_seal.baseline_start_utc": "2025-08-01T00:00:00.000Z",
  "audit.backfill_seal.baseline_end_utc": "2026-01-31T23:59:30.000Z",
  "audit.backfill_seal.baseline_entry_count": 4892346,
  "audit.backfill_seal.envelope_root": "5f8a2c1e9b4d7f0c3a6e9b2d5f8a1c4e7b0d3f6a9c2e5b8d1a4f7c0e3b6d9f2a",

  "audit.partition_coverage.partitions": [
    {
      "partition_id": "pre-acquisition",
      "start_utc": "2025-08-01T00:00:00.000Z",
      "end_utc":   "2026-01-31T23:59:30.000Z",
      "substrate": "aws-s3-aws-cloudhsm",
      "entry_count": 4892346,
      "tenant_id":   "mission-plaza-bank-prod"
    },
    {
      "partition_id": "cut-over-window",
      "start_utc": "2026-01-31T23:59:30.000Z",
      "end_utc":   "2026-02-01T00:00:01.000Z",
      "substrate": "n/a (no-write window)",
      "entry_count": 0,
      "tenant_id":   "n/a"
    },
    {
      "partition_id": "post-cut-over",
      "start_utc": "2026-02-01T00:00:01.000Z",
      "end_utc":   "open",
      "substrate": "azure-blob-azure-akv-mhsm",
      "entry_count": "open",
      "tenant_id":   "brazos-federal-prod"
    }
  ],

  "audit.late_arriving_entry_seal_discipline.applied": true,
  "audit.late_arriving_entry_seal_discipline.window_utc": "2026-01-31T23:59:30.000Z..2026-02-01T00:00:01.000Z",
  "audit.late_arriving_entry_seal_discipline.entries_received_in_window": 0,
  "audit.late_arriving_entry_seal_discipline.supplemental_seal_required": false
}
```

Chen reads it once. Then again.

**Chen:** "Run the verifier on the cross-anchor."

Cyrille types.

```
$ herald-verify --tenant=brazos-federal-prod \
                --entry-id=ce_a3d8f2... \
                --strict --explain \
                --cross-substrate-walk
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified
        against public key brazos-cross-anchor-2026q1,
        cross-substrate dispatch resolved,
        successor-attestation envelope verified,
        backfill seal envelope root recomputed,
        partition-coverage map resolved

additional_verifications:
  - cross_vendor_chain_merge_anchor_verified
  - cross_substrate_dispatch_walked
  - substrate_agnostic_clarifier_applied
  - successor_attestation_envelope_verified
  - dual_cfo_signature_pair_verified
  - backfill_seal_baseline_envelope_root_recomputed
  - partition_coverage_map_three_partition_verified
  - late_arriving_entry_seal_discipline_no_window_writes_confirmed

cross_substrate_pair:
  acquired_chain_terminal_substrate: aws-s3-aws-cloudhsm
  acquirer_first_seal_substrate:     azure-blob-azure-akv-mhsm
  byte_equality_method:              rfc8785-jcs-sha256
  acquired_terminal_merkle_root_recomputed: true
  acquired_terminal_merkle_root_match:      true

elapsed: 5m48s
```

Chen reads the verifier output line by line.

**Chen:** "Five minutes forty-eight seconds. — Cross-substrate dispatch. Substrate-agnostic clarifier applied. Eight additional verifications resolved. — Walk me through the byte-equality reconciliation."

**Cyrille:** "The byte-equality reconciliation pulls Mission Plaza's terminal seal record from AWS S3 in `us-east-1`, recomputes the Merkle root over Mission Plaza's last pre-close entries in canonical bytes per RFC 8785, and compares against the `acquired_chain_terminal_merkle_root` field in the cross-anchor envelope. The reconciliation reads the legacy chain entries from cold tier — they're under compliance-mode object lock with a retention floor that exceeds the cross-charter inheritance discipline by 14 months — and recomputes the SHA-256 over canonical bytes. The substrate-agnostic clarifier means the verifier dispatches against the §10.40 substrate-agnostic code path; it doesn't care whether the legacy seal record came from AWS S3 or from Azure Blob or from on-prem object storage. The Merkle root is the same Merkle root either way."

**Mike:** "And the cross-substrate pair — `aws-s3-aws-cloudhsm__azure-blob-azure-akv-mhsm` — is the canonical pair the §10.40 substrate-agnostic clarifier names?"

**Cyrille:** "The §10.40 substrate-agnostic clarifier names the pair-class abstractly — `<acquired-substrate>__<acquirer-substrate>` — and the canonical pair for this engagement is the concrete instantiation. The verifier resolves the pair-class to the §10.40 dispatch table; the dispatch table lists every known substrate pair and the substrate-pair-specific reconciliation walker. For pairs the dispatch table doesn't list, the verifier falls back to the substrate-agnostic generic walker — which just reads the bytes from wherever the institution names them and recomputes the SHA-256. Our pair is in the table, so we get the slightly-faster substrate-pair-specific walker. The substrate-agnostic generic walker would have produced the same answer in eight minutes instead of five forty-eight."

**Chen:** "And the dual-CFO signature pair?"

Cyrille pulls up the §10.39 signature pair. Mission Plaza's CFO — **Hortense Marbury-Caldwell**, who retired three months after close — signed under AWS CloudHSM at 23:59:45 UTC Jan 31, 2026; Brazos's CFO — **Tobias Wendell-Kincaid** — signed under Azure Key Vault Managed HSM at 00:00:00.500 UTC Feb 1, 2026. The two signatures attest the successor-attestation envelope under §10.17 partition-ceremony attestation discipline.

```
dual_signature_pair §10.39:
  acquired_party:
    institution:    mission-plaza-bank
    signer:         hortense-marbury-caldwell-cfo
    signer_role:    cfo (final-attestation, pre-retirement, pre-close-of-business)
    hsm_substrate:  aws-cloudhsm
    hsm_handle:     aws-cloudhsm:cluster/cluster-mp-prod/key/k-mp-cfo-2026q1-final
    signed_at_utc:  2026-01-31T23:59:45.000Z
    signature_alg:  ed25519
    signature:      MEUCIQDk5...base64-encoded-Ed25519...

  acquirer_party:
    institution:    brazos-federal-bancshares
    signer:         tobias-wendell-kincaid-cfo
    signer_role:    cfo (first-attestation, post-close, institutional-acceptance)
    hsm_substrate:  azure-key-vault-managed-hsm
    hsm_handle:     azure-akv-mhsm:vault/brazos-prod-mhsm/key/k-brazos-cfo-2026q1
    signed_at_utc:  2026-02-01T00:00:00.500Z
    signature_alg:  ed25519
    signature:      MEYCIQDp9...base64-encoded-Ed25519...

  envelope_integrity:
    enclosed_envelope_hash: 9e4c8b1f3a7d6e2c5b0a4f8d1c3e6b9a7d2f5c8e1b4a7d0c3f6b9e2a5d8c1f4b
    enclosed_envelope_signed_by_both_parties: true
    cross_substrate_signature_pair_verified: true
```

Chen reads it. He reads it again.

**Chen:** "The dual signatures are produced under two different HSM substrates fifteen seconds apart. The first under AWS CloudHSM in `us-east-1`; the second under Azure Key Vault Managed HSM in `eastus2`. The enclosed envelope is bit-identical to both signers at the moment of signing. — The §10.39 clarifier on `acquirer_hsm_key_fingerprint` substrate-agnosticism."

**Cyrille:** "Substrate-agnostic per the §10.39 clarifier paragraph. Any FIPS 140-2 Level 3+ HSM's public-key fingerprint is treated equivalently regardless of substrate. The verifier resolves both signatures against the published fingerprints under §10.5; the §10.5 attestation registry has the AWS CloudHSM partition attestation document and the Azure Key Vault Managed HSM attestation document side-by-side. Both attestations carry FIPS 140-2 Level 3 evaluation references; the verifier accepts both as Level 3+ HSM custody under §10.5 without distinguishing between substrate vendors."

**Raj:** "And the §10.42 backfill seal."

Cyrille pulls up the §10.42 backfill seal record. The seal was applied at close — a one-time seal at 00:00:01 UTC Feb 1 that produced a chain-shaped envelope retroactively over Mission Plaza's pre-close baseline (the six months from August 1, 2025 — Mission Plaza's TesseraSeal go-live — through January 31, 2026). The backfill seal does not mutate the legacy chain entries; it produces an envelope-level Merkle root over the legacy chain that the cross-anchor envelope can reference by hash without rewriting the legacy entries.

**Cyrille:** "The backfill seal is a wrapper. The legacy entries are byte-identical pre-seal and post-seal. The wrapper produces a single envelope root over the 4,892,346 pre-close entries; the envelope root is bound into the cross-anchor; the cross-anchor binds into Brazos's first post-close seal. The legacy chain entries reference the envelope by hash; the envelope references the cross-anchor by hash; the cross-anchor references the first post-close seal by hash. The chain is continuous from August 2025 through today; the substrate boundary is one anchor inside the continuous chain."

**Chen:** "Run the byte-equality reconciliation again on the full pre-close baseline."

Cyrille types.

```
$ herald-verify-handover --acquired-tenant=mission-plaza-bank-prod \
                         --acquirer-tenant=brazos-federal-prod \
                         --cross-anchor-id=ce_a3d8f2... \
                         --reconcile-acquired-baseline \
                         --substrate-agnostic-walk \
                         --strict
```

The terminal ticks. The reconciliation reads the 4,892,346 pre-close chain entries from AWS S3 cold tier in `us-east-1`, recomputes the Merkle root in canonical bytes, compares against the envelope root, walks the cross-anchor binding, walks the first post-close seal binding, walks the dual-CFO signature pair, walks the partition-coverage map. The output completes at five minutes forty-eight seconds — the same elapsed time as the first walk, because the cold-tier prefetch is warm from the morning.

```
Status: PASS
Step:   12
Reason: pre-close baseline byte-equality reconciled
        against backfill seal envelope root;
        cross-anchor binding verified;
        first post-close seal binding verified;
        dual-CFO signature pair verified across substrates;
        partition-coverage map three-partition resolved;
        substrate-agnostic clarifier applied throughout

Cross-substrate markers:
  cross_vendor_chain_merge_anchor_verified
  cross_substrate_dispatch_walked
  substrate_agnostic_clarifier_applied
  acquired_baseline_envelope_root_byte_equal
  successor_attestation_envelope_verified
  dual_cfo_signature_pair_verified_across_substrates
  partition_coverage_map_three_partition_verified

Elapsed: 5m48s
```

Chen sits back. He pours another cup of coffee from the carafe.

**Chen:** "Six minutes for byte-equality across two clouds, two HSM substrates, two charters, 4.89 million pre-close chain entries, a backfill seal envelope, a cross-anchor, a first post-close seal, a dual-CFO signature pair, and a three-partition coverage map. — That's the headline."

**Cyrille** (small smile): "Cross-cloud is the new same-cloud. The chain doesn't care where the artifacts live."

**Raj** (writing): "*§10.40 substrate-agnostic clarifier exercised live; byte-equality reconciliation across AWS↔Azure in five minutes forty-eight seconds; eight additional verifications resolved cleanly; cross-substrate dispatch is operational. — The chain doesn't care which cloud the artifacts live on. The substrate-trust boundary is just another anchor.*"

> ### Confirmation #1 — Cross-cloud chain consolidation under §10.40 substrate-agnostic clarifier reconciles byte-equal in five minutes forty-eight seconds
>
> The cross-vendor chain-merge anchor placed at 00:00:01 UTC Feb 1, 2026 binds Mission Plaza's full pre-close chain (4,892,346 entries on AWS S3 / AWS CloudHSM under the Texas state charter) into Brazos's Azure chain (Azure Blob Storage / Azure Key Vault Managed HSM under the OCC national-bank charter). The §10.40 substrate-agnostic clarifier dispatches against the cross-substrate pair `aws-s3-aws-cloudhsm__azure-blob-azure-akv-mhsm`; the verifier emits `cross_vendor_chain_merge_anchor_verified`, `cross_substrate_dispatch_walked`, `substrate_agnostic_clarifier_applied`, `acquired_baseline_envelope_root_byte_equal`, `successor_attestation_envelope_verified`, `dual_cfo_signature_pair_verified_across_substrates`, and `partition_coverage_map_three_partition_verified` as additional verifications under §10.12. The dual-CFO signature pair under §10.39 — Mission Plaza CFO signed under AWS CloudHSM at 23:59:45 UTC Jan 31, Brazos CFO signed under Azure Key Vault Managed HSM at 00:00:00.500 UTC Feb 1 — verifies cross-substrate against both signers' published Ed25519 fingerprints under §10.5 attestation discipline. The §10.42 backfill seal envelope over the pre-close baseline recomputes byte-equal against the envelope root. The §10.41 three-partition coverage map resolves: pre-acquisition (4,892,346 entries on AWS), cut-over window (zero entries; §10.36 supplemental-seal mechanism armed but unexercised), post-cut-over (open on Azure). End-to-end reconciliation completes in five minutes forty-eight seconds.

Chen runs the verifier two more times against different entries — a chain entry from August 4, 2025 (Mission Plaza's earliest production seal), a chain entry from December 24, 2025 (a heavy-traffic holiday day on the Mission Plaza fraud-screen surface), a chain entry from February 12, 2026 (the first post-close week, after the brand transition began). Each verifies. The cross-substrate dispatch walks cleanly for each. The substrate-agnostic clarifier resolves the same dispatch path for each.

**Chen:** "Sample size of three on either side of the boundary plus the cross-anchor itself. The chain holds across the substrate boundary. — Coffee."

The team breaks at 10:15. Sonya pours coffee at the carafe and stands next to Raj.

**Sonya:** "Cross-cloud reads as routine."

**Raj:** "Cross-cloud reads as routine. — That's the discipline. The team treats the operation as just another anchor type. The room reads our calm familiarity as evidence."

**Sonya:** "And the §10.36 supplemental-seal mechanism?"

**Raj:** "Armed but unexercised. The cut-over window between Mission Plaza's last AWS seal at 23:59:30 UTC Jan 31 and Brazos's first Azure seal at 00:00:01 UTC Feb 1 was a 31-second no-write window — both institutions stopped writes from 23:59:00 to 00:00:30 UTC under the cut-over runbook. No entries arrived in the window. The §10.36 supplemental-seal mechanism would have absorbed any that did; the verifier confirmed `entries_received_in_window: 0`. — That's the operational discipline Hollis ran the cut-over to. The runbook called for the supplemental-seal mechanism to be armed; the discipline confirmed no entries needed it."

**Sonya:** "And the Mission Plaza Story-20 partial-deployment shape carried into the post-close architecture cleanly."

**Raj:** "Carried cleanly. — Reyna and Donovan stood up the §10.19 `pattern_2_partial_coverage_with_named_scope` declaration on Day 1 of Mission Plaza's deployment thirteen months ago. The Phase A marketing-surface extension Easton signed budget on landed three weeks before close. The cross-cloud anchor at close inherited the partial-deployment-era declaration into Brazos's post-close §10.41 partition map. The pre-acquisition partition carries the `pattern_2_partial_coverage_with_named_scope` marker; the cut-over window carries no entries; the post-cut-over partition carries the Brazos `pattern_1_full_coverage` marker. The verifier resolves the two markers cleanly across the partition boundary."

**Sonya:** "Different shape; same discipline."

**Raj:** "Different shape; same discipline. — The Mission Plaza Story-20 engagement built the pre-close partial. Today's audit confirms the partial composed into the acquirer's full coverage under one continuous chain."

## 10:30 AM — The §10.21 cross-vendor model-handover for the AI-decisioning surface

Mike opens his laptop. The credit-decisioning composition is the load-bearing case for the AI-decisioning surface — Mission Plaza ran its credit-decisioning model under the §10.21 Yello-to-underwriting boundary on AWS; Brazos runs its credit-decisioning model under Salesforce FSC + Brazos's own underwriting on Azure; the handover at close composed the two surfaces under one customer-journey trail through the §10.21 cross-vendor model-handover envelope.

Cyrille pulls up the §10.21 handover chain entry — sealed at close, binding the Mission Plaza credit-decisioning model surface to the Brazos credit-decisioning model surface under the cross-cloud anchor.

```json
{
  "ffiec.chain.run_id": "mp-to-brazos-credit-decisioning-handover-2026-02-01",
  "ffiec.chain.chain_kind": "audit",
  "ffiec.chain.captured_at": "2026-02-01T00:00:01.500000000Z",
  "ffiec.chain.tenant_id": "brazos-federal-prod",
  "event": "model_handover.cross_institutional_acquisition",

  "audit.model_handover.provider": "mission-plaza-bank-legacy",
  "audit.model_handover.receiver": "brazos-federal-bancshares",
  "audit.model_handover.model_class": "credit-decisioning",
  "audit.model_handover.legacy_model_id":     "mission-plaza/credit-decision-gbm",
  "audit.model_handover.legacy_model_version": "credit-decision-gbm-v2-2026q1-final",
  "audit.model_handover.legacy_model_card_sha256": "8e3c1f4b9a7d2c6e0f5b8a4d1c3f6b9e2a5d8c1f4b7e0a3d6c9f2b5e8a1d4c7f",
  "audit.model_handover.legacy_inference_count_lifetime": 11247,
  "audit.model_handover.legacy_dictionary_version_at_close": "mission-plaza-rc-2026q1-final",
  "audit.model_handover.legacy_dictionary_artifact_sha256": "b4e8c2a6d0f4b8e2c6a0d4f8b2e6c0a4d8b2e6c0a4d8b2e6c0a4d8b2e6c0a4d8",
  "audit.model_handover.successor_model_id":      "brazos/credit-decision-xgb-ensemble",
  "audit.model_handover.successor_model_version": "credit-decision-xgb-v3-2026q1",
  "audit.model_handover.successor_dictionary_version": "brazos-rc-2026q1",
  "audit.model_handover.successor_dictionary_artifact_sha256": "c5d9e3a7f1b5e9c3a7d1f5b9e3c7a1d5f9b3e7c1a5d9f3b7e1c5a9d3f7b1e5c9",
  "audit.model_handover.composition_method": "decisioning_pivot_with_preserved_lineage",
  "audit.model_handover.legacy_inference_lookup_window_years": 7,
  "audit.model_handover.cross_substrate_pair": "aws-s3-aws-cloudhsm__azure-blob-azure-akv-mhsm"
}
```

**Mike:** "The composition method — `decisioning_pivot_with_preserved_lineage`. Walk it."

**Cyrille:** "The two credit-decisioning surfaces are not the same model. Mission Plaza's GBM ran a different feature set, a different reason-code dictionary, a different policy-version ceiling than Brazos's XGB ensemble. The composition at close doesn't merge the two surfaces into one; it pivots from one surface to the other at close, with the legacy surface's lineage preserved by reference. A post-close credit decision under Brazos's XGB references the customer's legacy credit-history under Mission Plaza's GBM if the customer was a Mission Plaza customer pre-close; the reference is integrity-bound via the §10.11.1 `prior_offer_run_id` / `prior_offer_seq` parent-linkage fields plus the cross-substrate dispatch through §10.40. Mission Plaza's legacy inferences are retained in the chain for the seven-year retention window and remain reachable from post-close credit decisions through the parent-linkage chain plus the cross-anchor."

**Mike:** "And the dictionary-version transition?"

**Cyrille:** "Two dictionaries. Mission Plaza's `mission-plaza-rc-2026q1-final` is the dictionary in force at close; it's the last Mission Plaza dictionary version. Brazos's `brazos-rc-2026q1` is the first post-close dictionary version. The two dictionaries are different reason-code dictionaries; a post-close credit decision on a Mission Plaza legacy customer uses the Brazos dictionary; a retrospective reinvestigation on a pre-close Mission Plaza credit decision uses Mission Plaza's dictionary in force at the time of the original decision — `mission-plaza-rc-2026q1-final` or one of its predecessors. The dictionaries are decision-time-bound under §10.11.1; the SR 11-7 model-risk binders for the two institutions track the two dictionary lineages separately."

Mike picks a load-bearing case. A customer who received a Mission Plaza HELOC pre-qualification under the legacy GBM on January 17, 2026 — two weeks before close — and applied for a HELOC under Brazos's XGB on May 22, 2026, four months after close. Customer ID, in Brazos's post-close customer-master, `brazos-cust-mp-legacy-42117`.

Cyrille pulls up the chain entries.

```
chain trail for customer brazos-cust-mp-legacy-42117:
  entries (chronologically):

  [pre-close, Mission Plaza chain, AWS-resident]
  1.  2025-08-11  account_opening.yello_handover           (Mission Plaza)
  2.  2025-08-11  fraud_screen.decision                    (pass_to_underwriting)
  3.  2025-08-11  credit_decision.decision                 (checking_account_approved)
  4.  2025-09-04  marketing.touchpoint.email_open          (Insider, evidentiary substitute pre-Phase-A)
  5.  2025-11-12  marketing.touchpoint.click_through       (Insider, Phase A post-go-live, chain-bound)
  6.  2026-01-17  marketing.heloc_pre_qualification_offer  (Insider, Phase A, chain-bound)
       - offer_text:           "you're pre-qualified for a $50K HELOC at 6.875%"
       - offer_hash:           5e2f8b1c4a7d0e3f6b9c2a5d8f1b4e7c0a3d6f9b2e5c8a1d4f7b0e3c6a9d2f5b
       - model_version:        insider/next-best-action-2026q1
       - template_id:          insider-tmpl-heloc-pre-qual-2026q1-a
       - variable_binding_hash: 3c9f6b2e5a8d1c4f7b0e3a6d9c2f5b8e1a4d7c0f3b6e9a2d5c8f1b4e7a0d3c6f
       - audit.cross_vendor_handover.source_vendor: insider
       - audit.cross_vendor_handover.source_signature_ref: insider-2026q1-sig-final

  [cut-over window, 31-second no-write band]
  --  2026-01-31 23:59:30 UTC → 2026-02-01 00:00:01 UTC  (no entries)

  [post-close, Brazos chain, Azure-resident]
  7.  2026-02-04  marketing.touchpoint.email_send          (SFMC, rebrand campaign, chain-bound)
  8.  2026-02-04  marketing.touchpoint.email_open          (SFMC, rebrand campaign, chain-bound)
  9.  2026-02-04  marketing.touchpoint.click_through       (SFMC, rebrand campaign, chain-bound)
  10. 2026-05-15  marketing.heloc_pre_qualification_offer  (Marketo Engage, chain-bound)
       - offer_text:           "Brazos HELOC up to $50K, rates from 7.125%"
       - offer_hash:           7b4e1c8d2a5f9b3e6c0a4d7f2b5e8c1a9d3f6b0e2c5a8d1f4b7e0c3a6d9f2b5e
       - model_version:        marketo/next-best-action-brazos-2026q2
       - prior_offer_reference_run_id: marketing.heloc_pre_qualification_offer.2026-01-17.mp-legacy
       - prior_offer_reference_status: linked
       - cross_substrate_pair: aws-s3-aws-cloudhsm__azure-blob-azure-akv-mhsm

  11. 2026-05-22  application.heloc                        (Salesforce FSC handover to Brazos UW)
  12. 2026-05-22  fraud_screen.decision                    (pass_to_underwriting)
  13. 2026-05-22  credit_decision.decision                 (approved, $50K, 7.250%, 10-year term)
       - product:              brazos-heloc-2026-standard
       - decision:             approved
       - decision_confidence:  0.91
       - rate_offered:         7.250
       - reason_codes:         []  (approval; no adverse reasons)
       - dictionary_version:   brazos-rc-2026q1
       - prior_offer_chain:
         - 2026-05-15 marketing.heloc_pre_qualification_offer (brazos)
         - 2026-01-17 marketing.heloc_pre_qualification_offer (mission-plaza-legacy, cross-substrate)
       - prior_offer_run_id:      marketing.heloc_pre_qualification_offer.2026-01-17.mp-legacy
       - prior_offer_seq:         6
       - prior_offer_status:      linked
       - prior_offer_substrate:   aws-s3-aws-cloudhsm
       - cross_substrate_walk:    walked
```

Mike reads through to the end.

**Mike:** "The May 22 credit decision binds the prior-offer reference to the May 15 Brazos offer and to the January 17 Mission Plaza legacy offer. — Run the verifier."

Cyrille types.

```
$ herald-verify --tenant=brazos-federal-prod \
                --entry-id=credit-decision-2026-05-22-brazos-cust-mp-legacy-42117 \
                --strict --explain \
                --cross-substrate-walk \
                --resolve-prior-offer-chain
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified,
        prior-offer chain walked transitively,
        cross-substrate prior-offer reference resolved,
        ECOA adverse-action-family schema validated
        (no adverse reasons; approval entry)

additional_verifications:
  - prior_offer_chain_walked
  - cross_substrate_prior_offer_reference_resolved
  - marketing_prior_offer_reference_resolved (x2: brazos + mp-legacy)
  - cross_vendor_handover_anchor_verified (x2: SFMC + Marketo Engage)
  - ecoa_adverse_action_family_schema_validated

prior_offer_chain:
  immediate_prior_offer:
    run_id:     marketing.heloc_pre_qualification_offer.2026-05-15.brazos
    seq:        10
    substrate:  azure-blob-azure-akv-mhsm
    status:     resolved
  transitive_prior_offer:
    run_id:     marketing.heloc_pre_qualification_offer.2026-01-17.mp-legacy
    seq:        6
    substrate:  aws-s3-aws-cloudhsm
    status:     resolved (via cross-substrate dispatch, cross-anchor binding)
    cross_anchor_id: ce_a3d8f2... (cross-vendor chain-merge anchor 2026-02-01)
elapsed: 1.4s
```

Mike sits back.

**Mike:** "The post-close credit decision walks the prior-offer chain through the May 15 Brazos offer and the January 17 Mission Plaza legacy offer transitively. The cross-substrate dispatch resolves through the cross-anchor binding at close. The §10.11.1 prior-offer parent-linkage closes the reference loop across the merger boundary and across the substrate boundary. — One point four seconds."

**Cyrille:** "The verifier doesn't pull the legacy offer's bytes from AWS S3 cold tier unless the entry is requested at byte-equality; the reference resolution walks the cross-anchor binding, the cross-anchor verifies the legacy chain's Merkle root recomputed byte-equal at engagement-open this morning, and the prior-offer reference resolves against the legacy chain entry's bound run_id and seq. — If a customer or a regulator wants byte-equality on the legacy offer specifically, the `--reconcile-legacy-offer-byte-equal` flag pulls the legacy offer's bytes from cold tier and recomputes the SHA-256 against the chain-bound offer_hash. That walk completes in about thirty seconds for a single offer entry. — We can run it if you want."

**Mike:** "Run it."

Cyrille types. The reconciliation completes in twenty-eight seconds. The legacy offer's bytes — the rendered HTML of the Insider pre-qualification email as it went to the customer on January 17, 2026 — recompute byte-equal against the chain-bound offer_hash.

**Mike:** "Walked. — The May 22 credit decision references the January 17 Mission Plaza legacy offer through one chain entry plus one cross-anchor plus one prior-offer parent-linkage. The reference is integrity-bound; the substrate boundary is one anchor; the substrate-trust boundary doesn't move the integrity claim. — Cyrille, the load-bearing piece is that the post-close credit decision's `prior_offer_status: linked` field is integrity-binding the linkage, not just naming it. The verifier walks the linkage and confirms the legacy entry exists and is bound to the legacy chain's Merkle root that the cross-anchor binds. — That's the chain reading the integrity claim from the §10.11.1 family across the merger boundary and across the substrate boundary in one walk."

**Cyrille:** "One walk. The §10.11.1 parent-linkage is substrate-agnostic by construction — the parent-linkage fields are `prior_offer_run_id` and `prior_offer_seq`, both opaque strings. The verifier resolves the parent-linkage against whatever substrate the parent chain entry lives on; the §10.40 cross-anchor binds the substrate boundary."

> ### Confirmation #2 — §10.11.1 prior-offer parent-linkage closes the marketing-to-credit reference loop across the merger boundary and across the substrate boundary
>
> The May 22, 2026 HELOC credit decision for customer `brazos-cust-mp-legacy-42117` binds two prior-offer references through the `audit.ecoa.adverse_action.prior_offer_run_id` / `prior_offer_seq` parent-linkage fields plus the `prior_offer_status: linked` integrity-binding marker: the May 15 Brazos pre-qualification offer (Marketo Engage, post-close, Azure-resident) and the January 17 Mission Plaza legacy pre-qualification offer (Insider, pre-close, AWS-resident). The transitive prior-offer reference resolves through the §10.40 cross-anchor binding placed at close; the substrate boundary is one anchor inside the continuous reference chain. The verifier walks the chain transitively in 1.4 seconds (reference resolution) or 28 seconds (full byte-equality reconciliation of the legacy offer's rendered HTML against the chain-bound offer_hash). The §10.11.1 family is operational across the merger boundary; the §10.11.1 parent-linkage is substrate-agnostic by construction; the §10.40 cross-anchor closes the substrate-boundary integrity claim.

Mike picks two more cases — a customer whose legacy Mission Plaza pre-qualification offer led to a pre-close HELOC approval that was later refinanced post-close under Brazos's rate sheet, and a customer whose legacy Mission Plaza credit-card pre-qualification offer led to no post-close application (the reference chain is half-open; the credit decision side never fires). Both cases walk cleanly. The half-open reference (legacy offer with no post-close response) is in chain as the legacy offer entry under the pre-close partition and stops there; the post-close credit-decision side is not populated for this customer; the verifier confirms the legacy entry is bound, integrity-claimed, and reachable via the cross-anchor for any future disclosure or examination request.

**Mike:** "Three cases walked. The §10.11.1 parent-linkage closes the marketing-to-credit reference loop cleanly across the merger boundary. — Eleven fifteen. Elena, the marketing-stack handover next."

## 11:15 AM — The §10.21 marketing-stack handover

Elena takes the bench. Insider and Yello have each retired from the Mission Plaza side; Salesforce Marketing Cloud + Marketo Engage handles the Brazos side; the §10.21 cross-vendor model-handover envelope at close bound the Insider chain and the Yello chain into the Brazos marketing chain under two separate handover-anchor entries — one per outgoing vendor — and the §10.21.4 vendor-version-registry lookup keeps the legacy version-card lookup endpoints alive at Insider's and Yello's published commitments for six years from version retirement.

Cyrille pulls up the §10.21 handover entries.

```
§10.21 cross-vendor model-handover entries at close, mission-plaza-bank → brazos-federal:

  1. insider-to-sfmc-marketo-handover-2026-02-01
     - source_vendor:         insider
     - source_substrate:      aws (Insider's vendor-hosted AWS instance)
     - target_vendor:         salesforce-marketing-cloud + marketo-engage (composite)
     - target_substrate:      azure (Brazos's Azure instance)
     - retired_model_classes:
       * cross-channel personalization (Insider next-best-action)
       * AI-personalization-for-offers (Insider personalization layer)
       * send-time optimization (Insider STO model family)
     - successor_model_classes:
       * Salesforce Einstein for Marketing Cloud (next-best-action, send-time, journey orchestration)
       * Marketo Engage Predictive Audiences (audience segmentation)
       * Brazos's in-house ML for personalization-for-offers (custom on Azure ML)
     - composition_method:    "vendor_retirement_with_legacy_lookup_preserved"
     - legacy_inference_lookup_window_years: 6  (per §10.21.4 Insider commitment, 6yr from version retirement)
     - cross_substrate_pair:  aws__azure
     - vendor_version_registry_lookup_endpoint: insider.com/api/v2/version-card  (still live)
     - vendor_version_registry_retention_attestation_signature_ref: insider-vvr-2026q1-retention-attestation-001

  2. yello-to-sfsc-handover-2026-02-01
     - source_vendor:         yello
     - source_substrate:      aws (Yello's vendor-hosted AWS instance)
     - target_vendor:         salesforce-financial-services-cloud
     - target_substrate:      azure (Brazos's Azure instance)
     - retired_model_classes:
       * account-opening journey orchestration (Yello)
       * front-of-funnel application capture (Yello)
     - successor_model_classes:
       * Salesforce FSC journey orchestration
       * Brazos's in-house front-of-funnel ML on Azure ML
     - composition_method:    "vendor_retirement_with_legacy_lookup_preserved"
     - legacy_inference_lookup_window_years: 6
     - cross_substrate_pair:  aws__azure
     - vendor_version_registry_lookup_endpoint: yello.io/api/v1/version-card  (still live)
```

**Elena:** "Two handover anchors at close. Insider out, SFMC + Marketo Engage in. Yello out, Salesforce FSC in. The §10.21.4 vendor-version-registry lookup endpoints remain live for six years per the published commitments. — Walk the load-bearing case. Pick a customer whose legacy Insider next-best-action model picked a specific creative on a specific date pre-close, then trace what the chain produces."

Cyrille pulls a load-bearing customer. The customer is `brazos-cust-mp-legacy-7892` — opened a Mission Plaza checking account in 2024, received an Insider next-best-action email on December 8, 2025 (rewards-program enrollment offer), opened the email December 8, did not click. Post-close, received a Brazos rebrand email on Feb 4, opened it, clicked through to a landing page, enrolled in Brazos's rewards program on Feb 19.

```
chain trail for customer brazos-cust-mp-legacy-7892 (rewards-program path):
  entries (chronologically):

  [pre-close, Mission Plaza chain, AWS-resident, Phase A Insider event-anchoring]
  1.  2025-12-08  marketing.email_send                     (Insider, chain-bound, Phase A)
       - campaign_id:          insider-camp-2025-q4-rewards-acquisition-c
       - model_version:        insider/next-best-action-2025q4
       - template_id:          insider-tmpl-rewards-acquisition-2025q4-variant-c
       - variable_binding_hash: a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456
       - rendered_output_hash:  b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3
       - audit.cross_vendor_handover.source_vendor: insider
       - audit.cross_vendor_handover.source_signature_ref: insider-2025q4-sig-final

  2.  2025-12-08  marketing.email_open                     (Insider, chain-bound, Phase A)
  3.  2025-12-08  marketing.email_no_click                 (Insider, chain-bound, Phase A)

  [cut-over window, no entries]

  [post-close, Brazos chain, Azure-resident]
  4.  2026-02-04  marketing.email_send                     (SFMC, rebrand campaign, chain-bound)
  5.  2026-02-04  marketing.email_open                     (SFMC, rebrand campaign, chain-bound)
  6.  2026-02-04  marketing.email_click                    (SFMC, rebrand campaign, chain-bound)
  7.  2026-02-04  web.landing_page_view                    (Brazos web analytics, chain-bound)
  8.  2026-02-19  account.rewards_program_enrollment       (Salesforce FSC, chain-bound)
       - prior_offer_chain:
         - 2026-02-04 marketing.email_click (sfmc rebrand)
         - 2025-12-08 marketing.email_no_click (insider, mp-legacy)
       - prior_offer_run_id:    marketing.email_send.2025-12-08.mp-legacy-rewards-acq
       - prior_offer_seq:       1
       - prior_offer_status:    linked
       - prior_offer_substrate: aws-s3-aws-cloudhsm
```

**Elena:** "December 8, 2025 — the customer received an Insider rewards-program acquisition email, opened it, didn't click. The next-best-action model that picked the variant — `insider/next-best-action-2025q4` — retired at close. Six weeks later, on February 4, post-close, the customer received a Brazos rebrand email, opened it, clicked through, and enrolled in Brazos's rewards program on February 19. — The post-close rewards-program enrollment binds the prior-offer chain transitively back to the pre-close Insider email that didn't get a click."

**Mike:** "And the Insider model version that picked the variant — `insider/next-best-action-2025q4` — is in chain as a §10.21.4 vendor-version-registry lookup reference, not as a bound artifact."

**Cyrille:** "Right. The version-card lookup endpoint is Insider's, not ours. The chain entry binds the version string; the version card resolves at audit time via Insider's API. — Run the lookup."

```
$ herald-verify --tenant=brazos-federal-prod \
                --entry-id=marketing.email_send.2025-12-08.mp-legacy-rewards-acq \
                --strict --explain \
                --resolve-vendor-version-card
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified,
        cross-vendor handover anchor verified,
        vendor-version-registry lookup resolved
        against insider.com/api/v2/version-card

additional_verifications:
  - cross_vendor_handover_anchor_verified
  - marketing_model_version_walk_consistent

vendor_version_card:
  version_string:            insider/next-best-action-2025q4
  training_corpus_version:   insider-corpus-2025q3-public-financial-services-mix
  training_completed_at_utc: 2025-09-15T14:00:00.000Z
  evaluation_outputs_sha256: c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4
  retention_attestation:     insider-vvr-2026q1-retention-attestation-001
  retention_horizon_utc:     2031-09-15T14:00:00.000Z  (6-year per §10.21.4 commitment)

elapsed: 2.1s
```

**Elena:** "The version-card lookup resolves against Insider's API. The version-card carries the training-corpus version, the training-completion timestamp, the evaluation-outputs hash, and the retention attestation valid through 2031. — The Mission Plaza Story 20 §10.21.4 composition Steve walked at the November engagement carries cleanly forward through the merger; Insider's retention commitment was for the Mission Plaza chain; the Brazos chain inherits the commitment under the cross-substrate dispatch through the §10.40 cross-anchor."

**Mike:** "And the half-open reference. — A future legal question naming the December 8 email — the variant the model picked, the variable bindings, the rendered output the customer received — pulls in how long?"

Cyrille types.

```
$ herald-verify --tenant=brazos-federal-prod \
                --entry-id=marketing.email_send.2025-12-08.mp-legacy-rewards-acq \
                --strict --explain \
                --reconcile-rendered-output-byte-equal \
                --cross-substrate-walk
```

The reconciliation completes in nine seconds. The rendered HTML of the December 8 Insider email — pulled from the legacy Mission Plaza chain via the cross-anchor — recomputes byte-equal against the chain-bound rendered_output_hash. The variable bindings (customer's name, the rewards-program copy variant the personalization-layer picked, the destination URL the next-best-action ranker chose) resolve against the Insider template-artifact pull.

**Mike:** "Nine seconds. — The rendered HTML the customer saw on December 8 reproduces byte-equal in nine seconds, fourteen months later, across the cross-cloud boundary, with the model version's training corpus and evaluation outputs resolvable via Insider's API."

> ### Confirmation #3 — §10.21 marketing-stack handover walks legacy Insider events to post-close SFMC + Marketo Engage events through the cross-anchor; §10.21.4 vendor-version-registry lookup resolves legacy Insider model versions for six-year retention horizon
>
> The Insider-to-SFMC+Marketo and Yello-to-Salesforce-FSC handovers at close are bound under two §10.21 cross-vendor model-handover envelopes. Each envelope names the retiring vendor, the receiving vendor or vendor composition, the retired model classes, the successor model classes, the §10.21.4 vendor-version-registry lookup endpoint (still live for six years per the published vendor commitment), and the cross-substrate pair (`aws__azure`). The rewards-program enrollment walk for customer `brazos-cust-mp-legacy-7892` traces back through the cross-anchor to the December 8, 2025 Insider next-best-action email; the chain entry binds the campaign_id, the model_version, the template_id, the variable_binding_hash, and the rendered_output_hash. The verifier resolves the Insider model version's version-card via Insider's published API (`insider.com/api/v2/version-card`) in 2.1 seconds; the byte-equality reconciliation of the rendered HTML completes in nine seconds. The composition is operational; the cross-substrate dispatch is operational; the vendor-version-registry retention commitment is operational across the merger boundary.

The team breaks at 11:55. Sandwiches under cover come out. The Insider PM and the Yello PM are on the Teams bridge with video off as planned; both confirmed they're available across Day 1 afternoon for any follow-up. Calliope Wynn-Devereaux from Insider has been on the bridge silently since 11:00 — the same Calliope from Story 20, who committed the §10.21.4 contract at the November Mission Plaza engagement. She unmutes briefly.

**Calliope:** "Elena, the rendered-output byte-equality at nine seconds is the discipline we built the Phase A integration to support. — Insider's retention commitment is what was on the Mission Plaza engagement letter; the merger inherits the commitment under the §10.21.4 contract. We're good through 2031 on the legacy-version lookup endpoint. — I'll drop unless the afternoon walk needs me."

**Elena:** "Drop. — Thank you, Calliope. — We'll bring you back at the §10.69 walk this afternoon for one specific customer where the legacy Insider model picked a creative that's now part of a CFPB §1033 disclosure request the customer filed in July."

**Calliope:** "I'll be on the bridge."

She drops.

## 12:00 PM — Dawn arrives

Dawn walks into the Brazos engagement room at 12:02 in a charcoal suit, carrying a laptop bag and two paper cups of coffee from the cafe on the ground floor of the building. She greets the room by first name — Renata, Margarethe, Donovan, Hollis, Easton at the back of the room with his laptop closed, and then the team — Raj, Mike, Elena, Diana, Luis, Chen, Sonya, Tom.

The conversation for ninety seconds is personal. Tom takes one of the coffees from her hand and gives the chair next to him a small tap.

**Tom:** "Dawn."

**Dawn:** "Tom. — How's the team?"

**Tom:** "Team's good. Sonya's on her ninth engagement. Mike and Chen handled the cross-cloud anchor walk this morning at the five-minute-forty-eight-second mark; Elena finished the marketing-stack handover three minutes ago. Raj has been Lead for ten months and has the room as much as anybody has the room. — How's Steve?"

**Dawn:** "Steve is in Austin tomorrow on a working-group call with the OCC's IT supervision side — they want a half-day on the §10.21.4 vendor-version-registry retention discipline for the post-merger framework supplement they're drafting. He'll be in Houston Thursday morning for the §10.41 partition closure memo walk-through with Hollis. — He sends his regards. — And the house?"

**Tom:** "House is good. Did you finish the kitchen?"

**Dawn:** "Finished the kitchen. The cabinets came in cherry instead of walnut and we kept them anyway. — How's Helena's youngest?"

**Tom:** "Junior at Northwestern. Decided on chemical engineering instead of pre-law. Helena is — adjusting. — I'll tell her you asked."

**Dawn:** "Please."

The ninety seconds close. Dawn sits next to Elena. Elena moves a chair so Dawn can see her laptop screen. Dawn opens the MMPWorks laptop and pulls up the vendor-side view of the cross-cloud anchor architecture — a single annotated diagram with the Mission Plaza AWS substrate on the left, the Brazos Azure substrate on the right, the §10.40 cross-anchor bridging the two, the §10.39 dual-CFO signature pair at the bottom, the §10.42 backfill seal envelope at the upper-left under the Mission Plaza side, and the §10.41 three-partition map labeled along the bottom.

**Dawn:** "Margarethe, Renata, Donovan — thank you for having me. — Renata, your call from sixty days before close opened the conversation that produced today's architecture. The vendor-side view I'll walk through this afternoon is the one MMPWorks's engineering bench operates against; it composes with the audit-side view the team has been walking this morning under one continuous spec-section reference."

**Margarethe:** "Welcome, Dawn. — The vendor-side view, when you're ready. The team has had cross-cloud as routine on the audit side; I want the room to hear the vendor side say it the same way."

**Dawn:** "I will."

Renata stands.

**Renata:** "Dawn, before you start — I want to thank you on the institution's behalf. The conversation in March, sixty days before close — when I called MMPWorks because Brazos's GC was carrying anxiety about the cross-cloud byte-equality demonstration showing up in pre-trial discovery on a marketing-promise suit three years out — that conversation produced the architecture we walked this morning. The §10.40 substrate-agnostic clarifier was the load-bearing piece. The fact that Brazos and Mission Plaza could keep operating on the substrates we were already operating on and let the anchor cross the substrate boundary without requiring either institution to migrate clouds at close — that's the institutional decision that let the integration timeline hold. We would have had to migrate Mission Plaza off AWS to Azure at close otherwise, and the migration window would have collapsed the cut-over inside a one-month brand-transition campaign; we'd have shipped the rebrand campaign on a half-migrated substrate; the UDAAP exposure would have been catastrophically higher. — The §10.40 substrate-agnostic clarifier let us avoid that. Today's audit confirms the architecture held."

**Dawn:** "Thank you, Renata. — I'll add one thing to your framing before I start. The §10.40 substrate-agnostic clarifier wasn't always in the spec. The §10.40 section in its original form covered the single-substrate cross-vendor chain-merge anchor; that's what Hill Country Federal Credit Union exercised three years ago at the AWS-resident vendor swap that engagement walked. — The substrate-agnostic clarifier extension shipped in a Herald release nine months ago. The extension answered a question I filed in the engagement file at Hill Country three years ago — a quiet note that the engagement-file procedure kept on the record without making it a finding or a recommendation. The note read: *§10.40 anchor reads as routine on AWS-only. What happens when the substrate moves?* I didn't have a way to test it at Hill Country. When I joined MMPWorks ten months ago, the question was the first thing I put on Steve's desk. He had the substrate-agnostic extension already roughed out — the working-group sub-track had been carrying the question through three review cycles since Hill Country's reading on the spec — and we built it together. Today is the first production engagement that exercises it. — That's the architecture I'm walking through this afternoon."

The room is quiet for a beat. Margarethe nods. Donovan writes a single line in his notebook. Tom catches Sonya's eye across the table — the same nod he gave her at Mission Plaza in November when Dawn pulled the §10.21 vendor-opaque-render wishlist page out of her notebook and handed it to her.

**Dawn:** "Twenty minutes on the vendor-side architecture. Then sandwiches. — Margarethe, the floor."

## 12:15 PM — Vendor-side architecture walk (Dawn)

Dawn walks the room through the §10.40 substrate-agnostic clarifier from the vendor side. The walk is brief and concrete — she has done it three times in the last quarter for other Brazos-side stakeholders, and the architecture is by now well-rehearsed. The substrate-agnostic clarifier defines the cross-vendor chain-merge anchor not against a specific cloud-substrate pair but against an abstract substrate-pair-class. The §10.40 dispatch table lists known substrate pairs and substrate-pair-specific reconciliation walkers; the generic fallback walker reads bytes from wherever the institution names them and recomputes the SHA-256 in canonical bytes per RFC 8785. The substrate-trust boundary is one anchor inside the continuous chain; the chain doesn't care which substrate the legacy bytes live on.

She walks the §10.39 dual-signature pair under the substrate-agnostic `acquirer_hsm_key_fingerprint` field — any FIPS 140-2 Level 3+ HSM's public-key fingerprint is treated equivalently regardless of substrate. The §10.5 attestation registry holds the AWS CloudHSM attestation document and the Azure Key Vault Managed HSM attestation document side-by-side, both with FIPS 140-2 Level 3 evaluation references.

She walks the §10.42 backfill seal envelope at the substrate-agnostic level — the envelope produces a chain-shaped envelope retroactively over the acquired institution's pre-close baseline; the envelope's root is bound into the cross-anchor; the legacy chain entries reference the envelope by hash without rewriting the legacy bytes.

She walks the §10.41 three-partition coverage map at the substrate-agnostic level — pre-acquisition (the acquired institution's substrate), cut-over window (no-write band; §10.36 supplemental-seal mechanism armed but unexercised), post-cut-over (the acquirer's substrate). The November 2027 partition closure boundary will close the partition map into a single coverage region under §10.41's partition closure attestation; the same composition (§10.39 + §10.42) that closed the Feb 1 close will close the November cut-over with the partition closure attestation as the final-form revision.

She walks the §10.21.4 vendor-version-registry retention commitment at the substrate-agnostic level — the vendor's retention commitment is on the version-card lookup endpoint, not on any specific substrate; Insider's commitment to keep the legacy version-card lookup endpoint live for six years from version retirement is inherited under the cross-substrate dispatch through the cross-anchor.

**Dawn:** "Eight spec sections compose under the cross-cloud anchor. — §10.39 successor-attestation envelope, §10.40 cross-vendor chain-merge anchor with substrate-agnostic clarifier, §10.41 chain-coverage map M&A temporal-slice partitioning, §10.42 backfill seal at close, §10.36 late-arriving-entry seal discipline at the cut-over window, §10.21 cross-vendor model-handover for the AI-decisioning surface and the marketing-stack handover, §10.21.4 vendor-version-registry lookup for the legacy version-card lookup endpoints, §10.5 HSM custody at FIPS 140-2 Level 3+ across substrate-vendor-equivalent attestations. — That's the composition. The cross-cloud byte-equality demonstration at six minutes is the headline; the eight-section composition is the architecture."

**Margarethe:** "And the audit-side confirmation from this morning."

**Dawn:** "Confirms the architecture cleanly. — Chen ran the cross-anchor byte-equality reconciliation in five minutes forty-eight seconds; Mike walked the §10.11.1 prior-offer parent-linkage across the merger boundary and across the substrate boundary in 1.4 seconds for reference resolution and 28 seconds for byte-equality on the legacy offer's rendered HTML; Elena walked the §10.21 marketing-stack handover with the rendered-output byte-equality at 9 seconds for a fourteen-month-old Insider email. — That's the audit's morning. The afternoon is the rebrand-period UDAAP case and the §10.69 per-customer disclosure walk and the §10.70 SAR-filing case. The Day 3 morning is the §10.71 Fedwire walk with the Federal Reserve Bank of Dallas on the bridge. The Day 3 afternoon is the §10.41 partition closure memo for the November cut-over and Steve's twenty minutes on the platform-migration path for the 2027 Marketo upgrade."

**Renata:** "And the four-thirty question I want to ask you on Day 1 close-out."

**Dawn:** "Renata named the question in March. She asked it again at the engagement-letter signing in June. She'll ask it at four-thirty this afternoon for the third time, in the room, with the chain having been walked. — That's the engagement."

**Margarethe:** "Sandwiches. — Then the Marketo legacy-anchor at one o'clock."

The team breaks for the working lunch. Dawn pulls Elena aside briefly to walk through the afternoon's reconciliation queue; Tom is on a call with the firm's GC walking through the spousal-disclosure paragraph language for the Day 3 close-out memo; Margarethe and Donovan are talking to Hollis about the November cut-over runbook draft.

Sonya pours coffee at the carafe and stands next to Raj.

**Sonya:** "Cross-cloud reads as routine on the vendor side too."

**Raj:** "Cross-cloud reads as routine on the vendor side too. — That's the discipline. The architecture and the audit both speak the same shape. The room reads our calm familiarity and the vendor's calm familiarity together as a form of evidence."

**Sonya:** "And the Hill Country note Dawn cited."

**Raj:** "The Hill Country note. — Three years ago at the FCU in Austin, Dawn filed an engagement-file note. The note was an observation, not a finding. The institution at the time operated on a single substrate; the spec section in its 2024 form covered the single-substrate case; the combination read as routine. Dawn wrote the note because the byte-equality demonstration worked cleanly on one substrate and the question of what happens when the substrate moves was real but not actionable at that engagement. — The note sat in the engagement file. Two years and seven months later, when Dawn joined MMPWorks, she put the question on Steve's desk. The working-group sub-track had been carrying the question through three review cycles since Hill Country's read on the spec. The substrate-agnostic clarifier extension shipped nine months ago. Today is the first production engagement that exercises it."

**Sonya:** "Foresight to production in three years and three weeks."

**Raj:** "Foresight to production in three years and three weeks. — That's the lesson on engagement-file discipline. The note sits in the file. The note isn't actionable today. The note might become actionable in a future engagement. The note's value is the institutional record that the question was on the team's notice at a specific date; the lineage is preserved for whoever picks up the question when it becomes actionable. — Dawn picked up her own question. The question matured into the §10.40 substrate-agnostic clarifier. Today's audit confirms the answer."

**Sonya:** "And the engagement-file note I tore out of Dawn's notebook at Mission Plaza in November."

**Raj:** "The §10.21 vendor-opaque-render sub-case. — Your engagement-file note. The next time a marketing-AI vendor's render is opaque at the chain boundary, your note becomes actionable. Until then, your note sits in the file. — Your foresight horizon could be three weeks, or three years, or never. The discipline is the same either way."

Sonya nods. She pours her coffee.

## 1:00 PM — The §10.19 Marketo legacy-anchor deep-dive (Mission Plaza CMO Easton)

Easton Wadsworth sets a 2.7-TB external SSD on the conference-room table next to his laptop. He has been carrying the SSD in his briefcase since Mission Plaza's last legacy-export pull on January 31, 2026 at 23:42:18 UTC. The SSD holds the legacy Insider campaign-history export from the moment Mission Plaza retired the Insider footprint at close — campaign history, customer lists, A/B variant data, send-time logs, click-stream telemetry, the entire pre-close Insider audit-log surface. The hash was committed at close. Easton has been carrying anxiety about that hash for seven months.

**Easton:** "The Insider footprint at Mission Plaza ran for four years. Phase A under §10.21 brought the per-event chain entries into chain six months before close; before Phase A, the audit-side substitute was the quarterly Insider campaign-history export — the §10.19 evidentiary substitute Mission Plaza's CC8.1 named. At close, we pulled the final-form Insider export — 2.7 terabytes — and hash-anchored it under §10.19's external-artifact family. — The question I've been carrying for seven months is whether the hash committed at close was actually what the Marketo backup contained, or whether there was drift in the 47 minutes between Marketo's last write at 23:42:18 UTC and the close timestamp at 00:00:01 UTC Feb 1."

**Dawn:** "Walk it. — Chen, you have the receipts."

Chen has the chain entries for the legacy-export hash commit. He pulls them up.

```
chain entries for legacy Insider export hash-anchor at close:

  1. 2026-01-31 23:42:18 UTC  insider.last_audit_log_write
       - source_vendor:           insider
       - audit_log_seq:           insider-mp-prod-2026q1-final-write-887442
       - write_payload_sha256:    e1f5b9c3a7d1e5b9c3a7d1e5b9c3a7d1e5b9c3a7d1e5b9c3a7d1e5b9c3a7d1e5

  2. 2026-01-31 23:42:18 UTC  insider.tenant_writes_quiesced
       - source_vendor:           insider
       - quiesce_signal:          mission-plaza-bank-prod
       - quiesce_attestation_ref: insider-quiesce-2026q1-mp-final-sig-001

  3. 2026-01-31 23:43:00 UTC  insider.legacy_export_initiated
       - export_artifact_class:   tar.gz
       - export_artifact_label:   mission-plaza-bank-prod-insider-2022q1-2026q1-final

  4. 2026-01-31 23:58:47 UTC  insider.legacy_export_completed
       - export_artifact_sha256:  9c4d7f0a3b6e9c2f5b8d1a4c7f0e3b6a9c2d5f8e1b4a7d0c3f6b9e2a5d8c1f4b
       - export_artifact_size_bytes: 2697346912847
       - export_completion_attestation_ref: insider-export-2026q1-mp-final-sig-002

  5. 2026-01-31 23:59:30 UTC  insider.legacy_export.hash_committed_to_mission_plaza_chain
       - chain_entry_id:          ce_mp-prod-final-pre-close-insider-export
       - external_artifact_sha256: 9c4d7f0a3b6e9c2f5b8d1a4c7f0e3b6a9c2d5f8e1b4a7d0c3f6b9e2a5d8c1f4b
       - external_artifact_class: insider_legacy_export
       - audit.external_artifact.classification: §10.19_evidentiary_substitute_at_chain_boundary

  6. 2026-02-01 00:00:01 UTC  brazos.cross_cloud_anchor_placed
       - acquired_chain_terminal_merkle_root: 5f8a2c1e9b4d7f0c3a6e9b2d5f8a1c4e7b0d3f6a9c2e5b8d1a4f7c0e3b6d9f2a
       - (Mission Plaza terminal Merkle root binds entry #5's external_artifact_sha256
          plus all other Mission Plaza chain entries through close)
```

Chen reads the entries.

**Chen:** "Easton — Marketo's — sorry, Insider's — last write was at 23:42:18 UTC. The tenant quiesce signal fired at 23:42:18 UTC the same second. The legacy export initiated at 23:43:00 UTC; the export completed at 23:58:47 UTC; the hash committed to the Mission Plaza chain at 23:59:30 UTC. The chain entry's `external_artifact_sha256` field is bound under the per-event MAC at 23:59:30 UTC. Mission Plaza's terminal Merkle root at 23:59:30 UTC covers entry #5; the cross-cloud anchor at 00:00:01 UTC binds the terminal Merkle root into Brazos's Azure chain. — There's no drift window. The Insider tenant quiesce signal at 23:42:18 UTC matches the last write at 23:42:18 UTC. After the quiesce signal, Insider's instance accepted no further writes against the Mission Plaza tenant. The 47-minute interval you've been carrying anxiety about is the export-and-hash-and-seal window, not a write window. Nothing was written during the export window."

He pulls the Insider tenant-quiesce attestation signature and resolves it against Insider's published key registry. The signature verifies.

**Chen:** "The quiesce attestation is signed by Insider's vendor key. The signature confirms Insider's instance accepted no writes against the Mission Plaza tenant from 23:42:18 UTC through close. — The 47-minute window has no drift. The hash committed at close is byte-equal to what Marketo — Insider — wrote at 23:42:18 UTC and quiesced on. — Run the byte-equality on the SSD you brought."

Easton plugs the SSD into Cyrille's laptop. The recompute reads the 2.7-terabyte tar.gz, streams the bytes through SHA-256 in canonical-encoding-aware mode, and produces a hash. The hash recomputes byte-equal against the chain-bound `external_artifact_sha256` field.

```
$ herald-verify-external-artifact \
    --artifact-path=/mnt/easton-ssd/mission-plaza-bank-prod-insider-2022q1-2026q1-final.tar.gz \
    --chain-entry-id=ce_mp-prod-final-pre-close-insider-export \
    --strict --explain
Status: PASS
Step:   12
Reason: external artifact byte-equality verified
        against chain-bound external_artifact_sha256;
        chain entry MAC verified;
        artifact byte-equality reconciled against
        chain-bound seal record at 2026-01-31T23:59:30Z

additional_verifications:
  - external_artifact_byte_equal
  - tenant_quiesce_attestation_signature_verified
  - no_drift_window_confirmed

elapsed: 6m12s
```

Six minutes twelve seconds. The terminal prints PASS.

Easton looks at the screen for a long moment.

**Easton:** "Six minutes twelve seconds. — Seven months of anxiety. — The hash committed at close is what Marketo's backup contained. There was no drift in the 47-minute interval. — Insider's quiesce attestation is signed. The chain has it. The byte-equality reproduces."

He exhales. The exhale is the first one he has taken on the legacy-export-hash question in seven months.

**Easton:** "Thank you. — Reyna at Mission Plaza walked me through Phase A in November; we landed the Phase A integration in February. The pre-close Insider footprint that retired at close was the part Phase A couldn't cover — it was four years of pre-Phase-A Insider events, all in the legacy export, hash-anchored under §10.19 because that's the chain-coverage-boundary discipline. I have been carrying the question of whether the hash was the right hash for seven months. — Today the byte-equality reproduces in six minutes. — I'm going to go for a walk after this meeting."

The room is quiet.

**Donovan** (from the Mission Plaza side): "Easton — Reyna built Phase A specifically so that the pre-Phase-A Insider footprint would have a clean §10.19 evidentiary-substitute anchor at retirement. The hash at close was Reyna's last institutional decision before she handed the CAE seat to me at the integration. — She knew the question you were going to carry. She built the architecture so the question would resolve cleanly at the post-close audit. Today's the audit. The question resolves."

**Easton:** "Reyna knew."

**Donovan:** "Reyna knew."

> ### Confirmation #4 — The pre-close Insider legacy-export hash committed at close is byte-equal to what the Insider tenant wrote and quiesced on; the seven-month drift-window question resolves in six minutes twelve seconds
>
> The legacy Insider campaign-history export — 2.7 terabytes covering four years of pre-Phase-A Mission Plaza marketing events — was hash-anchored at close under §10.19 as the §10.19 evidentiary-substitute at the chain boundary. The chain-entry timeline binds Insider's last audit-log write at 23:42:18 UTC Jan 31, the tenant-quiesce attestation signature at the same second, the legacy-export initiation at 23:43:00 UTC, the export completion at 23:58:47 UTC, and the hash commit to the Mission Plaza chain at 23:59:30 UTC. The Mission Plaza terminal Merkle root at 23:59:30 UTC covers the hash commit; the cross-cloud anchor at 00:00:01 UTC binds the terminal Merkle root into Brazos's Azure chain. The Insider tenant-quiesce attestation signature is signed by Insider's vendor key and verifies against the published key registry; no writes were accepted against the Mission Plaza tenant from quiesce through close. The byte-equality reconciliation of the 2.7-TB tar.gz from Easton Wadsworth's SSD against the chain-bound `external_artifact_sha256` completes in six minutes twelve seconds. The seven-month drift-window question resolves: no drift. The hash committed at close is byte-equal to what Marketo wrote and quiesced on.

## 2:30 PM — The rebrand-period campaign window and the cross-vendor brand-transition discipline

Renata Whitley-Aguilar takes the bench. The rebrand campaign window — Feb 4 through August 31, 2026 — is the operational window the §10.41 cut-over-window partition covers from the marketing-program side. The campaign window is also the UDAAP exposure window; the chain has been carrying the campaign data continuously through the window; the chain-bound discipline is what lets the bank produce the exact content and the exact recipients of any single campaign send across the seven-month window.

The team walks through the rebrand campaign architecture. The campaign was orchestrated under Salesforce Marketing Cloud's journey-builder; the audience segmentation was built from Brazos's customer-master with the Mission Plaza legacy customers added at close under the §10.21 Yello-to-Salesforce-FSC handover. The send-time optimization model was Salesforce Einstein for Marketing Cloud, the post-close successor to Insider's STO model family. Each send fired with a per-event chain entry binding the rendered output, the model version, the audience-segment binding, the customer-correlation index.

Total volume across the rebrand campaign window from Feb 4 through August 31, 2026: 7,924,103 emails, 2,847,229 SMS messages, 14,772,891 in-app notifications across the Brazos digital-banking surface, 481,007 push notifications. Approximately 26 million chain entries on the marketing surface alone across the seven-month rebrand window.

**Renata:** "The campaign window is the operational window. The chain-bound discipline is what gives Brazos the production capability to answer any campaign-content question at any granularity at any point in the seven-month window."

**Sonya:** "And the load-bearing case is February 4."

**Renata:** "February 4 is the load-bearing case. — Mike, you have the receipts."

## 3:00 PM — The §10.21 UDAAP scene: 47,000 emails on February 4, 2026

Mike has the February 4 receipts staged on his laptop. The case is the rebrand-period UDAAP misstep — on Feb 4, the rebrand campaign fired to approximately 340,000 Mission Plaza legacy customers. One variant of the email — variant B in the A/B test, sent to roughly 14% of the audience — accidentally referenced Mission Plaza's old fee schedule (the phrase "free overdraft protection" appeared in the copy) which Brazos does not offer at zero cost. Brazos's marketing operations team detected the issue at 14 minutes after the campaign fired; the campaign-stop button was hit at minute 14; 47,000 emails had already sent before the stop landed.

The CFPB settlement closed in March 2026 with a customer-restitution package: $35 per affected customer in waived overdraft-protection enrollment fees plus a written notice in plain English explaining the mismatch between the variant B copy and Brazos's actual fee schedule. The settlement closed in 23 days; the restitution was paid in 16 business days; the CFPB closed the matter without further action.

**Mike:** "Renata, the audit question — can the bank produce the exact list of 47,000 customers who received the misleading variant B, the exact text they received, the exact timestamp, the restitution receipt linkage, and the customer-by-customer disposition?"

**Renata:** "Pull it."

Mike types.

```
$ herald-verify --tenant=brazos-federal-prod \
                --campaign=brazos-rebrand-2026q1-day-of-close-plus-3 \
                --variant=B \
                --send-window-start=2026-02-04T15:00:00Z \
                --send-window-end=2026-02-04T15:14:00Z \
                --emit-affected-customer-list \
                --resolve-restitution-receipts \
                --strict --explain
Status: PASS
Step:   12
Reason: campaign-variant subset reconstruction
        verified against chain;
        sent-email population resolved;
        rendered-output byte-equality reconciled
        for representative entries;
        restitution-receipt linkage walked
        per customer across full subset

additional_verifications:
  - campaign_variant_subset_reconstruction_verified
  - sent_email_population_resolved
  - rendered_output_byte_equality_reconciled (sampled at 50 entries)
  - restitution_receipt_linkage_walked_per_customer

campaign_subset:
  campaign_id:              brazos-rebrand-2026q1-day-of-close-plus-3
  variant:                  B
  rendered_output_hash:     8f3c1a4b7e0d3c6f9b2e5a8d1c4f7b0e3a6d9c2f5b8e1a4d7c0f3b6e9a2d5c8f
  rendered_output_text:     [included in subset; bound by hash]
  sent_count:               47,247
  campaign_stop_at_utc:     2026-02-04T15:14:23.000Z
  stop_attestation_ref:     brazos-mkt-ops-2026q1-stop-button-sig-001
  affected_customer_count:  47,247
  restitution_population:   47,247
  restitution_paid_count:   47,247
  restitution_total_usd:    1,653,645.00
  cfpb_settlement_ref:      cfpb-2026-march-brazos-rebrand-variant-b-settlement
  cfpb_settlement_closed_at_utc: 2026-03-09T19:00:00Z
  customer_subset_csv:      [emitted to ./brazos-rebrand-2026q1-variant-b-affected.csv]
  customer_subset_csv_sha256: 4d7c0f3b6e9a2d5c8f1b4e7a0d3c6f9b2e5a8d1c4f7b0e3a6d9c2f5b8e1a4d7c

elapsed: 5m54s
```

The terminal prints PASS. The customer subset CSV writes to disk.

Mike opens the CSV. Forty-seven thousand two hundred forty-seven rows. Each row carries the customer ID, the customer's name as it appeared in the rendered email, the send timestamp, the rendered output hash bound to the customer-specific variable bindings, the restitution-receipt chain entry ID, the restitution amount paid, the restitution-paid timestamp, the CFPB settlement reference, the customer's chosen acknowledgment-receipt channel (email or US mail).

He picks one row at random — row 12,847 of the 47,247 — and runs the rendered-output byte-equality reconciliation against the customer's specific rendered email.

```
$ herald-verify --tenant=brazos-federal-prod \
                --customer-id=brazos-cust-mp-legacy-31882 \
                --campaign=brazos-rebrand-2026q1-day-of-close-plus-3 \
                --variant=B \
                --reconcile-customer-rendered-output-byte-equal \
                --strict --explain
Status: PASS
Reason: customer-specific rendered output byte-equal
        against chain-bound rendered_output_hash;
        restitution receipt entry walked;
        customer acknowledgment receipt resolved

customer_specific_subset:
  customer_id:                brazos-cust-mp-legacy-31882
  customer_name_rendered:     "Idalia Cantrell-Brown"
  email_subject_rendered:     "Same great service, new name — Brazos Federal"
  email_body_rendered_sha256: 8f3c1a4b7e0d3c6f9b2e5a8d1c4f7b0e3a6d9c2f5b8e1a4d7c0f3b6e9a2d5c8f
  email_sent_at_utc:          2026-02-04T15:11:47.000Z
  email_opened_at_utc:        2026-02-04T17:42:09.000Z
  restitution_paid:           true
  restitution_amount_usd:     35.00
  restitution_paid_at_utc:    2026-03-18T14:00:00.000Z
  restitution_receipt_ack_at_utc: 2026-03-21T09:14:00.000Z
  acknowledgment_channel:     us-mail

elapsed: 1.8s
```

**Mike:** "One point eight seconds for one customer. Six minutes for the full 47,247-customer subset reconstruction with rendered-output byte-equality sampled at 50 entries and restitution-receipt linkage walked per customer. — The bank can produce the exact misleading text, the exact list of 47,247 customers, the exact send timestamps within a fourteen-minute window, the customer-by-customer restitution receipts, the CFPB settlement reference, and the customer's acknowledgment receipts. — Renata, the regulator question — can the customer subset and the rendered output reproduce in court three years from now?"

**Renata:** "Adelaide carries that question on the GC side. — Adelaide?"

Adelaide Carrowmore-Finch has been at the back of the room since 2:30. She has been writing in a leather notebook. She closes the notebook.

**Adelaide:** "The customer subset and the rendered output reproduce under §1.1 Daubert four-factor grounding: testability via §7 verifier procedure, peer review under the spec working-group process, known error rate via §1.3 security definitions, general acceptance of HMAC-SHA-256, RFC 6962 Merkle, and Ed25519 across the cryptographic-engineering community. The §1.4 compositional security argument names the three custody layers — IKM, ledger storage, HSM — plus the §1.2 SDK-process residual. A false negative requires simultaneous compromise of all three custody layers plus the SDK-process residual. The bank's litigation posture on the cross-cloud Variant B subset is that the chain reproduces under Daubert; the legacy Mission Plaza side reproduces under the §10.40 substrate-agnostic clarifier; the cross-cloud byte-equality demonstration this morning is the canonical Daubert-reproduction case for the cross-cloud architecture going forward."

She opens the notebook again. She writes a single line. She closes it.

**Adelaide:** "Mike, can you produce the customer subset CSV with a single CLI flag against the chain on demand?"

**Mike:** "Single flag. — `--emit-affected-customer-list`. The verifier produces the CSV with the SHA-256 of the CSV bound to the chain at the moment of production. Any subsequent regulator or counsel request reproduces the CSV byte-equal against the bound hash."

**Adelaide:** "And the production-discipline registry."

**Cyrille:** "Every CSV production fires a chain entry under `audit.disclosure.production.csv_emitted` binding the verifier command line, the affected-population count, the CSV SHA-256, the requesting party, and the production timestamp. The production-discipline registry is the chain's own audit-log of its own disclosure productions. Adelaide has read access to the registry through the GC IAM role."

**Adelaide:** "Good. — The bank's litigation posture on the February 4 Variant B subset is that the chain produces the customer subset on a single CLI flag at six minutes; the production-discipline registry binds the production; the rendered-output byte-equality reproduces under Daubert; the restitution-receipt linkage walks per customer in 1.8 seconds. — Margarethe, I'm comfortable. — Yusuf, you're on the bridge?"

Yusuf Adekunle-Mensah unmutes from the Teams bridge.

**Yusuf:** "On the bridge. — The CFPB settlement closed in March. The settlement file references the rendered-output byte-equality demonstration capability as an enforcement-cooperation factor; the regulator was satisfied with the production capability the bank demonstrated in the March settlement meeting. — The settlement does not reopen. The §10.69 disclosure walk this afternoon will cover any individual customer's right under §1033 to their own subset; the disclosure walks honestly against the chain's coverage. The production capability is what the regulator wanted on the record."

**Margarethe:** "This is why we did the deployment. — The cross-cloud byte-equality demonstration this morning is the architecture; the 47,000-email subset reconstruction this afternoon is the operational test. — Renata, your call."

**Renata:** "Confirmed. The bank's posture on the rebrand-period UDAAP window is that the chain is the discipline; the discipline produces the subsets on demand; the regulator and the GC and the customer all have the same access to the chain's productions. — Mike, walk one more. Pick a customer who declined the restitution."

Mike pulls. The chain returns 23 customers across the 47,247-person affected population who chose to decline the restitution offer (chose to keep their old Mission Plaza-grandfathered fee schedule, which Brazos preserved for the customer's life-of-account as a lighter-touch alternative to the $35 fee waiver). Each customer has a chain entry binding the decline-restitution preference, the customer-acknowledgment channel, and the legacy-fee-schedule preservation reference.

**Mike:** "Twenty-three customers across the 47,247-person affected population chose to keep the Mission Plaza-grandfathered fee schedule. The chain has the preference, the acknowledgment, the legacy-fee-schedule reference, and the customer-by-customer disposition. — Renata, that's the case."

**Renata:** "That's the case."

> ### Confirmation #5 — The February 4 rebrand-period Variant B UDAAP scene reproduces in six minutes; rendered-output byte-equality and customer-by-customer restitution-receipt linkage walked per chain
>
> The Brazos rebrand campaign on February 4, 2026 fired to ~340,000 Mission Plaza legacy customers; Variant B (~14% of the audience) accidentally referenced Mission Plaza's grandfathered "free overdraft protection" language which Brazos does not offer at zero cost. Campaign-stop fired at minute 14; 47,247 emails had sent. The CFPB settlement closed in March 2026 with a $35-per-customer restitution package; total restitution paid: $1,653,645. The chain reconstructs the 47,247-customer affected population in five minutes fifty-four seconds via a single CLI flag (`--emit-affected-customer-list`); the customer subset CSV is bound under the §10.13-derived production-discipline registry. Rendered-output byte-equality reconciles for any individual customer in 1.8 seconds. The customer-by-customer restitution-receipt linkage walks per chain. Twenty-three customers across the affected population chose to decline restitution and keep their legacy-fee-schedule preservation; the chain binds each preference, acknowledgment, and disposition. Adelaide Carrowmore-Finch (GC) certifies the production discipline meets §1.1 Daubert four-factor grounding for any next-three-years litigation reproduction. The CFPB UDAAP attorney (Yusuf Adekunle-Mensah) confirms the settlement file references the rendered-output byte-equality demonstration capability as an enforcement-cooperation factor.

## 4:30 PM — The Brazos CAE's question and Dawn's answer

The room reassembles in the engagement room at 4:25. Margarethe has the floor for the Day 1 close-out. Dawn is at the table with Renata to her left and Tom to her right. Donovan and Easton are across the table. Hollis and Adelaide are at the back of the room. Raj is at the head of the table next to Tom.

**Margarethe:** "Day 1 summary. — The cross-cloud anchor walked clean in five minutes forty-eight seconds; the §10.11.1 prior-offer parent-linkage walked across the merger boundary and the substrate boundary in 1.4 seconds; the §10.21 marketing-stack handover walked the Insider and Yello retirements with vendor-version-registry lookup commitments live through 2031; the Insider legacy-export hash committed at close reproduced byte-equal in six minutes twelve seconds and Easton's seven-month drift-window question resolved; the February 4 Variant B UDAAP subset reconstructed in five minutes fifty-four seconds with customer-by-customer restitution-receipt linkage walked per chain. — Five confirmations on Day 1. One Nit, logged by Tom this morning: the cross-charter retention policy framework-fit memo against the OCC post-merger framework is not yet produced; Adelaide will draft before the 60-day OCC examination opens. — Raj, the audit-side close on Day 1?"

**Raj:** "Day 1 confirms. — Tom?"

**Tom:** "One Nit logged on the cross-charter retention policy. Zero Gaps. Zero Partials. — The recusal-protocol close-out under the spousal-disclosure paragraph operates cleanly across the engagement; Dawn's vendor-side appearance is on the schedule; the GC-side language is logged. — Day 2 kickoff at 8:00 in this room; §10.69 per-customer disclosure and §10.70 SAR-filing case this afternoon."

**Margarethe:** "Renata, you have one question for Dawn before close-out."

Renata stands.

**Renata:** "Dawn — I've been carrying this question since March. — If a Mission Plaza legacy customer sues Brazos three years from now over a pre-merger marketing promise we didn't honor, can we prove what they were actually told?"

The room is quiet.

Dawn closes her laptop halfway. She looks at Renata, not at Margarethe and not at the team.

**Dawn:** "Yes. — The Marketo legacy data is hash-anchored at close under §10.19 as the §10.19 evidentiary substitute at the chain boundary. Easton walked the byte-equality demonstration in six minutes at one o'clock; the seven-month drift-window question resolved. The post-close marketing events are in Brazos's TesseraSeal proper — Phase A Mission Plaza marketing events from the six months before close are in the legacy chain, the post-close Brazos marketing events are in the post-close chain, both bound under the cross-anchor at close. The AI underwriting decision binds both — the §10.11.1 prior-offer parent-linkage walks transitively across the merger boundary and across the substrate boundary in 1.4 seconds for the reference resolution and 28 seconds for byte-equality on the legacy offer's rendered HTML. The chain spans every relevant event from August 2025 forward — Mission Plaza's TesseraSeal go-live date — and the customer's pre-go-live Insider footprint is hash-anchored under the §10.19 evidentiary substitute for the four years before. Three-year window from today is well inside retention; both charters' retention floors are seven years. — The cross-vendor anchor is the load-bearing piece. The byte-equality demonstration this morning reproduces in court under §1.1 Daubert four-factor grounding; Adelaide certified the production discipline this afternoon."

She pauses.

**Dawn:** "I want to add one thing. — I had this question once, when I was sitting on your side of the table. The engagement was Hill Country Federal Credit Union, three years ago — a marketing-AI vendor swap, AWS-resident, NCUA AIRES exam coming. The byte-equality demonstration worked cleanly there, but the institution operated on a single substrate and the spec section worked on a single substrate. The combination read as routine. — I wrote a note in the engagement file at the close of Day 3. The note was an observation, not a finding. The note read: *§10.40 anchor reads as routine on AWS-only. What happens when the substrate moves?* I didn't have a way to test it at Hill Country. The institution had nothing to remediate; the spec section worked in the form the spec section shipped. The note sat in the engagement file."

She pauses again.

**Dawn:** "Three years and three weeks. — When I joined MMPWorks ten months ago, the Hill Country note was the first thing I put on Steve's desk. The working-group sub-track had been carrying the question through three review cycles since Hill Country's reading on the spec. Steve had the substrate-agnostic clarifier extension roughed out. We built it together. The §10.40 substrate-agnostic clarifier shipped in a Herald release nine months ago. — Today is the first production engagement that exercises it. The cross-cloud byte-equality demonstration this morning at five minutes forty-eight seconds is the answer to the engagement-file note from Hill Country. The chain doesn't care which cloud the artifacts live on. The substrate-trust boundary is just another anchor."

Renata writes a single line in her notebook. Adelaide closes hers. Margarethe nods once. Donovan looks at Easton; Easton looks at Donovan.

Tom gives Dawn a microscopic nod. Raj's expression doesn't change. The room reads the moment as the work compounding — Sonya at the back of the table, with her engagement-file note from Mission Plaza in November still in her own jacket pocket, recognizes the shape of foresight maturing into production over an audit horizon she had not yet experienced.

**Renata:** "Thank you, Dawn. — And the substrate-trust boundary as an anchor."

**Dawn:** "The substrate-trust boundary as an anchor. — That's the production-validated phrasing the standards memo will carry after this engagement. The §10.40 substrate-agnostic clarifier is now operationally exercised live. The canonical-reference shape for the cross-cloud chain-merge anchor is the Brazos × Mission Plaza engagement. — The standards body will pick up the engagement reference at the next quarterly review."

**Margarethe:** "Day 1 closes. — Dinner tonight is at the team's hotel; Brazos sends regards but does not crash the firm's dinner. Tomorrow at 8:00 in this room."

The room scatters at 5:25.

## 6:30 PM — Hotel restaurant, Day 1

The team takes a corner table at the Hyatt restaurant on Smith Street. The Houston downtown skyline through the floor-to-ceiling windows is gold-into-blue in the evening light. The team is tired and pleased and quiet.

Tom orders for the table — a Texas porterhouse for sharing, the brisket starter, the chimichurri, two bottles of a Texas tempranillo that the sommelier has been talking about for weeks. The food arrives. Mike pours.

**Mike:** "Day 1 confirms. — Five confirmations, one Nit on the cross-charter retention policy, zero Gaps, zero Partials. — Raj?"

**Raj:** "Day 1 confirms. The cross-cloud byte-equality at five forty-eight; the Insider legacy-export at six twelve; the Variant B subset at five fifty-four. The headline numbers are in the engagement notebook. The shape carries forward to Day 2."

**Sonya:** "And the four-thirty moment."

**Raj:** "The four-thirty moment. — Dawn's two-year-and-eleven-month-old engagement-file note from Hill Country answered itself in the room at five minutes forty-eight seconds this morning. The team read it as the work compounding. — Sonya, your vendor-opaque-render note from Mission Plaza in November is still in your jacket pocket. Three years and three weeks is the horizon for one foresight cycle. Your cycle might be three weeks or three years. The discipline is the same."

**Sonya:** "Three years and three weeks."

**Raj:** "Three years and three weeks. — And the next time we sit across the table from a marketing-AI vendor with an opaque render at the chain boundary, your note is what's actionable."

Elena raises her glass.

**Elena:** "To the engagement-file discipline."

The team raises their glasses.

**Tom:** "To the engagement-file discipline. — And to Dawn at lunch."

**Mike:** "Dawn at lunch was the right ninety seconds."

**Diana:** "Dawn at lunch was the right ninety seconds."

**Raj:** "Dawn at lunch was the right ninety seconds."

The team drinks.

The dinner runs to 9:30. Tom orders a Macallan 15 and sips it slowly while the team's conversation moves from the engagement to the flight schedule to the weather forecast for Houston Wednesday (clear, low 70s in the morning, climbing into the upper 80s by afternoon, light breeze off the Gulf) to the rental-car return logistics. Sonya excuses herself first at 9:15. Mike at 9:25. Tom is the last to leave at 10:00. He pays the bill.

In the elevator, he checks his phone. There is a text from Dawn: *Day 1 from your end?*

He types back: *Day 1 confirms. The Hill Country callback at 4:30 landed. The team read it the way you'd hope. — Day 2 at 8:00.*

A pause. The phone buzzes back.

*8:00. — D.*

Tom puts the phone away.

## Day 2 — 8:00 AM — Day 2 kickoff

Margarethe brings breakfast tacos from a place on Westheimer; Hollis brings the salsa. Sonya laughs as Mike's eyes water; the chorizo-and-egg is hotter than the Mission Plaza version was in November and Mike has not yet learned to ask for the flour tortilla instead of the corn. Adelaide arrives at 8:15 with a printed agenda; Yusuf is on the bridge by 8:30. Hollis Trent-Mosley brings a one-page §10.41 partition closure runbook draft for the November cut-over — the draft is the artifact Day 3 afternoon will finalize.

**Margarethe:** "Day 2 agenda. — Morning: §10.69 per-customer disclosure walk across the merger boundary; §10.70 SAR-filing case across the merger boundary walked under cleared and non-cleared verifier modes; the AI-decisioning composition walk for the credit-decisioning surface across the merger boundary on three more cases for completeness. — Afternoon: the §10.13 SR 11-7 model-risk binder composition walk across the merger boundary; the §10.17 partition-ceremony attestation walk for the cross-cloud-anchor placement at close; the §10.22 redaction-discipline walk for the rebrand-period campaign window. — Day 3 morning: §10.71 Fedwire walk with the Federal Reserve Bank of Dallas Wholesale Payments Office on the bridge. Day 3 afternoon: the §10.41 partition closure memo, Steve's twenty minutes on the 2028 Marketo platform-migration question, close-out."

**Raj:** "Acknowledged. — Diana, the §10.69 walk first."

## 8:45 AM — The §10.69 per-customer disclosure walk across the merger boundary

Diana takes the bench. The §10.69 surface is the per-customer audit-trail subset disclosure — the CFPB §1033 right that lets a consumer request the institution's complete record of their data and interactions across the merger boundary. Brazos has been operating §1033 disclosure as a standard compliance workflow for years; the §10.69 chain-bound discipline ships the disclosure as a structured artifact bounded by what the chain covers across both pre-close and post-close partitions and across the substrate boundary via the cross-anchor.

The load-bearing case is a customer who filed a §1033 disclosure request on July 14, 2026 — five months after close, three months after the CFPB rebrand-period settlement, two months before today's audit. The customer is a Mission Plaza legacy customer with two years of pre-close history and five months of post-close history; she received the Variant B email in February, accepted the restitution, applied for a HELOC in May post-close, received the approval, and filed the §1033 request after seeing a Texas Department of Banking consumer-alert news segment that mentioned the rebrand-period settlement.

Customer ID: `brazos-cust-mp-legacy-19447`. Customer name: **Vionetta Halloran-Pace**, retired teacher, age 67, San Antonio resident.

Diana pulls the chain trail. Twenty post-close entries; eight Phase-A pre-close entries on the Mission Plaza chain; approximately one hundred and twenty-seven pre-Phase-A marketing events covered by the §10.19 evidentiary substitute (Insider quarterly export, four-year retention floor). The disclosure document Brazos produced for Vionetta on July 25 is a 73-page structured PDF with a header section, a chain-coverage section explaining the merger boundary and the substrate boundary in plain English, the per-event chain trail, the §10.19 evidentiary-substitute trail for the pre-Phase A Insider footprint, and an appendix with the verifier output and the reconstruction-method hash.

The chain-coverage section reads:

> Vionetta — This disclosure spans your interactions with Mission Plaza Bank (San Antonio, Texas), which Brazos Federal Bancshares acquired on February 1, 2026. Your record is presented as one continuous trail across the merger boundary, even though Mission Plaza and Brazos used different cloud providers (Amazon Web Services for Mission Plaza, Microsoft Azure for Brazos) and different marketing-automation systems (Insider for Mission Plaza, Salesforce Marketing Cloud + Marketo Engage for Brazos). The chain-of-custody discipline both institutions operated under — called TesseraSeal — lets us produce one continuous record without losing track of the merger boundary or the technology boundary.
>
> Your record has three sections. (1) Events captured in Brazos Federal's chain — these include your post-merger Brazos checking-account activity, the February 4 rebrand-period email, the CFPB-settlement notice and restitution receipt, your May HELOC application and approval, and your July §1033 disclosure request. (2) Events captured in Mission Plaza's chain (pre-merger, August 2025 forward, when Mission Plaza was on TesseraSeal for the AI-decisioning surface and the marketing surface). (3) Events captured in Mission Plaza's pre-TesseraSeal evidentiary substitute (the Insider quarterly campaign-history export) for the four years before Mission Plaza went on TesseraSeal. The chain-side portions (sections 1 and 2) are independently verifiable using both institutions' published cryptographic fingerprints; the substitute portion (section 3) is named with the artifact type and your right to request the source artifacts under §1033 if you want them.

Mike pulls the verifier output appended to the disclosure.

```
$ herald-verify --tenant=brazos-federal-prod \
                --customer-correlation=brazos-cust-mp-legacy-19447 \
                --strict --explain \
                --customer-subset \
                --cross-substrate-walk \
                --span-merger-boundary
Status: PASS
Step:   12
Reason: chain integrity verified across both partitions;
        cross-substrate dispatch resolved;
        merger boundary traversed transitively via cross-anchor;
        pre-Phase-A evidentiary substitute trail resolved;
        customer subset disclosure produced

additional_verifications:
  - customer_subset_disclosure_verified
  - cross_substrate_dispatch_walked
  - merger_boundary_transitive_walk_verified
  - pre_phase_a_evidentiary_substitute_trail_resolved
  - rendered_output_byte_equality_reconciled_for_variant_b
  - cfpb_settlement_restitution_linkage_walked

customer_subset:
  total_chain_entries:               20
  pre_close_entries:                  8  (mission-plaza-bank-prod, AWS-resident)
  post_close_entries:                12  (brazos-federal-prod, Azure-resident)
  pre_phase_a_substitute_entries:    ~127 (insider quarterly export, named substitute)
  cross_anchor_traversals:            1  (the close cross-anchor)
  cross_substrate_dispatches:         1  (aws-s3-aws-cloudhsm → azure-blob-azure-akv-mhsm)

elapsed: 22 seconds
```

Twenty-two seconds.

**Diana:** "Twenty-two seconds for the full per-customer subset reconstruction across both partitions, both substrates, both vendor stacks, and with the pre-Phase-A evidentiary substitute trail resolved. — The §10.69 cross-tenant clarifier paragraph normates exactly this composition: the verifier traverses cross-tenant subtrees bound via §10.40 cross-anchors, producing one unified per-customer audit trail across the inheritance boundary. The disclosure is honest about the merger boundary; the chain-side and substitute-side trails compose under one continuous record."

**Renata:** "Vionetta's question to the customer-service agent who filed her §1033 request was whether the bank could produce all of her records from her time at Mission Plaza, including the marketing emails she's pretty sure she got in 2023 and 2024 about HELOCs that she didn't act on at the time. The agent confirmed the bank could produce them via §10.19 evidentiary substitute from the Insider quarterly export; the four-year pre-Phase-A retention floor was named in the disclosure plain-English summary; Vionetta acknowledged in writing that she understood the substitute-side trail was the named substitute and she could request the source artifacts if she wanted them. She didn't request the source artifacts. The chain-side portion of the disclosure was enough for her question."

**Donovan:** "The §10.19 evidentiary substitute Reyna stood up at Mission Plaza in August 2025 — the named substitute for the four-year pre-Phase-A Insider footprint — is the institutional substitute that resolves the four-year retention question for any Mission Plaza legacy customer's §1033 disclosure. The substitute is named, the retention floor is named, the customer's right to request the source artifacts is named. The substitute composition is operationally proven on Vionetta's case."

Diana walks two more disclosure cases — a small-business customer who opened a Mission Plaza account in 2019 and applied for a Brazos SBA-line in July post-close, and a Brazos-native customer whose entire history is post-close (no Mission Plaza-legacy footprint) but who received the Variant B email and the restitution package as one of the 47,247. Each disclosure walks cleanly; each composes honestly with the customer's specific scope.

> ### Confirmation #6 — §10.69 per-customer disclosure walks across the merger boundary, the substrate boundary, and the Phase-A coverage transition in 22 seconds
>
> Vionetta Halloran-Pace's §1033 disclosure (July 25, 2026) reconstructs 20 chain entries across two partitions, two substrates, and two vendor stacks plus the named pre-Phase-A evidentiary substitute trail (~127 marketing events from August 2022 through July 2025 under the Insider quarterly campaign-history export per §10.19) in 22 seconds. The §10.69 cross-tenant clarifier paragraph is operationally exercised: the verifier traverses cross-tenant subtrees bound via §10.40 cross-anchors, producing one unified per-customer audit trail across the inheritance boundary. The pre-Phase-A evidentiary substitute composes with the chain-side portions; the disclosure is honest about the merger boundary and the substrate boundary; the customer's right to request source artifacts under §1033 is preserved.

## 10:00 AM — The §10.70 SAR-filing case across the merger boundary

Brazos's BSA officer is **Padraic Calhoun-Reidy**, mid-50s, ex-FinCEN, twelve years at Brazos. He joins the engagement room at 10:00 with his cleared-mode credentials staged. The case is a SAR-filing chain that spans the merger boundary — opened by Mission Plaza's BSA officer (Padraic's predecessor on the Mission Plaza side, whose seat retired at close) on December 12, 2025 against a customer who had been on the Mission Plaza books for eleven years and whose post-close activity in March-April 2026 reinforced the original concern; the SAR ultimately filed with FinCEN on April 18, 2026 under Brazos's institutional identity per the FinCEN merger-inheritance discipline.

**Padraic:** "The SAR filing under §10.70 spans the merger boundary. — Walk the chain under non-cleared mode first; then I'll authenticate and we walk cleared mode."

Diana types.

```
$ herald-verify --tenant=brazos-federal-prod \
                --sar-investigation-id=sar-mp-to-brazos-2025q4-002 \
                --strict --explain \
                --span-merger-boundary \
                --mode=non-cleared
Status: PASS
Step:   12
Reason: SAR investigation chain integrity verified
        in non-cleared mode; investigation content
        redacted; existence claim resolved;
        merger boundary transitive walk verified

additional_verifications:
  - sar_investigation_chain_verified_non_cleared
  - merger_boundary_transitive_walk_verified
  - cross_substrate_dispatch_walked
  - sar_existence_claim_resolved
  - sar_content_redacted_per_§10.70_non_cleared_paragraph

sar_subset_non_cleared:
  investigation_id_redacted:     [redacted]
  customer_id_redacted:           [redacted]
  pre_close_entry_count:          18
  post_close_entry_count:         47
  cross_anchor_traversals:         1
  sar_filed_with_fincen:           true
  sar_filed_at_utc:                [redacted]
  sar_subject_summary_redacted:   [redacted]

elapsed: 1.9s
```

Non-cleared mode returns PASS with content redacted. Padraic authenticates and re-runs in cleared mode; the verifier walks the full 65-entry SAR investigation chain across both partitions and the substrate boundary in 3.4 seconds. Padraic reconciles the cleared-mode walk against his AML platform's case file. The two reconcile cleanly.

**Padraic:** "Cleared mode walks the full chain. The §10.70 cross-tenant-investigation-handover discipline at close brought the open Mission Plaza SAR file into Brazos's AML platform under one continuous investigation chain. The pre-close chain entries are byte-identical pre-seal and post-seal; the cross-anchor at close binds the legacy investigation chain into Brazos's post-close investigation chain; the post-close investigation continued under Brazos's BSA officer until the FinCEN filing on April 18. The chain holds across the merger boundary in cleared and non-cleared modes both."

> ### Confirmation #7 — §10.70 SAR-filing chain across the merger boundary walks under cleared and non-cleared modes both
>
> The SAR investigation chain `sar-mp-to-brazos-2025q4-002` spans the merger boundary across 65 chain entries (18 pre-close on Mission Plaza's AWS-resident AML platform; 47 post-close on Brazos's Azure-resident AML platform; bound via the cross-anchor at close). The verifier walks the chain under non-cleared mode (1.9 seconds; existence claim resolved with content redacted) and under cleared mode (3.4 seconds; full investigation content resolved against the BSA officer's authenticated credentials). The merger boundary is transitively walked; the cross-anchor binds the pre-close investigation chain into the post-close chain; the §10.70 cross-tenant-investigation-handover discipline is operational across the merger boundary and across the substrate boundary.

## 11:00 AM — Three more AI-decisioning composition cases

Mike walks three more credit-decisioning composition cases across the merger boundary for completeness. Case A: a Mission Plaza legacy customer who received a pre-close auto-loan pre-qualification, was declined for credit pre-close on dti-ratio grounds, refinanced an existing auto loan post-close under Brazos's rate sheet through a different product structure. Case B: a Mission Plaza legacy customer with multiple pre-close credit-card pre-qualifications across two years (none of which she acted on) who applied for a Brazos credit card in June post-close and received an adverse-action decision under Brazos's `brazos-rc-2026q2` dictionary. Case C: a Brazos-native customer with no Mission Plaza-legacy footprint who applied for a HELOC in March post-close referencing a March Brazos marketing offer (no cross-substrate dispatch needed; baseline post-close-only case for control).

Each case walks cleanly. The §10.11.1 family resolves under both Mission Plaza's and Brazos's dictionary versions on the appropriate sides of the merger boundary. The §10.11.2 FCRA reinvestigation clock walks correctly under Brazos's dictionary for the Case B adverse-action record (the customer disputed in July; reinvestigation completed in 19 days, well inside FCRA's 30-day floor; original decision affirmed).

**Mike** (writing): "*Three additional AI-decisioning composition cases across the merger boundary walked cleanly under §10.11.1 + §10.11.2 + §10.21 composition; the cross-substrate dispatch via §10.40 cross-anchor resolves on Cases A and B; Case C as the post-close-only control resolves under the post-close partition only. — No findings.*"

## 12:00 PM — Lunch

The team eats in the engagement room. Sandwiches from a place on Allen Parkway. Dawn is at the table with Renata and Easton; the conversation centers on the November cut-over runbook, the Phase B Brazos marketing-surface extension (already in progress; landed in production seven months ago at close, three months after Dawn started at MMPWorks), and the standards-memo language the spec body will pick up after the engagement.

Sonya sits next to Tom and asks a quiet question.

**Sonya:** "The §10.69 cross-tenant clarifier paragraph at 22 seconds is the same shape as Mission Plaza's §10.69 walk at 22 seconds in November. The cross-tenant clarifier paragraph composes both shapes under one verifier-output schema. — Was that the design intent, or the working-group sub-track's emergent answer?"

**Tom:** "Working-group emergent. — The §10.69 cross-tenant clarifier paragraph shipped in a Herald release seven months after Mission Plaza in November and three months before today's Brazos engagement. The clarifier emerged from the working-group sub-track that took up Mission Plaza's §10.69 walk as a canonical-reference shape and asked the cross-tenant question. The clarifier doesn't pick clouds or vendors; it picks the inheritance pattern across cross-anchors. — The 22-second number on both walks is the canonical shape because the verifier dispatches against the same code path either way. The Mission Plaza walk and the Brazos walk converge on the same elapsed time because they exercise the same primitive."

**Sonya:** "And the working-group sub-track."

**Tom:** "Three review cycles since Mission Plaza in November. Spec body picks it up at the next quarterly review. — The standards memo from this engagement will be the production-validated reference. Heather on Steve's documentation side has been keeping the spec-docs anchor stable across the section's evolution; she'll lift the canonical-reference shape into the standards memo by Friday."

Sonya writes the lesson in her engagement notebook.

*§10.69 cross-tenant clarifier paragraph: working-group emergent from Mission Plaza canonical-reference shape; cross-tenant traversal under one verifier dispatch; 22 seconds elapsed on both walks because the verifier code path is the same.*

She underlines *the same.*

## 1:00 PM — The §10.13 SR 11-7 binder composition walk across the merger boundary

Adelaide Carrowmore-Finch returns to the room with Brazos's Q2 2026 SR 11-7 model-risk binder. The binder is a structured PDF — 247 pages — covering both the post-close Brazos credit-decisioning model (the XGB ensemble) and the inherited Mission Plaza legacy credit-decisioning model (the GBM, retained in chain for retrospective reinvestigations on pre-close decisions). The binder composes both lineages under one quarterly model-risk governance framework; the MRM committee chair (a Brazos board member) signed the binder on June 30; the institution's CRO signed on July 8; the institution's CCO signed on July 15.

**Adelaide:** "The composition. — The Brazos SR 11-7 binder picks up Mission Plaza's legacy model-card lineage at close; the legacy lineage retires under §10.21's `decisioning_pivot_with_preserved_lineage` composition method; the legacy lineage remains in the binder for retrospective reinvestigations under the seven-year retention floor; the Brazos lineage is the active lineage going forward. Two lineages, one binder. — Walk the citation."

Mike pulls page 47 of the binder — *Adverse-Action Population Profile — Q2 2026 — Cross-Charter Inheritance Composition*. The page has a chart, a table, and a footnote.

The footnote reads:

> Adverse-action population reconstructed from Brazos's TesseraSeal chain (tenant `brazos-federal-prod`, service `brazos-credit-decision`, period 2026-04-01 through 2026-06-30) plus the inherited Mission Plaza legacy chain (tenant `mission-plaza-bank-prod`, service `mission-plaza-credit-decision`, period 2025-08-01 through 2026-01-31, bound to Brazos's chain via the cross-vendor chain-merge anchor at close per §10.40). Verifier output captured 2026-07-04 at 09:15 CDT; verifier exit code 0; verifier additional verifications include `adverse_action_family_verified`, `cross_substrate_dispatch_walked`, `dictionary_version_lineage_resolved` (both `brazos-rc-2026q2` and `mission-plaza-rc-2026q1-final` dictionaries traversed for the retrospective component). Reconstruction-method hash: `7c0f3b6e9a2d5c8f1b4e7a0d3c6f9b2e5a8d1c4f7b0e3a6d9c2f5b8e1a4d7c0f`. Reconstructor: Hollis Buchanan-Sherrod, Brazos CRO. Reconstructor's chain-bound signature reference: `ce_brazos-q2-2026-srm-binder-sig-001`.

**Mike:** "The footnote binds both dictionary lineages and the cross-substrate dispatch. — Walk the reconstruction."

Cyrille runs the reconstruction. The verifier pulls the chain entries for Q2 2026 (Brazos's chain) plus the retrospective component (Mission Plaza's chain, August 2025 through January 2026, for any reinvestigation that landed in Q2 2026 against a pre-close decision). The chart reconstructs identically; the table reconstructs identically; the reconstruction-method hash recomputes byte-equal against the bound value.

**Adelaide:** "The OCC examination at the post-merger cycle will read this binder. The composition is what the OCC will press hardest on — the cross-charter inheritance under SR 11-7 is the discipline they audit at every post-merger cycle. — The bank's posture is that the chain produces the reconstruction; the §10.13 evidentiary composition is operational; the cross-substrate dispatch resolves; both dictionary lineages are traversable. The OCC will close that line of inquiry in one meeting at the post-merger examination, the same way the Texas Department of Banking closed it at March's state-charter examination cycle."

> ### Confirmation #8 — §10.13 SR 11-7 model-risk binder composition spans both pre-close Mission Plaza and post-close Brazos lineages under cross-substrate dispatch; reconstruction-method hash recomputes byte-equal
>
> Brazos's Q2 2026 SR 11-7 model-risk binder composes Brazos's active credit-decisioning model lineage (XGB ensemble, `brazos-rc-2026q2` dictionary) with Mission Plaza's retired legacy lineage (GBM, `mission-plaza-rc-2026q1-final` dictionary and predecessors) under one quarterly governance framework. The reconstruction-method hash on every quantitative claim in the binder cites both lineages plus the cross-substrate dispatch via the §10.40 cross-anchor; the verifier emits `adverse_action_family_verified`, `cross_substrate_dispatch_walked`, and `dictionary_version_lineage_resolved` (both lineages traversed for retrospective components). The reconstruction recomputes byte-equal against the bound value. The §10.13 evidentiary composition is operational across the cross-charter inheritance; the OCC post-merger examination cycle will read the same composition Brazos walked at the March Texas Department of Banking state-charter cycle.

## 2:30 PM — The §10.17 partition-ceremony attestation walk and the §10.22 redaction-discipline walk

The §10.17 partition-ceremony attestation for the cross-cloud-anchor placement at close walks cleanly under Adelaide's GC-side certification. The cross-cloud-anchor placement was attested at close by both CFOs (Hortense Marbury-Caldwell for Mission Plaza, signing under AWS CloudHSM at 23:59:45 UTC Jan 31; Tobias Wendell-Kincaid for Brazos, signing under Azure Key Vault Managed HSM at 00:00:00.500 UTC Feb 1); the §10.17 partition-ceremony attestation document signed by both CFOs and witnessed by both institutions' GCs (Dolores Aguirre-Marín for Mission Plaza, who had been GC at Mission Plaza for nineteen years and signed the engagement-letter close-out at Mission Plaza in November before retiring at close on Jan 31; Adelaide for Brazos) is in the institution's evidence registry. The dual-GC witness attestation is referenced by every subsequent chain entry via the genesis-block-lineage of the cross-anchor.

**Adelaide:** "Dolores retired the day before close; she signed the Mission Plaza-side ceremony attestation as her last institutional act before the seat transitioned to me under the Brazos GC umbrella at close. Her signature is on file; the §10.17 attestation references the signature by Ed25519 fingerprint; the attestation verifies cleanly under the cross-substrate dispatch through the cross-anchor. — One ceremony, two GCs, two CFOs, two HSM substrates, one continuous attestation chain."

The §10.22 redaction-discipline walk covers the rebrand-period campaign window — specifically, the 47,247-customer Variant B subset. The customer-subset CSV the bank produced under §10.22 redaction discipline carries the customer-name field and the customer-id field but redacts the customer's payment account number, the customer's date of birth, and the customer's Social Security number — fields that are bound in the chain under per-event MAC but are surface-controlled at the disclosure-production boundary per the §10.22 schema-redaction-template family.

**Cyrille:** "The §10.22 redaction template for the customer-subset CSV is named at the production-discipline registry under `disclosure_template_id: brazos-customer-subset-redaction-template-2026q1`. The template names every field by classification; the production-discipline registry binds the template by hash; the verifier confirms the produced CSV's redaction matches the template at production time. — One template, every customer-subset CSV the bank produces. The disclosure is honest about what's redacted, why, and on what authority."

**Adelaide:** "Walked. — The §10.22 schema-redaction-template family is operational; the production-discipline registry binds the template; the verifier confirms the redaction matches. — Day 2 afternoon ran clean. — Margarethe, the close on Day 2?"

**Margarethe:** "Day 2 closes. — Two confirmations from this morning (§10.69 + §10.70); three additional AI-decisioning composition cases walked cleanly; one confirmation from this afternoon (§10.13 SR 11-7 composition); §10.17 partition-ceremony attestation and §10.22 redaction-discipline walked cleanly without separate confirmation entries because the composition is the §10.13 confirmation's sibling discipline. — Day 3 morning at 8:00; §10.71 Fedwire walk with the Federal Reserve Bank of Dallas Wholesale Payments Office on the bridge."

## 4:30 PM — Day 2 debrief

The team reconvenes at 4:30. Margarethe stays; Adelaide stays; Hollis Trent-Mosley stays with the November cut-over runbook draft. Donovan flies back to San Antonio in the morning and joins by video for Day 3.

**Raj:** "Day 2 summary. — Mike?"

**Mike:** "Six end-to-end cases plus the SR 11-7 binder composition walk. — The §10.69 per-customer disclosure across the merger boundary walks in 22 seconds; the §10.70 SAR-filing across the merger boundary walks under cleared (3.4s) and non-cleared (1.9s) modes both; three additional AI-decisioning composition cases walked under §10.11.1 + §10.11.2 + §10.21 composition with cross-substrate dispatch via §10.40; the §10.13 SR 11-7 binder composition spans both pre-close and post-close lineages with reconstruction-method hash byte-equal. — No findings beyond the Day 1 Nit. The Nit is unchanged: cross-charter retention policy framework-fit memo against the OCC post-merger framework not yet produced; Adelaide will draft before the 60-day OCC examination."

**Adelaide:** "Draft in your hands by Friday. — The framework-fit memo cites §10.40 substrate-agnostic clarifier as the operative spec text; cites the cross-substrate dispatch as the operational composition; cites the OCC post-merger framework's record-retention guidance as the inheritance discipline. The memo is short — three pages."

**Diana:** "§10.69 + §10.70 walked. The cross-tenant clarifier paragraph is operationally exercised on the customer side and on the BSA side both. — No findings."

**Luis:** "Storage tier append-only enforced on both substrates. AWS S3 object lock in compliance mode for the legacy Mission Plaza chain; Azure Blob immutable-storage with legal hold for the Brazos chain. Both retention floors exceed the 7-year cross-charter inheritance floor by 14+ months. — No findings."

**Chen:** "Cross-cloud anchor and Insider legacy-export reconciliation walked Day 1; SR 11-7 binder reconstruction walked Day 2 afternoon. — No findings."

**Sonya:** "From the working-group sub-track side: the §10.69 cross-tenant clarifier paragraph at 22 seconds on both Mission Plaza in November and Brazos × Mission Plaza today is the canonical-reference shape for the cross-tenant traversal under one verifier dispatch. The standards memo following this engagement will pick up the shape as production-validated. — That's the wishlist-on-the-spec side; not an engagement finding, but a working-group reference point for Heather to lift into the standards memo by Friday."

**Tom:** "Recusal-protocol close-out under the spousal-disclosure paragraph operates cleanly. Steve's twenty minutes tomorrow at 13:30 is on the engagement-letter side; Adelaide cleared the language with the firm's GC three weeks ago; the appearance is on the engagement calendar. — Day 3 kickoff at 8:00."

**Raj:** "Day 2 confirms. — Margarethe?"

**Margarethe:** "Day 2 ran clean. — Tomorrow morning the Fed of Dallas joins by bridge at 9:00; Magdalena Forsberg-Aliyev's on the bridge. Tomorrow afternoon Hollis brings the November cut-over runbook to the room; Steve joins by video at 13:30 for the platform-migration question; close-out at 15:00. — Engagement closes on schedule and on budget."

The team scatters at 5:15. Tom catches Sonya at the elevator.

**Tom:** "The 22-second number on both engagements is the lesson."

**Sonya:** "The 22-second number on both engagements is the lesson. — The verifier dispatches against the same code path. The chain doesn't care about the merger boundary or the substrate boundary or the vendor boundary; the verifier dispatches against the primitive. The primitive is what the spec normates; the engagement is what exercises the primitive in production."

**Tom:** "And Heather lifts it into the standards memo by Friday."

**Sonya:** "And Heather lifts it into the standards memo by Friday."

## Day 3 — 8:00 AM — Day 3 kickoff

The Day 3 morning opens with breakfast tacos again — Hollis insists on the same place — and Margarethe brings two thermoses of black coffee. Donovan joins by video bridge from San Antonio. Magdalena Forsberg-Aliyev from the Federal Reserve Bank of Dallas joins at 8:45 to test the bridge before the §10.71 walk at 9:00.

**Magdalena** (testing the bridge): "Margarethe, Padraic, the team. Good morning. — Bridge is clean. The §10.21.3 voluntary cross-institution-anchor registry is staged on my side; I have the Federal Reserve Bank of Dallas Wholesale Payments Office's observer credentials authenticated. Brazos's registry-discovery cross-anchor is registered; Mission Plaza's pre-close registry entry is on the registry as a retired institution; the cross-institution wire chain integrity for any outbound Fedwires across the merger boundary is auditable through the registry. — Ready when you are."

**Padraic:** "Ready."

## 9:00 AM — The §10.71 Fedwire walk with the Federal Reserve Bank of Dallas

The §10.71 surface — cross-institution Fedwire / ACH chain integrity — is the wholesale-payments analog of the per-customer §10.69 surface. Cross-institution chain integrity is verified through the §10.21.3 voluntary registry that the Federal Reserve Bank of Dallas Wholesale Payments Office operates; the registry is the institutional-side observer of the cross-institution-anchor binding for any Fedwire that crosses an institutional boundary where both institutions participate.

Padraic pulls five Fedwires across the audit period: three outbound Brazos Fedwires that originated post-close to counterparty banks that participate in the §10.21.3 registry, one outbound Brazos Fedwire to a counterparty bank that does NOT participate in the registry (a `cross_anchor_unbound` documented residual), and one outbound wire that originated as a Mission Plaza pre-close wire to a participating counterparty and chained transitively to Brazos's post-close chain via the cross-anchor.

Each of the five Fedwires walks under the §10.71 verifier dispatch. The participating-counterparty wires resolve through the §10.21.3 registry attestation in 4-6 seconds per wire. The non-participating-counterparty wire emits a `cross_anchor_unbound` documented residual marker — the wire is integrity-bound on Brazos's side under the per-event MAC; the counterparty-side anchor is unresolved because the counterparty does not participate in the registry; the residual is documented under §10.71's operational-residual-marker discipline.

```
$ herald-verify --tenant=brazos-federal-prod \
                --fedwire-id=brazos-fedwire-2026-04-15-imad-A1B2C3D4 \
                --strict --explain \
                --cross-institution-registry-walk
Status: PASS
Step:   12
Reason: Fedwire chain integrity verified;
        cross-institution-registry attestation
        resolved against the §10.21.3 voluntary
        registry operated by the Federal Reserve
        Bank of Dallas Wholesale Payments Office;
        counterparty bank's cross-anchor binding
        resolved

additional_verifications:
  - cross_institution_registry_attestation_resolved
  - counterparty_bank_cross_anchor_binding_resolved
  - fedwire_chain_integrity_verified

elapsed: 4.7s
```

**Magdalena:** "Registry attestation resolves cleanly. — The voluntary registry the Federal Reserve Bank of Dallas operates is the §10.21.3 institutional surface for cross-institution-anchor binding; Brazos's registry entry is current; the counterparty's registry entry is current; the cross-anchor binding resolves between them. — The Fed of Dallas's posture on the §10.21.3 registry is that the registry is operationally voluntary for counterparties but operationally helpful for the Fedwire chain integrity discipline; we have 47 institutions on the registry today out of roughly 1,500 Fedwire-eligible counterparties. The 23-institution chronic non-participant population is documented as `cross_anchor_unbound` residuals on the wires they receive; the integrity claim is preserved on the originating-bank side; the counterparty-side anchor is unresolved."

Padraic walks the cross-merger-boundary wire next — a $3.2M wire to a Florida regional bank that originated as a Mission Plaza pre-close wire on January 28, 2026 and was rebooked under Brazos's wholesale-payments operations on March 14, 2026 under a separate operational event (the original recipient's settlement instruction needed re-issuance after a routing change). The chain entry for the original wire is on the Mission Plaza chain; the chain entry for the rebooking is on the Brazos chain; both chain entries reference each other via §10.71's `parent_wire_run_id` parent-linkage and the cross-anchor binding at close.

```
$ herald-verify --tenant=brazos-federal-prod \
                --fedwire-id=brazos-fedwire-2026-03-14-imad-E5F6G7H8-rebook \
                --strict --explain \
                --cross-institution-registry-walk \
                --span-merger-boundary
Status: PASS
Step:   12
Reason: Fedwire chain integrity verified across
        merger boundary; parent wire on legacy
        Mission Plaza chain resolved via
        cross-substrate dispatch; counterparty's
        §10.21.3 registry attestation resolved;
        rebooking chain entry references parent
        wire via §10.71 parent-linkage

additional_verifications:
  - cross_institution_registry_attestation_resolved
  - merger_boundary_transitive_walk_verified
  - cross_substrate_dispatch_walked
  - parent_wire_linkage_resolved
  - cross_anchor_binding_resolved
  - fedwire_chain_integrity_verified

elapsed: 6.2s
```

**Magdalena:** "Six point two seconds for the cross-merger-boundary rebooked wire walked transitively through the cross-anchor and the §10.21.3 registry. — The Fed of Dallas's institutional reference for cross-institutional wire integrity across a post-merger boundary is now Brazos × Mission Plaza; the §10.71 cross-institution discipline is operational across the institutional boundary and across the merger boundary together. — I'm going to file the standards memo from my side after the engagement closes; the institutional reference for the §10.21.3 registry's cross-merger-boundary attestation discipline is this engagement."

**Padraic:** "Magdalena, thank you for the bridge. The Fed of Dallas's posture is on the record. — One more wire?"

**Magdalena:** "One more — pick the non-participating counterparty residual case so we have the documentation discipline on the record."

Padraic walks the `cross_anchor_unbound` residual case — a $480K wire to a small West Texas bank that does not participate in the §10.21.3 registry. The wire is integrity-bound on Brazos's side under the per-event MAC; the counterparty-side anchor is unresolved; the residual is documented under §10.71's operational-residual-marker discipline.

```
$ herald-verify --tenant=brazos-federal-prod \
                --fedwire-id=brazos-fedwire-2026-05-22-imad-J9K0L1M2 \
                --strict --explain \
                --cross-institution-registry-walk
Status: PASS (with documented residual)
Step:   12
Reason: Fedwire chain integrity verified on
        originating side; counterparty's §10.21.3
        registry attestation unresolved
        (counterparty does not participate in
        registry); residual documented per §10.71
        operational-residual-marker discipline

additional_verifications:
  - originating_side_chain_integrity_verified
  - counterparty_registry_non_participation_documented
  - cross_anchor_unbound_residual_marker_emitted

elapsed: 1.8s
```

**Magdalena:** "Documented residual. — The Fed of Dallas's posture is that operational residuals are operationally honest about what the chain can and cannot claim across the counterparty boundary. Brazos's integrity claim on the originating side is preserved; the counterparty's side is unresolved because the counterparty has not joined the §10.21.3 registry. The residual is the chain's honest accounting of the boundary. — Padraic, the Fed of Dallas observer leaves the bridge at the §10.71 walk's close. Magdalena out."

She drops.

> ### Confirmation #9 — §10.71 cross-institution Fedwire / ACH chain integrity walks under §10.21.3 voluntary registry attestation; cross-merger-boundary wire walked transitively in 6.2 seconds; non-participating-counterparty residual documented honestly
>
> The §10.71 surface walks five Fedwires across the audit period: three participating-counterparty post-close wires (4-6 seconds each via §10.21.3 registry attestation), one cross-merger-boundary rebooked wire (6.2 seconds, walked transitively via cross-anchor + §10.71 parent-wire linkage + §10.21.3 registry attestation), one non-participating-counterparty `cross_anchor_unbound` documented residual (1.8 seconds; originating-side integrity verified; counterparty-side anchor unresolved per §10.71 operational-residual-marker discipline). The Federal Reserve Bank of Dallas Wholesale Payments Office (Magdalena Forsberg-Aliyev) confirms Brazos × Mission Plaza as the canonical institutional reference for cross-merger-boundary Fedwire chain integrity under the §10.21.3 voluntary registry attestation.

## 11:00 AM — The Day 3 morning continued: §10.5 HSM custody walks and the §10.36 supplemental-seal mechanism walk

Luis walks the §10.5 HSM custody attestations for both substrates side-by-side. The AWS CloudHSM partition attestation document for Mission Plaza's legacy chain — issued by AWS at the cluster's FIPS 140-2 Level 3 certification — is in the §10.5 attestation registry. The Azure Key Vault Managed HSM attestation document for Brazos's post-close chain — issued by Microsoft at the vault's FIPS 140-2 Level 3 certification — is in the same registry. The verifier accepts both as Level 3+ HSM custody under §10.5's substrate-vendor-equivalent attestation discipline; the §10.5 clarifier paragraph normates the substrate-vendor-equivalent treatment.

The §10.36 supplemental-seal mechanism walk confirms the operational discipline: the cross-cloud cut-over window from 23:59:30 UTC Jan 31 to 00:00:01 UTC Feb 1 accepted no writes; the mechanism was armed; the mechanism remained unexercised. The chain entry for the no-write window at the cross-anchor names the entries-received-in-window count at zero and confirms `supplemental_seal_required: false`. The §10.36 mechanism is operational; the operational discipline at the cut-over was clean; the mechanism's existence preserves the chain's integrity claim against any future cut-over where entries do arrive in the window.

**Luis:** "Both HSM substrates attested at FIPS 140-2 Level 3 under §10.5 substrate-vendor-equivalent discipline. The §10.36 supplemental-seal mechanism remained unexercised at the cross-cloud cut-over; the operational discipline at the cut-over was clean. — No findings."

## 12:30 PM — Lunch, Day 3

The team eats in the engagement room. Hollis Trent-Mosley has the November cut-over runbook draft printed for the table — a three-page document with the §10.41 partition closure attestation language, the §10.39 successor-attestation-envelope final-form revision, the §10.42 backfill-seal discipline applied at the November cut-over partition closure boundary (the closure boundary, not the original placement boundary), and the §10.17 dual-witness attestation language for the partition closure ceremony.

**Hollis:** "November 15, 2027 at 00:00:01 UTC is the scheduled full-integration cut-over. The brand transition closes; the Mission Plaza brand retires fully; all customer touchpoints carry the Brazos brand. — The §10.41 partition closure attestation closes the three-partition map into a single coverage region under the post-close partition. The pre-acquisition partition remains in chain by reference; the cut-over window remains documented with zero entries; the post-cut-over partition extends through the November cut-over to today and forward. — The closure ceremony at November 15 is a single signature event under §10.41's partition closure attestation, witnessed by Adelaide (GC, Brazos) and by Donovan (CAE, formerly Mission Plaza, now reporting to Margarethe under integration), countersigned by Margarethe (CAE, Brazos) and by Tobias Wendell-Kincaid (CFO, Brazos). — That's the architecture. Adelaide and I walked the language draft last week; today's afternoon walk is the engagement-side confirmation."

**Adelaide:** "Steve's twenty minutes at 13:30 covers one specific technical question on the closure-ceremony architecture and the 2028 Marketo platform-upgrade question that Brazos's marketing-ops team has been carrying. — Margarethe?"

**Margarethe:** "Steve at 13:30. — Twenty minutes. Tom logs the appearance under the spousal-disclosure paragraph; Adelaide co-signs the language. — Dawn is in the room; Renata is in the room; Easton is on video from San Antonio. — That's the afternoon."

## 1:30 PM — Steve by video, twenty minutes, §10.41 partition closure + 2028 Marketo platform-migration

The room reassembles at 13:25. Margarethe, Renata, Easton on video from San Antonio, Hollis, Adelaide, Dawn at the table with Tom to her right, Raj at the head of the table, Mike and Sonya next to Dawn, the rest of the team around the back.

Tom opens the bridge for Steve at 13:30 exactly.

Steve joins. Video on; he's at MMPWorks's Austin office, the same conference room with the window behind him and the half-visible whiteboard. Same blazer-over-button-down; slightly more gray at the temples than the November video. He's holding a coffee.

**Steve:** "Margarethe. Renata. Adelaide. Hollis. — Dawn. — Tom, Raj, the team. — Morning."

**Tom:** "Steve. Welcome. — Tom logged the start at 13:30 CDT. Twenty-minute window. Two questions: the §10.41 partition closure ceremony architecture for November 15, and the 2028 Marketo platform-migration question Renata's marketing-ops team has been carrying. The spousal-disclosure paragraph is in force; this is Steve's appearance on the engagement under that paragraph; Adelaide cleared the language with the firm's GC three weeks ago."

**Steve:** "Acknowledged. — Hollis, the §10.41 partition closure ceremony architecture first. You sent the language draft last week. The closure attestation closes the three-partition map into a single coverage region under the post-close partition; the pre-acquisition partition remains in chain by reference; the cut-over window remains documented with zero entries. — The architecture is sound. One observation. The closure ceremony at November 15 has a sibling architecture decision: does the November ceremony's §10.41 partition closure attestation supersede the February cross-anchor or compose with it? Both are valid; the spec text covers both compositions; the choice has operational implications for retrospective reinvestigations on pre-close decisions. — My recommendation is compose, not supersede. The February cross-anchor remains the institutional reference for the pre-close-to-post-close binding; the November partition closure adds the closure attestation as a sibling event on the chain. Retrospective reinvestigations on pre-close decisions walk through the February cross-anchor; the November partition closure doesn't disturb the February cross-anchor's binding."

**Hollis:** "Compose, not supersede. — Adelaide, on the GC side?"

**Adelaide:** "Compose. — The retrospective-reinvestigation discipline carries through to the seven-year retention floor; the February cross-anchor is the institutional reference for any pre-close decision; the November closure is the operational reference for the full-integration brand transition. Two events, one chain, no supersession. The OCC will read both events at the next examination cycle."

**Steve:** "Good. — Renata, the 2028 Marketo platform-migration question."

**Renata:** "Marketo Engage has announced a major platform upgrade scheduled for the first half of 2028. The upgrade changes the internal hash format Marketo uses for its campaign-history exports — Marketo's internal format moves from SHA-256 over an older canonical-encoding scheme to BLAKE3 over a newer canonical-encoding scheme. The §10.21 chain entries we write today bind the rendered-output hash under SHA-256 over RFC 8785 — the hash discipline we operate under. — The question is what happens to the legacy Marketo-Engage chain entries when the Marketo platform upgrade lands. Specifically: can a 2025 Insider-era chain entry bound under SHA-256 + RFC 8785 still walk under a future verifier that may compose with Marketo's BLAKE3-era artifacts?"

**Steve:** "Short answer: yes. The §10.21 chain entries bind the hash under the institution's discipline at the moment of binding; the vendor's platform format is separate from the institution's binding. The institution's binding is SHA-256 + RFC 8785 today; the binding is preserved indefinitely under the institution's retention floor. — The vendor's platform format change is a vendor-side migration event; it affects what the vendor exports going forward, not what the institution bound at the moment of binding. — Longer answer: the §10.21.4 vendor-version-registry lookup contract Insider committed in November includes the vendor's commitment to maintain lookup-endpoint compatibility across vendor-side platform upgrades. Insider's commitment for the Mission Plaza legacy lookup endpoint is six years from version retirement — through 2031. The Marketo platform upgrade in 2028 falls inside that window; Marketo Engage's commitment to maintain lookup-endpoint compatibility for the legacy Insider footprint is operationally on the Marketo side; the institution's binding under SHA-256 + RFC 8785 is preserved. — The §10.21.4 vendor-version-registry lookup contract is the institutional surface that holds across vendor-side platform upgrades; the chain entries themselves don't need to migrate."

**Mike:** "And if Marketo retires the legacy lookup endpoint before 2031?"

**Steve:** "Then the §10.21.4 contract is breached; the institution's posture under §1.2 epistemic-scope discipline is that the chain entry's integrity claim on the binding is preserved (the SHA-256 + RFC 8785 binding is cryptographic), and the vendor-side commitment to the lookup endpoint is contractual. The two claims compose; the verifier produces both verdicts. — If the vendor retires the lookup endpoint, the verifier emits `vendor_version_registry_lookup_endpoint_unavailable` and surfaces the breach at audit. The cryptographic claim is preserved; the contractual claim is breached and documented. — That's the §1.2 + §10.21.4 composition."

**Renata:** "And the operational posture today on the Marketo platform upgrade?"

**Steve:** "Operationally, the Brazos side stays on the current §10.21 + §10.21.4 + §10.40 composition. The Marketo platform upgrade in 2027 is a vendor-side migration; the bank's SDK at the Marketo Engage boundary handles the migration through the §10.21.4 lookup endpoint, which Marketo Engage commits to maintain through the institution's retention floor. The bank doesn't need to retroactively re-anchor or re-bind legacy chain entries; the institution's binding under SHA-256 + RFC 8785 is preserved through the retention floor. — The Marketo platform upgrade is operationally a non-event for the chain. Brazos's marketing-ops team can move at Marketo's cadence on the platform upgrade without disturbing the chain's discipline."

**Renata:** "Good. — Hollis, the November cut-over runbook language acknowledges the 2027 platform-migration posture under the §10.21.4 + §1.2 composition; Adelaide and I will close the language by Friday."

**Hollis:** "Closed by Friday."

**Steve:** "Anything else from the room?"

**Dawn** (from the audit-room side, speaking for the first time on the Steve-bridge): "One question. — Steve, the §10.40 substrate-agnostic clarifier in its production-validated form after this engagement. Does the standards memo language carry the canonical-reference shape as 'cross-cloud byte-equality reconciliation at six minutes for 4.89 million pre-close entries' or as the §10.40 substrate-agnostic abstract pattern?"

**Steve:** "Both. — The canonical-reference shape carries the abstract pattern as the spec-text reference and the production-validated metric as the institutional-reference example. The standards memo names Brazos × Mission Plaza as the canonical institutional reference for cross-cloud chain consolidation as a routine M&A integration step; the abstract pattern is preserved as the substrate-agnostic primitive; the production-validated metric is the institutional example. — Heather has the standards-memo draft language already in the documentation queue; she lifts the canonical-reference shape by Friday after the engagement closes."

**Dawn:** "Good. — Tom, log the close."

**Tom:** "Logged. 13:48 CDT. Eighteen minutes; two minutes under window. The §10.41 partition closure ceremony architecture composition is confirmed; the 2028 Marketo platform-migration posture is confirmed; the §10.40 standards-memo canonical-reference shape is confirmed. Steve appears under the spousal-disclosure paragraph; the appearance is the second under that paragraph (the first was at the Hill Country follow-up working-group sub-track call in June). — Anything else from your side, Steve?"

**Steve:** "Nothing else. — Margarethe, Renata, Adelaide, Hollis, the Brazos team — thank you. — Dawn, I'll see you at the airport tomorrow."

**Dawn:** "Tomorrow."

Steve nods. The bridge closes. Tom logs the close in his appearance-log notebook; the line reads: *13:48 CDT, Day 3. Second appearance under the spousal-disclosure paragraph for institution Brazos Federal Bancshares, engagement 31. Composition questions §10.41 partition closure + §10.21.4 vendor-version-registry lookup + §1.2 epistemic-scope + §10.40 substrate-agnostic clarifier all resolved. Engagement closes Day 3 afternoon, 15:00 CDT.*

The room is quiet for a beat.

**Margarethe:** "Two minutes under window again. — Renata, the November cut-over runbook closes by Friday; Adelaide, the framework-fit memo by Friday; Hollis, the cut-over runbook draft to the board chair by Monday. — Engagement-close-out at 15:00."

## 2:00 PM — Memo finalization

The Day 3 afternoon between Steve's video and the close-out is memo-draft work. Mike and Sonya draft the §10.41 partition closure memo's executive summary; Elena and Chen draft the cross-cloud-anchor appendix; Diana drafts the §10.69 + §10.70 composition addendum; Luis drafts the §10.5 HSM-substrate-vendor-equivalent attestation appendix; Tom drafts the partner-letter close-out language.

The confirmation memo finalizes by 14:30. Six pages, headline up front, spec-section confirmation walks in the body, four appendices (cross-cloud anchor verifier output samples, SR 11-7 binder reconstruction-method-hash reference, §10.69 disclosure walk sample for Vionetta, §10.71 Fedwire walk samples including the documented residual case).

The §10.41 partition closure memo finalizes by 14:50. Four pages, headline up front, partition closure ceremony architecture composition (compose, not supersede), §10.39 successor-attestation-envelope final-form revision language, §10.42 backfill-seal discipline at the November closure boundary, §10.17 dual-witness attestation language. The closure ceremony at November 15 is named, calendared, and architected.

The partner-letter close-out finalizes by 15:00.

## 3:00 PM — Close-out

The close-out meeting is in Brazos's executive briefing room — a glass-walled room on the fourteenth floor with a view east across downtown Houston to the ship channel beyond. Margarethe, Renata, Adelaide, Hollis Trent-Mosley, Padraic Calhoun-Reidy, Easton Wadsworth on video from San Antonio, Donovan Eastlake-Boudreaux on video from San Antonio, Brigitte (from Mission Plaza's IA team) on video from Austin, and Brazos's M&A board member **Pastor Jeff Muchow** — LCMS pastor at Epiphany Lutheran Church in Cypress, six years in the pulpit there, six years on the Brazos board after Margarethe asked him to take the open community seat the same month he was called to Epiphany. He drove down from Cypress yesterday afternoon for the board's quarterly meeting on the seventeenth floor and walked one floor down for the close-out. From the firm: Raj, Tom, Dawn (vendor-side, in the room), and the rest of the team in seats around the back. Dawn and Jeff exchange a brief nod when she takes her seat; Steve had been on the bridge yesterday and her presence today is the first time Jeff has seen his sister-in-law in a vendor-side professional setting. He acknowledges her the way he acknowledges any congregant on a weekday — warmly, briefly, without making a moment of it.

**Margarethe:** "Close-out for engagement 31. — Raj, the floor is yours."

**Raj** (standing): "Margarethe, Renata, Adelaide, Hollis, Padraic, Donovan and Easton on video, Brigitte, Pastor Muchow, and the team — thank you. — Three days. — The confirmation memo confirms the cross-cloud chain consolidation operates as a routine integration step. Mission Plaza's full pre-close AWS-resident chain is byte-equal across the close boundary into Brazos's Azure-resident chain via the §10.40 substrate-agnostic cross-vendor chain-merge anchor; the byte-equality demonstration completes in five minutes forty-eight seconds for the cross-anchor walk and six minutes twelve seconds for the Insider legacy-export reconciliation. The §10.39 dual-CFO signature pair verifies across substrates under the §10.5 substrate-vendor-equivalent attestation discipline. The §10.42 backfill seal envelope recomputes byte-equal. The §10.41 three-partition coverage map resolves cleanly; the November partition closure architecture is composed, not superseded, per Steve's video confirmation this afternoon. The §10.21 cross-vendor model-handover for the AI-decisioning surface and the marketing-stack handover walks cleanly with the §10.21.4 vendor-version-registry lookup retained through 2031. The §10.69 per-customer disclosure across the merger boundary walks in 22 seconds. The §10.70 SAR-filing case across the merger boundary walks under cleared and non-cleared modes. The §10.71 Fedwire walk under the §10.21.3 Federal Reserve Bank of Dallas registry attestation walks cleanly including the documented cross-merger-boundary rebooked wire and the documented non-participating-counterparty residual. The §10.13 SR 11-7 binder composition spans both pre-close and post-close lineages. The §10.22 redaction-discipline and §10.17 partition-ceremony attestation walk under sibling composition. — Nine confirmations across three days. One Nit (the cross-charter retention policy framework-fit memo not yet produced; Adelaide drafts by Friday). Zero Gaps. Zero Partials."

He pauses.

**Raj:** "The engagement closes 18% under budget. — Brazos × Mission Plaza becomes the canonical institutional reference for cross-cloud chain consolidation as a routine M&A integration step. The standards memo following the engagement names §10.40 substrate-agnostic cross-vendor chain-merge anchor as production-validated. Magdalena Forsberg-Aliyev from the Federal Reserve Bank of Dallas Wholesale Payments Office is filing the institutional reference from the §10.21.3 registry side. Dawn's engagement-file note from Hill Country Federal Credit Union — *§10.40 anchor reads as routine on AWS-only; what happens when the substrate moves?* — is answered in production by today's engagement. — Tom, would you read the partner-letter close-out."

**Tom** (standing, reading from a printed copy): *"Engagement 31 (Brazos Federal Bancshares × Mission Plaza Bank) confirms the cross-cloud chain consolidation between Mission Plaza's pre-close AWS-resident chain and Brazos's post-close Azure-resident chain operates as a routine M&A integration step under the §10.40 substrate-agnostic cross-vendor chain-merge anchor. Nine spec-section confirmations across §10.5, §10.11.1, §10.13, §10.17, §10.21, §10.21.3, §10.21.4, §10.22, §10.36, §10.39, §10.40, §10.41, §10.42, §10.69, §10.70, §10.71. One documented Nit on the cross-charter retention policy framework-fit memo, pathwayed to remediation by Friday. Zero Gaps. Zero Partials. The engagement is the canonical institutional reference for cross-cloud chain consolidation as a routine operation; the standards memo follows."*

He sits down.

**Adelaide:** "GC signs off. The language is clean. The transition into the November cut-over is documented. — Brazos accepts the close-out as written."

**Margarethe:** "Brazos accepts. — Raj, the firm's signature."

Raj signs the partner letter as Lead Auditor. Tom countersigns as engagement-letter manager. Brigitte signs from the Mission Plaza side on video — the institutional-side language carries through cleanly. Margarethe signs from the Brazos side. Adelaide signs as GC. Donovan signs on video from San Antonio as legacy-CAE-now-reporting-into-Brazos.

**Margarethe:** "Engagement 31 closes. — Pastor Muchow, the board's chair-pro-tem, would you close the room."

Pastor Jeff Muchow stands. He has been silent across the close-out until this moment.

**Pastor Jeff Muchow:** "Margarethe, Renata, Adelaide, the institution's leadership and the firm's team and our vendor liaison and the Federal Reserve observer who left the bridge before this room reconvened — I am not going to give a benediction; the seat I hold on Brazos's board is a banking seat, not a pulpit, and the two vocations stay where they belong. But I have been on this board for six years and I have sat through one merger close-out before this one and I have not, before today, sat through one where the integration question — *can we prove what we did and didn't do* — was answered in six minutes by a verifier running across two clouds. The institutional question, when Margarethe asked me to take this seat in 2021, was whether the bank could survive an integration without losing customer trust. I am persuaded today that the institutional question's answer is the discipline this firm and this vendor and this chain have brought into the room. Honest dealings well-kept — that is what the chain produces, and that is what the room earned this week. — The work compounds. — Margarethe, close the room."

The room is quiet for a beat. Then Margarethe gathers her papers and nods to Raj.

**Margarethe:** "Engagement 31 closes. — Raj, the team, the vendor liaison — Brazos thanks you. — Dawn, the next time we see you it'll be in Houston or Austin; Renata and I have one more cross-vendor question coming up the working-group sub-track that may touch §10.21 model-handover sub-cases we haven't covered yet."

**Dawn:** "Whenever you'd like. — The MMPWorks vendor liaison's office in Austin is the bridge; Sonya carried the §10.21 vendor-opaque-render sub-case from Mission Plaza in November and would likely be the audit-side authoring auditor on whatever you bring to the working group next."

**Margarethe:** "Sonya — good. — Renata, walk Dawn to the elevator."

Renata stands. She walks Dawn to the elevator. The conversation between them is brief.

**Renata** (at the elevator): "Three years and three weeks from Hill Country to today. — Dawn, that's the long-shape work."

**Dawn:** "Three years and three weeks. — The engagement-file discipline. The note sits in the file; the question matures; the spec catches up; the engagement exercises the answer. — Today closes the long-shape."

**Renata:** "And the next long-shape?"

**Dawn:** "Sonya's vendor-opaque-render note from November. Three weeks or three years; the discipline is the same. — Whenever the vendor with the opaque render walks into a room, the note becomes actionable."

**Renata:** "Whenever the vendor walks into the room."

The elevator opens. Dawn rides down to the lobby.

## 4:30 PM — Lobby

The team gathers in the Brazos lobby. The Houston afternoon light is gold-and-warm across the courtyard fountain; the three live oaks at the entrance throw long shadows toward the parking lot. The team is tired and pleased and quiet in the way teams are when an engagement closes well.

Tom hands out the partner-letter copies. The firm's records are updated as of 15:42 CDT. The engagement is closed.

**Mike:** "Plane is at 7:30 tomorrow morning. — Three of us flying back to Chicago via Dallas; the rest connecting through the firm's other regional offices."

**Sonya:** "And the next engagement."

**Raj:** "Three weeks. — A pre-engagement readiness pass at a Carolinas-based community bank that just stood up their first §10.21 surface and wants the §10.21.4 vendor-version-registry lookup confirmation before next month's Fed exam. — Sonya, that's your engagement; you carry the §10.21 vendor-opaque-render sub-case in case the marketing-AI vendor at the Carolinas bank's stack has the opaque-render shape."

**Sonya:** "I have the note. — Three years or three weeks."

**Raj:** "Three years or three weeks."

The team scatters to their rental cars. Tom is the last to leave. He shakes Margarethe's hand at the front door, then walks to the SUV in the visitor lot.

Dawn is in the passenger seat of a separate rental — MMPWorks's car, parked next to the firm's SUV — with the laptop bag and an envelope in her lap. (Renata, at the elevator, had handed her the envelope without saying anything; Dawn will open it at the hotel.)

Tom catches Dawn's eye through the open window of her rental.

**Tom:** "Houston Friday."

**Dawn:** "Houston Friday. — Steve flies in tomorrow morning; we drive to Austin Friday for the standards-memo working-group call Monday. — Tom, thank you."

**Tom:** "Always."

He gets into the SUV. The team rolls out of the lot.

## 6:00 PM — Hotel restaurant, Day 3

The team takes the same corner table at the Hyatt. The Houston downtown skyline is amber and dust-rose; the air-conditioning is humming in the way it hums in September Texas. Sonya has her engagement notebook open on the table next to the cocktail menu.

Tom orders for the table — the Texas porterhouse for sharing again, the brisket starter, the chimichurri, two bottles of a Texas malbec. The food arrives. Mike pours.

**Tom:** "Engagement 31 closes. — To Brazos and to Mission Plaza, to Margarethe and to Donovan, to the cross-cloud chain consolidation as a routine M&A integration step, to Dawn's three-years-and-three-weeks Hill-Country-to-production cycle, and to the team."

The team drinks.

**Mike:** "And to the team."

**Tom:** "And to the team."

The team drinks again.

**Sonya:** "And to the engagement-file discipline."

**Tom:** "And to the engagement-file discipline."

The team drinks a third time. The food arrives. The conversation moves to the flight schedule, the weather forecast for Chicago (clear, mid-60s), the rental-car return logistics from Bush Intercontinental, and what Mike is going to write in his three-paragraph debrief to Raj on the Sunday-evening flight back. The conversation does not move to Dawn's vendor-side appearance or the Hill Country callback or the §10.40 substrate-agnostic clarifier's standards-memo language. The work is the work; tonight is dinner.

At 9:30 PM Sonya excuses herself for the night. Mike at 9:45. Tom is the last to leave at 10:15. He pays the bill.

In the elevator, he checks his phone. There is a text from Dawn: *Engagement closes. Sixteen-percent under budget; Margarethe's number on the budget reconcile was eighteen percent but the firm's reconcile lands at sixteen because Adelaide's framework-fit memo adds Friday hours.*

He types back: *Sixteen percent. — The Hill Country callback landed. Sonya is carrying her own engagement-file note to the Carolinas in three weeks. — Houston Friday.*

A pause. The phone buzzes back.

*Friday. — D.*

Tom puts the phone away. He thinks for a moment about engagement 30 at Northbridge eighteen years from now, when the §10.40 substrate-agnostic clarifier may not be a clarifier anymore — may be the base section, with the single-substrate language relegated to a deprecated paragraph at the bottom — and the cross-cloud byte-equality demonstration at six minutes may be the canonical-reference shape every junior auditor walks on Day 1 of their first audit. — He doesn't know whether the eighteen-year forward horizon will resolve that way. The engagement-file discipline doesn't require him to know.

He walks to his room.

## TesseraSeal sections exercised — engagement summary

Brazos Federal Bancshares × Mission Plaza Bank is the canonical institutional stakeholder entry for "cross-cloud chain consolidation as a routine M&A integration step" in spec §13. The engagement exercises the following spec sections in operational deployment:

### §10.40 — Cross-vendor chain-merge anchor with substrate-agnostic clarifier

**What Brazos × Mission Plaza operates today.** §10.40 is the load-bearing primitive for the cross-cloud chain consolidation at close. The substrate-agnostic clarifier paragraph — production-validated for the first time at this engagement — normates the substrate-pair-class abstraction: the cross-vendor chain-merge anchor is indifferent to whether the legacy bytes live on AWS S3 / AWS CloudHSM or Azure Blob Storage / Azure Key Vault Managed HSM or any other FIPS 140-2 Level 3+ HSM-rooted substrate. The §10.40 dispatch table lists known substrate pairs; the substrate-pair-specific reconciliation walker handles the AWS↔Azure pair in five minutes forty-eight seconds for the cross-anchor walk; the substrate-agnostic generic walker handles unknown substrate pairs through canonical-bytes byte-equality reconciliation.

**What the engagement confirms.** Cross-cloud chain consolidation operates as a routine integration step. The Mission Plaza pre-close AWS-resident chain and the Brazos post-close Azure-resident chain are byte-equal across the close boundary; the cross-cloud anchor binds them under one continuous evidentiary chain. The engagement is the canonical institutional reference for the §10.40 substrate-agnostic clarifier in production. The standards memo names §10.40 substrate-agnostic cross-vendor chain-merge anchor as production-validated.

**The Hill Country foresight cycle.** Dawn's engagement-file note from Hill Country Federal Credit Union three years and three weeks ago — *§10.40 anchor reads as routine on AWS-only. What happens when the substrate moves?* — is answered in production by this engagement. The note matured through the working-group sub-track across three review cycles before the substrate-agnostic clarifier shipped in a Herald release nine months before the engagement; the production exercise here is the first live validation.

### §10.39 — Institutional successor-attestation envelope (dual-CFO signature pair across substrates)

**What Brazos × Mission Plaza operates today.** §10.39 is operationally exercised across substrates: Mission Plaza CFO Hortense Marbury-Caldwell signed under AWS CloudHSM at 23:59:45 UTC Jan 31, 2026 (her final attestation before retirement); Brazos CFO Tobias Wendell-Kincaid signed under Azure Key Vault Managed HSM at 00:00:00.500 UTC Feb 1, 2026 (first attestation post-close). The §10.39 clarifier paragraph normates the substrate-agnostic treatment of `acquirer_hsm_key_fingerprint` — any FIPS 140-2 Level 3+ HSM public-key fingerprint is treated equivalently regardless of substrate.

**What the engagement confirms.** The dual-CFO signature pair verifies cross-substrate against both signers' published Ed25519 fingerprints under §10.5 attestation discipline. The §10.39 envelope is one continuous attestation across the cross-cloud boundary; the substrate-vendor-equivalent attestation registry composes both substrates' HSM custody under FIPS 140-2 Level 3 evaluation references.

### §10.41 — Chain-coverage map M&A temporal-slice partitioning

**What Brazos × Mission Plaza operates today.** §10.41 declares the three-partition map at close: pre-acquisition (4,892,346 entries on AWS), cut-over window (zero entries during the 31-second no-write band), post-cut-over (open on Azure). The November 2027 partition closure boundary is named and architected; the closure ceremony at November 15 will close the partition map into a single coverage region under the post-close partition.

**What the engagement confirms.** The three-partition map resolves cleanly; the cut-over window's no-write discipline holds. The November partition closure ceremony is architected per Steve's video composition recommendation: compose, not supersede — the February cross-anchor remains the institutional reference for the pre-close-to-post-close binding; the November closure adds the closure attestation as a sibling event. Hollis Trent-Mosley's runbook draft is the operational artifact; Adelaide's GC-side language closes by Friday.

### §10.42 — Backfill seal discipline at close

**What Brazos × Mission Plaza operates today.** §10.42 produced a chain-shaped envelope retroactively over Mission Plaza's six-month pre-close baseline at close. The legacy entries are byte-identical pre-seal and post-seal; the wrapper produces a single envelope root over the 4,892,346 pre-close entries; the envelope root is bound into the cross-anchor; the cross-anchor binds into Brazos's first post-close seal.

**What the engagement confirms.** The §10.42 backfill seal envelope root recomputes byte-equal; the legacy chain entries remain unmutated; the chain is continuous from August 2025 through today; the substrate boundary is one anchor inside the continuous chain.

### §10.36 — Late-arriving-entry seal discipline at the cut-over window

**What Brazos × Mission Plaza operates today.** §10.36 was armed across the 31-second cut-over window from 23:59:30 UTC Jan 31 to 00:00:01 UTC Feb 1, 2026. The operational runbook called for both institutions to stop writes from 23:59:00 to 00:00:30 UTC. The cross-anchor envelope binds `entries_received_in_window: 0` and `supplemental_seal_required: false`.

**What the engagement confirms.** The §10.36 supplemental-seal mechanism remained unexercised because no entries arrived in the window; the operational discipline at the cut-over was clean. The mechanism's existence preserves the chain's integrity claim against any future cut-over where entries do arrive in the window.

### §10.21 — Cross-vendor model-handover

**What Brazos × Mission Plaza operates today.** §10.21 carries two handover anchors at close: Insider-to-SFMC+Marketo composite for cross-channel marketing automation and AI personalization; Yello-to-Salesforce-FSC for account-opening journey orchestration. Each handover names the retired model classes, the successor model classes, the §10.21.4 vendor-version-registry lookup endpoint, and the cross-substrate pair.

**What the engagement confirms.** The §10.21 cross-vendor model-handover walks cleanly across both handover anchors. The Insider next-best-action model version that picked the December 8, 2025 rewards-program email variant resolves through Insider's published API in 2.1 seconds; the rendered-output byte-equality on the legacy email reproduces in nine seconds; the §10.21.4 lookup-endpoint retention commitment runs through 2031.

### §10.21.4 — Cross-vendor vendor-version-registry lookup

**What Brazos × Mission Plaza operates today.** §10.21.4 retains the legacy Insider and Yello vendor-version-registry lookup endpoints across the merger boundary. Insider's commitment is six years from version retirement (through 2031); Yello's commitment matches. The 2028 Marketo platform-upgrade question composes under §10.21.4 + §1.2: the chain entries' cryptographic binding is preserved under SHA-256 + RFC 8785; the vendor-version-registry contract is preserved under the vendor's commitment.

**What the engagement confirms.** The §10.21.4 retention commitments inherit through the merger boundary; the 2028 Marketo platform-upgrade question is operationally a non-event for the chain (per Steve's video confirmation); the bank doesn't need to retroactively re-anchor or re-bind legacy chain entries when the vendor's platform format changes.

### §10.11.1 — ECOA adverse-action family with prior-offer parent-linkage across the merger boundary

**What Brazos × Mission Plaza operates today.** §10.11.1's prior-offer parent-linkage fields (`prior_offer_run_id` / `prior_offer_seq`) with `prior_offer_status: linked` integrity-binding the linkage walks transitively across the merger boundary and across the substrate boundary. The pre-merger HELOC pre-qualification offer that pivoted to a post-merger HELOC approval reproduces in 1.4 seconds for reference resolution and 28 seconds for byte-equality on the legacy offer's rendered HTML.

**What the engagement confirms.** The §10.11.1 parent-linkage is substrate-agnostic by construction. The §10.40 cross-anchor closes the substrate-boundary integrity claim. The marketing-to-credit reference loop closes across the merger boundary in one transitive walk.

### §10.69 — Per-customer audit-trail subset disclosure across the merger boundary

**What Brazos × Mission Plaza operates today.** §10.69 produces one unified per-customer audit trail across the inheritance boundary per the §10.69 cross-tenant clarifier paragraph. The verifier traverses cross-tenant subtrees bound via §10.40 cross-anchors; the pre-Phase-A evidentiary substitute composes with the chain-side portions; the disclosure is honest about the merger boundary and the substrate boundary.

**What the engagement confirms.** Vionetta Halloran-Pace's §1033 disclosure (July 25, 2026) reconstructs 20 chain entries across two partitions, two substrates, two vendor stacks, and the pre-Phase-A evidentiary substitute trail in 22 seconds. The 22-second number on both Mission Plaza in November and Brazos × Mission Plaza today is the canonical-reference shape because the verifier dispatches against the same code path.

### §10.70 — Privileged-investigation overlay across the merger boundary

**What Brazos × Mission Plaza operates today.** §10.70's cross-tenant-investigation-handover discipline brought the open Mission Plaza SAR file into Brazos's AML platform at close under one continuous investigation chain. The §10.70 walks under cleared and non-cleared verifier modes both.

**What the engagement confirms.** The SAR investigation chain `sar-mp-to-brazos-2025q4-002` spans the merger boundary across 65 chain entries (18 pre-close, 47 post-close, 1 cross-anchor traversal). Non-cleared mode resolves the existence claim with content redacted (1.9 seconds); cleared mode resolves the full investigation content (3.4 seconds).

### §10.71 — Cross-institution Fedwire / ACH chain integrity

**What Brazos × Mission Plaza operates today.** §10.71 walks Fedwire chain integrity under the §10.21.3 voluntary registry that the Federal Reserve Bank of Dallas Wholesale Payments Office operates. Cross-merger-boundary wires walk transitively via cross-anchor + §10.71 parent-wire linkage + §10.21.3 registry attestation. Non-participating-counterparty wires emit `cross_anchor_unbound` documented residuals.

**What the engagement confirms.** Five Fedwires walked: three participating-counterparty post-close wires (4-6 seconds each), one cross-merger-boundary rebooked wire (6.2 seconds transitive walk), one non-participating-counterparty documented residual (1.8 seconds; originating-side integrity verified; counterparty-side unresolved per §10.71 operational-residual-marker discipline). Magdalena Forsberg-Aliyev of the Federal Reserve Bank of Dallas confirms Brazos × Mission Plaza as the canonical institutional reference for cross-merger-boundary Fedwire chain integrity.

### §10.13 — Evidentiary artifacts and SR 11-7 composition across cross-charter inheritance

**What Brazos × Mission Plaza operates today.** Brazos's Q2 2026 SR 11-7 model-risk binder composes Brazos's active credit-decisioning model lineage with Mission Plaza's retired legacy lineage under one quarterly governance framework. Both dictionary lineages remain traversable for retrospective reinvestigations under the seven-year retention floor.

**What the engagement confirms.** §10.13 composition spans both lineages with reconstruction-method hash byte-equal. The OCC post-merger examination cycle will read the same composition Brazos walked at March's Texas Department of Banking state-charter cycle.

### §10.5 — HSM custody at FIPS 140-2 Level 3+ across substrate-vendor-equivalent attestations

**What Brazos × Mission Plaza operates today.** §10.5 holds AWS CloudHSM and Azure Key Vault Managed HSM side-by-side in the substrate-vendor-equivalent attestation registry. Both attestations carry FIPS 140-2 Level 3 evaluation references.

**What the engagement confirms.** The substrate-vendor-equivalent treatment composes the AWS-side and Azure-side HSM custody under one §10.5 acceptance. The §10.5 clarifier paragraph normates the substrate-vendor-equivalent attestation discipline.

### §10.19 — Chain-coverage boundary documentation (inherited)

**What Brazos × Mission Plaza operates today.** §10.19's `pattern_2_partial_coverage_with_named_scope` declaration from Mission Plaza's pre-close partial deployment is inherited into the pre-acquisition partition of the §10.41 three-partition map. The Insider quarterly campaign-history export is the named evidentiary substitute for the four-year pre-Phase-A Mission Plaza Insider footprint.

**What the engagement confirms.** The §10.19 declaration carries across the merger boundary; the pre-Phase-A evidentiary substitute resolves cleanly in §10.69 per-customer disclosures (sampled at 22 seconds on Vionetta's case). The §10.19 boundary documentation discipline composes with the §10.41 partition-map discipline.

## Engagement debrief — Raj's voice (Lead Auditor, post-engagement)

> "Engagement 31. Brazos Federal Bancshares × Mission Plaza Bank. Houston operations center, Texas. Three days, mid-September 2027, ~19 months post-close. Cross-cloud chain consolidation between Mission Plaza's pre-close AWS-resident chain and Brazos's post-close Azure-resident chain. First MMPWorks-vendor-side appearance for Dawn as lead TesseraSeal liaison; first production exercise of the §10.40 substrate-agnostic clarifier.
>
> "Brazos × Mission Plaza is the canonical institutional stakeholder entry for 'cross-cloud chain consolidation as a routine M&A integration step' in spec §13. Margarethe Sundberg-Vallejo is the institutional reference engineer for the §10.41 partition-map discipline and the post-merger integration audit shape; Donovan Eastlake-Boudreaux is the inherited Mission Plaza reference engineer; Renata Whitley-Aguilar is the institutional reference engineer for the §10.21 cross-vendor marketing-stack handover; Hollis Trent-Mosley is the institutional reference engineer for the §10.41 partition closure ceremony architecture; Adelaide Carrowmore-Finch is the GC reference engineer for the §10.40 + §10.39 + §10.42 + §10.41 composition; Padraic Calhoun-Reidy is the BSA reference engineer for §10.70 cross-tenant-investigation-handover. Magdalena Forsberg-Aliyev at the Federal Reserve Bank of Dallas Wholesale Payments Office is the §10.21.3 voluntary-registry reference for cross-merger-boundary Fedwire chain integrity.
>
> "Nine spec-section confirmations across three days; one Nit (cross-charter retention policy framework-fit memo not yet produced; Adelaide drafts by Friday); zero Gaps; zero Partials. Engagement closes 16% under budget after Adelaide's Friday hours are reconciled. The cross-cloud byte-equality demonstration at five minutes forty-eight seconds is the architecture headline; the Insider legacy-export byte-equality reconciliation at six minutes twelve seconds resolves Easton Wadsworth's seven-month drift-window question; the Variant B UDAAP customer-subset reconstruction at five minutes fifty-four seconds with customer-by-customer restitution-receipt linkage walked per chain is the operational test that justified the deployment to Brazos's board.
>
> "Dawn appeared at lunch on Day 1 in her MMPWorks vendor-side role, on the engagement-letter schedule, under the spousal-disclosure paragraph of the firm's conflict-of-interest protocol. The ninety-second personal conversation between Tom and Dawn at the lunch table closed the personal-arc question that Story 20 opened at the November wedding; the team handled the moment with the discipline that defined Dawn's time as Lead. The four-thirty moment on Day 1 — Renata Whitley-Aguilar's *if a Mission Plaza legacy customer sues Brazos three years from now over a pre-merger marketing promise we didn't honor, can we prove what they were actually told* — closed with Dawn's answer that the chain spans every relevant event from August 2025 forward; her two-year-and-eleven-month-old engagement-file note from Hill Country (*§10.40 anchor reads as routine on AWS-only; what happens when the substrate moves?*) is answered in production by today's engagement. The room read it as the work compounding, not as a personal triumph; Tom's microscopic nod was the only acknowledgment.
>
> "Steve appeared by video bridge on Day 3 at 13:30 CDT for eighteen minutes — two minutes under window — to answer the November partition closure ceremony architecture composition question (compose, not supersede) and the 2028 Marketo platform-migration posture question (operationally a non-event for the chain). Tom logged the appearance as the second appearance under the spousal-disclosure paragraph; the first was at the Hill Country follow-up working-group sub-track call in June.
>
> "Sonya is on her ninth engagement with the firm. Her §10.21 vendor-opaque-render wishlist note from Mission Plaza in November is still in her jacket pocket. Her next engagement — a Carolinas community bank's §10.21 + §10.21.4 readiness pass — is in three weeks; she carries the note in case the marketing-AI vendor at the Carolinas stack has the opaque-render shape. The horizon for the note's actionability is three weeks or three years; the discipline is the same.
>
> "Heather lifts the §10.40 substrate-agnostic clarifier's production-validated canonical-reference shape into the standards memo by Friday. The spec body picks up the engagement reference at the next quarterly review. The standards memo's institutional reference is Brazos × Mission Plaza; the production-validated metric is the five-minutes-forty-eight-second byte-equality reconciliation across 4.89 million pre-close chain entries; the abstract pattern is the §10.40 substrate-agnostic primitive.
>
> "The work compounds. The seat has changed; the chain doesn't. — The engagement-file discipline is the long-shape discipline; the question matures; the spec catches up; the engagement exercises the answer. Today closes the long-shape on Hill Country. The next long-shape is Sonya's vendor-opaque-render note; that's the horizon for the next foresight cycle."

## Cross-references

- **Spec sections exercised**: §10.5 (HSM custody substrate-vendor-equivalent), §10.11.1 (ECOA adverse-action family with prior-offer parent-linkage across substrate boundary), §10.13 (SR 11-7 binder composition across cross-charter inheritance), §10.17 (partition-ceremony attestation), §10.19 (chain-coverage boundary documentation inherited into §10.41 partition map), §10.21 (cross-vendor model-handover across substrates), §10.21.3 (Federal Reserve Bank of Dallas voluntary cross-institution-anchor registry), §10.21.4 (cross-vendor vendor-version-registry lookup retention across merger boundary), §10.22 (redaction-discipline schema-template family at production-discipline registry), §10.36 (late-arriving-entry seal discipline at cut-over window; armed unexercised), §10.39 (institutional successor-attestation envelope with dual-CFO signature pair across substrates), §10.40 (cross-vendor chain-merge anchor with substrate-agnostic clarifier; production-validated), §10.41 (chain-coverage map M&A temporal-slice partitioning with November partition closure architecture), §10.42 (backfill seal at close), §10.69 (per-customer audit-trail subset disclosure across merger boundary via cross-tenant clarifier paragraph), §10.70 (privileged-investigation overlay across merger boundary), §10.71 (cross-institution Fedwire / ACH chain integrity under §10.21.3 registry).
- **Stakeholder navigation**: §13 stakeholder for "cross-cloud chain consolidation as a routine M&A integration step" — new canonical stakeholder entry. Brazos Federal Bancshares × Mission Plaza Bank named; Margarethe Sundberg-Vallejo (Brazos CAE), Donovan Eastlake-Boudreaux (legacy Mission Plaza CAE), Renata Whitley-Aguilar (Brazos CMO), Hollis Trent-Mosley (Brazos M&A integration lead), Adelaide Carrowmore-Finch (Brazos GC), Padraic Calhoun-Reidy (Brazos BSA officer) named as institutional reference engineers across §10.21 / §10.39 / §10.40 / §10.41 / §10.42 / §10.69 / §10.70 lanes. Magdalena Forsberg-Aliyev (Federal Reserve Bank of Dallas Wholesale Payments Office) named as the §10.21.3 voluntary-registry reference. Calliope Wynn-Devereaux (Insider PM, continuing from Mission Plaza Story 20) named as the §10.21.4 vendor-engineering counterpart inheriting through the merger boundary.
- **Auditor stories**: this engagement is the first under Raj's Lead Auditor tenure for the firm's post-Mission-Plaza succession; the first under the spousal-disclosure paragraph of the firm's conflict-of-interest protocol after the third-party-vendor frame closed at Mission Plaza in November 2026; the first MMPWorks-vendor-side appearance for Dawn; the first production exercise of the §10.40 substrate-agnostic clarifier. The engagement-file note Dawn filed at Hill Country Federal Credit Union (Story 12, three years prior) is answered in production by this engagement. Sonya's §10.21 vendor-opaque-render engagement-file note (Story 20, ten months prior) remains in her jacket pocket, awaiting its own actionability horizon. The next Mission Plaza engagement (the Phase B marketing-surface extension confirmation, three months out from today) opens under Raj's continued Lead Auditor tenure with Dawn as MMPWorks vendor-side liaison and Sonya as the audit-side authoring auditor on the Phase B working-group sub-track inheritance.

The confirmation memo, the §10.41 partition closure memo, and the cross-cloud-anchor confirmation appendix are filed under Brazos Federal Bancshares's compliance-track records. The partner-letter close-out is filed under the firm's engagement-history records as engagement 31, signed by Raj Kothari as Lead Auditor, Tom Beaumont as engagement-letter manager, Margarethe Sundberg-Vallejo as institutional CAE, Donovan Eastlake-Boudreaux as inherited legacy-CAE, Adelaide Carrowmore-Finch as institutional GC, and Brigitte (Mission Plaza IA team) as the legacy-institution internal-audit signature on video. The spousal-disclosure-paragraph appearance log records Steve's eighteen-minute appearance on Day 3 as the second appearance under the paragraph. The standards memo's institutional reference is Brazos × Mission Plaza; Heather lifts the canonical-reference shape into the standards memo by Friday.

