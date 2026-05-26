# Comparative Analysis — Chapter 14 (Northbridge Federal Savings — Return)

*The return engagement. The audit team and the institution have been in this room before; the framework has not moved in the intervening eighteen months. The reference specification has absorbed seven engagement-source amendments in that same window (§10.17 NetiVa; §4.4 + §4.4.1 Sun-Won; §10.19 + `audit.external_artifact.*` Salt Pond; §10.20 + §10.21 plural-array Eberhardt × Lumière). At Ch14 five new M&A-specific sections (§10.24 composition-note amendment + §10.39 + §10.40 + §10.41 + §10.42) meet a production exercise for the first time in the program. The framework reads each row in isolation cleanly across four fields; the M&A structural shape — institutional succession, cross-vendor inheritance, temporal-slice partitioning, multi-axis verdict — is silent in five places.*

---

## How to read this document

See `_STRUCTURE-comparison-template.md` for shape. Cross-chapter editorial migrates to `_OBSERVATIONS-running.md`.

This chapter produced **4 Framework Confirmations**, **5 Framework Inarticulabilities**, and **4 Framework-Silent Observations**. The chapter is the program's second confirmation-posture engagement (after Ch12 — Hill Country FCU); no on-the-record framework-substitution recommendation; institutional-memory closing observation from CAE Marcus Tan lands as cover-memo prose rather than a formal recommendation.

---

## New comparison points specific to this chapter

Five M&A-specific section exercises plus the multi-axis verdict mechanism produce five new comparison points (A through E). The §10.24 composition-note amendment is exercised as a wayfinder discipline rather than a new subsection — comparison point A combines §10.24 + the three-paragraph amendment.

---

### A. §10.24 entity-succession with cross-vendor-target composition-note amendment

**The audit-room question.** *"How does the post-close chain claim institutional inheritance of a fourteen-year non-chain history through a structured succession ceremony? What's the wayfinder that lets an auditor reading §10.24 reach §10.39, §10.40, and §10.42 without already knowing the M&A-wave section numbers?"*

**TesseraSeal.** §10.24 entity-succession discipline is the structural anchor for any acquisition / divestiture / merger / spinoff event. The composition-note amendment adds three paragraphs to §10.24 as a wayfinder for the cross-vendor-target subcase: (a) §10.39 successor-attestation envelope binds the eight fields; (b) §10.40 cross-vendor cross-anchor binds the foreign-vendor's signed artifacts under §10.19 reuse; (c) §10.42 backfill seal HSM-signs the Merkle-included baseline. Pre-mortem rejected three alternatives (new subsections; inline expansion; unstated composition) in favor of the wayfinder amendment because the cross-vendor-target subcase fits structurally inside §10.24's mental model. The amendment closes the spec's GAP-1.

**Kognitos.** No field for entity-succession discipline at all. The twelve-row schema has no mental model for "how an institution's chain inherits a predecessor's history through a structured succession ceremony." Field 2 (actor identity) form-mismatches against corporate-officer dual-signature pairs under HSM-rooted attestation; the field was authored for an SSO-authenticated session identity logging into a system, not for two CFOs executing a close ceremony.

**Speculation gap.** Under Kognitos, an auditor reading the chain six months post-acquisition sees twelve-field-conformant rows on the post-cut-over perimeter and either (a) takes the institution's word that the pre-cut-over history is inherited, or (b) treats the pre-cut-over history as out-of-scope for the AI-trail audit. Neither path lets the auditor verify that the inheritance is structurally bound. **The auditor speculates that "the prior records are inherited" without structural footing for the composition.**

**Structural reason for the gap.** Kognitos was authored as an AI-decision audit-trail framework. Entity-succession discipline is a chain-of-custody primitive that operates at the *institution's* lifecycle rather than at the AI decision's lifecycle. A framework that lists what data should be present on a single chain row cannot articulate institution-lifecycle events that span multiple chain rows under structural composition.

**Honest assessment.** This is the load-bearing wayfinder for the entire M&A integration audit. Without §10.24's composition-note amendment, the auditor reading the post-cut-over chain has to discover §10.39 / §10.40 / §10.42 independently and figure out how they compose. The amendment turns the cross-vendor-target subcase into a single-paragraph navigation aid. Under Kognitos, neither §10.24 nor the amendment exists; the OCC examination team would have to read the post-merger M&A integration without any structural anchor for institutional-inheritance discipline. **Severity: high.** First M&A integration audit in the program where §10.24's composition-note amendment is exercised; Ch04 (Atrio Cascadia acquisition) exercised the original §10.24 wording but pre-dated the §10.39-§10.42 wave.

