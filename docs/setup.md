# Setup-plan system — from approved BPA to a configured BC environment

Turns a client's BPA into an ordered, dependency-aware configuration plan the
consultant executes in the client's Business Central environments. Workspace:
`clients/<slug>/setup/` (template: `clients/_template/setup/`).

## Pipeline

1. **Input**: the client's BPA (coverage + content) at an approved version, plus
   their SDRs. The BPA content per scenario is the *specification*; the setup plan
   is the *work breakdown*.
2. **Derive steps**: for every in-scope scenario, list the concrete configuration
   actions with the actual BC page/object names — from `knowledge/` (setup pages per
   decision) and, for add-ons, the add-on module files. Version-check first
   (`system/stack-versions.md`): page names move between releases.
3. **Order into phases**: 0 environments/company → 1 financial basis (posting
   groups, chart of accounts, dimensions, VAT) → 2 master data per domain →
   3 process settings & add-ons → 4 interfaces/customisations (only after the TGD
   is delivered and built). Fill *Afhankelijk van* per step — that column is what
   makes the plan executable by someone else.
4. **Gate**: consultant reviews, status → `approved`, then execution starts (TEST
   first, then PROD).
5. **Track**: step status is maintained in the plan itself; deviations from the BPA
   require an SDR before the step is executed.

## Validator rules (`tools/check_client.py`)

- Every in-scope scenario from the BPA coverage appears in a phase **or** in the
  *Uitgesteld* table with a reason.
- Every scenario code referenced in the plan exists in the catalog.
- A plan marked `approved` may not contain empty phase tables and TBD dependencies.

## Boundary (deliberate)

The plan is **consultant-executed**, not auto-applied to the tenant: setup decisions
in a live project need human judgement at execution time (existing data, licence
state, timing). Automation hooks that fit later without changing the format:
RapidStart configuration-package export per phase, and AL/API scripts per step —
both would hang off the step rows.
