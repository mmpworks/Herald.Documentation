# Comparative Analysis — Chapter 08 (NetiVa Intelligence Ltd.)

*Side-by-side analysis of how the Kognitos 12-field framework and the TesseraSeal / FFIEC chain-of-custody v1.0b spec handle a **multi-tenant AI-vendor evaluation under nation-state threat model with a deliverable consented across three regulator audiences (OCC examiner downstream + Bank of Israel/ISA + INCD coordination)**. Honest assessment of where the framework's coverage gap moves from non-AI-decision zones into the cryptographic substrate itself.*

---

## New research signal

Chapter 08 sharpens the inarticulability category and introduces a new structural observation on framework evolution.

| New signal | Earlier reference | What is new in Chapter 08 |
|---|---|---|
| **Inarticulability shifts to substrate** | Ch03 §1.2; Ch06 public-safety §1.2; Ch07 civil-rights §1.2 | The 4th inarticulability is on §1.4 compositional security — the cryptographic substrate that gives Field 12 its meaning. Field 12 records that a proof exists; it cannot articulate why the proof holds. This is the first inarticulability where the gap is *underneath* every other field, not in a peripheral zone. |
| **Framework cannot grow from findings** | First instance in program | The reference spec has a change-log mechanism; §10.17 enters the normative text *because* this engagement surfaced a gap that prior text could not articulate. Kognitos's twelve fields are fixed. The audit team in the room can file a finding that names the absence — they cannot file a finding that grows the framework to cover it. This is a meta-property of the framework itself. |
| **Three-regulator deliverable cost** | Ch07 multi-regulator (5 frameworks) | Ch07's multi-regulator partitioning was *within* one institution's regulator stack. Ch08 introduces *cost-shared, cross-institutional* deliverable consent across three regulator audiences (OCC, Bank of Israel + ISA, INCD coordination). Framework silences are 3x as expensive because three regulators read the same deliverable. |

This chapter's central novelty: the framework gap is no longer about what the framework misses at the edges (litigation defense, public safety, civil rights). The gap is about what the framework misses at the foundation.

---

## Recurring from earlier chapters

| Recurring point | Earlier ref | Ch 08 instance |
|---|---|---|
| Compositional security | Ch01 §4 | §1.4 substrate now load-bearing on nation-state threat model — see new point C below for the deeper inarticulability |
| Field 11 (human review) thin reading | Ch01 | Eligible AML cases below human-review threshold; Field 11 marked "none" for this entry, true to spec |
| Field 12 single-slot for HMAC + Merkle + HSM | Ch01-07 | Now demonstrably collapses three independently-keyed mechanisms into one row |
| §10.16 four-number lag-bound discipline | Ch04, Ch06, Ch07 | Salesforce mirror: median 12s, p95 SLO 60s, alert 90s, RTO 5min. Third recurring instance. Stable pattern. |
| §4.4.6 connector_source attribution | Ch04, Ch06, Ch07 | Salesforce CRM mirror as SaaS-edge connector. Field 6 carries the source name; the temporal envelope around the source has no slot. |
| §1.2 (a)-(e) epistemic scope | Ch03, Ch06, Ch07 | Touched at threat-model exchange but not centerpiece this chapter |
| Operational-property invisibility | Ch01-07 | New shape: HSM custody under nation-state threat, ceremony attendance, framework-evolution mechanism |
| Stakeholder explicit attribution | Ch04, Ch05, Ch06, Ch07 | Pankaj Iyengar — fourth stakeholder statement; first one *recommending a framework substitution* for an engagement class |
| Operational-events as chain-carried | Ch04, Ch06 | §10.2 catalog: `chain.verification_failure`, `seal.job_*`, `master_key.rotation_observed`, `master.cross_region_replication_completed`, `connector.lag_observation`, `connector.outage`. No Kognitos representation. |
| §10.25 run-resume + tail acquisition | Ch06 PCP DR rejoin | April 30 NaN incident: 11 entries replayed under in-memory tail acquisition with ledger ingestion cross-check on `(prev_hash, seq)` monotonicity |
| §10.3 append-only enforcement | Ch01, Ch07 | Originals + replays both retained; application + database-role layer enforcement |
| §4.1 HMAC + HKDF tenant binding | Ch01 | New depth: same `tenant_id` value across two customer-banks is cryptographically distinct because IKMs differ. Reference spec catches; framework records identical strings. |

