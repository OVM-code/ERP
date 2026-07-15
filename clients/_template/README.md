# Client workspace template

Copy this folder to `clients/<client-slug>/` for a new client. One workspace per
delivery-pipeline stage; each stage has a guide in `docs/` and is checked by
`python3 tools/check_client.py clients/<client-slug>`.

| Folder / file | Stage | Guide |
|---|---|---|
| `intake.md` | client profile — feeds every stage | `system/instructions.md` |
| `decisions/` | Setup Decision Records (the *why* of every choice) | `system/instructions.md` |
| `bpa/` | Business Process Analysis (interactive BPMN deliverable) | `docs/bpa.md` |
| `setup/` | BC environment setup plan derived from the BPA | `docs/setup.md` |
| `gaps/` | FGD → human review → TGD per GAP | `docs/gap-designs.md` |
| `migration/` | client-run data migration: entity workbooks + RapidStart training + checkpoints | `docs/migration.md` |
| `test/` | UAT: generated scripts, defect register, acceptance gate | `docs/testing.md` |
| `training/` | training trajectory + session preps | `docs/training.md` |
| `manual/` | end-user manual (interactive, grounded or review-flagged) | `docs/manual.md` |
| `aftercare/` | issue + change-request registers (post-go-live) | `docs/aftercare.md` |

Worked demo of all stages: `clients/_demo-bakkerij-florax/`.
