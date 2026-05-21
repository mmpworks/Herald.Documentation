# Story 21 — Brazos Federal Bancshares × Mission Plaza Bank (Texas regional-acquires-community merger, cross-cloud AWS↔Azure chain consolidation, marketing-data load-bearing)

**Story file:** `docs/auditor-stories/21-brazos-federal-mission-plaza.md`
**Engagement type:** Three-day post-close integration audit at the Texas regional acquirer ~7 months after merger close; first vendor-side Dawn appearance as MMPWorks's lead TesseraSeal liaison
**Posture going in:** Brazos Federal has TesseraSeal in production for 15 months across all customer-facing surfaces on Azure (Herald.Core.Azure, multi-region per §10.15); Mission Plaza had partial TesseraSeal for six months pre-close on AWS (Herald.Core.Aws, AI-decisioning surface plus the marketing-surface Phase A from Story 20); the cross-vendor anchor was placed at close at 00:00:01 UTC Feb 1, 2026 binding Mission Plaza's full pre-close chain into Brazos's Azure chain; integration runs through November 2026; brand transition in progress
**Outcome posture:** Confirmation; exercises §10.39-§10.42 (institutional succession) + §10.40 substrate-agnostic cross-vendor chain-merge anchor + §10.21 cross-vendor model-handover across the cloud boundary; the canonical institutional reference for cross-cloud chain consolidation as a routine operation

## Type of audit
Three-day on-site at Brazos Federal's Houston operations center, mid-September 2026, ~7 months post-close and ~6 weeks before full operational integration to the Brazos brand. The audit confirms the chain holds across (1) the Mission Plaza-AWS to Brazos-Azure cross-cloud anchor placed at close, (2) the cross-vendor marketing-stack handover from Insider + Yello to Salesforce Marketing Cloud + Marketo Engage, (3) the brand-transition campaign window with its UDAAP exposure on rebrand-period customer communications, and (4) the marketing-data-to-credit-decision linkage across legacy-and-post-close customer journeys. Regulators in scope: OCC (lead, both legacy and acquired charters), CFPB (UDAAP on rebrand-period communications + §1033 disclosure across the merger boundary), Texas Department of Banking (state-chartered Mission Plaza legacy charter).

