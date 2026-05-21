# 13 — Saraswati Microfinance

> An Indian microfinance NBFC — non-banking financial company — headquartered Mumbai, with ~3.2 million borrowers across 1,800 branches in tier-2 and tier-3 cities and rural districts in seven Indian states. Field officers carry ruggedized Android tablets running an offline-first credit-decisioning AI; the model updates monthly via federated learning across the deployed device fleet. TesseraSeal in production for 4 months on the central-inference path; edge-AI integrity is the engagement question. Three of the team — Dawn, Mike, Chen — fly to Mumbai; the remaining five (Raj, Elena, Diana, Luis, Tom) join via video bridge from US Eastern Time during the late-evening IST overlap window. The engagement is three days. Saraswati exercises the spec's edge / federated / training-phase design points end-to-end — §10.32 per-device key derivation, §10.33 model-update events, §10.34 training-phase integrity, §10.35 edge-attestation, §10.36 late-arrival seal discipline, §10.37 hierarchical Merkle, §10.38 consent capture for DPDP Act.

## The team and the day

Three travel to Mumbai: Dawn (lead), Mike (application/API — he handles the Android-edge code path), Chen (data engineering — he handles federated-learning data flow). Five join from US Eastern Time on a video bridge that opens at 19:30 IST / 09:00 ET and runs until roughly 23:00 IST / 12:30 ET each day. Tom moderates the time-zone split.

The engagement is at Saraswati's headquarters in the Bandra Kurla Complex, Mumbai — a glass-and-steel office in a financial-district district that looks more like Singapore than the rural cities Saraswati serves. The contrast is the day's emotional weight.

## The drive-in monologue — in a Mumbai taxi

```
6:15 AM. Mumbai pre-monsoon humidity. Black-and-yellow Padmini taxi, BKC.
                          Dawn's first time in India. Mike second. Chen first.
```

**Dawn:** "Twelve prior engagements. Crescent was the most recent — real-time payments, streaming cadence under §10.27-§10.31. Today is the opposite end of the spectrum: edge-AI, federated learning, offline-first under §10.32-§10.38."

**Mike:** "And the bandwidth picture is — what."

**Dawn:** "Ruggedized Android tablets. Field officers carrying them on motorcycles to villages four hours from the nearest paved road. Cellular when they have it; no-cellular for hours at a time. The chain has to accommodate that posture without breaking the integrity claim."

**Chen:** "And the federated learning?"

**Dawn:** "Monthly model updates. Pushed from central to edge. The chain captures the model-update boundary moments under §10.33 — push, pull, verify, activate. Saraswati's MRM committee reviews them as integrity-bound chain entries."

**Mike:** "Plus DPDP Act. Plus RBI's IT Governance Master Direction. Plus the institutional posture for international-funder requirements — they have a NIST AI RMF mapping in their compliance portfolio."

**Dawn:** "Yes. Three regulatory regimes overlapping. Plus the RBI inspection coming up in nine weeks."

**Chen:** "That gives us a deadline."

**Dawn:** "It gives Saraswati a deadline. Our deadline is the spec-section confirmation memo by end-of-engagement. The spec already normates everything Saraswati exercises — §10.32 through §10.38 cover edge AI, federated learning, training-phase integrity, and DPDP consent capture. Our job is to confirm operational fidelity."

**Mike:** "It never is."

**Dawn:** "It never is. But Saraswati's edge geometry exercises spec sections that no prior engagement has stressed at scale. §10.32's per-device key derivation runs on 15,000 tablets. §10.34's training-phase integrity covers monthly federated-learning aggregation. §10.36's late-arrival seal discipline handles offline-first field-officer workflows. §10.37's hierarchical Merkle aggregation is what makes the bandwidth-constrained connectivity work. We're going to walk every section against operational reality."

The taxi turns into the BKC complex. Skyscrapers. Polished black granite. Indian flags on every building.

## 7:45 AM IST — Saraswati's office

The lobby has a wall of large-format photographs of Saraswati's borrowers — women weavers in Tamil Nadu, dairy farmers in Haryana, dhaba owners in rural Maharashtra, micro-tailors in Bihar. The institutional message is clear: this is what we do.

**Saraswati's CRO** — Vikram Singh, late 50s, ex-Bank of Baroda, ex-IFC: "Ms. Dawn. Welcome. Your taxi was on time?"

**Dawn:** "Mumbai pre-monsoon, 6 AM, traffic was reasonable."

**Vikram:** "It will not be reasonable later. Coffee?"

**Dawn:** "Yes please. The team in the US joins at seven thirty PM our time?"

**Vikram:** "Confirmed. Nineteen-thirty IST. We have the videoconference room booked. Tom is moderating?"

**Dawn:** "Tom is moderating. He'll handle the time-zone split."

**Vikram:** "Good. Let me introduce our CDO — Priya Krishnan. She runs the AI program."

