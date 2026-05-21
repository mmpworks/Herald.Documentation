# 17 — Helvetian Federal Tax Authority

> The Helvetian Federal Tax Authority (Eidgenössische Steuerverwaltung Helvetia, ESVH) — a fictional analog to a Swiss federal tax agency — operating an AI-augmented VAT audit-target selection system that has been in production for two years. **TesseraSeal in production for 18 months across the entire AI-augmented audit-target selection path; chain instruments the model invocation, the per-target rationale, the human-review boundary at the audit-decision step, and the public-transparency reporting surface where DP-noised aggregate counts are published quarterly to the Helvetian Parliament.** A three-day spec-section confirmation pass at the agency's Bern headquarters, scheduled by the Director General before a parliamentary inquiry committee opens hearings on AI-augmented administrative-law decisions in eleven weeks. The audit confirms §10.51-§10.55 in production. The recusal protocol — established at Northbridge, exercised at Polaris × Lloyd's, deepened at Lyceum — operates at parliamentary scale; Mike and Chen author vendor-architecture and PQ-cryptographic sections, Dawn authors audit-procedure, reconciliation, and parliamentary-defensibility sections, and the parliamentary inquiry committee receives Dawn's team's memo and Steve's separate testimony as parallel inputs.

## The team and the day

The full eight travel; Lufthansa from O'Hare via Frankfurt, into Bern's airport. The Bundeshaus — the Helvetian Federal Assembly building — is six minutes' walk from the agency offices in the Bundesgasse district. The Director General is **Walther von Salis-Soglio**, mid-50s, career civil servant, on his second term. The agency's CIO is **Liesl Frischknecht**, ex-Swiss Federal Cybersecurity Office, recruited specifically for the TesseraSeal procurement decision in 2024. The agency's chief audit officer is **Brida Albrecht-Köhler**.

The §10.51-§10.55 spec sections shipped in TesseraSeal release N+3 six months ago. The agency upgraded five months ago; the new sections have been in production through one full quarterly public-transparency reporting cycle.

## The drive-in monologue

```
6:50 AM. Cab from the Hotel Schweizerhof in Bern's old town to the Bundesgasse offices.
                          Dawn, Tom, Mike, Chen in the cab. The other four came up by an
                          earlier cab to set up the Day 1 reconciliation environment.
                          Bundeshaus visible across the bridge in the morning light.
```

**Tom:** "Engagement seventeen. Helvetian Federal Tax Authority. Walther von Salis-Soglio. Parliamentary inquiry committee in eleven weeks. Recusal protocol at parliamentary scale."

**Dawn:** "The hardest engagement of the year. AI-augmented VAT audit-target selection — the model picks which taxpayers get audited. The taxpayer challenge-response procedure under §10.55 is where the inquiry committee will press hardest. Three taxpayer challenges in the prior quarter, all dispositioned through §10.55, all signed by administrative-law judges. The committee will want to walk every disposition."

**Mike:** "And the post-quantum surface?"

**Dawn:** "§10.53 hybrid Ed25519 + ML-DSA seal — the agency's seals are signed under both algorithms. §10.54 decadal re-sealing — the institution's CC8.1 names the re-seal cadence at the 2036 boundary. Steve spent four years on the NIST PQC working group plus the Council of Europe Convention 108+ AI subgroup. The §10.53 lift to normative-when-applicable carries his fingerprint."

**Chen** (data engineering): "And §10.51?"

**Dawn:** "Public-transparency overlay. The agency publishes quarterly aggregates to the Parliament: number of audits initiated by sector, by canton, by enterprise size. Differential-privacy noise applied via Laplace mechanism with ε = 1.0 per published statistic; the chain binds the noised value, not the raw value. The integrity claim is on the published value — the regulator verifies that the published number is what was bound on the chain. The §1.2 epistemic-scope clarification on public transparency is what makes that chain claim defensible at a parliamentary hearing."

**Tom:** "Recusal."

**Dawn:** "Mike authors vendor-architecture; Chen authors the PQ-cryptographic sections; I author audit-procedure, reconciliation, and parliamentary-defensibility. Tom partners with Brida on internal-audit-side. Steve testifies independently to the parliamentary inquiry committee in eleven weeks; my team's memo is a parallel input. I will not be in the room for his testimony."

**Mike:** "And by next quarter?"

**Dawn** (after a pause): "Steve and I are engaged. The team knows. The recusal protocol stands. Tom and the firm's general counsel cleared the protocol expansion two months ago; the language on parliamentary-inquiry context is in our records."

**Chen:** "And we're glad. For both of you."

**Dawn:** "Thank you, Chen."

The cab pulls up at the Bundesgasse offices.

**Tom:** "Engagement starts in fifteen minutes."

**Dawn:** "Engagement starts in fifteen minutes. The work is the work."

## 7:30 AM — Lobby

The Bundesgasse offices. Limestone façade, federal-shield emblem above the entrance, the Bernese mountains visible to the south through the lobby's tall windows. The team checks in at security, gets the badges with photo and a bilingual (German + French) escort code. Walther, Liesl, Brida, and three of Liesl's senior engineers are waiting in the executive briefing room.

Walther rises.

**Walther:** "Welcome to Bern, Dawn. The full team — eight, as your engagement letter named. Liesl runs the technology platform. Brida runs internal audit. The three engineers are Liesl's leads on the AI-augmented selection model, the chain platform, and the public-transparency reporting pipeline. We've cleared the engagement letter's recusal language with the firm; Mike and Chen will author the vendor-architecture and PQ-cryptographic sections respectively. The parliamentary inquiry committee has formally requested vendor-side testimony from your principal designer for the long-retention crypto-agility section; the committee chair is aware that Steve will testify independently and your team's memo is a parallel input."

