## 10. Finance
"Finance" verwijst naar de bedrijfsprocessen voor het beheer van alle financiële standaard processen en informatie zoals het boeken van financiële transacties, het beheren van klant- & leverancierstransacties, kas & bank, budgetten, vaste activa, cashflow, voorraadwaardering.

### 10.1 Finance Instellen
#### 10.1.1 BS65.001 Finance instellen
Er wordt een onderscheid gemaakt tussen finance master data en finance instellingen. Master data zijn variabel en kunnen bijgemaakt worden, bv een grootboekrekening. Instellingen zijn eerder statisch en worden eenmalig opgezet.

Voorbeelden van algemene financiële instellingen:
- Boekhoudinstellingen
- Dagboeksjablonen en -batches
- Nummerreeksen

- Instellingen voor electronisch bankieren

- Boekingsgroepen

Binnen andere domeinen zijn er vaak raakvlakken met Finance die nagekeken moeten worden bv. in:
- Inkoopinstellingen
- Verkoopinstellingen
- Voorraadinstellingen

Per domein binnen Finance komen er ook nog algemene instellingen aan bod binnen dat domein, bv. leveranciersboekingsgroepen, aanmaningscondities,...

- 

10.1.2BS65.009 Beheer Setup BTW Om tot een correcte BTW aangifte te komen moeten een aantal BTW settings ingesteld worden. Cegeka levert een template aan met settings voor de Belgische BTW aangifte. Deze template dient door de klant gevalideerd en eventueel aangevuld te worden.

##### 10.1.2.1 BC65.009.01 Beheer Setup BTW (BE aangifte)
Volgende zaken dienen ingesteld te worden:
- Grootboekrekeningen

- BTW bedrijfsboekingsgroepen (BINNENL, EU, IMPEXP,…)
- BTW productboekingsgroepen (G21, D21,…)
- BTW boekingsgroepinstellingen
- BTW clausules
- BTW aangifte

##### 10.1.2.2 BC65.009.02 Beheer Setup BTW (Buitenlandse aangifte)
Volgende zaken dienen ingesteld te worden:
- Grootboekrekeningen
- BTW bedrijfsboekingsgroepen (bv BE-BINNENL, NL-BINNENL)
- BTW productboekingsgroepen
- BTW boekingsgroepinstellingen
- BTW clausules
- BTW aangifte

Voor een buitenlandse BTW aangifte in een Belgisch bedrijf moet er een aparte setup van BTW boekingsgroepen aangemaakt worden. Op die manier kan de buitenlandse BTW aangifte via een rapport bekomen worden (geen elektronische aangifte). Assumptie is dan wel dat op de facturen de juiste BTW bedrijfsboekingsgroep wordt ingegeven. In geval een bedrijf meerdere eigen BTW nummers heeft, moet er rekening gehouden worden met eventuele aanpassingen op de lay-out van documenten.

Een buitenlands bedrijf met buitenlands BTW nummer kan onder bepaalde voorwaarden opgezet worden in een Belgische database, maar vraagt meer technische aanpassingen (bv. uitschakeling van bepaalde lokalisaties). Het is bijgevolg aangeraden om de lokalisaties te gebruiken van het land waar het bedrijf gesitueerd is.

10.1.3BS65.012 Beheer Setup integratie Inventory - Finance In dit scenario wordt de setup beschreven om voorraad transacties te integreren met de boekhouding.

Boekingsgroepen op de artikelkaart (en klant/leverancierskaart) worden gebruikt om de grootboekrekeningen te sturen. De waarderingsmethode per artikel (FIFO, LIFO, gemiddeld, vast, specifiek) bepaalt aan welke waarde de artikelen in de voorraad gewaardeerd worden.

In de voorraadinstellingen (zie domein Voorraad) wordt bepaald of er een integratie is, en of verwachte kosten geboekt moeten worden.

In onderstaande boekingsschema's beschrijven we de boekingen voor een actual costing voorraadflow. De rekeningnummers die gesuggereerd worden moeten afgestemd worden tijdens de implementatie.

Inkoop Ontvangst

Voorraadrek. 300009 (tussenrek)

Voorraadcorrectiesrek. 444000 (tussenrekening)

Inkoop factuur

Voorraadcorrectiesrek. 444000 (tussenrekening)

Voorraadrek. (tussenrek) 300009

Voorraadrekening 300000

Vereffeningsrekening Directe 609000 Kosten

Ink. rekening 600000

Terug te vorderen BTW 411000

Schuldenrekening 440000

Verbruik op productie à kostprijs van de grondstof order

OHW rekening 320000

Voorraadrekening 300000

Boeken capaciteit

OHW rekening 320000

Vereffeningsrekening Directe 609100 Kosten

Klaarmelden à kostprijs van het productieorder geproduceerd artikel

Voorraadrekening 330009 (tussenrek.)

OHW rekening 320000

Afsluiten prod.order salderen van OHW rekening en opboeken op voorraadrekening

OHW rekening 320000

Voorraadrekening 330009 (tussenrek.)

Voorraadrekening 330000

OHW rekening 320000

Verkoopverzending

KPV rekening (interim) 404999

Voorraadrekening 330009 (tussenrek.)

Verkoopfactuur

Voorraadrekening 330009 (tussenrek.)

KPV rekening (interim) 404999

KPV rekening 710000 of 609200

Voorraadrekening 330000

Tegoedenrekening 400000

Te betalen BTW 451000

Omzetrekening 700000

Voorraadcorrectie Pos./neg. correcties, Herwaarderingen

Voorraadrekening 300000

Waarderingsrekening 609300

### 10.2 Finance Master Data
#### 10.2.1 BS65.100 Beheer Boekhoudperiodes
Per boekhoudjaar dienen er boekhoudperiodes gedefinieerd te worden. Bij begin van volgende boekhoudkundige periode, kunt u de toegang tot vorige boekhoudkundige periode beperken. Op deze manier kunt u verhinderen dat andere departementen nog financiële boekingen maken in periodes in het verleden of de toekomst.

Na het indienen van de btw aangifte kunt u een periode definitief sluiten. Hierdoor kunnen er geen boekhoudkundige transacties gemaakt worden en kan de definitieve rapportering opgesteld worden.

Opmerking: een gesloten periode kunt u terug open zetten om boekhoudkundige correcties uit te voeren.

Wanneer het einde van het boekjaar nadert, kunt u het nieuwe boekjaar aanmaken en deze periode blokkeren om te verhinderen dat iemand al boekhoudkundige transacties maakt in het volgende boekjaar.

Per boekjaar worden meestal 12 periodes ingesteld met een begindatum = 1ste dag van de maand. Er is geen aparte 'afsluitingsperiode'. Indien men afsluitingsboekingen wenst te isoleren kan men deze in een apart journaal verwerken. De jaarafsluitingsboeking (salderen van alle P&L rekeningen) wordt op een speciale datum geboekt = ultimo datum/closing date (bv U31/12/2019, C31/12/2019). Op deze manier kan een rapportage opgevraagd worden incl. of excl. deze afsluitingsboeking.

#### 10.2.2 BS65.109 Beheer Rekeningschema
Bij opstart wordt het rekeningschema van de klant geïmporteerd via Rapid Start. Dit wordt steeds bekeken in samenhang met een mogelijke dimensie setup (=analytische structuur).

Op de grootboekrekeningkaart worden volgende parameters beheerd:
- Rekeningsoort: Rekening / Totalen / Titel / BeginTotaal / Eindtotaal
- Aard van de Rekening: Resultatenrekening / Balansrekening
- Rekeningcategorie en subcategorie: bv Activa, Banken
- Dimensies: verplicht in te vullen, default waarde
- Default BTW tarief
Niet aftrekbaar BTW%

#### 10.2.3 BS65.101 Beheer Dimensies
Dimensies zijn analytische codes die gebruikt worden voor rapportering. Door dimensies te gebruiken kan men het aantal kosten- & omzet-rekeningen beperken en toch de nodige info in de boekhouding registreren.

Dimensies kunnen gekoppeld worden aan grootboekrekeningen, klanten, leveranciers, artikelen, vast actief, divisies, resources,...

Per grootboekrekening, klant,... kan er een regel ingesteld worden om een dimensie verplicht te maken bij boeken van een transactie. Per grootboekrekening, klant,... kan ook een default dimensiewaarde worden meegegeven.

Er zijn 2 'globale' dimensies: deze zijn altijd zichtbaar in de schermen. Hierop is snelle ingave mogelijk zowel op (factuur)header- als lijnniveau en u kan er rechtstreeks op filteren in lijsten en rapportages. Daarnaast zijn er 6 'shortcutdimensies' mogelijk. Deze zijn enkel op (factuur)lijnniveau zichtbaar en daar ook rechtstreeks invulbaar. Indien er meer dan 8 dimensies zijn ingesteld, kunnen deze enkel via een extra ingavescherm ingevuld worden. Rapportage op shortcut- en bijkomende dimensies kan via Analyseviews en Rapportageschema's.

