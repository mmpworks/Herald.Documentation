# Chapter File Structure Template

*Reference template for `NN-{client}.md` chapter files. Use this shape for every chapter so voice and rhythm stay consistent and post-compaction continuation is cheap.*

Companion documents:
- `_STRUCTURE-comparison-template.md` — comparison file shape
- `_OBSERVATIONS-running.md` — program-level signal
- `_CAST-audit-team.md` — recurring audit-team roster

---

## Required sections (in order)

### 1. Header block

```markdown
# NN — {Client Name} (Kognitos-lens)

*{One-sentence scoping line that names what is distinctive about this engagement
under the framework lens — e.g., "an engagement where {X} forces the audit team
to {Y}".}*

**Engagement:** {Type and regulator audience — e.g., "NERC CIP audit-readiness assessment with PHMSA pipeline-integrity overlay; three-state PUC interest"}
**Client:** {Name} — {one-line characterization including any post-incident / pre-launch / coordinated-examination framing}
**Status:** {Chain instrumentation scope, age, throughput. Where the chain is NOT instrumented — legacy systems by name. This sets up the OT / legacy / customer-side walks later.}
**Audit team lead:** Dawn
**Client liaison:** {Named stakeholder with title} ; {second liaison if relevant}

**Audit team's framework:** Kognitos's 12-field schema. {Sentence naming engagement count
("The team is now N engagements in.") and naming any new lens-stretching scenarios this
chapter introduces. This is the "what's new" preview for the reader.}
```

### 2. Time-stamped narrative sections

Five to eight sections per chapter. Use time-stamp markers with emoji prefix.

| Emoji | Typical use | Time slot |
|---|---|---|
| 🌅 | Kickoff / coverage-map walk | 8:30-9:00 AM |
| 🧬 | First chain entry / verifier exercise | 9:30-10:30 AM |
| 🚨 | Mid-engagement event (live alert, finding surfaces, escalation) | varies |
| 🛡️ | §1.2 / spec-anchor discussion (when stakes demand it) | varies |
| 🔧 | OT / legacy / SCADA / on-prem walkthrough | 1:00-3:00 PM |
| 💳 | Customer-side / billing / consumer-facing walkthrough | 3:30-4:30 PM |
| ⚡ | Auxiliary deep-dives (PMU clock, DR, attestation, etc.) | 4:30-5:00 PM |
| 🌆 | Auditor debrief | 5:00-5:30 PM |
| 🧾 | Final assessment theme | closing |

Section heading format:
```markdown
## {Emoji} {H:MM AM/PM} — {Section title naming what happens}
```

Body cadence:
- Action narration in third-person past tense
- Auditor running notes in italics: *Note for the chapter. Field N is satisfied with depth — the {detail} is bound to {context}.*
- Dialogue uses paragraph form for short exchanges; no quotation-mark heavy formatting
- Stakeholder names spelled out on first appearance; first-name basis after

### 3. Chain-entry exercise block

Within an early section (typically 🧬), exercise a sample chain entry. Standard format:

````markdown
```json
{
  "entry_id": "{chain-instance-id}",
  "tenant": "{tenant-id}",
  "service": "{service-name}",
  "seq": {sequence-number},
  "ts": "{ISO-8601-with-millis}Z",
  "model_id": "{model-identifier}",
  "model_version": "{semver-or-tag}",
  "gen_ai.request.model": "{otel-naming}",
  "gen_ai.response.model": "{otel-naming}",
  "prompt": { ... },
  "response": { ... },
  "audit.deployment.intent": "{production|validation|canary|ab_test|regulatory_sandbox}",
  "audit.deployment.policy_version": "{policy-ref}",
  "payload_hash": "...",
  "hmac": "...",
  "merkle_path": [...],
  "daily_seal_ref": "{seal-id}"
}
```
````

Add engagement-specific attributes inside the entry (dispatcher_disposition at PCP; redaction-disposition at Helmstad; tenant-isolation attributes at Atrio).

### 4. Verifier-output block

When the verifier runs, render the invocation + output verbatim:

````markdown
```
$ herald-verify --tenant={tenant} \
                --service={service} \
                --date={YYYY-MM-DD} \
                --entry-id={entry-id} \
                --strict
```

{Elapsed seconds}

```
Status: PASS
Step:   12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified
        against public key {key-fingerprint}
Elapsed: {N.N}s
```
````

Witness-mode runs produce `PASS-STRUCTURALLY` instead of `PASS`. Failure modes produce the appropriate exit code per §10.12.

### 5. Finding-tag conventions

Five tag shapes, all formatted as blockquote with H3 inside the blockquote:

```markdown
> ### ✓ Confirmation #{N} — {one-line summary of what was confirmed and against which field(s)}

> ### ⚠ Partial #{N} — {what's partially satisfied and why}

> ### 🚨 Finding-{NNN} — {what's failing and which field(s)}

> ### ◇ Framework-Silent Observation #{N} — {operational property the framework cannot record}

> ### ⚠ Framework Inarticulability #{N} — {finding that no Kognitos field can file under any reading}
```

