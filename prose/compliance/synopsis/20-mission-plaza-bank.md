# Story 20 — Mission Plaza Bank (Texas community bank, partial-deployment stand-up; Dawn's last Lead-Auditor engagement; wedding bookend)

**Story file:** `docs/auditor-stories/20-mission-plaza-bank.md`
**Engagement type:** Three-day deployment-confirmation engagement at a Texas community bank that stood up a partial TesseraSeal deployment six months ago on the AI-decisioning surface only; closes the recusal protocol's third-party-vendor frame for the audit team
**Posture going in:** Partial TesseraSeal in production for six months on the AI-decisioning surface (account-opening fraud screening, real-time credit-decisioning); marketing surface not yet chained; institution operates on a Jack-Henry-centric community-banking stack (Banno digital banking, Symitar NetTeller legacy online banking, JHA Payment Solutions, Yello account-opening CRM, Insider marketing automation, ASP.NET app stack, Splunk SIEM); AWS-resident; Herald.Core.Aws runs the partial chain
**Outcome posture:** Confirmation of the partial deployment + scope-expansion memo for the marketing-surface extension; Dawn's last Lead-Auditor engagement before her transition to MMPWorks; personal-arc bookend (Steve and Dawn marry the Saturday after engagement close)

## Type of audit
Three-day on-site at Mission Plaza Bank's San Antonio operations center for a deployment-confirmation pass on the six-month-old partial TesseraSeal stand-up. The engagement is scoped to (1) confirm that the partial AI-decisioning chain holds at every operational surface where it currently runs, (2) produce a scope-expansion memo recommending the marketing-surface extension to cover the Insider + Yello footprint, and (3) close out the recusal-protocol third-party-vendor frame on Dawn's last engagement as Lead Auditor — Steve appears under final-form recusal for a single §10.21 technical question on Day 2 by video bridge; Tom logs the engagement-letter recusal sunset; Dawn signs the partner-letter close-out as Lead Auditor for the last time. The wedding follows the engagement: small ceremony on the Saturday following Day 3, attended by the team in personal capacities.

## Interested parties (spec readers)
- **FDIC IT Examiner** — Mission Plaza's prudential supervisor; the institution is FDIC-insured and Texas state-chartered; the spec-section confirmation memo is shaped for the next FDIC IT examination cycle
- **Texas Department of Banking** — State-chartered Texas community bank co-supervisor; reads the deployment posture for the upcoming state IT examination
- **CFPB consumer-protection examiner** — UDAAP and §1033 surface on account-opening fraud screening
- **Mission Plaza Chief Audit Executive** — The CAE who stood up the partial deployment six months ago; consumes the confirmation memo and the scope-expansion recommendation
- **Mission Plaza Chief Risk Officer** — Owns the AI-decisioning model risk; consumes the §10.13 evidentiary composition with the institution's SR 11-7 workpapers
- **Mission Plaza Chief Information Officer** — Owns the Jack Henry stack and the AWS substrate; receives the marketing-surface scope-expansion architecture
- **Mission Plaza Chief Marketing Officer** — Owns the Insider + Yello marketing-AI footprint; will be the institutional sponsor of the marketing-surface extension recommended in the engagement memo
- **Mission Plaza M&A integration officer** — Carrying institutional awareness that a regional-acquirer conversation is in the air (not yet announced); the marketing-surface scope-expansion recommendation is sized with that future in mind
- **Jack Henry vendor-engineering liaison** — Banno + Symitar + JHA Payment Solutions integration; receives the SDK-side notes on the §10.21 hooks for downstream cross-vendor handover scenarios
- **Insider vendor-engineering liaison** — Marketing-AI vendor; receives the scope-expansion memo's §10.21 hooks at the Insider→Salesforce-FSC handover surface that will become relevant if the M&A conversation matures
- **Yello vendor-engineering liaison** — Account-opening journey; receives the §10.21 hooks at the account-opening-to-core handover surface
- **Verifier implementer** — Production verifier on the partial chain; readies the dispatch path for the marketing-surface extension