#### 10.2.4 BS65.102 Beheer Vreemde Munt & Wisselkoersen
In de Boekhoudinstellingen wordt de bedrijfsmunt bepaald (LV code= lokale valuta). Alle transacties die geregistreerd worden met een blanco valuta code worden beschouwd als LV. Vreemde valuta kunnen beheerd worden in Valuta's. Hieraan wordt een wisselkoers gekoppeld t.o.v. de LV, en grootboekrekeningen voor wisselkoersverschillen. De LV zelf wordt NIET als valutacode aangemaakt.

Transacties in Vreemde Valuta worden bijgehouden op volgende niveaus:

- klantenposten

- leveranciersposten
- bankposten
- grootboekposten

Naast de LV kan er ook 1 Rapporteringsvaluta worden ingesteld.

In de standaard template zijn enkele valuta voorgedefinieerd. De afrondingsparameters per valuta dienen tijdens de implementatie te worden afgestemd.

### 10.3 Beheer leveranciersboekhouding
#### 10.3.1 BS35.100 Leveranciers beheren
Voor leveranciers kunt u algemene gegevens zoals naam, adres, land en diverse telefoonnummers, e- mailadressen etc. registreren. Ook kunnen er andere leveranciersgegevens bijgehouden worden zoals facturatie- , ontvangst- en betalingsgegevens die belangrijk zijn binnen het inkoopproces.

Een leverancier kan geblokkeerd worden op verschillende niveaus:
- Blokkeren voor betalingen: Op deze manier worden de betalingen aan een leverancier geblokkeerd.
- Blokkeren voor alles: Op deze manier zijn er geen transacties mogelijk.

Vanuit financieel oogpunt zijn volgende parameters van belang:
- Boekingsgroepen: zorgen voor een juiste sturing naar grootboekrekeningen (controlerekening,
omzet/kostenrekening, BTW rekening).
- Betalingscondities: bepalen de vervaldatum en contant korting
- Betalingswijze
- BTW nr., Ondernemingsnummer

De taalcode is van belang voor de document lay-out van inkoopdocumenten. Standaard wordt een lay-out voorzien in NLB, ENU, FRB.

#### 10.3.2 BS65.105 Beheer Leveranciers bankrekeningen
Per leverancier kan men meerdere bankrekeningen beheren. Het is echter niet mogelijk om per factuur te bepalen op welke bankrekening er betaald moet worden. We adviseren dus om per leverancier 1 rekening bij te houden. Aandachtspunt in dit scenario is security: functiescheiding tussen beheer van betalingen en beheer van leveranciersbankrekeningen is aangewezen.

#### 10.3.3 BS65.200 Inkoopfacturen maken
Een inkoopfactuur kan op verschillende manieren geregistreerd worden:

- Rechtstreeks vanuit een inkooporder (niet aangeraden)
- Manuele inkoopfactuur gelinkt met inkooporder via ophalen ontvangstregels
- Manuele inkoopfactuur via ophalen standaard inkoopcodes
- Manuele inkoopfactuur via kopiëren document
- Manuele inkoopfactuur via manuele ingave (zonder inkooporder)
- Via OCR (Add-on Document Capture)

##### 10.3.3.1 BC65.200.01 Inkoopfactuur maken vanaf inkooporder
Indien u rechtstreeks vanuit de inkooporder de factuur wil boeken, dan moet er een exacte match zijn tussen prijs & hoeveelheden. Vermits dit vaak niet het geval gaat zijn is deze werkwijze niet aan te raden.

##### 10.3.3.2 BC65.200.02 Inkoopfactuur maken met ophalen ontvangstregels
Een inkoopfactuur van een leverancier kan verwerkt worden door het aanmaken van een manuele inkoopfactuur en het ophalen van de ontvangstregels. Via de functie "ontvangstregels ophalen" kunnen één of meerdere ontvangsten van de leverancier opgehaald worden. Daarbij worden de aantallen van de ontvangstegels en de prijzen en eventuele kortingen van de gekoppeld inkooporder toegepast. Het totale factuurbedrag (inclusief / exclusief btw) en het btw-bedrag kan gematched worden met de bedragen zoals die op de ontvangen factuur vermeld zijn. Na het invullen van het factuurnummer van de leverancier kan de inkoopfactuur geboekt worden.

##### 10.3.3.3 BC65.200.03 Inkoopfactuur maken (manueel)
Een inkoopfactuur kan ook rechtstreeks opgemaakt worden zonder link met een inkooporder. Dit kan bijvoorbeeld in het geval van een dienstenfactuur of facturen van kosten waar er geen inkooporder van bestaat.

Bij manuele ingave van een inkoopfactuur dient u op de detaillijn aan te geven over welk type factuur het gaat: Artikelen (meestal verwerkt via een order gerelateerde factuur en niet manueel)

- Grootboekrekeningen
- Vaste Activa (zie domein Vast Actief)
- Toeslagen

De BTW berekening is afhankelijk van 2 parameters. De BTW-bedrijfsboekingsgroep is afkomstig van de leverancierskaart, de BTW-productboekingsgroep is afkomstig van het artikel of de grootboekrekening, Deze combinatie zal de BTW berekening bepalen.

Dimensies (=analytische codes) kunnen toegevoegd worden op zowel hoofd- als regelniveau.

Het is mogelijk om voor gedefinieerde standaard inkoopcodes / grootboekrekeningen te linken aan een leverancier, zodat deze kunnen opgehaald worden bij de ingave van een inkoopfactuur. Alternatief is het kopiëren van een bestaand document.

##### 10.3.3.4 BC65.200.04 Inkoopfactuur maken via OCR (Document Capture)
Inkoopfacturen en (-cn’s) kunnen herkend en verwerkt worden via de OCR-tool Document Capture van Continia. Pdf’s die men ontvangt van de leveranciers en ingescande papier facturen moeten worden doorgestuurd naar een specifiek emailadres. De OC engine pikt deze pdf’s onmiddellijk op en verwerkt deze tot een document in Business Central, waar al een initiële mapping van herkende velden zal gebeuren. De gebruiker vult eenmalig deze mapping aan, zowel op header- als lijnniveau, zodat er een bruikbare template wordt gecreëerd waarmee toekomstige facturen van deze leverancier op een efficiënte manier verwerkt kunnen worden.

Facturen in Peppol formaat kunnen eveneens via Document Capture worden verwerkt. Bij voorkeur komen deze rechtstreeks binnen via het Continia Delivery Network (gecertifieerd Peppol access point) waar u zich als klant op kan registreren. Zie ook hoofdstuk Peppol onder sectie Beheer Klantenboekhouding.

#### 10.3.4 BS65.201 Inkoopcreditnota's maken
Een inkoopcreditnota wordt gemaakt in het geval dat er een correctie moet uitgevoerd worden op een inkoopfactuur.

Het creëren en verwerken van een manuele creditnota zonder inkoopretourorder is gelijkaardig aan het registreren van een manuele factuur. U kunt manueel een lijn creëren, manueel het type factuur bepalen en de leverancier en product BTW boekingsgroep zal de BTW percentage en rekeningen bepalen.

Daarnaast is het ook mogelijk om de lijnen van een bestaand document te kopiëren.

Wanneer de creditnota ontvangen wordt van de leverancier voor geretourneerde artikelen (via retourorder) dan kunnen de retourlijnen opgehaald worden op de creditnota.

U kunt één of meerdere openstaande leveranciersposten vereffenen bij het boeken van de creditnota.

De creditnota kan afzonderlijk geboekt worden of in batch.

#### 10.3.5 BS65.202 Goedkeuringaanvraag verzenden
In bepaalde situaties kan het voorvallen dat er een goedkeuring vereist is van een andere persoon alvorens er een inkoopfactuur kan geboekt worden. In Business Central worden hiervoor werkstromen gedefinieerd. De gebruiker die de factuur ingeeft stuurt een aanvraag tot goedkeuring naar de gebruiker met de juiste machtiging hiervoor. Afhankelijk van de setup van goedkeuringslimieten kan het nodig zijn dat meerdere gebruikers moeten goedkeuren.

#### 10.3.6 BS65.203 Inkoopfactuur goedkeuren voor boeken
Elke goedkeurder heeft een overzicht van de door hem goed te keuren facturen. Een factuur kan goedgekeurd of geweigerd worden. Van zodra de inkoopfactuur goedgekeurd is, krijgt deze de status 'Vrijgegeven' en kan ze geboekt worden. Deze goedkeuringsflow heeft enkel betrekking op het goedkeuren voor boeken van de factuur en staat dus los van een goedkeuring voor betaling.

#### 10.3.7 BS65.204 Inkoopfacturen boeken
Inkoopfacturen kunnen individueel geboekt worden of in batch.

