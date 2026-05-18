---
title: Adding a customer
slug: operator-runbook/01-adding-a-customer
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: published
last-reviewed: 2026-05-17
related:
  - prose/licensing/operator-runbook/02-issuing-a-license.md
  - prose/licensing/explanation/how-licensing-works.md
---

# Adding a customer

A new customer just signed up. Before you can give them a license
file, the portal needs to know who they are. This article walks
through adding that record.

The whole job is one form. It takes about a minute.

## The steps

1. Open the portal and click **Customers** in the left menu.
2. Click the **Add customer** button in the top right.

   ![TBD: customer-detail screenshot, empty form]

3. Fill in the fields:
   - **Company name** — exactly as it appears on the invoice. If
     the customer is "Acme Industries, Inc." don't shorten it to
     "Acme." The company name is what shows up on every license
     file we issue them, so consistency matters.
   - **Primary contact email** — the person who handles their
     servers, not the person who signed the contract. This is who
     we'll email when a license is about to expire.
   - **Billing email** — can be the same as primary contact, but
     usually it's accounts payable. Used only for invoice-related
     mail.
   - **Notes** — anything the next operator should know. "Renewed
     after a 60-day gap" or "asked us to call before any change to
     their license" is the kind of thing that belongs here.

4. Click **Save**.
5. The portal takes you to the new customer's detail page. From
   here, you can issue them a license (see
   [issuing a license](./02-issuing-a-license.md)).

> :bulb: **Why?** We separate "customer" from "license" because a
> customer can buy several licenses over time — Pro now,
> Compliance next quarter, Enterprise next year. Keeping the
> customer record separate means we don't lose their history when
> a single license expires.

## What NOT to do

> :warning: **Wait — should I really do this?** Before you click
> **Add customer**, search for the company first. The most common
> portal mistake is creating a duplicate record because the
> existing one had a slightly different spelling.

If the customer emails you to update their address, their billing
contact, or their company name — **edit the existing record**.
Don't create a new one and abandon the old. Duplicate records
split a customer's license history across two pages, and the next
operator can't tell which is current.

If you genuinely can't find them with a search, ask the previous
support rep before adding a new record. Two operators duplicating
the same customer in the same hour has happened before.

## When the search returns two records that look like the same customer

That's a cleanup task, not a new-customer task. Flag it in
#licensing-ops and let the team merge them. Don't try to merge
records from the portal yourself — there isn't a button for that
yet, and editing one record to match the other leaves an orphan.

## What happens next

The customer record now exists but has no licenses attached. Go
to [issuing a license](./02-issuing-a-license.md) to give them
what they paid for.
