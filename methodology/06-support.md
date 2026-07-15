# Phase 6 — Support

> New to this system? Read [`methodology/README.md`](README.md) first.
> Deep-dives: [`docs/aftercare.md`](../docs/aftercare.md) ·
> [`docs/operations.md`](../docs/operations.md).

## What this phase is

Everything after go-live: issues, change requests, Microsoft's twice-yearly
release waves — **and the learning loop**. This phase has no end date and two
jobs: keep this client running well, and make sure everything this project
taught us is captured so the next project starts smarter. A methodology that
skips the second job stays as dumb as its first project.

## Entry criteria

- Phase 5 done: live client, manual delivered.

## What you produce (continuously)

| Deliverable | Where | Rhythm |
|---|---|---|
| Issue register | `aftercare/issues.md` | as issues arrive |
| Change requests | `aftercare/crs.md` | as requested; delivered only from an `approved` design |
| Wave-impact reports | `aftercare/wave-reports/` | twice a year, per BC release wave |
| SDR outcomes | `decisions/SDR-*.md` (*Outcome & review* section) | at review milestones |
| Lessons learned | `expertise/lessons-learned.md` | when the promotion rule triggers |
| Baseline calibration | `pricing/effort-baselines.json` | after harvest, from actuals |

## How to work

1. **Register everything.** Issues → `issues.md` (severity, scenario code,
   resolution); change wishes → `crs.md`. The scenario code matters — it's how
   patterns become searchable expertise.
2. **The feeding rule.** A resolved issue that changed how the client works
   feeds the **manual** (update the topic, rebuild) and, if it generalises,
   a **lesson learned**. An issue caused by a wrong setup choice reopens the
   **SDR** (outcome: revisited) — that's the honest record future projects
   need.
3. **CRs like mini-GAPs.** A CR is designed (FGD-style), human-approved,
   built, and shipped with a **BPA version bump** — the BPA stays the living
   description of the client's system, not a historical artifact.
4. **Release waves.** Twice a year run `/wave-impact clients/<slug>`: it diffs
   the Microsoft release plan (and add-on release notes) against the client's
   in-scope scenario codes — "what changes for *you*, what to test, which GAP
   could become standard". A GAP that a wave made standard is a CR to *remove*
   code — the cheapest maintenance there is.
5. **Harvest at milestones.** At go-live + each review: `/harvest
   clients/<slug>` drafts SDR outcomes, lesson-learned candidates, effort-
   baseline updates and industry-pack improvements — you approve, nothing
   auto-merges.

## Your assets in this phase

| Asset | What it is for |
|---|---|
| `clients/_template/aftercare/` | issue + CR register formats, wave-report folder |
| `/wave-impact` skill | per-client release-wave impact report |
| `/harvest` skill | the milestone knowledge harvest |
| `/catalog-refresh` skill | monthly catalog verification (release waves feed it too) |
| `tools/metrics.py` + `check_client --log` | telemetry: cycle times, defect rates per stage |
| `pricing/effort-baselines.json` | quoting improves as actuals calibrate it |
| `clients/_demo-bakkerij-florax/aftercare/` | worked example |

## How expertise flows in — and out

This phase is where the expertise layer is *written*:

- **SDR outcomes** close the loop on every decision made in phases 2–3: did it
  hold? A decision that had to be revisited is the most valuable record in the
  whole system.
- **Lessons learned** are promoted by rule, not vibes: the same argument
  deciding the same way at ≥ 2 clients, or an outcome disproving a default
  recommendation. Drafted by `/harvest`, approved by you, cited forever after.
- **The catalog** gains evidence from every wave check and every issue that
  proves (or disproves) a scenario works as claimed.
- **Effort baselines** calibrate from actuals — the next quote is as good as
  this phase's bookkeeping.

## Definition of done

Never — but per cycle: registers current, wave report delivered ≤ a month after
the release plan drops, harvest run at every milestone, `check_client.py` clean.

## Common pitfalls

- **Fixing issues without registering them.** The fix helps this client once;
  the record helps every client forever.
- **Delivering CRs straight from a chat message.** No approved design, no
  build — the same gate as GAPs, deliberately.
- **Skipping the harvest because the project is "done".** The harvest *is* the
  product this repo exists for; 15 minutes per milestone.
- **Letting the BPA rot.** Every delivered CR bumps the BPA version — a client
  document that no longer matches reality is a liability at the next audit or
  upgrade.

**The loop closes:** what this phase feeds into `expertise/`, `bpa/catalog/`
and `pricing/` is exactly what [Phase 1](01-prepare.md) reads on the next
project.