**Severities unchanged.** Recurring points carry the same severity assessment as their prior appearances.

---

## New comparison points specific to Chapter 08

### A. Multi-tenant cryptographic isolation by per-bank IKM

**The audit-room question.** *"Same `tenant_id` value across two different customer-banks. How does Kognitos articulate that these two entries are cryptographically isolated?"*

**TesseraSeal.** Reference spec §10.1 (IKM-registry uniqueness on `(bank_id, tenant_id)`) combined with §4.1 HMAC keyed under HKDF with per-bank IKM produces cryptographically distinct chain entries for the same `tenant_id` string. The isolation is structural — the IKMs differ; HKDF binding makes the resulting MACs incomparable across banks. Adversarial inserts confirm: within-bank duplicate rejected; cross-bank accepted; short identifier rejected on §3 character class.

**Kognitos.** Field 4 carries AI-system identity. Field 6 carries inputs with source attribution. Neither field carries the *cryptographic-isolation domain*. Two entries with the same `tenant_id` string would be read by the framework as related entries.

**The under-reporting.** Reference spec catches the cross-bank isolation as a structural property; Kognitos collapses two cryptographically-distinct entries into apparent string-identity. For multi-tenant SaaS vendor evaluation, this is the property that justifies the tenancy model.

**Speculation gap.** An auditor walking 23 customer-banks under Kognitos has to carry the per-bank IKM context in a prose footnote, not a structured attribute. The cover memo can say "tenant separation enforced by per-bank IKM under HKDF binding" — but that is a footnote, not a field.

**Structural reason for the gap.** Kognitos was designed for single-tenant or shallow-multi-tenant AI-decision logging. The cryptographic-isolation domain assumes a substrate the framework does not model.

**Honest assessment.** Severity: medium-high for any multi-tenant SaaS vendor evaluation. Severity: highest for nation-state-threat-class vendors where isolation properties are the central security argument.

---

### B. §1.4 compositional security argument — substrate inarticulability

**The audit-room question.** *"Where does the three-layer compositional argument file in Kognitos?"*

**TesseraSeal.** Reference spec §1.4 names three independent layers: per-event HMAC (§4.1, EUF-CMA), daily Merkle seal (§4.2, second-preimage), HSM signature on seal (§4.3, EUF-CMA). The composite security is 128 bits under NIST SP 800-175B (§1.3). The argument is that compromise of any single layer does not compromise the chain — write privilege on the chain table does not allow forging a Merkle root that resolves; forging the seal does not allow forging the HSM signature on it. Each layer carries an independent threat model and an independent key.

**Kognitos.** Field 12 carries "tamper-evident integrity proof." One slot. The slot does not articulate that the proof composes from three mechanisms, nor that each mechanism is independently keyed, nor that the composition reaches 128 bits under named NIST guidance.

**Inarticulability gap.** No field, under any reading, can be made to carry the compositional argument. Field 12 says the proof exists. The framework's vocabulary has no slot for *why* the proof should be trusted.

**Speculation gap.** An auditor under Kognitos who is asked about substrate trust (by an INCD liaison, a CISO, an OCC examiner) has to deliver the answer in prose attached to a Field 12 row that records "yes, proof exists."

**Structural reason for the gap.** Kognitos's framework was authored at the layer of AI-decision recording. Substrate is assumed. The three-layer composition is a property of the *implementation* of an integrity proof, not the recording of one — and the framework records only the recording.

**Honest assessment.** Severity: highest for any engagement where cryptographic substrate is load-bearing (nation-state threat, regulated multi-tenant, HSM custody). Severity: medium for routine single-tenant AI decision logging where the substrate is delegated to vendor implementation.

