# Phase 1 — Repository Investigation

A checklist to sweep, not prose to read start to finish. The goal is that nothing meaningful
goes unexamined because it wasn't in the README.

## Contents

1. [What to read](#1-what-to-read)
2. [Product identity](#2-product-identity)
3. [Audience](#3-audience)
4. [Capability inventory](#4-capability-inventory)
5. [Hidden value](#5-hidden-value)
6. [Maturity](#6-maturity)

---

## 1. What to read

Study the complete codebase, including all relevant:

**Code** — source files, modules, packages, services, applications, routes, UI components,
pages, screens, CLI commands, protocols, plugins, extensions, adapters, integrations.

**Contracts and data** — APIs, API schemas, database schemas, migrations, configuration files,
manifests, environment templates, dependency files, package scripts.

**Documents** — user manuals, operator manuals, administrator guides, developer guides,
installation instructions, architecture documents, product requirements, design documents,
specifications, ADRs, changelogs, release notes, roadmaps.

**Process** — workflows, CI/CD configuration, deployment files, Docker files, issue templates.

**Evidence of behavior** — tests, mocks, fixtures, examples, demos, screenshots, diagrams, and
internal comments that reveal intended behavior.

**Declared support** — platforms, operating systems, databases, file formats, runtimes.

**Unfinished work** — incomplete or experimental modules, live TODOs, placeholder integrations,
disabled code paths.

Two things to watch for specifically, because they are where a landing page is won or lost:

- Capabilities that exist in the implementation but appear nowhere in the docs → **elevate them.**
- Documented features whose implementation is a stub, mock, or disabled path → **qualify them.**

---

## 2. Product identity

Establish, from evidence:

- the product name and software category
- the central problem it solves
- the main user outcome
- the primary workflow
- the most important differentiator
- the shortest accurate explanation of the product
- the strongest proof that it is real and useful

Then answer, internally:

- What is this? Who is it for? Why does it exist?
- What does it replace or improve? Why would someone choose it?
- What becomes easier after adopting it?
- What does the architecture enable?
- What is surprisingly capable? What is unfinished?
- What would impress an engineer?
- What would impress a non-technical decision maker?

---

## 3. Audience

Identify the actual audiences, not aspirational ones: end users, developers, administrators,
operators, organizations, businesses, schools, public agencies, governments, researchers,
makers, creators, infrastructure teams, contributors.

For each audience that matters:

- why they care
- what problem disappears
- which capability matters most to them
- what technical knowledge they need
- what trust signals they need
- what action the page should encourage from them

A page that claims everyone is the user tells a reader nothing about whether they are. Name who
it is *not* for.

---

## 4. Capability inventory

Build this internally, then decide what deserves prominence. Not everything belongs on the page;
some belongs in a technical section, and much belongs nowhere.

**Product** — core features, user workflows, automation, scheduling, processing, publishing,
collaboration, administration, search, reporting, import/export.

**Surfaces** — APIs, CLIs, SDKs, web app, desktop app, mobile app, worker, daemon, library,
headless mode.

**Reach** — integrations, protocols, plugins, extensions, adapters.

**Operation** — local operation, remote operation, offline operation, self-hosting, cloud
support, on-premises support, distributed behavior, scaling, caching, failure recovery.

**Security** — authentication, authorization, roles, security controls.

**Running it** — observability, monitoring, logging, alerts, backups, migrations.

**Experience** — customization, accessibility, internationalization.

**Support matrix** — platforms, databases, file formats, runtimes.

**Engineering** — developer tooling, tests, CI/CD, release automation.

**Edges** — known limitations, experimental features, roadmap evidence.

---

## 5. Hidden value

Maintainers routinely under-sell the thing that makes their project interesting, because to them
it is just how they built it. Look for:

modular architecture · adapter-based design · local-first behavior · self-hosted operation ·
headless operation · API-first design · event-driven workflows · extensibility · plugin systems
· automation primitives · reusable packages · provider abstraction · protocol abstraction ·
distributed operation · strong mocks or simulators · realistic test infrastructure · low
infrastructure requirements · hardware integration · graceful degradation · offline capability ·
strong operator tooling · MCP support · AI integration · remote management · batch processing ·
fault tolerance

Elevate only what is real and useful, and always state it as consequence rather than mechanism.
Do not inflate ordinary implementation details into selling points.

---

## 6. Maturity

Judge from: test depth · release history · installation reliability · upgrade paths ·
migrations · error handling · production configuration · security controls · observability ·
backups · deployment automation · active TODOs · unfinished UI · placeholder integrations ·
documentation quality · issue activity · release artifacts.

Classify honestly: *production-ready · production-oriented · actively developed · functional but
evolving · early-stage · experimental · prototype · proof of concept.*

Do not imply production readiness unless the evidence supports it, and do not read polish as
maturity — a well-styled prototype is still a prototype.
