# Phase 4 — Design System

Define the system before implementing the page. Deciding colors and type inside the markup is
how a page ends up inconsistent.

**First, re-check Phase 2.** If the repository already has tokens, brand colors, or declared
typefaces, this phase is *extending that system*, not authoring a new one.

## Contents

1. [Define the system](#1-define-the-system)
2. [Derive it from the product](#2-derive-it-from-the-product)
3. [Visual quality standard](#3-visual-quality-standard)
4. [Typography](#4-typography)
5. [Color and accessibility](#5-color-and-accessibility)
6. [Motion](#6-motion)
7. [Imagery](#7-imagery)

---

## 1. Define the system

Write these down before building:

**Color** — background, surface, text, accent, border. Semantic states (good / warning /
critical) separate from the accent.
**Typography** — scale, heading styles, body styles, line heights, text widths.
**Space** — spacing scale, section spacing, content width.
**Form** — border radius, shadows, button styles, card styles.
**Behavior** — navigation behavior, responsive breakpoints, motion principles.
**Detail** — icon treatment, image treatment, code block treatment.

---

## 2. Derive it from the product

Base the visual identity on the software itself. Consider its domain, audience, technical
character, project values, existing logo, repository colors, screenshots, existing UI, and
whether the tone is public-service or commercial, developer-oriented or end-user, playful or
institutional.

The useful question: **what does this software look like to the people who already live in its
domain?** A broadcast tool can borrow the control room. A CAD tool can borrow the drawing. A
security tool can borrow the audit log. That is where distinctive, non-generic choices come from.

**Do not default to** purple gradients · dark SaaS backgrounds · glassmorphism · neon glows ·
generic blue cards · abstract blobs · excessive gradient text · generic startup aesthetics.

**Do not copy the reference site you were shown.** If someone points at another project's page
as the bar, match its level of craft and reject its palette, type, and structural devices. Two
projects that look like siblings both look generic.

**Commit to one visual world.** A branded product page may fix its own palette rather than
following the viewer's light/dark preference — a legitimate choice when it is deliberate and
executed fully. If the product itself ships a dark theme, using it for one section is authentic
rather than decorative.

**Spend boldness once.** One place carries the personality — the hero visual, a status board, a
typographic moment. Everything around it stays quiet.

---

## 3. Visual quality standard

The page must look intentionally designed by a skilled product designer:

strong visual hierarchy · balanced whitespace · disciplined typography · clear section
transitions · polished component spacing · consistent alignment · meaningful contrast ·
restrained color · professional responsive behavior · thoughtful screenshots and diagrams ·
clear primary and secondary actions · a deliberate scroll narrative.

Do not confuse beauty with decoration. Avoid excessive animation · too many badges · too many
icons · walls of text · arbitrary gradients · repeated card grids · repetitive section patterns
· inconsistent radius or shadow · fake testimonials · fake metrics · fake customer logos ·
unsupported claims · empty decorative sections.

Every visual element either explains the product or guides the user. If it does neither, cut it.

---

## 4. Typography

Deliberate, not default: a strong display heading, a readable body face, restrained line length,
clear heading hierarchy, comfortable line height, consistent text widths, accessible sizing,
responsive scaling, strong contrast. No tiny body text. No giant headings that break on mobile.

Prefer system fonts or the repository's approved web fonts. Consider privacy, offline operation,
and project conventions before introducing an external font dependency — and if the page must be
self-contained, embed the face as a data URI rather than linking a CDN that will silently fail.

Reach for `font-variant-numeric: tabular-nums` wherever digits line up in columns.

---

## 5. Color and accessibility

Meet **WCAG AA** contrast for normal text, at minimum. Include:

- visible keyboard focus states
- semantic headings in real order
- proper button and link semantics
- alt text on meaningful images
- `prefers-reduced-motion` support
- a mobile navigation that actually works with a keyboard
- accessible forms, if there are any
- **no information carried by color alone** — pair a status color with a word

Do not sacrifice accessibility for aesthetics. The page must remain understandable with
animation disabled.

---

## 6. Motion

Sparingly. Subtle entrance transitions, hover states, nav transitions, diagram motion,
screenshot emphasis, very low-intensity background movement.

Respect `prefers-reduced-motion`. Avoid motion that blocks interaction, long page-load animation
sequences, gimmicky cursor effects, constant movement, and animation added only to imitate a
startup template.

---

## 7. Imagery

In order of preference:

1. actual product screenshots
2. repository diagrams
3. diagrams generated from the real architecture
4. real code examples
5. domain-specific illustration
6. restrained abstract graphics

If the application runs locally, **run it and capture current screenshots** — of the dashboard,
the primary workflow, configuration, monitoring, results, an admin view, a mobile layout. Check
every capture for secrets, tokens, and personal data before it ships. Caption them with the value
they demonstrate, not the name of the screen.

Never stock photography. Never imagery unrelated to the software. Never a fabricated screenshot,
customer logo, award, or press mention. When no assets exist, build tasteful CSS or SVG
compositions grounded in the product — and if you render a UI illustration rather than capturing
the real thing, say so honestly in a caption.
