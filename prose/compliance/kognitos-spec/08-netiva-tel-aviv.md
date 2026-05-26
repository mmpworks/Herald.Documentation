# 08 — NetiVa Intelligence Ltd. (Kognitos-lens)

*An engagement where the audit team is at a vendor instead of a bank, the deliverable lands across three regulator audiences, and a nation-state cyber directorate walks in unannounced — forcing the framework to articulate cryptographic substrate it cannot articulate.*

**Engagement:** Independent vendor-management evaluation commissioned by a $180B US OCC-regulated regional bank, cost-shared with the Israeli AI vendor, deliverable consented for Bank of Israel (Pikuach HaBankim — Directives 357 / 359 / 361 / 365 / 367 / 411 / 414) and Israeli Securities Authority — Day 1 of a 3-day on-site visit
**Client:** NetiVa Intelligence Ltd., Tel Aviv — 14 months in production across 23 Tier-1 customer-banks (US, UK, Singapore, Israel, Australia); ~110 tenants under per-bank IKMs in dedicated FIPS 140-2 Level 3 partitions; two Israeli regions under §10.15 Pattern A
**Status:** Chain instrumentation across all 23 customer-banks; HSM partitions on twelve PCIe Luna 7000s at a colocation facility split across two Israeli regions; 2-of-2 PIN split per partition between customer-bank CISO and NetiVa CISO at onboarding; INCD-coordinated 18-month-dwell threat assumption
**Audit team lead:** Dawn
**Client liaisons:** Ayelet Shoham (NetiVa CTO); Yoel Stern (NetiVa CISO); Reut Bercovici (NetiVa Chief Product Officer); Pankaj Iyengar (US customer-bank vendor-management lead — on-site for Day 1); Tamar Levanon (INCD banking-sector liaison — arrives unannounced at 11:00)

**Audit team's framework:** Kognitos's 12-field schema. The team is now eight engagements in. This is the first chapter where the team is at a vendor instead of a bank, and the first where the deliverable's framework choice has to land across three regulator audiences (customer-bank's OCC examiner downstream, Bank of Israel + ISA on supervisory cycle, INCD on national-threat-model coordination) instead of one or two. The chapter also introduces a new structural difficulty: the reference spec has a mechanism for growing from audit findings (§10.17 was produced *by* an engagement like this one); Kognitos's twelve fields are fixed.

---

## 🌅 8:30 AM — Kickoff: Three Audiences, One Deliverable

The audit team gathered in NetiVa's HaArba'a Tower conference room. Floor-to-ceiling glass faced the Mediterranean. Ayelet Shoham introduced the room: she would carry the architecture walk, Yoel Stern the cryptographic substrate, Reut Bercovici the product surface. Pankaj Iyengar, the US customer-bank's vendor-management lead, sat at the far end with a binder marked OCC-2026-VM-Q2.

Pankaj opened. *We are renewing NetiVa as a Tier-1 vendor for our institution.* He named the constraint quickly: the bank's vendor-management committee needed an audit deliverable that would satisfy three audiences. The bank's OCC examiner cycle would read it on the downstream side. Bank of Israel and ISA had consented to receive a redacted copy on Israeli supervisory cycle. INCD — the Israel National Cyber Directorate — would not formally receive the deliverable but had asked NetiVa to coordinate on the threat-model section.

Dawn asked which framework the customer-bank had specified.

Pankaj's binder named two options. The first was the Kognitos 12-field schema, which NetiVa had selected for ease of cross-vendor comparison. The second was the FFIEC chain-of-custody reference spec, which NetiVa was already implementing internally and which Bank of Israel had been seen citing in supervisory letters earlier in the quarter.

*The committee asked you to pick one,* Pankaj said. *We can revisit if Day 1 surfaces something the framework can't carry.*

Dawn confirmed the lens. The team would walk the engagement under the Kognitos 12-field schema, with running notes flagging what landed outside the schema's reach.

*Note for the chapter. The engagement starts with the framework selected. The customer-bank has already made the cross-vendor-comparison choice. We will see how the lens holds against the substrate that NetiVa has built.*

---

## 🧬 9:30 AM — First Verifier Exercise: One Customer-Bank, One Tenant, One Entry

