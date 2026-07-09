# TGD-<GAP-id> — <title> (Technical Gap Design)

> Written ONLY from an FGD with status `approved` (machine-checked). Audience: an
> **external AL developer with zero project background** — everything needed to
> build, test and deploy correctly must be in this document. Language: English
> (developers are often not Dutch-speaking). Guide: `docs/gap-designs.md`.

| | |
|---|---|
| Client / GAP | <slug> / GAP-x |
| Source FGD | FGD-GAP-x v<version> (**approved** on YYYY-MM-DD by <reviewer>) |
| Status | **draft** <!-- draft / in review / approved — machine-checked --> |
| Target platform | <BC version + localization + relevant add-ons AND their versions> |
| Author / Reviewer | / <developer or architect> |

## 1. Project context for the developer

<3–6 sentences: who the client is, what the surrounding process does, what this
customisation adds. Then a glossary table of every project/client term used below.>

| Term | Meaning here |
|---|---|

## 2. Solution overview

<One diagram-in-words: the objects involved, what triggers what, where data flows.>

## 3. Objects

> Object numbers from the project range: <range>. Prefix: <prefix>.

| Object | Type | New/Extend | Purpose |
|---|---|---|---|
| <prefix> … | TableExtension / Table / PageExtension / Page / Codeunit / Report / Enum / XmlPort / Query | | |

## 4. Data model

<Per (extended) table: fields with type, length, captions (all client languages),
init values, keys, and which existing fields they relate to.>

## 5. Logic

<Per codeunit/trigger/event subscriber: which event (publisher object + event name),
processing steps in numbered pseudocode, and the exact posting/validation routines
called. State WHERE standard behaviour must NOT be altered.>

## 6. Integrations & error handling

<APIs/endpoints with auth method, retry/queue behaviour (job queue?), idempotency,
what is logged where, and the user-visible error texts (all client languages).>

## 7. Permissions

<Permission set(s) and which roles get them.>

## 8. Upgrade & localization considerations

<SaaS-safe: events only, no base-app modification. Data upgrade needs? Behaviour
per localization if multi-country.>

## 9. Test plan

> Must cover every FGD acceptance criterion.

| Test | Covers FGD AC | Steps | Expected result |
|---|---|---|---|
| T-1 | AC-1 | | |

## 10. Deployment

<Build pipeline/app dependencies/order, configuration after publish, and the
setup-plan step(s) (fase 4) this unlocks.>

## 11. Assumptions

<Everything assumed about the environment or data — each item is a question the
developer would otherwise have to ask.>

## Gate

> Directieven van de consultant: hieronder geschreven of in chat gegeven (de
> assistent registreert ze hier, past ze toe en vinkt af met datum, bv.
> `- [x] kolom X toegevoegd (toegepast 2026-07-09)`). De Status in de kop van
> dit document is de poort; goedkeuren kan alleen zonder open directieven.
> Regels: `docs/gates.md`.

**Directieven**

*(geen open directieven)*
