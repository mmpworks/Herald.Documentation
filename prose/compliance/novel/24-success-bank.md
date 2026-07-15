# 24 — Success Bank

> Success Bank — a Texas state-chartered commercial bank, ~$2.9B consolidated assets, home office in a limestone office park off the southbound MoPAC frontage road in Austin, just west of Zilker Park. A state nonmember bank, so its federal prudential supervisor is the FDIC — but this is the alternate-year cycle, and the Texas Department of Banking examines alone. The bank has run a cryptographic chain-of-custody across its regulated evidence for a little over a year: loan-file provenance, board-minute binding, GL-extract hashing, the AI credit-decisioning surface, and its incident-response records. The team is on-site at the request of Success Bank's Chief Risk Officer for a three-day readiness-and-support engagement — but it is structurally different from every engagement before it. Across fourteen prior engagements the team prepared institutions for a regulator who would arrive weeks later; at Mission Plaza and Brazos, both Texas state charters, the team prepped for "the Texas Department of Banking examiner" as an off-page institutional fact — the examiner who "closed it in one meeting," always referenced, never met. This time the TDoB team is already in the building. For the first time in the firm's history the audit team is in the room while a live examiner works a chain — and no examiner has ever seen one. The recurring question all week is *"can the examiner check it himself?"* — and one examiner walks in not believing the answer can be yes, and says so out loud in the first hour. Raj is Lead. Dawn joins mid-day as MMPWorks's TesseraSeal liaison under the spousal-disclosure paragraph; Steve appears by video for twenty minutes on a single §10.21 question. It is, of all the cities the firm has worked, Steve's.

## The team and the day

The full eight travel: Raj, Elena, Mike, Diana, Luis, Chen, Tom, Sonya. Raj has been Lead Auditor for just over a year — the chair passed to him after Mission Plaza, Dawn's last as Lead before her move to MMPWorks. The specialties are the ones the firm has carried across two dozen engagements: Raj on the database and the chain walk, Elena on CRM and the model surfaces, Mike on the application and API layer, Diana on identity and access control, Luis on the seal job and the HSM signature trace, Chen on the ledger ingest and trusted time, Tom as internal-audit liaison running his standard four questions with the client's audit executive, and Sonya — twenty-two years of hardware and supply-chain custody out of a federal-logistics division before the firm, now four engagements past the newcomer framing — on the physical custody chain, which on this engagement means the hardware security module and the key registry it protects. Success Bank's home office is a low limestone building in an office park off the southbound MoPAC frontage road — the kind of glass-and-stone complex where a coastal-cooking place called Salt Traders shares the lot, and where Zilker Park and the Barton Springs pool are a couple of minutes east toward the river. The bank's Chief Risk Officer and head of internal audit is **Cindy Martinez**, ex-FDIC out of the Dallas field office nine years ago — she knows the exam from the examiner's chair, which is exactly why she called the firm. The Chief Information Security Officer, **Rachel Gonzalez**, stood up the chain fourteen months ago and owns it. The CIO is **Bobby Smith**; the SRE who runs the screens is **Kyle**. And down the hall, in a commandeered third-floor conference room the bank cleared out on Friday, the Texas Department of Banking has already set up.

## The drive-in monologue

```
6:55 AM CDT. Rental SUV, downtown Austin, from the hotel on
                          South Congress across Lady Bird Lake, then south on
                          MoPAC to the Success Bank office park on the
                          southbound frontage road, west of Zilker. Raj
                          driving. Sonya in the passenger seat for
                          her second turn in the right seat since Raj took the
                          chair.
```

**Raj:** "Engagement twenty-four. Success Bank. Austin. Three days. Readiness-and-support — and the first time the firm has ever been in the building while the examiner is."

**Sonya:** "That's the part I couldn't place when I read the letter. We've never overlapped with a regulator on-site."

**Raj:** "We've come close. Wasatch, we cleared out the morning the OCC and the Fed and nine state examiners walked in — we were gone before they sat down. Every other engagement, the examiner is three weeks out and we're building the memo they'll read before the entrance meeting. — This one, the Texas Department of Banking is already down the hall. They set up Friday. We're not prepping for an examiner who arrives later. We're in the room."

**Sonya:** "Why us in the room at all?"

**Raj:** "Because no examiner has ever seen a chain, and Cindy knows exactly how an examiner reacts to something they've never seen. She sat in that chair nine years at the FDIC. Her read is that a state examiner who's never met a chain-of-custody distrusts it on sight — that the first thing out of their mouth is going to be some version of *the bank signed its own evidence.* And she's right. So she retained us to be in the room when that happens. Not to argue for the chain. To help the examiner check it himself. That's the whole design of the thing — the examiner isn't supposed to take the bank's word. He's supposed to re-run it. Our job is to be there when he decides whether he believes that."

Sonya looked out at the lake going past.

**Sonya:** "Fourteen prior contexts. You want the recitation?"

**Raj:** "You do it. You've earned a turn at it."

**Sonya:** "Northbridge was the high-water mark. Atrio was the multi-bank platform. The European arc through six countries. Wasatch was the payments network on the fast clock. Hill Country was the credit-union marketing swap — and it was here, in this city, three years back. Saraswati was the edge-AI work. The Northbridge return was the M&A pattern. Polaris was the reinsurance horizon. Lyceum was the FDA foresight. Helvetian was the parliamentary scale. Argent Vector and Aerolith were the defense-and-frontier cluster — my first. Mission Plaza was the community-bank scale and the bench transition. Brazos was the post-merger integration. Aldergrove was the first SRO-flavored engagement." She paused. "Success Bank is the first time we watch the examiner instead of the bank."

**Raj:** "That's the shape. — And say the Texas part, because it's the part that matters."

**Sonya:** "Mission Plaza and Brazos were both Texas state charters. Both times we prepped the bank for the Texas Department of Banking examiner. Both times the examiner was a sentence in the workpaper — *the Texas Department of Banking examiner closed that line in one meeting at the March cycle.* We never met them. Two engagements, and the TDoB examiner was a fact we referenced and never a person we sat across from."

**Raj:** "And this week the sentence gets a name. — One more thing. It's Austin. Which means it's Steve's city, and Dawn's now, and the whole recusal apparatus is closer to the surface than it is anywhere else we work. Dawn joins at noon under the spousal-disclosure paragraph as MMPWorks liaison. Steve does twenty minutes by video on one §10.21 question and nothing else. Tom logged the language Friday. We keep the vendor line clean because in this city everyone can see it."

The SUV came off the bridge onto MoPAC southbound and dropped down to the frontage road, past a coastal place with SALT TRADERS on the sign already setting up for the lunch rush. The bank's limestone front came up in the office park behind it, a Texas flag flying at the same height as the U.S. flag on a single crossbar — the state-charter convention Raj registered without comment.