---

### B. §10.39 successor-attestation envelope — eight-field shape

**The audit-room question.** *"At the moment of legal close, what chain entry binds the eight institutional facts of the succession (target legal name + LEI, acquirer HSM key fingerprint, baseline-manifest kind, baseline-manifest SHA-256, companion-backfill-seal run-id, dual-signatures pair, effective UTC)? How does the verifier know it's looking at a succession event and not an ordinary chain entry?"*

**TesseraSeal.** §10.39 successor-attestation envelope is a single chain entry produced at the moment of legal close. Eight required fields under MAC: `target_legal_name`, `target_lei` (validated per RFC 9101 LEI registry), `acquirer_hsm_key_fingerprint`, `baseline_manifest_kind` (enumeration `prior_vendor_chain | prior_vendor_signed_pdfs | baseline_diary | mixed`), `baseline_manifest_sha256` (over JCS-canonicalized leaf list), `companion_backfill_seal_run_id` (bidirectional cross-reference to §10.42), `dual_signatures` pair (§10.17 from-entity / to-entity discipline), `effective_utc`. The dual-signature validator is a shared envelope-utility module across §10.24 / §10.39 / §10.42 — lifted out after a pre-mortem review pass caught divergent copies in the early drafts. Verifier dispatches on the envelope's discriminator and runs the eight-field validation.

**Kognitos.** Field 2 (actor identity) form-mismatches as described above. Field 12 (tamper-evident proof) confirms the envelope's integrity but cannot articulate the envelope's *role* — that the eight-field shape binds the institutional succession as a structured event. The other ten fields are either form-mismatched against the envelope's institutional-event shape (Fields 4-10 are oriented to AI-decision contents) or trivially satisfied (Field 11 hash chain; Field 1 timestamp).

**Speculation gap.** Under Kognitos, an auditor sees one chain entry on 2025-11-21 at 16:42 UTC with Fields 1, 11, and 12 satisfied and Fields 2-10 either blank or form-mismatched. The framework records "the integrity proof exists" and stops. The auditor cannot verify that the entry is a *successor-attestation envelope* with eight bound institutional facts; the auditor cannot verify that the eight facts are required, not optional; the auditor cannot verify that the envelope's `companion_backfill_seal_run_id` resolves bidirectionally to a §10.42 seal record. **The auditor speculates that "the M&A integration is captured" without structural footing for the envelope's eight-field shape.**

**Structural reason for the gap.** Kognitos's twelve-row schema treats each chain entry as a row of an AI-decision audit trail. The §10.39 envelope is an institutional-event chain entry — same chain, different mental model. A framework authored for AI-decision capture cannot articulate institutional-event shapes without expanding the row schema, and Kognitos's brevity at twelve rows is part of its value proposition.

**Honest assessment.** First chapter where §10.39 is exercised in production. Five months past the wave's spec-body landing; six months past the production cut-over. The envelope verifies cleanly under the reference spec verifier; the framework records one row with two satisfied fields and seven form-mismatched/blank fields and no structural slot for the eight-field shape. **Severity: high.** The eight-field envelope is the integrity claim's anchor for the M&A; if the auditor cannot articulate the envelope, the rest of the integration's structural reach collapses to "the proof exists."

---

### C. §10.40 cross-vendor chain-merge cross-anchor — 4,230-leaf reuse under `audit.external_artifact.*`

**The audit-room question.** *"The acquired institution ran on a non-chain vendor for fourteen years. How does the post-close chain claim institutional inheritance of 2,407 signed daily roll-up PDFs from the prior vendor plus 1,823 unsigned institutional-archive PDFs without breaking the chain's audit invariant?"*

