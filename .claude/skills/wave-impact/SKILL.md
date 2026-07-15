---
name: wave-impact
description: Produce a per-client Business Central release-wave impact report - diff the Microsoft release plan (and add-on release notes) against the client's in-scope scenario codes and stack, and deliver "what changes for YOU, what to test, which GAP could become standard". Use twice a year per aftercare client, or when asked about release impact.
---

# Release-wave impact report

Usage: `/wave-impact clients/<slug> [wave, e.g. "2026 wave 2"]`. Output:
`clients/<slug>/aftercare/wave-reports/<wave-slug>.md`. This is the layer-2
aftercare product — client-specific, grounded, renewable.

## Steps

1. **Scope**: read the client's coverage (in-scope codes + fits), stack versions
   (`bpa-config.json`), GAP register and manual chapter list.
2. **Fetch the release plan**: Microsoft Learn "What's new / release plans" for the
   target wave (use the Microsoft Learn tools / web search; cite URLs + retrieval
   date). Add-on notes for the client's stack (Aptean/Continia) where accessible —
   mark partner-gated items `verify with vendor`.
3. **Match**: for each release item, map to the client's in-scope scenario codes
   (via the catalog domains and BC terminology). Discard everything that doesn't
   touch their scope — the value of the report is what it leaves out.
4. **Classify each hit**:
   - `let-op` — behaviour/UI change in a process they use → what to tell users, which manual topic to update;
   - `test` — could break a flow/customisation → which TS-script to rerun;
   - `kans` — new standard feature → could it replace a GAP or workaround? (cite the GAP/FGD);
   - `terminologie` — renamed concepts → glossary + deliverable sweep.
5. **Write the report** (client language, ≤3 pages): summary table, then one short
   section per hit with the citation, the client-specific consequence, and the
   recommended action + owner. End with the proposed re-test list and manual
   review-flags — and log any glossary/knowledge edits in the usual freshness flow.
6. Validate (`check_client`), and register follow-ups as ISS/CR entries where the
   client must decide.
