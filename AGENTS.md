# TurboPhysAI Agent Skills

## 1. 定位

本文件定义 TurboPhysAI 的 Agent Skills 体系、开发工作流和质量验证框架。

- **AGENTS.md**（本文）：仓库级规则、工作流、资源定义与路由
- **SKILL.md**：具体技能的用户触发入口与执行步骤
- **GUIDE.md**：技能内部的专业知识、背景与决策指南
- **scripts/agent/validate_skills.py**：L0 结构校验工具

**原则**：
- Skill 入口（SKILL.md）应清晰、轻量、用户友好
- 专业细节与背景知识通过 GUIDE.md 或 references/ 按需加载
- 不在 SKILL.md 中重复仓库文档，而是引用

---

## 2. Skill 开发工作流

### 2.1 任务分类

| 任务类型 | 示例 | 对应 Skill |
|---------|------|-----------|
| 代码质量 | 规范检查、格式化、linter | `code-quality-check` |
| 代码审阅 | 行为风险、接口检查、并发问题 | `code-review` |
| 单元测试 | 新功能测试、回归测试 | `unit-test-development` |
| CI 排障 | 构建失败、测试异常诊断 | `ci-failure-diagnosis` |
| 环境验证 | DTK/PyTorch 兼容性、依赖冲突 | `training-environment-validation` |
| 模型接入 | 新模型架构集成、基线建立 | `model-integration` |
| 算子开发 | 自定义算子、绑定与导出 | `custom-operator-integration` |
| 优化组 | 算子替换规则、条件分发 | `optimization-group-development` |
| 正确性验证 | 精度检查、数值稳定性 | `model-correctness-validation` |
| 性能分析 | 瓶颈识别、基准对比 | `performance-analysis-and-validation` |
| 打包交付 | wheel 与镜像构建 | `package-and-container-delivery` |
| Cookbook 文档 | 复现指南、脱敏日志 | `cookbook-reproduction-documentation` |
| 发布检查 | 凭据审计、许可证合规 | `release-compliance-check` |

### 2.2 Skill 生命周期

1. **草稿阶段**：在 `.agents/skills/<skill-id>/` 中创建 SKILL.md
2. **结构校验**：运行 `python3 scripts/agent/validate_skills.py --root .agents/skills`
3. **内容完善**：补充 GUIDE.md 与 references/ 材料
4. **评测用例**：在 `evals/skills/<skill-id>/` 下准备测试用例
5. **发布**：通过 GitHub 推送，CI 自动校验

---

## 3. SKILL.md 编写规范

### 3.1 必需结构

每个 `SKILL.md` 必须包含以下部分（由 validate_skills.py 检查）：

```markdown
---
name: <skill-id>
description: <清晰的功能描述，一句话，支持换行>
---

## When to use
...

## When not to use
...

## Inputs expected
...

## Outputs required
...

[可选] ## Execution steps
...

[可选] ## References
...
```

### 3.2 各部分编写指南

#### **Frontmatter（必填）**

| 字段 | 要求 | 示例 |
|------|------|------|
| `name` | 小写字母、数字、连字符，完整描述功能 | `code-quality-check` |
| `description` | 一句话总结用途，支持多行缩进 | `Check whether code changes adhere to TurboPhysAI style guide...` |

#### **When to use（必填）**

阐述这个 Skill 的适用场景。使用场景应该是明确的、可识别的用户需求。

✅ **好的示例**：
```markdown
## When to use
- Before submitting code changes or pull requests.
- When CI quality gate fails on formatting, linter, or type checks.
```

❌ **避免**：
```markdown
## When to use
- 随时使用此技能
- 当您有代码时
```

#### **When not to use（必填）**

明确说明这个 Skill **不适用**的情况，与其他 Skill 进行边界区分。

✅ **好的示例**：
```markdown
## When not to use
- For deep logical code review or security auditing (use `code-review` instead).
- For runtime performance profiling on real hardware.
```

#### **Inputs expected（必填）**

列出执行此 Skill 需要的输入数据、文件、参数或上下文。

✅ **好的示例**：
```markdown
## Inputs expected
- Target file paths or git diff of current changes.
- Linter configuration from `setup.cfg` or `.pylintrc`.
```