Ayelet walked the architecture. Each of the 23 customer-banks held a dedicated FIPS 140-2 Level 3 partition under its own IKM. Inside the partition, tenant separation came from HKDF binding on `tenant_id` — same character class enforcement, no `|` byte. About 110 active tenants across the 23 banks.

Mike asked for a single chain entry from the customer-bank in the room: Pankaj's institution.

Mike ran the verifier:

```
$ herald-verify --tenant=mw_pankaj_bank_t41 \
                --service=adverse-action-decision \
                --date=2026-05-21 \
                --entry-id=entry_aa_pankaj_t41_20260521_0941_0007 \
                --strict
```

Five point one seconds.

```
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified
        against public key 7c:42:1a:8b:f0:33:c8:91
Elapsed: 5.1s
```

Twelve steps. PASS. The entry carried Field 1 (timestamp), Field 2 (decision ID), Field 3 (authenticated_user_id for Pankaj's institution's adverse-action analyst), Field 4 (AI system identity), Field 5 (model identity), Field 6 (inputs with source attribution including a SaaS-edge Salesforce CRM mirror connector), Field 7 (policy invoked), Field 8 (reasoning), Field 9 (output), Field 10 (downstream action), Field 11 (no human review on this one — eligible cases below threshold), Field 12 (HMAC + Merkle path + HSM signature).

> ### ✓ Confirmation #1 — Twelve-field schema satisfied on one entry from one customer-bank
> All twelve Kognitos fields populated. The verifier accepts the entry on the strict path.

Chen flipped a page in her notebook. She did not say anything. She drew a small circle around "Field 12" and wrote next to it: *one field for HMAC + Merkle + HSM signature.*

*Note for the chapter. The Kognitos lens reports the entry as satisfied. The substrate behind Field 12 is a three-layer compositional argument I cannot file in the framework.*

---

## 🛡️ 10:30 AM — §1.4: The Cryptographic Substrate That Has Nowhere to Go

Yoel pulled up NetiVa's threat-model design doc on the conference-room display. The first slide was a three-layer diagram. Layer 1: per-event HMAC with HKDF tenant binding (§4.1). Layer 2: daily Merkle seal (§4.2). Layer 3: HSM signature on the seal (§4.3). Below the diagram in 10-point type: *Composite security: 128 bits under NIST SP 800-175B per §1.3 + §1.4.*

Dawn asked Yoel to walk the substrate.

Yoel walked through it cleanly. The three layers compose under EUF-CMA + second-preimage + EUF-CMA. Each layer is independently keyed. The IKM is generated on-HSM under FIPS-validated CSPRNG. The seal job runs in the same region as the partition. The HSM signature binds the daily seal to a key fingerprint that the verifier carries by configuration. The composite holds against an adversary who has compromised any one layer (write privileges on the chain table, for instance) without compromising the others.

The audit team listened. Dawn took notes. Chen kept her pen moving the whole time.

When Yoel finished, Dawn turned to her own notes and asked the framework question.

*Where does the three-layer compositional argument file in Kognitos?*

The room was quiet for a moment. Reut, the CPO, leaned forward. *It is in the integrity proof field, I think?*

Dawn nodded slowly. *That field captures that a proof exists. The compositional argument is the reason the proof holds. The reason is what the customer-bank's vendor-management committee will be asked about when their OCC examiner reads this in 90 days.*

> ### ⚠ Framework Inarticulability #4 — §1.4 compositional security argument has no Kognitos slot
> The three-layer 128-bit composite under NIST SP 800-175B is what gives Field 12 its meaning. Field 12 says "yes, a tamper-evident integrity proof exists." It cannot articulate that the proof composes from three independent mechanisms, each independently keyed, each with its own threat model. The substrate is the answer to the substrate question. Kognitos can only point at the surface.

*Note for the chapter. This is the first chapter where the inarticulability is on the cryptographic substrate itself, not on a non-AI-decision zone or a litigation-defense gap. The framework can record that a proof exists. It cannot record why the proof should be trusted.*

---

## 🚨 11:00 AM — Unannounced Arrival: INCD at the Door

Ayelet's phone buzzed. She read the screen, blinked once, and stood up. *Tamar from INCD is downstairs.* Yoel followed her out. Three minutes later they returned with Tamar Levanon, INCD's banking-sector liaison.

