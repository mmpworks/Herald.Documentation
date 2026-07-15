# 24 — Success Bank

> Success Bank — a Texas state-chartered commercial bank, ~$2.9B consolidated assets, headquartered in Tyler in the East Texas piney woods. A state nonmember bank, so its federal prudential supervisor is the FDIC — but this is the alternate-year cycle, and the Texas Department of Banking examines alone, no FDIC in the building. The bank has run a cryptographic chain-of-custody across its regulated evidence for a little over a year: loan-file provenance, board-minute binding, GL-extract hashing, the AI credit-decisioning surface, and its incident-response records. The Department has never examined a bank that runs one; nobody on the team has. The exam is the ordinary rhythm — the First-Day Letter went out four weeks ago, the IT Profile questionnaire ninety days before that, and most of the loan and asset data is already staged through the secure portal, so the on-site week skews to judgment work: loan classifications, control testing, the IT exam, and one cybersecurity incident from the spring that everyone knows is coming. The story is structurally different from the government-agency engagements in one way — the institution is claiming something no examiner has been handed before: that the team can *re-run* the evidence check itself instead of trusting an attestation. The working posture is the one the Department always carries: verify, don't take the bank's word. The recurring question all day is *"can I check that myself?"* — and one examiner walks in not believing the answer can be yes, and says so out loud in the first hour.

## The team and the day

The Texas Department of Banking team is a five-examiner field crew out of the Arlington regional office, with one examiner up from Houston and Austin as the Commissioner's seat behind them. **Delia Marsh** is the Examiner-in-Charge — a Commissioned Bank Examiner, Financial Examiner VI, twenty-three years in, the one who signs the Report of Examination and fronts the exit and board meetings. **Hank Doyle**, Financial Examiner V, up from Houston, carries asset quality and loan classification — the one who decides what gets called substandard. **Emmett Cole**, Financial Examiner IV, is the IT and InTREx specialist: fifteen years in the Department and only lately commissioned, having come up the long way, moved into IT late, and sat his oral boards eight months ago — sharp, and disinclined to be impressed. **Lauren Vega**, Financial Examiner III, has BSA/AML and operations. **Priya Raman**, Financial Examiner II, is the Assistant Bank Examiner on her second field exam. The bank's liaison is **Marisol Tijerina**, Chief Risk Officer and head of internal audit at Success Bank, an ex-examiner herself out of the FDIC's Dallas field office nine years ago — calm, and she knows exactly how the week works. Success Bank's home office sits in Tyler; the bank has given the team the third-floor boardroom for the week.

## 8:00 AM — Kickoff

```
8:00 AM CDT. Success Bank home office, Tyler, in the East Texas
                          piney woods. Third-floor boardroom — long table,
                          windows on the pines, a coffee service kept full.
                          The TDoB team, on the alternate-year cycle. No
                          FDIC in the building.
```

A single laminated page was pinned to the corkboard by the door, and Emmett read it twice before he sat down — a network diagram, every box labeled, every arrow ending at something the legend called *the chain*. Under it, in modest type: **Success Bank — evidence chain-of-custody. Coverage map, CC8.1 §10.19.**

Emmett had been on eleven IT exams. He had never seen a bank put its own evidence-integrity architecture on the wall before the examiners asked for it.

*That's either confidence or theater*, he thought. *Usually it's theater.*

Delia poured coffee and stayed standing while the bank filed in — Marisol Tijerina first, then a tall man in shirtsleeves she introduced as Gus Whitfield, the CIO, then a woman with a laptop already open who was Renata Okafor-Salazar, the CISO. Behind them, quiet, a young engineer named Theo who sat at the second screen and didn't say anything for the first hour.

**Delia:** "Marisol. Good to be back in Tyler."

**Marisol:** "Delia. Welcome. FDIC's not with you this cycle."

Delia set her cup down.

**Delia:** "Alternate year. It's ours this time. — Which means when we sign the report, it carries the same weight the joint report carried two years ago. Same standard. Same file the FDIC reads next cycle. I say that because I want your board to understand that a state-only exam is not a lighter exam."

**Marisol:** "They understand. I used to sit on your side of the table."

Delia opened her folder.

**Delia:** "I remember. — Let's do the agenda. Hank has asset quality — he's already been through the loan download you staged, so today is file review and classifications. Lauren has BSA and operations. Emmett has IT — InTREx, the URSIT components, your information-security program, and the incident from April. Priya is with me on management and the governance minutes. Same rhythm as always: we pull, we reconcile, we ask follow-ups, we check in at the end of the day."

**Marisol:** "Understood."

Delia looked at the laminated page by the door, then back at Marisol.

**Delia:** "Now. — You've got something on the wall I don't usually see. Walk me through it before we split up. I'd rather hear what you think you have than guess from a diagram."

**Renata:** "I can take that. It's mine."

Delia nodded at her.

**Renata:** "About fourteen months ago we stood up a chain-of-custody layer over the evidence a bank exam actually touches. Loan files, board and committee minutes, general-ledger extracts, our policies, our logs, the BSA records, and the AI credit-decisioning model that sits between the loan-origination system and the core. Every one of those artifacts, when it's produced or captured, lands as a signed entry in an append-only ledger. Each entry carries a keyed hash over the artifact. The entries link — each one carries the hash of the one before it. Once a day the ledger computes a single root over that day's entries and signs the root with a key that lives in a hardware security module. The signature is the seal."

**Emmett:** "So it's a log."

It wasn't a question. A flat, testing statement.

**Renata:** "It's a log the way a notarized document is a piece of paper. The point isn't that we wrote things down. The point is that you can check whether what we wrote down was changed after we wrote it. There's an open-source verifier. It conforms to a public specification. You run it. Not us. You. On your own laptops, against the same records, and it tells you PASS or FAIL and why. You don't have to believe me. That's the whole design — you're not supposed to have to believe me."

The room was quiet for a second. Emmett set down his pen.

**Emmett:** "Can I say the thing that I'm going to be thinking about all day anyway."

**Delia:** "Go ahead, Emmett."

Emmett turned to Renata.

**Emmett:** "You built the chain. You run the ledger. The key that signs the seal is *your* key, in *your* HSM, in *your* cloud account. So when the verifier says PASS, all it's telling me is that the bank's evidence matches the bank's signature over the bank's evidence. You signed your own homework. You just used a fancier pen."

Nobody at the bank flinched. Marisol, in fact, almost smiled — the smile of someone who had been waiting for exactly that sentence.

**Renata:** "That is the right question. It's the first question every serious person asks, and if I couldn't answer it, I'd deserve to have the whole thing thrown out. Give me until mid-morning. Not a slide. I'll show you why signing your own evidence is still tamper-evident, and I'll show you how *you* — not me — confirm the signer independently. If I can't, then you're right and it's a fancy pen, and you should write it up as one."

Emmett wrote something on his notepad. Delia caught the first two words upside down: *fancy pen.*

*Good*, Delia thought. *Let him chase it. If it's theater, he's the one who'll find the seam. If it isn't — I'd like to know that too.*

**Delia:** "All right. Let's go to work."

