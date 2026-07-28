# Story 24 — Success Bank (Texas state-chartered bank; the team on-site during a live TDoB examination; first named encounter with a Department examiner)

**Story file:** `docs/auditor-stories/24-success-bank.md`
**Engagement type:** Three-day readiness-and-support engagement at a ~$2.9B Texas state-chartered commercial bank in Austin, on-site *during* the Texas Department of Banking's alternate-year (state-only) IT and safety-and-soundness examination — the first engagement in the corpus where the team is in the building while a live regulator works the chain. Raj is Lead Auditor.
**Posture going in:** The bank has run a cryptographic chain-of-custody for ~14 months; no TDoB examiner has ever seen one. The bank's ex-FDIC Chief Risk Officer retained the team specifically to be in the room when the Department's IT examiner encounters the chain, because a state examiner who has never met a chain-of-custody will distrust it on sight. The team's job is not to defend the chain but to help the examiner check it himself. One examiner — Danny Tran — walks in calling it "a bank signing its own homework with a fancier pen," and says so in the first hour.
**Outcome posture:** Confirmation — four confirmations; one remediated IT finding (key-registry retention floor) with a BSA-side cross-reference; composite 2, URSIT 2; no MOU, no Commissioner's order. Emotional payoff: the off-page "Texas Department of Banking examiner" of Stories 20–21 becomes a named person who, for the first time in fifteen years, writes *verified* rather than *as represented by management* — witnessed by the team.

## Type of audit
A three-day on-site readiness-and-support engagement that, unlike every prior engagement, overlaps the regulator's own examination in progress. The corpus norm is a pre-exam readiness pass with the examiner weeks off-page; here the TDoB team has already commandeered a conference room, and the audit team works the adjacent technical room, present when the Department's IT examiner comes across the hall to work the chain. The distinctive tension is structural: for two prior Texas engagements (Story 20 Mission Plaza, Story 21 Brazos) the team prepared banks for "the Texas Department of Banking examiner" as an off-page fact who "closed it in one meeting at the March cycle." This engagement gives that fact a name and a real objection, and the dramatic hinge is the shift from *trust by attestation* to *trust by reproduction* — witnessed in the examiner's own hands rather than argued in a memo. The recurring question is *"can the examiner check it himself?"*

## Interested parties (spec readers)
- **TDoB Examiner-in-Charge (Commissioned Bank Examiner, FE VI — Karen Wilson)** — signs the Report of Examination, sets the shared-floor arrangement, fronts exit and board meetings; reads for finding language and rating discipline.
- **TDoB IT examiner (Danny Tran)** — InTREx / URSIT specialist; the skeptical-examiner persona; reads for how the "bank signs its own evidence" objection is answered by independent registry validation performed by the examiner himself.
- **TDoB asset-quality and BSA examiners (Ray Hernandez, Melissa Johnson)** — loan classification and the five-year BSA retention window against the key-registry floor.
- **Institution CRO / CAE (ex-FDIC examiner)** — retained the team to stand next to the examiner; reads for the mechanism, not the enthusiasm.
- **Institution CISO / CIO** — stood up and operate the chain; remediate the retention floor on-site.
- **Texas Banking Commissioner / Austin HQ** — reviews the ROE; the 7 TAC §3.24 incident notice is filed to this office; Austin is also the Commissioner's seat and the vendor's home city.
- **FDIC (federal prudential supervisor, absent this cycle)** — reads the state ROE next cycle; the CSBS-accreditation "comparable to federal" bar is what the state-only exam rests on.
- **MMPWorks vendor liaison / principal designer** — Dawn (spousal-disclosure-paragraph liaison) states the scope boundary; Steve answers a single §10.21 composition question by video under the vendor-recusal protocol.