#### 10.3.8 Inkoopfactuur goedkeuren voor betaling
De Cegeka Finance Suite biedt de mogelijkheid om goed te keuren na het boeken van de facturen, dus een goedkeuring te doen voor vrijgave voor betaling. Wanneer een factuur wordt geboekt, wordt deze automatisch geblokkeerd voor betaling (het veld 'Afwachten' wordt automatisch ingevuld op de leverancierspost). Goedkeuring houdt dan in dat het veld 'Afwachten' wordt leeggemaakt, zodat de factuur kan worden voorgesteld in de betalingsbatch.

Goedkeuringsflows kunnen op verschillende manieren worden ingericht:

- De eerste goedkeurder kan worden ingesteld via de inkoper op de leverancier en kan tijdens het
boekingsproces nog worden gewijzigd door de gebruiker. Een tweede goedkeurder ontvangt een goedkeuringsverzoek nadat de eerste heeft goedgekeurd. De goedkeuringsprocedure werkt dus via een hiërarchie waarbij per gebruiker een maximale goedkeuringslimiet kan worden ingesteld.

- Als alternatief kan goedkeuring plaatsvinden via een vaste goedkeuringsgroep, die bv. gekoppeld
wordt aan een dimensie of een ander veld op de factuurhoofding.

Indien de factuur volledig matcht met het inkooporder kan via een specifieke setup de goedkeuringsflow geskipt worden.

Er is niet echt een geautomatiseerde Out of Office functionaliteit in bovenstaande goedkeuringsmodule. Wel kunnen goedkeuringsaanvragen gedelegeerd worden naar de vaste vervanger die aan de goedkeurder is gekoppeld.

Indien men ook een goedkeuringsflow wenst op inkoopcreditnota’s zal dit niet via bovenstaande flow kunnen verlopen, omdat een creditnota niet betaald wordt. Men wil in dit geval eerder weten dat de creditnota er is, om eventueel een hiermee gerelateerde inkoopfactuur goed te keuren. Men kan dan bv via de Teams integratie deze info meegeven aan de goedkeurder zonder dat er een echte goedkeuringsflow wordt opgestart, of de standaard goedkeuringsflow (voor boeken van de creditnota) gebruiken.

#### 10.3.9 BS65.205 Vooruitbetalingsfacturen maken
Vooruitbetalingsfacturen worden vanop een inkooporder gegenereerd als een inkoopfactuur, vooraleer op dit order een goederenontvangst werd geregistreerd. Voorbeelden: voorschot/schijvenfacturatie, overseas facturatie.

Omdat deze functionaliteit niet compatibel is met Document Capture (want factuur wordt rechtstreeks vanuit het inkooporder geboekt obv een vooruitbetalingspercentage) wordt deze zelden geïmplementeerd.

Er zijn verschillende mogelijke werkwijzes voor het behandelen van overseas facturatie, waarbij de factuur al door de leverancier werd gestuurd, maar de goederen nog onderweg zijn.

Preferente werkwijze:

- Boek de factuur als een manuele factuur zonder 3 way matching, op een balansrekening

- Van zodra de goederen ontvangen zijn, boek een nul factuur, waarbij de 3 way match gebeurt en
bovenstaande balansrekening in min wordt toegevoegd zodat de factuur op 0 valt

Alternatief 1:

- Boek de factuur nog niet en wacht tot de goederen ontvangen zijn. Meestal gaat men immers nog niet
betalen vooraleer de goederen zijn ontvangen.

Alternatief 2:

- Boek de ontvangst van zodra de factuur binnenkomt op een apart magazijn, en voer de 3 way match uit

- Doe een transfer naar het juiste magazijn van zodra de goederen binnenkomen

#### 10.3.10 BS65.207 Uitvoeren leveranciersbetalingen
Een SEPA betaalvoorstel kan aangemaakt worden in het betalingsdagboek. Met de functie 'Betalingsvoorstellen Maken' worden openstaande leverancierstransacties voorgesteld, rekening houdend met een aantal filtercriteria:
- Vervaldatum
- Vervaldatum contant korting
- Velden op de leverancierskaart, bv. landencode, betalingswijze, ...
Wanneer een voorschot moet betaald worden en u heeft nog geen factuur ontvangen, dan kunt u de leverancier en het bedrag manueel toevoegen in het betalingsdagboek.

Na controle van de betalingsregels kunt u het betalingsbestand (.xml file) aanmaken en inladen in de banksoftware. Tijdens de creatie van de .xml wordt het betalingsvoorstel klaargezet in een divers journaal. Na doorboeken van dit journaal worden de leveranciersfacturen afgepunt en overgeboekt naar een rekening "Betalingen onderweg".

#### 10.3.11 BS65.208 Opvolgen openstaande leveranciersfacturen
Aan de hand van verschillende rapporten kunt u op geregelde tijdstippen het openstaand saldo van leveranciers opvragen. De meest gebruikte rapporten zijn:
- Vervallen betalingen (aging)
- Leverancier - Saldo t/m datum
- Leverancier - Open posten
- Leverancier - Proefbalans

Openstaande posten kunnen manueel met elkaar afgepunt worden, zodat enkel de lijnen met een restbedrag zichtbaar zijn in de overzichtslijsten.

##### 10.3.11.1 BC65.208.01 Afpunten openstaande leveranciersposten
Openstaande documenten kunnen manueel met elkaar vereffend worden. Deze situatie komt voor bv. indien een betaling of een creditnota werd geregistreerd zonder link naar een factuur.

##### 10.3.11.2 BC65.208.02 Blokkeer factuur voor betaling
Op de leveranciersposten zijn slechts enkele velden editeerbaar, bv:
- de vervaldatum

- het veld 'Afwachten': dit geldt als blokkeringscode. Indien dit veld is ingevuld (3 karakters) wordt deze
factuur niet mee opgenomen in het betaalvoorstel. Dit veld wordt ook gebruikt door de goedkeuringsflow van de Cegeka Finance Suite, cfr hierboven. Nadat een goedkeuringsflow is doorlopen kan men alsnog een factuur blokkeren voor betaling door het veld Afwachten manueel in te vullen.

### 10.4 Beheer klantenboekhouding
#### 10.4.1 BS25.100 Beheren klant master data
Zie ook Order 2 Cash

Voor klanten kan men algemene gegevens zoals naam, adres, land en diverse telefoonnummers, e-mailadressen etc. registreren. Ook kunnen er andere klantgegevens bijgehouden worden zoals facturatie-, verzend- en betalingsgegevens die belangrijk zijn binnen het verkoopproces.

Vanuit financieel oogpunt zijn volgende parameters van belang:
- Boekingsgroepen: zorgen voor een juiste sturing naar grootboekrekeningen (controlerekening,
omzet/kostenrekening, BTW rekening).
- Betalingscondities: bepalen de vervaldatum en contant korting
- Betalingswijze (bv. Domiciliëring)
- BTW nr., Ondernemingsnummer
- Aanmaningscondities
De taalcode is van belang voor de document lay-out van verkoopdocumenten. Standaard wordt een lay-out voorzien in NLB, ENU, FRB.

#### 10.4.2 BS65.106 Beheer Klanten Bankrekeningen
Wanneer men werkt met domiciliëringen, is het vereist om klantenbankrekeningen bij te houden in Business Central. Aan deze klantenbankrekening wordt dan een mandaat gekoppeld dat nodig is om domiciliëringen te kunnen uitvoeren. Klantenbankrekeningen kunnen ook aangewend worden als herkenningspunt bij de import van CODA bestanden.

Op de klantenkaart kan men in het scherm 'Bankrekeningen' de klantenbankrekening ingeven. Vereiste parameters zijn:
- Code
- Naam
- Land
- Swift

- Iban

10.4.3BS65.004 Beheer Setup Administratiekosten In Business Central is het mogelijk om per klant/leverancier een bedrag aan administratiekosten in te stellen, geldend vanaf een bepaald minimumbedrag op de factuur/het order. Deze wordt per klant/leverancier ingesteld in het scherm Factuurkorting.

#### 10.4.4 BS65.108 Beheer Kredietlimieten
Per klant kan een kredietlimiet ingesteld worden. Van zodra een kredietlimiet overschreden wordt, kan het systeem zo ingesteld worden dat de gebruiker een waarschuwing krijgt.

Er kan een goedkeuringsflow worden ingesteld voor het wijzigen van de kredietlimiet op de klantenkaart. Er kan ook een goedkeuringsflow worden ingesteld op transacties waarbij de kredietlimiet is overschreden.

#### 10.4.5 BS65.209 Registreer manuele verkoopfactuur
Een verkoopfactuur kan op verschillende manieren geregistreerd worden:

- Uit een verkooporder
- Uit een manuele verkoopfactuur via ophalen verzendregels
- Uit een manuele verkoopfactuur zonder verkooporder
- Uit een verzamelfacturatie
Zie domein Verkoop voor een beschrijving van order gerelateerde verkoopfacturen. Dit scenario behandelt enkel de manuele facturen, zonder verkooporder.