**TesseraSeal.** §10.40 cross-vendor chain-merge cross-anchor binds the foreign-vendor's signed artifacts and the institution's unsigned baseline diary under §10.19's `audit.external_artifact.*` six-attribute family reuse — the same family Salt Pond drove into the reference spec at Ch10. Each baseline-manifest leaf carries `kind`, `identifier`, `sha256`, `received_at_utc`, `source_party`, `evidentiary_role`. The 4,230 leaves are JCS-canonicalized into a leaf list; the leaf list's SHA-256 is the `baseline_manifest_sha256` declared in the §10.39 envelope and cross-bound in the §10.42 seal. Verifier reconciles in approximately eleven minutes at close, eleven minutes at three months post-close, and eleven minutes at six months post-close. 4,230-for-4,230 byte-equal matches reproducibly.

**Kognitos.** Field 6 (input data + source attribution) partially applies to the institution's source-attribution claim — each leaf is attributed to "Cumberland Heritage Federal S&L (legacy vendor system)" — but the field's authoring assumes AI-influenced events as the artifact under capture, not pre-AI-era historic PDFs from a predecessor's daily operations. Field 12 confirms the Merkle-included integrity proof but cannot articulate the *cross-vendor* property.

**Speculation gap.** Under Kognitos, an institution claiming 4,230 inherited PDFs and an institution claiming 4,230 fabricated PDFs would record identically under Field 6 if both attributed the source string the same way. The framework provides no enumeration of what cross-vendor inheritance looks like structurally — no requirement that the artifacts be hash-bound under a §10.40 cross-anchor, no requirement that the cross-anchor be Merkle-included alongside a §10.42 seal, no requirement that the seal's HSM-key fingerprint match the §10.39 envelope's declared fingerprint. **The auditor speculates that "the prior records are captured" without structural footing for the cross-vendor inheritance.**

**Structural reason for the gap.** Cross-vendor chain-merge is a *cross-institutional-history* operation. Kognitos's mental model is single-institution AI-decision capture; cross-institutional history requires composition across two different audit-trail regimes (the post-close chain plus the prior-vendor signed PDFs), which is the same genre of composition that §1.4 substrate-class inarticulability surfaces under cross-vendor zero-trust composition (Eberhardt × Lumière at Ch11). The framework cannot articulate composition.

**Honest assessment.** First chapter where §10.40 is exercised in cross-vendor form. The cross-cloud form of §10.40 — the wishlist seed Dawn filed at Ch12 (Hill Country FCU) when she wrote *"§10.40 anchor reads as routine on AWS-only. Open question for the next pass: what happens when the substrate moves?"* — is not exercised here; Ch14 stays on AWS for both the original Northbridge perimeter and the inherited Cumberland Heritage perimeter. The cross-vendor variant is the structural feature that lets the post-close chain inherit fourteen years of foreign-vendor history. **Severity: high.** Without §10.40, the post-close chain has no defensible claim to the pre-close history.

---

### D. §10.41 chain-coverage map M&A temporal-slice extension — three named partitions with `out_of_chain_handoffs`

**The audit-room question.** *"The cut-over window was six weeks. During that window, the legacy vendor system and the post-close chain SDK ran in parallel. Three dual-write loan-servicing handoffs bypassed the chain briefly. How does the auditor read the coverage map to audit each partition independently, and how are the bypass moments documented with reconciliation contracts?"*

**TesseraSeal.** §10.41 chain-coverage map M&A temporal-slice extension partitions the institution's chain coverage by *time* across the M&A integration. Three named partitions: pre-acquisition (2011-04-01 through 2025-10-10 close-minus-1; coverage source `prior_vendor_signed_pdfs` + `baseline_diary_unsigned`; bound under §10.42); cut-over window (2025-10-10 through 2025-11-21; coverage source dual-write parallel operations; `out_of_chain_handoffs` enumerated with reconciliation timestamps); post-cut-over (2025-11-21 through present; coverage source post-close SDK fully instrumented; `out_of_chain_handoffs: 0`). Each partition's `out_of_chain_handoffs` entry names the specific moment, the operational context, and the reconciliation timestamp; the runbook requires reconciliation within twenty-four hours; all three handoffs landed within sixteen hours.

**Kognitos.** No field for temporal-slice partitioning. The twelve-row schema treats each chain entry as an independent row; it has no concept of partitions across time or of `out_of_chain_handoffs` that bypass the chain during a defined window with documented reconciliation. Field 12 verifies post-cut-over partition entries cleanly but cannot articulate the partitioning.

