# 23 — Aldergrove Wealth Partners

> An independent FINRA-member broker-dealer and dually-registered investment adviser, ~$41B client assets, headquartered Richmond, Virginia, ~900 registered representatives across ~140 branch offices in the Mid-Atlantic and Southeast. Gen AI in production on two surfaces: a "rep-assist" recommendation copilot that drafts investment recommendations for a registered rep to review before delivery, and a client-communications surface (a portal chatbot plus AI-drafted client emails). TesseraSeal in production for 10 months across both AI surfaces. The team is on-site at the request of Aldergrove's Chief Compliance Officer ahead of a FINRA cycle examination. The engagement is two days. The story is structurally different from the twelve financial-services engagements before it — this is the team's first **SRO-flavored** engagement, where the examiner is a self-regulatory organization rather than a government agency, and where the AI-readiness requirement set is not one FINRA rule but a set appropriated from SEC rule text and FINRA's technology-neutral posture. The recurring question all day is *"which rule actually says that?"* — and the team answers it with precision every time.

## The team and the day

The full eight travel: Dawn, Raj, Elena, Mike, Diana, Luis, Chen, Tom. Aldergrove's home office is a restored tobacco-warehouse building on the James River side of downtown Richmond, exposed brick and steel, a trading-floor-shaped operations room on the third floor that Aldergrove kept when it bought the building even though a wealth-management broker-dealer has no trading floor. The FINRA examiners arrive in three weeks; the team's job is the pre-examination readiness pass plus the spec-section confirmation memo to Aldergrove's CCO before the exam opens.

## The drive-in monologue

```
6:52 AM EDT. Rental SUV, downtown Richmond, from the hotel on
                          East Cary Street to the Aldergrove home office on the
                          James. Dawn driving. Raj in the passenger seat with
                          his coffee.
```

**Dawn:** "Twelve financial-services engagements in the rear-view. Northbridge was the banking high-water mark. Atrio was the multi-tenant platform. Hill Country was the credit-union marketing-AI swap. Wasatch was the payments network on the fast clock. — Every one of them, the examiner was a government agency. OCC. Fed. FDIC. CFPB. NCUA. FTC. State banking. — Aldergrove is different."

**Raj:** "Different how?"

**Dawn:** "FINRA isn't a government agency. It's a self-regulatory organization — a private membership body the broker-dealers belong to, overseen by the SEC. The examiner who walks in three weeks from now works for the industry's own regulator, not for the government. First SRO-flavored engagement the firm has done."

**Raj:** "And the AI-readiness rule."

**Dawn:** "There isn't one. — That's the whole engagement. There is no FINRA AI rule. No AI-specific sweep letter. No AI enforcement precedent. Aldergrove's CCO called us because her board keeps asking her which FINRA AI rule the firm has to comply with, and the honest answer is *none — and all of them.*"

**Raj:** "Say that again."

**Dawn:** "None, because FINRA hasn't written an AI rule and hasn't proposed one. All of them, because FINRA's rules are technology-neutral. If Gen AI touches a recommendation, a communication, a supervisory process, or a record, the existing rules apply in full. The requirement set for an AI exam isn't a new rule. It's appropriated — from SEC rule text FINRA already enforces, from FINRA's own supervision and communications rules, from Reg BI, and from the expectations FINRA published in the 2026 oversight report. — The firm keeps looking for the AI rule. There is no AI rule. There is a stack of existing rules pointed at AI."

**Raj:** "So what do we tell them?"

**Dawn:** "We tell them which rule actually says that. Every time someone in that room says *FINRA requires X for our AI*, we pin it to the rule text. Four-five-eleven for the records. Three-one-one-zero for supervision. Twenty-two-ten for communications. Reg BI for the recommendations. The 2026 report for the expectations — and we're careful there, because a report is not a rule. — And the settled anchor under all of it: seventeen-a-four-f. The audit-trail alternative. That one's the reason we're the right vendor in the room."

**Raj:** "It never is."

**Dawn:** "It never is. But this one's structural in a way I like. FINRA is appropriating a requirement that already exists in rule text and pointing it at AI. The chain we built to satisfy the FFIEC handbook already satisfies the SEC rule it's appropriated from — because it's the same requirement wearing two regulators' clothes. Today we prove that, section by section, and we're honest about the one question nobody has answered yet."

**Raj:** "Which question."

**Dawn:** "Whether the AI's own outputs are records the firm is *required* to keep. Not whether the firm *can* keep them — Aldergrove keeps all of them, chain-bound. Whether the rule *requires* it. The SEC and FINRA have not answered that. We are not going to answer it for them in a readiness memo. We're going to document it as open and show that Aldergrove is covered whichever way it lands. — Off the highway. Next light."

The SUV turns onto the cobblestones of the old warehouse district. The Aldergrove building comes into view — four stories of brick, a loading-dock canopy converted to a covered entrance, the U.S. flag and the Virginia flag on the old freight rail.

## 7:40 AM — Lobby

The lobby was a tobacco-drying floor a century ago and still has the timber columns. A receptionist checks the team in; badges carry photo plus a numeric escort code. Aldergrove's Chief Compliance Officer is **Delphine Marchetti-Soames**, early-50s, twelve years at the firm, nine years at FINRA before that — she examined broker-dealers for the SRO before she sat on the other side of the table. She knows the exam from the inside. Next to her is the Director of Internal Audit, **Gareth Enderby-Voss**, late-40s, who will partner with Tom.

