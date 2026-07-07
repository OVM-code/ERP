## 2. Verkoop
Het domein "Verkoop" omvat de bedrijfsprocessen die zorgen dat de klantenbehoeften gecapteerd worden en de betrokken diensten of goederen daarvoor geleverd worden en gefactureerd.

Het gaat concreet over:

- Het ontvangen, registreren van verkoopofferte en verkooporder

- Het leveren van de betrokken diensten of goederen

- Het factureren van het verkooporder

- Het beheer van retours en creditnota's.

De opvolging en afhandeling van de betaling van de verkoopfactuur wordt behandeld bij de financiële processen.

Business Scenario's - BPA Proces Verkooporder

Nieuw verkooporder aanmaken

Verkooporders: vastleggen van klantafspraken

Een verkooporder legt de overeenkomst vast tussen een organisatie en een klant voor de verkoop van producten en/of diensten, onder vooraf bepaalde leverings- en betalingsvoorwaarden. Het vormt de basis voor de opvolging van het volledige verkoopproces.

- Hoofding van het verkooporder

De algemene gegevens op de hoofding van een verkooporder worden standaard overgenomen van de klantinstellingen (indien beschikbaar). Deze gegevens kunnen per verkooporder worden aangepast, zonder impact op de stamgegevens van de klant.

Klantgegevens

- De klant waarmee de overeenkomst wordt gesloten, inclusief een eventuele contactpersoon.

- Het afleveradres: dit kan gekozen worden uit de vooraf ingestelde adressen van de klant, of als
eenmalig adres worden ingevoerd.

- Facturatiegegevens: bepalen wie de factuur ontvangt. Dit kan de klant zelf zijn, een andere klant,
of een eenmalig aangepaste facturatiepartij.

- Valutacode

Verzendgegevens

- Verzendwijze (bijv. Incoterms), expediteur en verzendservice (bijv. transportfirma of eigen
vervoer).

Logistieke gegevens

- De locatie (magazijn) van waaruit de goederen worden verzonden.

Intrastat-gegevens

- Voor statistische en douanedoeleinden, indien van toepassing.

Datumgegevens

- Belangrijke datums zoals orderdatum, verzochte leverdatum en toegezegde leverdatum.

- Regels van het verkooporder

Een verkooporder bevat één of meerdere regels. Elke regel beschrijft een artikel of dienst die aan de klant wordt verkocht.

Soorten verkoopregels

- Opmerking

- Grootboekrekening

- Artikel

- Resource

- Vast activum

- Toeslag (artikel)

- Toewijzingsrekening

Voor elke regel (behalve opmerkingen) moet een hoeveelheid worden ingevoerd.

Prijsbepaling

Voor artikelen en resources wordt de verkoopprijs en eventuele korting bepaald via een verkoopprijslijst of overgenomen van de artikelkaart. De eenheidsprijs en regelkorting kunnen handmatig worden aangepast indien nodig.

Orderbevestiging en status

Wanneer het verkooporder volledig is ingevuld, kan een orderbevestiging naar de klant worden verzonden (per e-mail of afgedrukt).

De laatste stap in het aanmaken van een verkooporder is het wijzigen van de status van Open naar één van de volgende:

- Vrijgegeven

- Wacht op goedkeuring

- Wacht op vooruitbetaling

Verkooporder wijzigen Wijzigingen kunnen aangebracht worden op een bestaand verkooporder. Indien het verkooporder een andere status heeft dan Open, moet het eerst heropend worden. Na het aanbrengen van wijzigingen kan het nodig zijn om:

- Een nieuwe orderbevestiging naar de klant te sturen.

- Een nieuwe goedkeuringsaanvraag te versturen (afhankelijk van de situatie).

- Een (bijkomende) vooruitbetalingsfactuur aan te maken.

Indien er wel al verzendingen geregistreerd zijn, gelden er uiteraard bepaalde beperkingen over wat aangepast kan worden.

Verzendingen ongedaan maken

Indien er toch wijzigingen nodig zijn op een verkooporder waarop al verzendingen gebeurd zijn, is het mogelijk om één of meerdere verzendingen ongedaan te maken, op voorwaarde dat deze nog niet gefactureerd zijn. Hierdoor worden de bijbehorende orderregels opnieuw bewerkbaar.

Verkooporder verwijderen Er zijn meerdere geldige redenen om een verkooporder te verwijderen in Business Central:

- Annulering door de klant
Wanneer een klant een order annuleert, kan het verkooporder verwijderd worden om de administratie op orde te houden.

- Administratieve correctie
Soms is het nodig om een verkooporder te verwijderen om het te vervangen door een nieuw order, bijvoorbeeld bij fouten in klantgegevens, prijzen of leveringsvoorwaarden.

- Backorders en herstructurering
Wanneer artikelen niet beschikbaar zijn op de gewenste leverdatum, ontstaat er een backorder. In sommige gevallen is het dan wenselijk om het bestaande order te verwijderen en de artikelen opnieuw toe te voegen aan een ander of nieuw verkooporder.

Voorwaarden voor het verwijderen van een verkooporder

Een verkooporder kan alleen verwijderd worden als aan de volgende voorwaarden is voldaan:

- Er zijn geen verzendingen geregistreerd op het order.

- Als er verzendingen zijn, moeten alle regels volledig gefactureerd zijn.

- Het order mag niet in een goedkeurings-workflow zitten.

- Er mogen geen vooruitbetalingsfacturen aan gekoppeld zijn.

### 2.1 Verkoop instellen
#### 2.1.1 BS25.001 Verkoop instellen
De verkoopinstellingen bevatten een aantal algemene instellingen die gelden binnen het domein verkoop. Het gaat onder meer over hoe kortingen geboekt worden, welke afrondingen er toegepast worden, de klantengroep- en verkoper-dimensies. De verkoopinstellingen bevatten ook de instellingen van de nummerreeksen die voor de verschillende verkoop-gerelateerde documenten worden gebruikt. Verder bevat de verkoopinstellingen de parameters voor het archiveren, het boeken in de achtergrond en de eventuele koppeling met Dynamics 365 for Sales.

### 2.2 Verkoop master data
#### 2.2.1 BS25.100 Beheren klantenfiche
Dit scenario behandelt het beheer van de basis klantengegevens.

