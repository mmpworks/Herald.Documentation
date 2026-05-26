# Comparative Analysis — Chapter 13 (Saraswati Microfinance)

*Side-by-side analysis of how the Kognitos 12-field framework and the TesseraSeal / FFIEC chain-of-custody v1.0b spec handle a **pre-RBI IT Governance Master Direction inspection with DPDP Act §6 overlay** at a ~$1.6B Indian NBFC-MFI running edge-AI federated learning across 15,000 ruggedized Android tablets. Honest assessment of where the architecture itself is structurally wider than the framework's vocabulary at three integrity surfaces simultaneously — the program's first chapter where framework inarticulability outnumbers framework confirmation on the AI side by a 5-to-3 margin.*

---

## New research signal — architecture-wider-than-framework as a chapter class

The program's prior framework-gap chapters had a common shape: one surface of the architecture (tenant-isolation at Atrio; redaction-disposition at Helmstad; stated-identity vs authenticated-identity at Pacific Crescent) produced a single framework-side inarticulability. The audit team would record the gap, the institutional liaison would optionally produce a boundary-setting statement, the engagement would close with operational compensation documented.

Saraswati is structurally different. The architecture has three integrity surfaces (central inference, edge inference across 15,000 tablets, federated-learning aggregator) and the Kognitos 12-field schema is structurally narrower than two of the three. The central inference path reads cleanly under all twelve fields. The edge inference path produces four Framework Inarticulabilities (per-device key derivation; edge attestation; late-arrival seal; hierarchical Merkle). The federated-learning aggregator produces one Framework Inarticulability (training-phase integrity) with four sub-aspects. The DPDP Act §6 consent-lifecycle binding produces a fifth Framework-Silent Observation (lifecycle-as-state invisible).

The new chapter-class signal: when the architecture has multiple integrity surfaces, framework reach must be evaluated per-surface. A framework can be sufficient for surface X and structurally silent on surface Y at the same engagement, and the institution must compose framework + operational compensation per-surface to maintain a defensible regulator-facing posture.

| Distinction | Prior framework-gap chapters | Saraswati (Ch13) |
|---|---|---|
| Number of inarticulability-producing surfaces | 1 per chapter | 3 simultaneously |
| Framework-confirmation count on AI side | Usually 5-8 | 3 (central path only) |
| Framework-inarticulability count on AI side | Usually 1-2 | 5 |
| Operational compensation systems named | 1-2 (runbook; SIEM) | 4 (runbook; MLflow; Confluence; parallel index) |
| Regulator-facing memo composition | Framework alone | Framework + compensation |

The closing line: this chapter is the program's clearest argument that audit-trail-framework vocabulary breadth, not depth, is the constraint that matters at architectural edges. Kognitos can verify what it has fields for. It cannot verify what it does not have vocabulary for.

---

## Recurring from earlier chapters

| Recurring point | Earlier ref | Ch 13 instance |
|---|---|---|
| Compositional security under §1.4 | Ch01 §4 | Central path's clean read is the §1.4 composition; edge + federated surfaces have no §1.4 equivalent under Kognitos because the framework has no vocabulary for the substrate primitives at those surfaces |
| Five-minute path under §0.5.4 | Ch04 §0.5.4 | Vikram's draft memo follows the §0.5.4 short-path structure (twelve fields named, four primitives named, stakeholder entry named) but applied to the institution's compensation matrix rather than the framework alone |
| Per-tenant HKDF binding under §4.1 | Ch04 Atrio | Saraswati extends §4.1 with the §10.32 per-device sub-component; the framework reads neither the tenant binding nor the device binding |
| Daubert / epistemic scope under §1.2 | Ch05 Helmstad | The SDK-process compromise residual is the §1.2 surface here; Android Keystore TEE attestation under §10.35 is the partial compensation; framework has no vocabulary for either the residual or the compensation |
| Stakeholder direct-boundary-setting voice pattern | Ch04 Veronika at Atrio | Aparna Desai at Saraswati — same voice pattern, applied to DPDP Act §6 compliance rather than tenant-isolation |
| Engagement closes with framework + compensation rather than framework alone | Ch04, Ch05, Ch06 | Saraswati composes framework + four distinct compensation systems per-surface |
| Reference spec named in client-side memo as alternative | Ch11 Eberhardt × Lumière | Vikram's memo explicitly names the FFIEC chain-of-custody reference spec as the framework that would close the gaps structurally; institution has not adopted as of engagement |
| IKM rotation across seal boundary | Ch10 Salt Pond | Saraswati retired-tablet case exercises §10.10 rotation; chain verifies cleanly; Kognitos reads Field 11 + Field 12 cleanly but cannot read the rotation as a rotation event |
| Foresight-cluster (Ch12-Ch17) substrate pressure | Ch12 Hill Country | Ch12 surfaced single-substrate within-organization; Ch13 surfaces multi-surface within-institution at the architectural edge — second data point in the cluster's trajectory |

