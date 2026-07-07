## 13. Cegeka 365 for Business Central
### 13.1 Algemene bedrijfsfunctionaliteit
#### 13.1.1 Algemene instellingen

##### 13.1.1.1 BS95.003 Activeer functionaliteiten
Vooraleer functionaliteiten van de Cegeka 365 add-ons in gebruik genomen kunnen worden, dienen deze geactiveerd te worden via de pagina “Cegeka 365 Functionaliteiten”. Via deze pagina kunnen functionaliteiten in- en uitgeschakeld worden, op voorwaarde dat ze zijn opgenomen in de licentie.

#### 13.1.2 Rapport- en documentparameters

##### 13.1.2.1 BS10.007 Documentopmerkingen
Klantenopmerkingen voor documenten Indien er op uitgaande documenten voor klanten extra informatie afgedrukt moet worden, kan er via deze functionaliteit uitgebreide tekstbestanden gelinkt worden aan deze klanten.

De tekst kan ingesteld worden via tekstuitbreiding vanaf de klantenkaart. Op de tabs “Verkoop” “en “Service” kan aangeduid worden op welke documenten deze tekst van toepassing is.

Klant/leveranciersopmerkingen bij binnenkomende mail Inkomende mails van contacten zijn een belangrijke bron van informatie. Indien contact dat een mail stuurt, gelinkt is aan een klant, gaan de opmerkingen die gelinkt zijn aan deze klant getoond worden in de email cliënt, zodat je onmiddellijk extra informatie bij de hand hebt om de mail te behandelen.

Hetzelfde principe geldt ook voor leveranciers.

##### 13.1.2.2 BS10.008 CMR afdrukken
De CMR is een internationale conventie bij grensoverschrijdend wegvervoer.

De CMR is van toepassing op alle vervoer over de weg van of naar een bij de conventie aangesloten land. De CMR is ook geldig bij een binnenlands transport als onderdeel van een internationaal transport.

Deze functionaliteit is bedoeld om de CMR af te drukken op basis van geboekte verzenddocumenten in Business Central.

### 13.2 Inkoop
#### 13.2.1 Inkoop instellen

##### 13.2.1.1 BS35.003 Extra velden inkoopvoorstel
Uitbreiding van het inkoopvoorstel met een factbox met volgende velden, zodat beoordeling van inkoop aan aantal parameters eenvoudig gecontroleerd kan worden:

- leverancier
- minimum bedrag leveranciers
- totaal bedrag inkoopvoorstellijnen
- minimum gewicht verkoper
- totaal gewicht inkoopvoorstellijnen
- totale aantal paletten

#### 13.2.2 Inkoop master data

##### 13.2.2.1 BS35.106 Commerciële basiskost artikelen beheren
De financiële of boekhoudkundige kost van een artikel komt vaak niet overeen met de kost die als basis voor de verkoopprijs wordt gebruikt. De boekhoudkundige kost wordt door Business Central berekend op basis van standaard instellingen van kostprijsbeheer (FIFO, LIFO, Gemiddeld...)

De commerciële basiskost maakt deel uit van het uitgebreid verkoopprijzenbeheer van de Cegeka 365 Wholesale add-on. Voor het bepalen van de commerciële basiskost stelt men een inkoopprijs in voor de standaardleverancier, waarbij veld “Basiskost voor commerciële marge” wordt ingeschakeld. Vervolgens kan de commerciële basiskost berekend worden via het “CGK Artikel Prijswijzigingsvoorstel”.

##### 13.2.2.2 BS35.107 Verplichte eenheden per leverancier
Met deze functionaliteit kan er tegengegaan worden dat er inkopen in kleine hoeveelheden of verpakkingen worden gedaan. Op de leverancier wordt dan aangegeven in welke eenheden of veelvouden van eenheden de goederen mogen aangekocht worden.

##### 13.2.2.3 BS35.108 Einde periode inkoopkortingen/vergoedingen beheren
Vaak zijn er met leveranciers afspraken over bijkomende kortingen op het einde van een periode voor bepaalde artikelen of artikelgroepen. Met deze functie kunnen alle geboekte factuur- en creditnotalijnen verzameld worden van de gefactureerde artikelen binnen die periode. Zo is het eenvoudig om een vereffeningsdocument op te stellen om zo het vergoedingsbedrag terug te vorderen van de leverancier.

