---
title: How MMP.Licensing defends against attacks, honest mistakes first
slug: explanation/how-licensing-defends
category: explanation
audience: new-to-licensing
since: 2.0
last-reviewed: 2026-05-17
related:
  - explanation/how-licensing-works
related-records: []
related-external:
  - repo: mmpworks/MMP.Licensing
    path: docs/adr/0001-mmp-licensing-architecture.md
    label: ADR-0001, engineering rationale
  - repo: mmpworks/MMP.Licensing
    path: doc/token-format-v2.md
    label: Wire format v2 specification
---

# How MMP.Licensing defends against attacks, honest mistakes first

This page is the companion to
[how MMP.Licensing works](./how-licensing-works.md). The first
page covered the mechanics. This one covers the threat model.

The threat model has an unusual shape. Most licensing writing
treats the customer as a suspect and spends pages on bypass
prevention. Ours runs the other way around. Most of the system
exists to catch the kind of small mistake a smart, busy engineer
makes on a Tuesday afternoon. The bypass-prevention layer is
real, but it's the smaller layer. We'll cover both, in that
order, because that order reflects how the system actually gets
used.

> **The frame, in the founder's words.** *"The goal of licensing
> is to help a company be honest, by accounting for all the
> 'mistakes' one can make when configuring and using. Clarity of
> design, careful review of the edge cases, and a simple workflow
> to get everything working is the big ask and the big win."*
>
> Read every defense below through that lens. We're not building
> a fortress to keep customers out. We're building a system
> where the easy path is also the correct path, and the wrong
> path fails loudly enough that the customer can fix it before
> it matters.

## Part A: defenses against honest mistakes

This is the bigger bucket. The customer is trying to do the
right thing. The system's job is to make the right thing easy,
and the wrong thing either impossible or very obvious.

### Multi-source detection: when both old and new env vars are set