**Dawn:** "Acknowledged, Director General."

**Walther:** "We chose TesseraSeal in part because Steve had publicly committed to the 2030 hybrid post-quantum posture three years before NIST's final transition guidance. The Federal Council's Cybersecurity Office cited that commitment in our 2024 procurement decision. Liesl was at the Council of Europe Convention 108+ AI subgroup sessions in 2024; she heard Steve speak on the §10.53 hybrid posture before it was in the spec."

**Liesl:** "Three sessions. Plus a closed-door working session afterward. He took my questions for an hour after the second session ended. We were nine months from our procurement decision."

**Dawn:** "Thank you for the context."

**Walther:** "Three days. Day 1: §10.51 public-transparency, §10.52 model-card binding. Day 2: §10.53 hybrid post-quantum seal, §10.54 decadal re-sealing. Day 3: §10.55 audit-target challenge-response, the parliamentary-defensibility memo, close-out. The inquiry committee opens hearings on January 12; my office wants the spec-section confirmation memo in their briefing packet by November 25."

**Tom:** "Engagement letter has the timing. We'll meet it."

**Walther:** "Liesl, walk Day 1."

## Day 1

### 8:30 AM — §10.51 public-transparency overlay

Liesl at the whiteboard. She projects the quarterly public-transparency report on the wall — the most recent one, published October 1.

**Liesl:** "Quarterly aggregate publication to the Helvetian Parliament. Eleven aggregate statistics per quarter — audits-initiated counts broken down by sector (manufacturing, services, retail, financial, agriculture, public-sector), by canton, by enterprise-size band. The §10.51 overlay binds each published statistic on the chain with the differential-privacy noise mechanism, the ε budget, and the seed."

**Mike:** "Walk a chain entry for one statistic."

```json
{
  "audit.public_transparency.aggregate_kind": "vat_audits_initiated_count_quarterly",
  "audit.public_transparency.aggregate_published_value": 1417.0,
  "audit.public_transparency.coverage_period_start_utc": "2026-07-01T00:00:00Z",
  "audit.public_transparency.coverage_period_end_utc": "2026-09-30T23:59:59Z",
  "audit.public_transparency.published_at_utc": "2026-10-01T10:00:00Z",
  "audit.public_transparency.dp_mechanism": "laplace",
  "audit.public_transparency.dp_epsilon": 1.0,
  "audit.public_transparency.dp_seed": 8927384092,
  "audit.public_transparency.dp_mechanism_version_sha256": "5b21...",
  "audit.public_transparency.cohort_subtree_root_sha256": "7c4d..."
}
```

**Mike:** "The chain binds the *noised* aggregate per §1.2's public-transparency epistemic-scope addition. The noise application is a separate attestable step the regulator may audit out-of-band by re-running the DP mechanism with the chain-bound seed against the underlying raw aggregate."

**Liesl:** "Yes. The Helvetian Federal Audit Office — separate from us — has the regulator-grade audit power to re-run the DP mechanism. They've done it twice in the past year as part of routine cross-agency oversight. Both times the DP application was correct: the noised value the chain bound matches the value produced by re-applying Laplace at ε=1.0 with the bound seed against the raw aggregate."

**Mike:** "And the dp_delta?"

**Liesl:** "Pure-DP — Laplace mechanism, δ=0. Per §10.51's paired-attribute discipline, dp_delta is absent for pure-DP mechanisms. We use Laplace for all aggregates because the canton-level breakdowns produce small enough cohorts that pure-DP without δ relaxation gives us tight enough utility."

**Mike:** "Cohort subtree root?"

**Liesl:** "The cohort subtree — the chain entries the aggregate was computed from — is anchored under §10.31 / §10.44 cohort subtree disclosure. The aggregate's coverage period is one quarter; the subtree root binds the leaves the institution computed the aggregate over. A regulator can pull the subtree, recompute the raw aggregate, and re-apply the bound DP mechanism to verify."

**Dawn:** "And the §1.2 epistemic-scope clarification?"

**Mike:** "§1.2 was extended in this release to name the public-transparency epistemic claim explicitly. The chain claims integrity over what was bound — the noised value. The chain does not claim correctness of the noise application; that's the regulator's audit. The chain does not claim correctness of the underlying raw aggregate; that's the institution's accounting. Each layer has its own integrity claim, and each layer is auditable independently."

**Walther** (joining briefly): "And the parliamentary-inquiry shape?"

**Dawn:** "The committee will ask whether the agency is publishing accurate aggregates. The answer has three parts. First: the chain binds what the agency published — the noised value with the noise mechanism, ε, and seed. The committee can verify that the chain claims what the publication claims. Second: the regulator (the Federal Audit Office) has independently verified the DP application correctness twice in the past year. The committee can ask the Audit Office for their findings. Third: the institution's accounting practice for the underlying raw aggregate is the agency's CC8.1 control. The committee can subpoena that. Each of the three layers is auditable; the chain provides the integrity foundation that ties them."

**Walther:** "Good answer. That's the answer for the committee."

### 10:30 AM — §10.52 public model-card binding

Mike continues.

**Mike:** "§10.52 normates that public model-card publications hash-anchor the model card under the existing §10.19 `audit.external_artifact.*` family. No new event family — the institution-named kind value is `model_card`. Any change to the model card emits a new chain entry with the updated SHA-256 and a new received_at_utc; the chain accumulates the publication history."

