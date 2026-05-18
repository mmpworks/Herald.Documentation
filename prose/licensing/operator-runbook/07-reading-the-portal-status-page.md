---
title: Reading the portal status page
slug: operator-runbook/07-reading-the-portal-status-page
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: published
last-reviewed: 2026-05-18
related:
  - prose/licensing/operator-runbook/03-handling-a-stuck-server-slot.md
  - prose/licensing/operator-runbook/04-investigating-a-collision-warning.md
  - prose/licensing/operator-runbook/09-auto-rollover-team-to-fleet.md
  - prose/licensing/operator-runbook/11-mid-quarter-upgrade-from-developer.md
---

# Reading the portal status page

The status page is the first thing you see when you log in. It's
the operator's dashboard. This article is a short tour so you
know what each part means and which warnings need your attention
today.

![TBD: status-page screenshot, full view]

## The top counter

The big number at the top reads something like:

> **412 licenses active across 168 customers**

In plain English:
- **412 licenses** — how many license files we've issued that
  are still on. Counts Pro (all segments), Enterprise, and
  Compliance attaches.
- **168 customers** — how many companies hold at least one
  active license. Many customers have more than one license,
  which is why these numbers don't match.

The counter expands into a **sub-SKU breakdown** when you click
it. The breakdown shows how many licenses are in each segment:

| Segment | Count |
|---|---|
| Pro Developer | (free tier, perpetual) |
| Pro Team | (1–25 instances) |
| Pro Fleet | (26+ instances) |
| Pro Provider | (MSP redistribution) |
| Pro Enterprise | (custom contract) |
| Compliance Pack attached | (add-on count) |

Use the breakdown for two things: spotting where growth is
happening, and catching when a segment count drops unexpectedly.
A sudden drop in Pro Team usually means an auto-rollover wave
into Pro Fleet (good) but can also mean a cluster of
cancellations (worth investigating).

If either the top counter or any sub-count drops a lot from
yesterday, that's worth a glance. A drop usually means a bulk
cancellation or a portal issue — both worth flagging in
#licensing-ops.

## The recent activity feed

A scrolling list of everything that's happened in the last 24
hours. Each row shows:

- **Time** — when it happened.
- **What** — "license issued," "license adjusted," "slot freed,"
  "license turned off," "Team rolled to Fleet," "Provider TOS
  accepted," "collision warning raised," etc.
- **Who** — the operator who did it (or "system" if it was
  automatic, like an auto-rollover).
- **Customer** — which customer was affected.

You read the feed for two reasons:
1. **Catching up.** If you've been off for a day, the feed shows
   what the team did while you were out.
2. **Spotting weirdness.** If you see ten "slot freed" actions in
   a row for the same customer, something unusual happened —
   either a customer rebuilt their fleet or an operator went
   slot-freeing without confirming. Worth asking about.

## The warning badges

The right side of the page shows colored badges. Each badge is a
count of customers in a particular state.

### Yellow badges (look this week)

- **Collision warnings** — customers where two or more instances
  checked in from the same address. Most are innocent (see
  [investigating a collision warning](./04-investigating-a-collision-warning.md)),
  but you should sort through them within a few days and decide
  which to follow up on.
- **Near cap** — customers using 80% or more of their
  instances. These are often warmed-up upsell opportunities for
  sales. Flag to the sales channel if a customer crosses 95%.
- **Dev near 3-instance cap** — Pro Developer customers running
  2 or 3 instances. These are upgrade candidates. The free tier
  is doing what it's supposed to — getting the customer hooked
  — and now they're ready for Pro Team. Hand to sales for the
  upgrade conversation (see article 11 for the operator side of
  the upgrade flow).
- **Crossed Fleet threshold this week** — Pro Team customers
  whose instance count just crossed 25, triggering an
  auto-rollover into Pro Fleet. The rollover happens
  automatically; this badge is informational so sales sees the
  shift and the operator team can audit any that look unusual.
  Most of these need no action. (Article 09 covers the
  auto-rollover flow in detail.)
- **Grace days remaining** — customers whose license is past
  expiry but still working on a short grace window (usually 7
  days). They need to renew this week or they'll hit zero.

### Red badges (look today)

- **Payment failed** — sales billed but the payment didn't go
  through. Sales handles the customer conversation; you don't
  need to do anything in the portal until sales tells you to
  turn off the license.
- **Grace period expired** — license is past the grace window
  and the customer's instances are about to stop working.
  Confirm with sales whether to turn off or extend.
- **Abuse signal** — the portal's automatic checks flagged
  something that needs a human look. Always escalate to the
  licensing-ops lead. Don't act on these alone.
- **Provider TOS expired** — a Pro Provider customer's MSP
  click-through is past its renewal date. Their Provider
  license is still active but they need to re-accept the TOS
  before the next renewal cycle. See article 10.

### Green badge (informational)

- **All healthy** — no customers need attention. Some days
  you'll see this. Enjoy it.

> :bulb: **Why the colors?** Yellow means "look this week." Red
> means "look today." Green means "no action needed." The portal
> stays calm on purpose so red actually means red.

## What to do first when you log in

A simple morning routine:

1. Glance at the top counter. Big drop from yesterday? Flag in
   #licensing-ops.
2. Open the sub-SKU breakdown for 5 seconds. Anything in a
   segment look off?
3. Scan the red badges. Anything new? Handle it before moving on.
4. Scan the yellow badges. Pick one or two to sort through and
   decide on today. The "Dev near 3-instance cap" and
   "Crossed Fleet threshold this week" badges usually need no
   operator action but should be glanced at so sales has the
   context.
5. Skim the recent activity feed for anything weird.
6. Move to your inbox.

That's it. The status page is meant to be a 60-second check, not
a 30-minute deep dive.

## When something on the status page doesn't make sense

If you see a number or a badge that doesn't match what you
remember doing yesterday, **don't refresh and forget it**. Take
a screenshot, post it in #licensing-ops, and ask. The status
page is the operator team's shared source of truth — when it
drifts from reality, we want to catch it fast.
