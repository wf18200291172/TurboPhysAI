---
name: release-compliance-check
description: Inspect credentials, third-party sources, licenses, commit author identity, commit message compliance, and documentation hygiene before publishing in TurboPhysAI.
---

## When to use
- Pre-release auditing of codebases, container images, and deliverables.
- Checking for hardcoded credentials, third-party attribution notices, and license compliance.
- Verifying git commit author identity and commit message compliance before merging to protected branches.
- Auditing documentation for leaked internal IPs, personal paths, or broken links.

## When not to use
- For routine daily code development or formatting checks.

## Inputs expected
- Release candidate commit/tag, container images, dependency manifest, git commit history, and documentation files.

## Outputs required
- Compliance check report, source registration, release blocker items, and resolution status.

## Execution steps

1. **Run Open-Source Commit Compliance Check**
   ```bash
   python3 scripts/agent/check_commit_compliance.py
   ```
   *Checks that commit authors, committers, and recent commit messages do not contain forbidden terms (`sugon`, `rogon`, `dcu`), and use valid email domains (`@hygon.cn`, personal emails).*

2. **Run Documentation Hygiene & Link Check**
   ```bash
   python3 scripts/check_docs.py
   ```
   *Checks that markdown files have no broken links, no trailing whitespace, no leaked internal IPv4 addresses (`10.x`, `192.168.x`), and no personal/machine-local paths (`/Users/...`, `/home/...`).*

3. **Check Third-Party Licenses and Notices**
   - Verify `THIRD_PARTY_NOTICES.md`, `NOTICE`, and `third_party/licenses/` completeness.

4. **Scan for Hardcoded Credentials**
   - Inspect diffs for API keys, passwords, or internal tokens.
