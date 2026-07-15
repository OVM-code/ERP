# 15. Continia

Continia Document Capture digitaliseert de crediteurenstroom; Document Output
verzorgt de elektronische facturatie via Peppol.

## BS65.253 Verwerken binnenkomende facturen met OCR
- **Invulling:** add-on: Continia Document Capture
- **Requirements:** REQ-010

Inkoopfacturen (PDF via de centrale mailbox, of rechtstreeks via Peppol) worden
automatisch geïmporteerd en met OCR herkend: leverancier, factuurnummer, datums,
bedragen en BTW. Per leverancier leert het sjabloon bij, zodat de herkenningsgraad
na de eerste weken hoog ligt. Na validatie registreert Document Capture het document
als niet-geboekte inkoopfactuur in BC; het originele PDF-bestand blijft gekoppeld
tot en met de geboekte factuur.

## BS65.254 Goedkeuring van documenten
- **Invulling:** add-on: Continia Document Capture
- **Requirements:** REQ-010

De goedkeuringsflow volgt de afgesproken bevoegdheden: de aankoper keurt goed tot
€5.000, daarboven gaat de factuur naar de zaakvoerder. Goedkeuren kan in BC zelf of
via de **Continia Web Approval Portal** in een webbrowser of op de smartphone —
daarmee kan de zaakvoerder ook op verplaatsing goedkeuren, met het originele
factuurbeeld op het scherm. Opmerkingen, doorsturen en in-wacht-zetten zijn
standaard mogelijk; elke stap wordt gelogd.

## BS65.256 PEPPOL
- **Invulling:** add-on: Continia Document Output
- **Requirements:** REQ-005

Alle verkoopfacturen en -creditnota's vertrekken als Peppol BIS-bericht; Continia is
zelf officiële Peppol service provider, dus er is geen aparte accesspoint-partij
nodig. Voor de retailketens blijft daarnaast het bestaande EDI INVOIC-bericht via
het integratieframework lopen (zie BS95.002 en GAP-2 voor de lay-outvereisten).
