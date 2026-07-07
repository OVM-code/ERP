---
name: dynamic-report
description: Build an interactive, assumption-driven advisory report (single-file HTML) from an analysis — findings register with live € formulas, adjustable sliders, filterable cards, prioritisation chart. Use when asked for a "dynamic report", strategy/methodology review, business case, or any deliverable where the reader should test the numbers themselves. Reference implementation: docs/methodology-review-2026-07.html.
---

# Dynamic suggestive report

Turns an analysis into a page the reader *operates*: they set the assumptions, the
report recomputes; they filter the findings, click through from chart to detail.
The credibility mechanism is **transparent formulas + cited evidence**, not polish.

## Procedure

### 1. Substance before pixels
- Ground every finding in verifiable evidence. In this repo that means citing real
  files/paths; in other contexts, sources. An uncited finding is an opinion.
- Structure findings as a uniform register: `{id, title, stage, category, effort
  (S/M/L), horizon, status, leak, evidence, fix, first-step, value-formula}`.
- Define the **assumption model** first: 4–6 sliders (volumes, rates, counts) that
  every € figure derives from via a stated one-line formula. Simple formulas the
  reader can argue with beat precise-looking black boxes. Label everything
  "directional"; include a calibration path (how assumed → measured).
- Include a "what NOT to change" section — reviews that only find faults read as
  naive and get defended against.

### 2. Design (mandatory pre-work)
- Load the `artifact-design` skill (treatment calibration, both themes, no
  templated look) and the `dataviz` skill **before writing chart code**.
- Validate the categorical palette with the dataviz validator for BOTH surfaces:
  `node <dataviz>/scripts/validate_palette.js "<hexes>" --mode light|dark`.
- Theme via CSS custom properties on `:root`, overridden under
  `@media (prefers-color-scheme: dark)` AND `:root[data-theme="dark"]` /
  `:root[data-theme="light"]` (the artifact viewer's toggle must win both ways).
- Subject-grounded type: for Microsoft/BC material, Segoe UI + Cascadia Mono is a
  deliberate fit, not a lazy default. `tabular-nums` on all figures.

### 3. Build (single self-contained file, vanilla JS)
- Artifact CSP: no CDNs, no external anything. Write the page as a fragment
  (`<title>` + `<style>` + markup + `<script>`, no doctype/html/head/body).
- Skeleton that works: sticky rail nav · hero with 3–4 headline stats · assumptions
  card (range inputs + `<output>`) · pipeline/stage map with count badges (click →
  filters register) · findings register (`<details>` cards, category filter chips,
  sort by value/effort) · SVG scatter value-vs-effort (viewBox, dots ≥8px with
  direct id labels, hover tooltip, click → opens the card) · roadmap columns whose
  totals also recompute · metrics + method/caveats sections.
- One render path: state object (assumptions + filters) → render functions; every
  slider input re-renders headline, register, chart, roadmap.
- Chart hygiene (from dataviz): gridlines/labels get `pointer-events:none`; spread
  same-band dots with wide jitter (≥52px) and label all dots to the right — do NOT
  alternate label sides (it scrambles dot–label association); legend chips for
  categories; the register is the chart's table view.

### 4. Verify in Chromium before publishing (non-negotiable)
Playwright + the preinstalled browser; wrap the fragment in a doctype for local
preview. Assert, don't eyeball: headline values present; slider change → totals
change; filters change card counts; stage click filters; a card expands; tooltip
appears (hover the `circle`, not the `<g>` — its bbox center is empty space);
`data-theme` override wins on the opposite OS scheme. Then screenshot light + dark
and actually look at them (label collisions live here). Fix, re-run, only then ship.
Beware sed on HTML/JS — one bad pattern silently clobbers a line; patch via Python
string replace with `assert old in s`.

### 5. Ship three ways
1. `Artifact` tool (same file path on redeploys → same URL; stable favicon).
2. Commit a standalone copy (doctype-wrapped) into the repo so the report lives
   with what it reviews — it is versioned advice, update it as findings close
   (`status` field: open / addressed / closed, with the headline split by status).
3. `SendUserFile` the repo copy with a one-line "how to operate it" caption.
