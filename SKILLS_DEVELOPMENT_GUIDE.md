# TurboPhysAI Skills 开发指南

## 概述

本文档列出所有 13 个 Skills 所需的资料、文档、工具和测试环境。

**相关规范文档**：
- [.agents/SKILL_STRUCTURE_SPECIFICATION.md](.agents/SKILL_STRUCTURE_SPECIFICATION.md) - Skill 文件结构与规范
- [.agents/TEMPLATE.md](.agents/TEMPLATE.md) - Skill 模板
- [AGENTS.md](AGENTS.md) - 仓库级 Agent 规则

---

## 13 个 Skills 速查表

| Skill | Priority | Progress | Status | Reference Source | Reuse Strategy |
|-------|----------|----------|--------|------------------|----|
| **code-quality-check** | ⭐⭐⭐ | **✅ Complete** | ✅ 100% | Project config + hygonpilot/clean-code-style | Reference preflight mode directly |
| **release-compliance-check** | ⭐ | **✅ Complete** | ✅ 100% | scripts/agent/check_commit_compliance.py + scripts/check_docs.py | Automated compliance & documentation hygiene |
| **training-environment-validation** | ⭐⭐ | **✅ Complete** | ✅ 100% | hygonpilot-skills-main/env-probe/GUIDE.md | Direct reuse for HCU/DTK environment probing |
| **unit-test-development** | ⭐⭐ | **✅ Complete** | ✅ 100% | Project test/ + pytest.ini configuration | Write standard pytest with @pytest.mark.hcu |
| **performance-analysis-and-validation** | ⭐⭐ | **✅ Complete** | ✅ 100% | hygonpilot-skills-main/dtk-profiler-analysis/GUIDE.md | Direct reuse for DTK profiler workflow |
| **code-review** | ⭐⭐⭐ | **✅ Complete** | ✅ 100% | Actual TurboPhysAI PR feedback analysis (#28, #29, #19, #33, #32) | Decision tree & checklist based on real findings |
| **ci-failure-diagnosis** | ⭐⭐⭐ | **⏳ Pending** | ⚠️ 40% | hygonpilot-skills-main/dtk-crash-debug | Troubleshooting framework for HCU failures |
| **ci-monitor-and-notify** | ⭐⭐ | **⏳ Pending** | ⚠️ 30% | GitHub Actions monitoring patterns | Adapt CI status reporting |
| **model-integration** | ⭐⭐⭐ | **⏳ Pending** | ⚠️ 50% | DrivingSDK multi-model integration + MindIE-SD model-wrapper | Three-stage closure: migrate → optimize → deliver |
| **model-correctness-validation** | ⭐⭐⭐ | **⏳ Pending** | ⚠️ 40% | MindIE-SD accuracy-gate/SKILL.md | Reference L1/L2/L3 layered acceptance standards |
| **cookbook-reproduction-documentation** | ⭐ | **⏳ Pending** | ⚠️ 30% | Project docs/zh/cookbook examples | Adapt existing structure into Agent skill |
| **package-and-container-delivery** | ⭐⭐ | **⏳ Pending** | ⚠️ 20% | Project setup.py + docker/ci/Dockerfile | Build & verify wheel/container in clean environments |
| **model-optimization-and-tuning** | ⭐⭐⭐ | **⏳ Pending** | ⚠️ 10% | hygonpilot model optimization patterns + MindIE-SD optimization skills | Operator-level & end-to-end optimization |

---

## 核心参考仓说明

### 1. hygonpilot-skills-main（海光 DTK 工程化最佳实践）
- `env-probe/GUIDE.md` → 复用到 `training-environment-validation`
- `dtk-profiler-analysis/GUIDE.md` → 复用到 `performance-analysis-and-validation`
- `dtk-crash-debug/` → 参考实现 `ci-failure-diagnosis`
- 优化类 Skills 的方法论与决策树

### 2. MindIE-SD-dev（模型集成与验收）
- `accuracy-gate/SKILL.md` → 参考 `model-correctness-validation` 的分层验收标准
- `AGENTS.md` → 复用到本仓库的路由与资源定义规则
- 多算子优化与编译优化框架

### 3. DrivingSDK（多模型集成范例）
- 多上游模型集成方案参考
- 优化配置与训练流程设计参考

---


---

## HCU 适配指导

详见 [HCU_ADAPTATION_GUIDE.md](HCU_ADAPTATION_GUIDE.md) — 系统化的 6 个维度适配检查清单。

---

## 快速上手指南

新建 Skill 时：

1. 查看 `.agents/skills/` 找现成模板
2. 参考对应仓库的实现（hygonpilot / MindIE-SD / DrivingSDK）
3. 按上述 HCU 适配清单改造
4. 运行 `python3 scripts/agent/validate_skills.py --root .agents/skills` 验证
