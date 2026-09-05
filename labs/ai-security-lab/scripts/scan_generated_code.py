"""Lightweight defensive scanner for risky patterns in AI-generated source code.

This is intentionally simple: it is a portfolio lab helper, not a replacement for
Semgrep, Bandit, CodeQL, SAST, dependency scanning, or manual security review.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

PATTERNS: dict[str, re.Pattern[str]] = {
    "possible-hardcoded-secret": re.compile(
        r"(?i)(api[_-]?key|secret|password|token)\s*=\s*['\"][^'\"]{8,}['\"]"
    ),
    "python-eval": re.compile(r"\beval\s*\("),
    "python-exec": re.compile(r"\bexec\s*\("),
    "subprocess-shell-true": re.compile(r"subprocess\.[A-Za-z_]+\([^\n]*shell\s*=\s*True"),
    "os-system": re.compile(r"\bos\.system\s*\("),
    "tls-verification-disabled": re.compile(r"(?i)verify\s*=\s*False"),
    "pickle-load": re.compile(r"\bpickle\.loads?\s*\("),
}


def scan_text(text: str) -> list[tuple[int, str, str]]:
    findings: list[tuple[int, str, str]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for label, pattern in PATTERNS.items():
            if pattern.search(line):
                findings.append((line_number, label, line.strip()))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan source code for simple risky patterns.")
    parser.add_argument("path", type=Path, help="Source file to scan")
    args = parser.parse_args()

    if not args.path.is_file():
        parser.error(f"File not found: {args.path}")

    text = args.path.read_text(encoding="utf-8", errors="replace")
    findings = scan_text(text)

    if not findings:
        print("No configured risky patterns found.")
        return 0

    print(f"Found {len(findings)} potential issue(s):")
    for line_number, label, line in findings:
        print(f"L{line_number}: [{label}] {line}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
