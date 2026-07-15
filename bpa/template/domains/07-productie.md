## 7. Productie
Het domein "Productie" omvat de processen voor het opvolgen van het produceren van goederen. Hiervoor worden materialen en machinetijd verbruikt en wordt als resultaat output (geproduceerde goederen of halffabricaten) gegenereerd. Dit domein bevat ook de master data die voor productie van toepassing is, zoals productiestuklijsten, afdelingen en bewerkingsplannen. Alle activiteiten vanaf het aanmaken van een productieorder, over het registreren van verbruik van materialen en uren, het registreren van output en uitval, tot het beëindigen van productieorders worden hier beschreven. Daarnaast wordt ook het beheer van uitbesteding behandeld.

### 7.1 Productie instellen
#### 7.1.1 BS40.001 Productie instellen
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-configure-production-processes

De productie-instellingen bevatten de algemene instellingen die de productie-functionaliteit sturen in Business Central: algemene instellingen, de nummerreeksen voor de verschillende soorten productieorders, afdelingen/bewerkingsplaatsen, productiestuklijsten en bewerkingsplannen en parameters voor het aansturen van de MPS/MRP-planning.

### 7.2 Productie Master Data
#### 7.2.1 BS40.100 Afdelingen/workcenter beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-how-to-set-up-work-and- machine-centers

Dit scenario beschrijft het beheer van afdelingen. Een afdeling is een groep van gelijksoortige handelingen, vb. de inpakafdeling, de plooiafdeling, zaagafdeling etc. De afdeling bevat een aantal belangrijke gegevens voor de planning en kostprijsberekening voor productie.