**Priya** — late 30s, ex-Flipkart, ex-Razorpay — joins at the breakfast table. She has a tablet open, evidently the same model her field officers carry: a ruggedized Samsung tablet with a thick case and a tethered card-swipe peripheral.

**Priya** (handing the tablet to Dawn): "This is what we ship to fifteen thousand field officers. The screen is the credit-decisioning interface. The camera does document capture. The card-swipe processes the PAN-and-Aadhaar fields. The whole stack runs offline-first; cellular sync happens when available."

**Dawn** (turning the tablet, looking at the case): "How long does the average field officer spend offline per day?"

**Priya:** "Median is two-and-a-half hours. Ninety-fifth percentile is six. Some districts in Jharkhand and the rural Northeast — there's no cellular for forty kilometers and the officer is offline for the whole field-day. They sync at the end of the day when they get back to the branch."

**Dawn:** "And the chain at the edge?"

**Priya:** "Per-event MAC at capture, written to local storage with fsync. Daily seal happens at the central server when the day's entries have been uploaded. So the integrity-claim asymmetry for edge-captured entries is *until upload completes*, which is end-of-day in the worst case but can be the next morning if the officer is in a no-cellular district."

**Dawn:** "Three-day engagement. We'll walk the architecture today, do reconciliation tomorrow, and produce the spec-section confirmation memo on day three before the team flies home. The RBI inspection is nine weeks out — your CC8.1 control description and our spec-section memo will go to the RBI's IT Governance assessor in advance of the inspection."

**Vikram:** "Yes. The IT Governance Master Direction was updated by RBI in 2024 with explicit AI-governance expectations. We have to document the chain coverage and the chain-coverage boundary."

**Dawn:** "Per spec §10.19. We'll walk that this morning."

## 9:00 AM IST — Architecture walk-through

Priya walks the team through the architecture. Schema:

```
                                            ┌──────────────────────────────────┐
                                            │  CENTRAL SERVER (Mumbai DC)      │
                                            │                                  │
                                            │  - HSM (FIPS 140-2 Level 3)     │
                                            │  - Daily seal job (02:30 IST)   │
                                            │  - Federated-learning aggregator │
                                            │  - Master credit model (canon)   │
                                            └──────────────────────────────────┘
                                                          ▲
                                                          │ (cellular when available;
                                                          │  end-of-day batch on rural)
                                                          │
                                                  ┌───────┴───────┐
                                                  │               │
                                                  ▼               ▼
                                      ┌──────────────────┐  ┌──────────────────┐
                                      │ EDGE TABLET A    │  │ EDGE TABLET B    │
                                      │ (rural Jharkhand)│  │ (urban Mumbai)   │
                                      │                  │  │                  │
                                      │ - Local SQLite   │  │ - Local SQLite   │
                                      │ - Per-event MAC  │  │ - Per-event MAC  │
                                      │ - Local model    │  │ - Local model    │
                                      │ - Hardware-     │  │ - Hardware-      │
                                      │   backed key     │  │   backed key     │
                                      │   store          │  │   store          │
                                      └──────────────────┘  └──────────────────┘
```

Two sub-systems, with three integrity surfaces:

1. **Central inference path** — when an officer is online, decisions go through a server-side path with full chain coverage under the spec's standard primitives.
2. **Edge inference path** — when offline, decisions happen on-device. Chain entries are MAC'd at capture and buffered to local SQLite. Sync happens on next connectivity.
3. **Federated learning** — monthly. The central server pushes a new credit model to every edge tablet. The edge tablets compute local gradients on local-data and send the gradients (not the data) back to the central aggregator. The aggregator computes the global update and pushes the new global model. **None of this is currently in the chain.**

**Mike:** "So the edge-tablet's session key — that's derived from the institution's IKM via HKDF, with the tablet identifier in the info parameter?"

**Priya:** "Yes. We extended the spec's per-tenant HKDF info to include a per-device sub-component. So the info is `HKDF_INFO_BASE || '|' || utf8(tenant_id) || '|' || utf8(device_id)`."

**Mike:** "That's a vendor-specific extension."

**Priya:** "It is. We documented it in our CC8.1 description as a 'binding to per-device session key derivation.' The institution is on the record as operating an extended derivation; the verifier we use is a custom build that knows about the extension."

**Mike:** "Wishlist item right there. Per-device session key derivation isn't in the spec. It's institution-side custom. The next institution that wants to do this has to roll their own; the verifier vendor has to know about the extension."

**Dawn:** "**§10.32 — Per-device session key derivation**. The spec extends §4.1's derivation with a per-device sub-component: `HKDF_INFO_BASE || '|' || utf8(tenant_id) || '|' || utf8(device_id)`. Saraswati exercises this on 15,000 tablets. Single-tenant-no-device institutions continue under §4.1's base derivation."

**Tom** (from the engagement notebook): "Saraswati is the canonical institutional reference for §10.32."

**Priya:** "We'd be honored."