## 9:10 AM — The First-Day Letter, reconciled

```
9:10 AM CDT. Boardroom corner. Priya at a two-screen setup —
                          the First-Day Letter on one, the bank's portal
                          submissions on the other. Twenty-eight of thirty-one
                          items staged before the team arrived.
```

Priya had done this once before, on her first field exam, and it had taken her a day and a half. The job was tedious and it mattered: confirm that the document the bank uploaded against request item 14 was the document request item 14 actually asked for, and confirm it hadn't been swapped for a friendlier version somewhere between the bank's file room and the portal.

Delia sat down next to her with a second coffee.

**Delia:** "How are you checking item integrity? Walk me through your method."

**Priya:** "The old way. I open the uploaded file, I read it, I tie it back to the request. For the loan trial balance I foot it and tie it to the GL. For the board minutes I check the dates are continuous and nobody skipped a month. It's slow. Mostly I'm trusting that what's in the portal is what the bank meant to give us, and I catch a swap only if the content looks wrong."

**Delia:** "That's the method. It's been the method my whole career. You trust the bank's attestation, you reconcile what you can tie to an authoritative source, and the transport is secure so nobody tampers with it in flight. Three legs. Attestation, reconciliation, secure transport. Nothing in that stool tells you whether the file the bank uploaded on Tuesday is byte-for-byte the file that existed in the bank on Monday. It tells you the numbers cross-tie. It doesn't tell you the file is the original."

Priya looked at the diagram on the wall.

**Priya:** "And that's what the chain is supposed to do."

Delia slid a printed sheet across.

**Delia:** "That's what they say it does. So here's your extra step this week. — Renata's people gave us the entry identifiers for every artifact they uploaded against the First-Day Letter. For each item, you've got the artifact, and you've got a chain entry that claims to bind it. Your job — after you reconcile the normal way — is to run the verifier against the entry and see whether the file we received hashes to the value the chain sealed over a year ago."

**Priya:** "And if it doesn't match?"

Delia stood.

**Delia:** "Then either the file changed, or the chain is lying, and either one is a finding I want to hear about before lunch. — Start with the board minutes. Governance is where the pressure lives."

Priya opened a terminal. She had been given a read-only credential scoped to the verifier, but Renata had told her, twice, that she didn't strictly need it — the public key that anchored the seals was published, and the verifier could check a seal on any network. Priya kept the credential anyway. It saved typing.

She pulled the March board minutes — a PDF the bank had uploaded against request item 6. She reconciled it the normal way first: the meeting date matched the calendar, the attendance matched the board roster, the loan-committee approvals referenced in the minutes matched the loan numbers Hank was already looking at. Fine. Clean.

Then she took the entry identifier for item 6 and ran it.

```
$ ffiec-verify --entry-id=sb_9c4e21f7a0... --profile tx-dob
Verdict: PASS
Step:    12/12
Reason:  artifact hash matches sealed value; per-event MAC
         recomputed; chain link to prev entry intact; Merkle
         inclusion resolved; daily seal signature verified
         against published key fingerprint 4b1e7...
Profile: tx-dob (Texas Department of Banking)
Artifact: board_minutes (audit.exam_artifact.artifact_kind)
Sealed:  2026-03-19  Supervisor: TX-DOB (state charter)
Elapsed: 0.7s
```

Priya read it twice.

She took the PDF the bank had uploaded, ran a plain SHA-256 over it herself, no verifier involved, and compared the digest against the `artifact_hash` value the chain entry carried. Match. The document that existed in the bank on the nineteenth of March, over a year ago, when the minutes were sealed, was the document sitting in the Department's portal folder this morning. Not a re-export. Not a re-save. The same bytes.

**Priya:** "Delia. The March minutes match the seal from the day they were adopted. I hashed it myself. It's the same file."

**Delia** (from across the room, not unkindly): "Now do the other twenty-seven. And flag me the first one that doesn't."

> ### Confirmation #1 — Staged First-Day-Letter artifacts hash to their year-old seals; provenance is confirmed byte-for-byte rather than taken on the bank's attestation
>
> Priya reconciled twenty-eight First-Day-Letter items the conventional way — foot, tie to GL, check continuity — and then ran the reference verifier against each item's chain entry. Every artifact the bank staged through the portal hashed to the value sealed at the time the artifact was produced. Board minutes, loan trial balance, GL extract, loan and investment policies, the information-security program. The examiner did not have to trust that the uploaded file was the original; she confirmed it, byte-for-byte, against a signed record over a year old. The `--profile tx-dob` flag surfaced the Texas-charter supervisory context on each entry.

Priya worked through the rest before ten. Twenty-eight PASS. Three items the bank hadn't staged were paper originals waiting in the file room; those she'd reconcile the old way.

*The old way isn't wrong*, she thought, footing the loan trial balance out of habit. *It's just that I always had to end with "as represented by management." I don't have to write that on these twenty-eight.*

She did notice one thing worth a check mark of her own. The verifier printed, on the loan-trial-balance entry, a line she didn't understand:

```
Note: source GL extract references parent run sb_gl_2026q1_007
```

She wrote it down to ask Hank about, because the GL extract was his.

## 10:00 AM — The IT exam, and the fancy pen

```
10:00 AM CDT. Boardroom. Emmett with the information-security
                          program open and the URSIT work program beside it.
                          Renata across the table with two laptops; Theo at
                          the second screen.
```

Emmett had the information-security program open, the URSIT work program next to it, and a growing suspicion that he was not going to enjoy this.

He ran the IT exam the way InTREx wanted it run: four URSIT components — Audit, Management, Development and Acquisition, Support and Delivery — each scored one through five, the composite feeding the Management and Sensitivity components of the safety-and-soundness rating. He'd been through the ninety-day IT Profile the bank had returned. He knew the shape of the environment before he walked in. AWS-resident. A modern loan-origination system feeding an AI credit-decisioning model. A commercial core. Splunk for the SIEM. A documented incident-response plan, which he would be reading closely, because of April.

But the chain was the thing he couldn't place in the work program, because the work program had no line for it. There was no InTREx module for "the bank cryptographically seals its own evidence." He was going to have to decide, on his own authority as the commissioned examiner in the room, whether it strengthened the control environment or was a liability dressed as a strength.

Renata sat down across from him with two laptops and Theo beside her.

**Emmett:** "You said mid-morning. It's mid-morning. Fancy pen."

**Renata:** "Fancy pen. Let me answer it in three moves. First move: tamper-evidence versus attestation. You're right that the bank signs the seal. What you're missing is what the signature is *over*, and what happens if any single piece is changed after the fact."

She turned the first laptop toward him. A chain entry, expanded.

**Renata:** "Every entry carries a keyed hash — a MAC — over the artifact's canonical bytes. The key is derived per-tenant from key material that lives in the HSM. The entry also carries the hash of the previous entry. So the entries are a linked chain: entry ten's stored link is entry nine's hash. Change anything in an old artifact — one digit in a loan balance, one word in the minutes — and that entry's MAC no longer recomputes. Fix the MAC to match your altered artifact, and now entry ten's stored link is wrong, because it pointed at the *old* hash. Fix entry ten, and eleven breaks. You'd have to re-derive every entry from the point of the change forward."

