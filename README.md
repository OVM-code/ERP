# ERP Setup Assistant

A decision-support system for an ERP functional consultant. It knows the setup options
of the client's ERP software and add-ons, argues which options fit a specific client
and why, learns from every past decision, and runs on any LLM platform that can read
files — Claude today, Microsoft Copilot Studio as a second deployment target.

**The repository is the system.** All knowledge, client records and expertise are plain
markdown under git: no infrastructure, no running cost, fully auditable, portable.

## What it does

Ask it, on any client engagement:

> "Client X runs Business Central with Aptean lot management and catch weight. We're
> designing the warehouse. What are my options and what do you recommend?"

and it will:

1. **Check for relevant software updates first** (at most once a day per stack — see
   `system/update-check-log.md`), then enumerate **every setup option** valid for that
   exact stack (standard ERP knowledge + add-on overlays that change or extend it).
2. **Argue each option** for/against based on the client's intake facts — and tell you
   which client facts are still missing.
3. Check the **expertise layer** — past decisions (SDRs) and lessons learned (LLs) —
   and cite them where they support or contradict an option.
4. Give a recommendation with confidence level, flagging irreversible choices.
5. **Record** the confirmed decision as a new SDR, closing the learning loop.

And on top of the advisory loop it produces the **client deliverable**:

> "Here are the transcripts and notes of the requirement workshops. Build the BPA."

The BPA system turns meeting material into a **Business Process Analysis**: an
interactive HTML file with clickable BPMN process diagrams where every step opens the
documentation of that business scenario — standard Business Central, add-on (Aptean,
Continia, …), workaround, or GAP. Built on the Cegeka Process Model template, filtered
to what is relevant for the client. See [`docs/bpa.md`](docs/bpa.md) and the worked
demo in [`clients/_demo-bakkerij-florax/`](clients/_demo-bakkerij-florax/).

## Repository map

| Path | What lives there |
|---|---|
| [`system/instructions.md`](system/instructions.md) | The assistant's behaviour — single source of truth |
| [`system/update-check-log.md`](system/update-check-log.md) | Throttle log for the once-a-day software-freshness check |
| [`CLAUDE.md`](CLAUDE.md) | Activates the assistant in any Claude session on this repo |
| [`knowledge/erp/business-central/`](knowledge/erp/business-central/) | Standard BC setup decisions per functional area |
| [`knowledge/addons/aptean-food-beverage/`](knowledge/addons/aptean-food-beverage/) | How Aptean F&B changes/extends those decisions |
| [`knowledge/_templates/`](knowledge/_templates/) | Templates to add any other ERP system or add-on |
| [`clients/`](clients/) | One folder per client: intake + Setup Decision Records + BPA workspace |
| [`bpa/`](bpa/) | BPA system: Cegeka Process Model template + scenario catalog, standard BPMN flows, interactive viewer |
| [`tools/`](tools/) | `build_bpa.py` (client BPA → interactive HTML) · `split_bpa_template.py` (template → catalog) |
| [`expertise/`](expertise/) | Lessons learned across clients — consulted before every recommendation |
| [`copilot-studio/`](copilot-studio/) | Instructions + step-by-step guide to run this in Copilot Studio |
| [`docs/`](docs/) | [Maintenance routine](docs/maintenance.md) · [Adding ERPs/add-ons](docs/adding-an-erp-or-addon.md) |

## Using it

- **In Claude** (Code, desktop, or web with this repo attached): just start asking.
  `CLAUDE.md` loads the role automatically. The assistant reads and *writes* files —
  intakes, SDRs, lessons — directly.
- **In Copilot Studio / Teams:** follow [`copilot-studio/DEPLOYMENT.md`](copilot-studio/DEPLOYMENT.md)
  (~30 min one-time). Decision records come back as copy-paste blocks there.
- **New client:** copy `clients/_template/` → `clients/<client-slug>/`, then let the
  assistant interview you to fill the intake.

## Keeping it alive

Three routines, all assistant-driven: record each confirmed decision (~5 min), review
outcomes at project milestones (~15 min), refresh knowledge after software releases
(2–3×/year). Details in [`docs/maintenance.md`](docs/maintenance.md).

⚠️ This repo will contain client-related information — keep it private and put only
what setup decisions need into intakes.