Voor klanten kunt u algemene gegevens zoals naam, adres, land en diverse telefoonnummers, e-mailadressen etc. registreren. Ook kunnen er andere klantgegevens bijgehouden worden zoals facturatie-, verzend- en betalingsgegevens die belangrijk zijn binnen het verkoopproces.

Vanuit financieel oogpunt zijn volgende parameters van belang:

- Boekingsgroepen: zorgen voor een juiste sturing naar grootboekrekeningen (controlerekening,
omzet/kostenrekening, BTW rekening).
- Betalingscondities: bepalen de vervaldatum en contant korting
- Betalingswijze (bv. Domiciliëring)
- BTW nr., Ondernemingsnummer
- Aanmaningscondities

De taalcode is van belang voor de document lay-out van verkoopdocumenten. Standaard wordt een lay-out voorzien in NLB, ENU, FRB.

#### 2.2.2 BS25.101 Beheren verkoopprijzen
https://learn.microsoft.com/nl-be/dynamics365/business-central/across-prices-and-discounts?tabs=current- experience

Verkoopprijzen worden gebruikt om de prijs te bepalen voor alle verkoopdocumenten zoals verkoopoffertes, verkooporders, verkoopfacturen en verkoopcreditnota's. Verkoopprijzen worden beheerd in de verkoopprijslijsten en kunnen gedefinieerd worden voor:

- Specifieke klanten

- Klantenprijsgroepen

- Alle klanten

- Campagne

en dit telkens per artikel.

De verkoopprijzentabel bevat volgende kenmerken:

- Eenheid: geeft aan in welke eenheid (stuks, kg, karton, …) de prijzen zijn uitgedrukt

- Eenheidsprijs: geeft de verkoopprijs aan, uitgedrukt in de eenheid die wordt ingesteld

- Minimum aantal: geeft aan dat de verkoopprijs geldig is vanaf een bepaald aantal (hiermee kunnen
staffelprijzen ingesteld worden).

- Begin- en einddatum: geeft de periode aan waarbinnen de prijs geldig is. Dit geeft de mogelijkheid om
nieuwe prijzen in te voeren die geldig zijn vanaf een bepaalde datum en biedt de mogelijkheid tot het raadplegen van de historiek van de verkoopprijzen.

- Variant

- Valutacode

##### 2.2.2.1 BC25.101.01 Uitgebreid verkoopprijzenbeheer
Met uitgebreid verkoopprijzenbeheer is de gebruiker in staat om een nieuwe commerciële kost te berekenen als basis voor nieuwe eenheidsprijzen te berekenen. Deze berekening is gebaseerd op de volgende formule: Nieuwe verkoopprijs = (basis kostprijs + extra kost) * verkoop winst %

##### 2.2.2.2 BC25.101.02 Klantenprijsgroep 'afhaal'
In het geval er aan klanten een speciale korting toegekend wordt als ze opteren om hun goederen af te halen kan er met deze functionaliteit eenvoudig een korting toegekend worden.

##### 2.2.2.3 BC25.101.03 Einde-periode verkoopvergoedingen beheren
Als er met klanten afspraken vastgelegd worden over kortingen op het einde van een bepaalde periode dan kan er gebruik gemaakt worden van deze functionaliteit. Bijvoorbeeld een klant die binnen een bepaalde periode een vooropgestelde hoeveelheid heeft afgenomen van specifieke artikelen/artikelgroepen kan het zijn dat er een korting gegeven wordt in de vorm van een vergoeding.

Het kortingsbedrag wordt aan de klant toegekend via een verkoopcreditnota op basis van een artikeltoeslag.

##### 2.2.2.4 BC25.101.04 Afsluiten vorige prijsrecord
In Business Central is het mogelijk om op veel verschillende niveaus kortingen in te geven. Dit zorgt ervoor dat er vaak meerdere kortingstarieven van toepassing zijn op verkoopprijzen, verkooplijnen, inkoopprijzen en inkooplijnen. Dit kan heel wat verwarring veroorzaken en mogelijks leiden tot verkeerde prijzen.

De functionaliteit 'afsluiten vorige prijsrecord' zorgt ervoor dat er geen 'dubbele' prijsvoorwaarden en kortingen meer mogelijk zijn. Hierdoor wordt vermeden dat er tegelijk meerdere prijsvoorwaarden actief zijn.

##### 2.2.2.5 BC25.101.05 Advanced pricing (Aptean)
2.2.2.5.1 Verkoop https://fnbdocs.apteancloud.com/bc/APR/contents/

The ‘advanced pricing’ extensie maakt het mogelijk om verkoopprijzen en kortingen voor producten te bepalen gebaseerd op een vooropgestelde hiërarchie. Standaard Business Central kiest de laagst mogelijke prijs met de hoogst mogelijke lijn korting op een gegeven datum. Deze extensie maakt het ons mogelijk om de prijs te bepalen per klant, per klant prijsgroep of voor alle klanten. Wanneer de ‘advanced pricing’ methode gekozen wordt als prijs berekeningsmethode, dan gaat de beschikbare prijs gezocht worden op basis van volgende hiërarchie: Campagne & product

1. Klant & product
2. Klant prijsgroep & product
3. Alle klanten & product
4. Product kaart
Wanneer een geldige prijs wordt gevonden, gaat de extensie niet verder zoeken naar prijzen van een lagere hiërarchie. Het is niet verplicht om de voorgestelde prijs te gebruiken, deze kan nog altijd manueel gewijzigd worden. Deze extensie geeft gedetailleerde informatie weer over de oorsprong van de verkoopprijs en de gehanteerde korting op de verkooplijnen. Dezelfde hiërarchie wordt gebruikt bij het zoeken naar kortingen maar hier zijn nog extra niveaus bijgevoegd door de aanwezige setup voor de product kortingsgroepen. Onderstaande visuele weergave vat de hiërarchie samen:

Standaard Business Central biedt enkel de mogelijkheid om te werken met kortingen in percentages. Deze extensie breidt dit uit met de mogelijkheid tot werken met kortingen in bedragen. Dit is enkel mogelijk wanneer er met de ‘advanced pricing’ methode wordt gewerkt.

