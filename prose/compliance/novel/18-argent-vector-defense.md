# 18 — Argent Vector Defense Systems

> A US defense-electronics prime-tier-1 supplier, ~$1.4B revenue, ~4,200 employees, headquartered Plano, Texas. Designs and integrates AESA radar systems for Lockheed F-35 sustainment and Northrop B-21 development. The next-generation R&D program is **TALON-X**, an attritable autonomous UAS — a stealthy wingman drone with on-board AI target-classification, an EO/IR-and-SAR sensor payload, a Type-1 cross-domain crypto module enforcing red/black separation between the classified sensor / inference side and the unclassified comms uplink, and a TEMPEST-qualified flight computer. *(Red/black separation is the cleared-environment discipline of physically and procedurally isolating "red" — plaintext classified information — from "black" — encrypted-or-unclassified information that may travel on shared infrastructure. The canonical reference is NSTISSAM TEMPEST/2-95 and CNSSI 7000; the practical implication is that wires, racks, power supplies, and software components are color-coded and the boundary is gated by NSA-evaluated cross-domain devices.)* The TALON-X program is in RDT&E phase 2; first flight is in eleven weeks; the equipment around the AI platform — the cross-domain crypto module, the TEMPEST-shielded sensor enclosure, the dedicated red-side HSM, the black-side downlink crypto — is being qualified now. Cleared facility under DD-254 with a TS/SCI annex; CMMC 2.0 Level 3 self-certification due in eight weeks. **TesseraSeal in production for 7 months on the AI radar-target-classification model path on F-35 sustainment; the hardware supply chain itself is NOT in chain today, and the TALON-X R&D program needs the same chain coverage extended over the autonomous-drone edge-AI surface plus the red/black separation discipline that today's chain doesn't address.** Two-day engagement; Dawn is in Boston on a long-planned vacation with her niece Kayla and Kayla's husband Hassan after the birth of their daughter; Tom is running the team. Sonya — newcomer to the team, ex computer-logistics manager from Howard-Pace's federal-government division in Houston — joins the engagement as her first day with the firm. The wishlist that emerges is the **hardware-supply-chain integrity** family plus the **red/black separation** addendum — §10.56 hardware bill-of-materials chain, §10.57 firmware-attestation across supplier tiers, §10.58 component cryptographic identity primitive, §10.59 RMA / sustainment chain re-entry discipline, §10.60 anti-counterfeit cross-anchor, §10.61 CMMC 2.0 / NIST 800-171 / NIST 800-161 regulator-pack overlay, §10.62 red/black separation chain integrity (introduced by the TALON-X R&D program).

## The team and the day

The full eight on-site, with Sonya making nine and Dawn out: Tom (lead this week), Raj, Elena, Mike, Diana, Luis, Chen, **Sonya**. Argent Vector's Plano campus is a low-slung tan-brick building with no signage, ringed by a perimeter fence, two badging vestibules, and a separate cleared-area annex behind a second fence. The team flies into DFW the night before and stays at the Marriott in Legacy West.

Argent Vector's VP of Compliance & Cyber is **Colonel (ret.) Brent Kazmierski**, ex-Air Force acquisition, second career — fifteen years at Argent Vector. The chief engineering officer is **Asha Iyengar**, ex-Raytheon, runs the F-35 / B-21 radar program. The chief supply-chain officer is **Pearline Voss-Marchetti**, ex-Boeing Defense, twenty-eight years in defense logistics. The TALON-X program engineering lead is **Major (ret.) Devon Calloway-Ipsen**, ex-USAF UAS test pilot, second career — six years running attritable-autonomous-systems R&D at Argent Vector. The TALON-X cross-domain-crypto qualification lead is **Stavroula Marinakis-Dell**, ex-NSA cryptographic-product-evaluation, eighteen years before joining Argent Vector last spring.

