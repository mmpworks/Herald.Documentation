# 06 — Pacific Crescent Power & Gas (Kognitos-lens)

*A utility audit where a live methane alert fires during the engagement and the framework's silence on public-safety epistemic scope produces the chapter's central inarticulability finding*

**Engagement:** NERC CIP audit-readiness assessment with PHMSA pipeline-integrity overlay; three-state PUC interest (WUTC, OPUC, CA-CPUC)
**Client:** Pacific Crescent Power & Gas — multi-state utility, post-incident audit after a near-miss methane event
**Status:** Chain instrumented on pipeline-leak-detection AI service only (9 months live, 1.6M inferences); legacy stack everywhere else (PI historian, GE iFIX SCADA, Itron AMI, OMS, CIS, Salesforce)
**Audit team lead:** Dawn
**Client liaison:** Soren Kovach, Chief Information Security Officer; Aiyana Whitehorse, OT Security Lead

**Audit team's framework:** Kognitos's 12-field schema. The team is now five engagements in. They will encounter two new lens-stretching scenarios in this chapter: (1) **a live alert during the audit** — the AI fires a medium-confidence methane reading on a real pipeline segment, the verifier runs in 4 seconds, a small leak is confirmed 22 minutes later; and (2) **public-safety stakes that change the consequence of the §1.2 epistemic-scope distinction** — at Helmstad it was a clinical-quality CAPA; at Pacific Crescent it's potentially a neighborhood-evacuation question.

---

## 🌅 8:30 AM — Kickoff (Post-Incident Context)

Soren walked in with a printed §10.19 coverage map. Four categories — chain-instrumented (pipeline-leak-detection AI), not-yet-instrumented (PI historian, iFIX SCADA, OMS), third-party-with-inspection (Schneider Electric model lineage), external-evidentiary (paper OMS work-orders, dispatcher voice logs).

He set it on the table.

"Three months ago we had a near-miss methane event. Crew dispatched on a high-confidence alert; small leak; no injuries; no media. The CISO board asked the question every CISO board asks after a near-miss: 'show us that the AI was right.' We've been operating the leak-detection chain for 9 months. The board wanted an audit. NERC CIP-002-014 are on the table. PHMSA pipeline-integrity is on the table. Three state PUCs want copies. The insurance carrier wants the dismissed-alarm evidence package. The General Counsel wants the Daubert grounding for any litigation that follows."

Dawn looked at the map.

"Under the framework we operate — Kognitos's 12 fields — we don't carry an epistemic-scope clause. At Helmstad two weeks ago, we had a chain-integrity-clean / source-data-wrong finding (the April 15 patient) that fell outside the framework. The reference spec has §1.2 to articulate the distinction. We borrowed the language. At a utility with public-safety stakes, the §1.2 distinction is going to matter more than it did at a clinical trial."

Soren nodded slowly.

"The General Counsel asked specifically for a one-page Daubert grounding. He wants four factors — testability, peer review, known error rate, general acceptance. Our reference spec §1.1 maps each factor to specific procedural sections. Your framework, I'm guessing, does not."

"It does not. The 12 fields cover data capture; they do not articulate evidentiary foundation. We can write the Daubert one-pager in cover-memo prose citing the reference spec's §1.1, the same way we cited §1.2 (c) at Helmstad."

"That works. Aiyana will walk you through the OT side after lunch. The live-alert system is up — if the AI fires today, you'll see it. We do not stop the audit for an alert."

Dawn wrote that down. *Live-alert capability during audit. Field 12 demonstration may be operational rather than synthetic. Note for the chapter.*

---

## 🧬 9:30 AM — Leak-Detection AI (Field Walk)

The pipeline-leak-detection AI ran a transformer-based time-series model fed by 4,700 pressure / temperature / flow sensors across 12 transmission lines. Each inference was a chain entry with sensor stream hashes, model version, predicted leak probability, predicted leak location bands, and dispatcher disposition.

Mike worked his template against a sample entry from three weeks earlier.

