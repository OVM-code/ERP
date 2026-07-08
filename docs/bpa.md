# BPA system — from requirement meetings to an interactive client deliverable

The BPA (Business Process Analysis) system turns requirement-meeting material
(transcripts, notes) into the client-facing analysis document: **one interactive HTML
file** showing the client's business processes as clickable BPMN diagrams, where every
process step opens the documentation of that business scenario — how the requirement
is met with standard Business Central, an add-on (Aptean, Continia, …), a workaround,
or a GAP (customisation).

It is built on the **Cegeka Process Model 3.01** content template: every domain
(Verkoop, Inkoop, Voorraad, …) with its coded business scenarios (`BS25.202
Verkooporders maken`, …). The BPA for a client is that template **filtered to what is
relevant and enriched with how it will work for them**.

## Moving parts

| Path | What it is |
|---|---|
| `bpa/template/source-cegeka-process-model-3.01.md` | Verbatim import of the Cegeka BPA template |
| `bpa/template/domains/NN-*.md` | The template split per domain — the source text when authoring client content |
| `bpa/template/catalog.json` | Machine-readable index of every domain and BS/BC scenario code (+ add-on flags). Regenerate with `tools/split_bpa_template.py` |
| `bpa/catalog/` | **Business Process Catalog** — same structure, but evidence-based: per scenario a status (verified/unverified/candidate/retired), evidence trail and last-verified stamp. Scenario-mapping starts here; refreshed monthly (`/catalog-refresh`); its report challenges the template (`bpa/catalog/README.md`) |
| `bpa/branding/` | Cegeka design tokens + logo assets, inlined into every build (see `bpa/branding/README.md`) |
| `bpa/processes/*.process.json` | Standard BPMN process flows per domain, steps linked to BS codes |
| `bpa/viewer/` | The interactive viewer (HTML/CSS/JS), inlined into every build |
| `tools/build_bpa.py` | Compiles a client's `bpa/` workspace into the deliverable |
| `clients/<slug>/bpa/` | Per-client BPA workspace (see `clients/_template/bpa/`) |
| `clients/_demo-bakkerij-florax/` | Worked demo: fictional client, end-to-end |

## The pipeline (what the assistant does)

**Step 0a — Brief.** Before each workshop, generate a briefing pack in
`bpa/briefings/` (format: `clients/_template/bpa/briefings/README.md`): known facts,
hypothesis scope per catalog scenario, numbered questions, applicable lessons. Fork
the industry pack (`bpa/packs/`) as the content starting point when one covers the
client's vertical — keep the pack attribution line for the reuse metric.

**Step 0 — Collect.** Drop meeting material in `clients/<slug>/bpa/inputs/`, one file
per meeting (`YYYY-MM-DD-<topic>-<type>.md`). Text only — transcribe recordings first
(Teams/Copilot/Whisper). Work with what exists: a verbatim transcript, rough notes, or
both; note the quality in the file header, and flag conclusions that rest on thin
sources.

**Step 1 — Extract requirements.** Read the inputs and distil discrete requirements
into `requirements.md` (`## REQ-xxx` blocks). Each keeps a literal client quote, a
source citation (`<file> §<n>`), the interpretation, and priority. Ask the consultant
about contradictions or gaps between meetings rather than guessing.

**Step 2 — Map to scenarios.** For every requirement, find the business scenarios in
the Business Process Catalog (`bpa/catalog/catalog.json` — same codes as the template,
plus evidence and status; grep the template domain files for wording context). Check
the status before promising anything: `verified` is backed by evidence, `unverified`
means double-check against official docs first, `retired` means it is no longer
achievable as claimed. If the catalog has no row for the current month in
`bpa/catalog/refresh-log.md`, offer `/catalog-refresh` first. Record scope decisions
in `coverage.md` — including what is explicitly **out** of scope and why. This is
where "only the relevant parts of the template" is decided.

**Step 3 — Enrich.** For each in-scope scenario, write the client documentation in
`content/NN-<domain>.md` (`## BSxx.xxx` blocks): start from the template text
(`bpa/template/domains/`), make it client-specific, and state the **Invulling**:
`standaard` / `add-on: <naam>` / `workaround` / `gap: GAP-x`. Ground capability claims
in `knowledge/` and check `expertise/` + past SDRs before recommending — the advisory
workflow in `system/instructions.md` applies here too. Anything needing customisation
becomes a `## GAP-x` block in `gaps.md`.

