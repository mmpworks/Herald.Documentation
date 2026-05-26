# 13 — Saraswati Microfinance (Kognitos-lens)

*An engagement where the architecture itself outruns the framework's vocabulary — three integrity surfaces (central inference, edge inference on 15,000 ruggedized Android tablets, monthly federated-learning cycle), and the Kognitos 12 fields can read one of the three cleanly and have no place to put the other two.*

**Engagement:** Three-day pre-engagement readiness pass before the Reserve Bank of India's IT Governance Master Direction inspection (nine weeks out). Audiences: RBI Department of Supervision (IT-governance lead and AI-governance subsection lead, 2024 update with explicit AI-governance expectations); Data Protection Board of India under the DPDP Act 2023 (consent-lifecycle observer); the institution's NIST AI RMF mapping for international funders (ADB, CDC Group, IFC) reads downstream.
**Client:** Saraswati Microfinance — Indian non-banking financial company (NBFC-MFI), Bandra-Kurla Complex Mumbai headquarters. ~$1.6B disbursed loan book across 1,800 branches in seven Indian states (Maharashtra, Karnataka, Tamil Nadu, Telangana, Andhra Pradesh, Odisha, West Bengal). 15,000 ruggedized Android tablets in the hands of field credit officers; offline-first SQLite buffering at the device; cellular when reachable. Central inference path in production four months on AWS Mumbai (`ap-south-1`) with cross-region replicas in `ap-south-2` (Hyderabad). Monthly federated-learning cycle pushes a new global model on Day 29 of each month; tablets pull, verify, activate.
**Status:** Chain in production: four months on the central inference path. Edge inference path: per-event MAC at capture, hardware-backed Android Keystore session key on each tablet, no central seal at capture time. Federated-learning aggregator: monthly cycle, four cycles run, no chain inscription of training-phase events because the framework has no place to put them. Single tenant `saraswati`, three `service.name` values (`central-credit-decision`, `edge-credit-decision`, `federated-aggregation`). The engagement is the institution's first formal audit-readiness pass on the edge + federated surfaces; the central inference path has had two prior internal-audit passes.
**Audit team lead:** Dawn
**Client liaisons:** Vikram Iyer (Chief AI/ML Officer — owns the federated-learning program); Aparna Desai (Data Protection Officer — owns DPDP Act §6 consent-lifecycle compliance); Rohit Bhandari (Chief Auditor, Internal Audit); Sandeep Mehta (AI vendor product-engineering lead, edge SDK on Android, on bridge from Bengaluru); Neha Pathak (Chief Information Security Officer — owns the Android Keystore TEE attestation posture).

**Audit team's framework:** Kognitos's 12-field schema. The team is now thirteen engagements in. This is the first engagement where the framework's vocabulary is structurally narrower than the architecture under audit. Prior chapters surfaced under-reporting and inarticulability at one boundary (Atrio's tenant-isolation; Helmstad's redaction-disposition; Pacific Crescent's stated-identity vs authenticated-identity). Saraswati surfaces inarticulability at three integrity surfaces simultaneously — per-device key derivation, edge-attestation, late-arriving-entry seal, hierarchical Merkle aggregation, training-phase integrity, DPDP consent lifecycle, model-update boundary moments. The 12 fields verify cleanly against the central inference path. They have no vocabulary for the other two surfaces.

---

## 🌅 8:30 AM IST Day 1 — Kickoff (BKC Mumbai, fourteenth floor, Saraswati Tower)

The audit team had arrived in Mumbai on Sunday evening. Dawn, Mike, Diana, Elena, and Chen took the fourteenth-floor conference room at Saraswati's BKC tower — floor-to-ceiling windows along the south side, the Bandra-Worli Sea Link visible in the distance through the haze, a long teak table that seated twelve. The institution had laid out tea, samosas, and a printed three-day agenda at each seat. The bridge to Bengaluru was scheduled to open for Sandeep Mehta at 9:00 IST sharp.

Vikram Iyer opened from the head of the table. He was the Chief AI/ML Officer — late forties, Stanford-trained, the institution's third hire when Saraswati pivoted from manual underwriting to machine-learning credit scoring six years ago. He owned the federated-learning program. He had been the one who insisted on per-device hardware-backed keys when the SDK was specified; he was the one who would have to explain to the RBI inspector in nine weeks whether the architecture met the 2024 update's AI-governance expectations.

Aparna Desai sat to his right. She was the institution's Data Protection Officer under the DPDP Act 2023 — appointed eighteen months earlier when the act came into force, with a background in privacy law from Mumbai University and three years at the IT Ministry before joining Saraswati. She owned consent-lifecycle compliance. Every credit decision touching an Indian borrower needed to bind to a consent record under DPDP Act §6, and every consent record needed to be revocable. The lifecycle binding was her responsibility.

Rohit Bhandari — Chief Auditor, Internal Audit — sat opposite. He was a quieter presence, fifteen years at Saraswati, the institution's load-bearing voice on documentation discipline. He had requested the engagement six weeks earlier. The RBI Master Direction's 2024 update had landed on his desk in January and he had read it three times. He wanted to know, before the RBI inspector arrived, what the institution's audit-trail posture looked like under a recognized AI-audit framework.

Neha Pathak — CISO — joined the in-person side at 8:45. She had been delayed by traffic on the Sea Link. She owned the Android Keystore TEE attestation posture; she would be the one walking the audit team through the device-side cryptographic surface during the afternoon session.

At 9:00 the bridge opened and Sandeep Mehta joined from Bengaluru. He was the AI vendor product-engineering lead — the edge SDK on Android was his team's deliverable, deployed across the 15,000 tablets in field-officer hands.

Dawn ran the three-day plan. Day 1 walked the architecture end-to-end across the three integrity surfaces (central inference, edge inference, federated aggregation). Day 2 reconciled ten credit decisions across a diversity matrix (rural vs urban; pre-rollout vs post-rollout; retired tablet; disputed override; KYC-failed; repaying-on-schedule; declined-then-complained). Day 3 delivered the closing memo at 09:00 IST.

*Note for the chapter. Three integrity surfaces. Four months of central-inference chain. Edge-inference path with per-event MAC at capture, no central seal at capture time. Monthly federated-learning cycle with no chain inscription of training-phase events. Under the reference spec, this is a §10.32-§10.38 wishlist engagement — every section in the family exercised in production at one institution. Under Kognitos, the question is what the framework can record about the architecture at all.*

## 🧬 9:30 AM IST Day 1 — Central inference path walkthrough

Mike pulled the first sample chain entry from the central-inference path. It was a Mumbai-urban credit decision dated 2026-05-19, a small-business loan to a fruit vendor in Dadar — application captured at the branch, scored against the central model, approved at 6:42 PM IST. The chain entry sat in the `central-credit-decision` service, sequence 184,712, four months into the chain.

