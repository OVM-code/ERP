---
name: review-system
description: Guide a human through reviewing any component of the methodology (a system like "bpa" or "testing", a tool, a template, a skill, or one client artifact) and turn their feedback into applied, validated changes. Use when someone says "review X", "walk me through X", "I want to check/change how X works", or during periodic methodology reviews. Every methodology component must pass through this at least once.
---

# Review a system (or part of one) with a human

The reviewer is the expert; the assistant's job is to make reviewing *cheap*:
brief them fast, ask sharp questions, capture verdicts, draft the changes, apply
only what they approve, and leave a trail. One session = one component (or one
slice of a big one).

Usage: `/review-system <component>` — e.g. `bpa`, `testing`, `migration`,
`fgd-template`, `tools/build_quote.py`, `bpa/terminology`, `clients/_demo-…/test`.

## 1. Assemble the briefing (before asking anything)

- Resolve the component to its files: guide in `docs/`, templates in
  `clients/_template/`, tools in `tools/`, skills in `.claude/skills/`, demo
  artifacts in `clients/_demo-bakkerij-florax/`. List them with one-line roles.
- Present a **2-minute briefing**: what the component does, its place in the
  pipeline (input → output → gate), what is machine-checked vs human-judged, and
  the worked demo example. Never make the reviewer read raw files to get oriented.
- Show the review history: `system/reviews/register.md` — has this been reviewed,
  what changed last time?

## 2. Walk it — sharp questions, not "any comments?"

Go section by section (template headings / tool behaviours / pipeline steps) and
ask **specific, closed-first questions** the expert can answer fast, e.g.:
- "The defect-vs-CR triage line is: *contradicts BPA = defect, wish = CR*. Match
  how you actually triage?"
- "Baseline says a standard sales scenario costs 0.5 day to specify. Plausible?"
- "This gate blocks cutover on open high-severity defects. Too strict, too soft?"
Use AskUserQuestion for real forks (batch up to 4); free-form for everything else.
Log every verdict, including "fine as is" — approval is information.

## 3. Capture → draft → approve → apply

- Record findings as numbered suggestions with a severity (blocker / improve /
  nice-to-have) and the reviewer's words.
- Draft the concrete change for each accepted suggestion (template edit, doc edit,
  tool change, validator rule). Show diffs; the reviewer approves per item.
- Apply approved changes only. Then: run `python3 tools/check_client.py
  clients/_demo-bakkerij-florax` (and rebuild affected demos); if
  `system/instructions.md` changed, sync the Copilot copy (≤8,000 chars); update
  `Last reviewed` stamps where they exist.

## 4. Leave the trail

Append to `system/reviews/register.md` (create from the header in that file if
missing): date · component · reviewer · verdict (approved / approved-with-changes /
needs-rework) · suggestions accepted/rejected · files changed. Write the detailed
record to `system/reviews/REV-<seq>-<component>.md` using the same structure as
the session (briefing shown, questions, verdicts, changes). Commit as
`Review <component>: <verdict> (REV-<seq>)`.

## Rules

- Never bundle unreviewed extras into an applied change — the diff the reviewer
  approved is the diff that lands.
- A rejected suggestion is recorded with the reason; it is expertise.
- Big components get sliced (e.g. `bpa` → catalog / flows / viewer / workflow),
  each slice its own REV record; the register shows coverage so "every component
  reviewed by a human" is checkable, not aspirational.
