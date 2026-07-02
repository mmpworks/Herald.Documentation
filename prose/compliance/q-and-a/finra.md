---
status: stable
title: FINRA Q&A — the appropriated requirement set
last-reviewed: 2026-07-02
---

# FINRA questions readers ask

This is the FINRA companion to the main spec Q&A. It answers the questions a broker-dealer's compliance team, board, and outside counsel ask when Gen AI is in production and a FINRA examination is coming.

One frame runs under every answer: **there is no FINRA AI rule.** FINRA has not written one and has not proposed one. Its rules are technology-neutral. So an AI-readiness requirement is not a new rule. It is appropriated from rules FINRA already enforces, plus the exam expectations in FINRA's 2026 oversight report. The recurring question is *"which rule actually says that?"* Each answer below pins the requirement to the rule that carries it.

Every answer marks its status so nobody upgrades a signal to a rule:

- **Settled rule text** — the requirement is in a rule you can cite by number.
- **Guidance** — FINRA has stated a position in a notice or report; it carries exam weight but is not itself a rule.
- **Open question** — the SEC and FINRA have not resolved it. We say so and show the covered-either-way posture.

The worked narrative behind this Q&A is **Story 23 · Aldergrove Wealth Partners** — a FINRA-member broker-dealer readiness engagement that walks the full citation map, section by section.

## Who each icon means

- 🔍 &nbsp;**Examiner** — here, FINRA examination staff and the SEC (FINRA is an SRO overseen by the SEC)
- 📋 &nbsp;**External auditor** — financial-statement and SOC engagement auditors
- 🛡 &nbsp;**Internal audit** — the firm's internal audit function
- 📐 &nbsp;**MRM officer** — model risk management lead and model risk managers
- 🏛 &nbsp;**Board / CCO** — board-level readers and the Chief Compliance Officer
- 🛠 &nbsp;**Implementer** — engineers and operators adopting the chain
- ⚖ &nbsp;**Legal counsel** — firm GC and outside FINRA regulatory counsel
- ⭐ &nbsp;**Featured** — the load-bearing answers a reader new to the FINRA surface should read first

Most questions carry two or more icons because most readers share the same concerns. Filter to your role in the rendered view, or use browser find (Ctrl+F / ⌘+F) with the icon glyph in the raw markdown. The `Spec` column cites the chain sections that deliver the capability, so each answer is verifiable against the source.

---

## There is no AI rule — the requirement set

| ⭐ | Audience | Question | Answer | Spec |
|---|---|---|---|---|
| ⭐ | 🔍 📐 🏛 ⚖ | Which FINRA AI rule does TesseraSeal address? | None — and all of them. FINRA has not written an AI rule and has not proposed one as of mid-2026. Its rules are technology-neutral: when Gen AI touches a recommendation, a communication, a supervisory process, or a record, the existing rules apply in full. The AI-readiness requirement set is appropriated from rules FINRA already enforces — Rule 4511 (books and records, incorporating SEA 17a-3 / 17a-4), Rule 3110 (supervision), Rule 2210 (communications), and SEC Regulation Best Interest — plus the exam expectations in the 2026 Annual Regulatory Oversight Report. The chain answers each because it satisfies the same audit-trail discipline underneath all of them. Story 23 walks the full citation map. | §4, §7 |
| ⭐ | 🔍 ⚖ 🏛 | FINRA is an SRO, not a government agency — does that change anything for the chain? | No. FINRA is a self-regulatory organization — a private membership body the broker-dealers belong to, overseen by the SEC — not a government agency. The examiner works for the industry's own regulator. The chain does not distinguish: the artifacts an SRO examiner reads are the artifacts a bank examiner reads — the ledger, the signed public key, the captured event corpus. The §7 verifier runs locally and reaches the same pass/fail exit code. Verification is examiner-agnostic by construction. | §7, §10.12 |
|   | 🏛 ⚖ 📐 | Can FINRA bring an AI enforcement action against a firm? | Not an "AI rule" action — no such rule exists to violate. The realistic shape is a Rule 3110 failure-to-supervise action. The published analogues are automated-process supervision failures: a firm fined for an untested algorithm, a firm fined for an unreliable automated identity-verification process, a firm fined for automated-monitoring failures. None was an AI-rule violation. The exposure is "you used an automated process in a regulated activity and can't show you supervised it." The chain is the defense — the supervisory record produced on demand, not described. | §14 |

---

## Recordkeeping — 17a-4(f) and the open records question