**Speculation gap.** Under Kognitos, an institution where the cut-over window was clean (zero bypass) and an institution where the cut-over window had three documented dual-write handoffs with reconciliation would record identically — both produce twelve-field-conformant chain rows after cut-over, both verify cleanly under Field 12. The bypass-discipline + reconciliation-contract is structurally invisible. **The auditor speculates that "the cut-over was clean" without structural footing for the bypass enumeration.**

**Structural reason for the gap.** Temporal-slice partitioning is a *coverage-shape primitive* across time. Kognitos's row-shape addresses what data should be present on a single chain row; it does not address how chain coverage varies across time during a structured institutional transition. This is the same genre of coverage-boundary inarticulability that the program has accumulated since Ch02 (Mercator's two-zone bifurcation) — first surfaced for spatial partitioning, now extending to temporal partitioning.

**Honest assessment.** The OCC examination team will read the coverage map first. The three named partitions, the three documented handoffs, and the reconciliation discipline are the structural shape of the M&A integration's audit defense. Under Kognitos, the coverage map is a piece of paper that names something the framework has no slot for. **Severity: high.** First temporal-slice extension exercise in the program; first chapter where chain-coverage boundary applies to time rather than to space.

---

### E. §10.12 `additional_verifications` array — multi-axis verdict mechanism

**The audit-room question.** *"When the verifier dispatches on the §10.42 backfill seal and returns PASS with exit code 0 plus `additional_verifications: ['backfill_seal_verified']`, what does the second axis mean? How is it different from the exit code? Why is the verdict mechanism two-axis instead of one-axis?"*

**TesseraSeal.** §10.12 verdict object carries one base exit code (0-6 closed enum) plus an `additional_verifications` array that names which additional integrity dimensions have been confirmed beyond the base proof. `backfill_seal_verified` for §10.42; `quantum_signature_verified` for §10.53 future hybrid post-quantum transitions; room for future bonus verifications. Pre-mortem explicitly rejected expanding the exit code enum to include code 7 / 8 / etc. because the combinatorial blow-up across §10.42 + §10.53 + future bonuses would make the exit-code semantics unstable. The two-axis verdict mechanism (one closed-enum exit code + one open-list array) preserves stable exit codes while allowing additional verifications to land additively.

**Kognitos.** Field 12 wording is singular — "a cryptographic proof — typically a hash chain, Merkle tree, digital signature, or append-only / WORM storage equivalent." The framework treats the integrity proof as a single binary verdict per row. There is no concept of multi-axis verdicts. The framework's mental model: one row carries one integrity proof.

**Speculation gap.** Under Kognitos, an institution running the verifier with exit code 0 and `additional_verifications: []` (no additional checks) and an institution running the verifier with exit code 0 and `additional_verifications: ['backfill_seal_verified']` (the backfill seal is structurally bound to the §10.39 envelope) would record identically as "Field 12: ✓." **The auditor loses the second axis.**

**Structural reason for the gap.** Multi-axis verdict mechanism is a verifier-output discipline that emerges only when the spec authors have implementation experience with verifier dispatch paths across spec sections that compose. A framework authored as a row-list schema cannot articulate verifier-verdict shape because the verdict shape is a property of the verification *procedure*, not of any single row.

**Honest assessment.** The multi-axis verdict matters specifically when the institution has additional integrity dimensions to claim beyond the base proof — backfill seals at M&A close (§10.42), hybrid post-quantum signatures at PQC transition (§10.53), GPU-attestation verification at hyperscale inference (§10.65), and any future bonus verifications that the spec absorbs through the §12 change-log mechanism. **Severity: medium-high.** At Ch14 specifically, the `backfill_seal_verified` axis is the structural claim that the seal at close is properly bound to the §10.39 envelope; without it, an auditor cannot distinguish a §10.42-bound chain from an ordinary chain that happens to have a seal record.

---

## Recurring from earlier chapters

Eighteen lines (M&A integration as a return engagement reproduces many prior framework-side issues).

1. **Single-timestamp model (Field 1 vs. §4.4 dual timestamps)** — recurring from Ch01; Northbridge unchanged from original architecture; capture-time vs sealing-time distinction still framework-silent at thirty-six months in production.

