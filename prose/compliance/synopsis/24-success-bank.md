# Story 24 — Success Bank (Texas Department of Banking IT + safety-and-soundness examination, alternate-year state-only cycle)

**Story file:** `docs/auditor-stories/24-success-bank.md`
**Engagement type:** Texas Department of Banking full-scope examination — combined safety-and-soundness (CAMELS) and IT (InTREx / URSIT) — of a ~$2.9B Texas state-chartered commercial bank on the alternate year when the Department examines alone and the FDIC is not present. The bank has run a cryptographic evidence chain-of-custody across regulated artifacts for ~14 months; the examination team encounters it cold.
**Posture going in:** State nonmember bank (FDIC is the federal prudential supervisor, absent this cycle). First-Day Letter out four weeks prior; IT Profile questionnaire out ~90 days prior; most loan and asset data staged through the secure portal, so on-site work skews to loan classification, control testing, the IT exam, and one spring cybersecurity incident. The novelty the exam has to reckon with: the bank claims the examiners can *re-run* evidence verification rather than accept an attestation. One commissioned examiner does not believe a self-signed chain can mean anything, and says so in the first hour.
**Outcome posture:** Confirmation — five confirmations; one remediated IT finding (key-registry retention floor) plus its BSA-side cross-reference; composite 2, URSIT 2; no MOU, no Commissioner's order.

## Type of audit
An alternate-year, state-only TDoB examination framed so the state cycle carries the same weight the joint federal-state cycle carried two years earlier. What makes it distinctive is that the institution runs a verifiable evidence chain-of-custody — the first the Department has examined — and the dramatic hinge is the shift from *trust by attestation* (the historical norm: bank attestation + examiner reconciliation + secure-portal transport + confidentiality) to *trust by reproduction*, where the examiner re-runs the reference verifier instead of taking the bank's word. The emotional core is a newly commissioned IT examiner (Emmett Cole, Financial Examiner IV) who dismisses the chain as "signing your own homework with a fancier pen" and is turned, on-page, not by persuasion but by independently validating the signer and breaking-then-reproducing the verdict himself.

## Interested parties (spec readers)
- **TDoB Examiner-in-Charge (Commissioned Bank Examiner, FE VI)** — signs the Report of Examination, fronts exit and board meetings; reads for finding language, rating discipline, and the boundary between "the bank has a good story" and "we verified it ourselves."
- **TDoB IT examiner (newly commissioned, FE IV)** — InTREx / URSIT specialist; the skeptical-examiner persona; reads for how the "bank signs its own evidence" objection is answered by independent registry validation.
- **TDoB asset-quality examiner (FE V)** — loan classification; reads for how provenance complements (never replaces) reconciliation to the loan trial balance and GL.
- **TDoB BSA/operations examiner (FE III)** — reads for the five-year BSA retention window against the key-registry retention floor.
- **TDoB Assistant Bank Examiner (FE II)** — First-Day-Letter reconciliation; reads for the artifact-hash-to-seal confirmation step layered onto conventional footing/tying.
- **Texas Banking Commissioner / Austin HQ** — reviews the ROE; the 7 TAC §3.24 incident notice is filed to this office; guards against a rating inflated *because* the bank runs a chain.
- **FDIC (federal prudential supervisor, absent this cycle)** — reads the state ROE next cycle; the CSBS-accreditation "comparable to federal" bar is what the state-only exam rests on.
- **Institution CISO / CIO / CRO-CAE** — stood up and operate the chain; consume the findings and remediate the retention floor same-day.

## Top spec sections used
- **§1.1 / §1.2** — compositional-security three-layer simultaneous-compromise model (the answer to "the bank signs its own evidence") and epistemic-scope limits (integrity/ordering proven; human determinations institution-asserted).
- **§10.76 + §10.1 + §10.5** — HSM-signed IKM key-registry manifest, independent fingerprint reconciliation, and separation-of-duties HSM custody — the mechanism by which the examiner confirms the signer without the bank's tooling.
- **§10.84** — preapproval/ordering primitive generalized to determination-precedes-customer-notice; the cryptographic basis for the 7 TAC §3.24 regulator-before-customer proof.
- **§10.9** — IKM-registry retention floor; the engagement's headline finding (set to 3yr against a 5yr BSA-record longest-lived chained artifact).
- **§14.13 (`audit.supervisory.*`)** — charter authority / dual-supervision context bound into the record and surfaced by the verifier's `tx-dob` profile.
- **Profile seam (verifier-side, presentation-only)** — `--profile tx-dob` changes report vocabulary and framing (surfacing the charter authority and the 7 TAC §3.24 reference) but never the integrity verdict or exit code; the reason a state-only cycle carries the same weight as a joint exam.

