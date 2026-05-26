# 04 — Atrio Banking Platform (Kognitos-lens)

*A vendor-side BaaS platform audit at multi-tenant scale, where the framework's silence is no longer just speculation — it's under-reporting*

**Engagement:** Vendor-side platform audit, coordinated examiner cycle
**Client:** Atrio Banking Platform — Banking-as-a-Service infrastructure, 12 sponsor banks, 47 fintech programs, 2 AWS regions active-active, 24 months on chain
**Status:** Full enterprise audit-trail capture, multi-tenant production
**Audit team lead:** Dawn
**Client liaison:** Veronika Sutton, Chief Compliance Officer; Daichi Park, Director of Platform Security

**Audit audiences (concurrent in the same building):**
1. Indiana state banking department examiner
2. North Carolina state banking department examiner
3. Georgia state banking department examiner
4. OCC examiner
5. CFPB analyst

Five regulator audiences. One vendor-side platform audit. The coordinated-examiner model is supposed to produce one audit deliverable serving five regulator readers, each running their own independent verification using partitioned credentials against the same underlying chain.

**Audit team's framework:** Kognitos's 12-field AI audit-trail schema. The team has now done three engagements under this framework (Northbridge, Mercator, Stelvio) and has consistent patterns for full-enterprise, two-zone bifurcated, and three-zone bifurcated assessments. Atrio is the first multi-tenant platform engagement. The team will discover a fourth research signal: at platform scale, the framework's silence stops being just *speculation* (the auditor invents anchors) and starts being *under-reporting* (the framework misses legitimate findings the reference spec would have caught).

---

## 🌅 8:30 AM — Kickoff (Five Examiners, One Platform)

The Atrio engagement room was unusual. Two adjoining conference rooms separated by a glass partition. The audit-team room was on the left. The coordinated-examiner room was on the right. Five regulator audiences would sit in the right-hand room running independent queries while the audit team worked on the left.

Veronika Sutton walked into the audit-team room with a one-page deck.

"Twelve sponsor banks. Forty-seven fintech programs. Two AWS regions active-active. Twenty-four months of operational chain data. Five regulator audiences next door. The examiners have their own partitioned credentials — each examiner can only see the chains for the institutions they regulate. Indiana sees Indiana-chartered banks; OCC sees nationally-chartered banks; CFPB sees consumer-protection cross-bank."

Dawn looked at the deck.

"The Kognitos framework we operate under doesn't have a field for multi-tenant scope partitioning. Field 3 asks for authenticated human identity at the AI event. Field 12 asks for tamper-evident integrity proof. Neither field addresses cross-tenant credential isolation. Walk us through how the partitioning is enforced."

Veronika nodded.

"Two pieces. First, the IKM registry has a `(bank_id, tenant_id)` PRIMARY KEY with a UNIQUE INDEX on the same. Twelve banks can each have a `tenant_id=production` because the IKMs differ — the HKDF tenant binding produces different per-event MAC keys, so cross-bank `tenant_id` collision is cryptographically safe. Second, the examiner credentials are scoped to specific `(bank_id, tenant_id)` pairs. Indiana's credential opens Indiana-chartered banks' chains and refuses Georgia's. That's the structural side."

She paused.

"The cryptographic side is §4.1 + §4.1.1 Model B — the HSM holds the per-tenant PRK; the SDK does the Expand. The IKMs are different by §10.1 design. The examiner refusals are demonstrated by the partitioned-credentials test."

Dawn wrote that down. Kognitos's Field 3 and Field 12 cover both of these implicitly but not explicitly. The bank's reference spec carries §10.1 as a structural hinge that the platform's entire claim rests on. Under Kognitos, an institution operating without §10.1's uniqueness constraint would satisfy the framework — and could have tenant-id collisions that compromise integrity at scale. Another ◇.

Tom — the visiting-team's internal-audit liaison — had a question. "The five examiners next door run independent verifiers. They each pull the published binary?"

