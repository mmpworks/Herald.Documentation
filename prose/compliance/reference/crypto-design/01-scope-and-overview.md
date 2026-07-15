# Plain-English: §0–§3 — orientation, scope, definitions

Covers the spec's front matter: version policy, how to read the document, scope statements, definitions. None of these sections describe the cryptographic primitives directly — they orient the reader and establish the vocabulary.

---

## §0 Version policy (informative)

**What it says.** This is a Public Review Draft. The version-numbering scheme uses MAJOR.MINOR.PATCH. Drafts are versioned with date stamps; finalized versions remove the date stamp and the version number is locked.

**Why it exists.** Standards documents go through many revisions. Implementers need to know which revision they're conforming to. The version policy makes that explicit so an implementation can say "we conform to v1.0b" and a reviewer can find exactly that text.

**Common reader questions:**
- *"Is this final?"* — No. (Public Review Draft 1) is feedback-stage. v1.0 final lock comes after public comment.
- *"Will the wire format change after public comment?"* — Possibly. Big changes are tracked in §12 Change log.

---

## §0.5 How to read this document (informative)

**What it says.** Five sub-sections that orient different audiences:
- **§0.5.1 The chain in three paragraphs** — the elevator pitch (HMAC chain at capture, daily Merkle seal, HSM-rooted root signature, OpenTelemetry-native wire).
- **§0.5.2 The chain at a glance** — a compact diagram of the four primitives.
- **§0.5.3 Reading paths by role** — examiners read these sections; implementers read those.
- **§0.5.4 If you only have five minutes** — emergency executive summary.
- **§0.5.5 What sits outside the spec** — what the chain DOESN'T cover (the runtime, the model, the policy library, etc.).

**Why it exists.** The spec is long (~3000+ lines). Different readers need different entry points. §0.5 is wayfinding — it tells each audience where to start.

**How to use it.** Pick the role closest to yours and follow the reading path. Don't try to read straight through cover to cover unless you're an implementer or a security reviewer.

---

## §0.6 Navigation and contextual-help URL convention (normative)

**What it says.** The spec is paired with a *companion repo* (currently the TesseraSeal repo per recent architecture decisions; originally framed as a "plain-spoken companion" repo). The companion holds operational context, examiner stories, and contextual help that the spec text itself doesn't carry. §0.6 normates the URL convention that links spec sections to companion content.

**Why it exists.** The spec is the standardization artifact — vendor-neutral, terse, normative-form. The companion is the operational layer — vendor-positioned, narrative, pedagogical. Keeping them in separate repos means the standardization submission stays clean while the operational layer can be opinionated. §0.6 is the bridge.

**Common reader questions:**
- *"Do I have to read the companion?"* — No. Companion content is informational. Verifiers conform to §7 + the test vectors alone.
- *"What if a companion link is broken?"* — The verifier doesn't check companion URLs. They're for human readers, not the verification path.

---

## §1 Scope

**What it says.** This spec defines a chain-of-custody primitive set for capturing AI-driven decisions in regulated systems. The primitives satisfy:
- FFIEC IT Examination Handbook integrity-of-logging requirements
- SR 11-7 / OCC Bulletin 2011-12 model-risk-management guidance (the 2011 framework)
- OCC Bulletin 2026-13 and counterpart Federal Reserve / FDIC issuances (the 2026 consolidated update)

The primitives are language-neutral, transport-agnostic in core construction (though OTLP wire-format is normative), and produce output that can be independently verified by an examiner.

The scope covers BOTH **decision-time integrity** (what the AI was asked, what it returned, what tools it called) AND **training-phase integrity** (training-data binding, gradient compute attestation, validation against held-out test sets). Inference-only institutions emit only inference-time chains; training-phase-bearing institutions emit both phases composed via cross-anchor patterns.

**Why it exists.** Banks use AI for loan approval, fraud detection, pricing, AML, stress testing. Regulators want to know what the AI said when something went wrong. Most teams cannot reconstruct AI decisions from production logs alone. §1 names the gap and what the spec fills.

