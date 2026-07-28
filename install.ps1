# landing-page installer — copies the skill into ~/.claude/skills/landing-page
# Usage: iwr -useb https://raw.githubusercontent.com/scottconverse/landing-page/main/install.ps1 | iex
$ErrorActionPreference = "Stop"
$raw = "https://raw.githubusercontent.com/scottconverse/landing-page/main"
$dest = Join-Path $HOME ".claude\skills\landing-page"
New-Item -ItemType Directory -Force (Join-Path $dest "references") | Out-Null
Invoke-WebRequest -UseBasicParsing "$raw/SKILL.md" -OutFile (Join-Path $dest "SKILL.md")
foreach ($f in @("investigation.md", "stack.md", "design.md", "structure.md", "review.md")) {
  Invoke-WebRequest -UseBasicParsing "$raw/references/$f" -OutFile (Join-Path $dest "references\$f")
}
Write-Host "landing-page installed to $dest"
Write-Host "Try it: tell Claude 'build a landing page for this repo' or '/landing-page'"
