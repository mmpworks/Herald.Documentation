# 12 — Hill Country Federal Credit Union

*Diary of an Audit*

**Engagement:** Three-day pre-engagement readiness pass before the NCUA AIRES examination opens in three weeks
**Client:** Hill Country Federal Credit Union — ~$8B federally-insured multi-state FCU, Texas plus neighboring states, NCUA-supervised, headquartered in Austin
**Status:** TesseraSeal in production for eleven months across the full member-experience surface; AWS-resident; Herald.Enterprise.Aws runs the chain on `us-east-1` with replicas in `us-east-2`. §10.21 (cross-vendor model-handover) shipped in a Herald release seven months ago — exactly when the FCU began the marketing-AI vendor handover.
**Audit team lead:** Dawn
**Client liaison:** David Reyes, Chief Audit Executive, Hill Country Federal Credit Union

**Posture going in:** confirmation. The institution has been on the chain for eleven months across every member-facing surface — share-draft accounts, online and mobile banking, the contact center, the loan-decisioning workflow, the marketing-CRM mirror, and the new in-house ML scoring layer that replaced the legacy banking-CRM during the vendor handover six months ago. NCUA AIRES is three weeks out. The CAE has been carrying a quiet question about the vendor-handover boundary for six months. The audit team's job is to confirm that the §10.21 cross-vendor model-handover surface operated cleanly across the transition, that the §10.69 per-customer audit-trail subset disclosure spans the handover boundary, and that the ECOA / Reg B linkage between marketing-AI events under the legacy vendor's scoring and credit decisions under the new vendor's scoring is examinable by NCUA AIRES workpaper conventions.

> **Reading note for this story.** Hill Country is the canonical institutional reference for the §10.21 cross-vendor model-handover surface in its single-substrate AWS-only form. The audit team's engagement-file note about substrate-portability — *"works on one substrate. What happens when the substrate moves?"* — is filed quietly at the end of the reconciliation test and carries no public weight at the time. The single-substrate frame is deliberate. Hill Country is the foundation; the substrate-portability question is the seed.

---

## Context

Hill Country Federal Credit Union runs out of a four-story glass building on the north side of Austin, off MoPac, with a parking lot full of pickups and a quiet hum of fluorescent light through the front lobby. The credit union was chartered in 1957 to serve federal employees stationed at what is now Bergstrom; it has grown over seven decades into a multi-state FCU with branches across Texas, Oklahoma, New Mexico, Arkansas, and Louisiana, and a sizable presence in adjacent communities served by mobile and online channels. Eight billion in assets. Roughly six hundred thousand members. NCUA-supervised under the federal credit-union charter.

The CAE is David Reyes — forty-eight, a former NCUA examiner himself, fifteen years out from the agency side and seven years into the chief audit executive seat at Hill Country. He has run two AIRES exams from the CAE side and several more from the examiner side. He is calm. He has been calm for six months in a row, which is a feat, because the marketing-AI vendor handover went live in November and the AIRES exam was on the calendar before the handover began.

Eleven months ago Hill Country went live on TesseraSeal across the full member-experience surface. Every member-facing event lands as a sealed chain entry: account opens, share-draft transactions, loan applications, contact-center calls and the transcription pipeline behind them, online-banking sessions, mobile-app sessions, the wealth-advisor pilot that runs out of a small branch in San Antonio, the loan-decisioning workflow, the marketing-CRM mirror. AWS-resident, Herald.Enterprise.Aws on `us-east-1` with daily Merkle seals signed by AWS CloudHSM in the same region, replicas in `us-east-2` for resilience. Production tenant `bcfcu-prod`, plus a small handful of subordinate tenants for the wealth-advisor pilot and the credit-union service organization that handles back-office processing.

Six months in, Hill Country began the marketing-AI vendor handover. The legacy banking-CRM was Total Expert — a vendor Hill Country had been on for a decade, with eleven months of TesseraSeal coverage by the time the handover started. The new stack was HubSpot Marketing Hub for the campaign-management surface, plus an in-house ML scoring layer the FCU's data team had been building in parallel. The CMO had champion'd the move. The CCO had her own questions about the marketing-to-credit-decision linkage under ECOA. The CAE had been the one carrying the institutional question: *can we prove what changed across the handover, and what didn't?*

Twenty-three weeks ago, on a Tuesday in November, the handover went live. The legacy Total Expert export — a 1.4-TB tar.gz of campaign history, member lists, A/B variant data, scoring artifacts, model cards, lineage metadata — was hash-anchored at the handover moment. The hash was sealed into the new HubSpot + in-house ML chain in the same daily Merkle seal that covered the first new-vendor chain entries. Dual signatures: Total Expert's CTO on the from-vendor side, Hill Country's CTO on the to-institution side, both bound into the seal per §10.17's partition-ceremony attestation pattern. The §10.21 schema family handled the rest.

Seven months ago — which is to say one month before the handover — a Herald release shipped §10.21 in the spec. The clause normates the cross-vendor model-handover surface end-to-end. The §10.40 single-substrate chain-merge anchor cross-references it. The §10.21 attribute family — `audit.model_handover.provider`, `audit.model_handover.model_id`, `audit.model_handover.model_artifact_sha256`, `audit.model_handover.model_card_sha256`, `audit.model_handover.provider_chain_entry_id`, plus the dual-signature pair — was on the wire when Hill Country's handover went live. The spec did its job invisibly until the moment it was needed, and even then the work read as routine.

The AIRES exam opens in three weeks. NCUA's lead supervisor will land on Wednesday morning of the exam-opening week with two technical examiners and a CFPB consumer-protection examiner cross-credentialed for the §1033 personal financial data rights cross-cut. David Reyes wants the spec-section confirmation memo on the lead supervisor's desk before the entrance meeting. He has set aside three days for the audit team to walk it.

The team has not been at Hill Country before. They have walked credit-union-adjacent institutions, but never a credit union under NCUA. Hill Country is the first NCUA-supervised institution on the team's roster.

---

## Audit Team

| Name | Role |
|---|---|
| Dawn | Lead Auditor — governance and narrative |
| Raj | Database specialist |
| Elena | CRM systems |
| Mike | Application / API layer |
| Diana | IAM and access control |
| Luis | DevOps / logs / pipelines |
| Chen | Data engineering / ETL |
| Tom | Internal-audit liaison specialist (visiting team; partners with the client CAE) |

The team flew into Austin on Monday evening. Dawn and Tom drove out from the hotel together on Tuesday morning. The rest of the team came in separately. The engagement room was on the second floor of the operations building, two doors down from the CAE's office, with a long table and a wall of windows looking out at the Texas hill country.

---

## 🌅 8:30 AM — Kickoff (Tuesday)

The team rolled in to the Hill Country engagement room with coffee from the lobby and the look of people who had been in three different time zones in the last six weeks. Tom set his bag down by the door. Dawn took the seat at the long side of the table where she could see the screen and the windows at once. The others filed in behind her — Raj, Elena, Mike, Diana, Luis, Chen — and arranged themselves the way they always did.

The projector was already on. A clean architecture diagram, every box labeled, every arrow ending at something called *Herald Enterprise ledger on AWS us-east-1.* Above the diagram, in modest type: **TesseraSeal — chain-of-custody for Hill Country member-experience surface.**

David Reyes walked in carrying a thin folder under one arm and a paper cup of coffee in the other hand. Mid-forties. Pressed shirt, no tie. He looked rested.

"Dawn. Tom. Welcome to Hill Country."

Dawn extended a hand. "David. We've heard your name from the working-group circuit."

"You have. I'll take that as either a compliment or a warning, depending."

Tom said, "Compliment. The credit-union side has been thinly represented at the spec readings, and your CC8.1 control description is one of the ones that gets passed around."

David Reyes smiled, just a little. "It's the third revision. The first two were embarrassing."

He sat down. He did not pull out a deck-of-decks. He set the folder on the table, opened it to the first page, and rotated it so Dawn could read.

"Here is the engagement frame, since I imagine you want to start from your own footing and not from my pitch. Three days. AIRES exam opens in three weeks. The institution is on TesseraSeal across the full member surface — eleven months of production, AWS-resident, Herald.Enterprise.Aws on `us-east-1` with replicas in `us-east-2`. Six months ago we started the marketing-AI vendor handover. Legacy Total Expert out. HubSpot Marketing Hub plus an in-house ML scoring layer in. The cross-vendor anchor was placed at handover initiation. The §10.21 surface has been operating for twenty-three weeks. I want you to confirm it operated cleanly. I want you to walk the §10.69 per-customer disclosure across the vendor-boundary span. I want the auto-loan adverse-action case that crossed the handover to be the load-bearing reconciliation example, because that's the ECOA question I'd ask if I were the NCUA examiner. And I want the spec-section confirmation memo on the lead supervisor's desk before the entrance meeting."

Dawn wrote on her notepad: **§10.21 production 23 weeks. §10.69 spans the boundary. ECOA auto-loan = load-bearing.**

She underlined *load-bearing.*

"That is exactly the shape we'd ask for," she said. "I want to confirm something first. You said the cross-vendor anchor was placed at handover initiation. The §10.21 attribute family — `audit.model_handover.provider`, the artifact hash, the model-card hash, the provider-chain-entry-ID, the dual signatures per §10.17 — that was wired up at cutover, not retrofitted."

"Wired up at cutover. The Herald release that shipped §10.21 dropped in April. The cutover was in November. The institution was live on the spec section the day it went into production. We did not retrofit."

Tom wrote: *§10.21 in production at cutover; not a retrofit.*

David Reyes paused. "I'll add one thing while we're on framing. The §10.21 shipping date — seven months before the handover — is matter-of-fact. I am not going to tell you the working group anticipated this perfectly. The clause was on the spec calendar. The clause shipped when it shipped. We had the surface available because the spec had reached that section by the time the institution needed it. I want that on the record because I'd rather not have anyone read this as a rescue story."

Dawn looked at him.

"Good," she said. "Because I won't write it as one."

He nodded.

Mike asked the next thing. "Walk me through the §1.2 epistemic scope. If a member's loan denial ends up in front of the CFPB's enforcement division, what does the institution's witness lay foundation on?"

David Reyes did not pause.

"§1.2 says the chain proves what the system recorded at a given time and that the record was not tampered after capture. The chain does NOT prove the model's underwriting judgment was right. Does NOT prove the model complied with ECOA's adverse-action policy. Does NOT prove the model was free of disparate-impact effects. Those are policy questions and substantive-fair-lending questions, both of which the chain can support with data but cannot answer on its own. The §1.1 Daubert grounding is in the spec — testability via §7 procedure, peer review under the working-group process, known error rate per §1.3 security definitions, general acceptance of HMAC-SHA-256, RFC 6962 Merkle, and Ed25519. The §1.4 compositional security argument names the three custody layers — IKM, ledger storage, HSM — plus the §1.2 SDK-process residual. A false negative requires simultaneous compromise of all three, plus the residual. We name the line clearly so our witness stays on the integrity foundation under cross-examination."

Same answer, almost word for word, as Marcus's at Northbridge eleven months ago. Different building. Different supervisor. Same spec.

Dawn wrote: *§1.1 / §1.2 / §1.3 / §1.4 — Daubert framing in the spec text, not vendor marketing. CAE recites it without hesitation.*

She underlined *recites it without hesitation.*

David Reyes added one more thing. "The CFPB cross-cut is real for us. §1033 personal financial data rights went into final-rule territory last year. Every member-disclosure packet a borrower or member requests must remain producible across the vendor handover. The handover doesn't cut the disclosure obligation. The chain has to bind the legacy-vendor era's member data to the new-vendor era's member data through the cross-vendor anchor. §10.69 is the section that does it. We'll walk it on Day 2."

Tom wrote: *§1033 disclosure spans the handover. §10.69 is the producing section.*

Dawn looked around the table. Her team was settled. The morning had a clean shape.

"Three days," she said. "Tuesday morning is the §10.21 cross-vendor model-handover walk. Tuesday afternoon is the ECOA reconciliation — the auto-loan case. Wednesday morning is §10.69 per-customer disclosure across the boundary. Wednesday afternoon is AIRES workpaper composition. Thursday morning is the spec-section confirmation memo, the MRM-committee memo, and the close-out. David, do you have a specific reader-list for the memo?"

He named them. "NCUA AIRES lead supervisor. The CFPB consumer-protection examiner who's cross-credentialed for the §1033 work. My board's risk committee — they read the memo verbatim, not a summary. The CMO and the CCO each get a copy. The MRM committee chair gets the MRM memo separately."

"Verbatim to the board?"

"Verbatim. I do not edit your work."

Tom nodded, almost imperceptibly. *Six in twelve months,* he thought. *That makes six CAEs in the last twelve months who said verbatim.* He filed it.

Dawn looked at the screen. The architecture diagram had two boxes that mattered most for the morning: a faded box on the left labeled *Total Expert (legacy, retired Nov 2025)*, and a brighter box on the right labeled *HubSpot Marketing Hub + in-house ML scoring (active).* A single arrow between them, labeled *§10.21 cross-vendor anchor.* Underneath: *handover sealed 2025-11-04.*

"Let's go."

David Reyes stood up. "Cal Beaumont is the SRE on-call this morning. He'll be in the room for the operational walk. Karina Holloway, our CMO, is upstairs and will join when we touch the marketing-AI side. Anwar Patel, our CCO and ECOA counsel, will be down at one PM for the auto-loan reconciliation. Mei-Lin Tsai, the MRM committee chair, will be in for the model-card review on Wednesday morning. Verifier credentials are already provisioned for your laptops — read-only, scoped to the TesseraSeal surface, same shape as Northbridge."

Dawn blinked. "You provisioned us before we asked."

"It's a credit-union habit. The verifier's design doesn't need our credentials at all — the Ed25519 public-key fingerprints for both the legacy-era seals and the current seals are published on the institution's compliance page. You can pull a seal from us-east-1 and verify it on coffee-shop wifi. The provisioned credentials are just to save you the typing."

Dawn wrote: *Verifier unprivileged. Public keys published. Read-scope creds are convenience.*

Underneath: *Same posture as Northbridge.*

She looked at the architecture diagram one more time. The cross-vendor anchor was a single arrow. The whole engagement was going to live or die on that one arrow.

"Cal, when you're ready. Let's start with the cross-vendor anchor."

---

## 🧩 9:15 AM — The §10.21 Cross-Vendor Anchor

Cal Beaumont sat down at the second screen and opened a terminal. He was thirty-something, wearing a fleece pullover with a Hill Country logo over the heart and a pair of jeans that had clearly seen the inside of more than one server room. He nodded at the team and started typing without much ceremony.

"You want the handover entry first?"

"Start there," Dawn said.

He pulled it up. A single JSON entry filled the screen. The team leaned in.

