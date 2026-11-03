# TurboPhysAI Skill 结构规范

## 1. 核心原则

- **轻量优先**：Skill 入口（SKILL.md）应清晰、易读、用户友好
- **渐进增强**：从必需内容开始，根据复杂度逐步添加可选章节
- **关注读者**：普通用户看 SKILL.md 的前 4 个章节就能判断是否适用
- **知识分层**：专业细节通过 GUIDE.md 或 references/ 按需加载

---

## 2. SKILL.md 章节分类

### 2.1 必需章节（Must Have）

每个 SKILL.md **必须**包含以下 4 个章节，由 `validate_skills.py` 自动检查：

| 章节 | 目的 | 最小内容 |
|------|------|---------|
| `## When to use` | 明确适用场景 | ≥1 个具体用例 |
| `## When not to use` | 明确边界，避免误用 | ≥1 个反面例子或与其他 Skill 的边界 |
| `## Inputs expected` | 说明需要什么 | 列出必需的输入类型和格式 |
| `## Outputs required` | 说明交付什么 | 列出预期的产物和形式 |

---

### 2.2 可选章节（Nice to Have）

根据 Skill 复杂度，**可选择性地添加**以下 7 类章节。这些章节如果不添加也不会被验证工具检查。

| 章节 | 目的 | 最小内容 | 何时添加 |
|------|------|---------|---------|
| `## Execution steps` | 说明具体执行流程 | ≥2 个步骤，每步含描述 + 命令 | Skill 有 2+ 个独立步骤 |
| `## References` | 指向相关文档与背景知识 | ≥1 个有效的链接 | Skill 依赖专业知识 |
| `## Decision tree` | 说明多条执行路径的选择 | ≥2 个不同条件分支 | Skill 有多条执行路径 |
| `## Known limitations` | 明确不支持的场景与限制 | ≥2 个限制项 + workaround | Skill 有明确功能限制 |
| `## Troubleshooting` | 常见错误诊断与修复 | ≥2 个错误 = 原因 + 检查 + 修复 | Skill 有常见失败情况 |
| `## Prerequisites` | 前置条件或依赖 | ≥2 个必需项（版本/硬件/权限） | Skill 需要特定环境 |
| `## Related skills` | 相关联的其他 Skills | ≥2 个相关 Skill + 关系说明 | Skill 与其他 Skills 关联 |

---

## 3. 章节选择决策树

**用途**：帮助开发者快速判断当前 Skill 需要哪些可选章节。从上到下逐项检查，若条件满足则添加该章节。

```
┌─ Is this a multi-step workflow?
│  ├─ YES → Add "Execution steps"
│  └─ NO → Check next condition
│
├─ Does this Skill have deep dependencies or background?
│  ├─ YES → Add "References" (point to GUIDE.md)
│  └─ NO → Check next condition
│
├─ Are there multiple execution paths?
│  ├─ YES → Add "Decision tree" or "Workflow routing"
│  └─ NO → Check next condition
│
├─ Are there known failures or edge cases?
│  ├─ YES → Add "Troubleshooting" and/or "Known limitations"
│  └─ NO → Keep minimal structure (4 mandatory only)
│
└─ Result: 4 mandatory + selected optional chapters
```

**使用示例**：
- `code-quality-check`：全 NO → 只需 4 个必需章节 ✅
- `training-environment-validation`：YES(多步) + YES(失败) → + Execution steps + Troubleshooting + Known limitations ✅
- `model-integration`：YES(多步) + YES(多路径) → + Execution steps + Decision tree ✅

---

## 4. Skill 类别与推荐结构

| 类别 | Skill 示例 | 推荐章节 | 原因 |
|------|----------|---------|------|
| **基础检查** | code-quality-check, code-review, unit-test-development | 4 必需 | 流程简单，工具调用 |
| **环境验证** | training-environment-validation, model-correctness-validation, package-and-container-delivery | 4 必需 + Execution steps + References + Known limitations | 多步工作流，背景知识，环境限制 |
| **性能优化** | performance-analysis-and-validation, optimization-group-development | 4 必需 + Execution steps + References + Decision tree + Known limitations | 多条路径，专业背景，常见陷阱 |
| **集成交付** | model-integration, custom-operator-integration, cookbook-reproduction-documentation, release-compliance-check | 4 必需 + Execution steps + References + Known limitations + Troubleshooting | 多阶段流程，高风险操作，常见错误 |

---

## 5. 编写规范（快速查表）

### When to use / When not to use

| 要求 | ❌ 避免 | ✅ 推荐 |
|------|--------|--------|
| 具体场景 | "When you need to check code" | "Before submitting to main branch" |
| 避免笼统 | "When you have a model" | "After training a PyTorch model on DTK" |
| 一行一例 | "Check code and format" | 分为两行：格式检查、语法检查 |

### Inputs expected / Outputs required

| 要求 | ❌ 避免 | ✅ 推荐 |
|------|--------|--------|
| 说明格式 | "Model files" | "PyTorch checkpoint (.pt) or ONNX (.onnx)" |
| 完整细节 | "Data" | "Validation dataset in CSV format with columns: image_path, label" |
| 标记可选 | "Config (optional)" | "(Optional) Custom config file; defaults to config.yaml" |

### Execution steps

