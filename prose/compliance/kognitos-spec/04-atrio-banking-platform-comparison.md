# Comparative Analysis — Chapter 04 (Atrio Banking Platform)

*Side-by-side analysis of how the Kognitos 12-field framework and the TesseraSeal / FFIEC chain-of-custody v1.0b spec handle a **multi-tenant BaaS platform audit** read concurrently by five regulator audiences. Honest assessment of where, for the first time in the program, the framework's silence produces **under-reporting** — legitimate findings the reference spec catches and the framework cannot detect at all.*

---

## The new research signal — under-reporting vs. speculation

Chapters 01-03 established a consistent pattern: the framework's silences force the auditor to **speculate** — to invent anchors, file findings against field spirit rather than literal wording, write prose where the framework should have a primitive. Speculation is extra work the auditor does to compensate for the framework's brevity.

Chapter 04 introduces a different pattern: **under-reporting**. Under FFIEC v1.0b, the Atrio audit produces 21 confirmations + 1 Partial (§10.15 invariant-5 cache lag) + 1 Nit (§10.18 missing runbook cross-reference). Under Kognitos, the same audit produces 11 confirmations + 0 findings. **The two findings the reference spec catches are invisible to Kognitos because the framework has no field that could surface them.**

| | Speculation | Under-reporting |
|---|---|---|
| What happens | Auditor invents anchors to fill silences | Framework misses findings the reference spec catches |
| Where the cost lands | Auditor's prose burden grows | Audit deliverable is materially weaker than operational reality |
| Recovery path | Cover-memo prose, institution culture | Cover-memo cross-walk to reference spec, institution culture |
| Structural consequence | Convergence on operational outcome at culturally-mature institutions | **Findings can ship to regulators as zero-findings at any institution** |

**Under-reporting is structurally worse than speculation.** Speculation requires extra auditor labor; the work happens and the operational outcome converges at mature institutions. Under-reporting means findings vanish from the audit deliverable entirely. An institution operating under Kognitos as the sole framework — and without the internal discipline to catch issues that the framework can't articulate — could ship with the same Partial and Nit Atrio caught, and the audit deliverable would record zero findings against them.

This is the most consequential framework-side property surfaced in the program so far.

---

## Recurring from Chapters 01-03 (multi-tenant instances)

These play out the same way under Kognitos at platform scale. Severities unchanged.

| Recurring point | Earlier ref | Ch04 instance |
|---|---|---|
| Compositional security | Ch01 §4 | All twelve sponsor-bank chains |
| Coverage-boundary primitive | Ch02 §A | Single-zone here (full enterprise); pattern still applies to multi-tenant scoping |
| Reference-verifier distribution | Ch01 §12, Ch02-Ch03 | Five-examiner concurrent verification |
| Entity succession | Ch01 §11 | §10.24 operational at Cascadia acquisition |
| Training-data retention | Ch01 §10 | Not surfaced this engagement |
| Connector-source family | Ch01 §6 | Not surfaced this engagement (full enterprise; no SaaS-edge boundaries) |
| Verifier procedure-step granularity | Ch03 §B | Not exercised this engagement |
| Catwalk demo / field-condition verification | Ch01-Ch03 | Coordinated-examiner room is the platform-scale analog |
| Cross-vendor model-handover | Ch02 §K, Ch03 §H | Not exercised |

---

## New comparison points specific to Chapter 04

Ten distinct new comparison points emerged from this engagement.

---

### A. Multi-tenant IKM registry uniqueness (the structural hinge)

**The audit-room question.** *"Twelve sponsor banks share a platform. Each bank can have a `tenant_id='production'`. What prevents cross-bank collision from compromising cryptographic isolation?"*

**TesseraSeal.** §10.1 IKM registry uniqueness at the database layer: `(bank_id, tenant_id, ikm_version)` PRIMARY KEY plus UNIQUE INDEX plus 2024 CHECK constraints for empty-string rejection. Cross-bank `tenant_id='production'` is cryptographically safe because the IKMs differ — the HKDF tenant binding produces different per-event MAC keys. The §10.1 normative semantics map one-to-one against four adversarial-insert test cases (duplicate-within-bank reject, same-tenant-across-banks accept, empty-string reject, null reject). The structural hinge of the multi-tenant claim.

