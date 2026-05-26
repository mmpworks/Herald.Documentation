---
title: Operator runbook for the MMPWorks licensing portal
slug: operator-runbook/index
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: published
last-reviewed: 2026-05-18
related:
  - prose/licensing/explanation/how-licensing-works.md
  - prose/licensing/explanation/non-support-faq.md
---

# Operator runbook for the MMPWorks licensing portal

This is the everyday playbook for MMPWorks staff who run the
licensing portal. If a customer just paid for Pro, or a customer
emails support saying "it stopped working," or a slot in the
portal looks stuck — start here.

Each article is short on purpose. You should be able to skim one
in under two minutes and know exactly what buttons to click.

> :information_source: **Heads up** — the portal screenshots in
> these articles are placeholders. The portal is still being built.
> When the screens land, we'll drop the real images in. The steps
> themselves are correct.

> :information_source: **About the SKU-aware articles (9–13).**
> The licensing rollout ships in phases (A through F). Articles
> 9–13 cover flows that lean on later-phase capability — auto-
> rollover (Phase B), Provider TOS + metering (Phase D), the
> `seg` claim mechanics (Phase A). Each article carries a
> "Not shipped yet" banner naming the phase that lands it.
> Until those phases ship, the articles are forward-looking
> specs; treat them as the operating shape the team is building
> toward, not as today's portal behavior.

## The articles

### Day-one operator playbook

1. [Adding a customer](./01-adding-a-customer.md) — a new
   customer signed up; get them into the system.
2. [Issuing a license](./02-issuing-a-license.md) — the
   customer paid; give them the file they need. Covers all
   five Pro segments + Compliance attach.
3. [Handling a stuck server slot](./03-handling-a-stuck-server-slot.md)
   — the most common support ticket.
4. [Investigating a collision warning](./04-investigating-a-collision-warning.md)
   — two instances checked in from the same internet address.
   Friend or foe?
5. [When a customer asks for more licenses](./05-when-a-customer-asks-for-more-licenses.md)
   — they hit the cap and need more instances. Six branches by
   segment.
6. [Turning off a license](./06-turning-off-a-license.md) —
   rare, but it happens. Cancellations, abuse, payment
   failures.
7. [Reading the portal status page](./07-reading-the-portal-status-page.md)
   — a tour of the main landing screen.
8. [What to do when a customer says "it doesn't work"](./08-what-to-do-when-a-customer-says-it-doesnt-work.md)
   — the four most common causes and how to spot them in 30
   seconds.

### SKU-aware flows (some flows ship in later phases)

9. [Auto-rollover from Pro Team to Pro Fleet](./09-auto-rollover-team-to-fleet.md)
   — what the rollover at 26 instances looks like end-to-end.
   (Phase B.)
10. [Onboarding a Pro Provider customer with the MSP TOS](./10-onboarding-a-provider-with-tos.md)
    — Provider has different legal shape; the click-through
    has to be done first. (Phase D.)
11. [Mid-quarter upgrade from Pro Developer to Pro Team](./11-mid-quarter-upgrade-from-developer.md)
    — the conversion path; usually self-service, sometimes
    needs an operator. (Phase B.)
12. [When a customer asks to remove the Demo tag after upgrading](./12-removing-the-demo-tag-after-upgrade.md)
    — three states, one diagnostic, no server-side toggle.
    (Phase A.)
13. [Diagnosing a segment-claim mismatch](./13-diagnosing-a-segment-mismatch.md)
    — three patterns, three different fixes. Mostly mundane.
    (Phase A.)

### Deployment + infrastructure

14. [Bootstrapping the license server on Azure](./14-bootstrapping-the-license-server-on-azure.md)
    — the order to stand things up in, the four gotchas that
    will bite you the first time, and the production-gap list
    that must close before the first paying customer. (Phase D.)

## When something here is wrong

If a step in any article doesn't match what you see in the portal,
flag it in the #licensing-ops channel. The docs follow the portal;
when they drift, we fix the docs. Don't try to make the portal
match the docs.

## What this runbook is not

This runbook is for **us** — MMPWorks staff. It is not the
customer-facing install guide. If a customer asks "how do I install
my license file on my server," send them to the customer install
guide, not these articles. The customer guide lives one folder up.
