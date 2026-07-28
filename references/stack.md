# Phase 2 — Stack, Location, Build, Deploy

Do this before any design work. What you find here decides whether you are extending an
identity or creating one, and getting that backwards produces a page that looks like a template
wearing the project's name.

## Contents

1. [Assess what already exists](#1-assess-what-already-exists)
2. [Preserve the existing brand](#2-preserve-the-existing-brand)
3. [Choose the stack](#3-choose-the-stack)
4. [Choose the location](#4-choose-the-location)
5. [Build scripts](#5-build-scripts)
6. [GitHub Pages deployment](#6-github-pages-deployment)
7. [File quality](#7-file-quality)

---

## 1. Assess what already exists

Search the repository for any:

marketing site · documentation site · frontend application · design system · component library ·
brand assets · logo · typography · icons · screenshots · color variables · CSS framework ·
Tailwind configuration · Astro site · Next.js site · Vite site · React site · Vue site · Svelte
site · static HTML site · GitHub Pages configuration · deployment workflow

Concretely, go looking for these — they are easy to miss and expensive to miss:

```bash
# declared design tokens and theme variables
grep -rn '^\s*--[a-z]' --include='*.css' --include='*.scss' . | head -40
# tailwind / theme config
find . -name 'tailwind.config.*' -o -name 'theme.*' -not -path '*/node_modules/*'
# fonts the product actually declares
grep -rn 'font-family' --include='*.css' --include='*.ts' --include='*.tsx' . | head
# existing sites and pages configuration
find . -name 'astro.config.*' -o -name 'next.config.*' -o -name 'vite.config.*' \
       -o -name '_config.yml' -o -name 'CNAME' -not -path '*/node_modules/*'
```

**If a suitable site already exists:** preserve its working architecture, improve it in place,
reuse its components, retain functional routes, follow its conventions, and avoid a rewrite.

**If none exists:** create one.

---

## 2. Preserve the existing brand

If the repository already has a recognizable identity, the landing page inherits it:

- preserve the project name
- preserve appropriate logo usage
- preserve established colors where suitable
- preserve domain-specific terminology
- preserve the tone the project already uses
- improve consistency rather than arbitrarily replacing the identity

**A tokens file, a set of CSS custom properties, or a declared type stack *is* the product's
visual identity.** Use it as the basis for the site's design system rather than inventing a
parallel one. A page built in the product's own colors and typefaces looks like the software; a
page built in colors you chose looks like a template.

If the declared typefaces are open-licensed and not bundled, embed them properly rather than
silently falling back to system fonts — a declared font that doesn't load is a design decision
lost.

Do not rebrand a project without evidence or instruction. If the existing brand is visually
weak, refine its presentation while preserving recognition.

---

## 3. Choose the stack

The lightest implementation that can produce a genuinely polished result, in order of
preference:

1. **The repository's existing website stack**
2. **Astro** — content-first, ships almost no JavaScript
3. **Vite + React** — when interactivity justifies it
4. **Next.js** — only when the repository already justifies it
5. **Static HTML, CSS, and JS** — right for simple projects, and never a lesser choice

Do not introduce a heavy framework for visual effect. Do not create a backend for a static page.
Do not add unnecessary dependencies. Do not switch the repository's package manager.

The site should be easy for a maintainer to understand and update six months from now.

---

## 4. Choose the location

Place the site in the most appropriate existing location:

```text
website/
site/
docs/
apps/web/
apps/website/
```

- Do not overwrite product code.
- Do not put the landing page inside `README.md`.
- If the repository already serves GitHub Pages from `/docs`, preserve that convention unless
  there is a strong technical reason not to.
- Document the final location clearly.

---

## 5. Build scripts

Add or update scripts so a maintainer can reliably run the site, using the repository's actual
package manager:

```bash
npm install
npm run dev
npm run build
npm run preview
```

Do not delete existing scripts unnecessarily. Document where the site lives, how to run it, how
to build it, how to preview it, and how to deploy it.

---

## 6. GitHub Pages deployment

Provide a working deployment path unless the repository clearly uses another host. When Pages is
appropriate:

- add a GitHub Actions workflow
- configure the correct build output directory
- **configure the base path for project sites** — the site is at `/<repo>/`, not the root
- ensure assets resolve under the repository subpath
- support a custom domain only if one is already configured
- avoid hard-coded `localhost` URLs
- verify static routing, and that a refresh on a deep link does not break
- ensure generated paths are portable

If the chosen framework needs a `base` or asset prefix for Pages, set it. Never assume the
project is hosted at a domain root.

---

## 7. File quality

Produce code a maintainer would accept in review:

clear component boundaries · sensible file names · reusable sections · minimal duplication ·
semantic HTML · clean CSS · no giant single-file component unless justified · no dependency
sprawl · no dead code · no lorem ipsum · no broken imports · no unused assets · no hidden
secrets · no hard-coded private URLs · no inaccessible interactive controls.

Comment only where a comment adds something the code doesn't.
