# Setup plan — Bakkerij Florax (demo)

| | |
|---|---|
| Status | in review |
| BPA version | 0.9 — demo |
| Environments | see `environments.md` |
| Stack | BC24 SaaS · Aptean F&B (lot/expiration) · Continia DC+DO |

## Werkwijze

- Volgorde is bindend (kolom *Afhankelijk van*). Status: `todo`/`bezig`/`done`/`nvt`.
- Elke stap implementeert het genoemde BPA-scenario; de BPA-tekst is de specificatie.
- Afwijkingen van de BPA: eerst SDR, dan uitvoeren.

## Fase 0 — Omgeving & bedrijf

| # | Stap | Scenario | BC-pagina / object | Afhankelijk van | Status | Wie | Toelichting |
|---|---|---|---|---|---|---|---|
| 0.1 | Bedrijf FLORAX aanmaken in TEST, bedrijfsgegevens invullen | BS10.001 | Companies, Company Information | — | todo | | |
| 0.2 | Aptean F&B + Continia apps installeren en licenties activeren | BS10.001 | Extension Management | 0.1 | todo | | AppSource, versies vastleggen in environments.md |

## Fase 1 — Financiële basis

| # | Stap | Scenario | BC-pagina / object | Afhankelijk van | Status | Wie | Toelichting |
|---|---|---|---|---|---|---|---|
| 1.1 | Rekeningschema en boekingsgroepen opzetten (BE-lokalisatie) | BS65.200 | Chart of Accounts, Posting Setup | 0.1 | todo | | basis voor alle domeinen |
| 1.2 | Leveranciers + betaalcondities met skonto | BS65.204 | Vendors, Payment Terms | 1.1 | todo | | skonto-condities uit BPA §10 |

## Fase 2 — Master data per domein

| # | Stap | Scenario | BC-pagina / object | Afhankelijk van | Status | Wie | Toelichting |
|---|---|---|---|---|---|---|---|
| 2.1 | Artikelcategorieën + artikelen laden (FIFO, houdbaarheidsformules) | BS50.100 | Items, Item Categories | 1.1 | todo | | configuratiepakket vanuit huidige lijst |
| 2.2 | Traceringscodes LOT-VOLLEDIG en GEEN aanmaken en toewijzen | BS50.104 | Item Tracking Codes | 2.1 | todo | | |
| 2.3 | Klanten + prijslijsten met promoperiodes | BS25.101 | Customers, Sales Price Lists | 1.1 | todo | | promoperiodes = datumbegrensde regels |

## Fase 3 — Processinstellingen & add-ons

| # | Stap | Scenario | BC-pagina / object | Afhankelijk van | Status | Wie | Toelichting |
|---|---|---|---|---|---|---|---|
| 3.1 | Verkoopinstellingen + verzendadvies per klantgroep | BS25.202, BS25.206 | Sales & Receivables Setup, Customers | 2.3 | todo | | retail = volledig, overige = deellevering |
| 3.2 | Ordertoezegging activeren | BS25.328 | Order Promising Setup | 3.1 | todo | | |
| 3.3 | Verzamelfacturatie retail (combine shipments) inrichten | BS25.213 | Customers (Combine Shipments) | 3.1 | todo | | wekelijkse batch |
| 3.4 | Aptean lot management: lotnummerreeksen + traceringscockpit | BS45.904 | Aptean F&B setup | 2.2 | todo | | recalltest uitvoeren als acceptatie |
| 3.5 | Aptean expiration management: FEFO + 2/3-resthoudbaarheid retail | BS45.902 | Aptean F&B setup | 3.4 | todo | | klantgroepregel retail |
| 3.6 | Lotstatussen GEBLOKKEERD-QC / VRIJGEGEVEN / AFGEKEURD + autoblokkering bij output | BS45.200 | Aptean status management | 3.4 | todo | | QC-workaround uit BPA §4 |
| 3.7 | Continia DC: mailbox, OCR-sjablonen, goedkeuringsflow (aankoper ≤ €5.000, daarboven zaakvoerder) | BS65.253, BS65.254 | Continia Document Capture Setup | 1.2 | todo | | Web Approval Portal activeren |
| 3.8 | Continia DO: Peppol-registratie + documentprofielen verkoopfacturen | BS65.256 | Continia Document Output Setup | 3.3 | todo | | |
| 3.9 | Retail-EDI ORDERS-mappings per keten configureren | BS95.002 | EDI framework (Partner Messages) | 3.1 | todo | | configuratiedeel; webshopdeel zie fase 4 |

## Fase 4 — Interfaces & maatwerk (na TGD-oplevering)

| # | Stap | Scenario | BC-pagina / object | Afhankelijk van | Status | Wie | Toelichting |
|---|---|---|---|---|---|---|---|
| 4.1 | Webshopkoppeling deployen + mapping/exportprofiel configureren | BS95.002 | per TGD-GAP-1 | 3.9, TGD-GAP-1 gebouwd | todo | | |
| 4.2 | Factuurlay-outs retail + INVOIC-mappings | BS25.213 | per FGD-GAP-2 (na goedkeuring) | 3.8 | todo | | FGD-GAP-2 nog in review |
| 4.3 | Inkoopfacturen boekenstroom end-to-end testen met OCR | BS65.200, BS65.204 | — | 3.7 | todo | | 20 echte facturen als testset |

## Uitgesteld

| Scenario | Reden | Herbekijken op |
|---|---|---|