```json
{
  "entry_id": "leak-2026-04-22-pcp-1238742",
  "tenant": "pacific-crescent-gas",
  "service": "pipeline-leak-detection",
  "seq": 1238742,
  "ts": "2026-04-22T14:38:11.412Z",
  "model_id": "pcp/leak-detection-v3.1",
  "model_version": "v3.1.4-schneider-2026-q1",
  "gen_ai.request.model": "pcp/leak-detection-v3.1",
  "gen_ai.response.model": "pcp/leak-detection-v3.1",
  "prompt": {
    "sensor_window_hashes": ["sha256:..."],
    "sensor_count": 47,
    "time_window_seconds": 3600
  },
  "response": {
    "leak_probability": 0.31,
    "predicted_location_band_meters": [4720, 4780],
    "anomaly_signature": "creep-pattern-class-3"
  },
  "audit.deployment.intent": "production",
  "audit.deployment.policy_version": "pcp-mrm-2026q2",
  "dispatcher_disposition": {
    "dispatcher_id": "pcp-disp-0042",
    "decision": "monitor-no-dispatch",
    "ts": "2026-04-22T14:39:08.114Z"
  },
  "payload_hash": "...",
  "hmac": "...",
  "merkle_path": [...],
  "daily_seal_ref": "2026-04-22-d-seal-pcp-gas"
}
```

All 12 Kognitos fields satisfied. Same depth as previous chapters — gen_ai naming, deployment-intent, MAC + Merkle + Ed25519.

The dispatcher disposition was the new attribute Mike paused on. The model predicted a 0.31 probability (medium-low); the dispatcher decided `monitor-no-dispatch`. The decision was its own attribute on the chain entry with the dispatcher's ID. Mike noted: ◇ Field 11 (human review) is satisfied with depth — the dispatcher's disposition is bound to the same chain entry as the model's output, so the question "did the human review the model's prediction" has a per-entry answer rather than a separate review log.

> ### ✓ Confirmation #1 — All 12 fields satisfied on leak-detection inference (Field 11 with chain-bound dispatcher disposition)

---

## 🚨 10:47 AM — The Live Alert

Mike was running the verifier against a fourth random entry when the dispatch center radio across the hall went off.

The team heard it. Soren walked into the room.

"Medium-confidence alert on Transmission Line 7. Sensor cluster 4400-4500 meter range. Probability 0.62. Schneider model. We just got it on the dispatch screen. Crew is en route."

Dawn looked at the team.

"Mike, run the verifier on the alert entry. Now."

Mike pulled the entry ID off the dispatch screen.

```
$ herald-verify --tenant=pacific-crescent-gas \
                --service=pipeline-leak-detection \
                --date=2026-05-06 \
                --entry-id=leak-2026-05-06-pcp-1409331 \
                --strict
```

Four seconds.

```
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified
        against public key pcp-gas-prod-2026-q2
Elapsed: 4.1s
```

The dispatch center radio kept talking. Crew was approaching the segment. ETA 18 minutes.

Mike asked for the entry record. He read it out loud.

"Model `pcp/leak-detection-v3.1`. Version `v3.1.4-schneider-2026-q1`. Sensor window — forty-seven sensors, 3,600-second window. Anomaly signature `creep-pattern-class-3`. Leak probability 0.62. Predicted location band 4,420 to 4,490 meters on TL-7. Dispatcher disposition pending."

Soren: "Crew is going to verify on the ground. We'll know in twenty minutes."

The dispatch radio reported in twenty-two minutes. Small methane leak at meter 4,461 on TL-7. Confirmed. Crew isolating the segment.

The dispatcher disposition entry landed in the chain about 30 seconds after that — `dispatch-confirmed-leak-found` with the dispatcher_id and timestamp. It chain-linked back to the original alert entry via `parent_run_id`.

Dawn watched it land.

She wrote in her template: *Live alert during audit. Verifier ran in 4 seconds while the dispatcher was reading the alert. Crew confirmed the leak 22 minutes later. The chain captured the model's prediction at 10:47:11.234 and the dispatcher's confirmation at 11:09:43.108. The 22-minute interval is the operational reality of the leak-detection-to-confirmation workflow. The framework records this as one Field 12 Confirmation. The operational property — verification works during a real alert at speed-of-dispatch — is invisible.*