For under-reportings, use the Framework-Silent or Finding tag with an explicit note that the reference spec catches it:

```markdown
> ### 🚨 Framework Under-Reporting #{N} — {what reference spec catches that Kognitos cannot}
```

Counters reset within-chapter except the global tag families (Finding-NNN uses a chapter-wide running number; Framework Inarticulability uses a program-wide running number).

### 6. Multi-finding rollup sections

When a single legacy-system or customer-side walkthrough produces 3+ findings in close succession, roll them up with a summary tag rather than five individual blocks:

```markdown
> ### 🚨 Findings {NNN}-{NNN} — {short list naming each finding briefly}

> ### ⚠ Partials #{N}-{N} — {short list naming each partial briefly}
```

Use rollups when the findings share a structural theme (all customer-billing-side; all OT-layer; all legacy retention). Keep individual blocks when each finding has a distinct structural shape.

### 7. Auditor debrief — whiteboard tally

End of working day. Section header `## 🌆 5:30 PM — Auditor Debrief`.

Dawn writes the day's tally on the whiteboard. Render as a fenced code block to preserve formatting:

````markdown
```
KOGNITOS 12-FIELD ASSESSMENT — {CLIENT NAME} ({ENGAGEMENT FRAME})

AI SIDE — {SERVICE NAME}:
  Confirmations:                  {N} ({field set})
  {operational demonstration if applicable}: {N}
  Partials:                       {N}
  Findings against bank:          {N}
  Nits:                           {N} (under Kognitos; reference spec records {N} {§-refs})
  Framework-silent observations:  {N} ({short list})

LEGACY/OT SIDE — {systems by name}:
  Findings against bank:          {N}  ({short list})
  Partials against bank:          {N}  ({short list})

{CUSTOMER/BILLING SIDE if applicable}:
  Findings against bank:          {N}
  Partials against bank:          {N}

CROSS-ZONE / FRAMEWORK-SIDE:
  Framework Inarticulability:     {N} ({short ref})
  Framework Under-Reporting:      {N} ({short ref})
  Framework Gap (recurring):      {N} ({short ref})
```
````

Follow with an `ENGAGEMENT-TEAM OBSERVATIONS ON FRAMEWORK SELECTION:` block — numbered list of 3-6 observations naming what the framework could not record.

### 8. Stakeholder on-the-record statement (if applicable)

When the chapter produces an on-the-record statement, place it after the whiteboard. Stakeholder comes back into the room. Direct quotes inside paragraph form, no special formatting beyond paragraph breaks. End the statement with "On the record." or equivalent verbatim closing. Dawn's reply: "On the record."

### 9. Final Assessment Theme

```markdown
## 🧾 Final Assessment Theme

> "{One-paragraph summary of the engagement's deliverable shape under Kognitos vs the
> reference spec. Counts, the central inarticulability/under-reporting if any, the
> stakeholder statement if any. This is the cover-memo-able paragraph.}"
```

### 10. Research takeaway

```markdown
## Research takeaway

{One-paragraph scoping of what this chapter uniquely contributes to the program-level
argument. Cross-references the prior chapter's pattern if relevant.}

{Bullet list of how the chapter's central pattern compares to prior chapters' patterns,
when the chapter is extending or refining a prior signal.}
```

### 11. Closing pointer (replaces the running-tally + editorial-closing blocks)

The chapter file ends with a one-line pointer rather than carrying running counts:

```markdown
---

*Running counts and program-level signal: see [`_OBSERVATIONS-running.md`](./_OBSERVATIONS-running.md).*
```

The per-chapter signal-log paragraph and the count delta land in `_OBSERVATIONS-running.md` rather than here. This keeps each chapter file scoped to its engagement.

---

## Pacing target

- Total length: ~600-800 lines per chapter file
- Section count: 6-10 time-stamped sections
- Findings per chapter: typically 5-12 individual findings; OT-heavy chapters skew higher with rollups
- Confirmations: typically 4-8 on the AI side
- Framework-silent observations: typically 2-4
- Stakeholder statement: 0-1 per chapter (~50% of chapters from Ch04 onward)

## Cadence rules

- Italicized auditor running notes appear at least once per major section (capture the auditor's *processing* of what they're seeing)
- The verifier exercise lands in the second or third time-stamped section
- The OT / legacy / customer-side walkthroughs accumulate Findings and Partials with rollups
- The §1.2 / Daubert / epistemic-scope discussion lands when stakes warrant it (not every chapter; chapters with public-safety, litigation, regulator-inspection, or clinical-quality stakes)
- The whiteboard tally is the bridge from narrative to research signal
- The Final Assessment Theme is one paragraph, not a list

## Voice rules

- Third-person past tense for action; present tense for the running-notes italics
- Stakeholder dialogue in paragraph form, no heavy quotation formatting
- "On the record" closings preserved verbatim when stakeholders deliver them
- Avoid editorial intrusion outside the running-notes italics and the Research takeaway
- The auditor team is doing competent work under a thin framework; the framework's silences cost them but their professional response is steady
