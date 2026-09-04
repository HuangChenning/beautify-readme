#!/usr/bin/env python3
"""Refresh CONTRIBUTORS stats blocks in README.md and README.zh-CN.md.

Uses git shortlog (commit counts) and git log --shortstat (insertions/deletions),
excluding merge commits. Replaces content between:
  <!-- CONTRIBUTORS:START -->
  <!-- CONTRIBUTORS:END -->
"""

from __future__ import annotations

import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
README_FILES = (REPO_ROOT / "README.md", REPO_ROOT / "README.zh-CN.md")
START = "<!-- CONTRIBUTORS:START -->"
END = "<!-- CONTRIBUTORS:END -->"
AUTHOR_RE = re.compile(r"^Author:\s+(.*)$")
FILES_RE = re.compile(r"^\s*(\d+)\s+files?\s+changed")
INS_RE = re.compile(r"(\d+)\s+insertions?\(\+\)")
DEL_RE = re.compile(r"(\d+)\s+deletions?\(-\)")


def run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def commit_counts() -> dict[str, int]:
    counts: dict[str, int] = {}
    for line in run_git("shortlog", "-sn", "--all", "--no-merges").splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(None, 1)
        if len(parts) != 2:
            continue
        counts[parts[1]] = int(parts[0])
    return counts


def line_stats() -> dict[str, tuple[int, int]]:
    """Map author name -> (insertions, deletions)."""
    inserts: dict[str, int] = defaultdict(int)
    deletes: dict[str, int] = defaultdict(int)
    current: str | None = None

    for line in run_git("log", "--shortstat", "--no-merges", "--pretty=format:Author: %aN").splitlines():
        author_match = AUTHOR_RE.match(line)
        if author_match:
            current = author_match.group(1).strip()
            continue
        if current is None or not FILES_RE.match(line):
            continue
        ins_match = INS_RE.search(line)
        del_match = DEL_RE.search(line)
        inserts[current] += int(ins_match.group(1)) if ins_match else 0
        deletes[current] += int(del_match.group(1)) if del_match else 0

    return {name: (inserts[name], deletes[name]) for name in set(inserts) | set(deletes)}


def format_table(commits: dict[str, int], lines: dict[str, tuple[int, int]], *, zh: bool) -> str:
    names = sorted(set(commits) | set(lines), key=lambda n: (-commits.get(n, 0), n.lower()))
    if zh:
        header = "| 贡献者 | 提交次数 | 新增行 | 删除行 |"
    else:
        header = "| Contributor | Commits | Lines added | Lines removed |"
    rows = [header, "| --- | ---: | ---: | ---: |"]
    for name in names:
        c = commits.get(name, 0)
        added, removed = lines.get(name, (0, 0))
        rows.append(f"| {name} | {c} | +{added:,} | −{removed:,} |")
    return "\n".join(rows)


def replace_block(text: str, table: str) -> str:
    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END),
        re.DOTALL,
    )
    replacement = f"{START}\n{table}\n{END}"
    if not pattern.search(text):
        raise SystemExit("CONTRIBUTORS markers not found; add START/END comments first")
    return pattern.sub(replacement, text, count=1)


def main() -> int:
    commits = commit_counts()
    lines = line_stats()
    if not commits and not lines:
        print("No contributor stats found", file=sys.stderr)
        return 1

    for path in README_FILES:
        if not path.exists():
            continue
        zh = path.name.endswith("zh-CN.md")
        table = format_table(commits, lines, zh=zh)
        updated = replace_block(path.read_text(encoding="utf-8"), table)
        path.write_text(updated, encoding="utf-8")
        print(f"Updated {path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
