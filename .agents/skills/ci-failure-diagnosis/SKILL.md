---
name: ci-failure-diagnosis
description: Diagnose CI build, test, or hardware runner failures and provide reproducible reproduction steps and fixes.
---

## When to use
- When GitHub Actions CI or HCU pipeline jobs fail.
- When encountering environment-specific test failures or compilation errors.

## When not to use
- For routine local code formatting checks before submission.

## Inputs expected
- CI log snippets, workflow error messages, and commit context.

## Outputs required
- Root cause evidence, local reproduction steps, and verified patch or fix instructions.
