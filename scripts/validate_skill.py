#!/usr/bin/env python3
"""Structural checks for the landing-page skill bundle.

Catches the ways this skill breaks in practice: a reference file that SKILL.md
points at but nobody shipped, an orphan reference nothing loads, an installer
that forgot a file, and the BOM PowerShell adds when you least want it.

    python scripts/validate_skill.py

Exit 0 = clean. Stdlib only, Python 3.8+.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
REFDIR = ROOT / "references"
INSTALLERS = (ROOT / "install.ps1", ROOT / "install.sh")

failures: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    check(SKILL.is_file(), "SKILL.md is missing")
    if not SKILL.is_file():
        return report()

    text = SKILL.read_text(encoding="utf-8")

    # --- frontmatter -------------------------------------------------------
    check(text.startswith("---\n"), "SKILL.md does not open with a frontmatter block")
    head = text.split("\n---\n", 1)[0] if "\n---\n" in text else ""
    check("name: landing-page" in head, "frontmatter is missing 'name: landing-page'")
    check(
        re.search(r"^\s+version:\s*\d+\.\d+\.\d+\s*$", head, re.M) is not None,
        "frontmatter is missing a semver 'version:' under metadata",
    )
    check("description:" in head, "frontmatter is missing 'description:'")
    check(
        "/landing-page" in head,
        "the description should name the '/landing-page' invocation so the skill triggers on it",
    )

    # --- references: shipped, referenced, and not orphaned ------------------
    shipped = {p.name for p in sorted(REFDIR.glob("*.md"))} if REFDIR.is_dir() else set()
    check(bool(shipped), "references/ contains no .md files")
    cited = set(re.findall(r"references/([A-Za-z0-9_.-]+\.md)", text))
    for name in sorted(cited - shipped):
        failures.append(f"SKILL.md cites references/{name} but the file is not in the repo")
    for name in sorted(shipped - cited):
        failures.append(f"references/{name} ships but SKILL.md never points at it")

    # --- installers fetch every shipped reference --------------------------
    for installer in INSTALLERS:
        check(installer.is_file(), f"{installer.name} is missing")
        if not installer.is_file():
            continue
        body = installer.read_text(encoding="utf-8")
        for name in sorted(shipped):
            check(name in body, f"{installer.name} does not install references/{name}")

    # --- anchors in each reference's Contents list resolve ------------------
    for ref in sorted(REFDIR.glob("*.md")) if REFDIR.is_dir() else []:
        body = ref.read_text(encoding="utf-8")
        slugs = {slugify(m) for m in re.findall(r"^#{1,6}\s+(.*)$", body, re.M)}
        for anchor in re.findall(r"\]\(#([A-Za-z0-9_-]+)\)", body):
            check(anchor in slugs, f"references/{ref.name}: link #{anchor} matches no heading")

    # --- byte hygiene ------------------------------------------------------
    for path in sorted(ROOT.rglob("*")):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".sh", ".ps1", ".py", ".html", ".yml", ".yaml"}:
            continue
        raw = path.read_bytes()
        rel = path.relative_to(ROOT).as_posix()
        check(not raw.startswith(b"\xef\xbb\xbf"), f"{rel} starts with a UTF-8 BOM")
        check(b"\t" not in raw or path.suffix == ".py", f"{rel} contains a literal tab")

    return report()


def slugify(heading: str) -> str:
    """GitHub's heading-anchor rule, near enough for these documents."""
    s = heading.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"[\s_]+", "-", s).strip("-")


def report() -> int:
    if failures:
        print(f"FAIL — {len(failures)} problem(s):")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("OK — skill bundle is structurally sound")
    return 0


if __name__ == "__main__":
    sys.exit(main())