- Afdelingen beheren: Afdelingen worden in productie in bewerkingsplannen gebruikt om een bewerking
aan te duiden die voor de productie van een artikel moet worden uitgevoerd. De afdelingskaart bevat informatie over de kostprijzen (directe en indirecte) en de manier waarop de kostprijs wordt berekend (tijd of eenheden). Op een afdeling worden ook parameters voor planning (eenheid, capaciteit, efficiëntie, agenda en wachttijd) ingesteld.
- Afdelingen voor uitbesteding beheren: Bij afdelingen voor uitbesteding geeft het veld
“toeleveranciersnummer” aan dat de bewerking extern (door een subcontractor) zal worden uitgevoerd. De overige parameters kunnen op dezelfde wijze ingesteld worden als bij een gewone afdeling, maar doorgaans wordt geopteerd voor de kostprijsberekening “eenheden”, omdat men de uitbesteder betaalt per geproduceerd artikel en niet op tijdsbasis. Verder wordt ook vaak geopteerd voor “specifieke kostprijs”, omdat verschillende artikelen die bij dezelfde uitbesteder worden gemaakt verschillende prijzen hebben (de kostprijs voor de uitbesteding wordt bij gebruik van “specifieke kostprijs” in het bewerkingsplan in plaats van op de afdeling ingesteld.

#### 7.2.2 BS40.102 Bewerkingsplaatsen/machines beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-how-to-set-up-work-and- machine-centers

Bewerkingsplaatsen zijn een onderdeel van afdelingen en worden gebruikt in bewerkingsplannen om de bewerkingen aan te duiden die nodig zijn voor de productie van een artikel. Bewerkingsplaatsen bevatten een aantal standaardwaarden voor kostprijzen en planning die in bewerkingsplannen worden gebruikt.

De bewerkingsplaats bevat standaardwaarden voor insteltijd, wachttijd na bewerking, transporttijd, doorgifteaantal, minimale verwerkingstijd en maximale verwerkingstijd. Deze tijden worden als standaardwaarde gebruikt in bewerkingsplannen.

Opmerking: in theorie kunnen deze machines ook mensen zijn, waarbij naast een machine, parallel ook één of meerdere mensen gepland worden om de machine te bedienen.

#### 7.2.3 BS40.101 Capaciteit beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-how-to-post-capacities

De capaciteit van afdelingen en bewerkingsplaatsen duidt aan hoeveel werk er kan verricht worden en wanneer er beschikbare werkuren zijn. De capaciteit wordt gebruikt voor de berekening van de doorlooptijd en planning van productieorders.

De capaciteit kan op 2 niveaus beheerd worden

  - op afdeling (work center)

  - op beweringsplaats (machine center): één bewerkingsplaats hangt altijd onder 1 afdeling. Eén afdeling
kan wel meerdere bewerkinsgplaatsen bevatten.

De capaciteit van afdelingen en bewerkingsplaatsen wordt gebruikt om de doorlooptijd van productieorders te berekenen. Op de afdelingskaart geeft het veld “capaciteit” aan hoeveel machines of personen gelijktijdig werken binnen de afdeling. De efficiëntie geeft het maximale niveau aan tot waar de beschikbare capaciteit wordt berekend. De productieagenda geeft de werkdagen en vakantiedagen aan, en de begin- en eindtijd van de ploegen. Via de agenda die vanaf de afdeling kan geopend worden, kan de capaciteit worden berekend (of herberekend) op basis van de parameters op de afdelingskaart.

In tegenstelling tot een afdeling, heeft een bewerkingsplaats altijd aantal 1 als capaciteit. De capaciteit van de afdeling is dan de som van de capaciteit van de onderliggende bewerkingsplaatsen (als deze gebruikt worden). Commented [NH68]: Consolidated calendar = true https://learn.microsoft.com/en-
#### 7.2.4 BS40.110 Meerdere artikelen produceren in 1 productie order us/dynamics365/business-central/production-how-to-
set-up-work-and-machine-centers#consolidated- Standaard zal een BC productieorder altijd 1 product als output leveren. Er zijn echter verschillende calendar

productieprocessen waarbij meerdere artikelen in één productie process worden gemaakt. Hieronder zijn enkele mogelijkheden in BC om dit te realiseren.

##### 7.2.4.1 BC40.110.01 Productfamilies
https://learn.microsoft.com/en-us/dynamics365/business-central/production-how-work-family

Een productfamilie is een verzameling afzonderlijke artikelen die onderling gerelateerd zijn vanwege een vergelijkbaar productieproces. Binnen Business Central is een productiefamilie een standaardbegrip dat meerdere artikelen groepeert onder één familienaam, waaraan een bewerkingsplan wordt gekoppeld.

Het aanmaken van een productieorder voor een productiefamilie kan standaard alleen handmatig, aangezien productiefamilies niet worden ondersteund in de planningsvoorstellen. Hierbij wordt de Bronsoort ingesteld op Familie en het Bronnummer op de familienaam, wat resulteert in:

- Een productieorderheader met meerdere productieorderregels, waarbij elke regel overeenkomt met
een artikel binnen de familie.

- Elke productieorderregel heeft een eigen productiestuklijst.

- Het bewerkingsplan wordt overgenomen van de productfamilie.

##### 7.2.4.2 BC40.110.02 Co-Products (Aptean)
https://fnbdocs.apteancloud.com/bc/PRM/co-products/

Deze extensie maakt het mogelijk om de input eenmaal te registreren en meerdere outputs te hebben tijdens het productieproces, vergelijkbaar met de productfamilie uit standaard BC. Maar in plaats van meerdere

productieregels op 1 productieorder, is er bij coproducten 1 productieregel en heeft men bij registreren van output de mogelijkheid andere artikelen te registreren als output. Deze extensie breidt dit uit door verbruiksartikelen, die worden gebruikt voor meerdere outputs, te registreren op de productieorderregel van het hoofdartikel. Het systeem wijst dit verbruik automatisch toe aan de verschillende bijproducten wanneer de productieorder wordt afgewerkt op basis van een verdeelsleutel. Deze verdeelsleutel wordt berekend met de "Hoeveelheid per" van de productiestuklijst en de werkelijke output.

##### 7.2.4.3 BC40.110.03 Negatief verbruik
Een derde mogelijkheid, is de BOM van het artikel met artikelen aan te vullen met een negatief aantal. Via deze werkwijze, worden de grondstoffen met positief aantal in de BOM verbruikt, het eindartikel opgeboekt op de output locatie van het productieorder, en de artikelen met een negatief aantal in de stuklijst opgeboekt op de verbruikslocatie. De kosten van het productieartikel zijn dan voor 100% voor het outputartikel. Deze werkwijze is dus alleen mogelijk als de voorraad waarde van de bijproducten verwaarloosbaar is, in tegenstelling tot de 2 vorige opties.

#### 7.2.5 BS40.103 Productiestuklijsten beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/inventory-how-work-boms

Een productiestuklijst bevat alle halffabricaten, componenten en grondstoffen die deel uitmaken van het productieproces van een hoofdartikel. De materiaalbehoefte voor productieorders wordt aangestuurd door middel van de productiestuklijst. Productiestuklijsten kunnen opgebouwd worden in meerdere niveaus. Productiestuklijsten worden toegekend vanaf de artikelkaart.

Productiestuklijsten kunnen verschillende types artikelen bevatten:

- Grondstoffen
- Hulpstoffen
- Componenten
- Verpakkingsmaterialen
- Andere (niet voorraadartikelen)

Versies kunnen worden toegepast om wijzingen aan productiestuklijsten en bewerkingsplannen te laten ingaan vanaf een bepaalde datum.

Uitval % bevat het uitvalpercentage dat verwacht wordt voor het materiaal wanneer het wordt gebruikt in de productiestuklijst. Als er uitval wordt vermeld op de productiestuklijstregel, moeten er meer materialen worden voorzien. Als het uitvalpercentage bijvoorbeeld 20 % is, het Aantal per 1 is en het aantal voor het hoofdartikel 1 is, zijn er (10 x (1 + 0,20) = 12 artikelen vereist.

“Phantom” productiestuklijsten

In bepaalde gevallen wordt een productiestuklijst ontworpen voor een halfabricaat, maar wordt de productiestuklijst in productie nooit geproduceerd als een halffabricaat op zich, maar wordt dit geproduceerd als een integraal onderdeel van het afgewerkt product. Een productiestuklijst die op deze manier wordt gebruikt wordt een “phantom” productiestuklijst genoemd.

Indien verschillende artikelen deze zelfde combinatie van grondstoffen gebruikt, is het efficiënter om deze lijst van artikelen als een phantom BOM in de BOM van het eindartikel te steken, dan bij iedere eindartikel opnieuw alle onderdelen in de BOM toe te voegen.

##### 7.2.5.1 BC40.103.03 Productiestuklijst-artikelen vervangen
De batchroutine “prod.-stuklijstartikel vervangen” maakt het mogelijk om een artikel (of productiestuklijst) in een productiestuklijst te vervangen door een ander artikel (of productiestuklijst), en daarbij eventueel ook het aantal aan te passen op basis van een vermenigvuldigingsfactor. Optioneel kan hierbij ook een nieuwe productiestuklijstversie worden aangemaakt. Indien men opteert om geen nieuwe versie aan te maken wordt de originele productiestuklijst aangepast. Men heeft dan de keuze om het vervangen artikel te verwijderen uit de originele productiestuklijst of het te laten staan met een einddatum op de productiestuklijstregel.

#### 7.2.6 BS40.104 Bewerkingsplannen beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-how-to-create-routings

Bewerkingsplannen (routings) worden gebruikt om de verschillende bewerkingen in het productieproces in detail te beschrijven. In het bewerkingsplan geeft men aan op welke afdeling (work center) of bewerkingsplaats (machine center) de bewerking wordt uitgevoerd, en wat de benodigde tijd is (insteltijd, bewerkingstijd, transporttijd en wachttijd). Bewerkingsplannen vormen de basis voor productieplanning en -controle.

Bewerkingsplannen bevatten de verschillende stappen die nodig zijn in het productieproces van een artikel. Bewerkingsplannen worden opgebouwd aan de hand van afdelingen en/of bewerkingsplaatsen. Voor elke productiestap kan de insteltijd, bewerkingstijd, wachttijd na bewerking en transporttijd ingesteld worden in de gewenste tijdseenheid. Ook het uitvalaantal (in vaste waarde of %) en het doorgifteaantal (hoeveel er van de huidige bewerking moet voltooid zijn voor met de volgende bewerking kan gestart worden) kan worden ingesteld. De gelijktijdige capaciteit op de bewerkingsplanregels geeft aan hoeveel eenheden er van de afdeling/bewerkingsplaats gebruikt worden om de bewerking uit te voeren.

Versies kunnen worden toegepast om wijzingen aan productiestuklijsten en bewerkingsplannen te laten ingaan vanaf een bepaalde datum.

De routingstappen kunnen ook op 2 manieren worden opgebouwd:

- Serieel: de “eenvoudigste” manier, een stap begint pas als voorgaande stap is afgewerkt
- Parallel: een stap begint pas als 2 of meer voorgaande stappen zijn afgewerkt. Commented [NH69]: Merk op dat de eerste en laatste
stap altijd 1 routing stap moet zijn.

##### 7.2.6.1 BC40.104.03 Bewerkingsplannen met uitbesteding beheren
Uitbesteding (onderaanneming) is een productiestap die niet intern wordt uitgevoerd maar aangekocht bij een leverancier. Dit wordt in BC aangestuurd via een afdeling (work center) waarop een toeleveranciersnummer is ingesteld. De prijs voor de uitbesteding kan bepaald worden op basis van aantallen of tijdsduur. Indien de kostprijs geldig is voor alle bewerkingen bij de onderaannemer kan de kostprijs op de afdeling ingesteld worden. Doorgaans gelden specifieke kostprijzen per type bewerking die door de onderaannemer wordt uitgevoerd. In dat geval kan de kostprijs ingesteld worden in het bewerkingsplan dat aan het uitbestede artikel is gekoppeld (en wordt het veld specifieke kostprijs ingeschakeld op de afdelingskaart).

#### 7.2.7 BS40.107 Afboekingsmethode artikelen beheren tijdens productie
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-how-to-flush-components- according-to-operation-output

Materiaalverbruik kan op verschillende manieren geregistreerd worden. Indien de afboekingsmethode van artikelen is ingesteld op "handmatig" kunnen artikelen verbruikt worden via het verbruiksdagboek of productiedagboek. Met de overige afboekingsmethodes kunnen artikelen ook automatisch verbruikt worden:

- Afboekingsmethode voorwaarts: bij voorwaartse afboeking wordt verondersteld dat de verwachte
aantallen van de materialen automatisch worden verbruikt bij het vrijgeven van de productieorder.  Indien er gebruik gemaakt wordt van bewerkingsplankoppelingen in de BOM & bewerkingsplan wordt het volledige verwachte aantal van het materiaal verbruikt bij de start van de bewerking. De start van de bewerking wordt bepaald door de eerste outputboeking op de bewerking.
- Afboekingsmethode achterwaarts: bij achterwaartse afboeking worden de materialen verbruikt
wanneer de status van een productieorder wordt gewijzigd naar gereed gemeld.

 Indien er gebruik gemaakt wordt van bewerkingsplankoppelingen in de BOM & bewerkingsplan wordt het materiaal verbruikt bij het beëindigen van de specifieke bewerking. Het materiaal wordt verbruikt a rato van het aantal van de outputboeking. Het voordeel van automatisch afboeken is dat de invoer van gegevens sterk wordt beperkt. Met de mogelijkheid om een bewerking automatisch af te boeken, kan het hele verbruik- en outputregistratieproces worden geautomatiseerd. Een mogelijk nadeel van automatisch afboeken is dat het verbruik en de uitval niet nauwkeurig wordt geregistreerd. Indien verbruik heel constant is of heel moeilijk exact te bepalen, is deze werkwijze meestal de aangeraden oplossing.

##### 7.2.7.1 BC40.107.01 Backflush on lot tracked items (Aptean)
https://fnbdocs.apteancloud.com/bc/PRM/backflush-on-lot-tracked-items/ Field Code Changed

Materialen en componenten die tijden de productie worden verbruikt, kunnen worden ingesteld met backflushing. (zie hierboven) Bij de standaardfunctionaliteit moet je manueel de lotnummers ingeven bij het gebruik van de backward flush-methode vooraleer de status van de productieorder op voltooid kan gezet worden. Deze extensie breidt dit uit door dit automatisch te doen bij het registreren van output. Dit is mogelijk bij elke stap in het bewerkingsplan. Er wordt onderscheid gemaakt tussen lotnummers die met en zonder vervaldatum worden aangemaakt. Wanneer deze vervaldatum is toegekend, worden de lotnummers met de vroegste vervaldatum (met een resterende hoeveelheid) toegewezen in de artikel trackingregels. Deze methode volgt het FEFO-principe (First Expired, First Out). Lotnummers zonder vervaldatum worden echter toegewezen op basis van FIFO (First In, First Out). Dit betekent dat de artikelboeking (met een resterende hoeveelheid) met het laagste boekingsnummer het eerst wordt toegewezen. Commented [NH70]: Opmerking: dit kan uitdagingen geven bij overpicking voor productie. Ook bij FEFO als
##### 7.2.7.2 BC40.107.02 Consolidated consumption (Aptean) er meerdere loten zijn met zelfde vervaldatum
https://fnbdocs.apteancloud.com/bc/PRM/consolidated-pick-and-consolidated/

Geconsolideerde consumptie kan nuttig zijn in hectische productieomgevingen waar de operators op de werkvloer geen tijd hebben om het verbruik handmatig te boeken. Hierbij is een routine voor geconsolideerde consumptie nodig. Bij geconsolideerde consumptie wordt de totale inhoud van een bin die in geselecteerde productielijnen wordt gebruikt, pro rata aan deze productielijnen toegewezen en als verbruik geboekt. De overschot van de artikelen die zijn klaargezet op de bij waarvan verbruikt wordt, moet dus eerst terug naar het magazijn verplaatst worden, voordat deze functie wordt uitgevoerd. Dit geconsolideerd verbruik kan per dag of per shift gebeuren.

#### 7.2.8 BS40.108 Uitval en afval artikelen beheren
Bij een productieproces is er uitval en/of afval mogelijk. Ook deze kunnen verwerkt worden via BC. In dit scenario worden de instellingen die nodig zijn om hier mee om te gaan behandeld.

De standaardwaarden voor uitval kunnen op verschillende plaatsen gedefinieerd worden via veld “uitval %”:

- Op de artikelkaart

- Op productiestuklijstregels
- Op de bewerkingsplaats
- Op de bewerkingsplanregels

Practisch zal het instellen van uitval, de hoeveelheid die nodig is om een goed eindartikel te verkrijgen verhogen met het ingestelde uitval %. Dit verhoogt de kostprijs en de benodigde hoeveelheid om klaar te zetten voor een productieorder.

### 7.3 Productieorders beheren
#### 7.3.1 BS40.200 Productieorders maken
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-about-production-orders

Productieorders kunnen gemaakt worden in 4 verschillende statussen. Op het productieorder wordt het verbruik (BOM) en de capaciteit (Routing) van het artikel gecombineerd op een werkdocument, met als doel deze 2 parameters te registeren op het vrijgegven productieorder.

- Gesimuleerde productieorders maken: Gesimuleerde productieorders worden hoofdzakelijk gebruikt
voor het maken van simulaties en waarderingen, bijvoorbeeld voor het maken van een kostprijsberekening van een artikel. Een gesimuleerd productieorder fungeert als een voorbeeld voor een productieorder. Gesimuleerde productieorders hebben geen invloed op de effectieve planning van productieorders. Planning (MPS en MRP) houdt geen rekening met gesimuleerde productieorders.
- Geplande productieorders maken: Geplande productieorders zijn geven de werklast weer van
afdelingen (work centers) of bewerkingsplaatsen (machine centers). Ook de nodige materialen (grondstoffen, halffabricaten, verpakkingsmaterialen enz.) worden berekend. Manueel geplande productieorders worden verwijderd bij het berekenen van planningsvoorstellen. Geplande productieorders die gemaakt worden vanuit een verkooporder, blijven wel behouden tijdens een planningsvoorstel.
- Vast geplande productieorders maken: Vast geplande productieorders: worden gebruikt om capaciteit
van afdelingen of bewerkingsplaatsen en de benodigde materialen te alloceren. Vast geplande productieorders worden niet verwijderd bij het berekenen van planningsvoorstellen, maar kunnen wel herpland worden of het aantal kan gewijzigd worden.
- Vrijgegeven productieorders maken: Vrijgegeven productieorders worden gebruikt voor de registratie
van verbruik, output en capaciteit (deze registraties zijn enkel mogelijk op vrijgegeven productieorders). Bij aanmaken van een vrijgegeven productieorder selecteert men het artikelnummer, de vestiging en de gewenste hoeveelheid. Via de actie "vernieuwen" worden de nodige materialen en bewerkingen berekend die nodig zijn voor de uitvoering van de productie. Hiervoor worden de productiestuklijst (materialen) en het bewerkingsplan (bewerkingen op afdelingen en bewerkingsplaatsen) toegepast die aan het artikel zijn gekoppeld, of de actieve versie van de productiestuklijst en bewerkingsplan indien er met versies wordt gewerkt. De productieorder-materialen en -bewerkingsplannen kunnen op de productieorder verder aangevuld of aangepast worden, bijvoorbeeld voor een eenmalige wijziging die enkel van toepassing is op de productieorder.

#### 7.3.2 BS40.212 Productieorders plannen
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-how-to-replan-refresh- production-orders

Zie BS30.202 - Beoordelen en fiatteren planningsvoorstellen: BC zal op basis van de benodigde datum van behoefte, productieorders plannen om deze voorraad aan te vullen. BC plant standaard achterwaarts: de verzochte leverdatum van de klant is het vertrekpunt en BC berekent wanneer productie & inkoop zouden moeten gebeuren voor alle benodigde materialen of het finale product aan de klant te leveren.

Het planningsvoorstel zal alle gesimuleerde en geplande orders verwijderen en opnieuw aanmaken met de nieuwe “optimale” datum volgens het BC algoritme.

Voor vast geplande & vrijgegeven productieorders, zal het planningsvoorstel deze orders niet herplannen.

De MRP planning zal ervoor proberen zorgen dat er voldoende voorraad is van alle grondstoffen, maar indien de levertermijn van een bepaalde grondstof ervoor zorgt dat een start datum van een productieorder of een inkooporder in het verleden ligt, wordt dit aangeduid in het planningsvoorstel (warnings of exception), het productieorder wordt niet automatisch naar achter gepland. Dit is een manuele actie, die best wordt aangevuld met aanpassing van de verzenddatum van het verkooporder.

##### 7.3.2.1 BC40.212.01 Production scheduling (Aptean)
https://fnbdocs.apteancloud.com/bc/PSG/contents/

- Workload
Met de production scheduling extensie kunt u productieorders efficiënter inplannen. Het geeft een visuele weergave van de werklast die aan meerdere werkcentra/machinecentra is toegewezen voor de nabije toekomst. Hieruit kan men conclusies trekken over de belasting van de werk- en machinecentra.

- Production order planning

Deze extensie biedt cruciale informatie die helpt bij het nemen van de juiste planningsbeslissingen. Op deze pagina zijn er verschillinde functionaliteiten om productieorders te verplaatsen. Na het verplaatsen kunnen de veranderingen gezien worden in het volledige productieplan. De volgende zaken zijn zichtbaar vanaf deze pagina:
  - Het is mogelijk om eventuele overlappingen tussen orders te bekijken om te zien of alles op één
dag past.
  - Het is mogelijk om de relatie tussen verkooporders en hun vervaldata te bekijken.
  - Het is mogelijk om de productieorders te sorteren op basis van de artikelattributen.

- Production scheduling attributes

De productieplanning attributen zijn specifieke artikelattributen die kunnen worden gebruikt bij het plannen van productieorders. Wanneer bijvoorbeeld chocolade wordt geproduceerd, is het efficiënt om eerst witte chocolade, dan melk en dan pure chocolade te produceren. Op die manier hoeft de productielijn niet te worden gereinigd bij het overschakelen tussen batches. Dit omdat zwarte chocolade de witte chocoladebatch zou beïnvloeden. Bijgevolg moeten de productieorders worden gepland in de volgorde van witte, dan melk en daarna pure chocolade. De productieplanning attributen kunnen worden ingesteld om deze volgorde van productieroutines te bereiken.
- Add downtime

Binnen de voedingsindustrie is het reinigen en onderhouden van productielijnen van vitaal belang. Vooral in omgevingen waar vaak wordt gewisseld tussen verschillende geproduceerde items met verschillende recepturen of anders gekleurde ingrediënten. Hierbij kunnen deze schoonmaak-/onderhoudsbeurten veel tijd in beslag nemen. Om dit proces efficiënt te plannen, is het mogelijk om standaard tijdvensters per werkcentrum in te stellen en deze te gebruiken binnen het productieplanningsproces.

##### 7.3.2.2 BC40.212.02 Visual Advanced Production Schedular (VAPS)
Een tweede mogelijkheid om de beperkte planningstools van BC uit te breiden is de VAPS extensie. https://help.netronic.com/en/visual-advanced-production-scheduler-vaps-for-dynamics-365-business-central

Deze extensie focust zich vooral op het visueel maken van de verschillende productieorders en hun bijhorende productiestappen. Via deze extensie krijgt de planner een visuele voorstelling van de verschillende productiestappen en eventuele planningsconflicten voor de bewerkingsplaatsen.

VAPS doet een semiautomatisch planningsvoorstel, waarbij de planner dan de eventuele conflicten kan oplossen.

Daarnaast biedt VAPS ook mogelijkheden om te controleren of alle grondstoffen voor een bepaald productieorder beschikbaar zijn bij de start van het productieorder.

Tenslotte zal de herplanning van een bepaalde productiestap, automatisch alle volgende productiestappen ook herplannen.

#### 7.3.3 BS40.201 Productieordermaterialen beheren
Dit scenario behandelt het beheer van productieorder-materialen op een productieorder, maw als er afwijkingen nodig zijn tov de standaard BOM. Productieorder-materialen zijn de artikelen (grondstoffen, verpakkingsmaterialen, halffabricaten, …) die nodig zijn voor de uitvoering van een productieorder.

Wanneer een productieorder wordt gemaakt, worden de artikelen uit de productiestuklijst/BOM die aan het geproduceerde artikel is gekoppeld, toegepast op de productieorder. De aantallen worden berekend op basis van het aantal op de productieorder. Vanaf de productieorder kunnen de productieordermaterialen geraadpleegd worden en ook wijzigingen aangebracht worden, zoals het toevoegen of verwijderen van productieordermaterialen, het wijzigen van het aantal of het selecteren van een vervangartikel.

##### 7.3.3.1 BC40.201.01 Production scenarios (Aptean)
https://fnbdocs.apteancloud.com/bc/PSC/contents/

De Aptean scenario’s extensie maakt het mogelijk om meerdere productiescenario’s op te zetten voor hetzelfde outputartikel. Zo kunnen artikelen op verschillende manieren worden geproduceerd. Vb : een artikel kan vanaf nul worden geproduceerd, maar ook op basis van een halffabricaat. Hier gebruiken beide scenario's een andere productiestuklijst en bewerkingsplan. Een ander voorbeeld is dat hetzelfde productieartikel kan worden geproduceerd op meerdere productielijnen op verschillende locaties met verschillende grondstoffen, ingrediënten en/of verpakkingsmaterialen. Daarom kan men meerdere productiescenario's opzetten waarbij per scenario een specifieke productiestuklijst-, bewerkingsplan- en locatiecode moet worden toegewezen aan hetzelfde productieartikel. Bovendien is het mogelijk om per locatie standaard één productiescenario toe te wijzen. Bij het aanmaken van productieorders wordt het standaard productiescenario toegepast. De gebruiker kan voor elk productiescenario een productie-eenheid instellen. Deze vervangt de maateenheid die oorspronkelijk uit de velden productiestuklijstnummer en bewerkingsplan nummer kwam. Productiescenario's worden ook gebruikt om in één keer de productiestuklijst, bewerkingsplan en productie- eenheid voor een productieorder te wijzigen via de functie productiescenario wijzigen.

#### 7.3.4 BS40.221 Productiematerialen klaarzetten
De materialen die op het productieorder staan, moeten klaargezet worden op de voorziene opslaglocatie voor het productieorder. Via welke document de goederen klaargezet worden, wordt bepaald door de instellingen van de vestiging (zie hoofdstuk “Magazijnbeheer”).

##### 7.3.4.1 BC40.211.01 Picking
https://learn.microsoft.com/nl-be/dynamics365/business-central/warehouse-how-to-set-up-locations-to-use- bins

Voor het klaarzetten van de grondstoffen of onderdelen voor productie zijn er 2 cases:

- Goederen worden klaargezet voor één specifiek productieorder
 Indien Afboekingsmethode = manueel/pick+voorwaarts/Pick+achterwaarts
- Goederen worden klaargezet voor meerdere productieorders
 Indien Afboekingsmethode = voorwaarts/achterwaarts

Dus in de eerste case, zijn goederen specifieke klaargezet voor één productieorder. Als er grondstoffen over zijn na de productie, moeten deze teruggeplaatst worden in het magazijn en voor het volgende productieorder gepikt worden. De eventuele lotnummers van de grondstoffen zijn ook gekend voor dit productieorder. Standaard moeten de lotnummers die verbruikt worden , manueel worden ingegeven. In de Cegeka oplossing is dit aangepast, ze worden eerst FEFO (goederen met oudste vervaldatum) en dan FIFO (als er meerdere paletten met zelfde vervaldatum staan, dan verbruikt BC verbruikt eerst de paletten die eerst gepikt zijn).

In de tweede case, zijn goederen niet specifiek klaargezet voor een order, maar voor alle orders. Ze worden dan ook verbruikt volgens een “first come, first served principe”. Wie het eerst grondstoffen wil verbruiken, zal deze eerst verbruiken. In deze case moet men bij verbruik van grondstoffen, wel specifiëren welke lotnummers voor welk productieorder worden verbruikt.

##### 7.3.4.2 BC40.211.02 Consolidated pick (Aptean)
https://fnbdocs.apteancloud.com/bc/PRM/consolidated-pick-and-consolidated/

De geconsolideerde pick maakt het mogelijk om in één keer een verplaatsing van geselecteerde onderdelen uit meerdere productieorders te maken, vergelijkbaar met de bovenstaande oplossing van open shopfloor. Maar met het verschil dat de lottracering van verbruik wel automatisch gebeurt. Zo kan de desbetreffende persoon het picken van componenten van meerdere productieorders in één magazijnactie doen in plaats van de componenten te picken per productieorder. Per artikel/voorraadeenheid moet worden aangegeven of een geconsolideerde picking van de magazijn bin naar de productie bin is ingeschakeld. Dit zorgt voor een hogere efficiëntie.

Let wel op: wanneer je voor een artikel geconsolideerde pick inschakelt, moet je de geconsolideerde pick ook gebruiken. De andere functies aanwezig op een vrijgegeven productieorder gaan artikelen waarvoor geconsolideerde pick is ingeschakeld, overslaan bij het verplaatsen van magazijn naar productie. Voor de lotnummer tracering bij geconsolideerd verbruik: de lotnummers worden verdeeld over alle productieorders. Als er 2 loten gepicked zijn voor 4 productieorders, zullen de 4 productieorders ieder de beide loten van de grondstof gebruiken.

##### 7.3.4.3 BC40.211.03 Over and Under-pick production consumption (Aptean +
Cegeka + standaard) STD BC: https://learn.microsoft.com/en-us/dynamics365/release-plan/2025wave1/smb/dynamics365- Field Code Changed business-central/enable-over-picking-production-orders

Aptean: https://fnbdocs.apteancloud.com/bc/OUP/contents/ Field Code Changed

De Aptean uitbreiding underconsumption maakt het mogelijk om meer of minder grondstoffen te gebruiken dan oorspronkelijk gepland op de componentregel. Over-pick kan geregistreerd worden voor een productieorder door het gebruik van een voorraad of een magazijnpick. Dit betekent dat het mogelijk is om meer grondstoffen te registreren dan de oorspronkelijk vereiste hoeveelheid, zonder dat de pick hoeveelheid wordt verhoogd. Bijvoorbeeld, als er voor een productieorder 24,99 kg van een bepaalde grondstof nodig is en de verpakking 25 kg bevat, kan de medewerker de volledige 25 kg gebruiken zonder de productieorder aan te passen. Onder-pick (Aptean)kan worden gebruikt om een magazijnactiviteit als voltooid te markeren, zelfs als er minder grondstoffen zijn geregistreerd dan de oorspronkelijke hoeveelheid. Dit betekent dat het niet nodig is om een nieuwe verpakking te openen als er niet genoeg grondstof beschikbaar is. De resterende hoeveelheid wordt na de registratie op nul gezet. Bijvoorbeeld, als een verpakking van een bepaalde grondstof leeg is en er slechts een kleine hoeveelheid nodig is voor het recept, kan de medewerker deze hoeveelheid registreren en de resterende hoeveelheid op nul zetten. Opmerking: oorspronkelijk niet beschikbaar in standaard BC, vandaar dat er verschillende versies bestaan.

#### 7.3.5 BS40.202 Productieorderbewerkingsplannen beheren
Wanneer een productieorder wordt gemaakt, worden de bewerkingen uit het bewerkingsplan dat aan het geproduceerde artikel is gekoppeld, toegepast op de productieorder. Vanaf de productieorder kan het productieorder-bewerkingsplan geraadpleegd worden. Er kunnen ook wijzigingen aangebracht worden, zoals het toevoegen of verwijderen van bewerkingen of het wijzigen van de insteltijd, bewerkingstijd, transporttijd of wachttijd na bewerking.

#### 7.3.6 BS40.203 Productieorders herplannen
De functie “Herplannen” in productieorders wordt doorgaans gebruikt nadat er materialen zijn toegevoegd of gewijzigd die onderliggende productieorders hebben. Met de functie worden wijzigingen berekend die in

materiaal- en bewerkingsplanregels zijn aangebracht. De functie heeft betrekking op lagere productiestuklijstniveaus en er kunnen nieuwe productieorders mee worden gegenereerd.

Op basis van de wijzigingen die u hebt aangebracht in de materiaal- en bewerkingsplanregels, zorgt de functie "Herplannen" voor het berekenen en plannen van alle nieuwe vraagregels voor de productieorder.

#### 7.3.7 BS40.204 Productieorders kostprijs bijwerken
https://learn.microsoft.com/nl-be/dynamics365/business-central/finance-about-finished-production-order- costs

De actie "Kostprijs bijwerken" op productieorders herrekent de kosten van productieartikelen op productieorders en werkt de kostprijs bij op de productieorderregel. Deze actie werkt de standaardkostprijs van een artikel op de artikelkaart of SKU kaart NIET bij.

### 7.4 Verbruik en output boeken
#### 7.4.1 BS40.205 Registratie verbruik en output
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-how-to-register-consumption- and-output

Dit scenario behandelt de registratie van verbruik (registratie van de materialen zoals grondstoffen, verpakking enz. die nodig zijn voor de productie) en output (geproduceerde artikelen zoals eindproducten, halffabricaten en bulk).

##### 7.4.1.1 BC40.205.01 Registreer verbruik en output (lot tracering)
Het productiedagboek combineert de registratie van verbruik en output in één scherm, dat direct toegankelijk is vanaf een vrijgegeven productieorder. Het doel van het productiedagboek is het bieden van één interface waarin u het verbruik en de output van een productieorder kunt registreren.

Het dagboek wordt direct vanuit een vrijgegeven productieorder geopend. De gegevens van de productieorder worden automatisch ingesteld in het dagboek.

Registratie van productie verbruik houdt in:

- Registreren van de verbruikte artikelen op basis van de productiestuklijsten (BOM)

- Registreren van de lotnummers: zie BS40.211 voor opties voor automatisch registeren van lotnummers

Registratie van productie-output houdt in:

- Het registreren van het aantal artikelen dat wordt geproduceerd
 Registreren van lotnummer(s) van de output (indien niet automatisch is toegekend)

- Registratie van uitval bij output
- De tijd die besteed is aan het uitvoeren van de bewerkingen

Deze informatie kan gebruikt worden voor een latere berekening gebaseerd op de werkelijke registraties (nacalculatie). Productieoutput kan worden berekend op basis van de verwachte aantallen van de productieorders. Het berekende voorstel kan manueel aangepast worden om te voldoen aan de reële registraties.

##### 7.4.1.2 BC40.205.02 Registreer reële hoeveelheden (registratie)
Het verbruiksdagboek kan worden toegepast voor de registratie van verbruik van materialen op productieorders. Via de actie “verbruik berekenen” wordt het verbruik voor één of meerdere productieorders berekend. Het verbruik kan berekend worden op basis van de verwachte output of de werkelijke geregistreerde output. De berekening resulteert in verbruiksregels op basis van de productieordermaterialen. De voorgestelde regels kunnen indien nodig aangepast (of verwijderd) worden, bijvoorbeeld wanneer het werkelijk verbruikt aantal niet overeenkomt met de berekende waarde. Indien er voor de componenten gebruik gemaakt wordt van artikeltracering kunnen de lotnummers (of serienummers) geselecteerd worden via de artikeltraceringsregels. Als laatste stap wordt het verbruiksdagboek geboekt, waarbij de artikelposten op de productieorders worden geregistreerd.

##### 7.4.1.3 BC40.205.03 Registreer theoretische hoeveelheden
Materiaalverbruik kan op verschillende manieren geregistreerd worden. Artikelen kunnen verbruikt worden via het verbruiksdagboek, maar kunnen ook automatisch verbruikt worden via een automatische afboekingsmethode (zie ook BS40.211 ivm picking):
- Afboekingsmethode voorwaarts: bij voorwaartse afboeking wordt verondersteld dat de verwachte
aantallen van de materialen automatisch worden verbruikt bij het vrijgeven van de productieorder. Indien er gebruik gemaakt wordt van bewerkingsplankoppelingen wordt het materiaal verbruikt bij de start van de bewerking (via bewerkingsplankoppelingen kan een link gemaakt worden tussen een bepaalde bewerking en de materialen die bij deze bewerking worden verbruikt).
- Afboekingsmethode achterwaarts: bij achterwaartse afboeking worden de materialen verbruikt
wanneer de status van een productieorder wordt gewijzigd naar gereed gemeld. Indien er gebruik gemaakt wordt van bewerkingsplankoppelingen wordt het materiaal verbruikt bij het beëindigen van de bewerking.

##### 7.4.1.4 BC40.205.04 Shop floor production (Aptean)
https://fnbdocs.apteancloud.com/bc/SFPBC/introduction/ Met behulp van de 'Shop Floor Production'-uitbreiding is het gemakkelijk om de input en output van een productieorder op de werkvloer te registreren. Ook het bijhouden van de duur van een productieorder in verschillende stadia is mogelijk met deze uitbreiding. De uitbreiding bestaat uit vier onderdelen:

- Shop Floor Production-app
- Shop Floor Production Work Instruction Setup-app
- Shop Floor Production Setup and Monitoring-app

Met de Shop Floor Production-app kunnen gebruikers de input en output van een productieorder registreren. De app toont informatie over details, werkvoorschriften en opmerkingen voor elke productieorder. Gebruikers kunnen ook de status van een productieorder aangeven, bijvoorbeeld of deze wordt opgestart, gepauzeerd is of er een storing is opgetreden. De tijd die nodig is voor de verschillende stadia van een productieorder wordt geregistreerd met behulp van tijdregistraties. Afhankelijk van de instellingen kunnen deze tijdregistraties worden geboekt als capaciteitsboekingen in Dynamics 365 Business Central. In de Shop Floor Production Work Instruction Setup-app kunnen werkvoorschriften worden gekoppeld aan een werkcentrum, item of een combinatie van beiden. Daarnaast kunnnen ook de kwaliteitstriggers (zie BC45.200.07) worden afgehandeld via de shopfloor app. De Shop Floor Production- en Shop Floor Production Work Instruction-apps kunnen worden weergegeven in verschillende talen. De Shop Floor Production Setup and Monitoring-app kan worden gebruikt om deze talen en vertalingen in te stellen. Deze app toont ook alle registraties die zijn gemaakt met de Shop Floor Production-app.

#### 7.4.2 BS40.902 Process Manufacturing (Aptean)
https://fnbdocs.apteancloud.com/bc/PRM/contents/

In de productie-industrie is het gebruikelijk om eerst een bulkmateriaal te produceren dat daarna wordt verpakt in handelseenheden (bv. kartonnen dozen). Deze handelseenheid bevat dan een bepaalde hoeveelheid consumptie eenheden (bv. Blikken 250ml/330ml). Het bulkmateriaal wordt vaak geproduceerd in een silo, blender of dergelijk machine. Deze worden als werk- of machinecentra gezien in Business Central. Elk werk- en machinecentrum heeft zijn eigen capaciteit. Voor de voorbereiding en de uitvoering van het productieproces is het noodzakelijk dat we weten hoeveel batches we moeten produceren voor het gewenst aantal (half)afgewerkte producten. Eveneens is het ook noodzakelijk dat we hierbij weten hoeveel kg/liter/stuks van ingrediënten en grondstoffen nodig zijn voor een batch te produceren. De process manufacturing extensie biedt hier een overzichtelijk antwoord op door de toevoeging van enkele velden op de productiestuklijst, productieorder en componenten.

##### 7.4.2.1 BC40.902.01 Gewicht en opbrengst percentage
https://fnbdocs.apteancloud.com/bc/PRM/weight-and-yield-percentage/

Het totale gewicht van de productiestuklijst wordt automatisch berekend gebaseerd op:
- Het type gewicht dat in aanmerking wordt genomen (netto- of brutogewicht)
- Het gewicht van een specifieke stuklijst component vóór het productieproces. Dit gewicht wordt
berekend op basis van de ingegeven hoeveelheid van de component, omgezet naar de gewichtseenheid van de productiestuklijst.
- Het gewicht van een specifieke stuklijst component na het productieproces. Dit gewicht wordt berekend
op basis van de ingegeven hoeveelheid van de component, omgezet naar de gewichtseenheid van de productiestuklijst.

Deze velden worden samengevoegd om inzicht te geven in het totale netto- en brutogewicht van één geproduceerde eenheid (uitgedrukt in de meeteenheid van de productiestuklijst). Tevens wordt uit deze cijfers het opbrengstpercentage berekend. Dit is wat er daadwerkelijk als output overblijft na het productieproces.

##### 7.4.2.2 BC40.902.02 Unplanned consumption function
https://fnbdocs.apteancloud.com/bc/PRM/unplanned-output-consumption/ Field Code Changed De functie ongeplande consumptie maakt het mogelijk een of meer artikelen in te stellen die bijvoorbeeld een onderdeel kunnen vervangen of als alternatief kunnen dienen wanneer een materiaal niet beschikbaar is. Dit wordt gedaan zodat een werkvloermedewerker onderdelen kan toevoegen zonder de geselecteerde productiestuklijst in de productieorder te wijzigen. Als tijdens het productieproces ongeplande consumptie moet worden toegevoegd, bijvoorbeeld omdat een bepaald artikel uit voorraad is geraakt, is het noodzakelijk de artikelen die als ongepland verbruik kunnen worden toegevoegd te beperken. Op die manier kan het productieproces worden voortgezet met een ander component dan het geplande artikel uit de productie stuklijst.

##### 7.4.2.3 BC40.902.03 Production variances
https://fnbdocs.apteancloud.com/bc/PRM/production-variances/

In standaard BC berekent de productieorderstatistiek de variantie en afwijking tussen de standaardkosten en de werkelijke kosten. Als de werkelijke kosten niet worden gebruikt, is de variantie daartussen niet zichtbaar. Deze extensie voegt de variantie en afwijking tussen de verwachte en werkelijke kosten toe. Dit is handig voor een variantie-analyse.

##### 7.4.2.4 BC40.902.04 Dimension in consumption posting
Standard Business Central gebruikt altijd de dimensiecode van het outputartikel in een productieorder. In de process manufacturing setup kan worden gedefinieerd welke dimensiecode wordt gebruikt voor het productieverbruik: het standaard uitvoerartikel of het verbruiksartikel.

### 7.5 Uitval boeken
#### 7.5.1 BS40.206 Uitval boeken
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-how-to-post-scrap

Uitval wordt gedefinieerd als een gedeelte van de output van een productieorder dat niet aan de vereisten voldoet en niet kan worden gebruikt als afgewerkt product of halfabricaat.

Uitval voor productie-output kan geboekt worden via het productiedagboek. Hiervoor wordt op de regel waar output op geboekt wordt het veld “uitvalaantal” ingevoerd worden. Bij het boeken van de output wordt het uitvalaantal geregistreerd in de gekoppelde capaciteitsposten. Het aantal dat als uitval geboekt wordt, komt niet op voorraad, maar verbruikt wel grondstoffen.

### 7.6 Capaciteit boeken
#### 7.6.1 BS40.207 Capaciteit boeken
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-how-to-post-capacities

De beschikbare capaciteit wordt ingesteld op afdelingen en bewerkingsplaatsen volgens een productiekalender en de toegewezen ploegen. Het aanmaken van productieorders resulteert in een werklast op de afdelingen en machines op basis van het bewerkingsplan dat gekoppeld is aan het artikel (en wordt toegepast op de productieorder). De toegewezen capaciteit kan geraadpleegd en bijgestuurd worden, bijvoorbeeld door het verplaatsen van een productieorder-bewerking naar een andere afdeling of bewerkingsplaats, of door het herplannen van een productieorder naar een andere datum.

Dit scenario beschrijft de registratie van de verbruikte uren van afdelingen en/of bewerkingsplaatsen die men niet op productieorders wenst toe te wijzen, bijvoorbeeld het uitvoeren van onderhoud of herstellingen aan machines.

Om de capaciteit die niet is toegewezen aan een productieorder te boeken kan er gebruik gemaakt worden van het capaciteitsdagboek.

### 7.7 Uitbesteding beheren
#### 7.7.1 BS30.209 Uitbestedingsvoorstellen berekenen
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-how-to-subcontract- manufacturing

Als er een behoefte ontstaat aan uitbesteed werk, dan zal hiervoor een productieorder worden voorgesteld via het planningsvoorstel. Ook de noodzakelijke transferorders (om de goederen bij de onderaannemer te krijgen of terug te doen keren naar het eigen magazijn.) zullen in het planningsvoorstel worden voorgesteld.

Uitbesteding wordt gedefinieerd als het uitvoeren van één of meerdere bewerkingen bij een externe leverancier. Hiervoor wordt op de afdeling (work center) een leverancier ingesteld. Wanneer een dergelijke afdeling wordt opgenomen in een bewerkingsplan en dit wordt gebruikt in een productieorder, resulteert dit in een behoefte voor uitbesteding.

Via het uitbestedingsvoorstel kunnen de behoefte voor uitbesteding berekend worden. Dit resulteert in voorstellen voor het aanmaken van inkooporders voor uitbesteding.

#### 7.7.2 BS30.210 Uitbestedingsvoorstellen beoordelen en fiatteren
Nadat de uitbesteding berekend is in het uitbestedingsvoorstel kunnen de voorstellen beoordeeld worden. Hierbij geeft het veld “planningsboodschap accepteren” of de voorgestelde actie moet worden uitgevoerd. Er worden inkooporders gemaakt gegroepeerd per leverancier. Bewerkingen voor verschillende productieorder die bij dezelfde uitbesteder worden uitgevoerd worden dus gebundeld op één verkooporder.

#### 7.7.3 BS40.208 Uitbestedingsinkooporders boeken
De ontvangst van artikelen die door een externe leverancier worden geproduceerd (uitbesteding) wordt geregistreerd als een ontvangst op de inkooporder voor uitbesteding.

Bij het boeken van de ontvangst zijn er 2 situaties mogelijk:

- De inkooporderregel is gekoppeld aan de laatste bewerking uit het productieorder-bewerkingsplan: in
dat geval wordt er capaciteit en output geboekt. Door de output-boeking komt het artikel op voorraad.
- De inkooporderregel is gekoppeld aan een productieorder-bewerkingsplanregel die niet de laatste
bewerking van de productieorder is: in dat geval wordt er enkel capaciteitsposten geboekt en komt het artikel niet op voorraad.

Combinaties van beide zijn mogelijk, bijvoorbeeld wanneer het bewerkingsplan meerdere bewerkingen bij dezelfde leverancier bevat, die via hetzelfde inkooporder voor uitbesteding worden verwerkt. Indien het niet wenselijk is dat het artikel op voorraad komt bij ontvangst van de uitbesteding, bijvoorbeeld omdat er nog een interne kwaliteitscontrole nodig is, kan er een extra interne bewerking aan het bewerkingsplan toegevoegd worden.

### 7.8 Productieorders afsluiten
#### 7.8.1 BS40.209 Productieorders afsluiten
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-about-production- orders#finished-production-order

Wanneer de registratie van verbruik, output en capaciteit voltooid is, kan de productieorder afgesloten worden. Hiervoor wordt de status gewijzigd naar gereed gemeld. Het wijzigen van de status van productieorders kan manueel (order voor order) of in batch gebeuren.

Bij het gereed melden van een productieorder worden aan een aantal controles uitgevoerd om te verifiëren of het order kan gereed gemeld worden:
- Is het materiaalverbruik geregistreerd?
- Is de capaciteit (bewerkingstijd) geregistreerd?
- Is de output geregistreerd?

Wanneer een productieorder wordt gereed gemeld worden de productieorder-materialen voor artikelen die zijn ingesteld met afboekingsmethode "achterwaarts" als verbruik geboekt (indien er gebruik gemaakt wordt van bewerkingsplankoppelingen kunnen deze artikelen reeds worden afgeboekt bij het gereed melden van de bewerking).

Nadat een productieorder is gereed gemeld, kunnen er geen registraties meer op uitgevoerd worden.

##### 7.8.1.1 BC40.209.01 Heropenen van productieorders
https://learn.microsoft.com/nl-nl/dynamics365/release-plan/2025wave1/smb/dynamics365-business- central/reopen-finished-production-orders

Oorspronkelijk konden gereedgemelde productieorders niet heropend worden in BC. Sinds v26 van BC is dit wel mogelijk om zo bepaalde correcties te doen (vb verbruik corrigeren, lot- of serienummers aanpassen, kostentransacties rechtzetten).

Er zijn 2 belangrijke beperkingen:
- Heropenen kan slechts 1 keer gebeuren
- Heropenen kan alleen voor productieorders waar output is geboekt.

### 7.9 Kostprijzenbeheer
Het sub domein kostprijzenbeheer bevat het uitvoeren van kostprijscalculaties en -simulaties voor productieartikelen (doorgaans met waarderingsmethode "vaste verrekenprijs"). Kostprijsboekhouding beschrijft het scenario voor het toewijzen van kosten aan kostendragers op basis van vooraf gedefinieerde regels.

#### 7.9.1 BS40.218 Beheer Fin. Master Data Kostprijscalculatie
Dit scenario beschrijft de instellingen die nodig zijn om de kostprijsberekening in Business Central in te stellen.

https://learn.microsoft.com/nl-be/dynamics365/business-central/finance-about-calculating-standard-cost

Materiaalkosten

De kostprijs van artikelen (grondstoffen, halffabricaten, verpakkingen, …) bestaat uit onderstaande segmenten:

- Vaste verrekenprijs: bevat de standaard kostprijs op basis van een kostprijscalculatie (voor
productieartikelen) of inkoopbedragen. Wordt enkel gebruikt in combinatie met waarderingsmethode = vast.
- Kostprijs: voor de andere waarderingsmethodes (FIFO, LIFO, specifiek of gemiddeld) wordt dit veld
automatisch bijgewerkt bij het boeken van inkoopfacturen of output (productie).
- Indirecte kosten %: bevat het percentage van de directe kosten van het artikel dat als indirecte kosten
wordt beschouwd (bijv. vrachtkosten, opslag, …).
- Overheadtarief: Bevat de indirecte kosten van het artikel als absoluut bedrag.
Capaciteitskosten

Standaard productiekosten worden, naast de materiaalkosten, bepaald door de toegepaste afdelingen (work centers) en bewerkingsplaatsen (machine centers).

De kostprijs van afdelingen en bewerkingsplaatsen bestaat uit onderstaande segmenten:

- Directe kostprijs: geeft de directe eenheidsprijs (per eenheid) weer van de afdeling of bewerkingsplaats.
Deze eenheid is uitgedrukt in tijd of per eenheid.
- Indirecte kosten %: geeft de kostprijs van de afdeling of bewerkingsplaats weer als een percentage.
Indirecte kosten zijn kosten die niet direct aan een eenheid kunnen worden toegewezen, zoals een algemene werkingskost van een afdeling.
- Overheadtarief: Het overheadtarief is een absolute waarde. Een overheadtarief kan worden ingesteld
voor andere kosten dan materiaal- of capaciteitskosten, zoals bijvoorbeeld een onderhoudskost voor een afdeling.

#### 7.9.2 BS40.219 Voer kostprijscalculatie uit
Voor geproduceerde artikelen wordt bij voorkeur de waarderingsmethode Vast gebruikt. Dit omdat zo de voorraadwaarde niet verandert bij elke productieorder, terwijl men wel nog de mogelijkheid heeft om de productievarianties te analyseren voor ieder onderdeel (materiaal, capaciteit en overhead). De standaard functionaliteit in BC biedt de mogelijkheid om de vaste verrekenprijs te berekenen:
- Vanaf de artikelkaart, via de functie Vaste verrekenprijs berekenen
- Via het vaste verrekenprijsvoorstel

Bij deze methodes wordt de vaste verrekenprijs berekend op basis van de materialen uit de gekoppelde productiestuklijsten en de bewerkingen uit de gekoppelde bewerkingsplannen.

Voor artikelen met een andere waarderingsmethode kan de vaste verrekenprijs op dezelfde wijze berekend worden, maar wordt deze niet toegepast in de uiteindelijke waardering van de artikelen, voor ieder productieorder is de kostprijs anders op basis van de werkelijk verbruikte materialen en

#### 7.9.3 BS40.220 Voer kostprijssimulatie uit
Voor het uitvoeren van een kostprijssimulatie voor geproduceerde artikelen kan een gesimuleerd productieorder gebruikt worden.

Via gesimuleerde productieorder krijgt men een inzicht in de berekende (theoretische) en de verwachte kosten (op basis van de actuele kostprijzen). In tegenstelling tot de vaste verrekenprijs, waarbij de kostprijs berekend wordt voor één basiseenheid, kan het aantal op een gesimuleerd productieorder vrij worden gekozen. Via de productieorderstatistiek krijgt men een inzicht in de verdeling van de kostprijs volgens volgende elementen:
- Materiaalkosten
- Capaciteitskosten
- Uitbestedingskosten
- Capaciteitsoverhead
- Productieoverhead

### 7.10 Assemblagebeheer
https://learn.microsoft.com/nl-be/dynamics365/business-central/assembly-assemble-items

Het domein "Assemblage" is gericht op 2 types processen:
- Het uitvoeren van "lichte" productie, waarbij er geen noodzaak is aan uitgebreide capaciteitsplanning.
- Het uitvoeren van "kitting", de verkoop van meerdere artikelen als kit, waarbij de artikelen vlak voor de
verzending uit het magazijn gehaald worden.

Binnen dit domein worden alle activiteiten vanaf het beheer van de master data, het aanmaken van assemblageorders, het registreren van verbruikte artikelen en uren tot de registratie van geassembleerde artikelen behandeld.

7.10.1BS40.002 Assemblage beheer instellen Assemblage werkt analoog aan productie door gebruik te maken van assemblagestuklijsten en assemblageorders, maar in vereenvoudigde vorm. Assemblage kan geïntegreerd worden met bestaande functies, zoals verkoop, planning, reserveringen en magazijnbeheer.

In de assemblage-instellingen worden zaken ingesteld zoals de te gebruiken nummerreeksen, de vestiging die gebruikt wordt voor assemblage, of verplaatsingen automatisch aangemaakt moeten worden en of er voorraadwaarschuwingen moeten gegeven worden.

7.10.2BS40.109 Assemblagestuklijsten beheren Voor elke regel wordt de soort ingesteld op artikel of resources, of blanco soort voor het toevoegen van tekstregels (informatief). Voor artikelen voert men het aantal in dat van de component nodig is om één eenheid van het geassembleerde artikel samen te stellen. Voor resources kan men kiezen of het aantal uit de assemblagestuklijst geldt voor het volledige assemblageorder (resourcegebruiktype “vast”) of vermenigvuldigd moet worden met het aantal van het assemblageorder (resourcegebruiktype “direct”).

#### 7.10.3 BS40.111 Assemblageorders beheren
Producten die bestaan uit meerdere componenten kunnen samengesteld worden zonder gebruik te maken van productiestuklijsten, bewerkingsplaatsen, productiecapaciteit, afdelingen, bewerkingsplaatsen, … m.a.w. zonder gebruik te maken van het productieorderproces.

Met assemblageorders kunnen artikelen (componenten) en resources (werkuren) verbruikt worden en samengestelde artikelen bekomen worden. Dergelijke orders worden meestal door de magazijnier uitgevoerd met een minimum aan administratie. Typische voorbeelden zijn het samenstellen van een set wisselstukken of eindmontageonderdelen (bv. bouten en moeren worden in een zakje gestoken en als set meegegeven met een eindproduct).

De artikelen en resources die nodig zijn om de samenstelling te bekomen, worden ingesteld in de assemblagestuklijst die aan het eindartikel gekoppeld is.

Er zijn 2 manieren om assemblage orders te benaderen:

  - Assemblage op order: op basis van wat klant besteld gaan we losse onderdelen uit magazijn samen
voegen tot één nieuwe (geassembleerd) artikel. Het geassembleerde artikel wordt zo laat mogelijk gemaakt.

  - Wanneer een artikel is ingesteld met Assemblagebeleid = Op order produceren wordt er
automatisch een assemblageorder aangemaakt voor iedere verkooporderregel door het invullen van het veld Aant. op order assembleren op de verkooporderregel.

  - Assemblage op voorraad: er zijn vooraf bepaalde samengestelde artikelen waarvan het bedrijf een
voorraad wil bijhouden.

  - Er wordt een assemblage order gemaakt vanuit het planningsvoorstel zodra de voorraad zakt
onder het bestelpunt. Er wordt 1 assemblage order gemaakt om voorraad terug aan te vullen tot het gewenste voorraadniveau.

https://learn.microsoft.com/nl-be/dynamics365/business-central/assembly-assemble-to-order-or-assemble-to- stock

7.10.4BS40.211 Assemblageorders registreren Het boeken van een assemblageorder resulteert in een voorraadtoename van het geassembleerde artikel en verbruik van de artikelen en resources die deel uitmaken van de assemblagestuklijst (of manueel werden toegevoegd aan het assemblageorder).

- Assemblageorders op voorraad

Wanneer een artikel wordt geassembleerd op voorraad dan wordt het artikel opgeslagen in de voorraad zonder dat er sprake is van een verkoopvraag. Het assemblage order moet manueel worden aangemaakt. Vanaf dit moment wordt het artikel gepickt, verwerkt en behandeld als een productieartikel.

- Assemblageorders op orders

Wanneer een artikel is ingesteld met assemblagebeleid = op order produceren wordt bij het invoeren van het artikel op een verkooporder in de achtergrond automatisch een assemblageorder gemaakt met in de kop de gegevens van de verkooporder-regel en waarbij de regels gebaseerd zijn op de assemblagestuklijst van het artikel. Wanneer de verzending geboekt wordt vanaf het verkooporder worden de componenten en resources verbruikt, het samengestelde artikel op voorraad geboekt en de verzending van het samengestelde artikel geboekt.