TesseraSeal sent two on-site for the engagement: **Steve** (principal designer) and **Kevin** (the devil's-advocate review-pass engineer Dawn met by name at Northbridge). With Dawn on PTO, the firm's recusal-protocol vendor-side technical-engagement constraint is naturally satisfied; Steve and Kevin are present without the firm's recusal-cleared escalation invocation. Tom logged the engagement-letter authorship boundaries with the firm's general counsel before flying out: Mike authors vendor-architecture, Sonya authors hardware-supply-chain, Tom authors audit-procedure, the firm holds the recusal-protocol assignment template intact for when Dawn returns.

## The drive-in monologue — orientation in a Texas SUV

```
6:35 AM. Rental Suburban, Sam Rayburn Tollway westbound. Tom driving.
                          Sonya in the passenger seat, second-day-on-the-job calm.
                          Mike in the second row with his laptop.
                          Day 1 of Sonya's first engagement.
```

**Tom:** "Sonya, the orientation talk you didn't get yet. Seventeen prior engagements, Dawn's pattern. The drive-in is where the lead reviews context with whoever is in the seat next to them. Today the lead is me; the seat next to me is yours. So talk to me about Howard-Pace."

**Sonya:** "Howard-Pace. Federal-government division. Houston. Twenty-two years. I started on the loading dock in '04 — first-line warehouse supervisor — and finished as senior director of computer logistics for the federal vertical. Forty million units a year through my organization at peak. Government, military, law-enforcement, intelligence community. We shipped to every classified facility in the United States and several outside it."

**Tom:** "And the chain-of-custody you ran."

**Sonya:** "Paper. Pallet stickers. RFID at the gate. SAP at the desk. Ten thousand line items per day in our mid-2010s peak. Thirty-seven sub-tier suppliers we audited annually. Two hundred and four supplier facilities we'd been inside. We knew where every chip was made. We didn't always know what was inside the chip."

**Tom:** "And the AI side?"

**Sonya:** "I came late to AI. Last three years at Howard-Pace was the federal-AI-procurement push. We shipped GPU servers to a lot of three-letter agencies. The conversation always turned on whether the model the agency deployed was the model the agency procured. The hardware was easy by then; the software was the part that scared people."

**Tom:** "And the spec we're confirming today?"

**Sonya:** "I read the audit-procedures and twelve of the prior stories on the flight last night. §0.6 normates the contextual-help URL convention — each §10.x section may reference its companion-repo scenario walkthrough, and URL stability is required across PRD revisions, so the stories I read on the flight cite the same §10.x anchors today's wishlist will surface. The chain handles the AI-decision-time integrity claim. What it doesn't handle yet — and what Argent Vector cares about — is the chip in the radar. The chip's bill of materials. The firmware that loaded on it. Where it was tested. Where it was returned and re-tested. Whether the part the prime received is the part the prime expected."

**Tom:** "That's exactly the wishlist surface today. Hardware supply chain. CMMC 2.0 Level 3 in eight weeks. DCMA on-site every six months. DARPA SHIELD overlap on three of their programs. Steve and Kevin from TesseraSeal are in the building today — Dawn's on PTO in Boston, so the recusal-protocol vendor-engagement constraint is naturally clear. They're here because TesseraSeal is positioning the next spec section family on hardware supply chain and Argent Vector is the canonical institutional reference if the engagement surfaces it."

**Mike** (from the back seat, looking up from his laptop): "It never is."

**Sonya:** "It never is?"

**Tom:** "Dawn's line. *Whether the audit will be clean.* Sometimes she means it as the seventeen-prior-engagements view of pessimism; sometimes she means it as the wishlist-surface invitation. Today it's the second sense. The chain handles AI inference. The chain doesn't handle the chip yet. Argent Vector knows it. We confirm what's in chain, and we propose §10.56 onward for what's not."

**Sonya:** "It never is."

The Suburban turns onto the Argent Vector access road. The perimeter fence comes up.

## 7:15 AM CDT — Cleared facility check-in

Sonya's clearance came through three weeks ago — the firm submitted her paperwork the day after she signed her offer letter — and the Argent Vector security desk has her badge, photo, escort code, and the cleared-area annex authorization ready. Tom watches her hand the badge to the badge reader without hesitation. *She has been through this before.* He files the observation.

The team files into the executive briefing room. Brent, Asha, and Pearline are at the head of the table. Steve and Kevin are seated at the far end, slightly apart from the Argent Vector executives. Steve nods to Tom; Kevin lifts a hand in greeting. Steve does not perform a romance reaction; he is here for the engagement.

**Brent:** "Welcome to Argent Vector. The engagement letter named eight; I count nine. And the engagement letter named two days on F-35 production chain; we've added TALON-X RDT&E walk-throughs to Day 1 afternoon and Day 2 morning. Devon and Stavroula are the program-side leads."

**Tom:** "Sonya joined the firm Monday. Her first day on the engagement is today. Sonya was twenty-two years at Howard-Pace, federal-government division, ending as senior director of computer logistics. She'll lead the hardware-supply-chain conversation today and tomorrow under my engagement-direction supervision. I have the firm's general counsel approval on the authorship boundaries. The TALON-X RDT&E expansion: we're prepared. Mike worked Type-1 cross-domain crypto on the Atrio engagement-letter post-script and on a separate engagement two years before Atrio. Sonya did red/black separation on Howard-Pace's federal-vertical TEMPEST-rated workstation line. The team is qualified."

**Pearline** (the supply-chain VP, leaning forward): "Howard-Pace federal-government division? You were at the supplier-summit in Round Rock in 2018? The cleared-electronics summit?"

**Sonya:** "I keynoted the second day. The talk was on tier-3 visibility under the 2017 NDAA Section 808 expansion."

**Pearline:** "I was in the front row. We've been trying to find someone with that vintage of operational experience for a chain-of-custody engagement for three years."

**Brent** (smiling): "Pearline, please restrain yourself. — Tom, your engagement letter says two days. Day 1: walk the AI-side chain that's already in production for seven months. Day 2: walk the hardware-supply-chain gap. By close-out, we want a wishlist memo we can put in front of DCMA at the December review and CMMC 2.0 self-certification at the eight-week boundary. The DCMA reviewer who reads the memo cold will need a five-minute orientation path; §0.5.4 is the canonical 'if you only have five minutes' entry — §1.2 lists, the §4 four-primitives table, and the §13 stakeholder entry — and we'd want the wishlist memo to reference it for the DCMA / JCDSO reader."

**Tom:** "Engagement letter has it. We'll meet it."

**Brent:** "Steve, Kevin — your role today?"

**Steve:** "We're here as TesseraSeal vendor-side. Engagement-letter says we observe the AI-side confirmation today and contribute to the hardware-supply-chain wishlist conversation tomorrow. Kevin runs the devil's-advocate sweep on the proposed shapes; I run the spec-text fit. We are not authoring any audit conclusion — that's the firm's. We are positioning whatever sections this engagement surfaces for the working-group sub-track that follows."

**Kevin:** "And I'll push back on every shape Steve proposes. That's what I do."

**Brent:** "Good. Asha — walk the F-35 production AI chain. Devon and Stavroula get the TALON-X RDT&E walk after lunch."

## 8:30 AM — AI-side chain walk-through (Day 1 morning, F-35 sustainment)

Asha at the whiteboard. The radar-target-classification AI runs as part of the airborne mission system on F-35 Block 4 sustainment kits and B-21 development articles. The model classifies radar returns as friendly / neutral / hostile / unknown with a confidence score. Pilot in the loop on the unknown class. The model is trained on classified labeled data; the training-phase chain is out of scope today (separate program with separate clearance). The deployment-phase chain — model weights signed by Argent Vector's HSM, deployment-target attestation, in-flight inference logging — is the seven-month TesseraSeal deployment.

**Mike:** "Walk a chain entry for an inference."

**Asha:** "Each inference is a chain entry. Per-event MAC under tenant session key. Daily seal at 02:00 CDT. The classified-network analog of the ledger; the seal job runs on a cleared-area HSM. The wire format is FFIEC chain-of-custody PRD-2 with the §10.35 edge-attestation primitive — every airborne unit has a TPM that signs the device-state attestation document before each chain entry is produced."

**Mike:** "And the deployment-phase model-update events from §10.33?"

**Asha:** "Quarterly model updates. The four boundary moments — push, pull, verify, activate — each chain-bound. Last update was August 12. The verifier dispatches against the new key version per §10.10."

**Mike:** "Cleanly. What's the audit period for confirmation today?"

**Asha:** "October 1 through November 4. Five weeks. Approximately 2.4 million chain entries. Seal records every day, all cleanly walking under the verifier. The aggregation is hierarchical per §10.37 — per-airframe Merkle root over each tail number's daily entries, rolling up into the daily apex root the cleared-area HSM signs — which is what makes the bandwidth math work for an airborne fleet of this size. The chain entries themselves upload on a longer cadence; integrity claims close via the per-airframe Merkle root."

**Diana:** "And the cleared-area / unclassified boundary?"

**Asha:** "The chain entries themselves are unclassified — they don't carry mission data, only the AI-decision metadata and per-event MAC. The classified-data side of the inference is in the airborne mission system; the chain captures only the integrity-bound metadata. Brent's compliance counsel reviewed the §1.2 epistemic-scope text and confirmed the chain-entry payloads are unclassified by construction."

**Tom:** "And DCMA's view?"

**Brent:** "DCMA reviewed the AI-side chain at the May audit. Two findings — minor, both closed by July. The chain-side is what they want every contractor doing. The hardware-supply-chain side is where DCMA's December review is going to focus. Sonya, take it from there."

## 10:30 AM — The Day-1 reconciliation test (AI side)

The team divides on the AI side. Mike runs SDK trace; Chen runs ledger ingest; Luis runs seal-job and HSM signature; Diana runs IAM. Five inferences chosen across the five-week audit period:

1. A November 2 test-flight return classified as `friendly` at 0.94 confidence.
2. A November 1 unknown-classification return that pilot reviewed and confirmed as friendly.
3. An October 28 inference at a model-update-boundary day (just after the August 12 update activated for that airframe — different schedule per tail number).
4. An October 19 inference where the airborne TPM attestation showed a state-shift anomaly that triggered an operational event and a brief grounding.
5. An October 4 inference cleanly bracketing the audit-period boundary.

For all five, the per-event MAC verifies. The daily seal covers each entry. The HSM signature verifies. The TPM attestation chain verifies against the platform-vendor root. The model-update-boundary entry (item 3) carries the new `audit.deployment.model_version` correctly bound to the August 12 activation event. The state-shift anomaly entry (item 4) carries the operational-event reference correctly.

**Mike:** "All five confirm. AI-side is the cleanest seven-month-deployment confirmation we've done since Atrio's twenty-four-month."

**Brent:** "And the part that isn't in chain."

**Sonya:** "The part that isn't in chain. Hardware supply chain after lunch. — Devon and Stavroula's TALON-X walk between."

## 12:30 PM — TALON-X RDT&E walk-through (Day 1, post-lunch, R&D context)

The team relocates to the cleared-area annex behind the second fence. Devon and Stavroula meet them at the SCIF vestibule. Sonya, Mike, Diana, and Chen are the four cleared-and-cleared-area-authorized auditors going in; Tom holds at the SCIF perimeter with Brent and Pearline; Steve and Kevin do not enter the SCIF (their TesseraSeal vendor read-on is at a different facility's annex and does not extend to Argent Vector's TALON-X cleared area). Steve and Kevin will pick up the engagement at the after-action debrief in an unclassified setting.

The annex's TALON-X RDT&E lab has two airframe articles in different states of integration. Article 7 is on a stand with the sensor payload uncovered; article 9 is in an enclosed test bay running a HIL (hardware-in-the-loop) flight simulation.

**Devon:** "TALON-X program. Attritable autonomous wingman drone. The mission is sensor-and-strike augmentation for crewed fifth-and-sixth-generation aircraft. The airframe carries an EO/IR camera, a low-power SAR radar, the AI target-classification stack, the cross-domain crypto module, the comms uplink, and the flight computer. The cross-domain crypto module is the equipment that's the day's question — it sits between the AI inference output (red side, classified) and the comms uplink (black side, unclassified-encrypted). Stavroula runs the qualification."

**Stavroula:** "Type-1 cross-domain crypto. NSA-evaluated. The module is from a sub-tier supplier — I won't name them in this room — and it's a clean-sheet design qualified for TALON-X. The module's job is to take a classified AI inference output, strip the classified metadata down to the unclassified-by-construction releasable form, encrypt it, and emit it to the comms uplink. Below the module is the red side; above it is the black side. The TEMPEST-shielded enclosure encloses the red side; the comms-side antenna and modem are outside the enclosure."

**Stavroula** (catching the read on Sonya, who's nodding, and Diana, who's tracking but new to the vocabulary): "For everyone's frame of reference — *red* in the cleared-environment sense means plaintext classified content. The AI inference on TALON-X reads classified sensor data and produces classified outputs; that whole subsystem is the red side. *Black* means encrypted-or-unclassified content that's safe to put on shared infrastructure — the comms uplink, the antenna, anything that emits RF the adversary can collect. The boundary between them is hard-gated. Wires are color-coded. Racks are partitioned. Power supplies are filtered to prevent compromising emanations. The cross-domain crypto module is the only authorized passage point: red goes in, the module applies a releasability filter and encrypts under a Type-1 algorithm, black comes out. Everything we do today, everything the chain has to integrity-bind, has to respect that boundary. If a red-side payload fingerprint shows up in a black-side chain entry — even just the hash — that's a red-side leak across the boundary, and at the operational-test stage that's a program-stop finding."

**Diana:** "Got it. The chain entries themselves have to be color-aware."

**Stavroula:** "The chain entries themselves have to be color-aware. That's the §10.62 conversation."

**Mike:** "And TesseraSeal is in the airframe today?"

**Stavroula:** "TesseraSeal is on the F-35 production side — Asha walked you through that this morning. TALON-X is RDT&E phase 2; we've stood up TesseraSeal instrumentation on the AI inference path inside the cleared area, but the chain entries currently capture the red-side-only view. We have not figured out how to span the red/black boundary yet."

**Diana** (IAM, but stepping into the cross-domain conversation): "Walk a chain entry for an inference."

**Stavroula:** "On the red side: the AI classifier produces an inference (target classification + confidence + sensor metadata). The chain entry records the inference, the per-event MAC under the red-side tenant session key, the model version, the sensor frame hash. All of this is classified. The chain entry stays inside the TEMPEST enclosure on the red-side HSM-coupled ledger."

**Mike:** "And the cross-domain transition?"

**Stavroula:** "The crypto module takes the inference, applies the releasability filter — strips the precise sensor metadata, retains the bare classification, applies the TALON-X-specific Type-1 encryption — and emits an encrypted black-side payload to the comms uplink. There is no chain entry on the black side today. The black-side payload is in flight; the chain stays on the red side."

**Devon:** "The DCMA / NSA / Joint Cross-Domain Solution Office expectation, when this drone gets to operational test in fourteen months, is that the integrity claim spans the boundary. They want to know that the AI inference that produced the classification on the red side is the same inference whose releasable form the comms uplink sent on the black side. They want to know that no red-side content has leaked across the boundary into the chain entries on the black side, and they want to know that the black-side chain entries do verify the red-side chain entry's existence without disclosing red-side content."

**Sonya:** "Hash equivalence. The red-side chain entry hashes the classified-form payload. The black-side chain entry hashes the releasable-form payload. The cross-domain transition record on the red side binds both hashes — the red-side hash and the releasable-form hash — and the verifier on the black side validates that *some* red-side chain entry existed whose releasable hash matches the black-side chain entry's, without seeing the red-side content. §5.0.1 enumerates the four top-level wire-format kinds — `chain_entry`, `seal_record`, `anchor_record`, and the PRD-4-added `cross_domain_transition` — that §7's pre-flight dispatch keys on; the cross-domain transition record we're describing rides under the fourth kind."

**Stavroula:** "That's the shape we'd want. The black-side verifier sees the cross-domain transition record's releasable-hash and the black-side chain entry's hash — they match; the integrity claim spans the boundary. The black-side verifier never sees the red-side content. The red-side verifier, running inside the cleared area, sees both sides of the transition record and validates the full chain."

**Mike:** "Two verifiers, one chain that respects the red/black boundary."

**Diana:** "And the threat model for red-side leakage?"

**Stavroula:** "Spec §1.2's fourth-class adversary applies plus a red-side-content-leakage residual. §9 is the spec's security-considerations pointer — it routes to the threat-model design doc, which Sonya and I worked through with Steve last quarter for the TALON-X cross-domain adversary framing; that doc is where the supply-chain-adversary class lives. The cross-domain transition record on the red side must be constructed so that its black-side-emission projection does not encode red-side content. The releasable-hash function and the cross-domain transition record schema have to be normative — every implementation has to construct the same projection. Otherwise a vendor's implementation could leak red-side content into the projection and we'd never know."

**Sonya:** "*§10.62.* — Tom, this is the seventh wishlist item. Red/black separation chain integrity."

**Devon:** "What we'd want is exactly this. TALON-X is the first program at Argent Vector that needs it. We'd be the canonical institutional reference."

**Mike** (writing on the SCIF whiteboard):

```
SECTION 7 — RED/BLACK SEPARATION CHAIN INTEGRITY (§10.62)
  - Red-side chain entry: full classified payload, per-event MAC under red-side
    tenant session key, daily seal under red-side HSM. Chain stays inside TEMPEST
    enclosure.
  - Cross-domain transition record on the red side:
      - red_chain_entry_id (the source inference entry)
      - releasable_hash (hash of the releasable-form payload that goes black-side)
      - releasability_filter_version
      - cross_domain_module_attestation (Type-1 module's attestation document)
      - bound under red-side tenant session key, sealed under red-side HSM
  - Black-side chain entry: releasable-form payload only, per-event MAC under
    black-side tenant session key, daily seal under black-side HSM. The
    `cross_domain_releasable_hash` field references the same releasable_hash.
  - Black-side verifier: validates that for each black-side chain entry, the
    cross-domain transition record's releasable_hash matches the black-side
    chain entry's payload hash. The black-side verifier never sees red-side
    content; the integrity claim spans the boundary by hash equivalence.
  - Red-side verifier: validates the full chain, both sides.
  - Releasable-hash function: normative; deterministic; constructed so that no
    red-side content leaks into the projection. Test vectors are byte-identical
    cross-implementation references.
  - Cross-domain module attestation: §10.21 cross-anchor pattern, anchors the
    Type-1 module's NSA-issued evaluation result and the per-airframe module
    serial number into the cross-domain transition record.
```

**Stavroula:** "That schema works. We'd want the releasability_filter_version field to be vendor-specific — TALON-X has a program-specific filter, and the next program will have its own. The verifier dispatches on `releasability_filter_version` to know which filter's projection-rules to validate. And on the airframe-fleet side: §10.65.2 normates the expected-state-evolution profile via the chain-published `audit.fleet.profile_updated` event — TALON-X's behavior-profile discipline for the AI-and-cross-domain stack is structurally parallel; we'd publish the expected boot-state and PCR evolution for each airframe class so a profile drift surfaces as a chain anomaly rather than as a silent operational event."

**Mike:** "Right. The §10.62 spec normates the schema and the dispatch; the per-program filter is referenced by version."

**Sonya:** "And the equipment — the TEMPEST enclosure, the red-side HSM, the cross-domain crypto module, the black-side modem — each is a hardware item with a §10.56 HBOM chain entry, a §10.57 firmware-attestation chain entry where applicable, a §10.58 component cryptographic identity. The §10.62 cross-domain transition record references the cross-domain module's identity directly. §10.65.1 normates the chassis-level cryptographic identity composition that §10.58 component-identity primitives roll up into — relevant for hyperscale GPU fleets and equally relevant here for AESA-radar chassis attestation, where the TEMPEST enclosure plays the chassis role and per-component §10.58 identities aggregate up. The R&D context layers the wishlist family on itself: §10.56 through §10.61 plus §10.62 compose into a TALON-X program-readiness story."

**Devon:** "Eleven weeks to first flight. The wishlist memo we'd put in front of the Joint Cross-Domain Solution Office a month before that."

**Stavroula:** "And to the Type-1 module's NSA evaluation team — they'd want to see how the chain captures the module's role at the boundary. The §10.62 schema and §10.58 component cryptographic identity together give them what they want."

The team exits the SCIF at 14:15 CDT. Tom, Steve, Kevin, Brent, and Pearline are waiting in the unclassified afternoon-conference room.

**Tom:** "Brief us — unclassified-by-construction — on what the TALON-X walk surfaced."

**Sonya** (handing Tom a single page of unclassified notes): "Seventh wishlist item. §10.62 red/black separation chain integrity. The schema, the projection-hash, the boundary-spanning verifier discipline. R&D-program-driven; TALON-X is the canonical institutional reference. Devon and Stavroula are the program-side reference engineers."

**Steve:** "Releasability-hash deterministic projection?"

**Sonya:** "Yes. Normative. Test vectors byte-identical."

**Kevin:** "Pushback. The releasability filter is program-specific. So the §10.62 spec normates the *contract* — the projection must be deterministic, must not leak red-side content into the black-side projection, must be referenced by version — but the per-program projection is implementation. The verifier dispatches on `releasability_filter_version` and validates against the per-program filter's reference projection."

**Steve:** "Right. §10.62 normates the contract; per-program filter is implementation. The test vector framework would carry one canonical filter as the reference and document the contract separately."

**Sonya:** "Good. — Tom, that's the day's seventh."

**Tom:** "Logged. Memo by tomorrow close-out. — Sonya, Pearline is waiting on the supply-chain walk-through. Lead it."

## 2:30 PM — The hardware-supply-chain walk-through

Pearline leads the team into the supply-chain operations room. The wall has a map with 47 supplier-facility pins — eleven in Texas, six in Arizona, four in Massachusetts, three in California, twenty-three across nine other states, with sub-tier markers showing where the chips are fabricated (Taiwan, two facilities; South Korea, one; Malaysia, one for packaging). A second display is a live SAP feed showing inbound shipments scheduled for the next 72 hours.

**Pearline:** "The radar BOM has 1,847 distinct line items at the integrate-level. Tier-1 suppliers are all CMMC-conformant; tier-2 we audit; tier-3 we sample. The chip-level — we know who fabbed it, we know who packaged it, we know who tested it incoming. We don't have integrity binding from the fab to the test bench to the radar. That's the AS6171 anti-counterfeit gap."

**Sonya:** "Walk me through a single chip's life. Pick one. Walk me through what you know today."

Pearline pulls up a record. Part number GaN-PA-4471, gallium nitride power amplifier, the radar's transmit-side workhorse. Twelve units arrived Monday for the Block 4 sustainment line.

**Pearline:** "Fabbed at TWMC's specialty foundry, Taiwan, lot 25-Q3-1184. Packaged in Malaysia at the same supplier we've used for nine years. Tested incoming at the Argent Vector test bench in Plano. Each unit gets a serial number etched at packaging; the serial number is in our SAP record. The fab's certificate of conformance is a PDF, signed by the fab's quality director. The packaging house's traveler is a printed sheet with handwritten signatures at each station. The test-bench result is digital — the test bench writes a record to our test-result database and prints a barcoded sticker on the unit."

**Sonya:** "And the gap."

**Pearline:** "Three gaps. One: the fab's certificate is paper-equivalent — a PDF — and we hash it manually into our records but we don't bind it as a chain anchor. Two: the packaging traveler is *only* paper; nothing digital comes with the chip from packaging. Three: when a chip fails incoming test and gets returned to the supplier, we lose the chip's digital provenance entirely — the supplier may rework it, may scrap it, may ship it back to us. We've seen chips come back to us on later POs that were reworked from earlier rejects. We can't prove they're not the same chip."

**Mike:** "And cryptographic identity at the chip level?"

**Pearline:** "Some of our newer parts have on-die PUFs — physically unclonable functions. The GaN PA does not. The next-generation digital-side ASICs that go into the B-21 development articles do. We'd want to bind the PUF response to the chain entry at incoming test."

**Sonya:** "And firmware?"

**Pearline:** "Each radar field-replaceable unit ships with firmware loaded by us. Three FRUs out of seventeen have firmware built by sub-tier suppliers — we receive a signed firmware artifact, we hash it into our records, but the build-time integrity (was the supplier's build environment sealed at build time? did the supplier's CI/CD chain produce that artifact?) is something we accept on the supplier's signed attestation. We don't see into the supplier's build chain."

**Steve** (from the side of the room, where he and Kevin have been observing): "Pearline, may I ask one question?"

**Pearline:** "Please."

**Steve:** "The October 19 anomaly Mike walked this morning — the state-shift on the TPM attestation that triggered a brief grounding. Was that hardware-supply-chain related?"

**Pearline:** "Inconclusive. We grounded the airframe pending investigation. The investigation said the TPM had transitioned out of its expected boot state, possibly due to a firmware-update event that wasn't authorized through our channels. We rolled the firmware back, the airframe came off ground, and the chain entries from the flight before the grounding were quarantined per our procedure. We don't know whether the firmware-update event was a benign dev-team oversight or whether it was something else. We'd like to have known."

**Kevin** (the first time he speaks at length): "So the chain knows the airframe's TPM left its expected state. It doesn't know who put the firmware that took it out of state. It doesn't know whether that firmware is the firmware Argent Vector built or whether it's something a sub-tier supplier inadvertently shipped. It doesn't know whether the firmware build itself was integrity-bound at the supplier."

**Pearline:** "Correct. All three."

**Kevin:** "That's three sections."

**Steve:** "Three sections at minimum. — Sonya, you're driving?"

**Sonya:** "I'm driving. Let me walk what I think we want, with Steve and Kevin pushing back. Tom moderates. Tom, ground rules."

**Tom:** "Sonya proposes; Steve fits to spec text; Kevin pushes back; Pearline confirms operational reality; Mike and I write it up. Pearline — you OK with that shape?"

**Pearline:** "I'm OK with that shape."

## 2:45 PM — Whiteboard session — the remaining six wishlist sections take shape

Back in the unclassified afternoon-conference room. Steve and Kevin rejoin; the SCIF's §10.62 (red/black separation) is logged on the engagement-letter side in unclassified-by-construction form, with the per-program filter referenced by version only. Sonya picks up the marker.

```
SECTION 1 — HARDWARE BILL-OF-MATERIALS CHAIN INTEGRITY (HBOM)
  - Each chain entry for a radar BOM line item:
      - part_number (canonical)
      - serial_number (per-unit; etched at packaging or assigned at incoming test)
      - cryptographic_identity (PUF response if available; serial+lot hash if not)
      - lot_origin: { fab_id, lot_id, fab_attestation_hash }
      - packaging_origin: { house_id, traveler_hash, station_signatures[] }
      - test_origin: { test_bench_id, test_program_version, test_result_hash }
  - Chain entry produced at incoming test pass; bound under tenant session key.
  - Successive events (FRU integration, depot maintenance, RMA) bind to the
    original incoming-test chain entry via cross-anchor.
```

**Steve:** "That's §10.56. The HBOM chain. Spec text would normate the schema, the canonical-form, the cross-anchor pattern back to incoming-test. Verifier dispatch on `audit.hbom.*` family."

**Kevin:** "Pushback. The fab attestation — TWMC's certificate of conformance — is a PDF the fab signs with the fab's commercial signature, not with anything tied to Argent Vector's chain. So the chain entry includes a hash of the PDF and the PDF's signing certificate's fingerprint. That's a §10.21 cross-vendor anchor pattern, not new spec."

**Steve:** "Kevin's right — the §10.21 cross-anchor is the right primitive. §10.56 is the HBOM chain *family* and the canonical-form, not the cross-anchor. Sonya, write that down."

**Sonya** (writing): "*§10.56 HBOM chain family and canonical-form; cross-anchor to fab attestation per §10.21.*"

```
SECTION 2 — FIRMWARE-ATTESTATION CHAIN ACROSS SUPPLIER TIERS
  - Each FRU's firmware build artifact:
      - build_environment_attestation (supplier-side TEE attestation that the
        build environment was sealed at build time)
      - build_inputs_hash (source code commit, build tools, build config)
      - build_output_hash (the firmware artifact bytes)
      - supplier_chain_entry_id (the supplier's chain-entry id if the supplier is
        a TesseraSeal user; cross-anchor to the supplier's chain if they are not)
  - Argent Vector's chain entry at firmware-load time references this.
  - Activation events at the airframe bind to the firmware artifact's chain entry.
```

**Kevin:** "Pushback. Three of seventeen FRU firmware are built by sub-tier suppliers. The other fourteen are built by Argent Vector itself. So the integrity story splits: for Argent Vector-built firmware, this is internal chain instrumentation; for sub-tier-built firmware, this is the cross-supplier chain extension. The §10.57 spec section has to handle both."

**Steve:** "Right. §10.57 normates the family for both — internal-build chain entries and cross-supplier-build chain entries. The latter uses §10.21 cross-anchor when the supplier doesn't share their full chain. Sonya?"

**Sonya:** "*§10.57 firmware-attestation chain. Internal-build path direct; cross-supplier-build path via §10.21 cross-anchor.*"

```
SECTION 3 — COMPONENT CRYPTOGRAPHIC IDENTITY PRIMITIVE
  - Per-component cryptographic identity, primary instances:
      - PUF response (gold standard; physical-to-cryptographic binding)
      - SEAL chiplet attestation (DARPA SHIELD-aligned; for SHIELD program parts)
      - Chip-level provisioned key (factory-provisioned, recorded at fab)
      - Serial+lot hash (fallback for parts without on-die identity)
  - Identity bound to the §10.56 HBOM chain entry at incoming test.
  - Verifier dispatch on identity_kind; PUF-class identities verifiable at every
    chain-walk via challenge-response when the component is in-hand.
```

**Kevin:** "Pushback. PUF challenge-response at chain-walk requires the component to be in-hand. Verifier in remote-walk mode can't challenge a PUF that's flying in an F-35 over the South China Sea. So the verifier has to support both modes — *binding-walk* (verify the chain entry's identity-binding hash) and *challenge-walk* (verify the identity directly when the component is available). The two modes need separate dispatch surfaces."

**Steve:** "§10.58 normates both modes plus the marker split. Both verifier modes (binding-walk and challenge-walk) exit `0` (PASS) per §10.12; the dispatch surface is the marker string in `additional_verifications` — `component_identity_binding_walk_verified` for the binding-walk mode, `component_identity_challenge_walk_verified` for the challenge-walk mode. The §10.12 contract stays at codes 0-3."

**Sonya:** "*§10.58 component cryptographic identity primitive. Identity-kinds enumerated; binding-walk and challenge-walk modes; verifier exit-code extension.*"

## 4:00 PM — Sonya's RMA contribution

Sonya pauses the whiteboard, sets the marker down, turns to Pearline.

**Sonya:** "Pearline, I want to walk the RMA case I saw at Howard-Pace twice. Same chip — different SKU, different PO, same physical part. We caught it in 2017 because the part had a PUF and the PUF response on the second receipt matched a part we'd previously rejected. The supplier had reworked the part, restickered it under a different SKU, and shipped it back to us through a different sales channel. We rejected the lot, opened a supplier-corrective-action, and the supplier paid for the lot."

**Pearline:** "We don't have that today. We've suspected it twice. We can't prove it."

**Sonya:** "What I want is — the chain entry at incoming test binds the cryptographic identity. If the same identity shows up later under a different SKU, the verifier flags the duplicate-binding anomaly. RMA / sustainment chain re-entry is the mirror — when a part comes back to Argent Vector for depot maintenance or RMA, the chain entry at re-entry references the original incoming-test chain entry. The full life of the part is a chain in itself. The verifier walks the part's life and produces a continuity verdict."

```
SECTION 4 — RMA / SUSTAINMENT CHAIN RE-ENTRY DISCIPLINE
  - When a component re-enters Argent Vector's chain (depot return, RMA, repair,
    cannibalization, scrap), the re-entry chain entry binds:
      - original_incoming_test_chain_entry_id (cross-anchor)
      - re_entry_event_kind (rma | depot_return | repair_complete | cannibalized | scrapped)
      - cryptographic_identity_re_verification (challenge-walk if PUF; binding-walk otherwise)
      - reason_code, disposition
  - Verifier walks part's life; flags identity_re_verification failures, duplicate
    bindings (same identity bound to multiple incoming-test entries under different
    serial numbers), and orphan re-entries (re-entry without a prior incoming).
```

**Kevin:** "Pushback. Cannibalization is the messy case. A failed FRU is opened; some of its components are good, some are bad; the good components get re-installed in another FRU. Each component needs an individual disposition. The re-entry record is per-component, not per-FRU."

**Steve:** "§10.59 normates per-component re-entry. The cannibalization event is a parent chain entry with N child component chain entries, each disposing one component. The verifier walks the cannibalization tree and validates each disposition."

**Sonya:** "*§10.59 RMA / sustainment chain re-entry; cannibalization handled as parent-children pattern; per-component re-entry.*"

```
SECTION 5 — ANTI-COUNTERFEIT CROSS-ANCHOR
  - When AS6171 anti-counterfeit testing or DARPA SHIELD chiplet attestation is
    performed by an independent third party, the test result is hashed and
    anchored on the chain via §10.21 cross-anchor.
  - The §10.58 cryptographic identity verification at incoming test composes with
    this anchor: a part that passes both the chain-entry identity binding and the
    independent anti-counterfeit anchor has cross-vendor anti-counterfeit assurance.
  - Suspect parts identified via §10.58 duplicate-binding anomalies trigger an
    AS6171 referral; the AS6171 result is anchored back as a §10.60 disposition.
```

**Kevin:** "Pushback. AS6171 testing is destructive on some parts. So the part that gets tested is by definition not the part that gets installed. The cross-anchor is on a sample of the lot, not on the installed part. The chain entry has to acknowledge the sampling."

**Steve:** "§10.60 normates the sample-cross-anchor pattern. The chain entry binds the lot-level anti-counterfeit attestation to the per-part chain entries via the lot identifier. Sample-based-attestation is explicitly named in the §10.60 schema."

**Sonya:** "*§10.60 anti-counterfeit cross-anchor; sample-based-attestation pattern.*"

```
SECTION 6 — CMMC 2.0 / NIST 800-171 / NIST 800-161 REGULATOR-PACK OVERLAY
  - The five sections above (§10.56-§10.60) compose into a defense-contracting
    regulator-pack overlay. The overlay maps:
      - CMMC 2.0 Level 3 controls (specifically AC.L3-3.1.4, MA.L3-3.7.5,
        SC.L3-3.13.2, SI.L3-3.14.6, and the supply-chain-risk-management family)
      - NIST 800-171 §3.4 Configuration Management; §3.7 Maintenance;
        §3.10 Physical Protection; §3.13 System & Communications Protection;
        §3.14 System & Information Integrity
      - NIST 800-161 SR-1 through SR-12 (supply-chain-risk-management practices)
      - DFARS 252.204-7012 incident-response binding
  - DCMA reviewers walk the overlay during contractor self-certification and
    DCMA visits; the overlay's verifier runs produce control-by-control PASS/FAIL
    against the chain.
```

**Kevin:** "Pushback. CMMC 2.0 Level 3 is on a four-year revision cadence. The overlay has to version against the published CMMC requirements. So §10.61 isn't one fixed overlay; it's a versioned overlay with each CMMC release."

**Steve:** "§10.61 normates the overlay framework; specific CMMC-version overlays are sub-overlays under it — the CMMC-2.0 sub-overlay today, the next-release sub-overlay when DCMA publishes it, with DCMA's published version as the reference."

**Sonya:** "*§10.61 regulator-pack overlay framework; versioned per CMMC release.*"

The whiteboard is full.

**Tom** (writing in the engagement notebook): "Seven sections all told. §10.56 through §10.61 surfaced just now in the unclassified room; §10.62 surfaced in the SCIF earlier on the TALON-X red/black walk. Sonya leads authorship; Mike consults on vendor-architecture; Steve and Kevin contribute spec-fit and devil's advocate. Memo by close-out tomorrow."

**Pearline:** "I want the §10.56-§10.61 in front of DCMA at the December review."

**Devon** (rejoining from the SCIF doorway, in the unclassified-vestibule transition): "And §10.62 in front of the Joint Cross-Domain Solution Office at our next program review — eight weeks from now, four weeks before TALON-X first flight."

**Brent:** "Yes. — Tom, what's the institutional-reference question?"

**Tom:** "Argent Vector is the canonical institutional reference for §10.56-§10.61 on the F-35 production side and for §10.62 on the TALON-X RDT&E side, if the spec working group accepts the proposed sections. Pearline becomes the reference engineer for the supply-chain family; Devon and Stavroula are the reference engineers for the red/black separation section; Asha contributes the airborne-side context. The engagement debrief documents both institutional postures."

**Pearline:** "I would be honored to contribute as the reference institution."

**Devon:** "TALON-X program-side accepts the same."

## 4:30 PM CDT — The Day-1 client question

Brent in his office. Late-afternoon Texas sun coming through the south window. Sonya, Tom, and Steve are present. Kevin is in the SCIF with Mike and Pearline reviewing the RMA records.

**Brent:** "DCMA in eight weeks. CMMC 2.0 Level 3 self-certification due. The hardware-supply-chain wishlist memo lands in DCMA's hands at the December review. What's our message?"

**Sonya:** "Our message is: the AI-side chain has been operational at integrity bar for seven months on F-35 sustainment. The hardware-supply-chain side is the next horizon, and the spec working group is actively positioning the §10.56-§10.61 family. Argent Vector is the canonical institutional reference for the family. The CMMC 2.0 self-certification we're submitting at the eight-week boundary cites the AI-side chain as in-scope-conformant; the hardware-supply-chain section cites the wishlist-memo and the timeline for §10.56-§10.61 production deployment as part of the institutional roadmap. The TALON-X RDT&E surface has its own program-readiness story — §10.62 red/black separation chain integrity, with TALON-X as the canonical institutional reference and first flight at the eleven-week boundary."

**Brent:** "And the answer when the DCMA reviewer asks why the chip in the radar isn't in chain today?"

**Sonya:** "The honest answer is: it's a real gap. We're proposing §10.56 through §10.61 to close it. We'll have the wishlist memo at the December review and we'd like the DCMA reviewer's input on the section text. Argent Vector's institutional commitment is to deploy the family within twelve months of the spec working group's normative-text adoption."

**Brent:** "And the reviewer will ask: what does Argent Vector do in the meantime?"

**Sonya:** "In the meantime: we tighten the SAP-side records, we maintain the per-part PDF cross-anchor on every fab certificate of conformance, we manually hash the packaging travelers and bind them as per-PO records, and we accept the residual that the digital-to-physical binding is paper-equivalent until §10.56 onward ships. The chain doesn't lie about what it doesn't yet have."

**Brent** (after a pause): "That's the right answer. And the TALON-X side — what's the answer at the program review?"

**Sonya:** "On the TALON-X side: today's chain captures red-side AI inference cleanly; the cross-domain transition record and the black-side chain entry are the §10.62 wishlist; until §10.62 ships, the program operates the chain on the red side only and accepts that the black-side integrity claim is the cross-domain module's NSA evaluation, not the chain. §10.62 closes that gap. Devon and Stavroula are the reference engineers; the program review and the JCDSO submission cite the wishlist-memo timeline."

**Brent:** "And — Steve, anything from the vendor side?"

**Steve:** "I want to be careful — I'm not authoring the audit conclusion. Sonya is. But Kevin and I will commit to fast-tracking the §10.56-§10.62 family at the next working-group meeting. Argent Vector's institutional reference, plus TALON-X program-side reference engineers, is the kind of input the working group needs. If you, Pearline, Devon, and Stavroula are willing to be cited, the family lands in the spec at the next release window."

**Pearline** (joining from the doorway): "We're willing to be cited. Argent Vector is the institutional reference."

**Devon:** "TALON-X program-side accepts the same."

**Brent:** "Tomorrow we close out the wishlist memo and the engagement debrief. Tom — same time tomorrow?"

**Tom:** "Same time. The team will be on-site at 7:30."

## 6:30 PM — Hotel restaurant, Legacy West

The team takes the corner of the Marriott restaurant. Tom has the engagement notebook open; Sonya is two seats down from him. Steve and Kevin have a separate table at the far end of the restaurant — there is professional respect in the spacing.

**Raj:** "Sonya. Day 1 of seventeen-and-counting. How does it feel?"

**Sonya:** "Familiar. The whiteboard work is the same work I did at Howard-Pace, just with a different vocabulary on the spec side."

**Mike:** "And the spec-side felt comfortable?"

**Sonya:** "Steve and Kevin are exactly the kind of vendor-side I worked with at Howard-Pace, when we were negotiating with Cisco or Lenovo on supply-chain provisions. They know the spec end-to-end, they push back when the proposal is fuzzy, they don't sell. I appreciate that."

**Tom** (from the head of the table): "Dawn is going to want a debrief on you when she gets back from Boston. I'll write her tomorrow night. The first read on a new team member is the first read."

**Sonya:** "What did she say when she heard I was joining?"

**Tom:** "She read your file twice. She told me on the phone last week — 'Howard-Pace federal-government division. Twenty-two years. She knows what a chain looks like that doesn't have integrity. She knows what it costs.' She told me to give you the seat next to me on the drive-in today. So I did."

**Sonya:** "Good. — Tell her thank you when you talk."

Tom's phone buzzes. He glances at it and smiles.

**Tom:** "Speak of the devil. — *Sonya did beautifully today. Tell her I said welcome. Niece Kayla and Hassan are doing well. Baby is a champion sleeper which I'm told is rare. — D*"

The table laughs. Sonya looks down at her plate, then up.

**Sonya:** "Tell Dawn I said thank you. And that I'll meet her properly when she's back."

**Tom:** "I will."

## Day 2 — wishlist memo finalization and close-out

Day 2 morning the team finalizes the wishlist memo. Sonya leads the §10.56-§10.61 section drafts with Mike on vendor-architecture review and Steve and Kevin on spec-fit. Tom partners with Brent on the audit-procedure walk and the CMMC 2.0 self-certification mapping.

By 1:30 PM, the memo is final. Six sections, with Argent Vector as the canonical institutional reference for each; Pearline named as the reference engineer; Sonya named as authoring auditor; Mike and Steve and Kevin named as contributing reviewers under the recusal-clean-by-Dawn's-absence note.

The close-out is at 3:00 PM in the executive briefing room. Brent, Asha, Pearline, the cleared-area annex commander, and DCMA's Argent Vector-relationship lead (a colonel-equivalent in the December-review preparatory cycle) are present.

**Brent** (to Tom): "Memo received. We'll submit it to DCMA for the December review and to the JCDSO for TALON-X program review and to the spec working group through TesseraSeal's channel by Friday. Pearline coordinates the institutional-reference attribution for §10.56-§10.61; Devon and Stavroula coordinate it for §10.62. Argent Vector commits to the §10.56-§10.62 deployment within twelve months of the working-group normative-text adoption, with §10.62 fast-tracked to align with TALON-X first flight."

**Tom:** "Engagement closes from our side. The audit-procedure memo is in your records; the wishlist memo goes to DCMA, JCDSO, and the working group. Sonya is the authoring auditor on the wishlist memo; Mike consulted; Steve and Kevin contributed under the recusal-naturally-satisfied note. The §10.62 portion is unclassified-by-construction; the per-program-filter content stays inside the SCIF."

**The DCMA reviewer:** "I'll read it on the flight back to Andrews. The §10.56-§10.61 family is exactly what the December review's hardware-supply-chain question was going to focus on. The §10.62 content is the JCDSO's lane, but I'll flag it on my side as a coming-soon item. We'll cite Argent Vector as the institutional reference if the working group accepts the family. Thank you."

**Brent:** "Tom, Sonya, Mike, the team — thank you. Wheels up?"

**Tom:** "DFW at 5:45. We'll be off the Plano campus by 4."

The team flies home. Sonya sits next to Tom on the flight; she has the firm's onboarding packet open and is reading the engagement-letter conventions for her authorship signature.

## TesseraSeal wishlist items Argent Vector surfaces

Argent Vector's deployment is mature on the AI side (F-35 sustainment) and confirms cleanly under existing spec primitives. The hardware-supply-chain side is the next-horizon family — six wishlist items that compose into a defense-contracting overlay — and the TALON-X RDT&E surface adds a seventh covering red/black separation chain integrity. Each is articulated below with what Argent Vector operates today, what the spec section would normate, and Argent Vector's commitment as the canonical institutional reference.

### Section 1 — Hardware bill-of-materials chain integrity (§10.56)

**What Argent Vector operates today.** SAP records of every BOM line item; PDF certificates of conformance from each fab; printed packaging travelers with handwritten station signatures; digital test-result records at incoming test; per-unit serial numbers etched at packaging. The records compose end-to-end at the human level; they do not compose at the chain-integrity level.

**What §10.56 would normate.** A canonical-form HBOM chain family — `audit.hbom.incoming_test`, `audit.hbom.fru_integration`, `audit.hbom.depot_return` — with chain entries bound under the institution's tenant session key. Cross-anchor to fab certificates of conformance via §10.21. Cross-anchor to packaging travelers via a digital-equivalent traveler signed by each station station-keeper. Verifier dispatch on the `audit.hbom.*` family produces a per-part lifecycle verdict.

**Argent Vector's commitment.** Canonical institutional reference. Pearline contributes operational-reality input to the working group. Argent Vector deploys §10.56 within twelve months of normative-text adoption.

### Section 2 — Firmware-attestation chain across supplier tiers (§10.57)

**What Argent Vector operates today.** Three of seventeen FRU firmware artifacts are built by sub-tier suppliers; the supplier's signed artifact is hashed into Argent Vector's records but the supplier's build-time integrity (was the build environment sealed at build time? what was the supplier's CI/CD chain state?) is accepted on the supplier's signed attestation. Fourteen of seventeen are built internally; the build is in Argent Vector's CI/CD with TesseraSeal instrumentation, but the build-time chain entries are not normatively framed.