```json
{
  "entry_id": "saraswati/central-credit-decision/2026-05-19#184712",
  "tenant": "saraswati",
  "service": "central-credit-decision",
  "seq": 184712,
  "ts": "2026-05-19T13:12:08.442Z",
  "model_id": "saraswati-credit-v3.2",
  "model_version": "3.2.4-2026-04-29",
  "gen_ai.request.model": "saraswati-inhouse/credit-scoring/v3.2",
  "gen_ai.response.model": "saraswati-inhouse/credit-scoring/v3.2",
  "prompt": { "applicant_kyc_ref": "kyc/...", "loan_amount_inr": 75000, "tenor_months": 24 },
  "response": { "decision": "approve", "interest_rate_pct": 18.5, "limit_inr": 75000 },
  "audit.deployment.intent": "production",
  "audit.deployment.policy_version": "saraswati-prod-policy-v2.1",
  "audit.consent.lifecycle_state": "given",
  "audit.consent.legal_basis": "dpdp_act_2023_§6",
  "audit.consent.given_at_utc": "2026-05-19T13:08:42Z",
  "audit.consent.given_chain_ref": "saraswati/consent/2026-05-19#88412",
  "payload_hash": "...",
  "hmac": "...",
  "merkle_path": [...],
  "daily_seal_ref": "saraswati/2026-05-19#seal"
}
```

Mike ran the verifier in strict mode.

```
$ herald-verify --tenant=saraswati \
                --service=central-credit-decision \
                --date=2026-05-19 \
                --entry-id=184712 \
                --strict
```

```
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified
        against public key 9b:c4:11:...
Elapsed: 1.2s
```

Mike read the twelve fields aloud against the entry. Timestamp at millisecond resolution under UTC. Actor identity: branch officer Pankaj Joshi, authenticated via the institution's IAM under federated SSO. Process identity: `central-credit-decision` service, version 3.2.4. Input data: KYC reference + loan parameters. Output data: approve, 18.5% APR, ₹75,000 limit. Action performed: credit-decision evaluation. Model identifier: `saraswati-credit-v3.2`, version 3.2.4 sealed at 2026-04-29. Context: deployment intent production, policy version 2.1. Result: approval. Reasoning: model scoring rationale captured in the response payload. Hash chain: integrity proof at HMAC + Merkle path + daily seal. Tamper-evident integrity proof: Ed25519 signature against AWS CloudHSM root in `ap-south-1`.

All twelve fields verified cleanly.

> ### ✓ Confirmation #1 — All 12 fields verified on central inference path
> Four months of chain, ~210,000 credit-decision entries across the central path. Strict-mode verifier passes. Field 1 (timestamp UTC ms), Field 2 (federated SSO identity), Field 3 (process identity), Field 4 (input), Field 5 (output), Field 6 (action), Field 7 (model id + version), Field 8 (deployment context), Field 9 (outcome), Field 10 (reasoning), Field 11 (hash chain), Field 12 (Ed25519 daily seal under FIPS 140-2 Level 3+ HSM) — all satisfied in isolation.

*Note. The central inference path is a clean Kognitos read. If the architecture stopped here the engagement would close as a confirmation-posture pass and we would be done by lunch on Day 2. The architecture does not stop here.*

## 🛡️ 11:00 AM IST Day 1 — Edge inference path walkthrough

Sandeep Mehta took the bridge for the edge-side walk. He shared the Android Studio profile of the edge SDK and walked the audit team through what happens at a field-officer tablet when the credit decision is made offline.

A field credit officer in a rural branch in Odisha — call him Sunil Patnaik — opens an applicant interview at 14:24 IST. The tablet has been offline since 11:00 that morning; the cellular tower has been down. The interview proceeds. The applicant signs the consent screen at 14:31. The KYC photo is captured at 14:33. The credit-scoring inference runs on-device at 14:38 — the edge model is a quantized variant of the central model, 24 MB on the tablet, runs in 380 ms. Approval at 14:39, ₹50,000 limit at 22% APR — a higher rate than the central path because the edge model carries a conservative-margin offset to account for thin-file rural applicants.

Each of these events — consent, KYC capture, inference, approval — is captured as a chain entry in the tablet's offline-first SQLite buffer. Each entry carries a per-event MAC computed against a session key derived from a per-device key in the Android Keystore. The session key never leaves the Keystore. The MAC is recomputed at central reconciliation time when the tablet uploads.

The tablet remains offline until 19:15 IST when Sunil reaches a connected branch in Berhampur. The buffer drains in 4 minutes 12 seconds — 84 chain entries pushed, each with its per-event MAC, each verifying against the per-device session key. The central seal cuts at 23:00 UTC the next morning (04:30 IST Day 2). Between the credit decision at 14:39 IST and the seal cut at 04:30 IST Day 2 there are 14 hours and 51 minutes of integrity-claim asymmetry. During that window the entries exist with per-event MAC integrity but no central seal coverage.

Sandeep walked the audit team through what the chain entry actually looks like at the tablet.

```json
{
  "entry_id": "saraswati/edge-credit-decision/tablet-7b41c9.../2026-05-19#0184",
  "tenant": "saraswati",
  "service": "edge-credit-decision",
  "device_id": "tablet-7b41c903a8d2e4f7",
  "seq_device": 184,
  "ts": "2026-05-19T08:54:31.108Z",
  "model_id": "saraswati-credit-edge-v3.2",
  "model_version": "3.2.4-edge-2026-05-01",
  "audit.deployment.intent": "production",
  "audit.deployment.policy_version": "saraswati-prod-policy-v2.1",
  "audit.consent.lifecycle_state": "given",
  "audit.consent.legal_basis": "dpdp_act_2023_§6",
  "audit.consent.given_at_device_ts": "2026-05-19T08:47:12.000Z",
  "audit.edge.session_key_derivation": "HKDF(saraswati_base || '|' || saraswati || '|' || tablet-7b41c903a8d2e4f7)",
  "audit.edge.attestation_doc_sha256": "a7c2...4f81",
  "audit.edge.attestation_doc_kind": "android_keystore_tee",
  "audit.edge.late_arrival_seal_ref": "saraswati/2026-05-20#seal-supplemental",
  "audit.edge.merkle_subtree_root": "8b41...c903",
  "payload_hash": "...",
  "hmac_per_event_at_capture": "...",
  "hmac_reconciled_at_upload": "..."
}
```

Mike asked which fields the Kognitos verifier could check on this entry.

