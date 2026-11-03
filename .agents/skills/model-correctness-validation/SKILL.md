---
name: model-correctness-validation
description: Verify that model training and evaluation results satisfy required metrics and numerical stability tolerances after integration and optimization.
---

## When to use
- Validating accuracy and correctness after model integration or applying optimization groups.
- Checking training stability, loss convergence, and numerical tolerances (including NaN/Inf checks).

## When not to use
- For basic code linting or unit test execution.

## Inputs expected
- Baseline and optimized training/eval outputs, evaluation datasets, and metric tolerances.

## Outputs required
- Aligned evaluation metrics, comparison report, stability verification records, and acceptance summary.
