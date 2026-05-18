---
title: Diagnosing a segment-claim mismatch
slug: operator-runbook/13-diagnosing-a-segment-mismatch
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: published
phase: A
last-reviewed: 2026-05-18
related:
  - prose/licensing/operator-runbook/08-what-to-do-when-a-customer-says-it-doesnt-work.md
  - prose/licensing/operator-runbook/11-mid-quarter-upgrade-from-developer.md
  - prose/licensing/operator-runbook/12-removing-the-demo-tag-after-upgrade.md
---

# Diagnosing a segment-claim mismatch

> :information_source: **Not shipped yet.** This article covers
> a flow that lands in **Phase A** of the licensing rollout —
> the `seg` claim is added to the v2 license payload as part
> of the Pro Developer work. The runbook is here so the
> eventual launch is smooth, but the portal does not yet
> support every step below. Glenn is implementing the `seg`
> claim addition right now in parallel.

A segment-claim mismatch means the customer's license file
declares one segment (`seg: team`) but their instances are
behaving as if they had a different one (`seg: dev`, for
example, with the Demo tag stamping events). Or the portal
shows the customer as Pro Fleet but their check-ins arrive
with `seg: team` in the file metadata.

This is rare — the file's `seg` claim and the portal record
should always match because the portal *issued* the file with
that claim. When they don't match, something diverged. This
article walks through finding the divergence.

> :bulb: **Quick picture.** The `seg` claim mismatch is like
> finding a credit card with one name on the front and a
> different name on the back's signature line. Both should
> have come from the same source — the bank — so one of them
> is either fake, stale, or accidentally swapped. The
> investigation is "where did each side come from, and which
> one is correct?"

## What the `seg` claim is

For background:

- Every license file has a `prd` claim (the tier — `pro`,
  `enterprise`, `tesseraseal`) and a `seg` claim (the
  segment — `dev`, `team`, `fleet`, `provider`, `enterprise`).
- The portal generates both claims at issue time. The values
  match what the operator picked in the **Issue new license**
  form.
- The customer's instances read the `seg` claim at startup
  and adjust behavior — most visibly, the Demo tag on
  `seg: dev`; less visibly, the metered billing payload on
  `seg: provider`.
- The portal also stores the issued `seg` value against the
  customer record. The check-in compares the file's `seg`
  against the stored value and flags a mismatch.

When the two don't match, **one of three things happened**:

1. The customer installed an older license file that has a
   different `seg` than their current one. (Most common.)
2. The portal's stored value got out of sync with what was
   actually issued. (Rare, indicates a portal bug.)
3. The license file was tampered with or corrupted on the
   customer's side. (Very rare; the IP-protected DLLs would
   reject a tampered file, so this almost always shows up as
   "license rejected" not "mismatch.")

## How a mismatch surfaces

The portal flags mismatches in two places:

- **Status page red badge** — **`Seg mismatch` (count)**.
  Each entry is a customer whose check-ins are arriving with
  a `seg` value different from what the portal expects.
