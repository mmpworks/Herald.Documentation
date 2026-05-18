---
title: When a customer asks to remove the Demo tag after upgrading
slug: operator-runbook/12-removing-the-demo-tag-after-upgrade
category: operator-runbook
audience: mmpworks-operator
reading-level: high-school (target = "no glossary needed")
since: 2.0
status: published
phase: A
last-reviewed: 2026-05-18
related:
  - prose/licensing/operator-runbook/02-issuing-a-license.md
  - prose/licensing/operator-runbook/08-what-to-do-when-a-customer-says-it-doesnt-work.md
  - prose/licensing/operator-runbook/11-mid-quarter-upgrade-from-developer.md
---

# When a customer asks to remove the Demo tag after upgrading

> :information_source: **Not shipped yet.** This article covers
> a flow that lands in **Phase A** of the licensing rollout —
> the Pro Developer mechanism itself (the `seg: dev` claim,
> the `LicenseModeEnricher` in the paid DLLs, the construction
> hook at the `LoopbackInterceptor.Wrap()` call site). The
> runbook is here so the eventual launch is smooth, but the
> portal does not yet support every step below. Glenn is
> implementing this Phase right now in parallel.

A customer who recently upgraded from Pro Developer to a paid
tier (Pro Team, Fleet, Provider, or Enterprise) emails to say:
"We installed the new license but events in our observability
tool still show `LicenseTier: Demo`. How do we turn this off?"

This article walks through the diagnosis and the answer. Most
of the time the fix is on their side, not ours. The Demo tag
is the architectural shape of the free tier — the only tier
where the product visibly remembers it's a trial shape — so
when it persists after an upgrade, the question is always
"which file is actually loaded?" not "is there a switch we
need to flip?"

> :bulb: **Quick picture.** The Demo tag is like a "VOID"
> watermark on a check from a starter pack — it's printed on
> the check, not added by the bank. When you switch to your
> real checks, the watermark goes away because you're using
> different checks, not because you asked the bank to remove
> it. The customer who's still seeing the watermark either
> (a) hasn't started using the new checks yet, or (b) is
> using a mix.

## How the Demo tag actually works

For background, so you can explain it to the customer:

- The Pro Developer license file has a `seg: dev` claim
  inside it.
- The paid DLLs the customer runs notice the `seg: dev` claim
  at startup and wrap the event-emit path with a small piece
  of code that adds `LicenseTier: Demo` to every event before
  it leaves.
- When the license file changes to one with a paid `seg` claim
  (`team`, `fleet`, `provider`, `enterprise`), that wrap goes
  away on the next process load.
- The wrap is in the **paid DLLs**, not in the customer's
  application code or the open-source layer. So the customer
  can't accidentally turn it off by editing their own code,
  and we can't turn it off from the portal — the trigger is
  the license file's `seg` claim, full stop.

This is the architectural shape we want. The customer trusts
the Demo tag because they can see in the binary's behavior
that it's tied to the license file, not to a server-side
toggle we might forget to flip.

## The three possible states

When the customer reports persisting Demo tags, exactly one of
these is true:

1. **A Pro Developer file is still on at least one of their
   instances.** They swapped some but not all. The instances
   still on Developer keep stamping the tag.
2. **The instance loaded the new file but didn't pick it up at
   runtime yet.** Some customer setups load the license file
   only at process startup; the new file is on disk, but the
   running process is still using the previously-loaded one.
3. **A stale build of the paid DLLs is in use.** The customer
   upgraded their license but is running an old build of the
   product that doesn't include the latest paid DLLs — usually
   because they pinned a version in their build pipeline and
   the pin is older than the upgrade.

The diagnostic is the same: ask the customer to confirm
**which `seg` value is actually on each instance**.

## The diagnostic

**Question to ask:**

> Quick check — on each instance that's still showing the
> Demo tag in events, can you run this command and paste the
> output? It just prints the `seg` claim from the currently-
> loaded license file.
>
> (Paste the product-specific license-inspect command from
> the support template.)

The output will be one of:

- `seg: dev` → state 1 (still on Developer file). Fix: install
  the paid file on this instance. See article 11.
- `seg: team` (or `fleet`, `provider`, `enterprise`) → state 2
  or 3. The license is paid, so the wrap should be off. Walk
  the next two questions.

**Follow-up question for `seg: <paid>` cases:**

> Two more checks:
>
> 1. Was this instance restarted (or the process reloaded)
>    after the new license file was installed?
> 2. What version of the product is this instance running?
>    Run this command and paste the output.

If the answer to (1) is "no," that's state 2 — tell the
customer to restart (or wait for the next natural restart).
The Demo tag will stop on next check-in after the load.

If (1) is "yes" and (2) reveals a build older than the version
that introduced the upgrade-handling code, that's state 3 —
tell the customer they need to pick up the latest build of
the product. The latest paid DLLs know how to honor the new
`seg` claim; older ones might not.

## When the customer pushes back

A few responses to expect:

### "Can you just turn it off from your side?"

No, and here's the honest answer to give them:

> The Demo tag isn't a server-side toggle on our end — it's
> built into the paid DLLs the product ships with, triggered
> by the `seg: dev` claim in the license file. When the
> license is paid, the tag goes away automatically; when it's
> free, the tag is there. We can't override the binary
> behavior from the portal, and we don't want to — it's part
> of why customers trust the Demo signal.

Customers usually accept this once they understand the
mechanism. The few who keep pushing are usually trying to
solve a different problem (Demo tag breaking a downstream
dashboard query, etc.); ask them what the downstream impact
is and route to support if it's not just a cosmetic
preference.

### "Our compliance team needs the events without the tag
retroactively."

The tag isn't on past events — it's only stamped on events
emitted while the Developer file was loaded. Past events in
their observability tool are *history* with the tag baked in
at the time. We can't and won't rewrite history. If their
compliance team needs filtered views, the observability tool
itself can usually exclude on the `LicenseTier` property.

### "We never actually used Developer in production, this is
new."

That's worth investigating. Usually it means one of:

- Their build pipeline grabbed a Developer license from a
  shared config by accident.
- A new instance came up using an older Ansible/Terraform/
  whatever file that pointed to the Developer license.
- An automated test environment that always uses Developer is
  leaking events into the production observability stream.

The right answer is to find where the Developer file is
still loaded and remove it. Walk article 08's cause-1
diagnostic on a per-instance basis.

## What NOT to do

> :warning: **Don't promise to "remove the tag from past
> events."** We can't. The events are already in the
> customer's observability tool, with the tag baked in.

> :warning: **Don't escalate to engineering unless the
> diagnostic genuinely doesn't fit any of the three states.**
> The states cover ~99% of cases. The exceptions usually mean
> the customer is running a custom build or has a non-standard
> deployment pattern, and engineering will need that context
> from the start.

> :warning: **Don't try to issue a "Demo-tag-removed Developer
> license."** That doesn't exist. There are two kinds of
> license: Developer (with the Demo tag) and paid (without).
> The path is upgrade, not "modify Developer."

## The shape of a good support reply

Three pieces, same as article 08:

1. **What you checked.** "I confirmed your paid Pro Team
   license is active on our side and the file is dated <date>."
2. **What you found.** "Three of your four instances are
   loading the paid file — the fourth still has the Developer
   file in place. The Demo tag is appearing on events from
   that one instance."
3. **What they should do next.** "Install the paid license
   file on `prod-web-04` and restart the process. The Demo
   tag should stop appearing on its events at the next
   check-in within 24 hours."