**Step 4 — Flows.** The standard flows in `bpa/processes/` are the default. Where the
client's process differs (extra channels, no approval step, …), copy the flow into
`clients/<slug>/bpa/processes/` and adapt it — same `domain` number overrides the
standard at build time.

**Step 5 — Build.**

```bash
python3 tools/build_bpa.py clients/<slug>
```

Output: `clients/<slug>/bpa/output/BPA-<slug>.html` — self-contained, offline,
shareable. The build cross-checks codes against the catalog and warns about: unknown
BS codes, in-scope scenarios without documentation, references to missing GAP/REQ ids.
Treat warnings as review items, not noise.

## Process flow format

`*.process.json` — rendered as a BPMN-style diagram (auto-layout, no coordinates
needed):

```jsonc
{
  "id": "verkoop",            // unique flow id (used by "goto")
  "domain": 2,                 // Cegeka Process Model domain number
  "title": "Verkoop",
  "subtitle": "Van klantvraag tot betaalde factuur",
  "lanes": [ { "id": "verkoop", "label": "Verkoop" } ],
  "nodes": [
    // types: start | end | task | subprocess | gateway | gateway-parallel
    { "id": "start", "type": "start", "label": "Klantvraag", "lane": "verkoop" },
    { "id": "order", "type": "task", "label": "Verkooporder maken",
      "lane": "verkoop", "scenario": "BS25.202" },          // clickable + colour-coded
    { "id": "wh", "type": "subprocess", "label": "Picken en verzenden",
      "lane": "verkoop", "scenario": "BS25.205", "goto": "magazijnbeheer" }
  ],
  "flows": [ { "from": "start", "to": "order", "label": "ja" } ]
}
```

Layout rules of thumb: the renderer computes columns from flow order (longest path)
and rows from lanes; loops are drawn through the corridor at the bottom of the lane.
Keep flows at 10–20 nodes; split anything bigger into a `subprocess` + `goto`.

## Colour coding (Invulling)

| Invulling | Colour | Meaning |
|---|---|---|
| `standaard` | blue | standard Business Central |
| `add-on: <naam>` | purple | met by a licensed add-on (Aptean, Continia, Tasklet, …) |
| `workaround` | amber | standard functionality + agreed way of working |
| `gap: GAP-x` | red | customisation, described in the GAP register |
| *(no documentation)* | grey dashed | step exists in the flow but not in this BPA version |

## Language

The deliverable follows `language` in `bpa-config.json` (`nl` and `en` built in).
Viewer chrome and the standard flows switch automatically (flow labels are
`{"nl": …, "en": …}` objects); client content is authored directly in the client's
language using the exact BC terms from `bpa/terminology/bc-terms.json`.
`tools/check_client.py` lints English content for leftover Dutch glossary terms.
Adding a language: `bpa/terminology/README.md`.

## Updating the template

When Cegeka ships a new Process Model version: replace
`bpa/template/source-cegeka-process-model-3.01.md` (adjust the filename in
`tools/split_bpa_template.py`), re-run `python3 tools/split_bpa_template.py`, and
review the catalog diff — client workspaces reference scenarios by code, so renamed or
renumbered scenarios show up as build warnings on the next build. Then run
`python3 tools/catalog.py seed` so the Business Process Catalog syncs to the new
structure (curated statuses and evidence survive the sync), and
`python3 tools/catalog.py reconcile` to see what the new template version changed
against the evidence base.

The reverse direction — evidence challenging the template — runs monthly via
`/catalog-refresh`: findings land in `bpa/catalog/vs-template-report.md`, and any
template edits they justify are drafted for human review (`/review-system`).

## PDF export

Every built BPA (and manual) has an **Export PDF** button: pick the domains
(the picker only offers what is in scope for this client — a deliverable never
exposes out-of-scope content) and the sections (intro, scope matrix,
requirements, GAPs), and the viewer composes a print document — Cegeka-branded
cover page, table of contents, running header, process diagram + full scenario
documentation per domain — and opens the browser's print dialog: choose *Save
as PDF*. No dependencies; works offline in any modern browser.
