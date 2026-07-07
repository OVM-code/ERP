# Migration plan — <Client name>

> Model: **the client migrates their own data** after an initial RapidStart
> (configuration packages) training. The consultant's value is the guardrails:
> entity workbooks, validation checklists, and three billable checkpoints — not
> typing data. Guide: `docs/migration.md`.

| | |
|---|---|
| Status | draft <!-- draft / in review / approved --> |
| Aanpak | client-run na RapidStart-training (`rapidstart-training.md`) |
| Omgeving | trial loads in <TEST>, final load in <PROD> tijdens cutover |
| Client data-owner | <naam — één eindverantwoordelijke aan klantzijde> |

## Entiteitenscope

> Volgorde = laadvolgorde (afhankelijkheden). Elke entiteit heeft een workbook in
> `entities/` — de validator controleert dat.

| # | Entiteit | Bron | Volume | Eigenaar (klant) | Workbook | Status |
|---|---|---|---|---|---|---|
| 1 | <bv. Klanten> | <legacy systeem/Excel> | | | `entities/klanten.md` | te starten |
| 2 | <Leveranciers> | | | | | te starten |
| 3 | <Artikelen> | | | | | te starten |
| 4 | <Openstaande posten> | | | | | te starten |

Statuswaarden: `te starten` → `mapping klaar` → `data geschoond` → `trial geladen`
→ `gevalideerd` → `final geladen`.

## Consultant-checkpoints (de drie gates)

| Gate | Wanneer | Wat de consultant controleert | Resultaat |
|---|---|---|---|
| CP1 — Readiness | na mapping + schoning per entiteit | mapping compleet, kwaliteitsregels toegepast, volumes plausibel | go voor trial load |
| CP2 — Trial review | na trial load in TEST | validatiechecklists per entiteit uitgevoerd en groen; steekproef; reconciliatie | go voor testfase (testscripts draaien op deze data) |
| CP3 — Cutover | final load in PROD | herhaalde validatie + reconciliatie openstaande posten met de oude boekhouding | sign-off, go-live |

## Log

| Datum | Gebeurtenis | Wie | Opmerkingen |
|---|---|---|---|
