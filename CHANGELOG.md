# Changelog

All notable changes to the `landing-page` skill.

## [1.0.0] — 2026-07-27

First public release. The skill itself was written on 2026-07-21 and has been in use since;
this is the packaged, installable version of it.

- `SKILL.md` — the protocol: completion bar, repository-as-source-of-truth rule, seven phases,
  positioning, evidence classification, voice, links and assets, README template, deliverables,
  completion report, final tests.
- `references/investigation.md` — Phase 1, repository investigation checklist.
- `references/stack.md` — Phase 2, existing stack and brand, stack choice, location, build,
  GitHub Pages deployment.
- `references/design.md` — Phase 4, design system.
- `references/structure.md` — Phase 5, section structure and scroll narrative.
- `references/review.md` — Phase 6, the run-it-and-look-at-it loop and quality review.
- `install.ps1` / `install.sh` — one-line installers.
- `scripts/validate_skill.py` — structural checks for the bundle, wired into CI.
- `docs/` — the project site, built with this skill.

### Notes on how it got here

The predecessor (`repo-landing-page`, v0.1, not released) produced only a `README.md` because
its source prompt asked for GitHub-flavored Markdown. That is the failure this version exists to
prevent: **the website is the deliverable, and the README is a short supporting artifact.**

Two rules in the skill are there because they were got wrong first:

- Phase 2 runs before any design work. If the repository already declares tokens, brand colors,
  or typefaces, that *is* the visual identity — inventing a parallel palette produces a template
  with the right words on it.
- Don't copy the reference site you're shown. Match its craft, reject its palette and structural
  devices.
