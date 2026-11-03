---
name: code-review
description: Review code changes for architectural consistency, style compliance, documentation, license headers, shared code opportunities, and open-source standards in TurboPhysAI.
---

## When to use
- Reviewing PRs or significant refactoring before merge to main branch
- Assessing code for compliance with TurboPhysAI architecture, style guide, and open-source standards

## When not to use
- Formatting fixes (delegate to code-quality-check Skill)
- Running automated linting (use code-quality-check with black, isort, flake8)
- Performance profiling (use performance-analysis-and-validation Skill)

## Inputs expected
- Pull request diff or changed files
- Target module and impacted feature scope
- Any architecture or design context

## Execution steps

### L1: Compliance Check (Automated)
- [ ] **License Header**: Every .py file must include `# Copyright 2026 Hygon ... SPDX-License-Identifier: BSD-3-Clause`
- [ ] **Import Organization**: Imports grouped stdlib → third-party → local, sorted via isort
- [ ] **Indentation**: Consistent 4-space indentation, no mixed tabs/spaces
- [ ] **Docstrings**: Public interfaces have clear docstrings (English or Chinese) with parameters, returns, exceptions

### L2: Architecture & Design Review
- [ ] **Separation of Concerns**: Optimization logic isolated from model source code
- [ ] **Code Reuse**: Identify shared patterns (e.g., sampler/assigner logic in MMDetection3D) that should move to `optimizations/common/`
- [ ] **Caching & Security**: Check cache directory permissions (0o700 or 0o755), avoid hardcoded sensitive config
- [ ] **Configuration**: Ensure launcher preservation and optimization scope clearly defined

### L3: TurboPhysAI-Specific Patterns
- [ ] **Upstream Commit Pinning**: Model patches must reference fixed upstream commit
- [ ] **HCU-Native Optimization**: Optimizations target Hygon HCU / DTK specifically, not generic hardware
- [ ] **No Model Source Modification**: Core model source should remain untouched

## Outputs required
- Categorized review findings (severity: high/medium/low), failure scenarios, actionable recommendations, and decision tree for routing complex architectural reviews.

## Execution steps

| Issue | Cause | Solution |
|-------|-------|----------|
| "License Header Missing" | New .py file created without header | Add `# Copyright 2026 Hygon... BSD-3-Clause` to file top |
| "Import Order Incorrect" | isort not run before commit | Run `isort <file>` or enable pre-commit hook |
| "Misleading Comment" | Comment contradicts or obscures actual logic | Clarify comment to match implementation |
| "Code Duplication in Operator Logic" | Sampler/assigner patterns repeated | Extract to `optimizations/common/mmdet3d/` for reuse |
| "Unsafe Cache Directory" | Permissions too open or hardcoded path | Use configurable paths with restricted permissions (0o700) |

## Known limitations & edge cases

- Manual architectural review required for novel optimization patterns (not in playbook)
- Some model-specific patches require domain expert sign-off
- Cross-framework optimizations (e.g., ONNX export) may need separate review track

## References
- [CONTRIBUTING.md](../../../CONTRIBUTING.md)
- [Architecture](../../../docs/zh/design/architecture.md)
- [License Requirements](../../../THIRD_PARTY_NOTICES.md)
