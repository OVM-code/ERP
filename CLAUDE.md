# ERP Setup Assistant

This repository IS the product: a decision-support system for an ERP functional
consultant. When working in this repo, act as the assistant defined in
`system/instructions.md` — read that file first, it governs everything.

## Quick orientation

- `system/instructions.md` — your role, workflow, and rules (single source of truth).
- `knowledge/` — what the ERP software and add-ons can do (standard + add-on layers).
- `clients/` — per-client intake and Setup Decision Records (SDRs).
- `expertise/` — lessons learned across clients; consult before every recommendation.
- `copilot-studio/` — deployment kit for running this system in Microsoft Copilot Studio.
- `docs/` — how to maintain and extend the system.
- `share/` — export kit for the shareable BC-only edition (strips Odoo + client data;
  distribution repo: `OVM-code/erp-bc`). If you edit a file the export filters
  (README, instructions, intake template, Copilot instructions, extension guide),
  the export may abort until its replacement table in `share/export-bc-edition.sh`
  is updated — that is intentional leak protection.

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
