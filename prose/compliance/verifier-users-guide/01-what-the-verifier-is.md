---
title: What the verifier is
slug: verifier-users-guide-01-what-it-is
surface: compliance
category: verifier-users-guide
section: 1
audience: auditor-or-it-operator
version: 2026-05-21
last-reviewed: 2026-05-21
diagrams:
  - ../../../diagrams/compliance/verifier-users-guide/D1-input-output-story.svg
related:
  - prose/compliance/verifier-users-guide/02-what-it-proves.md
  - prose/compliance/audit-trail-comparison/closing.md
  - https://github.com/mmpworks/ffiec-public/blob/main/spec/chain-of-custody-DRAFT-0.2.0.md
---

# What the verifier is

The verifier is a small program. It reads a chain file and tells you
whether the chain is authentic, in a line you can read or a script can
parse. You point it at the file, you point it at a public key, you run
it, you read the answer. That is the whole tool.

The chain file is the bank's tamper-evident record of every
consequential AI decision it made on a given day. The verifier is the
independent check that confirms the record is what the bank says it is.
The bank does not need to be in the room. The verifier reaches the same
answer in a coffee shop on hotel wifi as it does inside the bank's
data centre.

> **Quick picture.** Imagine the bank keeps every important decision in
> a bound book. Each page is stamped to the page before it. At close of
> business, a notary presses one big wax seal across the day's pages
> with a signet held in a safe. The signet's pattern is published on the
> wall outside the building.
>
> The verifier is the examiner with a magnifying glass walking the book.
> It confirms each stamp, recomputes the wax pattern from the pages,
> and compares the seal's imprint to the pattern on the wall. It uses
> only what the bank has already published, so the bank's cooperation
> ends at handing over the book.

## What you give it

Three things, in the simplest case:

- **The chain file.** A single file the bank produces for the period
  you are examining. The bank's chain-operations team knows how to
  produce it. On disk it is one binary file. Bring it on a USB stick
  or mount it read-only from the bank's evidence share.
- **The bank's public key.** A small text file (a PEM file, around 100
  bytes of base-64). The bank publishes this key on its public
  compliance page. The regulator has the key's fingerprint on file.
- **The bank's tenant ID.** A short string like `tenant_acme_prod_us_east_1`
  that names which tenant the chain file belongs to. The chain file
  carries the tenant ID in its header. You pass the same string on
  the command line so the verifier refuses to accept a file from a
  different tenant.

A fourth optional input, the bank's master key (called the IKM),
turns on a deeper per-event check. Most examinations do not need it.
Section 3.4 explains when it matters.

## What you get back

One line, on standard output, in a fixed shape:

```
Status: PASS
Step: 7
Reason: chain verified
```

Or, when something is wrong:

```
Status: FAIL
Step: 9
Reason: payload_hash MAC mismatch at seq 142
```

The `Status` field is one of `PASS` or `FAIL`. The `Step` field is the
number of the step in the verification procedure that produced the
result (steps 1 through 12, defined in the spec's §7). The `Reason`
field is the short human-readable explanation. A fourth field, the
`Verdict-Object`, follows on its own line and carries the same
information in a structured form a script can parse. Section 6 walks
through it.

The program also returns an exit code. Exit code 0 means the chain
verified. Exit code 1 means it did not. Your shell or your harness
can branch on that signal without parsing any text. Section 6 covers
all four possible codes.

## Why a separate program

Three properties the design earned on purpose. Each one is one
example of CUPID's *Predictable* property in action, and together
they are why you can trust the answer.

**The verifier is offline.** It does not call any server. It does
not look up anything on the internet. It reads the files you give
it on the command line and produces the answer. The full list of
trusted inputs is the binary, the chain file, the public key, the
tenant ID, and (optionally) the master key. Nothing else can change
the result.

**The verifier is deterministic.** Same chain file plus same public key
plus same tenant ID produces a byte-for-byte identical output. Two
examiners can run the verifier on different laptops and compare the
output by hash. If the hashes match, the runs agree.

**The verifier is independent of the institution.** Once the bank has
handed over the chain file, the bank's cooperation is no longer
required. The bank cannot dispute the math. The bank cannot refuse
to be present at the re-run. The bank can disagree with the verdict;
the verdict does not change because of the disagreement.

> **Quick picture.** Treat the verifier the way you treat a calculator.
> Same numbers in, same answer out. The calculator does not call the
> bank to ask whether the bank prefers a different answer.

## What "the verifier" actually means

Three reference implementations exist. They produce the same verdict
on the same input because they all implement the same §7 procedure
against the same chain format. Section 4 covers how to choose between
them; the short version is that the choice depends on where you are
running, not on what you are verifying.

- **The Go reference** is a single static executable with no
  dependencies. This is what most examiners run. It is the default
  whenever the trusted-computing-base needs to be as small as
  possible, including examiner laptops and air-gapped deployments.
  One binary, one set of command-line arguments, no configuration
  files. (Product name pending Steve's pick — Pearl's collision
  sweep ruled out the round-1 candidate; round-2 disambiguation in
  progress.)
- **Herald.Compliance** is the .NET reference. The verifier embedded
  inside the bank's own Herald pipeline. Banks running
  Herald.Compliance can verify their own chain in-process as part of
  normal operations. Daily seal verification, pre-export smoke-tests,
  and integration into the bank's internal control framework all use
  the same verdict surface.
- **Visus** is the Python reference. The verifier embedded as a
  library inside Python pipelines. Same verdict surface, invoked
  through a Python API or a small wrapper script.

All three produce the same `Status` / `Step` / `Reason` /
`Verdict-Object` surface and the same §10.12 exit codes. The
verdict for a given chain file is the same regardless of which
implementation you ran. That is the DRY discipline the spec
imposes on the implementations. One normative procedure, one
output shape, three independent code paths that must converge.

## What the verifier does not do

The verifier proves that the record is authentic. It does not prove
that the AI's underlying decision was correct.

If the bank's AI agent denied a loan, the verifier can confirm that
the denial was recorded exactly as it happened, that no one changed
the record afterwards, and that the record was sealed under the
bank's published key. The verifier cannot tell you whether the
denial was the right call. That question belongs to model-risk
review and fair-lending analysis, and ultimately to the bank's
internal control framework. None of those things are what the
verifier checks.

The distinction is what the whole chain-of-custody discipline rests
on. The spec says it plainly in §1.2: the chain proves what the AI
said, not whether what the AI said was correct. Section 2 walks
through the distinction in more detail. The rough shape to hold
onto is that the verifier is an integrity check, not a correctness
check.

## Where to go next

- **You want the five-minute orientation.** Read
  `ffiec/docs/examiner-quickstart.md`. It walks you from "what is
  this thing" to "I can produce a report" without reading the
  design docs.
- **You want to understand what the verifier proves and what it
  does not.** Continue to section 2.
- **You want to see the math.** Section 3 covers the four primitives
  in plain English. The deeper cryptographic material lives in the
  spec at §4.
- **You want to run the verifier right now.** Section 5 covers
  invocation. The Go reference's README at `ffiec/verifier/README.md`
  has the build and CLI reference. (The repository path will rename
  once Steve picks the locked product name.)
