---
title: How to run the Herald Demo, five mini-projects
slug: tutorials/running-the-demo
category: tutorial
audience: new-adopter
since: 0.9.0
status: draft (scaffold)
walk-verified: false
created: 2026-05-26
last-reviewed: 2026-05-26
author: Heather (documentation agent)
related:
  - quickstart
  - explanation/kernel-vs-chain
  - tutorials/running-the-demo/05-ship-to-production
related-records: []
---

# How to run the Herald Demo

You ran one command and the demo opened in your browser. This guide
takes you from there. It is five short projects, and they build on each
other:

1. **Add context to every event.** Enrichers.
2. **Keep secrets out of the logs.** Redaction.
3. **Tame a service that logs too much.** Filtering and sampling.
4. **Catch the last moments before a crash.** The flight recorder.
5. **Ship the logs to production.** Send them to Grafana over Docker.

Each project takes a few minutes. You do not need to write code. You
drive the demo from the browser and feed it traffic from one small
command-line tool.

> **Scaffold note.** This page is a draft outline. The numbered steps
> are the planned shape. They are not yet walk-verified in a browser.
> Each project gets its steps confirmed by a real run as the feature
> lands. Anything marked *provisional* depends on a config shape that
> is still being wired.

---

## Before you start: what you are looking at

You installed the demo with one command:

```bash
dotnet tool install --global Herald.DemoApp
herald-demo
```

The console printed a URL. You opened it. Here is what is on the screen.

- **The live feed.** The center of the page scrolls log events as they
  happen. Each row is one event: a timestamp, a level, a message, and
  any extra fields the event carried. This is a real Herald.OSS pipeline
  running inside the tool. It is not a mockup.
- **The levels.** Down the side you see the severity levels: Fatal,
  Error, Warning, Information, Debug, Verbose. Click one to filter the
  feed to that level and above. This is a view filter. It changes what
  *you* see, not what the pipeline keeps.
- **The Pipeline page.** This is where you change how the pipeline
  behaves. Add a level, raise the floor, add an enricher, add a sink.
  Your change rebuilds the pipeline and takes effect on the next event.
- **The JSON Pipeline page.** The same pipeline, shown as the config
  that built it. This is the source of truth. Everything the Pipeline
  page does, it does by editing this JSON.

> **Quick picture.** Think of the demo as a glass-walled mailroom. The
> live feed is the conveyor belt where you watch the mail go by. The
> Pipeline page is the control panel on the wall, where you change how
> mail gets sorted. The JSON page is the printed rulebook the mailroom
> runs on. Change the panel, and the rulebook updates to match.

### The one tool you will use for traffic

Every project below feeds the demo with `logcreator`, a small
command-line producer. Install it once:

```bash
go install github.com/mmpworks/logcreator/cmd/logcreator@latest
```

`logcreator` makes log events and POSTs them into the demo. The two
flags you will lean on:

- `--out http://localhost:5210/api/logs/incoming` sends events into the
  running demo. (Use whatever port the console printed. The default is
  the first free port from 5210.)
- `--rate N` sets how many events per second. This is your volume knob.

When real events arrive from `logcreator`, the demo's built-in synthetic
feed steps aside. You see *your* traffic flow through the same pipeline
shown on screen.

---

## Project 1, Add context to every event

**The goal.** Every log line should carry the basics: which machine,
which process, which thread, which request. You should not have to add
those by hand at every call site. An *enricher* adds them for you, to
every event, automatically.

**Step outline.**

1. Open the Pipeline page. Find the Enrichers panel.
2. See the seven enrichers Herald.OSS turns on by default: machine name,
   process id, thread id, and the rest.
3. Toggle one on. Watch the live feed. The enricher's field now tints
   inline inside the message, on every new event.
4. Toggle it off. The tint stops on the next event.
5. Send a burst with `logcreator` so you can see the enrichment land on
   outside traffic, not just the synthetic feed:
   ```bash
   logcreator --out http://localhost:5210/api/logs/incoming --rate 5
   ```

**What this teaches.** Enrichers are how you add context once and get it
everywhere. The context rides *inside* the event, so it travels to every
sink. You configure it in one place, and the pipeline applies it to every
event that passes through.

> CUPID note for this section: enrichers are *Composable*. You add the
> ones you want and leave the rest. The default seven cover the common
> case. The pipeline does not force a fixed bundle on you.

---

## Project 2, Keep secrets out of the logs

**The goal.** Logs leak. A token in a query string, a card number in a
request body, an email where it should be a hash. Once it lands in a
log, it lands in every sink, every backup, every screen. *Reshape Each
Event* is the step that fixes the event before any sink sees it. You
redact the secret at the pipeline, not at a thousand call sites.

> **Provisional.** The config shape for the Reshape Each Event step (the
> `eventProcessing` step) is still being wired. The steps below are the
> planned shape, not yet confirmed. Treat this whole section as a draft
> until the config surface lands.

**Step outline (provisional).**

1. Open the Pipeline page. Add the Reshape Each Event step.
2. Add a rule: match a field name (say `password` or `authorization`)
   and replace its value with `***`.
3. Send traffic that carries the secret field:
   ```bash
   logcreator --out http://localhost:5210/api/logs/incoming --rate 2
   ```
4. Watch the live feed. The matched field now shows `***` instead of the
   real value.
