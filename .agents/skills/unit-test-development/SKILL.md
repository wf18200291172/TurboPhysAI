---
name: unit-test-development
description: Develop unit tests for new code changes, operators, or regression tests for bug fixes using pytest and coverage in TurboPhysAI.
---

## When to use
- Adding new features, custom operators, or optimization groups
- Writing regression tests for bug fixes
- Improving code coverage for critical paths
- Before submitting a PR with new functionality

## When not to use
- For integration tests requiring full system setup or HCU hardware (those use `@pytest.mark.hcu` and are managed separately)
- For performance benchmarking (use dedicated benchmark suite)

## Inputs expected
- Source code file paths or git diff of changes
- Description of what needs testing or which bugs to regress-test

## Outputs required
- Test case code (`test_*.py` files), coverage reports, and test run logs
- Summary of test coverage increase and critical paths verified