### §1.1 Daubert four-factor grounding (informative)

The chain's evidentiary posture is structured so the four factors named in *Daubert v. Merrell Dow Pharmaceuticals* — testability, peer review, known error rate, general acceptance — each have a concrete answer an institution's expert witness can point at without re-engineering the system.

The §1.1 section also carries the **regulator-facing alignment note** (added 2026-05-09): how the spec maps onto the 2026 banking-supervision MRM guidance themes (proportionality, third-party-vendor accountability, lineage tracking, "effective challenge," governance posture, GenAI carve-out). The same artifacts that ground Daubert (spec text, test vectors, reference implementation, §7 verifier procedure) also answer regulator-facing examination questions.

**Why this matters.** Court admissibility (Daubert / FRE 702) and regulatory examination are two parallel admissibility regimes. The spec is structured so the same artifacts serve both. An institution's IT witness laying foundation under FRE 702 cites §1.1; an examiner reviewing the chain cites the same artifacts.

### §1.2 Epistemic scope (informative)

**What it says.** The chain proves two things and does NOT prove three others.

**Proves:**
- **(a) What the AI said at a specific time.** The captured event records the model's response, the prompt, the tools, the routing decision, the operational state. The per-event MAC and daily Merkle seal bind it.
- **(b) The record was not tampered with after capture.** The §7 verification procedure rejects post-hoc modifications.

**Does NOT prove:**
- **(c) The AI's statement is factually accurate.** Chain captures what was said; doesn't claim it's true.
- **(d) The AI's statement complied with policy.** Policy compliance is a separate audit.
- **(e) The AI's statement is free of bias.** Bias requires statistical testing across populations.

**Why it exists.** Without this section, readers (especially lawyers and examiners) over-claim what the chain delivers. The chain is the *integrity foundation*, not the *truth foundation*. Institutions composing chain evidence with their other evidence regimes need this distinction stated normatively.

### §1.3 Security definitions (informative)

**What it says.** Standard cryptographic-engineering vocabulary: EUF-CMA (existential unforgeability under chosen-message attack) for HMAC and Ed25519, second-preimage resistance for SHA-256, compositional security for the layered construction.

**Why it exists.** Cryptographic reviewers (NIST, CFRG, academic security community) read this section to confirm the spec's threat model is honest. Without rigorous definitions, security claims are hand-wavy.

### §1.4 Compositional security (informative)

**What it says.** The four primitives combine to produce a 128-bit composite security level under NIST SP 800-175B. Per-tenant HKDF binding + Ed25519 EUF-CMA + Merkle second-preimage compose without weakening.

**Why it exists.** Security claims need to compose. An attacker who could break only one of the layers shouldn't be able to forge a chain. §1.4 spells out why the composition holds.

### §1.5 Decision-event vs state-machine modeling (informative)

**What it says.** The chain models *decision events* (a discrete recorded fact) rather than *state machines* (an ongoing process). This affects how implementers structure their capture logic.

---

## §2 Out of scope

**What it says.** The spec does NOT cover:
- The runtime environment AI agents execute in
- The semantic meaning of captured events (those follow OpenTelemetry GenAI semantic conventions)
- The retention duration of ledger artifacts (regulators set this; implementations support configurable retention)
- The specific HSM model or vendor (any FIPS 140-2 Level 3+ device is conformant)

**Why it exists.** Without explicit out-of-scope statements, every reviewer asks "why doesn't this spec cover X?" §2 says: because it's outside this spec's remit. Other regimes cover those concerns.

---

## §3 Definitions

The vocabulary table. Every reader bookmarks this section.

**Key terms:**

