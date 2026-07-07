# FGD-GAP-2 — Factuurlay-out en EDI INVOIC retailketens (Functional Gap Design)

| | |
|---|---|
| Client | _demo-bakkerij-florax |
| GAP | GAP-2 — Factuurlay-out en EDI INVOIC retailketens |
| Requirements | REQ-005 |
| BPA scenarios | BS25.213 |
| Status | **in review** |
| Author / Reviewer | assistant + consultant / O. Vanmalleghem |
| Version / Date | 0.2 / 2026-06-20 |

## 1. Waarom dit maatwerk (context)

> "Retail wil wekelijks een verzamelfactuur, de rest factuur per levering. En alles
> moet via Peppol kunnen tegen de mandaatdatum." (REQ-005, transcript §8)

Beide retailketens stellen keteneigen eisen aan de wekelijkse verzamelfactuur (GLN,
contractnummer en actiecodes op regel- en documentniveau) en verwachten daarnaast
hun bestaande EDI INVOIC-bericht.

## 2. Waarom standaard + add-ons niet volstaan

De standaard factuurlay-out bevat de keteneigen referentievelden niet; Continia
Document Output levert Peppol BIS (BPA BS65.256) maar niet de keten-specifieke
INVOIC-formaten. De verzamelfacturatie zelf (combine shipments) is standaard en valt
NIET onder deze GAP.

## 3. Functioneel ontwerp

### 3.1 Procesverloop
Ongewijzigd t.o.v. BPA BS25.213; enkel de output verschilt per keten: verzamelfactuur
(pdf-lay-out per keten) + INVOIC-bericht via het EDI framework, parallel aan Peppol.

### 3.2 Documenten
- Verzamelfactuurlay-out per keten: GLN koper/leveradres, ketencontractnummer,
  actiecode per regel, subtotalen per leverweek.
- INVOIC-mapping per keten vanuit de geboekte verkoopfactuur (framework outbound).

### 3.3 Bedrijfsregels
Actiecode: overgenomen van de promoprijslijstregel die de prijs bepaalde
(voorbeeld: actie "WK26-BROOD" → regelveld ActieCode = WK26-BROOD).

## 4. Randgevallen & foutafhandeling

Factuur zonder promoregel → actiecode leeg (geen fout). INVOIC-verzending faalt →
framework-outboxfout + notificatie; Peppol-verzending staat er los van.

## 5. Acceptatiecriteria

| # | Criterium |
|---|---|
| AC-1 | De weekfactuur voor keten A toont GLN, contractnummer en per regel de actiecode uit het rekenvoorbeeld. |
| AC-2 | Bij het boeken van een retailweekfactuur vertrekken Peppol-bericht én INVOIC; falen van één blokkeert de ander niet. |
| AC-3 | Facturen voor niet-retailklanten blijven de standaardlay-out gebruiken. |

## 6. Buiten scope

Wijzigingen aan de verzamelfacturatielogica zelf; creditnota-INVOIC (manueel in
fase 1).

## 7. Impact

Rapport-extensie (lay-outs) + 2 framework-mappings; SaaS-safe; onderhoud bij
ketenwijzigingen = configuratie.

## 8. Open vragen

| # | Vraag | Voor wie | Antwoord |
|---|---|---|---|
| 1 | Definitieve INVOIC-specificatie keten B (versie 2019 of 2023?) | keten B EDI-desk | uitstaand |

## Review log

| Datum | Reviewer | Versie | Oordeel | Opmerkingen |
|---|---|---|---|---|
| 2026-06-20 | O. Vanmalleghem | 0.2 | in review | wacht op INVOIC-spec keten B (open vraag 1) |