---

### C. HSM partition-ceremony attestation — the engagement that produced spec text

**The audit-room question.** *"Where is the partition-ceremony attendance record bound to the chain?"*

**TesseraSeal.** Reference spec, *post-engagement*, adds §10.17 with the change-log naming this audit as the source: a `chain.partition_ceremony_attended` event carrying `attendance_pdf_sha256` and RECOMMENDED `hsm_attestation_token_b64`. Before this engagement, the spec had §10.5 (FIPS 140-2 Level 3) and §10.6.1 (HSM-internal CSPRNG) on HSM custody but no chain-coupled ceremony record. The Partial filed here became normative text.

**Kognitos.** No field, before or after, can absorb the finding. The framework's twelve fields are fixed. There is no mechanism for an audit to grow the framework.

**Inarticulability gap.** The HSM ceremony attendance is not an AI decision. It is an operational substrate event. Kognitos has no operational-events vocabulary (see point E below).

**Speculation gap.** The auditor can record "ceremony attended" in a prose footnote. The chain-coupled cryptographic binding (PDF hash + HSM attestation token) is invisible to the framework's field shape.

**Structural reason for the gap.** This is the meta-observation: the reference spec absorbs findings into the normative text through a change-log mechanism. Kognitos's twelve-field schema is a fixed catalog, not a living standard. An auditor under Kognitos can record an absence; an auditor under reference spec can produce a section.

**Honest assessment.** Severity: highest for any engagement where the spec needs to grow from findings. Material consequence: the customer-bank's renewal posture in this engagement landed on a Partial that became normative spec text within 60 days; under Kognitos, the same Partial would have remained an unfilable observation.

---

### D. Nation-state threat model + INCD coordination

**The audit-room question.** *"What does your framework say about HSM custody under nation-state threat?"* (Tamar Levanon, INCD banking-sector liaison, unannounced)

**TesseraSeal.** Reference spec §10.5 (FIPS 140-2 Level 3) + §10.6.1 (HSM-internal CSPRNG declared as `rng_source = "hsm.thales-luna-7000"`) + EAL4+ Common Criteria elevation above the spec floor + INCD-coordinated 18-month-dwell threat assumption documented in CC8.1 residual-risk acceptance. The spec articulates substrate against named threat models.

**Kognitos.** Field 4 (AI system identity) and Field 12 (integrity proof). Neither field has a slot for HSM custody, key-generation source, threat-model elevation above conformance floor, or coordination with a national cyber directorate.

**Speculation gap.** The auditor delivering a framework-scoped answer to "what does the framework say about HSM custody under nation-state threat" can only answer: "the framework records that a proof exists; the framework has no field for the custody of the key that signs the proof." That is an honest answer. It is not what INCD asked for.

**Structural reason for the gap.** Nation-state threat assumes adversary capability that exceeds the threat model implicit in Kognitos's framework design. The framework was authored for AI-decision integrity, not adversarial-custody articulation.

**Honest assessment.** Severity: highest for any vendor evaluation at a nation-state threat assumption. Pankaj Iyengar's on-the-record recommendation (see honest assessment section below) names framework substitution for this engagement class.

---

### E. §10.2 operational-events catalog has no Kognitos representation

**The audit-room question.** *"Three Bank of Israel directives engaged on one bug. Where does the operational-events sequence file?"*

**TesseraSeal.** Reference spec §10.2 enumerates the operational-events catalog as first-class chain entries: `chain.verification_failure`, `seal.job_started`, `seal.job_completed`, `master_key.rotation_observed`, `master.cross_region_replication_completed`, `connector.lag_observation`, `connector.outage`, `chain.coverage_map_published`. An examiner can correlate any incident timeline against the chain's own operational signal.

**Kognitos.** No field. The framework's twelve fields are designed for AI-decision entries; operational events are not decisions, do not have authenticated user identities, do not have model identities, do not have reasoning. The schema does not fit.

**The under-reporting.** Reference spec carries the April 30 NaN incident as a chain-observable sequence: `chain.verification_failure` at 09:47 → seal job adjustment → run-resume replay under §10.25 → ledger ingestion cross-check. Kognitos can record the eleven replayed AI-decision entries; it cannot record the operational events that surrounded them.

**Speculation gap.** Three Bank of Israel directives (411 §3 16-minute filing, 365 §3 2-hour first-restore, 367 §4 cloud-and-AI logging) all engaged on a single bug. The chain itself is the witness that the directives were satisfied. Under Kognitos, the witness has to be reconstructed from external records (incident-management system, SRE on-call log, separate audit-trail database).

**Structural reason for the gap.** Operational substrate is not AI decisions. The framework's design center is the decision; the operational substrate sits below the design center.

**Honest assessment.** Severity: high for any regulated-vendor engagement where operational-events are first-class chain entries in the implementation. Severity: highest where multiple regulator directives engage on a single incident.

---

### F. Three-regulator deliverable: cost of framework silence is 3x

**The audit-room question.** *"The deliverable lands across three regulator audiences. Which framework lets us answer all three?"*

**TesseraSeal.** Reference spec is read by OCC IT examiners (US side), Bank of Israel + ISA (Israeli supervisory side), and INCD (national-threat-model coordination side). The reference spec carries vocabulary that all three audiences recognize: HSM custody (§10.5 / §10.6.1), multi-region invariants (§10.15), operational events (§10.2), partition-ceremony attestation (§10.17). One deliverable, three audiences, one vocabulary.

**Kognitos.** Twelve fields. Cross-vendor comparability is the framework's strength on the customer-bank side. The three audiences each ask substrate questions Kognitos cannot answer. The customer-bank carries the framework's gap into three regulator briefings.

**Speculation gap.** Pankaj Iyengar would have to brief OCC on Kognitos vs reference spec; brief Bank of Israel on Kognitos vs Directive 411/365/367; brief INCD coordination on Kognitos vs nation-state-threat-model articulation. Three briefings, three explanations of what the framework cannot carry.

**Structural reason for the gap.** Cross-vendor comparability and cross-regulator vocabulary are different design goals. Kognitos optimized for the first. Reference spec optimized for the second.

**Honest assessment.** Severity: highest for any vendor evaluation with multi-regulator consent. Material consequence: Pankaj's on-the-record statement names this directly — Kognitos retained only as cross-vendor comparison summary, reference spec for the deliverable substance.

---

### G. Cross-language CC8.1 discoverability — the Hebrew runbook

**The audit-room question.** *"The customer-bank-facing distribution has an English README. The internal-ops runbook is Hebrew-only. Where does cross-language discoverability file?"*

**TesseraSeal.** Reference spec §10.18 (CC8.1 and runbook cross-referencing) + post-engagement §10.17 (cross-language CC8.1 discoverability clause). The vendor's external README in English; the operational runbook must be cross-referenced in a language the customer-bank's CC8.1 reader can follow. Closes in ~4 hours of translation work.

**Kognitos.** Field 7 (policy/prompt invoked) carries policy versioning. It does not carry operational-runbook discoverability. Field 7 is the wrong slot.

**Speculation gap.** The auditor noting Hebrew-only runbook has to file the finding as a prose Nit attached to the cover memo. The framework has no structural slot for the discoverability shape.

**Structural reason for the gap.** Operational runbooks are runbook artifacts, not policy artifacts. CC8.1 discoverability is a property of the runbook's cross-referencing, not its content. Kognitos does not model runbook artifacts.

**Honest assessment.** Severity: low-medium per individual instance; severity: medium when multi-regulator audiences read the same runbook. Closed against reference spec §10.18 + post-engagement §10.17 jointly in this engagement.

---

### H. HSM-internal CSPRNG declared in attestation

**The audit-room question.** *"What CSPRNG generated the IKM?"*

**TesseraSeal.** Reference spec §10.6.1: HSM-internal CSPRNG with `rng_source = "hsm.thales-luna-7000"` declared on the IKM. §10.5 elevates with FIPS 140-2 Level 3 + EAL4+ for INCD threat model. The CSPRNG source is part of the IKM registry attestation; the verifier configuration carries the key fingerprint that anchors trust in the source declaration.

