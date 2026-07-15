# Testing system — key-user acceptance, generated from the BPA

The testing stage proves before cutover that the environment does what the BPA
promised. The system's job is to remove the two classic failure modes: scripts that
never get written (so testing is ad-hoc clicking), and acceptance that is a feeling
instead of a record. Workspace: `clients/<slug>/test/` (template:
`clients/_template/test/`).

## Pipeline

1. **Generate scripts** (assistant): for every in-scope scenario, a `TS-` script
   derived from the BPA scenario doc (its text states the expected behaviour) and,
   for GAPs, the approved FGD acceptance criteria — each AC covered by a script.
   Start data uses the client's real master data from the migration workspace.
2. **Consultant trims** — remove artificial steps, add client-specific edge cases
   the workshops surfaced (the requirements register is the checklist).
3. **Key users execute** in rounds R1 (scenario) → R2 (end-to-end chains, incl.
   document output) → R3 (regression + cutover simulation). The scripts are
   self-checking: expected results concrete enough to verify without a consultant
   at every desk. Failures → `DEF-x`; wishes → `CR-x` (aftercare register).
4. **Acceptance gate**: exit criteria in `test-plan.md` + per-domain key-user
   sign-off. This is gate 4 of the methodology — no cutover with open high-severity
   defects or untested FGD criteria.

## Validator rules (`tools/check_client.py`)

- Every in-scope BPA scenario appears in ≥ 1 test script.
- Every acceptance criterion of every **approved** FGD is referenced by a script.
- Scripts reference only in-scope scenarios; defects reference existing scripts.
- A test plan marked `approved` with open `hoog`-severity defects is an error.

## Where the value is

Key users who tested their own process defend the system at go-live instead of
resisting it; defects surface in R1 instead of hypercare; and the sign-off log is
the contractual acceptance record when discussions arise later. Defect patterns
feed the flywheel: recurring defect themes per scenario become knowledge-base
warnings and better FGD templates.
