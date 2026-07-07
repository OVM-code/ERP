# FGD-GAP-1 — Webshopkoppeling: orders in, voorraadstanden terug (Functional Gap Design)

| | |
|---|---|
| Client | _demo-bakkerij-florax |
| GAP | GAP-1 — Webshopkoppeling |
| Requirements | REQ-001, REQ-006 |
| BPA scenarios | BS95.002 |
| Status | **approved** |
| Author / Reviewer | assistant + consultant / O. Vanmalleghem |
| Version / Date | 1.0 / 2026-06-18 |

## 1. Waarom dit maatwerk (context)

> "Orders moeten er automatisch in, en de webshop moet voorraadstanden terugkrijgen.
> Dat is voor ons de grootste zorg van het hele project." (REQ-006, transcript §10)

De eigen webshop blijft behouden en bedient de kleinere afnemers (±25% van het
ordervolume). Zonder koppeling worden webshoporders manueel overgetikt (foutgevoelig,
±30 orders/dag) en toont de webshop voorraad die er niet is.

## 2. Waarom standaard + add-ons niet volstaan

Het EDI/integratieframework (BPA BS95.002) levert de berichtafhandeling: webservice,
validatie, inbox/outbox, foutopvolging — dat deel is configuratie. Wat ontbreekt:
(a) de webshop spreekt de JSON-structuur van het framework niet en heeft geen
uitgaande orderfeed; (b) er bestaat geen standaard exportprofiel "verkoopbare
voorraad" dat rekening houdt met de THT-regels van de klant (BPA BS45.902): loten die
voor retail geblokkeerd zijn, tellen voor de webshop wél mee. Standaard
BC-API's (v2.0 salesOrders) zijn overwogen (SDR-kandidaat) maar afgevallen: de
webshopleverancier kan geen OAuth-clientflow implementeren binnen budget en het
framework biedt de gewenste foutopvolging in BC zelf.

## 3. Functioneel ontwerp

### 3.1 Procesverloop
1. Klant bestelt in de webshop → webshop POST het order als JSON naar de centrale
   framework-webservice (bestaand endpoint, nieuwe messagecode `WEBSHOP-ORDER`).
2. Framework valideert (klantnummer, artikel-SKU, aantallen) en maakt automatisch
   een verkooporder met herkomstkenmerk "WEBSHOP".
3. Uitval (onbekende SKU, geblokkeerde klant) verschijnt in de inbox-transacties;
   verkoop binnendienst corrigeert en herverwerkt (bestaande frameworkschermen).
4. Elk kwartier publiceert BC per artikel de **verkoopbare voorraad** naar de
   webshop-API: fysieke voorraad − geblokkeerde loten − gereserveerde aantallen.

### 3.2 Schermen & velden
- Verkooporder: bestaand veld "External Document No." = webshopordernummer;
  herkomst zichtbaar in de orderlijst (filterbaar).
- Geen nieuwe schermen voor eindgebruikers; beheer via de bestaande
  framework-pagina's (Partner Messages, Inbox/Outbox Transactions).

### 3.3 Bedrijfsregels
- Klantidentificatie: webshopklantnummer = BC-klantnummer (alignering vóór go-live,
  aanname A1 in de TGD).
- Voorraadfeed: `beschikbaar = voorraad(vestiging HOOFD) − QC-geblokkeerde loten −
  reserveringen`; loten die enkel de 2/3-retailregel schenden tellen mee.
  Rekenvoorbeeld: 1.200 st fysiek, 200 st GEBLOKKEERD-QC, 150 st gereserveerd,
  100 st enkel retail-geblokkeerd → webshop ziet **850**.
- Orders na 14:00 met leverdatum morgen krijgen leverdatum +1 werkdag (zelfde regel
  als telefonische orders, BPA BS25.202).

### 3.4 Rollen & rechten
Verkoop binnendienst: uitval behandelen. Applicatiebeheer: mappings wijzigen.

## 4. Randgevallen & foutafhandeling

- Webshop onbereikbaar bij voorraadpublicatie → outbox-retry (3×, dan foutstatus +
  dagelijkse e-mailnotificatie applicatiebeheer).
- Dubbel aangeboden webshoporder (zelfde webshopordernummer) → geweigerd met
  duidelijke inboxfout, geen duplicaatorder.
- Artikel zonder SKU-mapping → inboxfout "SKU onbekend", order NIET gedeeltelijk
  aangemaakt.
- Volumepiek (acties): 500 orders/uur moet zonder wachtrijopbouw > 15 min verwerkt
  worden.

## 5. Acceptatiecriteria

| # | Criterium (gegeven / wanneer / dan) |
|---|---|
| AC-1 | Gegeven een geldig webshoporder-JSON, wanneer het aangeboden wordt, dan bestaat binnen 2 min een verkooporder met External Document No. = webshopordernummer. |
| AC-2 | Gegeven een order met onbekende SKU, dan wordt géén verkooporder aangemaakt en toont de inbox één transactie met foutreden "SKU onbekend". |
| AC-3 | Gegeven het rekenvoorbeeld uit §3.3, dan publiceert de voorraadfeed 850 voor dat artikel. |
| AC-4 | Gegeven een tweede aanbieding van hetzelfde webshopordernummer, dan ontstaat geen tweede verkooporder. |
| AC-5 | Gegeven een offline webshop-API, dan staat het voorraadbericht na 3 retries in foutstatus en is een notificatie verstuurd. |

## 6. Buiten scope

Retour-/creditflow vanuit de webshop (manueel); klantaanmaak vanuit de webshop;
prijssynchronisatie (webshop behoudt eigen prijzen); B2C-betalingen.

## 7. Impact

- Licenties: geen extra BC-licenties; webshopleverancier bouwt aan eigen kant.
- Performantie: voorraadfeed per kwartier ≈ 400 artikelen — verwaarloosbaar.
- Integraties: raakt EDI framework-configuratie (fase 3.9) niet.
- Upgrade: enkel extension-objecten en frameworkconfiguratie (SaaS-safe).

## 8. Open vragen

| # | Vraag | Voor wie | Antwoord |
|---|---|---|---|
| 1 | Kan de webshop een REST-endpoint voor de voorraadfeed hosten? | webshopleverancier | Ja, bevestigd 2026-06-10 |

## Review log

| Datum | Reviewer | Versie | Oordeel | Opmerkingen |
|---|---|---|---|---|
| 2026-06-12 | O. Vanmalleghem | 0.2 | wijzigingen gevraagd | reservatieregel voorraadfeed verduidelijken |
| 2026-06-18 | O. Vanmalleghem | 1.0 | **approved** | |