**Kognitos.** No field. Key-generation source is not an AI decision. Field 12 records that an integrity proof exists; the framework does not articulate which RNG seeded the integrity proof's foundation.

**Inarticulability gap.** No field, under any reading. The CSPRNG source attribute is structurally invisible to the framework.

**Speculation gap.** Under nation-state threat assumption, an auditor's answer to "what RNG generated the key?" is critical. Under Kognitos, the answer has to be carried in prose attached to a Field 12 row.

**Structural reason for the gap.** The framework was designed at the layer of decision-recording, not substrate-attestation. The CSPRNG is substrate. The substrate is not modeled.

**Honest assessment.** Severity: highest for nation-state-threat-class engagements. Severity: medium for routine engagements where vendor implementation choice is trusted.

---

### I. §10.22 pre-MAC SDK redaction co-satisfying PPL Amendment 13 + GDPR 5(1)(c)

**The audit-room question.** *"Sensitive Israeli-resident data flows through US-region inference. What does the framework say about pre-MAC redaction?"*

**TesseraSeal.** Reference spec §10.22 (pre-MAC SDK redaction): redactions applied before HMAC computation, with redaction-disposition recorded in the entry. Co-satisfies PPL Amendment 13 (Israeli sensitive-information classification) and GDPR Article 5(1)(c) (data minimization) on the same redaction path. One mechanism, two regulatory satisfactions.

**Kognitos.** Field 6 (inputs with source attribution) and Field 8 (reasoning). Neither field carries pre-MAC redaction discipline. The redaction itself does not appear as a structural property of the chain entry — only the redacted output does.

**Speculation gap.** The auditor recording PPL 13 + GDPR 5(1)(c) co-satisfaction has to carry the pre-MAC redaction discipline in a prose footnote. The chain entry under Kognitos shows the redacted value; it does not show that the redaction happened before MAC computation, which is the property that closes both regulators jointly.

**Structural reason for the gap.** Pre-MAC redaction is a chain-mechanism property; Kognitos's twelve fields are entry-content properties. Different layers.

**Honest assessment.** Severity: high for any engagement crossing two privacy-regulation regimes. Severity: medium for single-jurisdiction engagements.

---

## Summary table

| # | Area | TesseraSeal anchor | Kognitos anchor | Speculation gap | Material impact |
|---|---|---|---|---|---|
| A | Cross-bank cryptographic isolation | §10.1 + §4.1 HKDF | No field | Under-reporting | Multi-tenant SaaS isolation argument invisible |
| B | §1.4 compositional security on substrate | §1.4 + §1.3 NIST SP 800-175B | Field 12 (collapses to single slot) | Inarticulability (highest) | Substrate trust argument cannot be filed |
| C | HSM partition-ceremony attestation | §10.17 (post-engagement) + §10.5/§10.6.1 | No field; framework cannot grow | Inarticulability (meta) | Spec absorbs finding; framework cannot |
| D | Nation-state threat + INCD coordination | §10.5 + §10.6.1 + EAL4+ + CC8.1 residual-risk | Field 4 + Field 12 inadequate | Speculation (highest) | Three-regulator audience can't be answered |
| E | §10.2 operational-events catalog | §10.2 + §10.25 + §10.3 | No field | Under-reporting (high) | Incident chain trail not representable |
| F | Three-regulator deliverable cost | Reference spec vocabulary shared across audiences | Cross-vendor comparability ≠ cross-regulator vocabulary | Speculation (highest) | Pankaj's framework-substitution recommendation |
| G | Cross-language CC8.1 discoverability | §10.18 + post-engagement §10.17 clause | Field 7 wrong slot | Under-reporting (medium) | Runbook artifact has no framework slot |
| H | HSM CSPRNG source declaration | §10.6.1 + §10.5 | No field | Inarticulability | Nation-state threat substrate question unanswerable |
| I | §10.22 pre-MAC SDK redaction | §10.22 + PPL 13 + GDPR 5(1)(c) | Field 6/8 entry-content only | Under-reporting | Cross-regulation co-satisfaction invisible |

