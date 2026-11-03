# TurboPhysAI Skills 结构验证工具

## 概述

`validate_skills.py` 是一个**自动化 L0（结构）验证工具**，用于检查 TurboPhysAI Skills 的目录结构、元数据完整性和文件格式。无需外部依赖或平台特定工具。

## 目的

Agent 加载 Skills 前，确保：
1. **入口存在**：每个 Skill 目录包含一个 `SKILL.md` 文件
2. **元数据完整**：`name` 和 `description` 字段存在且非空
3. **必需章节完整**：`SKILL.md` 包含所有必需的 Markdown 标题
4. **代码语法有效**：所有 `.py` 文件可正确解析（不需实际执行）
5. **文本编码正确**：所有文件为有效 UTF-8，无乱码
6. **本地链接有效**：所有本地文件引用 `[text](path)` 能正确解析

## 使用方法

### 命令行

```bash
# 检查默认目录（脚本目录下的 .agents/skills）
python3 scripts/agent/validate_skills.py

# 检查指定目录
python3 scripts/agent/validate_skills.py --root .agents/skills

# 兼容性标志（README 默认已检查）
python3 scripts/agent/validate_skills.py --include-readme-check
```

### 集成到 CI/CD

在 GitHub Actions 工作流中添加（`.github/workflows/quality-gate.yml`）：

```yaml
- name: Validate Skill Structure
  run: python3 scripts/agent/validate_skills.py --root .agents/skills
```

### 返回码

- `0`：无验证错误
- `1`：发现一个或多个验证错误

---

## 验证规则

### 1. 入口发现

**规则**：每个 `--root` 下包含 `SKILL.md` 的目录为一个有效入口。

**错误**：`No skill entrypoints found`
- **修复**：创建至少一个 `<skill-id>/SKILL.md` 文件

### 2. 编码与文本完整性

**规则**：所有文本文件（`.md`、`.py`、`.yaml`、`.yml`、`.json`、`.sh`）必须是有效的 UTF-8。

**错误**：
- `<file>: unreadable UTF-8: ...` → 文件不是有效 UTF-8
  - **修复**：用编辑器以 UTF-8 编码保存文件（设置 → 文件编码）
  
- `<file>:<line>: suspected corrupted text` → 行包含乱码字符（CJK 字符损坏）
  - **修复**：从版本控制恢复或手动重新输入该行

### 3. Python 语法验证

**规则**：所有 `.py` 文件必须能正确解析为 Python 代码（使用 `ast.parse()`）。

**错误**：`<file>:<line>: Python syntax: <message>`
- **修复**：修正 Python 语法错误（如缺少冒号、括号不匹配等）

### 4. SKILL.md Frontmatter 验证

**规则**：`SKILL.md` 必须以 `---` 开头的 YAML frontmatter 开始：

```yaml
---
name: <skill-id>
description: <description text>
---
```

**错误**：
- `<file>: missing YAML frontmatter` → 文件未以 `---` 开头
  - **修复**：在文件顶部添加 frontmatter 块

- `<file>: invalid YAML: ...` → YAML 语法错误
  - **修复**：检查 YAML 的缩进和引号

- `<file>: name and description required` → 缺少或为空的 `name` 或 `description`
  - **修复**：确保两个字段都存在且非空

### 5. SKILL.md 必需章节

**规则**：每个 `SKILL.md` 必须包含所有 4 个必需的 `##`（二级 Markdown 标题）：

```markdown
## When to use
## When not to use
## Inputs expected
## Outputs required
```

**错误**：`<file>: missing section <heading>`
- **修复**：用 `##` 添加缺失的章节

**注**：这些章节可以包含任何内容，只检查其存在性。

### 6. 本地链接有效性

**规则**：Markdown 文件中的链接必须指向存在的本地文件或有效的外部 URL。

**应用到**：
- 格式：`[text](path/to/file)` 或 `[text](URL)`
- 排除代码块（三个反引号）
- 跳过外部 URL（`http://`、`https://`）和锚点（`#section`）

**错误**：`<file>: broken local link: path/to/missing/file`
- **修复**：
  1. 更新链接指向现有文件
  2. 删除损坏的链接
  3. 创建缺失的文件

**示例**：
- ✅ `[Optimization Guide](../training-environment-validation/GUIDE.md)` → 检查文件是否存在
- ✅ `[Cloud](https://example.com)` → 跳过（外部 URL）
- ✅ `[Section](#when-to-use)` → 跳过（锚点）
- ❌ `[Missing](../nonexistent.md)` → 文件不存在时报错

---

## Skill 开发集成流程

### 推荐工作流

1. **创建 Skill 目录和 SKILL.md**
   ```bash
   mkdir -p .agents/skills/<skill-id>
   touch .agents/skills/<skill-id>/SKILL.md
   ```

2. **添加 YAML frontmatter 和必需章节**
   ```markdown
   ---
   name: <skill-id>
   description: <一句话描述>
   ---

   ## When to use
   ...

   ## When not to use
   ...

   ## Inputs expected
   ...

   ## Outputs required
   ...
   ```

3. **运行验证器**
   ```bash
   python3 scripts/agent/validate_skills.py --root .agents/skills
   ```

4. **迭代修复错误**
   - 添加缺失章节
   - 修复编码问题
   - 修正损坏的链接

5. **检查通过后提交**
   ```bash
   git add .agents/skills/<skill-id>/
   git commit -m "feat(skills): add <skill-name> skill"
   ```

---

## 验证器不检查的内容

- **语义正确性**：描述是否准确反映 Skill 的功能
- **执行成功**：Skill 运行时是否出错
- **Agent 路由**：用户是否能发现 Skill
- **内容质量**：写作风格、清晰度或说明完整性
- **链接目标**：被链接文件的内容（只检查文件存在性）

这些项目由 **L1–L5 评测** 覆盖（见 [质量验证规范](../../TurboPhysAI%20Skill%20质量验证规范.md)）。

---

## 故障排查

### 验证器运行缓慢

**原因**：扫描大型二进制目录（如 `.git`、`__pycache__`）

**修复**：验证器已排除这些目录。若仍缓慢，检查符号链接循环：
```bash
find .agents/skills -type l -exec ls -l {} \;
```

### Windows 上的 UTF-8 错误

**原因**：文件以系统默认编码保存（如中文 Windows 上的 GBK）

**修复**：
- VS Code：右下角 → 选择 "UTF-8"
- 命令行：`iconv -f GBK -t UTF-8 <文件> > <输出文件>`

### Frontmatter 解析失败

**原因**：缺少 `---` 或 YAML 格式错误

**修复**：
```markdown
---
name: skill-name
description: Description here
---
```

检查缩进（空格，不是制表符）。

### 本地链接报错

**原因**：引用的文件不存在或路径错误

**修复**：
```bash
# 验证文件确实存在
ls -la path/to/referenced/file.md

# 使用相对路径
# 错误：[Link](.../other-skill/GUIDE.md)
# 正确：[Link](../other-skill/GUIDE.md)
```