De extensie geeft ook nog de mogelijkheid tot volgende verkoopprijsstrategieën:
- Gebruik dezelfde verkoopprijsstrategie bij verschillende klanten gelijktijdig door het gebruik van een
referentie klant.
- Differentiëren van prijsstrategieën voor verschillende locaties van één klant door het definiëren van
prijsparameters op het niveau van het verzendadres.
- Definiëren van referentiedata voor prijsbepaling (orderdatum, verzenddatum, leveringsdatum) enkel
op klantniveau. 2.2.2.5.2 Bevriezen verkoopprijzen In sommige gevallen is het nodig om de verkoopprijs te bevriezen zodat de prijs niet meer verandert bij een wijziging van de bestelde hoeveelheid. Dit is het geval wanneer een bestelling niet volledige in één keer geleverd kan worden. De klant heeft dan wel recht op de vooraf afgesproken prijs. Deze extensie gaat automatisch de prijs bevriezen bij het gebruik van de ‘get shipment lines’ functie bij een verandering van de verzonden hoeveelheid. De prijs op de salesorder lijn zal overgenomen worden. Standaard Business Central gaat opnieuw de laagst mogelijke prijs selecteren met de hoogst mogelijke korting voor de nieuwe verzonden hoeveelheid, wat niet correct is. Het is mogelijk om manueel het bevriezen van de prijs af te zetten op de applied sales price and discount page. 2.2.2.5.3 Aankoop Advanced pricing voor het bepalen van aankoopprijzen bij leveranciers werkt op dezelfde manier als het bepalen van de verkoopprijzen bij klanten. Enkel de hiërarchie is iets anders, deze is namelijk als volgt bij stap 2:
1. Leverancier & product
2. Alle leveranciers & product
3. Product kaart
Aan de aankoopkant zijn dezelfde functionaliteiten te vinden als bij het verkoopluik.

#### 2.2.3 BS25.102 Beheren verkoopregelkortingen
https://learn.microsoft.com/nl-be/dynamics365/business-central/across-prices-and-discounts?tabs=current- experience

Verkoopregelkortingen worden net als verkoopprijzen beheerd in de verkoopprijslijsten en worden gebruikt om de korting te bepalen voor alle verkoopdocumenten zoals verkoopoffertes, verkooporders, verkoopfacturen en verkoopcreditnota's. Verkoopregelkortingen kunnen gedefinieerd worden voor:

- Specifieke klanten

- Klantenkortingsgroepen

- Alle klanten

- Campagne

en dit telkens per artikel of artikelkortingsgroep.

De verkoopregelkorting-tabel bevat volgende kenmerken:

- Eenheid: geeft aan in welke eenheid (stuks, kg, karton, …) de kortingen zijn uitgedrukt

- Regelkorting %: geeft het percentage van de regelkorting aan, uitgedrukt in de eenheid die wordt
ingesteld

- Minimum aantal: geeft aan dat de korting geldig is vanaf een bepaald aantal (hiermee kunnen
staffelkortingen ingesteld worden).

- Begin- en einddatum: geeft de periode aan waarbinnen de korting geldig is. Dit geeft de mogelijkheid
om nieuwe kortingen in te voeren die geldig zijn vanaf een bepaalde datum en biedt de mogelijkheid tot het raadplegen van de historiek van de kortingen.

- Variant

- Valutacode

#### 2.2.4 BS25.103 Beheren artikeltoeslag verkoop
https://learn.microsoft.com/nl-be/dynamics365/business-central/payables-how-assign-item-charges

Artikeltoeslagen kunnen worden toegepast voor het berekenen van bepaalde kosten op orders, zoals transportkosten, administratiekosten, ... of voor het toekennen van een verkoopvergoeding (bijvoorbeeld als tegemoetkoming voor een verkeerd geleverd of beschadigd product).

Artikeltoeslagen kunnen manueel worden toegevoegd op verkoopdocumenten.

Bij het gebruik van artikeltoeslagen moeten deze worden toegewezen:

- Aan artikelen op hetzelfde verkoopdocument (bijvoorbeeld op een verkooporder waar een
transportkost wordt vermeld).

- Aan artikelen op verzendregels of retourverzendregels van een ander verkoopdocument (bijvoorbeeld
voor de registratie van een transportkost die aan de klant wordt aangerekend).

#### 2.2.5 BS25.104 Beheren verkoopfactuurkortingen
Factuurkortingen worden gebruikt als een globale korting op het volledige bedrag van een verkoopdocument (bijv. verkooporder).

Factuurkortingen kunnen per klant worden ingesteld en gelden als een percentage op het totale bedrag van een verkooporder of -factuur. Hoewel de factuurkorting als een globale korting geldt, wordt het factuurkortingsbedrag per regel berekend en wordt ook per regel bepaald of er factuurkorting kan toegepast worden:

- Voor artikelen is het toepassen van de factuurkorting afhankelijk van een instelling op de artikelkaart.

- Voor resources wordt factuurkorting standaard toegepast

- Bij verkoop via grootboekrekeningen, vaste activa en artikeltoeslagen wordt factuurkorting standaard
niet toegepast.

Men kan het al dan niet toepassen van de factuurkorting op regelniveau aanpassen, bijv. om bij verkoop via een grootboekrekening toch factuurkorting te berekenen.

Naast de factuurkorting die gebaseerd is op een minimumfactuurbedrag, kan er ook een vaste administratiekost worden ingesteld die de klant moet betalen. De administratiekost is ook afhankelijk van het minimum bedrag dat voor de factuurkorting is ingesteld.

#### 2.2.6 BS25.105 Beheren verkoopbestellijsten (sales codes)
Standaardverkoopregels kunnen gebruikt worden om vaak terugkerende orderregels in te stellen, bijv. wanneer een klant dikwijls eenzelfde bestelling plaatst. De standaardverkoopregels kunnen aan klanten toegekend worden en al dan niet automatisch (afhankelijk van de instellingen) worden toegepast op offertes, orders, facturen en /of creditnota’s.

#### 2.2.1 BS25.902 Artikelasssortiment
In bepaalde gevallen, mogen klanten enkel kopen uit bepaalde artikelen. Het beperken van alle artikelen in het productgamma tot een specifieke lijst wordt ook wel assortiment of catalogus genoemd.