**Delphine:** "Dawn. Welcome to Richmond. — I'll say the thing I said on the phone so the room hears it. I spent nine years examining firms for FINRA. I know exactly what the examiner is going to ask, and I know there's no AI rule for them to cite. That's what makes this hard for my board. They want a checklist. There isn't a checklist. There's a set of old rules the examiner will read our AI systems against. I need to know, rule by rule, that our chain answers each one — and I need to know where the honest gaps are before the examiner finds them."

**Dawn:** "That's the engagement. Two days. We walk the rep-assist copilot and the client-communications surface, we pin every requirement to the rule that actually carries it, we sample the chain, we run reconciliation on a slate of recommendations and communications, and we hand you a spec-section confirmation memo before the exam opens. Tom partners with Gareth on the internal-audit side."

**Delphine:** "And the one question I've been losing sleep over — whether our chatbot transcripts are records we're required to preserve —"

**Dawn:** "— is a question the SEC and FINRA have not resolved, and we're not going to pretend they have. We'll document it as open and show you're covered either way. — More on that at lunch."

**Delphine:** "Good. That's the answer I was afraid I wouldn't get and the one I needed."

## 9:00 AM — The rep-assist path walk-through

Aldergrove's lead architect for the rep-assist copilot is **Anselm Kraviec**, late-30s, ex-fintech, joined Aldergrove two years ago to build the copilot. He walks the team through the architecture.

The rep-assist copilot is an agent. When a registered rep opens a client's account to consider a recommendation, the copilot runs a sequence of tool-calls: it pulls the client's holdings, pulls the client's stated risk tolerance and investment profile, runs a suitability check against the firm's product shelf, retrieves relevant research, and drafts a recommendation with a rationale. The rep reads the draft, edits or rejects it, and either delivers it to the client or discards it. Nothing reaches the client without the rep's review.

The chain instruments every step. A single rep-assist session generates one session-open chain entry and one chain entry per agent action — the holdings pull, the profile pull, the suitability check, the research retrieval, the draft generation — plus a chain entry for the rep's review decision and a chain entry for the delivery or the discard. All under one `run_id`. Roughly 8-12 chain entries per rep-assist session; roughly 3,000 sessions a day across the 900 reps.

**Mike** (the verifier operator): "What's captured on the draft-generation entry?"

**Anselm:** "The four-tuple. The prompt the copilot assembled, the retrieval context it grounded on, the model output it produced, and the model version that produced it. Bound under one chain entry per §10.47."

**Mike:** "And the agent actions before it — the holdings pull, the suitability check?"

**Anselm:** "Each is its own chain entry. The 2026 report was specific about AI agents — *track and log AI agent actions and decisions.* Every tool-call the copilot makes is a logged, integrity-bound action with its inputs, its output, and the model version. If the examiner asks what the agent did on a given recommendation, the chain has every step in order."

**Mike:** "Where does the entry land?"

**Anselm:** "Local SSD on the copilot host, fsync'd before commit, then shipped to the central ledger over OTLP. Daily Merkle seal at 03:00 UTC, HSM-signed Ed25519. Standard daily cadence — we're not on Wasatch's clock; a wealth-management recommendation doesn't need a per-second seal."

**Dawn** (closing the morning walk): "Let me articulate it back. Every rep-assist recommendation is a chain of integrity-bound agent actions ending in a human review event and a delivery-or-discard event. The prompt, the grounding context, the output, and the model version are bound on the generation entry. The rep's review is a chain-bound decision, not an assumption. — That's the raw material. Now we spend two days proving which regulatory requirement each piece answers."

## 10:00 AM — "Which rule actually says that?" — the recordkeeping hook

The team moves to the third-floor operations room. Chen sets up at the old trading desk. Delphine, Gareth, and Anselm are at the table. The firm's outside FINRA regulatory counsel — **Tobias Ellery-Fanshawe**, of a securities-regulatory practice in Washington — joins by video.

**Delphine:** "Start with recordkeeping. My board thinks FINRA has a new AI recordkeeping rule. Does it?"

**Dawn:** "No. Chen, walk the chain of citations. Slowly, because this is the load-bearing one."

**Chen** (at the desk): "The recordkeeping requirement for a broker-dealer runs through three layers, and none of them is an AI rule. — FINRA Rule 4511 is the books-and-records rule. 4511 doesn't invent recordkeeping requirements; it requires firms to make and preserve books and records as required by the SEC's rules — SEA Rule 17a-3, which says which records to make, and 17a-4, which says how long to keep them and in what form. So when someone says *FINRA requires us to keep this*, the rule that actually says it is an SEC rule, and 4511 is the FINRA hook that makes the SEC rule a FINRA violation if you break it."

**Delphine:** "And the AI part?"

**Chen:** "There is no AI part in the rule text. 17a-3 and 17a-4 are technology-neutral. They don't say 'AI records.' They say *these categories of records,* and if an AI system produces something that falls into one of those categories — a communication, a recommendation record, a required books-and-records entry — the existing obligation attaches. The AI doesn't create a new obligation. It creates content that lands inside an old one."

**Dawn:** "Now the settled anchor. The one that makes the chain the right answer. — Chen, 17a-4(f)."

**Chen:** "17a-4(f) is the electronic-records provision. Before 2022 it required WORM — write-once-read-many storage. The SEC amended it in 2022; the amendment took effect January 2023, compliance May 2023. The amendment added an alternative to WORM: an **audit-trail alternative.** The rule text now permits electronic records kept either on WORM media or on a system that maintains — and I'm quoting the rule — *a complete time-stamped audit trail that permits the recreation of an original record if it is altered or deleted.*"

