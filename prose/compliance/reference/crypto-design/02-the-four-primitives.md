# Plain-English: §4 — the four primitives

§4 is the cryptographic heart of the spec. Everything else (§5 wire format, §6 storage, §7 verification, all of §10) extends or composes with these four primitives. If you understand §4, the rest is detail.

---

## The shape of §4 in one paragraph

A captured event is wrapped in an HMAC chain at write time (§4.1). At end of UTC day, every event's HMAC for that tenant is fed into a Merkle tree; the apex hash is the daily seal (§4.2). The daily seal is signed by an HSM-resident Ed25519 key — that signature is what an examiner verifies independently a decade later (§4.3). The whole construction rides on OpenTelemetry's OTLP wire format, so the chain attributes flow through standard observability infrastructure rather than a bespoke chain-pipeline (§4.4).

Four primitives. Each addresses a different attack class.

---

## §4.1 Primitive 1 — HMAC chain at capture (normative)

**What it does.** Every captured event gets a `payload_hash` field that's the HMAC-SHA-256 of `prev_hash || canonical_event_bytes` under a per-tenant session key. The session key is derived from the tenant's long-lived IKM via HKDF-SHA-256 with the tenant_id bound into the HKDF info parameter.

> Conforms to FFIEC chain-of-custody spec §4.1 (HMAC chain at capture).

**The chain link.** Each entry's `prev_hash` is the previous entry's `payload_hash`. So every entry's MAC depends on the entire prior chain — modify any historical entry and every subsequent entry's MAC fails to verify.

**The MAC IS the payload_hash.** This is subtle: the spec doesn't store SHA-256(payload) separately from the HMAC. The HMAC output IS the `payload_hash` field. One field, one purpose: integrity-bind the event under a tenant-specific key. The §7 step 9 MAC compute checks the HMAC; there's no separate "and then SHA-256 the canonical bytes too" step.

**Why HKDF.** The IKM is long-lived (years). Per-event HMAC keys would be too painful to provision. HKDF derives a per-tenant 32-byte session key from the IKM that's good for the life of the IKM. The `info` parameter binds the tenant_id into the derivation, so the same IKM under a different tenant_id produces a different session key — closes the cross-tenant key-reuse risk.

> Conforms to FFIEC chain-of-custody spec §4.1 (HKDF salt/info rationale). The static salt is a public constant; the per-tenant `info` ensures derived-key independence (NIST SP 800-56C §5.4).

**Per-event stamp fields.** Every chain entry carries:
- `seq` (int64) — monotonic per `run_id`, starting at 1
- `prev_hash` (32 bytes) — genesis (32 zero bytes) for `seq=1`; previous entry's `payload_hash` thereafter
- `payload_hash` (32 bytes) — the HMAC output above
- `key_version` (int) — which IKM generation produced this entry's session key
- `key_fingerprint` (16 bytes) — SHA-256(utf8(tenant_id) || ikm)[:16]
- `format_version` (string) — `"v1"` for this spec
- `mac_computed_at_utc` (RFC 3339 UTC) — writer's wallclock at MAC compute (forensic only)
- `kms_handle_uri` (string) — KMS/HSM provenance pointer

> Conforms to FFIEC chain-of-custody spec §4.1 (fingerprint formula). Publishing this formula is safe **because** spec §10.6 mandates an IKM of ≥256 bits drawn from a FIPS-validated CSPRNG. That entropy floor closes the offline fingerprint-brute-force attack class — the only attack the published formula would otherwise enable. The 16-byte truncation hides the full digest state (spec §4.1 length-extension audit). The §10.6 entropy mandate is the control this disclosure rests on.

The `key_fingerprint` is the operational hero. The verifier asserts the looked-up IKM produces this fingerprint *before* computing any MAC. If a botched rotation has re-used `key_version=1` for a different IKM, the fingerprint mismatches and the verifier refuses without computing a MAC — preventing a MAC-failure storm that would otherwise bury the rotation error.

