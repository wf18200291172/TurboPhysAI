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
- Optional linter or formatting configuration files.

## Outputs required
- Lint/formatting check results, summary of fixes applied, and remaining unverified items.

## Execution steps

1. **Check git status and modified files**
   ```bash
   git status
   git diff --name-only
   ```

2. **Run formatting and style checks**
   ```bash
   # Run project formatting / lint checks
   python3 -m flake8 turbo_physai/ test/ || true
   python3 -m black --check turbo_physai/ test/ || true
   python3 -m isort --check-only turbo_physai/ test/ || true
   ```

3. **Apply automatic formatting (if authorized)**
   ```bash
   black turbo_physai/ test/
   isort turbo_physai/ test/
   ```

4. **Verify remaining issues**
   - Address any remaining static analysis warnings manually
   - Verify that all modified files pass the check

## Troubleshooting

### Error: "black would reformat file"
- **Cause**: Code style does not match Black formatting rules.
- **Fix**: Run `black <file_path>` to automatically reformat.

### Error: "Import sort order incorrect (isort)"
- **Cause**: Python imports are not sorted according to isort rules.
- **Fix**: Run `isort <file_path>` to fix import ordering.