**Mike** (turning back to the diagram): "Now the federated learning."

**Priya:** "Monthly. We push a new global model from central to all 15,000 tablets. The push is over HTTPS, signed by the central server's TLS certificate. The tablet verifies the TLS chain and replaces its local model. None of this is in the chain. The institution's MRM committee has the gap documented."

**Chen:** "What's covered when an officer makes a credit decision?"

**Priya:** "The decision itself — chain entry. The local model version is recorded as an attribute on the chain entry (`audit.deployment.model_version`). The features used are `audit.underwriting.features.*`. The output is the standard chain output."

**Chen:** "And the model-update event itself — the moment when the tablet pulls the new model and starts using it — is not a chain entry."

**Priya:** "Correct."

**Dawn:** "**§10.33 — Model-update events as chain entries**. The `audit.model_update.*` family captures the deployment-phase boundary: push at the central server, pull at each tablet, verify of the institution's signature, activate when the tablet begins serving decisions on the new model. This is deployment-phase, not training-phase — it's about *which* model was active at the moment of decision, not how the model was trained. Saraswati emits the family on every monthly cycle."

**Chen:** "And the federated-aggregator events — when the central server combines gradients from edge devices into a global update?"

**Dawn:** "That's *training-phase* under §10.34. Spec §1 scope includes training-phase integrity normatively, and §10.34 normates the `audit.training.*` family covering local_gradient, aggregation, validation, and model_artifact events. Saraswati emits the family on every monthly cycle. Training-phase events compose alongside the deployment-phase events of §10.33 via cross-anchor links per §10.21."

**Priya:** "Which is what we do today, but it's not in the chain. The MRM committee documents it under the institution's separate AI-development governance program."

**Dawn:** "**§10.34 — Training-phase integrity**. Saraswati's federated-learning aggregation is exactly the use case §10.34 normates. The `audit.training.*` family covers local_gradient, aggregation, validation, and model_artifact events. The training-phase chain composes alongside the deployment-phase chain via cross-anchor links per §10.21 / §10.33. Saraswati exercises every event in the family every month."

The morning fills the whiteboard.

## 11:30 AM IST — The Jharkhand officer

Priya pulls up a specific officer's chain — Anita, a field officer in Dumka, Jharkhand. Anita's tablet ID is `tab-7e2a-...`. Her last sync was yesterday at 18:42 IST when she rode her motorcycle back to the Dumka branch.

```
DEVICE TAB-7E2A-... (Anita, Jharkhand)
  - 14:00 IST: powered on, location verified, biometric login confirmed
  - 14:15 IST: officer arrives at applicant's home, starts interview
  - 14:18 IST: PAN/Aadhaar capture
  - 14:23 IST: features captured (income proof, family demographics, business plan summary)
  - 14:24 IST: chain entry: model call, output APPROVE-WITH-LIMIT
  - 14:25 IST: officer presents the result, gets applicant's signature
  - 14:26 IST: chain entry: deployment-intent (officer override flag NOT set)
  - 14:27 IST: chain entry: signature capture
  - 14:30 IST: officer rides motorcycle to the next applicant
  - ...
  - 17:50 IST: Anita is offline. Chain entries are buffered.
  - 18:42 IST: Anita arrives at the branch. Tablet syncs over branch wifi.
              Buffered entries upload to central server.
  - 23:00 IST: central daily-seal cuts at end of UTC day (which in IST is 05:30
               next morning). Anita's events from 14:00-17:50 IST are sealed.
  - 05:30 IST next morning: SEAL COMPLETES.
```

**Mike** (looking at the trace): "What's the integrity-claim asymmetry for Anita's 14:24 chain entry?"

**Priya:** "The per-event MAC is integrity-bound at 14:24. Buffered locally. The chain entry verifies in isolation against the device's session key, which the verifier can re-derive once it knows the institution's IKM and the device ID."

**Mike:** "And the cross-event integrity?"

**Priya:** "The seal completes at 05:30 IST the following morning."

**Mike:** "So in the worst case — Anita's tablet has been buffering for the whole field-day — the integrity-claim asymmetry is up to 15 hours."

**Priya:** "Yes."

**Dawn:** "And if Anita's tablet is stolen during that window?"

**Priya:** "The tablet is bound to Anita's biometric login plus a device-revocation registry. The IKM at central isn't on the tablet — only the device's session key is. A stolen tablet cannot generate new chain entries because the session key is hardware-key-store-bound and requires biometric unlock. Buffered entries on the tablet are MAC'd with the session key; we have the public fingerprint to validate them when they upload."

**Dawn:** "What about session-key extraction?"

**Priya:** "Android Keystore is hardware-backed. TEE-protected. We've deployed only on devices with verified-boot and Knox enrollment. Key extraction via root or jailbreak fails because the key is non-extractable from the TEE."