He lets it sit for a beat.

**Chen:** "That sentence is the chain. A complete time-stamped audit trail. Permitting recreation of an original record if altered or deleted. — The chain is a complete time-stamped audit trail by construction. Every entry carries a `mac_computed_at_utc` timestamp under a per-event MAC; the daily Merkle seal binds the day's entries under an HSM signature; the verifier recreates any original record and proves it byte-equal, or proves it was altered. That is not a capability we added for FINRA. It is the capability. 17a-4(f)'s audit-trail alternative describes what the chain already does."

**Dawn:** "And here's the part I want the board to hear. — This is where the word *appropriated* is exact and not loose. The chain was built to satisfy the FFIEC IT Handbook's logging-integrity discipline for banks. FINRA's AI-recordkeeping expectation is appropriated from SEC rule text — 17a-4(f). The two regulators wrote the same requirement: a tamper-evident, time-stamped audit trail that lets a third party recreate an original record. Banking calls it logging integrity. The SEC calls it the audit-trail alternative. FINRA points at the SEC's version and applies it to AI. — One requirement. Two regulators. Same chain. We didn't build a FINRA feature. The FINRA requirement is the FFIEC requirement wearing different clothes."

> 💡 **Quick picture.** Think of a building code that says a stairwell must have a handrail. A hospital inspector cites the hospital code; an apartment inspector cites the housing code; a school inspector cites the school code. Three inspectors, three code books, one handrail. The builder didn't install three handrails. He installed one that satisfies all three, because underneath the three code books is the same requirement. 17a-4(f)'s audit-trail alternative and the FFIEC handbook's logging-integrity discipline are two code books pointing at the same handrail. The chain is the handrail.

**Tobias** (by video): "For the record, from the regulatory-counsel chair — that's the correct read. 4511 incorporates 17a-3 and 17a-4 by reference; the 2022 audit-trail alternative is settled rule text; a hash-chained, time-stamped, append-only system is squarely within what the amendment permits. There is no daylight in that citation chain."

**Dawn:** "On the record. — Luis, the retention floors."

**Luis** (retention specialist): "17a-4 sets the retention periods — most books-and-records categories at three or six years, the first two years in an easily accessible place, some categories for the life of the enterprise. The chain's §10.13 evidentiary-retention table carries the floor inventory; Aldergrove's entries are under compliance-mode object lock with a retention floor that exceeds the longest 17a-4 category. — No retention finding. The floors are met with margin."

> ### Confirmation #1 — 17a-4(f)'s audit-trail alternative describes the chain by construction; the FINRA recordkeeping requirement is appropriated from settled SEC rule text
>
> FINRA Rule 4511 incorporates SEA Rules 17a-3 and 17a-4 by reference; the 2022 amendment to 17a-4(f) (effective January 2023, compliance May 2023) added an audit-trail alternative to WORM storage — *a complete time-stamped audit trail that permits the recreation of an original record if it is altered or deleted.* The chain satisfies this by construction: per-event MAC with a `mac_computed_at_utc` timestamp, daily Merkle seal, HSM-rooted Ed25519 signature, and a verifier (§7) that recreates any original record and proves it byte-equal or proves alteration. The §10.13 evidentiary-retention table carries the 17a-4 floor inventory; Aldergrove's entries are under compliance-mode object lock exceeding the longest 17a-4 category. The requirement is technology-neutral and appropriated from SEC rule text — the same audit-trail discipline the FFIEC IT Handbook requires of banks. No new AI recordkeeping rule exists; the chain built for the FFIEC discipline satisfies the SEC rule FINRA enforces because they are the same requirement.

## 11:00 AM — Rule 3110 supervision, and the enforcement shadow

Diana takes the bench. Rule 3110 is the supervision rule.

**Diana** (identity and supervision): "3110 requires a firm to supervise its associated persons and its activities. FINRA's stated position — in the 2024 notice and the 2026 report — is that a firm supervises an AI-assisted activity the way it supervises any other activity, and the firm is responsible for the output *regardless of whether it was generated by a human or by AI.* If the AI is used inside the supervisory system itself, the firm also has to assess the model's integrity, reliability, and accuracy."

**Delphine:** "So where does 3110 land on the copilot?"

**Diana:** "On the review event. — The copilot drafts; the rep reviews; the rep is a supervised associated person; the recommendation is delivered under the firm's supervisory structure. 3110 requires that a designated supervisory principal can demonstrate the recommendation was reviewed and that the firm supervised the process. The chain carries the human-in-the-loop review as a bound event under the §14 generation-and-HITL discipline — the rep's review decision, the principal's oversight where the firm's written supervisory procedures require principal review, the timestamp, the identity of the reviewer under authenticated identity, not stated identity."

She tags the field.

**Diana:** "Field 3 is clean here — the reviewer identity is authenticated, not a shared principal login. That matters, because a 3110 supervision claim collapses if the 'reviewing principal' is a shared account nobody can attribute. Aldergrove's principals review under individual authenticated identity. The chain binds who reviewed, when, and what they saw."

**Gareth** (internal audit): "The question my audit committee will ask — could FINRA bring an AI enforcement action against us?"