Een verkoopfactuur kan manueel aangemaakt worden zonder dat er een verkooporder voor bestaat.

Bij het manueel aanmaken van een verkoopfactuur worden de kop- en regeldetails manueel ingevoerd.

U dient op de detaillijn aan te geven over welk type factuurregel het gaat. Zo heeft u de keuze tussen:

- Artikelen (meestal verwerkt via een order gerelateerde factuur en niet manueel)
- Grootboekrekeningen
- Vaste Activa
- Resource
- Toeslagen

Afhankelijk van het gekozen type, zullen bepaalde parameters ingevuld worden. Zo zal bij de keuze van een artikel, de artikelprijs opgehaald worden en moet men bij een grootboekrekening zelf de nettowaarde ingeven.

De BTW berekening is afhankelijk van 2 parameters. De BTW-bedrijfsboekingsgroep is afkomstig van de klantenkaart, de BTW-productboekingsgroep is afkomstig van het artikel of de grootboekrekening. Deze combinatie zal de BTW berekening bepalen.

Dimensies (=analytische codes) kunnen toegevoegd worden op zowel hoofd- als regelniveau.

Bij het ingeven van wederkerende boekingen is het mogelijk om voor gedefinieerde standaard verkoopcodes / grootboekrekeningen te linken aan een klant, zodat deze kunnen opgehaald worden bij de ingave van een verkoopfactuur. Alternatief is het kopiëren van een bestaand document.

#### 10.4.6 BS65.211 Registreer manuele verkoopcreditnota
Een verkoopcreditnota kan op verschillende manieren ontstaan:

- Uit een verkoopretourorder
- Uit een manuele verkoopcreditnota via: Ophalen retourontvangstregels
- Uit een manuele verkoopcreditnota via: Geboekte documentregels ophalen voor tegenboeking
- Via document kopiëren
- Uit een verkoopcreditnota met manuele ingave van de lijnen

Zie domein Verkoop voor een beschrijving van order gerelateerde verkoopcreditnota's. De verwerking van een manuele verkoopcreditnota is gelijkaardig aan een manuele verkoopfactuur.

Een creditnota voor een prijscorrectie op artikelen kan geregistreerd worden op een grootboekrekening, of via een artikeltoeslag. Dit mag niet gebeuren op het artikel zelf, vermits dit een voorraadbeweging zou genereren.

#### 10.4.7 Peppol
Belgische ondernemingen zullen vanaf 2026 de verkoopfacturen en -creditnota’s in Peppol formaat moeten versturen naar bedrijfsklanten. De e-document module van Continia voldoet wat dit betreft aan de nodige vereisten. Deze module is inbegrepen in de licentie voor Document Capture (OCR). Continia heeft bovendien een eigen gecertifieerd access point (Continia Delivery Network) waarlangs alle Peppol verkeer, zowel inkomend als uitgaand, passeert. Via het verzendprofiel van de klant (en leverancier) wordt bepaald of de documenten via Peppol (of alsnog via mail/post) worden verstuurd.

10.4.8BS65.007 Klantendomiciliëring (Direct Debit) In de Belgische localisatie is voorzien dat SEPA domiciliëringen kunnen uitgevoerd worden via Isabel. Business Central kan een xml file aanleveren die in de Isabel software kan geïmporteerd worden.

Volgende zaken moeten ingesteld worden:

- Betalingswijze

- Domiciliëringsdagboek

- Klant bankrekening

- Mandaten

- Correcte parameters op klanten: naam, land, partnersoort, betalingswijze

Correcte parameters op eigen bankrekeningen: naam, land, IBAN, Swift, Exportindeling van SEPA Europese domiciliëring, Crediteurnummer.

Via het domiciliëringsdagboek kan een domiciliëringsvoorstel aangemaakt worden. Dit XML bestand kan vervolgens opgeladen worden in Isabel. Indien er geen problemen waren bij het opladen van het bestand kunnen de verkoopfacturen op de klant afgeboekt worden en tegengeboekt op een wachtrekening 'Klantdomiciliaties onderweg’.

#### 10.4.9 BS65.213 Opvolgen openstaande klantenvorderingen
Aan de hand van verschillende rapporten kunt u op geregelde tijdstippen het openstaand saldo van klanten beheren. De meest gebruikte rapporten zijn:
- Vervallen vorderingen (aging)
- Klant - Saldo t/m datum
- Klant - Vervallen posten
- Klant - Proefbalans

Openstaande documenten kunnen manueel met elkaar vereffend worden. Deze situatie komt voor bv. indien een betaling of een creditnota werd geregistreerd zonder link naar een factuur.

#### 10.4.10 BS65.214 Beheer van aanmaningen
In Business Central is het mogelijk om aanmaningen te laten genereren voor vervallen facturen.

Op de klant wordt een aanmaningsconditie ingesteld. Deze bepaalt op haar beurt volgende parameters:

- Aanmaningsniveaus: per niveau kunt u de toeslag, rente, respijt periode en teksten instellen
- Toeslagen toepassen, al dan niet onmiddellijk geboekt in het grootboek
Rente aanrekenen, al dan niet onmiddellijk geboekt in het grootboekBij het definiëren van de teksten kan men volgende variabelen gebruiken:

Variabele Waarde %1 Inhoud van het veld Documentdatum in de aanmaningskop %2 Inhoud van het veld Vervaldatum in de aanmaningskop %3 Inhoud van het veld Rente in de relateerde rentefactuurcondities

%4 Inhoud van het veld Restbedrag in de aanmaningskop %5 Inhoud van het veld Rentebedrag in de aanmaningskop %6 Inhoud van het veld Toeslag in de aanmaningskop %7 Het totaalbedrag van de aanmaning %8 Inhoud van het veld Aanmaningsniveau in de aanmaningskop %9 Inhoud van het veld Valutacode in de aanmaningskop %10 Inhoud van het veld Boekingsdatum in de aanmaningskop %11 De bedrijfsnaam %12 Inhoud van het veld Toeslag per regel in de aanmaningskop

Men kan onbeperkt verschillende aanmaningsniveaus aanmaken. Alle vervallen verkoopfacturen komen op eenzelfde aanmaning terecht. De aanmaningstekst is afhankelijk van in welk niveau de oudste vervallen factuur valt.

Men kan een klant uiteindelijk blokkeren voor verdere verkooptransacties.

Aanmaningen worden gemaakt vanuit een aanmaningsvoorstel. Dit is een batchproces waarin men op basis van filters de aanmaningsbrieven kan laten voorstellen. Men kan volledige aanmaningen verwijderen, of binnen 1 aanmaningsbrief bepaalde verkoopfacturen/creditnota's verwijderen.

Facturen die betwist werden, en waarvoor het veld 'Afwachten' werd ingevuld, zullen niet worden opgenomen in het aanmaningsvoorstel, tenzij men dit expliciet aanduidt.

Van zodra de aanmaning klaar is, kan deze verzonden (bevestigd) worden en afgedrukt of gemaild naar de klant.

#### 10.4.11 BS65.215 Beheer van rentefacturen
A.d.h.v. rentecondities kan men rentefacturen aanmaken, waarbij men rente aanrekent op de te laat betaalde facturen. Dit zijn aparte 'facturen' die als extra openstaande post op de klant zullen verschijnen.

Rentefacturen worden gemaakt vanuit een rentefactuurvoorstel. Dit is een batchproces waarin men op basis van filters de rentefacturen laat genereren. Na doorboeken (Verzenden) wordt dit een klantenpost van het type Rentefactuur.

De afdruk van het document gebeurt vanuit de Verzonden rentefacturen (aparte lay-out).

### 10.5 Beheer grootboek
- 

#### 10.5.1 BS65.216 Registeren van een diverse boeking
Diverse boekingen kunnen op verschillende manieren geregistreerd worden:
- Via manuele ingave in een divers dagboek
- Via ophalen van een standaarddagboek in een divers dagboek
- Via copy/paste vanuit Excel in een divers dagboek
- Via een periodiek dagboek

Wanneer een diverse (of andere) boeking geboekt is, is deze definitief. Enkel de lijnomschrijving kan nog aangepast worden. Sinds Business Central versie 18 kan men de geboekte dimensies rechtstreeks wijzigen in de grootboekposten, waar dit voorheen met een extra diverse boeking moest gebeuren.

In een diverse boeking kunnen ter informatie aantallen meegegeven worden. Deze worden behouden in de geboekte journaalpost. Let wel: geboekte posten die voortvloeien uit facturen, bevatten geen aantallen, omdat deze info vervat zit in de factuurtabellen.

##### 10.5.1.1 BC65.216.01 Verwerk divers dagboek
Diverse journalen kunnen gebruikt worden voor het maken van correcties of provisies op:
- Grootboekrekening
- Klant
- Leverancier
- Bank

Indien meerdere personen tegelijkertijd in hetzelfde divers dagboek werken, is het aangewezen om met meerdere dagboekbatches te werken binnen 1 journaal, met een voorlopige nummering.

