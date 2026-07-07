# BPA — Business Process Analysis system

Shared assets for turning requirement meetings into the interactive, client-facing
BPA deliverable. Full guide: [`docs/bpa.md`](../docs/bpa.md).

| Folder | Contents |
|---|---|
| `template/` | The Cegeka Process Model 3.01: verbatim source, per-domain split (`domains/`), and the machine-readable scenario catalog (`catalog.json`) |
| `processes/` | Standard BPMN process flow definitions per domain (`*.process.json`) — the starting point every client build falls back to |
| `viewer/` | The interactive viewer (BPMN SVG renderer + documentation panel), inlined into every built deliverable |

Per-client work lives in `clients/<slug>/bpa/`; build with
`python3 tools/build_bpa.py clients/<slug>`.
