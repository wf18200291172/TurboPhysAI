---
name: training-environment-validation
description: Verify training environment setup, DTK/PyTorch compatibility, and dependency conflicts on Hygon HCU hardware.
---

## When to use
- Setting up a new training node or container environment.
- Investigating dependency conflicts or missing Hygon/DTK libraries.

## When not to use
- For running individual unit tests or lint checks.

## Inputs expected
- Target container image or environment specs, installed package lists, and hardware notes.

## Outputs required
- Environment checklist, installation verification logs, dependency conflict analysis, and environment recommendations.