## All cited spec sections
- **§1.1** — compositional security across three independent custody layers (capture MAC, daily seal, registry custody); a false PASS requires simultaneous compromise of all three.
- **§1.2** — epistemic scope: chain proves integrity and ordering, not the truth of an institution-asserted human determination.
- **§4.1** — per-tenant HKDF-derived MAC over canonical bytes at capture; the per-event tamper-evidence.
- **§4.2** — daily Merkle seal; single signed root per day; published fingerprints in a location outside the ledger's account.
- **§4.3** — HSM-rooted daily-root signature.
- **§7** — twelve-step verification procedure; PASS/FAIL and the exit-code contract; the deliberate single-byte corruption caught at the byte offset (exit 2).
- **§10.1** — key-fingerprint reconciliation, performed by hand by the examiner before running the verifier.
- **§10.5** — FIPS-grade HSM custody with separation of duties (seal-requestor ≠ registry-custodian ≠ key-extractor).
- **§10.9** — IKM/key-registry retention; the finding: floor must be ≥ the longest-lived chained artifact (BSA 5yr), not the Call Report 3yr window.
- **§10.13** — evidentiary-artifact composition; artifacts citable in the ROE and any downstream state enforcement.
- **§10.19** — chain-coverage map / CC8.1 declaration (the laminated diagram on the boardroom wall).
- **§10.70** — access-trail primitive; examiner reads of confidential exam evidence can be access-trail-bound on the bank's side (the fact of access only, never examiner workpapers).
- **§10.76** — HSM-signed IKM registry manifest as the independently-validatable trust anchor.
- **§10.84** — approval/ordering primitive; the after-event binds the prior-event hash, making event ordering cryptographically provable across separately-sealed days.
- **§14.13** — `audit.supervisory.*` attribute family (charter type, primary state supervisor, federal prudential supervisor, dual-supervision flag); integrity-bound but institution-asserted.
- **Exam-artifact vocabulary** — `audit.exam_artifact.artifact_kind` (board_minutes, loan_file, call_report, gl_extract, policy, log, bsa_record) as a RECOMMENDED shared enumeration for cross-bank portability.
- **`--profile tx-dob`** — presentation-only verifier profile; identical integrity verdict and exit code to the federal profile on the same chain (the determinism guarantee that makes a state exam comparable to a federal one).

## Synopsis

### Audit activity
An alternate-year TDoB-only team out of the Arlington regional office (with one examiner up from Houston) ran a combined safety-and-soundness and IT examination: First-Day-Letter reconciliation with per-artifact hash confirmation, loan-file review and two substandard classifications, the InTREx/URSIT IT exam, the spring cybersecurity-incident timeline, and the exit/board close-out. The junior examiner confirmed twenty-eight staged artifacts hashed to seals over a year old; the asset-quality examiner verified that the appraisal driving a classification was the file the bank held eight months prior and that the GL extract was complete via its parent-job entry; the IT examiner independently validated the HSM-signed key registry against a published root using his own tooling, confirmed a daily seal's key fingerprint by hand, re-ran the verifier, and caught a deliberate single-byte corruption at the byte offset.

### How the spec was used
- **§10.76 / §10.1 / §10.5** — Examiner independently validated the signer (registry manifest vs. published root) before trusting any verifier output; the answer to the self-signed-evidence objection.
- **§1.1** — Three-layer simultaneous-compromise model articulated as the reason self-signed evidence stays tamper-evident.
- **§10.84** — Regulator-notice-before-customer-notice ordering proven cryptographically (after-event binds prior-event hash sealed in an earlier published root) for 7 TAC §3.24.
- **§1.2** — Examiner drew the honesty line: incident-determination time is institution-asserted; notification ordering is proven.
- **§10.9** — Key-registry retention floor finding: 3yr set against a 5yr BSA longest-lived chained artifact; remediated same-day.
- **Profile seam** — Same chain verified identically under `--profile ffiec` and `--profile tx-dob`; framing differs, verdict and exit code do not — the tooling-level expression of "a state exam and a federal exam reach the same answer."

### Results
Five confirmations. One real IT finding (key-registry retention floor set below the longest-lived chained BSA artifact), remediated on-site and taken to the board for the failure-mode education, with a cross-referenced BSA-booklet entry. Two substandard credits, both already watch-listed and adequately reserved; no doubtful, no loss. Composite 2, URSIT 2 (Support & Delivery carrying the one remediated finding), Management and Sensitivity holding. No MOU, no Commissioner's order. The load-bearing outcome is not the ratings but the shift the exam records: for the first time the IT examiner writes *verified* rather than *as represented by management* on evidence provenance and on a regulatory notification ordering — while keeping that word off the human determinations and off his own judgment, the epistemic line the spec's §1.2 scope requires.
