# Migration system — client-run, consultant-guarded

The methodology's model: an initial **RapidStart training**, after which **the
client migrates their own data**. That model is right — it lowers cost and puts
data ownership where accountability belongs — but unguarded it fails predictably:
mapping ambiguity, dirty data discovered at cutover, no reconciliation trail. This
system keeps the model and adds the guardrails. Workspace: `clients/<slug>/migration/`.

## The value logic

| Who | Does | Value |
|---|---|---|
| Assistant | Generates per-entity **workbooks** (field mapping from intake/BPA + configuration-package columns, cleansing rules, validation checklists) and the RapidStart training prep | the expensive thinking, at marginal cost |
| Client | Cleans, fills, loads, validates — with self-checking checklists | lower cost, real ownership, no "your consultant typed it wrong" |
| Consultant | Three **billable checkpoints**: CP1 readiness, CP2 trial-load review, CP3 cutover sign-off | judgement where it matters; firefighting replaced by gates |

## Pipeline

1. Entity scope + load order in `migration-plan.md` (dependencies: customers before
   open entries, items before BOMs …).
2. Assistant drafts one workbook per entity from `entities/_entity-template.md`,
   using the BPA (which fields matter: item tracking codes, posting groups …) and
   the setup plan (number series, dimensions).
3. RapidStart training with the client's **own data** (`rapidstart-training.md`) —
   competence, not theory.
4. Client executes per entity: clean → trial load in TEST → validation checklist.
   Statuses tracked in the plan; the trial-loaded data is what the test stage runs on.
5. Checkpoints CP1/CP2/CP3 — consultant reviews, signs, and unblocks the next gate.
   Final load at cutover repeats the same validation + reconciliation to the old books.

## Validator rules (`tools/check_client.py`)

- Every entity in the plan's scope table has a workbook in `entities/`.
- Every workbook contains the mapping, cleansing and validation sections.
- Plan `approved` with entities still `te starten` and no dates in the log → warning.

## Flywheel

Workbook mappings for common source systems (Exact, Navision, AFAS, webshop
platforms …) are anonymised into reusable packs — the second client migrating from
the same source starts at 80%.