#### **Outputs required（必填）**

明确说明执行成功后应该交付给用户的产物。

✅ **好的示例**：
```markdown
## Outputs required
- Lint/formatting check results, summary of fixes applied, and remaining unverified items.
```

#### **Execution steps（可选）**

如果 Skill 包含多个具体步骤，可补充此部分。通常包括：
- 数据准备
- 执行命令
- 结果验证
- 异常处理

```markdown
## Execution steps

1. **Validate environment**
   ```bash
   python scripts/check_env.py --out env_report.json
   ```

2. **Run quality checks**
   ```bash
   python -m pytest test/ --cov=turbo_physai --cov-report=term
   ```

3. **Interpret results**
   - If pass: proceed to next stage
   - If fail: apply `code-quality-check` or manual fixes
```

#### **References（可选）**

引用相关文档、决策指南或后台知识。

```markdown
## References

- [Linter Configuration](../../docs/style-guide.md)
- [Environment Probe Guide](../training-environment-validation/GUIDE.md)
- [Physics-Informed AI Numerical Stability](../../docs/numerical-stability.md)
```

---

### 3.3 代码示例：完整 SKILL.md

```markdown
---
name: model-correctness-validation
description: >
  Verify that model training and evaluation results satisfy required metrics
  and numerical stability tolerances after integration and optimization,
  including NaN/Inf checks for physics-informed AI workloads.
---

## When to use

- Validating accuracy and correctness after model integration or applying optimization groups.
- Checking training stability, loss convergence, and numerical tolerances.
- Detecting numerical instabilities (NaN/Inf) in physics-informed loss functions.

## When not to use

- For basic code linting or unit test execution.
- For raw operator implementation without correctness measurement.

## Inputs expected

- Baseline and optimized training/eval outputs, evaluation datasets.
- Metric tolerances (e.g., accuracy drop ≤ 0.5%, loss stability within 3σ).
- Hardware specs (Hygon DCU count, memory constraints).

## Outputs required

- Aligned evaluation metrics, comparison report, stability verification records.
- NaN/Inf detection logs and mitigation recommendations.
- Acceptance summary with signed-off baseline vs. optimized deltas.

## Execution steps

1. **Prepare evaluation environment**
   - Load baseline model weights and optimized checkpoint
   - Verify dataset integrity (checksums, sample counts)

2. **Run evaluation**
   ```bash
   python -m turbo_physai.eval \
     --baseline-ckpt baseline.pt \
     --optimized-ckpt optimized.pt \
     --dataset validation.tfrecord \
     --output eval_report.json
   ```

3. **Analyze numerical stability**
   - Check loss curves for NaN/Inf emergence
   - Quantify gradient clipping and precision loss
   - Flag any >5% accuracy regression

4. **Make accept/reject decision**
   - If metrics pass: mark as validated
   - If marginal: document known tradeoffs
   - If fail: initiate rollback workflow

## References

- [Physics-Informed AI Numerical Stability Guide](../../docs/numerical-stability.md)
- [Evaluation Metrics & Tolerances](references/evaluation-tolerances.md)
- [DTK Float Precision Characteristics](../training-environment-validation/GUIDE.md)
```

---

## 4. GUIDE.md 编写规范

GUIDE.md 是技能内部的**决策与背景知识文档**，供 Agent 在执行 Skill 时按需读取。

### 4.1 何时创建 GUIDE.md

- Skill 涉及复杂的决策树或多条执行路径
- Skill 依赖某个专业领域的背景知识（e.g., DTK profiler 命令参数）
- 需要记录**已知限制、替代方案、历史踩坑**

### 4.2 GUIDE.md 结构

```markdown
# <Skill 名称> - Implementation Guide

## 1. Context & Decisions

### Problem Statement
...

### Known Constraints
...

## 2. Execution Workflow

### When to apply each branch
...

### Common pitfalls
...

## 3. Reference Materials

- [External doc link]
- Local script: `scripts/...`

## 4. Troubleshooting

| Issue | Root Cause | Resolution |
|-------|-----------|-----------|
| ... | ... | ... |
```

### 4.3 示例：`training-environment-validation/GUIDE.md`