Tamar carried no laptop. She introduced herself in English, then in Hebrew to Yoel and Ayelet, then back to English for the room. *I have asked NetiVa to coordinate the threat-model section of the audit deliverable. I was not invited to today's session. I am here because the supervisory letter that triggered this audit referenced INCD's 18-month-dwell guidance, and I wanted to read your framework selection on the same day the customer-bank's people are in the room.*

She sat down. She did not ask permission.

Dawn briefed her on where the team was. Tamar listened. When Dawn got to the framework choice, Tamar's expression did not change. She asked one question.

*What does your framework say about HSM custody under nation-state threat?*

Yoel waited for Dawn.

Dawn answered honestly. *Field 12 says the integrity proof exists. The framework does not have a field for HSM custody as a separable property. The customer-bank chose this framework for cross-vendor comparability. I am running running-notes today on what the framework cannot carry, and HSM custody under nation-state threat is on that list.*

Tamar nodded once. *Continue. I will sit until lunch.*

> ### ◇ Framework-Silent Observation #11 — HSM custody under nation-state threat
> The INCD threat model assumes 18-month adversary dwell. The reference spec's §10.5 (FIPS 140-2 Level 3) and §10.6.1 (HSM-internal CSPRNG declared as `rng_source = "hsm.thales-luna-7000"`) elevate above the spec-conformance floor with EAL4+ Common Criteria for this threat class. Kognitos has no field for key-generation source. The audit team can confirm a proof exists. The audit team cannot articulate, in the framework's vocabulary, why the key behind the proof is trustworthy against IRGC-class dwell.

*Note for the chapter. The INCD liaison did not ask whether HSM custody was sound. She asked what the framework says about it. The answer is: the framework says nothing.*

---

## ⚡ 11:30 AM — Adversarial Inserts on the Staging IKM Registry

Yoel walked the team to a staging console. Diana ran three adversarial inserts on the IKM registry while Tamar watched.

Insert one — duplicate `(bank_id, tenant_id)` within the same bank.

```
UNIQUE INDEX violated on ikm_registry(bank_id, tenant_id)
Reject reason: §10.1 IKM-registry uniqueness — within-bank duplicate
Exit code: 32
```

Insert two — same `tenant_id` value across two different banks.

```
INSERT accepted
Reason: cross-bank isolation by per-bank IKM
Spec ref: §10.1 + §4.1 HKDF binding makes same tenant_id
         under different IKMs cryptographically distinct
```

Insert three — `tenant_id` shorter than the minimum length.

```
CHECK constraint violated on tenant_id
Reject reason: §3 character class enforcement
Exit code: 32
```

Three for three behaved per spec. Tamar made one note in a small notebook.

Diana looked at Chen.

*This second one,* Diana said. *The accepted insert. Same tenant_id across two banks. How does Kognitos articulate that these two entries are isolated?*

Chen wrote it out longhand and read it back. *Kognitos has Field 4 for AI-system identity. It does not have a field for cryptographic-isolation domain. The two entries share a tenant_id string value. The framework will see them as related unless the auditor manually carries cross-bank-isolation context.*

> ### 🚨 Framework Under-Reporting #4 — Cross-bank cryptographic isolation by per-bank IKM
> Reference spec §10.1 + §4.1 catches that same `tenant_id` across two banks is cryptographically distinct because the IKMs differ. Kognitos has no field for the isolation domain. The auditor would carry the distinction in a prose footnote, not a structured attribute. For a multi-tenant vendor evaluation, this is the structural property that justifies the vendor's tenancy model — and the framework does not record it.

*Note for the chapter. The under-reporting count just incremented on a property that is structurally central to multi-tenant SaaS vendor evaluation. This is the third under-reporting and the first one where reference spec catches a cryptographic isolation property.*

Tamar closed her notebook. *I will return tomorrow at 9.* She left.

---

## 🔧 1:00 PM — The HSM Colocation Visit: A Paper Trail That Does Not Reach the Chain

After a working lunch in NetiVa's cafeteria, the team drove to the colocation facility north of the city. Yoel held the badge ceremony. Mike, Diana, Luis, and Chen suited up. Dawn observed from the operations room.