| ⭐ | Audience | Question | Answer | Spec |
|---|---|---|---|---|
| ⭐ | 🔍 📋 🛠 ⚖ | How does the chain satisfy SEA Rule 17a-4(f)? | Settled rule text. FINRA Rule 4511 requires firms to make and preserve books and records per SEA Rules 17a-3 and 17a-4; 4511 is the FINRA hook that makes the SEC recordkeeping rules a FINRA obligation. Before 2022, 17a-4(f) required WORM — write-once-read-many — storage. The SEC's 2022 amendment (effective January 2023, compliance May 2023) added an alternative: a system that maintains *a complete time-stamped audit trail that permits the recreation of an original record if it is altered or deleted.* WORM is no longer the only path. The chain is that audit-trail alternative by construction — per-event MAC with a timestamp, daily Merkle seal, HSM-rooted Ed25519 signature, and a §7 verifier that recreates any original record byte-equal or proves it was altered. The §10.13 evidentiary-retention table carries the 17a-4 floor inventory. | §4, §7, §10.13 |
| ⭐ | 🔍 ⚖ 📐 🏛 | Are AI prompt and output logs required records? | Open question — and we do not pretend otherwise. FINRA raised it itself in Regulatory Notice 25-07 (April 2025), which asked whether AI-generated content — chatbot interactions and model outputs — constitutes records of the firm's business "as such" under 17a-4. The SEC and FINRA have not answered. No rule and no guidance today says all AI output must be preserved; firms make risk-based judgments under the technology-neutral principles. The defensible posture is to preserve as though the records are required, without conceding that they are. A firm that preserves is never wrong-footed by the resolution; a firm that decides for itself the transcripts are not records and deletes is exposed if it lands the other way. The chain over-satisfies the open question — every turn's prompt, context, output, and model version is bound whether or not the rule ends up requiring it. Story 23 documents this as open, not resolved by the audit team. | §10.47 |

---

## The rules pointed at AI — supervision, communications, recommendations

| ⭐ | Audience | Question | Answer | Spec |
|---|---|---|---|---|
| ⭐ | 🔍 📐 🛡 | How does Rule 3110 supervision become demonstrable through the chain? | Rule 3110 requires a firm to supervise its associated persons and activities. FINRA's stated position (RN 24-09 and the 2026 report) is that a firm supervises an AI-assisted activity as it supervises any other, and owns the output regardless of whether a human or AI generated it — guidance, not a new rule. The chain binds the human-in-the-loop review as an event under the §14 generation-and-HITL discipline: the reviewer's decision, the supervisory principal's oversight where written supervisory procedures require it, the timestamp, and the reviewer's authenticated identity. Authenticated, not shared — a 3110 claim collapses if the "reviewing principal" is a shared login nobody can attribute. The chain makes supervision a produced record instead of a narrative. | §14 |
| ⭐ | 🔍 ⚖ 📋 | How does Rule 2210 principal pre-approval bind to the chain? | Settled rule with a chain-bound mechanism. Rule 2210 sorts communications by audience and reach; a communication to more than 25 retail investors in any 30-day window is a retail communication, which generally requires principal pre-approval and must meet the 2210(d) fair-and-balanced content standards. The rule applies to AI-generated content the same way it applies to human-drafted content. On the chain, the approval is a bound event under the §14 HITL discipline — the approving principal's authenticated identity, the timestamp, and the exact rendered-output hash. The send binds the same rendered-output hash. So the approved content is provably identical to the sent content, and the approval provably precedes the send; the verifier confirms all three per named communication. | §14, §10.47 |
| ⭐ | 📐 ⚖ 🔍 | Does an AI recommendation fall under Regulation Best Interest? | Yes. An AI-generated recommendation to a retail customer is still a recommendation; the care, disclosure, and conflict obligations sit with the firm regardless of whether a human or the model originated it. Reg BI is an SEC rule; FINRA examines for it. The 2026 report frames it as supervising *outcomes* — the firm owns the recommendation the customer received. A best-interest defense is only as strong as the record of what informed the recommendation, and the chain carries the full lineage through the §10.11.1 parent-linkage family: the delivered recommendation links to its draft, the draft to the suitability check, the check to the holdings and profile pulls. One walk produces the whole decision trail, with the human review-and-edit bound inside it rather than assumed. | §10.11.1, §10.47, §14 |

---

## The 2026 report's expectations

| ⭐ | Audience | Question | Answer | Spec |
|---|---|---|---|---|
| ⭐ | 🔍 📐 🛠 | What does the 2026 FINRA oversight report expect for AI agents? | Exam expectation, not rule text — a firm does not "violate the report." The 2026 Annual Regulatory Oversight Report (published December 2025) carries FINRA's first dedicated GenAI section. For Gen AI generally it names: storing prompt and output logs for accountability and troubleshooting; tracking which model version was used and when; validation and human-in-the-loop review; and robust testing for privacy, integrity, reliability, and accuracy. For AI agents specifically it names: monitor the agent's system access and data handling, define human-in-the-loop protocols, track and log the agent's actions and decisions, and implement guardrails restricting agent behavior. The examiner reads a firm's AI systems against these — the rules say what a firm must do; the report says what the examiner looks for. Each expectation maps to a chain capability already in production; Story 23 shows the mapping. | §10.47, §14, §10.19, §10.21.4 |
|   | 🛠 📐 🛡 | The report says "restrict agent behavior with guardrails" — does the chain do that? | Partly, and here is the line between the layers. The chain records the agent's actions; it is the evidence surface. Guardrails that *restrict* the agent's behavior — a copilot's inability to deliver to a client without a human, its product-shelf constraints, its refusal conditions — are enforced in the application, not in the chain. The chain proves the guardrails held by recording that no out-of-policy action occurred. It is the integrity-bound evidence the guardrails held, not the guardrail itself. An examiner should see both: the application's guardrail design and the chain's record that it held. Story 23 logs this as a scope note, not a gap. | §10.19 |