**Raj:** "It never is."

Sonya had heard the line explained on her first day, in a back seat, at Argent Vector, and had asked what it meant, and Tom had told her it was Dawn's, and that it could carry a pessimism or a wish. She had watched Raj inherit it the way you inherit a house.

**Sonya:** "It never is."

*He says it now*, she thought, *as she used to. He used to be the one who told her she didn't get to write it in her notepad anymore. Now it's his.*

The SUV turned into the lot.

## 7:40 AM — Lobby

The lobby was cool limestone and glass with a view straight out across the office-park lot toward the frontage road, the Barton Creek greenbelt running green behind it. A receptionist checked the team in against a list; the badges carried a photo and a numeric escort code. Cindy Martinez was at the elevator bay with Rachel Gonzalez beside her.

**Cindy:** "Raj. Welcome to Austin. — I'll say the thing I said on the phone so the whole team hears it. I spent nine years examining banks for the FDIC out of Dallas. I know what a state examiner does when they walk into something they've never seen, and none of them have seen this. The Department set up Friday. Their Examiner-in-Charge is a commissioned examiner named Karen Wilson — twenty-three years, she signs the report. Her IT examiner is the one I'm watching. His name is Danny Tran, and he is going to distrust the chain on sight, and he is going to be right to, and I need him to be able to talk himself out of it. That's why you're here. Not to defend the chain. To stand next to the examiner while he tries to break it."

**Raj:** "That's the engagement as I read it too. Three days. We walk the chain with your people, we're in the room when the Department works it, we help the examiner re-run whatever he wants to re-run under his own hand, and Tom runs his four questions with you on the internal-audit side. We don't argue the examiner into anything. If the chain can't survive him checking it himself, that's the finding, and we write it."

**Cindy:** "That's the answer I wanted. — Karen opened with the Department yesterday afternoon; the first-day letter went to us four weeks ago, the IT Profile ninety days before that, and we staged the loan and asset data through the portal so their week is judgment work. They've taken the third-floor conference room. We've given you the technical room across the hall — it's where Rachel's people run the screens, and it's where Danny will come when he wants to see the chain, because that's where the chain is."

Rachel put in one line before the elevator came.

**Rachel:** "I told the Department the same thing I'm telling you. They don't have to believe me. The verifier is open source, the public key is published, and they can re-run any of it on their own laptops on the coffee-shop wifi across the street if they want. The whole point is that the bank doesn't get to be trusted. — Danny hasn't decided whether to believe that yet. That's the thing to watch this week."

Tom, who had been quiet, wrote a line in his engagement notebook and turned it so only Raj could see it: *First time the examiner is a character and not a citation.*

## 8:30 AM — Kickoff, and the room across the hall

```
8:30 AM CDT. Bank technical room, third floor. Two screen walls,
                          Kyle at the console. The team on one side of a long
                          table; Rachel and Bobby opposite. Across the hall, the
                          Department's commandeered conference room, door shut.
```

Rachel walked the architecture as an owner does, without a deck. Loan files, board and committee minutes, general-ledger extracts, the policies, the logs, the BSA records, and the AI credit-decisioning model that sat between the loan-origination system and the core — every artifact, when produced or captured, landing as a signed entry in an append-only ledger, each entry carrying a keyed hash over the artifact and the hash of the entry before it, and once a day a single root computed over the day's entries and signed by a key inside a hardware security module. The signature was the seal.

**Chen:** "Same substrate we walked at Brazos and at Aldergrove. Daily cadence?"

**Rachel:** "Daily. Seal at two in the morning, Central, under CloudHSM. We're a wealth-and-commercial bank; we don't need a per-second seal. The AI credit-decisioning surface is the only fast path, and even that seals daily."

**Mike:** "And the credit-decisioning model — inputs, outputs, model version, the reason codes on an adverse action?"

**Rachel:** "All bound on the generation entry. The adverse-action reason codes and the notice text are chained under the ECOA family. We had one consumer reinvestigation in the spring; the whole timeline walked in fifteen minutes. That's the kind of thing your Mission Plaza and Brazos memos told our board to expect, by the way. We read them. The §10.13 evidentiary composition, the retention-floor language — half of what we built, we built off memos your firm wrote for other Texas banks."

Raj registered that without making anything of it.

**Raj:** "Then you know how we work. — Here's the plan. Chen takes the ledger and the entry structure. Luis takes the seal job and the HSM signature trace. Sonya takes the module custody and the key registry, because that's the piece the examiner is going to distrust first and hardest. Diana takes the access trail. Elena takes the credit-decisioning surface and the incident-notice content. Mike takes the architecture and holds the one §10.21 question for Steve. Tom runs his four questions with Cindy. And when the Department wants to see the chain, we're across the hall and we help them see it under their own hand. — Rachel, where's the examiner now?"

The door across the hall opened before Rachel answered. A man in his late thirties, sleeves rolled, a laptop under one arm, crossed the hall and stopped in the doorway of the technical room. Behind him, unhurried, an older woman in a gray jacket with a Department lanyard.

**Rachel:** "Danny. Karen. — This is the readiness team the bank retained. Raj is their lead."

**Karen:** "Wilson, Examiner-in-Charge. — I'll be straight with the room, because it saves time. The Department doesn't usually share a floor with a bank's consultants during an examination, and I thought hard about the optics before I agreed to it. I agreed because Ms. Martinez made a case I couldn't argue with — that the thing on these screens is something none of my examiners has seen, and that the fastest way for my IT examiner to test it is to have the people who understand it in the building while he does. You are not going to sit in my exit meeting and you are not going to touch my workpapers. But when Danny wants to re-run something, you can be in the room. That's the arrangement."

**Raj:** "Understood on all of it. We're here so your examiner can check the bank's evidence himself, not so he takes anyone's word — the bank's or ours. If it doesn't survive that, we'll be the first to write it down."

Danny Tran had not sat down. He was looking at the screen wall, where Kyle had left a chain entry expanded.

**Danny:** "Can I say the thing I'm going to be thinking all week, so nobody has to guess."

**Karen:** "Say it, Danny."

**Danny:** "The bank built this. The bank runs the ledger. The key that signs the seal is the bank's key, in the bank's module, in the bank's cloud account. So when the verifier says PASS, all it's telling me is that the bank's evidence matches the bank's signature over the bank's evidence. That's a bank signing its own homework. A fancier pen than a wet signature on a board minute, but the same act. — Fifteen years I've read evidence a bank handed me and written *as represented by management* at the bottom of the conclusion, because that's all the honesty the job entitles me to. I don't see yet how a cryptographic version of the bank's own say-so gets me past that line. Convince me it does, or I write it up as a fancier pen."