The colocation hosted twelve PCIe Luna 7000s split across two cages, one per Israeli region. Each of the 23 customer-bank partitions had been initialized with a 2-of-2 PIN split between the customer-bank CISO and NetiVa CISO at onboarding. The partition-ceremony attendance log was kept in a binder on the operations-room desk: signed photocopies of attendance forms, PDF scans of HSM operator console logs, ceremony witnesses signed by hand.

Mike pulled the binder open at Pankaj's bank's partition. The attendance form was there. The PDF scan was there. The HSM operator-console log was there.

Mike asked the question that landed the Partial.

*Where is this attendance record bound to the chain?*

Yoel paused. The attendance log was a paper-and-PDF artifact. It was not emitted as a chain event. The bond was a SHA-256 of the PDF kept in a separate trust-anchor table.

Chen wrote it down carefully.

> ### ⚠ Partial #1 — HSM partition-ceremony attendance log is not chain-coupled
> The attendance record exists. The PDF hash exists. The chain does not carry a `chain.partition_ceremony_attended` event with `attendance_pdf_sha256` and an HSM attestation token. An auditor following the chain alone cannot verify that the ceremony happened, who attended, or which witnesses signed. The Kognitos framework has no field for ceremony attestation; the reference spec's §10.17 does not exist yet as of this morning either — but reference spec has §10.5 and §10.6.1 on HSM custody that this Partial closes against by extension.

*Note for the chapter. This is the kind of Partial that the reference spec would absorb as a new section in a change-log. Kognitos cannot absorb a new field. The framework's twelve fields are fixed. The reference spec is a living document; the Kognitos schema is not.*

Mike and Yoel agreed on a remediation path: emit a `chain.partition_ceremony_attended` event going forward, with `attendance_pdf_sha256` mandatory and an HSM attestation token recommended. Yoel committed to landing the change before the Q4 IKM rotation cycle — 60 days out. The Partial would close-by-spec at engagement-time-plus-sixty.

> ### ◇ Framework-Silent Observation #12 — The reference spec grows from audit findings; Kognitos does not
> The reference spec has a change-log mechanism. Sections like §10.17 enter the normative text *because* an engagement surfaced a gap that the existing text could not articulate. Kognitos's twelve fields are fixed by the framework author. An auditor in the room with NetiVa cannot file a finding that grows the framework — they can only file a finding that the framework cannot carry. The reference spec absorbs the finding; the framework records the absence.

*Note for the chapter. The structural difference between a framework that can grow and a framework that cannot is the difference between a living standard and a fixed catalog. This is a property of the reference spec that I have not seen in any other engagement to this point.*

---

## 🔧 2:30 PM — The Hebrew Runbook Discovery

Luis walked to the colocation operations desk and asked to see the verifier credential-rotation runbook. Yoel handed him a printed binder. Luis flipped through it. The runbook was in Hebrew.

*Where is the English copy?*

Yoel checked the operations directory. There was no English copy. The customer-bank verifier reference distribution carried an English README with a one-paragraph rotation summary. The colocation internal-ops runbook — the document NetiVa SREs used at 3 AM — was Hebrew-only.

Diana looked over Luis's shoulder. *This is a discoverability finding.*

Luis filed it.

> ### ⚠ Partial #2 — Cross-language CC8.1 discoverability gap on internal-ops runbook
> The customer-bank-facing distribution has an English README. The NetiVa-internal operations runbook is Hebrew-only. A US OCC examiner reading the customer-bank's CC8.1 listing would find the vendor's external interface documented. They would not find the operational runbook. Reference spec §10.18 has a cross-referencing rule that names CC8.1 and the runbook jointly; reference spec §10.17 (post-engagement) names the cross-language discoverability clause. Kognitos has no field for runbook cross-referencing in any language. The Nit closes by adding English translation; ~4 hours of work. NetiVa committed to landing before report filing.

*Note for the chapter. This is the second under-reporting candidate of the day. Reference spec has §10.18 to file this against. Kognitos has Field 7 (policy/prompt invoked) which is the wrong shape. The framework cannot articulate operational-runbook discoverability across two languages spoken by three regulator audiences.*

---

## ⚡ 3:30 PM — The April 30 NaN Incident

Back at NetiVa headquarters. Chen asked to walk the April 30 incident.