Chen and Dawn read the entry against the twelve fields. The first ten fields read normally — timestamp, identity (field officer Sunil Patnaik authenticated against the device's enrolled credentials), process identity, input, output, action, model id + version (`saraswati-credit-edge-v3.2`, version 3.2.4-edge sealed at 2026-05-01), context, result, reasoning. All ten read. Field 11 — hash chain — read partially: the per-event MAC was present and verified against the per-device session key, but the central seal coverage was 14 hours and 51 minutes lagged. Field 12 — tamper-evident integrity proof — read partially: the central daily seal eventually covered the entry once the late-arrival supplemental seal landed at the next-day's 23:00 UTC cut.

But the entry carried five attributes that the Kognitos schema had no field for at all: `audit.edge.session_key_derivation`, `audit.edge.attestation_doc_sha256`, `audit.edge.attestation_doc_kind`, `audit.edge.late_arrival_seal_ref`, `audit.edge.merkle_subtree_root`.

Chen marked the entry up in the running notes.

*Note. The edge entry has every Kognitos field satisfied at least nominally — but five attributes that carry the actual integrity claims for the edge case have no Kognitos field to land in. The framework does not have vocabulary for per-device key derivation, TEE attestation, late-arrival seal discipline, or hierarchical Merkle aggregation. We can record that the entry has integrity. We cannot record what kind of integrity it has, against which surface, with what compensation for the SDK-process compromise residual.*

> ### ⚠ Framework Inarticulability #1 — Per-device session key derivation has no Kognitos field
> The edge entry carries `audit.edge.session_key_derivation = "HKDF(saraswati_base || '|' || saraswati || '|' || tablet-7b41c903a8d2e4f7)"`. The derivation binds the MAC to the specific tablet — a compromised device's session key cannot forge entries for any other device. The Kognitos schema has Field 11 (tamper-evident integrity / hash chains) but no per-device key-derivation vocabulary. The Kognitos auditor can record that the entry has an integrity proof. They cannot record the *scope* of that proof. Under the reference spec this lands at §10.32. Under Kognitos it lands nowhere.

> ### ⚠ Framework Inarticulability #2 — Edge-attestation primitive has no Kognitos field
> Each edge entry carries `audit.edge.attestation_doc_sha256` referencing an Android Keystore TEE attestation document. The document binds device hardware-integrity state at the moment of chain-entry production — TEE attestation root, attestation chain to Google's root key, hardware-backed key generation, no rooted/jailbroken-device pollution. The Kognitos schema has no field for hardware attestation. The integrity-strengthening at the edge — the partial compensation for the SDK-process compromise residual that §1.2 of the reference spec names explicitly — is invisible to the framework. Under the reference spec this lands at §10.35. Under Kognitos it lands nowhere.

> ### ⚠ Framework Inarticulability #3 — Late-arriving-entry seal discipline has no Kognitos field
> The edge entry was produced at 14:39 IST 2026-05-19; the central daily seal cut at 04:30 IST 2026-05-20; the supplemental seal that covered the late-arrival entry landed at 04:30 IST 2026-05-21. The Kognitos schema has a hash-chain integrity field (Field 11) that assumes contemporaneous capture — the chain is sealed when the entry is produced. There is no vocabulary for an entry that exists with per-event MAC integrity but no central seal coverage for fourteen-plus hours, then gets covered by a supplemental seal the following day. The reference spec calls this Pattern A late-arrival seal discipline at §10.36. Under Kognitos it lands nowhere — the framework either says the chain is sealed or it isn't, with no third state for late-arrival-with-supplemental-seal.

> ### ⚠ Framework Inarticulability #4 — Hierarchical Merkle aggregation has no Kognitos field
> The edge entry carries `audit.edge.merkle_subtree_root` — the entry sits inside a per-device Merkle subtree that, in turn, sits as a leaf in the daily central Merkle seal. Two-level aggregation is bandwidth-efficient: when a tablet returns from a week of no-cellular operation it pushes only its subtree root plus the entries it produced, not the entire global chain. The Kognitos schema has Field 11 hash chains but no two-level Merkle aggregation vocabulary. The bandwidth-efficient verification path for offline-first edge devices is invisible to the framework. Under the reference spec this lands at §10.37. Under Kognitos it lands nowhere.

Diana joined from the IAM side. *Field 2 reads the field officer's identity cleanly. Field 11 reads the central-seal integrity cleanly. Neither field has anything to say about the per-device key scope. If a compromised tablet's session key surfaced in the chain claiming to be a different tablet, Kognitos would not flag it — the framework has no vocabulary for the scope of the proof.*

## 💳 1:30 PM IST Day 1 — Federated-learning aggregator walkthrough

After a working lunch in the BKC tower's eleventh-floor canteen, Sandeep and Vikram walked the audit team through the federated-learning cycle.

The cycle runs monthly. On Day 1 of each month the central team trains a new candidate global model using federated aggregation — each tablet that has been online during the prior month uploads a gradient computed against its local on-device data without uploading the underlying data itself; the central aggregator combines the gradients into a new global model; the new model is validated against a held-out test set; the model is then sealed as a model artifact. On Day 29 the central team pushes the new global model to all 15,000 tablets. Each tablet pulls the model, verifies the signature against the central HSM, activates the new model, and records `audit.model_update.activate` as a chain entry on the device.

The architecture has been running this cycle for four months — four full federated-learning cycles since the system went into production. Each cycle has produced:

- A `local_gradient` event on each participating tablet (~12,000 tablets per cycle, the others offline or out-of-cycle)
- An `aggregation` event at the central aggregator combining the gradients
- A `validation` event at the central aggregator validating the new model against the held-out test set
- A `model_artifact` event sealing the new model with a SHA-256 hash and Ed25519 signature
- 15,000 `push` events (central side, one per device)
- 15,000 `pull/verify/activate` events (device side, one per device)

Sandeep showed the chain. The central side had the `push` and `model_artifact` events recorded. The device side had the `pull/verify/activate` events recorded.

The `local_gradient`, `aggregation`, and `validation` events were not in the chain. They existed in MLflow run records, in the federated-aggregator's own logs, in the central S3 bucket holding the model artifacts. But they were not in the audit-trail chain.

Mike pulled the chain entry for a recent `model_artifact` event:

```json
{
  "entry_id": "saraswati/federated-aggregation/2026-05-01#0042",
  "tenant": "saraswati",
  "service": "federated-aggregation",
  "seq": 42,
  "ts": "2026-05-01T13:42:08.882Z",
  "audit.deployment.intent": "production",
  "audit.training.event_kind": "model_artifact_seal",
  "audit.training.model_artifact_sha256": "d4f1...c803",
  "audit.training.model_artifact_size_bytes": 25165824,
  "audit.training.cycle_number": 4,
  "audit.training.gradient_contributor_count": 12042,
  "audit.training.aggregation_method": "FedAvg",
  "audit.training.validation_holdout_set_ref": "saraswati-validation-holdout-v2",
  "audit.training.validation_metric_set_ref": "saraswati-validation-metrics-2026-05-01",
  "payload_hash": "...",
  "hmac": "...",
  "daily_seal_ref": "saraswati/2026-05-01#seal"
}
```

Sandeep walked the audit team through what the entry was claiming and what it was *not* claiming. The entry asserted that a model artifact with SHA-256 `d4f1...c803` was produced on 2026-05-01 from a federated-aggregation cycle involving 12,042 gradient contributors using FedAvg aggregation. The entry did not include any of the gradient contributors themselves; it did not include the aggregation operation; it did not include the validation outcome.

For the validation outcome, Saraswati's MRM committee had been relying on MLflow run records — a separate system, not chain-bound. Vikram acknowledged that the gap was deliberate at the time of the system's design four months ago. The training-phase activity was high-volume and the chain was sized for inference-phase capture; he had not wanted to expand the chain's storage footprint by an order of magnitude.

Chen marked the gap in the running notes.

*Note. The chain captures the deployment-phase boundary moments — push, pull, verify, activate, model artifact seal. It does not capture the training-phase events themselves. The gradient contributions, the aggregation operation, the validation outcome — these live in MLflow, not the chain. From the Kognitos framework's perspective there is no field for training-phase events; the framework's twelve fields cover the inference-phase audit trail. The gap on the Saraswati side is twofold: their chain doesn't capture it, and the framework wouldn't have a place to put it if it did.*

> ### ⚠ Framework Inarticulability #5 — Training-phase integrity has no Kognitos field
> The Kognitos schema's twelve fields are oriented to inference-phase audit-trail capture (an input arrives, a model evaluates, an output is produced, a decision is taken). The federated-learning cycle's training-phase events — `local_gradient`, `aggregation`, `validation`, `model_artifact` — are first-class events under a training-phase integrity model. The Kognitos framework has Field 7 (model id + version) which can record *which* model was used at inference time, but no vocabulary for *how the model was produced* — the gradient contributions, the aggregation operation, the validation against held-out test set. Under the reference spec this lands at §10.34 with §10.64 as the broader training-run primitive. Under Kognitos it lands nowhere.

> ### ◇ Framework-Silent Observation #12 — Model-update boundary moments captured but framework can't read them as a cycle
> The chain records push/pull/verify/activate events for each of the 15,000 tablets at each monthly cycle. The Kognitos schema reads each individual event under Field 7 (model id + version changes) and Field 11 (hash chain). The framework cannot read these events *as a federated-cycle event sequence* — it has no concept of cycle, no concept of cycle number, no concept of monthly cadence. The cycle structure exists in the chain (`audit.training.cycle_number = 4`) but the framework is silent on it. Under the reference spec the cycle is named at §10.33. Under Kognitos the events exist but the cycle does not.

## ⚡ 4:00 PM IST Day 1 — DPDP Act §6 consent lifecycle walkthrough

Aparna Desai took the room for the consent-lifecycle walk. The DPDP Act 2023 had come into force eighteen months earlier and Aparna's first six months on the DPO role had been spent rebuilding the institution's consent capture from the ground up. The result was a four-state consent lifecycle bound to every credit-decision chain entry touching an Indian borrower: `given`, `referenced`, `withdrawn`, `expired`.

A consent record is created when an applicant first agrees to processing — that produces an `audit.consent.given` chain entry with a unique consent ID, the legal basis (`dpdp_act_2023_§6`), the timestamp, the field officer who captured the consent, and the device or branch where it was captured. Every subsequent credit-decision chain entry references the consent ID. If the borrower withdraws consent, the chain captures an `audit.consent.withdrawn` event. If the consent record reaches its retention floor without renewal, the chain captures an `audit.consent.expired` event.

Aparna walked through the May 19 example. The branch officer Pankaj Joshi captured the fruit vendor's consent at 13:08:42 UTC on 2026-05-19, producing chain entry `saraswati/consent/2026-05-19#88412`. The credit-decision entry four minutes later carried `audit.consent.given_chain_ref = "saraswati/consent/2026-05-19#88412"`. The two entries were chain-bound — verifier could follow the reference from the credit decision to the consent record.

```json
{
  "entry_id": "saraswati/consent/2026-05-19#88412",
  "tenant": "saraswati",
  "service": "central-credit-decision",
  "seq": 88412,
  "ts": "2026-05-19T13:08:42.108Z",
  "audit.consent.lifecycle_state": "given",
  "audit.consent.consent_id": "consent-saraswati-2026-05-19-88412",
  "audit.consent.legal_basis": "dpdp_act_2023_§6",
  "audit.consent.purpose": "credit_evaluation_and_decision",
  "audit.consent.subject_borrower_ref": "kyc/...",
  "audit.consent.captured_by_actor": "pankaj.joshi@saraswati.in",
  "audit.consent.captured_at_branch": "branch-mumbai-dadar",
  "audit.consent.retention_expires_at_utc": "2031-05-19T13:08:42Z",
  "payload_hash": "...",
  "hmac": "...",
  "daily_seal_ref": "saraswati/2026-05-19#seal"
}
```

Mike ran the verifier with the consent-lookup flag.

```
$ herald-verify --tenant=saraswati \
                --service=central-credit-decision \
                --date=2026-05-19 \
                --entry-id=184712 \
                --strict \
                --consent-lookup
```

```
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified;
        consent reference saraswati/consent/2026-05-19#88412
        resolved, lifecycle state = "given", legal basis
        = "dpdp_act_2023_§6", retention expires
        2031-05-19T13:08:42Z
Elapsed: 1.4s
```

Elena worked through the Kognitos read. *Field 2 — actor identity — has the branch officer who captured the consent. Field 4 — input data — has the consent payload. Field 6 — action — would say "consent_captured" if we wrote it that way. Field 8 — context — could carry the legal basis. Field 11 — hash chain — carries integrity. But there is no Kognitos field for the lifecycle state. There is no field that says: this consent record is currently given, currently withdrawn, currently expired. There is no field that says: this credit decision is bound to consent record X, and if consent record X transitions to withdrawn the credit decision needs to be reviewed.*

She marked the entry in the running notes.

> ### ◇ Framework-Silent Observation #13 — DPDP Act §6 consent lifecycle bound to chain entries but framework can't read the lifecycle as state
> The chain captures a four-state consent lifecycle (`given`, `referenced`, `withdrawn`, `expired`) with cryptographic binding from each credit-decision entry to its source consent record. The Kognitos framework reads the consent capture as a Field 4 input + Field 6 action, and reads the credit-decision binding as a Field 8 context attribute. The framework cannot read the lifecycle *as state* — there is no field for "this consent is currently in state X and if it transitions to state Y the bound decisions need review." Under the reference spec this lands at §10.38 with explicit DPDP Act §6 legal-basis tagging. Under Kognitos the lifecycle exists in the chain but the framework cannot read it as a lifecycle.

*Note. Aparna's posture during the walk was professional but tight. She has been carrying DPDP Act compliance for eighteen months and she has built the consent lifecycle into the chain because the act requires revocability and traceability. She watches us read the chain entries one at a time without any way to express "what is the current state of consent N across the 184,712 credit decisions that reference it." The framework is reading every entry. It is not reading the lifecycle.*

## 🌆 5:00 PM IST Day 1 — Auditor Debrief — Whiteboard tally

Dawn wrote the day's tally on the whiteboard in the fourteenth-floor conference room. The team had stayed past 17:00 to compose it before the late-evening US-Eastern bridge opened at 19:30.

```
KOGNITOS 12-FIELD ASSESSMENT — SARASWATI MICROFINANCE (DAY 1 / 3)

AI SIDE — CENTRAL-CREDIT-DECISION SERVICE:
  Confirmations:                  1 (12-of-12 fields verified, 4 months chain)
  Partials:                       0
  Findings against client:        0
  Framework-silent observations:  0
  -- The central path reads clean.

AI SIDE — EDGE-CREDIT-DECISION SERVICE (15,000 tablets):
  Confirmations:                  0 (Kognitos reads 10 fields nominally;
                                     5 attributes have no field)
  Partials:                       2 (Field 11 lagged by 14-15 hrs;
                                     Field 12 covered late by supplemental seal)
  Findings against client:        0
  Framework-silent observations:  0
  Framework inarticulabilities:   4 (per-device key derivation; edge attestation;
                                     late-arrival seal discipline; hierarchical Merkle)

AI SIDE — FEDERATED-AGGREGATION SERVICE (monthly cycle):
  Confirmations:                  0
  Partials:                       0
  Findings against client:        0 (the gap is real but it is a framework gap,
                                     not a client gap — client captures everything
                                     the framework can hold)
  Framework-silent observations:  1 (model-update cycle structure invisible)
  Framework inarticulabilities:   1 (training-phase integrity)

CONSENT LIFECYCLE — DPDP ACT §6:
  Confirmations:                  0
  Partials:                       1 (Field 4 + Field 8 + Field 11 read; lifecycle invisible)
  Framework-silent observations:  1 (lifecycle as state invisible)

CROSS-ZONE / FRAMEWORK-SIDE:
  Framework Inarticulability:     5 new (§10.32 + §10.35 + §10.36 + §10.37 + §10.34)
  Framework Silence:              2 new (§10.33 cycle; §10.38 lifecycle)
```

ENGAGEMENT-TEAM OBSERVATIONS ON FRAMEWORK SELECTION:

1. The central inference path reads clean under Kognitos. If Saraswati's architecture stopped at the central path, the engagement would close as a confirmation-posture pass.
2. The edge inference path has 14-15 hour integrity-claim asymmetry between per-event MAC and central seal coverage. The Kognitos schema does not have vocabulary for either the per-event MAC scope or the supplemental-seal mechanism that closes the asymmetry.
3. The federated-learning cycle's training-phase events are not in the chain. The architectural choice on the Saraswati side is defensible (storage-footprint sizing four months ago). The framework gap is the more consequential issue — even if Saraswati added training-phase events to the chain tomorrow, the Kognitos schema would not have a field for them.
4. The DPDP Act §6 consent lifecycle is operationally bound to credit decisions via chain references. The Kognitos schema reads each entry but cannot read the lifecycle as state. A lifecycle-driven query — "give me all credit decisions bound to consent records currently in withdrawn state" — has no framework expression.
5. The RBI Master Direction 2024 update has explicit AI-governance expectations around training-phase integrity, edge integrity, and consent lifecycle. The Kognitos memo we would write today does not address those expectations because the framework's twelve fields do not address them.

## 📞 7:30 PM IST Day 1 — Late-evening bridge with US-Eastern team

The audit team moved to the BKC tower's seventh-floor video-bridge room at 19:15 IST. The connection to the US-Eastern side opened at 19:30 IST (10:00 AM EDT). Two team members were on the bridge: Chen joining from Boston and a fifth audit-team consultant who reviewed framework-selection memos.

The bridge ran for ninety minutes. Chen walked the US-Eastern side through the day's findings: 5 new Framework Inarticulabilities, 2 new Framework-Silent Observations, central path clean, edge and federated surfaces structurally invisible to the framework.

The bridge produced one tactical decision and one strategic concern.

Tactical decision: on Day 2 the team would walk the ten-credit-decision diversity matrix with explicit framework-vs-reference annotation — every entry would be annotated with what the Kognitos schema could read and what the reference spec could additionally read. The annotation would form the cover-memo backbone for the Day 3 deliverable.

Strategic concern: the engagement was producing five Framework Inarticulabilities on Day 1, and the RBI Master Direction 2024 update had explicit AI-governance expectations across exactly the surfaces where the framework was silent. The Day 3 memo would need to name the framework gap honestly. The institution had requested an audit-readiness pass; the team would deliver one, but the deliverable would necessarily flag that the framework chosen for the audit did not have vocabulary for the architecture under audit. That was a writing-the-memo problem; the bridge agreed it was Aparna and Vikram's call whether the memo went on the record.

*Note. The US-Eastern review confirms what the Mumbai team has been seeing all day. The framework is structurally narrower than the architecture. The honest memo names that. The Day 3 question is whether Saraswati's stakeholders are willing to put the framework-gap statement on the record.*

## 📋 9:00 AM IST Day 2 — Diversity matrix reconciliation (10 credit decisions)

Day 2 opened in the fourteenth-floor conference room. The team walked the ten-credit-decision diversity matrix that Sandeep and Vikram had prepared: rural Maharashtra woman applicant approved at the central path; urban Mumbai male applicant declined at the edge path; pre-rollout (cycle 1) vs post-rollout (cycle 4) decisions; a retired-tablet case where the tablet was decommissioned in March 2026 and the field officer's last credit decision was uploaded from the replacement tablet; a disputed-override case where the central path approval was overridden by branch manager discretion at +2.5% APR; a KYC-failed case where the consent was captured but the KYC reference resolved to a no-match and the decision was declined at the consent step; a repaying-on-schedule case where the borrower's six-month-prior credit decision was still in active loan-servicing chain; a declined-then-complained case where the borrower had filed a DPDP grievance under §13.

Each case was walked against the chain. Each case was annotated with the Kognitos read vs the reference-spec read.

The retired-tablet case was the most consequential walk. Tablet `tablet-3c4f12a8e904b1d7` had been retired on 2026-03-14 after three years of field service. The session key for the retired tablet had been derived under the institution's prior HKDF base key — the institution had rotated the base key on 2026-03-15. The chain entries produced by the retired tablet between 2025-09 and 2026-03-14 were sealed under the prior base key; the entries produced by the replacement tablet from 2026-03-15 onward were sealed under the new base key. The chain coverage spanned the rotation boundary.

Mike ran the verifier across the rotation.

```
$ herald-verify --tenant=saraswati \
                --service=edge-credit-decision \
                --device=tablet-3c4f12a8e904b1d7 \
                --span=2025-09-01:2026-03-14 \
                --span=replacement-2026-03-15:current \
                --strict \
                --rotation-walk
```

```
Status: PASS
Step:   12 (executed across rotation boundary at step 7)
Reason: chain integrity verified across IKM rotation;
        old-base-key HMAC validated for 2025-09 through 2026-03-14;
        new-base-key HMAC validated for 2026-03-15 through current;
        Merkle path resolved across both eras;
        signatures verified against AWS CloudHSM ap-south-1 root
Elapsed: 2.8s
```

> ### ✓ Confirmation #2 — Field 11 + Field 12 satisfied across an IKM rotation boundary
> The retired-tablet case exercised an HKDF base-key rotation that crossed the seal boundary. Both sides of the rotation verified under Kognitos. The framework reads the integrity claim cleanly — but it does not read the rotation as a *rotation event*; the rotation moment lives in the institution's key-management runbook, not in the chain.

> ### ◇ Framework-Silent Observation #14 — IKM rotation across seal boundary executed cleanly but framework can't read the rotation as an event
> The rotation moment is an operational discontinuity in the cryptographic substrate. Under the reference spec at §10.10 the rotation produces a chain-inscribed event that names the rotation, the prior root, the new root, and the seal-boundary crossing. The Kognitos schema has Field 11 + Field 12 covering the integrity proof on both sides of the rotation but no field for the rotation event itself. The institution's compensation is operational documentation in the runbook. The framework's compensation is none.

The disputed-override case surfaced a more subtle gap. Branch manager Mahesh Iyer (no relation to Vikram) had overridden a 17% APR central recommendation to 19.5% APR on 2026-04-22, citing borrower-risk discretion. The chain recorded the override as a chain entry with `audit.decision.override_kind = "branch_manager_discretion"`, `audit.decision.override_apr_delta_pct = 2.5`, `audit.decision.override_actor = "mahesh.iyer@saraswati.in"`, `audit.decision.override_rationale_ref = "manual-rationale-document/2026-04-22#0814"`.

Kognitos Field 10 (reasoning) carried the rationale reference. Field 2 carried the override actor. Field 5 captured the override outcome. But the *override-vs-base-decision* binding — the structural fact that a separate human action overrode an earlier model decision, with both decisions chain-bound and both readable — had no specific Kognitos representation.

Elena flagged it. *The chain represents the override as a discrete entry that references the prior model decision. The model decision and the override decision both exist in the chain. Kognitos reads both entries cleanly but cannot read the binding between them — that the second entry is a manual override of the first. Under the reference spec the binding is structural; under Kognitos it is implicit in the timestamps and the actor identities.*

> ### ◇ Framework-Silent Observation #15 — Manual override of model decision captured as paired chain entries but framework can't read the pairing
> The chain records both the model decision and the override as discrete entries with explicit binding (`audit.decision.override_of_chain_ref`). Kognitos reads each entry under all twelve fields. The framework cannot read the *pairing* — the structural fact that the second entry is a manual override of the first. The pairing is recoverable by an analyst reading the chain entries sequentially with engagement-specific knowledge. It is not recoverable by a verifier following the framework's twelve fields.

The KYC-failed case closed the morning. The applicant — call him Ravi Sharma, a Bengaluru urban professional — had attempted a loan application on 2026-04-08. The consent step captured cleanly. The KYC reference resolved to a no-match against the central KYC repository — the applicant had used a recently-updated PAN-Aadhaar linkage that had not yet propagated to the institution's KYC mirror. The credit-decision step was declined at the KYC validation point with `audit.kyc.outcome = "no_match"` and no further model evaluation. The chain captured all three events (consent, KYC, decision-decline-at-kyc) with full integrity.

Kognitos read the three entries cleanly across all twelve fields. The framework's read confirmed: input arrived (consent + applicant data), action performed (KYC lookup), outcome (no-match decline). The reference spec adds nothing here beyond what Kognitos reads — Field 6 (action) + Field 9 (outcome) + Field 10 (reasoning) cover the KYC decline.

> ### ✓ Confirmation #3 — KYC-failed decline read cleanly under all twelve fields
> The KYC-no-match decline is a clean Kognitos read. No framework inarticulability surfaces here. The reference spec does not add framework vocabulary at this boundary because the inference-phase nature of the event is exactly what the Kognitos schema was designed to capture.

## 🔧 11:30 AM IST Day 2 — Federated-aggregator deep walk

After the diversity-matrix morning, Sandeep took the room for a deep walk of the federated-aggregator's training-phase activity. He pulled the MLflow run record for cycle 4 — the most recent cycle, completed 2026-05-01.

The MLflow record showed 12,042 gradient contributors over a four-hour aggregation window on 2026-05-01. The FedAvg aggregation produced a candidate model at 13:08 UTC. The candidate model was validated against the held-out test set — 47,000 historical credit decisions from 2024-2025 that had been excluded from the training data on principle — producing a validation outcome of 0.847 AUC, marginally improved over cycle 3's 0.842 AUC. The model was sealed as artifact `d4f1...c803` at 13:42 UTC. The model artifact then propagated to all 15,000 tablets between 2026-05-01 and 2026-05-04.

The audit team had four hours to understand whether the validation discipline matched the institution's MRM committee expectations.

Vikram walked through what the MRM committee saw: a quarterly review of the federated-learning cycle's validation outcomes, comparing the new model's AUC against the prior cycle's AUC, flagging any cycle where AUC declined or where the validation-population coverage was insufficient. The committee had approved cycle 4 on 2026-05-03 with a routine sign-off.

The audit team had four issues with the MRM committee's posture:

1. The validation outcomes were captured in MLflow, not the chain. If MLflow's database was compromised or its records altered, there would be no cross-reference to the chain because the chain didn't capture the validation event.
2. The held-out test set itself was not chain-bound. The held-out test set was a SQL query against the historical credit-decision database with a deterministic seed; the seed and the query were documented in a Confluence page that the MRM committee referenced. The Confluence page was not chain-bound. The held-out test set could in principle be tampered with.
3. The FedAvg aggregation operation was a single line of Python code in the federated-aggregator. The aggregation operation was deterministic given the gradient inputs and the prior model — but the gradient inputs were captured only in transient memory at the aggregator and were destroyed after aggregation. The aggregation could not be re-run for verification.
4. The local-gradient events on the tablets were ephemeral. They were computed at the tablet from on-device data, MAC'd, transmitted to the aggregator, used for aggregation, and discarded at the tablet at session end. The chain captured nothing about them — the framework had no place to put them.

The four issues mapped directly to four spec sections in the reference (§10.34 + §10.64 + §10.37 + §10.32) but mapped to *zero* Kognitos fields. The framework had no vocabulary for any of the four.

Chen marked the issues in the running notes as Framework Inarticulabilities #6, #7, #8, #9 — though structurally they reduced to a single inarticulability: training-phase integrity has no Kognitos field. The four issues were sub-aspects of the same gap.

*Note. The MRM committee is doing competent work. The validation discipline is real — the held-out test set is genuinely held out, the AUC tracking is meaningful, the quarterly sign-off is documented. The gap is not in the institution's discipline; the gap is in what the chain captures and what the framework can read of what the chain captures. Under the reference spec the four issues are addressable. Under Kognitos they are structurally invisible.*

> ### ⚠ Framework Inarticulability #5 (expanded) — Training-phase integrity has four sub-aspects, none of which Kognitos can express
> (i) validation outcome chain-binding (§10.34); (ii) held-out test set chain-binding (§10.64); (iii) aggregation operation reproducibility (§10.34 + §10.37); (iv) local-gradient capture beyond ephemeral memory (§10.32 + §10.34). The reference spec addresses all four sub-aspects with explicit chain-binding vocabulary. The Kognitos schema addresses none of the four. The MRM committee's quarterly sign-off is the institution's compensation; under Kognitos the chain cannot demonstrate the MRM discipline because there are no entries to verify.

## 🛡️ 2:30 PM IST Day 2 — Aparna's on-the-record statement

After lunch Aparna asked for the room to herself with the audit team. Vikram and Rohit stepped out at her request; Neha stayed. Aparna had a one-page memo in her hand, drafted overnight. She had read Day 1's whiteboard tally before the team had left for the bridge.

She read the memo aloud.

The DPDP Act 2023 had come into force eighteen months earlier. Section 6 required explicit, informed, and revocable consent for every processing of personal data. The Data Protection Board of India was empowered to levy administrative penalties up to ₹250 crore for non-compliance. The institution had built the consent lifecycle into the chain because revocability and traceability had to be cryptographically demonstrable, not merely operationally documented.

The Kognitos audit-trail framework was, in her professional reading, acceptable as a baseline AI-audit-trail standard for the central inference path. It was not acceptable as a standalone framework for an institution that had to demonstrate DPDP Act §6 consent-lifecycle compliance. The framework's silence on lifecycle-as-state was not a minor gap — it was the structural reason her DPO function could not rely on the framework alone to defend the institution before the Data Protection Board if a consent-revocation grievance arose.

The institution would continue to capture the consent lifecycle in the chain. The institution would also continue to maintain a parallel consent-lifecycle index outside the chain, populated by the chain's lifecycle events, that the DPO function could query against. The parallel index was operational compensation for the framework's silence.

She wanted this on the record because if the RBI inspector arrived in nine weeks and asked "is your AI audit-trail framework sufficient for DPDP Act §6 compliance," the institution's answer needed to be: the framework is sufficient as a baseline; the institution's own operational compensation closes the framework's silence on lifecycle-as-state. The compensation was the institution's; the gap was the framework's.

On the record.

Dawn replied: On the record.

> ### Stakeholder explicit-attribution statement #1 (chapter-local; program-wide TBD on running doc)
> Aparna Desai (DPO, Saraswati Microfinance) — direct boundary-setting voice pattern. "The framework is acceptable as a baseline AI-audit-trail standard for the central inference path. It is not acceptable as a standalone framework for an institution that must demonstrate DPDP Act §6 consent-lifecycle compliance." The institution's parallel consent-lifecycle index is operational compensation for the framework's silence. On the record.

*Note. This is the cleanest direct-boundary-setting statement since Veronika at Atrio (Ch04). Aparna names the framework's gap as a gap, names the institution's compensation as compensation, names the DPDP penalty exposure as the reason both have to be on the record. The voice is Veronika's voice — regulator-readable, gap-naming, compensation-claiming, no hedging.*

## 🔧 4:00 PM IST Day 2 — Vikram's framework-gap memo draft

After Aparna's statement Vikram returned to the room with a draft memo of his own. He had also read Day 1's whiteboard tally and he had spent the morning reading the RBI Master Direction 2024 update against the team's findings. He did not want to read his memo as an on-the-record statement — he wanted to walk the team through his draft and ask whether it would survive RBI inspection.

The draft was three pages. Page 1 named the engagement's three integrity surfaces and the Kognitos framework's read on each. Page 2 named the seven framework inarticulabilities and the operational compensation the institution maintained for each. Page 3 named the RBI Master Direction 2024 update's specific AI-governance clauses and mapped the institution's compensation to each clause.

The draft was honest. It did not claim that the Kognitos framework was sufficient for the institution's RBI-facing posture; it claimed that the framework was sufficient for the central inference path and that the institution's operational compensation closed the gaps at the edge, federated, and consent-lifecycle surfaces. The RBI Master Direction clauses were addressed by the combination of framework + compensation, not by the framework alone.

Dawn read the draft. The team read it. Chen marked the structural shape of the memo as a model for future engagements where framework + compensation jointly defend a regulator-facing posture.

The team had two refinements to suggest. First, the memo should explicitly name where the compensation lives — runbook, MLflow, Confluence, parallel index — so an RBI inspector could verify the compensation independently. Second, the memo should name the framework alternative that would close the gap structurally (the reference spec) and acknowledge that the institution had not adopted it as of this engagement; that acknowledgment was honest and would land better with an inspector than silence.

Vikram took both refinements. The memo would land on the RBI's desk as the institution's audit-readiness response.

*Note. Vikram is doing what Aparna did but at the institution-wide AI-governance level. He is naming the framework as a baseline, naming the compensation as compensation, and naming the alternative framework that would close the gap. The RBI inspector arriving in nine weeks will see a posture that is defensible because it is honest about its own structure. The institution's discipline is what closes the gap; the framework's silence is documented.*

## 🌆 5:30 PM IST Day 2 — Auditor Debrief — Whiteboard tally update

```
KOGNITOS 12-FIELD ASSESSMENT — SARASWATI MICROFINANCE (DAY 2 / 3)

CUMULATIVE THROUGH DAY 2:
  Confirmations:                  3 (central path 12-of-12;
                                     IKM rotation across seal boundary;
                                     KYC-no-match decline)
  Partials:                       3 (edge: Field 11 lagged + Field 12 covered late;
                                     consent: lifecycle invisible)
  Findings against client:        0
  Framework-silent observations:  4 (model-update cycle; DPDP lifecycle state;
                                     IKM rotation as event; manual override pairing)
  Framework Inarticulabilities:   5 (per-device key; edge attestation;
                                     late-arrival seal; hierarchical Merkle;
                                     training-phase integrity)

STAKEHOLDER EXPLICIT-ATTRIBUTION STATEMENTS:
  1 (Aparna Desai, DPO, direct boundary-setting; DPDP §6 compliance)

UPCOMING DAY 3:
  Memo composition + delivery 09:00 IST
  Engagement close 12:00 IST
```

ENGAGEMENT-TEAM OBSERVATIONS ON FRAMEWORK SELECTION:

1. The chapter has produced more Framework Inarticulabilities (5) than any prior chapter in the program. The architecture is structurally wider than the framework's vocabulary at three surfaces simultaneously (edge, federated, consent-lifecycle).
2. The institution's operational compensation across all three surfaces is real and demonstrable. The chain captures what the framework can hold; the institution's operational systems (runbook, MLflow, Confluence, parallel index) capture what the framework cannot. The combined posture is defensible.
3. Aparna's on-the-record statement is the chapter's central event. The DPO function has explicitly named the framework gap as a gap and named the institution's compensation as compensation. The regulator-facing posture is honest.
4. Vikram's memo extends Aparna's framework-side claim to the institution-wide AI-governance level. The RBI Master Direction 2024 update is the relevant regulator surface; the institution's posture against the update is framework + compensation, not framework alone.
5. The reference spec (FFIEC chain-of-custody) appears in Vikram's memo as the structurally-superior alternative — explicitly named, not adopted as of this engagement, acknowledged as the framework that would close the gaps if adopted. The honesty lands.

## 📋 9:00 AM IST Day 3 — Spec-section confirmation memo delivery

Day 3 opened with the formal memo delivery. The team had drafted overnight; the institution had reviewed before breakfast.

The memo was four pages. Page 1: scope and methodology — three-day engagement, Kognitos 12-field assessment, three integrity surfaces (central, edge, federated), DPDP Act §6 consent-lifecycle binding. Page 2: findings summary — 3 confirmations, 3 partials, 0 findings against the institution, 4 framework-silent observations, 5 framework inarticulabilities. Page 3: stakeholder explicit-attribution — Aparna Desai's direct boundary-setting statement reproduced verbatim. Page 4: institutional compensation matrix — for each of the 5 framework inarticulabilities, the operational compensation the institution maintains, the system where the compensation lives, and the RBI Master Direction 2024 clause that the compensation addresses.

Rohit Bhandari took the memo at 09:42 IST. He spent forty minutes reading it cover to cover. He had two questions. First: was the memo's framework-gap claim defensible at the IT-Ministry level if a DPDP grievance arose; Aparna confirmed yes. Second: would the audit team be willing to be cited in the institution's CC8.1 control description as the framework's first formal assessor; Dawn confirmed yes.

Rohit signed off on the engagement at 10:42 IST. Vikram countersigned at 10:48 IST. Neha countersigned at 11:02 IST. Aparna countersigned at 11:14 IST, with a separate note appended that the institution's DPO function would maintain ongoing review of the consent-lifecycle index against the chain and would re-engage the audit team if a DPDP grievance surfaced.

The engagement closed at 12:00 IST exactly. The institution provided a working lunch at the BKC tower's eleventh-floor canteen. The audit team's return flight to Boston via Doha was scheduled for 22:35 IST.

## 🧾 Final Assessment Theme

> "Saraswati Microfinance closes a three-day Kognitos-lens audit-readiness pass with three integrity surfaces under review: central inference, edge inference across 15,000 ruggedized Android tablets, and a monthly federated-learning cycle. The Kognitos 12-field schema reads the central path cleanly under all twelve fields. The schema has no vocabulary for the per-device key derivation, the Android Keystore TEE attestation, the late-arrival seal discipline, the hierarchical Merkle aggregation, the training-phase integrity events, the federated-cycle structure, or the DPDP Act §6 consent-lifecycle state — seven framework-side gaps across the edge, federated, and consent surfaces. The institution's operational compensation across all seven gaps is real (key-management runbook; MLflow training-phase records; Confluence held-out test set documentation; parallel consent-lifecycle index) and demonstrable. The memo lands as framework + compensation, not framework alone. Aparna Desai (DPO) names the framework's silence on consent-lifecycle-as-state as a structural gap that the institution's parallel index closes operationally; the statement is on the record. Vikram Iyer (CAIO) extends the framework-gap claim to the institution-wide AI-governance posture under the RBI Master Direction 2024 update, explicitly naming the FFIEC chain-of-custody reference spec as the framework that would close the gaps structurally if adopted. The engagement closes at 12:00 IST with all four stakeholder sign-offs and zero findings against the institution; the chapter is the program's first engagement where framework inarticulability outnumbers framework confirmation by a margin of 5-to-3 on the AI side."

## Research takeaway

Saraswati is the program's first engagement where the architecture is structurally wider than the framework's vocabulary across three integrity surfaces simultaneously. The pattern is distinct from the prior under-reporting / inarticulability chapters in that the institution itself has built operational compensation for every gap — the chapter is not about institutional discipline (which is exemplary) but about framework reach.

- Compared to Atrio (Ch04): Atrio surfaced a single framework-side inarticulability (tenant-isolation binding). Saraswati surfaces five at three surfaces. Same direct-boundary-setting voice pattern from the institutional liaison (Veronika at Atrio; Aparna at Saraswati).
- Compared to Hill Country (Ch12): Hill Country closed confirmation-posture with framework + reference jointly reading the architecture cleanly. Saraswati closes with framework + operational compensation, where the reference spec is named as the structurally-superior alternative but not adopted. The honest acknowledgment of the alternative is the new editorial signal.
- Compared to the reference spec wishlist on the FFIEC side: the reference spec exercises §10.32-§10.38 in production at one institution; under Kognitos the same architecture produces five Framework Inarticulabilities and zero confirmations on the edge + federated surfaces. The chapter is the program's strongest argument for vocabulary breadth in audit-trail frameworks.
- Stakeholder voice pattern catalog: the chapter does not introduce a new voice pattern. Aparna's statement is direct boundary-setting (Veronika-pattern); Vikram's memo composition extends the pattern to institution-wide AI-governance scope but does not deliver as an on-the-record statement. The eight-in-eight stakeholder streak from Ch04-Ch11 was broken at Ch12 (confirmation-posture with no statement); Ch13 restores the streak as nine-in-thirteen.
- Foresight cluster Ch12-Ch17: Saraswati is the second engagement in the foresight cluster. Ch12 surfaced single-substrate handover; Ch13 surfaces edge + federated + consent-lifecycle simultaneously. The cluster's substrate-pressure trajectory now has two data points: single-substrate within-organization (Ch12) and multi-surface within-institution at the architectural edge (Ch13).

---

*Running counts and program-level signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