##### 10.5.1.2 BC65.216.02 Standaarddagboeken ophalen
Boekingen kunnen als template opgeslagen worden in een standaard dagboek zodat deze hergebruikt kunnen worden.

##### 10.5.1.3 BC65.216.03 Verwerk periodiek divers dagboek
Indien menwederkerende boekingen wenst aan te leggen, kan men gebruik maken van een periodiek divers dagboek. Voorbeelden: lonen, provisies, ...

De mogelijke periodieke methodes van deze boekingen zijn:
- Vast

- Variabel
- Saldo
- Omgekeerd Vast
- Omgekeerd Variabel
- Omgekeerd Saldo

De periodieke methode bepaalt enerzijds of de bedragen vast, variabel zijn of het saldo van de rekening moeten bevatten en anderzijds of de boeking ook omgekeerd moet gebeuren, m.a.w. moet tegengeboekt worden op de daaropvolgende dag.

De periodiciteit wordt in het veld Frequentie gedefinieerd aan de hand van een datumformule. Om de boekingsdatum van de eerstvolgende boeking automatisch op laatste dag van de maand te zetten is datumformule 1M+LM aangewezen.

In een periodiek dagboek is het eveneens mogelijk om via verdeelsleutels een rekeningsaldo te verdelen over andere rekeningen of uit te splitsen over bepaalde dimensiewaarden.

#### 10.5.2 BS65.217 Opladen algemene boekingen
Met de Rapid Start tool kunnen diverse boekingen vanuit een vaste voorgedefinieerde lay-out in Excel in Business Central ingelezen worden. In dit Excel bestand kan men volgende elementen meegeven:

- Transactiedatum
- Grootboekrekening
- Analytische dimensies
- Bedragen
- Munt
- Omschrijving
- Tegenrekeningen indien gewenst

Voorbeelden: U krijgt een bestand van het sociaal secretariaat voor het verwerken van de lonen.

Deze functie kan ook gebruikt worden om op het einde van de maand/periode een aantal kosten te verdelen naar andere grootboekrekeningen/analytische dimensies: de verdeling wordt voorbereid in Excel en wordt vervolgens opgeladen in Business Central.

Volgende stappen moeten uitgevoerd worden bij het importeren van diverse boekingen:

- Maak een Rapid Start template aan voor het inlezen van de boekingen, waarin bepaald wordt welke
velden worden ingelezen. Dit dient te gebeuren per bedrijf.

- Vul de template in met boekingsdata.
- Laad de ingevulde template op in de Rapid Start tool.
- Valideer of de boeking correct opgeladen is.
- Na validatie kunt u de boekingen doorboeken naar grootboek.

Men kan ook gebruik maken van de copy-paste functionaliteit vanuit Excel, op voorwaarde dat de Excel layout exact overeenkomt met de kolommen in het divers dagboek in Business Central.

#### 10.5.3 BS65.218 Financiële rapporten aanmaken
In Business Central is het mogelijk om zelf rapportages samen te stellen a.d.h.v. Financiële Rapporten en Analyseweergaves. Met deze rapporteringsmogelijkheden kan men grootboekposten combineren met budgetposten en dimensies.

##### 10.5.3.1 BC65.218.01 Beheer Financiële rapporten
Volgende zaken moeten worden opgezet:

- Rijdefinitie: bepaalt de lijnen van het rapport (welke grootboekrekeningen/totalen/formules, evt.
gefilterd op bepaalde dimensies)
- Kolomdefinitie: bepaalt de aard van de bedragen in de kolommen (budget/actual, mutatie/saldo/
YTD...)
- Analyseweergave: geeft de mogelijkheid om ook andere dimensies buiten de globale dimensies te
betrekken in het rapport

##### 10.5.3.2 BC65.218.02 Beheer Analyseweergaves
Analyseweergaves zijn vooral bedoeld om te rapporteren op analytische dimensies (max 4 per analyseweergavecode). De analyse per dimensie wordt opgebouwd op basis van een tussentabel, die gerefreshed moet worden om de meest recente cijfers te kunnen rapporteren. Analyseresultaten kunnen geëxporteerd worden naar Excel, waar ze nog verder bewerkt en geanalyseerd kunnen worden.

### 10.6 Beheer bank transacties
#### 10.6.1 BS65.110 Beheer Banken
Volgende zaken moeten ingesteld worden per bankrekening:

- Bankboekingsgroep
- Bankfiche
- Financieel dagboek

#### 10.6.2 BS65.219 Verwerk en boek financiële dagafschriften
Dit scenario beschrijft het verwerken van financiële dagafschriften. In de Belgische lokalisatie wordt dit afgehandeld in een apart financieel journaal per bank.

##### 10.6.2.1 BC65.219.01 Verwerk en boek financieel dagafschrift (manueel)
Bij de manuele ingave van een bankafschrift dient men per transactie aan te geven over welk soort bankverrichting het gaat:
- Klantenbetalingen
- Leveranciersbetalingen
- Transacties op Grootboekrekening

Aan de hand van het start- en eindbedrag van het dagafschrift zal een balanscontrole uitgevoerd worden voor het verwerken van het financiële dagafschrift.

Bij klanten betalingen kunnen volgende scenario's voorkomen:
- Klant betaalt verkoopfactuur (en trekt creditnota's af)
- Klant betaalt verkoopfactuur gedeeltelijk
- Klant betaalt met korting voor contant/zonder korting voor contant
- Klant betaalt met korting voor contant ondanks dat de datum hiervoor vervallen is/het niet is
toegestaan om een korting voor contant te gebruiken
- Klant betaalt de factuur maar er is een toegestaan betalingsverschil
- Wanneer er gebruik gemaakt wordt van direct debit (domiciliëringen) dan zijn de klanten facturen al
vereffend in een tijdelijke rekening "Ontvangsten onderweg". Bij het verwerken van de financiële dagafschriften zal deze rekening tegengeboekt worden.
- Klant betaalt voorschot

Voor transacties in vreemde valuta moet de wisselkoers die de bank heeft toegepast, ingevoerd worden. Het verschil (positief/negatief) tussen de koers van de verkoopfactuur en de koers van de bank, zal automatisch worden weggeboekt op een rekening Koersverschillen.

Leveranciersbetalingen worden meestal via Isabel afgehandeld (zie scenario Uitvoeren leveranciersbetalingen). De leveranciersfacturen zijn al vereffend, en tegen geboekt op de rekening "Betalingen onderweg" wanneer het betalingsbestand verwerkt is. De groepsbetaling die op het bankuittreksel verschijnt, wordt op dat moment dus op de rekening "Betalingen onderweg" tegen geboekt.

Als de leverancier manueel betaald wordt of via domiciliëring, dan zal bij ingave van het financieel dagafschrift de leveranciersfactuur rechtstreeks worden afgepunt.

Transacties op grootboekrekening kunnen ingegeven worden met of zonder BTW (bv. bankkosten).

##### 10.6.2.2 BC65.219.02 Verwerk financieel dagafschrift via CODA
CODA-afschriften worden elektronisch ontvangen in de bank applicatie. Na opladen en verwerken van een CODA- bestand kan het systeem het financieel dagboek automatisch opvullen.

Op basis van bepaalde parameters en identificatiecodes (type, familie, transactiecode, ...) in de CODA instellingen, zullen banktransacties automatisch herkend worden en het correcte type transactie worden toegekend.

Bij het ontvangen van klanten betalingen zal de juiste klant gevonden worden door volgende zoekactie:

- IBAN nummer
- Bankrekeningnummer
- Naam
- Adres

Volgende functionaliteit is niet standaard voorzien in Business Central en kunt u enkel gebruiken indien u beschikt over de Cegeka Finance Suite Add-on: Indien het een klantentransactie betreft, zal het systeem op basis van de gestructureerde mededeling (OGM) de overeenkomstige factuur opzoeken en matchen met de betaling. Bij het boeken van het financieel dagboek wordt de factuur vereffend. Het is dan uiteraard noodzakelijk om op het verkoopdocument een OGM-code te genereren en af te drukken.

Gebaseerd op volgende zoekactie worden de facturen gevonden voor vereffening:

- OGM: Gestructureerde mededeling (Cegeka Finance Suite)
- Bedrag (met korting contant verrekend)
- Bedrag (zonder korting contant)

Als er geen factuur kan gevonden worden zal er een manuele vereffening moeten gebeuren.

#### 10.6.3 BS65.220 Verwerk en boek KAS verrichtingen
De werkwijze voor registreren van Kas verrichtingen is identiek aan de manuele registratie van bankverrichtingen.

### 10.7 Beheer periodieke taken
#### 10.7.1 BS65.221 Afdrukken dagboeken
De Belgische lokalisatie voorziet alle wettelijke journalen die door de fiscale administratie kunnen opgevraagd worden:

- Inkoopdagboek
- Verkoopdagboek
- Divers dagboek
- Financieel dagboek
- Centralisatiedagboek

#### 10.7.2 BS65.222 Aanmaken periodieke BTW aangifte
De BTW-aangifte kan maandelijks of per kwartaal worden opgesteld op basis van de geboekte BTW-transacties. Het resultaat kan men bekijken in het BTW-aangiftevoorbeeld. Via de datumfilters bepaalt men de periode.

De Belgische lokalisatie voorziet de mogelijkheid om een Intervat bestand aan te maken dat kan worden opgeladen op de website van de BTW administratie.

##### 10.7.2.1 BC65.222.01 Aanmaken BTW aangifte - België
Naast het opstellen van de BTW-aangifte voorziet de Belgische lokalisatie in Business Central verschillende controlerapporten:
- Aankoopjournaal
- Verkoopjournaal
- Financieel journaal
- Divers journaal
- Lijst Aangifte-Samenvatting met logische controles Intervat
- Gedetailleerd rapport (afdruk aangifte in pdf)
- Controlelijst omzet en BTW

Indien u correcties wenst in te geven, kan dit via:
- Een diverse verrichting (zichtbaar in de boekhouding)
- Op de aangifte zelf (niet zichtbaar in de boekhouding)
- Een corrigerende creditnota

##### 10.7.2.2 BC65.222.02 Aanmaken BTW aangifte - Buitenlandse BTW
Een bedrijf met een Belgisch BTW nummer kan ook activiteiten in het buitenland hebben, op een buitenlands BTW nummer.

Door het aanmaken van specifieke BTW-boekingsgroepen voor de BTW registratie met het buitenlands BTW- tarief, wordt het mogelijk om zowel aftrekbare BTW als verschuldigde BTW op aparte grootboekrekeningen te boeken. Hierdoor kunnen we steeds een gedetailleerd BTW overzicht bekomen.

Voorbeeld: BE-BINNENL, BE-EU, BE-IMPEXP en NL-BINNENL, NL-EU, NL-IMPEXP.

Er kan een apart BTW sjabloon opgezet worden voor de buitenlandse BTW aangifte met enkel die specifieke BTW combinaties, die dan via rapportering kan worden gegenereerd en manueel worden ingegeven op de website van de buitenlandse BTW administratie.

#### 10.7.3 BS65.223 Aanmaken BTW jaaraangifte (jaarlijkse
Klantenlisting) De jaarlijkse klantenlisting is een lijst waarop alle klanten met een Belgische BTW nummer vermeld staan, aan wie de onderneming goederen heeft geleverd of diensten heeft verstrekt tijdens het opgegeven kalenderjaar. Enkel klanten met een omzet vanaf 250 euro (excl. btw) moeten opgenomen worden.

