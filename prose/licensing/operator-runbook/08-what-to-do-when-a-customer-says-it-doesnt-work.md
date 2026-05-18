---
title: What to do when a customer says "it doesn't work"
slug: operator-runbook/08-what-to-do-when-a-customer-says-it-doesnt-work
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: published
last-reviewed: 2026-05-18
related:
  - prose/licensing/operator-runbook/02-issuing-a-license.md
  - prose/licensing/operator-runbook/03-handling-a-stuck-server-slot.md
  - prose/licensing/operator-runbook/12-removing-the-demo-tag-after-upgrade.md
---

# What to do when a customer says "it doesn't work"

A customer emails support: "We installed the license but it's
not working." This article is the sort-and-decide script. Four
causes cover about 95% of these tickets. Walk through them in
order. Most of the time, you're done in two emails.

## The four usual suspects

In order from most common to least common:

1. **The license file is in the wrong path.**
2. **They downloaded the license for a different product.**
3. **Their server's clock is set wrong.**
4. **They installed a Pro Developer license in production by
   mistake** (the Demo tag shows up in their production
   observability and they think the product is broken).

Each one has a one-line question to ask the customer and a
one-line answer that confirms it. The whole script fits in a
single email.

## Cause 1: license file in the wrong path

This is the most common cause. The customer downloaded the file
but put it in the wrong folder on the instance. Their software
looks in a specific spot, doesn't find anything, and gives up.

**Question to ask:**

> Can you run this command on the instance and paste the output
> back to me? It's harmless — it just lists what's in the
> folder where the software looks for the license.
>
> (Paste the product-specific command from the support
> template.)

**Answer that confirms it:**

The customer pastes the output. If the license file is **not**
listed, that's your culprit. Walk them through moving it to the
right path. The support template has the path for each product.

> :information_source: **Heads up** — don't ask the customer to
> "check if the file is in the right place." That sentence puts
> the burden on them to know what "right" is. The command
> approach gets you the answer in one round.

## Cause 2: wrong product on the license file

Less common but very easy to spot. The customer bought
Compliance, but somewhere along the way they downloaded a Pro
license file and installed it on a Compliance server. The file
is valid, the path is right, but the product names don't match,
so the software refuses to use it.

**Question to ask:**

> Two quick checks:
>
> 1. Which product did you buy? (Pro, Enterprise, or
>    Compliance.)
> 2. Open the license file in a text editor and copy the first
>    line back to me. It'll look like a short string of letters
>    and numbers.

**Answer that confirms it:**

The first line of the file has the product name in it. If they
bought Compliance but the file says `pro` somewhere in that
first line, you've found the problem. Re-issue the right
license (see [issuing a license](./02-issuing-a-license.md))
and email them the correct file with a short apology.

## Cause 3: server's clock is wrong

Uncommon but easy to overlook. The customer's instance has its
clock set wrong — maybe by hours, maybe by days. The license
file has a start date and an end date. If the instance thinks
"today" is before the start date, it treats the license as not
yet valid. If the instance thinks today is after the end date,
it treats the license as expired.

**Question to ask:**

> Can you run this command on the instance and paste the output
> back? It just shows what date and time the instance thinks it
> is.
>
> (Paste the product-specific date command from the support
> template.)

**Answer that confirms it:**

The customer pastes the date. If it's way off from the actual
date, you've found it. Tell them the instance's clock is set
wrong and the license file looks invalid as a result. Ask their
IT team to fix the clock (usually a quick fix — turn on
automatic time sync). Once the clock is right, the license
starts working at the next check-in.

> :bulb: **Why does this happen?** Instances in a basement
> closet sometimes have their clock drift over time, especially
> if they were unplugged for a while or rebuilt from an old
> image. The licensing system trusts the instance's clock; if
> the clock lies, the license looks invalid. There's no way
> around this on our side — clocks have to be right for
> licensing to work.

## Cause 4: Demo tag visible in production

New since the Pro Developer tier shipped. The customer comes
back with a complaint that sounds like "your product is broken"
but really means "I'm seeing a `LicenseTier: Demo` property on
every event in my production dashboards and that doesn't look
right."

This is almost never the product being broken. It's the
customer running a **Pro Developer** license file in production
when they have a paid license sitting in their account too. The
free tier stamps every event with the Demo tag on the way out —
that's the architectural shape of the free tier, not a bug.

**Question to ask:**

> Quick check — can you confirm which license file is currently
> installed on the affected instance? Either copy the first
> line of the file, or run this command and paste the output:
>
> (Paste the product-specific license-inspect command from the
> support template.)

**Answer that confirms it:**

If the file's `seg` claim says `dev`, they're running the free
tier in a place where they meant to run their paid tier. The
fix is to install the correct paid license file on that
instance. Walk them to it. Once the paid file is in place, the
Demo tag stops appearing on the next check-in's events.

If the file's `seg` claim already shows their paid segment
(`team`, `fleet`, `provider`, or `enterprise`) but the Demo tag
is *still* showing up in observability, that's a different
problem — hand it to article 12 and escalate. The most common
real cause is a stale build of the customer's software that
still has the free DLLs from before they upgraded; the customer
needs to pick up the latest paid build.

> :bulb: **Why this matters.** The Demo tag is the
> architectural shape of the free tier — the only tier where
> the product visibly remembers it's a trial shape. That visible
> reminder is on purpose. The customer is supposed to see it and
> think "oh right, I'm still on the free plan." When the Demo
> tag appears in production observability, the question is
> always "which license file did they actually install?" — not
> "is the product broken?"

## When none of the four apply

If you've ruled out path, product, clock, and the Demo-tag
mix-up, escalate. The next likely causes are network issues
(the customer's firewall is blocking check-ins) or a portal-
side problem. Either way, those are harder and they take a
senior operator or an engineer.

Don't guess. Don't ask the customer to "try restarting the
software." Hand it off cleanly with what you've already
confirmed:

> Hi <name>, I've confirmed the license file is in the right
> path, matches the product you bought, your instance's clock
> looks correct, and the license is your paid tier (not Demo).
> I'm escalating this to our senior team. You should hear back
> from us within one business day.

Then post the ticket in #licensing-ops with the same summary.

## What NOT to say

> :warning: **Wait — should I really say this?** Avoid any of
> these phrases when emailing a customer:
>
> - "Your license verifier is returning NotYetValid." (No
>   customer knows what that means.)
> - "Try clearing the cache and restarting." (Cargo-cult
>   advice.)
> - "It works on our end." (Even if true, useless to the
>   customer.)
> - "The Demo tag is intentional, you can ignore it." (Even
>   when technically true, this dismisses a customer who is
>   reasonably confused. Walk them through *why* it's there
>   and *what to do about it*.)
>
> Use plain English. The customer is frustrated; jargon makes
> it worse. "Your instance's clock is set wrong and thinks the
> license isn't valid yet" is better than any of the above.

## The shape of a good support reply

Three short pieces:

1. **What you checked.** "I looked at your license in our
   portal and it's active and matches your instances."
2. **What you found.** "Your instance's clock is set 3 days
   ahead, which makes the license look like it expires sooner
   than it does."
3. **What they should do next.** "Can you ask your IT team to
   enable automatic time sync on the instance? Once the clock
   is right, the license should work within 24 hours."

That's the whole pattern. Don't pad it.