## Top spec sections used
- **§10.21** — Cross-vendor model-handover (the headline; six months in production on the AI-decisioning surface; the scope-expansion memo extends it to the marketing surface)
- **§10.13** — Evidentiary artifacts composition with the institution's SR 11-7 model-risk workpapers
- **§10.11.1** — `audit.ecoa.adverse_action.*` family; the AI-decisioning surface's adverse-action records
- **§10.69** — Per-customer audit-trail subset disclosure; CFPB §1033 right at a community-bank scale
- **§10.19** — Chain-coverage boundary documentation; the partial-deployment scope is declared explicitly as `pattern_2_partial_coverage_with_named_scope` under the §10.19 coverage-pattern enumeration, with a documented scope-expansion path. Also reserved for the marketing-surface extension's Insider campaign-history hash-anchoring via the `audit.external_artifact.*` family

## All cited spec sections
- **§0.5.1** — Three-paragraph elevator pitch for community-bank executive orientation
- **§1.1** — Daubert four-factor grounding
- **§1.2** — Epistemic scope
- **§4** — Four primitives; partial-coverage chain entries are spec-conformant in their scope and not spec-conformant beyond their scope; the §10.41 coverage map encodes that boundary explicitly
- **§4.1** — Per-tenant HKDF binding
- **§4.2** — Daily Merkle seal default cadence; production cadence on AWS CloudHSM `us-east-1`
- **§4.3** — HSM-rooted root signature
- **§7** — Twelve-step verifier procedure
- **§10** — Operational requirements
- **§10.5** — HSM custody at FIPS 140-2 Level 3+
- **§10.11.1** — ECOA adverse-action family
- **§10.13** — Evidentiary artifacts and SR 11-7 composition
- **§10.17** — Partition-ceremony attestation; dual-signature pair (vendor + institution) on the partial-deployment stand-up
- **§10.19** — Chain-coverage map; declares the partial-deployment scope under the coverage-pattern enumeration as `pattern_2_partial_coverage_with_named_scope`; the institution's CC8.1 names the in-scope and out-of-scope systems and the evidentiary substitutes; `audit.external_artifact.*` family reserved for marketing-surface extension
- **§10.21** — Cross-vendor model-handover; production on AI-decisioning surface; scope-expansion candidate for marketing surface
- **§10.40** — Cross-vendor chain-merge anchor; referenced in the scope-expansion memo as the primitive that will bind the future Insider→whatever-acquirer-marketing-stack handover. Substrate-agnostic per the §10.40 clarifier — the byte-hash binding mechanism is indifferent to whether the foreign chain is AWS-resident, Azure-resident, or otherwise
- **§10.41** — Referenced only in the scope-expansion memo's forward-dated M&A consideration (if a future acquirer arrives, §10.41's three-partition temporal map covers the cut-over); NOT exercised in this engagement (institution not yet under M&A)
- **§10.69** — Per-customer audit-trail subset disclosure
- **§13** — Stakeholder navigation; "Texas community bank with partial TesseraSeal deployment on AI-decisioning surface, Jack Henry stack, AWS-resident" becomes a canonical stakeholder entry

## Synopsis

### Audit activity
Day 1 walks the partial AI-decisioning chain end-to-end. Mission Plaza is a $3.2B Texas community bank with a typical Jack-Henry-centric stack: Banno for digital banking, Symitar NetTeller for legacy online banking, JHA Payment Solutions for payments, Yello for account-opening CRM, Insider for cross-channel marketing automation. The institution's CAE stood up TesseraSeal six months ago on the AI-decisioning surface only — account-opening fraud screening (~3,400 applications/month) and real-time credit-decisioning (~1,800 decisions/month). Marketing-surface AI activity (next-best-action under Insider, ~340,000 monthly customer touchpoints) is not yet chained. The §10.19 chain-coverage map declares the partial deployment under the coverage-pattern enumeration as `pattern_2_partial_coverage_with_named_scope` — the institution's CC8.1 names the scope (AI-decisioning surface, AWS-resident) and the systems explicitly out of scope (marketing surface, Banno digital-banking surface, Symitar NetTeller). The audit walks five end-to-end account-opening cases and five credit-decisioning cases; all ten verify clean within the declared scope. The verifier emits `partial_coverage_pattern_2_verified` per §10.12 alongside exit code 0.

