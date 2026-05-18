---
title: Onboarding a Pro Provider customer with the MSP TOS
slug: operator-runbook/10-onboarding-a-provider-with-tos
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: published
phase: D
last-reviewed: 2026-05-18
related:
  - prose/licensing/operator-runbook/02-issuing-a-license.md
  - prose/licensing/operator-runbook/05-when-a-customer-asks-for-more-licenses.md
  - prose/licensing/operator-runbook/07-reading-the-portal-status-page.md
---

# Onboarding a Pro Provider customer with the MSP TOS

> :information_source: **Not shipped yet.** This article covers
> a flow that lands in **Phase D** of the licensing rollout —
> Pro Provider, the check-in `activeTenantSlugs[]` field, and
> the `IMspBillingEventStore` interface plus Stripe metered
> billing. The runbook is here so the eventual launch is
> smooth, but the portal does not yet support every step below.
> Until Phase D ships, treat Provider requests as a custom
> Enterprise-shaped sale routed through the licensing-ops
> lead.

Pro Provider is the segment for managed service providers
(MSPs) who redistribute our product to *their* customers.
Different legal shape, different billing model, different
check-in payload. This article walks through the onboarding
flow end-to-end.

The thing that makes Provider different from every other Pro
segment isn't the price — it's the **MSP TOS click-through**.
The Provider customer is signing an agreement that lets them
redistribute, and they need to accept those terms before any
license can be issued. The portal enforces this.

> :bulb: **Quick picture.** Pro Team is renting an apartment —
> the customer lives in it. Pro Provider is owning a small
> apartment building — the customer rents units to other
> people. The legal agreement for owning a building isn't the
> same as the lease for living in one. Provider customers sign
> the "you can sublease" agreement (the MSP TOS); Pro Team
> customers don't. The portal can't issue a Provider license
> without that agreement on file.

## Before you start

You need four things from sales:

- **Confirmation the deal is a Provider deal**, not a regular
  Pro Team or Fleet. Sometimes a customer asks about
  "redistributing" without realizing they're describing
  Provider. Sales clarifies the relationship.
- **The MSP TOS click-through has been initiated.** Sales sends
  the customer a link; the customer clicks through. The portal
  shows the TOS state on the customer record.
- **The instance count and term.** Provider has a $15K annual
  floor and a $29 per-instance rate. Sales confirms the cap.