"Each pulls the published Cosign-signed reference verifier from GitHub Releases. Each runs the same binary against their partitioned credentials. The byte-identical-output property — five examiners, five verifier instances, same chain entries, same byte output — is the multi-implementation conformance bar §10.26 normates. Under our reference spec, examiner-to-examiner variance is bounded by the reference implementation. Under your framework, we'd have no equivalent bound."

Dawn noted: *◇ Multi-implementation conformance bar across five examiners. Recurring property from Chapters 01-03; first exercised at coordinated-examiner scale. Kognitos has no equivalent.*

She closed the deck.

"Let's start with the IKM registry walkthrough. Daichi can take us through the structural side."

---

## 🔐 9:15 AM — IKM Registry Walkthrough (Four Adversarial Inserts)

Daichi pulled up the IKM registry schema. The team gathered around.

```sql
CREATE TABLE ikm_registry (
    bank_id        VARCHAR(64)     NOT NULL,
    tenant_id      VARCHAR(255)    NOT NULL,
    ikm_version    INT             NOT NULL,
    ikm_handle     VARCHAR(512)    NOT NULL,
    created_at     TIMESTAMPTZ     NOT NULL,
    rotated_at     TIMESTAMPTZ,
    PRIMARY KEY (bank_id, tenant_id, ikm_version),
    UNIQUE       (bank_id, tenant_id, ikm_version),
    CHECK        (bank_id <> ''),
    CHECK        (tenant_id <> '')
);
```

"Twelve banks. Forty-seven fintechs. Each fintech may operate under one or more banks (sponsorship model). The schema enforces uniqueness at the bank-tenant-version triple. The check constraints — bank_id non-empty and tenant_id non-empty — were added in 2024 after a near-miss with an empty-string bank_id insert. The 2024 bug-fix is part of the schema's stable contract now."

Diana ran the four adversarial inserts against a staging copy.

**Insert 1 — duplicate within bank.** `(bank_id='IndianaBank01', tenant_id='production', ikm_version=4)` twice. Second insert rejected with `UNIQUE constraint violated`.

**Insert 2 — same tenant_id across banks.** `(bank_id='IndianaBank01', tenant_id='production', ikm_version=1)` and `(bank_id='GeorgiaBank03', tenant_id='production', ikm_version=1)`. Both accepted. Cryptographically safe because the IKMs differ.

**Insert 3 — empty-string bank_id.** `(bank_id='', tenant_id='production', ikm_version=1)`. Rejected by the 2024 CHECK constraint.

**Insert 4 — null bank_id.** `(bank_id=NULL, tenant_id='production', ikm_version=1)`. Rejected by the NOT NULL constraint.

Four adversarial inserts. Four expected outcomes. The §10.1 IKM registry uniqueness held in all four cases.

> ### ✓ Confirmation #1 — Multi-tenant IKM registry uniqueness operationally tested (Field 12, with depth not asked)
>
> Four adversarial inserts against the IKM registry staging copy returned four expected outcomes per the §10.1 normative constraint. Cross-bank `tenant_id='production'` is cryptographically safe because IKMs differ by §10.1 design. Kognitos's Field 12 satisfies; the structural hinge that prevents multi-tenant collision is framework-silent.

> ### ◇ Framework-Silent Observation #1 — Multi-tenant collision prevention
>
> The §10.1 IKM registry uniqueness constraint prevents cross-tenant collision via cryptographic binding rather than by IAM convention. An institution operating without the constraint could have tenant_id collisions that produce cross-tenant MAC equivalence — Field 12 would satisfy each tenant's chain individually but the framework would not detect the collision risk. Kognitos has no field for cross-tenant cryptographic isolation.

---

## 🔍 10:00 AM — The 5×5 Cross-Tenant Refusal Matrix

The examiners next door began their independent queries. The audit team sat where they could see the partition wall.