## Top spec sections used
- **§1.1 / §1.2** — compositional-security three-layer simultaneous-compromise model (the answer to "the bank signs its own evidence") and epistemic-scope limits (integrity/ordering proven; human determinations institution-asserted).
- **§10.76 + §10.1 + §10.5** — HSM-signed key-registry manifest, independent fingerprint reconciliation, and three-role separation-of-duties HSM custody — the mechanism by which the examiner confirms the signer without the bank's tooling (walked by Sonya, the team's custody specialist).
- **§10.84** — ordering primitive; the customer-notice event binds the prior regulator-notice event's hash — the cryptographic basis for the 7 TAC §3.24 regulator-before-customer proof.
- **§10.9** — key-registry retention floor; the engagement's finding (set to 3yr against a 5yr BSA-record longest-lived chained artifact).
- **§10.21** — cross-vendor model handover; the single question routed to Steve under the recusal protocol.
- **Profile invariance (verifier-side, presentation-only)** — `--profile tx-dob` changes report vocabulary and framing but never the integrity verdict or exit code; the reason a state-only cycle carries the same weight as a joint exam.

## All cited spec sections
- **§1.1** — compositional security across three independent custody layers (capture keyed hash, daily seal, registry custody); a false PASS requires simultaneous compromise of all three.
- **§1.2** — epistemic scope: chain proves integrity and ordering, not the truth of an institution-asserted human determination.
- **§4.1** — per-event keyed hash over canonical bytes at capture; the per-event tamper-evidence.
- **§4.2** — daily Merkle seal; single signed root per day; published fingerprints in a location outside the ledger's account.
- **§4.3** — HSM-rooted daily-root signature.
- **§7** — twelve-step verification procedure; PASS/FAIL and the exit-code contract; the deliberate single-byte corruption caught at the byte offset (exit 2).
- **§10.1** — key-fingerprint reconciliation, performed by hand by the examiner before running the verifier.
- **§10.5** — HSM custody with three-role separation of duties (seal-requestor ≠ registry-custodian ≠ key-extractor).
- **§10.9** — key-registry retention floor; the finding: floor must be ≥ the longest-lived chained artifact (BSA 5yr), not the Call Report 3yr window.
- **§10.11.1** — ECOA adverse-action lineage on the AI credit-decisioning surface (the spring reinvestigation walked in fifteen minutes).
- **§10.13** — evidentiary-artifact composition; carried forward from the Mission Plaza and Brazos memos the bank built its deployment against.
- **§10.19** — chain-coverage map / CC8.1 declaration.
- **§10.21** — cross-vendor model handover; the recusal-routed question.
- **§10.70** — access-trail primitive; examiner reads of confidential exam evidence can be access-trail-bound on the bank's side (fact of access only, never examiner workpapers).
- **§10.76** — HSM-signed key-registry manifest as the independently-validatable trust anchor.
- **§10.84** — ordering primitive; the after-event binds the prior-event hash, making event ordering cryptographically provable across separately-sealed days.
- **§14.13** — `audit.supervisory.*` attribute family (charter type, primary state supervisor, federal prudential supervisor, dual-supervision flag); integrity-bound but institution-asserted.
- **Exam-artifact vocabulary** — `audit.exam_artifact.artifact_kind` (board_minutes, loan_file, call_report, gl_extract, policy, log, bsa_record) as a shared enumeration for cross-bank portability.
- **`--profile tx-dob`** — presentation-only verifier profile; identical integrity verdict and exit code to the federal profile on the same chain.

