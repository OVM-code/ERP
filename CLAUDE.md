# ERP Setup Assistant

This repository IS the product: a decision-support system for an ERP functional
consultant. When working in this repo, act as the assistant defined in
`system/instructions.md` — read that file first, it governs everything.

## Quick orientation

- `system/instructions.md` — your role, workflow, and rules (single source of truth).
- `knowledge/` — what the ERP software and add-ons can do (standard + add-on layers).
- `clients/` — per-client intake, Setup Decision Records (SDRs) and BPA workspace.
- `bpa/` — BPA system: Cegeka Process Model template + scenario catalog
  (`bpa/template/catalog.json`), standard BPMN process flows, interactive viewer.
  Workflow: `docs/bpa.md`.
- `expertise/` — lessons learned across clients; consult before every recommendation.
- `copilot-studio/` — deployment kit for running this system in Microsoft Copilot Studio.
- `docs/` — how to maintain and extend the system.

## Claude-specific notes

- Use Grep to search expertise tags (e.g. `#costing`) across `clients/*/decisions/` and
  `expertise/` before recommending — this is step 4 of the workflow, don't skip it.
- You CAN write files here: create/update intakes, SDRs, and lessons directly instead of
  asking the consultant to copy-paste. Commit with clear messages when asked to save work.
- When editing `system/instructions.md`, also update `copilot-studio/agent-instructions.md`
  (condensed copy, ≤8,000 characters) so the Copilot Studio deployment stays in sync.
- New client: copy `clients/_template/` to `clients/<client-slug>/` and fill the intake
  interactively with the consultant.
- New ERP/add-on: follow `docs/adding-an-erp-or-addon.md`.
- Cloning / new instance: `python3 tools/doctor.py` is the clone health check (stdlib
  only, no Node); transfer procedure in `docs/cloning.md`.
- BPA request ("verwerk deze transcripten", "maak de BPA"): follow the pipeline in
  `docs/bpa.md` — extract requirements, map to scenario codes from
  `bpa/template/catalog.json`, enrich content per domain, then build with
  `python3 tools/build_bpa.py clients/<client-slug>` and resolve all warnings.
  Worked example: `clients/_demo-bakkerij-florax/`.
- Downstream stages (setup plan, FGD/TGD, training, manual): see the delivery
  pipeline table in `system/instructions.md` and the guide per stage in `docs/`.
  After EVERY authoring step run `python3 tools/check_client.py clients/<slug>` —
  zero errors/warnings is the definition of done. Never write a TGD unless the FGD
  status is `approved` (human gate).
- Language & terms: deliverables in the client's configured language with the exact
  BC terms from `bpa/terminology/bc-terms.json`. Versions: respect the client's
  pinned stack (`system/stack-versions.md`). Cost: `system/model-guide.md`; never
  read the 522 KB template source — use the catalog + split domain files.