**Mike:** "But the §1.2 SDK-process compromise residual still applies. If an attacker compromises Anita's tablet *while* it's in her possession, with the session key in the TEE, the attacker can use the session key to generate new MAC entries that verify."

**Priya:** "Yes. That's the residual. We compensate with a heartbeat-and-reconciliation discipline: every tablet sends a heartbeat every fifteen minutes when online. If a tablet hasn't heart-beat for over an hour while showing chain-entry production, that's an anomaly. We've not had an incident yet."

**Mike:** "**§10.35 — Edge-attestation primitive**. The spec normates the device-attestation layer. Chain entries carry `ffiec.chain.attestation` with the device's TEE attestation document. The verifier validates the attestation chain against the platform-vendor root at chain-walk time. Saraswati operates Android Keystore TEE attestation across all 15,000 tablets."

**Dawn:** "Good. That's the second edge-specific section confirmed. Adding it to the memo."

## 1:00 PM IST — Lunch

The Saraswati executive cafeteria has a buffet of regional Indian dishes. The team takes a corner table.

**Tom** (over a thali): "So far, four sections confirmed. §10.32 per-device key derivation, §10.33 model-update events, §10.34 training-phase integrity, §10.35 edge-attestation primitive."

**Dawn:** "Yes. The afternoon will surface more. The bandwidth question and the federated-learning aggregator are the next two."

**Chen:** "Bandwidth — yeah. The chain entry's wire size for a single credit decision is around 4 KB. A field-day with 30 decisions plus operational events is around 200 KB. That's reasonable for cellular. But a tablet that's been buffering across multiple field-days because the officer was in a no-cellular district for a week — that's a few MB to upload. And the central daily seal needs to wait for all of these to land."

**Mike:** "So the seal is delayed by the tail of stragglers."

**Chen:** "Or the seal cuts as scheduled and any straggler entries are sealed in the next day's seal — which means the chain has events with `mac_computed_at_utc` from yesterday but sealed under tomorrow's seal."

**Dawn:** "That's a §4.2 invariant question. The seal aggregation is per-tenant-day on UTC calendar boundaries. If a chain entry's `mac_computed_at_utc` is yesterday's UTC date but the entry doesn't reach the ledger until tomorrow's UTC day has started, where does it go?"

**Chen:** "Spec §4.2 says it goes in the day matching its `mac_computed_at_utc`. But that day's seal has already completed. So either we have to delay the seal (waiting for stragglers) or we have to allow late-arriving entries to be sealed in a 'late-arrivals' supplemental seal record."

**Dawn:** "**§10.36 — Late-arriving-entry seal discipline**. The spec normates two patterns: Pattern A supplemental seal in the day-N+1 record covering late-arriving day-N entries, or Pattern B rolling seal window keeping day-N's seal open for a defined window. Saraswati operates Pattern A — supplemental seal — and Saraswati's CC8.1 names the choice. The verifier dispatches on `seal.late_pattern`."

**Tom** (writing): "Five so far. What else does the afternoon cover?"

**Dawn:** "The federated-aggregator and the bandwidth-efficient incremental Merkle proof. Then we'll have the US team online at seven thirty PM IST and we'll review."

## 3:15 PM IST — Federated-learning aggregator walk-through

Priya pulls up the aggregator's monthly schedule.

```
FEDERATED LEARNING — MONTHLY CYCLE

Day 1-25 of month:  Edge devices accumulate local-data and compute local gradients
                    on the current global model. Local gradients are buffered.
Day 26:             Edge devices upload local gradients to central aggregator
                    over TLS. (Local gradients only; no underlying data.)
Day 27:             Central aggregator combines gradients into a candidate global update.
                    Validation team reviews the candidate against held-out test set.
Day 28:             If validation passes, candidate becomes the new global model.
                    Central server signs the new model artifact (Ed25519 in HSM).
Day 29:             Central server pushes new global model to all 15,000 tablets.
                    Each tablet pulls, verifies the signature, activates the new model.
Day 30:             All tablets reporting active on new model. Cycle ends.
Day 1 (next):       Cycle resumes.
```

**Chen:** "Where is each step in the chain today?"

**Priya:** "Steps 1, 2, 3 are out of chain. They're in the AI-development governance regime, separately documented. Steps 4 and 5 (the model-artifact signature and push) are partially in chain — we record the model artifact's signature and the institution-signed Ed25519 over the model bytes, but the chain entries for the per-device pull and activate are NOT in chain. Today the per-device activation is in the device's local logs only."

**Chen:** "So when Anita's tablet activates a new model on day 29 of the month, that activation is not chain-recorded?"

**Priya:** "Correct. The next chain entry from Anita's tablet (a credit decision on day 29 or day 30) carries the new `audit.deployment.model_version`, but the activation event itself isn't in the chain."

**Dawn:** "That's §10.33 — model-update events as chain entries. The push, pull, verify, and activate events are all in the chain. The chain captures the boundary moments of the federated-learning cycle, and §10.34 covers the cycle's training-phase activity (steps 1-3) end-to-end."

