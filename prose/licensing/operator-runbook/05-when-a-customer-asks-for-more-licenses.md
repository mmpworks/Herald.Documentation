---
title: When a customer asks for more licenses
slug: operator-runbook/05-when-a-customer-asks-for-more-licenses
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: published
last-reviewed: 2026-05-18
related:
  - prose/licensing/operator-runbook/02-issuing-a-license.md
  - prose/licensing/operator-runbook/07-reading-the-portal-status-page.md
  - prose/licensing/operator-runbook/09-auto-rollover-team-to-fleet.md
  - prose/licensing/operator-runbook/11-mid-quarter-upgrade-from-developer.md
---

# When a customer asks for more licenses

The customer hit their cap. They paid for 20 instances, they want
to run 30, and they're emailing you to make it happen. An
**instance** is one installation on a server or one spun-up cloud
VM — same unit across every product.

This article walks through the math, the portal change, and the
handoff to sales for billing. The good news: the new SKU lineup
auto-rolls Pro Team into Pro Fleet at 26 instances, so most of
the math you used to do by hand now happens by itself. Your job
is to confirm the customer's segment and click the right button.

> :bulb: **Quick picture.** Adding more instances used to mean a
> negotiation: how many, what discount, when does the contract
> reset. The new Pro lineup turned the common path into a
> conveyor belt — the customer adds instances, the system
> recalculates the bill at the published rate, and nobody has to
> pick up the phone unless the customer crosses into Provider or
> Enterprise. The harder calls (Provider, Enterprise) still need
> sales; the easy calls run themselves.

## Step 1 — confirm the instance math first

Before you change anything, make sure the request lines up with
what they're actually using.

1. Open the customer's detail page.
2. Look at **Active instances** versus **Instances allowed**.
   - If it says "20 of 20 in use," they're at the cap. Their
     request makes sense.
   - If it says "14 of 20 in use," ask first. They might be
     planning ahead for next quarter (fine), or they might have
     forgotten they freed slots last week.
3. Look at the **Active instances** tab. Are there any stale
   entries that should be cleaned up first?
   ([Handling a stuck server slot](./03-handling-a-stuck-server-slot.md)
   covers this.)

> :bulb: **Why?** Sometimes the customer doesn't need more
> instances — they need stale slots cleaned up. If you can solve
> their problem without adding cost, do it. Don't sell them
> instances they don't need.

## Step 2 — figure out which segment they're in (or moving to)

This is the part that changed. The portal now branches on segment.

1. Look at the **License** row on the customer's detail page. It
   shows their current segment — Pro Developer, Pro Team, Pro
   Fleet, Pro Provider, or Pro Enterprise.
2. Add the requested instances to their current count to get
   their *new* total. (If they have 20 and want 10 more, that's
   30.)
3. Find the matching branch below and follow it.

### Branch A — Pro Developer asking for more

Pro Developer is locked at 3 instances. If a Pro Developer
customer is asking for a 4th, that's an upgrade, not an
adjustment. Hand them to article 11 (mid-quarter upgrade from
Developer). Don't try to raise the cap from 3; the portal won't
let you, and even if it did, the Demo tag would still be on every
event because Demo is the architectural shape of the free tier.

### Branch B — Pro Team staying in Team (new total 1–25)

This is the easy path.

1. Click **Adjust license** on the Pro Team row.
2. Update **Instance count** to the new total (not the
   increase). If they had 20 and want 10 more, type 30.
3. Leave **End date** alone unless sales told you to change it.
4. In **Notes**, add a line: "Added 10 instances per sales order
   #12345 on 2026-05-18."
5. Click **Re-issue license**, download the new file, email it
   to the primary contact (use the template — see article 02 for
   the email shape).

Stripe handles the per-instance billing automatically. Instance 1
stays at $79; instances 2–25 are $59 each. The customer's next
invoice reflects the new count. No sales call needed for this
range.

### Branch C — Pro Team crossing into Pro Fleet (new total 26+)

This is the auto-rollover path. The customer is still on Team in
the portal today, but their request takes them past 25.

The portal handles the rollover for you, but **you should
confirm with the customer first** so they're not surprised by the
Fleet name appearing on their invoice.

1. Click **Adjust license** on the Pro Team row.
2. Type the new total (say 35).
3. The portal will show a banner: *"This change crosses 25
   instances. The license will roll into Pro Fleet at the
   per-instance rate of $39 from instance #26, with a $10K
   annual floor. Continue?"*
4. Before you click continue, send the customer a one-paragraph
   email: "Hi <name>, the change you asked for takes you past 25
   instances, which moves you to our Pro Fleet plan. The per-
   instance rate drops from $59 to $39 starting at instance #26.
   There's a $10K annual minimum on Fleet, so even at 26
   instances you'll be at the floor. Want me to proceed?"