| Term | Plain-English |
|---|---|
| **Event** | One recorded AI activity — a model call, a tool call, a decision, a retry. |
| **Run** | A bounded sequence of events sharing one `run_id`, representing one logical agent invocation (e.g., one user's session with the assistant). |
| **Tenant** | A regulated institution subscribed to a chain-of-custody implementation. Each tenant has independent keys + ledger. The `tenant_id` matches a regex character class — alphanumerics, underscore, hyphen, dot only — so the HKDF input parameter is unambiguously parseable. |
| **Tenant-day** | All events for one tenant in one UTC calendar day. The aggregation unit for the daily Merkle seal. |
| **IKM (Input Key Material)** | The long-lived per-tenant secret. Held in HSM/KMS, never on application hosts. ≥32 bytes (256 bits) of CSPRNG entropy per FFIEC chain-of-custody spec §10.6 / §10.6.1. Synonym in operations contexts: "master key." |
| **Session key** | A 32-byte HMAC key derived from IKM via HKDF. Bound to one tenant. Held in process memory only. |
| **`key_version`** | An integer ≥ 1 identifying which IKM generation produced a session key. Lets a verifier ten years from now look up the right IKM. |
| **`key_fingerprint`** | A public 16-byte identity binding: the first 16 bytes of `SHA-256(utf8(tenant_id) \|\| ikm)`. Stamped on every chain entry. The verifier asserts the looked-up IKM produces this fingerprint *before* computing any MAC — so a botched rotation that re-uses `key_version=1` for a different IKM is caught at lookup time, not buried in a MAC-failure storm. |
| **`format_version`** | The chain format string (`"v1"` for this spec). Stamped on every entry + audit-file header so a verifier reading an unrecognized version refuses with the right error. |
| **`chain_kind`** | The chain entry's event class. Closed v1 enumeration: `audit`, `model_call`, `tool_call`, `routing`, `translation`, `operational`. The verifier rejects any value outside the set. |
| **HSM** | A Hardware Security Module conforming to FIPS 140-2 Level 3 (or higher) or Common Criteria EAL4+. Used for daily root signing. |
| **Region** | An institution-defined unit of operational and cryptographic locality for multi-region deployments per §10.15. The institution names what each region encompasses (a cloud-provider region, a datacenter facility, a logical grouping that crosses cloud boundaries). |
| **CC8.1 (or equivalent)** | The institution's SOC 2 Trust Services Criteria CC8.1 control description (or equivalent under the institution's chosen audit framework — SOC 1 §8, ISAE 3402, etc.). The canonical institution-side authoritative document where the institution names which §10.x sections it adopts and which postures it operates. The cross-referencing discipline is normated in §10.18. |
| **Posture** | The institution's declared operational mode for a chain feature dimension. Each dimension has a closed set of conformant postures (e.g., FFIEC vs vendor-flag posture; single-algorithm vs dual-algorithm; multi-region Pattern A vs Pattern B); the institution selects one per dimension and records it in CC8.1; the verifier dispatches per the declared selection. |

### §3.1 Legacy tenant identifier handling (normative)

**The problem.** Many institutions have legacy tenant identifiers from upstream IAM systems that don't conform to the §3 character class — slashes, colons, Unicode characters, lengths over 255 bytes.

**Three migration patterns:**
1. **Opaque hash-of-legacy** — map `legacy_id → "tnt_" + SHA-256(legacy_id)[:24]`. Cryptographically deterministic, no character-class compromises.
2. **Controlled aliasing** — register a curated conforming canonical name per legacy tenant (`acme/prod` → `acme_prod`). More human-readable.
3. **Reject non-conforming new tenants** — chain covers only conforming tenants; legacy stays on legacy systems.

The institution names the chosen pattern in CC8.1.

---

## What §0–§3 buys you as a reader

After the front matter, you should have:
- A clear sense of what the spec covers (decision-time + training-phase integrity for AI in regulated systems).
- A clear sense of what it does NOT cover (the AI runtime, the meaning of events, retention duration, specific HSM vendors).
- A vocabulary you can use to read §4 onward without stumbling on `tenant_id` / `IKM` / `key_fingerprint` / `posture` / `CC8.1`.
- The Daubert + regulator-facing alignment framing for why this spec exists in the legal/regulatory landscape.

§4 is where the cryptographic content begins. Before you turn there: the chain is built from four composable primitives. If you remember nothing else from this orientation, remember that.
