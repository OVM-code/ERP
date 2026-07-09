# Changelog

## v2.1 — 2026-07

- **Documentation URLs per scenario** (`doc_url`, two-tier): every catalog entry
  links to its official documentation — the exact page consulted at verification,
  or a curated topic page (`bpa/catalog/doc-url-map.json`) until verified. Shown
  in the BPA deliverable (doc panel + PDF export).
- **Human gates between every pipeline step** (`docs/gates.md`): a uniform gate
  block (Status + Directieven) on requirements, scope, BPA sign-off, setup plan,
  FGD/TGD, migration, test, trajectory and manual sign-off. The consultant's
  directives reshape step N's output before it feeds step N+1; `check_client.py`
  enforces order and blocks approval with open directives.
- BPA/manual builds read the evidence-based catalog (`bpa/catalog/`) and show
  per-scenario catalog status in the deliverable; template numbering invariant
  machine-enforced (cost model keys on BS/BC codes).

## v2 — 2026-07

The "official deliverable" release: Cegeka identity, PDF export, an evidence
layer under the template, and an onboarding path for consultants new to the
system. (Kickoff brief: `system/handover-2026-07-v2-kickoff.md`.)

- **Cegeka branding** (`bpa/branding/`): design tokens and logo extracted from
  the official Cegeka PPT template; the interactive BPA/manual viewer now
  carries the corporate identity. Rebrandable by swapping one folder.
- **PDF export**: every built deliverable exports itself — pick domains
  (in-scope only) and sections, get a branded cover page, table of contents,
  running header and full documentation via the browser's print-to-PDF. No new
  dependencies.
- **Business Process Catalog** (`bpa/catalog/`): the evidence-based register of
  what is actually achievable in standard BC (+ used add-on processes), decoupled
  from per-client checks: refreshed at most **once a month** (`/catalog-refresh`,
  throttle in `refresh-log.md`, no cron or cloud dependency). BPA scenario-mapping
  now starts here; the reconciliation report challenges `bpa/template/`, and
  template edits it justifies go through `/review-system`.
- **Methodology guidance layer** (`methodology/`): six phase guides — Prepare →
  BPA → SDB (Solution Design & Build) → Test → Deploy → Support — each mapping
  the phase's purpose, workflow, assets, expertise entry points and exit gate,
  readable by a consultant who has never seen this system; plus a full glossary.
  The assistant guides by phase ("I'm in SDB for client X — what's next?").

## v1 — 2026-07 (earlier)

Advisory workflow + knowledge/expertise layers; BPA pipeline with interactive
BPMN viewer; delivery pipeline (setup, FGD/TGD, migration, test, training,
manual, aftercare) with templates, guides and mechanical gates; skills
(`dynamic-report`, `harvest`, `wave-impact`, `review-system`); demo client;
clone tooling (`doctor.py`, `docs/cloning.md`); Copilot Studio deployment kit.