### 13.3 Verkoop
#### 13.3.1 Verkoop instellen

##### 13.3.1.1 BS25.002 Bron verkooporders
Verkooporders kunnen op verschillende manieren aangemaakt worden, bijvoorbeeld via EDI/WEB/manueel etc. Deze functionaliteit voorziet een extra veld op het verkooporder, waarin kan aangegeven worden hoe dit verkooporder binnen is gekomen.

##### 13.3.1.2 BS25.003 Verkoopordernummer bij verzendregels ophalen
Deze instelling zorgt er voor dat er op het scherm 'ophalen verzendregels' de mogelijkheid is om een kolom met het verkoopordernummer zichtbaar te maken.

##### 13.3.1.3 BS25.004 Controle commerciële marge
Standaard wordt er bij de berekening van de marge enkel gekeken naar financiële kostprijs op de artikelkaart. Dit is een goeie indicatie voor de financiële marge, maar voor de commerciële marge spelen er andere zaken (prijzen van de concurrentie, oude stock...). Deze functionaliteit zal de marge procentueel weergeven tussen de 'basis kost voor commerciële marge (artikelniveau)' en het totale lijnbedrag op de verkooplijnen om de verkoopmedewerkers in staat te stellen de juiste beslissingen te nemen.

##### 13.3.1.4 BS25.005 Fostplus instellen
Voor de aangifte van Fostplus is het noodzakelijk om een groeperingscode in te geven. Deze groeperingscode wordt ingesteld als een standaardcode binnen de Cegeka 365 Wholesale functionaliteit.

#### 13.3.2 Verkoop master data

##### 13.3.2.1 BS25.101 Beheren verkoopprijzen
##### 13.3.2.2 BS25.110 Standaard verzendcode klant
Deze functionaliteit biedt de mogelijkheid om op een klant met meerdere verzendadressen een standaard verzendadres aan te geven. Dit kan handig zijn indien er hoofdzakelijk op 1 van verschillende adressen geleverd wordt.

##### 13.3.2.3 BS25.111 Instellen standaard transportkosten klant
Vaak wordt er bij het verkopen van goederen een transportkost bijgerekend. Het is mogelijk om aan klanten een standaard transportkost te koppelen. Hiervoor moet er een transportartikel aangemaakt worden en dit kan dan via een standaardverkoopcode gekoppeld worden aan de klant.

#### 13.3.3 Verkoopcreditnota's beheren

##### 13.3.3.1 BS25.226 Verkoopcreditnota's maken
13.3.3.1.1 BC25.226.01 Verkoopcreditnota maken op basis van einde-periode verkoopvergoeding Via het venster “Verkoopvergoeding ingaven” krijgt men een overzicht van alle verkoopfactuur- en creditnotaregels die in aanmerking komen voor een einde-periode vergoeding. Hier kunnen de gewenste lijnen geselecteerd worden en kan een creditnota worden aangemaakt waarmee de vergoeding aan de klant wordt verwerkt. De vergoeding op de creditnota wordt toegekend via een artikeltoeslag.

#### 13.3.4 Verkoopraamcontracten beheren

##### 13.3.4.1 BS25.227 Begin- en einddatum op verkoopraamcontracten
Moet nog ingebouwd worden.

Vaak is het bij het aanmaken van een verkooporder voor een klant in combinatie met bepaalde artikelen niet geweten dat er een bestaand verkoopraamcontract (afroeporder) is. Met deze functie wordt er een waarschuwing gegeven aan de gebruiker bij ingave van een verkooporder als er een bestaand verkoopraamcontract is.

#### 13.3.5 Verkooporders beheren

##### 13.3.5.1 BS25.228 Maak verkooporder

13.3.6Beheer periodieke taken

##### 13.3.6.1 BS25.231 Valipac en Fostplus aangifte
De Valipac en Fostplus aangiftes gaan respectievelijk over bedrijfsmatige en huishoudelijke verpakkingen die bedrijven op de markt brengen.