##### 2.2.1.1 BC25.902.01 Customer item catalog (Aptean)
Het primaire doel van deze extensie is het snel, gecontroleerd en gestructureerd invoeren van een verkooporder. Een artikelcatalogus kan verschillende combinaties van artikelnummer/variantcode en maateenheid bevatten. Meerdere artikelcatalogus codes kunnen dan aan een klant worden gekoppeld. Een artikelcatalogus heeft een start en einddatum. Vanop een verkooporder kan een extra scherm geopend worden waarvan snel bestelde hoeveelheden kunnen ingevoerd worden. Wanneer dit scherm gesloten wordt, gaan de verkoopregels gevuld worden met de juiste hoeveelheden op het verkooporder. Wanneer er een artikel staat op het verkooporder dat niet behoort tot de artikelcatalogus van de klant, zal er een error boodschap tevoorschijn komen. Deze extensie maakt het ook mogelijk om de klant specifieke artikelcatalogus als een Excel-bestand via email te sturen. De klant kan dan op zijn beurt de gewenste hoeveelheden ingeven in de Excel file waarna hij het kan terugsturen. De ontvangen email van de klant met het Excel bestand zal dan resulteren in een automatisch gecreëerd verkooporder. Deze extensie biedt ook de mogelijkheid om artikelen als private labels aan te duiden.

##### 2.2.1.2 BC25.902.02 Klanten assortiment (Cegeka)
De Cegeka oplossing bouwt verder op de verkoopbestellijst van standaard BC, met extra controles tijdens een verkoopproces of een artikel aanwezig op deze specifieke bestellijst.

### 2.3 Verkoopoffertes beheren
#### 2.3.1 BS25.200 Verkoopoffertes maken
https://learn.microsoft.com/nl-be/dynamics365/business-central/sales-how-make-offers

Dit scenario omvat het aanmaken van verkoopoffertes.

Verkoopoffertes worden gebruikt voor de registratie en opvolging van prijsaanbiedingen voor producten en/of diensten aan klanten of prospecten. Verkoopoffertes kunnen worden omgezet in een verkooporder of worden gearchiveerd voor toekomstige transacties met de klant of contact.

Indien er gebruik gemaakt wordt van opportuniteiten voor het opvolgen van de verkoopcyclus, kan een verkoopofferte worden aangemaakt vanaf de opportuniteit. Bij het beëindigen van een opportuniteit kan de waarde hiervan worden bijgewerkt op basis van de gekoppelde offerte.

### 2.4 Verkoopraamcontracten beheren
#### 2.4.1 BS25.201 Verkoopraamcontracten beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/sales-how-to-create-blanket-sales-orders

Op een verkoopraamcontract worden de artikelen en/of diensten vastgelegd met de hoeveelheden die een klant wenst af te nemen, tegen een afgesproken prijs. Vanaf een raamcontract kunnen verkooporders worden afgeroepen tot het volledige aantal van het raamcontract is voldaan. Bij elke afroep worden de prijzen en kortingen die op het raamcontract zijn ingesteld overgenomen naar het verkooporder.

De ingevoerde hoeveelheden op een raamcontract zijn niet van invloed op de artikelbeschikbaarheid zolang er geen verkooporders zijn voor aangemaakt. Op raamcontracten kunnen de afgeroepen hoeveelheden steeds geraadpleegd worden.

### 2.5 Verkooporders beheren
#### 2.5.1 BS25.202 Verkooporders maken
https://learn.microsoft.com/nl-be/dynamics365/business-central/sales-how-sell-products

Verkooporders leggen de overeenkomst met een klant vast om producten en/of diensten tegen bepaalde leverings- en betalingsvoorwaarden te verkopen. In dit scenario worden de verschillende methodes beschreven voor het aanmaken en opvolgen van verkooporders.

- Verkooporder maken: De registratie van een bestelling van een klant gebeurt door middel van een
verkooporder. Naast de algemene gegevens zoals afleverplaats, verzendwijze enz. wordt er geregistreerd welke artikelen met hun aantal en levertermijn er gewenst zijn. Het vastleggen van de

verkoopprijzen en eventuele toeslagen (transport en andere) is eveneens een essentieel onderdeel bij de opmaak van een verkooporder. Bij het manueel aanmaken van een verkooporder worden de kop- en regeldetails manueel ingevoerd.
- Verkooporder maken vanaf raamcontract: Het aanmaken van een verkooporder vanaf een
raamcontract start met het openen van het raamcontract waarvoor men een verkooporder wenst te maken. Op het raamcontract voert men het te verzenden aantal in op één of meerdere regels. Dit geeft de hoeveelheid aan waarmee het order moet aangemaakt worden. Vervolgens wordt via de actie “Order maken” het verkooporder aangemaakt. Op het verkooporder worden de kop- en regeldetails automatisch gevuld met de informatie afkomstig van het raamcontract.
- Verkooporder maken vanaf verkoopofferte: Het aanmaken van een verkooporder vanaf een
verkoopofferte start met het openen van de verkoopofferte die men wenst om te zetten naar een verkooporder. Via de actie “Order maken” wordt het verkooporder aangemaakt en de verkoopofferte verwijderd (afhankelijk van de verkoopinstellingen wordt de offerte al dan niet gearchiveerd). Op het verkooporder worden de kop- en regeldetails automatisch gevuld met de informatie afkomstig van de verkoopofferte.

##### 2.5.1.1 BC25.202.01 Snelle ingave verkooporders
“Snelle ingave verkooporders” is voorzien om het ingeven van verkooporders in Business Central te versnellen. Hiermee is het mogelijk om verkooporders aan te maken door enkel het artikelnummer en aantal in te vullen. De invoer kan ook gebeuren aan de hand van de artikelomschrijving of een deel ervan.

Verder is het ook mogelijk om de snelle ingave te doen aan de hand van een standaard verkoopcode. In dat geval worden alle artikelen en aantallen, die aan deze verkoopcode gekoppeld zijn, onmiddellijk op het verkooporder gezet.

##### 2.5.1.2 BC25.202.02 Klantenprijsgroep ‘Afhaal’
Het komt vaak voor dat wanneer klanten hun goederen komen ophalen er een speciale korting toegekend wordt. Deze functionaliteit voorziet dat de velden klantprijsgroep en klantkortingsgroep worden weergegeven op de verkooporderhoofding. Op deze manier kan er nog snel een korting toegewezen worden op een specifiek verkooporder bij afhaal.