The room was quiet for a second. Raj did not look at Rachel and did not look at his own team. He'd watched this objection get raised, in less precise words, by a dozen skeptics on a dozen engagements, and it had never once been raised by the person whose belief actually determined the outcome. Every prior time, the skeptic was the bank's board, or an internal-audit committee, and the regulator was three weeks away and off-page.

*This is the first time the objection comes from the chair that decides it*, Raj thought. *Cindy was right. Let him chase it. Don't argue him out of it. Let Sonya hand him the thread and let him pull it himself.*

**Raj:** "That's the right question, and it's the only one that matters, and I'm not going to answer it with a speech. Sonya's going to hand you the piece of it you can check without trusting anybody in this building, and then you're going to check it. If it holds, you'll have talked yourself out of the objection, which is the only way anyone is talked out of anything. If it doesn't hold, you found the biggest finding of the week and we'll help you write it."

**Danny:** "When."

**Sonya:** "Now, if you want. It's my piece."

## 9:30 AM — The custody chain, which is Sonya's

Sonya had spent twenty-two years proving where hardware had been — which loading dock, which sealed container, which RMA, which chip out of which tray — before she ever heard the phrase *chain-of-custody* used about a log file. She thought about the key registry as she thought about a tamper-evident shipping seal, and she started where she always started, with the thing you could hold.

**Sonya:** "You said the bank's key, in the bank's module. Let's take that apart, because 'the bank's key' is doing more work in that sentence than it can hold. — The key that signs the daily seal lives inside a hardware security module. It's generated inside the module and it cannot leave the module. Nobody at this bank has ever seen it, including the woman who built the whole system. The module signs when it's asked to sign; it does not hand out the key. So the first thing to separate is the key from the people. The bank does not have the key. The module has the key. The bank has the ability to ask the module for a signature — which is a different power, and it's a power that leaves a record."

**Danny:** "Fine. The module has the key. The bank runs the module."

**Sonya:** "The bank runs the module under separation of duties, and this is the part you can verify, so don't take it from me. The person who can request a seal signature is not the person who can change the registry that says which key is valid, and neither of them can extract the key. Three roles, three people, three controls. — Now, the registry. There's a published manifest that lists every signing key the chain has ever used, with a fingerprint for each and the window each was valid, and the manifest is itself signed, by a separate root of trust in the module, under the third role that neither of the first two can touch. That manifest is published, and its signature is published, in a place the ledger's own cloud account cannot reach in to change."

She slid a printed page across the table — the registry manifest, fingerprints and validity windows and a signature block at the bottom. Luis put the daily-seal record for a date up on the screen wall beside it.

**Sonya:** "So here's your check, and it does not require you to believe one word from anyone at Success Bank. You take a daily seal — pick any day. You read the key fingerprint the seal claims. You pull the published manifest off the open internet, no credential. You validate the manifest's signature against the published root with your own tool, not ours. Then you confirm the seal's fingerprint is in the manifest, and was valid on the day the seal was signed. If it is, the seal was signed by a key the bank cannot have swapped, because to swap it the bank would have to forge a new manifest signature under a root it doesn't hold. — That's the piece. Check it."

Danny looked at the manifest for a while.

**Danny:** "So the attack isn't 'forge one entry.'"

**Luis:** "No. Walk it. Alter one old artifact — one digit in a loan balance from last spring — and that entry's keyed hash stops recomputing. Fix the hash, and the next entry's link is wrong, because it pointed at the old one. Fix that, the next one breaks. You'd have to re-derive the whole tail from the point of the change. Then the daily root over that day comes out different — and the original root was signed and published a year ago, in a place your account can't reach. So you'd have to forge the historical seal too. And to make the forged seal check out, you'd need a signing key the published manifest vouches for on that date — which means forging the manifest signature, under a root held by the one role that can't request seals and can't extract keys."

**Sonya:** "Three custody layers. The specification is explicit that a false PASS — a tampered chain that verifies clean — takes compromising all three at once. Not one. The capture that writes the keyed hash, the seal that signs the daily root, and the module custody that vouches for the key. Different keys, different people, different controls. That's the whole answer to 'the bank signed its own evidence.' The bank can sign its evidence. The bank cannot sign it *twice* — once honestly today, once dishonestly next year — without the second signature disagreeing with the first in a place the bank doesn't hold."

> 💡 **Quick picture.** A wet signature on a board minute proves one thing: that a pen touched paper. If someone retypes the minute next year and signs it again, you have two documents and one bank's word about which is real. A tamper-evident shipping seal is different — you can't re-close it without the break showing, and the seal number is registered somewhere the shipper doesn't control. The chain is the shipping seal, not the wet signature. The bank can seal a box. It can't un-seal and re-seal a box from last year without the break showing in a registry it doesn't hold. The examiner doesn't have to trust the shipper. He reads the seal number off the box and looks it up in a registry the shipper can't quietly edit.

Danny closed the laptop halfway. Not all the way. Halfway.

**Danny:** "I'm not checking this with your tool."

**Sonya:** "I'd think less of you if you did. Use your own."

## 10:30 AM — The examiner checks the signer

Danny went back across the hall to the Department's room and did not come back for fifty minutes. When he came back he had four lines of his own script on his laptop and the look of a man who had tried to catch someone in a lie and failed.

Diana had watched him go and had said the thing the team was all thinking.

**Diana:** "He's going to validate the manifest before he runs the verifier. He's going to do it in the wrong order on purpose — signer first, verifier second — so that when the verifier agrees it isn't telling him anything he didn't already prove by hand."

**Raj:** "That's what I'd do. That's what makes him the right examiner for this. Let him."

When Danny came back he addressed the room, not any one person, as an examiner does when he wants it on a record he controls.

**Danny:** "I pulled the manifest off your compliance page over the open internet, no credential. I pulled the published root from the second location, the one outside the ledger account. I wrote my own four lines and validated the manifest signature against the root myself — it's a standard algorithm, I did cryptography on my boards. Valid. Then I took the seal for April 22nd, on purpose, because April is the month I care about, and I read its key fingerprint, and I found it in the manifest I'd just validated by hand, valid that day, in the partition the manifest names. Only then did I run your verifier."

Kyle put the run on the screen wall.

```
$ ffiec-verify --tenant=success-bank-prod --date=2027-04-22 \
               --strict --profile tx-dob --explain
Verdict: PASS
Step:    12/12
Exit:    0
Signature: verified against key 4b1e7... (registry-vouched,
           valid on 2027-04-22, partition hsm-p2)
Late-binding entries: 6  (see anomaly section)
Profile: tx-dob (Texas Department of Banking)
Supervisory context: charter_type=state_commercial;
           primary_state_supervisor=TX-DOB;
           federal_prudential_supervisor=FDIC;
           dual_supervision=alternating
Elapsed: 5.2s
```

**Danny:** "It agrees with the fingerprint I'd already confirmed by hand. So the verifier isn't telling me anything I hadn't checked myself. Then I did the other half. I copied one archived artifact to my own laptop, changed a single byte, and pointed the verifier at my copy."

```
$ ffiec-verify --tenant=success-bank-prod --artifact=./tampered.copy \
               --strict --profile tx-dob
Verdict: FAIL
Exit:    2
Reason:  per-event MAC recomputation failed at entry
         sb_2c9f... ; canonical bytes diverge at offset 0x41
```

**Danny:** "Failed at the byte and named the offset. I put the artifact back; it passed again."

He looked at Sonya, then at Rachel, then — briefly, and this was the thing Raj noticed — at Raj, the outside party with nothing to sell in the room.

**Danny:** "So it's not a fancy pen. The bank still signed its own evidence. But the bank can't change it after the fact without disagreeing with a signature I can check independently, and the bank can't get a forged key past a manifest custodied away from it. I trust the record because I re-ran it, not because anyone told me to. — I'll write that. Nobody in this room talked me into it, which is the only reason I believe it."

Rachel said the only thing she'd said in an hour.

**Rachel:** "That's the point of building it. If I could talk you into it, it would be worthless."

Raj wrote nothing down, because it wasn't his finding to write; it was the Department's. But he watched Tom, across the table, log it in the firm's own witnessed language — not the conclusion, which belonged to the examiner, but the fact of the event, which belonged to the engagement file — and he thought about how many times the team had told a nervous board that a real examiner *would* be able to verify the chain independently, and how this was the first time any of them had stood in a room and watched it happen.

> ### Confirmation #1 — Self-signed evidence is still tamper-evident under an examiner's independent check; the examiner validated the signer with his own tooling and reproduced the verdict
>
> The Department's IT examiner raised the load-bearing objection — "the bank signed its own evidence with its own key" — and answered it himself, not by accepting the bank's or the team's word. He validated the published key-registry manifest against a separately-published root of trust with his own script, confirmed a daily seal's key fingerprint by hand against that manifest, and only then re-ran the reference verifier, which agreed. A deliberate single-byte corruption produced FAIL with the offending entry and byte offset named. The bank's custody model puts a false PASS beyond reach of any single compromise — the per-event keyed hash, the daily HSM-signed seal, and the separately-custodied signed key registry are three independent layers. Trust was established by reproduction, witnessed by the team but performed by the examiner. The `--profile tx-dob` output surfaced the charter authority and the alternating dual-supervision posture directly in the verdict.

## 11:45 AM — Steve, twenty minutes

Mike had been holding one question all morning, because it was the one question the recusal protocol required him to route rather than answer. The credit-decisioning surface referenced prior model versions across a vendor boundary, and the composition of the §10.21 cross-vendor handover against Success Bank's own retraining cadence was a design question that touched the vendor's intent, and the firm's protocol did not let the team speak for the vendor. So at 11:45 the screen wall carried a video bridge to a conference room in a building four miles east, and Steve was on it — blazer over a button-down, a whiteboard behind him, slightly grayer at the temples than the last time the team had seen him on a screen.

**Steve:** "Mike. Twenty minutes, one question, and I answer only the §10.21 composition — nothing about the exam, nothing about the finding, nothing else on the screen. Tom has the language."

**Tom:** "Logged. The question is on the record; the window is on the record; the recusal frame is the spousal-disclosure paragraph and it's countersigned both sides."

Mike put the question — how the cross-vendor handover schema composed with the bank's quarterly retraining when the upstream vendor versioned on a different cadence — and Steve answered it, precisely, for eleven of his twenty minutes, and used the other nine on the one clarification Mike asked back, and then took himself off the bridge without drifting into a word about anything else. Danny, who had come back across the hall to watch, said nothing during it and one thing after.

**Danny:** "That's the vendor."

**Raj:** "That's the vendor. He answers the one composition question only the vendor can answer, on the record, in a fixed window, and he doesn't touch your exam or our engagement. The line between the vendor who builds the chain and the firm that helps you check it is one we keep visible on purpose, and in this city it's a line with a marriage on the other side of it, which is exactly why we keep it visible."

Danny wrote something down. Raj could not see it and did not try to.

## 12:30 PM — Lunch, the retention floor, and a thing Tom already knew

Somebody had walked across the lot to Salt Traders and come back with trays of Gulf fish and hush puppies; nobody left the building past that. Danny came in with the Department's asset-quality examiner, a heavyset man named Ray Hernandez who had spent the morning in loan files, and Karen behind them, and for a few minutes the two rooms were one room.

Ray had two credits he was calling substandard — a retail-strip loan out east where the guarantor's liquidity was gone, and an ag operating line paying interest out of principal — both already on the bank's own watch list, both adequately reserved, and he said so without heat, and Diana noted quietly to Raj that the bank not fighting the numbers was worth more to the exam than any control they'd walked all morning. But the thing that changed the afternoon came from Danny, and it was not a compliment.

**Danny:** "While I was in the registry this morning I looked at your retention on the key material. You've got the key registry set to hold three years. Where'd three come from?"

**Rachel:** "Call Report retention. Three years after the report date. We matched the longest artifact retention we thought we had."

**Danny:** "You don't have three-year artifacts as your longest. You've got BSA records. SAR and CTR support. Those are five years, and you're chaining them — I saw the BSA entries. So walk it forward. Four years out, someone wants to verify a chained BSA record from this spring. The artifact's there; you keep those five years. But the key material that lets the verifier confirm the seal over it — that you set to age out at three. In year four the record is still there and it's no longer verifiable, because you threw away the key that proves it wasn't altered."

Tom, who had been mostly silent since the morning's four questions, put his pen down. He had run the retention question at Mission Plaza and again at Brazos, and he carried the Texas floors the way other people carry phone numbers.

**Tom:** "He's right, and I can tell you why it's an easy mistake to make in this state specifically. At Brazos the retention floor was two numbers laid on top of each other — the Texas seven-year floor on customer records, and the FFIEC five-year floor on the AI-decisioning chain entries. When you're standing inside that, three years reads like the conservative *artifact* number, and it's easy to forget the key registry has to outlive the longest-lived thing it's *chaining*, not the shortest-lived thing you file. And your longest-lived chained artifact isn't the Call Report. It's the five-year BSA record. — Set the key floor to three and the oldest evidence you'll most need to authenticate is the first thing that goes dark."

**Rachel:** "We'll fix the setting this afternoon and I'll bring the Department the changed configuration. But it should still be written. If we did it, the next bank standing one up will do it."

**Danny:** "I'm writing it. It's a matter for the board's attention, not an order. But the board should understand the failure mode, because two more years and you'd have had a BSA record you couldn't authenticate the day you most needed to."

