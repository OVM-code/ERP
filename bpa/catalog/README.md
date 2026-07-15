# Business Process Catalog

The **standing, evidence-based register** of business processes: everything
consultants have, at some point, deemed settable-up with **standard Business
Central**, plus **add-on processes that are actually used** at clients. It
mirrors the domain → scenario structure of the Cegeka BPA template but is a
different thing:

| | `bpa/template/` | `bpa/catalog/` |
|---|---|---|
| What it is | the Cegeka document structure & wording (Process Model) | the evidence base |
| Source of truth for | how a BPA deliverable is worded and organised | whether a scenario is *actually achievable* and *actually used* |
| Changes when | Cegeka publishes a new template version | evidence arrives (client work, SDRs, lessons) or a monthly refresh verifies/refutes entries |
| Freshness | reviewed via `/review-system` | **once-a-month refresh** (`refresh-log.md` throttle, works on any Claude plan — no infrastructure) |

## Files

- `catalog.json` — the catalog. Per scenario: `status` (`unverified` /
  `verified` / `candidate` / `retired`), `evidence` (which client, SDR, lesson
  or official source backs it — demo clients marked, they never verify),
  `last_verified` (YYYY-MM), `fulfilment` (`standard` / `addon`), `notes`,
  and a **documentation URL** (`doc_url` + `doc_url_level`) so every entry is
  reviewable against its official source:
  - `specific` — the exact page a verification consulted (from `docs:` evidence);
  - `topic` — curated official landing page per domain/add-on from
    `doc-url-map.json`, assigned mechanically until verification upgrades it;
  - `none` — no public docs exist (Cegeka-internal layer).
  The links surface in the built BPA (doc panel + PDF export), so consultant
  and client can check any claim at the source.
- `doc-url-map.json` — the curated topic-URL map (per domain and per add-on),
  applied by `seed`; edit it here to change where unverified scenarios point.
- `vs-template-report.md` — the **challenge artifact**, regenerated on every
  refresh: template claims without evidence, stale entries, catalog entries the
  template lacks, frequently used add-on scenarios. Template edits that follow
  from it go through `/review-system` — nothing auto-merges.
- `refresh-log.md` — month-keyed throttle + audit trail.

## Numbering invariant (cost model!)

The BS/BC scenario numbering of the **original Cegeka BPA template is the
master**. The cost model (`pricing/effort-baselines.json`) prefix-matches on
these codes, and every client workspace references scenarios by code — so the
catalog **never renumbers, never reuses, never invents** template codes:

- `seed` copies codes verbatim from `bpa/template/catalog.json`.
- A scenario discovered by a refresh that is *not* in the template enters as
  `status: candidate` with `in_template: false` and **must be flagged for
  review** in `system/reviews/register.md` — it only gets a real template
  number when a human approves adding it to the template.
- `python3 tools/catalog.py check` enforces all of this mechanically: it fails
  on any code that drifts from the template numbering and on any candidate
  that isn't registered for review, and warns when the cost model references a
  code the template doesn't have.

## Toolchain

```
python3 tools/catalog.py seed        # sync structure from template + harvest evidence from clients/
python3 tools/catalog.py reconcile   # regenerate vs-template-report.md
python3 tools/catalog.py check       # validation (also run by tools/doctor.py)
```

## How it's used in client work

BPA scenario-mapping (step 3 of the BPA workflow in `system/instructions.md`)
starts from **this catalog**, not from the raw template text: an `unverified`
or `retired` status is a warning to double-check before promising a client that
something is standard BC. When client work confirms or refutes an entry, that
session updates the evidence here (or simply re-runs `seed`, which harvests it).

The monthly refresh is opportunistic: the **first session in a calendar month**
that touches catalog or BPA-mapping work checks `refresh-log.md`, and if the
month has no row yet, runs `/catalog-refresh`. No cron, no cloud dependency —
it works in any Claude session on this repo.