2. **Late-arrival event handling (no field; §4.4.2 `late_binding=true`)** — recurring; cut-over window's three out-of-chain handoffs are a structurally similar but distinct phenomenon (bypass-discipline rather than late-arrival within partition); both invisible to Kognitos.

3. **Severity-classification normativity (no clause; §10.16 MUST-NOT downgrade)** — recurring from Ch01; Northbridge unchanged.

4. **Compositional security (Field 12 singular vs. §1.4 three independent layers)** — recurring; the post-merger M&A integration adds a fourth layer (the §10.39-§10.42 wave) without changing the §1.4 base.

5. **IAM lifecycle as audit-trail-captured (Field 3 vs. §10.2 + §10.18 chain-driven IAM)** — recurring; the dual-signature pair under §10.39 envelope is an institutional-event IAM extension that the framework cannot articulate.

6. **Connector-source attribute family (Field 6 vs. §4.4.6 six-attribute family)** — recurring; the cross-vendor cross-anchor extends the family from connectors to historic-artifact baselines.

7. **Coverage-boundary primitive (no field; §10.19 chain-coverage map)** — recurring; the M&A temporal-slice extension at §10.41 is a temporal variant of the spatial coverage-boundary primitive surfaced from Ch02 onward.

8. **Cross-vendor model-handover schema (no field; §10.21)** — recurring; the §10.40 cross-vendor cross-anchor extends from in-vendor to cross-vendor-target for institutional inheritance.

9. **Entity-succession (no field; §10.24)** — recurring from Ch01 theoretical and Ch04 Cascadia acquisition; first chapter where §10.24's composition-note amendment is exercised in production.

10. **HSM partition-ceremony attestation (no field; §10.17 dual-signature pair shared envelope-utility module)** — recurring; the shared utility module across §10.24 / §10.39 / §10.42 surfaces through three different M&A-specific exercises in one engagement.

11. **§10.13 evidentiary-retention floor (no field; vendor-escrow variant for prior-vendor PDFs)** — recurring; Northbridge inherits Cumberland Heritage's prior-vendor escrow on the 2,407 signed PDFs under contractual arrangement with the legacy thrift-software vendor.

12. **§10.26 reference-verifier distribution (no field; CC8.1 three-name discipline)** — recurring; same verifier Mike ran in Ch01 with updated dispatch paths for §10.39 / §10.40 / §10.42.

13. **§10.66 model-weight lineage DAG (no field; vendor-replacement variant)** — recurring from Ch11 / Ch12; Cumberland Heritage's pre-close AI wealth advisor model is one lineage step back from Northbridge's current advisor model; the lineage DAG walks back through the cross-vendor anchor.

14. **§10.69 per-customer disclosure subtree (no field)** — recurring from Ch04 / Ch12; Northbridge's six-month-post-close §1033 disclosure capability extends across the cross-vendor anchor for any Cumberland Heritage customer who requests their disclosure.

15. **§10.18 cross-language CC8.1 discoverability (no field)** — not exercised at Ch14 (both Northbridge and Cumberland Heritage operate in English).

16. **§4.4 cross-border-transfer attribute family (no field)** — not exercised at Ch14 (both perimeters are US-only).

17. **§1.2 SDK-process-compromise residual (no field; §10.35 partial compensation only at edge)** — recurring as theoretical posture; Ch14 does not surface edge endpoints, so the residual sits as it did in Ch01.

18. **§12 change-log mechanism (the framework-can-grow meta-property)** — recurring; in the eighteen months between Ch01 and Ch14, the reference spec absorbed seven engagement-source amendments (§10.17 NetiVa; §4.4 + §4.4.1 Sun-Won; §10.19 + `audit.external_artifact.*` Salt Pond; §10.20 + §10.21 plural-array Eberhardt × Lumière); the Kognitos checklist Dawn carried to Northbridge today is byte-equal to the one she carried at Ch01. Eighteen months is the operational time at which the framework-grows-vs-fixed contrast becomes a structural property the institution can recognize directly.

---

## Research signal

### Confirmation-posture chapter-class — second instance

Ch12 (Hill Country FCU) was the first confirmation-posture chapter in the program: chain ran clean across eleven months on a single AWS substrate; framework recorded clean across twelve fields; no on-the-record stakeholder statement; engagement closed 22% under budget. Ch14 reproduces the pattern with a different shape: chain runs clean across thirty-six months (original perimeter) + six months (inherited perimeter); framework records four clean Confirmations; five Framework Inarticulabilities sit in the firm's parallel observations; no formal framework-substitution recommendation; engagement closes at 12:18 PM Day 2 (well within the two-day budget).