Valipac

Indien u bv. begin 2016 uw aangifte indient met betrekking tot het jaar 2015 en de tonnage aan bedrijfsmatige verpakkingen op uw aangifte < 5 ton bedraagt, dan kan u gebruik maken van de vereenvoudigde aangifte. Deze aangifte is gebaseerd op de evolutie van uw omzetcijfer van het ene jaar op het andere.

Deze aangifte zal als basis dienen voor de berekening van de aangiftes voor de komende 4 jaar: gedurende deze periode zal VAL-I-PAC u vragen om jaarlijks uw omzetcijfer mee te delen. Het volstaat de vereenvoudigde aangifte in te vullen en jaarlijks vóór 28 februari terug te sturen naar VAL-I-PAC. Op basis van de evolutie van uw omzetcijfer, berekent VAL-I-PAC vervolgens uw jaarlijkse bijdrage.

Het systeem blijft 5 jaar van toepassing, zelfs als uw tonnage de 5 ton overschrijdt (tenzij de tonnage meer dan 10 ton bedraagt). De deelnemer die van dit systeem gebruik maakt, dient VAL-I-PAC van elke belangrijke wijziging op de hoogte te brengen (wijziging van verpakking, overname van bedrijf, …) die invloed heeft op de tonnage aan bedrijfsmatige verpakking waarvoor hij verantwoordelijk is. Het vijfde jaar maakt u opnieuw uw gebruikelijke gedetailleerde aangifte op.

Fost Plus

Bedrijven die:
- Huishoudelijke producten verpakken of laten verpakken in België om ze onder hun eigen merk of een
neutraal merk op de Belgische markt te brengen.
- Verpakte huishoudelijke producten invoeren of laten invoeren om ze op de Belgische markt te brengen.
- Serviceverpakkingen produceren en/of invoeren om ze op de Belgische markt te brengen.
Serviceverpakkingen worden aangebracht op de plaats waar producten of diensten aan de consument worden aangeboden. Voorbeelden zijn onder meer inpakpapier, broodzakken, pizzadozen en kassazakjes.

U bent niet wettelijk verplicht om lid te worden van Fost Plus. U kunt er ook voor kiezen om een eigen systeem op te zetten. Uw bedrijf organiseert dan zelf de inzameling, het sorteren en het recycleren van uw verpakkingen en u bezorgt de Interregionale Verpakkingscommissie (IVC) de nodige gegevens om aan te tonen dat u de verplichte recyclagepercentages behaalt. Wanneer u lid wordt van Fost Plus, kunnen zij de terugname- en informatieplicht voor uw huishoudelijke verpakkingen overnemen. U betaalt dan een jaarlijkse ledenbijdrage, die Fost Plus gebruikt om de inzameling, het sorteren en de recyclage van uw huishoudelijke verpakkingen te financieren.

13.3.6.1.1 BC25.231.01 Valipac en Fostplus aangifte Deze variant beschrijft hoe de posten kunnen worden opgehaald die in aanmerking komen voor de Valipac en Fostplus aangiftes. Aan de artikelen kunnen een of meerdere aangifte-codes toegekend worden. Op periodieke basis kunnen de aangifteposten (op basis van verkoop) opgehaald worden. Het resultaat is een overzicht van de aangifte posten, deze kunnen nadien naar Excel geëxporteerd worden.

##### 13.3.6.2 BS65.249 Prodcom aangifte
De Prodcom-lijst is een nomenclatuur met ”producten” die door de lidstaten van de Europese Unie wordt gebruikt om de productiestatistieken op te stellen. De Prodcom-aangifte bevat informatie over de geproduceerde hoeveelheden van artikelen waaraan een nomenclatuur is toegekend.

De Prodcom-statistieken bestaan uit de volgende reeks indicatoren:
- Het fysieke productievolume dat tijdens de enquêteperiode is verkocht.
- De waarde van de tijdens de enquêteperiode verkochte productie.

- Het fysieke volume van de werkelijke productie tijdens de enquêteperiode, met inbegrip van de
productie die is verwerkt in de vervaardiging van andere producten van dezelfde onderneming.

