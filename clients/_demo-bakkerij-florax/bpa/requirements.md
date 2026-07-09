# Requirements register — Bakkerij Florax (demo)

> Extracted from the files in `inputs/`. Quotes keep the client's wording.

## Gate

> Menselijke poort (zie `docs/gates.md`): directieven van de consultant worden
> hier geregistreerd, toegepast en afgevinkt; daarna volgt expliciete goedkeuring.

| | |
|---|---|
| Status | approved <!-- draft / in review / approved --> |
| Goedgekeurd door | S. Willems (consultant, demo) |
| Datum | 2026-05-21 |

**Directieven**

- [x] REQ-004 prioriteit verhoogd van should naar must — promoafspraken zijn contractueel (toegepast 2026-05-20)
- [x] REQ-009 gesplitst: THT-bewaking en recall-rapportage zijn aparte requirements (toegepast 2026-05-20)


## REQ-001 — Orderintake via drie kanalen (EDI, webshop, manueel)
- **Bron:** 2026-05-12-verkoop-transcript.md §2
- **Domein(en):** 2, 12
- **Scenario's:** BS25.202, BS95.002
- **Prioriteit:** must

> "De twee retailketens sturen EDI-orders, dat is zowat 60 procent van het volume.
> Dan de webshop voor de kleinere afnemers, en de rest komt per telefoon of mail."

EDI-orders van 2 retailketens en webshoporders moeten automatisch verkooporders
worden; manuele intake blijft voor telefoon/mail.

## REQ-002 — Kanaalafhankelijk backorderbeleid
- **Bron:** 2026-05-12-verkoop-transcript.md §4
- **Domein(en):** 2
- **Scenario's:** BS25.206
- **Prioriteit:** must

> "Retail mag nooit een deellevering krijgen zonder verwittiging — wat niet mee kan,
> valt af, geen backorder. Voor webshop- en telefoonklanten houden we het saldo aan."

Retailklanten: restant annuleren bij deellevering. Overige klanten: backorder
aanhouden en naleveren.

## REQ-003 — Leverbetrouwbaarheid retail zichtbaar bij orderingave
- **Bron:** 2026-05-12-verkoop-transcript.md §5
- **Domein(en):** 2
- **Scenario's:** BS25.328
- **Prioriteit:** should

> "De retailorders hebben een leverdatum die heilig is. We willen bij het ingeven al
> zien of het haalbaar is."

Beschikbaarheids-/datumtoezegging (order promising) bij orderingave.

## REQ-004 — Klantprijslijsten met promoperiodes
- **Bron:** 2026-05-12-verkoop-transcript.md §7
- **Domein(en):** 2
- **Scenario's:** BS25.101
- **Prioriteit:** must

> "Per klant een prijslijst, en daarboven promoperiodes. Nu in Excel, foutgevoelig."

Klantspecifieke prijslijsten plus datumbegrensde actieprijzen die de basisprijs
tijdelijk overschrijven.

## REQ-005 — Facturatie: verzamelfactuur retail, Peppol voor iedereen
- **Bron:** 2026-05-12-verkoop-transcript.md §8; 2026-05-20-voorraad-finance-notes.md §6
- **Domein(en):** 2, 15
- **Scenario's:** BS25.213, BS65.256
- **Prioriteit:** must

> "Retail wil wekelijks een verzamelfactuur, de rest factuur per levering. En alles
> moet via Peppol kunnen tegen de mandaatdatum."

Wekelijkse verzamelfacturatie per retailketen; overige klanten per levering; alle
verkoopfacturen via Peppol, retail daarnaast via EDI INVOIC.

## REQ-006 — Webshopkoppeling (orders in, voorraad terug)
- **Bron:** 2026-05-12-verkoop-transcript.md §10
- **Domein(en):** 12
- **Scenario's:** BS95.002
- **Prioriteit:** must

> "Orders moeten er automatisch in, en de webshop moet voorraadstanden terugkrijgen.
> Dat is voor ons de grootste zorg van het hele project."

Tweerichtingskoppeling met de bestaande (eigen) webshop: inkomende orders,
uitgaande voorraadstanden.

## REQ-007 — Volledige lottracering met THT, recall binnen 4 uur
- **Bron:** 2026-05-20-voorraad-finance-notes.md §1
- **Domein(en):** 4
- **Scenario's:** BS45.904, BS50.104
- **Prioriteit:** must

> "Elke grondstof- en eindproductbeweging moet naar lot herleidbaar zijn, mét THT.
> Recall moet binnen 4 uur een volledige tracering opleveren."

Lottracering end-to-end (IFS + FAVV); tracering in beide richtingen op te vragen.

## REQ-008 — FEFO-uitlevering met resthoudbaarheidsregel retail
- **Bron:** 2026-05-20-voorraad-finance-notes.md §2
- **Domein(en):** 4
- **Scenario's:** BS45.902
- **Prioriteit:** must

> "Resthoudbaarheid bij levering aan retail minimaal 2/3 van de totale houdbaarheid.
> Uitleveren gebeurt FEFO."

THT-bewaking per lot; picken volgens FEFO; blokkeren van loten die de
2/3-resthoudbaarheidsregel voor retail niet meer halen.

## REQ-009 — Kwaliteitsvrijgave van productieloten
- **Bron:** 2026-05-20-voorraad-finance-notes.md §3
- **Domein(en):** 4
- **Scenario's:** BS45.200, BS10.904
- **Prioriteit:** must

> "Kwaliteit blokkeert loten na productie tot de labo-uitslag binnen is. Vrijgave nu
> op papier."

Loten na productie automatisch geblokkeerd; digitale vrijgave door kwaliteit.

## REQ-010 — Digitale verwerking en goedkeuring inkoopfacturen
- **Bron:** 2026-05-20-voorraad-finance-notes.md §4–5
- **Domein(en):** 10, 15
- **Scenario's:** BS65.253, BS65.254
- **Prioriteit:** must

> "± 250 inkoopfacturen/maand, vandaag manueel ingetikt en op papier ter goedkeuring
> rondgedragen. De zaakvoerder wil goedkeuren vanop verplaatsing."

OCR-verwerking van inkoopfacturen; goedkeuringsflow aankoper ≤ €5.000, daarboven
zaakvoerder; goedkeuren via webbrowser/mobiel.

<!-- Next ID: REQ-011 -->