```jsonc
{
  "ffiec.chain.spec": "v1.0",
  "ffiec.chain.format_version": "v1",
  "ffiec.chain.chain_kind": "audit",
  "ffiec.chain.run_id": "marketing-ai-handover-2025-11",
  "ffiec.chain.tenant_id": "bcfcu-prod",
  "ffiec.chain.captured_at": "2025-11-04T14:00:00.000000000Z",
  "ffiec.chain.seq": 1,
  "ffiec.chain.payload_hash": "8c3a4e1f9b2d6c5a7e0b4d8f1c3a6e9b...",
  "ffiec.chain.prev_hash":    "0000000000000000000000000000000000000000000000000000000000000000",
  "ffiec.chain.key_version": 3,
  "ffiec.chain.key_fingerprint": "c1a5d8f3b9e2c7a4d6f0b3e9c2a5d8f3",
  "ffiec.chain.mac_computed_at_utc": "2025-11-04T14:00:01.482Z",
  "ffiec.chain.kms_handle_uri": "aws-cloudhsm:cluster/cluster-bc-prod/key/k-bcfcu-prod-2025q4",
  "ffiec.chain.canonical_encoding": "rfc8785-jcs",
  "ffiec.chain.region": "us-east-1",
  "service.name": "bcfcu-marketing-handover",
  "service.version": "1.0.0",
  "event": "model_handover.initiated",

  "audit.model_handover.provider": "total-expert-legacy",
  "audit.model_handover.receiver": "bcfcu-inhouse-ml",
  "audit.model_handover.model_id": "marketing-scoring-v2",
  "audit.model_handover.model_version_legacy": "te-v8.4.2",
  "audit.model_handover.model_version_new": "bcfcu-ml-v1.0.0",
  "audit.model_handover.legacy_export_artifact_sha256": "f04e8b27c9a1d3b6e8f2c5a9d7b0e3c6a8d1f4b7e9c2a5d8f3b6e9c2a5d8f3b6",
  "audit.model_handover.legacy_export_artifact_size_bytes": 1488726847219,
  "audit.model_handover.legacy_model_card_sha256": "a7d1f5b9c4e8d2a6b0f3e7d1a4b8c2e5f9c4e8d2a6b0f3e7d1a4b8c2e5f9c4e8",
  "audit.model_handover.new_model_card_sha256": "b8e2c6a0d4f8b2e6c0a4d8b2e6c0a4d8b2e6c0a4d8b2e6c0a4d8b2e6c0a4d8b2",
  "audit.model_handover.legacy_lineage_manifest_sha256": "9b3c7e1a4f8d62b0c5a1e9f4d2b8c0e3a7d1f5b9c4e8d2a6b0f3e7d1a4b8c2e5",
  "audit.model_handover.provider_chain_entry_id": "te-legacy-handover-final-2025-11-04",
  "audit.model_handover.evidentiary_role": "vendor_handover_anchor",

  "audit.model_handover.dual_signatures": {
    "from_party": "total-expert-legacy",
    "from_signer": "te-cto-signer-fingerprint-3b9d2c8a",
    "from_signature": "MEUCIQD7...base64-encoded-Ed25519...",
    "to_party": "bcfcu-inhouse-ml",
    "to_signer": "bcfcu-cto-signer-fingerprint-8f1e4a7c",
    "to_signature": "MEYCIQC9...base64-encoded-Ed25519..."
  }
}
```

Dawn read it slowly. She had Tom's notebook in her sightline; he was writing down attribute names.

"This is the handover-initiated entry," Cal said. "Run-ID `marketing-ai-handover-2025-11`. Sequence 1, genesis form. The legacy export's SHA-256 is in the canonical bytes — 1.4 terabytes of Total Expert export, hashed at handover. The new model-card hash and the legacy model-card hash are both bound. The lineage manifest from the legacy side is bound. The provider-chain-entry-ID points at the matching entry on the Total Expert side — same hash family. The dual signatures are from §10.17's partition-ceremony attestation pattern: Total Expert's CTO signed the from-party side, our CTO signed the to-party side. Both signatures are bound into the seal that closed the day this entry landed."

Raj said, "Show me the seal."

Cal pulled it up. The seal record for 2025-11-04 carried a Merkle root over the day's entries, the dual signatures attested at the partition-ceremony level, and a `signing_key_fingerprint` matching the published key for that quarter.

```
seal_id:                 seal-bcfcu-prod-2025-11-04
tenant_id:               bcfcu-prod
seal_date:               2025-11-04
merkle_root:             7a2f9c1e4b8d6a3c5f1e7b9d2c8a4f6e0d3b7c1a5f9e2d8b4a6c0f3d7e1b5a9c
leaf_count:              14,872,341
signing_key_fingerprint: c1a5d8f3b9e2c7a4d6f0b3e9c2a5d8f3
signed_at_hsm_utc:       2025-11-05T04:15:23.001Z

attendance_attestation_§10.17:
  - party: total-expert-legacy
    signer: te-cto-signer-fingerprint-3b9d2c8a
    role:   from-party (handover provider, final attestation)
  - party: bcfcu
    signer: bcfcu-cto-signer-fingerprint-8f1e4a7c
    role:   to-party (handover receiver, institutional acceptance)
```

Raj said, "Run the verifier against this seal."

Cal typed.

```
herald-verify --tenant=bcfcu-prod --date=2025-11-04 --strict
```

Output:

```
Status: PASS
Step: 12
Reason: chain integrity verified, HMAC recomputed,
        Merkle path resolved, signature verified
        against public key c1a5d8f3...
Elapsed: 7.2s

Anomalies:
  late-binding entries: 0
  cross-vendor handover events: 1
    audit.model_handover.run_id = marketing-ai-handover-2025-11
    audit.model_handover.dual_signatures: verified
```

Raj read the output twice. He had the spec page open on his other monitor.

"The verifier reports the dual signatures as verified. That's §7 step 11 dispatch on §10.21 cross-vendor handover entries?"

"§7 step 11 dispatches on `chain_kind=audit` plus the presence of the `audit.model_handover.*` family. Step 11 walks the dual-signature pair, verifies both Ed25519 signatures against the published fingerprints, and confirms the legacy-export hash is bound into the canonical bytes. Step 12 emits the `cross_vendor_handover_verified` marker per §10.12 verifier-marker discipline."

Mike said, "Where does the legacy-export hash get validated against the actual export?"

Cal said, "That's the §10.40 byte-equality reconciliation. The 1.4-TB legacy export is on-disk in our S3 cold-tier under compliance-mode object lock. The verifier doesn't pull a terabyte by default — that would be a network punishment. But the chain entry has the hash. If anyone wants to verify byte-equality, the §10.40 reconciliation tool reads the on-disk export and recomputes the SHA-256, then compares against the chain entry. Let me run it."

He typed.

```
herald-verify-handover --run-id=marketing-ai-handover-2025-11 \
                       --reconcile-legacy-export \
                       --strict
```

The terminal began ticking. Cal looked at his watch.

"It's reading the export from S3 cold-tier. Nine minutes for 1.4 terabytes if the cold-tier prefetch is warm; closer to fifteen if not."

Dawn said, "We'll wait."

The team did wait. The terminal ticked through stages — `staging legacy export from s3-glacier-instant`, `streaming bytes`, `computing sha-256`, `final hash compare`. After nine minutes and eleven seconds, the output completed:

```
Status: PASS
Step: 12
Reason: chain integrity verified,
        legacy export byte-equality reconciled against
        audit.model_handover.legacy_export_artifact_sha256,
        cross-vendor handover dual signatures verified
Cross-vendor markers:
  cross_vendor_handover_verified
  legacy_export_byte_equal
Elapsed: 9m11s
```

Raj sat back. He took a long drink of coffee.

*Byte-equality against a 1.4-terabyte legacy export from twenty-three weeks ago,* he thought. *That's the thing that's supposed to be expensive and embarrassing to demonstrate. They demonstrated it in nine minutes.*

> ### ✓ Confirmation #1 — §10.21 cross-vendor model-handover verifies end-to-end with legacy-export byte-equality
>
> The November 2025 cross-vendor model-handover entry verifies under `herald-verify --strict` per the §7 procedure with the §10.21 dispatch path at step 11. The verifier emits `cross_vendor_handover_verified` per §10.12 verifier-marker discipline. The §10.17 dual-signature pair (Total Expert's CTO on the from-party side, Hill Country's CTO on the to-party side) verifies against both signers' published Ed25519 fingerprints. Byte-equality between the on-disk 1.4-TB Total Expert export and the chain entry's `audit.model_handover.legacy_export_artifact_sha256` reproduces in nine minutes eleven seconds end-to-end under §10.40's single-substrate cross-vendor chain-merge anchor reconciliation. The institution's CC8.1 names §10.21 + §10.40 as the institution's anchor pair for the handover boundary.

Dawn wrote: *§10.21 ✓. §10.40 single-substrate ✓. Byte-equality demonstrated end-to-end on a 1.4-TB legacy export. Nine minutes eleven seconds.*

She underlined the time. *Nine minutes for a 1.4-terabyte byte-equality reconcile is the kind of number you'd put in a memo,* she thought. *That's the demonstration the NCUA examiner is going to ask for.*

Cal said, "Anything else on the anchor?"

"One more thing," Dawn said. "The legacy provider's side. The Total Expert chain — that lives on Total Expert's infrastructure, not ours. How does the verifier confirm the legacy side is what it claims to be?"

"That's the `audit.model_handover.provider_chain_entry_id` field. It points at a Total Expert chain entry — `te-legacy-handover-final-2025-11-04` — which is on Total Expert's chain, not ours. Total Expert was on TesseraSeal too, on their own tenant. When we ran the §10.21 verifier in non-reconcile mode, the verifier just confirms our side — our chain entry references their entry by ID, and our entry's MAC binds the reference. If we want to walk the provider side, we ask Total Expert to produce a verifier output against the referenced entry. They did this at handover; the workpaper from the cutover ceremony has both verifier outputs."

Cal pulled up the cutover workpaper. Two verifier outputs, side by side. The Total Expert side returned PASS, step 12, against their tenant `total-expert-bcfcu-mirror`, on entry `te-legacy-handover-final-2025-11-04`, signed by their own CloudHSM partition. The Hill Country side returned PASS, step 12, against our entry. The two were cross-anchored: the entry IDs referenced each other; the dual signatures were on both sides; the legacy-export hash was bound in both.

"Bidirectional cross-anchor," Cal said. "Each side verifies the other's by-ID reference. Each side has the other's signature in their seal. The chain composes across the vendor boundary by hash-equality and signature-pair, not by trusting one side's claim of the other."

Mike said, "What's stopping Total Expert from going dark? They're a legacy vendor at this point. What if they decommission their chain in six months?"

Cal said, "§10.42 backfill-seal discipline. At handover we requested and received Total Expert's final backfill seal — a sealed record of every chain entry they produced for our mirror tenant over the lifetime of our relationship. The backfill seal is on our side now. If Total Expert goes dark tomorrow, the institutional record is preserved. We have the backfill seal's Merkle root, the daily-seal history, the per-event MACs in archival form, and the §10.19 `audit.external_artifact.*` family pointing at the backfill seal's artifact. The verifier walks the backfill seal under the §10.42 dispatch path."

Mike wrote: *§10.42 backfill-seal — survives provider going dark.*

Dawn nodded slowly. "OK. The handover is sealed. The byte-equality reconciles. The dual signatures pair correctly. The provider's chain history is preserved on our side via the §10.42 backfill seal. The next question is what the new-vendor side looks like."

---

## 🧠 10:00 AM — Database Deep Dive (Cross-Vendor Chain)

Raj wanted to look at the chain itself. He had the same forty-query checklist he ran against every chain-of-custody system. He started with the soft ones, the same way he always did.

```
SELECT COUNT(*) FROM chain_entries WHERE tenant_id = 'bcfcu-prod';
```

The count came back at 218,447,322. Eleven months of production, full member-experience surface, six hundred thousand members. That was roughly twelve entries per member per month, which was about what the architecture diagram had predicted.

```
SELECT COUNT(*) FROM chain_entries WHERE tenant_id = 'bcfcu-prod' AND prev_hash IS NULL;
```

One row. The genesis block from eleven months ago. As specified.

```
SELECT entry_id, seq, prev_hash, payload_hash FROM chain_entries
WHERE tenant_id = 'bcfcu-prod' AND chain_kind = 'audit'
  AND service_name = 'bcfcu-marketing-handover'
ORDER BY seq LIMIT 30;
```

Thirty rows. The first one was the November 4 handover-initiated entry. The next twenty-nine were post-handover entries on the same run — model-update events, periodic re-attestation entries, the §10.21 schema family running its normal cadence. Each `prev_hash` matched the previous row's `payload_hash`. Raj didn't say anything. He kept going.

He ran the chain-walk verifier against a 100,000-row window centered on the handover date.

```
herald-verify --tenant=bcfcu-prod --range=2025-10-15..2025-11-25 --strict
```

The verifier finished in twenty-seven seconds. Exit code 0. The output included a summary line:

```
Cross-vendor handover events processed: 1
Cross-vendor anchor verified: cross_vendor_handover_verified
Late-binding entries in window: 6
```

Raj noticed the six late-binding entries. "Six late-bindings in the handover window. Walk me through those."

Cal pulled them up. Each was a Total Expert mirror connector event that had been in flight during the cutover hour — entries whose `captured_at` was before 14:00 UTC on November 4, but whose `received_at` was after the seal cut. The handover ceremony had been timed at 14:00 UTC precisely; the connector lag had landed six entries on the wrong side of the cutover boundary by milliseconds to minutes. Each carried `late_binding=true` per §4.4 and was sealed in the next day's record.

Raj read each one. They were all benign — campaign-membership updates and an A/B variant assignment, all from the legacy Total Expert mirror, all closing out work that the connector had been doing right up to the cutover handshake.

"That's a clean cutover," Raj said. "Six in-flight entries. All labeled `late_binding=true`. None of them silently re-emerging in the post-handover stream."

Cal said, "The post-handover stream is from the new mirror — HubSpot CRM + in-house ML scoring. Different connector, different service name. Even if the late-bindings hadn't been labeled, they couldn't have been mistaken for new-vendor entries."

Raj wrote: *Late-bindings labeled. Service-name discriminates. No silent re-emergence.*

He picked a random entry from the new-vendor stream — a HubSpot campaign-membership event from December 12, 2025. He extracted its `entry_hash`, ran a manual SHA-256 over the canonicalized payload (RFC 8785 JCS) plus the `prev_hash`, and recomputed. The hash matched. He did the same with the HMAC, using the per-tenant HKDF-derived key. The HMAC matched. He repeated the process for entries from January, February, March, and April. Each one matched.

He picked one entry from each side of an IKM rotation boundary. Hill Country rotated IKM quarterly under §10.10 rotation-crossing-the-seal-boundary procedure. The Q4 2025 to Q1 2026 rotation had crossed seven weeks after the cutover. Raj picked one entry from Q4 2025, one from Q1 2026, both from the same run on the new-vendor side. Both verified. The `key_version` field on each was different; the `key_fingerprint` was different; the HKDF derivation for each was different; and the verifier had handled the dispatch correctly.

> ### ✓ Confirmation #2 — Chain walks cleanly across the cross-vendor boundary
>
> Raj independently recomputed the SHA-256 entry hash and the HMAC-SHA-256 MAC for sampled entries on both sides of the cross-vendor handover (the legacy-side mirror stream pre-handover, and the new-side HubSpot + in-house ML stream post-handover). The handover-window 100,000-row chain walk verified in twenty-seven seconds under `herald-verify --strict` with zero anomalies beyond six expected late-binding entries that bracketed the 14:00 UTC cutover handshake. The §10.10 IKM rotation crossing the seal boundary seven weeks post-handover handled cleanly — the verifier resolved the correct `key_version` and `key_fingerprint` per entry. The compositional security argument of §1.4 holds across the cross-vendor boundary because the boundary is bound into the chain via the §10.21 anchor; the §1.4 three-layer custody assumptions extend through the handover by the dual-signature pair plus the §10.42 backfill seal preserving the provider-side history.

Raj sat back. He looked at Cal.

"What about the late-binding entries from the legacy side that landed in the new-vendor era's seal? They were from the legacy service name, but they were sealed by the new-vendor side's daily seal."

Cal said, "Sealed by the same daily seal that closed the day. The seal is per-tenant-day. We have one tenant — `bcfcu-prod`. The legacy mirror was a service within that tenant; the new mirror is a service within the same tenant. Both share the daily seal. The §10.40 single-substrate cross-vendor anchor lets the seal cover both — the seal's Merkle tree includes leaves from both services on the cutover day. It's a clean composition because we never spun up a separate tenant for the new vendor."

Mike asked, "Why single-tenant?"

Cal said, "Because the institutional identity is the credit union, not the vendor. The vendor is operational. The institution is the FCU. If we had split tenants per vendor, the §10.69 disclosure walk would have to span tenants — and §10.69 disclosure subtrees walk within a tenant. Keeping single-tenant means the per-customer audit-trail subset disclosure is one walk, one Merkle root, one signature. The vendor change is a service-name change, not a tenant change."

Raj wrote: *Single-tenant decision pays off in §10.69. Vendor is a service; institution is the tenant.*

He underlined *tenant is institutional identity.*

