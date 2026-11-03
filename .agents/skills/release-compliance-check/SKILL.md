---
name: release-compliance-check
description: Inspect credentials, third-party sources, licenses, and release version completeness before publishing in TurboPhysAI.
---

## When to use
- Pre-release auditing of codebases, container images, and deliverables.
- Checking for hardcoded credentials, third-party attribution notices, and license compliance.

## When not to use
- For routine daily code development or formatting checks.

## Inputs expected
- Release candidate commit/tag, container images, and dependency manifest.

## Outputs required
- Compliance check report, source registration, release blocker items, and resolution status.
