---
name: performance-analysis-and-validation
description: Identify runtime bottlenecks and verify whether optimizations deliver reliable performance speedups using profiling tools in TurboPhysAI.
---

## When to use
- Analyzing performance hot-spots and profiling training bottlenecks on Hygon DCU.
- Running ablation and comparative benchmarks for optimizations.

## When not to use
- For functional correctness testing or code style checks.

## Inputs expected
- Profiling traces (hipprof/dtk), baseline vs optimized run configs, and hardware environment specs.

## Outputs required
- Hotspot analysis report, comparative benchmark results, speedup conclusions, and verification logs.
