---
name: harvest
description: Run the knowledge-flywheel harvest at a project milestone (BPA approved, go-live, review). Drafts SDR outcomes, lessons-learned candidates, effort-baseline updates, industry-pack diffs and stale-claim sweeps — the human approves, nothing auto-merges. Use at any milestone, or when asked to "harvest", "capture lessons", or "update baselines".
---

# Milestone harvest — make the project feed the system

Usage: `/harvest clients/<slug> [milestone]`. Everything below is DRAFTED for
approval — present each output as a diff/block the consultant accepts or rejects.

## Steps

1. **SDR outcomes.** For each of the client's SDRs with an empty *Outcome & review*
   section: reconstruct what actually happened from the later artifacts (setup-plan
   statuses, defects, issues, CRs) and draft the outcome (held / adjusted /
   reversed + what we learned). Flag LL-candidates.
2. **Lessons learned.** Grep all clients' SDRs and issues for the promotion rule
   (same argument decided the same way at ≥2 clients, or an outcome disproving a
   default). Draft `LL-<next>` entries citing sources; never client names.
3. **Effort baselines.** Compare `pricing/effort-baselines.json` seeds against this
   project's actuals (ask the consultant for time-writing per block, or use stage
   cycle times from `tools/metrics.py` as a proxy). Propose per-code adjustments;
   bump the baselines `version` and note the calibration source.
4. **Industry pack diff.** Diff the client's final `bpa/content/` against the pack
   it was forked from (attribution line): propose generalised improvements back
   into `bpa/packs/<pack>/` (placeholders re-inserted, client facts stripped).
5. **Stale-claim sweep.** Check `system/update-check-log.md` + release notes since
   project start; grep active clients for scenario codes whose behaviour changed;
   list deliverables needing a re-check.
6. **Defect/issue patterns.** Recurring themes per scenario code → propose a
   knowledge-base warning or FGD-template improvement.

## Output

One summary block per step with the proposed edits ready to apply on approval.
Close by updating the client's log (which harvest ran, when) and — after applying —
run `tools/check_client.py` and commit with message `Harvest <slug> @ <milestone>`.
