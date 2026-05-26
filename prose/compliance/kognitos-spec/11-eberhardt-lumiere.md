# 11 — Eberhardt Werkstoffe × Lumière AI (Kognitos-lens)

*An engagement where two companies in two countries operate two independent chains that join only at the §10.21 cross-vendor seam, and the audit team has to articulate, four times under the framework lens, what a byte-equal hash join across an organizational boundary proves when neither party trusts the other.*

**Engagement:** Joint cross-vendor pre-audit ahead of EU AI Act enforcement (Articles 11, 12, 16 conformity-assessment file build) and an OEM joint-supplier audit. Five readers: EU AI Act conformity assessor; BSI + TISAX (DE-side); LfDI Baden-Württemberg + CNIL (joint GDPR Articles 25 / 32); OEM vendor-management; Big-Four assurance attestation.
**Client:** Eberhardt Werkstoffe GmbH (Stuttgart) — Mittelstand automotive-electronics supplier; eight months of chain instrumentation on the OEM-facing predictive-maintenance inference path (battery-health-module service). AWS Frankfurt HSM, daily Ed25519 seals. PARTNER: Lumière AI (Paris) — ~80-person French AI consultancy; four months chained on the model-build pipeline; ANSSI-aligned OVHcloud HSM, Roubaix region. The two chains join at the §10.21 `audit.model_handover.*` family.
**Status:** Chain in production: eight months Stuttgart + four months Paris. Each side has independently passed §7 verifier. The cross-vendor seam between the two chains has not been exercised under audit. Today is the first joint reconciliation.
**Audit team lead:** Dawn
**Client liaisons (Stuttgart):** Heinrich Becker (CTO, Eberhardt); Lukas Bauer (Head of Engineering); Margarete Fischer (DPO, Eberhardt); Andreas Krüger (Vendor Management); Konstantin Vogel (OEM vendor-management observer). **Client liaisons (Paris):** Sébastien Aubert (Founder/CEO, Lumière); Camille Rousseau (Chief AI Officer); Élise Marchand (DPO, Lumière); Nicolas Lefèvre (Engineering Lead). **Regulator-side observers:** Sigrid Walden (BSI, Stuttgart room); Tobias Schreiner (LfDI Baden-Württemberg, Stuttgart room); Geneviève Toussaint (CNIL, Paris room); Pascal Mortier (ANSSI consultative, Paris room).

**Audit team's framework:** Kognitos's 12-field schema. The team is now eleven engagements in. Cross-vendor partnership joints across an organizational boundary are new — two chains independently instrumented at two companies in two countries, joined only at the §10.21 model-handover seam. The byte-equal hash join across the seam produces a *joint* integrity claim without either party having to trust the other. Kognitos has no field for an integrity proof composed across an organizational boundary. The team has had the §1.4 substrate inarticulability conversation once before (NetiVa, Ch08); this is the second instance and the first cross-vendor variant.

---

## 🌅 8:30 AM CET — Dual kickoff (Stuttgart room + Paris room on video bridge)

The audit team split into two rooms at half past eight Central European Time. Dawn, Mike, and Elena were in Eberhardt's conference room on the second floor of the Stuttgart office. Diana, Luis, and Chen were on the Paris bridge — Lumière's office in the 12th arrondissement, four blocks from a Carrefour. The bridge had been open since 8:15.

Heinrich Becker opened from the Stuttgart side. Sébastien Aubert opened from the Paris side, in English, then again briefly in French for Geneviève Toussaint's benefit. The engagement was a five-reader pre-audit: EU AI Act conformity-assessment file (Articles 11 deployment-intent, 12 logging, 16 record-keeping); BSI IT-Grundschutz + ISO 27001 + TISAX for Eberhardt; LfDI Baden-Württemberg + CNIL joint reading for GDPR Articles 25 (privacy by design) and 32 (security of processing); OEM vendor-management's three standard questions; and Big-Four cross-framework assurance attestation reading the deliverable for SOC, ISAE, ISO 42001 composition.

The cross-vendor seam was the engagement's load-bearing feature. Lumière trained the model. Eberhardt deployed it. Lumière handed over the model artifact, the model card, and the fairness-audit report at a contractually-specified handover event; Eberhardt's chain captured the receipt; the §10.21 family stamped a triple — `model_artifact_sha256`, `model_card_sha256`, `fairness_audit_report_sha256` — and Lumière's chain stamped the same three byte-for-byte. The hash join at the seam was the joint integrity claim.