**Dawn:** "Not an AI-rule action. There is no AI rule to violate. — The realistic enforcement shape is a Rule 3110 failure-to-supervise action, and it isn't hypothetical. The analogues are on the record: a firm fined for deploying an untested algorithm, a firm fined for an unreliable automated identity-verification process, a firm fined for automated-system monitoring failures. None of those was an 'AI rule' violation. Each was a supervision failure — the firm put an automated process into a regulated activity and couldn't demonstrate it supervised the process. — That's the exposure. Not 'you used AI.' 'You used an automated process in a regulated activity and can't show you supervised it.'"

**Gareth:** "And the chain answers that how?"

**Dawn:** "By making the supervision demonstrable instead of asserted. Every recommendation carries its agent-action log, its model version, its grounding context, its human review event, its principal oversight where required. When the examiner asks *show me you supervised the algorithm,* the firm doesn't describe its supervision — it produces the chain of supervisory events, integrity-bound, for any recommendation the examiner names. The 3110 defense is a chain walk, not a narrative."

> ### Confirmation #2 — Rule 3110 supervision is demonstrable, not asserted; the realistic enforcement shape is failure-to-supervise-the-algorithm, and the chain produces the supervisory record
>
> Rule 3110 requires the firm to supervise AI-assisted activity as it supervises any activity; the firm is responsible for the output regardless of whether a human or AI generated it. The chain binds the human-in-the-loop review under the §14 generation-and-HITL discipline — the reviewing rep's decision, the supervisory principal's oversight where the firm's written supervisory procedures require it, the timestamp, and the reviewer's authenticated identity (Field 3 clean; no shared-principal-login masquerade). The realistic FINRA enforcement exposure is not an "AI rule" violation — no such rule exists — but a 3110 failure-to-supervise-the-algorithm action, on the pattern of published fines for untested algorithms, unreliable automated verification, and automated-monitoring failures. The chain converts the 3110 defense from narrative assertion into a produced supervisory record: every recommendation's agent-action log, model version, grounding context, and review event, integrity-bound and recreatable per named recommendation.

## 12:30 PM — Lunch, and the one open question

The firm's cafeteria is the old warehouse mezzanine, brick and river light. The team takes a long table. Delphine and Tobias (still on video, propped at the end of the table) join.

**Delphine:** "Now the question I've been losing sleep over. Our client portal has an AI chatbot. It answers account questions, explains products, helps clients navigate. Thousands of conversations a day. — Are those transcripts records we are *required* to keep?"

**Dawn:** "Here is the honest answer, and it has two parts, and I'm going to keep them separate so nobody in this room walks away thinking the first part is settled when it isn't. — Part one: the question is genuinely open. FINRA raised it itself, in the 2025 notice that requested comment on modernizing its rules — it explicitly asked whether AI-generated content, chatbot interactions and model outputs, constitutes records of the firm's business 'as such' under 17a-4. The SEC and FINRA have not answered. As of now there is no rule and no guidance that says all AI output must be preserved. Firms are making risk-based judgments under the technology-neutral principles. Anyone who tells your board the answer is settled — in either direction — is guessing."

**Delphine:** "And part two?"

**Dawn:** "Part two: it doesn't put Aldergrove at risk, because you already preserve all of it, chain-bound, by your own risk-based choice. — The open question is whether you're *required* to keep the transcripts. You keep them regardless. So whichever way the SEC and FINRA eventually land, you're covered. If they decide chatbot transcripts are 'business as such' records, you have them, integrity-bound, recreatable. If they decide they're not required, you've lost nothing — you kept records you weren't obligated to keep, at a storage cost you already absorb. The chain over-satisfies the open question. — What we will *not* do is write a readiness memo that resolves the question by fiat. We'll document it as open, cite the notice that raised it, and record that Aldergrove's posture is covered under either resolution."

**Chen:** "That's the §10.47 four-tuple doing the work again. Every chatbot turn binds the prompt, the retrieval context, the model output, and the model version. Whether or not the rule ends up requiring it, the transcript exists as an integrity-bound record."

**Tobias** (by video): "I'll add the counsel note. The safe posture, and the one I advise, is exactly this — preserve under a risk-based judgment as though the records are required, without conceding that they are, and without waiting for the SEC to resolve it. The firm that preserves is never wrong-footed by the resolution. The firm that decides for itself that the transcripts aren't records, and deletes, is exposed if the resolution goes the other way. Aldergrove preserves. That's the defensible chair."

**Dawn:** "On the record. — Tom, log it."

**Tom** (writing): "*Open regulatory question: whether AI chatbot transcripts and model outputs are 17a-4(b)(4) 'business as such' records. Raised by FINRA in its 2025 rule-modernization notice; not resolved by SEC or FINRA as of engagement date. Aldergrove preserves all AI outputs chain-bound under a risk-based judgment; posture is covered under either resolution. — Documented as open. Not a Gap; not a Partial. Not resolved by the audit team; the regulators own the resolution.*"

## 1:30 PM — Rule 2210 communications

Elena takes the bench. Rule 2210 is the communications rule.

**Elena** (customer and communications side): "2210 governs a firm's communications with the public. It sorts communications by audience — correspondence, retail communication, institutional communication — and it sets content standards and, for retail communications, principal pre-approval. The rule applies to AI-generated content the same way it applies to human-drafted content. FINRA's own framing: a chatbot's output is a communication, and its category depends on its audience and reach."

**Delphine:** "The threshold I care about — retail communication."

**Elena:** "A communication distributed to more than 25 retail investors within any 30 calendar-day period is a retail communication. Retail communications generally require principal pre-approval before use and have to meet the 2210(d) content standards — fair and balanced, no misleading claims. — So the audit question is: for AI-generated content that crosses the retail-communication threshold, can the firm demonstrate principal pre-approval, and can it produce the exact content that went out?"

