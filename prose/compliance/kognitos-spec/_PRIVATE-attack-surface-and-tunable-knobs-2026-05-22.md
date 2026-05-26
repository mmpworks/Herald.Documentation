---
title: Kognitos Attack Surface + TesseraSeal Tunable Knobs — Private Strategic Brief
date: 2026-05-22
status: PRIVATE — not for public website; editorial-stage input only
author: Laura (media designer, MMPWorks)
audience: Steve
context_basis: Kognitos novelization Ch01-Ch14 observations corpus + FFIEC chain-of-custody DRAFT-0.2.0 spec
richard_validation: PENDING — dispatch deferred; brief stands on observations-corpus + spec read; Richard's pass should pressure-test items A4 (cross-vendor) and K2 (per-tenant IKM tier) most aggressively
brand_register: private — full bluntness; no public-copy sanding
---

# Kognitos Attack Surface + TesseraSeal Tunable Knobs — Private Strategic Brief
**2026-05-22 — PRIVATE**

Two questions. Five answers each. The corpus (93 speculation anchors, 15 under-reportings, 19 inarticulabilities, 9 on-the-record framework-substitution statements, 27 operational-property invisibilities across 14 chapters) is the ammunition. The reference spec is the contrast. Be honest about both directions.

---

## SECTION 1 — The Five Load-Bearing Attack Vectors

Filtering rule: a load-bearing failing is one where Kognitos's row-shape cannot admit the property *regardless of how an institution fills the twelve fields*. A defender saying "we're a baseline, institutions add what they need" loses because the institution physically cannot add the row. Content-gap failings (where Kognitos could grow into the property with a thirteenth field) are filtered out — they lose to the baseline defense. Only structural row-shape impossibilities make this list.

### A1. The chain-vs-truth boundary is structurally unspeakable

**Failure (one sentence).** Kognitos has no field that distinguishes "the chain proves what the AI said" from "the chain proves the input was true" from "the chain proves the output was accurate" — and that distinction is the load-bearing line in every litigation-defense and public-safety scenario.

**Reference-spec sections that close it.** §1.2 (a) through (e) — five epistemic-scope subclauses; §1.1 Daubert four-factor mapping; §10.13.1 discovery production form; §5.2.1 FRE 902(13)/(14) self-authentication posture.

**Why it's structural, not a content gap.** The §1.2 subclauses are not row attributes — they are *meta-properties of the audit-trail's evidentiary claim*. An institution cannot add the boundary by enriching a row's value; the framework would have to add a *concept* about what the rows collectively prove and do not prove. Kognitos's twelve fields are row-shaped at the event grain. Meta-properties live at the framework grain. The grain mismatch is permanent.

**Engagement class where it matters most.** Litigation defense (FRE 902(13)/(14) self-authentication — Salt Pond Ch10 Naomi); public-safety with dispatch consequences (Pacific Crescent Ch06 Soren); civil-rights consent-to-resolve exposure (Olmstead Ch07 Holland); clinical-trial post-enrollment correction (Helmstad Ch05 — first inarticulability anchor in the program).

**Stakeholder attribution.** Four explicit on-the-record statements across Ch05, Ch06, Ch07, Ch10 — the densest stakeholder convergence on any single failing.

**Website-headline draft.** *"Twelve fields cannot tell the difference between what your AI said and whether it was true. The reference spec can. Your closing argument depends on the difference."*

**Structural or content-gap.** Structural. Permanent. Non-recoverable inside the framework's genre.

---

### A2. Compositional security is field-12-flat

**Failure (one sentence).** Kognitos Field 12 records "a tamper-evident proof exists" as a single binary value, with no field to articulate the HMAC + Merkle + Ed25519 + HSM 128-bit composite-security argument that the proof actually rests on — and the composition argument is what regulators read when threat models scale to nation-state.

**Reference-spec sections that close it.** §1.4 compositional security; §10.5 HSM custody; §10.6.1 IKM generation requirements; §4.1 + §4.2 + §4.3 primitives one through three; §10.17 HSM partition-ceremony attestation.

**Why it's structural, not a content gap.** Composition is the *interaction* between independent integrity layers; it is not a property of any one layer recorded as a value in any one row. Kognitos Field 12's wording — "tamper-evident proof" — collapses the composite into a checkmark. An institution can write "HMAC + Merkle + Ed25519 + HSM" in Field 12's prose under any reading, and the prose becomes documentation, not structured evidence. The framework cannot articulate composition because composition is not field-bearing under a row-grained schema.

**Engagement class where it matters most.** Nation-state threat-class vendor evaluation (NetiVa Ch08 Pankaj — first framework-substitution recommendation in the program); cross-vendor zero-trust composition (Eberhardt × Lumière Ch11 Heinrich + Sébastien — fourth framework-substitution recommendation); HSM custody under sovereign-data residency.

**Stakeholder attribution.** Pankaj's NetiVa statement is the canonical example — he names that the framework "did not carry the engagement's most important findings" and recommends substitution for any vendor at nation-state threat assumption.

**Website-headline draft.** *"Your HSM, your Merkle seal, your MAC chain, and your signature root are four independent integrity layers. Kognitos sees one checkbox. The reference spec sees the composition."*

**Structural or content-gap.** Structural. The collapse from four-layer composite to one-field binary cannot be undone by enriching the row.

---

### A3. Cross-vendor and cross-organizational seams produce zero field-bearing evidence

**Failure (one sentence).** When two chains compose across an organizational boundary — a §10.21 cross-vendor model handover, a §10.40 M&A chain merge, a §10.21.1 sample-based attestation cross-anchor — the byte-equal SHA-256 hash join at the seam is the trust-producing step, and Kognitos has no row for the join because the join is the *interaction* between two chains, not a property of either chain in isolation.

