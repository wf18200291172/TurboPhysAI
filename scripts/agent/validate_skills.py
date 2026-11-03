#!/usr/bin/env python3
"""Validate entrypoints, internal guides, local references and scripts without platform dependencies."""
from __future__ import annotations

import argparse
import ast
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

MOJIBAKE = re.compile(r"\u922e|\u9225|\u922b|\u922d|\u9239|\u923b|\u9264|\ufffd|[\ue000-\uf8ff]")
TEXT_SUFFIXES = {".md", ".py", ".ps1", ".yaml", ".yml", ".json", ".sh"}


def validate(root: Path, include_readme: bool = True) -> list[str]:
    issues = []
    entrypoints = list(root.glob("*/SKILL.md"))
    if not entrypoints:
        issues.append("No skill entrypoints found")
    for path in sorted(root.rglob("*")):
        if not path.is_file() or any(part in {".git", "__pycache__", ".venv"} for part in path.relative_to(root).parts):
            continue
        if path.suffix not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            issues.append(f"{path.relative_to(root)}: unreadable UTF-8: {exc}")
            continue
        label = str(path.relative_to(root))
        for line_no, line in enumerate(text.splitlines(), 1):
            if MOJIBAKE.search(line):
                issues.append(f"{label}:{line_no}: suspected corrupted text")
        if path.suffix == ".py":
            try:
                ast.parse(text.lstrip("\ufeff"), filename=label)
            except SyntaxError as exc:
                issues.append(f"{label}:{exc.lineno}: Python syntax: {exc.msg}")
        if path.name == "SKILL.md":
            fm = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
            if not fm:
                issues.append(f"{label}: missing YAML frontmatter")
            else:
                try:
                    import yaml
                except ImportError:
                    data = {key: bool(re.search(rf"(?m)^{key}:\s*\S", fm[1])) for key in ("name", "description")}
                else:
                    try:
                        data = yaml.safe_load(fm[1])
                    except yaml.YAMLError as exc:
                        issues.append(f"{label}: invalid YAML: {exc}")
                        data = {}
                if not isinstance(data, dict) or not all(data.get(key) for key in ("name", "description")):
                    issues.append(f"{label}: name and description required")
            for heading in ("When to use", "When not to use", "Inputs expected", "Outputs required"):
                if not re.search(rf"(?m)^## {re.escape(heading)}\s*$", text):
                    issues.append(f"{label}: missing section {heading}")
        if path.suffix != ".md" or (path.name == "README.md" and not include_readme):
            continue
        # Example code may contain sample links. Validate actual prose links, including references.
        prose = re.sub(r"(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1\s*$", "", text)
        for match in re.finditer(r"\[[^\]]+\]\((<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)", prose):
            target = match[1].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith("#"):
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.exists():
                issues.append(f"{label}: broken local link: {target}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--include-readme-check", action="store_true", help="Compatibility flag; README is checked by default")
    args = parser.parse_args()
    issues = validate(args.root.resolve())
    for issue in issues:
        print(issue)
    print(f"Validation: {len(issues)} error(s)")
    return int(bool(issues))


if __name__ == "__main__":
    raise SystemExit(main())
