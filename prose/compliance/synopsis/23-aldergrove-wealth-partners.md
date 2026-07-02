# Story 23 — Aldergrove Wealth Partners (FINRA-member broker-dealer ahead of a FINRA cycle examination)

**Story file:** `docs/auditor-stories/23-aldergrove-wealth-partners.md`
**Engagement type:** Pre-examination readiness pass before a FINRA cycle examination of the firm's AI systems
**Posture going in:** Chained in production for 10 months across two AI surfaces (rep-assist recommendation copilot + client-communications chatbot/email); the firm is exam-ready but nervous because there is no FINRA AI rule to point at
**Outcome posture:** CONFIRMATION; no purpose-built spec-section family exercised — confirms the chain's foundational capabilities satisfy a requirement set appropriated from settled SEC rule text plus FINRA's technology-neutral posture; one documented-open regulatory question; one scope note; no findings

## Type of audit
Two-day pre-examination readiness pass at the firm's Richmond home office before a FINRA cycle examination of its Gen-AI systems. The deliverable is a spec-section confirmation memo — structured as a citation map, every AI-readiness requirement pinned to the rule that carries it — handed to the CCO before the exam opens. The firm runs Gen AI on two surfaces: a rep-assist recommendation copilot (an agent that pulls holdings/profile, runs a suitability check, retrieves research, and drafts a recommendation a registered rep reviews before delivery) and a client-communications surface (portal chatbot + AI-drafted client emails). The distinctive tension: this is the team's first **SRO-flavored** engagement (FINRA is a self-regulatory organization, not a government agency), and there is no FINRA AI rule — the requirement set is appropriated from SEC rule text (17a-3/17a-4, Reg BI) and FINRA's own technology-neutral rules (4511, 3110, 2210), armed with the 2026 Annual Regulatory Oversight Report's GenAI expectations. The recurring question is *"which rule actually says that?"* — answered with precision every time.

## Interested parties (spec readers)
- **FINRA cycle examiner** — Reads the firm's AI systems against existing rules; consumes the citation-map memo first
- **SEC recordkeeping examiner** — 17a-3/17a-4 books-and-records; the 17a-4(f) audit-trail alternative
- **Chief Compliance Officer** — Owns the FINRA relationship; needs the rule-by-rule confirmation and the honest gaps before the examiner finds them
- **Designated supervisory principal** — Rule 3110 supervision of the AI-assisted recommendation process
- **FINRA regulatory counsel** — The 17a-4(f) citation chain; the RN 25-07 open question posture; 2210 classification
- **Chief Risk / Model Risk chair** — Model-version provenance, documented testing, deployment-intent capture for the copilot
- **Standards-body reviewer** — The appropriated-requirement pattern (FFIEC discipline == SEC audit-trail alternative) feeds the cross-regulator navigation
- **SDK implementer** — Agent-action capture (one chain entry per tool-call under the session run_id)
- **Verifier implementer** — Recommendation-lineage walk; principal-approval reconciliation; four-tuple resolution

## Top spec sections used
- **§4** — The four primitives; the audit-trail alternative by construction (per-event MAC + Merkle seal + HSM signature)
- **§7** — Twelve-step verifier procedure; recreates an original record byte-equal or proves alteration (the 17a-4(f) recreation requirement)
- **§10.47** — Four-tuple binding (prompt/context/output/model-version); satisfies the 2026 report's prompt/output-logs + model-version-provenance expectations
- **§14** — Generation and human-in-the-loop; the rep review event + principal pre-approval (3110 supervision + 2210 approval)
- **§10.11.1** — Parent-linkage; the recommendation lineage for Reg BI (session → holdings → profile → suitability → draft → review → delivery)
- **§10.13** — Evidentiary-retention floor inventory; the 17a-4 retention categories
- **§10.19** — External-artifact binding; documented testing evidence hash-bound
- **§10.21.4** — Vendor-version-registry; model-version-card provenance

## All cited spec sections
- **§0.5.1** — Three-paragraph elevator pitch for executive-level orientation
- **§4** — Four primitives; audit-trail alternative by construction
- **§7** — Twelve-step verifier procedure; original-record recreation
- **§10.11.1** — Prior-decision / recommendation parent-linkage
- **§10.12** — Verifier exit-code contract (0 PASS)
- **§10.13** — Evidentiary-retention floors (17a-4 categories)
- **§10.19** — External-artifact binding (testing evidence)
- **§10.21.4** — Vendor-version-registry (model-version-card provenance)
- **§10.47** — Four-tuple binding (prompt/context/output/model-version)
- **§14** — Generation and human-in-the-loop review/approval

