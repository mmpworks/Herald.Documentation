---
title: Auto-rollover from Pro Team to Pro Fleet
slug: operator-runbook/09-auto-rollover-team-to-fleet
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: published
phase: B
last-reviewed: 2026-05-18
related:
  - prose/licensing/operator-runbook/05-when-a-customer-asks-for-more-licenses.md
  - prose/licensing/operator-runbook/07-reading-the-portal-status-page.md
  - prose/licensing/operator-runbook/11-mid-quarter-upgrade-from-developer.md
---

# Auto-rollover from Pro Team to Pro Fleet

> :information_source: **Not shipped yet.** This article covers
> a flow that lands in **Phase B** of the licensing rollout —
> the Pro Team rename and the Stripe tiered curve ($79 → $59 →
> $39 with the Fleet auto-rollover at instance 26). The runbook
> is here so the eventual launch is smooth, but the portal does
> not yet support every step below. Until Phase B ships, treat
> Team→Fleet adjustments the way article 05 used to: a manual
> conversation with sales. See `prose/licensing/explanation/`
> for the current state.

When a Pro Team customer crosses 25 instances, they roll into
Pro Fleet at the published $39 per-instance rate (with a $10K
annual floor). No sales call required. This is one of the
biggest "no negotiation needed" changes the new SKU lineup
introduced, and it removes most of the math the operator team
used to do by hand.

This article walks through what the rollover looks like on the
portal side, what the customer sees, and the rare cases where
you still need to step in.

> :bulb: **Quick picture.** Auto-rollover is like a phone plan
> that quietly upgrades you when you add a fifth line. The
> phone company doesn't ring you to "discuss your options" —
> they just add the family-plan discount because you crossed
> the threshold the published price card says you would. You
> see it on your next bill. No surprise, no sales pressure, no
> negotiation theater. That's the shape we want here.

## When the rollover fires

The portal triggers the rollover at the moment a Pro Team
customer's **issued instance count** crosses from 25 to 26 (or
higher). The trigger is on **issued count, not active count** —
the customer's purchase intent, not their current usage.

Two paths get to 26+:

- **Operator-driven.** An operator (you) is in the **Adjust
  license** form for a Pro Team customer and types a number
  greater than 25. The portal shows the rollover banner and
  asks you to continue. (See article 05, Branch C.)
- **Self-service in the customer dashboard.** If the customer
  buys additional instances through the self-service flow on
  their dashboard, the same threshold applies. The portal
  rolls them over without operator involvement and posts an
  activity-feed row.

In both paths, the same things happen:

1. The license segment changes from Pro Team to Pro Fleet.
2. The customer's next invoice from Stripe reflects the new
   per-instance rate ($39 for instances 26+, $59 for 2–25,
   $79 for instance 1). Stripe handles the tier math.
3. A `Team rolled to Fleet` row lands in the recent activity
   feed.
4. The status-page badge "Crossed Fleet threshold this week"
   ticks up by one.
5. The customer's primary contact gets an automated email
   telling them their plan changed and why.

## What the customer sees

The customer gets one email and one invoice change. Neither
should surprise them if you (or the self-service flow)
confirmed before the click.

The email is short and reads roughly:

> Your Pro Team license has rolled into Pro Fleet because you
> added an instance past the 25-instance Team band. Your
> per-instance rate from instance 26 onward drops to $39, with
> a $10K annual minimum on the Fleet plan. Nothing changes for
> you operationally — your instances keep running, your
> license file is unchanged. Your next invoice reflects the
> new plan name and the tiered pricing. Questions?
> support@mmpworks.com.

The license file itself **does not need to be re-issued for the
rollover**. The customer's existing file already authorizes the
new instance count (because the rollover happened *because* the
operator or self-service raised the cap). The segment label on
their portal page and on their invoice changes; the file on
their instances doesn't.

> :information_source: **Heads up** — this is different from
> the instance-count adjust flow, which re-issues the file.
> The auto-rollover is a *pricing* event, not a *capability*
> event. The capability change already happened when the cap
> was raised.

## When you, the operator, need to step in

Most rollovers run themselves. These are the rare cases where
the team needs an actual operator in the loop.

### The customer's account isn't ready for Fleet billing

If Stripe rejects the new per-instance rate change (usually
because the customer's payment method is failing, expired, or
on hold), the portal won't complete the rollover. The customer
shows up on the **Payment failed** red badge instead.

In that case:

1. The license stays at Pro Team on the portal until billing is
   resolved.
2. The customer's instances keep running under their existing
   cap (the new instance over 25 may or may not check in
   depending on when the operator-side cap raise happened —
   see "the half-rolled state" below).
3. Sales takes the customer conversation. You don't act on the
   portal side until sales tells you the billing is fixed.

### The half-rolled state (cap raised, billing failed)

Possible footgun: an operator raises the cap from 22 to 28 in
the **Adjust license** form, the cap raise succeeds (so the
customer's 28th instance can check in), but the billing tier
change fails on the Stripe side. The customer is now running
on Fleet capability with Team pricing.

The portal flags this with a red badge **Half-rolled**. The
fix is always sales-first: get billing sorted, then click
**Complete rollover** on the customer's detail page. Don't try
to "undo" the cap raise — the customer is already running on
the new instances and pulling the rug out causes downtime.

### Direct-Fleet issuance (customer wants Fleet from day one)

If sales sells a brand-new customer 50 instances of Pro on day
one, that customer starts at Pro Fleet without rolling through
Team. The portal supports this through the **Issue new
license** form (see article 02, Pro Fleet section).

There's no rollover event in this case because there's nothing
to roll *from*. The customer just starts at Fleet. No badge,
no activity-feed row for "rolled."

### The customer asks to roll *back* to Team

Rare but it happens. A Pro Fleet customer drops to 20 instances
during a downsize and asks if they can go back to Pro Team
pricing.

The portal supports this as a **downgrade-rollover**. The
mechanics are the mirror image:

1. Confirm with sales first. Renewal pricing is affected.
2. In the **Adjust license** form, type the new total (say
   20).
3. The portal shows: *"This change drops below 26 instances.
   The license will roll back to Pro Team with the
   $79/$59-per-instance rate. The $10K Fleet floor no longer
   applies. Continue?"*
4. Email the customer first, get the explicit yes, then click
   continue.

The mirror-image email saves a surprised support ticket. The
Fleet floor no longer applies, but the per-instance rate also
goes up.

## Why we don't make a sales call on the rollover

Worth being explicit about, because it's a culture change.
Auto-rollover defuses regret-aversion at the Fleet boundary —
the customer who'd otherwise stall at 24 instances ("if I add
one more do I trigger a sales call?") just adds and gets the
discount. That's the whole point of publishing the price curve.

The customer who *wants* a sales conversation (because they
have questions about Fleet, or Compliance, or Provider) still
gets one — they just have to ask. The default isn't "we'll
call you."

Don't make a sales call when a customer rolls over unless they
asked for one. The published curve is the deal.

## When the badge looks wrong

The "Crossed Fleet threshold this week" yellow badge is a
counter, not a worklist. Most days the number is small (one or
two customers). If you see a sudden jump (say 12 customers in
a week), that's worth flagging in #licensing-ops — usually it
means a sales push or a product release drove growth, but
occasionally it means a portal bug or a Stripe-side hiccup is
mis-categorizing customers.

A badge that won't clear after the week ends usually means a
rollover got stuck halfway (the **Half-rolled** scenario
above). Click the badge to see the affected customers and
walk each one with sales.
