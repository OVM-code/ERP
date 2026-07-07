# Training system — trajectory + session prep

Two artifacts under `clients/<slug>/training/` (templates in
`clients/_template/training/`):

1. **`trajectory.md`** — the map: target groups (from the BPA lanes + intake user
   counts), modules (coherent scenario packages per group), sequence (master data →
   transactions → periodic tasks; a module's *Vereist eerst* column enforces it),
   and the session calendar.
2. **`sessions/S##-<slug>.md`** — per-session prep: environment checklist tied to
   setup-plan step numbers, a demo script that walks the BPMN flow scenario by
   scenario, self-checking exercises per learning goal, decisions to confirm, and a
   post-session log.

## How the assistant derives them

- **Modules from coverage**: group the client's in-scope scenarios per domain and
  target group; scenario docs in the BPA are the course material — training never
  invents process content, it teaches the BPA.
- **Order from data dependencies**: the same logic as the setup plan (you cannot
  train sales orders before items and customers exist).
- **Session prep from the setup plan**: the checklist references the setup-plan
  steps that must be `done`; the validator warns when a session references
  scenarios outside the client's BPA scope.
- **Exercises from learning goals**: one exercise per goal, with concrete start
  data and an expected result the participant can verify alone.
- The interactive BPA (and later the manual) is the handout: participants click
  through the same flow the trainer demonstrates.

## Timing in the project

Trajectory drafted right after the setup plan is approved (it needs the same
dependency insight); each session prep finalised ~1 week before the session, after
checking the actual environment state. Session logs feed: parking-lot items → next
session prep, recurring confusion → manual review flags, decisions → SDRs.