- **Customer detail page** — a red banner across the top:
  *"This customer's instance(s) are checking in with `seg:
  team`, but the portal expects `seg: fleet`. Last seen:
  <date>. Investigate."*

The activity feed also gets a `Seg mismatch detected` row
when the mismatch first appears.

## The diagnostic

### Step 1 — confirm what the portal expects

1. Open the customer's detail page.
2. Look at the **License** row. The segment shown there is
   what the portal expects (the one the portal *issued* most
   recently).
3. Note the issue date of the current license file. If it's
   recent (within the last few days), the customer's
   instances might just be slow to pick up the new file —
   look at step 3.

### Step 2 — confirm what the file says

Ask the customer to run the license-inspect command on each
instance:

> Quick check — on each instance that's flagged, can you run
> this command and paste the output? It prints the `seg`
> claim from the currently-loaded license file.
>
> (Paste the product-specific license-inspect command from
> the support template.)

The customer pastes back per-instance output. Note the `seg`
each instance reports.

### Step 3 — match against the portal's expected `seg`

Three patterns, with three different fixes:

#### Pattern A — instance reports older `seg` than portal expects

Example: portal expects `seg: fleet` (the customer just
auto-rolled), but the instance reports `seg: team`.

Almost always means the customer's instance is still using
the older file. The new file is on our side; either it
wasn't sent to them or they haven't installed it. Check the
recent activity feed for the rollover event and the email
that was sent. Walk them through installing the new file.

After install + restart + next check-in, the mismatch
should clear automatically.

#### Pattern B — instance reports newer `seg` than portal expects

Example: portal expects `seg: team`, but the instance reports
`seg: fleet`.

This is unusual and indicates the portal record didn't update
when a license was re-issued. Check the activity feed for a
recent re-issuance — if there was one, the portal probably
should have updated the stored `seg` and didn't. Flag in
#licensing-ops; this is a portal bug, not a customer
problem.

In the meantime, the customer's instances are running on the
correct (newer) file. Don't take any action that disrupts
them — wait for the portal record to sync.

#### Pattern C — instance reports a `seg` that doesn't match any history

Example: portal expects `seg: team`, the instance reports
`seg: provider`, and the customer has never been a Provider.

This is the suspicious case. Three possibilities:

- The customer installed a license file from a different
  customer account by accident (someone's IT team grabbed
  the wrong file from a shared folder).
- A test environment is using a Provider-shaped file (maybe
  for a sandbox tenant) and it's leaking events into the
  production observability stream.
- Tampering. (Rare. The IP-protected DLLs would normally
  reject a hand-crafted file at startup, but if a customer
  managed to construct a valid-looking file, the mismatch is
  how it surfaces.)

For pattern C, **don't take action on the customer's behalf**.
Send an email asking which file is on the affected instance
and where it came from. Most of the time it's the cross-
account-mixup case (mundane) or the sandbox-leak case
(also mundane). If neither, escalate to the licensing-ops
lead.

## When you can't reach the customer

If the mismatch banner sits open for more than 3 business
days without a customer reply:

- For **Pattern A** (instance behind portal): leave it open.
  No urgency — the customer's instance is just using an older
  but still-valid file. The mismatch clears when they update.
- For **Pattern B** (instance ahead of portal): flag to
  licensing-ops if not already; portal bugs need follow-up.
- For **Pattern C** (unrecognized `seg`): escalate. Don't sit
  on a possible cross-account or tampering case for the full
  three days.

## What NOT to do

> :warning: **Don't re-issue a license file as your first
> move.** Re-issuance regenerates the file and resets the
> stored `seg` to whatever's in the form — which papers over
> the underlying problem instead of finding it. Re-issuance
> is the fix for Pattern A only, and only after the customer
> confirms the install path.

> :warning: **Don't override the portal's `seg` value
> manually.** There isn't a button for this in the operator
> portal. If there were, using it would mask Pattern B and
> hide the portal-side bug. If you find yourself wanting to
> "just edit the stored value to match what the instance is
> reporting," stop and post in #licensing-ops.

> :warning: **Don't treat all mismatches as suspicious.**
> Patterns A and B together cover 95%+ of mismatches and both
> are mundane (stale file or portal-sync bug). The reflex of
> "mismatch = abuse" leads to a lot of unfounded customer
> emails. Diagnose before you investigate.

## Why this exists

For the curious: the `seg` claim was added so the same
license schema could carry segment-specific behavior (Demo
tag, metered billing, MSP TOS) without splitting the schema
across multiple `prd` values. Keeping the `prd` claim at
tier granularity (`pro`, `enterprise`, `tesseraseal`) and
adding `seg` as a side-channel kept the binary verifier
simple — a `prd` mismatch is still "wrong product entirely,"
while a `seg` mismatch is "right product, wrong segment."

The mismatch check exists because the portal needs *some*
way to notice when its stored record disagrees with what the
customer is actually running. Without it, a Provider customer
running a Team file would never get billed on the Provider
metering — and we'd find out at a renewal review, six months
late.