**Severities unchanged.** No re-litigation of recurring points; the chapter introduces five new framework inarticulabilities and two new framework-silent observations against the recurring substrate.

---

## New comparison points specific to Chapter 13

### A. Per-device session key derivation

**The audit-room question.** *"If a field officer's tablet is compromised and the session key is extracted, can the attacker forge chain entries for any other tablet in the fleet?"*

**TesseraSeal.** §10.32 normates the per-device HKDF extension: `HKDF_INFO_BASE || '|' || utf8(tenant_id) || '|' || utf8(device_id)`. The session key is bound to the specific tablet's device ID. A compromised device's session key cannot produce valid MACs for any other device. The compromise is contained to the single tablet. The reference spec exercises this at 15,000 tablets in production.

**Kognitos.** Field 11 (tamper-evident integrity / hash chains) records that integrity proof exists. The schema has no vocabulary for the *scope* of the proof — whether the key is per-tenant, per-device, per-service, or flat across the entire institution.

**Inarticulability gap.** A compromised tablet's session key surfacing in chain entries claiming to be a different tablet would be invisible to a Kognitos auditor reading the twelve fields. The verifier would confirm Field 11 passes — the MAC is mathematically valid against *some* session key — but it has no way to express that the session key in question is bound to a different device than the entry claims. The auditor would have to invent the per-device-binding check from engagement-specific knowledge of the SDK.

**Structural reason for the gap.** Kognitos's twelve fields were designed for institution-scoped audit-trail capture where a single key root protects an institution's entire chain. Edge architectures break this assumption: every endpoint is its own key holder, and per-device key derivation is the structural mechanism that contains compromise. The framework has not engaged with the edge-architecture key-derivation pattern.

**Honest assessment.** Severity: high for institution class running edge architectures (microfinance, retail field operations, distributed sensor networks); not applicable for institutions whose architecture is wholly server-side.

### B. Edge-attestation primitive

**The audit-room question.** *"Can we demonstrate that each chain entry produced on a tablet was produced by a hardware-attested key on a non-rooted device, at the moment of chain-entry production?"*

**TesseraSeal.** §10.35 normates the edge-attestation primitive: every chain entry carries `audit.edge.attestation_doc_sha256` referencing an Android Keystore TEE attestation document that binds device hardware-integrity state — attestation root, attestation chain to Google's root key, hardware-backed key generation, no rooted/jailbroken pollution. The attestation is contemporaneous with chain-entry production. The §1.2 SDK-process-compromise residual is partially compensated.

**Kognitos.** No field. The schema has no concept of hardware attestation. Field 11's hash-chain integrity assumes the SDK process is trusted; there is no extension point for binding device hardware-integrity state to the chain entry.

**Inarticulability gap.** The integrity-strengthening at the edge — the partial compensation for the §1.2 SDK-process-compromise residual — is invisible to the framework. A Kognitos auditor cannot record that 15,000 tablets are hardware-attested. They cannot record that the field officer's device was non-rooted at the moment of the credit decision. They cannot record the attestation chain to Google's root.

**Structural reason for the gap.** Edge architectures rely on TEE hardware-attestation as the primary compensation for the wider compromise surface at the device. Server-side architectures do not have this requirement because the SDK process is institutionally trusted. The Kognitos schema's framework boundary stops at the SDK process; it has no vocabulary for compensations to the SDK process's own trust assumption.

