# Test plan — Bakkerij Florax (demo)

| | |
|---|---|
| Status | in review |
| BPA version | 0.9 — demo |
| Environment | FLORAX-TEST — bedrijf FLORAX |
| Testers | verkoop (2), magazijn/kwaliteit (2), finance (2) — zie training/trajectory.md |

## Entry criteria (before round 1 starts)

- [ ] Setup-plan fases 0–3 `done` in FLORAX-TEST
- [ ] Migratie trial load `gevalideerd` voor klanten, artikelen (testdata = echte data)
- [ ] Modules M1–M2, M4 gegeven (testers kennen de flows)
- [ ] GAP-1 build gedeployed (TGD-testplan T-1…T-6 door developer geslaagd)

## Test rounds

| Ronde | Doel | Scope | Wanneer | Status |
|---|---|---|---|---|
| R1 | Scenariotests per domein door key users | alle 16 in-scope scenario's | nov 2026 wk 1–2 | te plannen |
| R2 | Ketentest: EDI-order → FEFO-pick → verzamelfactuur → Peppol/INVOIC | verkoop + voorraad + finance | nov 2026 wk 3 | te plannen |
| R3 | Regressie na fixes + cutover-simulatie | gefaalde scripts + kernketen | dec 2026 | te plannen |

## Exit criteria (acceptance gate — cutover go/no-go)

- [ ] 100% scripts uitgevoerd; geen open defects severity hoog
- [ ] FGD-GAP-1 AC-1 t/m AC-5 aantoonbaar getest
- [ ] R2-keten geslaagd inclusief Peppol- én INVOIC-output
- [ ] Sign-off key users per domein

## Sign-off log

| Domein | Key user | Datum | Oordeel | Opmerkingen |
|---|---|---|---|---|