**Chen:** "And the federated-aggregator's combination step — step 3 — that's where the gradient combination happens. That's the *core* training activity. That's what training-phase integrity would cover."

**Dawn:** "§10.34 — training-phase integrity. Yes."

**Chen:** "What does training-phase integrity actually look like for a federated-learning aggregator?"

**Dawn** (whiteboarding):

```
TRAINING-PHASE INTEGRITY (V2.X CANDIDATE)

Per-edge-device local-gradient capture:
  - Hash of local data the gradient was computed against (privacy-preserving:
    a hash, not the data)
  - Hash of the gradient itself
  - Device attestation at gradient compute time
  - Local chain entry: `audit.training.local_gradient.*`

Aggregator-side:
  - Set of contributing devices (with hashes confirming each contributed)
  - Aggregation method (FedAvg, FedProx, secure aggregation)
  - Aggregator chain entry: `audit.training.aggregation.*`

Validation:
  - Test-set integrity (hash of held-out test data)
  - Validation-result chain entry: `audit.training.validation.*`

Model-artifact production:
  - Final model bytes
  - Model-card hash
  - Hyperparameter set hash
  - Training-environment attestation
  - Chain entry: `audit.training.model_artifact.*`
```

**Chen:** "That's a substantial scope expansion."

**Dawn:** "It is. Saraswati's posture under §10.34 covers the deployment-phase boundary (§10.33 model-update events) and the training-phase activity (§10.34 audit.training.* family) end-to-end. Saraswati is the canonical federated-learning institutional reference."

**Priya:** "We'd contribute to the working-group as a reference institution if asked."

**Dawn:** "Tom, that's an action item — the spec working group's federated-learning sub-track would benefit from Saraswati's institutional voice."

**Tom** (writing): "Action item logged."

## 4:30 PM IST — The CDO question

The team is still in the conference room. Priya joins for the day's wrap.

**Priya:** "Tomorrow you'll do the reconciliation test. Day three you'll write the spec-section confirmation memo. Before we break — let me ask the question I'd ask a regulator. *What does the chain currently prove about Saraswati's edge-AI integrity, today?*"

**Dawn:** "If the RBI assessor or our DPDP DPO has only five minutes, §0.5.4 is the canonical short path — the §1.2 lists, the §4 four primitives, and the §13 stakeholder entry. That's the spec answer without reading the whole spec. Today the chain proves:

1. Every chain entry that has been ingested at the central server has a per-event MAC integrity-bound to the device's session key, which is integrity-bound to the institution's IKM.
2. The daily seal at the central server covers all entries that have been ingested by the seal-cut time.
3. Edge-device chain entries that haven't yet uploaded are integrity-bound at the device locally; they will be visible at the central seal whenever they upload.

The chain does NOT prove:

1. The edge device's hardware integrity — that's the §1.2 SDK-process compromise residual, partially compensated by Android Keystore TEE attestation but not bound into the chain entries.
2. The model-update events at the boundary between federated-learning cycles — these are out-of-chain today.
3. The federated-aggregator's training-phase activity — out of future-extension scope.

The chain DOES support these RBI inspection questions:

1. *Show me an integrity-bound trace of a credit decision* — yes. Per-event MAC at capture, daily seal, HSM signature.
2. *Show me which model was active at the moment of decision* — yes, via `audit.deployment.model_version` on every entry.
3. *Show me how you confirm the chain isn't tampered with* — yes, the verifier."

**Priya:** "And the spec sections?"

**Dawn:** "Five sections so far, with one more I expect to surface tomorrow. §10.32 per-device key derivation, §10.33 model-update events, §10.34 training-phase integrity, §10.35 edge-attestation primitive, §10.36 late-arrival seal discipline, and probably §10.37 hierarchical Merkle aggregation tomorrow."

**Priya:** "And our message to RBI on the inspection?"

**Dawn:** "You exercise full conformance across §10.32-§10.38 today. Chain coverage is documented per §10.19. The institutional posture is: *we are the canonical federated-learning microfinance reference institution, every spec section we exercise is operationally exercised in production, the spec sections are part of our CC8.1 control description, and our deployment is the institutional reference for any future engagement that touches edge AI, federated learning, or DPDP consent capture*. For the RBI assessor, the DPDP DPO, and the field-officer org reading the spec for the first time, Appendix A.17 names the recommended reading-order — chain envelope first, then OTel-shaped attributes, then the schema families as needed."

**Vikram** (joining): "That is an excellent message for RBI."

**Dawn:** "It's defensible because it's true."

**Priya:** "Tomorrow morning, eight AM, we walk reconciliation. Let me know if you need anything different."

**Dawn:** "Eight AM works. Tom, the US team joins us on video at seven thirty IST tonight?"

**Tom:** "Confirmed. They'll be at home offices. I have the bridge link."

## 7:30 PM IST — Video bridge with the US team

