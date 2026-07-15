<!-- pack: food-manufacturing v1 — fork naar clients/<slug>/bpa/content/ en vervang <placeholders> -->
# 2. Verkoop

<KLANT> verkoopt via <kanalen — typisch: EDI-retail, webshop/B2B-portaal, manuele
intake>. Het verkoopproces bundelt die kanalen in één orderstroom met
kanaalafhankelijke afspraken voor deelleveringen en facturatie.
<!-- vraag: offertetraject aanwezig? zo nee, verwijder BS25.200 uit scope met reden -->

## BS25.101 Beheren verkoopprijzen
- **Invulling:** standaard

Per klant(groep) een verkoopprijslijst; promo-/actieprijzen als datumbegrensde
prijslijstregels die tijdens de actieperiode automatisch voorrang krijgen op de
basisprijs. BC bepaalt de geldige prijs op orderdatum.
<!-- vraag: bonussen/staffels achteraf? dan Aptean advanced pricing (BS25.900) afwegen -->
<!-- les (DEF-patroon): prijsherberekening bij wijziging leverdatum expliciet aanzetten -->

## BS25.202 Verkooporders maken
- **Invulling:** standaard

Alle kanalen monden uit in één verkooporder: EDI-/portaalorders automatisch via het
integratieframework (zie BS95.002) met controle van de uitvallijst door de
binnendienst; manuele intake met klantgegevens en prijzen uit de stamgegevens.
<!-- vraag: interne goedkeuringsflow op orders nodig? meestal niet als prijzen vooraf vastliggen -->

## BS25.328 Ordertoezegging
- **Invulling:** standaard

Voor klanten met harde leverdata (retail met boeteclausules) toont order promising
bij ingave de vroegst haalbare datum per regel — vóór bevestiging aan de klant.

## BS25.206 Beheer van backorders
- **Invulling:** standaard

Kanaalafhankelijk via *Verzendadvies* op de klantenfiche: retail typisch geen
backorders (restant annuleren + verwittigen), overige kanalen naleveren zodra er
voorraad is.

## BS25.213 Verkoopfacturen maken
- **Invulling:** standaard

Facturatieritmes per kanaal: verzamelfactuur (combine shipments) per <periode> voor
retail, factuur per levering voor de rest. Elektronische facturatie via Peppol
(BS65.256); keteneigen EDI INVOIC-formaten zijn typisch een GAP (lay-out +
framework-mapping).
