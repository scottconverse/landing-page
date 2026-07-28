# Phase 5 — Page Structure

Choose the structure the actual project needs. Do not use every section below; a strong page
usually uses most of them, in an order that carries a narrative.

## Contents

1. [Sections](#1-sections)
2. [Design rhythm](#2-design-rhythm)

---

## 1. Sections

### Navigation
Responsive and professional. Project name or logo, a few real anchors (Product, Features, How It
Works, Screenshots, Architecture, Documentation, GitHub, Contributing), one primary CTA, a
working mobile menu, visible keyboard focus, sensible sticky behavior. **No dead links.**

### Hero
Strong enough to carry the page. Product name, a precise headline, a concise value proposition,
a primary CTA, a secondary CTA, one visual proof element, and a few high-value trust signals.

Visual proof can be an actual screenshot, an interface rendering built from repository assets,
an architecture or workflow visualization, a code sample, a terminal, a device frame, the real
running application, or a product diagram. **Do not use meaningless abstract artwork when real
product proof is available, and never fabricate a screenshot.**

### Proof strip
A compact band of facts: self-hosted, open source, local-first, supported protocols, deployment
methods, key platforms, API availability, release status. Facts only — no invented user counts,
stars, uptime, customer numbers, or performance claims.

### Problem and purpose
What users struggle with today, why existing approaches fall short, why this project exists,
what changes after adoption. Grounded and concise — resist explaining the whole market.

### Core capabilities
Group features into meaningful product themes — Operate, Automate, Integrate, Monitor, Extend,
Deploy, Recover, Create, Publish, Manage, or names from the project's own vocabulary. Use as many
themes as the product needs.

Do not make every capability its own card. Do not ship generic cards labeled only *Fast*,
*Secure*, *Flexible*, or *Modern* — use concrete capability titles.

### Product screenshots
Real ones, showing meaningful states: dashboard, primary workflow, configuration, scheduling,
monitoring, results, admin view, mobile layout. Concise captions that explain value rather than
naming the screen. No secrets, tokens, or personal data in any capture.

### How it works
The primary workflow, visually — numbered steps, a timeline, a flow diagram, an annotated
product sequence, or a workflow tied to the architecture. Understandable to non-specialists.
Number steps only when the order is real.

### Architecture
When the repository is technical enough to justify it. Show real components and relationships:
browser, API, worker, database, queue, integrations, adapters, storage, external services,
hardware, plugin boundaries. Keep it readable — not a wall-sized engineering diagram.

### Use cases
Realistic scenarios supported by current capabilities: individual operator, small organization,
multi-site deployment, developer integration, public agency, education, automation-heavy
workflow, offline installation. No aspirational industries the product doesn't serve.

### Differentiation
Compare *approaches* fairly — self-hosted vs hosted, integrated workflow vs scripts, open source
vs proprietary, modular vs monolithic, local-first vs cloud-dependent, extensible vs fixed,
operator-focused vs developer-only. Never attack a competitor. Never build a strawman.

### Technical highlights
What builds trust with engineers: API structure, plugin model, event architecture, supported
protocols, deployment options, database support, test infrastructure, extension points, package
boundaries, reliability model. Enough to be credible without overwhelming the page.

### Quick start
The shortest verified route to a meaningful result: prerequisites, installation, configuration,
first run, expected output, next step. **Commands that actually work** — never an invented
package name, port, environment variable, or container image.

### Deployment
Supported options — local, Docker, Compose, Kubernetes, on-premises, cloud VM, edge device,
static hosting, GitHub Pages — with development setup, production-oriented deployment, and
experimental paths clearly distinguished.

### Current status and limitations
Maturity, honestly, plus the limitations that affect adoption: experimental integrations,
single-node limits, incomplete authentication, manual upgrade steps, unsupported operating
systems, early-stage APIs, missing production hardening, unfinished UI, external service
requirements.

State them neutrally and in context. Do not bury material risk; do not turn the section into
self-sabotage. On a well-designed page this reads as confidence.

### Contributing
Why the codebase is approachable, with real evidence: contributor guide, modular packages, test
suites, fixtures, mocks, issue templates, extension interfaces, local development commands,
clear package boundaries. Direct links.

### Final CTA
Concise and confident: try it, read the docs, view the repository, run it locally, explore the
demo, contribute, deploy your own instance. Working links only.

### Footer
Project name, documentation, repository, issue tracker, license, contribution link, community
links, and maintainership or copyright where it exists. **Never invent a social channel.**

---

## 2. Design rhythm

Do not repeat one layout pattern section after section. The tell of a generated page:

> hero → three cards → three cards → three cards → CTA

Vary the visual mode deliberately. A page that rewards scrolling might run:

> centered hero → proof strip → narrative → large screenshot → split section → capability grid →
> workflow sequence → architecture diagram → code example → comparison → limitations callout →
> final CTA

Each major section introduces a new visual mode **without breaking the design system**. Variation
without chaos.