Margarete Fischer and Élise Marchand introduced the GDPR-side joint scope. Within-EU transfers between Stuttgart and Paris were SHOULD-emit under the cross-border-transfer attribute family — not the full third-country apparatus, but still attribute-bearing for the joint LfDI / CNIL reading. The DPIA scope under Article 35 was unified across the two DPOs.

Konstantin Vogel — OEM vendor-management — sat at the Stuttgart room's back wall with a notebook. He did not speak; he was the OEM's signal-receiver for the cross-vendor audit. Sigrid Walden (BSI) was beside him.

*Note for the chapter. Two chains. Two HSMs in two regions. One partnership boundary. The cross-vendor seam at §10.21 is the structural feature the framework will be measured against. The byte-equal hash join across the boundary is going to surface a question that the team has not asked since NetiVa: when integrity is composed across organizational boundaries without either party trusting the other, where in Kognitos does that composition land?*

> ### ✓ Confirmation #1 — Field 1, 2, 3, 4 satisfied on both sides independently
> Eight months Stuttgart, four months Paris. Production deployment intent on every instrument. Model identification and version pins on every entry. Both sides answer Fields 1-4 cleanly when read in isolation.

> ### ✓ Confirmation #2 — Field 12 satisfied on both sides; two independent HSM roots
> Eberhardt: AWS CloudHSM Frankfurt. Lumière: OVHcloud HSM Roubaix. Both at FIPS 140-2 Level 3+. Daily Ed25519 seals across both chains. Tamper-evident integrity proof on each chain in isolation.

## 🧬 9:30 AM — Verifier exercises (Stuttgart on inference; Paris on model-build)

Mike pulled the morning's predictive-maintenance entry from the Stuttgart chain — a battery-health-module inference for a connected vehicle in the OEM's customer fleet:

```json
{
  "entry_id": "eberhardt/battery-health/2026-05-22#1842",
  "tenant": "eberhardt",
  "service": "battery-health-inference",
  "seq": 1842,
  "ts": "2026-05-22T07:08:42.391Z",
  "model_id": "eb-bhm-v2.4",
  "model_version": "2.4.1-prod-pin-2026-04-30",
  "gen_ai.request.model": "lumiere/battery-health-modelfamily/v2.4.1",
  "gen_ai.response.model": "lumiere/battery-health-modelfamily/v2.4.1",
  "prompt": { "vin_hash": "...", "cell_telemetry_window_30d": "..." },
  "response": {
    "soh_estimate_pct": 91.4,
    "anomaly_score": 0.07,
    "recommended_action": "monitor_no_intervention"
  },
  "audit.deployment.intent": "production",
  "audit.deployment.policy_version": "eb-prod-policy-v3.1",
  "audit.model_handover.source_party": "lumiere",
  "audit.model_handover.model_artifact_sha256": "9e2a...4f01",
  "audit.model_handover.model_card_sha256": "1b7c...d22e",
  "audit.model_handover.fairness_audit_report_sha256": "3f5d...a911",
  "payload_hash": "...",
  "hmac": "...",
  "daily_seal_ref": "eberhardt/2026-05-22#seal"
}
```

```
$ herald-verify --tenant=eberhardt \
                --service=battery-health-inference \
                --date=2026-05-22 \
                --entry-id=1842 \
                --strict
```

Four seconds.

```
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified
        against public key fp:a4:c8:...:18
Elapsed: 4.0s
```

Mike then ran the verifier against a 180-day-old entry — November 2025 — to confirm long-horizon verifier consistency. PASS in 4.1 seconds.

Diana, on the Paris bridge, walked the model-build chain. The same model — `lumiere/battery-health-modelfamily/v2.4.1` — had a model-build entry from the Paris chain dated 2026-03-14. The build entry carried the three SHA-256s (model artifact, model card, fairness-audit report) and a `audit.training_data.manifest_sha256`.

```
$ herald-verify --tenant=lumiere \
                --service=model-build \
                --date=2026-03-14 \
                --entry-id=387 \
                --strict
```

Four seconds.

```
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified
        against public key fp:c1:e3:...:9a
Elapsed: 3.9s
```

Two independent chains. Two PASS verdicts. Both held in isolation.

*Note for the chapter. Each chain reads as clean by itself. The interesting moment will be when we cross the seam.*

## 🛡️ 10:30 AM — Training-data retention floor mismatch

Luis surfaced the mismatch ninety minutes into the morning. Lumière's training-data retention policy was 90 days from training completion — a privacy-default posture grounded in GDPR Article 5(1)(c) data minimization. Eberhardt's deployment window for the OEM battery-health model was 9 to 18 months of production runtime before the next retrain cycle.