**Emmett:** "Fine. So I re-derive them all. It's your key. I have your key. I re-sign the whole tail."

Renata pulled up the second laptop.

**Renata:** "Second move. The daily seal. Once a day the ledger computes one root hash over the entire day's entries and signs *that* with the HSM key. The signed roots are published. We publish the fingerprint of each day's seal to a location outside the account that runs the ledger. So say you did re-derive the whole tail after altering a loan file from last spring. You'd produce a different root for that day. Which wouldn't match the seal that was already signed and published on that day, a year ago, and archived where the ledger's account can't reach it. To make the forgery clean you'd have to also forge the historical seal — and the historical seal's already in an examiner-reachable place with an earlier signature over it."

Emmett was quiet.

**Renata:** "Third move is the one that actually answers your question, so listen to this one and not the first two. You keep saying 'your key.' The whole thing hangs on whether *you* can confirm which key signed a given seal, independently, without asking me. If you can, then 'the bank signs its own evidence' stops mattering, because you're not trusting my say-so about which key is mine. You're checking it yourself against a record I can't quietly change."

She slid a printed page across the table. It was a manifest — a registry of the bank's signing keys, each with a fingerprint, a validity window, and the identity of the HSM partition that held it. At the bottom, a signature block.

**Renata:** "This is the key registry. It lists every signing key the chain has ever used, when each was valid, and the fingerprint of each. The registry itself is signed by a separate root of trust in the HSM, under separation-of-duties custody — the person who can request a seal signature is not the person who can alter the registry, and neither of them can extract the key. The registry is published. Its signature is published. You take a seal off any day's entries, you read the key fingerprint it claims, you look that fingerprint up in this signed registry, and you confirm the seal was signed by a key the registry vouches for *during the window that key was valid.* If I tried to introduce a new key to re-sign a forged history, it wouldn't be in the registry — and I can't add it to the registry without breaking the registry's own signature, which is anchored in a partition I don't control alone."

Emmett picked up the manifest. He read it slowly. Then he looked up.

**Emmett:** "So the attack isn't 'forge one entry.' The attack is 'forge every entry from the change forward, *and* forge the historical daily seal, *and* get a forged key into a separately-custodied signed registry, all at once, without any of the three noticing.'"

**Renata:** "Three independent custody layers. The specification is explicit that a false PASS — a tampered chain that verifies clean — requires compromising all three at the same time. Not one. All three. The capture layer that writes the MAC, the seal layer that signs the daily root, and the registry custody that vouches for the key. Different keys, different controls, different people. That's what makes signing your own evidence still mean something. It's not that you can't sign your own evidence. It's that you can't sign it *twice* — once honestly today, and once dishonestly next year — without the second signature disagreeing with the first in a place you don't control."

Emmett set the manifest down.

**Emmett:** "I'm not taking your word for that."

**Renata:** "I would think less of you if you did. Validate the registry yourself. The signature's a standard algorithm. The public root is published. Don't use my tooling if you don't trust my tooling — pull the registry, pull the root, check the signature with anything you like. Then re-run the verifier on a seal, read the fingerprint, and confirm it against the registry you just validated. If the two agree, you didn't trust me. You trusted the math. If they disagree, you found the biggest finding of your career and I'll help you write it."

*She's not nervous*, Emmett thought. *People who are bluffing get quicker when you push. She got slower.*

**Emmett:** "Give me an hour."

## 11:15 AM — The examiner checks the signer

```
11:15 AM CDT. Emmett alone with his own laptop. No bank tooling.
                          The published key registry pulled off the open
                          internet; the published root fingerprint from the
                          second location, outside the ledger's account.
```

Emmett did not use the bank's tooling.

He pulled the published key registry over the open internet from the bank's compliance page — no credential, no portal, the way Renata said he could. He pulled the published root fingerprint from the second location, the one outside the ledger's account. He wrote four lines of his own script — fifteen years in the Department and only lately commissioned; cryptography had been his strong suit on the boards — and verified the registry's signature against the published root himself. Valid. The registry was vouched for by a key he could confirm without asking anyone at Success Bank a single question.

Then he took a daily seal — he picked April 22nd, deliberately, because April was the month of the incident and he wanted the seal from the middle of the bank's worst week. He read the key fingerprint the seal claimed. He looked it up in the registry he had just independently validated. It was there, valid on April 22nd, custodied in the partition the registry named.

Then, and only then, he ran the verifier.

```
$ ffiec-verify --tenant=success-bank-prod --date=2026-04-22 \
               --strict --profile tx-dob --explain
Verdict: PASS
Step:    12/12
Exit:    0
Signature: verified against key 4b1e7... (registry-vouched,
           valid on 2026-04-22, partition hsm-p2)
Late-binding entries: 6  (see anomaly section)
Profile: tx-dob (Texas Department of Banking)
Supervisory context: charter_type=state_commercial;
           primary_state_supervisor=TX-DOB;
           federal_prudential_supervisor=FDIC;
           dual_supervision=alternating
Elapsed: 5.2s
```

A trace scrolled past. Fifty-odd lines. The verifier walked from the genesis entry through the day's chain, recomputed every MAC, resolved the Merkle inclusion for each entry, and checked the daily root's signature against the key fingerprint — the same fingerprint Emmett had just confirmed by hand against the registry he had validated by hand.

Emmett ran it a second time. Same verdict. Same exit code. He changed one byte of one archived artifact in a scratch copy — his own copy, not the bank's ledger — and pointed the verifier at the tampered copy. It came back FAIL, exit code 2, and named the entry whose MAC no longer recomputed and the exact byte offset where the canonical bytes diverged. He put the artifact back. PASS again.

He sat back.

*I checked the signer without asking her*, he thought. *I broke it on purpose and it caught me at the byte. I fixed it and it agreed with itself again. That's not a fancy pen. A fancy pen doesn't catch its own owner.*

He found Renata in the hallway.

**Emmett:** "The registry validates against the published root. The April 22 seal is signed by a key the registry vouches for, valid that day. I confirmed the fingerprint by hand before I ran your verifier, so the verifier isn't telling me anything I hadn't already checked myself. And when I corrupt an artifact it fails at the byte and names it."

**Renata:** "So."

He said it plainly, the way he'd want it read back to him in a report.

**Emmett:** "So it's not a fancy pen. You still signed your own evidence. But you can't change it after the fact without disagreeing with a signature I can check independently, and you can't get a forged key past a registry that's custodied away from you. I trust the record because I can re-run it, not because you told me to. Write that down, because I'm going to."

**Renata:** "I'd rather you wrote it down."

> ### Confirmation #2 — Self-signed evidence is still tamper-evident under independent check; trust is established by reproduction across three custody layers, not by attestation
>
> The examiner's core objection — "the bank signs its own evidence with its own key" — was answered on-page, by the examiner, not by the bank. Emmett independently validated the published key-registry manifest against a separately-published root of trust using his own tooling, confirmed a daily seal's key fingerprint by hand against that registry, and only then re-ran the reference verifier, which agreed. A deliberate single-byte corruption of an archived artifact produced FAIL with the offending entry and byte offset named. Trust was established by reproduction across three independent custody layers, not by attestation. The `--profile tx-dob` output surfaced the charter authority and the alternating dual-supervision posture directly in the verdict.