**Liesl:** "Our public model-card is a 24-page document — the canonical model description, training-data sources, evaluation results, fairness metrics across cantons and sectors, intended-use scope, out-of-scope use, recourse procedures. Published quarterly. Each publication is anchored on the chain at publication time."

**Mike:** "Show me the most recent."

```json
{
  "audit.external_artifact.kind": "model_card",
  "audit.external_artifact.identifier": "esvh-vat-audit-target-model-card-v3.4",
  "audit.external_artifact.sha256": "8c4f...",
  "audit.external_artifact.received_at_utc": "2026-10-01T10:00:00Z",
  "audit.external_artifact.source_party": "esvh_internal_publishing",
  "audit.external_artifact.evidentiary_role": "published_model_card"
}
```

**Mike:** "Verifier walk: pull the model-card PDF from the Federal Council's public document archive (where the agency publishes), recompute the SHA-256, compare to the chain entry. We've seen this pattern at every TesseraSeal deployment that runs §10.52 in production; the verification is straightforward."

**Liesl:** "We've published 12 model-card revisions over two years. Each has a chain entry. The Federal Audit Office has independently verified all 12 model-card SHA-256s against the public archive."

**Mike:** "Good. §10.52 in production. The composition with §10.51 is the parliamentary-defensibility shape: the public-transparency aggregate publication and the public model-card publication are both chain-bound; the committee can audit each independently and cross-walk them through the chain's apex."

### 12:30 PM — Lunch

Lunch in a private dining room. The team, Walther, Liesl, Brida, and the three engineers. Bratwurst, rösti, salad with walnut oil, mineral water. The conversation drifts to the parliamentary inquiry committee's published terms of reference.

**Brida:** "The committee chair is Conseillère Nationale Estelle Aubert-de-Châtelard. She's a former federal prosecutor. Her terms of reference name three questions: (1) is the agency's AI-augmented audit-target selection compliant with Convention 108+ AI requirements? (2) can taxpayers exercise their challenge rights effectively under the Helvetian Administrative Procedures Act? (3) will the agency's audit trail be verifiable by future parliaments — across decades, across cryptographic transitions? The first question lands on §10.51-§10.52 and the §10.55 challenge-response. The second question lands on §10.55 specifically. The third question lands on §10.53 and §10.54. Day 2 is the third question."

**Dawn:** "Walther, Liesl, the ALJs, the Federal Council members, and the eleven Conseillers Nationaux on Estelle's committee will all read this memo from different starting points. §0.5.3's per-role reading paths are the triage tool — each reader follows the path that matches their role, and the spec is fast-onboardable from any of those entry points without forcing every stakeholder to read the document end-to-end."

**Walther:** "Steve answers the third question to the committee in eleven weeks. Your team's memo answers the third question to me by November 25."

**Tom:** "Acknowledged."

The lunch closes.

### 2:00 PM — §10.51 reconciliation

The afternoon runs the §10.51 reconciliation. The team pulls the most recent quarterly publication's eleven aggregate statistics from the chain. For each, they:

1. Read the chain entry.
2. Pull the cohort subtree root by SHA-256.
3. Recompute the raw aggregate from the cohort subtree's leaves.
4. Re-apply the bound DP mechanism (Laplace, ε=1.0) with the bound seed against the recomputed raw aggregate.
5. Compare the re-applied value to the chain-bound published value.

For all eleven aggregates, the values match within DP-mechanism floating-point precision. The §10.51 verifier dispatch path (steps 1 through 5) PASSes for each of the 11 chain entries.

The team also walks the §10.51 negative tests: deliberately tampering with a cohort leaf in a test environment and confirming that the re-applied DP value diverges from the chain-bound value, surfacing the integrity finding.

**Mike:** "Eleven for eleven, plus negative tests confirming detection. §10.51 in production."

**Dawn:** "And the publication-time discipline. §10.30 is the spec's normative trusted-time integration for sub-daily-cadence publications — Helvetian's quarterly publication cycle doesn't trigger §10.30's streaming-mode threshold, but the same trusted-time discipline is the prudent posture for any cross-jurisdictional or parliamentary-defensibility-critical publication. We'll name it in the memo as a forward-leaning posture the agency may adopt if the publication cadence ever tightens."

**Liesl:** "Captured for the memo."

## Day 2

### 8:30 AM — §10.53 hybrid post-quantum seal mandate

Chen at the whiteboard.

**Chen:** "§10.53 lifts the §4.3.2 dual-algorithm guidance from informative to normative-when-applicable for institutions on long-retention horizons. ESVH's retention horizon is 60 years — Swiss tax archive law mandates retention through one human generation plus a defensibility margin. §10.53 normative-when-applicable kicks in for retention horizons exceeding 25 years."

**Liesl:** "The seal job signs each daily Merkle apex root under both Ed25519 (FIPS 186-5) and ML-DSA-65 (FIPS 204). The seal record carries both signatures. The verifier dispatches both: at Step 11 of §7, the institution's posture is checked, and if dual-algorithm posture is declared, both signatures are required to PASS."

**Chen:** "Show me a seal record."

```json
{
  "seal.day_utc": "2026-10-21",
  "seal.merkle_apex_root_sha256": "9a72...",
  "seal.signatures": [
    {
      "algorithm": "ed25519",
      "key_fingerprint_sha256": "1e3f...",
      "signature_b64": "..."
    },
    {
      "algorithm": "ml-dsa-65",
      "key_fingerprint_sha256": "7c92...",
      "signature_b64": "..."
    }
  ],
  "seal.signed_at_utc": "2026-10-22T02:15:00Z"
}
```

