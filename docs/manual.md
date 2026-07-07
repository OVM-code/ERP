# User-manual system — the client's post-go-live handbook

Same interactive deliverable as the BPA (clickable BPMN flows + doc panel), but the
content is **end-user work instructions**. Workspace: `clients/<slug>/manual/`
(template: `clients/_template/manual/`). Build:

```bash
python3 tools/build_manual.py clients/<slug>
```

## Sources and the review flag (the core mechanic)

Every topic declares its grounding in the `Bron` line:

| Bron | Colour | Meaning |
|---|---|---|
| `bpa` | blue | rewritten from the client's BPA scenario documentation |
| `docs: <url> (<BC version>)` | purple | grounded in official documentation; link + version shown to the user |
| `review` | red | **not grounded in either** — a draft/suggestion the consultant must review |

`review` topics are auto-collected into the deliverable's *Te reviewen* tab and
counted by the build and by `tools/check_client.py` — a manual ships when that list
is empty (or knowingly accepted). This is how "sections not explicitly found are
highlighted and suggested for consultant review" is enforced rather than hoped for.

## Authoring pipeline

1. **Skeleton from the BPA**: chapters = the client's BPA domains (same numbers →
   the BPMN flows attach automatically); topics = the in-scope scenarios, plus
   `MAN-xxx` general topics (login, navigation, search, personalisation).
2. **How-to from BPA content**: rewrite each scenario doc from "what we will set
   up" to "how you do it", using the client's real configuration (their locations,
   number series, roles) and the client's language/terminology (glossary!).
3. **Enrich from official docs**: for standard-BC mechanics, search Microsoft Learn
   (Copilot Studio grounding or the Microsoft Learn tools in Claude), verify against
   the client's BC version, and cite the URL in the `docs:` source. Add-on topics
   cite vendor documentation.
4. **Flag what is not found**: if neither the BPA nor official docs support a
   needed topic, still draft it — marked `review` — so the consultant reviews
   instead of the user guessing.
5. **Feed from training**: session-log parking points and recurring confusion are
   the priority list for extra topics.
6. Build, run `check_client.py`, resolve/accept review flags, deliver.