**Kognitos.** No field for multi-tenant IKM registry discipline. Field 12 (tamper-evident integrity proof) is satisfied per tenant; the framework does not address cross-tenant cryptographic isolation.

**Speculation gap.** Under Kognitos, an institution operating without §10.1's uniqueness constraint would satisfy the framework. If the platform had a tenant_id collision risk, an attacker could potentially craft a per-event MAC that validates under another tenant's key, compromising cryptographic isolation across the multi-tenant boundary. The framework would not detect the structural risk.

**Structural reason for the gap.** Kognitos's framework operates at the per-event row level. Multi-tenant isolation is a database-schema property that operates at the IKM-registry layer, not at the per-event row. The 12-field schema cannot articulate structural cryptographic-isolation properties without expanding into schema-genre artifacts.

**Honest assessment.** For institutions operating multi-tenant platforms (BaaS, SaaS-with-tenants, multi-customer audit-trail vendors), the IKM-registry-uniqueness property is the structural foundation. Atrio demonstrated it operationally through four adversarial inserts. Kognitos cannot detect whether the property is present. **Severity: highest for multi-tenant platforms; not applicable for single-tenant deployments.** New highest-severity point for this engagement class.

---

### B. Cross-tenant scope isolation enforced cryptographically (5×5 refusal matrix)

**The audit-room question.** *"An examiner with Indiana credentials should not be able to read Georgia's chain entries. How is the scope boundary enforced — by IAM convention or by cryptography?"*

**TesseraSeal.** §4.1.1 Model B HSM-resident PRK + §10.1 IKM registry uniqueness together enforce scope isolation cryptographically. Examiner credentials are scoped to specific `(bank_id, tenant_id)` pairs. The verifier's credential check at scope boundary is backed by the cryptographic impossibility of computing a valid MAC under a different bank's IKM.

**Kognitos.** No field for verifier-side scope enforcement. Field 3 (authenticated human identity) addresses the examiner's identity but not the scope enforcement mechanism.

