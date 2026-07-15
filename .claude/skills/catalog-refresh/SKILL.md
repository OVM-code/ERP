---
name: catalog-refresh
description: Monthly refresh of the Business Process Catalog (bpa/catalog/) - verify entries against official sources, harvest new client evidence, regenerate the template-challenge report, and draft template corrections for human review. Use when a new calendar month has no row in bpa/catalog/refresh-log.md yet, or when asked to "refresh the catalog", "verify the catalog", or "challenge the template".
---

# Catalog refresh — keep the evidence base honest

Usage: `/catalog-refresh [domain numbers]`. Throttled to **once per calendar
month**: check `bpa/catalog/refresh-log.md` first — if a row for the current
month exists, report that and stop (unless the consultant explicitly overrides).

Works on any Claude plan/model in a plain session: no cron, no cloud triggers.
Budget guidance: the mechanical steps (1, 5, 6) suit any model; step 3's
judgement calls benefit from the strongest available (`system/model-guide.md`).

## Steps

1. **Sync + harvest.** Run `python3 tools/catalog.py seed`. This syncs the
   structure from `bpa/template/catalog.json` and harvests evidence from every
   client workspace, SDR and lesson. Note what changed (new evidence, newly
   verified entries).

2. **Pick the verification slice.** 500+ entries can't all be web-verified
   monthly. Verify, in this order, until ~30–50 entries are covered:
   - entries flagged **stale** in `bpa/catalog/vs-template-report.md`;
   - **unverified** entries in domains that active clients have in scope
     (check `clients/*/bpa/coverage.md`);
   - domains named in the invocation, if any;
   - the unverified domain with the most entries, round-robin over months.

3. **Verify against official sources.** For the slice: search Microsoft Learn
   (Business Central docs + "what's new" release plans) and, for add-on entries,
   the vendor's release notes. Per entry decide:
   - **confirmed** → `status: verified`, `last_verified: <this month>`, append
     evidence `docs:<url>` (the next `seed` derives the scenario's specific
     `doc_url` from it, upgrading the topic-level link);
   - **changed** (renamed, moved, behaves differently) → keep/flag status, write
     the finding in `notes`, and draft the matching `bpa/template/domains/`
     correction (step 6);
   - **no longer achievable in standard BC** → `status: retired`, `notes` says
     why + since which release;
   - **missing from the template** (a standard BC process consultants would
     document, found while researching) → add as `status: candidate` with
     `in_template: false` and the source as evidence. **Numbering rule:** the
     template numbering is the master (the cost model keys on it) — never
     reuse or renumber an existing template code. Give the candidate a
     provisional code in the template's scheme that does not clash, and
     **register it in `system/reviews/register.md`** in the same session —
     `catalog.py check` fails on unregistered candidates. It becomes a real
     template code only after reviewer approval.
   Never mark verified from memory — only from a source you actually consulted.

4. **Update the catalog.** Apply step 3's decisions to
   `bpa/catalog/catalog.json` (edit the JSON directly; keep it valid — run
   `python3 tools/catalog.py check`).

5. **Regenerate the challenge report.** `python3 tools/catalog.py reconcile`.
   Summarise the movement for the consultant: newly verified, newly stale,
   candidates, retirements.

6. **Draft template changes — never apply them.** For every *changed* /
   *retired* / *candidate* finding, draft the edit to the affected
   `bpa/template/domains/*.md` (small and targeted) and register it for human
   review via the `/review-system` flow (`system/reviews/register.md`). The
   template only changes after reviewer approval.

7. **Log + commit.** Append a row to `bpa/catalog/refresh-log.md` (month, scope,
   sources, result, entries touched). Commit: `Catalog refresh <YYYY-MM>`.

## No web access?

Do steps 1, 5 and 7 (harvest-only refresh), log "no web access — evidence
harvest only", and tell the consultant which slice still needs verification.
