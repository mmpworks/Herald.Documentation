---
title: Logging practices, each with its Herald API
slug: reference/logging-practices
category: reference
subcategory: checklist
audience: intermediate
since: 0.14.0
last-reviewed: 2026-11-03
related:
  - quickstart
  - explanation/kernel-vs-chain
related-records: []
mirrors:
  - Herald.OSS samples/logging-practices (one runnable file per row)
source-rationale: green-field. The twelve practices come from the video "12 Logging BEST Practices in 12 minutes" (YouTube I2mWnh66Bkg). Each API was checked against Herald.OSS main at 45e582e.
---

# Logging practices, each with its Herald API

The table maps twelve common logging practices to the Herald API that covers
each one. Every row links to the source file and to a runnable sample. The
samples are one console app with one small file per practice.

Run every practice:

```bash
cd samples/logging-practices
dotnet run -c Release
```

Run one practice by number:

```bash
dotnet run -c Release -- 9
```

## The checklist

| # | Practice | Herald API | Source | Sample |
|---|----------|------------|--------|--------|
| 1 | Clear objectives | A team habit. Write the decision down as code: a catalog of `LogEventId` and `LogCategory` values, declared before any call site uses them. | [`LogEventId.cs`][src-eventid] | [01][s01] |
| 2 | Log levels and adjustable verbosity | `LogLevelSwitch` plus `WithFastDynamicLevel`, which installs `FastPathDynamicLevel`. Change the switch and the next call reads the new level. `WithFlightRecorder` (`FlightRecorderLogger`) holds lower-level events in a ring buffer and releases them when an error arrives. | [`FastPathDynamicLevel.cs`][src-dynlevel], [`FlightRecorderLogger.cs`][src-flight] | [02][s02] |
| 3 | Structured logging | Every template hole becomes a named property. A `.ndjson` path on `WithFileSink` selects the built-in JSON file sink. | [`QuickLogBuilder.Sinks.cs`][src-sinks] | [03][s03] |
| 4 | Context in every entry | `ActivityEnricher` stamps the trace id and span id on each event. `TraceContextPropagator` starts a trace and writes the W3C `traceparent` header. | [`ActivityEnricher.cs`][src-activity], [`TraceContextPropagator.cs`][src-propagator] | [04][s04] |
| 5 | Log sampling | Keep errors, sample success. `AdaptiveSamplingFilter` (`WithAdaptiveSampling`), `PriorityWindowSamplingFilter` (a per-level floor per time window), and `FastPathSampler` (`WithFastSampling`, on the kernel path). | [`AdaptiveSamplingFilter.cs`][src-adaptive], [`PriorityWindowSamplingFilter.cs`][src-window], [`FastPathSampler.cs`][src-fastsampler] | [05][s05] |
| 6 | Canonical log lines and distributed tracing | `UseSerilogRequestLogging()` installs `RequestLoggingMiddleware`: one summary line per HTTP request, shaped by `RequestLoggingOptions`. `SpanScope` logs entry and exit of the work inside the request, with the elapsed time. | [`RequestLoggingMiddleware.cs`][src-reqmw], [`RequestLoggingOptions.cs`][src-reqopts], [`SpanScope.cs`][src-span] | [06][s06] |
| 7 | Aggregate and centralize | The OTLP sinks. `WithOtlpJsonSink` and `WithOtlpProtobufSink` point a pipeline at an OpenTelemetry collector. The sinks are `OtlpJsonLogSink` and `OtlpProtobufLogSink` in `MMP.Herald.Sinks.Otlp`, and `OtlpGrpcLogSink` in `MMP.Herald.Sinks.OtlpGrpc`. `OtelLogRecord` maps a Herald event to the OpenTelemetry log record. | [`QuickLogBuilder.NetworkSinks.cs`][src-netsinks], [Herald.Sinks.Otlp][src-otlpsink], [Herald.Sinks.OtlpGrpc][src-otlpgrpc], [`OtelLogRecord.cs`][src-otelrecord] | [07][s07] |
| 8 | Retention policies | `FileSinkPolicy` gives each file sink its own lifetime: `WithMinLevel`, `WithRetentionDays`, and `WithTotalSizeCap`, plus the rolling interval. | [`FileSinkPolicy.cs`][src-filepolicy] | [08][s08] |
| 9 | Secure your logs | The HMAC chain. `HmacChainLogger` links each event to the one before it with HMAC-SHA256. `VerifyChain` returns the index of the first altered event, or -1 when the chain is intact. Encryption in transit, encryption at rest, and access control belong to the log store. | [`HmacChainLogger.cs`][src-hmac] | [09][s09] |
| 10 | Keep sensitive data out | `CompiledRedactionProcessor` (`WithCompiledRedaction`) masks, hashes, or replaces named properties before any sink sees them. `FastPathRedactor` (`WithFastRedaction`) applies the same rule shape on the kernel path. `LogPropertyVisibility.PiiSensitive` tags a property as personal data. | [`CompiledRedactionProcessor.cs`][src-redact], [`FastPathRedactor.cs`][src-fastredact], [`LogPropertyVisibility.cs`][src-visibility] | [10][s10] |
| 11 | Performance impact | Herald publishes per-call and soak numbers with the harness that produced them. The sample measures one typed call into the null sink on your machine. | [`docs/benchmarks/`][src-bench] | [11][s11] |
| 12 | Logs are not metrics | `LogMetricExtractor` turns matching log events into counters and gauges as they pass through the pipeline. `OtlpMetricsExporter` ships `GameMetrics` snapshots to an OTLP collector. | [`LogMetricExtractor.cs`][src-metrics], [`OtlpMetricsExporter.cs`][src-otlpmetrics] | [12][s12] |