The morning was settling into a rhythm. Raj kept running queries. He pulled up the daily seal for cutover day — November 4, 2025 — and walked through its Merkle tree depth. Twenty-three levels, three point four million entries that day across the full member surface. He pulled the seal for the day before — November 3 — and walked it too. Same depth, similar leaf count. The Merkle tree's shape was indistinguishable between the day before the handover and the day of the handover. The institutional substrate had not changed; only the marketing-AI service had.

"That's the property I needed to see," Raj said. "The day of the handover looks like every other day to the chain. The chain is invariant under the vendor change."

Cal said, "That's the institutional read on §10.21. The vendor changes; the chain doesn't notice except through the explicit handover entry. Every other entry is just a normal entry."

---

## 🔐 11:00 AM — IAM Review (Cross-Vendor)

Diana came in for the IAM review. She had a specific scenario she wanted to test: the vendor-handover credential transition. A change of marketing-AI vendor at this scale means dozens of service accounts deactivated on the legacy side and dozens issued on the new side, all within a tight cutover window, with the dual-signed handover ceremony binding the transition.

She started with the legacy side.

"Walk me through Total Expert's service-account decommissioning. The credentials they had into our infrastructure — how were they revoked?"

Cal said, "All of them are in the chain. Every Total Expert service account that had read access to our mirror tenant — about fourteen of them — was deactivated on November 4 between 14:00 and 14:30 UTC. Each deactivation is a chain entry. Each chain entry references the original grant entry by `parent_run_id` and `parent_seq` per §10.11 parent-linkage. The decommission window opens at handover initiation and closes at handover completion. After 14:30 UTC on November 4, no Total Expert service account had any read or write access to any Hill Country system."

Diana pulled up the decommission entries. Fourteen entries, each tagged `chain_kind=operational`, each with a `service.name=bcfcu-iam-revocation`, each binding the legacy service-account fingerprint to the revocation timestamp and the approver chain. Each had a dual approval — David Reyes as CAE and the institutional CTO — and each was sealed in the same November 4 daily seal that carried the handover event.

She picked one at random and walked the parent-linkage. The decommission entry referenced its grant entry from 2014, when Total Expert had been integrated into Hill Country for the first time. The grant entry was still in the chain — Hill Country had imported their historical IAM history into the chain when they went live on TesseraSeal eleven months ago, hash-anchored under §10.19 `audit.external_artifact.*` as `kind=legacy_iam_history_import`.

"You backfilled the IAM history?"

"Eleven months ago, when we went live on the chain. The IAM history before that date is not chain-native — it's the §10.19 external-artifact anchor — but the §10.42 backfill-seal pattern preserves it under the chain's daily seal. The decommissions in November had clean parent references because the grants were anchored."

Diana wrote: *IAM history backfilled at chain go-live via §10.19 + §10.42. Decommissions cross-reference grants cleanly.*

> ### ✓ Confirmation #3 — Cross-vendor service-account decommissioning is fully chain-coupled
>
> All fourteen Total Expert service accounts that held read access to Hill Country's mirror tenant were decommissioned on November 4, 2025 between 14:00 and 14:30 UTC. Each decommission is a sealed chain entry with `chain_kind=operational`, dual approval by the CAE and the CTO, and `parent_run_id` / `parent_seq` linkage per §10.11 to the original grant entry. The pre-chain-go-live grants are anchored via §10.19 `audit.external_artifact.*` with the §10.42 backfill seal preserving the legacy IAM history. After 14:30 UTC on November 4, no Total Expert service account retained any access to Hill Country infrastructure. The institutional decommissioning posture is verifiable end-to-end from the chain alone.

Diana moved to the new side. "And the HubSpot service accounts plus the in-house ML scoring layer's accounts — when were those issued?"

Cal said, "Starting November 4 at 14:30 UTC, immediately after the legacy decommission window closed. Each new account is a chain entry. Each grant is dual-approved. The new accounts ramped over the next forty-eight hours as the new vendor's services came online. By November 6 at 09:00 UTC the new-side IAM was at steady-state."

Diana ran the verifier on the new-side grant entries. PASS. PASS. PASS.

"What about the in-house ML scoring layer? That's not a vendor — that's your own infrastructure. How does the §10.21 cross-vendor anchor handle a vendor-to-in-house transition?"

Cal said, "The §10.21 attribute family has a `provider` field and a `receiver` field. The provider is `total-expert-legacy`. The receiver, in our case, is split — HubSpot Marketing Hub is the campaign-management surface, but the model-scoring layer that replaced Total Expert's ML scoring is `bcfcu-inhouse-ml`. The handover entry's `audit.model_handover.receiver` value is `bcfcu-inhouse-ml`. The HubSpot side gets its own service accounts under standard IAM, but doesn't carry the model-handover semantics because it didn't replace Total Expert's ML scoring — it replaced Total Expert's campaign-management surface. The ML scoring layer is the one §10.21 binds. The campaign-management side is just a normal new vendor with normal IAM."

Diana wrote: *§10.21 binds the model-scoring replacement specifically. Campaign-management transition is normal IAM. The two roles separate cleanly in the chain.*

Mike, who had been listening from the side, asked: "What about the in-house ML team's model-development environment? Where does that fit?"

Cal said, "Separate tenant — `bcfcu-mrm-dev`. The model-development pipeline is a different tenant from production. The ML team trains models in `bcfcu-mrm-dev` against held-out historical data. When a model is promoted to production, the promotion event lands in `bcfcu-prod` as an `audit.model_promotion.*` entry under §10.34 training-phase integrity, with the model-artifact hash, the model-card hash, and the training-environment attestation hash bound under the per-event MAC. The MRM committee reviews the promotion entries; the auditor walks them at AIRES exam time."

Mike wrote: *Separate tenant for MRM-dev. Promotion event in prod chain anchored under §10.34.*

He underlined *separate tenant for MRM-dev.*

Diana had one more question. "What happens if someone with access to both tenants tries to bypass the promotion event by writing directly into prod?"

Cal said, "The §10.34 promotion event is required by policy — the production deployment workflow refuses to activate a model that doesn't have a matching promotion entry in the prod chain. The workflow checks the model artifact's SHA-256 against the most recent `audit.model_promotion.*` entry for the model. Mismatch refuses. The verifier under `--strict` flags any model-call entry whose model-artifact hash doesn't reference a sealed promotion event."

"And if someone tampers with the promotion event after the fact?"

"They can't. The promotion event is sealed daily and the chain is append-only. A tampered promotion event would break the per-event MAC, the chain-walk, and the daily seal — three layers of refusal."

Diana wrote: *Promotion event sealed. Direct-to-prod model activation refused at workflow layer. Tamper closed at three layers per §1.4.*

> ### ✓ Confirmation #4 — Model-promotion gates are chain-coupled
>
> The in-house ML scoring layer runs its development workload in a separate tenant (`bcfcu-mrm-dev`). Model promotions to production land in `bcfcu-prod` as sealed `audit.model_promotion.*` entries under §10.34, with the model-artifact SHA-256, model-card hash, and training-environment attestation hash bound under the per-event MAC. The production deployment workflow refuses to activate a model whose artifact hash does not reference a sealed promotion event. Tampering with a promotion event after the fact is closed at three layers per §1.4 — per-event MAC, chain-walk, and daily seal.

The IAM walk took an hour and ten minutes. Diana had run forty-seven separate queries. Every IAM-lifecycle event from the cutover window had been chain-recorded; every grant had a clean parent reference; every decommission had a dual approval and a sealed timestamp. The §10.21 anchor had handled the institutional transition without introducing any IAM ambiguity.

She closed her laptop halfway.

"OK. That's the cleanest cross-vendor IAM transition I've seen. The legacy side decommissions cleanly. The new side ramps cleanly. The §10.21 receiver distinction handles the in-house-ML-vs-HubSpot split correctly."

Tom wrote that down.

---

## 🧪 12:00 PM — Lunch (But Not Really)

The team ordered barbecue from a place a mile down MoPac. Nobody left the building. The boxes came in twenty minutes — brisket, ribs, sausage, slaw, and a stack of white bread on the side. The engagement room smelled like a smoker by 12:30 PM.

Dawn poured herself a second coffee and sat at the long side of the table. Tom was at the end, on a phone call with David Reyes. The rest of the team was eating quietly.

When Tom got off the phone, Dawn caught his eye.

"What's our finding count?"

"Zero Gaps. Zero Partials. Zero Nits. The morning was a confirmation walk — the §10.21 cross-vendor anchor verifies end-to-end. The handover ceremony was clean. The IAM transition was clean. The chain walks cleanly across the boundary. The byte-equality reconciliation closes in nine minutes against a 1.4-terabyte legacy export."

"And the §10.16 connector lag wording — that was the one §10.16 specifically warns about. Did the HubSpot mirror runbook have the four quantified bounds?"

"It did. Median twelve seconds, ninety-fifth-percentile SLO ninety seconds, alerting threshold one-fifty seconds, RTO sixty minutes. The CC8.1 description cross-references the bounds and the §10.16 freshness invariant. David Reyes wrote that part of the runbook himself after he read the Northbridge engagement report — he said it was the second thing he updated when the §10.21 clause shipped, right after the marketing-AI vendor handover plan itself."

Dawn raised an eyebrow.

*He read the Northbridge report,* she thought. *That's a CAE who reads other people's reports. There aren't many.*

"Tom. There's one thing I want to disclose on the record before the afternoon. While we're still in the room with just the team."

Tom looked up.

"The Herald release that shipped §10.21 in April — that's the spec extension Hill Country exercised at cutover. I have a relationship with the spec author of that section. He is the principal designer of the §10.21 schema family. He is not in the room and he will not be in the room. I have no direct working relationship with him on this engagement. I am declaring it for the engagement file. I want it logged so the AIRES examiner can read the disclosure if they ask."

Tom wrote in his notebook, slowly. *Engagement file disclosure: lead auditor has prior professional relationship with §10.21 spec author. Author not present, not consulted, no involvement in this engagement. Logged at 12:35 PM Tuesday by the lead auditor's voluntary disclosure. Tom Burke, IA liaison, witness.*

He read it back. Dawn nodded.

"That's the disclosure," she said. "Append a separate note in the engagement file that the spec sections being exercised today — §10.21, §10.40, §10.69, §10.11.1 — are publicly shipped, publicly versioned, and the verifier is open source. The engagement does not rely on any private communication with the spec author. Every section is observable from the shipped artifact."

"Logged."

"Thank you."

She turned back to her plate.

Raj, across the table, said: "You did that for the Northbridge report too. The Vidimus team disclosure."

"Yes."

"Same routing?"

"Same routing. The disclosure goes into the engagement file. Tom witnesses it. The institution's audit committee can see it. The AIRES examiner can see it. I do not redact it. I do not paraphrase it."

"You should put that in the training materials."

"I have."

Raj almost smiled.

She thought, briefly, about the Northbridge engagement file. The disclosure paragraph had been six sentences long. David Reyes had not asked about it; he had assumed, correctly, that it was already filed and that the disclosure was standard for any spec extension Hill Country exercised. The professional norm was settled. The framing was matter-of-fact.

*Foresight isn't a rescue,* she thought. *It's a clause that shipped on the spec calendar before the institution needed it. The disclosure is for the file, not for the narrative.*

She ate the brisket. It was very good brisket.

---

## 🔄 1:00 PM — ECOA Reconciliation: The Auto-Loan Case

Anwar Patel came down at 1:00 PM sharp. He was Hill Country's CCO and ECOA counsel — mid-fifties, a former in-house lawyer at a regional bank in Houston before moving to the credit-union side ten years ago. He carried a single manila folder. He set it on the table, opened it, and turned the first page toward Dawn.

"This is the member I'd like you to walk."

The page was a single-member file. The member's name was redacted; the file was identified by a hashed member-ID — `mem-h:7a4e9c2f...`. The case was an auto-loan adverse-action case that had crossed the marketing-AI vendor handover boundary cleanly.

"Pre-handover," Anwar said, "the member received a 'you're pre-qualified for a $35,000 auto loan at 6.250%' marketing offer. The offer was generated on a Tuesday in February — February 4, 2025 — under the Total Expert ML scoring weights. The member did not act on the offer immediately. Three weeks later, on February 25, the member applied for the loan. Under the in-house ML scoring weights, which had not yet been promoted at that time. So in February the loan application went through the legacy scoring."

"And the loan was approved at 6.625% on a slightly different term structure than the marketing offer," Dawn said, reading from the folder.

"Approved at 6.625% on a 72-month term. The marketing offer had been 6.250% on a 60-month term. The member applied for 72 months because that was the term the dealer pushed. The 37.5 basis-point delta is what the CCO question is about. Did the marketing-AI event under one scoring regime inform the credit decision under another scoring regime, and if so, is the institution's adverse-action posture defensible if the member challenges the pricing under ECOA?"

Dawn looked at the dates again.

"The application was in February. The handover was in November. So in February both the marketing offer and the credit decision were under the legacy Total Expert scoring."

"Correct. The member's auto-loan was approved and disbursed in February. The member made regular payments through the year. In November 2025 — three weeks after the handover — the member was sent a refinance offer under the new HubSpot + in-house ML scoring. The refinance offer was at 5.875% on a 60-month term. The member accepted the refinance offer. The refinance loan was approved at 6.125% on a 66-month term."

Dawn re-read.

"So there are two adverse-action surfaces here. Or rather — two pricing surfaces. The original loan crossed from the legacy marketing offer to the legacy credit decision. The refinance loan crossed from the new marketing offer to the new credit decision. And the member's history with the institution crosses the handover."

"Correct. The CCO question is the second one specifically. The refinance offer in November was generated under the new HubSpot + in-house ML scoring. The refinance credit decision was made under the same new ML scoring. Both events are post-handover. But the member's *prior offers* and *prior credit decisions* — the data the new ML scoring uses as features — span the handover. The new ML scoring layer looks at the member's prior marketing engagement, prior loan applications, prior loan performance, and uses them as features. Some of that data was generated under the legacy regime."

"And if the member challenges the refinance pricing — if they say 'the November refinance offer at 5.875% became a credit decision at 6.125%, and the 25 basis-point delta is not explained' — what does the institution show?"

Anwar said, "I'd like the chain to show me the whole story. The marketing event in November under the new scoring. The credit decision in November under the same new scoring. The features the new scoring used. The hashes of the prior offers and prior credit decisions that fed into the feature set. The model card for the new scoring. The model-promotion event for the new scoring. The cross-vendor anchor that binds the prior-era data into the post-handover chain. And the parent-linkage that connects the November marketing event to the November credit decision."

"Walk me through it," Dawn said.

Cal pulled up the November chain entries for `mem-h:7a4e9c2f...`. Eight entries appeared on the screen.

The first was the November 14 marketing event — `audit.marketing.offer_generated`. The member's hashed ID, the offer terms (refinance, 5.875%, 60 months), the new in-house ML scoring's model version (`bcfcu-ml-v1.0.2`), the feature set used, and a `parent_offers` field listing the hashes of prior offers that had informed the new offer's feature engineering. One of those prior-offer hashes pointed at the February 4, 2025 marketing offer — the original pre-qualification offer under the legacy Total Expert scoring. The parent-offer hash was bound under the per-event MAC. The chain made it byte-equal that the new scoring had used the prior offer as a feature.

```jsonc
{
  "ffiec.chain.spec": "v1.0",
  "ffiec.chain.chain_kind": "model_call",
  "ffiec.chain.run_id": "mem-h:7a4e9c2f-marketing",
  "ffiec.chain.tenant_id": "bcfcu-prod",
  "ffiec.chain.captured_at": "2025-11-14T15:23:41.892000000Z",
  "ffiec.chain.seq": 47,
  "service.name": "bcfcu-marketing-scoring",
  "service.version": "bcfcu-ml-v1.0.2",
  "event": "audit.marketing.offer_generated",
  "gen_ai.request.model": "bcfcu/marketing-scoring",
  "gen_ai.response.model": "bcfcu/marketing-scoring",
  "audit.deployment.intent": "production",
  "audit.deployment.policy_version": "bcfcu-mrm-2025q4",
  "audit.marketing.offer_kind": "auto_loan_refinance",
  "audit.marketing.offer_terms": {
    "principal_offer_apr": "5.875",
    "term_months": 60,
    "principal": 28400
  },
  "audit.marketing.feature_set_hash": "c4e8d2a6b0f3e7d1a4b8c2e5f9c4e8d2",
  "audit.marketing.parent_offers": [
    {
      "prior_offer_run_id": "mem-h:7a4e9c2f-marketing",
      "prior_offer_seq": 12,
      "prior_offer_hash": "ad7e2c9f1b4d8e3a0c5b9d2e6f1a4c7e",
      "prior_offer_era": "legacy_total_expert"
    }
  ],
  "audit.model_card_sha256": "b8e2c6a0d4f8b2e6c0a4d8b2e6c0a4d8",
  "audit.model_promotion_ref": "promotion-bcfcu-ml-v1.0.2-2025-10-22"
}
```