**Honest assessment.** Severity: highest for institutions where edge devices are in untrusted physical environments (field officers, retail clerks, rural branches, BYOD-class endpoints); high for institutions where edge devices are in semi-trusted environments (warehouse staff, factory floor); not applicable for server-side-only architectures.

### C. Late-arriving-entry seal discipline

**The audit-room question.** *"For an entry produced offline at 14:39 IST that arrives at central reconciliation at 19:15 IST and gets covered by a supplemental seal at 04:30 IST the next day — between 14:39 and 04:30 the next day, what is the integrity claim?"*

**TesseraSeal.** §10.36 normates the Pattern A late-arrival seal discipline. The chain entry carries a per-event MAC at capture that proves device-binding integrity for the 14-15 hour window. The central daily seal cuts at the normal UTC boundary. A supplemental seal at the following day's seal cut explicitly covers the late-arriving entries with a `seal-supplemental` reference. The verifier knows about both the normal seal and the supplemental seal; the integrity claim is well-defined across the entire window.

**Kognitos.** Field 11 (hash chains) assumes contemporaneous capture — chain is sealed when the entry is produced. There is no vocabulary for an entry that exists with per-event MAC integrity but no central seal coverage for 14-15 hours, then gets covered by a supplemental seal the following day. The framework either says the chain is sealed or it is not.

**Inarticulability gap.** The integrity claim asymmetry between per-event MAC (covers 14-15 hour window) and central seal (covers the post-reconciliation period) is invisible to the framework. A Kognitos auditor cannot record a third state for "MAC-only / seal-pending" entries. They cannot demonstrate that the asymmetry is bounded and managed by the late-arrival seal discipline.

**Structural reason for the gap.** Offline-first edge architectures necessarily have asymmetric integrity windows. Server-side architectures do not because the chain is sealed at capture. The Kognitos schema was designed against the server-side assumption.

**Honest assessment.** Severity: high for institutions running offline-first edge operations (microfinance field officers, rural credit unions, disaster-response teams); medium for institutions with intermittent cellular but mostly online; not applicable for server-side-only architectures.

### D. Hierarchical Merkle aggregation

**The audit-room question.** *"When a tablet returns from a week of no-cellular operation, does the institution push the entire chain to verify the tablet's entries, or just the tablet's subtree?"*

**TesseraSeal.** §10.37 normates two-level Merkle aggregation. Each tablet maintains its own per-device Merkle subtree. The subtree root is a leaf in the daily central Merkle seal. When a tablet returns from extended offline operation, the verifier needs only the tablet's subtree root plus the entries the tablet produced — not the entire global chain. Bandwidth efficiency is essential for the rural-cellular reality.

**Kognitos.** Field 11 hash chains; no two-level Merkle aggregation vocabulary. The framework has a single integrity claim per entry; it cannot express the per-device subtree as a separable sub-claim.

**Inarticulability gap.** A bandwidth-efficient verification path for offline-first edge devices is invisible to the framework. The institution maintains the two-level structure in the chain; the verifier resolves it correctly. The Kognitos auditor cannot demonstrate the structure as a structural property of the chain.

**Structural reason for the gap.** Hierarchical aggregation is a bandwidth optimization specific to edge architectures with intermittent connectivity. Server-side architectures do not require it. The Kognitos schema does not engage with bandwidth-efficient verification at the edge.

**Honest assessment.** Severity: medium for institutions running edge operations in cellular-coverage-variable geographies; low for institutions with reliable connectivity at the edge; not applicable for server-side-only architectures.

### E. Training-phase integrity in federated learning

**The audit-room question.** *"For the federated-learning cycle that produced the new global model on 2026-05-01, can we demonstrate the gradient contributions, the aggregation operation, and the validation against held-out test set — all chain-bound?"*