**Chen:** "Verifier walk: §7 Step 7 retrieves the institution's posture; Step 11 checks both signatures. Both must PASS for the seal to verify under dual-algorithm posture."

**Liesl:** "We HSM-co-sign at the seal job — both keys are in the same HSM partition, partitioned by algorithm. The §10.5 custody attestation covers both keys. The §10.6 IKM minimum-length applies to both algorithms; ML-DSA's seed is 256-bit per FIPS 204. The §10.10 IKM rotation rotates both keys on the annual cadence."

**Chen:** "And the §10.17 partition-ceremony attestation?"

**Liesl:** "Witnessed by the Federal Cybersecurity Office during the original 2024 deployment, then re-witnessed at the §10.53 normative lift in 2026 when we added ML-DSA. Two ceremony events on the chain. Appendix A.13 documents the `chain.partition_ceremony_attended` schema (signatories, witness, attestation_pdf_sha256, hsm_attestation_token_b64) §10.17 and §10.53 reference."

**Chen:** "And ML-DSA-65 specifically?"

**Liesl:** "FIPS 204 final standard, August 2024. The Federal Cybersecurity Office mandated ML-DSA-65 as the minimum NIST-approved post-quantum signature for federal-systems retention exceeding 25 years. Our procurement decision in late 2024 cited Steve's commitment to hybrid Ed25519 + ML-DSA-65 from his 2022 NIST PQC working-group sessions. He was three years ahead of the federal mandate."

**Chen:** "Vector 015 from the original PRD-2 test corpus pins the dual-algorithm cosigned-seal byte form. §10.53 lifts that pattern from informative to normative-when-applicable for long-retention horizons; no new wire form, no new test vector. ESVH's production chain is byte-equivalent to vector 015 for the Ed25519 portion plus the ML-DSA-65 cosignature shape."

**Liesl:** "We verified vector 015 against our production chain last week as part of preparation for this engagement."

**Chen:** "Good. §10.53 in production."

### 10:30 AM — §10.54 decadal re-sealing discipline

Chen continues.

**Chen:** "§10.54 normates a recurring re-seal record at decadal boundaries. The re-seal record carries seven fields: the discriminator `seal.resealed_at_decadal_boundary = true`, the resealed window's start and end (the prior decade), the resealed-baseline-manifest SHA-256, the algorithm under which the re-seal is signed, the generation index (1, 2, 3, ...), the previous-generation anchor SHA-256. Generation 0 is the original seal; generation 1 is the first decadal re-seal; generation 5 would be a 50-year-old chain at its fifth re-seal."

**Liesl:** "Our retention horizon is 60 years per Swiss tax archive law. We expect 5-6 generations: original (2024-2034), gen 1 (2034-2044), gen 2 (2044-2054), gen 3 (2054-2064), and so on. Each re-seal binds the prior decade's chain under the then-current cryptographic suite."

**Chen:** "Walk the §10.54 verifier dispatch path."

**Liesl:** "Four steps. The re-seal record is itself a v1.0b sign_payload-bound seal record carrying the §10.54 discriminating attributes (`seal.resealed_at_decadal_boundary`, `seal.resealed_window_start_utc`, `seal.resealed_window_end_utc`, `seal.resealed_baseline_manifest_sha256`, `seal.resealed_under_algorithm`, `seal.resealed_generation_index`, `seal.resealed_previous_generation_anchor_sha256`) per the §10.42 annotated-seal-record precedent — no separate metadata leaf, the discriminator routes the verifier. The verifier (1) recomputes the baseline manifest hash from the prior generation's seal-record content hashes; (2) confirms the recomputed hash matches `seal.resealed_baseline_manifest_sha256`; (3) verifies the re-seal's algorithm-bound signature under the algorithm's public key; (4) confirms `seal.resealed_previous_generation_anchor_sha256` references a seal-record that exists on the chain and is the last seal of the prior generation."

**Chen:** "And the algorithm transition?"

**Liesl:** "Generation 0 (original 2024 seal) is signed under Ed25519 + ML-DSA-65 hybrid. Generation 1 (2034 re-seal, projected) will be signed under whatever NIST/FIPS recommends as the dominant post-quantum suite at that boundary. Likely ML-DSA-65 alone or ML-DSA-65 + a second post-quantum algorithm if the NIST cycle progresses. The institution's CC8.1 — and the Federal Cybersecurity Office's then-current guidance — will name the algorithm."

**Chen:** "And the auditor at year T+50?"

**Liesl:** "Walks 0 → 1 → 2 → 3 → 4 → 5 along the generation chain. Each generation's re-seal references the previous-generation anchor by SHA-256; each generation is signed under that generation's algorithm. The §10.54 verifier confirms each step. At year T+50, an auditor verifies the current signature under modern cryptography while the original signatures remain attestable through the generation linkage."

**Chen:** "Test vector 047 — the decadal-resealing annotated seal record — pins the byte form. We verified ESVH's planned generation-1 re-seal record against the test vector last week."

**Liesl:** "Captured for the memo."

### 1:00 PM — Reconciliation: §10.53 dual-algorithm verification at scale

The afternoon runs the §10.53 reconciliation. The team pulls 18 months of seal records — roughly 540 daily seals — and verifies each one's dual-algorithm signatures.

For each seal:

1. Read the seal record.
2. Verify the Ed25519 signature against the institution's HSM-held Ed25519 key.
3. Verify the ML-DSA-65 signature against the institution's HSM-held ML-DSA-65 key.
4. Confirm both signatures cover the same Merkle apex root.
5. Confirm both keys are bound to the same §10.17 partition-ceremony attestation chain.

The verification runs in parallel across the team's laptops. Each verification takes ~12ms (Ed25519) plus ~85ms (ML-DSA-65) per seal, so 540 seals takes roughly a minute per laptop. The team distributes the work; the full 540-seal verification completes in 4 minutes.

**Chen:** "540 for 540. Both signatures verify on every seal. Dual-algorithm posture in production for 18 months without a single single-algorithm-only seal."

**Liesl:** "Captured."

### 4:30 PM — The Director General's question

Walther's office. The window faces the Aare river and the Berner mountains beyond. Late October light. Dawn sitting across from Walther; Tom at the side.

**Walther:** "I have one question. The committee chair — Estelle Aubert-de-Châtelard — will ask it at the hearing. I want your team's answer first, so I know what answer the committee will hear from Steve in eleven weeks."

**Dawn:** "Ask."

**Walther:** "Will the chain be verifiable by my grandchildren?"

A pause.

**Dawn:** "Yes. Three reasons.

"First: §10.53 binds today's seal under both Ed25519 and ML-DSA-65. If Ed25519 is broken in the next twenty years — by a sufficiently large quantum computer or by an unforeseen cryptanalytic advance — the ML-DSA-65 signature remains independently attestable. Either signature alone is sufficient to verify integrity; both together is the §10.53 normative posture for institutions on long-retention horizons. The 'dual-algorithm posture' is the spec-named discipline that makes this true.

"Second: §10.54 normates decadal re-sealing under whatever cryptographic suite is current at each re-seal generation. Your grandchildren will see a chain that has been re-sealed 5-6 times by then — original generation 0 in 2024-2034, generation 1 in 2034-2044, generation 2 in 2044-2054, and so on. Each re-seal binds the prior decade's chain under the then-current algorithm. The §10.54 verifier walks the generation chain and confirms each step. The chain your grandchildren verify will look different in algorithm at the current generation, identical in integrity claim across the entire retention period.

"Third: Steve has been working toward that posture since 2022. He committed publicly to the 2030 hybrid post-quantum posture three years before NIST's final transition guidance. He spent four years on the NIST PQC working group plus the Council of Europe Convention 108+ AI subgroup. The institutional commitment is older than the NIST mandate; the spec sections we're confirming this week are the operational realization of that commitment. We confirmed §10.53 and §10.54 in production over the last two days. Your grandchildren will be able to verify the chain because the institution made the decision in 2024 to deploy the dual-algorithm posture, and the spec normates the decadal re-sealing that carries that decision forward."

Walther is quiet for a long moment.

**Walther:** "That is the answer the committee needs."

**Dawn:** "That is the answer your grandchildren need."

**Walther:** "And the recusal — your team writes that answer; Steve walks the same answer to the committee independently?"

**Dawn:** "The same answer. Independently. The parliamentary committee receives my team's memo and Steve's testimony as parallel inputs. Neither references the other. The committee draws its own conclusions from the convergence."

**Walther:** "I appreciate the discipline of the protocol."

**Tom** (from the side chair): "The protocol is the protocol because we wrote it for cases like this. It works at parliamentary scale the same way it works at NAIC market-conduct scale or at a CMS enforcement scale. The methodology and the execution have no daylight between them."

**Walther** (rising): "Tomorrow. §10.55. The challenge-response procedure. The taxpayer-facing surface."

**Dawn:** "Tomorrow."

### 8:00 PM — Hotel restaurant

The team in the hotel restaurant on the riverbank. Bratwurst, rösti again, but better; Swiss white wine; cheeses. Tom has the engagement notebook open at his place.

**Tom:** "Two clean days. Best 4:30 PM answer of the four engagements."

**Dawn:** "Walther asked the right question. The answer was already drafted in our memo."

**Mike:** "Recusal didn't cost anything. The cryptographic-section authorship was Chen's; the audit-procedure was Dawn's; the parliamentary-defensibility framing was Dawn's; Steve's testimony in eleven weeks will hit the same answer by the same path independently."

**Tom:** "The work is the work."

**Diana:** "And tomorrow we walk §10.55. Three taxpayer challenges in the prior quarter; three signed dispositions by administrative-law judges."

**Dawn:** "And the committee will press hardest on §10.55. The taxpayer's challenge right is the human-rights surface."

**Chen** (raising his glass slightly): "To Day 3."

**Tom** (raising too, but glancing at Dawn for half a beat): "And to the team. Steady through three days at parliamentary scale."

The team drinks. The conversation drifts.

Dawn excuses herself for ten minutes after the second course. The team gives her the corner of the restaurant.

The call to Steve is short — six minutes, not twenty. They both know what the next eleven weeks look like.

She returns to the table. Tom raises his glass slightly. She raises hers.

## Day 3

### 8:30 AM — §10.55 audit-target challenge-response procedure

Mike at the whiteboard.

**Mike:** "§10.55 normates the challenge-response event family for taxpayer challenges to AI-augmented audit-target decisions. The lifecycle is `filed → triaged → disposed`, with `filed → disposed` allowed when triage is operationally skipped. The disposition outcome enumeration is `upheld | overturned | modified | withdrawn`; institution-named outcomes are admitted under CC8.1. The dispositioning party signs the disposition under the GAP-5 HITL primitive; for the Helvetian context the dispositioning party is an administrative-law judge."

