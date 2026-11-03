---
name: code-review
description: Review code changes for behavioral risks, interface consistency, concurrency issues, and verification completeness in TurboPhysAI.
---

## When to use
- Reviewing PRs or significant refactoring before merge.
- Assessing architectural impact of custom operators or optimization groups.

## When not to use
- For automated syntax and lint formatting checks (use `code-quality-check` instead).

## Inputs expected
- Git diff or specific pull request reference, context on target module.

## Outputs required
- Verified findings ranked by severity, failure scenarios, and actionable recommendations.