**Delphine:** "Can we?"

**Elena:** "Walk it. — The AI-drafted client emails that go to segments above 25 recipients route through a principal-approval gate before send. The approval is a chain-bound event under the §14 HITL discipline — the principal's authenticated identity, the timestamp, the exact rendered content approved, bound by hash. The send binds the same rendered-output hash. So the content approved and the content sent are provably the same content, and the approval provably preceded the send."

Mike pulls a case. An AI-drafted market-commentary email sent to a segment of 4,200 retail clients on a rebalancing theme. Elena runs the walk.

```
$ herald-verify --tenant=aldergrove-wealth-prod \
                --communication=aldergrove-rebalance-commentary-2027q2-seg-a \
                --resolve-principal-approval \
                --reconcile-rendered-output-byte-equal \
                --strict --explain
Status: PASS
Step:   12
Reason: retail-communication content reconstructed;
        principal pre-approval event resolved;
        approved-content hash byte-equal to sent-content hash;
        approval timestamp precedes first send;
        audience count resolved above 25-recipient threshold

additional_verifications:
  - principal_pre_approval_event_verified
  - approved_content_equals_sent_content
  - approval_precedes_send_confirmed
  - retail_communication_threshold_resolved
  - reviewer_authenticated_identity_confirmed

communication_subset:
  communication_id:        aldergrove-rebalance-commentary-2027q2-seg-a
  audience_count:          4,200
  classification:          retail_communication (>25 in 30-day window)
  model_version:           aldergrove/client-comms-drafter-2027q2
  approving_principal:     authenticated (individual identity, not shared)
  approved_at_utc:         2027-04-18T13:02:11.000Z
  first_send_at_utc:       2027-04-18T14:00:00.000Z
  rendered_output_hash:    3f9c1a4b7e0d... (approved == sent)

elapsed: 2.3s
```

**Elena:** "Approved at 13:02, first send at 14:00, same rendered-output hash on the approval and the send. The principal pre-approved the exact content, under authenticated identity, before it went out, and the chain proves all three. — 2210(a) approval, 2210(d) content preserved for the record. The examiner can name any retail communication and get this walk."

> ### Confirmation #3 — Rule 2210 principal pre-approval and content preservation are chain-bound; approved content is provably identical to sent content, and approval provably precedes send
>
> Rule 2210 applies to AI-generated communications by audience and reach; a communication to more than 25 retail investors in a 30-day window is a retail communication requiring principal pre-approval and 2210(d) fair-and-balanced content standards. The AI-drafted client emails crossing the retail threshold route through a principal-approval gate bound under the §14 HITL discipline: the approving principal's authenticated identity, the timestamp, and the exact rendered-output hash. The send binds the same rendered-output hash. The verifier confirms approved-content equals sent-content, approval precedes send, and the audience count resolves above the threshold, per named communication in 2.3 seconds. The model version that drafted the content is bound under §10.47; the content is preserved and recreatable for the 2210 record.

## 2:30 PM — Reg BI and the recommendation lineage

Mike takes the verifier bench. Regulation Best Interest is the SEC rule; FINRA examines for it.

**Mike:** "Reg BI is simple to state and load-bearing to prove. An AI-generated recommendation to a retail customer is still a recommendation. The care obligation, the disclosure obligation, the conflict obligation — all of it sits with the firm, regardless of whether a human or the copilot originated the recommendation. The 2026 report frames it as supervising *outcomes* — the firm owns the recommendation the customer received, full stop."

**Delphine:** "So the audit question is whether we can show a given recommendation was in the client's best interest."

**Mike:** "The audit question is whether you can produce the recommendation's full lineage — what the copilot considered, what it recommended, what the rep did with it, and what the client received. Reg BI is a best-interest standard, and a best-interest defense is only as good as the record of what informed the recommendation. — The chain carries the lineage through the §10.11.1 parent-linkage family. The delivered recommendation links to its draft; the draft links to the suitability check; the suitability check links to the holdings and profile pulls. One walk produces the whole decision trail."

He picks a case. A recommendation delivered to a retail client on March 3 to shift from one fund to another. Mike walks the lineage.

```
$ herald-verify --tenant=aldergrove-wealth-prod \
                --recommendation=aldergrove-rec-2027-03-03-cust-44821 \
                --resolve-recommendation-lineage \
                --strict --explain
Status: PASS
Step:   12
Reason: recommendation lineage walked transitively;
        four-tuple binding resolved on generation entry;
        suitability-check inputs resolved;
        human review event resolved;
        delivery event resolved

additional_verifications:
  - recommendation_lineage_walked
  - four_tuple_binding_resolved (prompt/context/output/model-version)
  - suitability_check_inputs_bound
  - human_review_decision_bound
  - delivery_event_bound

lineage:
  1. session_open           2027-03-03T15:10:02Z
  2. holdings_pull          2027-03-03T15:10:03Z  (client 44821 holdings snapshot, hash-bound)
  3. profile_pull           2027-03-03T15:10:03Z  (risk tolerance + investment profile, hash-bound)
  4. suitability_check      2027-03-03T15:10:05Z  (product-shelf check, pass, reason-bound)
  5. research_retrieval     2027-03-03T15:10:06Z  (grounding context, hash-bound)
  6. draft_generation       2027-03-03T15:10:09Z  (§10.47 four-tuple bound)
       - model_version:     aldergrove/rep-assist-copilot-2027q1
  7. rep_review             2027-03-03T15:14:41Z  (edited; authenticated rep identity)
  8. delivery               2027-03-03T15:22:18Z  (delivered to client; rendered-output hash-bound)
elapsed: 1.8s
```

