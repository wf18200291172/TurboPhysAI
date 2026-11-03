---
name: performance-analysis-and-validation
description: Identify runtime bottlenecks and verify whether optimizations deliver reliable performance speedups using DTK profiling tools on Hygon HCU.
---

## When to use
- Analyzing operator-level performance hotspots in model training
- Measuring speedup from optimizations before and after changes
- Investigating latency regressions or throughput drops

## When not to use
- Static code analysis (use `code-review` instead)
- Unit test debugging (use `ci-failure-diagnosis` instead)
- First-pass model correctness validation (use `model-correctness-validation` first)

## Inputs expected
- Pre/post optimization trace artifacts (`.trace`, `.timeline`, or equivalents from DTK profiler)
- Model architecture and batch size
- Hardware (HCU) configuration and DTK version

## Outputs required
- Performance analysis report with operator-level breakdowns
- Speedup measurements with confidence intervals
- Bottleneck identification and prioritization
- Recommendations for further optimization