> ### ✓ Confirmation #2 — Live methane alert verified mid-engagement; verification in 4 seconds, leak confirmed in 22 minutes (Field 12, with operational depth not asked)
>
> The pipeline-leak-detection AI fired a medium-confidence alert on TL-7 sensor cluster 4400-4500m range during the audit. The verifier ran in 4.1 seconds. Crew confirmed a small methane leak at 4,461 meters 22 minutes later. The dispatcher confirmation entry was chain-bound to the original alert entry. **This became the executive-briefing artifact for the CISO board.** Under Kognitos, this records as one Field 12 Confirmation. The operational properties — verification at speed-of-dispatch, no engagement disruption from the live alert, chain-bound dispatcher-confirmation linkage — are framework-silent.

> ### ◇ Framework-Silent Observation #1 — Verification at speed-of-dispatch under live operational load
>
> The bank's reference spec implicitly supports this via §7 + §10.26 + §1.4 — verifier procedure is deterministic, distribution is independent of operational systems, and the cryptographic substrate is independent of dispatch. The Kognitos framework has no field for operational-load resilience of the verification path.

---

## 🛡️ 11:30 AM — The §1.2 Public-Safety Question

The live alert created an opening for the question the General Counsel had asked for. Dawn turned to Soren.

"Walk me through the §1.2 distinction for this morning's alert. The model said 0.62 leak probability on TL-7 at 4,461 meters. The crew confirmed a leak. If the leak had been at 4,520 instead — outside the model's predicted band — and we'd missed it, what does the chain prove?"

Soren nodded. This was the question he had prepared for.

"§1.2 (a) — the chain proves what the model said. At 10:47:11.234, the model said leak probability 0.62 with a predicted band of 4,420 to 4,490 meters, based on a 3,600-second window of 47 sensors. That's mathematically defensible. We can produce a witness for it."

"§1.2 (b)?"

"The record was not tampered after capture. HMAC plus Merkle plus Ed25519 plus the §10.5 HSM custody plus the §1.4 compositional security across three independent layers. Defensible."

"§1.2 (c)?"

"The chain does not prove the sensors were honest. The sensors are read off the iFIX SCADA layer. iFIX has UPDATE-by-DBA permission and a 60-day rolling audit window per §10.13 evidentiary-retention floor concerns. **If a sensor lied to the model, the model's prediction is wrong but the chain is intact.** That's the line between chain-integrity and sensor-integrity. The chain captures what the model saw and said; it does not authenticate the sensor that produced what the model saw."

Dawn wrote that down. She underlined `the chain captures what the model saw and said; it does not authenticate the sensor`.

"§1.2 (d)?"

"The chain does not prove the model's output was clinically — operationally — correct. The model said 0.62. The crew confirmed a leak. But if the model had said 0.62 and the crew had not found a leak (the dismissed-alarm scenario), the chain would not tell you whether the model was right. The model's accuracy is a separate audit."

"§1.2 (e)?"

"The chain does not prove the downstream action was the right action. If the dispatcher dismisses the alert and a leak follows, the chain proves the dispatcher dismissed; it does not prove the dismissal was justified. The dispatcher's reasoning is captured in `dispatcher_disposition` — but the chain doesn't litigate the reasoning."

Dawn closed her notes.

She had what she needed for the General Counsel one-pager. Five subclauses, five witnesses for the litigation file. Under Kognitos, none of these had a row. Under the reference spec, every distinction was articulated in §1.2.

She wrote: *Under our framework, the §1.2 (a)/(b)/(c)/(d)/(e) distinctions are inarticulable. Every Kognitos field satisfied; the framework cannot supply the General Counsel's one-pager. The litigation-support file will need to borrow §1.2 from the reference spec, citing it verbatim. This is the second chapter where the chain-integrity / source-data-versus-model-versus-action distinction matters, with public-safety stakes that make the §1.2 (c) line load-bearing. **Framework Inarticulability #2 — public-safety variant.***

