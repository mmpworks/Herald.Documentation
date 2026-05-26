---
project: kognitos-spec
kind: research-artifact
status: chapter-01-in-progress
parallel_to: ../novel/
created: 2026-05-22
---

# kognitos-spec — second-novel research source

This directory holds a parallel novel — the same audit scenarios, the same audit team, the same questions — but with one substitution: the audit team's only normative framework is **Kognitos's published 12-field AI audit-trail schema**. They have never heard of TesseraSeal, Vidimus, Herald Enterprise, or the FFIEC chain-of-custody spec. They walk into Northbridge Federal Savings with a 12-row checklist and try to do their job.

## Why this exists

Kognitos published a 12-field AI audit-trail schema in May 2026 as marketing collateral. The fields are real, cross-regulator, and have become a de-facto shorthand for "what an AI audit-trail row should carry." A separate research artifact (Heather PR #5 on `mmpworks/SR-26.2-Model-Risk-Management`) cross-referenced all 12 points against the PRD-1 / TesseraSeal spec and found that **9 of 12 are already exceeded today**, with 3 more (Points 3, 8, 10) crossing par-to-exceeds once planned spec changes land.

That cross-reference is a *structural* comparison. This novel is the *operational* counterpart — what does it actually look like when an audit team uses Kognitos's 12-field framework as their only assessment instrument against a deep TesseraSeal deployment? Where does the framework come up short? Where is it silent? Where is it imprecise enough that the audit team has to record "we cannot tell"?

## Methodology

- **Setting:** identical to the parallel novel (`../novel/01-northbridge-federal-savings.md`). Same bank, same MRA verification revisit, same prior-year history, same audit team members with the same competencies.
- **Audit team's framework:** Kognitos's 12-field schema (see `12-fields-reference.md` in this directory). No FFIEC chain-of-custody spec. No §10.16 severity-classification clause. No §4.4 attribute table. No §10.25 fork-detection responsibility. No §7 12-step verifier procedure. The Kognitos checklist is the only normative document in the room.
- **Same questions:** the audit team asks the same questions the parallel-novel team asked. The bank's facts on the ground are unchanged — Vidimus, Herald Enterprise, the daily seal, the verifier, the three-layer compositional security are all still running. The audit team's framework is what changes.
- **What we do not do:** we do not propose fixes to Kognitos's framework. We do not claim Kognitos is wrong. We just record what happens when the framework meets the field.

## Finding taxonomy

Each beat in the chapter produces one of five outcomes recorded against the Kognitos field it touches:

- **✓ Confirmation** — the bank's demonstration clearly satisfies the Kognitos field. The audit team checks the box and moves on.
- **⚠ Partial** — the Kognitos field asks the question, but doesn't specify a bar. The audit team sees the bank do something that *might* satisfy it, but the framework gives them no way to confirm sufficiency. They record "satisfied to the extent the framework asks" and move on.
- **✗ Gap** — the bank demonstrates a property the Kognitos framework doesn't ask about at all. The audit team has nowhere to record it. They make a private note ("worth bringing back to the framework committee") and move on.
- **◐ Nit** — the Kognitos field uses imprecise wording the audit team would normally challenge under a sharper framework. They can't downgrade it because the framework itself is the source of the imprecision. Recorded as a framework observation, not a bank finding.
- **🚨 Finding** — a genuine non-conformance against a Kognitos field. The bar to reach this is harder than under a sharper framework, because Kognitos's wording is broader and easier for an institution to claim it satisfies.

The interesting research question is the *ratio* of these outcomes. A clean Kognitos-framework audit at a deep TesseraSeal deployment is likely to produce many Confirmations and Partials (the bank is doing a lot of right things, but the framework can't articulate why they're sufficient), several Gaps (depth the framework doesn't ask about), some Nits (places where the framework's wording is the weak link), and zero or very few Findings (the bank actually exceeds the framework everywhere it's asked).

That's exactly the gap-and-shadow pattern this research is meant to expose.

## Index

| Chapter | Scenario | Status |
|---|---|---|
| 01 | Northbridge Federal Savings — MRA verification revisit | in progress |

## Related

- `../novel/01-northbridge-federal-savings.md` — the parallel novel chapter under the FFIEC chain-of-custody spec.
- `../synopsis/01-northbridge-federal-savings.md` — the synopsis form.
- `E:\dev\MMP.Media\_assistant_drafts\wiki\market-research\2026-05-20-kognitos-12-field-audit-schema.md` — Pearl's structured reference for Kognitos's 12 fields, cross-source confirmation, discrepancies surfaced.
- `mmpworks/SR-26.2-Model-Risk-Management` PR #5 (commit `4ca1de4`) — Heather's structural 12-point cross-reference against PRD-1.