He had one more thing to raise, and it was not a compliment.

**Emmett:** "While I was in the registry, I looked at your retention settings on the key material. You've got the IKM registry set to retain three years. Where'd you get three?"

**Renata:** "Call Report retention. Three years after the report date. We matched the longest artifact retention we thought we had."

**Emmett:** "You don't have three-year artifacts as your longest. You've got BSA records. SAR and CTR support. Those are five years. And you're chaining them — I saw BSA entries in the ledger. So walk it forward with me. Four years from now, an examiner or a grand jury wants to verify a chained BSA record from this spring. The artifact's retained; you keep those five years. But the key material that would let the verifier confirm the seal over it — that you set to age out at three. In year four, your oldest BSA evidence is still there, and it's no longer verifiable, because you threw away the key that proves it wasn't altered."

Renata was quiet for a moment. Not defensive. Working it.

**Renata** (slowly): "The registry entry ages out but the artifact doesn't. So the chain silently loses the ability to verify its own oldest evidence, exactly on the records with the longest legal life."

**Emmett:** "That's the finding. It's not that the chain is broken. It's that your retention on the key registry has to be at least as long as your longest *chained* artifact, and your longest chained artifact is a five-year BSA record, not a three-year Call Report. Set it to three and the oldest thing you most need to prove is the first thing that goes unverifiable."

**Renata:** "We'll fix the setting today and I'll bring you the changed configuration this afternoon. But you should still write it. If we did it, another bank standing this up will do it. The retention floor on the key registry is not obvious until someone walks it forward the way you just did."

**Emmett:** "I'm writing it. It's a matter for the board's attention. Not an order. But the board should see it, because if you'd gone another two years without catching it you'd have had a BSA record you couldn't authenticate the day you most needed to."

*She fixed it in the hallway*, he thought, walking back to the boardroom. *No committee. No 'let me check with legal.' She saw it, she agreed, she's changing the config before lunch. That's the tell. A bank that's faking the control argues about the finding. A bank that means it thanks you for it.*

## 12:30 PM — Lunch (nobody left the building)

```
12:30 PM CDT. Boardroom. Sandwiches brought up; nobody left the
                          building. Delia running the mid-day tally.
```

Delia asked for the mid-day tally the way she always did. Hank went first, because asset quality is always where the real exam lives.

**Hank:** "I've got two credits I'm calling substandard. A CRE loan on a retail strip in Longview that's been on the watch list two quarters and the guarantor's liquidity is gone, and an ag operating line where the borrower's been paying interest out of the principal we advanced. Neither one's a surprise; the bank's own watch list already had both. I'm not calling anything doubtful. Their allowance covers it. Management's not fighting me on the numbers."

**Delia:** "Documentation?"

Hank turned his laptop around.

**Hank:** "That's the part I want to say out loud. I pulled the loan file on the Longview credit — original note, three appraisals over the life of the loan, the credit memos, the guarantor financials. Then I did something I've never been able to do. Priya gave me the entry ID and I ran the verifier on the file. The appraisal that's driving my classification — the current one, the one that says the collateral value dropped — it hashes to a seal from the day it was uploaded to the loan system, eight months ago. So I know the appraisal I'm classifying against is the appraisal the bank had eight months ago. Not one they swapped in last week when they saw us coming."

**Delia:** "And the reconciliation? You still tie it out the normal way?"

Hank said it like a man who'd thought about it over the drive from Houston.

**Hank:** "I still tie it out the normal way, and I'm going to keep tying it out the normal way, because reconciliation and the chain answer two different questions. Reconciliation tells me the loan trial balance foots to the GL — that the bank's numbers are internally consistent. The chain tells me the file I'm holding is the file the bank actually had, unchanged. Consistency and provenance. I've always had the first one. I've never had the second one. Having both, the classification conversation gets shorter, because management can't tell me 'oh, that appraisal was preliminary' and hand me a different one. The chain says which appraisal was in the file eight months ago, and that's the one I'm working from."

**Priya:** "Hank — the GL extract you pulled. The verifier printed a line on it about a parent run. `sb_gl_2026q1_007`. What is that?"

Hank pulled it up.

**Hank:** "That's the GL extract job itself. The extract is a chain entry, and each account balance the extract produced references the extract job that produced it. So if I want to know whether this GL extract is complete — whether the bank pulled the whole ledger or a convenient subset — I can walk from the parent job to every child balance and confirm the count. It's the same trick they use on the loan download. The job is chained, and the rows reference the job. You can't hand an examiner a GL extract with three inconvenient accounts quietly dropped, because the extract job's entry names how many accounts it produced, and the count won't match."

**Delia:** "So a partial extract shows up as a partial extract."

Hank went back to his sandwich.

**Hank:** "Shows up as a mismatch between what the job says it produced and what's in the file. Yeah. I've been doing this nineteen years. Number of times a bank's handed me a GL extract that turned out to be missing exactly the accounts I'd have wanted to see — more than zero. This is the first exam where I could prove the extract was whole instead of asking nicely."

> ### Confirmation #3 — Provenance complements reconciliation rather than replacing it; the extract job's entry proves completeness the same way the artifact hash proves the file
>
> The asset-quality examiner reconciled the loan trial balance to the GL the conventional way, then verified that the specific appraisal driving a substandard classification hashed to a seal from eight months prior — establishing that the document under review was the document the bank held at the time, not a late substitution. The GL extract's chain entry named the count of account balances it produced, so a partial or curated extract would surface as a count mismatch. Reconciliation proved internal consistency; the chain proved provenance and completeness. The examiner used both.

Lauren had been listening with the patient expression of someone whose turn was next.

**Lauren:** "BSA and operations after lunch. But I already know my headline, because Emmett handed it to me in the hallway an hour ago. If they're chaining SAR and CTR support and the key retention was set to three years, then my five-year BSA records were going to outlive their own verifiability. He caught it. I'm going to write the BSA-side of the same finding — the retention floor has to key off the longest-lived chained artifact, and in a bank that's BSA at five years. Two examiners, one root cause, two booklets."

Delia nodded slowly.

**Delia:** "So at the half-day, we've got two substandard credits the bank already knew about and adequately reserved for, and one real IT finding about key-registry retention that the bank is fixing this afternoon and that's going in front of the board. That's a clean exam so far. Which means the afternoon is where it gets interesting, because the afternoon is April."

The room got a degree quieter. Marisol had come back for the afternoon; she spoke from the doorway.

**Marisol:** "The incident. You want to do it now?"

**Delia:** "After lunch. Emmett leads. I'll sit in. Bring Renata and whoever ran point on the notification."

## 1:45 PM — April, and the fifteen-day clock

```
1:45 PM CDT. Boardroom. The incident record on the screen. Emmett
                          leading, Delia sitting in. Renata, Marisol, and the
                          bank's information-security officer at the table.
```