**Reference-spec sections that close it.** §10.21 cross-vendor model-handover schema; §10.21.1 sample-based attestation; §10.21.2 independent-evaluator parallel-chain composition; §10.21.3 registry-discovery cross-anchor; §10.39 institutional successor-attestation; §10.40 cross-vendor chain-merge cross-anchor; §10.41 chain-coverage map M&A temporal-slice extension; §10.42 backfill seal discipline.

**Why it's structural, not a content gap.** Each side of a composition produces its own twelve fields cleanly under Kognitos. The composition itself is what's invisible — it cannot be filed under either side's twelve rows because the composition is not owned by either side. The reference spec admits composition as a first-class concept via the `additional_verifications` markers `cross_vendor_handover_verified` and the §10.42 `backfill_seal_verified`. Kognitos's row-shape cannot reach across to a second chain.

**Engagement class where it matters most.** M&A integration (Northbridge Ch14 — five spec sections compose into one structural exercise); cross-vendor partnerships (Eberhardt × Lumière Ch11 — first joint-vendor engagement in the program); vendor-replacement handovers in regulated industries (Hill Country FCU Ch12 — Total Expert→new-vendor under NCUA AIRES with FRE 902 implications); supply-chain integrity (Salt Pond Ch10 cross-anchor); biotech CDMO handovers; healthcare ML-vendor model handoffs.

**Stakeholder attribution.** Heinrich + Sébastien Ch11 — first cross-vendor partnership joint statement, fourth framework-substitution recommendation. Patrick + Naomi Ch10 — cross-functional executive joint naming cross-vendor institutional anchor as a structural under-reporting.

**Website-headline draft.** *"When two companies share a model, the audit needs to prove the seam. Kognitos audits each side. The reference spec proves the join."*

**Structural or content-gap.** Structural. Composition is not row-shaped under Kognitos and the grain mismatch is permanent.

---

### A4. Multi-tenant cryptographic isolation reads as identical strings

**Failure (one sentence).** Per-tenant IKM cryptographic isolation under §10.1 + §4.1 HKDF makes the same `tenant_id` string across two tenants cryptographically distinct — but Kognitos reads tenant identifiers as strings, and identical strings across two banks read as identical strings.

**Reference-spec sections that close it.** §10.1 IKM registry uniqueness; §4.1 + §4.1.1 session-key handshake + HSM-resident PRK; §4.1.2 vendor-namespaced constants + FFIEC conformance posture; §10.6 + §10.6.1 IKM generation requirements; §10.31 per-cohort subtree disclosure for cohort-grained tenant isolation.

**Why it's structural, not a content gap.** Per-tenant cryptographic isolation is not a value any field carries — it is a property of how the field values *bind to cryptographic material across the chain*. The same `tenant_id = "ACME"` at Bank A and Bank B is two different binding keys under §10.1; under Kognitos it's one string repeated. An institution could write "we use per-tenant HKDF" in a prose field, but the prose is not the proof — the proof is the cryptographic isolation, which the framework cannot read because the framework reads strings.

**Engagement class where it matters most.** Multi-tenant BaaS (Atrio Ch04 Veronika — first framework-substitution-adjacent statement); vendor SaaS at nation-state threat (NetiVa Ch08 Pankaj — 23 customer-banks under 23 per-bank IKMs); white-label platforms; multi-jurisdiction privacy where tenant equals jurisdiction (Sun-Won Ch09); credit-union shared-tenancy under NCUA AIRES; any cross-tenant adversarial-insert scenario.

**Stakeholder attribution.** Veronika Atrio Ch04 — the program's first explicit on-the-record statement, specifically framed on multi-tenant BaaS. Pankaj Ch08 — generalizes to nation-state threat-class vendor evaluation.

**Website-headline draft.** *"Twenty-three customer banks. Twenty-three independent cryptographic keys. Under Kognitos, they all read as the same string."*

**Structural or content-gap.** Structural. The cryptographic isolation lives in the binding, not in the field value.

---

### A5. Framework-cannot-grow is its own meta-property

**Failure (one sentence).** Kognitos's twelve fields are fixed; the reference spec absorbed seven engagement-source amendments in four consecutive chapters via the §12 change-log mechanism (NetiVa §10.17; Sun-Won §4.4 + §4.4.1; Salt Pond §10.19 + audit.external_artifact.*; Eberhardt × Lumière §10.20 + §10.21 plural-array) — institutions on the leading edge of audit-trail design discover findings that the framework cannot evolve into.

**Reference-spec sections that close it.** §12 change-log mechanism (the spec governance discipline itself); every engagement-source amendment listed above is the evidence that the spec moves to meet the work while Kognitos cannot.

**Why it's structural, not a content gap.** This is the meta-shape of every other failing on this list. Kognitos as published is the Kognitos that institutions get. The same checklist Dawn carries today (May 2026) is byte-equal to the checklist she carried at Ch01 (November 2024). Eighteen months of audit work; zero framework adaptations. The framework does not have a §12 mechanism because the framework does not have a §-system at all. A defender saying "we'll add a field for that" cannot demonstrate the discipline by which fields land — the reference spec demonstrates the discipline (engagement source named, errata governance, cross-chapter consecutive evidence). Kognitos cannot match that without becoming a different artifact.

**Engagement class where it matters most.** Any institution on the leading edge of audit-trail design — which is to say, every institution that ever surfaces a finding the framework hasn't seen before. NetiVa nation-state HSM (§10.17 partition ceremony). Sun-Won cross-jurisdiction transfer (§4.4 + §4.4.1). Salt Pond multi-audience reconciliation (§10.19 + audit.external_artifact.*). Eberhardt × Lumière cross-vendor training-data retention (§10.20). Saraswati federated learning at the edge (§10.32, §10.34, §10.35, §10.36, §10.37 cluster).