Yoel pulled up the incident timeline. On April 30 at 09:47 Israel time, the operational verifier ran its scheduled hourly check across the production chain. It surfaced a serialization-bug anomaly: a model output containing a NaN value was failing RFC 8785 JCS canonicalization (§5 test-vector 008). Eleven entries had been written with an invalid canonical form. The seal job had run on the daily roll-up and produced a Merkle root that included the invalid entries.

The on-call SRE caught the alert at 09:51 — four minutes after emission. Bank of Israel Directive 411 §3 required reporting cyber incidents within 30 minutes. NetiVa filed the §3 notification at 10:03 — sixteen minutes after operational detection, well inside the 30-minute clock. Directive 365 §3 required 2-hour first-restore; the patch landed at 11:42 — 1h 55m. Directive 367 §4 required cloud-and-AI logging duties; the operational-events chain (§10.2) had emitted `chain.verification_failure` automatically at 09:47.

Run-resume followed §10.25. The eleven invalid entries were replayed under in-memory tail acquisition with ledger ingestion cross-check on `(prev_hash, seq)` monotonicity. Originals and replays were both retained per §10.3 append-only enforcement. Total close: 6h 23m, including post-incident review.

Mike ran the verifier against one of the replayed entries.

```
$ herald-verify --tenant=mw_q2_bank_t89 \
                --service=adverse-action-decision \
                --date=2026-04-30 \
                --entry-id=entry_aa_q2_t89_20260430_0942_replay_03 \
                --strict
```

Four point eight seconds.

```
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified;
        run-resume tail consistent with prior ledger
        (prev_hash, seq) monotonic
Elapsed: 4.8s
```

> ### ✓ Confirmation #2 — April 30 incident handled per §10.2 + §10.25 + Directives 411/365/367
> Operational-events chain caught the bug. Run-resume replayed the eleven entries. Three Bank of Israel directives engaged on a single serialization bug; all three satisfied. The chain carries the incident as observable events.

Chen asked the framework question.

*Three Bank of Israel directives engaged on one bug. Kognitos has Field 1 timestamp and Field 12 integrity proof. Where does the operational-events sequence file?*

The room was quiet for a beat.

> ### 🚨 Framework Under-Reporting #5 — Operational-events sequence has no Kognitos representation
> Reference spec §10.2 enumerates the operational-events catalog: `chain.verification_failure`, `seal.job_started`, `seal.job_completed`, `master_key.rotation_observed`, `master.cross_region_replication_completed`, `connector.lag_observation`, `connector.outage`, `chain.coverage_map_published`. These are chain-carried operational signals that an examiner can correlate against incident timelines. Kognitos has no field for operational-events. The audit team can confirm the incident was handled. The audit team cannot, in the framework's vocabulary, point at the chain itself as the witness that handled it.

*Note for the chapter. The reference spec catches operational-events as first-class chain entries. Kognitos's twelve fields are designed for AI-decision entries. The operational substrate that *enables* the AI-decision integrity is invisible to the framework. This is the fifth under-reporting; the second under-reporting today; and structurally the most important one because operational-events are how the chain proves it is alive.*

---

## 💳 4:30 PM — Customer-Bank Salesforce Mirror: Four Numbers, No Adjectives

Elena was not on this engagement (the customer-side stack at NetiVa is the SaaS-edge mirror connector, not a downstream consumer-facing platform). Dawn walked the Salesforce mirror with Reut.

NetiVa pulled customer-bank Salesforce CRM data through a §4.4.6 connector. The mirror had four lag numbers named: median 12 seconds; p95 SLO 60 seconds; alert threshold 90 seconds; RTO 5 minutes. The severity classification clause was in the runbook.

Reut walked Dawn through three alert incidents in the last quarter. All three closed within the alert threshold. None reached RTO.

Mike ran the verifier on a Salesforce-sourced entry. PASS.

> ### ✓ Confirmation #3 — §10.16 four-number lag-bound discipline on Salesforce mirror
> Four numbers named by quantity. No "near real-time" adjective. The connector source attribution per §4.4.6 lands on the entry. Kognitos Field 6 carries the input source by name. The four numbers — and the severity classification clause — do not have a Kognitos slot.