*She agreed to it before he finished the sentence*, Raj thought, watching Rachel already messaging Kyle to change the floor. *No committee, no let-me-check-with-counsel. That's the tell Cindy was buying when she put us in this room. A bank faking the control argues the finding. A bank that means it fixes it at lunch and thanks the man who found it.*

Melissa Johnson, the Department's BSA examiner, had come in on the tail of it and claimed the other half.

**Melissa:** "Then I've got the BSA-booklet side of the same finding, from the records-retention angle. One root cause, two booklets, cross-referenced. — Your consultant just did half my work with the Brazos number, for what it's worth."

**Tom:** "It's the pattern I keep writing in this notebook. The specification shipped the retention-floor discipline before this bank needed it; the bank set the floor wrong anyway; and the reason it's catchable at all is that the floor is a named, testable number instead of a habit. The tools keep arriving before the institutions are ready for them. I've stopped being surprised and started just writing it down."

> ### Confirmation #2 — The key-registry retention floor must outlive the longest-lived chained artifact; the examiner caught a three-year floor set against five-year BSA records, and the bank remediated on-site
>
> The Department's IT examiner found the key registry set to a three-year retention floor, matched to the Call Report window, while the bank chains five-year BSA records — so the oldest, most-subpoena-prone BSA evidence would have become unverifiable in year four, the artifact retained but the key that authenticates it discarded. The team's internal-audit liaison corroborated from the Texas retention floors carried out of the prior Brazos engagement (the state seven-year customer-record floor and the FFIEC five-year AI-decisioning floor). The bank changed the configuration on-site and produced the corrected setting; the finding was recorded as a matter requiring board attention, cross-referenced across the IT and BSA booklets, not an order.

## 1:45 PM — April, and the fifteen-day clock

```
1:45 PM CDT. Bank technical room. The spring incident record on the
                          screen wall. Danny leading it, Karen sitting in.
                          Rachel and Elena at the console; the incident's
                          response point person, Christina, beside them.
```

The incident had happened on the ninth of April. Danny had read it on the ninety-day IT Profile and again in the staged documents, and Elena — who owned the incident-notice content for the team — had read it three times, because the notice content was where the state rule lived.

**Danny:** "Walk me through it. Plain language, then the timeline, then how you prove the timeline — because with an incident the timeline is the exam, and the Texas timeline has one relationship in it I've never once been able to verify."

**Rachel:** "April ninth. A vendor that runs our online-banking session analytics disclosed a compromise. Our data was in scope — session metadata, not credentials, not balances, but enough to be a reportable incident. We spent the ninth and into the tenth confirming scope. We determined it was reportable on April tenth at 4:20 in the afternoon. That determination starts the Texas clock."

**Danny:** "7 TAC §3.24. Fifteen days."

**Elena:** "Fifteen days — notify the Banking Commissioner as soon as practicable, no later than fifteen days after determining a reportable incident. And before customer notification. The rule is explicit on the ordering: the regulator hears it before the customers do. It's written into the incident-response plan inside the information-security program, as the rule requires. — Timeline: determination April tenth 4:20 PM. Commissioner notified April eleventh 9:15 AM, using the interagency thirty-six-hour notice, which the Texas rule lets satisfy the state notice. Customers notified April fifteenth 8:00 AM. Regulator first, customers second, whole thing inside the fifteen days."

**Danny:** "That's a good timeline. It's also the timeline every bank tells me. Nobody has ever sat across a table and told me they notified the customers first. Six months later, out of an email thread, I can't tell the difference between doing it in the right order and telling it in the right order. That's the part I've never been able to check."

Chen, who had spent the morning inside the ledger, took it, because the answer was a ledger fact.

**Chen:** "You don't check it with the timestamps, and you shouldn't — a timestamp is a number a computer wrote. You check it with the linkage. The customer-notification event carries, in its bound payload, a reference to the regulator-notification event — it names the prior event's hash. The specification has a primitive for exactly that: an event can bind a reference to a prior event, and the verifier confirms the referenced event actually exists earlier in the sealed chain. So the customer notice doesn't say it came after the regulator notice. It's built out of the regulator notice's hash — a hash already sealed into April eleventh's root, signed and published four days before the customer notice existed."

Kyle ran the ordering check. Luis had the two seals up side by side — the eleventh and the fifteenth, two roots, two signatures, both against manifest-vouched keys.

```
$ ffiec-verify --ordering-check --profile tx-dob \
               --before=sb_regnotice_2027-04-11 \
               --after=sb_custnotice_2027-04-15
Verdict: PASS
Ordering: sb_regnotice_2027-04-11 precedes sb_custnotice_2027-04-15
Basis:    after-event binds prior-event hash; prior event sealed
          in root of 2027-04-11 (signed, published); after event
          sealed in root of 2027-04-15 (signed, published);
          cross-day seal ordering confirmed
Regulator notice: chain_kind=operational; interagency 36h notice;
          satisfies 7 TAC §3.24 (tx-dob profile)
Elapsed:  1.1s
```

Danny looked at it for a while.

**Danny:** "So the customer notice can't have been created before the regulator notice, because it references the regulator notice's hash, and you can't reference the hash of a thing that doesn't exist yet. And the regulator notice is sealed into the eleventh's root, signed and published on the eleventh — four days before the fifteenth's root that carries the customer notice. To fake regulator-first, the bank would've had to know the regulator notice's hash before creating it, which is asking a hash function to run backward."

**Chen:** "That's all of it. The bank can lie about *when*. It can't lie about *order*, because the later event is built out of the earlier one's hash and the two seals landed in separate published roots on separate days."

Danny set his pen down, and Raj — who had learned to read the man over a single morning — understood that the pen going down was the sentence.

**Danny:** "Here's what I'll write, and here's what I won't. I won't write that the chain proves the bank determined the incident was reportable at 4:20 on the tenth. It doesn't. That determination time is the bank's assertion; the chain proves the bank *recorded* it and didn't alter the record, but the wall-clock moment a team's judgment crystallized is a human fact and no cryptography reaches it. I'd be overclaiming, and a defense lawyer would take the report apart for it. — But the ordering, regulator before customer, I will write as proven. That's not an assertion, that's arithmetic, and it's the exact relationship 7 TAC §3.24 turns on. I don't have to take the bank's word for it, and neither will the next examiner, and neither will a court."

Elena, who logged the team's read of every regulatory beat, wrote it down and underlined the distinction, because it was the cleanest statement of the chain's boundary she'd heard an examiner make.

