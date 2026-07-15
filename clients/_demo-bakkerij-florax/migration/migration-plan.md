# Migration plan — Bakkerij Florax (demo)

| | |
|---|---|
| Status | in review |
| Aanpak | client-run na RapidStart-training (`rapidstart-training.md`) |
| Omgeving | trial loads in FLORAX-TEST, final load in FLORAX-PROD bij cutover |
| Client data-owner | office manager (eindverantwoordelijk), per entiteit zie tabel |

## Entiteitenscope

| # | Entiteit | Bron | Volume | Eigenaar (klant) | Workbook | Status |
|---|---|---|---|---|---|---|
| 1 | Klanten | oude ERP + Excel-prijsafspraken | ±420 | verkoop binnendienst | `entities/klanten.md` | te starten |
| 2 | Artikelen | oude ERP + receptuurlijsten | ±640 | kwaliteitsverantwoordelijke | `entities/artikelen.md` | te starten |
| 3 | Openstaande posten | oude boekhouding | ±380 posten | hoofdboekhouder | `entities/openstaande-posten.md` | te starten |

## Consultant-checkpoints (de drie gates)

| Gate | Wanneer | Wat de consultant controleert | Resultaat |
|---|---|---|---|
| CP1 — Readiness | na mapping + schoning per entiteit | mapping compleet, kwaliteitsregels toegepast, volumes plausibel | go voor trial load |
| CP2 — Trial review | na trial load in FLORAX-TEST | validatiechecklists groen; steekproef; testfase draait op deze data | go voor testfase |
| CP3 — Cutover | final load in FLORAX-PROD | validatie herhaald; openstaande posten gereconcilieerd met oude boekhouding | sign-off, go-live |

## Log

| Datum | Gebeurtenis | Wie | Opmerkingen |
|---|---|---|---|
| 2026-09-15 | RapidStart-training gepland | consultant | zie rapidstart-training.md |

## Gate

> Directieven van de consultant: hieronder geschreven of in chat gegeven (de
> assistent registreert ze hier, past ze toe en vinkt af met datum, bv.
> `- [x] kolom X toegevoegd (toegepast 2026-07-09)`). De Status in de kop van
> dit document is de poort; goedkeuren kan alleen zonder open directieven.
> Regels: `docs/gates.md`.

**Directieven**

*(geen open directieven)*
