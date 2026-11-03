# TurboPhysAI Code Review Guide

## Common Issues Classification Based on PR History

This guide synthesizes code review feedback from analyzing actual TurboPhysAI pull requests, identifying recurring review issues and providing a decision tree.

### Reference Pull Requests

This analysis is based on the following real TurboPhysAI PRs:

- [PR #28: feat(dit4dit): add TurboPhysAI optimization support](https://github.com/HYGON-AI/TurboPhysAI/pull/28) – License headers, indentation, misleading comments
- [PR #29: Feat/Openpi Optimization](https://github.com/HYGON-AI/TurboPhysAI/pull/29) – Security concerns (shared cache), kernel file generation
- [PR #19: Feature/cosmos3 patch](https://github.com/HYGON-AI/TurboPhysAI/pull/19) – Configuration clarity, launcher preservation, optimization scoping
- [PR #33: Feat/Pointpillars Optimization](https://github.com/HYGON-AI/TurboPhysAI/pull/33) – Code reuse opportunities (MMDetection3D sampler/assigner)
- [PR #32: ci: align HCU base image with release workflow](https://github.com/HYGON-AI/TurboPhysAI/pull/32) – Configuration synchronization, testing notes

---

## Common Issues Quick Reference

| Issue Type | Severity | Check Frequency | Related PRs |
|-----------|----------|-----------------|------------|
| **Missing License Header** | 🔴 High | Every .py file | #28 |
| **Import Sort Non-Compliant** | 🟡 Medium | Import blocks | #28, #29 |
| **Inconsistent Indentation** | 🟡 Medium | Code blocks | #28 |
| **Misleading/Missing Comments** | 🟡 Medium | Complex logic | #28 |
| **Security Concerns** | 🔴 High | Permissions, caching | #29 |
| **Kernel File Generation** | 🟡 Medium | Build artifacts | #29 |
| **Configuration Clarity** | 🟡 Medium | Setup logic | #19 |
| **Architecture Decision** | 🟡 Medium | Major changes | #19, #32 |
| **Code Duplication/Reuse Opportunity** | 🟡 Medium | Optimization code | #33 |

---

## Decision Tree: L1 Compliance → L2 Architecture → L3 Performance

### L1: Compliance Check (Automated)

- [ ] **License Header**: Every `.py` file must start with `# Copyright 2026 Hygon... SPDX-License-Identifier: BSD-3-Clause`
- [ ] **Import Organization**: Imports grouped stdlib → third-party → local, sorted via isort
- [ ] **Formatting**: Code conforms to `black` spec, no mixed tabs/spaces
- [ ] **Docstrings**: Public interfaces have clear English documentation with parameters, return values, exceptions

### L2: Architecture & Design Review

- [ ] **Module Boundaries**: Changes respect existing module structure or create new modules with clear responsibility
- [ ] **Shared Code**: Recurring patterns (samplers, assigners, profilers) extracted to `optimizations/common/<domain>/`
- [ ] **Configuration Management**: No hardcoded credentials, sensitive paths, or internal IPs in code or docs
- [ ] **Error Handling**: Exceptions are descriptive, capture context without leaking internals

### L3: Performance & Optimization Review

- [ ] **Algorithmic Soundness**: Optimization doesn't trade correctness for speed without documented trade-offs
- [ ] **Benchmark Coverage**: Performance improvements backed by before/after metrics on actual hardware
- [ ] **Resource Management**: No resource leaks (memory, file handles, GPU allocations)

---

## Common Patterns & Mitigations

| Finding | Root Cause | Mitigation |
|---------|-----------|-----------|
| License Header Missing | New file without header template | Copy header from existing file, add Copyright 2026 Hygon |
| Import Disorder | Manual editing without isort | Run `isort <file>` to auto-sort |
| Inconsistent Indentation | Mixed tabs/spaces | Configure editor tab width = 4 spaces, run `black .` |
| Misleading Comment | Author assumptions unclear | Update comment to explain WHY not WHAT |
| Security Concern (cache permissions) | Permissive defaults or hardcoded paths | Check cache directory permissions (0o700 or 0o755), avoid absolute paths |
| Kernel File Generation | Build artifact placed insecurely | Place in `build/` or temp dir with restricted permissions |
| Configuration Ambiguity | Unclear intent or scope | Add config docstring explaining launcher selection, HCU-specific settings |
| Code Duplication in samplers/assigners | Repeated optimization logic across models | Extract to `optimizations/common/mmdet3d/` for reuse |

---

## References

- [CONTRIBUTING.md](../../../CONTRIBUTING.md)
- [Architecture Design](../../../docs/zh/design/architecture.md)
- [License Requirements](../../../THIRD_PARTY_NOTICES.md)
