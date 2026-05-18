---
title: Turning off a license
slug: operator-runbook/06-turning-off-a-license
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: published
last-reviewed: 2026-05-17
related:
  - prose/licensing/operator-runbook/04-investigating-a-collision-warning.md
  - prose/licensing/operator-runbook/02-issuing-a-license.md
---

# Turning off a license

Sometimes a license has to be turned off. The customer cancelled,
the customer abused the agreement, payment failed and the grace
period ran out, or the customer asked us to retire an old license
they're not using anymore.

This is rare. Most operators do it once a quarter, not once a
week. Because it's rare and the impact reaches the customer, the
checklist matters more than the click.

## What "turning off" actually does

When you turn off a license, two things happen:

1. **The license is marked off in the portal.** No new instances
   can check in using it — an instance being one installation on a
   server or one spun-up cloud VM. New check-ins get rejected.
2. **The existing instances stop working at their next 24-hour
   check-in.** Not immediately. The customer's running instances
   keep working until each one tries to check in again, which
   happens once a day per instance.

> :bulb: **Why the 24-hour delay?** Two reasons. The first is
> kindness — if a turn-off was a mistake, you have a window to
> undo it before the customer notices. The second is operational
> — taking down a running production system without warning is
> never the right move, even when the customer hasn't paid. The
> 24-hour window gives them time to download an invoice and pay,
> or for sales to call them, before anything breaks.

## Before you click

> :warning: **Wait — should I really do this?** Three things to
> confirm before turning off a license:
>
> 1. **Sales has signed off.** A "cancel" email from the customer
>    is not enough. Sales needs to acknowledge the cancellation
>    and close the account on their side first. Otherwise you turn
>    off a customer sales is still trying to save.
> 2. **The customer has been told.** They should know this is
>    happening, either from a cancellation confirmation email or
>    from a payment-failure notice. Surprise turn-offs lead to
>    angry calls.
> 3. **You know which license.** A customer can have several
>    licenses (Pro, Compliance, etc.). Make sure you're turning
>    off the right one. Read the product name twice.

If any of the three are missing, stop. Send a note to
#licensing-ops and let the lead make the call.

## The steps

1. Open the customer's detail page.
2. Find the license you're turning off in the **Licenses** list.
3. Click the **Turn off** button on that row.

   ![TBD: turn-off confirmation dialog screenshot]

4. The portal shows a confirmation dialog with three things you
   have to fill in:
   - **Reason** — pick from the dropdown (cancellation, abuse,
     payment failure, customer request, mistake).
   - **Reference** — the sales order number, the support ticket
     number, or the customer email subject. Anything that lets
     the next operator find the paper trail.
   - **Notify customer** — usually checked. Unchecks only if the
     customer already knows and another email would be noise.
5. Type the customer's company name in the confirmation box (the
   portal makes you type it to prevent accidents).
6. Click **Confirm turn-off**.

## What happens after

- The license shows **Off** on the customer's detail page.
- The customer's instances continue running until their next
  check-in (within 24 hours), then they stop accepting new
  events.
- If you checked **Notify customer**, an email goes to the primary
  contact telling them the license has been turned off and listing
  the reason.

## How the customer hears about it

Two paths:

- **The email we send.** Goes to the primary contact within a few
  minutes.
- **Their instances refusing to work.** Within 24 hours, their
  instances stop processing the protected product features. The
  customer's monitoring usually catches this first.

We hope they see the email before the instances stop, but we can't
count on it. That's why sales should have already had the
conversation.

## Undoing it (you turned it off by mistake)

It happens. Most of the time, undoing is fast:

1. Open the customer's detail page.
2. Find the turned-off license in the **Licenses** list.
3. Click **Restore**.
4. Confirm.

The license is active again immediately on our side. The
customer's instances pick the change up at their next check-in
(within 24 hours).

If you undo within an hour and the customer hasn't noticed,
you're fine. Add a note ("turned off by mistake at 14:02,
restored at 14:08") so the audit trail is clean.

If the customer already noticed and is on the phone, restore
first, apologize honestly ("we made a mistake on our side, your
license is back on"), and don't dress it up. Customers forgive
mistakes when they're owned. They don't forgive cover-ups.

## When you cannot undo

The portal won't let you restore a license that's been off for
more than 90 days. By that point, the customer record might have
moved through other cleanup and a restore could create stale
data. If a customer comes back after 90 days, treat it as a new
license — go to [issuing a license](./02-issuing-a-license.md).
