---
title: Issuing a license
slug: operator-runbook/02-issuing-a-license
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: published
last-reviewed: 2026-05-18
related:
  - prose/licensing/operator-runbook/01-adding-a-customer.md
  - prose/licensing/operator-runbook/05-when-a-customer-asks-for-more-licenses.md
  - prose/licensing/operator-runbook/09-auto-rollover-team-to-fleet.md
  - prose/licensing/operator-runbook/10-onboarding-a-provider-with-tos.md
  - prose/licensing/explanation/how-licensing-works.md
---

# Issuing a license

The customer paid. Now they need the license file that turns the
product on. This article walks through filling out the form and
sending them the file.

The form has three pieces: **tier**, **segment**, and
**instance count**. Get those three right and the rest of the form
fills itself in.

> :bulb: **Quick picture.** Picking a tier is like picking a
> phone plan. The tier (Pro, Enterprise, Compliance) is the family
> — same SIM, same network. The segment (Developer, Team, Fleet,
> Provider, Enterprise) is which plan inside that family — solo,
> couples, family, business. The instance count is how many lines
> are on the plan. You don't pick "Pro" and then separately pick
> "Team" — Pro Team is one choice in the dropdown. Same for the
> rest.

## Before you start

Make sure you have three things from sales:

- **Which product** — Pro, Enterprise, or Compliance. (Compliance
  is an add-on; see the Compliance section below.)
- **Which segment** (for Pro) — Developer, Team, Fleet, Provider,
  or Enterprise. Sales tells you which.
- **How many instances** — one instance is one installation on a
  server or one spun-up cloud VM. If they bought 50 instances,
  they can run the product on 50 servers or VMs at once.

You also need **the term** — usually one year, sometimes longer.
Sales tells you the start and end dates.

If you don't have all four, stop and ask sales. Guessing here
costs more time than asking does.

## The steps

1. Open the customer's detail page (search by company name on the
   **Customers** screen).
2. Click **Issue new license**.

   ![TBD: license-form screenshot, empty]

3. Fill in the form:

   - **Product** — pick from the dropdown. Pro, Enterprise, or
     Compliance.
   - **Segment** — only appears when Product is Pro. Pick
     Developer, Team, Fleet, Provider, or Enterprise.
   - **Instance count** — the number of installations or cloud VMs
     the customer can run this product on. If they bought 50,
     type 50. The cap behavior depends on the segment — see the
     segment notes below.
   - **Start date** — the day the license becomes active. Almost
     always today, unless sales told you otherwise (some customers
     pre-pay for a license that starts next month).
   - **End date** — the day the license stops working. For a
     one-year term that starts today, this is one year from today.
     Pro Developer is the exception — it's perpetual, no end date.
   - **Notes** — paste the sales order number here. Future-you
     will thank present-you when a customer asks "what did I buy
     last year?"

4. Click **Issue license**.
5. The portal generates a single file. It looks like a long string
   of letters and numbers and ends with `.license`. Download it.

> :bulb: **Why these dates?** The start date tells the customer's
> instances "ignore this license until this day arrives." The end
> date tells them "stop trusting this license after this day." We
> pick them precisely so the customer gets exactly what they paid
> for — no more, no less. Pro Developer is the exception because
> the free tier is perpetual — there's nothing to expire.

## Segment-specific things to watch for

The five Pro segments have different shapes. Most of the form
is the same; these are the spots that differ.

### Pro Developer (free, perpetual, 3-instance cap)

- **Instance count is locked at 3.** The form won't let you raise
  it. If sales is asking for 4+, they want Pro Team — go back and
  ask.
- **No end date.** Pro Developer is perpetual. The portal leaves
  the end-date field disabled.
- **Demo tag visible in every event.** This is the architectural
  shape of the free tier — the customer's instances stamp every
  event with a `LicenseTier: Demo` property as it leaves. That's
  on purpose, not a bug. If the customer asks why the tag is
  there or how to turn it off, the answer is "upgrade to Pro
  Team." Don't try to remove the tag from a Pro Developer
  license; see article 12.

### Pro Team ($79 first instance, $59 each from #2 to #25)

- **Instance count 1–25.** That's the Team band. Above 25 the
  pricing automatically rolls into Pro Fleet — covered in
  article 09.
- **Pricing is auto-tiered.** Don't try to talk pricing in the
  portal. The Stripe side handles the per-instance curve. Your
  job here is just the instance count.
- **Auto-rollover at 26.** When the customer hits 26, the system
  rolls them into Pro Fleet without a sales call. The portal will
  surface a yellow badge a few weeks before, so sales sees it
  coming.

### Pro Fleet ($39 per instance from #26, $10K floor)