**Stakeholder attribution.** Pankaj Ch08 names this directly — the partition-ceremony Partial became §10.17 normative within 60 days. Min-seo + Wei-ling Ch09 name the §12 change-log credit explicitly. Heinrich + Sébastien Ch11 cite the seven-amendments-in-four-chapters cadence.

**Website-headline draft.** *"In eighteen months our spec has absorbed seven amendments from real engagements. In eighteen months Kognitos has absorbed zero. Your audit trail is only as good as the framework's willingness to grow."*

**Structural or content-gap.** Structural. The absence of growth governance is the meta-failure that subsumes the other four.

---

### What I cut and why

- **§1.2 (c) source-data lifecycle / pre-chain era** (Helmstad April 15 patient; Sun-Won lookback): I folded this under A1 — it is a subclause of the chain-vs-truth boundary and would dilute A1's punch as a separate item. Strong dimension of A1, not a separate vector.
- **Absence-bearing structural properties** (SDK refusal-at-capture; consent lifecycle-as-state; pre-MAC redaction): defensible as a structural failing, but harder to render in marketing copy without an example the reader has to puzzle out. Strong for the technical paper; not load-bearing in headline copy.
- **Operational events catalog** (§10.2 chain.verification_failure, seal.job_*, etc.): defender can counter with "institutions add operational-events catalogs to their own SIEM." Content-gap-recoverable. Filtered.
- **Multi-axis verdict mechanism** (§10.12 additional_verifications array): too implementation-detailed for marketing; lives in technical documentation.
- **Time-trust grade** (§10.14 PMU vs. NTP): real failing at Pacific Crescent Ch06 but reads as niche to non-utility audiences; folded conceptually into A1's public-safety dimension.

The five I kept are the ones where the structural failure is permanent, the stakeholder evidence is multi-chapter, the engagement classes are commercially load-bearing for Herald.OSS, and the defender's "we're a baseline" counter loses on grain-mismatch grounds.

---

## SECTION 2 — The Five Tunable Knobs

Filtering rule: a tunable knob softens a real cost for a customer who genuinely doesn't need the check, while preserving the verifier's evidentiary discipline. The non-negotiable: the verifier must report which tier/profile it validated, so "verified at Tier 1" is honestly distinguishable from "verified at Tier 3." No silent waivers.