Diana ran the cross-tenant refusal matrix. Five examiner credentials × five tenant scopes = 25 attempted reads.

| Credential | IN-chartered | NC-chartered | GA-chartered | National | Consumer-cross |
|---|---|---|---|---|---|
| Indiana | ✓ read | ✗ refused | ✗ refused | ✗ refused | ✗ refused |
| North Carolina | ✗ refused | ✓ read | ✗ refused | ✗ refused | ✗ refused |
| Georgia | ✗ refused | ✗ refused | ✓ read | ✗ refused | ✗ refused |
| OCC | ✗ refused | ✗ refused | ✗ refused | ✓ read | ✗ refused |
| CFPB | (partial) | (partial) | (partial) | (partial) | ✓ read |

25 of 25 expected outcomes. The CFPB credential had partial-read access on a §1033 cross-bank consumer-data path; the other four diagonal cells were full-read on their respective scopes.

Diana noted in her template: *Field 3 satisfied at the credential-issuance layer. The cross-tenant isolation is enforced at the verifier-side credential check, not just at the IAM layer. The framework's Field 3 covers "the authenticated human user identity"; it doesn't address whether the verifier itself respects scope boundaries when the user is an authenticated examiner. The bank's §4.1.1 Model B HSM-resident PRK is what enforces the scope boundary cryptographically.*

> ### ✓ Confirmation #2 — Cross-tenant scope isolation (5×5 matrix, 25 of 25 expected) (Field 3 + Field 12 with depth)
>
> Five examiner credentials × five tenant scopes returned 25 of 25 expected outcomes. Scope isolation is enforced cryptographically via §4.1.1 Model B HSM-resident PRK plus §10.1 IKM registry uniqueness. The Kognitos framework does not address verifier-side scope enforcement.

---

## 🧬 11:00 AM — Merkle Reconciliation Test (10 Random Triples)

Dawn ran her own reconciliation test. She picked 10 random `(bank_id, tenant_id, date)` triples spanning 24 months, six banks, and 12 fintechs. For each triple, she pulled the seal record, recomputed the Merkle root from the day's chain entries, and verified the Ed25519 signature.

10 of 10 PASS. Average 2.1 seconds per triple. Total wall clock: 21 seconds.

> ### ✓ Confirmation #3 — 10-random-triple Merkle reconciliation (Field 12)

She ran a second batch: 10 triples that included two CloudHSM key-rotation boundaries. Same procedure. 10 of 10 PASS. The verifier resolved each entry's signing-key fingerprint per `seal_date` metadata.

> ### ✓ Confirmation #4 — Cross-rotation Merkle reconciliation transparent (Field 12, recurring depth)

She ran a third: 10 triples from a tenant operating on streaming cadence (per §10.27/28/29) rather than daily Merkle. The verifier handled the streaming cadence under a different procedural branch.

> ### ✓ Confirmation #5 — Streaming-cadence verification (Field 12 with framework-silent depth)

> ### ◇ Framework-Silent Observation #2 — Streaming vs daily cadence
>
> Three of Atrio's 47 fintech programs run on streaming cadence rather than daily Merkle. The bank's reference spec carries §10.27, §10.28, §10.29 for streaming cadence, streaming IKM rotation, and streaming verifier procedure. Kognitos's Field 12 does not address cadence at all. An institution running streaming cadence and one running daily Merkle satisfy Field 12 identically. The framework cannot distinguish.

---

## 🛰️ 1:00 PM — Multi-Region Replication (Where the Framework Stops Detecting Findings)

After lunch, Luis took the multi-region replication walkthrough. This was where Chapter 04 produced its first non-Confirmation under the bank's reference spec.

Daichi walked through the Pattern A active-active topology. Both AWS regions (`us-east-1` and `us-east-2`) write to local Herald Enterprise. ETL reconciliation runs on a schedule, publishing a sealed `master.cross_region_replication_completed` event each batch.