The arithmetic was uncomfortable. If a regulator opened an inquiry on a model output at month 12 of deployment, the training-data corpus that produced the model was already 12 months removed from training completion — and Lumière had retained it for 90 days. The training data was gone.

Margarete Fischer fielded it from the Stuttgart side. The retention floor needed to bind to the deployment window, not to the training event. Élise Marchand agreed from the Paris side. Both DPOs had been talking to each other about this asymmetry for three weeks. Neither chain had a field that expressed the binding.

Lukas Bauer added the engineering dimension: the model artifact was hash-anchored at handover, the model card was hash-anchored, the fairness-audit report was hash-anchored — but the training-data manifest hash existed only on Lumière's side and pointed to a corpus that would be deleted at 90 days.

Chen, on the Paris bridge, wrote on his notepad. *No Kognitos field for retention-floor that binds to deployment-window. Field 4 (tools/models used) can name the model. Field 12 (integrity proof) can name the hash. Neither field can articulate "the training-data manifest hash points to an artifact that must be preserved for X months past handover where X is set by the deployment-window of the consuming chain."*

> ### ⚠ Partial #1 — Training-data retention floor binding to deployment window
> Lumière 90-day retention vs Eberhardt 9-18 month deployment window produces a coverage gap where the training-data manifest hash, while anchored in chain, points to a corpus that is deleted before the deployment-window closes. The two DPOs negotiated a 24-month retention commitment within ninety minutes — GDPR Article 6(1)(f) legitimate interest tied to EU AI Act Article 12 logging, with Article 35 DPIA. CAPA in flight. Under the reference spec, §10.20 will absorb this asymmetry as the worked example for "training-data retention floor bound to consuming-chain deployment window." Kognitos has no field for the binding.

> ### 🚨 Framework Under-Reporting #9 — Training-data retention floor as a chain-bound constraint
> Reference spec §10.20 (training-data retention floor, lifted to spec body via fourth errata, naming Eberhardt × Lumière as the source engagement) articulates `audit.training_data.retention_floor_days` as an attribute that propagates from the consuming chain's deployment-window discipline. Kognitos's twelve fields cannot articulate "this artifact's retention floor is set by a downstream chain's deployment-window." The training-data manifest can be hash-anchored under Field 12; the binding to deployment-window cannot be carried under any Kognitos row.

## ⚡ 11:00 AM — Within-EU cross-border-transfer Nit

Diana opened the next thread. The Stuttgart chain's predictive-maintenance entries carried `audit.cross_border_transfer.*` family stamps on three of every four entries — the data flow was Stuttgart → Paris for periodic re-evaluation against the fairness audit. But within-EU transfers were SHOULD-emit under the §10.21 worked-example paragraph, not MUST. Some of the entries omitted the attribute family on the basis that within-EU is structurally lower-risk than third-country.

Geneviève Toussaint, from the Paris room, raised a hand. CNIL's reading was that within-EU was not exempt from attribute-bearing — the GDPR Article 30 record of processing activities still required the transfer to be recorded, even where Chapter V's third-country apparatus did not apply. The §10.21 worked-example paragraph used SHOULD, not MUST, but the operational guidance was emit-by-default.

Sébastien agreed. Lumière would update the SDK to emit the attribute family on every cross-border entry within the next sprint. Nicolas Lefèvre — Engineering Lead — committed to the change before the joint reconciliation at 3 PM.

*Note for the chapter. The within-EU framing is fine substantively, but the framework cannot articulate the SHOULD-vs-MUST distinction at the attribute level — it's a per-jurisdiction reading question. Kognitos has no row for "emit this attribute family per jurisdiction policy."*

> ### 🚨 Finding-001 — Within-EU cross-border-transfer attribute emission inconsistent
> Three of every four entries carry the attribute family; the fourth omits it. Within-EU is SHOULD per §10.21 worked-example paragraph but the SHOULD-by-default operational reading is emit. Lumière will update the SDK before 3 PM. Under Kognitos this is a Nit at best — Field 5 (inputs) carries the data flow; nothing articulates the cross-border discipline.

## 🚨 11:30 AM — Author-approver SDK refusal walk (Paris side)

Diana walked the Paris-side IAM discipline. Lumière's model-build pipeline had a schema-enforced author-approver separation: the SDK refused to seal a build entry when the author identity matched the approver identity. The refusal was structural — at the SDK boundary, before chain entry construction — and produced an exit code that the build pipeline halted on.

Diana asked Camille Rousseau to demonstrate. Camille pulled a sandbox build environment and tried to commit a build entry with herself as both author and approver. The SDK refused at compile-of-the-chain-row. Build halted. The chain produced no row. Camille then logged in a second user (Nicolas) as approver and committed. Build succeeded; chain row produced.