- **Instance count 26+.** Below 26 they belong in Pro Team. The
  portal will refuse Fleet under 26.
- **$10K annual floor.** Even a small Fleet (say 26 instances at
  $39 = $1,014) bills at the $10K floor. The Stripe side enforces
  this; you don't enter it on the form, but you should know it
  exists if the customer asks.
- **Customers usually arrive here by auto-rollover, not by
  picking Fleet directly.** A direct Fleet issuance is the
  exception. Always ask sales why if you see one.

### Pro Provider ($29 per managed instance, $15K floor, MSP TOS)

- **MSP TOS click-through is required.** The customer is signing
  a different legal agreement than every other Pro segment — they
  redistribute the product to *their* customers, so they need the
  MSP terms. Sales handles the click-through; the portal won't
  let you issue a Provider license until sales marks the TOS as
  accepted. If the **Issue license** button is greyed out, that's
  usually why.
- **`activeTenantSlugs[]` shows up on check-ins.** Provider
  instances report which of their downstream customers they're
  serving. This is how we meter Provider billing.
- **$15K annual floor.** Same shape as Fleet — the per-instance
  rate is small but the floor protects the relationship.
- **First-time Provider onboarding has its own article** —
  see article 10.

### Pro Enterprise ($50K+ annual, contact-sales)

- **Custom terms.** Enterprise is whatever sales negotiated.
  Instance count, term length, support level — all on the order.
- **Read the sales order twice.** Enterprise contracts have more
  moving parts than Team or Fleet. If the order says "50
  instances + Compliance + 24/7 support" make sure you don't
  miss the Compliance attach (next section).

## Compliance is an add-on, not a license

Compliance Pack is **not** its own license file. It attaches to
an existing Pro Team, Pro Fleet, or Pro Enterprise license as an
add-on. The customer's instances pick it up at next check-in.

To attach:

1. Open the customer's detail page.
2. Find the Pro license they want to add Compliance to.
3. Click **Add Compliance Pack** on that row.
4. The portal asks you to confirm the term (usually matches the
   parent license).
5. The portal does not re-issue the license file. The Compliance
   capability lights up at the next check-in — no new download
   needed.

> :information_source: **Heads up** — Compliance Pack is +$2K /yr
> and ships the BAA and SOC paperwork. Sales handles delivery of
> the paperwork; your job is the portal attach. If the customer
> asks where their BAA is, hand the question to sales — don't
> guess at the timeline.

## What the customer gets

You email the file to the primary contact on the customer record.
Include three things in the email:

1. **The file** as an attachment.
2. **Where to put it.** The customer's instances read the file
   from a specific path. The exact path depends on the product.
   The sales email template has the paths for each product — use
   that template; don't free-write.
3. **What to do if it doesn't work.** Tell them to email
   support@mmpworks.com and reference the sales order number.

> :information_source: **Heads up** — never send the license file
> over chat. Always email. Chat history is harder to recover six
> months from now when the customer's IT team rebuilds an
> instance and asks "where's our license file?"

## What NOT to do

> :warning: **Wait — should I really do this?** Don't issue the
> license until the payment has cleared. Sales will sometimes ask
> you to issue early as a favor. Push back — say "happy to once
> payment posts." A license issued before payment is hard to take
> back without an awkward conversation. The one exception is Pro
> Developer, which is free — you can issue it as soon as the
> customer record exists.

Don't issue a license with a start date in the past unless sales
explicitly asks for it. A license dated yesterday is fine, but a
license dated three months ago looks like you're trying to cover
up a missed renewal. Ask if you see this request.

Don't reuse instance counts across products. If a customer has
Pro Team for 20 instances and adds another Pro tier (say a
separate Enterprise line for a different division), that's a new
license — not "Team and Enterprise on the same 20 instances."
Each license file stands on its own.

Don't pick Pro Fleet directly if the customer has fewer than 26
instances. They belong in Pro Team, and they'll auto-rollover
into Fleet when they grow. The pricing curve is published and
the customer trusts it; don't shortcut around it.

## When something goes wrong

If the portal shows an error when you click **Issue license**,
take a screenshot, paste it in #licensing-ops, and **do not click
the button again**. Repeated clicks can issue two license files
for the same order. The team can clean up the duplicate, but
it's faster to catch it on the first try.

If the **Issue license** button is greyed out, the usual reasons
are:

- Sales hasn't marked payment as cleared (Pro Team / Fleet /
  Enterprise).
- The MSP TOS isn't accepted yet (Pro Provider only).
- The customer already has an active license at this tier and
  the portal is preventing a duplicate. Adjust the existing one
  instead — see [when a customer asks for more licenses](./05-when-a-customer-asks-for-more-licenses.md).