Luis pulled up the event. He read the §10.15 invariants out loud — there were five.

1. Each region's chain integrity holds independently. ✓
2. Cross-region reconciliation publishes a sealed event each batch. ✓
3. Reconciliation deltas are themselves chained. ✓ (Two historical deltas in the last 24 months, both reviewable.)
4. Region failover preserves chain identity. ✓
5. The `master.cross_region_replication_completed` event's source-region count is read from the authoritative source at event time, not from a cached value.

Luis asked Daichi about invariant 5.

Daichi paused.

"That's the one we caught internally six weeks ago. The event is published correctly, but the source-region count in the event payload is read from an internal poll-cache with a five-minute freshness window. For most tenants on hourly or daily cadence this is invisible — the cache lag is shorter than the cadence. For the three streaming-cadence tenants, the cache lag can produce a stale count in the event. The chain and seal correctness are intact (invariants 1-4 hold), but invariant 5 is non-conformant for fast-cadence tenants."

Luis pulled up §10.15 invariant 5 text. It was normative:

> *"For fast-cadence tenants, the source-region count published in the `master.cross_region_replication_completed` event MUST be read from the authoritative source at event time. Poll-cached read of the count, regardless of cache freshness window, is non-conformant for any tenant whose chain cadence is shorter than the cache freshness window."*

Daichi: "Engineering ticket open. 60-day ETA. Push-update mechanism replaces the cache poll. We caught it internally six weeks ago when we were rotating the cache infrastructure; the audit happened to fall in the window before the fix lands."

Under FFIEC v1.0b, this is a clean Partial — invariant 5 is normative and fails mechanically. The engagement team has no discretion to downgrade because §10.15 invariants are listed as normative.

Under Kognitos, Luis worked his template. Field 12 (tamper-evident integrity proof) is satisfied — the chain itself is sound. The framework has no field for multi-region invariants. The poll-cached count compromises a property the bank's reference spec normates and the framework does not articulate. **There is no Kognitos row to file this against.**

Luis wrote in his margin: *Bank's reference spec records this as Partial-001 against §10.15 invariant 5. Under our framework, this is a Confirmation-with-framework-silent-depth, not a Partial. The framework cannot articulate the invariant the bank's discipline operates against. **This is the first chapter where the Kognitos framework UNDER-REPORTS a finding the bank's spec would record cleanly.** Recorded as Framework Under-Reporting #1.*

> ### ✓ Confirmation #6 — Multi-region active-active replication operational (Field 12)
>
> The bank's Pattern A active-active topology operates correctly across `us-east-1` and `us-east-2`. Reconciliation events are sealed and chained. Historical deltas (two in 24 months) are reviewable. Field 12 (tamper-evident integrity proof) is satisfied for the chain itself.

> ### ⚠ Framework Under-Reporting #1 — §10.15 invariant 5 violation not detectable under Kognitos
>
> The bank's reference spec records this as Partial-001 against §10.15 invariant 5 (poll-cached source-region count for fast-cadence tenants). The chain and seal correctness are intact; only invariant 5 is affected. Under FFIEC v1.0b, the engagement team has no discretion to downgrade. Under Kognitos, the framework has no field for multi-region invariants; the violation is invisible to the framework. **The bank caught the issue internally six weeks before the audit and has a 60-day remediation ETA. Under Kognitos, an institution without that internal discipline would never see this issue surface in an audit deliverable.** Filed as Framework Under-Reporting.

Dawn read the margin.

She added to it: *◇ This is the first chapter where the framework's silence produces under-reporting, not just speculation. Speculation = auditor invents anchors to fill silence. Under-reporting = framework misses findings the reference spec catches. Both are framework-side issues; under-reporting is structurally worse because the audit deliverable is materially weaker than the operational reality.*

---

## 📋 2:00 PM — Runbook Cross-Referencing (The Disappearing Nit)

