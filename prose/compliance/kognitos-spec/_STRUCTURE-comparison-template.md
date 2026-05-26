# Comparison Document Structure Template

*Reference template for `NN-{client}-comparison.md` files. Use this shape for every chapter comparison so context stays lean across the program.*

Companion document — `_OBSERVATIONS-running.md` — carries program-level editorial continuity (counts, stakeholder statements, pattern observations). Each comparison file stays scoped to the engagement; the observations file carries cross-chapter signal.

---

## Required sections (in order)

### 1. Title + scoping line

```markdown
# Comparative Analysis — Chapter NN ({Client Name})

*Side-by-side analysis of how the Kognitos 12-field framework and the TesseraSeal /
FFIEC chain-of-custody v1.0b spec handle a **{engagement type}** {audience context}.
Honest assessment of where {chapter's distinctive research signal — one sentence}.*
```

### 2. New research signal (only when the chapter introduces a new category or sharpens an existing one)

Skip this section when the chapter is recurring-only. Include when the chapter introduces:
- A new framework-side issue category (speculation / under-reporting / inarticulability) — first instance
- A sharper variant of an existing category (e.g., Ch06 took Ch05's inarticulability under public-safety stakes)
- A new operational-property class

Shape: one-paragraph framing → comparison table → one closing line that names what is new.

### 3. Recurring from earlier chapters

Compact table. Two columns: recurring point + earlier ref + this-chapter instance.

```markdown
| Recurring point | Earlier ref | Ch NN instance |
|---|---|---|
| Compositional security | Ch01 §4 | {how it appeared here} |
| ... | ... | ... |
```

**Severities unchanged.** No re-litigation of recurring points; one-line each.

### 4. New comparison points specific to this chapter

Each new point gets a fixed sub-structure. Aim for 8-12 new points per chapter; fewer if the chapter is mostly recurring.

```markdown
### {Letter}. {Short title naming the structural distinction}

**The audit-room question.** *"{Verbatim question from the chapter, or paraphrase that
captures the decision point.}"*

**TesseraSeal.** {Reference-spec section + 2-4 sentences on what the spec articulates.
Cite § numbers.}

**Kognitos.** {What field, if any, comes close. Why it's not adequate. Usually 1-3 sentences.}

**Speculation gap.** {What the auditor has to invent or do without. 2-4 sentences.}

**Structural reason for the gap.** {Optional — include when the gap is genre-shaped
rather than coverage-shaped. Skip when the gap is just a missing row.}

**Honest assessment.** {Closing severity line. Use format: "Severity: {low/medium/high/
highest} for {institution class}; {applicability note}."}
```

When a point is an **inarticulability**, add `**Inarticulability gap.**` between Speculation gap and Structural reason. Make explicit that no field can be made to surface the finding.

When a point is an **under-reporting**, add `**The under-reporting.**` between Kognitos and Speculation gap. State what the reference spec catches and what the framework misses.

### 5. Summary table

Single table at the end of the new-points section. Columns:

```markdown
| # | Area | TesseraSeal anchor | Kognitos anchor | Speculation gap | Material impact |
|---|---|---|---|---|---|
| A | {short title} | {§ ref} | {field or "No field"} | {category/severity} | {1-line impact} |
```

Follow with:
- `**Plus recurring from Chapters 01-NN:** N comparison points unchanged.`
- `**Total comparison points exercised in Chapter NN:** N.`
- `**Of which inarticulabilities: N.**` (only if applicable)
- `**Of which under-reportings: N.**` (only if applicable)

### 6. Honest assessment — engagement-scoped only

What is in this section:
- What this engagement uniquely contributes (1-3 short subsections)
- The stakeholder statement (if one was made on-the-record) — quote it
- Engagement-specific consequences

What is **NOT** in this section anymore (moved to `_OBSERVATIONS-running.md`):
- Running speculation / under-reporting / inarticulability counts
- Program-level pattern observations
- Editorializing on what this chapter signals for chapters NN+1..22
- Cross-chapter consolidation language

Keep this section to roughly 80-150 lines. Anything that would be repeated across multiple comparisons belongs in the observations document.

---

## Closing pointer

Every comparison file ends with:

```markdown
---

*Program-level running tally and editorial signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
```

This is the single anchor that lets a reader (or me, in a fresh session) follow the cross-chapter thread without re-reading prior comparisons.

---

## What goes in the observations document

The companion `_OBSERVATIONS-running.md` carries:

1. **Aggregate counts** — speculation anchors, under-reportings, inarticulabilities, on-the-record stakeholder statements
2. **Category definitions** — the three framework-side issue categories with their canonical instances
3. **Per-chapter signal log** — one short paragraph per chapter naming what that chapter uniquely contributed
4. **Operational-property invisibility log** — list of demonstrations the framework could not record
5. **Stakeholder statement log** — quoted on-the-record requests, by chapter
6. **Stakes-pattern observations** — how inarticulability / under-reporting / speculation scale with engagement stakes
7. **Forward signal** — what the running pattern predicts for upcoming chapters

The observations document grows by ~20-40 lines per chapter (not by re-stating everything; by appending the new chapter's row to each running log).

---

## Why this split

Three benefits:

1. **Compaction-resilient.** A future session can read the observations document in one shot and recover full program context without re-reading 22 comparison files.
2. **Comparison files stay scoped.** Each comparison stops growing the editorial section across chapters; it stays bounded to what the engagement uniquely contributes.
3. **Cleaner deliverable.** When the program ships, the observations file becomes the executive summary; the comparison files become the engagement-by-engagement detail.