The structural property — that the SDK refuses at capture rather than accepting and flagging — is a quality of the §10.22 + §10.21 family discipline. The chain cannot record an event that the SDK refused to seal, by design.

*Note for the chapter. Where, in Kognitos, does the refusal-at-capture event land? Field 11 (approval/oversight) names the approver when the event seals. When the event does not seal, there is no chain row to name anything. Field 10 (errors/exceptions) is wrong by category — the refusal isn't an error, it's an enforced policy. The structural property is at the SDK boundary, before any Kognitos field could file under any reading.*

> ### ◇ Framework-Silent Observation #5 — SDK-side refusal-at-capture as a structural property
> The SDK refusal at author-approver violation is a discipline that produces *no chain row at all* when it fires. Reference spec §10.22 + §10.21 + the SDK-side §4.4 enforcement clause carry the operational property as "capture-time enforcement; non-events do not appear in the chain because the SDK does not seal them." Kognitos can only describe what is in the chain. A discipline that prevents wrongness from entering the chain by refusing at the SDK boundary cannot be articulated by any Kognitos row — the discipline's signature is *absence*, and absence is not field-bearing.

## 🌍 12:00 PM — Joint bridge: byte-equal hash compare across two terminals

The room rearranged at noon. The Stuttgart and Paris terminals were each at the front of their respective rooms; both rooms were on the same video bridge. Mike, in Stuttgart, pulled the three SHA-256s from the Stuttgart chain entry. Diana, in Paris, pulled the three SHA-256s from the Lumière chain entry. The bridge had a shared whiteboard tile.

Both terminals showed the three values on screen:

```
EBERHARDT chain (Stuttgart) — entry 1842, attribute audit.model_handover.*:
  model_artifact_sha256:        9e2a...4f01
  model_card_sha256:            1b7c...d22e
  fairness_audit_report_sha256: 3f5d...a911

LUMIERE chain (Paris) — entry 387, attribute audit.model_handover.*:
  model_artifact_sha256:        9e2a...4f01
  model_card_sha256:            1b7c...d22e
  fairness_audit_report_sha256: 3f5d...a911
```

Three byte-for-byte matches across two independent chains. Heinrich Becker exhaled audibly. Sébastien Aubert smiled. The joint integrity claim was not produced by either chain alone; it was produced by the byte-equal composition of two independent chains, neither of which had to trust the other.

Sigrid Walden (BSI) asked the question that landed the §1.4 conversation later in the afternoon. She asked Dawn how Kognitos described the structural property she had just watched.

Dawn answered honestly. Kognitos described each of the two chain entries as Field-12 confirmation in isolation — a tamper-evident integrity proof on each side. The fact that the two field-12 proofs *also* compose into a joint integrity claim across an organizational boundary, without requiring either party to trust the other, was not articulated in any of the twelve fields. The composition was the load-bearing security argument under the reference spec's §1.4 — extended across the partnership boundary by §10.21. Kognitos's twelve fields named the components; nothing named the composition.

> ### ✓ Confirmation #3 — Byte-equal hash join across two independent chains; joint integrity claim demonstrated
> Three SHA-256s match byte-for-byte across the Stuttgart and Paris chains at the §10.21 model-handover seam. Each chain independently passes §7 verifier; the two chains compose into a joint integrity claim through the byte-equal hash join, without either party trusting the other. Operationally clean.

> ### ◇ Framework-Silent Observation #6 — Cross-vendor zero-trust composition across organizational boundary
> The joint integrity claim is produced by composition of two independent chains. The composition is structural — neither party is the source of trust; the byte-equal hash join is the integrity claim. Reference spec §1.4 (compositional security) extended across §10.21 (cross-vendor model-handover schema) carries the property as the central security argument of the engagement. Kognitos can describe each chain in isolation; it cannot articulate that the composition produces trust where no single chain could.

## 🛡️ 1:30 PM — §1.4 organizational-boundary inarticulability + §1.2 model-bias boundary

After the lunch break, Margarete and Élise opened the §1.2 boundary conversation. The chain proved what was deployed and what was handed over. The chain did not prove that the model was unbiased. The fairness-audit report was hash-anchored at handover; the audit had been run by an independent third party under Lumière's contracting; the chain held the integrity proof that the audit document existed at handover and had not been mutated since. The chain did not prove the audit's conclusions were correct.

Élise walked the boundary in French and then in English: the chain proves the fairness audit was the audit at handover. The chain does not prove the audit's conclusions are correct.

