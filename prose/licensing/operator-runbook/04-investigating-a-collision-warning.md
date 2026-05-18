---
title: Investigating a collision warning
slug: operator-runbook/04-investigating-a-collision-warning
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: published
last-reviewed: 2026-05-17
related:
  - prose/licensing/operator-runbook/03-handling-a-stuck-server-slot.md
  - prose/licensing/operator-runbook/06-turning-off-a-license.md
---

# Investigating a collision warning

The portal shows a yellow warning on a customer: **two servers
checked in from the same internet address**. This article tells
you what that means, what the innocent reasons are, what the
suspicious reasons are, and how to decide whether to call the
customer.

## What the warning means, in plain English

Every instance that uses the customer's license checks in with us
once a day. An **instance** is one installation on a server or one
spun-up cloud VM — same unit for every product. The check-in
includes the instance's internet address — the public number that
identifies where it's connecting from.

Most customers' instances each have their own address. So when two
of their instances check in from the **exact same** address, the
portal flags it. The warning isn't an accusation. It's a "hey,
take a look at this."

> :bulb: **Quick picture.** Imagine you run a small office with
> ten employees. The office has one internet connection. To the
> outside world, all ten employees appear to be browsing the web
> from the same address — the office's. That's normal and not
> suspicious. Same idea here.

## The innocent reasons (most of the time)

Most collision warnings have a boring explanation:

- **Office network.** The customer runs several instances from one
  office, all sharing one outbound internet address. Common in
  small companies and labs.
- **Corporate firewall.** A large customer might funnel all their
  outbound traffic through one or two security gateways. Hundreds
  of instances, one or two addresses.
- **Cloud setup with shared egress.** Cloud customers sometimes
  route all their outbound traffic through a single shared
  gateway. Looks like one address from our side, even though the
  instances are separate.

If you look at the active instances list and the instance names
look distinct (`web-01`, `web-02`, `db-prod`, etc.) and the
customer has a history of running this way, the warning is almost
certainly innocent. Click **Dismiss warning** with a note like
"customer's normal office setup — confirmed 2026-05-17."

## The suspicious reasons (rare, but worth catching)

A collision warning is worth a closer look when **any** of these
are true:

- The customer's instance count suddenly jumped from a few to
  many, all checking in from one address, with no advance notice.
- The instance names look duplicated or generated
  (`server-1`, `server-2`, `server-3` showing up overnight).
- The address belongs to a hosting region the customer has never
  used before.
- The customer's account flagged a different warning recently
  (near-cap, payment issue, weird usage pattern).

These can mean someone copied the license file and is running it
in a second environment they didn't pay for. Or someone leaked
the file outside the company.

## How to decide whether to call

Use this order:

1. **Check the customer's history.** Have they had this warning
   before? Was it dismissed as normal? If yes, dismiss again with
   a note.
2. **Look at the instance names and counts.** Distinct names,
   count matches what they bought, no sudden jump → innocent. Move
   on.
3. **Look at the address.** Run a quick lookup on the address
   (the portal has a **Lookup** button next to each row). If it
   resolves to a known cloud provider in a region the customer
   uses, that's consistent with their setup.
4. **If two or more things look off**, email the primary contact.
   Don't accuse. Ask: "We noticed your instances are checking in
   from one address, and the count jumped recently. Is this a new
   office setup, or did you spin up a second environment we should
   know about?"

> :warning: **Wait — should I really do this?** Never turn off
> a license based on a collision warning alone. Always email the
> customer first. Most "suspicious" warnings turn out to be a new
> firewall or a routine cloud migration the customer just didn't
> tell us about.

## What if the customer doesn't reply

Give it three business days. If no reply and the warning
persists, escalate to the licensing-ops lead. They have a
follow-up script that gets used before any license action.

## When to dismiss versus when to leave open

- **Dismiss with a note** when you've confirmed it's innocent.
  Future operators see your note and don't have to re-investigate.
- **Leave open** when you've emailed the customer and are waiting
  for a reply. The warning serves as your reminder.

Never dismiss a warning you haven't actually looked at. Future-you
or future-someone-else will assume the previous operator did the
work, and that's how things slip.