**Mike:** "Eight steps, in order, one point eight seconds. The copilot pulled the holdings and the profile, ran the suitability check and passed it with a bound reason, grounded on retrieved research, drafted the recommendation with the four-tuple bound, the rep edited it under authenticated identity, and it was delivered with the rendered output bound by hash. — A Reg BI best-interest inquiry on this recommendation gets the entire decision trail. What the copilot considered, what it recommended, what the rep changed, what the client received. That's the care-obligation record, integrity-bound."

**Dawn:** "And the rep edited the draft — step 7. That's worth naming for the board. The copilot doesn't make recommendations. It drafts them. The rep made the recommendation, informed by the copilot, and the chain shows the rep's edit. Reg BI's obligation is the firm's and the rep's; the chain shows the human decision inside the lineage, not an AI decision the human rubber-stamped."

> ### Confirmation #4 — Reg BI recommendation lineage is fully recreatable; the human recommendation decision is bound inside the lineage, not assumed
>
> Reg BI's care, disclosure, and conflict obligations attach to an AI-assisted recommendation the same as to a human recommendation; the firm owns the recommendation the retail customer received. The chain carries the full recommendation lineage through the §10.11.1 parent-linkage family: session-open, holdings pull, profile pull, suitability check (with bound pass reason), research retrieval (grounding context), draft generation (§10.47 four-tuple: prompt/context/output/model-version), rep review (edited, under authenticated identity), and delivery (rendered output hash-bound). The verifier walks the lineage transitively per named recommendation in 1.8 seconds. The rep's review-and-edit is a bound decision inside the lineage — the recommendation is the human's, informed by the copilot, and the chain shows the human decision rather than assuming it.

## 3:30 PM — The 2026 report's four AI-agent expectations

Chen takes the bench for the last walk of the day — the 2026 FINRA Annual Regulatory Oversight Report's GenAI expectations.

**Chen:** "One discipline point before the mapping, because it's the difference between a defensible memo and an overreach. The 2026 report is not a rule. It's FINRA's statement of observed practices and exam expectations. It carries weight — the examiner will read your AI systems against it — but a firm doesn't 'violate the 2026 report.' The report tells you what the examiner is looking for. The rules tell you what you have to do. We keep those separate."

**Delphine:** "Understood. What does the report say it's looking for?"

**Chen:** "Four named practices for AI, and a specific set for AI agents. — For Gen AI generally: storing prompt and output logs for accountability and troubleshooting; tracking which model version was used and when; validation and human-in-the-loop review; and robust testing for privacy, integrity, reliability, and accuracy. For AI agents specifically: monitor the agent's system access and data handling, define human-in-the-loop protocols, track and log the agent's actions and decisions, and implement guardrails restricting agent behavior. — Every one of those maps to a chain capability the firm already runs. Let me walk them."

He puts the mapping on the screen.

```
2026 FINRA report expectation          →  chain capability (already in production)
────────────────────────────────────────────────────────────────────────────────
prompt and output logs                 →  §10.47 four-tuple: prompt + context +
                                           output bound per generation entry
model version used and when            →  model_version field on every generation
                                           entry; §10.21.4 vendor-version-registry
                                           for version-card provenance
human-in-the-loop review               →  §14 generation-and-HITL: rep review event
                                           + principal approval, authenticated identity
track and log agent actions/decisions  →  one chain entry per agent tool-call under
                                           the session run_id; ordered, integrity-bound
monitor agent access + data handling   →  Field-3 authenticated identity on each
                                           action; data pulls hash-bound to source
documented testing                     →  test evidence bound as external artifacts
                                           under §10.19; model-eval outputs hash-bound
```

**Chen:** "Six expectations, six capabilities, all in production for ten months. — The point that matters for the memo: the firm didn't build these to satisfy the 2026 report. The report named practices; the chain already implemented them, because they're the same practices the FFIEC handbook asked of banks and the same the SEC's audit-trail alternative describes. The report is appropriating the discipline, not inventing it. Aldergrove was compliant with the report's expectations before the report was published, because it was compliant with the older requirements the report is built on."

**Diana:** "And the guardrails-restricting-agent-behavior expectation — that's the one place the report asks for something the chain doesn't fully carry by itself."

**Chen:** "Right, and I'll flag it honestly. The chain *records* the agent's actions; it's the evidence surface. Guardrails that *restrict* the agent's behavior — the copilot's inability to deliver to a client without a rep, its product-shelf constraints, its refusal conditions — those are enforced in the copilot application, not in the chain. The chain proves the guardrails held by recording that no out-of-policy action occurred. But the guardrail enforcement itself is Anselm's application logic, not TesseraSeal. — We note that in the memo: the chain is the evidence the guardrails held, not the guardrail. The examiner should see both — the application's guardrail design and the chain's record that it held."

**Dawn:** "That's the honest line. Log it as a scope note, not a gap. The chain does what the chain does — it's the integrity-bound record. The guardrails are the firm's application controls. Both exist; they're different layers; the memo says so."