The second entry was the November 14 contact event — the offer landed in the member's email and the member opened it the same day. The third entry was a click-through to the refinance application page. The fourth was the start of the refinance loan application. The fifth was the application submission. The sixth was the in-house ML credit-decision event.

That sixth entry was the load-bearing one. Anwar pointed at it.

```jsonc
{
  "ffiec.chain.spec": "v1.0",
  "ffiec.chain.chain_kind": "model_call",
  "ffiec.chain.run_id": "mem-h:7a4e9c2f-credit",
  "ffiec.chain.tenant_id": "bcfcu-prod",
  "ffiec.chain.captured_at": "2025-11-14T15:51:08.244000000Z",
  "ffiec.chain.seq": 28,
  "service.name": "bcfcu-credit-decisioning",
  "service.version": "bcfcu-credit-v3.7.1",
  "event": "audit.ecoa.adverse_action.scoring_complete",
  "audit.deployment.intent": "production",
  "audit.deployment.policy_version": "bcfcu-mrm-2025q4",
  "audit.ecoa.adverse_action.decision_kind": "counter_offer",
  "audit.ecoa.adverse_action.outcome": "approved_at_modified_terms",
  "audit.ecoa.adverse_action.original_request": {
    "apr_requested": "5.875",
    "term_months_requested": 60,
    "principal_requested": 28400
  },
  "audit.ecoa.adverse_action.counter_offer": {
    "apr": "6.125",
    "term_months": 66,
    "principal": 28400
  },
  "audit.ecoa.adverse_action.reason_codes": [
    "TI-01: Term-length adjustment for risk-bracket match",
    "PR-04: Pricing-tier alignment with credit-bureau refresh"
  ],
  "audit.ecoa.adverse_action.feature_set_hash": "f9c4e8d2a6b0f3e7d1a4b8c2e5f9c4e8",
  "audit.ecoa.adverse_action.prior_offer_run_id": "mem-h:7a4e9c2f-marketing",
  "audit.ecoa.adverse_action.prior_offer_seq": 47,
  "audit.ecoa.adverse_action.prior_offer_hash": "9b3c7e1a4f8d62b0c5a1e9f4d2b8c0e3",
  "audit.ecoa.adverse_action.cross_vendor_handover_ref": "marketing-ai-handover-2025-11",
  "audit.model_card_sha256": "d4a8c2e5f9c4e8d2a6b0f3e7d1a4b8c2",
  "audit.model_promotion_ref": "promotion-bcfcu-credit-v3.7.1-2025-09-30",
  "audit.fcra.reason_code_dictionary_version": "bcfcu-rcd-2025q4"
}
```

Anwar said, "The `prior_offer_run_id` and `prior_offer_seq` fields are the parent-linkage. The credit decision points at the marketing offer that informed it. Same pattern §10.11 establishes for translation-to-decision linkage, reused here for the prior-offer-to-decision pivot. The CCO question gets answered by walking from the credit-decision entry back to the marketing-offer entry to the model-promotion entry to the model-card to the prior offers under the legacy era — all the way back to the February 4, 2025 pre-qualification offer."

Dawn said, "Walk me through what the verifier sees when it processes this credit-decision entry."

Cal typed.

```
herald-verify --tenant=bcfcu-prod \
              --entry-id=mem-h:7a4e9c2f-credit:28 \
              --strict --explain
```

A 73-line trace scrolled past. The verifier walked the chain backward from the credit-decision entry. Step 6 confirmed the per-event MAC. Step 7 confirmed the structural walk. Step 8 confirmed the key fingerprint. Step 9 confirmed the `expected_prev_hash` linkage. Step 11 dispatched on the `audit.ecoa.adverse_action.*` family per §10.11.1. The verifier emitted three markers:

```
ecoa_adverse_action_dispatched
prior_offer_linkage_resolved
cross_vendor_handover_referenced
```

The `prior_offer_linkage_resolved` marker confirmed the parent-linkage between the November 14 credit decision and the November 14 marketing offer. The `cross_vendor_handover_referenced` marker confirmed that the credit-decision entry's `audit.ecoa.adverse_action.cross_vendor_handover_ref` field pointed at a sealed handover entry (the November 4 handover-initiated event), and that the handover entry's anchor was intact.

Anwar said, "Walk further. Pull the prior-offer entry — the February 4 legacy-era offer that informed the November feature engineering."

Cal pulled it up. February 4, 2025. Pre-handover. Service-name `bcfcu-marketing-mirror-legacy`. The entry was on the legacy Total Expert mirror, sealed under the legacy daily seal, signed by the same CloudHSM key (the institutional signing key, not a vendor-specific key — Hill Country owned the signing key throughout).

```jsonc
{
  "ffiec.chain.spec": "v1.0",
  "ffiec.chain.chain_kind": "model_call",
  "ffiec.chain.run_id": "mem-h:7a4e9c2f-marketing",
  "ffiec.chain.tenant_id": "bcfcu-prod",
  "ffiec.chain.captured_at": "2025-02-04T19:14:22.703000000Z",
  "ffiec.chain.seq": 12,
  "service.name": "bcfcu-marketing-mirror-legacy",
  "service.version": "te-cdc-mirror-v4.8.1",
  "event": "audit.marketing.offer_generated",
  "audit.connector_source.system": "total-expert-cdc",
  "audit.connector_source.replay_id": 873421,
  "audit.connector_source.commit_timestamp": "2025-02-04T19:14:21.541Z",
  "audit.connector_source.lag_observed_ms": 1162,
  "audit.connector_source.change_kind": "CREATE",
  "audit.marketing.offer_kind": "auto_loan_prequalification",
  "audit.marketing.offer_terms": {
    "principal_offer_apr": "6.250",
    "term_months": 60,
    "principal": 35000
  },
  "audit.marketing.feature_set_hash": "ad7e2c9f1b4d8e3a0c5b9d2e6f1a4c7e",
  "audit.marketing.legacy_vendor_model_version": "te-marketing-scoring-v8.4.2"
}
```

Cal said, "That's the February 4 entry. The hash `ad7e2c9f1b4d8e3a0c5b9d2e6f1a4c7e` is the entry's payload hash, which is also what the November 14 credit decision's `prior_offer_hash` field references. The linkage is byte-equal between the two entries via the parent-linkage fields."

Dawn ran the verifier on the February 4 entry independently.

```
herald-verify --tenant=bcfcu-prod \
              --entry-id=mem-h:7a4e9c2f-marketing:12 \
              --strict
```

PASS. Step 12. 4.7 seconds. The seal that closed February 4, 2025 verified against the legacy-era signing key fingerprint, which was the same fingerprint as the current one — Hill Country's IKM had rotated quarterly per §10.10, but the institutional signing key (the seal-signing Ed25519 key in CloudHSM) had been on a longer rotation cadence. The February 4 entry was under `key_version=2`; the November 14 entry was under `key_version=3`; the verifier handled the dispatch transparently.

Anwar said, "Now walk through what NCUA's examiner would see. The CCO question is: can the institution show that the marketing-AI event under the legacy regime informed the credit decision under the new regime, and that the linkage is examinable in workpaper form?"

Dawn answered. "The chain shows the linkage directly. The November 14 credit-decision entry references the February 4 marketing offer by hash. The hash is bound under the per-event MAC on both entries. The §10.21 cross-vendor handover anchor binds the legacy era to the new era. The §10.11.1 `audit.ecoa.adverse_action.*` family carries the parent-offer linkage via `prior_offer_run_id` and `prior_offer_seq`. The verifier emits `prior_offer_linkage_resolved` and `cross_vendor_handover_referenced` on the credit-decision entry. The institution can produce, on an examiner's request, a workpaper that walks from the credit-decision entry back to the model promotion, back to the model card, back to the cross-vendor handover, back to the prior-offer hash, all the way to the February 4 legacy-era entry. Every link in the chain is verifiable."

She paused.

"Whether the policy is fair is a different question. The chain proves what happened. It does not prove that what happened was right. That's the §1.2 epistemic-scope line."

Anwar said, "I agree. And I want the §1.2 line on the cover memo. The chain shows the linkage. The fair-lending substantive analysis is a separate program. I do not want our witness drawn onto the truth foundation by a CFPB examiner who hasn't read §1.2."

Dawn said, "On the cover memo. Front of the package. I'll write it."

Anwar smiled, just a little. "Thank you."

Tom wrote: *§1.2 epistemic-scope line on cover memo. Marketing-AI to credit-decision linkage is chain-bound; fair-lending substantive analysis is separate.*

> ### ✓ Confirmation #5 — ECOA prior-offer-to-decision linkage walks cleanly across the cross-vendor boundary
>
> The November 14, 2025 refinance credit-decision entry for `mem-h:7a4e9c2f` references the November 14 marketing offer via `audit.ecoa.adverse_action.prior_offer_run_id` and `prior_offer_seq` parent-linkage per §10.11.1. The November 14 marketing offer's feature engineering references the February 4, 2025 legacy-era pre-qualification offer via `audit.marketing.parent_offers[].prior_offer_hash`. The February 4 entry was generated under the Total Expert ML scoring regime; the November 14 entries were generated under the in-house ML scoring regime. The cross-vendor handover anchor binds the two eras. The verifier emits `ecoa_adverse_action_dispatched`, `prior_offer_linkage_resolved`, and `cross_vendor_handover_referenced` on the credit-decision entry. Five members were walked end-to-end (the auto-loan refinance case shown, plus four additional members spanning HELOC, mortgage-refinance, credit-card-pricing, and a denied applicant). All five resolved cleanly. The institution can produce, on examiner request, a single-member workpaper walking from credit decision through model promotion through model card through cross-vendor anchor through prior-offer hash to the legacy-era origin entry. Whether the policy is substantively fair under ECOA is outside the chain's evidentiary scope per §1.2; the chain proves the linkage but not the fairness.

Anwar stayed for another twenty minutes. He walked Dawn through the four additional members. The HELOC case had a similar shape — a legacy marketing offer, a new credit decision, parent-linkage clean. The mortgage-refinance case crossed the handover during the application window itself, so the marketing offer was under the legacy regime and the credit decision was under the new regime, with the handover-initiated entry referenced explicitly. The credit-card-pricing case was post-handover entirely. The denied applicant had been denied under the new in-house ML scoring, with the adverse-action notice generated and the §10.11 ECOA translation event chained, the reason-code dictionary version pinned per §10.18, and the consumer-correlation index tracked under §10.23.

By 2:50 PM, the team had walked five end-to-end member traces. Each had taken roughly fifteen to twenty minutes of verifier work, model-card review, and feature-set inspection. All five reconciled cleanly.

Anwar closed his folder.

"Thank you," he said. "That's the question I needed answered. The institution can stand in front of a CFPB examiner and walk the linkage. The chain is the workpaper. The verifier is the procedure. The spec sections are the citations."

He stood up to leave. At the door, he turned back.

"One more thing. The fair-lending substantive analysis. We have a separate program for that. The chain feeds it; the chain doesn't replace it. I wanted to be clear about that line because last year a vendor at a peer institution told their CCO that the chain proved fair lending. It doesn't. Their CCO believed them. It got messy."

Dawn said, "§1.2 doesn't let the chain make that claim. Anyone selling it that way is selling something the spec specifically prohibits."

"Yes. That's the line. Thank you for keeping it."

He left.

---

## 🧬 3:00 PM — The Marketing-AI Lineage Walk (Karina, CMO)

Karina Holloway came in at 3:00 PM. She was the CMO — late forties, brisk, a marketing operations background, MBA from Texas. She had been at Hill Country for five years and had championed the marketing-AI vendor handover. She wanted to walk the team through the lineage on the new in-house ML scoring side and answer questions about model-card discipline.

She sat down at the second screen. "Where do you want to start."

Elena, who had been waiting for the marketing-AI deep dive since 1:00 PM, was first. "Model-card discipline first. Then the feature engineering. Then the A/B variants. Then the consent capture for cross-marketing-and-credit-decision linkage under DPDP-equivalent state law — Texas has the breach-notification regime, and the institutional posture for member consent capture is a Reg P / GLBA cross-cut we should walk."

Karina pulled up the model card for `bcfcu-ml-v1.0.2`.

The card was a structured document. Model purpose, training-data summary, feature inventory, performance metrics across demographic slices, known limitations, deployment-environment requirements, the model-promotion event hash, and the model-decommissioning policy. The card itself was hash-anchored to the chain via the §10.19 `audit.external_artifact.*` family — `kind=model_card`, `evidentiary_role=regulatory_compliance_mrm`, `received_at_utc=2025-09-30T14:00:00.000000000Z`. The card was reviewed quarterly by the MRM committee, with each review producing a new chain entry that referenced the prior version's hash.

Elena said, "And the legacy-era model card — the Total Expert scoring's card — that's preserved on our side via the cross-vendor handover?"

Karina said, "Via the §10.21 anchor. The handover-initiated entry binds `audit.model_handover.legacy_model_card_sha256` and `audit.model_handover.new_model_card_sha256`. The legacy model card itself is in our archival storage with compliance-mode object lock; the hash in the chain entry binds it. If an examiner asks for the legacy card, we produce it; the hash binds the artifact to the institutional record."

Elena wrote: *Legacy model card preserved via §10.21 + §10.19 anchor. New model card under MRM quarterly review with chain-anchored review entries.*

She kept going. "What about the feature inventory? The new in-house ML scoring uses features from member data, transaction history, and prior marketing engagement. The prior marketing engagement includes legacy-era data. How is the feature set documented as fair-lending-defensible?"

Karina said, "The MRM committee reviews the feature set against ECOA, FCRA, and HMDA disparate-impact tests on every promotion. The disparate-impact tests are themselves chain entries — `audit.fairness_audit.disparate_impact.*`. The tests are run against the held-out validation set. Each test is a chain entry with the test outcome, the demographic slice, the metric, and the threshold. The MRM committee signs off on each promotion only if the disparate-impact tests are within institutional tolerance. The tolerances are themselves chained as policy entries under §10.18 cross-referencing the CC8.1 control."

Elena pulled up the disparate-impact test entries for the September 30 promotion. Twelve test entries — one per demographic slice across the protected classes covered by ECOA — plus four supplementary tests on credit-score bands, geographic distribution, age bands, and self-identified veteran status. Each was a sealed chain entry. The MRM committee's sign-off was a thirteenth entry that referenced all twelve plus the four supplementary tests by hash.

Elena said, "That's the cleanest fairness-audit chain I've seen. Not because the tests are clever — they're standard disparate-impact tests — but because the linkage from the promotion event back to the tests back to the policy tolerances is fully chained."

Karina said, "The MRM committee chair will be in tomorrow morning to walk you through the policy-tolerance entries. She is more careful about the linkage than I am. I run the marketing side. She runs the validation side. We argue about the threshold values quarterly."

Mike asked, "What about the A/B variants in the new system? Are those chained?"

Karina said, "Every campaign variant is a chain entry. Variant definition under `audit.marketing.ab_variant.defined`. Variant assignment per-member under `audit.marketing.ab_variant.assigned`. Variant outcome under `audit.marketing.ab_variant.outcome`. The variant lineage is preserved. The MRM committee reviews any A/B test that crosses a regulatory threshold — pricing-related variants, eligibility-related variants, that kind of thing — with a fairness audit attached."

Mike wrote: *A/B variants chained. Variant lineage preserved. MRM review on regulatory-threshold variants.*

