# 03 — Stelvio Industrial (Kognitos-lens)

*A three-zone audit at a steel mill where Kognitos's row-list-as-schema meets PLCs, HMIs, and a historian with `db_owner` mutability*

**Engagement:** CMMC 2.0 Level 2 readiness re-assessment with AS 9100D quality-systems overlay
**Client:** Stelvio Industrial — third-generation family-owned $2.1B specialty steel mill, DoD prime supplier, ITAR §125 export-controlled records, downstream medical-device customer running an FDA design-verification pipeline
**Status:** Three AI services chained for 14 months; OT environment and IT business systems unchained
**Audit team lead:** Dawn
**Client liaison:** Renata Voss, Chief Compliance Officer; Joaquin Hidalgo, Director of OT Security

**Audit team's framework:** Kognitos's 12-field AI audit-trail schema. The team has now done two engagements under this framework (Northbridge, Mercator) and has a working pattern for bifurcated assessment — staple two complete framework runs and author the cross-zone narrative in prose. Stelvio is the first three-zone engagement: AI / OT / IT business. The framework still has no concept of coverage scope. The team will be stapling three runs this time.

**Posture going in:** Stelvio is asking for confirmation that the chained AI services pass CMMC 2.0 Level 2 / AS 9100D / ITAR §125 / DFARS 252.204-7012 for the in-scope subset, plus a documented remediation timeline for the OT and IT business systems. They've published a quarterly chain-coverage map for 14 months. They expect the audit team to confirm each cell rather than discover boundaries per-finding.

---

## 🌅 8:30 AM — Kickoff (Printed Coverage Map on the Table)

Renata Voss walked into the engagement room with two binders and a wall-sized print of the chain-coverage map. The map had three columns: green (AI chained), amber (OT unchained, Phase 2 in 12 months), red (IT business unchained, Phase 3 in 18 months / Phase 4 distant). Every system, every rollout posture, every evidentiary substitute on one page.

Dawn looked at it.

The Kognitos 12-field template in her bag still had no row for "coverage map." She had stopped looking for one.

"Renata. Before we start. I want you to know what we're walking into. The framework we're operating under has 12 rows. Your map has three columns and twenty-something rows of systems. We will run our framework against each column separately and write a three-part report. The cross-zone narrative will be in the cover memo. The coverage map you've printed is what gives us the structure; our framework does not have an equivalent."

"Understood," Renata said. "The map has been published quarterly for 14 months. Every quarter, the institution emits a sealed `chain.coverage_map_published` chain event that anchors the version we're operating under for the lookback period. The audit team's job is to confirm each cell, not discover boundaries."

She turned the map around so the team could see all three columns.

"Green column. Three AI services — predictive maintenance, QC classification, ITAR screening NLP. Chained for 14 months. The cells in this column are what we expect to confirm pass."

"Amber column. OT. The historian, the TIA Portal log, the Plex MES, the HMI on the catwalk, the PLC line. Phase 2 in 12 months — funding is approved pending this report."

"Red column. IT business. SAP with `SAP_ALL` closure discipline issues, Dynamics with field-history selectively enabled, SharePoint QMS without integrity checks. Phase 3 in 18 months; Phase 4 distant."

She paused.

"Joaquin is the OT side. He'll walk you through after lunch. Joaquin is direct."

"Good," Diana said.

Renata had a follow-up that Dawn was starting to expect from clients running the reference spec.

"You'll want to ask the §1.2 epistemic-scope question. The chain proves what each AI service said at a specific time and that the record was not tampered after capture. It does NOT prove the QC classification was right, the predictive maintenance prediction was accurate, or the ITAR screening was complete. The downstream medical-device customer's FDA design-verification submission references three of our chain entries directly — the cover letter to the FDA uses §1.2 verbatim language so the BIMO inspector reads the spec's epistemic-scope clause directly rather than the institution's gloss."