The conference room. Mumbai dusk through the windows. Tom moderates. The US team is on the screen — Raj at his home office in Brooklyn, Elena at hers in Chicago, Diana in San Francisco, Luis in Austin, Tom in DC.

The video bridge runs for two-and-a-half hours. The US team gets briefed on the day's spec-section confirmations, asks clarifying questions, and the on-site team gets fresh angles on the analysis.

**Diana** (from San Francisco): "On the edge-attestation primitive — I've been thinking about this. The Android Keystore TEE attestation produces a signed attestation document. That document could be embedded as an attribute on the chain entry. Then the verifier could verify the attestation document against Google's TEE root certificate authority chain at verify time."

**Mike** (in Mumbai, looking up): "That's a good shape. The chain entry stamps the attestation document; the verifier verifies the attestation chain. It would prove the device's hardware integrity at the moment of chain-entry production."

**Diana:** "It would prove that *the device that produced this chain entry was a genuine TEE-backed Android device with verified-boot at chain-entry time*. That's a real strengthening of the SDK-process compromise residual."

**Dawn:** "**§10.35** is the right shape. Edge-attestation specifies the attestation-chain verification as part of the verifier procedure. The verifier validates the attestation chain at chain-walk time. Saraswati exercises the Android Keystore variant; institutions on Apple devices exercise the Secure Enclave variant under the same §10.35 schema."

**Luis** (from Austin): "What about the bandwidth-efficient Merkle proof point Chen raised? That's the §10.37 hierarchical aggregation."

**Chen:** "Yes. The current §4.2 ships full chain entries plus the seal record. For an edge-device upload after a week-long no-cellular period, that's potentially MB of chain data to upload at once. The aggregation could be done incrementally — the device computes a local Merkle root over its buffered entries and uploads (1) the local Merkle root, (2) the per-entry inclusion proofs against the local root, (3) the entry data. Then the central server includes the local Merkle root as a leaf in the daily seal's Merkle tree, with the local Merkle proof being the path from the local root to the daily root."

**Dawn:** "**§10.37 — Hierarchical Merkle aggregation**. Two-level Merkle: each tablet computes a per-device Merkle root over its locally-buffered entries; the central server includes the per-device root as a leaf in the daily seal's Merkle tree. The verifier walks the hierarchy. Saraswati operates this in production — bandwidth-efficient upload of per-device roots and inclusion proofs, full payloads on a longer cadence."

**Raj** (from Brooklyn): "And the bandwidth efficiency comes from the device only uploading its local Merkle root and the relevant inclusion proofs, not all the per-entry data."

**Chen:** "Right. The device can upload the entries themselves separately on a longer cadence; the integrity claim closes via the Merkle root."

**Dawn:** "Six sections confirmed. Tomorrow's reconciliation will surface §10.38 — DPDP Act consent capture under `audit.consent.*`."

**Tom:** "What about that?"

**Dawn:** "DPDP Act requires consent records bound to data-processing decisions. The chain has consumer-correlation-index integrity per §10.23 and adverse-action translation per §10.11. DPDP-specific consent capture is a regulator-pack overlay candidate, not a spec change. We'll cover it tomorrow."

The bridge wraps at 22:15 IST. Tom logs the action items.

## Day 2 — 8:00 AM IST — Reconciliation

The team and Priya pick ten credit decisions from the prior week. The diversity is intentional:

1. Anita's 14:24 IST decision in rural Jharkhand (urban-vs-rural contrast).
2. A Mumbai BKC officer's decision (urban high-volume).
3. A decision from a tablet that synced after a 3-day no-cellular period.
4. A decision where the customer disputed the AI's recommendation and an officer overrode.
5. A decision on day 28 of the federated-learning cycle (just before model rollout).
6. A decision on day 29 (just after model rollout, on the new model).
7. A decision on a tablet that has since been retired (officer left the company).
8. A decision involving an applicant whose Aadhaar verification failed.
9. A decision that was APPROVED and the loan disbursed; the borrower has been repaying on schedule.
10. A decision that was DECLINED; the applicant later complained and the matter was reviewed.

For all ten, the trace runs end-to-end:

- Per-event MAC verifies in isolation.
- Daily seal covers each chain entry.
- HSM signature verifies.
- Cross-vendor anchor — the day-29 decision (item 6) crosses the model-update boundary; §10.33's model-update events are emitted at the boundary, integrity-binding the new-model activation directly to the credit decisions made on it.
- Tablet retirement (item 7) — the tablet's session key was rotated when retired; the §10.10 rotation covered it. The post-retirement chain history is bound to the prior key; the verifier handles the rotation correctly per the existing §7 procedure.

The reconciliation passes. Ten of ten chain traces complete with full integrity claims.

**Priya:** "And the gaps?"

**Dawn:** "The model-update event boundary at item 6 — in chain under §10.33. The federated-learning cycle activity — in chain under §10.34 training-phase integrity. The DPDP Act consent records — in chain under §10.38 `audit.consent.*` family.