**TesseraSeal.** §10.34 normates training-phase integrity. The `audit.training.*` family covers `local_gradient` (privacy-preserving via hash, no underlying data), `aggregation`, `validation` against held-out test set, `model_artifact` production. §10.64 normates the broader training-run code-and-config chain primitive. The federated-learning cycle produces chain entries at every boundary moment of the training-phase activity. The validation outcome is chain-bound; the held-out test set is chain-bound; the aggregation operation's deterministic re-runnability is chain-bound.

**Kognitos.** Field 7 (model id + version) records *which* model was used at inference time. The schema has no vocabulary for *how the model was produced* — the gradient contributions, the aggregation operation, the validation outcome.

**Inarticulability gap.** The training-phase activity is operationally documented at Saraswati in MLflow records, in Confluence documentation, in the federated-aggregator's own logs. The institution's MRM committee reviews validation outcomes quarterly. None of this is chain-bound under Kognitos because the framework's twelve fields are oriented to inference-phase audit-trail capture. The training-phase integrity story is structurally invisible to the framework.

**Structural reason for the gap.** Kognitos was designed before training-phase integrity emerged as a regulatory expectation. The RBI Master Direction 2024 update is one of the first regulator surfaces that explicitly requires training-phase visibility. The framework's twelve fields predate this requirement.

**Honest assessment.** Severity: highest for institutions running federated learning, on-device personalization, or any architecture with non-trivial training-phase activity; high for institutions running scheduled model retraining; low for institutions using only externally-trained foundation models.

### F. DPDP Act §6 consent lifecycle as state

**The audit-room question.** *"For consent record C, what is its current lifecycle state across the 184,712 credit-decision entries that reference it — and if it transitions to withdrawn, which decisions need review?"*

**TesseraSeal.** §10.38 normates the consent-lifecycle binding. Each consent record produces an `audit.consent.given` entry with a unique consent ID, the legal basis (`dpdp_act_2023_§6`), the timestamp, the field officer, the device or branch. Every subsequent decision references the consent ID. Lifecycle transitions (`withdrawn`, `expired`) produce additional chain entries. The verifier follows the references and reports lifecycle state for any consent record at any point in time.

**Kognitos.** Field 4 (input data) carries the consent payload at capture. Field 6 (action) records the consent capture action. Field 8 (context) carries the legal basis. Field 11 (hash chain) carries integrity. The schema does not have a field for *lifecycle state* — there is no place to say "consent record C is currently in state X and decisions bound to it need review if it transitions to state Y."