**What §10.57 would normate.** A firmware-attestation chain family — `audit.firmware.build`, `audit.firmware.activate` — with `build_environment_attestation`, `build_inputs_hash`, `build_output_hash` fields. For sub-tier-supplier-built firmware, cross-anchor to the supplier's chain via §10.21 when the supplier is a TesseraSeal user, or to the supplier's signed attestation document via §10.21 when not. Activation events at the airframe bind to the firmware build chain entry. Late-arriving supplier attestations follow §10.36's late-arrival seal discipline — Pattern A (supplemental seal) is the right fit for the DCMA workflow where suppliers may ship signed attestations days after delivery; the day-of-delivery seal stays unchanged and the day-N+K supplemental seal binds the late-arrival into the day-N integrity envelope retroactively.

**Argent Vector's commitment.** Canonical institutional reference for the cross-supplier-build path. Argent Vector commits to extending instrumentation to the three sub-tier suppliers within twenty-four months of normative-text adoption (commercial-relationship dependency).

### Section 3 — Component cryptographic identity primitive (§10.58)

**What Argent Vector operates today.** Some next-generation digital-side ASICs have on-die PUFs; the PUF response is captured at incoming test but is not bound to the chain entry. SEAL chiplet attestation is in production on three DARPA SHIELD-aligned program parts; the attestation document is captured but not chain-bound. Older parts (the GaN PA, for example) have no on-die identity; the identity is the etched serial number plus the lot identifier.

