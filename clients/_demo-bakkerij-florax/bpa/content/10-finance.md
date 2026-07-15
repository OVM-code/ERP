# 10. Finance

De financiële processen volgen standaard Business Central (Belgische lokalisatie:
CODA, Intervat, Intrastat). De grootste verandering zit in de crediteurenstroom: de
±250 papieren inkoopfacturen per maand worden digitaal verwerkt en goedgekeurd via
Continia Document Capture (zie domein 15).

## BS65.200 Inkoopfacturen maken
- **Invulling:** standaard
- **Requirements:** REQ-010

Inkoopfacturen komen binnen via de centrale mailbox of Peppol en worden door
Document Capture herkend en als conceptfactuur in BC geregistreerd (variant
*Inkoopfactuur maken via OCR*, BC65.200.04 — zie BS65.253). Facturen met een
inkooporder worden regel per regel gematcht met de ontvangsten; prijs- of
hoeveelheidsafwijkingen buiten de tolerantie gaan automatisch naar de goedkeuringsflow.
Kostenfacturen zonder order krijgen hun grootboekrekening via herkenningsregels per
leverancier.

## BS65.204 Inkoopfacturen boeken
- **Invulling:** standaard
- **Requirements:** REQ-010

Na goedkeuring (zie BS65.254) wordt de factuur geboekt. De betaaltermijn en
skontocondities komen van de leveranciersfiche, zodat kortingen voor snelle betaling
— die vandaag verloren gaan door de papieren doorlooptijd van drie weken — gehaald
worden. Het originele PDF-document blijft aan de geboekte factuur gekoppeld en is
vanuit de boeking raadpleegbaar (bewijsstuk voor de audit).