> Conforms to FFIEC chain-of-custody spec §7 step 8 — botched-rotation detection at lookup time, no MAC compute on mismatch.

### §4.1.1 IKM delivery models (normative)

Two conformant ways for an SDK to obtain the IKM at runtime:

1. **IKM-delivered.** The HSM/KMS vends the IKM bytes to the SDK at process start; the SDK derives the session key in-process. Higher trust assumption (process memory holds IKM); lower latency.
2. **Session-key-delivered.** The HSM/KMS derives the session key inside the HSM and vends only the session key. The SDK never sees IKM bytes. Higher security assumption; HSM round-trip cost on session-key refresh.

Both produce per-tenant determinism: the same IKM produces the same session key produces byte-identical `payload_hash` for byte-identical input. That property is what lets a verifier ten years from now reproduce a MAC.

> Conforms to FFIEC chain-of-custody spec §4.1.1 — two conformant IKM-delivery models (session-key handshake).

### §4.1.2 Vendor-namespaced constants and FFIEC conformance (normative)

**The problem.** Several vendors shipped HMAC-SHA-256 + HKDF audit chains under their own namespace constants before v1.0 was published. The construction is identical at the function level — only two byte values (the HKDF salt and the HKDF info-base) differ.

**The resolution.** SDKs MAY parameterize `HKDF_SALT` and `HKDF_INFO_BASE` at construct time. A chain entry is **FFIEC-conformant** ONLY when produced under the spec's named constants (`"ffiec.chain-of-custody.v1.salt"` and `"ffiec.chain-of-custody.v1.info"`). Chain entries under any other constants are non-FFIEC chains; the institution names which regulatory framework (if any) they satisfy.

**The on-disk witness.** Both the audit-file header and the seal record carry `hkdf_inputs_digest = SHA-256(HKDF_SALT || info_for_tenant || length_LE32)`. This unambiguously records which constants were in force. A verifier under FFIEC posture computes the expected digest from the spec's constants and constant-time compares. A non-FFIEC chain fails this check at the file-header pre-flight — there's no silent acceptance mode.

**Posture is binary at the chain-file level.** Either the file's events were produced under FFIEC constants, or they weren't. Mixed-posture chains are not conformant.

> Conforms to FFIEC chain-of-custody spec §4.1.2 — the named constants `ffiec.chain-of-custody.v1.salt` / `.v1.info`; the `hkdf_inputs_digest` records which constants were in force.

---

## §4.2 Primitive 2 — Daily Merkle seal (normative)

**What it does.** At end of UTC day, the institution's ledger collects every chain entry's `payload_hash` for the tenant-day in `(run_id, seq)` ascending order. Those become the leaves of an RFC 6962 Merkle tree. The apex hash is the day's `merkle_root`.

**Why aggregate.** A 10,000-event day produces one signature, not 10,000. The HSM-rooted signature in §4.3 is over the merkle_root, not over each event. The aggregation is what makes the construction economical at scale.

**Leaf ordering is mandatory.** Two implementations sealing the same day MUST produce byte-identical `merkle_root`. The ordering is `(run_id, seq)` ascending. Implementations MUST NOT use `received_at` or `captured_at` for ordering — those vary across implementations and would break the cross-implementation byte-equivalence the test-vector corpus enforces.

**Empty-day discipline.** A tenant-day with zero events still gets a seal record. Empty-tree Merkle root is `SHA-256(b"")` = `e3b0c44...b855`. Empty-day seal continuity means a verifier can detect a missing day (chain gap) regardless of whether events were captured. A missing empty-day seal is reported as `missing seal for tenant-day {D}` (control-completeness anomaly, NOT chain-integrity failure).

**Late-binding events.** Events arriving after their `received_at` UTC date is sealed are recorded with `ffiec.chain.late_binding = true` and included in the next day's seal. The original seal MUST NOT be altered. The verifier reports late-binding entries as a PASS-with-anomaly line.