## Regulatory citations (the appropriated requirement set)
- **SEA 17a-3 / 17a-4** — Books and records; **17a-4(f) audit-trail alternative** (2022 amendments, effective Jan 2023, compliance May 2023): a complete time-stamped audit trail permitting recreation of an original record if altered or deleted — the settled anchor the chain satisfies by construction
- **FINRA Rule 4511** — Books and records; incorporates the SEC recordkeeping rules by reference
- **FINRA Rule 3110** — Supervision; failure-to-supervise-the-algorithm is the realistic enforcement shape, never an "AI rule" violation
- **FINRA Rule 2210** — Communications; retail-communication principal pre-approval (>25 retail investors in 30 days)
- **SEC Regulation Best Interest** — AI-generated recommendation is still a recommendation; obligations sit with the firm
- **FINRA RN 24-09** — Technology-neutral AI guidance
- **FINRA RN 25-07** — Rule modernization; raised whether AI outputs are "business as such" records (the documented-open question)
- **2026 FINRA Annual Regulatory Oversight Report** — GenAI section; exam expectation, not rule text

## Synopsis

### Audit activity
Day 1 walks the rep-assist copilot architecture: an agent that logs one chain entry per tool-call (holdings pull, profile pull, suitability check, research retrieval, draft generation) plus a human review event and a delivery/discard event, all under one `run_id`, ~8-12 entries per session, ~3,000 sessions/day across 900 reps. Daily seal at 03:00 UTC (not Wasatch's clock — a wealth-management recommendation doesn't need a per-second seal).

The day proceeds requirement by requirement, each pinned to the rule that carries it: the recordkeeping hook (4511 → 17a-3/17a-4 → the 17a-4(f) audit-trail alternative), Rule 3110 supervision, the enforcement shadow (3110 failure-to-supervise, on the Interactive Brokers / Brex analogue pattern), the lunch conversation on the open RN 25-07 question, Rule 2210 communications, Reg BI recommendation lineage, and the 2026 report's four GenAI + four AI-agent expectations mapped to chain capabilities. Day 2 runs a ten-recommendation + ten-communication reconciliation slate and finalizes the citation-map memo by 3 PM Thursday.

### How the spec was used
- **§4 + §7** — The chain is the 17a-4(f) audit-trail alternative by construction; the verifier recreates an original record byte-equal or proves alteration
- **§10.13** — Carries the 17a-4 retention-floor inventory; entries under compliance-mode object lock exceeding the longest category
- **§14** — Binds the rep review event and the principal pre-approval under authenticated identity (3110 supervision + 2210 approval); approved-content hash equals sent-content hash; approval precedes send
- **§10.11.1** — Walks the recommendation lineage transitively for Reg BI (session → delivery), with the rep's review-and-edit bound inside the lineage
- **§10.47** — Four-tuple binding satisfies the 2026 report's prompt/output-logs and (with the `model_version` field + §10.21.4) model-version-provenance expectations
- **§10.19** — Binds documented-testing evidence as external artifacts
- Per-tool-call agent-action entries under the session `run_id` satisfy the report's "track and log AI agent actions and decisions"

### Results
Five spec-section confirmations, one documented-open regulatory question, one scope note, no findings. The chain satisfies a requirement set appropriated from settled rule text — the FFIEC logging-integrity discipline and the SEC 17a-4(f) audit-trail alternative are the same requirement in two regulators' clothes, and the chain built for the first satisfies the second. No purpose-built spec-section family was needed; the foundational chain answers the appropriated requirements.

**Documented-open:** whether AI chatbot transcripts and model outputs are 17a-4(b)(4) "business as such" records — raised by FINRA in RN 25-07, unresolved by SEC or FINRA. The firm preserves all AI outputs chain-bound under a risk-based judgment as though required, without conceding they are; the posture is covered under either resolution. The audit team documented the question as open and did not resolve it by fiat.

**Scope note:** the chain records that behavioral guardrails held; it does not enforce them. Guardrail enforcement (copilot delivery constraints, product-shelf limits, refusal conditions) is the firm's application logic; the chain is the integrity-bound evidence the guardrails held. The examiner should see both layers.

Message to the FINRA examiner: there is no AI rule; every AI-readiness requirement is pinned to the rule that carries it; the chain produces the supervisory record (3110), the approved-and-sent communication (2210), the recommendation lineage (Reg BI), and the recreatable original record (17a-4(f)) on demand per named item.