Dawn nodded. Field 8 (reasoning/rationale) carried the fairness-audit hash; Field 12 (integrity proof) carried the seal. No field distinguished "the audit document exists" from "the audit's conclusions are correct."

The §1.4 organizational-boundary conversation came next. Sigrid Walden returned to her noon question. The byte-equal hash join at the seam produced the joint integrity claim. The joint claim was *structurally* stronger than either chain in isolation — composition added trust where independent inspection could not. Under the reference spec, §1.4 articulated the composition explicitly: per-event HMAC + daily Merkle seal + HSM signature on each side, plus the §10.21 cross-vendor anchor, composed to a 128-bit-composite zero-trust integrity claim across the organizational boundary.

Under Kognitos, the composition was structurally inarticulable. Field 12 named one party's proof. There was no field that named the composition with the other party's proof. There was no field that named what the composition added.

*Note for the chapter. This is the second instance of §1.4 substrate-class inarticulability in the program. NetiVa was within-vendor (per-event + Merkle + HSM signature within one chain). Eberhardt × Lumière is cross-vendor (two chains composing at the §10.21 seam). The framework's row-shape cannot articulate composition in either case. The cross-vendor case is sharper because the composition is also where trust originates — neither party trusts the other, and the byte-equal hash join is the trust-producing step.*

> ### ⚠ Framework Inarticulability #8 — Cross-vendor zero-trust composition across organizational boundary (§1.4 variant)
> Reference spec §1.4 (compositional security) extended across §10.21 carries the joint integrity claim as a 128-bit composite that produces trust where no single chain produces it. Kognitos's twelve fields name the components in isolation; no field names the composition or what the composition adds. This sharpens NetiVa's §1.4 substrate inarticulability into a cross-vendor case — second instance of substrate-class inarticulability; first cross-vendor instance.

> ### ⚠ Framework Inarticulability #9 — Model-bias boundary (§1.2 variant: fairness-audit-vs-model-fairness)
> The chain proves the fairness audit document existed at handover and has not been mutated since. The chain does not prove the audit's conclusions are correct, the model is unbiased, or the audited claims are factually true. This is the fifth §1.2 variant in the program — after Helmstad (post-enrollment correction), PCP (sensor mutation), Olmstead (civil-rights litigation), Sun-Won (pre-chain era), Salt Pond (FRE 902(13)/(14) litigation-defense). Eberhardt × Lumière adds: the fairness-audit-document-vs-model-fairness boundary. Kognitos has no field for this distinction.

## 🔧 2:30 PM — Plural-array `audit_report_languages` Nit

Chen surfaced the third Nit on the Paris-side fairness-audit walk. Lumière's fairness-audit report was written in French. The chain entry's `audit.model_handover.audit_report_language` attribute was a singular string field: `"fr"`. The §10.21 worked-example paragraph in the reference spec specified `audit_report_languages` as a *plural array* — `["fr", "en"]` once translation existed, `["fr"]` for the current state.

The plural-array discipline mattered for the OEM vendor-management reader. OEM's standard audit-report-language expectation was English — the OEM ran its global supplier-audit under English. Eberhardt would consume a French audit; OEM would consume an English audit. The chain had to carry both languages once the English translation existed.

Sébastien committed: Lumière would deliver the English fairness-audit translation in four weeks; SDK update to plural-array within the next sprint; standing practice across all engagements going forward.

*Note for the chapter. The plural-array discipline is genuinely structural — the chain carries the language inventory as a row attribute, and any reader can query which languages cover which artifacts. Under Kognitos, no field carries language inventory. Field 4 (tools/models) names the model; nothing names the audit-document language coverage.*

> ### 🚨 Finding-002 — Plural-array `audit_report_languages` alignment
> Current chain attribute is singular `"fr"`. Reference spec §10.21 plural-array discipline requires `["fr", "en"]` once translation exists. Sébastien committed to four-week translation delivery + SDK update. Under Kognitos this surfaces as a free-text gap — no field carries audit-document language inventory.

> ### 🚨 Framework Under-Reporting #10 — Audit-document language coverage as chain attribute
> Reference spec §10.21 plural-array `audit_report_languages` is the canonical row shape for tracking which audit-document language coverages exist at handover. Kognitos has no field for the inventory.

## 💳 3:00 PM — Fifteen-minute seven-leg cross-vendor end-to-end trace

Lukas Bauer started the timer at three sharp. The chosen OEM alert was from May 14 — a single vehicle in the OEM's customer fleet had triggered an anomaly score above threshold. The recall-trace tool walked the chain across both companies, joining at the §10.21 seam:

1. Vehicle telemetry → Eberhardt ingestion (1 chain row)
2. Eberhardt inference run → battery-health output (1 chain row)
3. §10.21 model-handover anchor at inference time → Lumière model build (1 hash join across chain boundary)
4. Lumière model-build entry → training-data manifest hash (1 chain row)
5. Training-data manifest → per-shard transfer reconciliation (5 chain rows)
6. Fairness-audit report hash → fairness-audit document retrieval (1 chain row + 1 external-artifact resolution)
7. OEM alert receipt → vendor-management notification (1 chain row)

Total chain rows across both chains: 11. Verifier produced PASS across all 11 in the join order. Byte-equal hash matches at each of the three §10.21 anchors and at the training-data manifest cross-anchor.

Lukas stopped the timer. Fourteen minutes, forty-eight seconds.

Konstantin Vogel — OEM vendor-management — wrote in his notebook for the first time that day. He looked up at Heinrich.

This was the OEM's three-questions test: can the supplier produce a verifiable trace from a customer-facing anomaly back to training data, across the partnership boundary, in operationally sensible time? Eberhardt and Lumière, jointly, had answered yes in under fifteen minutes.

*Note for the chapter. The seven-leg trace is the cross-vendor analog of Salt Pond's fourteen-minute cross-location reconciliation. The structural property is the same — chain rows are sequenced, hashable, verifier-walkable in cross-service joins, reconcilable at the seam. The difference is that the seam crosses an organizational boundary, and the byte-equal hash join is the trust-producing step. Under Kognitos this trace would have to be argued out as editorial summary across two independent twelve-field deliverables, with the join itself unarticulated.*

> ### ◇ Framework-Silent Observation #7 — Cross-vendor seven-leg end-to-end trace as a structural property
> Under fifteen minutes elapsed; byte-equal hash matches at every §10.21 anchor; verifier PASS across all eleven chain rows in join order. The structural property combines §10.21 (model-handover), §7 (verifier), §5 (RFC 8785 JCS canonicalization), and §8 (conformance test vectors enabling cross-vendor byte equality). Reference spec produces the property as a reproducible operational outcome. Kognitos's per-row architecture cannot articulate the join across organizational boundary as a structural property.

## 🌆 5:00 PM CET — Joint debrief

Both rooms reconverged on the bridge. Dawn wrote the joint whiteboard tally:

```
KOGNITOS 12-FIELD ASSESSMENT — EBERHARDT × LUMIÈRE
(JOINT CROSS-VENDOR / DE + FR / EU AI ACT + BSI + LfDI/CNIL + OEM + ASSURANCE)

EBERHARDT SIDE — BATTERY-HEALTH-INFERENCE (8 MONTHS):
  Confirmations:                  3 (Fields 1-4, 5-8, 12)
  Partials:                       0
  Findings:                       0
  Nits (under Kognitos):          1 (within-EU cross-border-transfer; ref spec §4.4.1)

LUMIERE SIDE — MODEL-BUILD (4 MONTHS):
  Confirmations:                  3 (Fields 1-4, 5-8, 12)
  Partials:                       0
  Findings:                       0
  Nits (under Kognitos):          1 (plural-array audit_report_languages; ref spec §10.21)

JOINT / CROSS-VENDOR SEAM:
  Confirmations:                  2 (byte-equal hash join at §10.21 seam; 15-min seven-leg trace)
  Partials:                       1 (training-data retention floor; ref spec §10.20 CAPA)
  Findings:                       0

FRAMEWORK-SIDE:
  Framework Inarticulability:     2 (§1.4 cross-vendor zero-trust composition; §1.2 fairness-audit-vs-model-fairness variant)
  Framework Under-Reporting:      2 (training-data retention floor binding; audit-doc language coverage)
  Framework-Silent Observation:   3 (SDK refusal-at-capture; cross-vendor zero-trust composition; 7-leg cross-vendor trace)

CROSS-CHAPTER META:
  §12 engagement-source amendments this engagement: 2 (§10.20 + §10.21)
  §12 amendments in last 4 chapters: 7 (NetiVa 1 + Sun-Won 2 + Salt Pond 2 + Eberhardt-Lumiere 2)
  Framework-cannot-grow meta:     4 consecutive chapters now confirmed
```

Dawn ran the framework-side observations:

1. **Cross-vendor zero-trust composition is structurally inarticulable.** The byte-equal hash join at §10.21 produces a joint integrity claim that neither chain alone could produce. Kognitos's twelve fields name the components of each chain in isolation; no field names the composition or what it adds. This is the second §1.4 substrate-class inarticulability instance in the program (after NetiVa Ch08); first cross-vendor variant.

