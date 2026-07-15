# Entiteit: Artikelen — migratieworkbook

| | |
|---|---|
| BC-tabel(len) | Item (27) + Item Unit of Measure |
| Configuratiepakket | FLX-ART |
| Bron | oude ERP + receptuurlijsten kwaliteit · volume: ±640 records |
| Eigenaar (klant) | kwaliteitsverantwoordelijke |
| Status | te starten |

## 1. Veldmapping

| Bronveld | BC-veld (pakketkolom) | Transformatie / regel | Verplicht |
|---|---|---|---|
| ArtNr | No. | overnemen | ja |
| Omschrijving | Description | trim, max 100 | ja |
| Groep | Item Category Code | mapping: GRONDSTOF / VERPAKKING / DIEPVRIES-* | ja |
| Houdbaarheid (d) | Expiration Calculation | uit receptuurlijst, formaat <n>D | ja voor traceerplichtig |
| Traceerplichtig | Item Tracking Code | ja → LOT-VOLLEDIG, nee → GEEN (BPA BS50.104) | ja |
| Waardering | Costing Method | alles FIFO (BPA BS50.100) | ja |
| WebshopSKU | (frameworkvertaaltabel, niet in pakket) | apart bestand voor GAP-1 mapping | nee |

## 2. Schoningsregels

- [ ] Artikelen zonder beweging sinds 2024 niet migreren
- [ ] Elke traceerplichtige referentie heeft houdbaarheid uit de receptuurlijst
- [ ] Eenheden geharmoniseerd (ST/DOOS/KG) + omrekenfactoren gecontroleerd
- [ ] Webshop-SKU's compleet voor alle webshop-artikelen (GAP-1 aanname A4)

## 3. Validatiechecklist

- [ ] Aantallen bron = geladen; import zonder onverklaarde foutregels
- [ ] Steekproef 25 artikelen incl. houdbaarheidsformule en traceringscode
- [ ] Specifiek: géén traceerplichtig artikel met code GEEN (query op categorie vs code)
- [ ] Functioneel: ontvangst boeken op traceerplichtig artikel eist lot + berekent THT

## 4. Load-log

| Datum | Omgeving | Records bron | Records geladen | Fouten | Uitgevoerd door |
|---|---|---|---|---|---|
