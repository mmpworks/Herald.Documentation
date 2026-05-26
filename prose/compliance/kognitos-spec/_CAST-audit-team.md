# Audit Team Cast Sheet

*Recurring audit-team roster for the Kognitos-lens novel. Use these roles consistently across chapters so the reader builds continuity with the same names doing the same kinds of work.*

The audit team is the same six people across all 22 engagements. The client liaisons change every chapter; the team does not.

---

## Core team

### Dawn — Audit Team Lead
- Runs the engagement. Owns the audit deliverable.
- Walks the kickoff section, asks the §1.2 / spec-anchor questions when stakes demand it, writes the whiteboard tally at end of day, replies "On the record" to stakeholder explicit-attribution statements.
- Voice: composed, direct, professional. She is doing competent work under a thin framework and her running notes (italicized) carry the chapter's research signal.
- Appears in: every chapter.

### Mike — Verifier Operator
- Runs the verifier against sample chain entries. Owns the verifier-output blocks.
- Reads entry records aloud when the engagement has a live event (Pacific Crescent live alert was his to verify).
- Strong technical voice; comfortable with the cryptographic substrate.
- Appears in: every chapter where chain-entry exercises happen (effectively all of them).

### Diana — Identity / Access / Field-3 Specialist
- Walks IAM, role separation, shared-account scenarios, MFA posture.
- Tags Field 3 ✗ when stated-identity is masquerading as authenticated-identity (Pacific Crescent dispatcher_id; Stelvio Plant_Engineer).
- Comfortable with legacy DBA-permission audits and modern federated identity.
- Appears in: chapters where the legacy / OT / shared-account pattern surfaces (most engagements).

### Luis — Retention / Field-1 + Field-12 Specialist
- Walks audit-log retention floors, regulatory minimum compliance, evidentiary-retention discipline.
- Tags Field 1 ✗ + Field 12 ✗ when retention is below regulatory floor (NERC CIP-008/009; HIPAA; FFIEC; SOX).
- Comfortable with the §10.13 evidentiary-retention table and the regulator-by-regulator floor inventory.
- Appears in: chapters with retention-floor compliance burdens (PCP's PI historian 60-day; most regulated industries).

### Elena — Customer / Consumer-Side Walker
- Walks customer-facing stacks (CIS, CRM, billing, consumer-facing disclosure, §1033 protocols).
- Owns the late-afternoon customer-side section. Tags findings on Salesforce-style field-history selectivity, retention-floor-on-CIS, AMI override propagation downstream.
- Voice: pragmatic about consumer-facing-system patterns; familiar with how vendor SaaS quirks affect audit-trail discipline.
- Appears in: chapters with customer-side or consumer-facing stacks (most engagements).

### Chen — Template / Notes Specialist
- Holds the engagement template and the running-notes record. Tags partials when the partial is structurally subtle (stated-identity vs authenticated; redaction-disposition; under-reporting candidates).
- Owns the cross-walk to the reference spec when the engagement needs cover-memo borrowing.
- Voice: precise, careful with framework-vs-reference distinctions.
- Appears in: chapters where framework-side issues surface (Ch04 onward, increasingly).

---

## Cast usage rules

### Each chapter does NOT need all six
A typical chapter exercises 3-5 of the six. Use whoever fits the engagement's structural shape:
- AI-heavy engagement: Dawn + Mike + Chen
- Legacy / OT-heavy engagement: Dawn + Diana + Luis (+ Mike for AI side)
- Customer-side-heavy engagement: Dawn + Elena + Chen
- Multi-stakeholder coordinated examination: full team

### Distinct voices, not interchangeable
- Mike runs the verifier — never Dawn or Diana
- Luis tags retention findings — Diana doesn't
- Elena walks customer-side — Mike doesn't
- Chen tags framework-side / template issues — distinct from Mike's technical posture

### First-name only after introduction
First mention in a chapter: "Diana (audit-team identity specialist)" or whatever framing fits. After that: "Diana" alone. Roles are implicit from prior chapters.

### Client liaisons are chapter-scoped
The client liaisons (Soren at PCP; Veronika at Atrio; Helmstad's CCO + CQD; Aiyana the OT lead at PCP; etc.) are introduced fresh per chapter in the header block. The team is consistent; the liaisons rotate.

---

## Stakeholder voice patterns observed across chapters

When a chapter produces an on-the-record statement, the stakeholder voice falls into one of three patterns:

| Pattern | Example | Characteristic |
|---|---|---|
| Direct boundary-setting | Veronika (Atrio Ch04) | "The framework is acceptable as X. It is not acceptable as Y." Clean, regulator-readable claim. |
| Joint-leadership formal request | Helmstad CCO + CQD (Ch05) | Two stakeholders making the same request in formal language. Signals organizational consensus. |
| Sharper-dimension addition | Soren Kovach (PCP Ch06) | Names an engagement-class boundary ("any utility with public-safety stakes") that generalizes beyond this engagement. |

Future chapters likely produce variations on these three patterns. Maintain the structural distinction — direct, joint-formal, or generalizing — when surfacing a new statement.

---

## Notes for adding cast members

Do not add new audit-team members unless a future chapter genuinely needs a specialty the existing six cannot cover. Six is the working ceiling. If a chapter introduces a forensic-accounting expert or a clinical-trial expert, treat them as a temporary client-side or third-party consultant rather than expanding the audit team.

The team is the constant. The engagement is the variable.
