# 4. Voorraad

Volledige lottracering met THT-bewaking is voor Florax niet onderhandelbaar
(IFS-certificering, FAVV-recalltest 2×/jaar). De voorraadinrichting steunt op de
Aptean Food & Beverage-laag bovenop standaard Business Central: lot management voor
tracering en expiration management voor THT/FEFO. Waardering gebeurt volgens FIFO.

## BS50.100 Artikelen beheren
- **Invulling:** standaard

Grondstoffen, verpakkingen en eindproducten (diepvriespatisserie) worden als
artikelen aangelegd met artikelcategorieën per productgroep. Elk traceerplichtig
artikel krijgt een artikeltraceringscode (zie BS50.104) en een houdbaarheidsformule
waarmee BC de THT berekent bij productie of ontvangst. Waarderingsmethode: FIFO.

## BS50.104 Artikeltraceringscodes beheren
- **Invulling:** standaard
- **Requirements:** REQ-007

Er worden twee traceringscodes ingericht: `LOT-VOLLEDIG` (lotverplicht bij ontvangst,
verbruik, productie en verzending) voor grondstoffen en eindproducten, en `GEEN` voor
niet-traceerplichtige hulpstoffen en verpakking zonder voedselcontact. Daarmee is
elke voorraadbeweging van traceerplichtige artikelen naar lot herleidbaar — de basis
voor de recallvereiste van 4 uur.

## BS45.904 Lot management
- **Invulling:** add-on: Aptean Food & Beverage
- **Requirements:** REQ-007

De Aptean-lotmanagementlaag breidt de standaard BC-lottracering uit met de
traceringscockpit: vanuit één scherm wordt een lot in beide richtingen getraceerd —
van grondstoflot naar alle eindproductloten en afnemers (forward) en van
eindproductlot terug naar alle gebruikte grondstofloten en leveranciers (backward).
De FAVV-recalltest die vandaag een dag Excel-werk kost, wordt daarmee een rapport
van enkele minuten, ruim binnen de 4-uursvereiste.

Lotnummers worden automatisch toegekend volgens een nummerreeks per productiedatum;
leverancierslotnummers worden bij ontvangst mee geregistreerd.

## BS45.902 Expiration management
- **Invulling:** add-on: Aptean Food & Beverage
- **Requirements:** REQ-008

THT-beheer en uitleverregels:

- Elke lot krijgt bij productie/ontvangst automatisch zijn THT op basis van de
  houdbaarheidsformule van het artikel.
- Picken gebeurt **FEFO**: het lot met de kortste resthoudbaarheid eerst.
- Voor de retailketens geldt de **2/3-resthoudbaarheidsregel**: per klant(groep)
  wordt een minimale resthoudbaarheid ingesteld; loten die daar niet meer aan
  voldoen, biedt het systeem niet meer aan voor die klant en blijven beschikbaar
  voor kanalen zonder die eis.

## BS45.200 Artikelen blokkeren
- **Invulling:** workaround
- **Requirements:** REQ-009

Florax heeft geen QC-labomodule in scope. De kwaliteitsvrijgave wordt daarom
opgevangen met een afgesproken werkwijze op de standaard lotstatussen (Aptean
status management, zie BS10.904):

1. Elk productielot krijgt bij output automatisch de status **GEBLOKKEERD-QC** —
   het lot is dan niet pickbaar en niet verzendbaar.
2. Na de labo-uitslag (±4 u) zet de kwaliteitsverantwoordelijke de status digitaal
   op **VRIJGEGEVEN** (of **AFGEKEURD**, waarna afboeking of herbestemming volgt).
3. De statuswijziging wordt gelogd (gebruiker + tijdstip) — dat vervangt het
   papieren vrijgaveformulier en volstaat voor de IFS-audittrail.

De labo-uitslag zelf (meetwaarden) wordt niet in BC geregistreerd; die blijft in het
labosysteem. Enkel de beslissing (vrijgave/afkeuring) komt in BC. Als dit later
onvoldoende blijkt, is de Aptean QC-module de opstap — dat is dan een change request.