Enkel Belgische BTW-plichtige klanten met een ondernemingsnummer in Business Central, worden opgenomen in de jaaraangifte.

Na controle en eventuele correcties, wordt de BTW jaaraangifte ingediend door middel van een .xml bestand dat wordt ingeladen op INTERVAT.

#### 10.7.4 BS65.224 Aanmaken BTW Intracommunautaire Listing
De BTW Intracommunautaire Listing is een aangifte van alle verkopen die uw onderneming met klanten (met BTW nummer) in andere landen van de EU heeft verricht. Deze transacties worden onderverdeeld in goederen en diensten.

De Intracommunautaire Listing genereert een .xml bestand dat kan worden opgeladen in INTERVAT. Filter op BTW Bedrijfsboekingsgroep EU (en BTW Produktboekingsgroep <> GEEN) om enkel de EU transacties mee te nemen in de aangifte.

Correcties zijn mogelijk via het scherm BTW Correctie.

#### 10.7.5 BS65.225 Aanmaken INTRASTAT aangifte
De Intrastataangifte bevat alle goederenoverbrengingen binnen de EU voor zowel ontvangsten (stelsel 19: Inkoop) als verzendingen (stelsel 29: Verkoop). De INTRASTAT aangifte is verplicht wanneer een bepaalde drempel, vastgesteld op jaarbasis, wordt overschreden.

Aan de hand van parameters kan u aangeven of u de vereenvoudigde of gedetailleerde Intrastataangifte moet indienen.

De aangifte zelf doet men in de Intrastatrapportlijst. In dit scherm worden de EU goederenbewegingen (inkoop en verkoop) per periode opgehaald.

De voorgestelde lijnen kan men nog bewerken: transacties toevoegen, verwijderen, correcties doorvoeren, ...

Daarna kan men een .xml bestand genereren voor de aankoop Intrastat aangifte en verkoop Intrastat aangifte, die via het web kan worden opgeladen bij de bevoegde instantie.

#### 10.7.6 BS65.226 Wisselkoersen herwaarderen
Op elke vreemde valuta kan een wisselkoers worden ingegeven die geldt vanaf een bepaalde datum.

Periodiek kunnen de banken en open klanten- en leveranciersposten in vreemde valuta geherwaardeerd worden aan de herwaarderingskoers die op dat ogenblik in Business Central van toepassing is, zodat de waarde in dossiermunt correct wordt weergegeven in de balans per openstaande klanten-, leveranciers-, bankpost.

Bij de automatische herwaardering zal er per valutacode een correctieboeking gebeuren waardoor de waarde in de dossiermunt correct (aan de juiste koers) wordt weergegeven.

Onderstaande zaken worden meegenomen in de automatische herwaardering:

- Openstaande klantenposten (niet gerealiseerde wisselkoersverschillen)
- Openstaande leveranciersposten (niet gerealiseerde wisselkoersverschillen)
- Bankposten (gerealiseerde wisselkoersverschillen)

Zie ook Beheer Vreemde Munt & Wisselkoersen.

#### 10.7.7 BS65.227 Kosten verdelen over dimensies
In Business Central is het mogelijk om een verdeling te boeken van rekeningbedragen over verschillende dimensies heen.
- Dit kan manueel via een divers dagboek, evt. via copy/paste vanuit Excel.
- Via het periodiek dagboek kunnen verdeelsleutels gebruikt worden
- Via de module Kostprijsboekhouding kunnen dynamische verdeelsleutels berekend en toegepast
worden
- Via de Cegeka Finance suite functionaliteit ‘allocatieschema’s’ kunnen o.b.v. voorgedefinieerde
verdeelsleutels de kosten per boekingslijn verdeeld worden

#### 10.7.8 BS65.228 Kosten verdelen over periodes
In Business Central is het mogelijk om aan de hand van een uitstelsjabloon, kosten te verdelen over meerdere periodes.

Deze functionaliteit is voorhanden in de aankoopfacturen/creditnota's, verkoopfacturen/creditnota's en het divers dagboek.

In het uitstelsjabloon worden volgende parameters meegegeven :

- Uitstelrekening

- Uitstelpercentage

- Berekeningsmethode (Lineair, Gelijk per periode, dagen per periode, door gebruiker gedefinieerd)

- Begindatum (Boekingsdatum, Begin van de periode, Einde van de periode, Begin van een volgende
periode)

Uitstelcodes zullen veelal gebruikt worden op inkoopfacturen. Vb: abonnementskosten voor een gans jaar worden uitgesplitst per maand.

Bij het registreren van een inkoopfactuur bestaat de mogelijkheid om een deferral code (uitstelcode) in te geven per factuurlijn. De uitstelcode gaat deze kost uitsplitsen over verschillende periodes. Deze boeking wordt gelijktijdig gedaan met de boeking van de factuur. De gebruiker kan het verdelingsvoorstel nog aanpassen vooraleer door te boeken.

#### 10.7.9 BS65.229 Afpunten grootboektransacties
Grootboektransacties kunnen afgepunt worden via Posten Controleren op de grootboekposten. Wanneer een grootboekrekening zowel een debet als een credit bedrag heeft, kanmen deze met elkaar afpunten (enkel volledige bedragen) zodat men een duidelijker zicht heeft op de effectief openstaande posten op een specifieke rekening.

Uitgevoerde afpuntingen kunnen ook ongedaan gemaakt worden.

#### 10.7.10 BS65.230 Registreer en Betaal commissies
Wanneer men producten verkoopt, dan wordt soms commissie berekend. Deze commissie wordt betaald aan:

- een interne medewerker zonder BTW nummer (bv. vertegenwoordiger)
- een externe partij met BTW nummer (bv. trader)

Voor een interne vertegenwoordiger wordt aan de hand van een overzichtstaat van geboekte transacties een bepaald bedrag uitbetaald.

Wanneer een externe partij de commissie ontvangt, dan maakt hij soms een facturatie voorstel op. Na goedkeuring van het voorstel, kunt u een verkoopcreditnota maken of de externe partij maakt een verkoopfactuur die u als inkoopfactuur inboekt.

Aan de verkopercode kan een percentage gekoppeld worden voor de commissieberekening. Dit is een globaal percentage geldig op alle omzet die aan deze verkoper is gekoppeld. Via sales rapportering kan de omzet en commissie per verkoper gerapporteerd worden.