The two instances confirm confirmation-posture as a reproducible chapter-class:

| Property | Ch12 (Hill Country FCU) | Ch14 (Northbridge Return) |
|---|---|---|
| Chain integrity | Clean across 11 months on AWS `us-east-1` | Clean across 36 months original + 6 months inherited on AWS |
| Framework Confirmations | All twelve fields PASS | Field 1 + Field 6 (partial) + Field 11 + Field 12 = 4 clean |
| Framework Inarticulabilities (new) | 0 | 5 (M&A-wave-specific) |
| Framework Under-Reportings (new) | 0 | 0 |
| Framework-Silent Observations (new) | 4 | 4 |
| On-the-record stakeholder statement | None (CAE closes anxiety quietly) | None (CAE delivers institutional-memory closing observation) |
| §12 engagement-source amendments | 0 | 0 |
| Engagement closes | 22% under budget | At 12:18 PM Day 2, within two-day budget |
| Foresight-cluster pressure on §10.40 | Opener — filed quietly | Partial — cross-vendor variant exercised; cross-cloud variant remains pending |

The confirmation-posture chapter-class is structurally distinguished from the framework-substitution chapters (Ch04 Veronika; Ch05 Helmstad CCO+CQD; Ch06 Soren; Ch07 Holland; Ch08 Pankaj; Ch09 Min-seo+Wei-ling; Ch10 Patrick+Naomi; Ch11 Heinrich+Sébastien; Ch13 Aparna composed-compensation variant) by *absence of formal recommendation*. The institution recognizes the framework gap through observation rather than escalation; the audit team's parallel observations carry the structural reach; the cover memo includes both the framework Confirmations and the parallel observations side by side.

### Return-engagement institutional-memory pattern

Ch14 is the program's first return engagement. Marcus Tan's closing observation — *"I read your firm's running notes when they come across my desk through industry channels. I read Pankaj's NetiVa cover memo when it became public a year ago. I read Heinrich and Sébastien's Eberhardt × Lumière cover memo when it landed. I am not going to ask for an on-the-record framework-substitution recommendation today, because the firm's parallel observations have done that work already and the OCC examination team will read both side by side."* — names a new dynamic that emerges only at return engagements: *the institution has watched the framework apply across multiple engagements through industry channels and has reached its own conclusion without needing to escalate at this specific engagement*.

This is structurally distinct from first-engagement direct boundary-setting (Veronika, Aparna) and from sharper-dimension addition (Soren, Holland). It is the recognition that the firm's parallel observations have become the de facto institutional record of what the framework cannot articulate, and that the OCC examination team — like Marcus himself — will read the parallel observations alongside the framework Confirmations. The institutional-memory pattern is likely to recur at other return engagements; the prediction is that Ch20 (Mission Plaza Bank — possibly a return), and any future return engagement, may close the same way.

### M&A integration as a chapter-class

Ch14 is the program's first M&A integration audit in production (Ch04 Atrio exercised §10.24 against a Cascadia subsidiary that was already on the chain; that was *intra-institutional* succession, not *cross-vendor-target* succession). The M&A integration chapter-class is structurally characterized by:

- One engagement that exercises five spec sections simultaneously (§10.24 composition-note amendment + §10.39 + §10.40 + §10.41 + §10.42).
- A baseline-manifest assembly process spanning weeks (three weeks at Cumberland Heritage).
- Three named partitions across time (pre-acquisition / cut-over window / post-cut-over).
- A structured close ceremony with dual-signature pair under HSM-rooted attestation.
- A backfill seal that Merkle-includes the baseline-manifest alongside a metadata leaf with `seal.backfill_at_close = true`.
- An OCC (or analog regulator) post-merger examination that reads the chain-coverage map first.

Future M&A integration audits — and the program has at least two more probable M&A engagements in Stories 15-22 (Polaris Reinsurance's likely Lloyd's syndicate roll-up posture; potential Mission Plaza Bank / Brazos Federal Mission Plaza variant) — are likely to reproduce this five-section exercise with variations. The chapter-class establishes that M&A integration produces a structurally dense exercise that the framework's row-shape cannot articulate at five distinct spots.

