# Plain-English: §5–§7 — wire format, storage, verification

§4 introduced the four primitives. §5–§7 are the operational machinery that turns those primitives into something a verifier can walk byte-by-byte ten years from now.

---

## §5 Wire format

**What it says.** Two normative encoding rules:
- **On-the-wire:** OTLP protobuf. Carries chain attributes between the SDK, collectors, and the receiver. Standard OpenTelemetry transport.
- **Inside `payload_hash`:** RFC 8785 JCS (JSON Canonicalization Scheme). Implementations MUST NOT use OTLP protobuf bytes for hashing — protobuf is non-deterministic for some field types.

**Two encodings, one purpose.** OTLP carries the events on the network. JCS produces the bytes the per-event MAC is computed over. Two implementations producing the same logical event produce byte-identical JCS bytes — that's how the chain achieves cross-implementation byte-equivalence in the test-vector corpus.

> Conforms to FFIEC chain-of-custody spec §5 — bytes input to any MAC or hash are RFC 8785 JCS-canonical.

### §5.0.1 Top-level wire-format kinds (normative)

The v1 enumeration: `chain_entry`, `seal_record`, `anchor_record`, `cross_domain_transition`. Adding new kinds within v1 is **additive** — does NOT increment `format_version`. A v2 spec that changes per-event canonical-form rules or seal-record byte structure would increment `format_version`. The §7 unknown-wire-format-kind fallthrough rule handles forward-compat: a v1.0Y verifier seeing a kind it doesn't know PASSes with an anomaly marker, never crashes.

### §5.1 Transport encryption (normative)

TLS 1.3 minimum. TLS 1.2 sunset 2028-01-01. Server authentication required; client auth via Bearer token or mTLS. Receiver-policy discovery endpoints inherit the same security floor.

### §5.2 Best-evidence posture (informative)

Under FRE 1001-1004, the *captured JSON* (the redacted form, post-§10.22 redaction discipline) is the content-bearing form; the *canonical bytes* are the integrity-bearing form. Both are "originals" under FRE 1001(d).

**Why this exists.** Litigation cares which byte form is "the original." The spec answers the question normatively so an institution's IT witness doesn't have to invent the answer at deposition.

### §5 take-away

JCS is the universal canonicalization for everything in the chain that gets hashed or signed. §10.49 retrieval-set Merkle, §10.58 binding-hash, §10.39 baseline manifest, §10.66 lineage Merkle — all use JCS. If you remember one rule: **bytes that go into a hash are JCS-canonical, period.**

---

## §6 Storage

**What it says.** Three rules + a header rule.

1. **Chain-stamp preservation.** The seven chain-stamp fields (`prev_hash`, `payload_hash`, `key_version`, `key_fingerprint`, `format_version`, `mac_computed_at_utc`, `kms_handle_uri`) MUST be preserved byte-for-byte. No canonicalization, normalization, re-encoding. A storage layer that base64-encode-decodes these fields without preserving padding is non-conformant.

   > Conforms to FFIEC chain-of-custody spec §6 — the seven chain-stamp fields MUST be preserved byte-for-byte.

2. **File format header.** Line-oriented files start with the header record (per §4.4 schema). Every line ends with `\n` (0x0A). The verifier rejects files whose last byte is not `\n` — that's the mid-write truncation refusal.
3. **Empty-file structure.** A tenant-day with zero events is a single header line plus terminating `0x0A`. The verifier accepts the empty file as structurally valid and computes the empty-tree Merkle root (`SHA-256(b"")` = `e3b0c44…b855`). A zero-byte file is rejected.

**Why this exists.** Cheap mistakes — wrong base64 padding on a chain-stamp roundtrip, missing terminator on the last line, silent truncation of an empty file — would invalidate a chain. The §6 rules close those mistake classes at the storage-layer contract.

### §6 take-away

Storage is a verbatim-bytes substrate. Don't touch the bytes. The chain's integrity rests on byte-identicality from write to read; storage that mutates breaks the chain at the per-event MAC layer.