**Liesl:** "Three challenges in the prior quarter. One overturned — a Helvetian taxpayer challenged an AI-flagged audit and the agency reversed the decision after administrative-law-judge review. Two upheld — both audit-target selections held under judicial review. All three dispositions are on the chain with the §10.55 + GAP-5 envelope."

**Mike:** "Walk the overturned one."

```json
{
  "audit.challenge_response.original_decision_run_id": "esvh-vat-audit-target-2026-04-12-taxpayer-CH184729",
  "audit.challenge_response.original_decision_seq": 1,
  "audit.challenge_response.outcome": "overturned",
  "audit.challenge_response.rationale_hash": "8f4c...",
  "audit.challenge_response.signed_disposition": {
    "audit.signed_review.reviewer_id": "esvh-administrative-law-judge-key-id-CH-2026-08",
    "audit.signed_review.reviewer_role": "administrative_law_judge",
    "audit.signed_review.reviewer_public_key_fingerprint": "sha256(...)",
    "audit.signed_review.signed_at_utc": "2026-05-20T14:00:00Z",
    "audit.signed_review.signed_payload_sha256": "7e22...",
    "audit.signed_review.signature_b64": "..."
  }
}
```

**Mike:** "Lifecycle binding: `filed` event when the taxpayer filed the challenge under the Helvetian Administrative Procedures Act; `triaged` event when the agency's procedures office accepted the challenge for ALJ review; `disposed` event with the ALJ's signed disposition. State-machine validates the walk under §10.55's transitions table. The four canonical outcomes — `upheld | overturned | modified | withdrawn` — exhaust the dispatch surface. The 'overturned' outcome here was the agency's reversal of an audit-target selection after the ALJ found the model's reasoning insufficient under Helvetian administrative-law standards."

**Liesl:** "The taxpayer's chain entries reference their challenge-response events through the run_id. The taxpayer's representative — a tax-law firm — was given a chain disclosure that included the §10.55 events, the §10.49 retrieval-source integrity for the model's reasoning, the §10.47 four-tuple binding for the model invocation. They could verify the agency's audit trail end-to-end. The taxpayer's representative confirmed the chain held; the ALJ's overturning was on substantive grounds, not on chain integrity."

**Mike:** "Substate semantics?"

**Liesl:** "The §10.55 normative text covers the high-level lifecycle. Helvetian Administrative Procedures Act has substates for the triage step (received → assigned → preliminary_review → forwarded_for_alj). Those substates are CC8.1-named on our side; the high-level state stays `triaged` while the substates move through. The verifier dispatches on the high-level enumeration."

**Dawn:** "And the modified-outcome paired-attribute discipline?"

**Mike:** "If the outcome is `modified`, the chain entry MUST include `audit.challenge_response.modified_decision_sha256` — the SHA-256 of the canonical bytes of the modified decision. If the outcome is anything else, `modified_decision_sha256` MUST be absent. Paired-attribute discipline closes the failure mode where the agency claims `modified` but doesn't bind the modified decision. None of the three challenges in the prior quarter had a `modified` outcome; the paired-attribute discipline didn't fire. The next quarter's challenges may exercise it."

**Liesl:** "We have the test environment scenario for `modified` ready; the verifier handles it cleanly."

### 10:30 AM — Reconciliation: the three challenges

The team walks each of the three challenges end-to-end.

**Challenge 1 (filed 2026-04-12, overturned 2026-05-20).** Helvetian taxpayer in Geneva canton, retail sector, mid-size enterprise. Audit-target flag triggered by the model on April 11; flagged for VAT-evasion-pattern review. Taxpayer filed challenge on April 12; agency's procedures office triaged on April 18; ALJ review opened on April 25; ALJ disposition on May 20 — overturned, on grounds that the model's reasoning relied on a feature derivation that the Helvetian Federal Court had ruled insufficiently grounded in March 2026. The disposition was signed by ALJ Mira Helvetier-Goldfarb; her public-key fingerprint resolves to the Federal Justice Department's key registry; the signature verifies against the canonical bytes of the disposition rationale.