##### 2.5.1.3 BC25.202.03 Ingave via lengte/breedte/hoogte
De prijsberekening wordt gedaan op basis van de ingestelde verkoopeenheid op de artikelkaart. Vaak wordt er echter verkocht in een verkoopeenheid die verschilt van de instelling op de artikelkaart. Met deze functionaliteit is het mogelijk om het artikel in te geven met een andere eenheid. Afhankelijk van de instellingen op de artikelkaart wordt er dan een berekening gedaan voor de standaard verkoopeenheid.

##### 2.5.1.4 BC25.202.04 Toevoegen transportkosten
Bij het verkopen van goederen moeten in vele gevallen transportkost bijgerekend worden. Met deze functionaliteit kan je gemakkelijk de transportkosten standaard instellen voor specifieke klanten.

Bij het aanmaken van een verkooporder kan er via de functie ‘toevoegen transport’ automatisch de verschillende transportkosten opgehaald worden die ingesteld zijn op klantenniveau.

Er kunnen verschillende soorten transport aangemaakt en ingesteld worden (e.g. normaal transport, express transport etc.)

##### 2.5.1.5 BS25.202.05 Call plan (Aptean)
Deze extensie functioneert als hulp bij het organiseren van de bestellingen & verzendingen van een organisatie. Het is mogelijk om de volgende zaken te plannen:
- Wie er gecontacteerd moet worden
- Wanneer de klant of de contactpersoon gebeld moet worden
- De dagen wanneer het verzenden en leveren van de bestellingen wordt gedaan.
Deze extensie houdt rekening met aanvullende informatie van elke klant in het verkoopproces. Deze uitbreiding kan een call plan structuur opzetten waarmee de verkoopmedewerkers de lijst van klanten gerelateerd aan een order kunnen zien en ermee kunnen interageren. Met behulp van het call plan kan de verkoper direct een nieuwe verkooporder aanmaken en de bestaande verkooporders met betrekking tot die call plan record bekijken.

#### 2.5.2 BS25.203 Doorverzendingen en speciale orders
Doorverzendingen en speciale orders zijn methodes om producten die men verkoopt aan klanten rechtstreeks door te bestellen naar de eigen leveranciers.

- Doorverzending vanuit verkooporder: Bij doorverzendingen worden de producten rechtstreeks door de
leverancier bij de klant geleverd. Het aanmaken van een verkooporder met doorverzending gebeurt op analoge wijze als het aanmaken van een gewoon verkooporder. Via de “inkoopcode” kan men aanduiden welke regels via doorverzending moeten geleverd worden. https://learn.microsoft.com/nl-be/dynamics365/business-central/sales-how-drop-shipment Formatted: English (United States) Formatted: English (United States)
- Speciale order vanuit verkooporder: Bij speciale orders worden de producten van de klant besteld bij
de leverancier, maar worden deze eerst in het eigen magazijn ontvangen en dan verstuurd naar de klant. Field Code Changed Het aanmaken van een verkooporder met "special order" gebeurt op analoge wijze als het aanmaken van een gewoon verkooporder. Via de “inkoopcode” kan men aanduiden welke regels als speciale order moeten behandeld worden. https://learn.microsoft.com/nl-be/dynamics365/business-central/sales-how-to-create-special-orders Field Code Changed

#### 2.5.3 BS25.204 Reserveer voorraad op een verkooporder
https://learn.microsoft.com/nl-be/dynamics365/business-central/inventory-how-to-reserve-items

Het reserveren van voorraad op een verkooporder is een optionele stap en kan toegepast worden wanneer men de voorraad van een artikel (of een deel ervan) wenst voor te behouden voor een specifieke klant of

verkooporder. Naast het reserveren van artikelen in voorraad kan er ook gereserveerd worden op productieorders of inkooporders (voor handelsgoederen).

In het algemeen geldt dat

- de gereserveerde artikelen [vandaag] beschikbaar moeten zijn bij reservering op de voorraad
onafhankelijk van de verzenddatum van het order. Commented [NH1]: Dit is grootste “zwakte” van reserveringen. Iemand die voor 6 maand in de
- de gereserveerde artikelen op de ontvangstdatum van het inkooporder beschikbaar moeten zijn bij toekomst een order plaatsten en we reserveren de
reservering op inkooporder. Deze datum moet voor de verzenddatum van het order vallen, anders stock daarvoor, zorgt ervoor dat we tijdens die 6 manden een hoge stock gaan bijhouden van dit artikel. wordt reservering verwijderd. In het ideale geval reserveer je een artikel pas op de verzenddatum - levertermijn artikel. Vb als artikel 1 Het reserveren kan automatisch of manueel gebeuren. Bij de automatische reservering gebeurt dit bij de ingave maand levertermijn heeft en moert verzonden worden van het verkooporder. op 01/07 --> reservatie pas vastleggen op 01/06

#### 2.5.4 BS25.205 Verkooporder verzenden
https://learn.microsoft.com/nl-be/dynamics365/business-central/ui-post-sales

Indien er geen nood is aan het beheren van de magazijnprocessen voor het picken en verzendklaar maken van de artikelen, kan een verzending heel eenvoudig rechtstreeks vanaf het verkooporder uitgevoerd worden. Bijvoorbeeld:

- Eén persoon is verantwoordelijk voor zowel de orderadministratie als voor de magazijnadministratie

- Indien de magazijnprocessen eenvoudig zijn en er geen nood is aan real-time registratie

Indien er wel extra magazijnprocessen van toepassing zijn, wordt de verzending in detail besproken onder “BS50.214 Magazijnverzending maken”.

#### 2.5.5 BS25.206 Beheer van backorders
Wanneer slechts een deel van de producten in een order geleverd kan worden, ontstaat een backorder en dringt de keuze zich op wat er met de overige goederen dient te gebeuren:

- Annuleren

- Naleveren op een andere datum

Restlevering annuleren: Wanneer de gevraagde goederen niet volledig op de gevraagde datum kunnen worden geleverd, ontstaat er een backorder. Indien er geopteerd wordt om de restlevering niet meer na te leveren, kunnen de aantallen op het verkooporder aangepast worden zodat er niet langer een openstaand aantal is, of indien de regel nog niet verzonden is, kan deze verwijderd worden.

Restlevering bijwerken: Wanneer de gevraagde goederen niet volledig op de gevraagde datum kunnen worden geleverd, ontstaat er een backorder. Indien er geopteerd wordt om het resterend opstaand aantal na te leveren, kan het verkooporder bijgewerkt worden om zo de nalevering te organiseren.