He had one more. "What about cross-channel marketing — voice campaigns, email, SMS, the mobile app's in-app notifications? Are those all chained?"

Karina said, "Every member-facing marketing event lands in the chain. The channel is captured as an attribute on the entry — `audit.marketing.channel`. The CC8.1 control description names the channels and the chain coverage per §10.19. The coverage is end-to-end on every member-facing surface."

She pulled up the §10.19 chain-coverage map for the marketing surface. The map was a one-page document, hash-anchored to the chain, listing every member-touchpoint and the chain-coverage posture for each. Email, SMS, voice, in-app notifications, branch-tablet kiosks, the wealth-advisor pilot's in-person interaction layer — every surface had a coverage entry, a service-name binding, a connector-source attribution where applicable, and a §10.16 freshness-bound published in CC8.1.

Mike studied the map for a long minute.

"That's a useful artifact," he said. "I want to see how it's maintained."

Karina said, "Quarterly review with the MRM committee. Each update is a chain entry. The version history of the coverage map is in the chain — every version, every change. If a new channel comes online, a new entry lands; the §10.19 map version increments and a `chain.coverage_map_published` event seals the update per §10.2 cross-referencing."

Mike wrote: *Coverage map version-controlled in chain. Quarterly MRM review.*

> ### ✓ Confirmation #6 — Marketing-AI lineage is fully chained across the cross-vendor boundary
>
> The new in-house ML scoring layer's model card is hash-anchored under §10.19 `audit.external_artifact.*` with `evidentiary_role=regulatory_compliance_mrm`. The legacy Total Expert model card is preserved via the §10.21 handover anchor and hash-bound in the cross-vendor handover entry. Fairness-audit disparate-impact tests under `audit.fairness_audit.disparate_impact.*` are run on every model promotion and sealed as chain entries with MRM committee sign-off. A/B variant lineage is fully chained — definition, assignment, and outcome events all land as sealed entries. The §10.19 chain-coverage map for the marketing surface is version-controlled in the chain with quarterly MRM committee review. Every member-facing marketing channel — email, SMS, voice, in-app notification, branch-tablet kiosk, wealth-advisor in-person — is captured in the chain with `audit.marketing.channel` discriminating attributes.

By 4:00 PM, Karina had walked through the lineage from marketing-event capture through feature engineering through model promotion through fairness audit through model card to deployment policy. The walk had taken forty-five minutes. She had answered every question without consulting notes. The marketing-AI handover, from the CMO's seat, was a settled program.

She stood up. "The CCO's question was the load-bearing one. Mine is whether the institution can keep iterating on the model without breaking the chain. The answer so far is yes — every quarterly promotion has been a clean event in the chain, every fairness audit has been chained, and the cross-vendor handover anchor has held."

Dawn said, "What's the next promotion cycle?"

"January. The new model version will be `bcfcu-ml-v1.1.0`. We're tightening the disparate-impact thresholds on two demographic slices. The MRM committee has already reviewed the validation results. The promotion event will land at the end of January."

"Will it be a routine promotion?"

"It'll be routine."

She left.

---

## 😬 4:00 PM — Friction: the Refinance-Era Feature

Dawn wanted to push on something. She had been listening to the linkage walk, and one thing had not sat clean for her. She wanted to find out whether the team's assessment held under stress.

"Cal, I want to look at one specific feature in the in-house ML scoring's feature set. The 'prior offer engagement velocity' feature. Karina mentioned it in passing — how a member's response time to prior offers feeds into the new scoring. I want to walk the data lineage for that feature on a single member."

Cal pulled up the feature documentation. The 'prior offer engagement velocity' feature was a computed metric — for any member, it summarized the median time between offer-presentation and offer-engagement across the member's prior twelve months. The feature was computed at scoring time from the member's marketing event history.

"Show me the computation for the November 14 refinance scoring on `mem-h:7a4e9c2f`."

Cal pulled it up. The feature was computed from twenty-seven prior marketing events for the member, spanning fourteen months. Of those twenty-seven events, eighteen were pre-handover (legacy Total Expert era) and nine were post-handover. The computation ran against all twenty-seven events without distinguishing era.

Dawn looked at it.

"The new scoring uses pre-handover marketing engagement data as a feature."

Cal said, "Yes. The member's marketing history is a continuous record from the institution's perspective. The vendor changed. The member did not."

Dawn said, "But the legacy-era marketing events were generated under a different scoring regime. They were generated under Total Expert's targeting weights, not the new in-house weights. So when the new scoring uses 'prior offer engagement velocity' as a feature, it's measuring engagement against offers that were targeted by a different model."

Cal said, "That's true."

Dawn said, "Is that documented? Does the model card name it?"

Cal pulled up the model card. The 'known limitations' section had a paragraph headed *Pre-handover feature compositional asymmetry*:

> *The 'prior offer engagement velocity' feature and related engagement-history features are computed against the member's full marketing-event history including events generated under the legacy Total Expert ML scoring regime (events prior to 2025-11-04). The legacy era's targeting model differed from the new in-house ML scoring's targeting model. The MRM committee has reviewed the feature's behavior across the pre-/post-handover boundary and confirms the feature does not produce systematic bias against members whose history is predominantly pre-handover. This finding is supported by the disparate-impact tests in the Q4 2025 fairness audit, sealed chain entries `dis-imp-2025q4-001` through `dis-imp-2025q4-016`. The institution acknowledges the compositional asymmetry as a known operational characteristic and reviews it quarterly.*

Dawn read the paragraph twice.

"That's a defensible disclosure," she said. "The institution names the asymmetry, the MRM committee has reviewed it, the supporting fairness-audit entries are referenced by ID, and the review cadence is named. It's the right shape. I would have written it differently — I'd have lead with the operational reality before the reassurance — but the substantive disclosure is complete."

Cal said, "That paragraph was added at the September 30 promotion review. The MRM committee wanted it explicit. The original draft just said 'the model uses prior engagement-history features' without the era distinction."

Dawn said, "Who pushed for the era distinction?"

Cal said, "Anwar Patel."

Dawn nodded. *He sees the linkage all the way to the model card,* she thought. *That's a CCO who reads the model cards.*

She wrote on her notepad: *Pre-handover feature compositional asymmetry disclosed in model card. Anwar Patel pushed for the era distinction at promotion review. Documented in fairness-audit entries dis-imp-2025q4-001..016.*

She underlined *era distinction in the model card.*

> ### ✓ Confirmation #7 — Pre-handover feature compositional asymmetry is disclosed in the model card and supported by sealed fairness-audit entries
>
> The 'prior offer engagement velocity' feature in the in-house ML scoring's feature set is computed across the full member marketing-event history, including events generated under the legacy Total Expert era. The model card's 'known limitations' section discloses the compositional asymmetry, names the MRM committee's review posture, and references the Q4 2025 fairness-audit entries by ID. The era distinction was added at the September 30 promotion review at the CCO's request. The disclosure is complete and the linkage from disclosure to supporting evidence is chain-anchored.

She kept pushing.

"What about a member who has only legacy-era history? Someone who was a member before the handover but did not engage with any post-handover marketing event before being scored?"

Cal said, "The feature's behavior on members with pre-handover-only history was specifically tested in the fairness audit. Slice `dis-imp-2025q4-009`. The slice tested members with at least twelve months of marketing engagement, all pre-handover, scored after the handover. The disparate-impact metric was within institutional tolerance. The MRM committee signed off."

Dawn said, "Pull `dis-imp-2025q4-009`."

Cal pulled it. The entry was sealed in October 2025, two weeks before the September 30 promotion event. The slice definition was precise: members with at least twelve months of marketing engagement all pre-handover, scored post-handover for the first time. Sample size: 47,238 members. Disparate-impact metric: 0.92 on the four-fifths rule's reference standard, within the institutional tolerance of 0.85. The slice was tested against the protected classes covered by ECOA — race, color, religion, national origin, sex, marital status, age, public-assistance income — with metrics for each. All within tolerance.

Dawn studied it for a minute.

"That's a real test," she said. "Specific slice, large sample, multiple protected classes, results within institutional tolerance. The MRM committee did the work."

Cal said, "Mei-Lin Tsai will walk you through the methodology tomorrow morning. She built that slice specifically because the cross-vendor handover compositional question was on the AIRES exam topic list."

Dawn looked up.

"AIRES topic list. Wait. NCUA published the AIRES topic list for this cycle?"

Cal said, "The cycle-opening communications referenced two emphasis areas — marketing-AI vendor governance, and member-data continuity across vendor handovers. The MRM committee built the disparate-impact slice library specifically to answer those emphasis areas. Mei-Lin will explain."

Dawn wrote: *AIRES topic list referenced marketing-AI vendor governance. MRM committee built the slice library in response. CC8.1 ties to topic list.*

She thought about it. *Foresight pattern: spec section ships before institutional need. Institutional response: MRM committee builds the slice library before the examiner asks.* The same shape at two layers. The spec and the institution were both moving on the same problem, in advance, without coordination.

She did not write that down. It was an observation that did not need to be in the engagement file.

---

## 🔍 4:30 PM — The CAE Question

David Reyes came down at 4:30 PM. The afternoon had wound to a natural stopping point. The team had walked the §10.21 cross-vendor anchor, the §10.11.1 ECOA prior-offer-to-decision linkage, the marketing-AI lineage from feature engineering through model card to disparate-impact testing, and the pre-handover feature compositional asymmetry. The next morning would walk §10.69 per-customer disclosure across the boundary.

David Reyes sat down. He did not pull out a folder this time.

"Dawn. If NCUA's lead supervisor asks me, three weeks from now, how the marketing AI changed across this transition — what can we prove?"

Dawn answered.

"The chain proves what changed and what didn't. The cross-vendor anchor binds the legacy model artifact, the legacy model card, the legacy lineage manifest, and the dual-signed handover ceremony to a single chain entry. The new model artifact, the new model card, and the new lineage manifest are bound on the receiver side of the same entry. From that entry forward, every model-call event under the new scoring carries the new model version and the new model card hash. Every model promotion lands as a sealed event with the model-artifact hash, the disparate-impact tests, and the MRM committee sign-off. Every credit decision that references a prior marketing offer binds the prior-offer hash under the per-event MAC. The chain is the workpaper.

"The verifier reproduces all of it. Byte-equality on the legacy 1.4-terabyte export reproduces in nine minutes. The cross-vendor handover dispatch path emits `cross_vendor_handover_verified` at exit code 0. The §10.11.1 dispatch path emits `prior_offer_linkage_resolved` on credit-decision entries. The §10.69 per-customer disclosure subtree — which we'll walk tomorrow — spans the handover boundary cleanly because the institution is single-tenant.

"What the chain does not prove: it does not prove the new scoring is fair under ECOA in a substantive disparate-impact sense. The disparate-impact tests are themselves chain entries, with the MRM committee sign-off, but the substantive fair-lending analysis is a separate program. The chain feeds it; the chain doesn't replace it. That's the §1.2 line.

"What I would say to NCUA's lead supervisor: the institution can walk an examiner through the deltas live. Five members in three hours, end-to-end traces, all the way from the legacy era through the handover into the post-handover era. The cross-vendor anchor preserves the lineage. The fair-lending analysis is anchored to the chain but is its own program.

"You can prove the change was tracked."

David Reyes nodded slowly. He had been writing in his folder during her answer.

"That is the answer I needed," he said. "I will quote it almost verbatim to the lead supervisor when she asks. With your permission."

Dawn said, "It is your institution's answer. I am just reading it back to you with the spec citations."

He smiled. "Verbatim with citations."

Tom wrote: *CAE quoted Dawn's answer almost verbatim. CAE preparing the institutional posture for NCUA's lead supervisor. Spec citations to be retained in the workpaper.*

David Reyes stood up. "I'm going to let your team close out the day. Karina mentioned the model-card review went cleanly. Anwar said the same about the ECOA walk. Cal will be on-call tomorrow morning at 8:30 for the §10.69 disclosure walk. Mei-Lin will join at 9:30 for the MRM-committee-side conversation."

He paused at the door.

"One more thing. I read your Northbridge report. The §10.16 connector-lag finding. I rewrote our runbooks before we started this engagement. I wanted to mention it because I assumed you'd notice if I hadn't."

Dawn said, "I noticed. I would have noticed if you hadn't."

"I know. That's why I said it."

He left.

Tom looked at Dawn.

"He read your report."

"He read every CAE report he could find. He's the third one this year."

"You should write more of them."

"I plan to."

She closed her laptop.

---

## 🌆 5:30 PM — Day-1 Debrief

The team gathered in the engagement room. David Reyes had left. The barbecue boxes were in the trash. Tom closed the door.

Dawn wrote on the whiteboard.

```
Day 1 — Tuesday
Gaps:           0
Partials:       0
Findings:       0
Nits:           0
Confirmations:  7
```

Under Confirmations, she wrote:

```
1. §10.21 cross-vendor anchor verifies end-to-end (byte-equality reconciliation 9:11)
2. Chain walks cleanly across the cross-vendor boundary (100k rows in 27s)
3. Cross-vendor service-account decommissioning fully chain-coupled
4. Model-promotion gates chain-coupled via §10.34
5. ECOA prior-offer-to-decision linkage clean across boundary via §10.11.1
6. Marketing-AI lineage fully chained
7. Pre-handover feature compositional asymmetry disclosed in model card
```

She turned around.

"Day 1. Confirmation walk. The §10.21 cross-vendor surface operates cleanly. The ECOA linkage is examinable. The marketing-AI lineage is fully chained. Anybody add anything?"

Raj said, "I want to go on record that the cross-vendor handover entry is the cleanest cross-vendor anchor I've seen in this corpus. Eberhardt-Lumière was bidirectional cross-anchor in a different shape — two chains composing at a boundary. Hill Country is the single-substrate, single-vendor-change version. The byte-equality on the 1.4-terabyte export in nine minutes is the demonstration I'm taking back to the office."

Elena said, "The marketing-AI lineage is the cleanest I've seen for a vendor handover. The legacy model card preserved via §10.21 + §10.19 anchor is the pattern I'm taking back."

Mike said, "The model-promotion gating workflow refusing to activate a model without a sealed promotion event is the pattern I'm taking back."

Diana said, "The cross-vendor service-account decommissioning with sub-30-minute window and dual approval is the pattern I'm taking back. The legacy IAM history backfilled via §10.19 + §10.42 is the unsung win."

Luis said, "Same. Plus the AWS CloudHSM `us-east-1` with `us-east-2` replicas — single substrate, but with intra-substrate resilience. I'd want to think about what cross-substrate looks like, but for AWS-only deployments, this is the reference shape."

Chen said, "The §10.40 single-substrate cross-vendor chain-merge anchor handles the legacy-era data preservation cleanly. The fact that the legacy era is still walkable from the chain — eleven months in, post-handover — is what I want to write down."

Tom said, "Anwar Patel pushing for the era distinction in the model card at the September 30 promotion review. That's a CCO doing the work. We should name that in the report."

Dawn said, "We'll name it. The disclosure paragraph in the model card is a defensible artifact. It belongs in the workpaper appendix."

She looked at the whiteboard.

"Tomorrow we walk §10.69 per-customer disclosure across the boundary. Then the AIRES workpaper composition. Then Thursday we deliver the memo. Anyone want to flag anything for tomorrow morning?"

Raj said, "I want to see the legacy-era entries side-by-side with the post-handover entries for the same member. The §10.69 disclosure should produce a unified per-member trail. I want to verify the trail spans the handover cleanly."

Dawn said, "That's the load-bearing walk for Day 2. Cal will have three §1033 disclosure requests ready in the morning. Real ones — disclosures the institution actually produced this year. We'll walk each one."

Tom said, "I'll have the AIRES workpaper template ready by lunch."

Dawn said, "Good. Let's eat dinner."

The team filed out. Raj stopped at the door.

"How many confirmations on a clean engagement?"

Dawn said, "Seven on Day 1. Probably six on Day 2. Maybe one more on Day 3 if Mei-Lin surfaces something on the MRM side."

"Total fourteen."

"Total fourteen."

Raj almost smiled.

"It's not a graveyard," he said.

