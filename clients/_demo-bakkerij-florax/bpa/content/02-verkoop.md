# 2. Verkoop

Florax verkoopt via drie kanalen: EDI-orders van twee retailketens (±60% van het
volume), de eigen webshop en manuele intake (telefoon/mail). Het verkoopproces is
daarop ingericht: geautomatiseerde orderintake waar het kan, met kanaalafhankelijke
afspraken voor deelleveringen en facturatie. Er is geen offertetraject: prijzen
liggen vast in klantprijslijsten en promoafspraken.

## BS25.101 Beheren verkoopprijzen
- **Invulling:** standaard
- **Requirements:** REQ-004

Per klant(groep) wordt een verkoopprijslijst aangelegd in Business Central. De
promoperiodes die vandaag in Excel beheerd worden, worden datumbegrensde
prijslijstregels: een actieprijs met begin- en einddatum die tijdens de promoperiode
automatisch voorrang krijgt op de basisprijs. Bij het ingeven of importeren van een
order bepaalt BC de geldige prijs op orderdatum — de foutgevoelige manuele opzoeking
vervalt.

Prijslijsten worden beheerd door de verkoopbinnendienst; een goedkeuringsdatum en
status (concept/actief) voorkomen dat onafgewerkte prijzen gebruikt worden.

## BS25.202 Verkooporders maken
- **Invulling:** standaard
- **Requirements:** REQ-001

Alle kanalen monden uit in één en hetzelfde verkooporder in Business Central:

- **EDI-retail en webshop**: orders komen automatisch binnen via het
  integratieframework (zie BS95.002) en worden als verkooporder aangemaakt met
  klant, artikelen, aantallen en gevraagde leverdatum reeds ingevuld. De
  binnendienst controleert enkel uitval (onbekend artikel, afwijkende prijs).
- **Telefoon/mail**: manuele ingave door de binnendienst; klantgegevens,
  leveradres en prijzen worden automatisch uit de klantenfiche en prijslijsten
  overgenomen.

Na volledige ingave wordt het order vrijgegeven richting magazijn. Er is geen
interne goedkeuringsflow op verkooporders: prijscontrole gebeurt vooraf via de
prijslijsten.

## BS25.328 Ordertoezegging
- **Invulling:** standaard
- **Requirements:** REQ-003

Voor de retailorders met een harde leverdatum gebruikt de binnendienst de
standaard ordertoezeggingsfunctionaliteit (order promising): bij het ingeven van de
orderregel berekent BC op basis van voorraad en geplande ontvangsten de vroegst
haalbare verzenddatum. Regels die de gevraagde leverdatum niet halen, kleuren
onmiddellijk af — vóór bevestiging aan de keten, niet pas bij het picken. Zo worden
boetes voor gemiste leverdata vermeden.

## BS25.206 Beheer van backorders
- **Invulling:** standaard
- **Requirements:** REQ-002

Het backorderbeleid verschilt per kanaal en wordt gestuurd via het veld
*Verzendadvies* op de klantenfiche:

- **Retailketens** — geen backorders: wat bij verzending niet mee kan, wordt op het
  order geannuleerd zodat het order administratief afgesloten wordt en de keten een
  correcte pakbon krijgt. De binnendienst verwittigt de keten vóór levering.
- **Webshop- en telefoonklanten** — restsaldo blijft als backorder openstaan en
  wordt automatisch mee opgenomen in de eerstvolgende picking zodra er voorraad is.

## BS25.213 Verkoopfacturen maken
- **Invulling:** standaard
- **Requirements:** REQ-005

Facturatie volgt twee ritmes:

- **Retailketens**: wekelijks een verzamelfactuur per keten. De geboekte
  verzendingen van de week worden via *Verzamelfacturen* (gecombineerde
  verzendingen) op één verkoopfactuur samengebracht.
- **Overige klanten**: factuur per levering, automatisch aangemaakt bij het boeken
  van de verzending.

Alle verkoopfacturen vertrekken elektronisch via Peppol (zie BS65.256); de
retailketens ontvangen daarnaast hun vertrouwde EDI INVOIC-bericht. De specifieke
lay-outvereisten van de ketens zijn opgenomen in het GAP-register (GAP-2).
