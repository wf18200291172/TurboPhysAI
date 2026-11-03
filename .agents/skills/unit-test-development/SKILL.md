---
name: unit-test-development
description: Develop unit tests for new code changes or regression tests for bug fixes in TurboPhysAI.
---

## When to use
- Adding new features, operators, or optimization groups requiring test coverage.
- Writing regression tests for fixed bugs or CI failures.

## When not to use
- For full end-to-end model training correctness evaluation (use `model-correctness-validation` instead).

## Inputs expected
- Target code changes, expected behaviors, and existing test patterns under `test/`.

## Outputs required
- Unit test code, execution results, test coverage summary, and edge case coverage notes.