Diana walked the platform's operational runbooks. The 'Multi-Tenant Operations' section had cross-references to §4.2, §10.5, §10.15, §10.16, §10.17. It did not cross-reference §10.1 — the IKM registry uniqueness constraint that grounds the entire multi-tenant claim.

She pulled up §10.18:

> *"Institution-side runbooks and CC8.1 control descriptions MUST cross-reference the spec sections their operational discipline implements. Missing cross-references on load-bearing structural controls are a Nit; missing on non-load-bearing controls are an observation."*

§10.18 distinguishes between Nit and observation by load-bearing status. The §10.1 reference is load-bearing — it's the structural hinge of the multi-tenant claim. Under FFIEC v1.0b, the missing reference is Nit-001.

Diana wrote in her template: *Under our framework, runbook cross-referencing has no field. The platform's runbook quality is not measurable by Kognitos. This Nit disappears under our framework. Framework Under-Reporting #2.*

She walked over to Daichi.

"You're missing a §10.1 cross-reference in 'Multi-Tenant Operations.' Under your spec that's a Nit."

Daichi pulled up the runbook. "I see it. Yes. Thirty-minute fix. I'll have it in by close of business today."

Diana made a note. She did not file a Nit under her own framework — she had no row to file it against.

> ### ⚠ Framework Under-Reporting #2 — Runbook missing §10.1 cross-reference; not detectable under Kognitos
>
> The bank's reference spec records this as Nit-001 against §10.18 (runbook cross-referencing). Under Kognitos, the framework has no field for runbook cross-referencing discipline. The missing reference is invisible to the framework. The bank acknowledged and remediated within 30 minutes.

---

## 💾 2:30 PM — Run Resume from DR Rebuild (§10.25 Operational)

Chen walked through the run-resume story. Daichi had pulled the audit log for last week's `us-east-2` cluster rebuild — five tenants were running on the cluster when the rebuild happened. The SDK's three-place tail acquisition (in-memory state → SQLite sidecar → ledger query) resolved cleanly for all five. No re-genesis events. The cluster rebuild appeared in the chain as five `chain.tail_acquired` events with `acquisition_source=ledger` and `acquisition_reason=cluster_rebuild`.

Chen wrote Field 12 ✓ for the run-resume capability. Same Gap as Northbridge silent-restart but exercised in a real DR scenario at platform scale.

> ### ✓ Confirmation #7 — Run resume from us-east-2 cluster rebuild (Field 12)
>
> Last week's us-east-2 cluster rebuild produced five `chain.tail_acquired` events, no re-genesis. The three-place tail acquisition (in-memory / SQLite sidecar / ledger query) resolved cleanly. Recurring from Ch01 silent-restart depth.

---

## 🛡️ 3:00 PM — Streaming + GPU Attestation + §1033 Disclosure

Three more sections walked quickly because the framework had limited language for any of them.

**Streaming cadence (§10.27/28/29).** Three high-volume fintechs run on streaming MAC. The streaming verifier procedure was demonstrated against one tenant's last 24-hour streaming chain. The framework has no field for cadence.

**GPU-fleet attestation (§10.65).** The platform's fraud / credit / AML inference fleets run on hyperscale GPU pools. Each inference pool attests to its hardware identity at job-allocation time; attestation events are chain-captured. The framework has no field for hardware attestation discipline.

**Per-customer §1033 disclosure (§10.69).** The CFPB analyst next door ran a `consumer-cross` query that returned a per-customer audit-trail subset for a synthetic test consumer. The disclosure protocol uses §10.23 Shape 2 daily `consumer_index.attestation` events as the integrity anchor. The framework has no field for consumer-disclosure protocols.

Three more ◇ marks. Three more framework silences.

> ### ✓ Confirmation #8 — Streaming cadence verification (Field 12)
> ### ✓ Confirmation #9 — GPU-fleet attestation (Field 12 with depth not asked)
> ### ✓ Confirmation #10 — §1033 per-customer disclosure (Field 6 + Field 12 with depth)