> ### Confirmation #3 — The 7 TAC §3.24 regulator-before-customer ordering is cryptographically provable; the incident-determination time stays an institution assertion
>
> Texas rule 7 TAC §3.24 requires a state bank to notify the Banking Commissioner of a reportable cybersecurity incident before notifying customers, within fifteen days of determining the incident is reportable. The bank's regulator notice (April 11, interagency 36-hour notice satisfying the state clock) and its customer notice (April 15) were both chained; the customer-notice event bound the hash of the regulator-notice event, which had been sealed into a signed, published daily root four days earlier — so the ordering cannot be reconstructed or reversed after the fact. The examiner drew the boundary himself: the incident-determination *time* is an institution assertion (integrity-bound, not truth-proven), while the notification *ordering* is genuinely proven by the chain. The rule turns on the ordering, and the ordering is what the chain establishes.

## 3:00 PM — Whose exam is in the chain, and Dawn joins

Dawn joined at three, in person, walking in from the Austin traffic in a way none of the team had ever seen her arrive at an engagement — not driving, not leading, carrying a single folder, a visitor's badge with a different escort code than the team's. She was MMPWorks now, the vendor's TesseraSeal liaison, and the room re-arranged itself around that fact as rooms do.

**Dawn:** "Raj. — I'm here on the spousal-disclosure paragraph, as liaison, for the composition questions only. Tom has my window logged. I sat in the chair you're in for twenty engagements; I know how much of this room isn't mine anymore, and I'm going to stay on my side of that line. — What do you need from the vendor side?"

**Raj:** "Diana's about to walk the examiner the scope boundary — what the chain covers and what it can't. If the vendor has a clean statement of the boundary, this is the moment."

Diana took it, because the boundary was an access-and-identity question and that was her lane.

**Diana:** "Examiner Tran. One thing before you close the IT booklet, because it's the thing that separates understanding this tool from being sold it. The chain covers the bank's evidence. It does not cover your work. Your workpapers, your access to these files this week, the report you'll write — those are the Department's confidential supervisory information, custodied on your side, wiped off your laptops at exam close as they always are. They're not in this chain and they shouldn't be. If anyone told you the chain covers the examination itself, they'd be selling you something."

**Danny:** "Good. Wrong answer and I'd have written the bank up for over-claiming."

**Dawn:** "There's one thing on the seam, and it's the vendor's to state so the bank doesn't over-promise it. Your *access* to the bank's evidence — which examiner pulled which confidential file, when, through the portal — that can be chain-bound on the bank's side, if the Department ever wants it. Not your workpapers. Just the fact of the access, against the bank's files. The specification has an access-trail primitive for it; it's the same mechanism the bank uses to record who inside the bank reads a privileged file. It means a year from now, if someone asks who saw a confidential customer record during this exam, there's an integrity-bound answer on the bank's side, independent of the bank's own say-so. — The vendor's position is that it's the Department's call whether to use it, and never the bank's."

**Karen:** "We'd use it. Confidentiality is a hard constraint for us, not a courtesy. As long as it's the fact of access on the bank's side and never our judgment or our workpapers, which stay ours."

Danny had one more, and it was the one that tied the day back to the line the verifier had printed on every verdict since morning.

**Danny:** "The verifier printed a supervisory context on every run. Charter type, state supervisor, federal supervisor, dual-supervision posture. Where's that from, and did the profile flag change what the verifier *decided*, or only what it printed?"

**Dawn:** "Two questions, and the second is the one that matters, so let me be careful with it. The supervisory context is a small attribute family the record carries — that this artifact was produced under a Texas state charter, dual-supervised, FDIC as federal prudential supervisor. Same boundary as the incident determination: the chain proves the bank *recorded* that context and didn't alter it, not that it's metaphysically true. It means a record doesn't lose its supervisory context when it travels. — The profile flag, `tx-dob`, changes the vocabulary and the framing. Which markers the report surfaces, that it prints the 7 TAC §3.24 reference on the incident notice, that it names the charter authority. It does not change a single accept-or-reject decision, and it cannot move a verdict or an exit code. If it could, the same chain would verify differently for a Texas examiner than for a federal one, and the guarantee that two verifiers walking the same chain reach the same verdict would be dead. Run the same chain under the federal profile and the Texas profile — same PASS, same exit code, different words. There's a test that asserts exactly that, and you can run it."

**Danny:** "Run it. Because if the profile could move the verdict, then 'the Texas exam counts the same as the federal exam' would be a lie at the tooling level, and the whole reason a state-only cycle carries federal weight is that it's the same underlying check."

Kyle ran it — the same chain under `--profile ffiec` and `--profile tx-dob`. Identical verdict. Identical exit code. Only the framing differed: the Texas run named the charter authority and the state incident rule; the federal run didn't.

*That's the accreditation argument, in code*, Dawn thought, watching two identical verdicts come up on a screen in a room she no longer ran. *The Department is accredited so a federal regulator accepts its exam in lieu of doing its own. Accreditation certifies the examiner. This certifies the evidence is the same evidence under either flag. Two layers, same claim: a state exam and a federal exam should reach the same answer. First time I've watched a machine agree with the principle — and I'm watching it from the vendor's chair, which is the strangest part.*

> ### Confirmation #4 — The verifier's Texas profile changes framing only, not the verdict; the scope boundary holds between bank evidence and examiner work product
>
> The verifier's Texas profile surfaces the charter authority, the dual-supervision posture, and the 7 TAC §3.24 reference, while the underlying integrity verdict and exit code are identical to the federal profile on the same chain — the determinism guarantee that lets a state-only cycle carry the same weight as a joint federal exam. The scope boundary held cleanly under the examiner's questioning: the chain covers institution-side evidence, not examiner workpapers or the Report of Examination, and the fact of examiner access to confidential files can be access-trail-bound on the bank's side without ever reaching the examiner's work product — the Department's call to use, never the bank's. The team walked the boundary; the vendor stated the seam; the examiner set the limit.

## 4:30 PM — Raj closes the first day

Raj gathered the team in the technical room after the Department went back across the hall, and did the thing he had watched Dawn do at the end of twenty first days, which was to make sure nobody had fallen for their own client.

**Raj:** "Before anybody tells me this is the best-run bank we've seen. Findings. Real ones. What's the Department writing that we'd have written."

**Tom:** "One real IT finding, and it's the Department's, not ours — the key-registry retention floor, three years against five-year BSA records, remediated at lunch, going to the board. I've got the records-retention corroboration in the file with the Brazos floors cited. It's a matter for board attention, not an order."

**Diana:** "Access and identity are clean. The scope boundary held under the examiner's own questioning, which is the strongest way it can hold."

**Elena:** "The incident-notice ordering proved. The examiner drew the line on the determination time himself, which means he understands the tool and won't over-claim it in the report. That's better for the bank than a finding-free walk."

**Chen:** "Ledger and seal reconcile across the whole window. The profile determinism ran clean under his own hand."