13.3.6.2.1 BC65.249.01 Prodcom aangifte Deze variant beschrijft hoe de posten kunnen worden opgehaald die in aanmerking komen voor de Prodcom- aangifte. Aan de artikelen kunnen een of meerdere aangifte-codes toegekend worden. Op periodieke basis kunnen de aangifteposten (op basis van verkoop) opgehaald worden. Het resultaat is een overzicht van de aangifte posten, deze kunnen nadien naar Excel geëxporteerd worden.

13.3.7

#### 13.3.8 BS25.903 Trade management (Aptean)
Bij de aankoop en verkoop van artikelen ontstaan kosten. De Trade Management-extensie maakt het mogelijk om deze kosten in te stellen en toe te wijzen aan een artikel. De kosten kunnen worden toegewezen aan de verkoop-/aankoopprijs, wat leidt tot een prijsverhoging of -verlaging, of de kosten kunnen worden toegewezen als artikelkosten. De kosten worden ingesteld met behulp van een handelsplan. Deze handelsplannen kunnen zeer specifiek zijn (bijvoorbeeld een kostenpost die alleen van toepassing is wanneer het verkoopdocument voor een specifieke klant is), maar in veel gevallen worden kosten en kortingen op een meer algemeen niveau ingesteld (bijvoorbeeld voor klanten van het type 'detailhandel' wordt een korting van 1% verleend). Om deze meerdere benaderingen te ondersteunen, kunt u handelsplannen definiëren op een specifiek of algemeen niveau, op basis van een combinatie van klantgroepen (handelsgroepen) en artikelgroepen (handelsproductgroepen). Via handelsplannen kunt u aangeven of deze kosten van invloed zijn op de verkoop- en aankoopprijs. De artikelkosten, genaamd toerekening, kunnen worden ingesteld als standaard- of werkelijke kosten/opbrengsten. Standaardkosten of -opbrengsten worden direct geboekt. Werkelijke kosten of opbrengsten worden geboekt als verwachte kosten of opbrengsten, en later vervangen door de werkelijke kosten/opbrengsten via een factuur van een handelspartner. U kunt een artikelkost boeken met een handelskostenorder. Deze handelskostenorders worden automatisch aangemaakt en geboekt wanneer handelsdocumentlijnen worden geboekt met een bepaald toerekeningstype. Het is ook mogelijk om handmatig een handelskostenorder aan te maken om extra kosten voor een artikel in te voeren. Er kunnen verschillende tarieven, handelstarieven genoemd, voor het berekenen van de kosten aan een handelsplan worden gekoppeld. Deze handelstarieven worden opgehaald als een handelsdocumentlijn wanneer een verkoop-/aankoopdocumentlijn wordt gemaakt. De kosten of prijsaanpassingen worden berekend op basis van de verkoop-/aankoopdocumentlijn en de handelsplan-tarieven. De Trade Management-extensie is gebaseerd op de verkoop-/aankoopprijs en instellingen van de Advanced Pricing-extensie. Daarom is het alleen mogelijk om de Trade Management-extensie te gebruiken als de Advanced Pricing-extensie is geïnstalleerd.

#### 13.3.9 BS25.904 Trading board (Aptean)
Met de Aptean Trading Board-extensie kun je de verwachte en ontvangen voorraad bekijken op het niveau van lotnummers per locatie. Vanaf de Trading Board-pagina kun je direct nieuwe documenten aanmaken, bestaande

documenten bijwerken en lotnummers toewijzen met prijzen. Je kunt ook de Trading Board openen vanuit bestaande documentkoppen en -regels.

### 13.4 Voorraad
#### 13.4.1 Voorraad instellen