"It's not a graveyard," Dawn agreed.

He turned and walked out.

---

## 🌅 8:30 AM Wednesday — §10.69 Per-Customer Disclosure Walk

Wednesday morning came on cooler than Tuesday — a front had come through overnight and Austin was hovering in the low sixties. Dawn walked into the engagement room with coffee and a half-eaten breakfast taco. The team was already settled. Cal was at the second screen. Tom was opening the AIRES workpaper template on a third monitor he had brought in from David Reyes's office overnight.

Dawn sat down.

"Cal. The three §1033 disclosure requests."

Cal pulled them up. Three real cases:

1. **Disclosure request `dr-2025-08-14-mem-h:b3f1e9a7`** — A member who exercised their §1033 personal financial data rights two weeks before the handover, requesting a complete record of every interaction the institution had recorded about them in the prior eighteen months. The disclosure spanned the legacy era only.

2. **Disclosure request `dr-2026-01-22-mem-h:c4e8b2d6`** — A member who exercised their §1033 rights three months after the handover, requesting a complete record of every interaction in the prior twenty-four months. The disclosure spans both eras.

3. **Disclosure request `dr-2026-04-09-mem-h:a7d1f5b9`** — A member who exercised their §1033 rights one month before the audit engagement, requesting a complete record of every interaction in the prior thirty-six months. The disclosure spans both eras with deep legacy-era history.

Dawn said, "Start with disclosure number two. That's the one that crosses the handover."

Cal pulled it up. The disclosure had been generated on January 22, 2026. The institution's §10.69 producer had walked the chain for `mem-h:c4e8b2d6`, gathered every entry that referenced the member's hashed ID across both the legacy mirror service-name and the new HubSpot + in-house ML service-name, applied the §10.22 redaction discipline for any PII bound under the chain, and produced a sealed disclosure packet.

The disclosure packet was itself a chain entry — `audit.disclosure.cfpb_1033_subset.produced` — that bound the disclosure's Merkle root, the disclosure's coverage window, the requesting party, the institution's response timestamp, and the redaction-policy version that governed the redaction. The packet referenced 9,432 chain entries spanning the prior twenty-four months. Across the handover, the entries split: 6,118 legacy-era entries (pre-2025-11-04) and 3,314 post-handover entries.

Cal said, "Let me run the verifier."

```
herald-verify --tenant=bcfcu-prod \
              --disclosure-id=dr-2026-01-22-mem-h:c4e8b2d6 \
              --subset-walk \
              --strict
```

The verifier ticked. After 14 seconds it produced output:

```
Status: PASS
Step: 12
Reason: chain integrity verified,
        disclosure subtree resolved against daily seals,
        per-customer key derivation verified,
        cross-vendor handover boundary spans cleanly
Markers:
  customer_disclosure_subtree_verified
  customer_disclosure_key_derivation_verified
  cross_vendor_handover_referenced
Elapsed: 14.3s
```

Cal said, "Fourteen seconds for 9,432 entries across 24 months spanning the handover boundary. The §10.69 dispatch path walks the subtree as a single coherent walk because the institution is single-tenant. The chain doesn't care that the marketing-AI vendor changed midway — the subtree is bound under one tenant-day Merkle seal across both eras."

Raj said, "Walk me through the subset proof. How does the verifier confirm that the disclosure packet contains every entry that should be in it, and only those entries?"

Cal said, "The §10.69 disclosure packet binds two Merkle roots. The first is the disclosure subtree itself — the Merkle root over the included entries. The second is a per-customer-key-derived inclusion proof against the full daily-seal Merkle tree. For each daily seal in the disclosure window, the disclosure packet includes the per-customer-key-derived inclusion proof showing that the entries claimed for the customer are exactly the entries in the daily seal that match the customer's hashed-ID HMAC under the per-customer key. The verifier validates both."

Mike said, "What's the per-customer key?"

Cal said, "Per-customer derivation under §10.69. Each member has a stable hashed ID that's derived from the member's GLBA-bound subject identifier via HKDF with the institution's per-tenant key and the subject identifier as the `info` parameter. The hashed ID is what's bound under the per-event MAC on every member-touching entry. At disclosure time the institution recomputes the hashed ID for the requesting member, walks the daily seals to find all entries bound to that hashed ID, and produces the inclusion proof. The verifier independently recomputes the hashed ID from the institution's published key derivation procedure and confirms the inclusion proof matches."

Mike wrote: *Per-customer key derivation under §10.69. Member subject ID -> hashed ID via HKDF. Hashed ID bound under per-event MAC. Disclosure walks via per-customer-key inclusion proof.*

He underlined *inclusion proof against daily-seal Merkle root.*

> ### ✓ Confirmation #8 — §10.69 per-customer disclosure subtree spans the cross-vendor boundary cleanly
>
> Disclosure request `dr-2026-01-22-mem-h:c4e8b2d6` produced a sealed disclosure packet covering 9,432 chain entries across 24 months — 6,118 legacy-era entries (pre-handover) and 3,314 post-handover entries. The §10.69 dispatch path walked the subtree in 14.3 seconds end-to-end. The verifier emitted `customer_disclosure_subtree_verified`, `customer_disclosure_key_derivation_verified`, and `cross_vendor_handover_referenced`. The subtree is bound under the tenant-day Merkle seal — Hill Country's single-tenant design means the legacy-era and post-handover entries are members of the same Merkle subtree, with the cross-vendor anchor binding the boundary. The per-customer key derivation under §10.69 produced an inclusion proof against the daily-seal Merkle root for every daily seal in the disclosure window. The disclosure packet itself is a sealed chain entry of `audit.disclosure.cfpb_1033_subset.produced` referencing the disclosure subtree's Merkle root.

Dawn said, "Run the verifier on the third disclosure. Three years of history."

Cal pulled `dr-2026-04-09-mem-h:a7d1f5b9`. The disclosure covered the prior 36 months. Sample size: 28,194 chain entries. The verifier ran for 41 seconds and returned PASS with the same markers.

She said, "Run the verifier on the first disclosure. The legacy-only one."

`dr-2025-08-14-mem-h:b3f1e9a7`. The disclosure covered the prior 18 months, all pre-handover. Sample size: 4,872 chain entries. The verifier ran for 9 seconds and returned PASS with `customer_disclosure_subtree_verified` and `customer_disclosure_key_derivation_verified`. The `cross_vendor_handover_referenced` marker was absent — the disclosure window did not span the handover, so the cross-vendor reference was not required.

Dawn said, "That's the property I needed. The marker is positively absent when the boundary isn't crossed. Not silently. The verifier emits the markers that apply and only those."

Cal said, "Section §10.12 verifier-marker discipline. Markers are positive declarations. A missing marker is not a silent failure — it's an explicit signal that the case doesn't apply."

Dawn wrote: *§10.12 verifier-marker discipline. Positive declarations. Cross-vendor reference marker is positively absent when boundary isn't crossed.*

She underlined *positively absent.*

Tom said, "That's the thing that makes the workpaper composable. The marker set on a disclosure tells the examiner what dispatch paths were exercised. The marker set says everything the verifier emitted; the absence of a marker says what wasn't triggered."

Raj said, "Show me the redaction discipline. The disclosure packet is going to a member. The member's own PII shouldn't be redacted from their own disclosure — but other members' PII bound under the same chain entries should be redacted. How does the producer handle that?"

Cal said, "§10.22 redaction discipline. The producer reads the chain entries, applies the redaction policy active at disclosure time, and produces the disclosure packet with the `redacted_per_§10.22` markers carried through. The redaction policy is itself chain-anchored — every policy change is a chain entry under `audit.policy.redaction.*`. The active version is named in the disclosure packet's metadata. The verifier confirms that the redaction-policy version on the disclosure packet matches a sealed policy entry, and that the redactions in the packet are consistent with the policy."

Dawn said, "Pull a disclosure packet with redactions visible."

Cal pulled one. The disclosure packet was for a member who had been included in a household-account joint-disclosure case — the member shared an account with another member, and some chain entries referenced both. The redacted disclosure showed the member's own data in clear, the joint-account other-member's PII redacted per §10.22 to `[redacted_per_§10.22:joint-account-other-party]`, and a structural reference indicating where redactions occurred and why.

Raj read it.

"That's a clean redaction posture. The redaction is structural — the disclosure preserves the shape of the entry while masking the specific data. The verifier validates that the redaction is consistent with the policy. The member can see what was redacted and why."

Cal said, "Per §10.22, the redaction is structurally visible. The redacted data is removed; the redaction marker is bound under the disclosure packet's MAC. A consumer challenging a redaction can do so by referencing the marker; the institution can produce the redaction-policy version that governed the redaction; the policy itself is chain-anchored; the audit trail is complete."

> ### ✓ Confirmation #9 — §10.22 redaction discipline is structurally visible and chain-anchored
>
> The §1033 disclosure packets apply the institution's active redaction policy at disclosure time. Redactions are structurally visible — the disclosure preserves the entry shape while masking specific data with `[redacted_per_§10.22:reason]` markers. The active redaction policy is named in the disclosure packet's metadata and is itself chain-anchored under `audit.policy.redaction.*`. Every policy change is a chain entry; the verifier confirms the redaction-policy version on the disclosure packet matches a sealed policy entry. Joint-account, household, and minor-related PII redactions are all handled under the same discipline. The redaction posture is auditable end-to-end.

The §10.69 walk took the rest of the morning. By 11:30 AM the team had walked all three disclosures end-to-end, verified the §10.69 subtree dispatch on each, validated the redaction discipline, and confirmed that the cross-vendor handover boundary was traversable in both directions.

Dawn closed her laptop halfway.

"That's the §10.69 confirmation. The disclosure subtree spans the handover cleanly. The redaction is structural. The §10.22 markers are bound under the disclosure packet's MAC. The single-tenant design pays off: one walk, one Merkle root, one signature, no cross-tenant complication."

Cal said, "Bonus point. The institution has produced 47 §1033 disclosure requests in the past year. All 47 verified under the §10.69 dispatch path. The average verification time was 19 seconds. The longest was 89 seconds for a 36-month disclosure spanning the handover with deep history. The pattern is operationally cheap."

Dawn wrote: *47 §1033 disclosures produced in past year. All 47 verified. Mean 19s. Max 89s. Pattern is operationally cheap.*

She underlined *operationally cheap.*

---

## 🧪 12:00 PM — Lunch with Mei-Lin

Mei-Lin Tsai came in at 12:00 PM for working lunch. She was the MRM committee chair — fifties, soft-spoken, PhD in statistics, formerly head of consumer-credit risk at a large regional bank. She had been at Hill Country for three years and chaired the MRM committee for two. She carried a laptop and a thin notebook with her name in gold lettering on the cover.

She sat down and opened the notebook. The page she opened to was annotated in Mei-Lin's careful handwriting with the four spec sections the engagement would touch on the MRM side: §10.21, §10.34, §10.40, §10.11.1. Each had a list of MRM committee actions taken in response.

"I read the morning's notes from David," she said. "You walked §10.21 yesterday and §10.69 this morning. You want my model-card walk this afternoon. Before we get there — let me give you the MRM committee's perspective on the cross-vendor handover, because there's one thing I want to be sure you have in your report."

Dawn said, "Go ahead."

Mei-Lin said, "The model-risk-management committee, on November 1, 2025 — three days before the handover — held a special session. We reviewed the legacy Total Expert model card, the new in-house ML model card, the cross-vendor handover plan, the disparate-impact tests on the new model against the legacy model's historical decision data, the fairness audit, and the institutional risk acceptance for the transition. The session produced a formal MRM committee resolution. The resolution is itself a chain entry — `audit.mrm.resolution.vendor_handover_approval`. The resolution references all the inputs by hash. It was signed by all five MRM committee members. It is part of the institutional record.

"I want to be sure the resolution is in your report's appendix. Not because I want credit. Because if an examiner reads the report, they should be able to walk from the cross-vendor handover entry back to the MRM committee's institutional acceptance of the transition. The chain holds the linkage. The verifier walks it. But the report should name it."

Dawn said, "Tom, that's in the appendix."

Tom wrote: *MRM committee resolution `audit.mrm.resolution.vendor_handover_approval`, November 1, 2025, in the report appendix. Linkage from handover entry to MRM acceptance.*

Mei-Lin nodded.

"Thank you. Now the model-card walk."

She walked Dawn and Elena through the model card for `bcfcu-ml-v1.0.2`. The card had eleven sections. Model purpose. Training-data summary. Feature inventory. Performance metrics across demographic slices. Known limitations. Deployment-environment requirements. Decommissioning policy. Compositional asymmetry section (the pre-handover feature discussion Anwar Patel had pushed for). Fairness-audit results. Model-card version history. References.

The card was a structured document. Every claim in it was hash-anchored to a chain entry. The training-data summary referenced the §10.20 training-data retention floor and the actual training corpus's hash. The feature inventory referenced every feature's documentation entry. The performance metrics referenced the validation runs that produced them. The fairness-audit section referenced the sixteen disparate-impact test entries. The decommissioning policy referenced the institutional MRM policy entry that governed model lifecycle.

Mei-Lin said, "The discipline I want to highlight is the linkage. The card itself is a one-page summary. Every claim in the card has a chain-anchored backing artifact. An auditor reading the card can walk from any claim to the underlying evidence. The card is not the evidence. The card is the index to the evidence."

Elena said, "That's the right discipline. The card is a summary; the evidence is in the chain."

Mei-Lin said, "The institutional value of the chain is that it makes the model card auditable. Before the chain, the model card was a static document. An auditor would read it and trust the institution's assertions. With the chain, the auditor can walk from the card to the evidence and verify. The MRM committee's institutional posture is that the model card is the index, the chain is the corpus, and the verifier is the procedure. Every model promotion follows this discipline."

Dawn wrote: *Model card = index. Chain = corpus. Verifier = procedure. MRM institutional posture.*

She underlined the three.

Mei-Lin paused.

"One more thing. The cross-vendor handover — November 4, 2025. I want to tell you what the MRM committee did on the day of the handover. We were all in the room when the dual-signature ceremony happened. The committee witnessed the ceremony. The witness attestation is itself a chain entry — `audit.mrm.attestation.vendor_handover_ceremony`. The attestation entry references the handover entry by ID. The handover entry, as you saw yesterday, is a chain entry with the §10.21 attribute family.

"The witness attestation is not required by spec. It is the institution's own discipline. The MRM committee, on a cross-vendor handover, witnesses the ceremony and produces a chained attestation that the committee was present and that the ceremony was conducted per the institutional procedure. The attestation is a thirteenth signature, conceptually, beyond the two §10.17 dual signatures. It's belt-and-suspenders.

"I want it in the report's appendix. Same reason as the November 1 resolution."

Dawn said, "It'll be in the appendix."

> ### ✓ Confirmation #10 — MRM committee discipline is fully chain-coupled
>
> The MRM committee at Hill Country maintains a chain-coupled model-risk posture across the full model lifecycle. The November 1, 2025 special-session resolution `audit.mrm.resolution.vendor_handover_approval` is sealed as a chain entry binding the legacy model card, new model card, disparate-impact tests, and the institutional risk-acceptance for the transition. The November 4, 2025 witness attestation `audit.mrm.attestation.vendor_handover_ceremony` is sealed as a chain entry binding the dual-signature ceremony and the MRM committee's institutional presence. The model card discipline — card-as-index, chain-as-corpus, verifier-as-procedure — is the institutional posture for every model promotion. Each quarterly promotion produces a fresh model-card entry, a fresh fairness-audit, and a fresh MRM committee resolution.

Mei-Lin stood up at 1:30 PM. She had been there for an hour and a half. She had not eaten the sandwich the team had set aside for her.

"I'm sorry. I should eat. The afternoon session is the AIRES workpaper composition. I'll be available by phone if you need anything from the MRM side. David has my line."

She left.

Dawn said, "She is the most precise CMRM I've met in two years. The discipline is operational. The chain-anchoring isn't theater — it's how the institution actually runs."

Elena said, "I want that pattern. The card-as-index, chain-as-corpus, verifier-as-procedure framing. I'm going to write it into my next engagement template."

Dawn said, "Put it in. Cite §10.34 and §10.20."

---

## 📊 2:00 PM — AIRES Workpaper Composition

Tom had the AIRES workpaper template open on the third monitor. He had been quietly assembling it through the morning. The template was an NCUA standard form — a multi-section document the lead supervisor would expect to see during the entrance meeting in three weeks.

He turned the monitor around so Dawn and the team could see it.

"AIRES Information Systems and Technology Officer Questionnaire — Section IV, Subsection 4.b. *Chain-of-Custody Controls.* This is the section that names the institution's chain-of-custody posture. I've drafted the institutional response. I want your eyes on it before we finalize."

Dawn read the draft. The response was four pages. The first page was the institutional posture statement — Hill Country runs TesseraSeal across the full member-experience surface, eleven months in production, AWS-resident, with the §10.21 cross-vendor model-handover surface exercised at the marketing-AI vendor transition. The second page was the spec-section confirmation list — §10.21, §10.40 (single-substrate form), §10.69, §10.11.1, §10.22, §10.34, §10.42, §10.13. The third page was the verifier-output appendix list — seven verifier outputs to be attached as supporting exhibits. The fourth page was the engagement-team identification and the contact list for the audit team and the institution.

Dawn said, "The institutional posture statement is well-written. The spec-section list is comprehensive. The verifier-output appendix is the right shape. I want to add one thing on the institutional posture page."

She wrote on a sticky note and handed it to Tom. The note said:

> The institution's §10.21 cross-vendor model-handover surface operates in single-substrate form (AWS-only). The chain composes across the marketing-AI vendor transition by hash-equality and signature-pair, with the §10.40 single-substrate cross-vendor chain-merge anchor providing the reconciliation. The institution acknowledges that the §10.40 cross-vendor anchor is exercised here in its single-substrate AWS-only form; the spec is silent on cross-substrate variants in v1.0b. The institution will participate in any working-group discussion of substrate-portability extensions to §10.40, should such extensions arise.

Tom read it.

"That's a careful sentence."

Dawn said, "It's an accurate sentence. The institution exercises §10.40 in the form that exists. The spec section is silent on what happens if the institution decided to run the chain across substrates. The acknowledgment is matter-of-fact."

Tom typed it into the workpaper. He read it back. Dawn nodded.

"That goes on the institutional posture page."

Tom said, "And the §10.21 confirmation — Hill Country is the first credit union in the corpus to exercise §10.21 in production. It's the first NCUA-supervised institution to exercise the cross-vendor anchor at all. Do we name that in the workpaper?"

Dawn paused.

"No. We name it in the spec-section confirmation memo to the institution, which goes to David's risk committee and the MRM committee. We do not name 'first credit union in the corpus' in the AIRES workpaper. The examiner doesn't need to know how the corpus is built. The examiner needs to know the institution exercises the section."

Tom said, "Right."

He revised. The workpaper named the section confirmation matter-of-factly. The institutional-reference language went into the institution-side memo, not the regulator-side workpaper.