> ### ◇ Framework-Silent Observations #3-5 — Streaming cadence, GPU attestation, §1033 consumer disclosure

---

## 🧪 4:00 PM — 1,410-Run Nightly Verifier Batch

Daichi kicked off the nightly verifier batch as a demonstration. 47 fintech programs × 30 days = 1,410 verifier runs. The batch executed in 86 seconds wall clock.

```
1,410 runs initiated
1,410 runs completed
1,410 PASS
0 FAIL
Total wall clock: 86 seconds
Average per-run: 61 milliseconds
```

Tom watched the batch finish.

"At platform scale, the verifier is operationally feasible. 1,410 runs in under two minutes. The bank can run this nightly across the full multi-tenant chain and have results in the audit window every morning."

Daichi nodded. "We run it nightly. The 86-second wall clock is what makes the nightly cadence sustainable."

The Kognitos framework had no field for operational verification feasibility at scale.

> ### ✓ Confirmation #11 — 1,410-run nightly verifier batch in 86 seconds (Field 12)

> ### ◇ Framework-Silent Observation #6 — Verification cost sub-linear at platform scale

---

## 🤝 5:00 PM — Entity Succession (§10.24 Operational)

Veronika walked the team through the §10.24 entity-succession story. 18 months earlier, Atrio acquired a smaller BaaS competitor (Cascadia Banking Tech). The acquisition included:
- Three sponsor-bank relationships
- Seven fintech programs
- An IKM registry merger event with the §10.24 attribute family
- Key custody transfer documented in a chain entry with attestation hashes from both pre-acquisition and post-acquisition HSM partitions

Under §10.24, the chain entries from Cascadia's pre-acquisition history did not move. The Atrio successor entity inherits the keys, the IKM custody, and the chain history under documented procedure. The integrity guarantee is preserved across the M&A boundary.

Mike wrote: ✓ Field 12 covers integrity within Atrio's current chain. The framework has no field for entity-succession discipline.

> ### ◇ Framework-Silent Observation #7 — Entity-succession discipline operational across M&A
>
> The Atrio platform absorbed Cascadia Banking Tech 18 months earlier. The §10.24 entity-succession discipline preserved chain integrity across the M&A boundary. Cascadia's pre-acquisition chain entries are still verifiable today under Atrio's post-acquisition keys. The Kognitos framework has no field for entity-succession discipline (recurring from Ch01 §11).

---

## 🌆 5:30 PM — Auditor Debrief

Veronika returned with coffee. The team gathered.

Dawn wrote on the whiteboard.

```
KOGNITOS 12-FIELD ASSESSMENT — ATRIO BANKING PLATFORM (multi-tenant BaaS)

Confirmations:                  11 platform-level + dozens of cell-level
                                (12 fields × 47 fintech programs satisfied per-tenant)

Partials against bank:            0   (under Kognitos)
Findings against bank:            0
Nits:                             0   (under Kognitos)

Framework-silent observations:   7   (multi-tenant collision prevention,
                                       streaming cadence, GPU attestation,
                                       §1033 disclosure, verification feasibility,
                                       entity succession, IKM registry uniqueness)

Framework Under-Reporting:       2   (§10.15 invariant-5 cache-lag Partial;
                                       §10.18 runbook cross-reference Nit)

Cross-zone:                       N/A (single-zone full enterprise)
```

Underneath, she wrote:

```
ENGAGEMENT-TEAM OBSERVATIONS ON FRAMEWORK SELECTION:

1. Under the bank's reference spec (FFIEC v1.0b), the audit produces 21 confirmations,
   1 Partial (§10.15 invariant-5 cache lag), 1 Nit (§10.18 missing cross-reference).
   Under our framework, the audit produces 11 platform-level confirmations and zero
   findings. The two findings the reference spec would catch are invisible to our
   framework because:
     - Multi-region invariants (§10.15) have no Kognitos field
     - Runbook cross-referencing (§10.18) has no Kognitos field

2. This is the first chapter where the framework UNDER-REPORTS legitimate findings,
   not just where the auditor SPECULATES around silences. Under-reporting is
   structurally worse because the audit deliverable becomes materially weaker than
   the operational reality. Atrio's institution-side culture caught both issues
   internally before the audit; under our framework alone, an institution without
   that culture could ship with both issues silently present.

3. At multi-tenant scale, the framework's silences accumulate. Twelve banks ×
   forty-seven fintechs = 564 tenant pairs. The cross-tenant collision risk
   (prevented by §10.1 IKM registry uniqueness) has no Kognitos field. An
   institution operating without §10.1's discipline would satisfy the framework
   identically and could ship with multi-tenant cryptographic collisions.

4. The coordinated-examiner room demonstrated five-examiner multi-implementation
   conformance under §10.26 (Cosign-signed reference verifier). Under our framework,
   examiner-to-examiner variance has no normative bound.

5. The 1,410-run nightly verifier batch (86 seconds) demonstrates operational
   feasibility at platform scale. The framework has no field for verification
   cost or batch feasibility.
```

She turned around.

The Indiana examiner, who had been watching through the glass partition for the last ten minutes, came around to the audit-team room. She introduced herself.

"Genevieve Marchetti, Indiana banking. I want to comment on something. Your framework gave you eleven confirmations. We have been operating under Atrio's reference spec for the last sixteen months and our internal cross-walk produces 21 confirmations against the same chain. Are you not concerned that ten of our confirmations are not in your report?"

Dawn took her time.

"We're concerned. Our report records eleven confirmations at the platform level because those are the ones the framework's 12 rows can articulate. Your sixteen-month cross-walk records 21 because the bank's reference spec has spec sections for properties our framework doesn't enumerate — streaming cadence, GPU attestation, multi-tenant IKM uniqueness, §1033 disclosure, entity-succession discipline, multi-region invariants, runbook cross-referencing discipline, and verification batch feasibility. Each of those properties is operationally significant. Each is invisible to our framework."

Genevieve nodded.

"And the two findings."

"The §10.15 invariant-5 Partial and the §10.18 Nit. Both are invisible to our framework. The bank caught both internally. Atrio's CISO told us this morning. Under your reading, the bank's report has two outstanding remediation items. Under ours, the bank's report has zero. The operational reality is identical — both items exist and both are being fixed."

"So if we are reading both reports, we trust which one?"

"You trust the union. The bank's reference-spec report is more complete by 10 confirmations and 2 findings. Our report adds the cross-walk to the 12-field framework as a baseline. Neither report is wrong; ours is shallower. We'd recommend you use ours as the AI-baseline framework summary and the bank's reference report as the operational ground truth."

Genevieve almost smiled.

"That's the answer I was hoping for. I'll note both in our examination workpaper."

She walked back to the examiner room.

Tom finished writing in his cover memo.

He had a question for Dawn.

"This is the first time we've had to explicitly call out under-reporting. Two missing findings. How do we make that recoverable in our report so a less-rigorous reading of our framework doesn't lose the findings the bank caught?"

Dawn took her time.

"Cover memo. The Engagement-Team Observations section already names both under-reportings. We add a separate section: *Findings detectable under the institution's reference spec that are invisible to the 12-field framework.* List both with the bank's remediation timeline. Under the firm's documentation conventions, that section travels with the report into vendor management workflows. The bank's own remediation tracking covers the operational follow-up; our framework documents that the framework didn't see the issues."

"And we name the framework's silence as the cause."

"We name it as the cause. The framework's silence is a property of the framework, not of the bank. The bank fixed the issues. The framework didn't see them."

Tom wrote.

Veronika came back into the room.

"Are we done?"

