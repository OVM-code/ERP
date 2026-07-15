# GAP register — Bakkerij Florax (demo)

## GAP-1 — Webshopkoppeling: orders in, voorraadstanden terug
- **Scenario's:** BS95.002
- **Requirements:** REQ-001, REQ-006
- **Inschatting:** M (mapping + exportprofiel + aanpassing webshopzijde)
- **Status:** voorgesteld

De webshop is eigen bouw en blijft behouden. Het EDI/integratieframework dekt de
berichtafhandeling (webservice, validatie, inbox/outbox, foutafhandeling), maar er
is maatwerk nodig op twee punten:

1. **Inkomend** — de webshop levert vandaag geen JSON in de structuur die het
   framework verwacht; de webshopleverancier bouwt de aanroep van de centrale
   webservice, en in BC wordt de mapping webshoporder → verkooporder geconfigureerd
   (klantidentificatie via e-mail/klantnummer, artikelmapping via webshop-SKU).
2. **Uitgaand** — een exportprofiel "beschikbare voorraad per artikel" dat elk
   kwartier naar de webshop-API publiceert, inclusief de THT-regel: enkel loten die
   nog verkoopbaar zijn tellen mee als beschikbaar.

Aannames: de webshop kan een REST-endpoint aanbieden voor de voorraadfeed; het
bestaande klant- en artikelbestand van de webshop wordt vóór go-live gealigneerd op
de BC-nummering.

## GAP-2 — Factuurlay-out en EDI INVOIC retailketens
- **Scenario's:** BS25.213
- **Requirements:** REQ-005
- **Inschatting:** S
- **Status:** voorgesteld

De twee retailketens stellen eigen eisen aan de wekelijkse verzamelfactuur: eigen
referenties (GLN, contractnummer, actiecodes) op regel- én documentniveau, en
daarnaast het EDI INVOIC-bericht in het bestaande formaat van elke keten. De
standaard factuurlay-out en de standaard Peppol-output dekken dit niet:

- aangepaste verzamelfactuurlay-out per keten (dataset-uitbreiding + lay-out), en
- twee uitgaande INVOIC-mappings in het integratieframework (per keten één),
  gevoed vanuit de geboekte verkoopfactuur.

<!-- Next ID: GAP-3 -->