5. When the customer replies yes, click continue.
6. The portal re-issues the license under the Pro Fleet name.
7. Tell sales the rollover happened so the Stripe side reconciles
   cleanly.

Article 09 covers the auto-rollover flow end-to-end if you want
the longer walk-through.

### Branch D — Pro Fleet adding more (staying in Fleet)

Same as Team — adjust, re-issue, email. Fleet has no upper bound
inside Pro; very large customers just pay the $39 rate on each
additional instance. The $10K floor is already met by anyone in
Fleet, so the math just adds.

When a Fleet customer crosses into "this is starting to look
like Enterprise" territory, that's a sales conversation, not a
portal one. Rough thresholds:

- 200+ instances → flag to sales for an Enterprise check-in
- Adds an unusual support need (24/7, on-call escalation) →
  same flag
- Adds Compliance + multi-region + audit + custom support →
  same flag

The Fleet → Enterprise jump is not auto. It's intentional that
sales has to be in the room for it.

### Branch E — Pro Provider needs metered reconciliation

Provider is the segment where adding instances isn't just a
number on a form. Provider check-ins include
`activeTenantSlugs[]` — the list of *their* customers they're
serving. The bill is metered, not flat.

When a Provider asks for more instances:

1. Confirm with sales first. Provider growth is a Stripe
   metered-billing reconciliation, not a single-click adjust.
2. Once sales is in, click **Adjust license** on the Pro
   Provider row.
3. Raise the instance count.
4. The portal will prompt: *"Provider licenses are metered.
   Confirm the new instance ceiling and the billing reconciles
   on the next cycle. Continue?"*
5. Click continue, re-issue, email, log.

If the Provider is also onboarding new MSP customers (new
`activeTenantSlugs`), that's worth a note in the customer record
so the next operator has context.

### Branch F — Pro Enterprise asking for more

Always sales. Enterprise is custom from the start; instance
changes mid-term are part of the contract negotiation. Don't
adjust an Enterprise license without an explicit "yes, do this"
from the account owner on the sales side. Then follow the same
steps as Team — adjust, re-issue, email, log.

## Step 3 — confirm with sales (depending on segment)

The sales handoff depends on which branch you just walked:

- **Branch A (Developer → upgrade):** Hand the customer to
  sales. Use article 11.
- **Branch B (Team stays Team):** No sales call. Stripe handles
  it. Just log the change.
- **Branch C (Team → Fleet):** Tell sales the rollover happened.
  No approval needed (the curve is published), but they should
  know for the relationship.
- **Branch D (Fleet stays Fleet):** No call unless the customer
  crossed any of the sales-attention thresholds (200+, custom
  support, etc.).
- **Branch E (Provider metered):** Sales confirms first.
  Metered reconciliation is their lane.
- **Branch F (Enterprise):** Sales drives. You execute after
  their nod.

## What the customer experiences

When the customer drops the new file on each of their
instances, the next check-in picks up the higher cap. Their
dashboard updates, the cap warning clears, and their new
instances can join.

If they install the new file on some instances but not others,
the ones with the old file keep working under the old cap until
they get the new file. There's no scary failure — just a slow
rollout on their side.

For Pro Fleet auto-rollover, the customer sees one extra thing:
the segment name on their invoice changes from "Pro Team" to
"Pro Fleet" at the next billing cycle. The portal banner
prepares them; the email you send during step 2C reinforces it.

## When the customer wants to add a different product

That's a new license, not an adjustment. If they had Pro Team
for 20 instances and want to add Compliance, attach Compliance
as an add-on to their existing Pro license — see the Compliance
section in [issuing a license](./02-issuing-a-license.md).
Compliance does not need its own license file.

If they want to add an entirely separate Pro line (say their
parent company runs one Pro Team and a subsidiary wants its own
Pro Team), that's two customer records with two licenses. Don't
try to bundle.

## When the customer wants fewer instances (downgrade)

This is rare but it happens. Treat it the same as adding, just
in reverse:

1. Confirm with sales first. Downgrades affect renewal pricing
   and sometimes the segment changes (a Pro Fleet dropping to
   24 instances goes back to Pro Team, which the portal handles
   on re-issue).
2. Adjust the instance count down.
3. Re-issue, email, log.

The customer's existing instances above the new cap will stop
checking in once the new file is installed. Warn the customer
to retire their lowest-priority instances first.

> :warning: **Downgrade gotcha.** If a Pro Fleet customer drops
> to 25 or fewer instances, the portal will offer to move them
> back to Pro Team. The Stripe per-instance rate changes from
> $39 back to $79/$59. That's correct behavior — Fleet is a
> growth plan, not a permanent home. But the customer should
> know before the next invoice arrives. A one-line email saves
> a surprised support ticket.