5. Confirm the redaction happens *before* the sinks. The console output
   and the live feed both show the masked value, because the reshape
   runs once, upstream of the fan-out.

**What this teaches.** Redaction belongs in the pipeline, not in your
application code. One rule covers every event. The secret never reaches
a sink, so it never reaches storage. The reshape runs once, before the
fan-out, so every destination sees the same safe event.

> CUPID note: the reshape step is *Predictable*. The same rule produces
> the same masked output every time, for every sink. There is no
> "redacted here, leaked there."

---

## Project 3, Tame a service that logs too much

**The goal.** One chatty service can drown your logs. Filtering and
sampling let you turn the volume down without turning the service off.
Three knobs: raise the floor (drop the low-severity noise), keep one in
N (sample), or cap the rate (throttle).

**Step outline.**

1. First, make some noise. Point `logcreator` at the demo at a high rate
   so the feed floods:
   ```bash
   logcreator --out http://localhost:5210/api/logs/incoming --rate 200
   ```
   The live feed should be a blur.
2. **Raise the floor.** On the Pipeline page, set the minimum level to
   Warning. Watch the Information and Debug events disappear from the
   feed. Volume drops immediately.
3. **Keep one in N.** Add sampling to the Level Filtering step. Keep 1
   in 10. The feed thins to a tenth without losing the shape of the
   traffic.
4. **Cap the rate.** Add throttling. No more than, say, 20 events per
   second. The feed holds steady at the cap even while `logcreator` keeps
   flooding.
5. Drop the rate back down (`--rate 5`) and confirm the feed recovers.

**What this teaches.** You have three independent tools for volume, and
they stack. The floor drops by severity. Sampling drops by count.
Throttling caps by time. You pick the one (or the mix) that fits the
service, and you tune it live while the traffic runs.

> **Provisional.** Sampling wires through the real Core sampling filter
> today. Throttling and adaptive sampling are persisted in the config
> and round-trip, but their live-apply path is still being confirmed.
> The "Cap the rate" step is the part to treat as draft.

---

## Project 4, Catch the last moments before a crash

**The goal.** When a service crashes, the logs you most want are the
ones just before the crash. And those are usually the ones you dropped
for being too low-severity. The flight recorder, *Keep the Last Few for
Crashes*, holds a rolling buffer of recent low-severity events and
flushes them when something goes wrong. You get the pre-crash tail you
would otherwise have thrown away.

**Step outline.**

1. **Capture a clean run.** Run `logcreator` with a fixed seed so the
   run is repeatable, and save the output:
   ```bash
   logcreator --seed 42 --out http://localhost:5210/api/logs/incoming --rate 10
   ```
   Let it run a fixed number of events, then stop. Save the feed as your
   "good run."
2. **Turn on the flight recorder.** On the Pipeline page, add the Keep
   the Last Few for Crashes step. Set its buffer and its trigger level.
3. **Capture a bad run.** Run the *same* seed, but this time let it
   produce an error event that trips the recorder:
   ```bash
   logcreator --seed 42 --out http://localhost:5210/api/logs/incoming --rate 10
   ```
   Save this as your "bad run." Because the seed matches, the two runs
   are identical up to the point the error appears.
4. **Compare the two runs.** Load both saved runs into the compare tool
   (`logviews`). Line them up side by side.
5. **Read the recovered tail.** The `+` rows in the compare view are the
   events the bad run kept that the good run did not. Those are the
   low-severity events the flight recorder held in its buffer and flushed
   when the error tripped it. That is the pre-crash tail, recovered.

**What this teaches.** The flight recorder buys you the context around a
failure without paying to keep that context all the time. It holds
recent events cheaply and only commits them when something trips the
trigger. The seed-matched compare is the proof: same input, and the only
difference is the tail the recorder saved.

> **Quick picture.** A flight recorder on a plane does not stream every
> reading to the ground. It keeps the last stretch in a loop and
> preserves it only when something goes wrong. Herald's flight recorder
> does the same for your logs: a rolling buffer of recent events, kept
> cheap, flushed on a trigger.

> CUPID note: the flight recorder is *Domain-based*. It is named for what
> it does in the real world, keep the last few readings for after a
> crash, not for a generic "ring buffer logger." The name carries the
> intent.

---

## Project 5, Ship the logs to production

**The goal.** The demo shows logs in your browser. Production needs them
somewhere durable and searchable. This project sends the demo's logs to
**Grafana Loki** running in Docker, so you can query them in Grafana the
way you would in a real deployment. You reuse the working Loki + Grafana
stack Herald already ships at `Modules/Herald.Sci/samples/loki-stack`.

This project has its own page because it needs a Docker setup.

➡️ **[Project 5, Ship the logs to production](05-ship-to-production.md)**

**What this teaches.** A sink is how Herald delivers events to a
destination. *Deliver to Every Destination*, the fan-out, lets one
pipeline feed many sinks at once: your console, your live feed, and Loki,
all from the same events. You add the Loki sink, point it at your Docker
Loki, set it live, and the same events you have been watching all guide
start landing in Grafana.

---

## Where to go next

- [The kernel fast path, what it is and why it exists](../explanation/kernel-vs-chain.md)
- [Quickstart, the smallest useful pipeline](../quickstart.md)
