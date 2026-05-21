# 19 — Aerolith Compute

> A US frontier-AI training laboratory, ~3,500 employees, headquartered San Francisco with the primary training-cluster campus in Quincy, Washington. Builds large frontier models on a 32,000-GPU cluster (mixed H100 and Blackwell). Counterparty to a voluntary pre-deployment evaluation partnership with the US AI Safety Institute (NIST AISI) under the Executive-Order-derived testing-and-attestation framework that became the AISI Reference Evaluation Program. **TesseraSeal in production for 11 months on the inference-time chain (the production model-serving path that customers and API users hit); the training-time chain — pre-training corpus provenance, training-run code-and-config integrity, hyperscale GPU-fleet attestation, model-weight lineage across multi-month runs, pre-deployment evaluation chain — is NOT in chain today.** Three-day engagement at the Quincy campus; AISI sends two observers (a senior evaluator and the program's chain-of-custody lead) to Days 2 and 3 under a coordinated-observer letter. Tom is running the team; Dawn is in Boston for the second engagement of her vacation week. Sonya joins this one as her second engagement; she contributes the GPU-fleet-logistics view that maps her Howard-Pace experience onto Aerolith's hyperscale compute discipline. Steve and Kevin from TesseraSeal are on-site again — the recusal-protocol vendor-engagement constraint remains naturally satisfied by Dawn's absence. The wishlist that emerges is the **frontier-model training-provenance** family — §10.63 training-corpus provenance chain, §10.64 training-run code-and-config chain, §10.65 hyperscale GPU-fleet attestation, §10.66 model-weight lineage across multi-month runs, §10.67 pre-deployment evaluation chain, §10.68 AI Safety Institute pre-deployment-attestation regulator-pack overlay.

## The team and the day

Tom (lead), Raj, Elena, Mike, Diana, Luis, Chen, Sonya travel to Quincy on a Tuesday-Wednesday-Thursday window. The flight is Sea-Tac to Pangborn (Wenatchee); from there it's a forty-five-minute drive northeast to the Quincy datacenter campus. The Quincy datacenter belt sits along the Columbia River; the air smells of irrigation and basalt; the buildings are big tan boxes behind double fences, the hum is structural. Aerolith's campus is two of the boxes plus a small office building.

Aerolith's chief evaluation officer is **Dr. Xan Tedeschi-Quirke**, mid-30s, ex-DeepMind safety, ex-Anthropic alignment science, second academic career — runs the pre-deployment evaluation program. Aerolith's chief infrastructure officer is **Margaux Veerendraver**, late 40s, ex-Cloudflare and ex-OpenAI infra, runs the training cluster. Aerolith's chief trust officer is **Renaud Simard-Calenda**, late 50s, ex-NIST CSD, hired specifically for the AISI partnership relationship. AISI's two observers are **Dr. Imogen Bartow-Slade** (senior evaluator, ex-DARPA AI exploration) and **Yusuf el-Mansouri** (program chain-of-custody lead, ex-NIST cryptographic engineering).

TesseraSeal sent **Steve** and **Kevin** again — recusal-naturally-satisfied posture continues since Dawn is on PTO. Tom logged the engagement-letter authorship boundaries with the firm's general counsel before Argent Vector and the same boundaries hold for Aerolith. Mike and Sonya jointly author the training-provenance wishlist; Tom authors audit-procedure; Chen consults on data-engineering. AISI's observers attend under the coordinated-observer letter with the same authorship convention applied to their input — they observe and contribute, but the audit conclusion is the firm's.

## The drive-in monologue — eastbound on Highway 28

```
6:50 AM PST. Rental Suburban, Highway 28 northeast from Wenatchee toward Quincy.
                          Tom driving. Sonya in the passenger seat for the second
                          engagement in a row. Mike and Chen in the second row.
                          Sun coming up over the Columbia Plateau; the air clean.
```

**Tom:** "Engagement nineteen. Aerolith Compute. Frontier-AI training lab. AISI pre-deployment evaluation partnership. Three days. Steve and Kevin in the building today and tomorrow. Sonya, this is your second."

**Sonya:** "Second one. Argent Vector was hardware supply chain plus a TEMPEST cleared-area annex with a drone R&D program. This one's hyperscale compute. Different surface, same shape — the chain doesn't yet bind everything the institution wants bound."

**Tom:** "What's the shape this time, in your read?"

**Sonya:** "I read the Aerolith engagement-letter file on the plane. They have inference-time chain in production for eleven months — every model call from a customer or API user is chain-bound. What they don't have is *training*-time chain. Training is where the model was made. The training corpus is petabytes; the training run is months long; the GPU fleet is thirty-two thousand cards; the model weights at the end are the artifact. None of that is in chain today."

**Mike** (from the second row): "And AISI — the AI Safety Institute — wants what?"

**Sonya:** "AISI's pre-deployment evaluation program asks the lab to produce evidence that the model the lab evaluated is the model that gets deployed. That's a provenance question. Today the lab's answer is a series of internal attestations — *trust us, this is the same model* — backed by checksums and signed engineering attestations. AISI wants the same kind of integrity claim that the inference-time chain provides on the customer side, applied to the training-time provenance."

**Tom:** "So the engagement is — confirm the inference-side chain (one day), walk the training-side gap (two days), produce a wishlist memo for Renaud and a coordinated-observer copy for AISI."

**Mike:** "Six wishlist sections, Steve and Kevin already told me on the flight. They've been positioning this with Margaux and Xan for two months. The §10.62 red/black work at Argent Vector was the first day Steve had touched a non-financial-services frontier-line section in production; the §10.63 onward training-provenance is the next."

**Chen** (data engineering): "And the §10.34 training-phase integrity from Saraswati — does it not extend?"

**Tom:** "Different geometry. Saraswati was federated learning. Fifteen thousand small devices contributing local gradients to a monthly aggregator. The §10.34 spec text covers federated geometry. Aerolith is centralized hyperscale — single org, thirty-two thousand GPUs in one campus, four-month continuous training run, terabyte-per-second checkpoint flow. The §10.34 family doesn't trivially extend. The wishlist is the new sections."

**Sonya:** "It never is."

**Tom:** "It never is. — Sonya, your call this morning?"

**Sonya:** "My call is: AISI is the regulator-equivalent on the bench. They observe Days 2 and 3. The wishlist memo has a parallel coordinated-observer copy; the spec working group sub-track that follows includes AISI as a stakeholder. Aerolith is the canonical institutional reference for the family. Renaud, Margaux, Xan are the reference engineers. The §10.68 AISI pre-deployment-attestation overlay is the regulator-pack item that lifts the family into the AISI evaluation-submission framework."

**Tom** (after a pause): "That is the right call. — Off the highway, second exit."

The Suburban turns off Highway 28 onto the access road. The campus comes into view — two enormous datacenters and a smaller office building, ringed by an outer perimeter fence and an inner security fence at the building line. The hum is audible from the parking lot: thirty-two thousand GPUs converting electricity into matrix multiplications, plus the cooling that keeps them alive.

## 7:45 AM PST — Lobby

The Aerolith office building lobby has a wall display of the inference-time TesseraSeal verifier output running in real time — the API-traffic chain at customer-call rate, with the per-event MAC verifications cascading down the screen. The display is a bit of an aesthetic flex. Tom registers it; Sonya registers it.

Renaud, Margaux, Xan, and Imogen and Yusuf from AISI are at the security desk. Steve and Kevin are already in the executive briefing room — they flew in last night.

**Renaud:** "Welcome to Quincy. Eight from your firm; two AISI observers under the coordinated letter. Let me introduce Imogen and Yusuf — they'll join us Day 2 and Day 3. Today is the inference-side confirmation; AISI doesn't observe Day 1 by construction. They observe the training-side gap walk."

**Imogen** (AISI, shaking Tom's hand): "Tom. We've read the seventeen prior engagements that the project published. We're particularly interested in §10.34 federated training-phase integrity from Saraswati and the §10.50 generative-AI four-tuple binding from Lyceum, plus the §10.62 red/black work that just landed at Argent Vector this week. The training-provenance question is the natural next horizon for the AISI program."

Imogen and Yusuf had read the auditor-stories companion before flying out — §0.5.5 names that the spec, the auditor stories, the question bank, and Herald.Py are layered: the spec is precise, the stories are scenario-driven, the question bank is reactive.

**Tom:** "We'll walk it carefully. Sonya, Mike, and Chen carry the training-provenance wishlist drafting; I'll partner with Renaud on engagement procedure."

**Imogen:** "Yusuf is our chain-of-custody lead. He'll work the cryptographic-engineering side with Mike and Chen. We're observing for the AISI program's working-group input; we don't author."

**Yusuf:** "That's right. Observers."

**Renaud:** "Day 1: inference-side chain confirmation. Eleven months in production, ~30 billion chain entries, daily-cadence seal under the §10.27 default cadence. Day 2 morning: training-corpus provenance and the GPU-fleet attestation walk. Day 2 afternoon: model-weight lineage and the pre-deployment evaluation chain. Day 3 morning: AISI submission-framework overlay. Day 3 afternoon: wishlist memo close-out."

**Tom:** "Engagement letter has it. We'll meet it."

## 8:30 AM PST — Inference-side chain walk-through (Day 1)

Margaux walks the inference path. The production model-serving path is fronted by a customer-facing API; each API call hits a routing layer, a model-server pod, and the model's compute path on a small dedicated inference-cluster (eight thousand H100s in a separate building from the training cluster). The chain entries land in Aerolith's central ledger, signed under the AWS CloudHSM in `us-west-2`. Daily seal at 02:00 PST.

**Mike:** "Walk a chain entry for an inference."

**Margaux:** "Each API call is a chain entry. `audit.inference.request`, `audit.inference.response`, plus model-version, prompt-hash, output-hash. Per-event MAC under tenant session key. The §10.47 generation four-tuple binding from Lyceum is in production here too — every inference is bound to (request_hash, model_version, sampling_seed, output_hash). The customer-side audit-trail is full."

**Mike:** "Cleanly. — and the training-side?"

**Margaux:** "The training-side is what we don't have. Today's chain captures the inference. It does not capture how the model that's being inferenced came to be. That's Day 2."

The team walks the inference-side reconciliation through the morning. Five inferences picked across the eleven-month audit period. All five trace cleanly. The §10.47 four-tuple binding verifies; the §10.48 stochasticity attestation verifies; the §10.49 retrieval-source integrity verifies (one of the five inferences hit a retrieval-augmented generation path). The verifier produces PASS verdicts on every entry.

By 11:30 PST, Day 1's confirmation is logged. Margaux closes the morning.

**Margaux:** "Production inference-side is what we're proud of. AISI observes that on the public side via our regular publication of the verifier-output dashboard. — Lunch, then training."

## 12:30 PM PST — Lunch in the Aerolith cafeteria

The cafeteria is in the office building. Sun coming through the south-facing windows; the Columbia visible in the distance. The team takes a long table; Renaud, Margaux, Xan, Steve, Kevin join. Imogen and Yusuf sit one table over (they're not present for Day 1's confirmation by the coordinated-observer letter; they'll re-engage tomorrow).

**Tom:** "Sonya — open the training conversation with what you saw at Howard-Pace."

**Sonya:** "Howard-Pace shipped GPU servers — DGX boxes, custom-spec compute appliances — to a lot of frontier labs in the 2022-2024 window. I sat in a lot of customer-success calls. The customer's question was always the same: *can we prove that the GPUs in the rack are the GPUs in the bill of materials?* We had a good answer for that — chain of custody from fab through Howard-Pace's depot through the customer's loading dock. What we didn't have a good answer for was: *can the customer prove that the model the customer trained on those GPUs was trained on the data the customer's compliance team thought was used?* That was the customer's problem, not ours. But every customer asked, every time. By 2024 it was the question."

**Margaux:** "The training-side provenance question. From the GPU's view: I have thirty-two thousand cards. They run for four months continuously. I produce checkpoints every six hours. At the end I have a model. The model is what AISI evaluates. The question we cannot today fully answer is: how do I prove that this checkpoint is the result of running this code on this corpus on these GPUs?"

**Mike:** "And what you have today?"

**Margaux:** "Internal attestations. The training scheduler has logs. The data-loading pipeline has logs. The checkpoints are stored on a high-throughput filesystem and we hash each one as it's written. The hashes are signed by an internal HSM. The training code is in a git monorepo with signed commits. The model card cites the corpus by name and version. AISI gets the model card and the signed checkpoints. AISI does not get an integrity-bound chain that ties the corpus to the code to the GPUs to the checkpoints."

**Xan** (the chief evaluation officer, leaning in): "And on AISI's side — Imogen has been honest about this — the AISI evaluation submission framework is being designed this year. They want the integrity primitive for the next AISI submission cycle. We're the willing institutional reference if the spec working group surfaces the §10.63 onward family."

**Steve:** "We've been talking to Renaud and Margaux for two months. The shape is roughly: training corpus chain, training code-and-config chain, GPU-fleet attestation chain, model-weight lineage chain, evaluation chain, and an AISI submission overlay. Six sections. Kevin and I have prototype text on three of them."

**Kevin:** "Pushback ready on all six."

**Tom:** "Engagement letter has the wishlist drafting on the firm's side, with Sonya and Mike co-authoring. Steve and Kevin contribute spec-fit and devil's-advocate. AISI observes Days 2-3. Let's eat."

The lunch finishes; the team files into the training-cluster building for the afternoon walk.

## 2:00 PM PST — The first datacenter walk

The training-cluster building is colder than the office building, much louder, and visually overwhelming. Rows of racks; thirty-two thousand GPUs; cooling pipes the diameter of small trees; power feeds from a utility substation Aerolith built dedicated to the campus. Margaux gives the team safety cards and ear-muffs.

**Margaux:** "What you're hearing is sixty megawatts of compute. Each rack is one hundred twenty-eight GPUs in eight chassis. Each chassis has its own TPM and a node-level TEE. The training scheduler runs on top, distributes the gradient computation across the fleet, and aggregates at the parameter-server layer."

**Sonya** (loudly, to be heard over the cooling): "You attestation per-chassis or per-GPU?"

**Margaux:** "Per-chassis today. The TPM signs the boot-state of the chassis at boot time. The GPUs themselves don't have first-class attestation in our setup; we trust the chassis-level attestation to cover the GPUs in that chassis. The next-generation cluster — if we build a third building with Blackwells in 2027 — would use per-GPU attestation."

**Mike:** "And the training scheduler — when it dispatches a gradient computation to a chassis — does it record the chassis attestation?"

**Margaux:** "Today, no. The scheduler records the dispatch in its internal log; the chassis attestation is in a separate log. They're correlatable by node-id and timestamp; they're not chain-bound."

**Sonya:** "And during the run — chassis attestation re-validation?"

**Margaux:** "Daily. Each chassis re-attests at the start of each day. If the attestation shifts — TPM PCR-shift, boot-state change — the scheduler quarantines the chassis and reroutes the workload. We've had 47 attestation-shift events in the last training run; 41 were benign (firmware updates we authorized), 6 were unexplained and the chassis was decommissioned and replaced."

**Sonya:** "Six unexplained shifts in four months on thirty-two thousand chassis. That's the cost of operating a frontier training run. Each one wants to be a chain entry."

**Margaux:** "Each one wants to be a chain entry. The §10.65 hyperscale fleet attestation."

The team walks to a parameter-server cluster at the back of the building. Margaux pulls up the corpus-loading dashboard.

**Margaux:** "The corpus is six hundred terabytes — text, code, multimodal data. We index it at corpus-build time and the data-loader streams it to the trainers. Each training step pulls a batch of tokens from the corpus index. The mapping from training-step-id to corpus-shard is recorded in the data-loader log. The corpus itself is stored in an immutable object store; each shard has a content hash. The corpus index is signed at build time. The data-loader log is in our internal logs."

**Chen:** "And the dedup, the license screen, the safety filtering?"

**Margaux:** "All those happen at corpus-build time. We have a data-build pipeline that takes the raw corpus, dedups it, applies the license-and-safety filters, and produces the indexed corpus. Each filter has a deterministic transformation; the build pipeline is reproducible from the input set. We log the filter decisions; the logs are signed at build time. They are not in chain."

**Sonya:** "Wishlist item. — §10.63 training-corpus provenance chain. Every shard, every dedup decision, every filter pass, integrity-bound."

**Mike** (at his laptop, sketching):

```
SECTION 1 — TRAINING-CORPUS PROVENANCE CHAIN (§10.63)
  - Corpus-build pipeline emits chain entries:
      - audit.training_corpus.shard_ingested (per shard; license, source attribution,
        content_hash)
      - audit.training_corpus.dedup_decision (per dedup pass; input_hash,
        output_hash, dedup_algorithm_version)
      - audit.training_corpus.filter_pass (per filter; filter_kind, filter_version,
        filter_decision_hash)
      - audit.training_corpus.index_built (final indexed corpus content_hash,
        manifest_hash, build_environment_attestation)
  - Per-event MAC under tenant session key; daily seal under tenant HSM.
  - Cross-anchor to source-license attestations via §10.21.
  - Verifier dispatches on `audit.training_corpus.*`; produces a corpus-integrity
    verdict per indexed-corpus version.
```

**Kevin:** "Pushback. The corpus-build pipeline is run once per major model release, not continuously. The chain entries are batched at build time. The §10.63 family is build-time chain, not training-time chain. They're related but distinct. The training-time chain references the corpus's indexed-corpus version (which integrity-binds to the corpus-build chain via the indexed-corpus content_hash) but doesn't re-bind the corpus itself per training step."

**Steve:** "Right. §10.63 normates the corpus-build chain; the training-time chain references the indexed-corpus version. Sonya, write it down."

**Sonya:** "*§10.63 training-corpus provenance chain — build-time; training-time chain references the indexed-corpus version.*" Sample-based corpus attestation — auditing a representative shard rather than every shard — uses §10.21.1's sample-attestation cross-anchor pattern: the sampled shard's attestation hash binds at the cohort level, and per-shard chain entries inherit transitively.

## 4:30 PM PST — Day-1 client question

Renaud in his office. Quincy late-afternoon sun. Tom, Sonya, Mike, Steve, Kevin present. Margaux and Xan have stepped out for a separate operations review.

**Renaud:** "AISI submission cycle next year. The next major model release we plan to put through AISI's pre-deployment evaluation is twelve months out. The §10.63-§10.68 family — if it lands in the spec at the next release window, can we deploy it before the AISI submission?"

**Sonya:** "Spec working group's timeline is the variable. Steve and Kevin can answer that better than I can."

**Steve:** "If Aerolith is the canonical institutional reference, with AISI as observer-stakeholder, and Argent Vector is in parallel for §10.56-§10.62, the working group can absorb both sub-tracks at the next release window. Six to nine months to normative-text adoption. Aerolith's deployment timeline depends on engineering capacity, but technically the spec text would be ready ahead of the AISI submission."

**Kevin:** "Pushback. Six wishlist sections is a lot of normative text. The working group's process is to surface, draft, review, push back, revise, ratify. Each section takes a calendar quarter at minimum if it's contentious. If §10.63-§10.68 are uncontentious — because Aerolith and AISI are aligned on the shape — the calendar shrinks. If a competing frontier lab pushes back on the schema, the calendar extends."

**Renaud:** "Aerolith is committed to the shape. Xan and Margaux and I will be visible in the working-group sub-track. We'll cite AISI's observer-stakeholder role explicitly so other frontier labs see the trajectory."

**Tom:** "And the institutional reference is firm?"

**Renaud:** "Firm. Aerolith is the canonical institutional reference for §10.63-§10.68. AISI is the regulator-equivalent observer. The §10.68 overlay binds the family into the AISI submission framework."

**Tom:** "Engagement letter records it."

**Renaud:** "One more question. — When AISI's evaluator presses on whether our June model was actually trained on the corpus we said it was trained on — what's our message today, before §10.63 ships?"

**Sonya:** "The honest answer is the same as Argent Vector's hardware-supply-chain answer last week: it's a real gap. We're proposing §10.63-§10.68 to close it. We have signed engineering attestations and content-hash chains today; they compose end-to-end at the human level. They do not compose at the chain-integrity level. AISI's submission framework is the right surface for the gap; the §10.68 overlay closes it once the family ships."

**Renaud:** "And in the meantime."

**Sonya:** "In the meantime: tighten the data-build pipeline's per-step logging; cross-anchor every signed attestation back to the inference-side chain via §10.21; surface every checkpoint hash on a publicly-visible AISI-readable log; accept the residual that the build-time provenance is signed-engineering-attestation-equivalent until §10.63 onward ships. The chain doesn't lie about what it doesn't yet have."

**Renaud** (after a pause): "That's the same answer Sonya gave Brent at Argent Vector. I read the engagement debrief Tom forwarded last night."

**Sonya:** "It's the same answer. Different surface."

**Renaud:** "Tomorrow morning — eight thirty. Margaux and Xan will walk training-run code-and-config and model-weight lineage. AISI joins."

## 7:00 PM PST — Hotel restaurant in Quincy

The team takes a corner table at the Quincy Inn restaurant. The town is small; the menu is steakhouse-and-burger; the beer list is local. Steve and Kevin are at the bar; they nod and stay separate. Tom's phone buzzes.

**Tom:** "Dawn. — *Sonya's first read on Aerolith?*"

**Sonya:** "Tell her the second engagement is the test of whether the first engagement was the new normal. Which it is. The room is the same room — different industry, different vocabulary, same shape — and the spec working group's wishlist surface follows the same pattern: surface, push back, refine, commit to institutional reference."

**Tom** (typing): "*Sonya says: second engagement confirms first. The room is the room. New industry, same shape.*"

The phone buzzes back almost immediately.

**Tom** (reading): "*Tell Sonya she's exactly right and that I knew that on her first read. — D. PS — Boston is glorious. Kayla and Hassan want to meet the team next time we're East. Baby is currently asleep on Hassan's chest in approximately seventy-degree winter sun. — D.*"

**Sonya:** "Tell her thank you. And that I'd like to meet Kayla and Hassan and the baby."

**Tom** (typing): "*Sonya says she'd like to meet Kayla and Hassan and the baby.*"

A longer pause this time, then: "*Tell her she will. — D.*"

The team eats. Sonya is quiet for the second half of dinner. Mike notices, says nothing about it, but does meet her eye and lift his glass once. Sonya lifts hers back.

## Day 2 — 8:30 AM PST — Training-run code-and-config walk-through (AISI observing)

Imogen and Yusuf join the team in the training-cluster conference room. Margaux at the whiteboard.

**Margaux:** "Training-run code is in our monorepo. Each training run starts with a snapshot of the monorepo at a specific commit hash, plus a hyperparameter config (the YAML), plus the corpus version, plus the GPU-fleet manifest (which racks, which chassis, which networking topology). All of that is captured today as a 'run launch record' — a signed JSON document committed to a runs registry. The signed JSON is hashed; the hash is the run-id."

**Mike:** "Walk a run-launch record."

Margaux pulls up a record. Run `r-2025-Q3-major-7`. The training run for Aerolith's latest frontier model. Started July 14, 2025; ended November 3, 2025; 112 days; 6,400 checkpoints (one every 25 minutes).

**Margaux:** "The run-launch record commits to the code commit, the hyperparameter config, the corpus version, and the fleet manifest. As the run progresses, we emit checkpoint records every 25 minutes. Each checkpoint record contains the checkpoint's content_hash plus the run-id plus the step-id. The checkpoint records are signed at write-time; the signing key is on the training-cluster HSM."

**Yusuf** (AISI's chain-of-custody lead): "And the connection between the checkpoint records and the AISI submission?"

**Margaux:** "When we submit a model to AISI, we cite the run-id, the final checkpoint, the model card. The AISI evaluator can re-derive the model card's citations. The integrity claim is on the signed checkpoint hash. AISI's evaluator trusts the signed-engineering-attestation chain; they don't have a chain-bound integrity primitive."

**Imogen:** "And the gap is right there."

**Sonya:** "Wishlist item. §10.64 training-run code-and-config chain. The run-launch record becomes a chain entry; the checkpoint records become chain entries; the chain composes end-to-end through the run."

**Mike** (at the whiteboard):

```
SECTION 2 — TRAINING-RUN CODE-AND-CONFIG CHAIN (§10.64)
  - audit.training_run.launch (run-id, code_commit_hash, hyperparameter_config_hash,
    corpus_version, fleet_manifest_hash, build_environment_attestation)
  - audit.training_run.checkpoint (run-id, step-id, checkpoint_content_hash,
    chassis_set_attestation_summary, gradient_aggregation_proof_hash)
  - audit.training_run.completed (run-id, final_checkpoint_hash, model_card_hash)
  - Chain entries bound under tenant session key, sealed daily.
  - Cross-anchor to §10.63 corpus chain via corpus_version reference.
  - Verifier dispatches on `audit.training_run.*`; produces a run-integrity
    verdict per run-id.
```

**Kevin:** "Pushback. The gradient_aggregation_proof_hash is hand-wavy. The aggregation across thirty-two thousand chassis at every training step produces gigabytes of gradient data per step. Hashing the gradient aggregation cryptographically per step is bandwidth-prohibitive. So §10.64 has to specify what the aggregation_proof actually is — likely a Merkle root over the per-chassis gradient contributions for the step, with the chassis attestation set integrity-bound to the leaf."

**Steve:** "Right. §10.64 normates a per-step aggregation proof — a Merkle root over per-chassis contributions. The §10.65 hyperscale GPU-fleet attestation provides the per-chassis attestation that's a leaf in the Merkle tree."

**Sonya:** "*§10.64 training-run code-and-config chain; per-step aggregation proof as Merkle root over per-chassis contributions, leaves bound to chassis attestation.*"

## 10:30 AM PST — §10.65 hyperscale GPU-fleet attestation

The whiteboard fills with the fleet-attestation schema.

**Margaux:** "Per-chassis attestation, daily re-attestation, scheduler integration, anomaly handling. The shape is similar to §10.35 edge-attestation primitive but at hyperscale. The differences:

1. Number of attestation events: §10.35's tablets are ~15K; Aerolith is ~250 chassis (32K GPUs at 128/chassis). The order of magnitude is comparable but the cadence per chassis is different — daily, not per-event.
2. Attestation is per-chassis, not per-GPU. The GPU-level attestation is implicit via the chassis's TEE attestation chain. The §10.65 schema names this explicitly.
3. The chassis attestation chain composes with the §10.64 per-step Merkle aggregation: every leaf in the per-step Merkle tree is a per-chassis contribution; every per-chassis contribution is integrity-bound by the chassis's daily re-attestation. The §10.64 verifier and the §10.65 verifier compose."

**Yusuf:** "And anomalies — your six unexplained attestation shifts in 112 days?"

**Margaux:** "Each one was a chassis decommissioning event. The §10.65 chain entries would integrity-bind: chassis-attestation-shift event, scheduler-quarantine event, decommissioning disposition, replacement chassis admission. The audit trail is end-to-end; today it's split across our scheduler logs and our hardware-ops Jira tickets."

**Mike** (writing):

```
SECTION 3 — HYPERSCALE GPU-FLEET ATTESTATION (§10.65)
  - audit.fleet.chassis_admitted (chassis-id, TPM_attestation, boot_state)
  - audit.fleet.chassis_attested (per chassis, daily; PCR_state, drift_seen)
  - audit.fleet.chassis_quarantined (chassis-id, reason, scheduler_dispatch_blocked)
  - audit.fleet.chassis_decommissioned (chassis-id, disposition, replacement_chassis_id)
  - Per-chassis identity bound via §10.58 component cryptographic identity (GPU
    nodes use the chassis-level TPM as their cryptographic identity; in
    next-generation deployments, per-GPU TEEs become a §10.58 identity-kind).
  - Integrates with §10.64 via Merkle leaf: each per-chassis gradient contribution
    in a §10.64 aggregation_proof is integrity-bound by the §10.65 chassis
    attestation at the time of contribution.
```

§10.65.1 normates the composition with §10.58 — every chassis carries a TPM 2.0-bound `cryptographic_identity` (typically `factory-provisioned-key` kind) that the chassis-attestation events reference.

**Kevin:** "Pushback. PCR_state changes constantly during normal training — kernel modules load, drivers update, monitoring agents update. The §10.65 schema has to distinguish between *expected* PCR state evolution and *unexpected* state shift. Otherwise every routine kernel update produces a chain anomaly."

**Steve:** "Right. §10.65.2 normates the expected-state-evolution profile — and importantly, the profile is *chain-published* via a new `audit.fleet.profile_updated` event, not stored only in CC8.1. That's the load-bearing distinction: public verifiers running outside Aerolith's IKM access can perform the `drift_seen` discrimination by walking the chain. A CC8.1-only profile attachment would let the institution retroactively claim a different 'expected' profile after the fact; chain-publication forecloses that."

**Sonya:** "*§10.65 hyperscale GPU-fleet attestation; expected-state-evolution profile chain-published via `audit.fleet.profile_updated` (not CC8.1-only); verifier dispatches on `drift_seen` by walking the chain — public-verifier accessible without IKM.*"

## 1:00 PM PST — Lunch with the AISI observers

Imogen and Yusuf at the corner of the team's table; Renaud and Margaux and Xan also present.

**Imogen:** "I want to ask the question I'd ask a frontier lab during AISI evaluation. — Aerolith trains a model in 2026. AISI evaluates it. AISI's evaluator finds a behavioral pattern in the model — say, the model declines a specific category of dual-use chemistry queries unevenly across phrasing. The evaluator wants to know: was this trained-in or fine-tuned-in? Was a specific corpus shard responsible? Was a specific RLHF preference pair responsible? Today, can Aerolith answer?"

**Margaux:** "Today: partially. The corpus shards are content-hashed; we can search the corpus for the chemistry-related content and attribute. The RLHF preference pairs are similarly hashed and stored; we can attribute. But the *integrity* claim is what we provide — *trust us, this is the corpus we trained on, this is the preference set, this is the run* — backed by signed engineering attestations. Not by an end-to-end chain-integrity-bound audit trail."

**Imogen:** "And tomorrow, with §10.63-§10.65 in place?"

**Margaux:** "Tomorrow, the AISI evaluator runs the verifier against our chain — corpus chain, run chain, fleet chain — and gets a deterministic per-corpus-shard, per-RLHF-pair, per-checkpoint integrity report. The evaluator's behavioral attribution becomes a chain-integrity-grounded query, not a vendor-trust-grounded query."

**Imogen:** "Which is what AISI needs to publish a credible attribution claim. Right now we hedge — *we cannot independently verify the lab's attestation*. With §10.63-§10.68 we don't have to hedge."

**Yusuf:** "And on the submission side — there's a sensitivity-tagging discipline AISI carries: pre-disclosure inputs that stay internal to the submission review versus disclosable inputs that AISI publishes alongside its evaluation report. §10.62.1's red/black-aware chain entry tagging is structurally parallel — chain entries carry a side tag (in §10.62.1: `audit.color_classification.side` ∈ {`red`, `black`}; for AISI: a sensitivity tag) that the verifier dispatches on. Aerolith isn't classified-defense, but the tagging shape is shared."

**Sonya:** "And the §10.68 overlay binds the family into the AISI submission. The submission cites the corpus chain version, the run chain id, the fleet chain coverage, the checkpoint chain history, the evaluation chain (§10.67). AISI's evaluator runs the §10.68 verifier as part of the submission processing. The evaluation report cites the verifier's integrity verdict."

**Imogen:** "That is the program the AISI working group has been trying to articulate."

**Renaud:** "Aerolith commits to the institutional-reference role. We'll be the first frontier lab to deploy §10.63-§10.68 in production for the next major model release."

## 2:30 PM PST — §10.66 model-weight lineage

The afternoon is on model-weight lineage. Margaux and Xan jointly at the whiteboard.

**Xan:** "A frontier model's life: pre-training run produces base weights; supervised fine-tuning produces SFT weights; RLHF or DPO produces preference-aligned weights; eval and red-team passes produce final-pre-deployment weights. Each transition has its own corpus, its own code, its own run-id. The full lineage is a directed acyclic graph from base weights to deployed weights."

**Mike:** "So §10.66 is the lineage chain — every transition is a chain entry; the parent and child weights are integrity-bound by their content_hashes; the lineage graph is walkable from the deployed model back to the pre-training base."

**Xan:** "Exactly. Plus the merging operations — sometimes we merge weights from two SFT branches into one, or interpolate between checkpoints. Those are chain entries with N parents."

**Mike** (writing):

```
SECTION 4 — MODEL-WEIGHT LINEAGE ACROSS MULTI-MONTH RUNS (§10.66)
  - audit.model_weights.transition (parent_weights_hashes[], child_weights_hash,
    transition_kind: pretrain | sft | rlhf | dpo | merge | interpolation,
    transition_run_id: cross-anchor to §10.64 run chain)
  - audit.model_weights.deployed (model_id, deployed_weights_hash,
    lineage_root_hash: Merkle root of full lineage DAG)
  - Verifier walks lineage from deployed back to pre-training root; produces
    lineage-integrity verdict.
  - Cross-anchor to §10.64 (each transition references the producing run);
    cross-anchor to §10.67 (each transition references the post-transition
    evaluation chain); cross-anchor to §10.68 (deployment cites the full
    lineage at AISI submission).
```

**Kevin:** "Pushback. Weight content_hashes are huge — frontier models are hundreds of gigabytes per checkpoint. The hash is fine; the *retention* of the actual weights is the operational question. The §10.66 chain commits to the hash; the institution holds the weights in cold storage with cross-references back. The §10.66 schema has to specify the retention-of-weights commitment, not just the hash."

**Steve:** "Right. §10.66 normates the lineage chain plus the institution's retention commitment. Aerolith's CC8.1 names the retention horizon (likely 60 months for frontier models, aligned with the §10.54 decadal re-sealing posture)."

**Sonya:** "*§10.66 model-weight lineage chain; retention commitment in CC8.1.*"

## 4:00 PM PST — §10.67 pre-deployment evaluation chain

Xan moves to evaluation-chain content. The shape:

```
SECTION 5 — PRE-DEPLOYMENT EVALUATION CHAIN (§10.67)
  - audit.evaluation.run (eval_id, evaluation_corpus_hash, evaluation_code_hash,
    target_model_weights_hash, eval_environment_attestation)
  - audit.evaluation.result (eval_id, per-metric results_hashes, aggregated_score,
    evaluator_attestation_signature)
  - audit.evaluation.disposition (eval_id, deployment_decision: ship | block |
    revise, decision_rationale_hash, decision_authority)
  - Cross-anchor to §10.66 (evaluation references the model-weight lineage node);
    cross-anchor to §10.68 (AISI submission cites the eval chain).
  - Verifier validates evaluation-chain integrity; produces eval-coverage verdict.
```

**Yusuf** (AISI): "On the AISI side — we'd run our own evals plus reference the lab's internal evals via the §10.67 chain. The AISI eval results would be a parallel evaluation chain (different evaluator, same target weights), with cross-anchor between."

**Imogen:** "Yes. And the AISI submission framework — §10.68 — composes both."

**Steve:** "§10.67 normates the eval chain schema; per-evaluator instances of the chain compose via §10.21 cross-anchor. AISI's evals and Aerolith's evals are parallel chains anchored at the target-model-weights level."

**Sonya:** "*§10.67 pre-deployment evaluation chain; per-evaluator parallelism via cross-anchor.*" AISI's pre-deployment evaluation runs in parallel with Aerolith's internal evaluation; both anchor at the target-model-weights boundary per §10.21.2 — the parallel-evaluator composition pattern. Cardinality = 2 (known); the verifier emits `parallel_evaluator_anchor_verified` alongside `evaluation_chain_verified`.

The whiteboard is full.

## Day 3 — 8:30 AM PST — §10.68 AISI submission overlay

Day 3 opens with Imogen, Yusuf, Renaud, Xan, and the team in the conference room. Steve and Kevin observe; the §10.68 overlay is regulator-pack content and the firm-side authoring carries it.

**Sonya** at the whiteboard:

```
SECTION 6 — AI SAFETY INSTITUTE PRE-DEPLOYMENT-ATTESTATION OVERLAY (§10.68)
  - The five sections above (§10.63-§10.67) compose into an AISI-submission
    regulator-pack overlay.
  - The overlay maps:
      - AISI evaluation submission framework requirements (per the AISI
        Reference Evaluation Program documentation; versioned)
      - NIST AI RMF 1.0 applicable functions (GOVERN-1, MAP-2, MEASURE-1,
        MEASURE-2, MANAGE-2)
      - NIST AI 800-218 secure software development practices for AI
      - The submitting institution's chain-of-custody coverage for training
        provenance
  - AISI's evaluator runs the §10.68 verifier as part of submission processing;
    the verifier produces a per-submission integrity verdict.
  - Cross-anchors AISI's eval results back into the lab's chain via §10.21,
    closing the evaluation loop.
```

AISI submission packets are projections of the underlying chain — §10.62.2's releasability-projection contract framework is the canonical pattern; the AISI overlay's submission filter is structurally parallel to TALON-X's program filter.

**Imogen:** "This is the right shape. AISI commits — through the working-group sub-track — to be the regulator-equivalent observer-stakeholder for §10.68. The first reference deployment is Aerolith's next major model release; subsequent deployments at other frontier labs are welcomed."

**Renaud:** "Aerolith commits as the canonical institutional reference."

**Tom** (writing): "Six sections logged. Memo finalization through the rest of the morning. Wishlist memo to Renaud; coordinated-observer copy to Imogen and Yusuf at AISI; spec working group submission through TesseraSeal's channel. — Sonya, Mike, lead the drafts. Chen consults on data-engineering. Steve and Kevin on spec-fit. I'll write the audit-procedure section."

By 1:00 PM the wishlist memo is final. Six sections, with Aerolith named as canonical institutional reference for each, AISI named as observer-stakeholder, Renaud / Margaux / Xan named as program-side reference engineers, Imogen and Yusuf cited as observer attribution.

## 3:00 PM PST — Close-out

Renaud, Margaux, Xan, Imogen, Yusuf, the team in the executive conference room. The wishlist memo on the table.

**Renaud:** "Memo received. Aerolith commits to the §10.63-§10.68 deployment within twelve months of normative-text adoption. The §10.68 overlay is fast-tracked to align with the next major model release's AISI submission."

**Imogen:** "AISI's program working group will receive the coordinated-observer copy this afternoon. We'll publish the wishlist family as a referenced input to the AISI Reference Evaluation Program update next quarter. AISI commits to be the regulator-equivalent observer-stakeholder."

**Tom:** "Engagement closes from our side. Sonya and Mike are the authoring auditors on the wishlist memo; Chen consulted; Steve and Kevin contributed under the recusal-naturally-satisfied note."

**Renaud:** "Tom, Sonya, Mike, Chen, the team — thank you. — Imogen, Yusuf — thank you for joining. — Steve, Kevin — your TesseraSeal vendor-side contribution made the spec-fit conversation efficient. We expect to see §10.63-§10.68 land in the spec inside the next nine months."

**Steve:** "We'll hold up our side."

The team files out. Pangborn flight is at 6:30 PM; the drive back to the airport is forty-five minutes. Tom leaves the campus with Sonya in the passenger seat again.

## TesseraSeal wishlist items Aerolith surfaces

Aerolith's deployment is mature on the inference-side and confirms cleanly under existing spec primitives. The training-side is the next-horizon family — six wishlist items that compose into a frontier-model training-provenance regulator-pack overlay for the AISI Reference Evaluation Program. Each is articulated below with what Aerolith operates today, what the spec section would normate, and Aerolith's commitment as the canonical institutional reference.

### Section 1 — Training-corpus provenance chain (§10.63)

**What Aerolith operates today.** A corpus-build pipeline that takes a raw corpus (~600 TB), applies dedup / license / safety filters, and produces an indexed corpus. Each shard has a content hash; each filter pass is logged with a signed engineering attestation; the indexed corpus has a manifest hash signed at build time. The records compose end-to-end at the human level; they do not compose at the chain-integrity level. The training-side data-loader log references the indexed corpus by manifest hash but is not chain-bound to per-step training events.

**What §10.63 would normate.** A training-corpus provenance chain family — `audit.training_corpus.shard_ingested`, `audit.training_corpus.dedup_decision`, `audit.training_corpus.filter_pass`, `audit.training_corpus.index_built` — with chain entries bound under tenant session key, sealed under tenant HSM. Cross-anchor to source-license attestations via §10.21. Verifier dispatches on `audit.training_corpus.*` and produces a corpus-integrity verdict per indexed-corpus version.

**Aerolith's commitment.** Canonical institutional reference. Margaux contributes operational-reality input to the working group; Aerolith deploys §10.63 within twelve months of normative-text adoption.

### Section 2 — Training-run code-and-config chain (§10.64)

**What Aerolith operates today.** Run-launch records as signed JSON committed to a runs registry; checkpoint records signed at write-time with the training-cluster HSM. The run-launch record commits to the code commit, hyperparameter config, corpus version, fleet manifest. The checkpoint records commit to the checkpoint hash, run-id, step-id. Per-step gradient aggregation across 32K chassis is logged at the parameter-server layer but is not cryptographically bound at chain-integrity scale.

**What §10.64 would normate.** A run-chain family — `audit.training_run.launch`, `audit.training_run.checkpoint`, `audit.training_run.completed` — with cross-anchor to §10.63 via corpus_version reference. Per-step aggregation_proof normated as a Merkle root over per-chassis gradient contributions; leaves of the Merkle tree integrity-bound to §10.65 chassis attestation. Verifier dispatches on `audit.training_run.*` and produces a run-integrity verdict per run-id.

**Aerolith's commitment.** Canonical institutional reference. The next major model release's training run is the first deployment of §10.64 in production.

### Section 3 — Hyperscale GPU-fleet attestation (§10.65)

**What Aerolith operates today.** Per-chassis TPM attestation at boot; daily re-attestation with PCR-state validation; scheduler quarantine on attestation-shift events; decommissioning workflow on unexplained shifts (six in the last 112-day run). The events are split across scheduler logs and hardware-ops tickets; not chain-bound.

**What §10.65 would normate.** A fleet-attestation chain family — `audit.fleet.chassis_admitted`, `audit.fleet.chassis_attested`, `audit.fleet.chassis_quarantined`, `audit.fleet.chassis_decommissioned` — with per-chassis identity bound via §10.58 component cryptographic identity (chassis-level TPM as identity-kind today; per-GPU TEE as a future identity-kind for next-generation deployments) per §10.65.1. Expected-state-evolution profile *chain-published* via the `audit.fleet.profile_updated` event per §10.65.2 — not CC8.1-only — so public verifiers running outside the institution's IKM access can perform the `drift_seen` discrimination by walking the chain. The verifier dispatches on `drift_seen` to discriminate operational events from chain anomalies. Integrates with §10.64 via Merkle leaf — each per-chassis gradient contribution is integrity-bound by the chassis attestation at the time of contribution.

**Aerolith's commitment.** Canonical institutional reference. Aerolith publishes the expected-state-evolution profile per chassis class to the chain via `audit.fleet.profile_updated` events; the §10.65 deployment integrates with the §10.64 deployment as a single milestone.

### Section 4 — Model-weight lineage across multi-month runs (§10.66)

**What Aerolith operates today.** Pre-training → SFT → RLHF / DPO → red-team / eval → final pre-deployment weights. Each transition has its own run; transitions are tracked in an internal lineage database; weights are stored in cold storage with content hashes. The full lineage is reconstructible from the database but is not chain-bound.

**What §10.66 would normate.** A lineage chain family — `audit.model_weights.transition`, `audit.model_weights.deployed` — with per-transition cross-anchor to §10.64 (the producing run). Deployed-weights chain entry carries a Merkle root over the full lineage DAG. Retention-of-weights commitment specified in the institution's CC8.1 (60 months for frontier models, aligned with §10.54 decadal re-sealing). Verifier walks the lineage from deployed back to pre-training root.

**Aerolith's commitment.** Canonical institutional reference. Aerolith's CC8.1 names the 60-month retention horizon and the cold-storage architecture.

### Section 5 — Pre-deployment evaluation chain (§10.67)

**What Aerolith operates today.** Pre-deployment evaluations run on a separate evaluation cluster; evaluation results are signed and stored; evaluation-disposition records are signed by the deployment-decision authority. AISI's pre-deployment evals (when conducted) are external; AISI returns its own evaluation report to Aerolith. The two evaluation streams are correlated by manifest hash but not chain-bound.

**What §10.67 would normate.** An evaluation chain family — `audit.evaluation.run`, `audit.evaluation.result`, `audit.evaluation.disposition` — with cross-anchor to §10.66 (the evaluated weights). Per-evaluator instances of the chain compose via §10.21 cross-anchor (Aerolith's chain and AISI's chain are parallel, anchored at the target-model-weights level). Verifier validates evaluation-chain integrity and produces an eval-coverage verdict.

**Aerolith's commitment.** Canonical institutional reference for the lab-side §10.67 chain. AISI as observer-stakeholder for the AISI-side parallel chain.

### Section 6 — AI Safety Institute pre-deployment-attestation overlay (§10.68)

**What Aerolith operates today.** AISI submission is a structured documentation package — model card, evaluation report, training description, deployment scope — submitted under voluntary partnership terms. AISI conducts its own evaluations and returns a report. The integrity claim across the submission is on the lab's signed engineering attestations, not on a chain-integrity-bound audit trail.

**What §10.68 would normate.** A regulator-pack overlay framework binding the family (§10.63-§10.67) into the AISI Reference Evaluation Program submission. Maps AISI's evaluation submission framework requirements to chain entries; maps NIST AI RMF 1.0 applicable functions (GOVERN-1, MAP-2, MEASURE-1, MEASURE-2, MANAGE-2) to chain entries; maps NIST AI 800-218 secure-software-development practices to chain entries. AISI's evaluator runs the overlay's verifier as part of submission processing. Cross-anchors AISI's eval results back into the lab's chain via §10.21, closing the evaluation loop. Versioned per AISI Reference Evaluation Program release.

**Aerolith's commitment.** Canonical institutional reference. The next major model release's AISI submission is the first deployment of §10.68 in production. AISI as regulator-equivalent observer-stakeholder for the working-group sub-track.

## Engagement debrief — Tom's voice (Dawn returns Story 20)

> "Engagement nineteen. Aerolith Compute. Quincy, Washington. Sonya's second engagement. Dawn on PTO in Boston (week two). Steve and Kevin from TesseraSeal on-site again, recusal-protocol vendor-engagement constraint naturally satisfied by Dawn's continuing absence. AISI's two observers, Imogen and Yusuf, joined Days 2 and 3 under the coordinated-observer letter — first time the team has had a regulator-equivalent observer in the room while drafting wishlist sections.
>
> "Six wishlist sections — §10.63 training-corpus provenance, §10.64 training-run code-and-config, §10.65 hyperscale GPU-fleet attestation, §10.66 model-weight lineage, §10.67 pre-deployment evaluation, §10.68 AISI overlay. Aerolith is the canonical institutional reference; AISI is the regulator-equivalent observer-stakeholder. Margaux and Xan are the program-side reference engineers; Renaud is the trust-side counterpart.
>
> "Sonya's second engagement confirmed her first. Her Howard-Pace federal-vertical experience mapped onto Aerolith's hyperscale compute discipline at the GPU-fleet boundary in particular. The §10.65 expected-state-evolution profile shape came from her articulation of how Howard-Pace had to distinguish authorized firmware updates from unexplained TPM drift on shipped GPU servers — same operational shape, different scale. Her Day 1 close-out answer to Renaud was the same answer she gave Brent at Argent Vector: *the chain doesn't lie about what it doesn't yet have*. Renaud told me he'd read the Argent Vector engagement debrief overnight; he recognized the answer.
>
> "Steve and Kevin again contributed exactly what the engagement letter named. Kevin's pushback on the §10.64 gradient_aggregation_proof — that hashing the full aggregation cryptographically per step is bandwidth-prohibitive and the schema must specify the Merkle-root-over-per-chassis-contributions shape — was the day's tightest spec-fit moment. The vendor-side intellectual rigor was again useful and not improper.
>
> "AISI's observer presence elevated the conversation. Imogen's question at lunch — *was the corpus shard responsible? was a specific RLHF preference pair responsible?* — articulated the regulator-equivalent's gap. The §10.67 evaluation-chain plus §10.68 overlay close it. The working-group sub-track that follows has AISI as a stakeholder, which gives the family regulator-grade gravity. Dawn returns next week; she'll read both engagement debriefs together.
>
> "The next time we visit a frontier-AI training lab, this engagement is the canonical reference. Aerolith ran it the way the spec working group needs."

## Cross-references

- **Spec impact (proposed)**: §10.63 (training-corpus provenance), §10.64 (training-run code-and-config), §10.65 (hyperscale GPU-fleet attestation), §10.66 (model-weight lineage), §10.67 (pre-deployment evaluation chain), §10.68 (AISI pre-deployment-attestation overlay).
- **Test-vector references (proposed)**: vectors 065-076 referenced by the proposed sections above per `spec/test-vectors/PRD-4-INDEX.md` — §10.63 corpus-build chain (065-066), §10.64 training-run with per-step Merkle aggregation (067-068), §10.65 hyperscale-fleet attestation including expected-state-evolution and unexplained-shift (069-071), §10.66 model-weight lineage linear and merge (072-073), §10.67 evaluation chain single and parallel-lab-AISI (074-075), §10.68 AISI overlay verifier dispatch (076). The training-run Merkle aggregation vector (068), the fleet expected-state-evolution vector (069), the parallel-evaluator lab-AISI composition vector (075), and the AISI-overlay verifier-dispatch vector (076) are the four most novel additions.
- **Stakeholder navigation**: §13 stakeholder for "frontier-AI training laboratory" plus a regulator-equivalent observer-stakeholder for the AI Safety Institute (NIST AISI) — two new candidate stakeholders for spec §13.
- **Auditor stories**: this story's wishlist contrasts with Story 12 Crescent (real-time decisioning, §10.27-§10.31), Story 13 Saraswati (edge-AI federated, §10.32-§10.38), and Story 18 Argent Vector (hardware supply chain plus red/black separation, §10.56-§10.62) — the fourth wishlist engagement, the first with a regulator-equivalent observer in the drafting room, and the first to articulate frontier-model training provenance as a normative spec surface. Sonya's second engagement; Tom's second lead in Dawn's absence; AISI's first on-the-record observer-stakeholder posture in the working-group sub-track that follows. Saraswati's §10.34 federated training-phase integrity is the antecedent; §10.63-§10.68 are the centralized-hyperscale generalization.

The wishlist memo and engagement debrief are filed under Aerolith's compliance-track records, with the §10.63-§10.68 wishlist items submitted to the spec working group under Sonya and Mike's joint authorship. AISI's coordinated-observer copy goes to Imogen and Yusuf under the AISI Reference Evaluation Program documentation track. Renaud (Aerolith), Margaux (cluster), Xan (evaluation), Imogen (AISI evaluation lead), Yusuf (AISI chain-of-custody) are named as contributing stakeholders for the working-group sub-track.