## What the sample prints

These lines come from one run of the sample. Timestamps, trace ids, and hashes
change on every run.

Practice 5, sampling 100 info events and 5 errors:

```text
  AdaptiveSamplingFilter         kept: information 10, error 5
  PriorityWindowSamplingFilter   kept: information 5, error 5
```

Practice 9, the HMAC chain before and after one message is changed:

```text
  verify original: -1  (-1 = intact)
  verify tampered: 1  (index of the first altered event)
```

Practice 10, what a sink receives after redaction:

```text
  [information] Receipt sent to ***************com for card [REDACTED]  { email=***************com, cardNumber=[REDACTED] }
  [information] Identity check passed  { taxId=hmac-sha256:3586837469153de30688fc7045fba9f4 }
```

## Technical Notes

The redaction row names two processors: one for the chain path and one for
the kernel path. The *kernel path* is the fast route for events that need no
decorator chain. Both processors take the same `CompiledRedactionRule`, so a
rule you write once runs on either path. That is CUPID's *Composable*
property: the pipeline step changes, the rule stays.

Row 7 has two halves. The builder methods live in Herald.OSS. The sink code
ships as a separate package in [Herald.Sinks][src-sinksrepo]. You add the
package when a pipeline sends OTLP.

[src-eventid]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Events/LogEventId.cs
[src-dynlevel]: https://github.com/mmpworks/Herald.OSS/blob/main/native/dotnet/Pipeline/Kernel/FastPathDynamicLevel.cs
[src-flight]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Addons/GamePerformance/FlightRecorderLogger.cs
[src-sinks]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Quick/QuickLogBuilder.Sinks.cs
[src-activity]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Enrichers/ActivityEnricher.cs
[src-propagator]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Addons/Observability/TraceContextPropagator.cs
[src-adaptive]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Addons/MetricExtraction/AdaptiveSamplingFilter.cs
[src-window]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Filters/PriorityWindowSamplingFilter.cs
[src-fastsampler]: https://github.com/mmpworks/Herald.OSS/blob/main/native/dotnet/Pipeline/Kernel/FastPathSampler.cs
[src-reqmw]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Serilog.AspNetCore/RequestLoggingMiddleware.cs
[src-reqopts]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Serilog.AspNetCore/RequestLoggingOptions.cs
[src-span]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Addons/Instrumentation/SpanScope.cs
[src-netsinks]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Quick/QuickLogBuilder.NetworkSinks.cs
[src-otlpsink]: https://github.com/mmpworks/Herald.Sinks/tree/main/src/Herald.Sinks.Otlp
[src-otlpgrpc]: https://github.com/mmpworks/Herald.Sinks/tree/main/src/Herald.Sinks.OtlpGrpc
[src-otelrecord]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Addons/OtlpSinks/OtelLogRecord.cs
[src-filepolicy]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Configuration/FileSinkPolicy.cs
[src-hmac]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Addons/Compliance/HmacChainLogger.cs
[src-redact]: https://github.com/mmpworks/Herald.OSS/blob/main/native/dotnet/Pipeline/Processors/CompiledRedactionProcessor.cs
[src-fastredact]: https://github.com/mmpworks/Herald.OSS/blob/main/native/dotnet/Pipeline/Kernel/FastPathRedactor.cs
[src-visibility]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Templating/LogPropertyVisibility.cs
[src-bench]: https://github.com/mmpworks/Herald.OSS/tree/main/docs/benchmarks
[src-metrics]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Addons/MetricExtraction/LogMetricExtractor.cs
[src-otlpmetrics]: https://github.com/mmpworks/Herald.OSS/blob/main/src/Addons/OtlpSinks/OtlpMetricsExporter.cs
[src-sinksrepo]: https://github.com/mmpworks/Herald.Sinks

[s01]: https://github.com/mmpworks/Herald.OSS/blob/main/samples/logging-practices/Practices/01-ClearObjectives.cs
[s02]: https://github.com/mmpworks/Herald.OSS/blob/main/samples/logging-practices/Practices/02-LevelsAndVerbosity.cs
[s03]: https://github.com/mmpworks/Herald.OSS/blob/main/samples/logging-practices/Practices/03-StructuredLogging.cs
[s04]: https://github.com/mmpworks/Herald.OSS/blob/main/samples/logging-practices/Practices/04-ContextInEveryEntry.cs
[s05]: https://github.com/mmpworks/Herald.OSS/blob/main/samples/logging-practices/Practices/05-LogSampling.cs
[s06]: https://github.com/mmpworks/Herald.OSS/blob/main/samples/logging-practices/Practices/06-CanonicalLogLines.cs
[s07]: https://github.com/mmpworks/Herald.OSS/blob/main/samples/logging-practices/Practices/07-AggregateAndCentralize.cs
[s08]: https://github.com/mmpworks/Herald.OSS/blob/main/samples/logging-practices/Practices/08-RetentionPolicies.cs
[s09]: https://github.com/mmpworks/Herald.OSS/blob/main/samples/logging-practices/Practices/09-SecureYourLogs.cs
[s10]: https://github.com/mmpworks/Herald.OSS/blob/main/samples/logging-practices/Practices/10-KeepSensitiveDataOut.cs
[s11]: https://github.com/mmpworks/Herald.OSS/blob/main/samples/logging-practices/Practices/11-PerformanceImpact.cs
[s12]: https://github.com/mmpworks/Herald.OSS/blob/main/samples/logging-practices/Practices/12-LogsAreNotMetrics.cs