> ### ⚠ Framework Inarticulability #2 — §1.2 epistemic-scope distinctions under public-safety stakes
>
> The General Counsel requested a one-page Daubert + §1.2 grounding for any litigation following a dismissed-alarm scenario. The bank's reference spec §1.2 (a)-(e) supplies the five distinctions verbatim. Under Kognitos, no field articulates any of the five. The litigation-support file borrows §1.2 from the reference spec in cover-memo form. This is the second inarticulability in the program (after the April 15 patient at Helmstad), with stakes that scale to public safety rather than clinical-quality CAPA.

---

## 🔧 1:00 PM — OT Walkthrough with Aiyana (Multiple Findings)

After lunch, Aiyana Whitehorse — the OT Security Lead — walked them through the legacy OT stack. She was direct, like every OT security lead the team had encountered.

"PI historian. 60-day rolling audit trail. Below the NERC CIP-008-6 three-year incident-handling retention floor and below the CIP-009-6 three-year recovery-plan floor. We've known about this for two years. Funding is pending."

Luis: ✗ Field 12 + ✗ Field 1 (retention scope incomplete).

> ### 🚨 Finding-001 — PI historian 60-day retention below NERC CIP-008-6 / CIP-009-6 3-year minimum (Field 12 + Field 1)

"GE iFIX SCADA. UPDATE permission held by 8 DBAs across day and night shifts. The iFIX audit log is itself editable by the same DBAs. The hardening guide for iFIX 6.x recommends database-role split; we have not implemented."

Diana: ✗ Field 3 + ✗ Field 12 (legacy DBA UPDATE, mutable audit log).

> ### 🚨 Finding-002 — GE iFIX SCADA UPDATE-by-8-DBAs with mutable audit log (Field 3 + Field 12)

"Itron OpenWay AMI. Version 5.2 on most endpoints. Endpoint-side override lock is firmware-locked open on 23% of endpoints due to a known 5.2 firmware bug. The 5.4 firmware ships in Q3 2026 and closes the override. We have a Phase 2 plan to mass-rotate to 5.4."

Mike: ✗ Field 12 (firmware-level override-lock bug; tamper-evident integrity proof compromised at endpoint).

> ### 🚨 Finding-003 — Itron OpenWay AMI 5.2 firmware override-lock bug on 23% of endpoints (Field 12; pending firmware-rotation Phase 2)

"Shared HMI account in the dispatch center. Six dispatchers use one account for 18 months on the same SCADA terminal. No MFA. Same pattern as Stelvio's Plant_Engineer."

Diana: ✗ Field 3.

> ### 🚨 Finding-004 — Shared HMI dispatcher account; six dispatchers, one account, 18 months, no MFA (Field 3)

"Dispatcher_id binding. The `dispatcher_disposition` attribute on the leak-detection chain entries carries the dispatcher_id, but the binding is to the SCADA session — which is logged in to the shared HMI account. The dispatcher_id is the operator's stated identity, not the SCADA-authenticated identity. The chain captures who the operator says they are; SCADA cannot independently authenticate the individual."

Chen wrote: ⚠ Partial — Field 3 + Field 11 (dispatcher identity is stated, not authenticated).

> ### 🚨 Finding-005 — Dispatcher_id chain binding is stated-identity, not SCADA-authenticated (Field 3 partial)

"OMS work-order content-coupling. Work orders dispatched from the OMS reference the chain entry by entry_id, but the work-order content itself is in OMS — which is mutable. If someone retroactively edits a work order, the chain entry's reference still resolves but to mutated content."

Luis: ⚠ Partial — Field 10 (downstream action recorded; downstream-content mutable).

> ### ⚠ Partial #1 — OMS work-order content-coupling to chain entry resolves to mutable content

"Sensor-to-AI authentication. The 4,700 sensors feed iFIX. iFIX feeds the PI historian. PI feeds the leak-detection model via an ingestion adapter. The adapter has no `audit.connector_source.*` family today. We have Phase 2 plans to add it, plus firmware-attestation chain across supplier tiers when Itron 5.4 ships an integrity-checking firmware artifact."

