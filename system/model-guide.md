# Model guide — same quality on Sonnet/Opus, at the lowest cost

This system is designed so output quality comes from **structure + validation**, not
from raw model strength: explicit step-by-step pipelines, templates with required
sections, definition-of-done checklists, and mechanical validators that catch what a
model misses. Any Claude model that can follow `system/instructions.md` can run it;
the difference between models becomes *how many validator iterations* are needed, not
whether the result is right.

## Non-negotiables on ANY model

1. **Run the validators.** `python3 tools/check_client.py clients/<slug>` after every
   authoring step, and `tools/build_bpa.py --strict` before calling a deliverable
   done. Zero warnings = done; a warning is a work item, not noise.
2. **One pipeline step per session/turn.** Extract requirements, THEN map coverage,
   THEN enrich — don't do all three in one pass. Small steps keep any model accurate.
3. **Cite as you go.** Requirements cite transcript sections; content cites REQ ids;
   FGD cites GAP + REQ; TGD cites FGD. The validators check the chain — an uncited
   claim is where hallucination hides.
4. **Copy templates, don't improvise structure.** Every artifact has a template with
   required sections; missing sections are validator errors.

## Model routing (cost ↓, quality =)

| Task | Suggested tier | Why |
|---|---|---|
| Transcript → requirements extraction | Sonnet | pattern extraction with citations; validator catches misses |
| Coverage mapping (REQ → BS codes) | Sonnet | lookup against `catalog.json`; mechanical cross-check exists |
| Translations / terminology application | Sonnet | glossary-driven; lint verifies |
| BPA content enrichment, setup plan | Opus (Sonnet for simple domains) | argumentation grounded in knowledge/expertise layers |
| FGD drafting | Opus | design judgement; human review gate follows anyway |
| TGD drafting | strongest available (Opus/Fable) | must be correct for a developer with zero context |
| Training trajectory / session prep / manual how-tos | Sonnet | template-driven, grounded in existing BPA content |
| Reviews of any artifact before human review | a DIFFERENT model/session than the author | fresh eyes find author blind spots |

## Cost practices

- **Never read `bpa/template/source-cegeka-process-model-3.01.md` (522 KB).** Use
  `catalog.json` for lookups and grep the split `domains/*.md` for the one section
  you need.
- Read only the client files the current step needs; the pipeline files are designed
  to be self-contained per step.
- Let Python do mechanical work (builds, checks, splitting, translation migration) —
  a script run costs nothing and never hallucinates.
- Batch questions to the consultant (one round-trip), and batch file edits per step.
- Re-builds are free: iterate content in markdown, build once at the end of a step.
