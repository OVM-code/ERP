# Phase 2 — BPA (Business Process Analysis)

> New to this system? Read [`methodology/README.md`](README.md) first.
> Deep-dive on the mechanics: [`docs/bpa.md`](../docs/bpa.md).

## What this phase is

The analysis phase. Workshop material (transcripts, notes) becomes the **BPA**:
one interactive HTML document showing the client's business processes as
clickable BPMN diagrams, where every step opens the documentation of how that
process will work — standard BC, add-on, workaround, or customisation (GAP).
The client signs this document; everything built later traces back to it. It
also carries the commercial consequence: scope → quote.

## Entry criteria

- Phase 1 done: intake filled, workshop briefings used.
- At least one workshop's material in `clients/<slug>/bpa/inputs/` (text only —
  transcribe recordings first).

## What you produce

| Deliverable | Where | Done when |
|---|---|---|
| Requirements register | `bpa/requirements.md` | every `REQ-xxx` has a literal quote + source citation |
| Scope matrix | `bpa/coverage.md` | every relevant scenario explicitly in or out, with reason |
| Client-specific content | `bpa/content/NN-<domain>.md` | every in-scope scenario documented with its *Invulling* |
| GAP register | `bpa/gaps.md` | every customisation described as a `GAP-x` block |
| Adapted process flows | `bpa/processes/` | only where the client deviates from the standard flows |
| **The BPA deliverable** | `bpa/output/BPA-<slug>.html` | builds with zero warnings; client-ready (PDF export built in) |
| Setup Decision Records | `decisions/SDR-*.md` | one per decision that surfaced (e.g. add-on vs workaround) |
| Quote annex | `commercial/quote-annex.md` | generated from coverage via `tools/build_quote.py` |

## How to work

The assistant drives; you feed it material and decide. Per workshop cycle:

1. **Drop the material** in `bpa/inputs/` (`YYYY-MM-DD-<topic>-<type>.md`).
2. **"Process the inputs"** — the assistant extracts `REQ-xxx` blocks with
   literal quotes and source citations, and batches its open questions to you
   instead of guessing.
3. **Map to scenarios** — requirements are matched against the **Business
   Process Catalog** (`bpa/catalog/`): the evidence-based register of what is
   achievable in standard BC. Catalog status matters: `verified` is safe to
   promise, `unverified` gets double-checked first, `retired` is not promised
   at all. Scope lands in `coverage.md`. *(First session in a new month: the
   assistant offers `/catalog-refresh` — say yes unless you're in a hurry.)*
4. **Enrich** — per in-scope scenario the assistant drafts client-specific
   content and argues the *Invulling* (`standaard` / `add-on` / `workaround` /
   `gap`) using the advisory workflow: options, arguments from intake facts,
   lessons learned cited. **You choose**; the choice becomes an SDR.
5. **Adapt flows** where the client's process differs from the standard BPMN.
6. **Build & check:**

   ```bash
   python3 tools/build_bpa.py clients/<slug>
   python3 tools/check_client.py clients/<slug>
   ```

   Fix every warning — they are review items, not noise. Open the HTML, click
   through, use **Export PDF** for the version you send ahead of sign-off.
7. **Quote** — once coverage stabilises: `python3 tools/build_quote.py
   clients/<slug>` prices the scope from `pricing/effort-baselines.json`.

## Your assets in this phase

| Asset | What it is for |
|---|---|
| `bpa/catalog/` | evidence per scenario — your mapping starts here (`bpa/catalog/README.md`) |
| `bpa/template/domains/` | the Cegeka Process Model text — wording source for content |
| `bpa/processes/*.process.json` | standard BPMN flows per domain (bilingual) |
| `bpa/terminology/bc-terms.json` | official BC terms per language — never invent terminology |
| `bpa/viewer/` + `bpa/branding/` | the interactive viewer and Cegeka identity, inlined at build |
| `tools/build_bpa.py` / `check_client.py` / `build_quote.py` | build · quality gate · quote |
| `clients/_template/bpa/` | READMEs describing every file's format |
| `clients/_demo-bakkerij-florax/bpa/` | worked example of all of the above |

## How expertise flows in

- **Step 3** uses the catalog's evidence (which real clients run this scenario,
  when it was last verified against official docs).
- **Step 4** is the advisory workflow from `system/instructions.md`: knowledge
  files for options, `expertise/lessons-learned.md` + past SDRs for arguments —
  cited as `LL-…`/`SDR-…`, never revealing another client's identity.
- Every confirmed choice becomes an **SDR**, which is how this project pays the
  expertise forward.

## Definition of done

- BPA builds with **zero warnings**; `check_client.py` clean.
- Every in-scope scenario has content and an argued *Invulling*; every GAP has
  a `GAP-x` block; every requirement traces to scenarios or an explicit
  out-of-scope row.
- SDRs recorded for the decisions taken; quote annex generated.
- Client sign-off on the BPA (the PDF export is the formal version).

## Common pitfalls

- **Documenting from memory instead of the catalog/knowledge files** — if the
  catalog says `unverified`, check before promising.
- **Letting "Invulling" default to `standaard` silently.** It is a setup
  recommendation and needs the advisory argumentation — that's what the client
  is paying a consultant for.
- **Skipping SDRs because the BPA already says what was chosen.** The BPA says
  *what*, the SDR says *why and what else was considered* — the system learns
  from the second one.
- **Building once at the end.** Build after every enrichment session; warnings
  point at real inconsistencies while they're still cheap to fix.

**Next phase:** [3 — SDB](03-sdb.md) once the client signs the BPA.