Het kan ook nuttig zijn om een dimensie te koppelen aan de verkoper, zodat ook de financiële rapportering deze info bevat.

#### 10.7.11 BS65.231 Voorraadwaardering
Bij afsluiten van een periode wordt ook de voorraad gecontroleerd (hoeveelheid en waarde).

- Op periodieke tijdstippen wordt de voorraad in de magazijnen geteld. Indien nodig moeten
voorraadcorrecties worden geboekt. Zie hoofdstuk Inventarisatie.
- Indien nodig worden er herwaarderingen doorgevoerd voor oude stock. bv. artikels die reeds 6
maanden in het magazijn liggen, artikels dicht bij de vervaldatum, ...

##### 10.7.11.1 BC65.231.01 Bereken en boek voorraadwaarde (geïntegreerd)
Bij het afsluiten van de periode is het noodzakelijk dat de voorraad correct gewaardeerd is.

Het kan immers voorkomen dat de Cost of Sales van een bepaalde verkoop beïnvloed wordt door een inkoopfactuur die geboekt is nadat de verkoop zelf werd geboekt. Om deze kost terug recht te trekken bestaat er een batch 'Kostprijs Herwaarderen - Artikelposten', die de negatieve beweging van de verkoop gaat matchen met de juiste positieve beweging (inkoop, productie output, correctie...), en dit volgens de gekozen waarderingsmethode (LIFO, FIFO...) per artikel.

##### 10.7.11.2 BC65.231.02 Bereken voorraadwaarde en boek periodiek door (geïntegreerd)
Indien bij het uitvoeren van de batch 'Kostprijs Herwaarderen - Artikelposten', de parameter 'Boeken naar GB' afstaat, moet men nog een extra batch 'Voorraadwaarde boeken' draaien om de voorraadwaarde te integreren met de boekhouding. Deze werkwijze is niet aangeraden door de kans op fouten (foute parameters, foute filters) bij het draaien van deze batch.

##### 10.7.11.3 BC65.231.03 Bereken en boek de voorraadwaarde (manueel)
Hoewel het sterk aanbevolen is om de voorraadintegratie te activeren, kan er ook voor gekozen worden om op periode einde 1 globale voorraadcorrectieboeking te doen (met een diverse boeking) op basis van het rapport Voorraadwaarde.

##### 10.7.11.4 BC65.231.04 Herwaardeer voorraad
Indien zou blijken dat bepaalde artikelen moeten af/opgewaardeerd worden, kan men dit doen via het Herwaarderingsdagboek.

Men start van een voorraadwaarde die correct berekend is volgens de data gekend in Business Central. Vervolgens gaat men de juiste waarde ingeven en boeken.

#### 10.7.12 BS65.232 Boek Intercompany transacties
De Intercompany module zorgt ervoor dat transacties die aangemaakt worden in het ene bedrijf, automatisch worden klaargezet in het andere bedrijf. Hiervoor kunnen de nodige mappings opgezet worden, zowel voor grootboekrekeningen als voor dimensies.

##### 10.7.12.1 BC65.232.01 Maak inkoopfactuur uit IC verkoopfacturen
Met de intercompany module kan een verkoopfactuur van bedrijf A automatisch omgezet worden naar een inkoopfactuur in bedrijf B. M.a.w. het boeken van de verkoopfactuur in bedrijf A, zet een (te boeken) inkoopfactuur klaar in bedrijf B op de juiste IC leverancier.

##### 10.7.12.2 BC65.232.02 Maak verkooporder uit IC inkooporder
Met de intercompany module kan een inkooporder in bedrijf A automatisch omgezet worden naar een verkooporder in bedrijf B.

##### 10.7.12.3 BC65.232.03 Boek IC journalen
Diverse posten die men boekt in het Intercompany dagboek op een IC partner, kunnen via de intercompany module klaargezet worden in het andere bedrijf dat gelinkt is aan die IC partner.

#### 10.7.13 BS65.233 Uitvoeren consolidatie grootboek
Business Central laat toe om de grootboekposten van 2 of meerdere bedrijven te consolideren in een specifiek consolidatiebedrijf. Elk bedrijf dat dient geconsolideerd te worden zal als bedrijfsunit zichtbaar zijn in het consolidatiebedrijf.

In Business Central is het mogelijk om bedrijven te consolideren binnen eenzelfde database, maar ook bedrijven uit een andere database (bv in een multi-country setup).

Het consolidatieproces houdt in dat men de grootboektransacties van de dochterondernemingen geaggregeerd doorstuurt naar het consolidatiebedrijf. Deze aggregatie gebeurt per grootboekrekening/dimensiecombinatie, per periode.

In het dochterbedrijf moet elke grootboekrekening gemapped worden naar een grootboekrekening uit het consolidatiebedrijf. Idem voor de dimensies en de dimensiewaarden, indien deze mee geconsolideerd moeten worden.

In het dochterbedrijf geeft men het participatie % aan. De bedragen worden in deze verhouding geconsolideerd.

Om IC eliminaties te vergemakkelijken is het aangewezen om een intelligente mapping op te zetten, zowel op grootboek als op dimensie niveau. Op grootboekniveau via een aparte rekening voor intercompany transacties, op dimensieniveau via een dimensie ‘INTE CO’ die aan de IC klanten en leveranciers zijn gekoppeld.

Indien 1 van de dochterbedrijven een andere bedrijfsmunt heeft dan het consolidatiebedrijf, moet de nodige aandacht besteed worden aan de juiste keuze van de consolidatie vertaalmethode per grootboekrekening.

#### 10.7.14 BS65.234 Afsluiten boekjaar/Financiële periode
Om een periode af te sluiten moeten de toegestane boekingsperiodes aangepast worden.

Voor een jaarafsluiting zijn een aantal extra stappen vereist.

##### 10.7.14.1 BC65.234.01 Afsluiten periode
Boekingsperiodes worden afgeschermd door het toegestane boekingsbereik aan te passen (boeken toegestaan van - tot). Dit kan op 3 niveaus:
- Algemeen, in de boekhoudinstellingen
- Per dagboek
- Per gebruiker
Eens een periode is afgeschermd, kunnen er geen verrichtingen meer uitgevoerd worden in deze periode.

Indien er voorraadperiodes zijn opgezet moeten ook deze worden afgesloten.

##### 10.7.14.2 BC65.234.02 Afsluiten boekjaar en openen nieuw boekjaar
Om het boekjaar af te sluiten worden volgende stappen gevolgd:

- Boekhoudperiodes beheren/afsluiten
- Nieuw boekjaar aanmaken
- Nummerreeksen aanpassen voor het nieuwe boekjaar
- Winst- en verliesrekeningen afsluiten en doorboeken
- Toegestane boekingsdatums aanpassen

#### 10.7.15 BS65.235 Afsluiten BTW periode
Nadat de BTW aangifte is ingediend, kan u de BTW vereffening boeken met het rapport 'BTW-vereff. berek. en boeken'. Dit heeft tot gevolg dat:

- de BTW posten van de periode worden afgesloten, en dus niet dubbel kunnen aangegeven worden
indien men bij het maken van de aangifte filtert op 'Open' entries.
- het saldo van de BTW rekeningen wordt overgeboekt naar een rekening BTW Rekening Courant

### 10.8 Beheer vast actief
#### 10.8.1 BS65.236 Maak Vast Actief aan
Vast activa kunnen we onderverdelen in:

- Financieel
- Materieel
- Immaterieel
De boekhouding dient een vaste actief kaart aan te maken met:

- Algemene informatie (nummer, naam, ...)
- Klasse & Subklasse
- Afschrijvingsmethode
- Duur -> afschrijvingspercentage
- Dimensies

Het is mogelijk om meerdere afschrijvingsboeken aan te maken, en deze kunnen indien gewenst allemaal geïntegreerd worden met het grootboek. Zo kunnen fiscale afschrijvingen en bedrijfseconomische afschrijvingen apart beheerd worden, in een aparte set grootboekrekeningen. Het is ook mogelijk om enkel de fiscale afschrijvingen te integreren met het grootboek, en de bedrijfseconomische afschrijvingen enkel binnen de vast actief module zichtbaar te houden voor rapportage.

In te geven parameters in het afschrijvingsboek per vast actief:
- Afschrijvingsmethode
- Begindatum afschrijving
- Afschrijvingspercentage
- Boekingsgroep

Indien men een globaal overzicht wenst van bepaalde sub-activa (onderdelen), kan men deze groeperen in een hoofdactivum. De totale boekwaarde van het hoofdactivum is zichtbaar in de Hoofdactivumstatistiek.

#### 10.8.2 BS65.237 Aanschaffen Vast Actief

##### 10.8.2.1 BC65.237.01 Koop Vast Actief aan via aankoopfactuur
De aanschaf van een vast actief kan onmiddellijk geboekt worden met een aankoopfactuur door het vast actief rechtstreeks op de aankoopfactuurlijn te zetten.

##### 10.8.2.2 BC65.237.02 Boek AW via diverse VA verrichting
Indien pas later beslist wordt om een bepaalde kost te activeren, dan kan men deze inboeken via een divers dagboek binnen de VA-module door rechtstreeks de aanschafwaarde op het vast actief te boeken.

Indien een aangeschaft artikel geactiveerd wordt, dient dit artikel uitgeboekt te worden in het artikeldagboek. De voorraadcorrectierekening die gebruikt wordt bij deze negatieve correctie, zal de tegenrekening zijn die men moet ingeven in het VA divers journaal.

#### 10.8.3 BS65.238 Schrijf een Vast Actief af
Business Central voorziet verschillende afschrijvingsmethodes.

- Lineair
- Degressief
- Lineair / Degressief
- Handmatig
- Eigen methode

Met de functie ‘Afschrijvingen berekenen’ worden de afschrijvingsbedragen per vast actief berekend en klaargezet in een dagboek, dat men vervolgens moet doorboeken.

#### 10.8.4 BS65.239 Buitengebruikstelling van een vast actief
Een vast actief kan buiten gebruik gesteld worden door middel van een verkoopfactuur of een diverse VA boeking.

Het resultaat dat voortvloeit uit het verschil tussen het verkoopbedrag en de huidige boekwaarde (min- /meerwaarde), zal o.b.v. de boekingsgroepinstellingen automatisch geboekt worden naar een resultaatrekening.

##### 10.8.4.1 BC65.239.01 Stel Vast Actief buiten gebruik via verkoop
Vast actief kan rechtsreeks ingegeven worden op een verkoopfactuurlijn. Min/meerwaarde wordt bepaald door verschil verkoopprijs en boekwaarde.

##### 10.8.4.2 BC65.239.02 Stel Vast Actief buiten gebruik via divers journaal
Vast actief kan buitengebruik gesteld worden zonder verkoopfactuur, maar rechtstreeks via het VA journaal. Min/meerwaarde wordt bepaald door het bedrag dat men ingeeft op de journaallijn min de boekwaarde.

#### 10.8.5 BS65.240 Herwaardeer een vast actief
Een waardevermindering of -vermeerdering kan rechtstreeks via het VA journaal geboekt worden, met VA Boekingssoort 'Waardevermindering' of 'Waardevermeerdering'.

#### 10.8.6 BS65.242 Registreer onderhoud op Vast Actief
Op de vast activa kaart is het mogelijk om alle onderhoudsbeurten bij te houden en te registreren door wie het onderhoud werd uitgevoerd.

#### 10.8.7 BS65.243 Reclassificeer een vast actief
Bij een reclassificatie gaat een vast actief (deels) overgeboekt worden naar een ander vast actief.

Dit gebeurt i.g.v.:
- gedeeltelijke buitengebruikstelling: hierbij wordt een percentage van de waarde van het originele vast
actief overgeboekt naar een nieuw vast actief, waarbij enkel het nieuwe vast actief wordt verkocht en het oude wordt behouden.
- een bestemmingswijziging die andere boekingsschema's tot gevolg heeft, bv. leasing wordt eigendom:
hierbij kan er een volledige overboeking gebeuren van een oud naar een nieuw vast actief

Vaste activa kunnen geherclassificeerd worden via het VA-herindelingsdagboek. Zowel de aanschafwaarde, geboekte afschrijvingen en alle herwaarderingen kunnen overgezet worden.

### 10.9 Beheer budgetten
#### 10.9.1 BS65.244 Maak (grootboek)budget aan
Business Central bevat een budgetmodule die toelaat om budgetten manueel in te geven of te importeren vanuit Excel. In een budget kan men maximum 6 verschillende dimensies ingeven.

Bij de creatie van een nieuw budget k an men een reeds bestaand budget kopiëren of een nieuw budget aanmaken aan de hand van de werkelijke bedragen van een bepaalde periode, eventueel met toepassing van een multiplicatiefactor..

#### 10.9.2 BS65.245 Controle budget t.o.v. grootboek
Op regelmatige tijdstippen wenst men de gebudgetteerde posten te vergelijken met de werkelijke bedragen. Hiervoor zijn diverse rapporten aanwezig. De budget functionaliteit in Business Central dient enkel voor rapportage. Tijdens het boeken van transacties is er geen blockage aanwezig indien het vooropgestelde budget wordt overschreden.

#### 10.9.3 BS65.246 Maak (verkoop/aankoop)budget aan
Business Central bevat een verkoopbudgetmodule die toelaat om verkoop- en aankoopbudgetten manueel in te geven of te importeren vanuit Excel.

Dit kan per artikel, artikelgroep, klant, klantgroep, leverancier.

#### 10.9.4 BS65.247 Controle (verkoop/aankoop)budget t.o.v. werkelijk
Controle van de gebudgetteerde cijfers ten opzichte van de werkelijke cijfers is mogelijk per artikel, artikelgroep, klant, klantgroep, leverancier.

### 10.10 Beheer cashflow
Met de cashflow functionaliteit is het mogelijk om op geregelde tijdstippen een cashflow prognose te laten berekenen. We kunnen uit diverse bronnen gegevens laten opnemen in deze berekening, zoals de tegoeden, de schulden, beschikbare liquide middelen, verkooporders, inkooporders, handmatige uitgaven, handmatige inkomsten, budgetten, projecten enz...

#### 10.10.1 BS65.111 Beheer Master Data Cash Flow
Volgende zaken dienen ingesteld te worden:
- Cash flow rekeningschema
- Cash flow rapportageschema

#### 10.10.2 BS65.255 Bereken cashflow
Bij het opmaken van een cashflow prognose kunt u gebruik maken van onderstaande elementen:
- Handmatige kosten
- Handmatige opbrengsten
- Cashflowrekeningen / rekeningschema
- Orders
- Projecten
- Facturatie

Van zodra alle elementen van de prognose gedefinieerd zijn, kan men de rapporten gebruiken om het resultaat te bekijken.

### 10.11 Kostprijsboekhouding
Met de Cost Accounting module (Kostprijsboekhouding) kunnen verdeelsleutels berekend worden om kosten en opbrengsten te verdelen naar andere rekeningen, kostenplaatsen of kostendragers. Deze module staat los van de algemene boekhouding en dient enkel voor rapportage. Rapportering is wel mogelijk binnen de Cost Accounting module zelf.

#### 10.11.1 BS65.112 Beheer Master Data Kostprijsboekhouding
Volgende zaken dienen ingesteld te worden:

- Kostensoorten
- Kostenplaatsen
- Kostendragers
- Kostentoewijzingen
- Kostenbudgetten
- Rapportage

#### 10.11.2 BS65.248 Wijs kosten toe - Kostprijsboekhouding
De kostprijsboekhouding module in Business Central laat toe om kosten toe te wijzen aan bepaalde kostendragers aan de hand van op voorhand gedefinieerde toewijzingsregels. Kosten kunnen toegewezen worden op basis van een vast percentage, per aandeel of berekend op basis van rekeningbedragen, aangekochte/verkochte hoeveelheden van bepaalde artikelen etc.

De verdeelde resultaten maken geen deel uit van de G/L rapportering, maar staan hier volledig los van.

In de kostprijsboekhouding moeten volgende stappen uitgevoerd worden:
- Grootboekposten kopiëren naar de kostprijsboekhouding (enkel P&L rekeningen)
- Verdeelsleutels ingeven of laten berekenen
- Kosten toewijzen

### 10.12 Document Lay-outs Finance
#### 10.12.1 BS65.800 Verkoopfactuur
Cegeka Lay-out:

#### 10.12.2 BS65.801 Verkoopcreditnota
Cegeka Lay-out:

#### 10.12.3 BS65.802 Aanmaningen
Cegeka Lay-out:

### 10.13 BS65.900 Excise duty management (Aptean)
Accijnzen zijn een indirecte belasting op specifieke producten om het gebruik ervan te ontmoedigen. In de drankenindustrie is alcohol het meest voor de hand liggende product waarvoor accijnzen worden berekend. Accijnzen op alcohol moeten periodiek aan de plaatselijke douane worden betaald wanneer de accijnsproducten worden verkocht of tot verbruik worden vrijgegeven.

### 10.14 BS65.901 Taks process handling (Aptean)
De Aptean Tax Process Handling-extensie helpt u de procesbeveiliging en transparantie voor financiële transacties binnen Business Central te verhogen. Met deze extensie kunt u automatisch de boekingsgroep op de transactie wijzigen. U kunt specifieke Business Posting Types instellen die de boekingsgroep instellingen op een

document wijzigen. Deze instellingen variëren op basis van de combinatie van afzender-/ontvangeradres, die worden beïnvloed door wijzigingen in het verzend-/besteladres. Daarnaast kunt u een nieuw btw-registratienummer aanmaken en toewijzen aan de order wanneer het Business Posting Type wordt toegepast.
