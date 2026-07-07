# Industry content packs — project #13 is cheaper than project #12

A pack is **anonymised, reusable BPA scenario documentation per vertical**. A new
client in a covered industry forks the pack instead of a blank template: the
assistant replaces placeholders with workshop facts and deletes what doesn't apply.
The knowledge curator owns pack quality; packs are updated from every finished
project (harvest step).

## Rules

- Packs contain **no client-identifying data** — placeholders in `<hoeken>`,
  patterns instead of names ("twee retailketens" → `<retailklanten>`).
- Same file format as client content (`## BSxx.xxx` blocks with `Invulling`), so
  forking is a copy + edit, and pack lint = content lint.
- **Attribution line** at the top of each forked file:
  `<!-- pack: food-manufacturing v1 -->` — this is how the reuse ratio (metrics)
  is measured.
- A pack block states its *typical* Invulling and, in comments, the fork decisions
  (`<!-- vraag: ... -->`) the consultant must answer.
- Update flow: after each project, the harvest step proposes diffs from the
  client's final content back into the pack (generalised); curator approves.

## Available packs

| Pack | Covers | Source projects | Version |
|---|---|---|---|
| `food-manufacturing/` | Verkoop, Voorraad/kwaliteit (lot/THT), Continia AP | _demo-bakkerij-florax | 1 |
