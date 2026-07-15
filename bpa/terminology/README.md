# Terminology — one wording everywhere

`bc-terms.json` is the canonical Business Central glossary for every language this
system delivers in. It exists so that a sales order is called *sales order* in the
EN BPA, the EN setup plan, the EN training material **and** the EN manual — never
"sale order", "customer order" or a half-translated Dutch term.

## Rules

1. **Deliverables follow the client's language** (`language` in the client config);
   the repository's internal docs stay English.
2. When authoring in any language, use the glossary term exactly. If a term is
   missing, add it to `bc-terms.json` first (check the actual BC UI or Microsoft
   Learn for the official wording), then use it.
3. Version-dependent terms carry a `note` (e.g. *Job* → *Project* since BC24).
   Use the term that matches the client's BC version in `bpa-config.json` → `stack`.
4. `tools/check_client.py` lints English-language client content for leftover Dutch
   glossary terms — run it before every delivery.

## Adding a language (e.g. French)

1. Add `"fr": "..."` to every term in `bc-terms.json` (source: the BC French UI).
2. Add a `fr` language pack to `LANGS` in `bpa/viewer/viewer.js` (viewer chrome).
3. Add `"fr"` labels to the standard process flows (`bpa/processes/*.process.json`,
   see `tools/translate_processes.py` for the NL→EN reference map — copy the pattern).
4. Set `"language": "fr"` in the client's config. Client content (`content/`,
   `requirements.md`, …) is authored directly in the client language.