## Interested parties (spec readers)
- **OCC examiner (lead)** — Post-merger examination opens 60 days after this engagement; consumes the spec-section confirmation memo as the first read on the cross-cloud and cross-vendor anchors
- **OCC consumer-protection examiner / CFPB** — UDAAP exposure on the rebrand-period campaign window; §1033 disclosure spanning the merger boundary
- **Texas Department of Banking examiner** — State-chartered Mission Plaza legacy charter; integration-period oversight
- **Brazos Chief Audit Executive** — Integration veteran (Brazos's third acquisition under her tenure); consumes the cross-cloud and cross-vendor confirmation as the load-bearing integration assurance
- **Mission Plaza legacy CAE** — Now reports to Brazos's CAE under integration; was the institutional sponsor of the partial deployment audited in Story 20; this is the engagement where his pre-close institutional choices pay off
- **Brazos Chief Marketing Officer** — Called MMPWorks 60 days before close, asked for an integration plan, got one; invited Dawn to attend the engagement in her vendor capacity
- **Mission Plaza legacy CMO / Director of Brand Transition** — Marketo+Insider stack person; has carried integration-period anxiety about whether the pre-close marketing data is recoverable byte-equal under audit pressure
- **M&A integration program lead (Brazos)** — Owns the November 2026 full-integration cut-over; consumes the §10.41 partition closure memo
- **Counterparty bank (Federal Reserve Bank of Dallas)** — Wholesale Payments Office; operates the §10.21.3 voluntary cross-institution-anchor registry referenced under §10.71; cross-institution wire-handover registry observer on the video bridge
- **General Counsel** — Pre-merger-marketing-promise litigation posture; consumes the cross-cloud byte-equality demonstration as evidentiary discipline
- **CFPB UDAAP attorney** — The 47,000-email Feb 4 rebrand-period misstep is in the chain; restitution receipts and customer lists pull in six minutes
- **Standards-body reviewer** — Cross-cloud byte-equality demonstration is the canonical-reference shape for §10.40's substrate-agnostic clarifier. The standards memo follows the engagement
- **MMPWorks vendor-side liaison (Dawn)** — First vendor-side appearance; technical lead on the cross-cloud anchor architecture
- **Verifier implementer** — Cross-cloud dispatch verifier on the AWS↔Azure boundary

## Top spec sections used
- **§10.40** — Cross-vendor chain-merge anchor across substrates (AWS S3 / AWS CloudHSM ↔ Azure Blob / Azure Key Vault Managed HSM); Mission Plaza's full pre-close chain hash-anchored at close and bound into Brazos's Azure chain. Substrate-agnostic per the §10.40 clarifier paragraph — the byte-hash binding is indifferent to substrate. Byte-equality demonstration in six minutes is the headline
- **§10.39** — Institutional successor-attestation envelope; dual-signature pair (Mission Plaza CFO + Brazos CFO) at close
- **§10.41** — Chain-coverage map M&A temporal-slice partitioning (pre-acquisition / cut-over window / post-cut-over); November 2026 full-integration cut-over is the scheduled closure boundary
- **§10.42** — Backfill seal discipline at close; one-time seal at 00:00:01 UTC Feb 1, 2026 producing chain-shaped envelope retroactively over Mission Plaza's pre-close baseline
- **§10.21** — Cross-vendor model-handover; Insider→Salesforce Marketing Cloud and Marketo Engage→Salesforce Marketing Cloud handovers at the marketing-stack boundary
- **§10.11.1** — `audit.ecoa.adverse_action.*`; the pre-merger HELOC pre-qualification → post-merger HELOC approval pivot
- **§10.69** — Per-customer audit-trail subset disclosure across the merger boundary; per the §10.69 cross-tenant-disclosure clarifier paragraph, the verifier traverses cross-tenant subtrees bound via §10.40 cross-anchors, producing one unified per-customer audit trail across the inheritance boundary; CFPB §1033 right
- **§10.71** — Cross-institution Fedwire / ACH chain integrity; registry-discovery cross-anchor at the Federal Reserve Bank of Dallas

## All cited spec sections
- **§0.5.1** — Three-paragraph elevator pitch for OCC executive orientation
- **§1.1** — Daubert four-factor grounding; cross-cloud byte-equality reproduction is the new canonical Daubert reproduction case
- **§1.2** — Epistemic scope
- **§4** — Four primitives; cross-cloud anchors live at the §4.3 HSM-rooted root signature layer with one signature on each substrate's Merkle root and the cross-anchor binding them
- **§4.2** — Daily Merkle seal cadence; Mission Plaza's last pre-close seal on AWS CloudHSM and Brazos's first post-close seal on Azure Key Vault Managed HSM
- **§4.3** — HSM-rooted root signature on both substrates; cross-cloud anchor binds the two roots
- **§7** — Twelve-step verifier procedure; cross-cloud dispatch path
- **§10** — Operational requirements
- **§10.5** — HSM custody at FIPS 140-2 Level 3+; both AWS CloudHSM (Mission Plaza side) and Azure Key Vault Managed HSM (Brazos side) attestation
- **§10.11.1** — ECOA adverse-action family
- **§10.13** — Evidentiary artifacts and SR 11-7 composition
- **§10.15** — Multi-region resilience on Azure side
- **§10.17** — Partition-ceremony attestation
- **§10.19** — `audit.external_artifact.*` family; reused for the Marketo 2.7-TB campaign-history export hash-anchoring
- **§10.21** — Cross-vendor model-handover at the marketing-stack boundary
- **§10.22** — Redaction discipline
- **§10.36** — Late-arriving-entry seal discipline; named explicitly to cover the brief cut-over window between Mission Plaza's last AWS seal (23:59:30 UTC Jan 31) and Brazos's first Azure seal (00:00:01 UTC Feb 1). Confirmed no chain entries arrived in the gap; the §10.36 supplemental-seal mechanism would have absorbed any that did
- **§10.39** — Institutional successor-attestation envelope; `acquirer_hsm_key_fingerprint` substrate-agnostic per §10.39 clarifier
- **§10.40** — Cross-vendor chain-merge anchor; the engagement's signature primitive, exercised across substrates per §10.40 substrate-agnostic clarifier
- **§10.41** — Chain-coverage map M&A temporal-slice partitioning
- **§10.42** — Backfill seal discipline at close
- **§10.69** — Per-customer disclosure across the merger boundary
- **§10.70** — Privileged-investigation overlay; one SAR-filing chain spans the merger boundary and is walked under cleared and non-cleared verifier modes
- **§10.71** — Cross-institution Fedwire / ACH; Federal Reserve Bank of Dallas Wholesale Payments Office operates the §10.21.3 voluntary registry; cross-institution chain integrity verified for outbound Fedwires
- **§13** — Stakeholder navigation; "Texas regional acquirer × Texas community-bank target, cross-cloud chain consolidation, marketing-data load-bearing, mid-integration audit" is the canonical institutional reference

## Synopsis

### Audit activity
Brazos Federal Bancshares is a Houston-HQ Texas regional bank, $45B consolidated assets, Texas + Oklahoma footprint, OCC-supervised, TesseraSeal in production for 15 months on Azure (Herald.Core.Azure with multi-region resilience per §10.15; Azure Key Vault Managed HSM for the root signature). Mission Plaza Bank was a San Antonio-HQ community bank, $3.2B assets at close, acquired by Brazos in a $269M cash-and-stock deal that closed Feb 1, 2026 — full operational integration scheduled for November 2026. Mission Plaza ran a Jack-Henry-centric community-banking stack (Banno, Symitar NetTeller, JHA Payment Solutions, Yello, Insider, ASP.NET, Splunk, AWS-resident) with partial TesseraSeal on Herald.Core.Aws across the AI-decisioning surface and the Phase-A marketing surface stood up in the six months pre-close (per the Story-20 scope-expansion memo). Brazos runs Fiserv DNA core banking, Q2 Holdings for digital banking, Salesforce Financial Services Cloud for CRM, Salesforce Marketing Cloud + Marketo Engage for marketing automation, Datadog for observability.

Day 1 morning opens with both CAEs in the room. Tom's standard four questions; the legacy-side CAE pauses on the cross-charter retention policy fourth question; note logged. Raj — Lead Auditor since Dawn's transition to MMPWorks eight months ago — names eleven prior contexts in the drive-in monologue and slots this one: *"Post-merger integration with marketing-data as load-bearing. Cross-cloud anchor at the close boundary. Closest precedent is Atrio's coordinated-examiner-room, but here the chain crosses a vendor-merger boundary inside the acquiring bank itself and crosses two cloud substrates inside the audit window."* The cross-cloud framing is treated as routine — the team's calm familiarity with the operation is itself a form of evidence.

Day 1 mid-morning walks the §10.40 cross-cloud anchor end-to-end. Mission Plaza's last pre-close Merkle seal was sealed under AWS CloudHSM at 23:59:30 UTC Jan 31; Brazos's first post-close seal was sealed under Azure Key Vault Managed HSM at 00:00:01 UTC Feb 1; the cross-anchor binds the two roots in a single attestation envelope (§10.39 + §10.40 + §10.42 composition). Chen pulls the receipts; the verifier returns PASS on the cross-cloud dispatch in six minutes. Cross-cloud is the new same-cloud. The chain doesn't care where the artifacts live.

Day 1 afternoon walks the marketing-stack handover under §10.21. Five customer journeys traced end-to-end across the merger and stack boundary; the load-bearing case is a customer who received a pre-merger Mission Plaza HELOC pre-qualification email at 6.875% on Jan 17 (under Insider's next-best-action under Mission Plaza's pre-close stack), a post-merger Brazos rebrand email on Feb 4 ("Same great service, new name"), and then a HELOC application on May 22 approved at 7.250% under a different product structure (Salesforce Marketing Cloud + Salesforce FSC + Brazos's underwriting). All three marketing events chain through; the AI underwriting decision binds the prior marketing offer via §10.11.1's `audit.ecoa.adverse_action.prior_offer_run_id` / `prior_offer_seq` parent-linkage fields, with `prior_offer_status = "linked"` integrity-binding the linkage; the verifier traverses transitively across §10.21 model-handover and §10.40 cross-anchors to reach the pre-close Mission Plaza marketing-event entry.

Lunch on Day 1: Dawn arrives at noon at the joint invitation of Brazos's CMO and the audit team — pre-arranged, on the schedule, fully disclosed in the engagement letter. She has met Brazos's CAE twice in the last quarter in vendor capacity. The conversation for 90 seconds is personal — Tom asks about Steve, asks about the house — then everyone moves on. Dawn opens her laptop and pulls up MMPWorks's view of the cross-cloud anchor architecture. Elena moves a chair so Dawn can see.

Day 1 afternoon late: Dawn walks Mission Plaza's legacy CMO and Chen through the Marketo legacy-anchor: 2.7-TB tar.gz of campaign history, customer lists, A/B variant data, send-time logs, click-stream telemetry. Hash committed at close. Mission Plaza's legacy CMO has been carrying anxiety for seven months — was the hash actually what the Marketo backup contained, or was there drift in the 47 minutes between Marketo's last write and the close timestamp? Chen pulls the Marketo audit-log receipt: last write at 23:42:18 UTC Jan 31; hash computed at 23:59:30 UTC; seal at 00:00:01 UTC Feb 1. No drift window. Mission Plaza's legacy CMO exhales for the first time in seven months.

Day 2 morning walks the rebrand-period UDAAP scene. On Feb 4 the rebrand campaign fired to ~340,000 Mission Plaza legacy customers; one variant accidentally referenced Mission Plaza's old fee schedule ("free overdraft protection") which Brazos does not offer at zero cost. Campaign-stop hit at 14 minutes; 47,000 emails had already sent. The CFPB settlement closed in March with a customer-restitution package. The audit question today: can the bank produce the exact list of 47,000 customers who received the misleading variant, the exact text they received, the exact timestamp, and the restitution receipt linkage? Mike pulls all four in six minutes; verifier passes. The CAE: *"This is why we did the deployment."*

Day 2 afternoon walks §10.69 per-customer disclosure across the merger boundary; one §1033 disclosure spans both pre-close Insider/Mission Plaza era and post-close Salesforce/Brazos era and verifies in 22 seconds against ~14,000 chain entries. Day 2 also covers §10.70 with one SAR-filing chain that spans the merger boundary, walked under both cleared and non-cleared verifier modes.

Day 3 morning walks §10.71 with the Federal Reserve Bank of Dallas Wholesale Payments Office on video bridge; five wires walked including one `cross_anchor_unbound` documented residual at a non-participating counterparty bank. Day 3 afternoon: the §10.41 partition closure memo is drafted for the November 2026 full-integration cut-over; the partition map will close cleanly under the same composition (§10.39 + §10.42) used at the Feb 1 close. Steve joins by video bridge for twenty minutes mid-afternoon for one specific technical question about how the §10.21 surface handles a future Marketo platform upgrade in 2027; he walks the room through §10.21 + §10.40 + the platform-migration path; he signs off; he logs off.

### The 4:30 PM moment
Brazos's CAE asks Dawn directly, in her vendor-liaison role: *"If a Mission Plaza legacy customer sues Brazos three years from now over a pre-merger marketing promise we didn't honor, can we prove what they were actually told?"*

Dawn's answer (concrete, sober, the pattern preserved across the seat change): the Marketo legacy data is hash-anchored at close; the post-close marketing events are in Brazos's TesseraSeal proper; the AI underwriting decision references both; the chain spans every relevant event from 2024 forward; three-year window is well inside retention; the cross-vendor anchor is the load-bearing piece; the byte-equality demonstration this morning reproduces in court. She then names the engagement-file note she filed at Bishop Crescent Federal Credit Union three years earlier — *"works on one substrate. what happens when the substrate moves?"* — and observes that today is the first production engagement that exercises §10.40's cross-cloud extension. The chain doesn't care which cloud the artifacts live on. The substrate-trust boundary is just another anchor.

Tom's microscopic nod is the only acknowledgment. Raj's expression doesn't change. The room reads the moment as the work compounding.

### How the spec was used
- **§10.40** — Mission Plaza's AWS-resident chain hash-anchored at close, bound into Brazos's Azure-resident chain via the substrate-agnostic cross-vendor chain-merge anchor primitive; byte-equality reproduction in six minutes; cross-cloud is operationally indistinguishable from same-cloud, per the §10.40 clarifier paragraph
- **§10.39 / §10.42** — Successor-attestation envelope with dual-signature pair (Mission Plaza CFO + Brazos CFO) under Brazos's Azure HSM; backfill seal at close producing chain-shaped envelope over Mission Plaza's pre-close baseline; the §10.39 envelope's `acquirer_hsm_key_fingerprint` field carries the Azure Key Vault Managed HSM public-key SHA-256 — substrate-agnostic per the §10.39 clarifier paragraph, since any FIPS 140-2 Level 3+ HSM's public-key fingerprint is treated equivalently regardless of substrate
- **§10.41** — Three-partition coverage map (pre-acquisition / cut-over window / post-cut-over); November 2026 closure memo drafted on Day 3
- **§10.21** — Insider→Salesforce Marketing Cloud and Marketo Engage→Salesforce Marketing Cloud cross-vendor handovers walked end-to-end
- **§10.11.1** — Pre-merger HELOC pre-qualification → post-merger HELOC approval ECOA-adverse-action pivot in the chain
- **§10.69** — Per-customer disclosure spans the merger boundary in one unified trail
- **§10.70** — SAR-filing chain that spans the merger boundary walked under cleared and non-cleared verifier modes
- **§10.71** — Cross-institution wire chain integrity verified; Federal Reserve Bank of Dallas Wholesale Payments Office attests via the §10.21.3 voluntary registry it operates
- **§10.11.1 prior-offer parent-linkage** — The HELOC pre-merger-to-post-merger pivot is bound via §10.11.1's `prior_offer_run_id` / `prior_offer_seq` parent-linkage fields on the credit-decision chain entry; the prior marketing offer is itself a chain entry under the legacy Mission Plaza §10.21 model-handover-anchored marketing-AI inference, hash-anchored at close via §10.40 and reachable from the post-close credit decision through the parent-linkage

### Results
Cross-cloud chain consolidation operates as a routine integration step. The Mission Plaza AWS pre-close chain and the Brazos Azure post-close chain are byte-equal across the close boundary; the cross-cloud anchor binds them under one continuous evidentiary chain. The marketing-data thread is load-bearing — the rebrand-period 47,000-email UDAAP scene reproduces in six minutes, the HELOC pre-merger-to-post-merger pivot reproduces in the same window, the Marketo legacy CMO's seven-month anxiety resolves in six minutes. One Nit (the legacy-side CAE's cross-charter retention policy gap); zero Gaps; zero Partials. Engagement closes 18% under budget.

Brazos × Mission Plaza becomes the canonical institutional reference for cross-cloud chain consolidation as a routine M&A integration step. The standards memo following the engagement names §10.40 substrate-agnostic cross-vendor chain-merge anchor as production-validated. Dawn's two-year-old Bishop-Crescent nagging question is answered in production. The marketing thread is normalized as load-bearing audit content rather than background — the chain extends across the marketing-data boundary because the spec says it does, and Brazos built it that way because the regulators were going to ask.
