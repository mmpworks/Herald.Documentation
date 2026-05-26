# Comparative Analysis — Chapter 03 (Stelvio Industrial)

*Side-by-side analysis of how the Kognitos 12-field framework and the TesseraSeal / FFIEC chain-of-custody v1.0b spec handle each audit moment in Chapter 03. Honest assessment of how much an auditor has to speculate under a **three-zone partial deployment** with OT-specific failure modes, downstream-customer verification, and a defense-industry regulator stack (CMMC 2.0 / NIST 800-171 / DFARS 252.204-7012 / ITAR §125 / AS 9100D).*

---

## How this chapter differs from Chapters 01-02

| Chapter | Deployment | Findings | Distinctive lens-stretching property |
|---|---|---|---|
| Ch01 (Northbridge) | Full enterprise | 0 against bank | Bank exceeds framework everywhere; speculation gap dominates |
| Ch02 (Mercator) | Two zones (AI / legacy) | 4 + 2 against bank | Bifurcation; framework lacks coverage-boundary primitive |
| Ch03 (Stelvio) | **Three zones (AI / OT / IT business)** | **7 + 4 against bank** | **OT-specific failure modes; downstream-customer verification; regulator-pack overlay** |

Chapter 03 stretches the framework in three new directions simultaneously:
1. **Three-zone bifurcation** — exercises Chapter 02's coverage-boundary Gap at higher complexity.
2. **OT-specific scenarios** (PLCs, HMIs, historians, shared workstations) — Kognitos's 12 fields were authored for SaaS / finance / healthcare and do not naturally cover OT failure modes.
3. **Downstream-customer verification** — the medical-device customer's five-step independent verification path has no Kognitos equivalent.

### Recurring from Chapters 01-02

These play out the same way under Kognitos. Severities unchanged.

| Recurring point | Ch01 ref | Ch02 ref | Ch03 instance |
|---|---|---|---|
| Compositional security | Ch01 §4 | Ch02 (AI side) | All three chained services |
| Coverage-boundary integrity propagation | — | Ch02 §A | Three-zone extension |
| Deployment-intent capture | — | Ch02 §D | Predictive-maintenance retraining Q4 2025 |
| OpenTelemetry GenAI naming | — | Ch02 §E | All three chained services |
| Reference-verifier distribution | Ch01 §12 | Ch02 (FDA reviewer) | **Customer-driven verification (new instance)** |
| Training-data retention / pre-launch backfill | Ch01 §10 | Ch02 §L | 540-day floor operational |
| Cross-vendor model-handover schema | — | Ch02 §K | §10.21 operational at Q4 2025 retraining |

---

## New comparison points specific to Chapter 03

Eight distinct new comparison points emerged from this engagement.

---

### A. Downstream-customer verification procedure — five-step independent path

**The audit-room question.** *"The medical-device customer's compliance lead ran a five-step independent verification of three chain entries that fed their FDA submission. How does the framework articulate this capability?"*

**TesseraSeal.** Five distinct sections cooperate to make downstream verification possible without institution-side cooperation:
- **§10.26** — reference verifier distribution (Cosign-signed releases, reproducible builds, SBOM, per-platform binaries)
- **§5.1** — unprivileged-readable seal surface (institution publishes seal records and public-key fingerprint without requiring credentials)
- **§7 witness mode** — verifier flag for read-only verification with no write access
- **§4.4** — chain envelope including the publicly-disclosable attributes
- **§1.2** — epistemic-scope clause that grounds what the chain proves vs. what it does not

The customer's compliance lead at Stelvio used all five sections to verify three QC chain entries that fed their April 7 FDA submission. No Stelvio credential was used at any layer.

**Kognitos.** No equivalent procedure. Field 12 records that there is an integrity proof. The framework does not address whether downstream parties can verify the proof, what trust path they use to obtain the verifier, how they obtain the published key, how they scope verification to witness-mode, or what epistemic-scope clause governs the proof's evidentiary value.

