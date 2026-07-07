# 2. Verkoop — testscripts

## TS-2.01 Manueel verkooporder met promoprijs en ordertoezegging
- **Scenario:** BS25.202, BS25.101, BS25.328
- **Rol/tester:** verkoop binnendienst
- **Startdata:** klant DEMO-BAKKER-01, artikel 10001, promo WK-TEST actief

| Stap | Actie | Verwacht resultaat |
|---|---|---|
| 1 | Maak verkooporder, leverdatum in promoweek | actieprijs op de regel |
| 2 | Wijzig leverdatum naar ná de promoweek | basisprijs op de regel |
| 3 | Open Ordertoezegging op een regel met te weinig voorraad | vroegst haalbare datum getoond, regel gemarkeerd |

### Uitvoeringslog
| Ronde | Datum | Tester | Resultaat | Defect |
|---|---|---|---|---|

## TS-2.02 Webshoporder automatisch → verkooporder (GAP-1 inbound)
- **Scenario:** BS25.202, BS95.002
- **Dekt:** FGD-GAP-1 AC-1, AC-2, AC-4
- **Rol/tester:** verkoop binnendienst
- **Startdata:** webshop-testorder WS-1001 (geldig), WS-1002 (onbekende SKU)

| Stap | Actie | Verwacht resultaat |
|---|---|---|
| 1 | Bied WS-1001 aan via de webservice | verkooporder binnen 2 min, External Document No. = WS-1001, herkomst WEBSHOP (AC-1) |
| 2 | Bied WS-1001 nogmaals aan | geen tweede order; inboxfout DUPLICATE_ORDER (AC-4) |
| 3 | Bied WS-1002 aan | geen order; inboxfout "SKU onbekend" (AC-2) |

### Uitvoeringslog
| Ronde | Datum | Tester | Resultaat | Defect |
|---|---|---|---|---|

## TS-2.03 Kanaalafhankelijk backorderbeleid en weekfacturatie
- **Scenario:** BS25.206, BS25.213
- **Rol/tester:** verkoop binnendienst + finance
- **Startdata:** DEMO-RETAIL-A (retail), DEMO-BAKKER-01 (webshopprofiel), artikel met tekort

| Stap | Actie | Verwacht resultaat |
|---|---|---|
| 1 | Verzend deellevering voor DEMO-RETAIL-A | restant geannuleerd, order administratief afgesloten |
| 2 | Verzend deellevering voor DEMO-BAKKER-01 | restant blijft als backorder openstaan |
| 3 | Draai de wekelijkse verzamelfacturatie | één factuur per keten met alle verzendingen van de week |

### Uitvoeringslog
| Ronde | Datum | Tester | Resultaat | Defect |
|---|---|---|---|---|