> Conforms to FFIEC chain-of-custody spec §4.2 — RFC 6962 tree, mandatory `(run_id, seq)` leaf ordering, empty-day root `SHA-256(b"")`.

### §4.2.1 Configurable cadence (cross-reference §10.27)

Default cadence is daily. Institutions with sub-second decision rates may operate hourly seals; institutions with low-volume long-retention regimes may operate weekly. The cadence is in CC8.1. The seal record carries `cadence` in its `sign_payload`, so a verifier knows what window the seal covers.

### §4.2.2 Day-boundary semantics

The `received_at` partition is the seal region's `received_at` (per §10.15 multi-region). Events captured in replication regions and replicated after the seal region's UTC-day boundary belong to the next day.

---

## §4.3 Primitive 3 — HSM-rooted root signature (normative)

**What it does.** The daily Merkle root is signed by an Ed25519 key held in an HSM (FIPS 140-2 Level 3 or higher). The HSM-private key is non-extractable. The seal record carries the signature plus everything a future verifier needs.

**Why HSM-rooted.** Software keys can be exfiltrated by an insider with debug access. HSM keys cannot. The chain's tamper-evidence rests on the HSM key's non-extractability — an attacker who can sign forged seals defeats the chain. Without HSM custody, the chain is structural integrity only; with it, the chain is forensic-grade evidence.

**Sign payload byte-form.** The Ed25519 signature is over `sign_payload` — a structured byte form whose canonical layout is normated. v1.0b is a 12-line form binding:
- magic line (literal `"FFIEC-CHAIN-v1"` or similar)
- `sign_payload_version = "v1.0b"`
- `algorithm` (e.g., `"ed25519"`)
- `format_version` (e.g., `"v1"`)
- `tenant_id`
- `seal_date` (ISO 8601 UTC date)
- `merkle_root` (lowercase hex, 64 chars)
- `hkdf_inputs_digest` (lowercase hex, 64 chars)
- `cadence` (e.g., `"daily"`)
- `dev_mode` (e.g., `"false"`)
- `key_versions_canon` (canonical sorted-distinct comma-separated form, e.g., `"1,2,3"`)
- `hex(kms_handle_uris_digest)` (SHA-256 of canonical sorted-distinct URI form, lowercase hex)

Each line terminated with a single `\n` byte (0x0A). The signature is over the byte-concatenation of the 12 lines.

> Conforms to FFIEC chain-of-custody spec §4.3 — HSM-rooted Ed25519 root signature over the 12-line `sign_payload` byte form; signing key non-extractable per §10.5.

### §4.3.1 HSM unavailability (informative)

Institutions SHOULD notify regulators within 72 hours if the HSM is unavailable to seal. Day's events get sealed when the HSM returns; late-binding discipline applies.

> The seal record's `algorithm` field discriminates `"ed25519"` from future signers, so a v1 verifier dispatches on it (see §7 step 11). The forward-design of algorithm rotation and quantum-readiness — the dual-algorithm posture and the working-group commitment — is candidate-normative and tracked separately, not in this published v1 surface.

---

## §4.4 Primitive 4 — OpenTelemetry-native wire (normative)

**What it does.** The chain attributes are emitted on the OpenTelemetry OTLP wire format, with the OpenTelemetry GenAI semantic conventions applied to model-call events.

**Why OTLP.** Banks already deploy OpenTelemetry collectors for application observability. The chain's wire format piggybacks on existing infrastructure — no separate chain-pipeline to operate.

**Attribute namespaces:**
- `ffiec.chain.*` — chain-stamp fields (`payload_hash`, `prev_hash`, `key_version`, etc.)
- `gen_ai.*` — OpenTelemetry GenAI semantic conventions (`gen_ai.request.model`, `gen_ai.response.model`)
- `tool.*` — tool invocations
- `audit.*` — institution-emitted operational evidence (`audit.routing.*`, `audit.deployment.*`, `audit.cross_border_transfer.*`, `audit.model_handover.*`, etc.)