参考 hygonpilot-skills 中的 [env-probe/GUIDE.md](../hygonpilot-skills-main/env-probe/GUIDE.md)，包含：
- 如何检查 HCU 设备状态与内存
- DTK/PyTorch 版本对应关系
- 常见依赖冲突与解决方案

---

## 5. 校验与 CI 集成

### 5.1 本地校验

```bash
# 检查所有 Skills 结构
python3 scripts/agent/validate_skills.py --root .agents/skills

# 输出示例
code-quality-check/SKILL.md: name and description required
model-integration/SKILL.md: missing section When not to use
Validation: 2 error(s)
```

**validate_skills.py 检查清单**：

| 检查项 | 错误类型 | 修复方法 |
|--------|---------|---------|
| 无 SKILL.md 入口 | `No skill entrypoints found` | 在 `skill-id/` 下创建 SKILL.md |
| 编码错误 | `unreadable UTF-8` | 转换文件为 UTF-8 |
| YAML 格式错误 | `missing YAML frontmatter` | 添加 `---name:...\n---` |
| 缺失字段 | `name and description required` | 填充 YAML 字段 |
| 缺失必需 Heading | `missing section When to use` | 添加 4 个必需章节 |
| Python 语法错误 | `SyntaxError: ...` | 修复 Python 代码 |
| 文本乱码 | `suspected corrupted text` | 检查编码，重新保存 |
| 死链接 | `broken local link: ...` | 修复或删除无效链接 |

### 5.2 GitHub Actions CI 配置

在 `.github/workflows/quality-gate.yml` 中添加：

```yaml
- name: Validate Skill Structure
  run: python3 scripts/agent/validate_skills.py --root .agents/skills
```

---

## 6. 目录结构参考

```text
.agents/skills/
├── code-quality-check/
│   ├── SKILL.md                    # 用户入口
│   ├── GUIDE.md                    # 背景知识（可选）
│   ├── references/
│   │   ├── linter-config.md
│   │   └── formatting-rules.md
│   └── scripts/                    # 技能专用脚本（可选）
│       └── format_check.py
│
├── model-integration/
│   ├── SKILL.md
│   ├── GUIDE.md
│   ├── references/
│   │   ├── model-registry.md
│   │   └── baseline-template.py
│   └── scripts/
│       └── setup_baseline.sh
│
└── training-environment-validation/
    ├── SKILL.md
    ├── GUIDE.md
    ├── references/
    │   ├── dcu-requirements.txt
    │   └── pytorch-compatibility.md
    └── scripts/
        └── check_hcu_setup.py

evals/skills/
├── code-quality-check/
│   ├── manifest.json              # 评测包元数据
│   ├── cases.json                 # 用例定义
│   ├── fixtures/                  # 测试数据
│   └── grading/                   # 判据与参考答案
│
└── model-integration/
    ├── manifest.json
    └── ...
```

---

## 7. 文档维护清单

- [ ] 每个 Skill 有清晰的 `When to use` 与 `When not to use`
- [ ] YAML frontmatter 包含 `name` 和 `description`
- [ ] 四个必需 Heading 都已填充内容
- [ ] 所有本地链接都指向存在的文件
- [ ] GUIDE.md 包含背景知识与决策指南
- [ ] 校验工具通过：`python3 scripts/agent/validate_skills.py --root .agents/skills`
- [ ] PR 描述包含新增或修改的 Skill 清单

---

## 参考与规范

- [Skill 结构规范](.agents/SKILL_STRUCTURE_SPECIFICATION.md) — **必读**：定义必需/可选章节与编写标准
- [Skill 增强路线图](.agents/SKILL_ENHANCEMENT_ROADMAP.md) — 13 个 MVP Skills 的优化计划
- [Skill 开发模板](.agents/TEMPLATE.md) — 快速创建新 Skill 的起点
- [validate_skills.py 使用文档](scripts/agent/README.md) — L0 结构校验工具详解
- [TurboPhysAI Skill 质量验证规范](../TurboPhysAI%20Skill%20质量验证规范.md) — L0-L5 完整评测框架
- [MindIE-SD AGENTS.md](https://github.com/Ascend/MindIE-SD/blob/main/AGENTS.md) — 参考架构
- [hygonpilot-skills README](../hygonpilot-skills-main/README.md) — Hygon DTK 优化 Skills
