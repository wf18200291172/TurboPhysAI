# Skill Development Template

Use this as a starting point when creating a new skill.

## Directory structure

```
.agents/skills/<skill-id>/
├── SKILL.md              # Entry point (required, checked by validator)
├── GUIDE.md              # Internal decision guide (optional)
├── references/           # Support materials
│   ├── <reference-1>.md
│   └── <reference-2>.py
└── scripts/              # Skill-specific scripts (optional)
    └── <helper-script>.py
```

## SKILL.md Template

```markdown
---
name: <skill-id>
description: >
  <One-sentence description of what this skill accomplishes.
  Can span multiple lines with continuation.
  Keep it clear and user-friendly.>
---

## When to use

- <Use case 1>
- <Use case 2>

## When not to use

- <Boundary case 1 — use Skill X instead>
- <Boundary case 2>

## Inputs expected

- <Input type 1>: description and format
- <Input type 2>: description and format

## Outputs required

- <Output type 1>: what exactly is delivered
- <Output type 2>: what exactly is delivered

## Execution steps

Optional; include if the skill has multiple concrete steps.

1. **Step 1 title**
   Description and/or command
   
   ```bash
   # example command
   python script.py --arg value
   ```

2. **Step 2 title**
   ...

## References

Optional; link to related documents or guides.

- [Reference Title](../related-skill/GUIDE.md)
- [Documentation](../../docs/path/to/doc.md)
```

## GUIDE.md Template (optional)

Create `GUIDE.md` when the skill involves complex decisions or specialized knowledge.

```markdown
# <Skill Name> Implementation Guide

## Overview

Brief explanation of what decisions this guide covers.

## When to read this guide

When executing the parent `SKILL.md` and encountering:
- Complex branching logic
- Multiple valid implementation paths
- Technical background knowledge not in the skill entry

## Key concepts

### Concept 1

Explanation and rationale.

### Concept 2

Explanation with examples.

## Decision tree

When you encounter X, follow this process:
1. Check condition A
2. If true, do Y
3. If false, do Z

## References

Link to external docs or related skills.
```

## Naming conventions

- **Skill ID** (directory and `name` field): lowercase, hyphens, descriptive
  - ✅ `code-quality-check`
  - ✅ `model-correctness-validation`
  - ✅ `dtk-crash-debug`
  - ❌ `CodeQualityCheck`, `code_quality_check`, `cq-check`

- **Heading names**: Match exactly (case-sensitive)
  - ✅ `## When to use`
  - ❌ `## When To Use`, `## WHEN TO USE`

- **File paths**: Lowercase with hyphens
  - ✅ `optimization-contract.md`
  - ❌ `Optimization_Contract.md`

## Checklist before commit

- [ ] Skill ID is lowercase with hyphens
- [ ] `name` and `description` are non-empty
- [ ] All 4 required headings present: "When to use", "When not to use", "Inputs expected", "Outputs required"
- [ ] Files are UTF-8 encoded
- [ ] Python files have valid syntax
- [ ] Local links are valid (reference existing files)
- [ ] `validate_skills.py --root .agents/skills` returns 0 errors
- [ ] Related GUIDE.md or references are created (if needed)
- [ ] Description clearly differentiates from neighboring skills

## Validation

Before pushing, run:

```bash
python3 scripts/agent/validate_skills.py --root .agents/skills
```

If no errors, you're ready to commit:

```bash
git add .agents/skills/<skill-id>/
git commit -m "feat(skills): add <skill-name> skill"
```
