# 4. Voorraad — testscripts

## TS-4.01 Artikel met lottracering en THT aanmaken
- **Scenario:** BS50.100, BS50.104
- **Rol/tester:** kwaliteitsverantwoordelijke
- **Startdata:** nieuw testartikel cat. DIEPVRIES-CROISS, houdbaarheid 270 dagen

| Stap | Actie | Verwacht resultaat |
|---|---|---|
| 1 | Maak artikel aan met traceringscode LOT-VOLLEDIG | lot verplicht bij elke boeking |
| 2 | Boek een ontvangst zonder lotnummer | boeking geweigerd |
| 3 | Boek met lotnummer | THT automatisch berekend (ontvangst + 270 d) |

### Uitvoeringslog
| Ronde | Datum | Tester | Resultaat | Defect |
|---|---|---|---|---|

## TS-4.02 QC-blokkering, vrijgave en recall-tracering
- **Scenario:** BS45.200, BS45.904
- **Rol/tester:** kwaliteitsverantwoordelijke
- **Startdata:** productielot LOT-TEST-01 met 2 grondstofloten

| Stap | Actie | Verwacht resultaat |
|---|---|---|
| 1 | Boek productie-output | lot krijgt status GEBLOKKEERD-QC, niet pickbaar |
| 2 | Zet status op VRIJGEGEVEN | lot pickbaar; gebruiker + tijdstip gelogd |
| 3 | Traceer LOT-TEST-01 backward en forward in de cockpit | beide grondstofloten resp. alle afnemers zichtbaar; rapport < 5 min |

### Uitvoeringslog
| Ronde | Datum | Tester | Resultaat | Defect |
|---|---|---|---|---|

## TS-4.03 FEFO en 2/3-resthoudbaarheidsregel retail
- **Scenario:** BS45.902
- **Rol/tester:** magazijn
- **Startdata:** artikel met 3 loten: THT +30 d, +120 d, +200 d (totale houdbaarheid 270 d)

| Stap | Actie | Verwacht resultaat |
|---|---|---|
| 1 | Pick voor webshopklant | lot THT +30 d gekozen (FEFO) |
| 2 | Pick voor DEMO-RETAIL-A | lot +30 d en +120 d overgeslagen (< 2/3 rest); lot +200 d gekozen |

### Uitvoeringslog
| Ronde | Datum | Tester | Resultaat | Defect |
|---|---|---|---|---|
