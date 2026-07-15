# Phase 1 — Prepare

> New to this system? Read [`methodology/README.md`](README.md) first — it
> explains the six phases and every term used below.

## What this phase is

Everything before the first requirement workshop: create the client's file,
capture what we already know about them, and walk into each workshop better
prepared than the client expects. A well-run Prepare phase means the BPA phase
starts producing on day one instead of spending workshops discovering basics.

## Entry criteria

- A client (or serious prospect) with a name, an industry, and an intent to
  implement Business Central.

## What you produce

| Deliverable | Where | Done when |
|---|---|---|
| Client workspace | `clients/<client-slug>/` | copied from `clients/_template/`, slug is stable |
| Intake | `clients/<slug>/intake.md` | every field filled or explicitly marked unknown |
| Workshop briefing(s) | `clients/<slug>/bpa/briefings/` | one per planned workshop, before it happens |

## How to work

1. **Create the workspace.** Copy `clients/_template/` to
   `clients/<client-slug>/`. The template contains every folder later phases
   need — leave the ones you don't use yet alone.

2. **Fill the intake — interactively.** Tell the assistant "new client
   <name>, interview me for the intake". It asks batched questions (industry,
   size, processes, current systems, the ERP + add-on stack, constraints,
   timeline) and writes `intake.md`. The intake is the fact base every later
   recommendation argues from — a vague intake produces vague advice.

3. **Establish the stack.** Which BC version, which add-ons? If the stack
   includes an add-on without a `knowledge/addons/<addon>/` folder, the
   assistant flags it and scaffolds one from `knowledge/_templates/` — better
   to know the blind spot now than mid-BPA.

4. **Fork an industry pack if one fits.** Check `bpa/packs/` (e.g.
   `food-manufacturing`). A pack is pre-written BPA content for a vertical —
   forking it into the client's `bpa/content/` means workshops confirm and
   adjust instead of starting blank. Keep the attribution line in the file.

5. **Brief every workshop.** Before each requirement meeting, ask the
   assistant to generate a briefing (format:
   `clients/_template/bpa/briefings/README.md`): known facts, hypothesis scope
   per catalog scenario, numbered questions to ask, applicable lessons learned.
   Walk in with questions, walk out with answers.

## Your assets in this phase

| Asset | What it is for |
|---|---|
| `clients/_template/` | the blank client workspace — folders for every later phase |
| `clients/_template/intake.md` | the intake form the assistant interviews you through |
| `clients/_template/bpa/briefings/README.md` | briefing format for workshop prep |
| `bpa/packs/` | pre-written BPA content per industry vertical |
| `knowledge/erp/` + `knowledge/addons/` | what the stack can do — the assistant reads these when the stack is set |
| `knowledge/_templates/` | scaffolds for ERPs/add-ons we don't cover yet |
| `clients/_demo-bakkerij-florax/` | a complete worked example — peek at it whenever you wonder "what should this look like when done?" |

## How expertise flows in

- The **briefing generator** searches `expertise/lessons-learned.md` and past
  SDRs for the client's industry/size pattern — lessons show up as "watch out
  for X in the workshop" before you ever meet the client.
- Intake questions come from the **Required client info** lists in the
  knowledge files — you collect exactly what later decisions will need.

## Definition of done

- `intake.md` complete (or unknowns explicit) — the assistant will refuse to
  guess missing facts later, so gaps here become questions mid-BPA.
- A briefing exists for the first workshop.
- `python3 tools/check_client.py clients/<slug>` runs clean for this stage.

## Common pitfalls

- **Skipping the intake because "we'll learn it in the workshops".** The
  workshops are for *processes and requirements*; burning them on company
  basics wastes the client's key users.
- **Not forking the industry pack.** Writing sales/inventory content from
  scratch that the pack already had costs a day per domain.
- **Briefing after the workshop is scheduled for the same morning.** The
  briefing's value is that *you* choose what to ask; generate it the day before.

**Next phase:** [2 — BPA](02-bpa.md), the moment the first workshop material lands.