> Conforms to FFIEC chain-of-custody spec §4.4 — OTLP-native wire format and the `ffiec.chain.*` / `gen_ai.*` / `audit.*` attribute namespaces.

**SDK MUST refuse incomplete model calls.** An entry with any `gen_ai.*` attribute and missing either `gen_ai.request.model` or `gen_ai.response.model` is non-conformant. SDKs reject before MAC compute; verifiers re-check at §7 step 12a (defense-in-depth).

**OTLP collector pass-through (normative).** Collectors MUST NOT mutate chain attributes. Mutation surfaces as MAC mismatch (or chain gap for dropped events). Disambiguating "collector misconfiguration" from "active tampering" is institution-side IR work — the chain doesn't distinguish at the verifier level.

**SDK per-process region binding (normative; Pattern A enforcement).** When operating §10.15 Pattern A, SDKs are configured per-region — one SDK process per region. A multi-region SDK process can't mechanically enforce §10.15 Pattern A invariant 2 (run-locality), so it's non-conformant for Pattern A.

### §4.4.1 AI routing decisions (normative)

**The problem.** A multi-provider LLM deployment routes calls between providers (Anthropic, OpenAI, Google, vendor-specific). When an examiner asks "why was THIS user routed to provider B?" the answer is in the routing logic, not in the LLM call itself. Without chain-bound routing decisions, that answer is buried in failover-tool logs that retain shorter than the chain.

**The schema.** Six routing event types: `audit.routing.attempt`, `audit.routing.success`, `audit.routing.failure`, `audit.routing.failover`, `audit.routing.refused`, `audit.routing.classifier_output` (parent-of-attempt for classifier-driven routing). Each carries the institution's policy version + provider identifier + circuit-breaker state.

### §4.4.2 Deployment-intent capture (normative)

**The problem.** Was this LLM call part of a regulator-supervised A/B test, a steady-state production call, a canary deployment, an internal stress test? The chain entry's `audit.deployment.intent` answers from the chain alone.

**Enum:** `production`, `ab_test`, `canary`, `regulatory_sandbox`, `disparate_impact_test_run`, `unknown`. The MRM committee disposition table normates expected committee action per intent.

### §4.4.3 OTLP transport identification (normative)

Required Resource attributes (`ffiec.chain.spec`, `service.name`, `service.version`, `ffiec.chain.posture`, `ffiec.chain.format_version`) plus recommended HTTP headers (`X-FFIEC-Chain-Spec`, `X-FFIEC-Chain-Posture`) and gRPC metadata.

### §4.4.4 Severity for chain-of-custody traffic (normative)

Collectors MUST NOT downgrade chain traffic to TRACE / DEBUG. Severity numbers within the spec range `9..20` (INFO floor through ERROR4 ceiling, just below FATAL=21) are conformant; the institution tunes per CC8.1.

### §4.4.5 Underwriting features family + §4.4.6 SaaS-edge connector source attribution (normative when applicable)

Schema additions for credit underwriting (§10.21-bound model-supply, fairness audit binding) and SaaS-edge connector mirroring (Salesforce → chain-bound run_id derivation).

---

## What §4 buys you as a reader

By the end of §4 you understand:
- **How a single event becomes integrity-bound** — HMAC under a tenant-specific session key (§4.1).
- **How a day of events is aggregated** — RFC 6962 Merkle tree in `(run_id, seq)` order (§4.2).
- **How the day is signed** — Ed25519 over a 12-line `sign_payload` byte form, by an HSM key (§4.3).
- **How the chain rides existing infrastructure** — OTLP attributes in named namespaces, with mandatory schema for routing / deployment / model-call events (§4.4).

The four primitives are independent in construction but compose into one cryptographic claim: *"this event was captured at time T under tenant T's chain, sealed in the day-D Merkle root, and signed by HSM key K — and any of those bindings can be independently re-checked."*

Everything in §10 is some institution's specific way of using these four primitives. Knowing §4 means you can read any §10.x section without re-learning the cryptographic substrate.
