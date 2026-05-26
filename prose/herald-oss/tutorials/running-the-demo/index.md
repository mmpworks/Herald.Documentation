---
title: How to run the Herald Demo, five mini-projects
slug: tutorials/running-the-demo
category: tutorial
audience: new-adopter
since: 0.9.0
status: walk-verified
walk-verified: true
walk-verified-on: 2026-05-26
walk-verified-notes: "Full e2e walk, all five mini-projects, 17/17 steps. M5 visualization step is Docker-dependent (loki-stack)."
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

> **Walk-verified.** A full run through all five projects passed, every
> step. You can follow these in order and each one works against the demo
> as shipped. One step in Project 5 needs Docker (standing up Grafana
> and Loki locally), and that page calls it out where it applies.

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

**Steps (walk-verified).**

1. Open the Pipeline page. Find the Enrichers panel.
2. The seed pipeline wires seven Core enrichers. Four of them write a
   real value on every event and show up in the feed: **machine name**,
   **process id**, **thread id**, and **correlation id**. The other
   three are wired and ready but stay quiet until they have something to
   say. The exception enricher, for example, only fires on an event
   that carries an exception.
3. Toggle one of the four on. Watch the live feed. The enricher's field
   now tints inline, right inside the message, on every new event.
4. Toggle it off. The tint stops on the next event.
5. Send a burst with `logcreator` so you see the enrichment land on
   outside traffic, not just the demo's built-in feed:
   ```bash
   logcreator --out http://localhost:5210/api/logs/incoming --rate 5
   ```

**What this teaches.** Enrichers are how you add context once and get it
everywhere. The context rides *inside* the event, so it travels to every
sink. You configure it in one place, and the pipeline applies it to every
event that passes through. The four lit fields are the ones that always
have a value; the rest wait for the event that needs them.

> CUPID note for this section: enrichers are *Composable*. You add the
> ones you want and leave the rest. The seven seed enrichers cover the
> common case. The pipeline does not force a fixed bundle on you.

---

## Project 2, Keep secrets out of the logs

**The goal.** Logs leak. A token in a query string, a card number in a
request body, an email where it should be a hash. Once it lands in a
log, it lands in every sink, every backup, every screen. *Reshape Each
Event* is the step that fixes the event before any sink sees it. You
redact the secret at the pipeline, not at a thousand call sites.

**The rule shape.** A redaction rule names a field and a mode. The
modes are `remove`, `mask`, and `hash`. The config is a `rules` array,
one entry per field:

```json
{
  "rules": [
    { "field": "password", "mode": "remove" },
    { "field": "ssn",       "mode": "hash" },
    { "field": "sessionId", "mode": "mask", "visibleChars": 4 }
  ]
}
```

- `remove` drops the field. `password: [REDACTED]`.
- `hash` replaces the value with a SHA-256 digest. `ssn: sha256:…`. The
  value is gone but two events with the same secret still hash alike, so
  you can correlate without storing the secret.
- `mask` keeps a few characters and stars the rest. `visibleChars: 4`
  leaves the last four. A masked `sessionId` keeps just enough to match
  a session in a support call without exposing the token.

This is Herald's **Community-tier** redaction: a compiled rule list, the
same `CompiledRedactionProcessor` an app would wire by hand. It is not
the Enterprise DSL parser, which is a separate, richer surface. For
field-name redaction, the compiled list is all you need.

**Steps (walk-verified).**

1. Open the Pipeline page. Open the Reshape Each Event step. Add the
   three rules above.
2. Send traffic that carries the secret fields:
   ```bash
   logcreator --out http://localhost:5210/api/logs/incoming --rate 2
   ```
3. Watch the **Live Viewer**. The matched fields now show their redacted
   form: `password: [REDACTED]`, `ssn: sha256:…`, a masked `sessionId`.

> **Where the redaction shows, and where it does not.** The redacted
> values appear in the **Live Viewer**, the streaming feed. They do
> **not** appear in `/api/logs/recent`. That endpoint is the raw
> pre-pipeline ingest buffer: it holds events as they arrived, before
> the pipeline reshaped them. So if you peek at the recent buffer you
> may still see the original value. That is expected. The feed is the
> redacted view; the recent buffer is the raw warm-start view. The
> demo redacts on the feed through `DrainRedactor`, which runs the same
> Community-tier processor against each event on its way to the sinks
> and the live stream.