##### 13.4.1.1 BS50.004 Lotnummer ingave op document lijn
Standaard worden lotnummers ingegeven via een apart scherm dat onder de artikeltraceringsregels te vinden is. Met deze functionaliteit wordt het aantal klikken dat moet gedaan worden in het geval dat er slecht sprake is van 1 lotnummer gereduceerd tot 1. Deze versnelde manier van ingave maakt het mogelijk om het lotnummer al op lijnniveau in te geven. Dit op volgende plaatsen:
- inkooporder
- inkoopretourorder
- verkooporder
- verkoopretour
- magazijnontvangst
- magazijnverzending
- transferorder
- artikeldagboek
- magazijndagboek
- productiedagboek
- outputdagboek
- consumptiedagboek
- assemblageorder
- artikelherclassificatie
- magazijnherclassificatie
- interne bewegingen
- fysieke voorraaddagboek

##### 13.4.1.2 BS50.005 Extra velden artikelposten
13.4.1.2.1 BC50.005.01 Extra velden artikelpost Met deze functionaliteit is het mogelijk om de velden verkoper, expediteur en servicecode expediteur weer te geven onder de artikelposten. Deze velden kunnen dan gebruikt worden om te filteren op bepaalde waarden. Deze functionaliteit biedt de mogelijkheid om de verkoper, expediteur en servicecode expediteur van het verkooporder over te nemen naar de artikelposten indien geboekt wordt, wat nuttig is voor rapporteringsdoeleinden.

13.4.1.2.2 BC50.005.02 Omschrijving op artikelposten Bij het boeken van bijvoorbeeld een verkoopverzending of een inkoopontvangst wordt in standaard Business Central de artikelomschrijving op de artikelposten als blanco weggeschreven. Wanneer er handmatig een artikelomschrijving wordt ingevoegd of aangepast zal deze wel overgenomen worden in de artikelposten. Deze functionaliteit biedt de mogelijkheid om de standaard omschrijving van het artikel over te nemen naar de artikelposten indien geboekt wordt wat nuttig is voor rapporteringsdoeleinden.

##### 13.4.1.3 BS50.006 Automatisch aanmaken lotnummerinformatiekaart
13.4.1.3.1 BC50.006.01 Automatisch aanmaken lotnummer info In standaard Business Central kunnen lotnummerinformatiekaarten manueel aangemaakt worden. Op deze kaart kan dan extra informatie gezet worden i.v.m. bv. geteste kwaliteit.

Deze functionaliteit zorgt ervoor dat lotnummerinformatiekaarten automatisch aangemaakt worden als er een inkomende transacties voor een lotnummer wordt geboekt.

13.4.2

#### 13.4.3 Artikeltracering

##### 13.4.3.1 BS50.235 Printen labels via Bartender
In heel wat bedrijfsprocessen kan het nodig zijn dat er verschillende soorten labels afgedrukt worden. Denken we maar aan verzend labels, artikel labels, lotnummerinformatielabels...

Deze labels kunnen afgedrukt worden via een speciale labelsoftware. Deze functionaliteit maakt het de gebruiker mogelijk om de informatie, nodig voor het printen van deze labels, vanop verschillende plaatsen in Business Central, naar een file te sturen. De nodige gegevens zoals label lay-out, printer waarop kan afgedrukt worden, artikelomschrijvingen, aantallen, lotnummers, palletnummers... kunnen dan door de printersoftware wordt afgedrukt.

### 13.5 Magazijnbeheer
#### 13.5.1 Magazijn Master Data

##### 13.5.1.1 BS50.111 Leveringsweek op basis van gevraagde leverdatum
Standaard werkt Business Central met exacte datums voor het bepalen van de ontvangst- of verzenddatum op het order. Met deze functionaliteit wordt het mogelijk om ook de leveringsweek te tonen op verkoop- en inkooporders. Deze leveringsweek is afhankelijk van de te verwachten ontvangst- of verzenddatum op het order.

#### 13.5.2 Artikelen ontvangen

##### 13.5.2.1 BS50.112 Voorbereiding inkooporders voor ontvangst
De workload voor het magazijn hangt onder andere af van het aantal leveringen en de hoeveelheid te ontvangen goederen.

Bovendien is het zo dat, aangezien de nog te ontvangen aantallen worden meegenomen in de beschikbaarheidsberekeningen, deze zo goed mogelijk up-to-date moeten zijn. Het beheer hiervan is vaak niet eenvoudig en kan gaan over meerdere inkooporders.