Dawn wrote: *§1.2 epistemic scope. Downstream cover letter uses verbatim spec language. Kognitos has no equivalent.* ◇.

She wrote a second note: *Three-zone bifurcation. Same framework limit as Chapter 02 but extended. Kognitos still has no coverage-map primitive; the institution carries one anyway.*

"Let's start with the AI side this morning. After lunch, we'll do the OT walkthrough. Tomorrow morning is the IT business systems. Three days is the schedule."

Renata nodded.

"There's a thing I'd like to show you before you start. Five minutes. We're going to walk to the catwalk."

---

## 🔍 9:00 AM — The Catwalk Demo

The catwalk was a steel walkway 30 feet above the QC inspection floor. The PLCs were below. The HMI was below. The TIA Portal log was on a workstation on the floor. The chain backing store was in a server room two buildings away.

Renata pulled a laptop out of a hard case. She tethered it to a 4G hotspot. No corporate WiFi. No bank credentials. The laptop was her personal one — she carried it specifically for this demonstration.

"Pick a date. Pick a service. Pick an entry ID."

Dawn picked 2025-12-04, predictive-maintenance service, the first entry of the day.

Renata typed.

```
$ herald-verify --tenant=stelvio-mill \
                --service=predictive-maintenance \
                --date=2025-12-04 \
                --entry-id=pm-2025-12-04-mill-00001 \
                --strict
```

Four seconds.

```
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified
        against public key stelvio-prod-2025-q4
```

Renata closed the laptop.

"Four seconds. 4G hotspot. Personal laptop. No Stelvio credentials. The downstream medical-device customer ran the same verification last quarter against three of our QC chain entries that fed their April 7 FDA submission. Their compliance team has the published Cosign-signed reference verifier; they pulled the seal records from our published TesseraSeal surface; they verified independently. We were not in the loop on their verification at any layer."

Mike looked at the laptop.

"They got the binary from where?"

"GitHub Releases of the reference verifier project. Cosign signature verified against the sigstore.dev published public key. CycloneDX SBOM in the release. Reproducible build. The customer's compliance lead pulled a per-platform binary, verified the signature, and ran it. That's the §10.26 distribution discipline operationalized."

Mike wrote that down. The Kognitos framework had no field for verifier distribution. Same Gap as Northbridge and Mercator. Now exercised in a real customer-downstream-verification scenario.

> ### ✓ Confirmation #1 — Live verifier demonstration over 4G, no Stelvio credentials (Field 12 with depth not asked)
>
> Renata ran `herald-verify` on her personal laptop tethered to 4G, no Stelvio infrastructure access. Four seconds. PASS. The Kognitos framework records this as one Field 12 Confirmation. The properties of (a) zero institution-side trust at any verification layer, (b) reproducible-build reference-verifier distribution, (c) Cosign-signature trust path, (d) sub-five-second verification over consumer-grade network are framework-silent. Four ◇ marks under one Field 12 Confirmation.

Dawn watched the team take notes. They had seen the same property at Northbridge. They had seen it at Mercator. The framework still didn't have language for it. They were beginning to develop their own internal shorthand: when a bank demonstrated zero-trust verification with a published reference verifier, they marked the property in their own auditor shorthand — *Mercator-class zero-trust verification* — and noted that Kognitos couldn't capture it.

---

## 🧩 10:00 AM — AI Side (Three Chained Services)

Back in the engineering office. Renata's deputy, Sandeep, walked them through the three AI services.

**Predictive maintenance.** A regression model trained on 14 months of vibration sensor data. Daily inferences. Each inference is a chain entry with the model version, the input sensor stream hashes, the predicted-failure-window output, the confidence interval, and the `audit.deployment.intent` attribute. Q4 2025 had a model retraining event that crossed an §10.21 cross-vendor handover — internal handover from the platform team to the operations team, but the §10.21 schema was applied so the handover artifacts (model card, training-data summary, evaluation outputs, hashes) were all sealed chain entries.