> ### Confirmation #5 — The 2026 FINRA report's GenAI and AI-agent expectations map to chain capabilities already in production; the report appropriates the discipline rather than inventing it
>
> The 2026 FINRA Annual Regulatory Oversight Report is a statement of observed practices and exam expectations, not rule text; a firm does not "violate the report." Its named GenAI practices — prompt and output logs, model-version tracking, human-in-the-loop review, documented testing — and its AI-agent expectations — monitor agent access and data handling, define HITL protocols, track and log agent actions and decisions, restrict agent behavior with guardrails — map to chain capabilities Aldergrove has run for ten months: §10.47 four-tuple binding (prompt/context/output), the `model_version` field plus §10.21.4 version-registry provenance, the §14 generation-and-HITL review and approval events, per-tool-call agent-action entries under the session `run_id`, Field-3 authenticated identity on each action, and §10.19 external-artifact binding of testing evidence. **Scope note:** the chain records that behavioral guardrails held; it does not enforce them. Guardrail enforcement (the copilot's delivery constraints, product-shelf limits, refusal conditions) is the firm's application logic; the chain is the integrity-bound evidence the guardrails held. The examiner should see both layers.

## 4:30 PM — The CCO question

Delphine's office overlooks the river. The light is going amber over the water.

**Delphine:** "Can I tell my board there's no AI rule and mean it as good news?"

**Dawn:** "You can tell your board there's no AI rule, and it's neither good news nor bad — it's the shape of the thing. FINRA regulates AI through rules it already has, applied technology-neutrally. The requirement set is real. It's just appropriated from rule text you already comply with, rather than written fresh for AI. Your board wanted a checklist. The truer thing is a citation map: every AI-readiness requirement pinned to the rule that carries it. That's the memo."

**Delphine:** "And when the examiner asks the hard question — the one about whether our chatbot transcripts are required records?"

**Dawn:** "You say what's true. The question is open; the SEC and FINRA haven't resolved it; you preserve all of it under a risk-based judgment as though it's required, without conceding that it is; and you're covered whichever way it resolves. — An examiner respects that answer far more than a firm that claims the question is settled. You're not guessing. You're preserving, and you're honest that the rule hasn't caught up to the practice. That's the strongest chair in the room."

**Delphine:** "And the enforcement risk."

**Dawn:** "Not an AI-rule action — there's no rule to cite. A 3110 failure-to-supervise action is the realistic shape, and the chain is your defense: every recommendation's supervisory record, produced on demand, integrity-bound. You don't describe your supervision. You produce it. — The firms that got fined couldn't demonstrate they supervised their automated processes. You can. That's the difference between the enforcement risk and the enforcement defense."

**Delphine:** "That's the message I needed. — What's the memo say on top?"

**Dawn:** "Five spec-section confirmations, one documented-open question, one scope note. 17a-4(f) audit-trail alternative satisfied by construction. 3110 supervision demonstrable per named recommendation. 2210 principal pre-approval chain-bound and content-preserved. Reg BI recommendation lineage recreatable with the human decision inside it. The 2026 report's expectations mapped to capabilities already in production. The open question — chatbot transcripts as required records — documented as open with your posture covered either way. The scope note — the chain records that guardrails held; the firm's application enforces them. — No findings. One honest open question that isn't yours to close."

**Delphine:** "Good. Memo to me before the exam opens."

**Dawn** (rising): "Tomorrow's reconciliation slate at nine. Memo to you Thursday morning."

## Day 2

The reconciliation slate runs cleanly: ten rep-assist recommendations and ten client communications, traced end-to-end. Each recommendation's lineage walks — session through delivery. Each retail communication's principal approval resolves and matches the sent content by hash. The one chatbot transcript in the slate — pulled to exercise the open-question posture — is present, integrity-bound, four-tuple-complete; whether the rule ends up requiring it or not, it's there.

The §10.13 retention-floor walk confirms every 17a-4 category is above its floor with margin. Diana's Field-3 walk confirms authenticated reviewer identity across the sampled review and approval events — no shared-principal masquerade anywhere in the slate.

The spec-section confirmation memo finalizes by 3 PM Thursday. The team hands it to Delphine and flies home. The FINRA examiner arrives in three weeks; Delphine has the citation map, Gareth's internal-audit team supports the exam, and the engagement closes from the team's side.

## TesseraSeal confirmations — the FINRA requirement set mapped to the chain

Unlike Wasatch, this engagement exercised no purpose-built spec-section family. It confirmed that the chain's foundational capabilities satisfy a requirement set appropriated from settled rule text. That is the engagement's whole point: FINRA's AI-readiness requirements are the FFIEC discipline and the SEC audit-trail alternative wearing a different regulator's clothes, and the chain built for the first already satisfies the second.

### The recordkeeping anchor — 17a-4(f) audit-trail alternative

**What Aldergrove operates.** Daily-cadence chain across both AI surfaces: per-event MAC, daily Merkle seal at 03:00 UTC, HSM-rooted Ed25519 signature. The verifier recreates any original record byte-equal or proves alteration. Entries under compliance-mode object lock exceeding the longest 17a-4 retention category.

**Which rule actually says that.** SEA Rule 17a-4(f), as amended in 2022 (effective January 2023, compliance May 2023): electronic records may be kept on a system maintaining *a complete time-stamped audit trail that permits the recreation of an original record if it is altered or deleted.* FINRA Rule 4511 makes the SEC recordkeeping rules a FINRA obligation by reference. The chain is the audit-trail alternative by construction.

### The supervision anchor — Rule 3110

**What Aldergrove operates.** Human-in-the-loop review bound under §14 on every rep-assist recommendation; principal oversight where written supervisory procedures require it; authenticated reviewer identity (Field 3 clean).

**Which rule actually says that.** FINRA Rule 3110. The firm supervises AI-assisted activity as it supervises any activity and owns the output regardless of whether a human or AI generated it. The realistic enforcement shape is a 3110 failure-to-supervise-the-algorithm action, not an "AI rule" violation; the chain produces the supervisory record on demand.

### The communications anchor — Rule 2210

**What Aldergrove operates.** Principal pre-approval gate on AI-drafted communications crossing the retail threshold, bound under §14; approved-content hash equals sent-content hash; approval precedes send; audience count resolved.

**Which rule actually says that.** FINRA Rule 2210. Retail communications (more than 25 retail investors in a 30-day window) require principal pre-approval and meet 2210(d) content standards; the rule applies to AI-generated content by audience and reach.

### The recommendation anchor — Reg BI

**What Aldergrove operates.** Full recommendation lineage under §10.11.1 parent-linkage: session, holdings, profile, suitability check, research grounding, draft generation (§10.47 four-tuple), rep review-and-edit, delivery — recreatable per named recommendation.

**Which rule actually says that.** SEC Regulation Best Interest. The care, disclosure, and conflict obligations attach to an AI-assisted recommendation the same as to a human one; the firm owns the recommendation the retail customer received. The human recommendation decision is bound inside the lineage.

### The expectations layer — the 2026 FINRA report

**What Aldergrove operates.** §10.47 prompt/output logs, model-version provenance, §14 HITL, per-tool-call agent-action entries, §10.19 testing-evidence binding — all in production for ten months.

**Which rule actually says that.** None — the 2026 Annual Regulatory Oversight Report is exam expectation, not rule text. It names the practices the examiner looks for; the chain implemented them before the report was published because they are the older FFIEC and SEC disciplines the report is built on.

## Engagement debrief — Dawn's voice

> "It never is. But Aldergrove is the cleanest example I've worked of a regulator appropriating a requirement instead of writing one. There is no FINRA AI rule. There is a stack of old rules — 4511 pulling in 17a-3 and 17a-4, 3110, 2210, Reg BI — pointed at AI, plus a 2026 report that names what the examiner looks for. Every AI-readiness requirement the firm faces is appropriated from settled rule text and applied technology-neutrally.
>
> "The load-bearing anchor is 17a-4(f)'s audit-trail alternative — settled rule text since the 2022 amendments. *A complete time-stamped audit trail that permits recreation of an original record if altered or deleted.* That sentence is the chain. We built the chain for the FFIEC handbook's logging-integrity discipline; the same chain satisfies the SEC rule FINRA enforces, because the two regulators wrote the same requirement. The FINRA requirement is the FFIEC requirement in a different suit.
>
> "The part I'm proudest of is the one thing we didn't do. Aldergrove's CCO asked whether the chatbot transcripts are records the firm is required to keep, and the honest answer is that nobody knows — FINRA raised the question itself and neither it nor the SEC has answered it. We didn't resolve it for them in a readiness memo. We documented it as open, showed that Aldergrove preserves everything chain-bound under a risk-based judgment, and confirmed the posture is covered whichever way it lands. An examiner trusts the firm that says 'this is open and here's how we're covered' more than the firm that claims certainty it doesn't have.
>
> "The next time we walk into an SRO-flavored engagement — the next broker-dealer, the next AI system with no rule of its own — this is the reference. Pin every requirement to the rule that carries it. Preserve honestly through the open questions. Produce the supervisory record instead of describing it. The chain doesn't care that FINRA is an SRO and the OCC is an agency. The audit trail is the audit trail."

## Cross-references

- **Spec impact**: §4 (four primitives — the audit-trail alternative by construction), §7 (verifier recreates the original record), §10.11.1 (recommendation lineage parent-linkage), §10.13 (evidentiary-retention floors — 17a-4 categories), §10.19 (external-artifact binding — testing evidence), §10.21.4 (vendor-version-registry — model-version provenance), §10.47 (four-tuple binding — prompt/context/output/model-version), §14 (generation and human-in-the-loop), §0.5.1 ("The chain in three paragraphs" for the executive orientation).
- **Regulatory citations**: SEA 17a-3 / 17a-4 (books and records; 17a-4(f) audit-trail alternative, 2022 amendments); FINRA Rule 4511 (books and records by reference); FINRA Rule 3110 (supervision); FINRA Rule 2210 (communications); SEC Regulation Best Interest; FINRA Regulatory Notice 24-09 (technology-neutral AI guidance); FINRA Regulatory Notice 25-07 (rule modernization; raised the AI-outputs-as-records question); 2026 FINRA Annual Regulatory Oversight Report (GenAI section — exam expectation, not rule text).
- **Documented-open**: whether AI chatbot transcripts and model outputs are 17a-4(b)(4) "business as such" records — raised by FINRA in RN 25-07, not resolved by SEC or FINRA. Recorded as open, not resolved by the audit team.
- **Auditor stories**: this story is the first SRO-flavored engagement and the first where the requirement set is appropriated rather than written. It contrasts with Story 22 Wasatch (which exercised a purpose-built streaming-mode family) — Aldergrove exercises no new family and confirms the foundational chain satisfies an appropriated requirement set. The banking engagements (Story 01 Northbridge, Story 04 Atrio, Story 12 Hill Country) share the financial-services register; the FFIEC-to-SEC requirement convergence is the through-line.

The spec-section confirmation memo and engagement debrief are filed under Aldergrove's compliance-track records, with the citation map — each AI-readiness requirement pinned to the rule that carries it — cited in the firm's WSP (written supervisory procedures) AI-governance section.
