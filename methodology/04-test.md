# Phase 4 — Test

> New to this system? Read [`methodology/README.md`](README.md) first.
> Deep-dive: [`docs/testing.md`](../docs/testing.md).

## What this phase is

Key users prove, script by script, that the configured system supports their
processes. This is **UAT (User Acceptance Testing)** — not you clicking through
your own configuration, but the client's people running their daily work
against the new system and signing off per domain. It is gate 4 of the
methodology: **no cutover with open high-severity defects.**

## Entry criteria

- Phase 3 (SDB) done: setup executed and verified, GAP builds deployed to the
  TEST environment, test data present (CP2 test load is ideal for this).

## What you produce

| Deliverable | Where | Done when |
|---|---|---|
| Test plan | `test/test-plan.md` | scope, roles, environment, exit criteria agreed |
| Test scripts per domain | `test/scripts/NN-<domain>.md` | every in-scope scenario + every FGD acceptance criterion covered |
| Defect register | `test/defects.md` | every finding logged with severity and status |
| Per-domain sign-off | in the test plan | key user signature per domain |

## How to work

1. **Generate the plan and scripts.** The assistant derives test scripts
   **from the BPA + the FGD acceptance criteria** — every in-scope scenario
   becomes steps a key user can follow (real BC page names, the client's own
   cases from the workshop material). GAP tests come straight from the FGD's
   acceptance criteria, so customisations are tested against what was agreed,
   not what was built.
2. **Run the sessions.** Key users execute the scripts in TEST; you facilitate,
   they test. Every deviation goes into `test/defects.md` with a severity —
   resist fixing-on-the-spot without logging; unlogged fixes resurface in PROD.
3. **Fix and retest.** Defects route back: configuration defects → setup plan
   (SDB track 1), GAP defects → the FGD/TGD they violate. A fixed defect is
   retested by the user who found it.
4. **Gate check.** `python3 tools/check_client.py clients/<slug>` verifies
   coverage (scripts ↔ scenarios ↔ acceptance criteria) mechanically; exit
   criteria + no open high-severity defects + per-domain sign-off close the
   phase.

## Your assets in this phase

| Asset | What it is for |
|---|---|
| `clients/_template/test/` | test plan, script and defect register formats |
| `clients/<slug>/bpa/coverage.md` | the source of *what* must be tested |
| `clients/<slug>/gaps/FGD-*.md` | acceptance criteria = GAP test cases |
| `tools/check_client.py` | mechanical coverage check scripts ↔ scope |
| `clients/_demo-bakkerij-florax/test/` | worked example |

## How expertise flows in

- Script generation reuses **defect patterns from past clients** (harvested
  into lessons learned): a scenario that broke elsewhere gets an extra test
  case here.
- Defects with a lesson in them (wrong default recommended, add-on quirk) are
  flagged during `/harvest` at the phase milestone — that's how the next
  project's scripts get smarter.

## Definition of done

- Every in-scope scenario and every FGD acceptance criterion has a script, and
  every script has a result.
- Exit criteria met; **zero open high-severity defects**; per-domain sign-off
  recorded.
- `check_client.py` clean.

## Common pitfalls

- **Consultant-run "UAT".** If key users didn't run the scripts, you tested
  your own homework — sign-off means the *client* accepts.
- **Scripts written from the configuration instead of the BPA.** Then the test
  proves "the system does what the system does" — circular and worthless.
- **Severity inflation/deflation negotiations at the gate.** Severity is
  defined in the test plan *before* testing starts, precisely to avoid this.

**Next phase:** [5 — Deploy](05-deploy.md) once sign-off is complete.
