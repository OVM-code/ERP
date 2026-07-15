# FGD-<GAP-id> — <title> (Functional Gap Design)

> One FGD per GAP from the client's BPA gap register. Drafted by the assistant,
> **reviewed and approved by a human** before any TGD is written. Write for the
> client's key users and project lead: functional language, concrete examples, no
> implementation detail. Guide: `docs/gap-designs.md`.

| | |
|---|---|
| Client | <slug> |
| GAP | GAP-x — <title from gaps.md> |
| Requirements | REQ-…, REQ-… |
| BPA scenarios | BS…, BS… |
| Status | **draft** <!-- draft / in review / approved / rejected — machine-checked --> |
| Author / Reviewer | <assistant+consultant> / <consultant name> |
| Version / Date | 0.1 / YYYY-MM-DD |

## 1. Waarom dit maatwerk (context)

<Het requirement in klanttaal, met citaat/REQ-referentie. Wat de klant hiermee moet
kunnen dat nu niet kan.>

## 2. Waarom standaard + add-ons niet volstaan

<Welke standaardfunctionaliteit en workarounds zijn overwogen en waarom die
afvallen — verwijs naar de BPA-scenariotekst en SDR's. Dit is de bestaansreden van
de GAP; als dit hoofdstuk niet overtuigt, hoort de GAP niet te bestaan.>

## 3. Functioneel ontwerp

### 3.1 Procesverloop
<Stap voor stap hoe het proces mét het maatwerk verloopt. Wie doet wat, waar in BC.>

### 3.2 Schermen & velden
<Welke pagina's/velden erbij komen of wijzigen, functioneel beschreven ("op de
verkooporderregel komt een veld X dat …"), geen objectnummers.>

### 3.3 Bedrijfsregels
<Regels, berekeningen, valideringen — elk met een concreet rekenvoorbeeld met echte
klantdata.>

### 3.4 Rollen & rechten
<Wie mag wat.>

## 4. Randgevallen & foutafhandeling

<Wat gebeurt er bij ...? Minstens: lege/foute invoer, volumepieken, annulaties,
en wat een gebruiker ziet als het misgaat.>

## 5. Acceptatiecriteria

> Genummerd en individueel testbaar — de TGD en de test bij oplevering mappen
> hier 1-op-1 op.

| # | Criterium (gegeven / wanneer / dan) |
|---|---|
| AC-1 | |

## 6. Buiten scope

<Expliciet wat dit maatwerk NIET doet, om scope-kruip bij ontwikkeling te stoppen.>

## 7. Impact

- Licenties/kosten: | Performantie: | Integraties: | Upgrade-gevoeligheid:

## 8. Open vragen

| # | Vraag | Voor wie | Antwoord |
|---|---|---|---|

## Review log

| Datum | Reviewer | Versie | Oordeel | Opmerkingen |
|---|---|---|---|---|

## Gate

> Directieven van de consultant: hieronder geschreven of in chat gegeven (de
> assistent registreert ze hier, past ze toe en vinkt af met datum, bv.
> `- [x] kolom X toegevoegd (toegepast 2026-07-09)`). De Status in de kop van
> dit document is de poort; goedkeuren kan alleen zonder open directieven.
> Regels: `docs/gates.md`.

**Directieven**

*(geen open directieven)*