**Raj:** "So we've got a sound bank with one remediated finding going to the board, two substandard credits the bank already reserved for, and a first-time examiner who talked himself into trusting the evidence by re-running it. — Here's the thing I want said out loud, because it's the trap. We are not here to make the Department like the chain. We're here so the Department can check it. Danny didn't believe a word this morning and he shouldn't have, and the reason he believes it now is that he broke it himself and it caught him and he fixed it and it caught him again. If he'd taken it on anybody's word — the bank's, Rachel's, ours — it'd be worth nothing, and it'd deserve to be. The chain earned its place in that room by surviving the one person who walked in wanting it to fail. Write it that way in the memo. Not the enthusiasm. The mechanism."

Cindy had come in for the tail of it.

**Cindy:** "That's the memo I retained you for. — Karen's exit meeting is Thursday morning, then the board. The Report of Examination comes from the Department in the usual weeks; it's confidential supervisory information, we hold it, we don't publish it. Composite is going to be a two, from what she's signaling — a sound bank, one finding, no order, no memorandum of understanding. — I sat in that chair nine years. I never once watched an examiner change his mind about evidence in a single day. I watched it today."

## Day 2 and Day 3

The reconciliation slate ran on Day 2: ten loan files traced from the origination system through the chain to the seal, ten board-and-committee minutes hashed against their year-old seals, the GL extract walked from its parent-job entry to the count of balances it produced, so a curated extract would have surfaced as a count mismatch. Every artifact the bank had staged through the portal hashed to the value sealed when it was produced. Ray Hernandez finished his loan classifications — the two substandard credits and nothing doubtful — and told Raj, unprompted, that it was the first exam where he'd been able to prove the appraisal driving a classification was the appraisal the bank held eight months ago and not one swapped in the week the examiners arrived. Diana's access-trail walk confirmed authenticated identity across every review and approval in the slate; no shared-login masquerade anywhere.

Danny spent most of Day 2 in the Department's room and came across the hall twice — once to re-run a seal on a date he picked himself without telling anyone which, and once, late, to ask Sonya a question about module partition ceremonies that had nothing to do with the exam and everything to do with a man who had decided to actually understand the thing. Sonya answered it for forty minutes past when she needed to.

The exit meeting was the Department's and the team was not in it, by the arrangement Karen had set on the first morning. What came back through Cindy was a composite of two, a URSIT of two with the one remediated retention finding sitting under Support and Delivery, the two substandard credits adequately reserved, no memorandum of understanding, no Commissioner's order. The Report of Examination would come from the Department in the usual weeks, stamped confidential supervisory information, the bank's to hold and not to publish. On Thursday afternoon, after the board meeting the team also wasn't in, Danny Tran crossed the hall one last time to collect a laptop bag he'd left, and stopped in the doorway of the technical room where Raj and Sonya were closing out the engagement file.

**Danny:** "You're the outside firm. You had nothing to sell me. So I'll say the thing to you I'm not going to write in a report. — For fifteen years the last line of every evidence conclusion I've written has been some version of *as represented by management.* Every loan file, every incident timeline, every extract. I reconcile what I can tie out, I trust the rest, and I sign it *as represented,* because that's all the honesty the job entitles me to. Today's the first day I got to cross that line out on a few of them and write *verified* instead. Not all of them — the determination time is still the bank's assertion, the classifications are still my judgment. But the provenance, the completeness, the ordering — those I checked myself, with my own hands, and I don't have to trust anybody. That's new. In fifteen years, that's new."

**Raj:** "That's the idea. Nobody was ever supposed to make you trust them. You were just never handed the tools not to."

Danny picked up his bag. He looked at Sonya.

**Danny:** "The custody piece. You handed me the one thing I could check without believing anyone, and then you let me go check it. Most people in your position argue. You handed me a thread and stepped back."

**Sonya:** "I spent twenty-two years proving where hardware had been to people who didn't want to take my word for it. You never win those by arguing. You win them by handing over the thing they can check and getting out of the way."

He nodded, and left, and that was the last the team saw of the first Texas Department of Banking examiner any of them had met.

## Chain confirmations — the Texas exam requirement set met in the examiner's own hands

This engagement exercised no purpose-built spec-section family. It confirmed that the chain's foundational capabilities answer the questions a Texas exam actually asks — provenance, completeness, ordering, and the identity of the signer — and it did so in a way the firm had never done before: with a live examiner in the room, checking the evidence under his own hand rather than through a memo the team wrote for a regulator three weeks out. The through-line of two prior Texas engagements — the Department examiner as an off-page fact that "closed it in one meeting" — became, for one week, a person with a real objection who talked himself out of it by re-running the math.

### The self-signed-evidence answer — module custody and the key registry

**What Success Bank operates.** Per-event keyed hash over each artifact; hash-linked entries; a daily seal signed by a non-extractable HSM key; the seal fingerprint published outside the ledger account; a separately-custodied, HSM-signed key-registry manifest under three-role separation of duties, published with its own signature.

**What the examiner verified.** That "the bank signs its own evidence" is answered by tamper-evidence, not attestation — a false PASS takes simultaneous compromise of three independent custody layers. He validated the manifest against a separately-published root with his own tooling, confirmed a seal's fingerprint by hand, re-ran the verifier for agreement, and produced FAIL at the byte on a deliberate corruption. The team handed him the thread; he pulled it himself.

### The provenance-and-completeness answer — artifact and job binding

**What Success Bank operates.** Every exam artifact bound by hash at production time under the shared `audit.exam_artifact.artifact_kind` vocabulary; GL-extract and loan-download jobs chained as parent runs whose child rows reference the job and whose entry names the count produced.

**What the examiner verified.** That reconciliation and the chain answer different questions and a good exam uses both — reconciliation proves internal consistency, the chain proves provenance and completeness. The appraisal driving a substandard classification hashed to a seal eight months old; a curated GL extract would have surfaced as a count mismatch.

### The ordering answer — 7 TAC §3.24

**What Success Bank operates.** Incident-response events chained; the customer-notification event binds the hash of the regulator-notification event, sealed into an earlier signed, published daily root.

**What the examiner verified.** That the regulator-before-customer ordering the Texas rule turns on is cryptographically provable — the later event is built from the earlier event's hash, the seals landed in separate published roots on separate days, and the order cannot be reversed after the fact. The determination *time* stays an institution assertion; the *ordering* does not.

### The retention-floor finding — key registry vs. the five-year BSA floor

**What Success Bank operates.** An HSM key registry whose retention had been set to three years, matched to the Call Report window.

**What the examiner verified.** That the key-registry retention floor must outlive the longest-lived chained artifact, and the bank's longest is a five-year BSA record — so a three-year floor would render the oldest, most-subpoena-prone BSA evidence unverifiable in year four. Remediated on-site; corroborated from the team's Brazos retention floors; a matter for board attention, not an order.

### The determinism answer — the tx-dob profile