**Challenge 2 (filed 2026-06-15, upheld 2026-07-22).** Helvetian taxpayer in Bern canton, manufacturing sector, large enterprise. Audit-target flag triggered by anomalous VAT filings. Taxpayer filed challenge; agency triaged; ALJ Vieri Aldebrand-Steiner reviewed; disposition: upheld. The audit proceeded; the agency's audit findings (separate from the chain) were sustained. Chain integrity confirmed: the §10.55 event chain references the §10.47 four-tuple of the model invocation, the §10.49 retrieval-source integrity for the model's reasoning, and the §10.50-equivalent (here the agency's internal-grounding-review surface) that ALJ Aldebrand-Steiner consulted.

**Challenge 3 (filed 2026-08-04, upheld 2026-09-10).** Helvetian taxpayer in Vaud canton, services sector, small enterprise. Filed; triaged; ALJ Albérik de Châtelard-Fyrenne (no relation to the parliamentary committee chair, though Liesl confirms the surname is a common Helvetian formal-naming pattern). Disposition: upheld. Chain holds.

The team reconciles each challenge's chain trace, the ALJ key registry, the §10.55 verifier dispatch path, and the cross-bindings to §10.47 / §10.49 / §10.51-§10.52. All three challenges' chain integrity verifies cleanly.

**Mike:** "Three for three."

**Liesl:** "Captured."

### 1:30 PM — Parliamentary-defensibility memo

The afternoon runs the memo drafting. Mike authors the §10.51-§10.55 vendor-architecture sections; Chen authors the §10.53-§10.54 PQ-cryptographic sections; Dawn authors the audit-procedure, reconciliation summaries, and the parliamentary-defensibility framing. Tom partners with Brida on the institutional-side internal-audit attestation.

The memo's parliamentary-defensibility section closes with three paragraphs:

> *§10.53 binds today's seal under both Ed25519 and ML-DSA-65. §10.54 normates decadal re-sealing under whatever cryptographic suite is current at each re-seal generation. The chain examined by future regulators, future parliaments, and future taxpayers' representatives will look different in algorithm than the chain produced today; it will be identical in integrity claim across the full 60-year retention horizon. The institution's commitment to the dual-algorithm posture in 2024 is the design decision that carries forward; the spec sections operationalize it.*
>
> *§10.51 binds the public-transparency aggregate value the institution publishes — the noised value, per §1.2's epistemic-scope clarification. The chain integrity claim is on what was published; the noise correctness is the regulator's audit; the underlying raw aggregate's accounting accuracy is the institution's CC8.1 control. Each layer is auditable independently. The Federal Audit Office has independently verified the DP application correctness twice in the past year.*
>
> *§10.55 binds the taxpayer's challenge-response lifecycle and the dispositioning ALJ's signed disposition. The four canonical outcomes — upheld, overturned, modified, withdrawn — exhaust the verifier's dispatch surface. The institution's ALJs sign under their Federal Justice Department-issued keys; the §10.55 verifier confirms the reviewer-key registry binding at chain-walk time. Three challenges in the prior quarter; one overturned, two upheld; all three dispositions chain-verifiable end-to-end. The taxpayer's representative can verify the agency's audit trail with the same verifier the parliamentary committee will use.*

The memo finalizes by 4:00 PM. Tom files it with Walther's office; the agency forwards it to Estelle Aubert-de-Châtelard's parliamentary committee on November 25 per the agreed timing.

### 4:30 PM — Close-out

Walther's office. Walther, Liesl, Brida, the team. The Bernese mountains are catching the late October light through the south-facing windows.

**Dawn:** "Five spec-section confirmations, in production at the Helvetian Federal Tax Authority. §10.51 public-transparency overlay: 11 quarterly aggregates verifiable via cohort subtree disclosure plus DP re-application. §10.52 model-card binding: 12 model-card revisions anchored, all SHA-256s match the public archive. §10.53 hybrid post-quantum seal: 540 daily seals over 18 months, dual-algorithm signatures verify on every seal. §10.54 decadal re-sealing: institutional CC8.1 names the cadence, the test environment exercises generation-1 against vector 047, the verifier dispatch path confirms generation linkage. §10.55 audit-target challenge-response: three challenges in the prior quarter, three signed ALJ dispositions, all three chain-verifiable. The recusal protocol — Mike and Chen authoring vendor-architecture and PQ-cryptographic sections, Dawn authoring audit-procedure and parliamentary-defensibility — operated as designed. Steve will testify to the parliamentary committee independently in eleven weeks; this memo is the parallel input."

**Walther:** "Brida — the institutional-side attestation?"

**Brida:** "We confirm the team's findings. Internal audit signs the cross-walk. The memo enters our compliance-track records and the parliamentary-committee briefing packet."

**Walther** (to Dawn, pausing): "Estelle's committee is more demanding than NAIC, more demanding than the FDA's enforcement cycle. The committee will press hardest on §10.55 because the taxpayer's challenge right is what the Helvetian voter recognizes as the locus of justice. Your memo answers that. Steve's testimony will answer it again, independently, in eleven weeks. The convergence is what the committee will draw conclusions from."

**Dawn:** "The convergence is the point of the protocol."

**Walther:** "The institution thanks you."

**Dawn:** "Thank you, Director General."

The close-out closes. The team flies home. The §10.51-§10.55 spec-section confirmation memo is filed under ESVH's compliance-track records and forwarded to the parliamentary committee on November 25; the engagement debrief is logged under the firm's parliamentary-inquiry-context engagement category.

## TesseraSeal forward-thinking design points the Helvetian Federal Tax Authority exercises

### Section 1 — Public-transparency overlay (§10.51)

**What ESVH operates.** Quarterly publication of 11 aggregate statistics to the Helvetian Parliament; each statistic chain-bound under the §10.51 envelope (aggregate kind, published value, coverage period, DP mechanism, ε, seed, mechanism-version SHA-256, optional cohort subtree root). DP mechanism is Laplace at ε=1.0 (pure-DP, dp_delta absent per paired-attribute discipline). The Federal Audit Office has independently verified DP application correctness on two cycles.

**Why TesseraSeal designed for this.** Public transparency for AI-augmented administrative decision-making is the Convention 108+ AI subgroup's central question. §10.51 gives the institution a normative chain envelope that the Helvetian Parliament — or any equivalent legislative body — can audit without running specialized cryptographic infrastructure. The §1.2 epistemic-scope clarification names what the chain claims and what it does not.

### Section 2 — Public model-card binding (§10.52)

**What ESVH operates.** Quarterly model-card revisions anchored under §10.19 with the institution-named kind value `model_card`. 12 anchored revisions over 24 months. Federal Audit Office has independently verified all 12 SHA-256s.

**Why TesseraSeal designed for this.** Public model cards are the operational realization of the EU AI Act Article 13 transparency mandate and the Convention 108+ AI subgroup's model-disclosure expectation. §10.52 reuses §10.19 — no new event family — with a normative narrative for the model-card site.

### Section 3 — Hybrid post-quantum seal mandate (§10.53)

**What ESVH operates.** 540 daily seals over 18 months, each signed under both Ed25519 and ML-DSA-65 from the institution's HSM partition. Dual-algorithm posture declared on every seal record; both signatures cover the same Merkle apex root. Federal Cybersecurity Office mandates ML-DSA-65 minimum for federal-systems retention exceeding 25 years.

**Why TesseraSeal designed for this.** §10.53 lifts §4.3.2 algorithm-rotation guidance from informative to normative-when-applicable for long-retention-horizon institutions. Without §10.53 the institution would have to make ad-hoc commitments to dual-algorithm signing without normative weight; the lift names the discipline and the verifier-dispatch responsibility.

### Section 4 — Decadal re-sealing discipline (§10.54)

**What ESVH operates.** Institutional CC8.1 names the decadal re-seal cadence at the 2034 boundary with successor cadences at 2044, 2054, 2064, 2074, 2084. Generation-1 re-seal will be signed under whatever NIST/FIPS recommends as the dominant post-quantum signature suite at the boundary. The §10.54 verifier dispatch path is confirmed against vector 047 in the test environment.

**Why TesseraSeal designed for this.** 60-year retention horizons (Swiss tax archives, clinical trial archives, civil aviation records) outlive any single cryptographic algorithm. §10.54 normates the institutional discipline that walks the chain forward across cryptographic transitions. Each generation's re-seal binds the prior decade under the current suite; the auditor at year T+50 walks the generation chain.

### Section 5 — Audit-target challenge-response procedure (§10.55)

**What ESVH operates.** §10.55 + GAP-5 composition: every taxpayer challenge transitions through `filed → triaged → disposed`; the dispositioning ALJ signs under their Federal Justice Department-issued key; the chain entry binds the four canonical outcomes (`upheld | overturned | modified | withdrawn`). Three challenges in the prior quarter — one overturned, two upheld — all three chain-verifiable end-to-end.

**Why TesseraSeal designed for this.** AI-augmented administrative-law decision-making touches the human-rights surface. §10.55 binds the taxpayer's challenge-response lifecycle so the chain provides what the Helvetian Administrative Procedures Act needs: an auditable record of every challenge, its disposition, and the dispositioning judge's signature.

## Engagement debrief — Dawn's voice

> "It never is. But the Helvetian Federal Tax Authority runs §10.51 through §10.55 across an AI-augmented audit-target selection system at parliamentary-inquiry scale. Three taxpayer challenges in the prior quarter — chain-verifiable end-to-end. Eleven public-transparency aggregates per quarter — Federal Audit Office has independently verified the DP application correctness. 540 daily seals signed under hybrid Ed25519 + ML-DSA-65. Decadal re-seal cadence written into institutional CC8.1; the re-seal generation-1 will land in 2034 under whatever post-quantum suite is current then.
>
> "TesseraSeal's design anticipated long-retention horizons and AI-augmented administrative-law decision-making years before the Helvetian parliamentary inquiry was scheduled. Steve was on the NIST PQC working group from 2022; on the Council of Europe Convention 108+ AI subgroup from 2023. The §10.51-§10.55 spec sections landed in production six months before this engagement. The recusal protocol my firm wrote at Northbridge holds at parliamentary scale; the parliamentary committee receives my team's memo and Steve's testimony as parallel inputs.
>
> "The chain my grandchildren verify will look different in algorithm, identical in integrity claim. Steve has been working toward that posture since 2022. We confirmed it in production this week. Walther will brief the committee. The work is the work."

## Cross-references

- **Spec impact**: §10.51 (public-transparency overlay), §10.52 (public model-card binding via §10.19 reuse), §10.53 (hybrid post-quantum seal mandate, lifts §4.3.2 to normative-when-applicable), §10.54 (decadal re-sealing discipline), §10.55 (audit-target challenge-response procedure, composes §1.5 GAP-2 + GAP-5). §1.2 epistemic-scope clarification on public-transparency claim added in this release.
- **Test-vector references**: vectors 045 (public-transparency DP aggregate — §10.51), 046 (public model-card binding — §10.52), 047 (decadal re-sealing annotated seal record — §10.54), 048 (challenge-response disposition — §10.55). §10.53 hybrid post-quantum seal mandate lifts the existing dual-algorithm cosigned-seal pattern from PRD-2 (test vector 015) to normative-when-applicable for institutions with retention horizons exceeding 25 years; no new Phase-8 vector.
- **Stakeholder navigation**: §13 stakeholder for "civic-AI vendor and parliamentary-inquiry context" — ESVH becomes the canonical institutional reference. The docs/regulator-pack/civic-ai-overlay.md and docs/regulator-pack/long-retention-overlay.md operational supplements name the parliamentary-defensibility shape and the 60-year retention discipline.
- **Auditor stories**: this story closes the Stories 12-17 forward-thinking cluster and brings the recusal-protocol arc to its parliamentary-scale instantiation. Dawn's 4:30 PM grandchildren-verifiability answer is the spec's most concentrated parliamentary-defensibility statement; Steve's eleven-weeks-later parallel testimony is the protocol working at its highest stakes.

The spec-section confirmation memo and engagement debrief are filed under ESVH's compliance-track records and the firm's parliamentary-inquiry-context engagement category.