Mike: ⚠ Partial — Field 6 (inputs with source attribution; SaaS-edge equivalent missing).

> ### ⚠ Partial #2 — Sensor-to-AI ingestion adapter lacks `audit.connector_source.*` family

She continued through six more legacy systems. The pattern was familiar. Each system was either field-history-disabled, DBA-mutable, or unchained altogether.

By 4 PM the OT side had 5 Findings + 6 Partials.

---

## 💳 4:30 PM — Customer-Billing Tier (Three More Findings)

Elena walked the customer-side stack. Itron OpenWay AMI feeds the CIS (Customer Information System). CIS feeds Salesforce. Salesforce drives customer-facing communications including dismissed-alarm follow-up. None of these are chain-instrumented.

She walked through three Findings on the customer-billing side: AMI override bug propagates downstream, CIS retains 30-day backups deletable by IT, Salesforce customer-contact field-history disabled selectively (same shape as Mercator).

> ### 🚨 Findings 006-008 — AMI override propagation, CIS backup mutability, Salesforce field-history selective

> ### ⚠ Partials #3-6 — IEC 62443-3-3 SR 7.5 audit-log discoverability; historian disk sizing; AMI override propagation; CIS retention discrepancy

---

## ⚡ 5:00 PM — PMU Clock + DR Rejoin

Two more sections that the framework had limited language for.

**PMU-grade GPS-disciplined master clock.** §10.4 normates NTP discipline as the minimum bar. The institution exceeded the bar with PMU (Phasor Measurement Unit)-grade GPS-disciplined timing — sub-microsecond accuracy across the multi-region utility grid. The bank's reference spec §10.14 trusted-time integration recognizes PMU-grade as exceeding the SHOULD bar. Under Kognitos, no field for time-trust grade.

**DR rejoin to Bonneville Power cold site.** §10.25 three-place tail acquisition. Six months ago, the institution exercised a DR drill that flipped the leak-detection chain from us-west-2 active to a cold site at Bonneville Power Administration's compute facility. Five tenants rejoined with no re-genesis events. The drill itself was a chained operational event.

> ### ◇ Framework-Silent Observations #2-3 — PMU-grade time-trust; DR rejoin to BPA cold site

---

## 🌆 5:30 PM — Auditor Debrief

The team gathered.

Dawn wrote on the whiteboard.

```
KOGNITOS 12-FIELD ASSESSMENT — PACIFIC CRESCENT POWER & GAS (POST-INCIDENT)

AI SIDE — PIPELINE LEAK DETECTION:
  Confirmations:                  12 (all fields)
  Live-alert demonstration:        1 (4-second verification; leak confirmed 22 min)
  Partials:                        0
  Findings against bank:           0
  Nits:                            0 (under Kognitos; reference spec records 1 §10.18)
  Framework-silent observations:   3 (live-alert speed; PMU clock; DR rejoin)

OT SIDE — PI / SCADA / AMI / OMS:
  Findings against bank:           5  (PI retention; iFIX UPDATE;
                                       Itron firmware override; HMI shared;
                                       dispatcher_id stated identity)
  Partials against bank:           6  (OMS coupling; sensor-to-AI adapter;
                                       SR 7.5; historian disk; AMI propagation; CIS)

BILLING SIDE — CIS / SALESFORCE:
  Findings against bank:           3
  Partials against bank:           4

CROSS-ZONE / FRAMEWORK-SIDE:
  Framework Inarticulability:      1 (§1.2 (a)-(e) distinctions for General Counsel
                                       one-pager; public-safety variant of Ch05's
                                       Inarticulability #1)
  Framework Under-Reporting:       1 (§10.18 dispatcher-runbook Nit; no Kognitos field)
  Framework Gap (recurring):       1 (coverage-boundary primitive — three-tier)
```

Underneath, she wrote:

