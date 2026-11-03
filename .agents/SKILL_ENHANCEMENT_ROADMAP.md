# TurboPhysAI MVP Skills 增强计划

基于 [SKILL_STRUCTURE_SPECIFICATION.md](.agents/SKILL_STRUCTURE_SPECIFICATION.md)，下表说明每个 MVP Skill 的当前状态与建议增强。

## Phase 1：MVP 5 个 Skills（基础研发闭环）

| Skill | 当前状态 | 推荐增强 | 优先级 | 理由 |
|-------|---------|---------|--------|------|
| **code-quality-check** | 4 个必需章节 ✅ | 无增强 | - | 功能简单，无分支流程 |
| **code-review** | 4 个必需章节 ✅ | 无增强 | - | 决策性 Skill，无步骤流程 |
| **unit-test-development** | 4 个必需章节 ✅ | `## Troubleshooting` | 低 | 可选：常见测试框架问题 |
| **ci-failure-diagnosis** | 4 个必需章节 ✅ | `## Troubleshooting` + `## Decision tree` | **高** | 诊断 Skill 必须包含决策树（错误类型） |
| **training-environment-validation** | 4 个必需章节 ✅ | `## Execution steps` + `## Troubleshooting` + `## Known limitations` | **高** | 多步骤，常见依赖冲突 |

---

## Phase 2：模型与优化（模型接入与性能）

| Skill | 当前状态 | 推荐增强 | 优先级 | 理由 |
|-------|---------|---------|--------|------|
| **model-integration** | 4 个必需章节 ✅ | `## Execution steps` + `## Decision tree` + `## Related skills` | **高** | 核心工作流，复杂路径 |
| **custom-operator-integration** | 4 个必需章节 ✅ | `## Execution steps` + `## References` + `## Known limitations` | **高** | 多步骤，需引用算子开发指南 |
| **optimization-group-development** | 4 个必需章节 ✅ | `## Execution steps` + `## Decision tree` | 中 | 优化配置有多条路径 |
| **model-correctness-validation** | 4 个必需章节 ✅ | `## Execution steps` + `## References` + `## Known limitations` | **高** | 关键把关，需数值稳定性指南 |
| **performance-analysis-and-validation** | 4 个必需章节 ✅ | `## Execution steps` + `## Decision tree` + `## References` + `## Troubleshooting` | **高** | 多路径，需 profiler 指南 |

---

## Phase 3：交付与发布

| Skill | 当前状态 | 推荐增强 | 优先级 | 理由 |
|-------|---------|---------|--------|------|
| **package-and-container-delivery** | 4 个必需章节 ✅ | `## Execution steps` + `## Known limitations` | 中 | 构建步骤明确 |
| **cookbook-reproduction-documentation** | 4 个必需章节 ✅ | `## Execution steps` + `## Troubleshooting` | 中 | 文档编写有步骤 |
| **release-compliance-check** | 4 个必需章节 ✅ | `## Execution steps` + `## Troubleshooting` | 低 | 检查清单式 Skill |

---

## 增强优先级建议

### 🔴 **立即执行**（关键路径）

1. **ci-failure-diagnosis**
   - 添加 `## Decision tree`：按错误类型分类（编译、测试、硬件、网络）
   - 添加 `## Troubleshooting`：常见 CI 错误速查表

2. **training-environment-validation**
   - 添加 `## Execution steps`：3-4 个具体步骤
   - 添加 `## Troubleshooting`：依赖冲突、版本不匹配等
   - 添加 `## Known limitations`：不支持的环境或配置

3. **model-correctness-validation**
   - 添加 `## Execution steps`：准备 → 运行 → 分析 → 决策
   - 添加 `## References`：链接数值稳定性、精度容差指南
   - 添加 `## Known limitations`：受限的评估指标范围

### 🟡 **次优先**（工作流完整性）

4. **model-integration**
   - 添加 `## Execution steps`：从源代码到启动的流程
   - 添加 `## Decision tree`：不同模型源的路径
   - 添加 `## Related skills`：前置与后续 Skills

5. **performance-analysis-and-validation**
   - 添加 `## Execution steps`：baseline → profiling → 对比 → 决策
   - 添加 `## Decision tree`：不同瓶颈的分析路径
   - 添加 `## References`：profiler 使用指南
   - 添加 `## Troubleshooting`：测量波动、缓存影响等

