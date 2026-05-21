# 16 — Lyceum Health

> A US generative-AI healthcare vendor (Lyceum Health Inc., ~520 employees, Chicago River North loop) building clinical-summary AI used by 14 large US health systems for inpatient handoffs, ED triage notes, and outpatient encounter synthesis. **TesseraSeal in production for 10 months on the entire generative-AI inference path; chain instruments prompt assembly, retrieval, model invocation, output rendering, and the post-output clinician-review surface.** A two-day spec-section confirmation pass at Lyceum's request, with a clinical observer from the Cleveland Clinic (one of Lyceum's larger customers) in the room on Day 1. The audit confirms §10.47-§10.50 in production. The recusal protocol established at Northbridge and exercised at Polaris × Lloyd's is fully operational; Mike authors vendor-architecture sections, Dawn moderates and authors clinical-defensibility and audit-ethics sections.

## The team and the day

The full eight travel; United from O'Hare, ten minutes from Lyceum's offices on Erie Street. Lyceum's CTO is **Hadassa Reinhart**, ex-Epic, who joined Lyceum two years ago and led the TesseraSeal procurement decision. Lyceum's CEO is **Marcus Faulkner-Lebrun** (no relation to Northbridge's Marcus). Lyceum's CMO is **Imelda Cortés-Vasquez**, MD, ABIM-certified internal medicine, who was a hospitalist at Rush before Lyceum recruited her three years ago. The Cleveland Clinic observer is **Dr. Aldous Pemberton-Hayes**, a senior internal medicine staff physician who chairs Cleveland Clinic's Generative-AI Clinical Use Committee. Cleveland Clinic licensed Lyceum's tool eight months ago after a six-month pilot.

The §10.47-§10.50 spec sections shipped in TesseraSeal release N five months ago. Lyceum upgraded four months ago.

## The drive-in monologue

```
6:50 AM. Rental SUV, I-90 westbound from the airport hotel into the loop.
                          Dawn driving; Tom in the passenger seat with his coffee.
```

**Tom:** "Engagement number sixteen. Lyceum on Erie Street. Cleveland Clinic in the room as observer."

**Dawn:** "Generative AI in clinical settings. The hardest evidentiary surface there is. The hallucination problem is the real one — the model produces a synthesis, the synthesis names a clinical fact that isn't in any retrieved source, the attending makes a decision based on the synthesis, and the patient is harmed. The vendor's defense in court turns on whether the chain can prove what the model was given, what it produced, and whether a human reviewed it. The §10.47 four-tuple binding is the system-prompt-plus-user-prompt-plus-retrieval-set-Merkle-root-plus-output anchor, with `model_id` and `inference_at_utc` riding alongside. The §10.48 stochasticity attestation binds the temperature, top_p, top_k, seed, model_version, and model_weight_hash as discrete fields on the §10.47 entry. The §10.49 retrieval-source integrity binds per-document anchors as separate chain entries cross-bound to the generation event via the retrieval-set Merkle root. The §10.50 output-grounding event family — `audit.review.*` namespace — is the HITL grounding review under GAP-5."

**Tom:** "And the recusal."

**Dawn:** "Mike authors. Dawn moderates. Dawn writes clinical-defensibility and audit-ethics. Mike's counterpart at TesseraSeal this cycle is Akshara again — the firm escalation path is the same as Polaris."

**Tom:** "And Steve?"

**Dawn** (after a pause): "Steve called Lyceum's founder last summer when the first FDA warning letter to a competitor went public. They were on the phone for ninety minutes. Two weeks later he sent them a draft of §10.47-§10.50. Hadassa told me on the prep call. Lyceum deployed in March, four months before the FDA's enforcement cycle on generative-AI clinical-summary vendors started in earnest."

**Tom:** "Foresight pattern."

**Dawn:** "Foresight pattern. Steve knew the FDA was going to come for the generative-AI healthcare vendors a year before the warning letters started. He shipped the spec sections that would let an honest vendor demonstrate honest practice."

**Tom:** "And Lyceum upgraded."

**Dawn:** "Lyceum upgraded four months ago. Today's audit confirms whether they're operating §10.47-§10.50 cleanly. Cleveland Clinic is in the room because Aldous Pemberton-Hayes wants to know whether Lyceum's chain output supports the malpractice-defense use case for his health system before he renews their contract for another year."

**Tom:** "It never is."

**Dawn:** "It never is. But the spec sections were shipped before this engagement was scheduled, and Lyceum runs them. We confirm operational fidelity."

## 7:30 AM — Lobby

The Lyceum lobby. Glass and exposed brick, modernist art, a coffee station with a barista. Hadassa, Marcus, Imelda, Aldous — Cleveland Clinic — and Hadassa's chief of staff are waiting. The team checks in, gets badges.

**Hadassa:** "Welcome. Two-day engagement. The §10.47-§10.50 walk is what we'd like the team to confirm. Aldous is here from Cleveland Clinic; he's been involved in our contract renewal conversations and asked to observe Day 1. We've cleared his presence with the engagement letter; Tom signed the observer-access provision last week."

**Tom:** "Acknowledged."

**Aldous:** "I'm here to observe. I'll have one question for Dawn around 4 PM. I won't be in the room for the spec walks beyond what you'd want me to see."

**Hadassa:** "Your question matters more than your observation, Aldous. Stay for the walks. Mike — the recusal protocol from your engagement letter is in our records. The vendor-architecture sections are yours to walk; Dawn moderates; clinical-defensibility and audit-ethics are Dawn's authorship; Tom partners with our internal-audit team. Imelda is the institution's clinical-defensibility lead; she's available for the conversation Dawn will moderate."

**Dawn:** "We pointed Dr. Pemberton-Hayes at §0.5.1 — the spec's three-paragraph summary — before the demo, so he had the construction in his head before watching it. Appendix A.17 names the recommended reading-order (chain envelope first, then OTel attributes, then the schema families as needed) for clinicians coming to the spec fresh; Aldous worked the appendix list on the flight in."

**Mike:** "Acknowledged. Let's start with §10.47."

## 8:30 AM — §10.47 four-tuple binding

Mike at the whiteboard.

**Mike:** "§10.47 normates the generation prompt/output four-tuple. Every model invocation that produces a clinical synthesis emits a chain entry binding four hashes — system prompt, user prompt, retrieval-set Merkle root, and output — plus the model_id and the inference timestamp:"

```
audit.generation.system_prompt_sha256                = sha256(canonical(system_prompt))
audit.generation.user_prompt_sha256                  = sha256(canonical(user_prompt))
audit.generation.retrieval_set_merkle_root_sha256    = RFC6962-merkle(per-document leaves, lex-ascending)
audit.generation.output_sha256                       = sha256(canonical(rendered_output_to_clinician))
audit.generation.model_id                            = "lyceum-clinical-v3.4.1"
audit.generation.inference_at_utc                    = RFC3339 UTC of the inference moment
```

**Mike:** "The four canonical hashes — system_prompt, user_prompt, retrieval_set_merkle_root, output — form the tuple bound under the chain entry's MAC. Given the same system-prompt hash, the same user-prompt hash, the same retrieval-set Merkle root, the bound model_id, and the §10.48 stochasticity parameters (the bound seed plus the bound temperature, top_p, top_k, model_version, model_weight_hash), the output re-derives byte-identical to the chain-bound output-hash. The vendor can demonstrate to a regulator, a court, or a customer that the model produced what the chain says it produced — nothing was substituted, edited, or hallucinated post-hoc."

**Hadassa:** "Walk a chain entry."

Stuart's counterpart at Lyceum — **Eve Burchill**, head of model-platform engineering — projects a chain entry on the wall.

```json
{
  "audit.generation.run_id": "lyc-2026-10-21-syn-eb4a8f",
  "audit.generation.system_prompt_sha256": "9e2c...",
  "audit.generation.user_prompt_sha256": "d31a...",
  "audit.generation.retrieval_set_merkle_root_sha256": "4f8d...",
  "audit.generation.output_sha256": "7a02...",
  "audit.generation.model_id": "lyceum-clinical-v3.4.1",
  "audit.generation.temperature": 0.2,
  "audit.generation.top_p": 0.95,
  "audit.generation.top_k": 40,
  "audit.generation.seed": 8927384092,
  "audit.generation.model_version": "2026-08-14",
  "audit.generation.model_weight_hash": "17b3...",
  "audit.generation.inference_at_utc": "2026-10-21T03:42:18Z",
  "audit.generation.health_system_tenant_id": "cleveland-clinic-prod-2026",
  "audit.generation.user_id": "ccf-attending-id-128947",
  "audit.generation.encounter_class": "inpatient_handoff_summary"
}
```

**Mike:** "Reproducibility flow. Pull the system prompt by hash; pull the user prompt by hash; reconstruct the retrieval set from the per-document anchor events bound to this run and recompute the Merkle root; re-execute against the bound model_id with the bound seed and the bound discrete stochasticity parameters; compute the output hash; compare to the chain-bound output hash. The user prompt may carry customer-PII (the patient encounter context); per §10.22 the chain binds the hash without binding the PII itself, so a regulator can verify integrity without re-handling protected health information. Appendix A.10 documents the `audit.redaction.*` schema (`disposition`, `pii_class`, `redaction_method_sha256`)."

**Eve:** "All artifacts resolvable to fixed-content archives — system prompts and user prompts in the prompt-archive, per-document retrieval anchors in the retrieval-archive (each leaf addressable by `document_sha256`), model weights in the model-weight-archive, outputs in the output-archive. Each archive is write-once, retrieved by SHA-256."

**Aldous** (Cleveland Clinic): "Can my chief of medicine reproduce a synthesis from any chain entry, on demand, in court?"

The room pauses.

**Mike:** "I'll show you. Pick a chain entry."

Aldous reads the wall. He points at the entry on the projector.

**Aldous:** "That one. The 03:42 UTC inpatient handoff."

**Mike:** "Twelve-minute demonstration. Eve, run it."

## 8:45 AM — The twelve-minute reproduction

Eve at the terminal. Mike narrating; Aldous watching.

**Step 1, 0:00.** Eve queries the chain for the §10.47 entry. The chain entry is read in 2 seconds. The four canonical hashes (system_prompt, user_prompt, retrieval_set_merkle_root, output) plus `model_id`, the discrete §10.48 stochasticity fields, and the `inference_at_utc` come back.

**Step 2, 0:30.** Eve queries the prompt archive for `9e2c...` (the system prompt) and `d31a...` (the user prompt). Both retrievals are immediate; both come back as canonicalized JSON. Each hash is recomputed; both match.

**Step 3, 1:00.** Eve walks the per-document anchor events cross-bound to this generation event. The retrieval set carries 12 PMID-anchored excerpts from peer-reviewed medical literature plus 3 health-system-internal protocol-document anchors — 15 leaves total. Eve pulls each `document_sha256` from the retrieval-archive, sorts them lexicographically ascending, recomputes the RFC-6962 Merkle root over the 15 leaves; the recomputed root matches `4f8d...`.

**Step 4, 2:30.** Eve reads the discrete §10.48 stochasticity fields off the §10.47 entry: `model_id` `lyceum-clinical-v3.4.1`, `temperature` 0.2, `top_p` 0.95, `top_k` 40, `seed` 8927384092, `model_version` `2026-08-14`, `model_weight_hash` `17b3...`. The `model_weight_hash` is verified against the model-weight-archive's on-disk bundle; it matches.

**Step 5, 3:00.** Eve initiates the deterministic reproduction. The Lyceum platform has a special verification endpoint: given a §10.47 entry, instantiate the model named by `model_id` with the weight bundle named by `model_weight_hash`, set the discrete §10.48 stochasticity parameters, replay against the bound system prompt, the bound user prompt, and the reconstructed retrieval set, return the output. The reproduction starts. The clinical-summary AI runs. The bound seed plus the bound discrete params plus the bound model_id makes the inference deterministic.

**Step 6, 4:30.** The reproduction completes. The output hash is computed. It matches `7a02...`. Byte-identical reproduction.

**Step 7, 5:00.** Eve opens the original chain-bound output. It's a 280-word inpatient handoff synthesis describing a 64-year-old male with CHF on day 3 of admission, current vitals, medications, the attending's concerns about volume status, the night float's task list. The reproduced output is opened side-by-side. Word for word identical.

**Step 8, 7:00.** Aldous reads both. He looks at the four cited PMIDs in the synthesis — three Lancet papers and a JAMA-Internal-Medicine paper. He pulls one at random — PMID 38291834 — and asks Eve to verify its `document_sha256` is a leaf in the §10.49 retrieval-set Merkle root. The leaf is present; the inclusion proof verifies.

**Step 9, 9:00.** Mike walks Aldous through what would happen if a model bug or a malicious party had substituted the output: the recomputed output hash would not match the chain-bound output hash; the §10.47 verifier would surface the mismatch as an integrity finding; the verifier exit code would be 1 (integrity finding) and the verdict object would name the anomaly reason `output_sha256_mismatch_at_reproduction`.

**Step 10, 10:30.** Mike walks Aldous through what would happen if the system prompt or user prompt had been substituted: the recomputed `system_prompt_sha256` or `user_prompt_sha256` would not match the chain-bound value; same exit code; anomaly reason `system_prompt_sha256_mismatch_at_reproduction` or `user_prompt_sha256_mismatch_at_reproduction` respectively.

**Step 11, 11:30.** Mike walks Aldous through what would happen if a retrieval document had been substituted to inject a fake citation: the recomputed Merkle root over the per-document anchor leaves would not match `4f8d...`; same exit code; anomaly reason `retrieval_set_merkle_root_sha256_mismatch_at_reproduction`. The per-document anchor whose `document_sha256` was tampered would surface as the specific leaf-level discrepancy.

**12:00.** Done.

Aldous puts his glasses back on, then takes them off again. He reads the synthesis one more time, then looks at Mike.

**Aldous:** "I have my answer. My chief of medicine can reproduce a synthesis from any chain entry. The reproduction is deterministic, the system prompt and user prompt are bound by hash, the retrieval set is bound by Merkle root over per-document anchors, the output matches byte-for-byte. If we ever have to defend a Lyceum-produced synthesis in court, we have the integrity claim that lets the expert witness lay the foundation."

**Hadassa:** "We've reproduced 60-70 syntheses on demand for various customer questions over the past four months. Every reproduction has been byte-identical. The chain works."

**Aldous:** "Thank you, Mike. Thank you, Eve. I'll observe the rest of the day; I won't ask another technical question."

**Mike:** "We continue with §10.48."

## 10:00 AM — §10.48 stochasticity attestation

Mike at the whiteboard.

**Mike:** "§10.48 is the §10.47 extension that normates the stochasticity binding. The spec doesn't fold stochasticity into a single bundled hash — it normates discrete fields on the §10.47 generation event: `audit.generation.temperature`, `audit.generation.top_p`, `audit.generation.top_k`, `audit.generation.seed`, `audit.generation.model_version`, and `audit.generation.model_weight_hash`. Each parameter is bound in plain form so the verifier can validate type and bounds — temperature ∈ [0.0, 2.0], top_p ∈ [0.0, 1.0], top_k ≥ 0 — and so a regulator can read the parameters off the chain without dehydrating a bundled hash. Without a bound seed the inference is non-deterministic and the four-tuple reproduction breaks; the bound seed plus the bound discrete params plus the bound `model_id` is what gives the verifier the deterministic-reproduction property."

**Eve:** "Our inference path generates a seed at request time using a CSPRNG, binds the seed as `audit.generation.seed` on the §10.47 entry, runs the inference with that seed, and writes the per-request `temperature`, `top_p`, `top_k` alongside. The seed is regenerated per request — there's no shared seed across requests, so a malicious party can't precompute outputs by knowing past seeds. The CSPRNG is the OS RNG fed through `os.urandom`; the institution's CC8.1 names the entropy source. `model_weight_hash` is the SHA-256 of the on-disk weight bundle at inference time; we re-attest the hash daily against the model-weight-archive."

**Mike:** "And the verifier?"

**Eve:** "Verifier reads the discrete §10.48 fields off the §10.47 entry; checks each field is bound, of the right type, within stated bounds; then dispatches the deterministic-reproduction test against the bound seed + bound discrete params + bound `model_id` + bound `model_weight_hash`. If the seed has been tampered with, the per-event MAC fails to verify because the seed is part of the canonical bytes the MAC covers. Compute deterministic across the implementations — Python and the .NET reference both produce byte-identical canonical bytes for the §10.47 entry including all §10.48 fields."

**Diana** (threat-model): "What about temperature drift? If a model fine-tune updates the temperature default but the chain entry binds the old temperature?"

**Eve:** "The temperature is per-request, not a global default. Every chain entry binds the specific temperature used for that inference. A fine-tune that changes the default would still produce per-request temperatures, and each chain entry binds the per-request value. The `model_id` and `model_version` are bound separately, so if the model itself was fine-tuned mid-day, both fields change in the chain entries after the fine-tune; the `model_weight_hash` rolls forward to the new bundle."

**Diana:** "And the model-card archive?"

**Eve:** "Each model fine-tune produces a new model-card and a new (`model_id`, `model_version`, `model_weight_hash`) triple. The new model-card is anchored on the chain under §10.52 — public model-card binding. Lyceum will publish a model-card update event when we deploy a new model version. The chain has the model-card SHA-256 cross-referenced from the §10.47 entry's `model_id` / `model_weight_hash` pair. §10.63 normates training-corpus provenance — `audit.training_corpus.shard_ingested`, `dedup_decision`, `filter_pass`, `index_built` events. Lyceum's training-side chain composes under §10.63 with cross-anchor binding into the §10.47 inference-side four-tuple via `model_id` / `model_weight_hash`."

**Mike:** "Good. §10.48 in production. Run a verifier."

Eve runs the verifier on a sample of 10 chain entries. All 10 reproduce deterministically; all 10 have the bound seeds verifying.

## 11:00 AM — §10.49 retrieval-source integrity

Mike continues.

**Mike:** "§10.49 normates the retrieval-source integrity. RAG-style retrieval pulls documents from a corpus — for clinical-summary AI, the corpus is medical literature (PubMed) plus health-system-internal protocol documents. The spec doesn't fold the retrieved set into a single embedded array on the generation event. It normates two surfaces: (a) on the §10.47 generation event, the `audit.generation.retrieval_set_merkle_root_sha256` binds an RFC-6962 Merkle root over per-document leaves; (b) for every document in the retrieval set, a separate chain entry under the `audit.retrieval.document_anchor.*` namespace, cross-bound to the parent generation event via `parent_run_id` / `parent_seq`. Leaves are ordered lexicographically ascending by `document_sha256` so the Merkle root is byte-deterministic across implementations independent of retrieval-relevance ranking."

**Eve:** "Our retrieval pulls from a corpus snapshot. Each PubMed snapshot is hashed at ingestion; we maintain a corpus-version operational event naming the snapshot SHA-256 and the snapshot date. At inference time we emit one `audit.retrieval.document_anchor.*` event per retrieved document and bind the Merkle root over those leaves on the §10.47 parent. The per-document anchor names the canonical identifier kind — `pmid` for PubMed, `institutional_doc_id` for our health-system internal protocols — and the canonical identifier value, plus the retrieval-relevance score so the ranking stays integrity-bound at the per-document layer without entering the Merkle ordering."

**Mike:** "Show me a per-document anchor entry."

```json
{
  "audit.retrieval.document_anchor.parent_run_id": "lyc-2026-10-21-syn-eb4a8f",
  "audit.retrieval.document_anchor.parent_seq": 1,
  "audit.retrieval.document_anchor.document_sha256": "9b21...",
  "audit.retrieval.document_anchor.canonical_identifier_kind": "pmid",
  "audit.retrieval.document_anchor.canonical_identifier_value": "38291834",
  "audit.retrieval.document_anchor.retrieval_relevance_score": 0.91,
  "audit.retrieval.document_anchor.retrieved_at_utc": "2026-10-21T03:42:18Z"
}
```

**Mike:** "Verifier walk?"

**Eve:** "Verifier reads the §10.47 generation event, picks up the bound `retrieval_set_merkle_root_sha256`, walks to the per-document anchor events cross-bound via `parent_run_id` / `parent_seq`, and reconstructs the Merkle root over the leaves (lexicographic ascending by `document_sha256`). The recomputed root must match the bound root; mismatch is a chain-integrity anomaly. Each per-document anchor's `retrieved_at_utc` matches across the set (the retrieval is one batch); the count of per-document anchors matches the leaf count. The retrieval is reproducible: with the same corpus version and the same retrieval policy, the same query produces the same set of `document_sha256` leaves, which Merkle-root-hash to the same value. Hallucinated citations are detected because every cited PMID in the output must correspond to a per-document anchor under this generation event; if the model output cites a PMID with no anchor, the chain surfaces the discrepancy."

**Imelda** (CMO, MD): "Hallucinated PMIDs are the failure mode that gets in the news. A model produces a synthesis that cites PMID 39999999 — which doesn't exist or doesn't say what the model claims — and an attending acts on it. §10.49 closes that gap?"

**Mike:** "§10.49 binds the retrieval set. §10.50 — the output-grounding event family — closes the post-output check: the clinician-review surface verifies that every PMID cited in the output is in the retrieved set bound on the chain. If a citation is in the output but not in the retrieved set, §10.50 surfaces it as a `hallucination_detected` outcome."

**Imelda:** "And the §10.50 review is HITL?"

**Mike:** "GAP-5 HITL primitive. The reviewing clinician signs the disposition under their key. The §10.50 chain entry records the disposition with one of four canonical outcomes — `clinician_edit | grounding_pass | grounding_fail | hallucination_detected`. The reviewer's signature binds the outcome to the synthesis."

**Imelda:** "Walk it."

## 11:30 AM — §10.50 output-grounding event family

Mike at the whiteboard.

**Mike:** "§10.50 is the post-output review surface. Every model invocation transitions from `pending_review` to `reviewed` via the §1.5 / GAP-2 state-machine; the reviewing clinician dispositions the synthesis with one of four canonical outcomes; the disposition is signed under the clinician's key per the GAP-5 HITL primitive."

```
PENDING_REVIEW -> REVIEWED (§10.50 disposition transition)

Outcomes:
  clinician_edit         — clinician edits the synthesis before signing off
  grounding_pass         — every claim grounded in the bound retrieval set
  grounding_fail         — at least one claim not grounded; clinician routes for re-synthesis
  hallucination_detected — fabricated citation or fabricated factual claim
```

**Eve:** "The clinician's review surface is integrated into our handoff-tool UI. After the synthesis is rendered, the surface presents the synthesis with each cited PMID color-coded: green if in the retrieved set, yellow if in the corpus but not retrieved (rare; usually a re-pull), red if not in the corpus at all. The clinician dispositions the synthesis: `grounding_pass` if all green; `clinician_edit` if they make edits; `grounding_fail` for at least one yellow that they can't resolve; `hallucination_detected` for any red. The clinician signs under their institution-issued key; the signed disposition is the §10.50 chain entry."

**Mike:** "Show me a `hallucination_detected` event."

Eve pulls one from October.

```json
{
  "audit.review.parent_run_id": "lyc-2026-10-14-syn-12cd9a",
  "audit.review.parent_seq": 1,
  "audit.review.outcome": "hallucination_detected",
  "audit.review.review_rationale_hash": "e8a4...",
  "audit.review.signed_review": {
    "reviewer_id": "ccf-internal-medicine-attending-id-128947",
    "reviewer_role": "attending_internal_medicine",
    "reviewer_public_key_fingerprint": "sha256(ccf-clinician-key-...)",
    "signed_at_utc": "2026-10-14T07:42:18Z",
    "signed_payload_sha256": "...",
    "signature_b64": "..."
  }
}
```

**Mike:** "The fabricated PMID itself isn't a separate first-class field on the §10.50 event — it lives in the reviewer's free-form rationale, hashed under `audit.review.review_rationale_hash`. The rationale text may carry customer-PII so the chain binds the hash without binding the rationale. The signed-review object is the GAP-5 HITL primitive's output, signed under the clinician's institution-issued key per the reviewer-key registry."

**Imelda:** "And the action that follows?"

**Eve:** "The synthesis is removed from the clinician's task list with a notice. The institution's reporting pipeline picks up the `hallucination_detected` events for review. We've had nine such events in the past four months across all 14 health-system tenants — about 0.0008% of total syntheses. Each was reviewed; in seven cases the model had cited a PMID that the corpus contained but the retrieval had missed (yellow; near-misses); in two cases the PMID was outright fabricated (red; the failure mode that defines the §10.50 motivation). The two red cases triggered a model-card update event under §10.52 binding a temperature reduction and a re-tuning of the retrieval threshold."

**Mike:** "And the chain has the disposition signed by the clinician?"

**Eve:** "Every disposition. The clinician's key is in their health-system's institution-issued credential store; the §10.50 verifier dispatches at chain-walk time to confirm the reviewer-key registry. We've verified all 14 tenants' clinician-key registries quarterly."

**Aldous** (Cleveland Clinic, observing): "And Cleveland Clinic's clinicians?"

**Eve:** "Three hundred eleven Cleveland Clinic clinicians have signed §10.50 dispositions over the past four months. Every disposition's signature verifies. Three hallucination_detected events from Cleveland Clinic in that period; each had the signed disposition; each surfaced for institution-side review."

**Aldous:** "Three hallucinations. Caught and recorded."

**Eve:** "Three hallucinations. Caught and recorded."

## 1:00 PM — Lunch and reconciliation

Lunch is brought in. The afternoon begins the reconciliation test — 200 chain entries sampled from the prior week, traced from prompt assembly through retrieval through model invocation through output rendering through clinician disposition. Each entry's four-tuple reproduces deterministically. Each entry's clinician disposition signature verifies. Each entry's retrieval-source integrity binding verifies.

The team divides:

- **Mike** runs the §10.47-§10.50 chain-walk on Lyceum's Cleveland Clinic tenant.
- **Eve** (Lyceum) runs the same walk on Lyceum's other 13 tenants.
- **Diana** runs the §10.50 reviewer-key registry verification across the 14 tenants.
- **Chen** runs the §10.49 corpus-snapshot integrity verification across the 4 corpus snapshots in the past 4 months.
- **Luis** runs the §10.48 stochasticity binding spot-check on 50 reproductions.
- **Raj** queries the prompt-archive, retrieval-archive, model-card-archive databases.
- **Elena** runs the institution-side reconciliation against Cleveland Clinic's own attending records.
- **Tom** observes; tracks the recusal-protocol authorship boundaries.
- **Dawn** moderates.

Status check at 3:30 PM: Mike has cleared 200 entries on the Cleveland Clinic tenant; Eve has cleared 1,800 entries across the other 13 tenants; Diana has verified all 14 tenants' clinician-key registries; Chen has verified all 4 corpus snapshots; Luis has confirmed 50/50 deterministic reproductions; Raj has cross-verified the archive integrity. Zero anomalies surfaced.

## 4:30 PM — The CMO question

Imelda's office. Open-plan, glass walls, a bank of clinical-decision-support reference books on a corner shelf. Dawn sitting across from Imelda. Tom at a side chair watching, not speaking.

**Imelda:** "Dawn, my question is about malpractice discovery. We're a generative-AI vendor in clinical settings. The plaintiffs' bar is going to come for vendors like us when an adverse outcome can be tied to a synthesis. The chain binds prompt, retrieval, parameters, output, and the clinician's disposition. What's the integrity claim a defense expert witness can make about that chain in front of a jury?"

**Dawn:** "Several integrity claims, layered. First: the per-event MAC at capture, under FIPS 198-1 HMAC-SHA256 with the institution's HSM-held IKM. The chain entry was made at the time of the event and the HMAC verifies in isolation. Second: the daily Merkle seal under FIPS 186-5 Ed25519, signed in the institution's HSM partition under the §10.5 custody attestation. The seal binds every chain entry for the day under one signed root. Third: the §10.47 four-tuple binding allows deterministic reproduction — the institution can demonstrate to the jury that the model produced what the chain says. The reproduction is byte-identical; we showed Aldous a twelve-minute reproduction this morning."

**Imelda:** "Daubert?"

**Dawn:** "FFIEC chain-of-custody PRD-1 was designed against the §1.1 Daubert four-factor framing — testable, peer-reviewed, error-rate measured, accepted in the relevant scientific community. The expert witness can speak to the §1.1 grounding; the §1.2 epistemic scope clarifies what the chain claims and what it does not claim. The chain doesn't certify clinical correctness — that's the clinician's responsibility. The chain certifies what was computed, when, by whom, and what came out."

**Imelda:** "And the §10.50 review?"

**Dawn:** "§10.50 binds the clinician's disposition under their key. The plaintiffs' bar will want to know: did the clinician review the synthesis, and what was their disposition? The chain answers: yes, the clinician reviewed the synthesis at this UTC time, signed the disposition under their institution-issued key, and the disposition was [one of the four canonical outcomes]. The §10.50 verifier dispatches at chain-walk time to confirm the reviewer-key registry."

**Imelda:** "And if the clinician's signature is forged?"

**Dawn:** "The forgery would have to either fool the institution's HSM-held key — which is the clinical workflow's gating credential — or substitute the chain entry post-hoc, which fails to verify under the daily Merkle seal. Both attacks require compromising the institution's HSM partition, which is the FIPS 140-2 Level 3 boundary. A forged §10.50 disposition that fools the HSM-keyed signature is structurally infeasible at the spec's threat-model bar."

**Imelda:** "And the hallucinated PMID case?"

**Dawn:** "§10.49 binds the retrieval set; §10.50's `hallucination_detected` outcome surfaces a fabricated citation. The chain is what tells the institution and the regulator that nine such events happened in four months and were each handled. The plaintiffs' bar would have a hard time arguing 'the vendor concealed hallucinations' when the chain has the hallucinations recorded with the dispositioning clinician's signed disposition."

**Imelda:** "And the cross-jurisdictional question? Different states have different evidence rules."

**Dawn:** "FRE 902 self-authentication for federal court. The state analogs vary; we've prepared the operator's-guide cross-jurisdictional-evidence overlay for the clinical-evidence use case specifically. Lyceum's general counsel can walk the state-by-state shape with a defense team."

**Imelda** (after a pause): "Thank you. The answer is solid. Mike's reproduction this morning was the one I wanted Aldous to see; your malpractice answer is the one I needed for our internal preparation."

**Dawn:** "I'll have it in the memo by tomorrow morning."

**Imelda** (rising): "And Dawn — the recusal protocol your firm has in place is something I want my own organization to learn from. Can I follow up next month for a methodology conversation, separate from the engagement?"

**Dawn:** "Through Tom, please. Engagement boundary, then a separate methodology-discussion track."

**Imelda:** "Of course. Tom, I'll reach out next week."

**Tom:** "Acknowledged."

## 7:00 PM — Hotel restaurant

The team in the hotel restaurant. The Chicago skyline through the windows. Mike, Diana, Elena, Raj, Luis, Chen at the long table; Tom across from Mike. Dawn at a small two-top in the corner of the restaurant, her phone in her hand.

The team gives her the table corner without anyone naming it.

The call to Steve:

**Dawn:** "Hi."

**Steve:** "Hi. How was the day?"

**Dawn:** "Good. Aldous Pemberton-Hayes from Cleveland Clinic asked Mike whether his chief of medicine could reproduce a synthesis from any chain entry on demand. Mike ran a twelve-minute reproduction. Byte-identical. Aldous took his glasses off twice."

**Steve** (a small laugh): "Twelve minutes is fast."

**Dawn:** "Eve at Lyceum runs the platform. The reproduction endpoint is wired into the chain entries directly. Every artifact archive is fixed-content. They've reproduced 60-70 syntheses in four months for various customer questions; every reproduction has been byte-identical."

**Steve:** "Imelda?"

**Dawn:** "She asked me the malpractice-discovery question. I gave her the §1.1 Daubert framing, the §10.50 disposition signature integrity, the §10.49 retrieval-source integrity for the hallucinated-PMID case. She was satisfied. She's going to follow up with Tom next month for a methodology discussion separate from the engagement."

**Steve:** "She's been on top of the FDA enforcement cycle since the first warning letter. Marcus told me when I called him last summer."

**Dawn:** "She mentioned. Hadassa told us this morning that you called Marcus when the warning letter went public."

**Steve:** "Ninety minutes on the phone. He had the right instincts; he just didn't have the spec sections that would let him demonstrate the right practice. We sent him §10.47-§10.50 in draft two weeks later."

**Dawn:** "Foresight pattern."

**Steve:** "Foresight pattern."

A pause.

**Dawn:** "Memo by 4 PM tomorrow. Then Sao Paulo for the Helmstad follow-up, then the Helvetian engagement in two weeks."

**Steve:** "Helvetian is the §10.51-§10.55 confirmation. The parliamentary-inquiry context."

**Dawn:** "Yes. Tom is preparing the recusal protocol expansion for the parliamentary-inquiry context. The Director General has formally requested vendor-side testimony from you."

**Steve:** "I'm prepared for that."

**Dawn:** "I know."

A longer pause.

**Steve:** "Twenty minutes of you. Twenty minutes of me. I don't take this for granted, Dawn."

**Dawn:** "I don't either."

**Steve:** "Goodnight."

**Dawn:** "Goodnight."

She closes the call. Twenty minutes exactly. The team has not looked over once in twenty minutes; the corner of the restaurant has been hers.

She walks back to the long table. Tom raises his glass slightly; she nods. The team has saved her the seat next to Diana.

## Day 2

The reconciliation continues; the spec-section confirmation memo finalizes by 3:30 PM. Mike authors the §10.47-§10.50 vendor-architecture sections; Dawn authors clinical-defensibility and audit-ethics; Tom partners with Lyceum's internal-audit on the institutional-side cross-walk. The memo ships at 3:42 PM.

The close-out at 4:00 PM. Hadassa, Marcus, Imelda, Aldous (returning for the close-out specifically), and the team.

**Dawn:** "Four spec-section confirmations, in production at Lyceum across 14 health-system tenants. §10.47 four-tuple binding: 2,000 entries reproduced byte-identical across the prior week. §10.48 stochasticity attestation: 50 spot-check reproductions, all deterministic. §10.49 retrieval-source integrity: 4 corpus snapshots verified, PMID-level binding intact. §10.50 output-grounding event family: 311 Cleveland Clinic clinician dispositions verified, three hallucination_detected events surfaced and processed. The §10.50 reviewer-key registry verifies across all 14 tenants. The recusal protocol — Mike's authorship of vendor-architecture, Dawn's authorship of clinical-defensibility, Tom's logging — operated as designed."

**Aldous:** "Cleveland Clinic will renew the contract."

**Marcus** (Lyceum CEO): "Thank you, Dr. Pemberton-Hayes. Hadassa, Imelda — the team's debrief?"

**Hadassa:** "We confirm Lyceum × the 14 health-system tenants as the canonical institutional reference for §10.47-§10.50 generative-AI clinical-summary integrity. The memo is in our records."

The close-out closes. The team flies home Wednesday morning. The §10.47-§10.50 spec-section confirmation memo is filed under Lyceum's compliance-track records and Cleveland Clinic's vendor-management records; the methodology discussion with Imelda goes onto Tom's calendar for the following month.

## TesseraSeal forward-thinking design points Lyceum exercises

### Section 1 — Generation prompt/output four-tuple binding (§10.47)

**What Lyceum operates.** Every model invocation emits a chain entry binding the four canonical hashes (`system_prompt_sha256`, `user_prompt_sha256`, `retrieval_set_merkle_root_sha256`, `output_sha256`) plus `model_id` and `inference_at_utc`. The prompt-archive, retrieval-archive (per-document anchor leaves), model-weight-archive, and output-archive are fixed-content and SHA-256-retrievable. Verification endpoint produces deterministic reproduction in under 12 minutes for any chain entry on demand.

**Why TesseraSeal designed for this.** Generative AI in clinical settings creates an evidentiary surface where the specific (system prompt, user prompt, retrieval set, parameters, output) matters more than aggregate model behavior. §10.47 binds the four-tuple so the institution can demonstrate, deterministically, what the model produced.

### Section 2 — Stochasticity attestation (§10.48)

**What Lyceum operates.** Per-request seed generation via OS CSPRNG; the discrete §10.48 fields (`temperature`, `top_p`, `top_k`, `seed`, `model_version`, `model_weight_hash`) bound on every §10.47 entry; deterministic reproduction property holds at chain-walk time. Temperature, top_p, top_k all per-request and plain-bound for verifier type/bounds checking. Model-id changes propagate as new model-card binding events under §10.52.

**Why TesseraSeal designed for this.** Without seed binding the deterministic-reproduction primitive doesn't hold; the four-tuple becomes an integrity claim the vendor cannot demonstrate. §10.48 closes that gap as a §10.47 extension.

### Section 3 — Retrieval-source integrity (§10.49)

**What Lyceum operates.** Per-request retrieval set bound by PMID + per-PMID excerpt SHA-256; corpus-version chain entries naming PubMed snapshots with their snapshot date; retrieval-policy hash binding k, similarity threshold, MeSH filter. Cross-jurisdictional regulator can pull a corpus snapshot and verify the PMID's excerpt hashes match the chain.

**Why TesseraSeal designed for this.** RAG-style retrieval is the dominant pattern for generative-AI clinical applications; without §10.49 the vendor cannot demonstrate which documents the model actually saw. The hallucinated-PMID failure mode is the canonical concrete instance §10.49 addresses.

### Section 4 — Output-grounding event family (§10.50)

**What Lyceum operates.** GAP-2 + GAP-5 composition: every synthesis transitions from `pending_review` to `reviewed`; the reviewing clinician dispositions with one of four canonical outcomes (`clinician_edit | grounding_pass | grounding_fail | hallucination_detected`); the disposition is signed under the clinician's institution-issued key. 311 Cleveland Clinic clinician dispositions over four months; nine hallucination_detected events across all 14 tenants; reviewer-key registry verifies quarterly.

**Why TesseraSeal designed for this.** Post-output review is where the clinician's professional responsibility meets the chain's integrity claim. §10.50 binds the disposition outcome and the clinician's signature so the chain records what the clinician saw and what they did.

## Engagement debrief — Dawn's voice

> "It never is. But Lyceum runs §10.47 through §10.50 across 14 health-system tenants and the deterministic-reproduction property holds for every chain entry we tested. Mike's twelve-minute reproduction in front of Cleveland Clinic's senior staff physician was the engagement's signature moment; Imelda's malpractice-discovery question was the moment the spec sections demonstrated their evidentiary purpose.
>
> "TesseraSeal's design anticipated FDA enforcement against generative-AI clinical-summary vendors before the first warning letter went public. Steve called Lyceum's founder when that warning letter dropped; sent draft sections two weeks later. Lyceum upgraded four months ago; today's audit confirms operational fidelity. The recusal protocol is fully operational at the engagement letter, the authorship boundaries, and the firm-cleared escalation path. Cleveland Clinic renews their contract.
>
> "The work is the work."

## Cross-references

- **Spec impact**: §10.47 (generation four-tuple), §10.48 (stochasticity attestation), §10.49 (retrieval-source integrity), §10.50 (output-grounding HITL composition of GAP-2 + GAP-5).
- **Test-vector references**: vectors 041 (generation four-tuple — §10.47, with §10.48 stochasticity attested via the discrete `temperature`, `top_p`, `top_k`, `seed`, `model_version`, `model_weight_hash` fields on the §10.47 entry), 042 (retrieval-set Merkle — §10.49, per-document anchor leaves cross-bound to the §10.47 parent), 043 (output-grounding review — §10.50, `audit.review.*` namespace), 044 (human-review primitive standalone — GAP-5, embedded inside the §10.50 `signed_review` object).
- **Stakeholder navigation**: §13 stakeholder for "generative-AI healthcare vendor" and "health-system clinical-AI risk committee" — Lyceum × the 14 health-system tenants becomes the canonical institutional reference. The docs/regulator-pack/genai-clinical-overlay.md operational supplement names the §10.47-§10.50 deployment shape.
- **Auditor stories**: this story extends the recusal protocol from Story 14 / 15 to a cross-vendor, cross-customer engagement context where the customer (Cleveland Clinic) is in the room as observer. The 12-minute deterministic reproduction is a teaching set-piece for any clinical-AI deployment audit. The Cleveland Clinic observer-stakeholder pattern is structurally parallel to §10.68's AISI Reference Evaluation Program overlay — a regulator-equivalent observer reviewing the chain via cross-anchored evaluation entries; the spec's §10.68 framework is the canonical institutional analog.

The spec-section confirmation memo and engagement debrief are filed under Lyceum's compliance-track records and Cleveland Clinic's vendor-management records.