*Note for the chapter. This is the third recurring instance of the four-number lag-bound discipline observation. Kognitos has Field 6 for source attribution; it does not have anything for the temporal-quality envelope that the source attribution sits inside. We have logged this in three prior engagements. It is now a stable pattern.*

---

## 🌆 5:00 PM — Auditor Debrief

Dawn went to the whiteboard. The team was tired. Pankaj was still in the room. The room was quiet.

```
KOGNITOS 12-FIELD ASSESSMENT — NETIVA INTELLIGENCE LTD. (VENDOR EVALUATION, DAY 1)

AI SIDE — 23 CUSTOMER-BANKS, ~110 TENANTS:
  Confirmations:                  3 (Field-12 surface, April 30 close, four-number lag)
  Adversarial-insert demonstrations: 3 (within-bank reject, cross-bank accept, short-id reject)
  Partials:                       2 (HSM ceremony attestation; Hebrew runbook)
  Findings against vendor:        0  (this is a confirmation engagement on the reference side)
  Framework-silent observations:  2 (HSM nation-state custody; framework cannot grow)

CRYPTOGRAPHIC SUBSTRATE:
  §1.4 compositional security argument: NO KOGNITOS SLOT
  §10.1 cross-bank isolation by per-bank IKM: NO KOGNITOS SLOT
  §10.5 / §10.6.1 HSM custody + CSPRNG declared: NO KOGNITOS SLOT
  §10.17 HSM partition-ceremony attestation: NO KOGNITOS SLOT (spec didn't have it either; will after this engagement)

OPERATIONAL SUBSTRATE:
  §10.2 operational-events catalog: NO KOGNITOS SLOT
  April 30 incident chain trail: NOT REPRESENTABLE in framework
  Directives 411 §3 + 365 §3 + 367 §4 engaged on one bug: ARTICULABLE ONLY IN PROSE

CROSS-ZONE / FRAMEWORK-SIDE:
  Framework Inarticulability:     1 (§1.4 compositional security on substrate)
  Framework Under-Reporting:      2 (cross-bank isolation; operational-events sequence)
  Cross-language discoverability: 1 (§10.18 + post-engagement §10.17 clause)
```

Dawn drew a box around the cryptographic-substrate block and the operational-substrate block. She underlined the line `framework cannot grow`.

**ENGAGEMENT-TEAM OBSERVATIONS ON FRAMEWORK SELECTION:**

1. Kognitos's twelve fields are designed for AI-decision entries. The substrate underneath — keying material, ceremony attendance, multi-region invariants, operational-events stream, run-resume integrity — has no representation.
2. The vendor here is operating against a nation-state threat model. The threat model is articulated by INCD in coordination guidance, not in the framework. The audit team can confirm an integrity proof exists; the framework cannot articulate whether that proof holds against an 18-month-dwell IRGC adversary.
3. Same `tenant_id` value across two customer-banks is cryptographically distinct under per-bank IKM. Reference spec §10.1 + §4.1 catches this; the framework records the two tenant_ids as identical strings. For a multi-tenant SaaS vendor evaluation, this is the structural property that justifies the tenancy model.
4. The April 30 NaN incident generated three Bank of Israel directive engagements on one chain trail. The reference spec's §10.2 operational-events catalog represents the incident as a chain-carried sequence. Kognitos has no operational-events field. Three directives, one bug, no framework articulation.
5. The HSM partition-ceremony Partial is the kind of finding that, under reference spec governance, becomes a new normative section. The reference spec absorbs the finding into §10.17. The Kognitos framework has no mechanism for absorbing a finding. Twelve fields go in, twelve fields come out.
6. The Hebrew runbook Nit is filable. The structural shape of the Nit — cross-language CC8.1 discoverability — is not. Reference spec §10.18 carries the shape. Kognitos has Field 7 (policy/prompt) which is the wrong slot for an operational runbook.

Chen put down her pen. Pankaj closed his binder.

---

## 🧾 Stakeholder On-the-Record Statement — Pankaj Iyengar

Pankaj asked for the room.

He spoke slowly, mindful that the deliverable would land in three regulator audiences. He named what he wanted on the record.

