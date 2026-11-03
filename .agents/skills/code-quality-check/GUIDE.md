# Code Quality Check Guide

## 1. Context & Scope

The `code-quality-check` skill ensures that all code modifications in TurboPhysAI conform to project formatting and static analysis standards before merging. It aligns with the external Quality Gate (`HYGON-AI/quality-gate`).

## 2. Execution Workflow

### Step 1: Pre-check
Identify modified files using git diff to avoid scanning the entire repository unnecessarily.

### Step 2: Formatting Tools
- **Black**: Enforces uncompromising Python code formatting.
- **isort**: Automatically sorts and categorizes Python imports.
- **Flake8 / Pylint**: Catches syntax errors, unused imports, and style violations.

### Step 3: Resolution
- Automated fixes (`black`, `isort`) should be applied first.
- Manual fixes for linter warnings must preserve original code semantics.

## 3. Common Pitfalls
- **Unused imports**: Leftover from refactoring; remove them to keep code clean.
- **Line length violations**: Keep lines within the project's max length (typically 88 or 100 chars).
- **Type hinting**: Ensure new functions have basic type annotations where required by mypy.
