# 10. Finance & Continia — testscripts

## TS-10.01 Inkoopfactuur via OCR met goedkeuringsflow
- **Scenario:** BS65.253, BS65.254, BS65.200, BS65.204
- **Rol/tester:** finance + zaakvoerder (mobiel)
- **Startdata:** 2 test-pdf's: factuur €3.200 (≤ limiet aankoper) en €8.500 (> limiet)

| Stap | Actie | Verwacht resultaat |
|---|---|---|
| 1 | Mail beide pdf's naar de DC-mailbox | beide herkend: leverancier, bedragen, BTW correct |
| 2 | Registreer factuur €3.200 | goedkeuring bij aankoper; na akkoord boekbaar |
| 3 | Registreer factuur €8.500 | flow escaleert naar zaakvoerder; goedkeuren lukt via Web Approval Portal op smartphone |
| 4 | Boek beide facturen | pdf gekoppeld aan geboekte factuur; betaaltermijn met skonto uit leveranciersfiche |

### Uitvoeringslog
| Ronde | Datum | Tester | Resultaat | Defect |
|---|---|---|---|---|

## TS-10.02 Peppol- en INVOIC-output verkoopfactuur (GAP-2 voorbereid)
- **Scenario:** BS65.256, BS25.213
- **Rol/tester:** finance
- **Startdata:** geboekte weekfactuur DEMO-RETAIL-A uit TS-2.03

| Stap | Actie | Verwacht resultaat |
|---|---|---|
| 1 | Controleer de Peppol-verzending van de weekfactuur | BIS-bericht verstuurd, status afgeleverd |
| 2 | Controleer de INVOIC-outbox (na GAP-2-levering) | INVOIC klaargezet per keten; falen van één kanaal blokkeert het andere niet |

### Uitvoeringslog
| Ronde | Datum | Tester | Resultaat | Defect |
|---|---|---|---|---|

## TS-12.01 Voorraadfeed naar webshop (GAP-1 outbound)
- **Scenario:** BS95.002
- **Dekt:** FGD-GAP-1 AC-3, AC-5
- **Rol/tester:** applicatiebeheer
- **Startdata:** artikel uit FGD §3.3-rekenvoorbeeld (1.200/200/150/100)

| Stap | Actie | Verwacht resultaat |
|---|---|---|
| 1 | Draai de voorraadfeed | webshop ontvangt 850 voor het testartikel (AC-3) |
| 2 | Zet het webshop-endpoint tijdelijk offline en draai de feed | 3 retries, daarna foutstatus in outbox + notificatiemail (AC-5) |

### Uitvoeringslog
| Ronde | Datum | Tester | Resultaat | Defect |
|---|---|---|---|---|
