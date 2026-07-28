# Phase 6 — Run It, Look At It, Fix It

This phase is what separates a built site from a delivered one. Skipping it is how a page ships
with a broken mobile menu and a diagram nobody can read.

## Contents

1. [Visual verification loop](#1-visual-verification-loop)
2. [Quality review](#2-quality-review)

---

## 1. Visual verification loop

When the environment allows it:

1. install dependencies
2. run the site locally
3. render the page
4. inspect at **desktop** width
5. inspect at **tablet** width
6. inspect at **mobile** width
7. capture screenshots
8. review the visual hierarchy
9. fix the layout defects
10. repeat until polished

Look specifically for:

broken layouts · clipping · overflow · poor contrast · inconsistent spacing · excessive blank
space · unreadable diagrams · broken images · missing assets · dead links · mobile navigation
failures · text wrapping problems · overlapping elements · inaccessible focus states · visual
monotony.

**Do not declare completion without visually inspecting the result when tooling permits.** If
tooling does not permit it — no renderer, no display, a blocked server — say so plainly rather
than implying you saw it. An unverified claim about appearance is the same defect as an
unverified claim about a feature.

Verify the built output too, not just the dev server: run the build, preview it, and confirm
asset paths still resolve under the deployment subpath.

---

## 2. Quality review

Work through every question. A "no" is a revision, not a footnote.

### Product understanding
- Can a new visitor understand the product within ten seconds?
- Is the main audience clear?
- Is the primary outcome clear?
- Is the strongest differentiator clear?
- Does the page explain the real product, rather than the README's version of it?

### Visual quality
- Does the page look professionally designed?
- Is the hero memorable and clear?
- Is the typography disciplined?
- Is the spacing consistent?
- Is there enough visual variation?
- Are sections distinct without feeling disconnected?
- Does it avoid generic template aesthetics?
- Does it look credible beside leading open-source product sites?

### Technical quality
- Does the site build? Does it run?
- Are all links functional?
- Are all assets present?
- Does the deployment routing work, including under a repository subpath?
- Is the implementation maintainable?
- Are the dependencies justified?
- Is the responsive behavior correct at all three widths?

### Accuracy
- Is every major claim supported by repository evidence?
- Are planned features labeled planned?
- Are experimental features labeled experimental?
- Are mocked integrations excluded from claims of working support?
- Are limitations honestly represented?
- Are the installation steps verified?

### Accessibility
- Is the text readable and the contrast sufficient?
- Is keyboard navigation usable end to end?
- Are focus states visible?
- Are images labeled?
- Is reduced motion supported?
- Does the mobile menu work accessibly?

### Persuasion
- Is the page compelling because of real value?
- Would a user know what to do next?
- Would an engineer trust the technical claims?
- Would a decision maker understand the benefit?
- Would a contributor see clear entry points?

---

### Final tests

**Does this look and behave like a real world-class product website, or like a README converted
into cards?** If it still feels like a README, redesign it.

**Does the page use actual product evidence, or generic marketing patterns?** If it leans on
generic patterns, revise it.

**Would I be comfortable using this as the public face of a serious open-source project?** If
not, keep refining.