**The mistake.** A customer rotates from a file-based license to
an environment-variable license, but forgets to remove the old
file. Or the reverse. They set the new env var but the old file
is still on disk. Both contain valid tokens, possibly different
ones (the new one is a renewal, the old one was last year's).

**What goes wrong without the defense.** A naive verifier picks
whichever source it checks first and never mentions the other.
The customer's app starts up cleanly. Months later, they
discover the renewal didn't actually take effect because the
verifier silently used the stale token.

**The defense.** The locator checks every source on every
startup, even after it finds a hit. When it finds more than one
source with a valid-looking token, it fires a *multi-source
detected* hook with sanitized details, and uses a documented
precedence (file beats env var). The customer's app gets a clear
log line on startup: "we found tokens in two places, used the
file at /etc/herald/license.key, ignored HERALD_LICENSE_KEY".

The customer sees the message, cleans up the stale source, and
moves on. No outage. No support ticket. Just a polite heads-up
that something looks ambiguous.

### Clock drift: the 30-second NTP skew

**The mistake.** The customer's server clock is 30 seconds ahead
of NTP because their virtualization layer had a hiccup. A token
that legitimately expires at midnight gets rejected at 23:59:30
local clock.

**What goes wrong without the defense.** The verifier compares
the current clock to the `exp` field directly. The 30-second
offset becomes a startup failure. The on-call engineer wakes up
to a "license expired" alert that resolves itself the moment
they reach for a keyboard.

**The defense.** The verifier allows a small skew window, 60
seconds in each direction by default, before declaring a token
expired or not-yet-valid. The window is documented and
configurable. Customers running highly synchronized clusters can
tighten it. Customers on flaky virtualization can loosen it.

This is not a back door. A token still expires when its `exp`
plus 60 seconds is in the past. We just don't make the boundary
hair-trigger.

### The license inventory DB: so no one has to remember

**The mistake.** A growing customer has 25 licenses across their
fleet. One per region. One per service. A couple for staging
environments. The platform engineer who set them up six months
ago has left. The new engineer needs to know which tokens cover
which services, which are expiring next month, and which can be
safely revoked.

**What goes wrong without the defense.** Without a central
record, the new engineer is reduced to grepping config files and
emails. Tokens that nobody can attribute get left in place "just
in case". Renewal becomes a guessing game.

**The defense.** `MMP.Licensing.Server` keeps an inventory DB
(small Azure SQL instance) of every token we've ever issued. It
tracks the customer, the product, the flavor, the kid that
signed it, issuance time, expiry, revocation status, last
check-in time, and current usage counters. An operator portal
exposes CRUD over this inventory. A future customer
self-service portal will let the customer view their own
licenses without going through support.

The token itself is still self-contained. The DB isn't in the
hot path. It's the record-keeper, so neither the customer nor
MMPWorks has to remember 25 small facts spread across 25
different places.

### Test license in production: the production denylist

**The mistake.** During development, the team minted a test
license signed with a development keypair (the `minter-test`
binary, separate from the production minter). Someone copies a
deployment script that has the test token baked in, runs it
against production, and the production service starts up "fine".

**What goes wrong without the defense.** The customer ships a
test-signed token to production. The verifier accepts it because
the signature math checks out against *some* known key. Months
later, the test key's expiration date arrives and production
fails. Or worse, the test key gets rotated and production breaks
at an unrelated time.

**The defense.** The production verifier ships with a hardcoded
**test-pubkey denylist**. Every token signed by the known
development keypair is rejected at the production verifier, with
a specific error message: "this token was signed by a
development key; production rejects it". The customer
immediately knows what happened.

This is belt-and-suspenders. The first line of defense is that
the test minter is a separate binary that only knows about test
keys, and the production minter is a separate binary that only
knows how to talk to the HSM. The second line is the verifier's
denylist, which catches the case where a test token somehow made
it into a production binary anyway.

### Fake key-map in a PR: signed snapshots and CI re-verification

**The mistake.** A contractor working on a Herald product writes
a feature branch that touches the licensing scaffolder. As part
of their work, they generate a local kid-map for testing and
accidentally commit it into the wrong file. The PR now proposes
shipping a key-map literal that *they* control.

**What goes wrong without the defense.** Without a check, the
PR merges. The next release embeds the contractor's key-map.
Every token signed with the contractor's private key is now
trusted by production. The contractor (or anyone who steals
their key) can mint valid tokens.

**The defense.** Every product reads its kid-map from
`src/trusted-kid-maps/<product>.json` in the MMP.Licensing repo.
That file is itself **signed** by the license server. PR CI
re-verifies the signature on every push. A PR that modifies the
kid-map content without a matching server-issued signature fails
CI loudly.

The scaffolder that generates new product wiring reads from this
same trusted-kid-maps directory. It never hits the live license
server during scaffolding. The signed snapshot is the single
source of truth, and any tampering with the snapshot will show
up in CI.

### Summary: the small mistakes that aren't outages

Each of the five mistakes above is the kind that lands in
ordinary incident logs all the time. Each one is what happens
when someone tries to do the right thing under time pressure.
The system catches all of them with a clear message, and the
customer fixes the issue in minutes.

The CUPID property at work here is *Predictable*. The system
behaves the way you'd guess it behaves, and when it can't, it
tells you. The DRY discipline is that **every "mistake" defense
lives in one place**. The clock-skew window is one constant in
the engine. The multi-source check is one branch in the locator.
The denylist is one constant in the production verifier. If we
ever change one of these defenses, we change it once.

## Part B: defenses against adversarial actors

This bucket is smaller. The customer is no longer the actor.
A malicious party is trying to use our product without paying.
Our goal is to make bypass expensive enough that paying is
easier.

### Why we don't ship a single shared DLL

**The threat.** An attacker swaps a single licensing library
(`MMP.Licensing.dll`) with a stub that returns "allowed" for any
token. Every product on the machine that depends on that DLL
now accepts forged tokens.

**The defense.** We don't ship a shared DLL. Every product
compiles its own copy of the licensing code from source, pulled
in via git submodule at build time. There's no
`MMP.Licensing.dll` in the install directory to swap.

To bypass a single product, the attacker has to modify *that
product's* compiled assembly. That's a far more visible
operation, detectable by signature checks the product itself
runs at startup. To bypass three products, they have to do it
three times. The shared-DLL attack scales. The per-product
attack doesn't.

> **Quick picture.** Imagine you're trying to break into every
> bank in a city. If they all share one central vault, you only
> need to crack one lock. If each bank has its own vault, with
> its own lock, you have to crack every one. We chose the second
> shape.

That's also why source-link is worth the inconvenience for our
own engineers. The asymmetric bypass cost is what we're buying.

### Why the private signing key lives in an HSM

**The threat.** An engineer's laptop holds the private signing
key. The laptop gets stolen, an employee turns rogue, or malware
exfiltrates the key. The thief can now mint unlimited valid
tokens for any product, at any tier, with any expiration.

**The defense.** The private signing key never exists outside a
Hardware Security Module. The specific HSM is **Azure Key Vault
Premium**, certified to **FIPS 140-2 Level 2**. Its only job is
to hold keys and produce signatures. The license server sends
the HSM the bytes to sign and gets back a signature. The key
itself doesn't leave the box. **No employee has direct access to
the signing keys** — there is no `kv export-key` button, no
break-glass "give me the bytes" mode, no engineer with a copy.

If the license server is compromised, the attacker can ask the
HSM to sign things while they have access, but they can't
extract the key and use it later from somewhere else. Key Vault
has its own authentication layer, its own audit log, and its own
rate limits. Recovery from a server compromise is "rotate the
Key Vault credentials". Recovery from a key compromise would
mean rotating the kid, pushing a verifier update to every
shipped product, and invalidating every issued token. One of
those is manageable. The other is the kind of incident that
takes a company down.

### Two minter binaries, not one minter with a flag

**The threat.** A minter program has a `--test` flag. An
engineer forgets the flag is set and mints a production token
with the test keypair, or vice versa. Or the minter is one
binary that knows about both keys, and an attacker who
compromises the test environment finds production-capable code
sitting in the same binary.

**The defense.** Two separate binaries. `minter` is production.
`minter-test` is test. The production minter has zero code paths
that touch the test keypair. It doesn't import the test key
bytes. It doesn't know the test key's `kid`. It can't be coerced
into producing a test-signed token. The test minter has zero
code paths that touch the HSM. It doesn't have the credentials,
and it doesn't know the HSM endpoint.

A mistake is impossible because the wrong thing isn't *present*
in the binary. It's not "guarded against". It's missing
entirely.

This is one of the cleanest applications of CUPID's *Unix
philosophy*. Each binary does one thing, and the things are
small enough that "does this binary touch production keys?" is
a yes-or-no answer instead of a long audit.

### Retired kids stay in the map with a RetiredAt timestamp

**The threat.** We rotate the signing key. An attacker gets hold
of the old (now-retired) private key from some forgotten backup.
They mint a token with the retired kid and submit it to a
customer's verifier.

**The defense.** Retired kids don't get removed from the
verifier's kid-map. They stay in the map with a `RetiredAt`
timestamp, and the verifier treats them differently depending on
where the incoming `kid` shows up:

- A token whose `kid` is in the map and **not retired** validates
  normally.
- A token whose `kid` is in the map but **retired** is rejected
  with a specific error: "this key was retired on 2026-01-15;
  request a re-issued token". The customer knows exactly what
  happened.
- A token whose `kid` is **not in the map at all** is rejected
  with a different error: "unknown key id 2099-3; verifier is
  out of date or token is forged".

That distinction matters. "Known but retired" tells the customer
their old token needs a re-issue. "Never heard of it" tells them
either their product is too old to know about the key, or
someone forged the token. Two different problems, two different
fixes.

> **Quick picture.** Imagine a building's master-key system.
> When a lock is retired, the building doesn't just forget about
> it. They keep a record saying "lock #47 was retired on
> 2026-01-15, request a new key from the office". If someone
> shows up with key #47, the doorman knows it's a former key,
> not a counterfeit. If someone shows up with a key numbered
> #999, the doorman knows it never existed in this building.
> Both visitors get turned away, but the doorman gives them
> different reasons and different next steps.

### Ed25519 over canonical JSON, and what "canonical" means

**The threat.** The token payload is JSON. JSON allows
whitespace, key reordering, and unicode escapes that all
represent the same logical object. An attacker takes a valid
signed token, modifies the JSON's whitespace, re-base64-encodes
it, and submits it. If the verifier signs over the *parsed*
JSON object and re-serializes it, the signature might still
validate even though the byte representation changed.

**The defense.** Two pieces.

First, **the verifier signs over the encoded payload bytes
exactly as they appear in the token**, not over the parsed JSON.
Whitespace, key order, escape choices. Whatever the issuer wrote
into the base64-encoded segment is what gets signed. This
matches JWT's signing convention. Changing a single byte in the
encoded payload changes the signature check result.

Second, **the issuer always produces canonical JSON before
signing**. "Canonical" here means a single, deterministic byte
representation for a given logical object. Keys are sorted in a
defined order. There's no extraneous whitespace. Escape
sequences are chosen by a fixed rule. Every signed token from
our server looks byte-identical given the same input, and every
verifier in every language agrees on what those bytes should
look like.

Together, the two pieces mean an attacker can't take a
legitimately signed token and rearrange it without invalidating
the signature. They can't write their own payload, sign it
(they don't have the private key), and submit it. The only
payloads that verify are payloads we issued.

We picked **Ed25519** because it's modern, fast on every
platform we ship, and produces a small fixed-size signature (64
bytes). The kid-map carries an `alg` field defaulted to
`ed25519`, so a future migration to a different algorithm
(should the cryptography world ever require it) is a
kid-rotation event rather than a format break.

### Summary: bypass is expensive, not impossible

We don't claim the system is unbreakable. A determined,
well-resourced attacker who is willing to modify a product
binary, dodge our integrity checks, and operate without our
support team's help can probably get a stripped-down version of
a Herald product running. What they can't do, easily:

- Forge a valid token. They don't have the private key.
- Swap a shared verifier. There isn't one.
- Convince our HSM to sign for them. The HSM doesn't talk to
  random callers.
- Roll their token forward past `exp`. The timestamp is signed.
- Trick a verifier into accepting a retired key. The
  retired-kid state survives in the map.

Each defense is a small, focused piece. None of them is doing
heroic work on its own. Together, they raise the bypass cost to
where the attacker's effort starts to look comparable to just
paying us. And paying us comes with support.

## How the two buckets relate

The honest-mistake bucket is most of what the system does day
to day. Customers benefit from it constantly without noticing.
Their cluster's clock drifts. Their staging environment has the
wrong env var. Their contractor commits the wrong file. The
system catches each one and tells the customer in plain English.

The adversarial-defense bucket runs in the background as a
structural property. The customer doesn't think about HSMs,
denylists, or canonical JSON. Those exist because we want the
system to be sound, not because we want the customer to feel
policed.

The CUPID property tying both buckets together is *Domain-based*.
The system's vocabulary is honest about its purpose. We have
`RevocationResult` with three named cases, not a boolean. We
have `kid` and `RetiredAt`, not generic version numbers. We have
a "test license in production" denylist, not a "fraud detection"
subsystem. The words match the concepts. When something goes
wrong, the customer's error message speaks the language of the
actual situation.

## Where to go next

The companion mechanics page,
[how MMP.Licensing works](./how-licensing-works.md), is the
prerequisite for everything above. If something on this page
was unclear, that page probably grounds it.

For the engineering rationale, read
[ADR-0001](../../../../MMP.Licensing/docs/adr/0001-mmp-licensing-architecture.md):
the trade-offs we considered, the alternatives we rejected, and
the design decisions recorded with their reasons.

For the byte-level wire format, read
[token-format-v2.md](../../../../MMP.Licensing/doc/token-format-v2.md):
exact field names, allowed values, signature conventions.
