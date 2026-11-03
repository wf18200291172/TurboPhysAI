---
name: code-quality-check
description: Check whether code changes adhere to TurboPhysAI style guide and CI quality gates, and fix formatting or lint issues.
---

## When to use
- Before submitting code changes or pull requests.
- When CI quality gate fails on formatting, linter, or type checks.

## When not to use
- For deep logical code review or security auditing (use `code-review` instead).

## Inputs expected
- Target file paths or git diff of current changes.

## Outputs required
- Lint/formatting check results, summary of fixes applied, and remaining unverified items.