```
ENGAGEMENT-TEAM OBSERVATIONS ON FRAMEWORK SELECTION:

1. The live methane alert during the engagement (10:47 AM) became the executive-
   briefing artifact for the CISO board. Verifier returned PASS in 4.1 seconds;
   crew confirmed a small leak in 22 minutes. Under our framework, this records as
   one Field 12 Confirmation. The operational properties — verification at speed-
   of-dispatch, no engagement disruption, chain-bound dispatcher-confirmation — are
   framework-silent.

2. The §1.2 (a)-(e) distinctions for the General Counsel's Daubert one-pager are
   inarticulable under our framework. The reference spec supplies five subclauses;
   our framework supplies none. The litigation-support file borrows §1.2 verbatim
   from the reference spec.

3. Public-safety stakes (a wrong reading and a dismissed alarm could blow up a
   neighborhood) make the §1.2 (c) line — chain proves what the model said,
   not what the sensor measured — the load-bearing forensic distinction. Our
   framework cannot articulate the line.

4. PMU-grade GPS-disciplined master clock exceeds the reference spec's §10.14
   SHOULD bar. Under our framework, time-trust grade has no row.

5. The §10.18 dispatcher-runbook missing-cross-reference Nit is invisible to our
   framework (recurring from Ch04 §E under-reporting).
```

She turned around.

Soren came back into the room. He had read the live-alert capture.

"That's the artifact. The CISO board meets tomorrow. The four-second verification capture is going on the first slide. The §1.2 (c) line is going on the second. The framework inarticulability you've documented is going in the appendix, because the General Counsel asked for the one-pager and your framework didn't supply it."

He paused.

"Tell your firm. The framework is acceptable as a vendor-facing summary. It is not acceptable as the only assessment artifact for any utility with public-safety stakes. We've been operating under the reference spec for nine months because the framework you brought cannot articulate the distinction between what the model said and what the sensor measured. Under public-safety law, that distinction is the difference between defending the dispatcher and not. On the record."

Dawn nodded.

"On the record."

---

## 🧾 Final Assessment Theme

> "The pipeline-leak-detection AI passes all 12 Kognitos fields with a live-alert demonstration during the engagement (4-second verification; leak confirmed 22 minutes). The OT and customer-billing tiers carry 8 Findings + 10 Partials. The §1.2 (a)-(e) epistemic-scope distinctions the General Counsel requested for the Daubert one-pager are inarticulable under the framework; the reference spec supplies them and the litigation-support file borrows them in cover-memo form. Under public-safety law, the §1.2 (c) distinction — chain proves what the model said, not what the sensor measured — is load-bearing and the framework cannot articulate it. The CISO requested on-the-record attribution of the framework's inadequacy for any utility with public-safety stakes."

---

## Research takeaway

Chapter 06 produces a second instance of Chapter 05's framework inarticulability category, this time with public-safety stakes that change the consequence:

- **Helmstad (Ch05):** §1.2 (c) finding inarticulable; consequence = clinical-quality CAPA + medical-monitor follow-up.
- **Pacific Crescent (Ch06):** §1.2 (a)-(e) distinctions inarticulable; consequence = General Counsel Daubert one-pager + potential public-safety litigation.

The same framework gap (no epistemic-scope clause) produces materially different consequences depending on engagement stakes. In Helmstad, the institution caught the M0-to-M1 correction via internal QC review. In Pacific Crescent, the institution operates with sensor-integrity at iFIX layer (mutable by 8 DBAs); the chain captures what the model saw; **the framework would discount the §1.2 (c) line and the litigation defense would be weaker.** Public-safety stakes don't tolerate framework silence the same way clinical-quality stakes can.

Running tally across six chapters:
- 47 speculation anchors (+4)
- 3 under-reportings (+1)
- 2 inarticulabilities (+1, second instance)
- 3 on-the-record stakeholder statements (Atrio, Helmstad, Pacific Crescent)

The pattern is consolidating: at every engagement where stakes scale beyond compliance-confirmation (regulator inspection, public safety, litigation defense), the framework's silences cost the institution materially. Three CISOs have now requested explicit attribution. Pacific Crescent's Soren added a new dimension — "any utility with public-safety stakes" — to the explicit-attribution pattern.