The incident had happened on the ninth of April.

Emmett had read the write-up on the ninety-day IT Profile and again in the staged documents, and he'd formed the opinion he formed about most incidents, which was that the technical facts were usually fine and the *timeline* was usually where a bank got itself in trouble. Not because banks were dishonest. Because reconstructing who-knew-what-when, six months later, out of email threads and Slack messages and half-remembered phone calls, was genuinely hard, and the Texas rule was unforgiving about one thing in particular.

**Emmett:** "Walk me through it. Plain language first. Then I'm going to want the timeline, and I'm going to want to know how you can prove the timeline, because the timeline is the exam."

Renata pulled up the incident record. Marisol sat down next to her. A third person joined — a woman named Devika introduced as the bank's information-security officer, who'd run point on the response.

**Renata:** "April ninth. A vendor that provides our online-banking session analytics disclosed a compromise of their environment. Our data was in scope — session metadata, not credentials, not balances, but enough that we had to treat it as a reportable cybersecurity incident. We spent the ninth and into the tenth determining scope and confirming it was reportable. We made the determination that it was a reportable incident on April tenth at 4:20 in the afternoon. That determination is what starts the Texas clock."

**Emmett:** "7 TAC §3.24. Fifteen days."

**Renata:** "Fifteen days. Notify the Banking Commissioner as soon as practicable, and no later than fifteen days after we determine a reportable incident occurred. And — this is the part that matters — before we notify customers. The rule is explicit about the ordering. The regulator hears about it before the customers do. It's written into our incident-response plan, in the information-security program, the way the rule requires."

**Emmett:** "So tell me the timeline."

**Renata:** "April tenth, 4:20 PM: we determine it's reportable. April eleventh, 9:15 AM: we notify the Commissioner. We used the interagency computer-security incident notice — the same thirty-six-hour federal notice — which the Texas rule allows to satisfy the state notice. One notice, both regulators. April eleventh through the fourteenth: we finalize customer notification content with counsel. April fifteenth, 8:00 AM: we notify affected customers. Regulator first, customers second, whole thing inside the fifteen days with room to spare."

Emmett wrote it down. Then he looked up.

**Emmett:** "That's a good timeline. It's also exactly the timeline every bank tells me. Nobody has ever sat across this table and told me they notified the customers before the regulator. Of course the story is regulator-first. The question I've never been able to answer is whether the story is *true* — whether you actually notified the Commissioner before you notified the customers, or whether that's the order you reconstructed afterward because you know that's the order the rule wants. Six months later, out of an email thread, I can't tell the difference between 'we did it in the right order' and 'we're telling it in the right order.'"

**Renata:** "I know. That's why I'm about to show you the two events chained."

She pulled up two entries.

**Renata:** "The regulator-notification event and the customer-notification event are both in the chain. Here's the regulator notice — April eleventh, 9:15 AM, the interagency notice, sealed that day. Here's the customer notification — April fifteenth, 8:00 AM, sealed that day. Now. You don't have to trust the timestamps, and you shouldn't, because a timestamp is just a number a computer wrote and I could have written any number I wanted."

**Emmett:** "So why show them to me."

Renata pulled up the linkage.

**Renata:** "Because the *ordering* doesn't depend on the timestamps. It depends on the chain. The customer-notification event carries, in its bound payload, a reference to the regulator-notification event — it names the prior event's hash. And the specification has a primitive for exactly this: an event can bind a reference to a prior event it depends on, and the verifier confirms the referenced event actually exists earlier in the sealed chain. So the customer notice doesn't just *say* it came after the regulator notice. It cryptographically references a regulator-notice event that was already sealed into an earlier day's root — April eleventh's seal, signed and published four days before the customer notice existed."

Emmett leaned in.

**Emmett:** "Run it."

Renata ran the ordering check. Theo, at the second screen, had the two seals up side by side — the eleventh and the fifteenth, two different daily roots, two different signatures, both against registry-vouched keys.

```
$ ffiec-verify --ordering-check --profile tx-dob \
               --before=sb_regnotice_2026-04-11 \
               --after=sb_custnotice_2026-04-15
Verdict: PASS
Ordering: sb_regnotice_2026-04-11 precedes sb_custnotice_2026-04-15
Basis:    after-event binds prior-event hash; prior event sealed
          in root of 2026-04-11 (signed, published); after event
          sealed in root of 2026-04-15 (signed, published);
          cross-day seal ordering confirmed
Regulator notice: chain_kind=operational; interagency 36h notice;
          satisfies 7 TAC §3.24 (tx-dob profile)
Elapsed:  1.1s
```

Emmett looked at it for a while.

**Emmett:** "So the customer-notification event can't have been created before the regulator-notification event, because it references the regulator event's hash, and you can't reference the hash of something that doesn't exist yet. And the regulator event is sealed into the eleventh's root, which was signed and published on the eleventh — four days before the fifteenth's root that carries the customer notice. To fake regulator-first, you'd have had to know the regulator event's hash before you created it, which is the same as asking a hash function to run backward."

**Renata:** "That's the whole trick. I can lie about *when* something happened — a timestamp is just a claim. I cannot lie about *what order* two sealed events happened in, because the later one is built out of the earlier one's hash, and the seals landed in separate published roots on separate days. The ordering is the thing the rule cares about, and the ordering is the thing the chain can actually prove."

Emmett set his pen down, which for Emmett was a whole sentence.

**Emmett** (slowly, because he wanted to get the honesty of it right): "Here's what I'm going to write. I'm not going to write that the chain proves you determined the incident was reportable at 4:20 PM on the tenth. It doesn't. That determination time is your assertion. The chain proves you *recorded* that determination and didn't alter the record after, but the wall-clock moment your team's judgment crystallized — that's a human fact, and no cryptography reaches it. I'd be overclaiming if I wrote otherwise, and a defense lawyer would take my report apart for it."

**Renata:** "That's the right line. The chain proves integrity and ordering. It doesn't prove the truth of a human determination. I'd never claim it did."

**Emmett:** "But the *ordering* — regulator before customer — that I am going to write down as proven. Because that's not an assertion. That's math. You notified the Commissioner before you notified your customers, and I don't have to take your word for it, and neither will the next examiner, and neither will a court. That's the part 7 TAC §3.24 actually turns on, and it's the part I've never once been able to verify in fifteen years of reading incident timelines out of email."

*The one relationship the rule is about*, he thought, *and it's the one I can actually stand behind. Not the whole timeline. Just the part that matters, checked instead of taken on faith.*

> ### Confirmation #4 — The 7 TAC §3.24 regulator-before-customer ordering is cryptographically provable; the determination time stays an institution assertion
>
> Texas rule 7 TAC §3.24 requires a state bank to notify the Banking Commissioner of a reportable cybersecurity incident before notifying customers, within fifteen days of determining the incident is reportable. Success Bank's regulator notice (April 11, interagency 36-hour notice, satisfying the state clock) and its customer notice (April 15) were both chained. The customer-notice event bound the hash of the regulator-notice event, which had been sealed into a signed, published daily root four days earlier — so the ordering cannot be reconstructed or reversed after the fact. The examiner drew the honest line: the incident-determination *time* is an institution assertion (integrity-bound but not truth-proven, per the spec's epistemic-scope limits), while the notification *ordering* is genuinely proven by the chain. The rule turns on the ordering, and the ordering is what the chain establishes.