*I came here as a customer-bank vendor-management lead with a $180B institution and a Tier-1 vendor and a renewal cycle and a binder full of OCC expectations. I have heard the audit team walk this engagement under the Kognitos framework with care and discipline. I have also heard, in their running notes, what the framework cannot carry. The vendor we are evaluating runs at a nation-state threat assumption. The vendor we are evaluating handles 23 customer-banks under per-bank cryptographic isolation. The vendor we are evaluating has a partition-ceremony record that, under proper governance, becomes a new clause in the normative spec by the end of next quarter. None of those properties have a slot in the framework on the audit-deliverable cover.*

He paused.

*I will be returning to my committee on Monday. I will be naming, in the cover memo, that the framework I chose for cross-vendor comparability did not carry the engagement's most important findings. I will recommend that future evaluations of this vendor — and of any vendor that operates at a nation-state threat model — be delivered against the reference specification, with Kognitos retained only for the cross-vendor comparison summary table. The audit team's running notes will be the record of what the framework missed. I want that recommendation, and the team's discipline in surfacing it, on the record.*

Dawn waited a beat. *On the record.*

*Note for the chapter. Pankaj's statement is the fourth on-the-record stakeholder request. It is also the first one where the stakeholder names a future remediation: switch frameworks for nation-state-threat-class vendors, retain Kognitos only as a summary surface for cross-vendor comparability. This is the sharpest framework-selection recommendation in the program to this point.*

---

## 🧾 Final Assessment Theme

> "NetiVa Intelligence Ltd. is a confirmation engagement on the reference side: twenty Confirmations, one Partial that closes by spec at §10.17 within sixty days, one Nit that closes against §10.18 within four hours. Under the Kognitos lens, the same engagement reads thinner. The cryptographic substrate that gives Field 12 its meaning has no framework slot. The cross-bank cryptographic isolation that justifies the vendor's multi-tenancy model has no framework slot. The operational-events sequence that proved the chain was alive during the April 30 NaN incident has no framework slot. The HSM partition-ceremony Partial that — under reference governance — will become §10.17 normative text has no framework slot, and the framework has no mechanism to absorb it even if it did. The customer-bank's vendor-management lead delivered an on-the-record recommendation that future nation-state-threat-class vendor evaluations be delivered against the reference spec, with Kognitos retained only as a cross-vendor comparison summary. The reference spec leaves this engagement with a new section. The Kognitos framework leaves this engagement with the same twelve fields it walked in with."

---

## Research takeaway

Chapter 08 introduces the first vendor-evaluation engagement in the program and produces three structurally new observations. First, the cryptographic-substrate inarticulability (§1.4 compositional security) is a different kind of inarticulability than the prior three: the prior inarticulabilities concerned non-AI-decision zones, public-safety stakes, and civil-rights litigation; this one concerns the substrate underneath the AI decisions themselves. Field 12 records that a proof exists; the framework has no vocabulary for *why the proof holds*. Second, multi-tenant cryptographic isolation (§10.1 + §4.1 HKDF) is a structural property the framework cannot record — relevant for any SaaS vendor evaluation, not just nation-state-threat ones. Third, the framework-cannot-grow observation is the most important meta-finding to this point: the reference spec absorbs findings into new normative sections; Kognitos's twelve fields are fixed. An auditor cannot, under Kognitos, file a finding that improves Kognitos.

- Compared to Ch07 (Olmstead), this chapter's inarticulability is on a deeper layer of the stack. Olmstead's inarticulability concerned civil-rights litigation as a §1.2 epistemic-scope variant. NetiVa's inarticulability concerns the cryptographic substrate that every other field depends on.
- Compared to Ch06 (Pacific Crescent), the stakeholder statement here advances Soren Kovach's "any utility with public-safety stakes" pattern into a new dimension: "any vendor at a nation-state threat model — name the framework that lets us answer all three regulator audiences."
- Compared to Ch04 (Atrio), Pankaj's statement is the first one that *recommends a future framework switch*. Veronika's statement set a boundary on what Kognitos could be used for. Pankaj's statement names what should replace it for the nation-state-threat class of engagement.

The pattern is clarifying: at every engagement where the framework's coverage gap concerns substrate (cryptographic, operational, multi-regulator-coordination), the stakeholder either asks for explicit attribution of framework selection (Atrio, Helmstad, PCP, Olmstead) or — now — recommends an explicit framework substitution for that class of engagement.

---

*Running counts and program-level signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
