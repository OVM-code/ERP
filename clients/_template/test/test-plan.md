# Test plan — <Client name>

> The testing stage exists to prove, **before cutover**, that the system behaves as
> the BPA promised — with the key users as testers, in their own words. Scripts are
> generated from the BPA scenario docs and FGD acceptance criteria; execution and
> defects are tracked here. Guide: `docs/testing.md`.

| | |
|---|---|
| Status | draft <!-- draft / in review / approved — machine-checked --> |
| BPA version | <version scripts were generated from> |
| Environment | <TEST env + company, from ../setup/environments.md> |
| Testers | <key users per domain, from ../training/trajectory.md doelgroepen> |

## Entry criteria (before round 1 starts)

- [ ] Setup-plan phases 0–3 `done` in the test environment
- [ ] Migration trial load completed for the entities the scripts need
- [ ] Training modules for the domains under test delivered (testers know the flows)
- [ ] All GAP builds for this round deployed (TGD test plans passed by the developer)

## Test rounds

| Ronde | Doel | Scope | Wanneer | Status |
|---|---|---|---|---|
| R1 | Scenariotests per domein door key users | alle in-scope scenario's | | te plannen |
| R2 | Ketentests (end-to-end: order → levering → factuur → betaling) | kritieke ketens | | te plannen |
| R3 | Regressie na defectfixes + cutover-simulatie | gefaalde scripts + kernketen | | te plannen |

## Exit criteria (acceptance gate — cutover go/no-go)

- [ ] 100% van de scripts uitgevoerd; geen open defects met severity hoog
- [ ] Elke FGD-acceptatiecriterium aantoonbaar getest (validator controleert dekking)
- [ ] Ketentest R2 volledig geslaagd inclusief documentoutput (facturen, Peppol/EDI)
- [ ] Sign-off key users per domein — vastgelegd in het logboek hieronder

## Sign-off log

| Domein | Key user | Datum | Oordeel | Opmerkingen |
|---|---|---|---|---|

## Gate

> Directieven van de consultant: hieronder geschreven of in chat gegeven (de
> assistent registreert ze hier, past ze toe en vinkt af met datum, bv.
> `- [x] kolom X toegevoegd (toegepast 2026-07-09)`). De Status in de kop van
> dit document is de poort; goedkeuren kan alleen zonder open directieven.
> Regels: `docs/gates.md`.

**Directieven**

*(geen open directieven)*