## 3:00 PM — Whose exam is in the chain, and whose isn't

```
3:00 PM CDT. Boardroom. Lauren's BSA walk-through done. The
                          question of the chain's scope boundary on the table —
                          bank evidence versus examiner work product.
```

Lauren finished her BSA walk-through, wrote the five-year-retention half of Emmett's key-registry finding, and then asked the question that Delia had been waiting for someone to ask, because it was the question that separated an examiner who understood the tool from one who'd been dazzled by it.

**Lauren:** "Renata. The chain covers the bank's evidence. Does it cover *our* work? Our workpapers, our access to your files this week, the report we're going to write?"

**Renata:** "No. And it can't, and it shouldn't. Your workpapers and your report are the Department's confidential supervisory information. They're the examiner's work product, custodied on the examiner's side, under your rules — backed up and then wiped off the field laptops at exam close, the way it's always been. Those aren't in my chain. My chain covers *my* evidence: the artifacts the bank produces and hands you. The line between the two is a scope boundary, and if anybody told you the chain covers the exam itself, they'd be selling you something."

**Lauren:** "Good answer. Wrong answer and I'd have written you up for over-claiming."

**Renata:** "There is one thing on the seam, though. Your *access* to our evidence — which examiner pulled which confidential file, and when, through the portal — that can be chain-bound on our side, if the Department wants it. Not your workpapers. Just the fact of the access, against our files. The specification has an access-trail primitive for exactly that; it's the same mechanism we use to record who inside the bank reads a privileged investigation file. It means that a year from now, if there's a question about who saw a confidential customer record during the exam, there's an integrity-bound answer on the bank's side, independent of the bank's own say-so."

Delia had come in for this part.

**Delia:** "We'd use it. Confidentiality is a hard constraint for us, not a nice-to-have. The Report of Examination and everything under it is confidential supervisory information. If the bank can show, integrity-bound, that examiner access to confidential files was scoped and recorded — that helps *us*, because it protects the bank's customers and it protects the Department from a claim that we mishandled a record. As long as it's the *fact* of access on your side, and never our judgment or our workpapers, which stay ours."

**Renata:** "Never your workpapers. That's the line. Your side is yours."

Emmett had one more question, and it was the one that tied the whole day back to the diagram on the wall.

**Emmett:** "The verifier printed a supervisory context on every verdict. Charter type, state supervisor, federal supervisor, the dual-supervision posture. Where does that come from, and why is it in the record?"

**Renata:** "It's a small attribute family the record carries. It binds the supervisory context into the evidence itself — that this decision, this artifact, was produced under a Texas state charter, dual-supervised, with the FDIC as the federal prudential supervisor. Same caveat as the incident determination: the chain proves we *recorded* that context and didn't alter it, not that it's metaphysically true. But it means a record doesn't lose its supervisory context when it travels. Four years from now, in a different proceeding, someone reading this chain entry knows it was rendered under Texas authority, in an alternating cycle, without having to reconstruct that from the letterhead."

**Emmett:** "And the profile flag. `tx-dob`. That changed what the verifier printed. Did it change what the verifier *decided*?"

Renata said it with a small emphasis, the emphasis of someone who knew this was the one place the whole thing could have gone wrong.

**Renata:** "No. The profile changes the vocabulary and the framing — which markers the report surfaces, how it names the Texas-specific things, that it prints the 7 TAC §3.24 reference on the incident notice. It does not change a single accept-or-reject decision. It cannot change PASS to FAIL or move an exit code. If it could, then the same chain would verify differently for a Texas examiner than for a federal one, and the whole guarantee — that two verifiers walking the same chain reach the same verdict — would be dead. So the profile sits strictly above the integrity check. Run the same chain with the federal profile and the Texas profile: same PASS, same exit code, different words on the page. I can prove that to you if you want; there's a test that asserts exactly it."

Emmett thought about it.

**Emmett:** "I do want that. Because if the profile could change the verdict, then 'the Texas exam counts the same as the federal exam' would be a lie at the tooling level, and the whole reason a state-only cycle carries federal weight is that it's the *same* underlying check. Show me the two profiles agreeing on the verdict and disagreeing only on the words."

Renata ran it. Same chain, `--profile ffiec` and `--profile tx-dob`. Two runs. Identical verdict. Identical exit code. The only difference was the framing — the Texas run named the charter authority and the state incident rule; the federal run didn't. The integrity core was byte-for-byte the same decision.

> ### Confirmation #5 — The verifier's Texas profile changes framing only, not the verdict; the tooling enforces the identity that lets a state-only cycle carry federal weight
>
> The examiner confirmed that the verifier's Texas profile changes only reporting vocabulary and framing — surfacing the charter authority, the dual-supervision posture, and the 7 TAC §3.24 reference — while the underlying integrity verdict and exit code are identical to the federal profile on the same chain. The scope boundary held cleanly: the chain covers institution-side evidence, not examiner workpapers or the Report of Examination, and the fact of examiner access to confidential files can be access-trail-bound on the bank's side without ever reaching the examiner's work product. A state-only cycle carrying the same weight as a joint federal exam depends on the underlying check being the same check; the tooling enforced that identity rather than merely asserting it.

*That's the CSBS accreditation argument, in code*, Delia thought, watching the two identical verdicts. *We're accredited so that a federal regulator will accept our exam in lieu of doing their own. The accreditation certifies the examiners. This certifies the evidence. Different layers. Both saying the same thing: a state exam and a federal exam should reach the same answer. It's the first time I've watched a machine agree with the principle.*

## 4:30 PM — The Examiner-in-Charge closes the day

```
4:30 PM CDT. Boardroom, bank sent out. Delia running the findings
                          round with the team before anyone falls in love with
                          the technology.
```

Delia gathered the team at four-thirty, sent the bank out of the room, and did the thing an EIC does at the end of a strong day, which is to make sure nobody had fallen in love.

**Delia:** "Before anybody tells me this was the best-run bank they've ever seen, I want the findings. Real ones. What are we writing."

**Emmett:** "One IT finding, real, in front of the board: the key-registry retention was set to three years against a longest-lived chained artifact of five years — the BSA records. Left alone, the bank's oldest BSA evidence goes unverifiable in year four, exactly when it's most likely to be subpoenaed. The bank changed the configuration this afternoon and brought me the corrected setting. I've confirmed the new retention floor is five years plus a margin. It's a matter requiring board attention because the board should understand the failure mode, not because it's unresolved."

**Delia:** "Lauren, you're the BSA side of that same finding."

**Lauren:** "Same root cause, written into the BSA booklet from the records-retention angle. One finding, two booklets, cross-referenced."

**Delia:** "Hank."