Deze functionaliteit biedt een overzicht van alle inkooporderlijnen die nog moeten ontvangen worden. Vanuit dit scherm kan dan de workload voor het magazijn bepaald worden en kunnen inkooporders gemakkelijk aangepast worden.

Men kan namelijk van hieruit:
- Te ontvangen aantallen instellen
- Verwachte ontvangstdatums instellen
- Magazijndocumenten aanmaken

#### 13.5.3 Artikelen verzenden

##### 13.5.3.1 BS50.113 Voorbereiding verkooporders voor levering
Wanneer er veel verkooporders zijn, is het belangrijk om te kunnen bepalen of alle orders wel op tijd kunnen geleverd worden en of er bepaalde orders eventueel later dienen geleverd te worden, gezien de beschikbaarheid van de artikelen.

Deze functionaliteit geeft een overzicht van alle te verzenden orderlijnen over alle verkooporders heen. Vanuit dit overzicht kan eenvoudig de beschikbare voorraad bekeken worden en magazijnopdrachten aangemaakt worden.

#### 13.5.4 BS55.900 Packaging (Aptean)
Deze extensie biedt gebruikers een gemakkelijke en consistente manier om retour verpakkingsartikelen te registreren. Vanuit alle ordertypes, inclusief de verschillende magazijndocumenten die per locatie kunnen worden gebruikt, kunnen gebruikers retour verpakkingsartikelen definiëren zoals vaten of paletten die zijn verzonden of ontvangen. Het is mogelijk om de verschillende verpakkingsartikelen (vaten/paletten) te linken met de artikelen die verkocht worden. Dit zorgt ervoor dat we voorraadniveaus en de waarde van de voorraad kunnen aanhouden voor retour verkappingsartikelen. Artikelen kunnen worden ingesteld met standaard verpakkingen die automatisch worden berekend wanneer transacties voor de specifieke artikelen plaatsvinden. Bovendien is er de mogelijkheid om te definiëren of de verpakking artikelgebonden of ordergebonden is.

- Een artikelgebonden verpakking is een inherent onderdeel van het artikel en wordt standaard
verzonden/ontvangen bij de inkoop/productie van het artikel. Indien dit is gekoppeld aan een artikel is het niet mogelijk hiervan af te wijken binnen een transactie.
- Een ordergebonden verpakking is vrijer gedefinieerd omdat gebruikers de hoeveelheden en soorten
verpakkingen verzonden/ontvangen kunnen overrulen bij transacties. Bij het boeken van aankoop- en verkooporder transacties met verpakkingsartikelen wordt een aparte administratie van verpakkingsboekingen bijgehouden. Dit zorgt voor een real time overzicht van de uitstaande verpakkingssaldi op klant- of leveranciers(groep)niveau.

13.5.5

### 13.6 Finance
In de Cegeka Finance Suite add-on zijn volgende functionaliteiten toegevoegd:

- Naam Klant/Leverancier op grootboekpost
- Controle inkoopfactuurnummer op niet geboekte documenten
- Verzendprofiel op geboekte documenten
- BTW nummer zichtbaar op overzichtslijsten
- Validatie ondernemingsnummer
- Verzamelfacturatie via factuurgroeperingscode
- Rapport Te ontvangen facturen/te factureren verzendingen
- Controle op inkooporder bij boeken artikelen op inkoopfactuur
- BTW bedrijfsboekingsgroep op basis van verzendadres
- Broncode op verkooporder
- CODA: Update bankrekening op klantenkaart bij import CODA
- CODA: Prefix voor Belgische financiële nummering
- SEPA verbeteringen
- Betaalwijze van de factuur selecteren in de betalingsflow
- Gestructureerde mededeling op inkoop & verkoop
- Controlerapport op betalingsdagboek
- Allocatiecodes
- Uitstelboekingen klaarzetten i.p.v. onmiddellijk door te boeken
- Ongeboekte dagboekregels tonen
- BTW eenheid
- Fiche 281.50
- Intrastat defaults
- Gebruikers en datum informatie
- Menu ‘Sessions’

- Goedkeuring voor betaling