### Foresight-cluster pressure on §10.40 — partial landing

Ch12 (Hill Country FCU) filed the foresight-cluster opener: *"§10.40 anchor reads as routine on AWS-only. Open question for the next pass: what happens when the substrate moves?"* Ch13 (Saraswati Microfinance) did not press on §10.40 — the architecture stayed within AWS Mumbai single substrate within India sovereign-data territory. Ch14 partially lands the cluster: §10.40 is exercised in cross-vendor form (the foreign-vendor's signed PDFs as cross-anchor), but not in cross-cloud form. The substrate stays AWS for both the original Northbridge perimeter and the inherited Cumberland Heritage perimeter.

The cross-cloud variant of §10.40 — the original substrate-move question — remains pending. Ch15 (Polaris Reinsurance Lloyd's), Ch16 (Lyceum Health), or Ch17 (Helvetian Tax Authority — most likely cluster-closer given Swiss sovereign-data hard edge) are the candidates for the cross-cloud §10.40 amendment. The cluster-tracking discipline calls for the spec-section catalog row for §10.40 to be updated at Ch14 from "wishlist seed" to "engagement-source for cross-vendor variant," with the cross-cloud variant carried forward as a separate sub-row that remains pending.

---

## What's distinct about this chapter

1. **First return engagement in the program.** Dawn and most of the audit team have been at Northbridge before (Ch01); Marcus Tan is the same CAE; Greg is the same SRE; the same engagement room with new paint. The audit team carries eighteen months of accumulated framework-silent observations against the Kognitos checklist from thirteen other engagements; the institution has watched the framework apply across thirty-six months in production and through industry-channel reading of other firms' cover memos.

2. **First M&A integration audit in production.** Five M&A-specific spec sections (§10.24 composition-note amendment + §10.39 + §10.40 + §10.41 + §10.42) exercised simultaneously at one institution for the first time in the program. Ch04 (Atrio Cascadia) was intra-institutional succession only; the cross-vendor-target subcase was not part of the spec at Ch04 time.

3. **Second confirmation-posture chapter.** Reproduces Ch12's pattern with different shape: no on-the-record framework-substitution recommendation; institutional-memory closing observation from Marcus Tan lands as cover-memo prose; engagement closes within budget; parallel observations carry the five Framework Inarticulabilities to the OCC examination team.

4. **Cross-vendor variant of §10.40 partially lands the foresight cluster.** The cross-vendor cross-anchor exercise at Ch14 is the first §10.40 production exercise in any form; the cross-cloud variant — the original Ch12 question — remains pending for Ch15-Ch17.

5. **First multi-axis verdict mechanism exercise (§10.12 `additional_verifications` array).** The verifier's verdict object carries `backfill_seal_verified` alongside exit code 0 in PASS form for the first time in the program. Field 12's singular wording cannot articulate the second axis.

6. **First exercise where Field 2 (actor identity) form-mismatches against a corporate-officer dual-signature pair under HSM-rooted attestation.** The §10.39 envelope's dual-signature pair (target CFO + acquirer CFO) is an institutional-event identity that the framework's AI-decision-session mental model has no analog for.

7. **First chapter where the firm's parallel observations corpus is named explicitly as an internal-knowledge-base.** Dawn references "approximately eighty observations indexed by engagement and spec-section" across the fourteen engagements. The cover memo names the parallel observations as a reading aid for the OCC examination team. The institutional-memory pattern recognizes the parallel observations as a structural compensation for the framework's reach.

8. **Marcus Tan's closing observation as a new variant of institutional voice.** Distinct from on-the-record framework-substitution recommendation (Pankaj+Min-seo+Wei-ling+Patrick+Naomi+Heinrich+Sébastien); distinct from direct boundary-setting (Veronika, Aparna); distinct from sharper-dimension addition (Soren, Holland). Marcus delivers a *return-engagement institutional-memory observation* that names the firm's parallel observations as the institution's de facto reading and explicitly declines to escalate at this engagement because the cumulative work has done the escalating already through industry channels. This may be an eighth voice pattern, depending on whether it recurs at other return engagements or stands as a one-off variant of the confirmation-posture closing.
