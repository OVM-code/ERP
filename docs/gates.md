# Gates — human input between every pipeline step

Every step in the delivery pipeline ends at a **gate**: the assistant produces
the step's output and stops; the consultant reviews it, optionally steers it
with **directives**, and only their explicit approval opens the next step. The
output of step N — as corrected by the directives — is the input of step N+1.
`tools/check_client.py` enforces all of it mechanically.

## The gate block

Every gated artifact carries a `## Gate` section:

```markdown
## Gate

| | |
|---|---|
| Status | draft <!-- draft / in review / approved --> |
| Goedgekeurd door | — |
| Datum | — |

**Directieven**

- [ ] verzendkosten-scenario ook opnemen voor de webshopstroom
- [x] REQ-004 prioriteit verhoogd naar must (toegepast 2026-05-20)
```

- **Status** `draft` → `in review` (assistant done, awaiting the consultant) →
  `approved` (consultant's explicit decision — the assistant never sets this
  itself).
- **Directives** are the consultant's change instructions. Write them in the
  file, or just say them in chat — the assistant records them in the block,
  applies them to the artifact, and ticks them off with a date. That keeps a
  full audit trail of *what the human changed between steps* at zero extra
  process cost.
- Artifacts that already had a `| Status |` header (setup plan, test plan,
  migration plan, trajectory, FGD, TGD) keep it — their `## Gate` section only
  holds the directives.

## The gate chain

| # | Gate (carrier) | Approval unlocks |
|---|---|---|
| 1 | Requirements — `bpa/requirements.md` | scenario-mapping (`coverage.md`) |
| 2 | Scope — `bpa/coverage.md` | content enrichment (`content/`) |
| 3 | BPA sign-off — `bpa/approval.md` (client + consultant, on the built HTML/PDF) | setup plan · FGD's · definitive quote |
| 4 | Setup plan — `setup/setup-plan.md` | migration · test |
| 5 | FGD per GAP — `gaps/FGD-GAP-x.md` | its TGD (existing, machine-enforced) |
| 6 | TGD per GAP — `gaps/TGD-GAP-x.md` | its AL scaffold (existing) |
| 7 | Migration plan — `migration/migration-plan.md` | checkpoint sign-offs CP1–CP3 |
| 8 | Test plan/exit — `test/test-plan.md` | training · manual authoring |
| 9 | Trajectory — `training/trajectory.md` | session delivery |
| 10 | Manual sign-off — `manual/approval.md` | aftercare registration (first ISS/CR) |

## What the checker enforces

- **Order**: step N+1 artifacts existing while gate N is not `approved` → error
  (e.g. `content/` files while the scope gate is `in review`).
- **No approval with open directives**: `approved` + any unchecked `- [ ]` in
  the Gate section → error. Apply or withdraw them first.
- **Visibility**: every run prints one line with all gate statuses and the
  total open directives — that line is the consultant's to-do list.

## How to work a gate (user-friendly + cost-efficient)

1. The assistant finishes a step, sets the gate to `in review`, and tells you
   what to look at (with the built artifact or a summary — not a wall of text).
2. You react in chat: *"approve"*, or *"change X, drop Y, then it's fine"*.
3. The assistant records your remarks as directives, applies them **to that
   artifact only** (no pipeline-wide rework), ticks them off, and asks again.
4. On your approval it fills in Status/name/date and moves to the next step.

Ask at any time: **"which gates are open for client X?"** — the assistant reads
the check output and lists what awaits your input. Directives are deliberately
small and local: correcting step N's output at its gate costs a targeted edit,
instead of discovering the issue two stages later and reworking everything in
between.
