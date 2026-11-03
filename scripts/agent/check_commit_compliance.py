#!/usr/bin/env python3
"""Check git commit author identity and commit messages for open-source compliance (no sugon/rogon/dcu)."""
from __future__ import annotations

import subprocess
import sys
import re

FORBIDDEN_TERMS = re.compile(r"\b(sugon|rogon|dcu)\b", re.IGNORECASE)
FORBIDDEN_EMAIL_DOMAINS = ("sugon.com", "rogon.cn")

def run_git(args: list[str]) -> str:
    try:
        res = subprocess.run(["git"] + args, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except subprocess.CalledProcessError as exc:
        return ""

def check_identity() -> list[str]:
    issues = []
    name = run_git(["config", "user.name"])
    email = run_git(["config", "user.email"])

    if FORBIDDEN_TERMS.search(name):
        issues.append(f"Git user.name '{name}' contains forbidden term (sugon/rogon)")

    if FORBIDDEN_TERMS.search(email):
        issues.append(f"Git user.email '{email}' contains forbidden term (sugon/rogon)")

    for domain in FORBIDDEN_EMAIL_DOMAINS:
        if email.lower().endswith(domain):
            issues.append(f"Git user.email domain '{domain}' is forbidden for open-source publication")

    return issues

def check_recent_commits() -> list[str]:
    issues = []
    log_output = run_git(["log", "-n", "10", "--pretty=format:%H|%an|%ae|%s"])
    if not log_output:
        return issues

    for line in log_output.splitlines():
        parts = line.split("|", 3)
        if len(parts) == 4:
            commit_hash, author_name, author_email, subject = parts
            if FORBIDDEN_TERMS.search(author_name):
                issues.append(f"Commit {commit_hash[:7]} author name '{author_name}' contains forbidden term")
            if FORBIDDEN_TERMS.search(author_email):
                issues.append(f"Commit {commit_hash[:7]} author email '{author_email}' contains forbidden term")
            for domain in FORBIDDEN_EMAIL_DOMAINS:
                if author_email.lower().endswith(domain):
                    issues.append(f"Commit {commit_hash[:7]} author email domain '{domain}' is forbidden")
            if FORBIDDEN_TERMS.search(subject):
                issues.append(f"Commit {commit_hash[:7]} message subject '{subject}' contains forbidden term (sugon/rogon/dcu). Use hygon/hcu instead.")

    return issues

def main() -> int:
    issues = []
    issues.extend(check_identity())
    issues.extend(check_recent_commits())

    if issues:
        print("❌ Open-Source Compliance Check FAILED:")
        for issue in issues:
            print(f"  - {issue}")
        print("\nCompliance Rules:")
        print("1. Author/Committer name & email must NOT contain 'sugon' or 'rogon' (or @sugon.com / @rogon.cn).")
        print("2. Allowed emails: @hygon.cn or personal emails (Gmail, QQ, 163, etc.).")
        print("3. Commit messages must NOT contain 'sugon', 'rogon', 'dcu'. Use 'hygon', 'hcu' instead.")
        return 1
    else:
        print("✅ Open-Source Compliance Check PASSED.")
        return 0

if __name__ == "__main__":
    sys.exit(main())