**Plus recurring from Chapters 01-07:** 18 comparison points unchanged.

**Total comparison points exercised in Chapter 08:** 27 (9 new + 18 recurring).

**Of which inarticulabilities (new this chapter):** 1 (point B — §1.4 substrate; plus meta-shape in C and H).

**Of which under-reportings (new this chapter):** 2 (point A — cross-bank isolation; point E — operational-events catalog).

---

## Honest assessment — engagement-scoped only

### What NetiVa uniquely contributes

The vendor-evaluation engagement class breaks new ground in three ways. First, the audit team is at a vendor instead of a bank, which shifts the framework's domain pressure: the framework was authored for AI-decision recording on a single institution's behalf; here the same framework has to evaluate substrate properties that 23 customer-banks depend on. Second, the deliverable lands across three regulator audiences with cost-shared consent, which triples the cost of every framework silence. Third, the engagement is the first one in the program where the framework gap is on the cryptographic substrate itself — §1.4 compositional security, §10.1 isolation, §10.6.1 CSPRNG source — rather than at the framework's edges.

### The framework-cannot-grow observation

The HSM partition-ceremony Partial is structurally important. Under reference-spec governance, the Partial became §10.17 normative text within 60 days. Under Kognitos, the same Partial has no closure path — the framework cannot absorb the finding. This is the first chapter where the audit produced a normative spec section *by being run*. The reference spec is a living standard; the Kognitos schema is a fixed catalog. The structural difference is the difference between a framework that improves under audit pressure and a framework that records absences under audit pressure.

### Stakeholder statement: Pankaj Iyengar — framework substitution recommendation

> *I came here as a customer-bank vendor-management lead with a $180B institution and a Tier-1 vendor and a renewal cycle and a binder full of OCC expectations. I have heard the audit team walk this engagement under the Kognitos framework with care and discipline. I have also heard, in their running notes, what the framework cannot carry. The vendor we are evaluating runs at a nation-state threat assumption. The vendor we are evaluating handles 23 customer-banks under per-bank cryptographic isolation. The vendor we are evaluating has a partition-ceremony record that, under proper governance, becomes a new clause in the normative spec by the end of next quarter. None of those properties have a slot in the framework on the audit-deliverable cover.*
>
> *I will be returning to my committee on Monday. I will be naming, in the cover memo, that the framework I chose for cross-vendor comparability did not carry the engagement's most important findings. I will recommend that future evaluations of this vendor — and of any vendor that operates at a nation-state threat model — be delivered against the reference specification, with Kognitos retained only for the cross-vendor comparison summary table. The audit team's running notes will be the record of what the framework missed. I want that recommendation, and the team's discipline in surfacing it, on the record.*

This is the fourth on-the-record stakeholder statement in the program. It is the first one that names a *future framework substitution*. Prior statements (Veronika, Helmstad, Soren) named explicit attribution of framework selection. Pankaj's statement names a class-of-engagement (nation-state-threat-class vendor evaluation) for which the framework should be replaced rather than annotated.

### Engagement-specific consequences

For NetiVa: the Partial closes-by-spec at §10.17 within 60 days; the Nit closes against §10.18 within 4 hours; twenty Confirmations on the reference side; one normative spec section produced.

For Pankaj's customer-bank: the vendor renewal supports a 30-day-notice OCC-acceptable framing because the chain is a property of data the bank has already received, not a service the vendor renders. The framework-substitution recommendation goes to the vendor-management committee Monday.

For Bank of Israel + ISA: the redacted deliverable arrives within the Israeli supervisory cycle. The §10.17 amendment, when it lands in the next quarter's spec revision, will be cited in supervisory letters.

For INCD: Tamar Levanon will return tomorrow morning at 9. The 18-month-dwell threat-model coordination will continue.

---

*Program-level running tally and editorial signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