The architectural pattern across the five: **profile flag in the seal record + verifier posture field on the verdict object**. The chain self-describes its tier; the verifier emits the tier on the `posture` field of the verdict object (§10.12 schema's REQUIRED field — currently carries `"ffiec"` or `"vendor:<name>"`; we extend to `"ffiec:tier-N"` or analogous). The verifier validates the full chain at the declared tier; checks scoped to higher tiers are skipped *and the skip is named* on the verdict object.

**SKU placement (Steve, 2026-05-22).** All five tunable knobs (K1-K5) live in **Herald.Enterprise only** — not in Pro. The principle: Pro says "your system won't fall down" (reliability, operational stability); Enterprise adds auditability (the chain-of-custody substrate, the tunable spec-knob structure, the verifier's knob-aware dispatch). Core/Pro deployments operate at implicit defaults with no profile fields emitted on the seal record. Enterprise licenses unlock the profile fields, and the MMP.Licensing payload identifies which profiles the deployment is licensed to declare. A Core/Pro chain that emits a profile field is non-conformant; an Enterprise chain that declares a profile its license does not cover is non-conformant. The verifier reads the license to know which declarations are valid for the chain under test, and the verdict object names the active knob set on every verification. The original per-knob pricing splits below (Core/Pro/Compliance/Edge) are superseded by this rule; the per-knob `Pricing hook` fields are retained as historical record and corrected inline.

### K1. Time-trust grade tunable (PMU-grade vs. NTP-floor)

**Tunable.** §10.14 trusted-time integration. The current spec admits NTP as minimum and PMU-grade GPS-disciplined time as SHOULD-when-applicable. Tunable: a customer declares time-trust grade `ntp_minimum`, `gps_disciplined`, or `pmu_grade` in the seal record.

**Segment that doesn't need it.** Single-tenant on-prem deployments with no public-safety stakes, no millisecond-grade event reconstruction obligations, and no litigation-defense posture requiring time-trust attestation. Internal-operations audit trails. Compliance-floor SaaS where NTP is the regulator-accepted minimum.

**Segment that DOES need it.** Public-safety utilities (Pacific Crescent Ch06 — PMU-grade was load-bearing for dispatch-defense reconstruction); payments rails with sub-second settlement reconstruction; market-surveillance and HFT audit; sovereign-grade timekeeping (defense, intelligence).

**Verifier behavior change.** The seal record carries a `time_trust_grade` field. The verifier reads it on §7 step 1 and dispatches accordingly:
- `ntp_minimum` → verifier validates timestamp monotonicity and bounded drift against NTP-floor tolerance; does NOT validate GPS-disciplined or PMU attestation artifacts.
- `gps_disciplined` → verifier additionally validates GPS-disciplined clock attestation; does NOT validate PMU sub-microsecond bounds.
- `pmu_grade` → verifier additionally validates PMU attestation against utility-grade time-source bindings.

**Verdict object.** The `posture` field carries `"ffiec:time-trust-ntp"`, `"ffiec:time-trust-gps"`, or `"ffiec:time-trust-pmu"`. The `additional_verifications` array emits the corresponding closed-enum marker (`time_trust_grade_ntp_validated`, etc.). On a chain claiming PMU but the verifier reading NTP-minimum scope, the verdict object is FAIL with exit code 1 — claim mismatch is not silently downgraded.

**Pricing hook.** ~~Tiered. Core ships with `ntp_minimum`. `gps_disciplined` is Pro. `pmu_grade` is Compliance-edition (utility/payments-vertical).~~ **Superseded 2026-05-22:** All time-trust grades live in **Herald.Enterprise only**. Core/Pro deployments emit no `time_trust_grade` field and operate at implicit NTP-floor. Enterprise license unlocks the field; the license-key payload names which grades (`ntp_minimum` / `gps_disciplined` / `pmu_grade`) the deployment is licensed to declare. Vertical-targeted bundles (utility, payments) are license-key configurations within Enterprise, not separate editions.

---

### K2. Per-tenant cryptographic isolation tunable

**Tunable.** §10.1 IKM registry uniqueness + §4.1 session-key handshake. A customer declares isolation tier: `single_tenant`, `tenant_grouped`, or `per_tenant_cryptographic`.

**Segment that doesn't need it.** Single-tenant on-prem deployments with one customer's data; small-fleet internal-only AI tooling; pre-launch internal experimentation environments.

**Segment that DOES need it.** Multi-tenant BaaS (Atrio Ch04 — the program's strongest existing positioning); vendor SaaS at nation-state threat (NetiVa Ch08 — 23 customer-banks). **Critical guardrail: this is the tunable most adjacent to a load-bearing attack vector (A4), and softening too aggressively gives ammunition to a competitor.** The customer-segment boundary must be drawn cleanly: cryptographic isolation is the *default* for any multi-tenant deployment; softening is only for *single-tenant* declarations.

**Verifier behavior change.** The seal record carries an `isolation_tier` field. The verifier dispatches:
- `single_tenant` → verifier validates one IKM and its lineage; does NOT validate cross-tenant uniqueness across the registry (because there's only one).
- `tenant_grouped` → verifier validates per-group IKM uniqueness; the chain self-declares groups.
- `per_tenant_cryptographic` → verifier validates the full §10.1 IKM-registry uniqueness invariant across every tenant_id in the chain.

**Verdict object.** The `posture` field carries the tier. The `trust_anchor_manifest_sha256` field still carries the IKM-registry manifest hash (which is the empty-string sentinel under `single_tenant` and a real hash under the multi-tenant tiers). **The verdict object MUST emit a tier downgrade attempt as FAIL** — a chain claiming `single_tenant` that surfaces multiple distinct `tenant_id` strings is a non-conformant declaration and the verifier exits 1.

**Pricing hook.** ~~Core ships with `single_tenant`. `tenant_grouped` is Pro. `per_tenant_cryptographic` (full §10.1 multi-tenant cryptographic isolation) is Enterprise.~~ **Superseded 2026-05-22:** All isolation tiers live in **Herald.Enterprise only**. Core/Pro deployments emit no `isolation_tier` field and operate as implicitly single-tenant. Enterprise license unlocks the field; the license-key payload names which tiers (`single_tenant` / `tenant_grouped` / `per_tenant_cryptographic`) the deployment is licensed to declare. Because of A4's load-bearing role in the attack-vector list, the `tenant_grouped` middle tier requires mandatory CC8.1 documentation of grouping rationale as a license-grant prerequisite (Richard's K2 validation pass also recommends a `cohort_lifecycle_state` chain field — see appendix).

---

### K3. Edge-attestation primitive (gated module)

**Tunable.** §10.35 edge-attestation primitive (Android Keystore TEE / Intel TDX / AMD SEV-SNP / AWS Nitro attestation). Customer declares architecture profile: `central_only`, `edge_capture_no_attestation`, or `edge_attestation_required`.

**Segment that doesn't need it.** Central-only inference paths with no edge tablets, no offline-first ingest, no field-device capture (Hill Country FCU Ch12 — server-side only inference, ran clean across eleven months under central path alone).

**Segment that DOES need it.** Federated learning at the edge with hardware-backed device identity (Saraswati Ch13 — 15,000 ruggedized Android tablets, hardware-backed session keys, monthly federated cycle); IoT sensor fleets (Pacific Crescent Ch06 dimension); medical-device ingest; field-officer mobile workflows in regulated industries.

**Verifier behavior change.** The seal record carries an `edge_attestation_profile`. The verifier dispatches:
- `central_only` → verifier skips §10.35 attestation validation entirely; chain entries with no `audit.edge_attestation.*` rows are conformant.
- `edge_capture_no_attestation` → verifier validates that edge-captured chain entries are present and per-event MAC-bound, but does NOT validate TEE attestation documents.
- `edge_attestation_required` → verifier validates §10.35 attestation documents bind to device hardware-integrity state per the institution's published trust roots.

**Verdict object.** The `posture` field carries the profile. The `additional_verifications` array emits `edge_attestation_validated` or `edge_attestation_waived_per_profile`. **The waiver marker is the load-bearing honesty discipline** — the verifier never silently waives the check; it names it.

**Pricing hook.** ~~Core ships with `central_only`. `edge_capture_no_attestation` is Pro. `edge_attestation_required` is a separately-licensed module (Edge edition) — federated-learning institutions and IoT fleets pay for it because the threat model demands it.~~ **Superseded 2026-05-22:** All edge-attestation profiles live in **Herald.Enterprise only**. Core/Pro deployments emit no `edge_attestation_profile` field and operate as implicit `central_only`. Enterprise license unlocks the field; the license-key payload names which profiles (`central_only` / `edge_capture_no_attestation` / `edge_attestation_required`) the deployment is licensed to declare. The "Edge edition" framing collapses into an Enterprise-license configuration; institutions running federated-learning / IoT / field-officer workflows license the top profile through their Enterprise key rather than purchasing a separate edition.

---

### K4. Late-arriving-entry seal discipline + hierarchical Merkle aggregation (paired tunable)

**Tunable.** §10.36 + §10.37 paired. Customer declares ingest topology: `synchronous_only`, `lag_window_within_24h`, or `lag_window_with_aggregation`.

**Segment that doesn't need it.** Synchronous-only ingest with no offline-first paths, no lag windows, no multi-device subtree aggregation (Hill Country FCU Ch12 again — central-path-only single-substrate single-organization).

**Segment that DOES need it.** Offline-first edge architectures with lag windows up to 15 hours between per-event MAC and central seal (Saraswati Ch13); federated learning with monthly aggregator cycles; field-capture workflows under intermittent connectivity (rural healthcare, mining, oil-and-gas IoT, military forward-deployed); multi-region active-active with cross-region lag.

**Verifier behavior change.** The seal record carries an `ingest_topology_profile`. The verifier dispatches:
- `synchronous_only` → verifier rejects any chain entry whose capture-timestamp diverges from seal-time by more than the synchronous-bound (default: same UTC day); does NOT validate Pattern A supplemental-seal logic.
- `lag_window_within_24h` → verifier validates §10.36 Pattern A supplemental seal at next-day's UTC cut for lag-window entries.
- `lag_window_with_aggregation` → verifier additionally validates §10.37 hierarchical Merkle aggregation (per-device subtree root as leaf in central seal).

**Verdict object.** The `posture` field carries the topology. The `additional_verifications` array emits `late_arriving_seal_verified` and/or `hierarchical_aggregation_verified` as applicable, or `lag_window_discipline_waived_per_profile` under `synchronous_only`. **A chain declaring `synchronous_only` that surfaces an entry with a 15-hour lag is FAIL** — the profile claim and the chain evidence must agree.

**Pricing hook.** ~~Core ships with `synchronous_only`. `lag_window_within_24h` is Pro. `lag_window_with_aggregation` is bundled into the Edge edition (paired with K3).~~ **Superseded 2026-05-22:** All ingest-topology profiles live in **Herald.Enterprise only**. Core/Pro deployments emit no `ingest_topology_profile` field and operate as implicit `synchronous_only`. Enterprise license unlocks the field; the license-key payload names which profiles (`synchronous_only` / `lag_window_within_24h` / `lag_window_with_aggregation`) the deployment is licensed to declare. K4 pairs operationally with K3 — institutions running edge architectures typically need both profiles licensed; the license-key encoding should make the K3+K4 pairing first-class.

---

### K5. Hybrid post-quantum seal + decadal re-sealing (deferred tier)

**Tunable.** §10.53 hybrid post-quantum seal mandate + §10.54 decadal re-sealing discipline + §4.1.3 algorithm agility. Customer declares retention horizon and PQ-readiness tier: `retention_under_7yr_no_pq`, `retention_7_to_25yr_pq_advisory`, or `retention_over_25yr_pq_mandatory_with_decadal_reseal`.

**Segment that doesn't need it.** Short-retention scenarios (sub-7-year regulatory floors with no litigation-defense extension, no FOIA exposure, no decadal-cycle audit obligations). Most commercial SaaS audit-trail use cases at standard 7-year retention with no PQ-readiness obligations land here.

**Segment that DOES need it.** Long-retention regulated industries — clinical trials with 25-year retention (Helmstad Ch05 dimension); defense and intelligence (multi-decade retention); FOIA-bound public-sector workflows; sovereign-data archive obligations; institutional record archives where harvest-now-decrypt-later is a documented threat.

**Verifier behavior change.** The seal record carries a `retention_pq_profile`. The verifier dispatches:
- `retention_under_7yr_no_pq` → verifier validates single-algorithm seals; does NOT enforce hybrid PQ-readiness; does NOT validate decadal re-sealing artifacts.
- `retention_7_to_25yr_pq_advisory` → verifier validates that `payload_hash_alt` (algorithm agility per §4.1.3) is present; does NOT require active PQ-algorithm dual-signature.
- `retention_over_25yr_pq_mandatory_with_decadal_reseal` → verifier validates §10.53 hybrid post-quantum seal AND §10.54 decadal re-sealing artifacts.

**Verdict object.** The `posture` field carries the PQ profile. The `additional_verifications` array emits `pq_hybrid_seal_verified` and `decadal_reseal_verified` at the highest tier. **The honesty discipline: a chain claiming long-retention with no PQ seal is FAIL at the high tier and the operator must downgrade the profile declaration explicitly to PASS at a lower tier.** The chain cannot silently inherit a downgraded posture.

**Pricing hook.** ~~Core ships with `retention_under_7yr_no_pq`. Pro adds `retention_7_to_25yr_pq_advisory`. Enterprise / Compliance-edition adds `retention_over_25yr_pq_mandatory_with_decadal_reseal` (clinical, defense, FOIA, archival institutions).~~ **Superseded 2026-05-22:** All retention-PQ profiles live in **Herald.Enterprise only**. Core/Pro deployments emit no `retention_pq_profile` field and operate at implicit sub-7-year retention with no PQ-readiness obligations. Enterprise license unlocks the field; the license-key payload names which profiles (`retention_under_7yr_no_pq` / `retention_7_to_25yr_pq_advisory` / `retention_over_25yr_pq_mandatory_with_decadal_reseal`) the deployment is licensed to declare. Long-retention regulated industries (clinical, defense, FOIA, archival) license the top profile through their Enterprise key.

---

### What I did not propose as tunable, and why

**Not tunable: §10.1 IKM registry uniqueness as a whole concept.** K2 lets the *isolation tier* be declared, but the §10.1 registry-uniqueness invariant at the declared tier remains non-waivable. If you claim per-tenant, the verifier checks per-tenant. Silently waiving multi-tenant cryptographic isolation while the chain is multi-tenant would surrender attack vector A4 entirely.

**Not tunable: §1.2 epistemic-scope clause.** This is the load-bearing claim from attack vector A1; making it optional in the spec is the marketing equivalent of unilateral disarmament. It is informative-section text; it cannot be "waived" because there is nothing for the verifier to skip — the institution either has the §1.2 clause in its litigation file or it does not. We claim §1.2 closes the gap Kognitos cannot; we cannot then offer a tier that does not include §1.2.

**Not tunable: §1.4 compositional security as a security argument.** Same as §1.2 — informative, the foundation for attack vector A2, and the basis on which the four-primitive composition is read together. Customers can decline to operate at high cryptographic threat, which is what K2 and K5 give them; they cannot decline §1.4 as the *security model under which their tier is read*.

**Not tunable: §10.12 verifier CLI exit-code contract.** The honesty discipline of the verdict object is the load-bearing trust-producing artifact. Tunability of *what gets verified* never extends to tunability of *how the verifier reports what it verified*. The posture field, the additional_verifications array, and the closed-enum marker discipline are non-negotiable across all tiers.

---

## Editorial notes for Steve

**Cross-cuts and tensions you specifically asked about.**

The single sharpest cross-cut is between attack vector **A4 (multi-tenant cryptographic isolation reads as identical strings)** and tunable knob **K2 (per-tenant cryptographic isolation tunable)**. We are claiming, on the website, that Kognitos cannot articulate cryptographic tenant isolation — and simultaneously offering customers the option to *waive* that isolation under a `single_tenant` profile. The defensible posture: K2's waiver is gated to *genuinely single-tenant* deployments only; the verifier's tier downgrade attempt (a `single_tenant` chain with multiple distinct tenant_ids) is FAIL with exit code 1. **The brand-promise duality is intact here only if K2's customer-segment boundary holds**: the single-tenant tier is for institutions that physically have one customer's data, not for multi-tenant institutions choosing to skip the check. I would consider tightening K2 further before public release — specifically, marking the `tenant_grouped` middle tier as "Pro with mandatory CC8.1 documentation of grouping rationale" so it cannot become a sliding-scale loophole.

Less tense but worth naming: **A5 (framework-cannot-grow)** vs. our own tunable-knob discipline. We're making a marketing claim that Kognitos's twelve fields are fixed and the reference spec absorbs amendments via §12 governance. Our tunable knobs are profile flags on the seal record — they extend the spec additively (closed-enum marker additions to §10.12; profile fields in §10.x) and the §12 mechanism is the discipline by which those additions land. So far, intact. **The trap to avoid**: if a tier downgrade becomes the easiest path for new customer acquisition, the spec accumulates softening pressure that the §12 mechanism is designed to resist. Periodic editorial discipline — quarterly review of which tiers customers are actually selecting, and whether the segment-boundary rationale still holds — is worth building into product governance from launch.

Two other notes the brief did not surface but that you should weigh:

(1) **The attack-vector list is denser on litigation-defense and public-safety / nation-state engagement classes than on the bread-and-butter mid-market**. That is the truthful read of where Kognitos breaks worst — those are the highest-stakes inarticulability scenarios — but it does mean the website copy may read as enterprise-only. Whether that's a problem depends on Steve's go-to-market: if Herald.OSS is positioning as "the framework that wins when the stakes are real," the density is a feature, not a bug. If positioning is broader, A4 (multi-tenant) and A5 (framework-cannot-grow) are the two that generalize down-market.

(2) **Richard's validation pass is genuinely pending** — I deferred his dispatch because the brief's load-bearing claims are observable from the corpus + spec without a deep architectural read. He should specifically pressure-test A4 (the cryptographic-isolation reads-as-strings claim) for whether the framework-cannot-grow defense at the marketing level survives a sophisticated competitor architect; and K2 (the single-tenant tier's waiver discipline) for whether the FAIL-on-tier-mismatch invariant holds under all edge cases (cross-region replicas; tenant deletion across seal boundaries; tenant-id collision under HKDF). His pass should land before public copy ships.

**The brief is private. Bluntness preserved. Public copy will be sanded.**

---

## Richard's Validation Pass — A4 + K2 — 2026-05-22

Two pressure-tests landed before website copy gets drafted off the brief. Both load-bearing, both worth running honestly because the alternative is reading the counter-argument in a competitor blog.

### A4 — Multi-tenant cryptographic isolation reads as identical strings

**Verdict: HOLDS — with one framing sharpening.**

The Kognitos defender's strongest wordsmith move is exactly the one the prompt names: Field 3 (human-user identity verified) and Field 12 (tamper-evident proof) together require cryptographic tenant isolation as an implementation detail; institutions just do that. Walked maximally charitably, the defender argues that any institution shipping a multi-tenant audit-trail under Kognitos *would* operate per-tenant HKDF because Field 12's tamper-evident proof obligation forces it — therefore A4 is an implementation detail Kognitos institutions already do rather than a framework gap.

That argument loses on two distinct grounds, and they're worth keeping straight because they answer two different versions of the rebuttal.

**Ground 1 — Field-extension wording cannot reach into binding-grain.** Kognitos's twelve fields are row attributes at the event grain. Per-tenant cryptographic isolation under §4.1 + §10.1 is not a value any row carries; it is a *property of how field values bind to cryptographic material across the chain*. The HKDF derivation `info_for_tenant = HKDF_INFO_BASE || "|" || utf8(tenant_id)` lives in the SDK's key-derivation routine, not in any row. An institution writing "we use per-tenant HKDF" in Field 12's prose produces *documentation*, not *structured evidence* — the prose is unverifiable from the chain. The reference spec produces structured evidence via the per-entry `key_fingerprint` (§10.1 P-6 reconciliation), the seal record's `hkdf_inputs_digest`, and the verifier's per-tenant IKM lookup at §7 step 7. The Kognitos defender cannot wordsmith binding-grain into row-grain — the grain mismatch is permanent.

**Ground 2 — The load-bearing attack is the cryptographic refusal at insert-time, not the existence of per-tenant key derivation.** This is the framing sharpening the brief should adopt. The Atrio Ch04 multi-tenant BaaS adversarial-insert exercise and NetiVa Ch08 23-bank-scale variant don't just demonstrate "we have per-tenant keys"; they demonstrate that **a forged cross-tenant insert fails at MAC verification (§7 step 9 `payload_hash MAC mismatch at seq N`) AND at the structural cross-chain-lift check (§7 step 4 `cross-chain lift detected at seq N`)** — the chain's two-layer defense rejects the insert mechanically, at insert-time, without any institutional discipline involved. A Kognitos defender invoking "implementation detail" is invoking institutional discipline (a policy that institutions chose to apply HKDF). The reference spec invokes a *structural property* (the SDK refuses non-conformant inserts at the cryptographic primitive layer, and the verifier refuses non-conformant chains at the verification layer). Those are different epistemic claims. The defender's "institutions already do it" is unverifiable from the row; ours is verifiable from the §7 verifier walk plus the verdict object's posture field plus the `trust_anchor_manifest_sha256` binding.

**The sharper attack-vector framing.** Drop the headline's "23 banks, 23 keys, 1 string" formulation and replace with the refusal-property framing:

> Under Kognitos, a forged cross-tenant insert is rejected by institutional discipline (if the institution wrote a discipline). Under the reference spec, it is rejected by the verifier at §7 step 4 before any MAC compute. Discipline can fail. The cryptographic refusal cannot.

That framing makes the defender's "implementation detail" rebuttal recoil on itself — they're invoking discipline; we're invoking a structural property of the verification pipeline.

**One-sentence response to the implementation-detail defender.** If it's an implementation detail Kognitos institutions already do, name the row that records it — and name the verifier whose §7 walk refuses the chain when it isn't.

The defender has neither. A4 holds.

---

### K2 — Per-tenant cryptographic isolation tier (FAIL-on-mismatch invariant)

**Verdict: HOLDS on cases 1 and 3. NEEDS A FOURTH CASE for case 2 (tenant deletion). The middle tier `tenant_grouped` needs more than CC8.1 documentation — it needs a structural invariant.**

Walking the three cases honestly.

#### Case 1 — Cross-region replication

**Dispatch path.** The spec already closes this at §10.1 (multi-deployment uniqueness enforcement, normative) and §10.15 (Pattern A vs. Pattern B). Cross-region replication does NOT operate per-region IKM registries — it operates a single global IKM registry across deployments. Under Pattern A (shared chain across regions), the verifier walks the seal region's ledger; per-event MAC verification succeeds because the session_key is derived from the same IKM registered globally, not from region-local material. The HKDF derivation context is NOT something the replica can "structurally lose" — it's reconstructed by the verifier at §7 step 7 from `(tenant_id, key_version)` against the IKM registry manifest, and the manifest hash is bound into the verdict object's `trust_anchor_manifest_sha256` field. The verifier's posture-field claim of `per_tenant` is honest precisely because the manifest binding is what proves per-tenant isolation, not the region the bytes happen to live in.

**Where a Kognitos defender might probe.** But the institution might run a per-region IKM registry — surely the verifier accepts the chain as-if-per-tenant when it's actually per-region? The §10.1 multi-deployment-uniqueness rule (normative) explicitly forbids per-region registries under a single institution; an institution operating that pattern is non-conformant and the verifier's §7 step 8 fingerprint check catches the cross-region key confusion (a session-key collision would produce MAC matches against the wrong tenant's IKM). The institutional non-conformance surfaces structurally, not silently.

**Verdict on case 1: K2 holds.** The verifier dispatch path is: posture-field claim `per_tenant` then manifest hash bound to verdict then §7 step 7 IKM lookup against global registry then §7 step 8 fingerprint check catches any per-region confusion. No path where the verifier accepts a tier the chain has structurally lost.

#### Case 2 — Tenant deletion with historic entries

**This is the case that needs work.** A `tenant_grouped` customer deletes a cohort. The chain retains historic entries under the deleted cohort's HKDF context. Six months later the verifier runs against entries that were valid at write-time but reference a now-deleted cohort.

**The spec's existing answer.** §10.9 IKM registry retention is normative and explicit: the tenant key registry MUST retain every IKM generation for at least as long as any chain entry stamped with that `key_version` is retained. A `master_key.retired` operational event under §10.2 marks the moment an IKM is removed; the retention coupling is enforced at the registry layer with an explicit override required to retire an IKM whose `key_version` is still referenced.

**The gap K2 exposes.** §10.9 covers IKM retention. It does NOT cover the case where the *cohort grouping itself* changes — a `tenant_grouped` customer who deletes the cohort `acme-cohort-A` is operating at the cohort-grouping layer, not the IKM layer. The IKM may still be in the registry (per §10.9), but the cohort's HKDF derivation context — the bytes that went into `info_for_cohort` — is institutional metadata. If the institution simply forgets which IKM-version belonged to `acme-cohort-A`, the verifier sees `unknown key_version: no IKM for (cohort=acme-cohort-A, key_version=V) at seq N` and FAILs — which is the correct dispatch (FAIL is more honest than silent acceptance), but the FAIL reads as a chain-integrity failure rather than a cohort-management failure.

**The mismatch path that needs explicit handling.** Customer declares `tenant_grouped`. Customer deletes cohort `acme-cohort-A` from operational records but the chain retains entries from that cohort. Six months later:

- If the IKM is retained (§10.9 compliance), the verifier walks cleanly and emits PASS with posture `ffiec:isolation-tenant-grouped`. *But the customer no longer has institutional knowledge of what `acme-cohort-A` referred to.* The PASS is structurally correct but operationally orphaned.
- If the IKM is NOT retained (§10.9 violation), the verifier emits FAIL at §7 step 7. The FAIL is correct but the customer reads it as "the chain broke," not "we violated §10.9 by retiring an IKM whose entries still exist."

**Recommendation: K2 needs a fourth case named explicitly — `tenant_grouped_with_deleted_cohorts`.** The verifier dispatch:

- The seal record carries an `isolation_tier` plus a new `cohort_lifecycle_state` field with values `active`, `cohort_deleted_ikm_retained`, or `cohort_deleted_ikm_retired`.
- A chain claiming `tenant_grouped` with `cohort_lifecycle_state = cohort_deleted_ikm_retained` PASSes with posture `ffiec:isolation-tenant-grouped-with-retired-cohorts` and the `additional_verifications` array emits `cohort_lifecycle_seen_at_seq_N` per cohort-deletion event observed.
- A chain claiming `tenant_grouped` with `cohort_lifecycle_state = cohort_deleted_ikm_retired` FAILs at §7 step 7 with a more honest message: `ikm_retired_for_active_chain_entry: cohort=C, key_version=V, retired_at=T` — making the §10.9 violation legible to the operator.

The middle-tier discipline Laura recommended (mandatory CC8.1 documentation of grouping rationale) is necessary but insufficient — the cohort-lifecycle state is *also* a structural invariant the chain must self-declare. CC8.1 prose alone is institutional discipline (the same epistemic class as the Kognitos defender's implementation-detail rebuttal). The structural invariant lives in the seal record.

#### Case 3 — HKDF collision under malformed IKM

**Dispatch path.** Two `single_tenant` customers happen to derive the same session key. This requires either (a) identical IKM bytes — vanishingly improbable under §10.6.1 conformant RNG, structurally impossible under §10.1 IKM registry uniqueness within an institution, but possible *across* institutions because each operates its own registry — or (b) HKDF input collision under malformed IKM.

**Under §10.1, case 3 sub-case (a) is conformant.** Two different institutions, two different IKM registries, two `single_tenant` customers. The HKDF output may happen to collide (the birthday bound on 256-bit HKDF output is 2^128 — infeasible) but each institution's verifier reads only its own institution's chain. There is no shared verifier walk; the collision is not detectable across institutions and does not need to be. **K2's tier claim does not get exploited by this — the tier is per-institution.**

**Under §10.1, case 3 sub-case (b) — malformed IKM producing same session key.** This is what the §10.1 IKM registry uniqueness rule is designed for. The registry MUST reject duplicate `tenant_id` values; the registry-layer uniqueness check is non-waivable across all K2 tiers. A `single_tenant` customer cannot, by definition, surface a duplicate `tenant_id` collision — there's only one tenant. Under `tenant_grouped` or `per_tenant`, the §10.1 enforcement catches the duplicate at registration time, not at verifier-time.

**The verifier's §7 step 8 fingerprint check is the cryptographic backstop.** Even if the registry somehow accepted a duplicate (institutional non-conformance), a session-key collision would produce MAC matches against the wrong tenant's IKM, and the fingerprint check catches it. K2's tier claim is *upstream* of this — the registry uniqueness invariant runs regardless of the declared tier.

**Verdict on case 3: K2 holds.** The §10.1 IKM registry uniqueness is the structural backstop independent of K2's tier declaration. K2 lets the *scope* of the uniqueness check vary by tier (`single_tenant` checks one IKM; `per_tenant` checks every IKM); it does not let the *invariant itself* be waived.

#### Summary verdict on K2

K2's FAIL-on-mismatch invariant holds on cases 1 and 3 cleanly. Case 2 (tenant deletion) needs the additional `cohort_lifecycle_state` invariant in the seal record — CC8.1 prose alone is insufficient because cohort-lifecycle is operational metadata that needs to be chain-bound to remain legible to the verifier. **The middle tier `tenant_grouped` needs a structural invariant, not just documentation.**

**The one-sentence response when a competitor says your tier system has a silent-failure mode under tenant deletion.** The §10.9 IKM retention rule already binds the verifier to FAIL when an entry's IKM is missing; the cohort-lifecycle state field makes the FAIL message name cohort-management as the root cause instead of reading as chain corruption.

That's the difference between a fail-closed system that confuses operators and a fail-closed system that teaches them what went wrong. The K2 sharpening lands the second.

---

**Both pressure-tests preserve the brand-promise duality.** A4's structural-property framing is the forward-optimism (cryptographic refusal is mechanically stronger than discipline) plus the plainspoken honesty (discipline can fail). K2's tenant-deletion sharpening is the same — fail-closed verifiers that name the root cause are more useful than fail-closed verifiers that produce opaque integrity errors. The website copy can ship after the K2 fourth-case is folded into the spec (or noted as a v1.x roadmap item with an interim verifier message that names cohort-lifecycle explicitly).
