# S01 — Masterdata verkoop: klanten & prijslijsten (sessievoorbereiding)

| | |
|---|---|
| Module / trajectory | M1 — zie `../trajectory.md` |
| Doelgroep & deelnemers | Verkoop binnendienst (6) |
| Duur / datum / locatie | 2u / 2026-10-06 / Florax, opleidingslokaal |
| Omgeving | FLORAX-TEST — bedrijf FLORAX |
| Status | voor te bereiden |

## 1. Leerdoelen

Na deze sessie kunnen deelnemers: (a) een klant aanmaken met de juiste
klantgroep en verzendadvies; (b) een klantprijslijst lezen en een prijs
aanpassen; (c) een promoperiode ingeven die op de juiste datums voorrang krijgt.

## 2. Voor te bereiden (checklist consultant)

- [ ] Setup-plan stappen 2.3 en 3.1 `done` in FLORAX-TEST
- [ ] Testdata: klanten DEMO-RETAIL-A (retail, verzamelfactuur), DEMO-BAKKER-01
      (webshopprofiel); artikelen 10 st uit categorie DIEPVRIES-CROISS
- [ ] Prijslijst PL-DEMO met basisprijzen + promoregel "WK41" (−15%, 05–11 okt)
- [ ] Gebruikersaccounts met rol Verkoop voor alle 6 deelnemers getest
- [ ] Interactieve BPA (domein 2) klaar om te delen; beamer-script §3 doorlopen

## 3. Te doorlopen processen (demo-script)

| # | Scenario | Wat tonen / vertellen | Let op |
|---|---|---|---|
| 1 | BS25.101 | Prijslijst PL-DEMO openen; hoe BC de prijs kiest op orderdatum; promoregel WK41 laten "winnen" | promo's vervangen het Excel-bestand — benoem het expliciet |
| 2 | BS25.101 | Prijs wijzigen met ingangsdatum; concept vs actief | wie mag activeren = teamlead |
| 3 | BS25.202 | Kort vooruitblikken: order DEMO-BAKKER-01 pakt automatisch de juiste prijs | volledige orderflow = S02 |

## 4. Oefeningen

| # | Opdracht | Startdata | Verwacht resultaat |
|---|---|---|---|
| O1 | Maak klant "Bakkerij Test-<jouw naam>" aan met webshopprofiel | klantsjabloon WEBSHOP | verzendadvies = deellevering, betalingsconditie 30 dgn |
| O2 | Geef promoprijs −10% op artikel 10001 voor volgende week | PL-DEMO | order met leverdatum volgende week toont de actieprijs; deze week de basisprijs |
| O3 | Controleer welke prijs een order van 12 okt krijgt (na promo WK41) | PL-DEMO | basisprijs — promo verlopen |

## 5. Te bevestigen beslissingen

- Wie beheert prijslijsten na go-live (teamlead verkoop of finance)? → SDR na
  bevestiging.

## Logboek (na de sessie)

- Aanwezig: | Behandeld t/m: | Parkeerpunten: | Huiswerk: | Opvolging:
