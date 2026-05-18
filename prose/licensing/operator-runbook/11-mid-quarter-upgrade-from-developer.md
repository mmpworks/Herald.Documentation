---
title: Mid-quarter upgrade from Pro Developer to Pro Team
slug: operator-runbook/11-mid-quarter-upgrade-from-developer
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: published
phase: B
last-reviewed: 2026-05-18
related:
  - prose/licensing/operator-runbook/02-issuing-a-license.md
  - prose/licensing/operator-runbook/05-when-a-customer-asks-for-more-licenses.md
  - prose/licensing/operator-runbook/12-removing-the-demo-tag-after-upgrade.md
---

# Mid-quarter upgrade from Pro Developer to Pro Team

> :information_source: **Not shipped yet.** This article covers
> a flow that lands in **Phase B** of the licensing rollout —
> Pro Team rename, Stripe tiered curve, and the upgrade-from-
> Developer path. The runbook is here so the eventual launch is
> smooth, but the portal does not yet support every step below.
> Until Phase B ships, treat upgrades as a manual sales-driven
> sequence (issue a Team license alongside, walk the customer
> through swapping files).

Pro Developer customers who want to upgrade to Pro Team can do
so any time. This is one of the most common upgrade paths
because the free tier is designed to convert — a customer at
the 3-instance cap who needs a 4th instance has self-selected
into being a Pro Team customer.

This article walks through the upgrade from the operator side.
The customer side of the upgrade is mostly self-service in
their dashboard; this is what *we* do when their upgrade lands
in our queue or when they ask for help.

> :bulb: **Quick picture.** Mid-quarter upgrade is like
> switching from a free trial to a paid plan on day 47 — the
> trial doesn't pretend you started over, and the paid plan
> doesn't make you re-do the setup. The customer's existing
> instances stay where they are, the Demo tag goes away on the
> next check-in, and the bill starts at the upgrade date. The
> only operator job is to make sure the swap is clean.

## What "upgrade" actually means

The customer has a Pro Developer license file on each of their
existing instances (1, 2, or 3 of them). The upgrade does
three things:

1. **Issues a new Pro Team license file** under the same
   customer record.
2. **Marks the Pro Developer license as superseded.** The
   Developer file keeps working until the customer swaps it
   out, but the portal stops counting it as their primary
   license.
3. **The Demo tag stops appearing on events** at the next
   check-in *after the new file is installed*. Article 12
   covers the Demo-tag-specific mechanics.

The upgrade is not a cap raise on the existing license. Pro
Developer is structurally capped at 3 instances and stamps
the Demo tag on every event — those are the architectural
shape of the free tier, not knobs the portal lets you turn
off. The upgrade is a *different license file* for a different
segment.

## Before you start

Confirm three things:

- **Sales has approved the upgrade.** Pro Team isn't free; the
  customer needs a paid Stripe relationship. Sales handles
  payment setup, then signals you to proceed.
- **The customer knows the swap is happening.** The customer
  needs to install the new file on each of their instances.
  If they're surprised when the Demo tag disappears and the
  invoice arrives, that's a bad day on support.
- **You know the new instance count.** Often the same as their
  Developer count (1–3). Sometimes the upgrade comes with
  growth ("we're upgrading and we want 10 instances now");
  use the sales-provided number.

## The steps

### Step 1 — issue the Pro Team license

1. Open the customer's detail page.
2. Click **Issue new license**. (You're not adjusting the
   existing Pro Developer license — you're creating a new
   one. The portal supports both alongside each other during
   the swap.)
3. In the form:
   - **Product** — Pro
   - **Segment** — Team
   - **Instance count** — what sales told you (1–25 stays in
     Team; anything 26+ skips to Fleet — see article 09)
   - **Start date** — today, unless sales told you otherwise
   - **End date** — one year out (or whatever the contract
     specifies)
   - **Notes** — paste the sales order number plus a
     one-liner: "Upgrade from Pro Developer (account-bound
     license #<id>) on <date>"
4. Click **Issue license**, download the file.

### Step 2 — email the file with the upgrade-specific template

Use the **Upgrade from Developer** template in the portal's
email-template list. It differs from the regular Pro Team
issuance template in three places:

- **Acknowledges the upgrade.** "Thanks for upgrading from Pro
  Developer to Pro Team." Sets the tone.
- **Explicit swap instructions.** "Replace your existing
  Developer license file on each instance with the attached
  Team file. The path is the same. Your existing instances
  keep running through the swap." Customers who've never
  swapped a license file before need this spelled out.
- **Demo-tag-disappearance heads-up.** "Once the new file is in
  place, the `LicenseTier: Demo` property stops appearing on
  events at the next check-in." This is the question the
  customer is most likely to ask in week 1, so we answer it
  before they ask.

### Step 3 — mark the Pro Developer license as superseded

1. Back on the customer's detail page, find the Pro Developer
   license in the **Licenses** list.
2. Click **Mark superseded**.
3. The portal asks you to confirm and pick the new license it's
   being superseded by — select the Pro Team license you just
   issued.
4. The Developer license stays usable for 30 days as a fallback
   in case the customer's swap doesn't go cleanly. After 30
   days the portal stops accepting check-ins on the Developer
   file. (Plenty of time for any reasonable swap.)

### Step 4 — log the upgrade

Add a note on the customer record: "Upgraded Pro Developer
(license #<old>) to Pro Team (license #<new>) on <date>, sales
order #<order>." The next operator will use this when the
customer asks "did we still have Developer last quarter or
were we already on Team?"

## What the customer experiences

In sequence:

1. Email arrives with the new Pro Team license file.
2. The customer's IT team replaces the old file on each
   instance. (One file swap per instance, no software restart
   usually needed.)
3. Each instance picks up the new file at the next check-in
   (within 24 hours).
4. The Demo tag stops appearing on events emitted *after* the
   new file is loaded. Old events in their observability tool
   still show the tag — that's history, not a bug.
5. The next invoice from Stripe shows Pro Team pricing,
   prorated to the upgrade date.

For an upgrade where the customer is also growing (going from
3 Developer instances to 8 Team instances), the same flow
applies. The 5 new instances pick up the Team file from
day one; the 3 existing instances swap their file at the
customer's pace.

## When the upgrade gets stuck

A few common stuck states:

### "I installed the file but I still see the Demo tag."

Two possibilities:

- **They installed the file but didn't restart the load.** Some
  customer setups load the license file at startup. The file
  is in place, but the running process is still using the old
  one. The next check-in still reports Developer. Tell them
  to restart, or wait for the next natural restart.
- **They installed the new file on some instances but not all.**
  The instances still running Developer still emit the Demo
  tag. Ask them to confirm all instances got the swap.

If both are ruled out, hand to article 12 (Demo tag persistence
diagnostics).

### "The new file doesn't work."

Walk article 08's four-cause script. Most "doesn't work" after
an upgrade is a path mistake (cause 1) or a wrong-product
mistake (cause 2).

### "Can we go back to Developer?"

Yes, the customer can downgrade. It's rare and almost always
followed by a cancellation conversation. Hand to sales — they
should be in the loop before you re-issue a Developer license
to a customer who was paying yesterday.

## What NOT to do

> :warning: **Don't try to raise the Pro Developer cap.** The
> 3-instance cap is structural — it's part of the free tier
> shape, not a configurable limit. Even if you could (you
> can't), the Demo tag would still appear on every event
> because the tag mechanism is paired with the segment, not
> with the cap. Upgrade is the only path; don't promise the
> customer a "Developer with 5 instances" workaround.
> Internally that doesn't exist.

> :warning: **Don't issue Pro Team without sales approval.**
> Pro Team is paid. An operator-issued Team license without
> Stripe billing in place is hard to recover from — the
> customer has the file, they're running on it, and now sales
> has to ask for payment after the fact.

## What about Compliance during upgrade?

Compliance can be attached to the new Pro Team license at the
same time. Just include the Compliance attach in step 1 (in
the **Issue new license** form, the Compliance Pack section).
Sales should have told you whether the upgrade comes with
Compliance — if you're not sure, ask.

If the customer asks for Compliance after the upgrade, that's
the normal Compliance-attach flow (see article 02's Compliance
section).