**Hank:** "Two substandard credits, both already on the bank's watch list, both adequately reserved. No doubtful. No loss. Management didn't fight the numbers. Asset quality is a two."

**Delia:** "Priya, governance."

**Priya:** "Board minutes are continuous and complete. Loan-committee approvals tie to the credits. Attendance is documented. The chain let me confirm the minutes I reviewed are the minutes adopted at the time — no post-hoc editing. Management and governance look like a two."

Delia nodded, and did the arithmetic she'd been doing in her head all afternoon.

**Delia:** "So here's where I am on ratings, and it's preliminary until I write it and until Austin reviews it. Composite looks like a two — a sound bank with a manageable finding, not a problem bank. On the IT side, URSIT: Audit is strong, Management is strong, Development and Acquisition is strong, Support and Delivery has the one retention finding that's already remediated. URSIT composite two. Which feeds the safety-and-soundness Management and Sensitivity components, and those hold at two. No MOU. No Commissioner's order. A clean report with one finding the board needs to see and one that's already fixed."

She looked around the table.

**Delia:** "I want to be careful about one thing, because it's a trap, and Emmett already saw it this morning so I'll say it to the whole team. We are not giving this bank a better rating *because* they run a chain. The chain isn't a control that earns a number. It's a tool that changed how *we* worked — we verified provenance we used to have to take on faith, we proved an incident-notification ordering we used to have to accept as represented, we confirmed a GL extract was whole instead of asking nicely. The rating reflects the bank's condition. The chain reflects our confidence in the evidence behind the rating. Don't confuse the two in the report, because Austin will catch it and they'll be right to."

Emmett had walked in this morning calling it a fancy pen, and he felt he owed the table the correction out loud.

**Emmett:** "Understood. And — for the record. I came in this morning ready to write that a self-signed evidence chain was a liability dressed as a control. I don't think that anymore. Not because they impressed me. Because I checked the signer myself, without their help, and re-ran the evidence myself, and it agreed with itself when I tried to break it. The finding I'm writing is a real finding. But the chain earned its place today by answering the one objection I actually had, and it answered it with math instead of asking me to trust them."

Delia let that sit for a second.

**Delia:** "Write it exactly that way. Not the enthusiasm. The mechanism. An examiner reading our report in three years should be able to tell the difference between 'the bank has a good story' and 'we verified it ourselves and here's how.' That difference is the whole reason we get paid."

She closed her folder.

**Delia:** "Exit meeting tomorrow morning, nine o'clock, management. Marisol, the CISO, the CIO, the CEO if he wants to be there. I'll preview the two findings, the classifications, and the preliminary ratings. Then the board meeting — I want the full board for the key-registry finding, because it's the kind of thing a board needs to hear from us directly, not filtered through management. The Report of Examination goes out from Austin in the usual weeks. It's confidential supervisory information; the bank holds it, the bank doesn't publish it. Same as always."

Marisol had come back to the doorway to hear the shape of it.

**Marisol:** "Same as always. Thank you, Delia."

**Delia:** "Thank you for a clean week. The finding's real. The bank's sound. That's the report."

## 5:40 PM — After

```
5:40 PM CDT. Boardroom emptying. Emmett finishing the IT booklet
                          while it's fresh. Renata packing up two laptops. Long
                          gold light over the piney woods.
```

Emmett stayed after the others had packed up, finishing the IT booklet while it was fresh. Renata found him there, packing up her own two laptops.

**Renata:** "You got your finding."

He didn't look up.

**Emmett:** "I got my finding. You know the thing I'm actually going to remember from this exam? It's not the cryptography. I understood the cryptography before lunch. It's that when I handed you a finding in the hallway, you fixed the configuration before I'd finished writing the sentence. Banks don't do that. Banks argue. You saw the failure mode faster than I could explain it and you closed it before you'd have to."

**Renata:** "Because you were right. The whole point of building the thing was to be checkable. If I argue with the examiner who checks it, I've thrown away the reason I built it. The chain only means anything if the examiner can find the crack and I close it. You found a real crack. Three-year retention on five-year evidence. That's a crack. I'd rather you find it now than a grand jury find it in year four."

Emmett finally looked up.

**Emmett:** "Here's what I keep landing on. For fifteen years, the last line of every evidence conclusion I've ever written was, in one form or another, *as represented by management.* Every loan file. Every incident timeline. Every extract. I reconcile what I can tie out, I trust the rest, and I sign it *as represented.* That's the job. That's always been the job. Today's the first day I got to cross that line out on a few of them and write *verified* instead. Not all of them — the determination time is still your assertion, the classifications are still my judgment. But the provenance, the completeness, the ordering — those I checked myself. That's new. In fifteen years, that's new."

**Renata:** "That's the whole idea. You were never supposed to have to trust us. You were just never given the tools not to."

Emmett went back to the booklet. He'd already written the finding. Now he wrote one more line into his own examiner notes, the ones that didn't go in the report, the ones that were just for the next examiner who'd draw a bank running one of these:

*If a bank hands you an evidence chain, don't be dazzled and don't be dismissive. Do both things I did today. Validate the signer yourself, without their tooling, against a published root they can't quietly change — if you can't confirm the key independently, the whole thing is a fancy pen and you write it up as one. Then try to break it, corrupt one byte and watch whether it catches you at the byte. If it survives both, you can write "verified" instead of "as represented" on the provenance and the ordering — but never on the human determinations, and never on your own judgment. The chain proves the file wasn't changed and the order things happened in. It does not prove the bank was right. Keep that line clean and the tool is worth more than any bank's word. Blur it and you've overclaimed, and the first defense lawyer who reads your report will make you regret it.*

He closed the laptop.

Outside, over the piney woods, the light was going long and gold the way it did in East Texas in the early evening, and somewhere in Austin the Commissioner's office would, in a few weeks, receive a Report of Examination for Success Bank with a composite of 2, a URSIT of 2, one finding remediated and one for the board's attention, no order, no memorandum of understanding — and, buried in the IT booklet, a paragraph that a Department examiner had written the word *verified* into, and meant it, for the first time in his career.

*It never is a clean week*, Delia had said that morning, out of long habit. It usually wasn't.

This one was close.

## The chain, mapped to the Texas exam

This engagement exercised no purpose-built spec-section family. It confirmed that the chain's foundational capabilities answer the questions a Texas exam actually asks — provenance, completeness, ordering, and the identity of the signer — and that a verifiable chain lets the examiner re-run the evidence rather than accept an attestation. That is the engagement's whole point: for the first time, an examiner could write *verified* where the job has always forced *as represented by management.*

### The tamper-evidence anchor — the self-signed-evidence answer

**What Success Bank operates.** Per-event MAC over each artifact's canonical bytes; hash-linked entries; a daily Merkle seal signed by an HSM-resident key at daily cadence; the seal fingerprint published to a location outside the ledger's account; an HSM-signed key registry under separation-of-duties custody, published with its own signature.

**What the examiner verified.** That "the bank signs its own evidence" is answered by tamper-evidence, not attestation. A false PASS requires simultaneous compromise of three independent custody layers — capture, seal, and registry. The examiner validated the registry against a separately-published root with his own tooling, confirmed a seal's key fingerprint by hand, re-ran the verifier for agreement, and produced FAIL at the byte on a deliberate corruption.