"We're done. Eleven confirmations against the 12-field framework at the platform level. Two framework under-reportings noted in the cover memo where the bank's reference spec catches findings ours can't articulate. Zero findings against the bank under our framework. The §10.15 invariant-5 and §10.18 Nit are recorded as framework-side silences, not as bank-side findings, because the framework has no row to file them against."

Veronika picked up the draft report.

She paused at the door.

"Tell your firm this. The 12-field framework is acceptable as a vendor-facing summary. It is not acceptable as the only assessment artifact for a multi-tenant BaaS platform. Twelve banks × forty-seven fintechs × twenty-four months produces operational properties the framework's row count cannot articulate. Atrio operates under the reference spec because we have to — the framework you brought is not enough. I want that in your cover memo, attributed to me, on the record."

Dawn nodded.

"On the record."

Veronika walked out.

---

## ❌ What They Expected vs ✅ What They Found

**❌ What They Expected:**

- Multi-tenant platform audit would surface significant Findings.
- The framework would have language for at least some multi-tenant-specific concerns.
- The five-examiner coordinated room would be the hardest part of the day.

**✅ What They Found:**

- Atrio passes cleanly at the platform level (11 confirmations).
- The framework has language for the AI-event-level properties; it has no language for the multi-tenant-scale properties.
- The five-examiner room was the easiest part of the day — five independent verifier runs all produced byte-identical output.

**⚠ What Their Framework Could Not Record:**

- §10.15 invariant-5 multi-region replication cache lag (Partial-001 under reference spec).
- §10.18 runbook cross-referencing Nit-001.
- §10.1 multi-tenant IKM registry uniqueness as a structural property.
- §10.27/28/29 streaming cadence.
- §10.65 GPU-fleet attestation.
- §10.69 per-customer §1033 disclosure protocol.
- Verification-batch feasibility (1,410 runs in 86 seconds).
- §10.24 entity-succession discipline (recurring).
- Multi-implementation conformance bar across five examiners.

---

## 🧾 Final Assessment Theme

> "The Atrio platform satisfies all twelve fields of the Kognitos framework at multi-tenant scale, with depth in seven directions materially exceeding what the framework articulates and two specific Findings (cache lag, runbook cross-reference) that the framework cannot detect at all. The institution operates under its reference spec because the framework's twelve rows cannot articulate the multi-tenant, multi-region, multi-examiner, multi-cadence operational reality. The audit deliverable under our framework is acceptable as a vendor-facing summary and inadequate as the sole assessment artifact. The CISO requested explicit on-the-record attribution of this observation in the cover memo."

---

## Research takeaway

Chapter 04 introduces a new research signal: **framework under-reporting**. Under the bank's reference spec, the audit produces 21 confirmations + 1 Partial + 1 Nit. Under Kognitos, the same operational reality produces 11 confirmations + 0 findings — because the framework lacks the spec sections (§10.15 invariants, §10.18 runbook discipline) the reference spec uses to catch the findings.

Under-reporting is structurally worse than speculation:
- **Speculation** (Chapters 01-03): auditor invents anchors to fill framework silences. Auditor is doing extra work to compensate.
- **Under-reporting** (Chapter 04): framework misses findings the reference spec would catch. The audit deliverable is materially weaker than the operational reality.

Both are framework-side issues. Under-reporting is the more consequential one because the audit deliverable is the artifact that reaches regulators and stakeholders. An institution operating under Kognitos alone could ship with findings present and the audit deliverable would record zero findings.

The running tally:
- Chapter 01: 14 speculation anchors
- Chapter 02: 12 new anchors (26 total)
- Chapter 03: 8 new anchors (34 total)
- Chapter 04: 9 new framework silences (43 total) **plus 2 framework under-reportings**

The Atrio CISO requested on-the-record attribution that the framework is "acceptable as a vendor-facing summary and inadequate as the sole assessment artifact for a multi-tenant BaaS platform." That's the cleanest stakeholder statement of the framework's limits surfaced in any chapter so far.