**What this teaches.** Redaction belongs in the pipeline, not in your
application code. One rule covers every event. The secret is reshaped
before the event reaches a sink, so it never reaches storage. The same
rule produces the same redacted output every time, for every sink.

> CUPID note: the reshape step is *Predictable*. The same rule produces
> the same masked output every time, for every sink. There is no
> "redacted here, leaked there."

---

## Project 3, Tame a service that logs too much

**The goal.** One chatty service can drown your logs. Filtering and
sampling let you turn the volume down without turning the service off.
Three knobs: raise the floor (drop the low-severity noise), keep one in
N (sample), or cap the rate (throttle).

**Steps (walk-verified).**

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

All three knobs apply live. They wire through Herald.OSS's multi-filter
seam, so you can stack the floor, sampling, and throttling on the same
Level Filtering step and tune any of them while the traffic runs.

**What this teaches.** You have three independent tools for volume, and
they stack. The floor drops by severity. Sampling drops by count.
Throttling caps by time. You pick the one (or the mix) that fits the
service, and you tune it live while the traffic runs.

> **The two places an event can get dropped, and why they look
> different.** This is the one thing to keep straight. There are two
> gates, and they are not the same gate.
>
> 1. **Ingest accepts every *leveled* event.** When `logcreator` POSTs
>    to `/api/logs/incoming`, the demo accepts any event that carries a
>    level (Debug, Information, all of it). Those events land in the raw
>    ingest buffer (`/api/logs/recent`). An event with *no* level is a
>    different story: it is rejected right at ingest and never appears
>    anywhere. (A log without a severity is not a log Herald will route.)
> 2. **The pipeline floor is the real gate.** Once a leveled event is in
>    the pipeline, the Level Filtering step is the floor. Set the floor to
>    Warning, and a Debug event gets dropped *before* it reaches the sinks
>    or the live feed.
>
> So here is the part that trips people up: after you raise the floor to
> Warning, a Debug event can still show up in `/api/logs/recent` (it
> passed ingest) but **not** in the live feed (the floor dropped it). That
> is not a bug. The recent buffer is the raw arrivals; the live feed is
> what survived the pipeline. A below-floor leveled event passes ingest,
> then the pipeline drops it. A level-less event never gets that far.

---

## Project 4, Catch the last moments before a crash

**The goal.** When a service crashes, the logs you most want are the
ones just before the crash. And those are usually the ones you dropped
for being too low-severity. The flight recorder, *Keep the Last Few for
Crashes*, holds a rolling buffer of recent low-severity events and
flushes them when something goes wrong. You get the pre-crash tail you
would otherwise have thrown away.

**Steps (walk-verified).**

1. **Turn on the flight recorder.** On the Pipeline page, add the Keep
   the Last Few for Crashes step. Set its buffer (how many recent events
   it holds) and its trigger level. Set the trigger to **Error**, so an
   Error event flushes the buffer.
2. **Capture a clean run.** Drive a stretch of normal traffic and let it
   settle. Save it in Log Views as your "good run" and call it A. No error
   trips the recorder, so A is just the events that passed the floor.
3. **Trip an Error and capture the bad run.** Use the beaker (the inject
   control) to send an event at **Error**. That trips the recorder: it
   flushes its buffer of recent low-severity events alongside the error.
   Save this as your "bad run" and call it B.
4. **Compare A and B.** Open Log Views and load both runs into the
   compare view, side by side.
5. **Read the recovered tail.** The `+` rows in the compare (the rows in
   B that A does not have) are the low-severity events the flight
   recorder was holding in its buffer and flushed when the error tripped
   it. That is the pre-crash tail, recovered.

**What this teaches.** The flight recorder buys you the context around a
failure without paying to keep that context all the time. It holds recent
events cheaply and only commits them when something trips the trigger.
The dual-pane compare is the payoff: line A against B, and the only
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
Loki, set it live, and the same events you have been watching all along
start landing in Grafana. The sink reaches Live and stays healthy on the
walk; the Grafana visualization step needs Docker, which the Project 5
page sets up.

---

## Where to go next

- [The kernel fast path, what it is and why it exists](../explanation/kernel-vs-chain.md)
- [Quickstart, the smallest useful pipeline](../quickstart.md)