Confirming **§10.38 — Consent capture** for DPDP Act 2023 §6. The `audit.consent.*` family covers the lifecycle (given / referenced / withdrawn / expired) with `legal_basis = \"dpdp_act_2023_§6\"`. Saraswati exercises the family on every credit-decision touching an Indian borrower."

## 1:00 PM IST — Wishlist memo finalization

The team and Priya draft the spec-section confirmation memo. By 4 PM IST, the memo is final and reviewed.

## Day 3 — Wishlist memo to Vikram, then home

The memo is delivered to Vikram at 09:00 IST on day three. Vikram briefs the Saraswati AI Governance Committee at 10:00. The committee endorses the spec-section confirmations and authorizes the institution's representation to the spec working group as the canonical federated-learning institutional reference.

The team flies home Tuesday evening. Mumbai-Frankfurt-NewYork (Dawn). Mumbai-Singapore-LosAngeles (Mike, Chen). The spec-section confirmation memo is filed under Saraswati's compliance-track records, with the §10.32-§10.38 spec-section confirmations cited in the institution's CC8.1 control description.

## TesseraSeal forward-thinking design points Saraswati exercises

Saraswati's deployment exercises seven spec sections that TesseraSeal's design anticipated for edge-deployed federated-learning institutions. Each is articulated below with what Saraswati operates and which spec section the institution is conformant against.

### Section 1 — Per-device session key derivation (§10.32)

**What Saraswati operates.** 15,000 ruggedized Android tablets each derive an independently-bound session key from the institution's IKM via HKDF, with the device identifier bound into the `info` parameter (`HKDF_INFO_BASE || '|' || utf8(tenant_id) || '|' || utf8(device_id)`). Each device's session key is independent. A compromised device's session key cannot forge entries for any other device. The institution's CC8.1 names the device-id issuance and revocation procedure. Test vector `024-per-device-derivation` is the byte-identical reference.

**Why TesseraSeal designed for this.** §10.32 normates the per-device extension precisely so edge-deployed institutions like Saraswati get device-isolated cryptographic identities without rolling their own.

### Section 2 — Model-update events (§10.33)

**What Saraswati operates.** The monthly federated-learning cycle emits chain entries at all four deployment-phase boundary moments. `audit.model_update.push` when the central server pushes the new global model. `audit.model_update.pull` when each tablet pulls. `audit.model_update.verify` when each tablet verifies the institution's signature. `audit.model_update.activate` when each tablet begins serving decisions on the new model. Subsequent decision entries carry the new `audit.deployment.model_version` per §4.4.2, integrity-bound by the activation event. The institution's MRM committee reviews the model-update boundary as integrity-bound chain entries.

**Why TesseraSeal designed for this.** §10.33 normates the family. Examiners and validation programs read the model-update boundary directly from the chain.

### Section 3 — Training-phase integrity (§10.34)

**What Saraswati operates.** The federated-learning aggregator emits the `audit.training.*` family across the monthly cycle. `audit.training.local_gradient` per tablet (with `local_data_hash` and `gradient_hash` — privacy-preserving via hash). `audit.training.aggregation` at the central aggregator combining gradients. `audit.training.validation` against the held-out test set. `audit.training.model_artifact` at final model production. The training-phase chain composes alongside the deployment-phase chain via cross-anchor links — an examiner walking from a credit decision traverses model_update → model_artifact → validation → aggregation → local_gradient.

**Why TesseraSeal designed for this.** §10.34 lifted training-phase integrity into normative spec scope alongside inference-phase per §1. Federated-learning institutions like Saraswati get end-to-end chain coverage from training through deployment to decision. §10.64 normates the broader training-run code-and-config chain primitive — `audit.training_run.launch / checkpoint / completed` events with per-step Merkle aggregation over gradient contributions — that §10.34 specializes for the federated case. Saraswati's per-aggregation-cycle events roll up under §10.64 at the central-coordinator side.

### Section 4 — Edge-attestation primitive (§10.35)

**What Saraswati operates.** Every chain entry produced on a Saraswati tablet carries `ffiec.chain.attestation` with the Android Keystore TEE attestation document. The verifier validates the attestation chain against Google's Android Keystore root at chain-walk time. Devices that fail the attestation requirement (verified-boot state changed, root certificate chain broken, Knox enrollment lost) are excluded from chain-entry production until remediated. The institution's CC8.1 names the device-class attestation requirement.

**Why TesseraSeal designed for this.** §10.35 narrows the §1.2 SDK-process compromise residual at the edge significantly. The attestation document captures device hardware-integrity state at every chain-entry production; a compromised device's attestation shift is detectable at the verifier.

### Section 5 — Late-arriving-entry seal discipline (§10.36)