**The under-reporting.** The chain captures the lifecycle (the institution's discipline is exemplary). The framework cannot read the lifecycle as state. The framework reports each entry as a discrete event; the lifecycle is implicit in the sequence and would need to be reconstructed by an analyst. Under the reference spec, lifecycle is a first-class queryable property; under Kognitos, it is at best a reconstruction.

**Speculation gap.** A DPDP grievance arrives. The Data Protection Board asks: "list all credit decisions bound to consent records currently in withdrawn state at the time of the grievance." Under Kognitos, the auditor must walk the chain entry-by-entry, identifying consent-given events, identifying consent-withdrawn events, and computing the lifecycle state at the grievance moment for each consent ID. The query is operationally expensive and structurally fragile.

**Structural reason for the gap.** Lifecycle-as-state requires a different shape of audit-trail vocabulary than discrete-event audit-trail capture. Privacy-regime compliance (GDPR, DPDP, CCPA) all share this requirement. Kognitos was designed against the discrete-event model.

**Honest assessment.** Severity: highest for institutions operating in DPDP, GDPR, or CCPA jurisdictions with consent-lifecycle obligations; high for institutions with any explicit consent-revocability requirement; low for institutions operating in jurisdictions without consent-lifecycle regulation.

### G. Federated-cycle structure invisibility

**The audit-room question.** *"The chain captures 30,000+ push/pull/verify/activate events per monthly federated cycle. Can the framework read those events as a cycle?"*

**TesseraSeal.** §10.33 normates model-update events as chain entries with explicit cycle structure: `audit.training.cycle_number`, `audit.training.gradient_contributor_count`, `audit.training.aggregation_method`. The cycle is a first-class queryable property. The verifier can resolve "show me all 30,000 events from cycle 4" and produce the deployment-phase boundary moments as a coherent sequence.

**Kognitos.** Field 7 (model id + version) reads each event's deployment state. Field 11 (hash chain) reads each event's integrity. The framework has no concept of cycle, no concept of cycle number, no concept of monthly cadence. Each event reads cleanly in isolation; the cycle structure that the events compose is invisible.

**Speculation gap.** An RBI inspector asks: "show me cycle 4's deployment timeline — when did the model artifact land at the aggregator, when did it propagate to each tablet, what was the activation latency distribution?" Under Kognitos the auditor walks 30,000+ individual chain entries and reconstructs the cycle from timestamps and model-version changes.

**Honest assessment.** Severity: medium for institutions running scheduled model-update cycles (federated, scheduled retraining, version-controlled deployment); low for institutions with continuous deployment; not applicable for institutions running only externally-sourced models.

### H. Manual override of model decision as paired chain entries

**The audit-room question.** *"Branch manager Mahesh Iyer overrode the 17% central recommendation to 19.5% on 2026-04-22. The chain records both the model decision and the override. Can the framework read the pairing — that the second entry is a manual override of the first?"*

**TesseraSeal.** Implicit support via `audit.decision.override_of_chain_ref`. The override entry carries an explicit reference to the prior model decision. Verifier follows the reference. The pairing is structural.

**Kognitos.** Field 10 (reasoning) carries the rationale. Field 2 carries the actor identity. Field 5 captures the override outcome. The framework reads each entry under all twelve fields but cannot read the pairing — the structural fact that the second entry is a manual override of the first.

**Speculation gap.** A regulator asks: "what proportion of credit decisions are overridden by branch-manager discretion, and what is the rate-delta distribution of overrides?" Under Kognitos the auditor scans for entries whose rationale string contains "override" — a fragile pattern that depends on engagement-specific knowledge of how the institution writes its rationales.

**Honest assessment.** Severity: medium for institutions where manual overrides are a material fraction of decisions (microfinance branch discretion; medical clinician override; trading-desk discretion); low for institutions where model decisions are routinely binding.

### I. The composed posture — framework + compensation

**The audit-room question.** *"If the framework is structurally narrower than the architecture, can the institution still maintain a defensible regulator-facing posture under the framework?"*

**TesseraSeal.** Implicit: the reference spec is structurally as wide as the architecture, so framework alone is sufficient. The institution's operational compensation is documentation rather than substitution.

**Kognitos.** Framework alone is *not* sufficient at Saraswati. The institution composes framework (twelve fields verified on central path) + four distinct operational compensation systems (key-management runbook; MLflow training-phase records; Confluence held-out test set documentation; parallel consent-lifecycle index). Each compensation system addresses a specific framework gap. The combined posture is defensible because each gap has an explicit compensation and each compensation lives in a system the regulator can independently verify.

**Honest assessment.** Severity: not a framework gap per se; it is a framework-pattern observation. The composed posture is acceptable when the institution maintains operational compensation that an inspector can independently verify. It is unacceptable when the institution relies on framework alone and the framework is structurally narrower than the architecture under audit.

---

## Summary table

| # | Area | TesseraSeal anchor | Kognitos anchor | Speculation gap | Material impact |
|---|---|---|---|---|---|
| A | Per-device session key derivation | §10.32 | Field 11 (scope-silent) | Inarticulability | Compromised-device containment invisible to framework |
| B | Edge-attestation primitive | §10.35 | No field | Inarticulability | §1.2 SDK-process-compromise residual compensation invisible |
| C | Late-arriving-entry seal | §10.36 | Field 11 (timing-silent) | Inarticulability | 14-15 hour integrity-claim asymmetry invisible |
| D | Hierarchical Merkle aggregation | §10.37 | Field 11 (structure-silent) | Inarticulability | Bandwidth-efficient verification path invisible |
| E | Training-phase integrity | §10.34 + §10.64 | Field 7 (production-silent) | Inarticulability | Gradient contributions, aggregation, validation invisible |
| F | DPDP §6 consent lifecycle as state | §10.38 | Fields 4/6/8/11 (lifecycle-silent) | Under-reporting | Lifecycle reconstruction required for grievance response |
| G | Federated-cycle structure | §10.33 | Fields 7/11 (cycle-silent) | Under-reporting | Cycle-level queries require manual reconstruction |
| H | Manual override pairing | `audit.decision.override_of_chain_ref` | Fields 2/5/10 (pairing-silent) | Framework-silent observation | Override-rate queries fragile under string matching |
| I | Composed posture (framework + compensation) | n/a (framework alone) | n/a (framework alone) | Pattern observation | Operational compensation independent verification required |

**Plus recurring from Chapters 01-12:** 17 comparison points unchanged.

**Total comparison points exercised in Chapter 13:** 26 (17 recurring + 9 new).

**Of which inarticulabilities: 5** (A through E).

**Of which under-reportings: 2** (F, G).

**Of which framework-silent observations: 1** (H).

**Of which pattern observations: 1** (I).

---

## Honest assessment — engagement-scoped

### What Saraswati uniquely contributes

The chapter is the program's first engagement where framework inarticulability outnumbers framework confirmation on the AI side. The ratio is 5-to-3 against the framework. Prior chapters had at most a 1-to-many ratio in favor of confirmation; Saraswati flips the ratio.

The chapter is also the program's first engagement where the institution's operational compensation across multiple distinct compensation systems is what closes the framework's gaps. Hill Country's confirmation posture (Ch12) closed clean on framework alone; Eberhardt × Lumière (Ch11) closed clean on framework alone with cross-organizational handover; Saraswati closes on framework + four compensation systems. The composed posture is the new operational pattern.

### Aparna Desai's on-the-record statement

> "The Kognitos audit-trail framework is acceptable as a baseline AI-audit-trail standard for the central inference path. It is not acceptable as a standalone framework for an institution that has to demonstrate DPDP Act §6 consent-lifecycle compliance. The framework's silence on lifecycle-as-state is not a minor gap — it is the structural reason my DPO function cannot rely on the framework alone to defend the institution before the Data Protection Board if a consent-revocation grievance arose. The institution will continue to capture the consent lifecycle in the chain. The institution will also continue to maintain a parallel consent-lifecycle index outside the chain, populated by the chain's lifecycle events, that the DPO function can query against. The parallel index is operational compensation for the framework's silence. The compensation is the institution's; the gap is the framework's. On the record."
>
> — Aparna Desai, Data Protection Officer, Saraswati Microfinance. Day 2, 14:42 IST.

The statement is Veronika-pattern (direct boundary-setting, regulator-readable, gap-naming, compensation-claiming). It is the cleanest direct-boundary-setting statement since Veronika at Atrio (Ch04). It restores the stakeholder explicit-attribution streak that broke at Ch12.

### Vikram Iyer's memo extension (not on-the-record but structurally significant)

Vikram drafted a three-page institutional memo extending Aparna's framework-gap claim to the RBI Master Direction 2024 update's AI-governance posture. The memo explicitly named the FFIEC chain-of-custody reference spec as the framework that would close the gaps structurally if adopted. The institution had not adopted the reference spec as of the engagement; the acknowledgment that the alternative existed was the honesty signal that would land with an RBI inspector.

The memo's three-page structure (scope + 7 inarticulabilities mapped to compensation matrix + RBI 2024 clause mapping) is the new template for framework-narrower-than-architecture engagement memos. The team will use the structure as a starting point if future chapters in the foresight cluster (Ch14-Ch17) produce similar patterns.

### Engagement-specific consequences

The institution closed the three-day pass at 12:00 IST Day 3 with all four stakeholder sign-offs (Rohit, Vikram, Neha, Aparna) and zero findings against the institution. The RBI Master Direction 2024 inspection lands in nine weeks; the institution's audit-readiness response will be the team's memo + the institutional compensation matrix + Aparna's on-the-record statement. The posture is defensible.

The institution will re-engage the audit team if a DPDP grievance surfaces between this engagement and the RBI inspection. Aparna explicitly conditioned her sign-off on this re-engagement provision.

The audit team's return flight to Boston via Doha departed at 22:35 IST Day 3.

---

*Program-level running tally and editorial signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