## Regulatory citations (the Texas exam layer)
- **7 TAC §3.24** — Texas cybersecurity-incident notification: notify the Banking Commissioner as soon as practicable, before customer notification, no later than 15 days after determining a reportable incident; the interagency 36-hour federal notice satisfies it. The regulator-before-customer *ordering* is the relationship the chain proves.
- **Texas Finance Code Title 3** — state-charter examination and supervision authority; Austin as the Commissioner's seat.
- **FFIEC IT Examination Handbook + FDIC InTREx** — the IT-exam scaffolding TDoB adopts by reference.
- **URSIT** — the four IT components (Audit / Management / Development & Acquisition / Support & Delivery); composite feeds the CAMELS Management and Sensitivity components.
- **CAMELS** — the Uniform Financial Institutions Rating System composite (a two here).
- **CSBS accreditation** — the trust substrate that makes the alternate-year state exam carry federal weight; the tooling-determinism confirmation (identical verdict under both profiles) reinforces the "comparable to federal" bar.
- **Retention floors** — Call Report 3 years, BSA records 5 years; the 5-year BSA window is the floor behind the key-registry-retention finding, corroborated from the Texas seven-year customer-record floor and FFIEC five-year AI-decisioning floor the team carried out of Brazos (Story 21).
- **Enforcement ladder** — Board Resolution → Memorandum of Understanding → Commissioner's order; none triggered — the finding is a matter for board attention, not an order.

## Synopsis

### Audit activity
The team (Raj Lead; Elena, Mike, Diana, Luis, Chen, Tom, Sonya) worked a three-day readiness-and-support engagement on-site during the TDoB's alternate-year examination, in a technical room across the hall from the Department's commandeered conference room. Day 1 walked the chain with the bank and hosted the Department's IT examiner as he encountered it: Sonya (custody specialist) handed him the published key-registry manifest and stepped back; he validated it against a separately-published root with his own script, confirmed a daily seal's fingerprint by hand, re-ran the verifier only afterward, and produced FAIL at the byte on a deliberate corruption. The retention-floor finding surfaced at lunch (Danny caught it; Tom corroborated from the Brazos floors; the bank remediated on-site). The April incident's regulator-before-customer ordering proved via hash-linkage across two published daily roots. Dawn joined at three as MMPWorks liaison to state the scope boundary; Steve answered a single §10.21 question by video. Day 2 ran the reconciliation slate (loan files, minutes, GL extract completeness, access-trail identity); Day 3 was the Department's exit meeting and board (the team not present, by arrangement).

### How the spec was used
- **§10.76 / §10.1 / §10.5** — The examiner independently validated the signer (manifest vs. published root) with his own tooling before trusting any verifier output; the answer to the self-signed-evidence objection, walked by the team's custody specialist and performed by the examiner.
- **§1.1** — Three-layer simultaneous-compromise model articulated as why self-signed evidence stays tamper-evident.
- **§10.84 / §1.2** — Regulator-before-customer ordering proven cryptographically for 7 TAC §3.24; the examiner drew the honesty line himself (determination time institution-asserted; ordering proven).
- **§10.9** — Key-registry retention floor finding (3yr against 5yr BSA); remediated same-day, corroborated from the Brazos retention floors.
- **§10.21** — The cross-vendor composition question routed to the vendor under the recusal protocol.
- **Profile invariance** — Same chain verified identically under `--profile ffiec` and `--profile tx-dob`; framing differs, verdict and exit code do not — the tooling-level expression of "a state exam and a federal exam reach the same answer."

### Results
Four confirmations. One real IT finding (key-registry retention floor set below the longest-lived chained BSA artifact), remediated on-site, cross-referenced across the IT and BSA booklets, a matter for board attention. Two substandard credits, both already watch-listed and adequately reserved; no doubtful. Composite 2, URSIT 2 (Support & Delivery carrying the remediated finding); no MOU, no Commissioner's order. The load-bearing outcome is a continuity payoff, not a rating: the "Texas Department of Banking examiner" who existed only as an off-page citation across Stories 20–21 becomes a named person (Danny Tran) who, for the first time in fifteen years, gets to write *verified* rather than *as represented by management* — on provenance and ordering, never on the human determinations or his own judgment — because he re-ran the evidence under his own hand while the team watched. The corpus's first engagement with the team on-site during a live regulator examination; an escalation from Story 22 Wasatch, where the team cleared out as the examiners arrived.