##### 2.5.5.1 BC25.206.01 Backorder management (Aptean)
Deze extensie helpt om het verkoopproces en de klantenbinding te verbeteren. Deze extensie helpt de vraag naar artikelen te begrijpen en te voorspellen. Deze extensie voegt een scherm toe met alle backorders. Vanaf dit scherm kunnen lijnen van backorders naar:
- Een nieuw sales order gezet worden.
- Een bestaand sales order gezet worden
Deze extensie kan enkel gebruikt worden wanneer de ‘Over and Under delivery’ extensie actief is.

##### 2.5.5.2 BC25.206.02 Beheer van backorders (Cegeka)
Deze functionaliteit bepaalt of het mogelijk is om backorder bij te houden of niet. Indien dit voor een klant verboden is om backorders bij te houden zullen mogelijke backorders opgelijst worden als eens tegel op een rolcentrum. Dan kan er eenvoudig order per order bekeken worden wat er mee te doen. Deze functionaliteit past geen orders aan, dit moet nog manueel gedaan worden. In de lijst van backorders kunnen de orders verwijderd worden. Belangrijk is dat voor deze orders waar het aantal 'te verzenden/te factureren' niet gelijk is aan 0 er geen actie zal ondernomen worden.

#### 2.5.6 BS25.207 Verkooporders annuleren
Op voorwaarde dat er geen verzendingen geboekt zijn op het verkooporder kan het verkooporder steeds geannuleerd worden door het te verwijderen. Wanneer wel al verzendingen geboekt zijn, moeten de verzendregels eerst ongedaan gemaakt worden en kan vervolgens het order verwijderd worden. Indien de verzending wel al gefactureerd is, moet een retourproces gestart worden.

#### 2.5.7 BS25.208 Verwerk intercompany verkooporders
https://learn.microsoft.com/nl-be/dynamics365/business-central/intercompany-how-setup

Wanneer een onderneming uit verschillende legale entiteiten (bedrijven) bestaat, en er tussen de bedrijven onderling verkoop- en inkooptransacties plaatsvinden, kan er gebruik gemaakt worden van intercompany.

Indien intercompany is ingesteld tussen de verschillende bedrijven kan een verkooporder dat in het ene bedrijf is aangemaakt worden omgezet naar een inkooporder in een ander bedrijf. In deze zin is dit dus het spiegelbeeld van intercompany inkooporders. Het belangrijkste doel van de IC module is om repetitieve orderingave te vereenvoudigen en zo fouten te vermijden.

Deze IC module kan in beide richtingen werken:

- Inkooporder van bedrijf A naar B (In B wordt het een verkooporder)

- Verkooporder van Bedrijf A naar B (In B wordt het een inkooporder)

#### 2.5.8 BS25.209 Productieorders maken vanaf verkooporders
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-how-to-create-production- orders-from-sales-orders

Als er voor een bepaald verkooporder onvoldoende stock is, of wanneer eindproducten heel specifiek voor een verkooporder geproduceerd worden, is het mogelijk om vanuit het verkooporder rechtstreeks een planningsberekening te uit te voeren. Vanaf de verkooporderplanning kunnen productieorders aangemaakt worden voor de artikelen met bestelbeleid productieorder die op het verkooporder aanwezig zijn.

Er wordt automatisch een reservering gemaakt van de verkooporderregels naar de bijhorende productieorder.

#### 2.5.9 BS25.211 Goedkeuringsaanvraag verzenden
https://learn.microsoft.com/nl-be/dynamics365/business-central/across-how-to-create-workflows

In bepaalde situaties kan het voorvallen dat er een goedkeuring vereist is van een andere persoon alvorens er een verkooporder kan verwerkt worden, bv. de boekhouder die moet goedkeuren of aan een bepaalde klant nog verkocht mag worden. Indien dit het geval is, stuurt de gebruiker een aanvraag tot goedkeuring naar de gebruiker die hierover kan beslissen. Die kan indien nodig ook op zijn beurt een goedkeuringsaanvraag versturen naar een andere bevoegde indien dit nodig is. Nadat de verantwoordelijke de aanvraag verwerkt heeft, krijgt de aanvrager hiervan een melding en kan het verkooporder vrijgegeven en verder verwerkt worden.

Dezelfde goedkeuring kan ook op andere verkoopdocumenten van toepassing zijn (verkoopfacturen, creditnota’s, offertes, …)

2.5.10BS25.212 Verkooporder goedkeuren Goedkeurders ontvangen berichten over goedkeuringsaanvragen voor verkooporders. Deze moeten beoordeeld worden en goedgekeurd worden vooraleer het order kan vrijgegeven worden om verder te worden verwerkt. Wanneer een verkooporder is goedgekeurd, krijgt de aanvrager hiervan een melding.

Dezelfde goedkeuring kan ook op andere verkoopdocumenten van toepassing zijn (verkoopfacturen, creditnota’s, offertes, …)

2.5.11BS25.237 Verkoopverzending ongedaan maken https://learn.microsoft.com/nl-be/dynamics365/business-central/finance-how-reverse-journal-posting

Een verzending kan ongedaan gemaakt worden vanaf de geboekte verkoopverzending. Hiervoor selecteert men de regel die ongedaan gedaan moeten worden en kies men de actie “Verzending ongedaan maken”. Enkel regels

met soort “Artikel” kunnen ongedaan gemaakt worden. Door het ongedaan maken komen de artikelen opnieuw op voorraad.

#### 2.5.12 BS25.328 Ordertoezegging
https://learn.microsoft.com/nl-be/dynamics365/business-central/sales-how-to-calculate-order-promising- dates

Via ordertoezegging op een verkooporder kunnen leveringsdata worden bepaald aan de hand van twee functies: Available to Promise (ATP) en Capable to Promise (CTP).

Indien een gewenste leverdatum wordt ingevuld op het verkooporder, zal Business Central volgende berekening uitvoeren:

Gewenste leverdatum – verzendtijd = Geplande verzenddatum

Geplande verzenddatum – uitgaande whse verwerkingstijd = Verzenddatum

Indien de artikelen niet beschikbaar zijn op de verzendatum, zal een waarschuwing worden getoond.

- Available to Promise berekent de vroegste datum waarop een artikel kan worden verzonden, in rekening
van de beschikbare voorraad. Dit houdt rekening met de niet-gereserveerde voorraad van geplande productie, aankopen, transfers en verkoopretouren.

