# 2. Verkoop

Zo verwerkt u orders van de drie kanalen (EDI-retail, webshop, telefoon/mail) tot en
met de factuur. Het diagram bovenaan is uw proces — klik op een stap.

## BS25.202 Een verkooporder ingeven (telefoon/mail)
- **Bron:** bpa
- **Rol:** verkoop binnendienst

1. Kies **Verkooporders** en dan **Nieuw**.
2. Kies de klant in **Klantnr.** — adres, betalingscondities en prijslijst worden
   automatisch ingevuld vanuit de klantenfiche.
3. Vul de **verzochte leverdatum** in. Orders na 14:00 kunnen ten vroegste
   overmorgen geleverd worden.
4. Voeg per regel het artikel en het aantal toe; de prijs volgt uit de prijslijst
   (promoprijzen krijgen automatisch voorrang tijdens de actieperiode).
5. Controleer via **Ordertoezegging** of de leverdatum haalbaar is (zie BS25.328).
6. Kies **Vrijgeven**. Het order verschijnt bij het magazijn voor picking.

EDI- en webshoporders komen automatisch binnen — u controleert alleen de uitvallijst
(zie hoofdstuk 12 van de BPA voor de foutafhandeling).

## BS25.328 Leverdatum controleren (ordertoezegging)
- **Bron:** docs: https://learn.microsoft.com/en-us/dynamics365/business-central/sales-how-to-calculate-order-promising-dates (BC24)
- **Rol:** verkoop binnendienst

1. Open het verkooporder en kies **Order** > **Ordertoezegging**.
2. BC berekent per regel de vroegst haalbare verzenddatum op basis van voorraad en
   geplande ontvangsten.
3. Rood gemarkeerde regels halen de gevraagde datum niet: pas de datum aan of
   overleg met het magazijn — **vóór** u bevestigt aan een retailketen (boeteclausule!).

## BS25.206 Backorders opvolgen
- **Bron:** bpa
- **Rol:** verkoop binnendienst

Het beleid verschilt per kanaal en is vooraf ingesteld — u hoeft alleen te weten:

- **Retailketens:** geen backorders. Wat niet mee kan, wordt bij verzending
  automatisch geannuleerd; verwittig de keten vóór de levering.
- **Webshop/telefoon:** het restant blijft openstaan en wordt automatisch mee
  gepickt zodra er voorraad is. Openstaande backorders vindt u via
  **Verkooporders** met filter *Volledig verzonden = Nee*.

## MAN-001 Aanmelden en het rolcentrum
- **Bron:** review
- **Rol:** iedereen
- **Review:** schermafbeeldingen en de juiste rolcentrumnamen per gebruikersgroep toevoegen na de definitieve rolinrichting.

1. Ga naar businesscentral.dynamics.com en meld aan met uw Florax-account.
2. Uw startscherm (rolcentrum) toont de taken van uw rol; via het zoekicoon
   (of Alt+Q) vindt u elke pagina.
3. Persoonlijke instellingen: tandwiel > **Mijn instellingen** (taal, bedrijf).
