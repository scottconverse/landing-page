#!/usr/bin/env bash
# landing-page installer — copies the skill into ~/.claude/skills/landing-page
# Usage: curl -fsSL https://raw.githubusercontent.com/scottconverse/landing-page/main/install.sh | bash
set -euo pipefail
RAW="https://raw.githubusercontent.com/scottconverse/landing-page/main"
DEST="$HOME/.claude/skills/landing-page"
mkdir -p "$DEST/references"
curl -fsSL "$RAW/SKILL.md" -o "$DEST/SKILL.md"
for f in investigation.md stack.md design.md structure.md review.md; do
  curl -fsSL "$RAW/references/$f" -o "$DEST/references/$f"
done
echo "landing-page installed to $DEST"
echo "Try it: tell Claude 'build a landing page for this repo' or '/landing-page'"
