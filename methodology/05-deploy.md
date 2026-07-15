# Phase 5 — Deploy

> New to this system? Read [`methodology/README.md`](README.md) first.
> Deep-dives: [`docs/training.md`](../docs/training.md) ·
> [`docs/manual.md`](../docs/manual.md).

## What this phase is

The system is accepted — now the organisation has to be able to run it. Deploy
covers **training** the end users, handing over the **user manual**, and the
**go-live** itself (final migration load + cutover). Success here is measured
weeks later: do users work in the system, or around it?

## Entry criteria

- Phase 4 done: UAT signed off, no open high-severity defects.
- Migration CP2 passed (test load) — CP3 (final load) lands during cutover.

## What you produce

| Deliverable | Where | Done when |
|---|---|---|
| Training trajectory | `training/trajectory.md` | sessions planned per role, tied to go-live date |
| Session preps | `training/sessions/S0x-*.md` | per session: environment prep, demo script, exercises |
| Learning packets | `training/packets/` | handout per module for the trainees |
| User manual | `manual/` → `manual/output/Manual-<slug>.html` | every topic grounded, zero `review` flags left |
| Go-live | production | CP3 signed, cutover checklist done, first live transactions verified |

## How to work

1. **Plan the trajectory.** The assistant derives it from scope + roles: who
   needs which domains, in what order, how close to go-live (train late enough
   to be remembered, early enough to recover).
2. **Prepare each session.** Per session the assistant generates: environment
   preparation steps (tied to actual setup-plan steps — the demo works because
   the config is real), a demo script in the client's own scenarios, and
   exercises. Sessions reference **only in-scope scenarios** — the checker
   enforces this; don't train what they didn't buy.
3. **Build the manual.** Like the BPA, it's one interactive HTML file
   (`python3 tools/build_manual.py clients/<slug>`), reusing the client's own
   process flows. Every topic states its source: from the BPA, from official
   docs (with URL), or flagged `review` — a flagged topic means the assistant
   could not ground it and **you** must review it before handover. Zero flags
   at delivery. PDF export works here too.
4. **Cut over.** Final data load (CP3 — client runs, you verify and sign),
   cutover checklist, verify the first real transactions against the test
   scripts of the critical path.

## Your assets in this phase

| Asset | What it is for |
|---|---|
| `clients/_template/training/` | trajectory, session prep, packet formats |
| `clients/_template/manual/` | manual workspace format (`chapters/README.md` explains grounding) |
| `tools/build_manual.py` | builds the interactive manual (Cegeka-branded, PDF export) |
| `clients/<slug>/setup/setup-plan.md` | environment prep for demos references its steps |
| `clients/<slug>/migration/` | CP3 lives here |
| `clients/_demo-bakkerij-florax/{training,manual}/` | worked examples |

## How expertise flows in

- Session preps reuse **what confused users at past clients** (lessons learned
  tagged `#training`): those topics get more exercise time.
- The manual's grounding rule is the expertise system in miniature: every claim
  traces to the BPA or official docs — the same "never improvise capabilities"
  rule the advisory workflow enforces.

## Definition of done

- Gates approved ([`docs/gates.md`](../docs/gates.md)): trajectory (unlocks
  session delivery) and **manual sign-off** (`manual/approval.md` — unlocks
  aftercare registration).
- All planned sessions delivered; packets handed out.
- Manual built with **zero ungrounded topics**; delivered to the client.
- CP3 signed; cutover checklist complete; first live transactions verified.
- `check_client.py` clean.

## Common pitfalls

- **Training in a demo environment that doesn't match PROD config.** The
  env-prep-from-setup-plan link exists to prevent exactly this.
- **Shipping the manual with `review` flags "to fix later".** A wrong manual is
  worse than no manual — users trust it exactly once.
- **Treating go-live as the finish line.** It's the starting line of the phase
  where the client actually lives — plan the first-week support before cutover.

**Next phase:** [6 — Support](06-support.md), starting the morning after go-live.