- **The expected `activeTenantSlugs` pattern.** Provider
  check-ins include the list of *their* customers being served.
  Sales gives you the rough shape ("they're starting with 3
  downstream tenants, expect that to grow to 20 over the
  quarter").

If any of these are missing, stop and ask sales. Provider is
the segment where "guessing" is most likely to land you in a
TOS-violation conversation later.

## The onboarding steps

### Step 1 — verify the MSP TOS is accepted

1. Open the customer's detail page.
2. Look at the **MSP TOS** row. It shows one of three states:
   - **Not initiated** — sales hasn't sent the click-through
     link yet. You can't issue a Provider license. Tell sales.
   - **Pending** — link sent, customer hasn't clicked yet. You
     still can't issue. Tell sales to nudge the customer.
   - **Accepted** — date and the customer's signing email show.
     You're cleared to proceed.
3. If the state is anything but Accepted, the **Issue license**
   button stays greyed out for the Provider segment. The portal
   enforces this — you can't override it.

### Step 2 — issue the Provider license

1. Click **Issue new license** on the customer's detail page.
2. In the form:
   - **Product** — Pro
   - **Segment** — Provider
   - **Instance count** — the cap sales confirmed
   - **Start date** — usually today
   - **End date** — one year out (or whatever the contract
     specifies)
   - **Notes** — paste the sales order number and a one-line
     description of the MSP relationship ("MSP serving Acme,
     Beta Co, and Gamma Inc as their initial downstream
     tenants")
3. Click **Issue license**. The portal generates the file.
4. Download it.

The file looks identical to a Pro Team file at a glance, but
the `seg` claim inside reads `provider` instead of `team`. The
customer's instances will publish `activeTenantSlugs[]` on
their check-ins as a result — that's the field that drives
metered billing.

### Step 3 — email the file (with the Provider-specific
template)

The Provider email template differs from the regular Pro Team
template in three places:

- **The path is the same** (Provider isn't a different
  product, just a different segment).
- **Metered-billing language up front.** The customer should
  see in the first paragraph that their bill scales with the
  number of downstream tenants they serve, not just the
  instance count. Sales should already have set this
  expectation, but the email reinforces it.
- **Reference to the MSP TOS.** A one-liner at the bottom:
  "Your MSP TOS acceptance is on file as of <date>. The terms
  govern redistribution; if you need a copy, reply and we'll
  send it."

Use the **Provider** template in the portal's email-template
list — don't free-write and don't use the Pro Team template.

### Step 4 — confirm the first check-in arrives correctly

Within 24 hours of the customer installing the file, their
first instance should check in. Look for the check-in in the
recent activity feed on the customer's detail page. The row
should show:

- The instance name (whatever the customer's IT team called
  it).
- The internet address.
- **`activeTenantSlugs[]`** — the list of downstream tenants
  this instance is serving. For a brand-new Provider, this
  list might be small (1–3 tenants) at the start.

If the first check-in arrives **without** `activeTenantSlugs[]`
populated, something went wrong on the customer's side —
usually they're running an older build of the product that
doesn't know about the Provider segment yet. Hand to support
with the note "Provider check-in missing tenant slugs — likely
stale build."

## The first billing reconciliation

Provider is **metered**, not flat. The first invoice doesn't
arrive immediately; it arrives at the end of the first billing
cycle and reflects:

- The flat $15K annual floor (prorated to the cycle).
- The per-tenant metering on top of the floor, if the customer
  exceeded the included tenants for the floor amount.

Sales handles the customer-facing invoice conversation. Your
job is to make sure the check-in data is clean so the metering
math is right. If the activity feed shows weird
`activeTenantSlugs[]` patterns (the list jumping wildly week
to week, or always empty), flag it to sales before the cycle
closes — a metered invoice based on bad data is harder to fix
than one based on good data.

## When the customer asks "can we add downstream tenants?"

That's not a portal action on our side. The customer adds
downstream tenants by serving them — the next check-in from
their instances reports the larger `activeTenantSlugs[]` list,
and the metered billing picks it up at the next cycle.

The customer might be asking because they want to know if
there's a *cap* on downstream tenants. There isn't one inside
the Provider segment — that's the whole point of metered
billing. The cap is on the instance count (the number of
installations they run); the downstream tenant count is what
they get billed for.

## When the MSP TOS expires

The MSP TOS has a renewal date (usually one year from
acceptance). Before it expires, the portal flags the customer
on the status page with a yellow **Provider TOS renewal due**
badge. Sales should be reaching out to the customer to
re-accept.

If the TOS expires without renewal, the customer's Provider
license is still active — instances keep running — but the
status page flags them with a red **Provider TOS expired**
badge. They cannot renew their license or add instances until
they re-accept.

Don't turn off a Provider license because the TOS expired.
That's an escalation, not an operator action. Hand to the
licensing-ops lead with a one-line: "Acme Provider TOS
expired <date>, license still active, sales aware?"

## What NOT to do

> :warning: **Wait — should I really do this?** Three things to
> avoid:
>
> 1. **Don't issue a Pro Team license as a "stand-in" for a
>    Provider deal that's waiting on TOS click-through.** Even
>    if sales is asking. Team and Provider are different
>    licensing shapes — issuing Team to an MSP means the MSP is
>    operating outside their actual agreement.
> 2. **Don't accept the MSP TOS on the customer's behalf.** The
>    click-through is recorded against the customer's email.
>    Operators do not have permission to accept it for them.
>    If the customer can't access the link, regenerate it; if
>    they can't sign, escalate.
> 3. **Don't free `activeTenantSlugs[]` entries.** They aren't
>    instance slots — they're billing-related data. If a
>    Provider says "we stopped serving Acme, can you remove
>    them from our tenant list?" the answer is: their instances
>    will stop reporting Acme on the next check-in and the
>    metering will adjust automatically. There's no manual
>    knob.

## What happens next

Once the customer's instances are checking in cleanly with
populated `activeTenantSlugs[]`, the Provider relationship is
operational. The next interaction is usually:

- A first-cycle invoice (sales handles).
- A request to add or remove instances (article 05, Branch E).
- A TOS renewal one year out.

Provider customers tend to be lower-touch than Enterprise but
higher-touch than Team. They have their own product
relationship with their downstream customers and they want our
licensing to stay out of the way.