Day 2 morning walks the scope-expansion architecture for the marketing surface. The CMO joins the room with the Insider product manager on a video bridge. The §10.21 cross-vendor model-handover surface is the structural primitive: each Insider-driven marketing event would be hash-anchored into the chain at emission, and the marketing-event-to-credit-decision pivot (covered today in §10.11.1's adverse-action records) would resolve cleanly across the handover. Steve joins at 11:00 by video bridge for twenty minutes to answer a specific question about how the §10.21 surface composes with Insider's internal model-versioning cadence; he confirms; he signs off. The recusal log entry is filed by Tom at 11:25. The afternoon walks §10.69 per-customer disclosure across the partial scope.

Day 3 closes the engagement with the spec-section confirmation memo, the scope-expansion memo, and the partner-letter close-out. The confirmation memo cites §10.21, §10.13, §10.11.1, §10.69, and §10.19 (declaring `pattern_2_partial_coverage_with_named_scope` under the coverage-pattern enumeration). The scope-expansion memo recommends extension to the marketing surface in two phases: Phase A (Insider event-anchoring under §10.21, three months) and Phase B (full marketing-surface chain coverage with cross-vendor anchor primitives in place for any future regional-acquirer scenario, six additional months). The Mission Plaza CAE accepts both memos; the CMO signs the Phase A budget approval on Day 3 afternoon.

The wedding is the Saturday following Day 3 — small private ceremony, team members attending in personal capacities. Tom's toast is short. The engagement letter for the next Mission Plaza engagement (eight months out, intended to be the marketing-surface deployment confirmation) is signed two weeks later with Raj on the partner line as new Lead Auditor and Dawn explicitly named as the MMPWorks vendor-side liaison for any §10.21-touching technical question.

### How the spec was used
- **§10.21** — Production on the AI-decisioning surface for six months; the scope-expansion memo extends it to the marketing surface in two phases. Steve's twenty-minute video appearance addresses one specific §10.21 question about composition with Insider's internal model-versioning cadence; recusal protocol is logged for the last time under the third-party-vendor frame
- **§10.19** — Chain-coverage map declares the partial-deployment scope under the coverage-pattern enumeration as `pattern_2_partial_coverage_with_named_scope`; the partial deployment is spec-conformant inside its named scope and not beyond it; the institution's CC8.1 names the scope, the systems explicitly out of scope, and the evidentiary substitutes. The scope-expansion memo's two phases are forward-dated coverage-pattern transitions (Phase A → `pattern_2_partial_coverage_with_named_scope` with marketing surface added; Phase B → `pattern_1_full_coverage`)
- **§10.13** — Evidentiary composition with Mission Plaza's SR 11-7 model-risk workpapers; the AI-decisioning surface is producing the chain entries that the institution's MRM committee was already collecting in PDF form
- **§10.11.1** — ECOA adverse-action records on the AI-decisioning surface; ten cases walked, all clean
- **§10.69** — Per-customer disclosure across the partial scope; one walked CFPB §1033 disclosure (a member of two years' tenure with no marketing-AI exposure under the current partial scope) returns one unified trail in the chain's coverage
- **§10.40 (referenced, not exercised)** — The scope-expansion memo names §10.40 as the future primitive for any Insider→acquirer-marketing-stack handover; the cross-cloud generalization question is preserved as the standards-body wishlist seed from Story 12

### Results
Two memos delivered: (1) spec-section confirmation memo confirming the partial AI-decisioning chain holds at every named surface with no findings; (2) scope-expansion memo recommending the marketing-surface extension in two phases with Phase A budget approved on Day 3 afternoon. Mission Plaza becomes a canonical stakeholder entry for "Texas community bank with partial TesseraSeal deployment on AI-decisioning surface, Jack Henry stack, AWS-resident" in §13. The recusal protocol's third-party-vendor frame closes for the audit team as Dawn's last Lead-Auditor engagement; the engagement letter for the next Mission Plaza pass names Raj as Lead Auditor and Dawn as MMPWorks vendor-side liaison. Engagement closes 16% under budget. The marketing-surface extension stands up in Phase A on the timeline recommended in the scope-expansion memo; Phase B becomes structurally relevant when Brazos Federal's acquisition of Mission Plaza closes nine months later, at which point the partial-marketing-surface chain is what allows the cross-cloud reconciliation walked in Story 21.
