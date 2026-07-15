# Training trajectory — Bakkerij Florax (demo)

| | |
|---|---|
| Status | draft |
| BPA version | 0.9 — demo |
| Environment | FLORAX-TEST (zie `../setup/environments.md`) |
| Trainingsperiode | oktober–november 2026 |

## Doelgroepen

| Groep | Rollen / personen | Domeinen |
|---|---|---|
| Verkoop binnendienst | 6 medewerkers verkoop | 2, 12 |
| Magazijn & kwaliteit | 12 magazijn + kwaliteitsverantwoordelijke | 4 |
| Finance | 5 medewerkers boekhouding | 10, 15 |

## Modules

| # | Module | Doelgroep | Scenario's | Vereist eerst | Sessies | Duur |
|---|---|---|---|---|---|---|
| M1 | Masterdata verkoop: klanten & prijslijsten | Verkoop binnendienst | BS25.101 | setup fase 2 done | S01 | 2u |
| M2 | Verkooporders: intake, toezegging, backorders | Verkoop binnendienst | BS25.202, BS25.328, BS25.206 | M1 | S02, S03 | 2×2u |
| M3 | Facturatie & verzamelfacturen | Verkoop binnendienst + Finance | BS25.213 | M2 | S04 | 2u |
| M4 | Artikelen, loten & THT | Magazijn & kwaliteit | BS50.100, BS50.104, BS45.904, BS45.902 | setup fase 3.4–3.5 done | S05, S06 | 2×2u |
| M5 | Kwaliteitsvrijgave (QC-workaround) | Magazijn & kwaliteit | BS45.200 | M4 | S07 | 1,5u |
| M6 | Inkoopfacturen digitaal (Continia) | Finance | BS65.253, BS65.254, BS65.200, BS65.204 | setup fase 3.7 done | S08 | 2u |
| M7 | Webshop- & EDI-uitval behandelen | Verkoop binnendienst | BS95.002 | M2 + setup 4.1 done | S09 | 1,5u |

## Sessieplanning

| Sessie | Module | Datum | Deelnemers | Status | Prep-document |
|---|---|---|---|---|---|
| S01 | M1 | 2026-10-06 | verkoop (6) | voor te bereiden | `sessions/S01-masterdata-verkoop.md` |
| S02–S09 | M2–M7 | te plannen | | te plannen | |

## Leerdoelen per go-live

- Verkoop: order in 3 kanalen verwerken, backorderbeleid per kanaal toepassen,
  uitval webshop/EDI zelfstandig oplossen.
- Magazijn/kwaliteit: lot volgen in twee richtingen (recalltest), THT-blokkades
  begrijpen, QC-vrijgave digitaal uitvoeren.
- Finance: inkoopfactuur van mailbox tot betaling zonder papier; weekfacturatie
  retail draaien.

## Gate

> Directieven van de consultant: hieronder geschreven of in chat gegeven (de
> assistent registreert ze hier, past ze toe en vinkt af met datum, bv.
> `- [x] kolom X toegevoegd (toegepast 2026-07-09)`). De Status in de kop van
> dit document is de poort; goedkeuren kan alleen zonder open directieven.
> Regels: `docs/gates.md`.

**Directieven**

*(geen open directieven)*