- Capable to Promise berekent de vroegste datum waarop een artikel kan worden verzonden, waarbij het
geproduceerd, gekocht en getransfereerd moet worden. Business Central gaat uit van een Wat Als- scenario, enkel van toepassing op artikelhoeveelheden die niet in voorraad zijn, of op een gepland bestelling staan. CTP kan de aanmaak van een bv een inkooporder triggeren en alle bijhorende tijd hiervan meenemen in de berekening van wanneer het artikel de klant kan bereiken.

### 2.6 Verkoopfacturen beheren
#### 2.6.1 BS25.213 Verkoopfacturen maken
Dit scenario omvat het maken van verkoopfacturen op basis van verzendingen, via het ophalen van verzendregels op een manuele verkoopfactuur en via verzamelfacturatie. Daarnaast wordt ook het maken van een manuele verkoopfactuur (zonder verkooporder) vermeld.

https://learn.microsoft.com/nl-be/dynamics365/business-central/sales-how-invoice-sales

https://learn.microsoft.com/nl-be/dynamics365/business-central/sales-how-to-combine-shipments-on-a- single-invoice

- Verkoopfactuur maken vanaf verkooporder: Wanneer een of meerdere verzendingen voor een
verkooporder geregistreerd zijn, kan er een verkoopfactuur gemaakt worden. Indien nodig kunnen bijkomende kosten (bijv. transportkosten) toegevoegd worden. Bij het aanmaken van een verkoopfactuur vanaf een verkooporder worden alle regels waarvoor een verzending is geregistreerd op de factuur opgenomen. De prijzen en kortingen worden van het verkooporder overgenomen
- Verkoopfactuur maken met ophalen van verzendregels: Bij het maken van verkoopfacturen via het
ophalen van verzendregels wordt eerst een manuele factuur gemaakt waarop de klant en verzendadres (indien van toepassing) worden geselecteerd. Vervolgens wordt een overzicht geopend van alle verzonden-niet gefactureerde verzendingen voor de klant op het gekozen verzendadres. Uit dit overzicht worden de regels geselecteerd die men wenst te factureren.
- Verkoopfacturen maken via verzamelfacturatie: Verzamelfacturering is een periodieke taak die kan
gebruikt worden om alle verzonden artikelen van verschillende verkooporders van eenzelfde klant op één factuur samen te voegen. Deze periodieke taak verzamelt alle niet gefactureerde verzendingen van klanten en maakt hiervoor één of meerdere factureren (afhankelijk van hoeveel verzendingen geboekt werden).
- Verkoopfactuur maken (manueel): Een verkoopfactuur kan manueel aangemaakt worden zonder dat er
een verkooporder voor bestaat. Bij het manueel aanmaken van een verkoopfactuur worden de kop- en regeldetails manueel ingevoerd.

#### 2.6.2 BS25.214 Verkoopfacturen boeken
Het boeken van de factuur zal de financiële afhandeling van de verkooptransactie regelen. Er zijn 4 mogelijkheden om deze facturen te boeken.

- Verkoopfacturen boeken: Een verkoopfactuur wordt geboekt vanaf het overzicht of de kaart van de
niet-geboekte verkoopfacturen. Het boeken van een verkoopfactuur resulteert in een geboekte verkoopfactuur. Voor het boeken van een verkoopfactuur kan een testrapport uitgevoerd worden of kan een voorbeeld van de boekingen opgevraagd worden.
- Verkoopfacturen boeken via verzamelfacturatie: Verzamelfacturering is een periodieke taak die kan
gebruikt worden om alle verzonden artikelen van verschillende verkooporders van eenzelfde klant op één factuur samen te voegen. Deze periodieke taak verzamelt alle niet gefactureerde verzendingen van klanten en maakt hiervoor één of meerdere factureren (afhankelijk van hoeveel verzendingen geboekt werden). Indien er geopteerd wordt voor het boeken van de facturen resulteert dit onmiddellijk in het aanmaken van geboekte verkoopfacturen.
- Verkoopfacturen boeken in batch (verkoopfactuurlijst): Nadat facturen zijn aangemaakt, manueel of via
de periodieke taak voor verzamelfacturering kunnen de facturen in batch geboekt worden. Hierbij worden meerdere facturen in één beweging geboekt vanaf het overzicht van de verkoopfacturen.
- Verkoopfacturen boeken in batch (verkooporderlijst): Vanaf het overzicht van de verkooporders kunnen
facturen in batch geboekt worden. Hierbij worden in één beweging geboekte verkoopfacturen gemaakt voor alle orders waar niet-gefactureerde verzendingen op voorkomen.

#### 2.6.3 BS25.215 Periodieke verkoopfacturen maken
https://learn.microsoft.com/nl-be/dynamics365/business-central/sales-how-to-combine-shipments-on-a- single-invoice

Bij periodieke verkoopfacturatie wordt er op periodieke basis een factuur aangemaakt voor alle producten en diensten die in de afgesproken periode in aanmerking komen voor facturatie. Bijvoorbeeld een maandelijkse

factuur voor het gebruiken van een dienst of verkochte artikelen tijdens deze periode. Hiervoor kan gebruik gemaakt worden van standaardverkoopregels.

##### 2.6.3.1 BC25.215.01 Verzamelfacturatie via factuurgroeperingscode (Cegeka)
Deze functionaliteit biedt meer mogelijkheden om de groepering van bepaalde verzendingen te doen. De factuurgroeperingscode die geselecteerd wordt op de klantenkaart wordt doorgetrokken bij het aanmaken van een verkooporder. De code die zal toegewezen worden in de hoofding van het verkooporder zal op zijn beurt worden doorgetrokken op lijnniveau. Het is mogelijk om op lijnniveau de factuurgroeperingscode nog te veranderen. Het automatisch vullen van de factuurgroeperingscode kan op verschillende manieren, dit is afhankelijk van welke code geselecteerd is op de klantenkaart. De opties die standaard mogelijk zijn:

- Factuurgroeperingscode manueel ingeven
- Factuurgroeperingscode op basis van het ordernummer
- Factuurgroeperingscode op basis van de maand van boeking van verzending
- Factuurgroeperingscode op basis van de week van boeking van verzending
- Factuurgroeperingscode op basis van verzendcode
- Factuurgroeperingscode per vestiging (magazijn)
! Opmerking: Bij de groeperingswijzen ‘Maand’ & ‘Week’ wordt de code pas opgevuld wanneer de verzending effectief is gebeurd. (De verzenddatum zal gebruikt worden voor het aanmaken van een code). Voor de andere wijzen moet de verzending nog niet zijn geboekt voor het invullen van de groperingscode.

#### 2.6.4 BS25.216 Vooruitbetalingsfacturen maken
https://learn.microsoft.com/nl-be/dynamics365/business-central/finance-how-to-create-prepayment-invoices

Vooruitbetalingen zijn betalingen die worden gefactureerd en waarvoor een vooruitbetalingsfactuur wordt geboekt vóór de definitieve facturering.

Het vooruitbetalingspercentage kan worden ingesteld voor een klant, voor alle artikelen, of bepaalde artikelen. Nadat deze instellingen werden gedaan, kunt u vooruitbetalingsfacturen genereren vanuit verkooporders voor het berekende vooruitbetalingsbedrag. U kunt, indien nodig, de bedragen op de vooruitbetalingsfactuur wijzigen door het vooruitbetalingspercentage in het verkooporder te wijzigen. Ook kunt u aanvullende vooruitbetalingsfacturen versturen, als er bijvoorbeeld extra artikelen werden toegevoegd op het order. Commented [NH2]: Het verlagen van een order waarvoor een vooruitbetalingsfactuur bestaat is niet
### 2.7 Verkoopretourorders beheren zo eenvoudig. Dan moet ofwel % verlaagd worden
ofwel creditnota geboekt worden voor de vooruitbetalingsfactuur. Niet onmogelijk, wel voor
#### 2.7.1 BS25.219 Verkoopretourorders maken administratief werk...

https://learn.microsoft.com/nl-be/dynamics365/business-central/sales-how-process-sales-returns-orders

Dit scenario behandelt het aanmaken van een verkoopretourorder. Indien na verzending of facturatie blijkt dat de klant om een bepaalde reden niet tevreden is met de geleverde goederen, kan hiervoor een retourorder worden aangemaakt. Op basis van het retourorder kan er indien nodig ook worden opgevolgd of er goederen moeten worden teruggestuurd en kan er een creditering volgen.

- Verkoopretourorders maken met fysieke ontvangst: Een verkoopretourorder kan gebruikt worden voor
de opvolging van goederen die door een klant worden teruggestuurd naar het bedrijf. Naast het bevestigen van de retour via een retourorderbevestiging kan ook de ontvangst van de geretourneerde goederen opgevolgd worden en kan er uiteindelijk een creditnota worden opgemaakt. Voor het aanmaken van de documentregels kan er gekozen worden om verzendregels van eerdere verkopen op te halen of om de regels van een ander document te kopiëren. Voor het opvolgen van een retour met fysieke ontvangst worden op de retourorder de artikelen vermeld die worden geretourneerd.
- Verkoopretourorders maken zonder fysieke ontvangst: Indien men het retourproces wil opvolgen maar
het niet vereist is dat de klant de goederen terugstuurt, dan kan ook gebruik gemaakt worden van een verkoopretourorder. In dit geval wordt geen gebruik gemaakt van artikelen, maar van artikeltoeslagen of grootboekrekeningen. In dit geval kan er op basis van het retourorder ook een creditnota worden opgemaakt.

### 2.8 Verkoopcreditnota's beheren
#### 2.8.1 BS25.220 Verkoopcreditnota's maken
In geval van fouten bij de facturatie kan er een credit nota’s aangemaakt worden.

Typisch gaat dit dan over:

- Verkeerde BTW

- Verkeerde prijs

- Verkeerde kortingen of bepaalde kortingen vergeten

- Ontbrekende of beschadigde artikelen

Deze creditnota kan op verschillende manieren gemaakt worden:

- Manueel

- Ophalen van ontvangstregels van een verkoopretourorder

- Rechtstreeks factureren/crediteren van een verkoopretourorder.

#### 2.8.2 BS25.221 Vooruitbetalingscreditnota's maken
Als een vooruitbetalingsfactuur geboekt is voor een order, kan er nog steeds een correctie gedaan worden op dat order. Er kunnen regels worden toegevoegd en voor die regels een nieuwe vooruitbetalingsfactuur aanmaken. Eenmaal er voor een regel op het verkooporder een vooruitbetalingsfactuur geboekt is, kan deze niet

meer verwijderd worden. Er moet eerst een creditnota verzonden worden voor die bestaande vooruitbetaling alvorens de regel kan worden verwijderd.

### 2.9 BS25.222 Subscription management
https://learn.microsoft.com/nl-be/dynamics365/business-central/srb/welcome

Subscription Management in Business Central is een geïntegreerde functionaliteit die organisaties helpt bij het beheren van terugkerende inkomstenstromen, zoals abonnementen, servicecontracten of periodieke facturatie. Het doel is om bedrijven die werken met recurring billing – denk aan SaaS-aanbieders, onderhoudsdiensten, of leveranciers van producten met een abonnementsmodel – een gestructureerde en efficiënte manier te bieden om deze processen te automatiseren.

Met Subscription Management kun je abonnementen definiëren, opvolgen en factureren op basis van vooraf ingestelde termijnen en voorwaarden. Dit omvat het vastleggen van start- en einddatums, factureringsfrequenties (maandelijks, jaarlijks, etc.), prijsmodellen en eventuele kortingen. De functionaliteit ondersteunt ook scenario’s waarin klanten meerdere abonnementen hebben, inclusief upgrades, downgrades of opzeggingen, en zorgt ervoor dat wijzigingen correct worden verwerkt in de facturatie.

Er bestaat ook een mogelijkheid voor usage-based billing waarbij kosten afhangen van het daadwerkelijke gebruik, zoals cloudservices, transacties of resourceverbruik.

Merk op: deze functionaliteit heeft een aantal gelijkenissen met de contracten in de servicemodule van BC maar ook een aantal duidelijk verschillen.

2.10Document Lay-outs Verkoop 2.10.1BS25.800 Verkoopofferte Microsoft Lay-Out.

2.10.2BS25.801 Verkooporder Cegeka Lay-out:

2.10.3BS25.802 Verkoopretourorder Microsoft Lay-out.

2.10.4BS25.803 Pro Forma Factuur Cegeka Lay-out:
