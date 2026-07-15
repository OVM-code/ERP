# Phase 3 — SDB (Solution Design & Build)

> New to this system? Read [`methodology/README.md`](README.md) first.
> Deep-dives: [`docs/setup.md`](../docs/setup.md) ·
> [`docs/gap-designs.md`](../docs/gap-designs.md) ·
> [`docs/migration.md`](../docs/migration.md).

## What this phase is

The signed BPA becomes a working system. SDB covers both the **design** and the
**build** of the solution, three tracks that run largely in parallel:

1. **Configure** — turn the BPA scope into an ordered BC configuration
   workbook and execute it in the client's environments.
2. **Customise** — design every GAP twice (functional, then technical) and
   build it as an AL extension.
3. **Migrate** — prepare the client to load their own master data after
   RapidStart training, with consultant checkpoints.

## Entry criteria

- Phase 2 done: BPA signed, zero build warnings, GAPs registered, SDRs recorded.

## What you produce

| Deliverable | Where | Done when |
|---|---|---|
| Setup plan | `setup/setup-plan.md` | status `approved`; every in-scope scenario covered or explicitly deferred |
| Environments register | `setup/environments.md` | DEV/TEST/PROD listed with versions and access |
| Environment verification | `setup/verification.md` | probes confirm the setup plan was actually executed |
| FGD per GAP | `gaps/FGD-GAP-x.md` | **human-reviewed**, status `approved` |
| TGD per GAP | `gaps/TGD-GAP-x.md` | derived only from an approved FGD; tests cover all acceptance criteria |
| AL scaffold per GAP | `gaps/al/GAP-x/` | compiles; an external developer can take it from here |
| Migration plan + entity workbooks | `migration/` | entities complete; checkpoints CP1–CP3 signed |

## How to work

**Track 1 — Configure.**
1. "Generate the setup plan" — the assistant orders every in-scope scenario
   into concrete BC configuration steps (actual page/field names from
   `knowledge/`), dependencies first.
2. Execute in the client's TEST environment; tick off steps in the plan.
3. Run the verification probes (`setup/verification.md`) — they catch the
   configured-in-the-plan-but-not-in-BC drift.

**Track 2 — Customise (per GAP, strictly in this order).**
1. **FGD** — the assistant drafts the functional design from the GAP block +
   requirements: what it must do, acceptance criteria, screens/fields.
2. **Human review** — an FGD only counts when a human set it to `approved`
   (via `/review-system`). The machine enforces this: no TGD from an
   unapproved FGD.
3. **TGD** — technical design an external developer can build without asking
   questions: objects, events, error handling, test cases covering every FGD
   acceptance criterion.
4. **AL scaffold** — generated starting code under `gaps/al/GAP-x/`.

**Track 3 — Migrate.**
1. Draft the migration plan; per entity (customers, items, open entries, …) an
   entity workbook: source, mapping, cleansing rules, who does what.
2. Deliver the **RapidStart training** (`migration/rapidstart-training.md`) —
   after it, *the client* runs their loads.
3. Sign checkpoints CP1 (mapping agreed) → CP2 (test load ok) → CP3 (final
   load verified). You verify; the client executes.

After every authoring step: `python3 tools/check_client.py clients/<slug>` —
zero errors/warnings is the bar on any model.

## Your assets in this phase

| Asset | What it is for |
|---|---|
| `clients/_template/setup/` | setup plan, environments, verification formats |
| `clients/_template/gaps/FGD-template.md` / `TGD-template.md` | the two design formats |
| `clients/_template/gaps/al/README.md` | AL scaffold conventions |
| `clients/_template/migration/` | plan, entity workbook, RapidStart training formats |
| `knowledge/erp/` + `knowledge/addons/` | the actual setup pages/fields the plan references |
| `system/stack-versions.md` | pin the client's BC/add-on versions |
| `/review-system` skill | runs the human FGD review, tracked in `system/reviews/register.md` |
| `clients/_demo-bakkerij-florax/{setup,gaps,migration}/` | worked examples incl. a full FGD→TGD→AL chain |

## How expertise flows in

- Setup-plan choices already argued in the BPA carry their SDR citations; new
  decisions that surface during configuration get **new SDRs** — SDB is where
  "revisited after 6 months" lessons are born, record them.
- FGD drafting checks past GAPs across clients: a GAP another client solved
  with a workaround or that a release wave made standard is a **cheaper
  answer** — the assistant flags it, `/wave-impact` history is the evidence.
- The freshness check (daily throttle) applies to deliverable work: a scenario
  the current BC wave changed shouldn't be configured from stale knowledge.

## Definition of done

- Gates approved ([`docs/gates.md`](../docs/gates.md)): setup plan (unlocks
  migration and test), FGD per GAP (unlocks its TGD), TGD (unlocks its AL
  scaffold), migration plan (unlocks CP sign-offs).
- Setup plan `approved` and executed; verification probes pass.
- Every GAP: FGD approved by a human → TGD complete → AL scaffold compiles.
- Migration: workbooks complete, client trained, CP1–CP3 signed.
- `check_client.py` clean across `setup/`, `gaps/`, `migration/`.

## Common pitfalls

- **Writing the TGD before the FGD is human-approved.** The tooling blocks it
  for a reason: reversing a technical design after a functional change costs
  triple.
- **Configuring beyond the plan.** Undocumented setup is invisible to testing,
  training and the manual — if you touch a setting, it goes in the plan.
- **Doing the client's migration for them.** The model is client-run for a
  reason (ownership + cost); your job is the checkpoints, not the CSV wrangling.
- **Treating verification as optional.** "Configured" and "configured as
  planned" diverge in every project; the probes exist because of that.

**Next phase:** [4 — Test](04-test.md) when configuration and built GAPs land in TEST.