**What Success Bank operates.** A verifier profile (`tx-dob`) that surfaces the charter authority, the dual-supervision posture, and the 7 TAC §3.24 reference, and an `audit.supervisory.*` attribute family that binds the supervisory context into the record.

**What the examiner verified.** That the profile changes only reporting vocabulary and framing, never a verdict or an exit code — the same chain under `--profile ffiec` and `--profile tx-dob` produced identical PASS and identical exit code. The tooling enforces the identity that lets a state-only cycle carry the same weight as a joint federal exam, just as CSBS accreditation certifies the examiner.

## Engagement debrief — Raj's voice

> "It never is. But Success Bank is the one I'll tell the next new person about on their first drive-in, because it's the engagement where the examiner stopped being a citation and became a man in a doorway. Two Texas banks we prepped for the Texas Department of Banking examiner — Mission Plaza, Brazos — and both times the examiner was a sentence in the workpaper. *The Department examiner closed that line in one meeting at the March cycle.* We wrote memos for a person we never met. This week the person had a name, and a real objection, and I got to watch him talk himself out of it instead of watching a memo do it for him.
>
> "The whole thing turned on Danny Tran calling the chain a fancy pen in the first hour, which was the correct thing to call it, and which is why Cindy put us in the room. A self-signed record is worth nothing if you can't confirm the signer without asking the signer. So Sonya handed him the one piece he could check without believing anyone in the building — the published key registry — and stepped back, and he pulled it. Validated the manifest against a published root with his own script. Confirmed a seal's fingerprint by hand. Only then ran the verifier, so it couldn't tell him anything he hadn't already proved. Then broke it on purpose and watched it catch him at the byte. He didn't trust us and he didn't trust the bank. He trusted the arithmetic, because he did the arithmetic. That's the only kind of trust worth anything, and the only kind the chain was ever built to earn.
>
> "The finding is real and I want it read as real. Their key-registry floor was three years against five-year BSA records — the oldest evidence they'd most need to authenticate would have gone dark in year four. Tom had the number cold from Brazos and corroborated it inside a minute; Rachel fixed it before Danny finished the sentence. A bank faking the control argues the finding. A bank that means it fixes it at lunch. That told the Department as much as the cryptography did.
>
> "Here's the trap I made everyone say out loud, because it's the one you fall into when you're in the room with a client you like: our job in that room was never the Department's belief. It was the Department's ability to check. The distance between those two is the job. The chain doesn't ask to be believed; it asks to be re-run. Danny re-ran it, and the machine agreed with itself under his hand, and now there's an examiner in the Department who's met one — which means the next Texas bank that stands one up walks into a Department that has seen it work.
>
> "The chain proves the file wasn't changed and the order things happened in. It does not prove the bank was right. Danny held that line himself, in his own report, which is more than we could have done for him. Hold that line and the tool is worth more than any bank's word — and worth exactly as much as the examiner's willingness to check it, which this week was a great deal."

## Cross-references

- **Spec impact**: §1.1 (compositional security — the three-layer simultaneous-compromise model behind the self-signed-evidence answer), §1.2 (epistemic scope — integrity and ordering proven, human determinations institution-asserted), §7 (verifier recreates the original record byte-equal or proves alteration; exit-code contract exercised at exit 2 on the deliberate corruption), §10.1 (key-fingerprint reconciliation, done by hand by the examiner before the verifier ran), §10.5 (separation-of-duties HSM custody — the three-role model Sonya walked), §10.9 (IKM/key-registry retention floor — the finding), §10.11.1 (ECOA adverse-action lineage on the credit-decisioning surface), §10.13 (evidentiary-artifact composition — carried forward from the Mission Plaza and Brazos memos the bank built against), §10.19 (chain-coverage map / CC8.1 declaration), §10.21 (cross-vendor model handover — the single question routed to Steve under the recusal protocol), §10.70 (access-trail primitive — examiner-access provenance on the bank side), §10.76 (HSM-signed IKM registry manifest — the independently-validatable trust anchor), §10.84 (approval/ordering primitive — the after-event binds the prior-event hash), §14.13 (`audit.supervisory.*` family — charter authority and dual-supervision context), the `audit.exam_artifact.artifact_kind` shared vocabulary, and the presentation-only `tx-dob` verifier profile.
- **Regulatory citations**: 7 TAC §3.24 (Texas cybersecurity-incident notification — Commissioner before customers, within fifteen days; interagency 36-hour notice satisfies it); Texas Finance Code Title 3 (state-charter examination authority; Austin as the Commissioner's seat); the FFIEC IT Examination Handbook and FDIC InTREx program (the IT-exam scaffolding); URSIT (Audit / Management / Development & Acquisition / Support & Delivery, feeding CAMELS Management and Sensitivity); CAMELS (the safety-and-soundness composite — a two here); CSBS accreditation (why the alternate-year state exam carries federal weight); Call Report retention (three years) and BSA-record retention (five years) as the floors behind the key-registry finding.
- **Documented finding**: key-registry retention floor set below the longest-lived chained artifact (three years against five-year BSA records). Remediated on-site; recorded as a matter requiring board attention, cross-referenced across the IT and BSA booklets, not a Commissioner's order.
- **Continuity**: Raj is Lead Auditor (the chair passed after Story 20 Mission Plaza, Dawn's last as Lead); the traveling eight are Raj, Elena, Mike, Diana, Luis, Chen, Tom, Sonya; Dawn appears as MMPWorks TesseraSeal liaison under the spousal-disclosure paragraph, and Steve by video for a single §10.21 question — the vendor-recusal format established at Story 20 and Story 21. The Texas Department of Banking, referenced off-page and unnamed at Story 20 (Mission Plaza) and Story 21 (Brazos) as the examiner who "closed it in one meeting at the March cycle," appears on-page and named for the first time here — Karen Wilson (EIC) and Danny Tran (IT). Austin is the team's return to the city of Story 12 (Hill Country FCU) and of MMPWorks itself. The retention-floor finding pays off the Texas seven-year and FFIEC five-year floors Tom carried out of Story 21 (Brazos).
- **Auditor stories**: the corpus's first engagement in which the team is on-site while a live regulator works the chain, an escalation from Story 22 Wasatch (where the team cleared out as the examiners arrived). It shares the Texas state-charter register with Story 20 Mission Plaza and Story 21 Brazos, and the FFIEC IT-Handbook foundation with the banking engagements (Story 01 Northbridge, Story 04 Atrio, Story 12 Hill Country). The through-line is the shift from trust-by-attestation to trust-by-reproduction — witnessed, this once, in the examiner's own hands rather than argued in a readiness memo.

The spec-section confirmation memo and the engagement debrief are filed under Success Bank's compliance-track records; the Report of Examination and its workpapers remain the Department's confidential supervisory information, held by the bank and not published, with the corrected key-registry floor now exceeding the longest BSA window.