### 🟢 **可选增强**（便利性）

6. **custom-operator-integration**
   - 添加 `## Execution steps` + `## References`

7. **unit-test-development**
   - 添加 `## Troubleshooting`（可选）

---

## 实施步骤

### 第 1 周：关键路径（3 个 Skills）

```bash
# 1. 增强 ci-failure-diagnosis
# 2. 增强 training-environment-validation  
# 3. 增强 model-correctness-validation
# 运行验证
python3 scripts/agent/validate_skills.py --root .agents/skills
```

### 第 2 周：工作流完整性（2 个 Skills）

```bash
# 4. 增强 model-integration
# 5. 增强 performance-analysis-and-validation
```

### 第 3 周及之后：便利性增强

```bash
# 6. 增强其他 Skills
# 定期更新参考材料和故障排查指南
```

---

## 编写检查清单（增强章节时）

### `## Execution steps`
- [ ] 每个步骤以动词开头（Check, Run, Verify, Analyze）
- [ ] 包含实际命令或代码示例
- [ ] 说明预期结果或验证方式
- [ ] 提示早期终止条件（如"若失败则停止"）

### `## Decision tree`
- [ ] 清晰列出决策条件
- [ ] 每个分支指向具体操作
- [ ] 说明选择标准（优先级、风险等）

### `## References`
- [ ] 每个链接都在本仓或 github.com 中存在
- [ ] 包含一句话说明为何需要此引用
- [ ] 不超过 5 个链接（精选）

### `## Troubleshooting`
- [ ] 列出 3-5 个最常见的失败情况
- [ ] 包含原因、检查方式和修复办法
- [ ] 提供具体的命令或日志查看方式

### `## Known limitations`
- [ ] 明确说明不支持的场景
- [ ] 包含 workaround（如果有）
- [ ] 指出跟踪 issue 或计划修复

---

## 示例：增强 ci-failure-diagnosis

**当前**（4 个必需章节）→ **增强后**（+Decision tree +Troubleshooting）

```markdown
## When to use
- When GitHub Actions CI or HCU pipeline jobs fail.
- When encountering environment-specific test failures or compilation errors.

## When not to use
- For routine local code formatting checks before submission.

## Inputs expected
- CI log snippets, workflow error messages, and commit context.

## Outputs required
- Root cause evidence, local reproduction steps, and verified patch or fix instructions.

## Decision tree

**[Compilation Errors]**
→ Check Python/C++ syntax, DTK headers, build flags
→ See references/compilation-error-guide.md

**[Test Failures]**
→ Check test isolation, environment variables, dependency versions
→ Reproduce locally, capture logs

**[Hardware/Runtime Errors]**
→ Check GPU allocation, memory limits, kernel issues
→ Use dtk-crash-debug Skill if applicable

**[Timeout/Hanging]**
→ Check resource contention, deadlock indicators
→ Use performance-analysis-and-validation if needed

## Troubleshooting

### "ModuleNotFoundError: No module named 'torch'"
- **Cause**: DTK not installed or PATH misconfigured
- **Check**: `python -c "import torch; print(torch.__version__)"`
- **Fix**: Run `training-environment-validation` Skill

### "CUDA out of memory"
- **Cause**: GPU memory exhausted or not released
- **Check**: `hy-smi` shows GPU memory usage
- **Fix**: Reduce batch size, enable gradient checkpointing

### "Test timeout after 1800s"
- **Cause**: Infinite loop, resource contention, or slow hardware
- **Check**: Look for spinning processes in CI logs
- **Fix**: Add timeout guards to test code, check HCU allocation

## References

- [CI Quality Gate Workflows](.github/workflows/quality-gate.yml)
- [Compilation Troubleshooting](docs/compilation-guide.md)
- [DTK Crash Debug Skill](../dtk-crash-debug-pilot/GUIDE.md)
```

---

## 文档维护

每次 Skill 更新时，保持此表最新：

- [ ] 新增可选章节时，更新上表的"推荐增强"
- [ ] Skill 功能变化时，重新评估优先级
- [ ] 每月回顾是否需要调整增强计划