2. **Training-data retention floor binding is structurally missing.** Lumière's 90-day retention vs Eberhardt's 9-18-month deployment window produces a coverage gap that the reference spec absorbs at §10.20 as the worked example. Kognitos has no field for retention-floor-bound-to-deployment-window.

3. **Audit-document language coverage is structurally missing.** Plural-array `audit_report_languages` is the canonical row shape; Kognitos has no field for language inventory.

4. **SDK-side refusal-at-capture cannot be articulated.** When the SDK refuses to seal an event (author-approver violation), no chain row exists. Absence is not field-bearing under any Kognitos reading.

5. **Cross-vendor seven-leg end-to-end trace is a structural property of the joined chains.** Under fifteen minutes; byte-equal hash matches at every seam; reproducible operational outcome. Kognitos's per-row architecture cannot articulate join-across-organizational-boundary as a structural property.

6. **Fairness-audit-vs-model-fairness boundary (§1.2 variant) is structurally inarticulable.** The chain proves the fairness audit existed at handover; it does not prove the audit's conclusions are correct or the model is unbiased. Fifth §1.2 variant in the program.

Chen, on the Paris bridge, added the meta-property observation. The reference spec absorbed two amendments from this engagement — §10.20 (training-data retention floor) and §10.21 (plural-array `audit_report_languages` plus within-EU cross-border-composition note). With NetiVa's §10.17, Sun-Won's §4.4 + §4.4.1, and Salt Pond's §10.19 + `audit.external_artifact.*`, the running tally is now *seven engagement-source amendments across four consecutive chapters*. The framework-grows-vs-fixed contrast is now four-chapter-consecutive reproducible. Predicts that any future engagement on the leading edge of audit-trail design will produce §12 change-log entries that Kognitos cannot match.

## Stakeholder statement — Heinrich Becker (Eberhardt CTO) + Sébastien Aubert (Lumière CEO), cross-vendor partnership joint

Both came back at six-fifteen, on the bridge, with Konstantin Vogel still in the back of the Stuttgart room and Geneviève Toussaint still in the Paris room. Heinrich spoke first; Sébastien followed.

Heinrich, on the record: *"I am the Chief Technology Officer of Eberhardt Werkstoffe. We are a Mittelstand automotive-electronics supplier with eight months of chain instrumentation on our OEM-facing inference path. Our partner Lumière trains the model; we deploy it. The cross-vendor seam between our two chains is the structural feature on which our OEM joint-supplier audit will turn, and it is the structural feature that will determine our EU AI Act conformity-assessment file's load-bearing security argument. The audit team walked our chain and Lumière's chain with discipline today, under the Kognitos framework. The framework records each chain in isolation cleanly. It does not record the cross-vendor seam — neither the byte-equal hash join that produces our joint integrity claim, nor the §10.21 model-handover schema that lets two independent companies compose trust without either trusting the other. I have read Patrick Cavanaugh's statement from Salt Pond and the cross-jurisdiction statement from Sun-Won and the framework-substitution statement from Pankaj Iyengar at NetiVa. Eberhardt co-signs the framework-substitution recommendation, with the new sharpening dimension that our engagement adds: cross-vendor partnership composition across an organizational boundary. The framework cannot articulate composition. We need the reference spec, not the framework, for the engagement that defines our partnership."*

Sébastien, on the record: *"I am the founder and chief executive of Lumière AI. We are an eighty-person French AI consultancy. We have spent four months instrumenting our model-build pipeline under the reference spec, and today is the first day we have read the cross-vendor seam under joint audit. The byte-equal hash join at our handover with Eberhardt produced what I hoped it would produce: a joint integrity claim that did not require either of us to trust the other. The composition is the trust-producing step. Under Kognitos, neither side's deliverable can articulate what the composition adds, because the composition is the *interaction* between two chains, and the framework has no row for interaction. The framework-substitution recommendation that Heinrich co-signs, I co-sign. The reference spec absorbed our engagement's two findings — the training-data retention floor at §10.20 and the plural-array `audit_report_languages` at §10.21 — within the past week, under the §12 change-log mechanism. Seven engagement-source amendments in four consecutive chapters. The reference spec is moving to meet the work; the framework cannot move. We want that distinction on the record. The cross-vendor partnership joint is the seventh voice pattern in our auditor's running notebook, and we want our names against it: Eberhardt Werkstoffe and Lumière AI, joint signatories, framework-substitution recommendation for any engagement where the structural feature crosses an organizational boundary at a §10.21 cross-vendor seam."*

Heinrich and Sébastien both signed. Dawn replied: *"On the record."*

## 🧾 Final Assessment Theme

> "Eberhardt Werkstoffe × Lumière AI produced a clean joint cross-vendor deliverable on the chain side — two independent chains across an organizational boundary, joined byte-for-byte at the §10.21 cross-vendor model-handover seam, fifteen-minute seven-leg end-to-end trace across the seam, two independent HSM roots in two EU jurisdictions, byte-equal hash matches at every cross-vendor anchor. Under Kognitos, the deliverable carried two Findings (within-EU cross-border-transfer emission, plural-array `audit_report_languages` alignment), two Framework Under-Reportings (training-data retention floor binding, audit-document language coverage), two Framework Inarticulabilities (§1.4 cross-vendor zero-trust composition as second substrate-class instance; §1.2 fairness-audit-vs-model-fairness as fifth §1.2 variant), three Framework-Silent Observations (SDK refusal-at-capture as absence-bearing; cross-vendor zero-trust composition; cross-vendor seven-leg trace as structural property), and one Partial (§10.20 training-data retention floor; CAPA in flight, 24-month commitment). Heinrich Becker and Sébastien Aubert co-signed the cross-vendor partnership joint statement — the seventh voice pattern in the program, the fourth framework-substitution recommendation, sharpened against the cross-vendor composition dimension. Reference spec's fourth errata absorbed §10.20 + §10.21 amendments from this engagement; with NetiVa's §10.17, Sun-Won's §4.4 + §4.4.1, and Salt Pond's §10.19 + `audit.external_artifact.*`, the running tally is seven engagement-source amendments across four consecutive chapters. The framework grew, four chapters in a row. The framework with twelve fixed fields did not."

## Research takeaway

Eberhardt × Lumière is the fourth consecutive engagement to drive content into the reference spec body and the first cross-vendor partnership engagement in the program. The framework-grows-vs-fixed contrast is now four-chapter-consecutive reproducible (NetiVa §10.17 + Sun-Won §4.4 + §4.4.1 + Salt Pond §10.19 + `audit.external_artifact.*` + Eberhardt-Lumière §10.20 + §10.21 = seven engagement-source amendments). Predicts that any future engagement on the leading edge of audit-trail design will produce §12 change-log entries Kognitos cannot match.

The new dimensions Eberhardt × Lumière contributes:

- **Cross-vendor partnership composition across an organizational boundary** as the second §1.4 substrate-class inarticulability instance. NetiVa's substrate-class inarticulability sat within one vendor (per-event + Merkle + HSM composing under one HSM root). Eberhardt × Lumière's sits across an organizational boundary (two chains, two HSM roots, two companies, two jurisdictions). The composition is the trust-producing step; Kognitos cannot articulate composition under any reading.
- **Training-data retention floor bound to consuming-chain deployment window** as a new under-reporting class. §10.20 absorbs the binding into the spec body; Kognitos has no field for retention-floor as a deployment-window function.
- **Audit-document language coverage** as a new under-reporting class. Plural-array `audit_report_languages` carries the language inventory as a row attribute; Kognitos has no field.
- **SDK-side refusal-at-capture** as a structural property the framework cannot articulate. The discipline's signature is *absence* — events that the SDK refuses to seal produce no chain row — and absence is not field-bearing under any Kognitos reading.
- **Cross-vendor seven-leg end-to-end trace** as a structural property of the joined chains. Extends Salt Pond's 14-minute cross-location reconciliation into the cross-organizational-boundary case. Kognitos's per-row architecture cannot articulate join-across-boundary as a structural property.
- **Cross-vendor partnership joint stakeholder statement** as the seventh voice pattern. Distinct from Helmstad-style same-dimension same-institution joint, from Sun-Won-style cross-jurisdiction same-institution joint, and from Salt Pond-style cross-functional same-institution joint. First instance of two-executive joint across an organizational boundary.
- **Fourth framework-substitution recommendation**, now stable as a four-chapter-consecutive pattern (Pankaj → Min-seo + Wei-ling → Patrick + Naomi → Heinrich + Sébastien). Sharpening dimension this chapter: cross-vendor composition.
- **Within-EU cross-border-transfer attribute emission** as a recurring §4.4.1 variant — third cross-border instance (after NetiVa cross-border legs Ch08, Sun-Won cross-jurisdiction Ch09), first within-EU SHOULD-vs-MUST framing.
- **Cross-language CC8.1 across three languages** — German + French + English. Fourth cross-language variant in the program (after English-default, Hebrew, Korean+Mandarin).

---

*Running counts and program-level signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