**What §10.58 would normate.** A component cryptographic identity primitive enumerating identity-kinds (PUF, SEAL chiplet attestation, factory-provisioned key, serial+lot hash). Identity bound to the §10.56 HBOM chain entry at incoming test. Verifier dispatch on `identity_kind` with two modes — *binding-walk* (always available; verifies the chain entry's identity-binding hash) and *challenge-walk* (component-in-hand; verifies the identity directly via challenge-response). Both verifier modes (binding-walk and challenge-walk) exit `0` (PASS) per §10.12; the dispatch surface is the marker string in `additional_verifications` — `component_identity_binding_walk_verified` for the binding-walk mode, `component_identity_challenge_walk_verified` for the challenge-walk mode. The §10.12 contract stays at codes 0-3.

**Argent Vector's commitment.** Canonical institutional reference. Argent Vector commits to PUF-binding deployment on all PUF-equipped parts within twelve months of normative-text adoption; SEAL chiplet attestation binding within nine months on the three DARPA SHIELD-aligned program parts.

### Section 4 — RMA / sustainment chain re-entry discipline (§10.59)

**What Argent Vector operates today.** Returned units (RMA, depot return, repair) re-enter the SAP records under a separate disposition workflow. The original incoming-test record exists in SAP; the re-entry record exists in SAP; the linkage is by serial number lookup but is not chain-bound. Cannibalization (a failed FRU opened, components removed and re-installed in another FRU) is dispositioned per-component on a paper traveler; the per-component records are not in chain. Pearline's twice-suspected-but-unprovable rework-and-restickering case is the operational pain point.

**What §10.59 would normate.** A re-entry chain family — `audit.rma.depot_return`, `audit.rma.repair_complete`, `audit.rma.cannibalized`, `audit.rma.scrapped` — with cross-anchor to the original §10.56 incoming-test chain entry. Cannibalization handled as a parent chain entry with N child component chain entries, each disposing one component. Verifier walks the part's life; flags identity-re-verification failures, duplicate bindings (same identity bound to multiple incoming-test entries under different serial numbers), and orphan re-entries.

**Argent Vector's commitment.** Canonical institutional reference. Sonya as engagement-side authoring auditor contributes the duplicate-binding anomaly pattern from her Howard-Pace 2017 institutional-history experience.

### Section 5 — Anti-counterfeit cross-anchor (§10.60)

**What Argent Vector operates today.** AS6171 anti-counterfeit testing is performed quarterly by an independent third-party laboratory on samples drawn from incoming lots of suspect parts. DARPA SHIELD chiplet attestation is performed at the SHIELD-program enrollment for the three SHIELD-aligned program parts. Both produce signed attestation documents that are filed in Argent Vector's records but not chain-anchored.

**What §10.60 would normate.** A sample-based anti-counterfeit cross-anchor pattern. AS6171 / SHIELD attestation documents are hashed and anchored on the chain via §10.21; the chain entry binds the lot-level attestation to the per-part chain entries via lot identifier. Sample-based-attestation is explicitly named in the §10.60 schema (the sample is destroyed; the attestation extends to the lot, not the installed part). Suspect parts identified via §10.58 duplicate-binding anomalies trigger an AS6171 referral; the AS6171 result is anchored back as a §10.60 disposition. §10.60 is the canonical institutional consumer of the §10.21.1 sample-based-attestation cross-anchor pattern — lot-level destructive testing per AS6171 binds at the lot, and per-component chain entries inherit transitively via the lot identifier.

**Argent Vector's commitment.** Canonical institutional reference. Argent Vector commits to AS6171 cross-anchor within nine months of normative-text adoption; SHIELD attestation binding within nine months on the three SHIELD-aligned program parts.

### Section 6 — CMMC 2.0 / NIST 800-171 / NIST 800-161 regulator-pack overlay (§10.61)

**What Argent Vector operates today.** CMMC 2.0 Level 3 self-certification is at the eight-week boundary; controls are walked manually against the AI-side chain plus the paper-equivalent hardware-supply-chain records. NIST 800-171 and 800-161 are walked alongside CMMC. DCMA reviews are every six months; the December review will focus on hardware supply chain.

**What §10.61 would normate.** A regulator-pack overlay framework mapping CMMC 2.0 Level 3 controls (specifically AC.L3-3.1.4, MA.L3-3.7.5, SC.L3-3.13.2, SI.L3-3.14.6, and the supply-chain-risk-management family) to chain entries; NIST 800-171 §§3.4, 3.7, 3.10, 3.13, 3.14 to chain entries; NIST 800-161 SR-1 through SR-12 to chain entries; DFARS 252.204-7012 incident-response binding. Versioned per CMMC release as sub-overlays under §10.61 — the CMMC-2.0 sub-overlay today, the next-release sub-overlay when DCMA publishes it, etc. Verifier produces control-by-control PASS/FAIL.

**Argent Vector's commitment.** Canonical institutional reference for §10.61's CMMC-2.0 sub-overlay. Argent Vector commits to the overlay deployment in tandem with §10.56-§10.60.

### Section 7 — Red/black separation chain integrity (§10.62)

**What Argent Vector operates today.** TALON-X RDT&E phase 2; first flight in eleven weeks. The on-board AI target-classification stack runs inside a TEMPEST-shielded enclosure (red side); a Type-1 NSA-evaluated cross-domain crypto module gates the boundary; the comms uplink is on the black side outside the enclosure. TesseraSeal instrumentation is stood up on the red-side AI inference path — chain entries on the red-side HSM-coupled ledger inside the cleared area. The black side is uninstrumented today; the cross-domain transition is not chain-bound; the integrity claim across the red/black boundary is the cross-domain module's NSA evaluation only.

**What §10.62 would normate.** A red/black-aware chain entry schema with two color-tagged sides (red-side full-payload chain entries; black-side releasable-form chain entries). §10.62.1 normates the `audit.color_classification.side` tag (red / black / cross-domain) every chain entry under §10.62 carries — this is the per-entry discriminator the verifier dispatches on. A cross-domain transition record on the red side that binds the source red chain entry's id, the deterministic releasable-hash projection, the releasability_filter_version, and the cross-domain module's §10.21-anchored attestation document. A black-side chain entry that carries the same releasable-hash and is verifiable by a black-side verifier without sight of the red-side content. Two verifier modes — *black-side verifier* (validates hash equivalence at the boundary; never sees red content) and *red-side verifier* (validates the full chain inside the cleared area). §10.62.2 normates the per-program releasability-projection contract — TALON-X is the PRD-4 reference projection; the contract names the deterministic filter that produces the byte-identical releasable-hash from a red-side payload. The releasable-hash function and the cross-domain transition record schema are normative; the per-program releasability filter is referenced by version. Test vectors are byte-identical cross-implementation references for the contract; the per-program filter has its own reference projection logged separately.

**Argent Vector's commitment.** Canonical institutional reference for §10.62 via the TALON-X RDT&E program. Devon (program-engineering lead) and Stavroula (cross-domain-crypto qualification lead) are the program-side reference engineers. Argent Vector commits to deploying §10.62 instrumentation on TALON-X before operational test (fourteen months out), with the JCDSO program review at the eight-week boundary as the first external surface for the wishlist memo.

## Engagement debrief — Tom's voice (Dawn returns Story 20)

> "Engagement eighteen. Argent Vector Defense Systems. Plano, Texas. Sonya's first day with the firm. Dawn on PTO in Boston with Kayla and Hassan and the new baby. Steve and Kevin from TesseraSeal on-site for the wishlist conversation; recusal-protocol vendor-engagement constraint naturally satisfied by Dawn's absence; the firm's general-counsel-cleared engagement-letter authorship boundaries held cleanly. Mike consulted on vendor-architecture; Sonya led the hardware-supply-chain wishlist drafting; I authored audit-procedure.
>
> "Seven wishlist sections — §10.56 hardware bill-of-materials chain, §10.57 firmware-attestation across supplier tiers, §10.58 component cryptographic identity primitive, §10.59 RMA / sustainment chain re-entry, §10.60 anti-counterfeit cross-anchor, §10.61 CMMC 2.0 regulator-pack overlay framework, §10.62 red/black separation chain integrity. Argent Vector is the canonical institutional reference for §10.56-§10.61 on the F-35 production side; the TALON-X RDT&E program is the reference for §10.62. Pearline is the supply-chain reference engineer; Devon and Stavroula are the TALON-X program-side reference engineers.
>
> "Sonya earned her engagement-letter signature on the day. Twenty-two years at Howard-Pace's federal-government division gave her the operational vocabulary for hardware supply chain that the spec text needed. Her 2017-rework-and-restickering institutional memory became the §10.59 duplicate-binding-anomaly pattern. Pearline at Argent Vector recognized her from the 2018 Round Rock supplier-summit keynote — they spent an hour after Day 1 wrap-up on PUF-binding details. In the SCIF on Day 1 afternoon she carried the §10.62 red/black projection-hash conversation cleanly with Stavroula and Devon — Howard-Pace's federal-vertical TEMPEST workstation line gave her the cross-domain vocabulary she needed. The day worked because Sonya's depth fit Argent Vector's gap on both surfaces.
>
> "Steve and Kevin contributed exactly what the engagement letter named — Steve fit the proposed shapes to spec text; Kevin pushed back on every shape until the shape was clean. The vendor-side intellectual rigor was useful and not improper. Their TesseraSeal vendor read-on did not extend to the TALON-X SCIF, so Sonya, Mike, Diana, and Chen carried §10.62 in the cleared area and Steve and Kevin picked up the unclassified-by-construction projection in the afternoon-conference room. Dawn will read this debrief Friday when she's back from Boston.
>
> "The next time we visit a defense-electronics prime, this engagement is the canonical reference. The next time we visit an autonomous-systems R&D program with red/black separation, the §10.62 surface is exercised first here. Argent Vector ran it the way the spec working group needs."

## Cross-references

- **Spec impact (proposed)**: §10.56 (HBOM chain), §10.57 (firmware-attestation), §10.58 (component cryptographic identity), §10.59 (RMA / sustainment), §10.60 (anti-counterfeit cross-anchor), §10.61 (CMMC 2.0 regulator-pack overlay), §10.62 (red/black separation chain integrity).
- **Test-vector references (proposed)**: vectors 054-064 (Phase 12, Story 18) referenced by the proposed sections above per `spec/test-vectors/PRD-4-INDEX.md`; PUF binding-walk vector (050) and PUF challenge-walk vector (051), SEAL chiplet attestation vector (058), and the red/black projection-hash vector for the TALON-X reference filter (063) plus the black-side hash-equivalence walk vector (064) are the most novel additions across the §10.58 and §10.62 surfaces.
- **Stakeholder navigation**: §13 stakeholder for "defense-electronics prime supplier" and "autonomous-systems R&D program with red/black separation" — two new candidate stakeholders for spec §13.
- **Auditor stories**: this story's wishlist contrasts with Story 12 Hill Country (real-time decisioning, §10.27-§10.31) and Story 13 Saraswati (edge-AI federated, §10.32-§10.38) — the third wishlist engagement, the first with a hardware-physical-product surface and the first with cleared-environment red/black separation. Sonya's first engagement with the firm; Tom's first lead in Dawn's absence; Steve and Kevin's first vendor-side on-site under the recusal-naturally-satisfied posture.

The wishlist memo and engagement debrief are filed under Argent Vector's compliance-track records, with the §10.56-§10.61 wishlist items submitted to the spec working group under Sonya's authorship and Pearline as canonical institutional reference engineer; the §10.62 wishlist memo (unclassified-by-construction) is submitted in parallel with TALON-X program-side references. DCMA's Argent Vector-relationship lead receives the supply-chain wishlist memo at the December six-month review; the JCDSO receives the §10.62 portion at the TALON-X program review eight weeks out.
