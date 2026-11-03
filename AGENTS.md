# TurboPhysAI Agent Skills

## 1. 定位

本文件定义 Agent Skills 体系、工作流规则和质量标准。

---

## 2. Skill 开发工作流

- **代码改动**：自动路由到 code-quality-check、unit-test-development、code-review
- **CI 故障**：ci-failure-diagnosis  
- **部署 / 发布**：release-compliance-check
- **环境问题**：training-environment-validation
- **性能分析**：performance-analysis-and-validation

---

## 3. Skill 文件结构

每个 Skill 必须包含：

- **SKILL.md**：用户触发入口（When to use、Inputs、Outputs、Execution steps）
- **GUIDE.md**：专业知识与决策指南
- **evals/**：测试用例

详见 [SKILL_STRUCTURE_SPECIFICATION.md](.agents/SKILL_STRUCTURE_SPECIFICATION.md)

---

## 4. 校验与 CI

本地校验：
```bash
python3 scripts/agent/validate_skills.py --root .agents/skills
python3 scripts/check_docs.py
python3 scripts/agent/check_commit_compliance.py
```

---

---

## 5. Skills 开发进度追踪表

| Skill | Priority | Progress | Status | Reference Source | Reuse Strategy |
|-------|----------|----------|--------|------------------|----|
| **code-quality-check** | ⭐⭐⭐ | **✅ Complete** | ✅ 100% | Project config + hygonpilot/clean-code-style | Reference preflight mode |
| **release-compliance-check** | ⭐⭐ | **✅ Complete** | ✅ 100% | `scripts/check_commit_compliance.py` + `scripts/check_docs.py` | Direct enforcement |
| **training-environment-validation** | ⭐⭐ | **✅ Complete** | ✅ 100% | hygonpilot-skills-main/env-probe/GUIDE.md | Direct reuse for HCU/DTK environment probing |
| **unit-test-development** | ⭐⭐⭐ | **✅ Complete** | ✅ 100% | Project `test/` directory + pytest configuration | Write standard pytest with @pytest.mark.hcu |
| **performance-analysis-and-validation** | ⭐⭐ | **✅ Complete** | ✅ 100% | hygonpilot-skills-main/dtk-profiler-analysis/GUIDE.md | Direct reuse of DTK Profiler diagnostic steps |
| **code-review** | ⭐⭐⭐ | **✅ Complete** | ✅ 100% | Actual TurboPhysAI PR feedback analysis (#28, #29, #19, #33, #32) | Decision tree & checklist based on real code review findings |
| **ci-failure-diagnosis** | ⭐⭐⭐ | **⏳ Pending** | ⚠️ 50% | hygonpilot-skills-main/dtk-crash-debug/ | Reference troubleshooting methodology |
| **model-integration** | ⭐⭐⭐ | **⏳ Pending** | ⚠️ 40% | DrivingSDK-master/ + MindIE-SD/ | Multi-model integration pattern |
| **model-correctness-validation** | ⭐⭐⭐ | **⏳ Pending** | ⚠️ 20% | MindIE-SD/accuracy-gate/SKILL.md | Reference L1/L2/L3 layered acceptance standards |
| **cookbook-reproduction-documentation** | ⭐ | **⏳ Pending** | ⚠️ 30% | Project existing cookbook examples | Reference existing structure and documentation pattern |
| **package-and-container-delivery** | ⭐⭐ | **⏳ Pending** | ⚠️ 30% | Project setup.py + docker/ci/Dockerfile | Coordinate with release workflow |
| **ci-monitor-and-notify** | ⭐⭐ | **⏳ Pending** | ⚠️ 10% | GitHub Actions + workflow monitoring | Reference hygonpilot CI monitoring strategy |
| **optimization-tuning-advisor** | ⭐⭐⭐ | **⏳ Pending** | ⚠️ 5% | TurboPhysAI optimization configs | Multi-dimension optimization routing |

---

## 参考

- [Skill 结构规范](.agents/SKILL_STRUCTURE_SPECIFICATION.md)
- [Skill 模板](.agents/TEMPLATE.md)