**QC classification.** A vision model that classifies steel coil surface defects. The medical-device customer's April 7 FDA submission references three QC entries directly. Each QC entry carries the image hash, model version, classification, confidence, and the inspector's override (if any).

**ITAR screening NLP.** A text-classification model that screens export-control documentation for ITAR-controlled language. Each document scan is a chain entry with the document hash, model version, classifier output, and the human reviewer's disposition (approved / flagged / escalated).

Mike walked his template through each service.

For predictive maintenance:
- Field 1 (Timestamp) — RFC 3339 nanosecond UTC. ✓
- Field 2 (Decision ID) — `entry_id` per inference. ✓
- Field 3 (Human identity) — operations technician identity on override entries. ✓
- Fields 4-5 (System / Model identity) — model_id, model_version, gen_ai.request/response.model. ✓ (Plus the OTel naming depth Kognitos doesn't require.)
- Field 6 (Inputs) — vibration sensor stream hashes with source-sensor IDs. ✓
- Field 7 (Policy/prompt) — `audit.deployment.policy_version` on every entry. ✓
- Field 8 (Reasoning) — feature attributions in the response payload. ✓
- Field 9 (Output) — predicted-failure-window with confidence interval. ✓
- Field 10 (Downstream action) — linked to the maintenance work-order ID. ✓
- Field 11 (Human review) — operations technician override entries chain-linked. ✓
- Field 12 (Integrity proof) — HMAC chain + Merkle + Ed25519 + CloudHSM. ✓

For QC classification: identical pattern. Twelve fields satisfied per entry. Mike noted the downstream FDA submission case — the chain entries the customer referenced satisfied all 12 fields independently, and the customer ran their own verification under §10.26 without any Stelvio-side privilege.

For ITAR screening NLP: identical pattern. The human reviewer's disposition (approved / flagged / escalated) was captured in Field 11 with the structured pick-list reason linked back to the source document.

> ### ✓ Confirmation #2 — All 12 fields satisfied across three chained AI services (predictive maintenance, QC classification, ITAR NLP)
>
> Three distinct AI services, 14 months of operation, all Fields 1-12 cleanly satisfied. Downstream medical-device customer's April 7 FDA submission references three QC entries with independent verification. ITAR §125 export-control documentation screening operates with chain-captured human-reviewer dispositions per Field 11.

Diana walked the IAM split for the AI side. Same chain-driven discipline she had seen at Northbridge and Mercator. Service identities under `predictive-maintenance-prod@stelvio-mill`, `qc-classifier-prod@stelvio-mill`, `itar-screening-prod@stelvio-mill`. Each inference carries the calling operations-technician identity threaded through. IAM grants, revocations, elevation requests all chain-captured.

She added the same chain of ◇ marks the framework couldn't articulate.

> ### ◇ Framework-Silent Observations #1-5 — AI-side compositional security, deployment-intent, OTel GenAI naming, override provenance, IAM lifecycle (recurring from Chapters 01-02)
>
> Five framework-silent observations on the AI side, all matching the pattern established in Chapters 01-02. Severity unchanged.

---

## 🛡️ 11:00 AM — The Direct Tamper Test

Dawn had something she wanted to try. She had run verifier-detection demos at Northbridge (silent-restart) and Mercator (key-rotation transparency). She wanted to try a different attack class here: a direct UPDATE against the chain backing store itself.

"Renata, who has UPDATE permission on the chain backing store database?"

"No one. The INSERT role is the SDK's service account. The SELECT role is the analytics team and the audit team. There is no UPDATE role. There is no DELETE role. The role-creation role was retired after deployment."

"Can we synthesize one for a demo? Sandbox tenant."

Renata thought for a moment.

"We can. Sandbox tenant, with a privileged engineer simulating an UPDATE attempt against the backing store. We have a demo fixture from a Q3 disaster-recovery drill."

She made a call. Twenty minutes later, the screen was up.

The fixture had a 100-entry chain in the sandbox tenant. The "attacker" was a privileged engineer with simulated UPDATE permission on the backing store. They modified one of the middle entries — changed the model output from `defect: minor` to `defect: none` — and recomputed nothing else. The backing store now had an entry whose stored `entry_hash` no longer matched a fresh hash of the modified canonical bytes.

Dawn ran the verifier against the sandbox tenant's day.

```
Status: FAIL
Step:   9
Exit:   3
Reason: entry payload mismatch at entry_id=sb-fixture-2025-q3-00037.
        recomputed entry_hash does not match stored entry_hash.
        single-entry tamper detected.
```

The verifier flagged the tamper at §7 step 9.

Renata ran it with a different switch.

```
$ herald-verify --tenant=sandbox-stelvio --date=2025-09-15 --strict --detect-merkle-mismatch
```

```
Status: FAIL
Step:   10
Exit:   3
Reason: Merkle root mismatch. recomputed root differs from sealed root.
        multi-entry tamper plausible.
```

The verifier flagged the same tamper at §7 step 10 from the Merkle side.

> ### ✓ Confirmation #3 — Tamper-evident integrity proof catches direct backing-store UPDATE
>
> A privileged engineer modified one chain entry directly via simulated UPDATE on the backing store. The verifier flagged the tamper at §7 step 9 (single-entry recomputation) and §7 step 10 (Merkle root mismatch). Two independent verification steps caught the same attack. Field 12 (tamper-evident integrity proof) is satisfied with operational demonstration.

> ### ◇ Framework-Silent Observation #6 — Verifier procedure-step granularity
>
> The verifier reported the specific procedure step (§7 step 9 / step 10) where the tamper was detected. Different attack vectors fail at different procedure steps; the institution's incident-response runbook keys remediation off the procedure step. The Kognitos framework has no language for verifier procedure-step granularity. An institution operating a verifier that returns only "PASS/FAIL" satisfies Field 12 identically.

Dawn wrote that down. She noted: *the bank's reference spec has §7 12 procedure steps with named-reason discipline; Kognitos has none. Specific failure attribution at the IR level depends on the procedure-step granularity the framework doesn't require.*

---

## 🧬 1:00 PM — OT Walkthrough (Joaquin Hidalgo)

Lunch was sandwiches at the visitor lot picnic table. Then Joaquin Hidalgo, Director of OT Security, walked them down to the plant floor.

Joaquin was direct. "We have five OT systems in scope. None are chained today. Phase 2 chains them in 12 months. The audit's job is to document what we have now so the Phase 2 budget number is defensible. I'll walk you through what fails."

The team's working template carried five rows for the OT walkthrough — one row per OT system, each with twelve Kognitos columns.

### Historian (PI System)

Joaquin pulled up the historian database connection. The historian held 18 months of plant-floor sensor data. The connection was bound to a `db_owner` role with no row-level audit. Anyone with that role could UPDATE or DELETE historian rows without leaving a forensic trail.

Joaquin: "We've had this for 22 years. The vendor's recommended pattern doesn't include row-level audit. We're aware. Phase 2 chains the historian extraction via a §4.4.6-style connector pattern."

Mike worked the template:
- Field 12 (Tamper-evident integrity proof) — ✗ Fail. `db_owner` mutability with no row-level audit.
- Field 1 (Timestamp) — ✓ The historian stores millisecond UTC timestamps. (But the timestamps are mutable, so Field 1 satisfied literally but compromised structurally.)

He elevated Field 12 to Finding-001 for the historian.

> ### 🚨 Finding-001 — Historian `db_owner` mutability, no row-level audit (Field 12 fail)
>
> The OT historian operates with `db_owner` role mutability and no row-level audit. UPDATE and DELETE on historian rows leave no forensic trail. Field 12 fails decisively. Phase 2 remediation extends chain coverage via SaaS-edge connector discipline.

### Shared `Plant_Engineer` Workstation

Joaquin walked them to a workstation on the plant floor. The workstation was logged in to a shared `Plant_Engineer` account. He pulled up the login history — the account had been logged in for 18 months without an intervening logout. The workstation drove a single PLC line.

"Eighteen months on the same shared account, no MFA, no individual attribution. The day shift uses it. The night shift uses it. There are six people who have the password."

Diana wrote on Field 3 (authenticated human identity): ✗ Fail. No individual attribution. Six humans, one account, 18 months stuck.

> ### 🚨 Finding-002 — Shared `Plant_Engineer` workstation, no MFA, six humans on one account 18 months (Field 3 fail)
>
> Six individuals share one `Plant_Engineer` workstation account driving a single PLC line. No MFA. No individual attribution for any control action taken from this workstation. Login state has been continuous for 18 months. Field 3 (authenticated human user identity) fails decisively for any control action originating from this workstation.

### TIA Portal Log

The TIA Portal log captured PLC programming changes. Joaquin opened the log file. It was a text file on a network share, editable by anyone with the network share's write permission. He had a list of seven engineering principals who had write access.

"Editable log file. Seven engineers can modify it. We have it on a backup schedule but the backups are also editable."

Luis wrote Field 12: ✗ Fail. Editable log, editable backups.

> ### 🚨 Finding-003 — TIA Portal PLC programming log is plaintext-editable by seven principals (Field 12 fail)

### Plex MES Audit Log

The Plex MES (Manufacturing Execution System) had an audit log feature. Joaquin pulled up the audit log configuration. The retention was set to 0 days — meaning the log was effectively disabled. He checked the change-log of the retention setting. It had been set to 0 six months ago by a senior plant engineer who was no longer with the company.

Chen wrote Field 12: ✗ Fail. Audit log was active but cleared 6 months ago via retention=0 setting change; the change itself has no audit trail of the change.

> ### 🚨 Finding-004 — Plex MES audit log cleared 6 months ago by retention=0 setting change (Field 12 fail; active destruction not silent neglect)
>
> The Plex MES audit log feature exists but was disabled 6 months ago via retention=0 configuration change. The change itself has no audit trail. Six months of plant-execution audit history is unrecoverable. This is active destruction of audit trail, not silent neglect.

### HMI on the Catwalk

Joaquin walked them to the HMI on the catwalk. The HMI was the operator's interface to the plant floor. It logged operator actions to a local file that rotated every 7 days and was not retained centrally.

"This is uninstrumented. We know. Phase 2 chains it via the same OT data-collection pattern as the historian."

Mike wrote Field 12: ✗ Fail. No capture beyond 7-day rotation, no central retention.

Joaquin acknowledged.

> ### ⚠ Partial #1 — HMI uninstrumented, local 7-day rotation only (Field 12 minimal compliance pending Phase 2)

The OT side closed with 4 Findings + 1 Partial against the bank. Joaquin's posture was that this was exactly what Stelvio expected; the budget request needed concrete language and the audit team had provided it.

---

## 🧾 Day 2 Morning — IT Business Systems

The next morning the team walked the IT business systems with Sandeep.

**SAP with `SAP_ALL` closure discipline issues.** Sandeep showed them the IAM dashboard. There were 47 principals with `SAP_ALL` role assignment. Eight of them had been assigned the role temporarily for support incidents that closed more than 90 days ago. The closure workflow had broken — temporary `SAP_ALL` grants were not auto-revoked.

Diana wrote Field 3: ✗ Fail. Over-privileged accounts persist; no IAM-lifecycle integrity.

> ### 🚨 Finding-005 — SAP `SAP_ALL` closure discipline broken; 8 principals over-privileged past intended revocation (Field 3 fail)

**Dynamics field-history selectively enabled.** Elena walked the Dynamics CRM. Field history was enabled on some entities but not others. Customer-contact entities had field history; opportunity-pipeline entities did not. Notes and free-text descriptions had field history disabled for storage-cost reasons.

She wrote Field 1 and Field 12: ✗ Fail for the un-historied fields.

> ### 🚨 Finding-006 — Dynamics field-history selectively disabled on opportunity-pipeline and free-text fields (Field 1 + Field 12 fail for affected scope)

**SharePoint QMS no integrity check.** The Quality Management System lived on SharePoint. Document versioning was on, but there was no integrity check — anyone with edit access could replace a document version with no audit trail of the replacement.

Mike wrote Field 12: ✗ Fail.

> ### 🚨 Finding-007 — SharePoint QMS no integrity check on document version replacement (Field 12 fail)

The IT business side closed with 3 Findings + 4 Partials. Sandeep noted: "These are the systems on the Phase 3 / Phase 4 remediation track. Phase 3 in 18 months chains the most critical IT business surfaces — SAP IAM events, Dynamics customer-contact entity, SharePoint QMS document-version events. Phase 4 is the long tail."

---

## 🏛️ Day 2 Afternoon — Customer-Question Session

The medical-device customer who consumes Stelvio's QC classifications had asked for a session. Their compliance lead joined remotely.

The customer's lead: "I want to walk through how I verify Stelvio's chain entry that fed our April 7 FDA submission. Five steps."

Renata: "Go ahead."

The customer's lead walked through:

1. **Get the published reference verifier.** GitHub Releases. Cosign signature verified. Hash matches the published manifest. (§10.26 distribution.)
2. **Get the published seal record from Stelvio's regulator-facing surface.** No Stelvio credential required. (§5.1 unprivileged-readable seal surface.)
3. **Get the chain entry by `entry_id` from the public chain-record path.** Verified the public-key fingerprint against the published TesseraSeal page. (§4.4.)
4. **Run the verifier in witness mode.** No write access to anything, only verification. Returned PASS in three seconds. (§7 12-step procedure.)
5. **Read the §1.2 epistemic-scope clause.** Confirmed what the chain proves (model said X at time T, untampered) and what it doesn't (clinical/regulatory accuracy of the classification). The customer's expert witness will lay foundation on §1.2 (a) and (b); the customer's defense in any downstream litigation is integrity, not accuracy.

The customer's lead closed: "Five steps. No Stelvio cooperation required. I have the binary, the seal, the entry, the verification, and the epistemic-scope clause. Everything I need to defend the chain entry in front of an FDA reviewer."

Dawn watched.

The Kognitos framework had no row for any of this. Field 12 records that there is an integrity proof. It doesn't address whether a downstream customer can verify the proof without the institution's cooperation, what the published-key trust path looks like, what the witness-mode verifier flag is, or what the epistemic-scope clause covers.

She wrote in her cover-memo notes: *Downstream verification scenario. The customer ran five distinct verification steps using the institution's reference spec. Under our framework, the customer would have no equivalent procedure — they would have to take Stelvio's word that the chain entry was sound. The bank's reference spec gives downstream parties an independent verification path; the framework we operate under does not.*

> ### ◇ Framework-Silent Observation #7 — Downstream-customer verification procedure
>
> The customer's compliance lead ran a five-step independent verification using §10.26, §5.1, §7 witness mode, §4.4, and §1.2. The Kognitos framework has no equivalent procedure. Under Kognitos, a downstream party would have to trust the institution's audit-trail capture without an independent verification path.

---

## 🌆 5:30 PM Day 2 — Auditor Debrief

The team gathered. Renata stepped out.

Dawn wrote on the whiteboard.

```
KOGNITOS 12-FIELD ASSESSMENT — STELVIO INDUSTRIAL (THREE-ZONE)

GREEN ZONE — AI SERVICES (Predictive Maintenance / QC Classification / ITAR NLP):
  Confirmations:                  12 fields × 3 services = 36 cell-confirmations
                                  (aggregated to 7 system-level Confirmations per CMMC posture)
  Partials:                        0
  Findings against bank:           0
  Framework-silent observations:  7    (catwalk demo, verifier procedure-step granularity,
                                        compositional security, deployment-intent, OTel naming,
                                        override provenance, IAM lifecycle)

AMBER ZONE — OT SYSTEMS:
  Findings against bank:           4   (historian mutability;
                                        Plant_Engineer shared workstation;
                                        TIA Portal editable log;
                                        Plex MES audit log cleared)
  Partials against bank:           1   (HMI uninstrumented)
  Confirmations:                   0

RED ZONE — IT BUSINESS SYSTEMS:
  Findings against bank:           3   (SAP_ALL closure discipline;
                                        Dynamics selective field-history;
                                        SharePoint QMS no integrity check)
  Partials against bank:           3   (audit-log retention discrepancies)
  Confirmations:                   0

CROSS-ZONE:
  Framework Gap (re-recorded from Ch02):  1  (coverage-boundary primitive missing)
  Framework Gap (new):                    1  (downstream-customer verification procedure)
  Reconciliation test:
    3/3 QC classification end-to-end (PASS forward and backward)
    Downstream FDA submission cross-referenced; customer verified independently
```

Underneath, she wrote:

```
ENGAGEMENT-TEAM OBSERVATIONS ON FRAMEWORK SELECTION:

1. The Kognitos 12-field framework gave clean language for each per-system finding
   across all three zones. The framework's row-list-as-schema genre is adequate for
   the per-system diagnosis at scale (7 Findings + 4 Partials filed without
   engagement-team improvisation).

2. The three-zone bifurcation requires three complete framework runs stapled with
   prose cross-zone language. The cover memo for this report has three sections
   plus a fourth section explaining what's not in the framework.

3. The downstream-customer verification scenario is the first time the team has
   exercised this property in a real audit. The customer's compliance lead ran a
   five-step independent verification using §10.26, §5.1, §7 witness mode, §4.4,
   §1.2. The Kognitos framework has no equivalent procedure. This is recorded as
   a new Framework Gap.

4. The catwalk demo — four-second verification on 4G with no Stelvio credentials —
   matches the zero-trust verification pattern observed at Northbridge and Mercator.
   Under our framework, all three demonstrations record as single Field 12
   Confirmations. The properties of (a) zero institution-side trust, (b)
   reproducible-build reference-verifier distribution, (c) Cosign-signature trust
   path, (d) sub-five-second verification over consumer-grade network are
   framework-silent in each case.

5. CMMC 2.0 Level 2 + AS 9100D + DFARS 252.204-7012 + ITAR §125 produces a multi-
   framework regulatory stack. Kognitos's framework is regulator-agnostic and does
   not map to any of these directly. The bank's reference spec carries §10.61
   CMMC 2.0 / NIST 800-171 / NIST 800-161 regulator-pack overlay framework which
   provides the cross-walk; we do not.
```

She turned around.

Joaquin walked in.

"Tom, you want to add anything?"

Tom said: "I want to note in the cover memo that the OT findings (4 + 1) are not unusual for a 30-year-old plant floor. The remediation timeline (Phase 2 in 12 months) is aggressive but realistic. The budget number Renata had pre-committed to the board — $4.2 million over 18 months for Phases 2 and 3 — is in the right range based on the surface area we walked."

Renata came back into the room with coffee.

"What did you find?"

Dawn pointed at the whiteboard.

"Seven Findings against the bank across the unchained zones. Four Partials. The chained AI services pass cleanly for CMMC Level 2 in-scope subset. The downstream FDA-customer verification works without your cooperation. The catwalk demo over 4G is the property the framework can't articulate but your CFO will recognize."

Renata read the board.

"That is exactly the report I asked for. Joaquin, the Phase 2 budget request will use Findings 001 through 004 verbatim. The Phase 3 / Phase 4 plan uses Findings 005 through 007."

Joaquin nodded.

Renata picked up the draft report.

She paused at the door.

"The customer-question session was the part I was nervous about. The medical-device customer is the largest single FDA-pathway customer we have. If their compliance lead couldn't verify independently, our entire chain-of-custody investment would be discounted. The fact that they can — and that they did, this afternoon, in front of you — is the part that makes the next ten years of customer relationships work."

She paused.

"The framework you brought records that as one Field 12 Confirmation. We carry it as the load-bearing operational property. Both readings are correct. The framework's reading is just shallower than the property."

Dawn nodded.

"That's the most honest summary of the framework's relationship to your operations I've heard."

Renata almost smiled. "We've been thinking about it for 14 months."

She walked out.

---

## ❌ What They Expected vs ✅ What They Found

**❌ What They Expected:**

- The three-zone bifurcation would produce a complicated report.
- Kognitos's framework would have some language for downstream-customer verification.
- OT findings would be hard to articulate under a framework designed for SaaS / finance / healthcare.

**✅ What They Found:**

- AI side passed cleanly across three services and seven Confirmations.
- OT side produced four Findings + one Partial, all named cleanly under Kognitos's per-system fields.
- IT business side produced three Findings + three Partials, similar pattern.
- Downstream-customer verification was a property the framework had no row for; the bank's reference spec provides the procedure.
- The four-second catwalk demo over 4G crystallized the zero-trust verification property; framework cannot articulate it.

**⚠ What Their Framework Could Not Record:**

- Downstream-customer five-step verification procedure (new Gap; will recur).
- Verifier procedure-step granularity (which §7 step caught a specific tamper — affects IR remediation).
- Cross-zone coverage discipline (recurring from Chapter 02).
- §10.61 regulator-pack overlay framework (CMMC / NIST 800-171 / NIST 800-161 cross-walk).
- Three-layer compositional security on chained services (recurring from Chapters 01-02).

---

## 🧾 Final Assessment Theme

> "The organization operates a three-zone partial chain-of-custody deployment with strong integrity on three chained AI services and material integrity gaps across both unchained zones (OT and IT business). The Kognitos 12-field framework records the green zone as seven Confirmations, the amber zone as four Findings + one Partial, and the red zone as three Findings + three Partials, with two Framework Gaps on cross-zone narrative and downstream-customer verification procedure. The institution operates the downstream-customer verification capability under its reference spec; the framework cannot articulate the capability. Phase 2 budget request ($4.2M over 18 months) is supported by the Findings."

---

## Research takeaway

Chapter 03 surfaces a new framework Gap that recurs at any deployment with a downstream-customer verification scenario: the customer's five-step independent verification procedure has no Kognitos equivalent. Under the bank's reference spec, downstream parties verify independently; under Kognitos, they trust the institution's word.

The running tally of speculation anchors:
- Chapter 01: 14 invented anchors
- Chapter 02: 12 new anchors
- Chapter 03: 7 new anchors (downstream verification procedure; verifier procedure-step granularity; OT-specific Findings against bank under Field 12 spirit reading; CMMC / NIST regulator-pack overlay; three-zone bifurcation extension of Ch02's coverage-boundary Gap; catwalk demo zero-trust property; ITAR §125 / DFARS 252.204-7012 / AS 9100D regulator-agnostic gap)

Running total across three chapters: **33 speculation anchors invented under Kognitos**, against approximately zero under the bank's reference spec.

The pattern is consistent: the bank's reference spec is regulator-anchored, scope-aware, and procedure-aware. The Kognitos framework is regulator-agnostic, scope-agnostic, and procedure-agnostic. Each property the bank operates that one of those three dimensions touches is invisible to the framework, and each invisibility produces an auditor speculation anchor.
