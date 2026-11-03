# Unit Test Development Guide

## 1. When to Read This Guide
When writing new unit tests, adding regression tests for bug fixes, or checking code coverage in TurboPhysAI.

## 2. Testing Conventions & Rules

- **Framework**: Use `pytest` for all unit and integration tests.
- **File Structure**:
  - `test/engine/`: Engine execution, configuration generators, and handler tests.
  - `test/operators/`: Custom operator correctness tests.
  - `test/optimizations/`: Optimization group and recipe tests.
- **Markers**:
  - Use `@pytest.mark.hcu` for tests requiring a real Hygon HCU device and compiled native extensions.
  - Use `@pytest.mark.model_deps` for tests requiring upstream model dependency stacks.
- **Coverage**: Maintain high test coverage using `coverage` and `diff-cover` as configured in `requirements-test.txt`.

## 3. Example Test Structure

```python
import pytest
from turbo_physai import apply

def test_engine_basic():
    # Test logic here
    assert True

@pytest.mark.hcu
def test_native_operator():
    # Test requiring HCU hardware
    pass
```