**Speculation gap.** Under Kognitos, a downstream customer asking "how do I verify your chain entries that feed my regulatory submission?" has no framework-supplied answer. The institution must either:
- Provide the customer with institution-side tooling (circular trust — the customer trusts the tool the institution wrote)
- Refuse to provide tooling (the customer must trust the institution's word)
- Borrow the five-section pattern from another framework (TesseraSeal, AICPA SOC-style assertions, an industry-specific standard)

Stelvio's customer borrowed from the bank's reference spec. The Kognitos framework provided no anchor.

**Structural reason for the gap.** Kognitos's framework defines what an audit-trail row should contain. The downstream-verification procedure is a multi-section discipline that operates outside any single row — it requires a verifier-distribution channel, a seal-publication discipline, a witness-mode flag in the verifier, and an epistemic-scope clause. These are five distinct framework-genre artifacts; Kognitos's row-list-as-schema cannot articulate any of them.

**Honest assessment.** For institutions where downstream parties consume the audit trail (regulatory submissions, customer due-diligence, court-of-law evidence), the downstream-verification procedure is the most operationally consequential property of the audit trail. The chain entry is only as useful as the procedure that verifies it. Stelvio's medical-device customer can defend the QC classification in an FDA inquiry; an institution without an equivalent procedure cannot. **Severity: highest for downstream-consumed audit trails; not applicable for purely internal audit.** New highest-severity gap, joining compositional security (Ch01 §4) at the top of the list.

---

### B. Verifier procedure-step granularity

**The audit-room question.** *"The verifier caught the direct UPDATE tamper at §7 step 9 (single-entry recomputation) and also at §7 step 10 (Merkle root mismatch). Why does the framework care which step caught it?"*

**TesseraSeal.** §7's 12-step verification procedure assigns specific named steps to specific verification properties. Step 0 is JCS pre-flight self-test. Step 6 is structural-walk (genesis-form anti-spoof). Step 8 is fingerprint check before MAC compute. Step 9 is single-entry recomputation. Step 10 is Merkle root recomputation. Step 11 is signature dispatch on `sign_payload_version`. Step 12 is the closing PASS/FAIL determination. The institution's incident-response runbook keys remediation off the step number — different steps imply different attack vectors and different remediation paths.

**Kognitos.** No language for verifier procedure-step granularity. An implementation returning only "PASS/FAIL" satisfies Field 12 identically to one returning "FAIL at step 9 — single-entry tamper" or "FAIL at step 10 — Merkle root mismatch."

**Speculation gap.** Under Kognitos, the verifier's diagnostic granularity is not specified. Institutions building IR runbooks against the framework have no anchor for "what does the verifier tell me when it fails?" The runbook either invents step-numbering language or operates without it.

**Structural reason for the gap.** Procedural granularity is a verifier-implementation property. Kognitos defines the data, not the verifier. The 12-step procedure is a spec-genre artifact; the row-list-as-schema framework does not address verifier implementation.

**Honest assessment.** For institutions operating IR programs against the audit-trail integrity proof, procedure-step granularity is operationally significant. A verifier that returns only PASS/FAIL forces the IR team to investigate every dimension of every failure; a verifier that returns step-numbered failures lets the IR team scope investigation to the specific attack vector. The Stelvio tamper test showed both steps catching the same attack; the institution's IR runbook keys both detections to specific remediation paths. **Severity: medium-high** for institutions running IR programs against the integrity proof; lower for pure compliance posture.

---

### C. OT-specific Field 12 failure modes — `db_owner` mutability, retention=0 destruction, shared workstation accounts

**The audit-room question.** *"The historian has `db_owner` mutability with no row-level audit. The Plex audit log was disabled by retention=0 setting six months ago. The PLC workstation has six humans on one shared account for 18 months. Field 12 fails for the historian and the Plex log; Field 3 fails for the workstation. The framework gives me language for each — but how do I express the OT-specific severity?"*

**TesseraSeal.** §10.3 (append-only at storage tier and database role layers) names the database-role discipline that excludes `db_owner` mutability. §6 (append-only storage discipline) covers retention-policy changes as chain events. §1.4 + §10.5 cover IAM individual attribution at the operational layer. The bank's reference spec also carries §10.61 regulator-pack overlay for CMMC 2.0 / NIST 800-171 / NIST 800-161, which provides the cross-walk to OT-specific control families.

**Kognitos.** Field 12 and Field 3 give the failure-naming. The framework does not have OT-specific elaboration — Field 12 treats "tamper-evident integrity proof" as a single property regardless of whether the substrate is a transactional database, a historian, an HMI log file, or a PLC workstation.

**Speculation gap.** Under Kognitos, the four OT findings (historian mutability, shared workstation, editable TIA Portal log, Plex retention=0 destruction) record as four field failures. The OT-specific remediation patterns (historian extraction via §4.4.6-style connector, IAM lifecycle via chain-driven discipline, log-file extraction via SaaS-edge attribute family) are framework-silent. The institution's Phase 2 remediation roadmap must author the OT-specific patterns independently.

**Structural reason for the gap.** Kognitos's framework was authored against SaaS / finance / healthcare. OT and industrial scenarios were not in scope. The 12-field schema does not include OT-specific patterns because the cross-regulator synthesis didn't reach into IATF 16949, AS 9100D, or CMMC's OT-side controls. Extending Kognitos to OT would require a different schema or an overlay; neither exists today.

**Honest assessment.** For manufacturing, energy, defense, and infrastructure institutions, OT-side audit trails are the largest single category of audit-trail material. Kognitos's framework gives auditors clean failure-naming language for OT failures but no OT-specific remediation patterns. The Phase 2 remediation Stelvio funded ($4.2M over 18 months) was scoped under the bank's reference spec's §4.4.6 SaaS-edge connector pattern applied to the historian. Under Kognitos, the institution would have authored the remediation pattern from scratch. **Severity: high** for OT-heavy institutions; not applicable for pure SaaS / cloud-native deployments.

---

### D. Regulator-pack overlay framework — CMMC 2.0 / NIST 800-171 / DFARS 252.204-7012 / ITAR §125

**The audit-room question.** *"The engagement is CMMC 2.0 Level 2 readiness with AS 9100D overlay, DFARS 252.204-7012 in scope, ITAR §125 export-control records in scope. How does the framework map to each regulator?"*

**TesseraSeal.** §10.61 names the regulator-pack overlay framework: a documented cross-walk between the spec's controls and each regulator's control families. CMMC 2.0 Level 2 controls (110 from NIST 800-171), AS 9100D quality controls, DFARS 252.204-7012 covered-defense-information handling, ITAR §125 export-control discipline — each maps to specific spec sections via the §10.61 cross-walk. The institution can demonstrate compliance against each regulator using the same audit-trail substrate.

**Kognitos.** No regulator-pack overlay. The framework is regulator-agnostic by design (per its marketing posture as a "cross-regulator synthesis"). It does not map to CMMC, DFARS, ITAR, or AS 9100D directly. Each regulator must be addressed independently with the framework's 12 fields as a generic baseline.

**Speculation gap.** Under Kognitos, an auditor at a CMMC engagement has to invent the cross-walk between the 12 fields and CMMC's 110 controls (or borrow from another framework). The Stelvio engagement required CMMC + AS 9100D + DFARS + ITAR cross-walk; the team used four separate regulator references plus the 12-field framework. The bank's reference spec carries §10.61 to bundle the cross-walk; Kognitos does not.

**Structural reason for the gap.** Kognitos's framework genre is cross-regulator marketing synthesis — it deliberately doesn't commit to a specific regulator-pack overlay because that would limit its broad applicability. The trade-off is that institutions operating in specific regulatory contexts (defense, healthcare, aerospace) have to invent the cross-walk themselves.

**Honest assessment.** For institutions operating under specific regulatory frameworks (CMMC, FFIEC IT, FDA SaMD, EU AI Act high-risk, ISO 27001, HITRUST), the cross-walk is operationally significant — the audit deliverable must cite the regulator's control families, not the audit framework's fields. Stelvio's CMMC report cited CMMC controls; the engagement team mapped Kognitos's 12 fields to CMMC controls in the cover memo. **Severity: medium-high** for regulator-specific engagements; not applicable for compliance-agnostic posture.

---

### E. Catwalk demo / zero-trust verification under field conditions

**The audit-room question.** *"Renata ran the verifier in four seconds on a 4G hotspot, no Stelvio credentials. The CFO will watch this video for the budget brief. How does the framework articulate the capability the video demonstrates?"*

**TesseraSeal.** This is the operational instantiation of §10.26 (distribution discipline) + §5.1 (transport encryption + unprivileged-readable seal surface) + §1.4 (compositional security with cryptographic independence from institution infrastructure). The catwalk demo is what the spec calls "out-of-band verification" — the verifier runs without any institution-side dependency at any layer of the stack.

**Kognitos.** Field 12 records that there is an integrity proof. The framework does not address the operational properties that make the proof useful under field conditions: reproducible-build verifier distribution, sub-five-second verification time, consumer-grade-network feasibility, zero institution-side trust dependency.

**Speculation gap.** Under Kognitos, the catwalk demo records as one Field 12 Confirmation. The properties that make the video compelling for a CFO briefing — speed, no credentials, no institution infrastructure, reproducible verifier — are framework-silent.

**Structural reason for the gap.** Field-condition verification is a deployment-architecture property. Kognitos's framework is per-row; deployment-architecture is per-system. The genre mismatch recurs.

**Honest assessment.** For institutions where the audit trail must be demonstrable to non-specialist stakeholders (CFOs, board members, regulators in walk-through inspections), the catwalk demo capability is operationally significant. Northbridge's Greg-on-call demo, Mercator's FDA-reviewer independent verification, and Stelvio's catwalk-over-4G are three instances of the same property. **Severity: medium-high** for institutions facing stakeholder demonstration scenarios; recurring across multiple chapters.

---

### F. Three-zone coverage-map extension

**The audit-room question.** *"Chapter 02 had two zones. This engagement has three. The framework's coverage-boundary Gap recurs; does it recur identically or does the three-zone case stretch the gap further?"*

**TesseraSeal.** §10.19 chain-coverage map handles N-zone deployments natively. The map names every system, every rollout posture, every evidentiary substitute. Stelvio's map has three columns; the framework supports any N.

**Kognitos.** No coverage-map primitive (Chapter 02 §A established this). The three-zone case requires three complete framework runs stapled with prose cross-zone language. The cover memo grows from Chapter 02's three sections (AI side, legacy side, cross-zone) to four sections (AI side, OT zone, IT business zone, cross-zone).

**Speculation gap.** Under Kognitos, the three-zone case extends the Chapter 02 coverage-boundary Gap rather than producing a fundamentally new one. The framework's silence is the same; the auditor's prose burden is larger.

**Honest assessment.** Same severity as Chapter 02 §A — high, for any partial-deployment institution. The three-zone case is concrete evidence that the gap scales with deployment complexity. **Severity: high.** Recurring.

---

### G. ITAR §125 / DFARS 252.204-7012 export-control records

**The audit-room question.** *"The ITAR screening NLP is one of the three chained AI services. Each scan is a chain entry with the document hash, model version, classifier output, and human reviewer disposition. How does the framework address ITAR §125 export-control records specifically?"*

**TesseraSeal.** ITAR §125 export-control records are addressed via §10.61 regulator-pack overlay + §10.19 chain-coverage map + §10.22 redaction discipline (for export-controlled content). The spec doesn't have ITAR-specific sections per se, but the regulator-pack overlay binds the spec's controls to ITAR's requirements.

**Kognitos.** No ITAR-specific language. The framework's regulator-agnostic posture means ITAR records are treated identically to non-export-controlled records. An institution running ITAR-controlled AI must invent the additional discipline (CUI handling, document classification, foreign-national access restrictions).

**Speculation gap.** Under Kognitos, the auditor at an ITAR-controlled deployment has no framework anchor for ITAR-specific record-keeping requirements. The Stelvio engagement required the team to reference ITAR §125 directly in the cover memo.

**Honest assessment.** For defense, aerospace, and dual-use technology institutions, ITAR is the governing record-keeping framework for export-controlled content. Kognitos's silence here is structural (regulator-agnostic genre); the institution must address ITAR independently. **Severity: medium-high** for defense / aerospace; not applicable elsewhere.

---

### H. Cross-vendor model-handover schema operational (recurring from Ch02 §K but newly instantiated)

**The audit-room question.** *"The Q4 2025 predictive-maintenance retraining was a cross-vendor handover under §10.21 — internal team-to-team handover but the schema was applied as if it were external. What did the schema produce?"*

**TesseraSeal.** §10.21 cross-vendor model-handover schema names the attribute family for any model handover, internal or external: model card hash, training-data summary hash, evaluation outputs hash, handover-event chain entry. Stelvio applied the schema at the Q4 2025 internal handover from the platform team to the operations team. The handover produced four sealed chain entries with the §10.21 attribute family.

**Kognitos.** No field for model-handover discipline (Chapter 02 §K).

**Speculation gap.** Same as Chapter 02 §K. The framework cannot articulate the handover discipline. The institution authored it under §10.21.

**Honest assessment.** This is the first chapter where §10.21 is operational rather than forward-looking. Stelvio's Q4 2025 retraining is a concrete instance — the chain entries are in the audit-trail, the verifier confirmed them, and the regulator-pack cross-walk binds the handover to AS 9100D quality-management control families. Under Kognitos, the institution would have applied an internally-authored discipline; under the reference spec, the discipline is normative. **Severity: medium** — recurring but newly operational.

---

## Summary table — Chapter 03 new comparison points

| # | Area | TesseraSeal anchor | Kognitos anchor | Speculation gap | Material impact |
|---|---|---|---|---|---|
| A | Downstream-customer verification procedure | §10.26 + §5.1 + §7 witness mode + §4.4 + §1.2 | No equivalent | **Highest** | Customer cannot verify independently |
| B | Verifier procedure-step granularity | §7 12-step procedure | No language | Medium-High | IR runbook anchor missing |
| C | OT-specific Field 12 failure modes | §10.3 + §6 + §10.61 | Field 12 generic | High | OT remediation patterns framework-silent |
| D | Regulator-pack overlay (CMMC/NIST/DFARS/ITAR/AS9100D) | §10.61 cross-walk | Regulator-agnostic | Medium-High | Each regulator addressed independently |
| E | Catwalk demo / field-condition verification | §10.26 + §5.1 + §1.4 | Field 12 generic | Medium-High | Stakeholder-demo capability invisible |
| F | Three-zone coverage-map extension | §10.19 N-zone support | No primitive | High | Recurring from Ch02 §A |
| G | ITAR §125 / DFARS 252.204-7012 records | §10.61 + §10.22 + §10.19 | Regulator-agnostic | Medium-High (defense) | Export-control records have no framework |
| H | Cross-vendor model-handover (newly operational) | §10.21 | No field | Medium | Recurring from Ch02 §K |

**Plus recurring from Chapters 01-02:** 6 comparison points unchanged (compositional security, deployment-intent, OTel naming, reference-verifier distribution, training-data retention, coverage-boundary primitive).

**Total comparison points exercised in Chapter 03:** 22 (8 new + 6 from Ch01 + 8 from Ch02).

---

## Honest assessment — three chapters in, the pattern is consolidating

### What the framework handled adequately

The Kognitos 12-field framework gave the Chapter 03 audit team clean per-system failure-naming for **seven Findings + four Partials** across the OT and IT business zones. The framework's row-list-as-schema genre **is** adequate for per-system diagnosis at scale. The seven Findings (historian mutability, shared workstation, editable TIA Portal log, Plex retention=0 destruction, SAP_ALL closure, Dynamics selective field-history, SharePoint QMS no integrity check) all map to specific Kognitos fields. The remediation roadmap (Phase 2 / Phase 3 / Phase 4) is grounded in those findings.

### What the framework could not handle

Three high-severity blind spots emerged or were reinforced:

1. **Downstream-customer verification procedure** (new; highest severity). The medical-device customer's five-step independent verification has no Kognitos equivalent. Under the reference spec, downstream parties verify without institution cooperation; under Kognitos, they trust the institution.

2. **OT-specific failure-mode patterns** (new; high severity). Kognitos was authored against SaaS / finance / healthcare. OT scenarios (historians, PLCs, HMIs, shared workstations) produce Field 12 / Field 3 failures the framework can name but not contextualize.

3. **Regulator-pack overlay** (new; medium-high severity). CMMC / DFARS / ITAR / AS 9100D produce a multi-framework regulatory stack that the framework's regulator-agnostic posture cannot map.

The three-zone coverage-boundary gap (Chapter 02 §A) recurs at higher complexity. The catwalk demo / zero-trust verification (recurring from Chapters 01-02) is the third demonstration of the same Kognitos blind spot.

### Running speculation tally

- **Chapter 01:** 14 invented anchors
- **Chapter 02:** 12 new anchors (26 total)
- **Chapter 03:** 8 new anchors (34 total)

Three chapters in, the pattern is clear: each engagement produces roughly 10-15 new speculation anchors under Kognitos, plus the recurring set from prior chapters. By Chapter 22, the cumulative anchor count is on track for **150-250 invented anchors across the program** — measured against approximately zero under the bank's reference spec.

The convergence pattern continues: institution-side culture is the load-bearing variable that prevents the framework's silences from producing materially weaker operational outcomes. Stelvio's Renata had pre-committed the Phase 2 budget; the audit produced the Findings that justified it. Under either framework, the operational outcome converges because Renata's culture is doing the work. At an institution without that culture, the convergence breaks.

### What this comparison adds to the program-level signal

Chapter 03 demonstrates that the framework's blind spots scale with deployment complexity (three zones is worse than two) and surface specifically in regulatory contexts the framework's genre cannot reach (OT, defense, downstream-customer verification). The reference spec's coverage, regulator-pack overlay, and downstream-verification procedure together address scenarios that a 12-row cross-regulator-synthesis framework structurally cannot.

The honest read: Kognitos is a competent baseline for AI audit-trail discussions. It is not adequate as the sole framework for institutions operating in regulator-anchored, downstream-consumed, or N-zone-bifurcated contexts. Three chapters of evidence point in the same direction.
