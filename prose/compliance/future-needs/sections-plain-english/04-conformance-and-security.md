# Plain-English: §8–§9 — conformance test vectors and security considerations

Two short sections that close the spec's conformance contract.

---

## §8 Conformance test vectors

**What it says.** `spec/test-vectors/` contains the canonical conformance corpus. A conforming implementation produces output identical to the test vectors for the cases they cover. Implementations SHOULD extend the corpus when they add features.

**Why it exists.** The spec text is one half of the conformance contract; the test vectors are the other half. Two clean-room implementations reading the same spec should produce the same bytes for the same inputs. The test-vector corpus is what proves it.

**Vector categories:**
- **Positive vectors** — inputs that produce a valid chain; the verifier emits `Status: PASS` with byte-identical line-oriented output.
- **Negative vectors** (under `negative/`) — inputs that exercise an attack class; the verifier emits `Status: FAIL` with the spec-named reason string and the correct exit code.
- **Reference fixtures** — JCS edge cases (vector 008), Merkle inclusion proofs (vector 023), per-device derivation (vector 024), partial disclosure (vector 017), `sign_payload` byte forms (vectors 018 and 019), verdict-object structural shape (vector 036), and others.

**Vector 036 — verdict-object schema pin.** This is the canonical pin for the `additional_verifications` array shape. Three sub-cases (036a empty, 036b one marker, 036c two markers, all `exit_code = 0`) cover the structural cases an implementer needs.

**The JCS self-test.** §7 pre-flight bakes a fixture from `008-jcs-edge-cases/` into the verifier binary. A verifier that doesn't pass the self-test refuses to walk any chain. This makes JCS conformance non-negotiable at process startup.

### §8 take-away

Test vectors are normative-equivalent. A spec edit that changes byte forms requires regenerating affected vectors in the same change-set. Implementers consume vectors continuously during development; a chain that doesn't byte-match its corresponding test vector is non-conformant.

---

## §9 Security considerations

**What it says.** The spec's threat model and security argument live in §1.3 (security definitions), §1.4 (compositional security), and §10 operational requirements. §9 is a brief pointer; the substantive material is elsewhere.

The compositional argument: per-tenant HKDF binding (§4.1) + Ed25519 EUF-CMA (§4.3) + Merkle second-preimage resistance (§4.2) compose to a 128-bit composite security level under NIST SP 800-175B. A successful false-negative — a tampered chain that verifies as PASS — requires the simultaneous compromise of three independent custody layers:
1. The tenant's IKM (held in HSM/KMS)
2. The institution's ledger storage (append-only, operator-controls)
3. The HSM signing key (FIPS 140-2 Level 3 or higher)

The three layers are operated by different roles under separation-of-duties controls. Compromise of any one alone does not produce a verifying tamper.

**Threat-model docs (referenced but separate):**
- `docs/design/09-threat-model.md` — adversary capability matrix (15 adversaries × 7 capabilities) and residual-risk register (R1–R19).
- `docs/incident-response-playbook.md` — IR scenarios for each adversary class.

**Common confusions clarified elsewhere in the spec:**
- The chain depends on **second-preimage resistance** of SHA-256, not collision resistance (§4.2 informative paragraph). A future weakening of SHA-256 collision resistance does not by itself break the chain.
- The 16-byte `key_fingerprint` is **not load-bearing for cryptographic security** — it serves operational audit (§10.1 P-6 reconciliation) and pre-flight rejection of botched rotations (§7 step 8). Cryptographic properties depending on collision resistance use the full 32-byte SHA-256 output.
- **Fault-injection attacks (FIA / DFA)** on FIPS 140-2 Level 3 HSMs are accepted residual risk. Institutions deploying in nation-state-attacker threat models SHOULD select FIPS 140-3 Level 4 or Common Criteria EAL5+ HSMs (TCCP axis 3 — TesseraSeal posture covers this above the spec floor).

### §9 take-away

The security model is layered, compositional, and grounded in NIST-standardized primitives. The spec does not invent crypto; it composes existing primitives in a way that makes a successful tamper require three simultaneous compromises across three operational roles. §10 operational requirements is where most of the substantive security discipline lives.