### The provenance anchor — reconciliation's complement

**What Success Bank operates.** Every exam artifact bound by hash at production time under the `audit.exam_artifact.artifact_kind` vocabulary (board_minutes, loan_file, gl_extract, policy, log, bsa_record); GL-extract and loan-download jobs chained as parent runs whose child rows reference the job and whose entry names the count produced.

**What the examiner verified.** That reconciliation and the chain answer two different questions and the exam uses both — reconciliation proves internal consistency (foots to the GL), the chain proves provenance (this is the file the bank held) and completeness (the extract is whole; a dropped account surfaces as a count mismatch). The appraisal driving a substandard classification hashed to a seal eight months old.

### The ordering anchor — 7 TAC §3.24

**What Success Bank operates.** Incident-response events chained; the customer-notification event binds the hash of the regulator-notification event, which was sealed into an earlier, signed, published daily root.

**What the examiner verified.** That the regulator-before-customer ordering the Texas rule turns on is cryptographically provable — the later event is built from the earlier event's hash, and the seals landed in separate published roots on separate days, so the order cannot be reversed after the fact. The incident-determination *time* remains an institution assertion; the *ordering* does not.

### The retention finding — IKM registry vs. the five-year BSA floor

**What Success Bank operates.** An HSM key registry whose retention had been set to three years, matched to the Call Report window.

**What the examiner verified.** That the key-registry retention floor must be at least as long as the longest-lived *chained* artifact, and Success Bank's longest is a five-year BSA record — so a three-year floor would render the oldest, most-subpoena-prone BSA evidence unverifiable in year four. Remediated on-site; a matter for the board's attention, not an order.

### The determinism anchor — the tx-dob profile

**What Success Bank operates.** A verifier profile (`tx-dob`) that surfaces the charter authority, the dual-supervision posture, and the 7 TAC §3.24 reference, and an `audit.supervisory.*` attribute family that binds the supervisory context into the record.

**What the examiner verified.** That the profile changes only reporting vocabulary and framing — never a verdict or an exit code. The same chain under `--profile ffiec` and `--profile tx-dob` produced identical PASS and identical exit code. The tooling enforces the identity that lets a state-only cycle carry the same weight as a joint federal exam.

## Engagement debrief — Delia's voice

> "It never is. But Success Bank is the cleanest example I've worked of the difference between a bank with a good story and a bank you can actually check. The Department has run the same three-legged stool my whole career — the bank's attestation, our reconciliation, the secure portal. It tells you the numbers cross-tie. It never told you the file the bank uploaded on Tuesday was the file that existed on Monday. This is the first exam where an examiner of mine could answer that question with math instead of a signature line.
>
> "The load-bearing beat wasn't the technology. It was Emmett. He walked in calling the chain a fancy pen — the bank marking its own homework — and he was right to. A self-signed record is worth nothing if you can't confirm the signer without asking the signer. So he did. He pulled the key registry off the open internet, validated it against a published root with his own script, confirmed a seal's fingerprint by hand, and only then ran their verifier. He didn't trust them. He trusted the math, and the math agreed with itself when he tried to break it. That's the whole product, and he found it himself, which is the only way an examiner ever believes anything.
>
> "The finding is real and I want it read as real. Their key-registry retention was set to three years against five-year BSA records — the oldest evidence they most need to prove would have gone unverifiable in year four, exactly when a grand jury would ask for it. They fixed it in the hallway before Emmett finished the sentence. A bank that's faking the control argues about the finding. A bank that means it thanks you for it. That told me as much as the cryptography did.
>
> "The trap I made the team say out loud: we do not rate a bank higher because it runs a chain. The chain isn't a control that earns a number. It changed how *we* worked, not how *they* stand. Composite two, URSIT two, one finding remediated and one for the board — that reflects the bank's condition. The chain reflects our confidence in the evidence behind it. Keep those two things separate in the report or Austin will separate them for you.
>
> "The next time one of us draws a bank running one of these — and there will be a next time — the discipline is what Emmett wrote in his own notes. Validate the signer yourself. Try to break it. Write *verified* on the provenance and the ordering, and keep it off the human determinations and off your own judgment. The chain proves the file wasn't changed and the order things happened in. It does not prove the bank was right. Hold that line and the tool is worth more than any bank's word."

## Cross-references

- **Spec impact**: §1.1 (compositional security — the three-layer simultaneous-compromise model behind the self-signed-evidence answer), §1.2 (epistemic scope — integrity and ordering proven, human determinations institution-asserted), §7 (verifier recreates the original record byte-equal or proves alteration; exit-code contract exercised at exit 2 on the deliberate corruption), §10.1 (key-fingerprint reconciliation, done by hand before the verifier ran), §10.5 (separation-of-duties HSM custody), §10.9 (IKM/key-registry retention floor — the finding), §10.13 (evidentiary-artifact composition), §10.19 (chain-coverage map / CC8.1 declaration), §10.70 (access-trail primitive — examiner-access provenance on the bank side), §10.76 (HSM-signed IKM registry manifest — the independently-validatable trust anchor), §10.84 (approval/ordering primitive — the after-event binds the prior-event hash), §14.13 (`audit.supervisory.*` family — charter authority and dual-supervision context), the `audit.exam_artifact.artifact_kind` shared vocabulary, and the presentation-only `tx-dob` verifier profile.
- **Regulatory citations**: 7 TAC §3.24 (Texas cybersecurity-incident notification — Commissioner before customers, within fifteen days; interagency 36-hour notice satisfies it); Texas Finance Code Title 3 (state-charter authority); the FFIEC IT Examination Handbook and FDIC InTREx program (the IT exam scaffolding); URSIT (Audit / Management / Development & Acquisition / Support & Delivery, feeding CAMELS Management and Sensitivity); CAMELS (the safety-and-soundness composite); CSBS accreditation (why the alternate-year state exam carries federal weight); Call Report retention (three years) and BSA-record retention (five years) as the retention floors behind the key-registry finding.
- **Documented finding**: key-registry retention floor set below the longest-lived chained artifact (three years against five-year BSA records). Remediated on-site; recorded as a matter requiring board attention, not a Commissioner's order.
- **Auditor stories**: this is the first examiner-side engagement in the corpus where the protagonists are the regulator rather than an external audit firm, and the first Texas Department of Banking exam. It shares the Texas community-bank register with Story 20 Mission Plaza Bank and Story 21 Brazos Federal, and the FFIEC IT-Handbook foundation with the banking engagements (Story 01 Northbridge, Story 04 Atrio, Story 12 Hill Country). The through-line is the shift from trust-by-attestation to trust-by-reproduction — the examiner re-runs the evidence rather than accepting the bank's word.

The Report of Examination and its supporting workpapers are filed under the Department's confidential-supervisory-information custody; the bank holds its copy of the report and does not publish it, and the chain artifacts the exam relied on remain under the institution's own retention with the corrected key-registry floor now exceeding the longest BSA window.