**What Saraswati operates.** Pattern A — supplemental seal. Field-officer tablets in rural Jharkhand, Bihar, and Northeast India routinely run offline for hours and occasionally days. When entries arrive at the central ledger after the daily-seal cut for their UTC date, the next day's seal record includes a supplemental sub-record covering the late-arriving entries with its own Merkle root and signature. Saraswati's CC8.1 names the Pattern A choice. The verifier dispatches on `seal.late_pattern = "supplemental"` and reconciles late-arrivals into the day-N integrity envelope retroactively without altering the original day-N seal.

**Why TesseraSeal designed for this.** §10.36 normates the late-arrival pattern for offline-first edge institutions. Saraswati's field-day workflow is exactly the use case.

### Section 6 — Hierarchical Merkle aggregation (§10.37)

**What Saraswati operates.** Two-level Merkle. Each tablet computes a per-device Merkle root over its locally-buffered entries. The central server includes the per-device Merkle root as a leaf in the daily seal's Merkle tree. Bandwidth efficiency: tablets upload their per-device root and the inclusion proofs for entries the central server hasn't seen yet (hash-only, not full payloads). Chain entries themselves upload on a longer cadence. The verifier walks the hierarchy: per-event Merkle audit path to per-device root, per-device root to daily root, both verifying against the seal's signed apex root.

**Why TesseraSeal designed for this.** §10.37 normates the hierarchy. Bandwidth-constrained connectivity in rural India is exactly what the hierarchical aggregation was designed for.

### Section 7 — Consent capture for DPDP Act (§10.38)

**What Saraswati operates.** The `audit.consent.*` family on every credit-decision chain entry that touches an Indian borrower under DPDP Act 2023 §6. `audit.consent.given` at applicant-onboarding capturing the consent text hash and the legal basis (`"dpdp_act_2023_§6"`). `audit.consent.referenced` on each subsequent decision processing the borrower's data. `audit.consent.withdrawn` when a borrower exercises §13 withdrawal rights. `audit.consent.expired` on time-bound consents reaching expiration. The verifier validates consent-lifecycle coherence (no `referenced` after `withdrawn`; no `withdrawn` without prior `given`). Saraswati's token vault holds the subject-id-to-hash mapping under controlled access.

**Why TesseraSeal designed for this.** §10.38 normates the family for any privacy regime requiring consent-bound processing — DPDP, GDPR Article 6(1)(a), CCPA, PIPA, LGPD. Saraswati is the canonical DPDP Act institutional reference.

## Engagement debrief — Dawn's voice

> "It never is. And edge changes the geometry. The chain is in motion at the device, in flight on cellular, then sealed at the center. Each leg has its own integrity story. The spec handles each leg through explicit normative text — §10.32 per-device key derivation at the device, §10.36 late-arrival seal discipline for in-flight legs, §10.37 hierarchical Merkle aggregation at the center. The legs are explicit, not implicit.
>
> "Saraswati is the canonical federated-learning microfinance institutional reference. The seven spec sections they exercise — §10.32 per-device key derivation, §10.33 model-update events, §10.34 training-phase integrity, §10.35 edge-attestation, §10.36 late-arrival seal discipline, §10.37 hierarchical Merkle aggregation, §10.38 consent capture for DPDP Act — cover the edge / federated / training-phase design space end-to-end:
>
> - **Edge-side sections**: §10.32 per-device key, §10.35 edge-attestation, §10.37 hierarchical Merkle.
> - **Boundary sections**: §10.33 model-update events, §10.36 late-arrival seal discipline.
> - **Center sections**: §10.34 training-phase integrity, §10.38 consent capture.
>
> "Saraswati exercises every section in production. The institution is the reference deployment for any future federated-learning microfinance engagement.
>
> "RBI's IT Governance inspection in nine weeks will see the spec-section confirmation memo as part of Saraswati's CC8.1 control description. The institution's posture is defensible: full conformance across §10.32-§10.38, with the spec sections each operationally exercised in production."

## Cross-references

- **Spec sections exercised**: §10.32 (per-device derivation), §10.33 (model-update events), §10.34 (training-phase integrity), §10.35 (edge-attestation), §10.36 (late-arrival seal), §10.37 (hierarchical Merkle), §10.38 (consent capture for DPDP Act).
- **Test-vector references**: vectors 024-033 referenced by the spec sections above; training-phase vectors land alongside §10.34.
- **Stakeholder navigation**: §13 stakeholder for "edge-deployed federated-learning institution" — a new candidate stakeholder.
- **Auditor stories**: this story's spec-section confirmation contrasts with Story 12 Crescent (real-time central, streaming-mode confirmation) and Story 11 Eberhardt × Lumière (cross-vendor, both fully chained). The geometry of edge-deployed chain capture is structurally different from any of the prior 12 engagements; Saraswati is the canonical reference for edge.

The spec-section confirmation memo and engagement debrief are filed under Saraswati's compliance-track records, with the §10.32-§10.38 spec-section confirmations cited in the institution's CC8.1 control description.
