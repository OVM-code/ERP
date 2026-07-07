# BPA workspace — <Client name>

This folder turns requirement-meeting material into the client-facing **Business
Process Analysis**: an interactive HTML deliverable with clickable BPMN process
diagrams, where every process step opens the documentation of that business scenario.

Full workflow guide: [`docs/bpa.md`](../../../docs/bpa.md) · Scenario catalog:
[`bpa/template/catalog.json`](../../../bpa/template/catalog.json)

## Files

| File | What it is | Produced in step |
|---|---|---|
| `inputs/` | Meeting transcripts, notes, follow-up answers (text only) | 0 — collect |
| `requirements.md` | Requirements register (`REQ-xxx`) extracted from the inputs, with source traceability | 1 — extract |
| `coverage.md` | Scope matrix: every relevant scenario in/out of scope + how it is met | 2 — map |
| `content/<NN-domain>.md` | Enriched BPA documentation per domain (`## BSxx.xxx` blocks) | 3 — enrich |
| `gaps.md` | GAP register (`GAP-x`) for anything needing customisation | 3 — enrich |
| `processes/` | Client-adapted process flows (optional; standard flows from `bpa/processes/` are the fallback) | 4 — flows |
| `intro.md` | The "Inleiding" chapter of the deliverable | 5 — build |
| `bpa-config.json` | Client name, period, language, accent colour | 5 — build |
| `output/` | The built deliverable (`BPA-<client>.html`) | 5 — build |

## Build

```bash
python3 tools/build_bpa.py clients/<client-slug>
```

The output is a single self-contained HTML file — it works offline and can be shared
with the client as-is (mail, Teams, SharePoint).