**Speculation gap.** Under Kognitos, scope enforcement could be implemented at the IAM layer (a database role with row-level security) or at the cryptographic layer (the bank's pattern). The framework cannot distinguish. An institution operating IAM-only scope enforcement would pass; an examiner with sufficient credentials elevation could potentially bypass IAM and access cross-tenant data.

**Honest assessment.** For multi-tenant platforms with regulator audiences (BaaS, fintech infrastructure, healthcare clearinghouses), cryptographic scope enforcement is materially stronger than IAM convention. Atrio's 5×5 refusal matrix demonstrated 25 of 25 expected outcomes; the framework records this as Field 3 ✓ and Field 12 ✓ without articulating the cryptographic enforcement mechanism. **Severity: high for multi-tenant platforms.**

---

### C. Multi-implementation conformance bar (five examiners, byte-identical output)

**The audit-room question.** *"Five examiners are running independent verifier instances next door. The byte-identical-output property bounds examiner-to-examiner variance. How does the framework articulate this bound?"*

**TesseraSeal.** §10.26 distribution discipline produces a single reference-verifier binary distributed via Cosign-signed releases. Five examiners running the same binary against the same chain entries produce byte-identical output. Multi-implementation conformance is bounded by the reference implementation; a third party can write a competing verifier in another language, but the spec's test-vector corpus is the conformance harness.

**Kognitos.** No equivalent. The framework does not address examiner-tool conformance. Five examiners running five different verification tools could produce five different results and the framework would not normate convergence.

**Speculation gap.** Under Kognitos, an audit using multiple examiner tools has no framework-supplied bound on examiner-to-examiner variance. Cross-examiner disagreement is not detectable as a framework anomaly.

**Honest assessment.** For coordinated-examination cycles (FFIEC, multi-state, multi-regulator), examiner-tool conformance is operationally significant. The bank's reference spec gives the examiners convergence; the framework does not. **Severity: medium-high for coordinated examinations; not applicable for single-examiner engagements.**

---

### D. §10.15 multi-region invariants — framework under-reporting #1

**The audit-room question.** *"The `master.cross_region_replication_completed` event reads source-region count from a five-minute-stale cache. Chain and seal correctness intact; invariant 5 fails. How does the framework articulate this?"*

**TesseraSeal.** §10.15 Pattern A enumerates five normative invariants for multi-region active-active. Invariants 1-4 cover chain identity, reconciliation events, delta tracking, region failover. Invariant 5 covers the source-region count discipline — must be read from authoritative source at event time, not from a poll-cached value, for fast-cadence tenants. The invariant 5 violation is mechanically determinable; engagement-team discretion to downgrade is removed by the normative text.

**Kognitos.** No field for multi-region invariants. Field 12 (tamper-evident integrity proof) is satisfied because the chain itself is sound. The poll-cached count compromises a property the bank's reference spec normates and the framework does not articulate. **There is no Kognitos row to file this against.**

**The under-reporting.** Under FFIEC, Partial-001 with 60-day remediation ETA. Under Kognitos, the issue is invisible. An institution without internal discipline (Atrio caught it 6 weeks before the audit) would ship with this Partial silently present and the audit deliverable would record zero findings.

**Structural reason for the gap.** Multi-region invariants are spec-architecture properties that operate at the platform level. Kognitos's framework operates per-event. The genre boundary is real and not fixable inside the framework.

**Honest assessment.** For institutions operating multi-region active-active deployments, the §10.15 invariants are the cleanest articulation of the multi-region discipline available. Kognitos's framework cannot supply equivalent normative anchors. **Severity: high for multi-region platforms; the first instance of framework under-reporting in the program.**

---

### E. §10.18 runbook cross-referencing discipline — framework under-reporting #2

**The audit-room question.** *"The platform's runbook is missing a §10.1 cross-reference on the multi-tenant operations section. The §10.1 reference is load-bearing (it grounds the multi-tenant claim). Is this a Nit?"*

**TesseraSeal.** §10.18 normates: institution-side runbooks MUST cross-reference the spec sections their operational discipline implements. Missing cross-references on load-bearing structural controls are a Nit; missing on non-load-bearing controls are an observation. The bank's §10.1 reference is load-bearing.

**Kognitos.** No field for runbook cross-referencing discipline. The framework does not address runbook quality at all. Missing cross-references are invisible.

**The under-reporting.** Under FFIEC, Nit-001 with 30-minute remediation. Under Kognitos, the issue is invisible.

**Honest assessment.** Runbook quality is operationally significant for the institution's IR program and for examiner readability. The bank's reference spec normates the discipline; Kognitos does not. **Severity: medium for runbook quality; second instance of framework under-reporting.**

---

### F. Streaming cadence (§10.27/28/29)

**The audit-room question.** *"Three high-volume fintechs run on streaming MAC instead of daily Merkle. How does the framework articulate the cadence choice?"*

**TesseraSeal.** §10.27 streaming cadence, §10.28 streaming IKM rotation, §10.29 streaming verifier procedure together define the streaming-mode operation. The verifier dispatches on cadence — daily Merkle path vs. streaming path — and produces appropriate verification under each. Streaming cadence is a per-tenant property.

**Kognitos.** No field for cadence. Field 12 (tamper-evident integrity proof) is satisfied regardless of whether the cadence is streaming, daily, hourly, or weekly. An implementation running on weekly cadence and one on streaming both satisfy Field 12.

**Speculation gap.** Under Kognitos, the auditor cannot record cadence choice. An institution running streaming cadence (which is more demanding cryptographically) is invisible; an institution running weekly cadence (which is operationally weaker for fast-evolving threats) is also invisible.

**Honest assessment.** For high-volume institutions where streaming cadence is operative, the discipline is material. The framework cannot articulate the cadence; the institution must document the choice independently. **Severity: medium-high for high-volume institutions; not applicable for slow-cadence deployments.**

---

### G. GPU-fleet attestation (§10.65)

**The audit-room question.** *"The platform runs fraud / credit / AML inference on hyperscale GPU pools. Each pool attests to hardware identity at job-allocation time. How does the framework articulate this?"*

**TesseraSeal.** §10.65 hyperscale GPU-fleet attestation: each inference pool attests to its hardware identity at job-allocation time; attestation events are chain-captured. The hardware-attestation provenance feeds into Field 5 (model identity and version) at the inference time.

**Kognitos.** No field for hardware attestation. Field 5 (model identity) records the model but not the hardware substrate.

**Speculation gap.** Under Kognitos, an institution operating GPU-fleet attestation and one operating "trust the cloud provider" satisfy Field 5 identically. The hardware-provenance discipline is invisible.

**Honest assessment.** For institutions running inference on shared GPU infrastructure (most large-scale AI deployments today), hardware attestation is the foundation for model-supply-chain integrity. The framework cannot detect whether attestation is present. **Severity: medium for hyperscale GPU consumers.**

---

### H. §1033 per-customer audit-trail subset disclosure (§10.69)

**The audit-room question.** *"CFPB §1033 gives customers the right to request their own audit-trail subset. The platform produces this per-customer disclosure via §10.69. How does the framework articulate the disclosure protocol?"*

**TesseraSeal.** §10.69 per-customer audit-trail subset disclosure uses §10.23 Shape 2 daily `consumer_index.attestation` events as the integrity anchor. A customer can request their subset; the institution produces it with the consumer-index attestation as proof that the subset is the complete and unmodified audit trail relevant to that customer.

**Kognitos.** No field for consumer-disclosure protocols. Field 6 (inputs with source attribution) covers the per-event source but not the customer-disclosure procedure.

**Speculation gap.** Under Kognitos, an institution receiving a §1033 request has no framework-supplied disclosure procedure. The institution either invents one or borrows from another framework.

**Honest assessment.** For consumer-financial-data institutions under CFPB §1033, the disclosure protocol is operationally required. The bank's reference spec gives them the protocol; Kognitos does not. **Severity: medium-high for consumer-financial institutions.**

---

### I. Verification cost / batch feasibility at platform scale

**The audit-room question.** *"The platform runs a 1,410-run nightly verifier batch (47 fintechs × 30 days) in 86 seconds wall clock. How does the framework articulate operational feasibility?"*

**TesseraSeal.** Verification cost is implicit in §7 (12-step procedure) and §10.26 (reference verifier distribution). The procedure's complexity is sub-linear in chain size; batch verification at platform scale is operationally feasible. No specific section, but the property emerges from the spec's design choices.

**Kognitos.** No field for operational feasibility, batch cost, or verification time.

**Speculation gap.** Under Kognitos, an institution running nightly verification and one running quarterly verification satisfy Field 12 identically. The cadence of verification is not specified.

**Honest assessment.** For institutions operating IR programs against the audit trail, nightly verification is the cadence that supports next-day issue identification. Without it, issues can lurk in the chain for months. The framework cannot articulate the verification cadence. **Severity: medium for institutions running IR programs.**

---

### J. §10.24 entity-succession at platform scale (recurring + new instance)

**The audit-room question.** *"Atrio absorbed Cascadia Banking Tech 18 months ago. The acquisition included IKM registry merger and key custody transfer. How does the framework articulate this?"*

**TesseraSeal.** §10.24 entity-succession: documented procedure for chain history transfer across M&A boundaries. The acquisition event is a chain entry with attestation hashes from both pre- and post-acquisition HSM partitions.

**Kognitos.** No field for entity succession (recurring from Chapter 01 §11).

**Honest assessment.** Same severity as Chapter 01 §11. The new instance is that this is the first chapter where §10.24 was operationally exercised (rather than theoretically considered). The discipline produced four sealed chain entries with the §10.24 attribute family during the acquisition. **Severity: medium.**

---

## Summary table — Chapter 04 new comparison points

| # | Area | TesseraSeal anchor | Kognitos anchor | Speculation gap | Material impact |
|---|---|---|---|---|---|
| A | Multi-tenant IKM registry uniqueness | §10.1 | No field | **Highest (multi-tenant)** | Cross-tenant collision risk invisible |
| B | Cross-tenant scope isolation cryptographic | §4.1.1 + §10.1 | Field 3 + 12 generic | High (multi-tenant) | IAM convention vs cryptography indistinguishable |
| C | Multi-implementation conformance bar | §10.26 | No equivalent | Medium-High | Examiner-to-examiner variance unbounded |
| D | **§10.15 multi-region invariants — under-reporting** | §10.15 | No field | **Under-reporting** | Legitimate Partial invisible to framework |
| E | **§10.18 runbook cross-referencing — under-reporting** | §10.18 | No field | **Under-reporting** | Legitimate Nit invisible to framework |
| F | Streaming cadence | §10.27/28/29 | No field | Medium-High | Cadence choice invisible |
| G | GPU-fleet attestation | §10.65 | No field | Medium | Hardware attestation invisible |
| H | §1033 per-customer disclosure | §10.69 | No field | Medium-High | Consumer disclosure protocol missing |
| I | Verification cost / feasibility at scale | Implicit in §7 + §10.26 | No field | Medium | Verification cadence not specified |
| J | §10.24 entity-succession at platform scale | §10.24 | No field | Medium | Recurring |

**Plus recurring from Chapters 01-03:** 8 comparison points (multi-tenant instances of compositional security, multi-implementation conformance, etc.).

**Total comparison points exercised in Chapter 04:** 18.

**Of which under-reportings: 2 (new category).**

---

## Honest assessment — Chapter 04's distinct contribution

### The framework can be cleaner than the operational reality

This is Chapter 04's distinctive research signal. Under the bank's reference spec, the Atrio audit produces 21 confirmations + 1 Partial + 1 Nit. Under Kognitos, the same audit produces 11 confirmations + 0 findings. **The Kognitos report is cleaner than the operational reality, not because the bank is more compliant under Kognitos but because the framework can't see what the reference spec sees.**

An institution shipping a Kognitos-only audit deliverable to regulators would present zero findings against a system that has two outstanding remediation items. Atrio's culture caught both internally; the framework would not have caught either.

### What this changes about the program-level argument

Chapters 01-03 framed the framework's limits as **shallowness** — the auditor speculates to fill silences; institution culture covers the operational outcome. Chapter 04 introduces **under-reporting** — the framework's silences cause findings to vanish from the audit deliverable entirely, not just from the auditor's working notes. Institution culture can catch the findings internally, but the audit deliverable still reads as zero findings.

For institutions where the audit deliverable is the artifact that goes to regulators (almost all engagements involving examiners), this distinction matters. The deliverable's findings-count is what's read. Under-reporting compresses the findings-count below the operational reality.

### The Atrio CISO's on-the-record statement

Veronika requested on-the-record attribution in the cover memo: "The 12-field framework is acceptable as a vendor-facing summary. It is not acceptable as the only assessment artifact for a multi-tenant BaaS platform." That's the cleanest stakeholder statement of the framework's limits surfaced in any chapter so far. It's also the model for how institutions can document the framework's limits without claiming the framework is wrong.

### Running speculation tally

- Chapter 01: 14 speculation anchors
- Chapter 02: 12 new (26 total)
- Chapter 03: 8 new (34 total)
- Chapter 04: 9 new framework silences + **2 framework under-reportings** (43 silences total; 2 under-reportings)

Four chapters in, the framework has produced 43 speculation points and 2 under-reportings. The under-reporting category is new and structurally consequential — the audit deliverable's findings count diverges from the reference spec's findings count by 2.

### What this signals for chapters 05-22

The under-reporting category is likely to recur in any engagement where the bank's reference spec catches findings that the framework's 12 rows cannot articulate. Multi-region deployments will produce §10.15 under-reportings. Platforms with mature runbook discipline will produce §10.18 under-reportings. Engagements with streaming cadence, GPU attestation, §1033 disclosure, or multi-tenant scope will produce structural-silence under-reportings.

The program-level honest signal at the end of Chapter 22 will likely be: a count of how many distinct under-reportings the framework produces across 22 representative scenarios. That count, alongside the speculation-anchor count, will give regulators and audit firms a defensible measure of where Kognitos is adequate as the sole framework and where it should be paired with a more rigorous reference spec.