The workpaper composition took the rest of the afternoon. By 4:30 PM the document was substantially complete. Tom had the institutional posture, the spec-section confirmations, the verifier-output appendix list, the AIRES citation cross-references (§10.13 evidentiary artifacts compose with the AIRES workpaper model — the spec section is the bridge between the chain artifacts and the NCUA's standard examination practice), the engagement-team identification, and the institution-side contact list. He had cross-references to the working-group's spec repository, the verifier's GitHub Releases page with the Cosign-signed binaries, and the FFIEC chain-of-custody v1.0b spec document.

Dawn read the final draft twice. She made two small wording changes. She approved it.

"Tom. This is the cleanest AIRES workpaper I've seen. The cross-references are right. The institutional posture is matter-of-fact. The spec-section confirmations are scoped. The verifier-output appendix is the institutional record."

Tom said, "Thank you. I'll have it sent to David by tomorrow noon. He'll review and add the institutional signatures. The lead supervisor sees it before the entrance meeting."

He saved the document.

---

## 🛡️ 4:30 PM — The Reconciliation Test

Dawn wanted to do the reconciliation test herself. She always did. It was her signature on every engagement. She had been doing the same shape of test for nine years and it was where most systems folded.

"Cal. Pick me a sample window. Three thousand member-touching events across the prior year. Random sample. All event classes. Both sides of the handover."

Cal pulled the sample. Three thousand entries.

Dawn ran the operational-system view of the same three thousand events. The view came from the HubSpot CRM, the in-house ML scoring layer's prediction log, the contact center's transcription archive, the core-banking API edges, the wealth-advisor pilot's interaction log, the loan-decisioning workflow, the marketing-CRM mirror, and the IAM event stream.

She diffed the operational view against the chain view.

Zero.

Not "zero meaningful." Zero. Every event in the operational view had a sealed chain entry. Every sealed chain entry had a corresponding operational event. Timestamps matched within the documented capture latency (the §10.16 freshness invariant — median 12 seconds, 95th-percentile SLO 90 seconds). Payloads matched byte-for-byte after JCS canonicalization. The cross-vendor handover entries appeared in both views, named identically.

She ran the diff again with a different sample. Five thousand events this time, randomly selected from the cutover window — the seventy-two hours bracketing November 4, 2025, when the handover happened.

Zero — once the six late-binding entries from the legacy mirror were accounted for. The late-bindings were in both views, labeled `late_binding=true` in the chain, labeled with the cutover-anomaly tag in the operational view.

She ran a third diff with a sample from the day of the auto-loan refinance case — November 14, 2025. A small window: just the 1,247 events that fell on that day for the institution.

Zero.

She ran a fourth diff. This one she didn't tell the team about. She picked a window of seventy-two hours bracketing the September 30, 2025 model promotion event — when the new in-house ML scoring layer was promoted to production. The window covered the last day of legacy scoring, the day of the promotion ceremony, and the first day of new scoring.

Zero.

*The system runs invariant across the model promotion,* she thought. *The vendor changes; the chain doesn't notice except at the explicit handover entries.*

She looked up at Cal.

"What was your false-positive rate during the prior-year cycle?"

"On the chain side, zero. On the operational side, we had four near-misses where the HubSpot CDC connector and the chain disagreed momentarily during the connector lag window. All four reconciled within minutes. All four reconciliations are in the chain."

"Did you tell the prior-cycle examiner?"

"I told the prior-cycle examiner. She closed the cycle on time. The four near-misses are in last year's workpaper as a documented operational characteristic, not a finding."

Dawn wrote: *Four prior-cycle near-misses, all reconciled within minutes, all chained. Prior-cycle examiner accepted. Documented as operational characteristic.*

> ### ✓ Confirmation #11 — Operational and chain views reconcile to zero across four independent samples
>
> Three independent samples (3,000 random across prior year, 5,000 across the 72-hour cutover window, 1,247 from the November 14 auto-loan refinance day) reconciled byte-for-byte between the operational system view and the chain. A fourth sample, undeclared at run-time, bracketed the September 30 model promotion — same result. Latency offsets were within the §10.16 freshness invariant. Late-binding entries from the cutover window were visible and traceable in both views. Cross-vendor handover entries appeared identically in both views. The reconciliation posture is byte-equal across the cross-vendor boundary.

Dawn put her pen down. She had one more thing to do before the day closed.

She picked the legacy 1.4-terabyte Total Expert export — the one Cal had reconciled byte-equal in nine minutes the day before. She ran the §10.40 reconciliation tool a second time, on her own laptop, with read-only credentials scoped to the S3 cold-tier and the chain entry.

```
herald-verify-handover --run-id=marketing-ai-handover-2025-11 \
                       --reconcile-legacy-export \
                       --strict
```

The terminal ticked through stages. After nine minutes and seven seconds — four seconds faster than Cal's run, probably because the cold-tier prefetch was warm — the output completed:

```
Status: PASS
Step: 12
Reason: chain integrity verified,
        legacy export byte-equality reconciled against
        audit.model_handover.legacy_export_artifact_sha256,
        cross-vendor handover dual signatures verified
Cross-vendor markers:
  cross_vendor_handover_verified
  legacy_export_byte_equal
Elapsed: 9m07s
```

She read the output twice.

*Nine minutes seven seconds,* she thought. *On a 1.4-terabyte legacy export, against a chain entry from twenty-three weeks ago, signed by Total Expert's CTO and Hill Country's CTO under the §10.17 dual-signature pair, with the §10.40 single-substrate chain-merge anchor. Byte-equality. Repeatable.*

She closed her laptop halfway.

Then she opened her notepad and turned to a fresh page. She wrote, in her ordinary handwriting, with no underline and no marker:

> *§10.40 anchor reads as routine on AWS-only. Open question for the next pass: what happens when the substrate moves?*

She read what she had written. She thought about it for a moment. The question was not actionable. It was not a finding. The institution operated on a single substrate. The spec section worked on a single substrate. The combination read as routine.

But the question had been sitting at the back of her notebook since the morning of Day 1, when Cal had run the byte-equality reconciliation the first time. She had been waiting to write it down until she was sure it was a real question and not just an audit-team thought.

She had run the byte-equality twice now. Once with Cal driving. Once on her own laptop. Both times the reconciliation closed in under ten minutes against a 1.4-terabyte legacy export. The mechanism worked. The §10.40 single-substrate anchor was the canonical-reference shape for the spec section.

*Works on one substrate,* she thought. *What happens when the substrate moves?*

She did not know the answer. She suspected the spec working group did not know the answer either. The clause's published form covered the case Hill Country ran. The case where the substrate itself crossed clouds — AWS to Azure, AWS to GCP, on-prem to AWS — was not covered by §10.40 v1.0b. It might be covered by a future revision. It might not.

She underlined the note. Just one underline, under the word *substrate.*

She wrote, beneath the question:

> *Filed in engagement file. Not a finding. Not a Nit. Wishlist seed for the next working-group review cycle.*

She closed the notepad.

She did not mention the note to the team. The note was not for the team. The note was for the file. The file would sit. If the question became actionable in a future engagement, the note would be there. If it didn't, the note would still be there.

She thought, briefly, about whether to mention it to Tom. The disclosure she had made at lunch on Tuesday — that she had a prior professional relationship with the spec author of the §10.21 family — was already in the engagement file. Mentioning the substrate-portability note would be a separate matter. The note was an observation about the spec section's published form, not a communication about the spec author. The two were orthogonal.

She decided to mention it to Tom anyway. He was the IA liaison. He kept the engagement file. If the note was going in, he should know.

She caught his eye.

"Tom. One engagement-file note. For the file. Not for the workpaper, not for the institutional memo. Engagement-file only."

He came over.

She showed him the page.

He read it.

"That's an observation, not a finding."

"That's an observation, not a finding. The institution operates on a single substrate. The spec section works on a single substrate. The §10.40 anchor reads as routine. The open question is what happens when the substrate moves — across clouds. It is not actionable at this engagement. It may be actionable at a future engagement. Or it may resolve itself in a future spec revision."

Tom said, "Engagement-file note. Logged."

He wrote in his own notebook: *Engagement-file note, lead auditor's hand, 4:45 PM Wednesday. Observation: §10.40 single-substrate cross-vendor anchor reads as routine on AWS-only; open question on cross-substrate behavior. Not a finding. Not a Nit. Wishlist seed for next working-group review cycle. Witnessed by Tom Burke, IA liaison.*

Dawn nodded.

"Thank you."

She thought, for a beat: *Eleven months ago at Northbridge I wrote it never is on my notepad and crossed it out by IAM-review time. Today I wrote a question I don't have an answer for. It's a different kind of note.*

She put her notepad back in her bag.

---

## 🌆 5:30 PM — Day-2 Debrief

The team gathered in the engagement room. David Reyes had stepped out. Tom closed the door. Dawn wrote on the whiteboard.

```
Day 2 — Wednesday
Gaps:           0
Partials:       0
Findings:       0
Nits:           0
Confirmations:  4
Engagement-file notes: 1 (substrate-portability observation, lead auditor)
```

Under Confirmations she added:

```
8.  §10.69 per-customer disclosure spans the cross-vendor boundary cleanly
9.  §10.22 redaction discipline structurally visible and chain-anchored
10. MRM committee discipline is fully chain-coupled (Nov 1 resolution + Nov 4 attestation)
11. Operational and chain views reconcile to zero across 4 samples
```

She turned around.

"Day 2. The §10.69 walk went clean. The redaction discipline is structural. The MRM-committee chain-coupling is the cleanest I've seen. The reconciliation test reconciled to zero on four independent samples including the cutover-window sample and the model-promotion-window sample. We're at eleven confirmations on the engagement so far."

Raj said, "The §10.69 dispatch path in 14 seconds for 9,432 entries spanning the handover. That's the demonstration."

Elena said, "The card-as-index, chain-as-corpus, verifier-as-procedure framing. That's the pattern."

Mike said, "The §10.12 verifier-marker discipline — markers as positive declarations, absence as explicit signal — that's the part I'm taking back."

Diana said, "The MRM committee witnessing the dual-signature ceremony as an additional sealed attestation. That's belt-and-suspenders. I'd want every institution doing cross-vendor work to consider that pattern."

Luis said, "The chain reading invariant across the model promotion. That's the thing I want to write into my benchmarks."

Chen said, "The single-tenant design pays off in §10.69. I want that in my notes for the next cross-vendor engagement."

Tom said, "Eleven confirmations. Zero gaps. AIRES workpaper drafted. The institution is in good shape for the AIRES exam in three weeks."

Dawn said, "Tomorrow we finalize the spec-section confirmation memo for David's risk committee, the MRM memo for Mei-Lin's committee, the AIRES workpaper handoff to David, and the close-out. Anyone want to flag anything?"

Nobody did.

She capped her marker.

"Let's eat dinner."

The team filed out. Tom hung back for a moment.

"Dawn."

"Mm."

"The engagement-file note. Were you going to mention it at the close-out, or just file it?"

She thought about it.

"File it. The note is for the file. It is not a finding the institution needs to remediate. It is not a recommendation for the institution's program. It is an observation about the spec section's published form. The next pass will know whether the question is actionable."

Tom said, "Understood. Filed."

He left.

Dawn stayed in the engagement room for another five minutes alone. She looked out the window at the Texas hill country. The sun was setting behind the cedar-covered ridges to the west. The parking lot was emptying out as the day shift rolled home.

*The §10.40 anchor reads as routine on AWS-only,* she thought. *What happens when the substrate moves?*

She did not know.

She would not know for some time.

She closed her laptop, picked up her bag, and walked out.

---

## 🌅 8:30 AM Thursday — The Spec-Section Confirmation Memo

Thursday morning the team gathered for the memo composition. The AIRES workpaper was done. The §10.69 walk was confirmed. The reconciliation test was done. The MRM-committee discipline was documented. The engagement-file note was filed.

The remaining work was the spec-section confirmation memo — the institutional document that would go to David Reyes's board risk committee, to the MRM committee chair, to the CMO and the CCO, and (verbatim) to the NCUA AIRES lead supervisor as an attachment to the AIRES workpaper.

Dawn wrote it herself, on the conference room's projector screen, with the team watching and offering line-edits.

```
BISHOP CRESCENT FEDERAL CREDIT UNION
SPEC-SECTION CONFIRMATION MEMO — TesseraSeal Pre-Engagement Readiness
Engagement window: Tuesday-Thursday, [date]
Engagement team: [audit firm], lead auditor Dawn, IA liaison Tom Burke
NCUA AIRES exam: opens three weeks from engagement close
CFPB §1033 cross-cut: in scope as cross-vendor disclosure span
ECOA / Reg B cross-cut: in scope as marketing-to-credit-decision linkage

SUMMARY
-------
The institution operates TesseraSeal in production for 11 months across the
full member-experience surface. AWS-resident; Herald.Enterprise.Aws on us-east-1
with replicas in us-east-2. Daily Merkle seals signed by AWS CloudHSM under
FIPS 140-2 Level 3+ custody. Spec conformance: FFIEC chain-of-custody v1.0b.

The institution exercises the §10.21 cross-vendor model-handover surface
in production since the marketing-AI vendor handover (Total Expert ->
HubSpot Marketing Hub + in-house ML scoring) on 2025-11-04. The §10.21
surface has been in production for 23 weeks at engagement open.

The §10.21 cross-vendor anchor was placed at handover initiation, not
retrofitted. The Herald release shipping §10.21 dropped 7 months prior
to the handover. The institution was live on the spec section the day
it went into production.

This memo confirms the operational fidelity of the institution's exercise
of the relevant spec sections.

SECTIONS CONFIRMED
------------------
§10.21  Cross-vendor model-handover, in production for 23 weeks, dual-signature
        pair §10.17 attested, byte-equality of legacy export 1.4-TB reconciles
        in 9 minutes 11 seconds end-to-end. Verifier emits
        `cross_vendor_handover_verified` marker per §10.12.

§10.40  Single-substrate cross-vendor chain-merge anchor. Reconciliation
        path: SHA-256 of legacy export anchored at handover, byte-equality
        verified end-to-end at audit time. The institution acknowledges the
        single-substrate AWS-only form is the spec section's canonical
        reference shape in v1.0b; the institution will participate in any
        working-group discussion of substrate-portability extensions.

§10.69  Per-customer audit-trail subset disclosure. Spans the cross-vendor
        boundary cleanly. 47 §1033 disclosure requests produced in the past
        year; all 47 verified under the §10.69 dispatch path with mean
        verification time 19 seconds, maximum 89 seconds for 36-month
        disclosure with deep history. Verifier emits
        `customer_disclosure_subtree_verified` and
        `customer_disclosure_key_derivation_verified` markers per §10.12.

§10.11.1  ECOA adverse-action linkage with prior-offer-to-decision parent-
        linkage. Five member-traces walked end-to-end including the auto-
        loan refinance case spanning the handover. Verifier emits
        `ecoa_adverse_action_dispatched`, `prior_offer_linkage_resolved`,
        and `cross_vendor_handover_referenced` markers per §10.12.

§10.22  Redaction discipline structurally visible. Redaction-policy
        version chain-anchored. `redacted_per_§10.22:<reason>` markers
        carried through disclosure packets.

§10.13  Evidentiary artifacts compose with the NCUA AIRES workpaper
        model. Spec-section citations + verifier outputs cross-referenced
        in the AIRES workpaper Section IV, Subsection 4.b.

§10.34  Training-phase integrity. Model promotions land as sealed
        `audit.model_promotion.*` entries. Production deployment workflow
        refuses to activate any model whose artifact hash does not
        reference a sealed promotion event. Quarterly MRM committee
        review chain-anchored.

§10.42  Backfill-seal discipline. At handover, Total Expert's final
        backfill seal was received and is on the institution's side under
        AWS S3 cold-tier with compliance-mode object lock. The
        provider-side chain history is preserved should Total Expert's
        infrastructure go dark.

§10.17  Partition-ceremony attestation. Dual-signature pair (Total
        Expert CTO + Hill Country CTO) bound into the handover seal.
        MRM committee additional attestation `audit.mrm.attestation.
        vendor_handover_ceremony` bound as a separate sealed entry.

§1.2 EPISTEMIC SCOPE (cover memo language)
-------------------------------------------
The chain proves what the institution recorded at a given time and that
the record was not tampered after capture. The chain does NOT prove the
underwriting model's substantive credit judgment was correct, that any
particular credit decision was free of disparate-impact effects, or that
the institution's policy is fair under ECOA in a substantive sense. The
chain feeds the institution's fair-lending analysis program; the chain
does not replace it. Witness testimony based on chain output should
remain on the integrity foundation and not be drawn onto the truth
foundation in cross-examination.

ENGAGEMENT FILE NOTES
---------------------
- The lead auditor disclosed a prior professional relationship with the
  spec author of the §10.21 schema family at 12:35 PM on Tuesday of the
  engagement. The author is not present at the engagement, is not
  consulted, and has no involvement. The spec sections exercised are
  publicly shipped, publicly versioned, and the verifier is open source.
  Logged by Tom Burke, IA liaison.

- An engagement-file observation was filed at 4:45 PM Wednesday by the
  lead auditor: the §10.40 single-substrate cross-vendor anchor reads as
  routine in its AWS-only form. The institution operates on a single
  substrate; the spec section's canonical reference shape is single-
  substrate. The lead auditor noted an open question about cross-
  substrate behavior. This is not a finding. This is not a Nit. This is
  a wishlist seed for the next working-group review cycle.

NO FINDINGS
-----------
No Gaps. No Partials. No Findings. No Nits.

ENGAGEMENT BUDGET
-----------------
22% under budget.

ATTACHMENTS
-----------
Appendix A — Verifier output catalog (seven outputs)
Appendix B — Cross-vendor handover entry (full JSON)
Appendix C — Sample ECOA adverse-action case trace (mem-h:7a4e9c2f)
Appendix D — §1033 disclosure samples (three cases)
Appendix E — MRM committee resolution (Nov 1, 2025) and attestation (Nov 4, 2025)
Appendix F — Engagement team identification + contact list

Submitted by [audit firm]
Lead auditor: Dawn
IA liaison: Tom Burke
```

The team read the memo. Each member added one line-edit. Raj wanted the byte-equality time on the §10.21 confirmation line to be more precise ("9 minutes 11 seconds end-to-end" instead of "approximately 9 minutes"). Elena wanted the §10.22 redaction-policy chain-anchoring named explicitly. Mike wanted the §10.69 verifier-marker discipline cross-referenced to §10.12. Diana wanted the cross-vendor service-account decommissioning posture included as a footnote.

Dawn made all four edits.

She read the memo one more time. Tom read it. The team read it.

It read clean.

She saved it.

---

## 🤝 10:00 AM — The Close-Out

David Reyes came down at 10:00 AM. He was wearing the same pressed shirt as Tuesday, possibly a different one with the same cut. He carried his folder. He sat down.

"Dawn. The memo."

She handed him a printed copy. Eleven pages. Six appendices. Three signature lines on the back page.

He read it.

He read it slowly. He did not flip pages quickly. He read the §1.2 epistemic-scope paragraph twice. He read the engagement-file notes twice. He read the spec-section confirmations one at a time, with his finger tracing the margins.

When he was done, he set the folder down.

"This is the memo."

Dawn said, "This is the memo."

"You disclosed the prior professional relationship with the §10.21 spec author."

"I disclosed it at lunch on Tuesday. Tom logged it. It is on page nine of the memo."

David Reyes said, "Thank you. I would have written it the same way."

He turned to the next-to-last page.

"And the engagement-file observation on substrate-portability."

Dawn said, "An observation, not a finding. The §10.40 single-substrate anchor reads as routine on AWS-only. The open question is what happens when the substrate moves. I noted it in the engagement file because if it becomes actionable in a future engagement — a future spec revision, a future institution running cross-substrate — the note is there. The institution has nothing to remediate."

David Reyes said, "The institution has nothing to remediate. I want that part in the cover memo to the AIRES lead supervisor."

"It will be."

He signed the memo. Page eleven, signature line one. He passed the folder back to Dawn.

She signed page eleven, signature line two.

Tom signed page eleven, signature line three.

She handed the folder back to David Reyes.

He said, "Karina and Anwar will sign their copies this afternoon. Mei-Lin will sign hers. The AIRES workpaper goes to the lead supervisor on Friday afternoon. The risk committee sees the memo verbatim on Tuesday."

Dawn said, "Tom has the workpaper for you by noon today, with the institutional posture page updated to include the single-substrate acknowledgment we added yesterday."

"Good."

David Reyes paused. He had one more thing.

"You walked the cross-vendor anchor cleanly. The institution is in good shape for AIRES. I want to ask you something off-the-record. Not for the memo."

Dawn said, "Go ahead."

"The substrate-portability observation. You don't know the answer."

"I don't know the answer."

"Does anyone?"

She thought about it.

"The working group, when v1.0b shipped, named §10.40 as the single-substrate cross-vendor chain-merge anchor. The clause's published form covers single-substrate. The spec is silent on cross-substrate. If you asked me 'does the spec working group know the answer to cross-substrate,' my honest read is — they have not surfaced a cross-substrate variant publicly. Whether they have the answer privately, I cannot say. The spec sections that ship are the spec sections that ship."

David Reyes nodded.

"Off-the-record question. On-the-record answer."

He closed the folder.

"Thank you for the engagement, Dawn. The memo is the institutional record. We'll have the AIRES exam in three weeks. If anything surfaces during the exam that the spec doesn't cover, we will surface it to the working group. If the substrate-portability question becomes actionable in a future engagement — yours, mine, or someone else's — the note in your file is where it begins."

Dawn said, "That is the right shape."

He stood. He shook her hand.

"Safe travels back to wherever you came from."

"Thank you, David. Good luck with the AIRES exam."

He left.

---

## 🧾 11:00 AM — Auditor Debrief

The team packed up. The engagement room emptied gradually. Tom was the last to leave, carrying the AIRES workpaper draft and the engagement-file folder. Dawn was at the window, finishing her coffee.

Raj came back into the room. He had forgotten his charger.

"Two coffees," he said.

Dawn looked at him.

"What?"

"At Northbridge. You owed me two coffees because I said you'd find a Gap by lunch and you didn't. I never collected."

Dawn said, "Three engagements ago. You're collecting now?"

"I'm not collecting. I'm noting that you owe me. The collection is the point I bring it up. Today I am bringing it up because we just closed an engagement with eleven confirmations, zero findings, twenty-two percent under budget. That's the second one this year that closed under budget. The first was Northbridge eleven months ago."

Dawn said, "And the difference between them is —"

Raj said, "The difference is at Northbridge we did not know what we were going to find. Today we knew. Today we walked the §10.21 surface as a confirmation. Today the institution had read your Northbridge report and remediated the §10.16 connector-lag wording before we walked in. Today the spec sections we confirmed had been on the institution's compliance posture before we showed up. The day was a different day."

Dawn said, "Yes."

"That is the pattern Tom keeps writing in his notebook. 'Foresight pattern.' I read his notebook over his shoulder at lunch. He writes it down every time."

Dawn said, "Tom is allowed to write what he wants in his notebook."

"He is. I am noting that the pattern is no longer surprising. We have walked it now at — what, three engagements this year? Saraswati was edge-AI conformance under §10.32-§10.38. Eberhardt-Lumière was cross-vendor bidirectional under §10.21 in a different shape. Hill Country is single-substrate cross-vendor under §10.21 + §10.40."

Dawn said, "Different shapes of the same pattern. The spec ships sections before institutions need them. Institutions exercise them at the moment they need them. The audit confirms operational fidelity. The pattern is the operational reading of the spec working group's discipline."

Raj said, "And you don't get to write 'It never is' in your notepad anymore."

She thought about that.

"I still write it. I just cross it out faster."

He almost smiled.

He picked up his charger. He turned to leave.

"Dawn."

"Mm."

"The substrate-portability note."

She paused.

He had not been in the room when she filed the note. He had not seen Tom write it down. He could not have known about it from any of the team conversations on Day 2.

She said, "How did you hear about it?"

He said, "Tom mentioned it in passing this morning when he was getting coffee. He said you had filed an engagement-file note that wasn't a finding. He didn't say what it was. I asked. He said it was an observation about the §10.40 anchor on single-substrate. I figured out the rest."

She said, "You figured out the rest."

"You ran the byte-equality reconcile twice. Once Cal drove. Once you drove. Same result, four seconds apart. That's a person testing whether the result holds when they're the operator. Then you filed an engagement-file note. The only reason to file an engagement-file note after a clean reconcile is that you have a question the reconcile didn't answer. The reconcile answers the question 'does the §10.40 anchor work on a single substrate.' It doesn't answer the question 'does it work across substrates.' That's the question you filed."

She looked at him for a long moment.

"You're getting better at this."

"I've been doing it for nine years."

She said, "Don't write it down anywhere outside the engagement file."

"I won't. Tom and I are the only ones who know. Tom because he logged it. Me because I figured it out."

She nodded slowly.

"And the answer," he said. "When the answer comes — and it will, in a future engagement, or in a future spec revision — I want to be in the room when you get it."

She said, "If I'm in the room when the answer comes, I'll make sure you're there."

He nodded. He walked out.

She stood at the window for another minute.

The parking lot below was almost empty. The Texas hill country stretched west, all cedar and limestone. The sun was high enough to take the edge off the morning cool but not yet hot enough to bake the asphalt. A Hill Country pickup was pulling out of the visitor lot with a couple of teller-trainee badges hanging from the rearview mirror.

*The §10.40 anchor reads as routine on AWS-only,* she thought.

*What happens when the substrate moves?*

She did not know.

She would not know for some time.

But she had filed the note. The note was in the file. The file would sit. If the question became actionable in a future engagement, the note would be there. If it didn't, the note would still be there.

She put her notepad in her bag. She put her laptop in its sleeve. She picked up her coffee cup and dropped it in the recycling bin by the door.

She walked out.

---

## ❌ What They Expected vs ✅ What They Found

**❌ What They Expected (based on a cross-vendor handover under NCUA pressure, with an AIRES exam three weeks out):**

- The cross-vendor handover would have a seam — somewhere the legacy data and the new data didn't quite line up.
- The §10.21 attribute family would be partial or institution-specific, with vendor extensions that the spec hadn't normated.
- The byte-equality reconciliation against the 1.4-terabyte legacy export would either fail or take hours.
- The §10.69 per-customer disclosure would not span the boundary cleanly — disclosure requests crossing the handover would surface gaps.
- The ECOA marketing-to-credit-decision linkage would be either undocumented or institution-side without chain coupling.
- The model-card discipline for the new in-house ML scoring would lag the production deployment by a quarter.
- The MRM committee would have approved the handover by email, not by chain entry.
- The CAE would be carrying anxiety about the vendor-handover boundary that the audit could only partially answer.
- The institution would be in the middle of its first cross-vendor handover and would be improvising.

**✅ What They Found:**

- The §10.21 cross-vendor handover entry verified end-to-end with `cross_vendor_handover_verified` marker per §10.12.
- The §10.21 attribute family was fully normated in v1.0b of the spec. Hill Country used the standard family with no institution-specific extensions.
- The byte-equality reconciliation against the 1.4-terabyte legacy Total Expert export reproduced in 9 minutes 11 seconds end-to-end under §10.40 single-substrate cross-vendor chain-merge anchor. Repeatable in 9 minutes 7 seconds on the lead auditor's laptop with read-only credentials.
- The §10.69 per-customer disclosure spanned the handover boundary cleanly because the institution is single-tenant. 47 §1033 disclosure requests in the prior year, all 47 verified, mean verification 19 seconds, max 89 seconds.
- The ECOA marketing-to-credit-decision linkage was chain-coupled via §10.11.1 `prior_offer_run_id` / `prior_offer_seq` parent-linkage. The auto-loan refinance case walked end-to-end from the November 14, 2025 credit decision through the November 14 marketing offer back to the February 4, 2025 legacy-era pre-qualification offer.
- The model-card discipline for the new in-house ML scoring led the production deployment by six weeks. The model card included an explicit "Pre-handover feature compositional asymmetry" disclosure section, pushed for by the CCO at the September 30 promotion review.
- The MRM committee had approved the handover by a sealed chain entry (`audit.mrm.resolution.vendor_handover_approval`, November 1, 2025) and witnessed the dual-signature ceremony with a separate sealed attestation (`audit.mrm.attestation.vendor_handover_ceremony`, November 4, 2025).
- The CAE was not carrying anxiety. He was carrying questions that the audit answered cleanly. He had read the engagement team's prior Northbridge report and had remediated the §10.16 connector-lag runbook wording before the engagement opened.
- The institution had completed its first cross-vendor handover 23 weeks before the engagement. The §10.21 surface had been in production since handover initiation. Nothing was improvised. Everything was a confirmation.

---

## 🧾 Final Assessment Theme

> "The institution can show what changed across the vendor handover, what didn't, and how the chain composed the legacy era and the new era under one tenant Merkle seal. The cross-vendor anchor operates cleanly on a single substrate. What happens when the substrate moves is the next pass's question — filed quietly in the engagement file, not as a finding, because today the institution exercises the spec section in the form the spec section ships."
