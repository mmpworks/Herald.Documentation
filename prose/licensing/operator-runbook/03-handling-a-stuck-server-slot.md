---
title: Handling a stuck server slot
slug: operator-runbook/03-handling-a-stuck-server-slot
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: published
last-reviewed: 2026-05-17
related:
  - prose/licensing/operator-runbook/04-investigating-a-collision-warning.md
  - prose/licensing/operator-runbook/07-reading-the-portal-status-page.md
---

# Handling a stuck server slot

This is the most common support ticket you'll see. The customer
took down an old server but the portal still counts the instance
as active, so their new one can't check in. They need a slot freed
up. An **instance**, throughout the portal, is one installation on
a server or one spun-up cloud VM — same unit for every product.

This article walks through doing that safely. The walking part
takes 30 seconds. The "should I really do this?" check is the part
that matters.

> :bulb: **Quick picture.** Think of a customer's license like a
> small parking lot. If they paid for 50 instances, the lot has 50
> parking spots. Each running instance takes one spot. When they
> retire an old one, the spot is supposed to free up automatically
> — but sometimes the old instance didn't tell us it was leaving
> (it got powered off, the network went down, someone pulled the
> plug). The portal still thinks that spot is taken. Freeing the
> slot is the manual override that opens the spot back up.

## The steps

1. Open the customer's detail page.
2. Click the **Active instances** tab. You'll see a list of every
   instance currently holding one of their slots.

   ![TBD: active-instances tab screenshot]

3. Each row shows three things that help you spot the stale one:
   - **Instance name** — what the customer's IT team called it
     (often a hostname like `web-prod-03`).
   - **Last seen** — when this instance last checked in with us.
     Healthy instances check in every 24 hours. If "last seen" was
     three days ago, that instance is almost certainly gone.
   - **Internet address** — where the instance checks in from. Two
     instances checking in from the same address is a different
     issue, covered in
     [investigating a collision warning](./04-investigating-a-collision-warning.md).

4. Find the stale instance (long "last seen," matches what the
   customer described).
5. Click the **Free this slot** button on that row.
6. Confirm.

The portal removes that instance from the active list. The next
time the customer's new instance checks in, it gets the slot.

## Wait — should I really do this?

> :warning: **Wait — should I really do this?** Before you click
> **Free this slot**, get the customer to confirm two things:
>
> 1. **The instance name matches** what they retired. If they said
>    they tore down `web-prod-03` and the stale row says
>    `web-prod-07`, stop. Don't guess.
> 2. **They're sure it's actually gone.** An instance that's just
>    offline for an hour (rebooting, network blip) will check back
>    in and reclaim its slot. If you free it manually, the customer
>    ends up with a slot that flickers in and out — confusing for
>    them, confusing for the next operator looking at the history.

The safest exchange goes like this. Customer says "we retired
web-prod-03 yesterday but it still shows active." You look at the
list, find a row named `web-prod-03` with "last seen" 26 hours
ago, and reply: "I see it. Last check-in was 26 hours ago, which
lines up with what you described. Freeing it now — you should see
your new instance check in within the next 24 hours."

If the numbers don't line up, ask one more question before
clicking.

> :warning: **Check the SKU before freeing.** If the customer is on
> **Pro Developer** and sitting at their 3-instance cap, freeing a
> slot is the wrong answer — point them at the upgrade path. Pro
> Developer is the free tier; the cap is the product shape, not a
> stuck instance. Same goes for any customer who keeps hitting the
> cap week after week. Freeing a slot is a one-shot fix for a stale
> instance, not a renewable workaround for "we outgrew the tier."

## When the customer says "free all of them"

Don't. If a customer asks you to clear every slot at once, that's
a different problem — usually they just rebuilt their whole fleet
and want a clean slate. Flag it in #licensing-ops. The team has
a bulk-clear procedure that handles it more safely than clicking
**Free this slot** fifty times in a row.

## What happens after you free a slot

Nothing dramatic. The customer's new instance, when it checks in,
takes the freed slot. The customer's instance count drops by one
and goes back up by one. No emails get sent. No alarms fire.

If the customer is watching the portal in real time and wants
confirmation, tell them to refresh their dashboard. The change
shows up immediately on our side; the customer's dashboard syncs
within a minute.