---

## §7 Verification

The procedure. Twelve numbered steps, plus a 12a step for GenAI-specific completeness, plus pre-flight checks, plus the witness-verifier mode, plus the customer-disclosure verifier mode, plus the unknown-wire-format-kind fallthrough rule, plus the forward-compatibility / fault-tolerance discipline.

### The pre-flight phase

Before any of the 12 steps execute:

- **JCS self-test.** The verifier runs its JCS implementation over a baked-in fixture (from `008-jcs-edge-cases/`) and constant-time compares against a baked-in expected output. This catches a verifier that shipped with a non-conformant JCS path. Fail → exit 3 (configuration error). The cost is negligible (one-time per process).
- **Empty-file pre-flight.** Zero-byte file → `empty file: header missing` (exit 2). Non-empty files proceed to byte-level seek check.
- **Mid-write truncation.** Verifier reads the last byte; if not `\n`, FAILs with `audit file ends mid-line — possible mid-write crash`. Stdlib line readers don't catch truncation; the byte-level check is mandatory.

### The 12 steps (per file/day/seal)

1. **Format-version check.** `header.format_version == "v1"`. Variants like `"v1.0"`, `"v1.1"`, `"v2"` are refused with `format_version <X> not supported by this verifier (running v1)`.
2. **HKDF inputs digest.** Recompute and compare against `header.hkdf_inputs_digest`. Mismatch → vendor-flag mode under different constants, or stale verifier config, or adversarial supply.
3. **Genesis-hash check.** `header.genesis_hash == 32 zero bytes`.
3a. **Tenant-id character class check.** Per §3 regex.
4. **Per-entry binding (cross-chain-lift defence).** `event.tenant_id == header.tenant_id` AND `event.run_id == header.chain_id`. Mismatch → `cross-chain lift detected at seq N`.
5. **Per-entry format check.** `entry.format_version == header.format_version`.
6. **Structural walk.** `seq` monotonic (starts at 1); `prev_hash` correct (genesis for `seq=1`; previous entry's `payload_hash` thereafter).
7. **IKM lookup.** Resolve the tenant's IKM from the verifier's registry. Null → `unknown key_version`. **No MAC compute on lookup miss.**
8. **Fingerprint check.** Recompute `expected_fingerprint = SHA-256(utf8(tenant_id) || ikm)[:16]`; constant-time compare against `entry.key_fingerprint`. Mismatch → `key_fingerprint mismatch`. Catches botched rotations.
9. **MAC recompute.** Derive `session_key = HKDF-SHA-256(IKM, salt, info)`; recompute `expected_mac = HMAC-SHA-256(session_key, expected_prev_hash || canonical_bytes)`. **Uses `expected_prev_hash` (the structurally walked value), NOT `entry.prev_hash`** — defends against an attacker substituting `prev_hash`.
10. **Merkle recomputation.** Stream events in `(run_id, seq)` order; compute RFC 6962 Merkle root from each `payload_hash`. Compare against `seal.merkle_root`.
11. **Signature verification.** Reconstruct `sign_payload` per §4.3, dispatching on `sign_payload_version` (absent / `"v1.0a"` / `"v1.0b"` / unrecognized). Verify Ed25519 signature. Plus dual-algorithm dispatch for §4.3.2 posture. Plus the `key_versions` cross-check.
12. **Cadence and dev-mode check.** `seal.cadence` matches institution; `seal.dev_mode == false` under `--strict`.
12a. **GenAI model identifier completeness check.** For chain entries with any `gen_ai.*` attribute, BOTH `gen_ai.request.model` and `gen_ai.response.model` MUST be present. SDK-side refusal closes the source; §7 step 12a is defense-in-depth.

> Conforms to FFIEC chain-of-custody spec §7 — the 12-step verification procedure. Step 8 (fingerprint check) precedes step 9 (MAC recompute), which uses the structurally-walked `expected_prev_hash`.

### Step ordering — normative for data-dependent steps

Steps 7→8→9 MUST execute in order (each step depends on the previous). Steps 1-6 sequential because each establishes preconditions. Steps 10/11/12/12a operate on day-level or per-event data and MAY execute in any order relative to each other. Skipping a step entirely is non-conformant; reordering data-independent steps is fine.

### Verifier output format

**Line-oriented form** (default, backward-compat):
- PASS: `Status: PASS` (one line, optionally followed by anomaly lines)
- FAIL: 3 lines — `Status: FAIL` / `Step: N` / `Reason: <text>`
- Witness mode: `Status: PASS-STRUCTURALLY, key-bound verification skipped`
- Customer-disclosure mode: `Status: PASS-CUSTOMER-DISCLOSURE, institution-IKM verification skipped`

**Verdict-object trailing line** (always emitted, regardless of mode):
```
Verdict-Object: {"additional_verifications":[<markers>],"exit_code":<int>}
```

The verdict object is JCS-canonical, two fields, closed shape. Vector 036 pins the byte form. Existing harnesses parsing the first three lines and ignoring the rest remain conformant; new harnesses scan for `Verdict-Object: ` prefix.

Failure-reason strings are **byte-for-byte normative**. A verifier that produces `"MAC mismatch at entry 1"` instead of `"payload_hash MAC mismatch at seq 1"` is non-conformant. Implementations MAY append diagnostic detail after `: ` or on subsequent lines (`Hint:...`, `Detail:...`).

### Three verifier modes

| Mode | IKM access | Steps executed | Status output |
|---|---|---|---|
| **Strict** | full IKM via `--master-key` | all 12 (or 13 with 12a) | `PASS` or `FAIL` |
| **Witness** | none | skip 7/8/9 | `PASS-STRUCTURALLY, key-bound verification skipped` |
| **Customer-disclosure** (§10.69) | per-customer derived disclosure key (NOT institution IKM) | all 12; steps 7-9 against disclosure key | `PASS-CUSTOMER-DISCLOSURE, institution-IKM verification skipped` |

Plus the §7 witness-mode applicability table covers which §10.x verifier dispatches compose with witness mode (most do; a handful are strict-only).

### Unknown-wire-format-kind fallthrough

A v1 verifier ingesting a chain with a `cross_domain_transition` record (or any future v1.x kind it doesn't know) MUST:
1. Not silently treat the unknown record as a chain entry.
2. Not FAIL the entire run on the unknown kind alone.
3. Emit anomaly line: `unknown wire-format kind present: <kind_string> (count: N)`.
4. Emit `additional_verifications: ['unknown_kind_present']`.
5. Exit code remains `0` (PASS).
6. Recompute Merkle root over the day's full leaf sequence including the unknown-kind records.

### Forward-compatibility / fault-tolerance (normative — added 2026-05-09)

A v1.0Y verifier reading a v1.0Y+ chain MUST handle six classes of unknown constructs gracefully (named fail-closed dispatch OR PASS-with-anomaly), never crash:
1. Unknown `sign_payload_version` → fail closed with named reason
2. Unknown wire-format kinds → §7 fallthrough rule
3. Unknown OTel attributes on chain entries → MAC verifies; semantic skip
4. Unknown `additional_verifications` markers → harness opaque-on-read
5. Unknown seal-record fields → ignored if outside the `sign_payload_version`'s signed scope
6. Unknown `canonical_encoding` → fail closed with named reason

A verifier that crashes, hangs, segfaults, or produces undefined behavior on any of these is non-conformant.

### §7 take-away

The verification procedure is the spec's testable contract. If you understand §7, you can reason about every assurance the chain provides. The 12-step ordering matters; the byte-for-byte reason strings matter; the mode dispatch matters; the forward-compatibility discipline matters.

A reader who has internalized §4 + §5 + §6 + §7 has the spec's full cryptographic + procedural model. Everything in §10 extends or composes with this base.