| 要求 | ❌ 避免 | ✅ 推荐 |
|------|--------|--------|
| 动词开头 | "Environment setup" | "**Check DTK installation**" |
| 包含命令 | "Run validation" | "Run `python -m pytest test/ --cov`" |
| 期望输出 | "Should work" | "Expected: 0 errors, coverage ≥ 85%" |

### References

| 要求 | ❌ 避免 | ✅ 推荐 |
|------|--------|--------|
| 精选链接 | 10+ 个链接 | 2-3 个最相关的链接 |
| 说明用途 | `[Link](url)` | `[Link](url) — explains X, needed for Y` |
| 验证有效 | 断链接 | validate_skills.py 检查通过 |

### Decision tree / Troubleshooting

| 要求 | ❌ 避免 | ✅ 推荐 |
|------|--------|--------|
| 条件清晰 | "Sometimes A, sometimes B" | "**If GPU memory < 8GB:** use gradient checkpointing" |
| 对应操作 | "Try different things" | "→ Run with `--enable-gradient-checkpoint`" |
| 完整诊断 | "Error happened" | "Error: OOM \| Cause: batch size too large \| Fix: reduce to 32" |

---

## 6. 参考仓库实践

### MindIE-SD `accuracy-gate` Skill

**文件**：[github.com/Ascend/MindIE-SD/.agents/skills/accuracy-gate/SKILL.md](https://github.com/Ascend/MindIE-SD/blob/main/.agents/skills/accuracy-gate/SKILL.md)

- **特点**：复杂的多层决策与验收标准
- **启示**：
  - 复杂 Skill 可使用"分步骤定义"而非代码块
  - 要明确与相邻 Skill 的职责分工
  - 验收标准需分层：L1(逐位) → L2(数值门) → L3(质量门)

---

### DrivingSDK `vla-model-adaptation-optimization` Skill

**文件**：[github.com/Ascend/DrivingSDK/.agent/skills/vla-model-adaptation-optimization/SKILL.md](https://github.com/Ascend/DrivingSDK/blob/master/.agent/skills/vla-model-adaptation-optimization/SKILL.md)

- **特点**：长流程、多阶段、有执行约束
- **启示**：
  - 长任务 Skill 应包含"上下文管理"部分（lazy loading、检查点压缩）
  - 要列出关键约束（"禁止做什么"）
  - 分阶段检查点比通篇流程更清晰

---

### hygonpilot `env-probe` Skill

**文件**：[github.com/HYGON-AI/hygonpilot-skills/env-probe/SKILL.md](https://github.com/HYGON-AI/hygonpilot-skills/blob/main/env-probe/SKILL.md) + [GUIDE.md](https://github.com/HYGON-AI/hygonpilot-skills/blob/main/env-probe/GUIDE.md)

- **特点**：简洁的 SKILL.md + 详细的 GUIDE.md
- **启示**：
  - SKILL.md 可以很短（2-3 句话）
  - 专业知识放在 GUIDE.md 避免肥大化
  - 包含具体的命令示例与参数说明

---

### KsanaDiT Skills

**文件**：[github.com/Tencent/KsanaDiT/.skills/](https://github.com/Tencent/KsanaDiT/tree/main/.skills)

- **特点**：职责分离、架构知识分层
- **启示**：
  - 轻量级 SKILL.md 入口
  - `references/` 存放扩展知识
  - 与 Agent 路由紧密协作

---

## 7. TurboPhysAI 适配

### 参考仓对标

| 参考仓 | 复杂特性 | 采用 | 用于 |
|-------|---------|------|------|
| MindIE-SD | 多层验收标准 | ✅ | `model-correctness-validation` |
| DrivingSDK | 长流程 + 检查点 | ✅ | `model-integration`、`performance-analysis-and-validation` |
| hygonpilot | SKILL.md 精简 | ✅ | 所有 Skills |
| KsanaDiT | 架构分层 | ✅ | Skill 设计模式 |

### 避免过度设计

- ❌ 不用"兼容性"字段（MindIE-SD 特有，与硬件平台耦合）
- ❌ 不强制所有 Skill 都有"上下文管理"（只用于复杂 Skills）
- ✅ 优先用"References" + "GUIDE.md"分层

---

## 6. 参考仓库实践

### MindIE-SD `accuracy-gate` Skill
- **特点**：复杂的多层决策与验收标准
- **启示**：复杂 Skill 可使用"分步骤定义"而非代码块；要明确与相邻 Skill 的职责分工

### DrivingSDK `vla-model-adaptation-optimization` Skill
- **特点**：长流程、多阶段、有执行约束
- **启示**：长任务应包含"上下文管理"；要列出关键约束；分阶段检查点比通篇流程清晰

### hygonpilot `env-probe` 设计
- **特点**：简洁的 SKILL.md + 详细的 GUIDE.md
- **启示**：SKILL.md 可以很短；专业知识放在 GUIDE.md 避免肥大化；包含具体的命令示例

---

## 常见问题

**Q: 可选章节会被 validate_skills.py 检查吗？**
A: 不会。检查工具只验证 4 个必需章节。可选章节的质量由代码审查把关。

**Q: 是否每个 Skill 都应该有 `Troubleshooting`？**
A: 不。只有当 Skill 有常见失败场景、用户可能遇到特定错误时才添加。

**Q: 我能自定义章节名称吗？**
A: 4 个必需章节的名称固定（validate_skills.py 检查）。可选章节使用建议名称以保持一致性。
