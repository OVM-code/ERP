## 6. Planning (MPS/MRP)
Het domein "Planning" omvat de deelprocessen voor het maken van productieprognoses (forecast), het berekenen van inkoop-, productie-, assemblage- en transfervoorstellen en het aanmaken van orders (inkooporders, productieorders, assemblageorders en transferorders) vanaf de planningsvoorstellen.

https://learn.microsoft.com/nl-be/dynamics365/business-central/production-how-to-run-mps-and-mrp

Ook het inplannen van uitbesteed werk (subcontracting) wordt hierbij behandeld.

Master production schedule (MPS) is een planningssyteem, het geeft aan wat er geproduceerd moet worden, wanneer en in welke hoeveelheden. De focus ligt op de eindproducten die in BC geproduceerd worden. Material requirements planning (MRP) is een stockcontrole en planningssysteem. MRP integreert data van productieplannen met stock, stuklijsten en formules om aankoop voorstellen te berekenen voor alle grondstoffen die nodig zijn om de producten te maken & en eindproducten die ingekocht worden,.

Er zijn drie primaire functies:
- Ten eerste helpt het systeem om de juiste grondstoffen beschikbaar te hebben voor productie.
- Ten tweede helpt het systeem om verlies te verminderen door ervoor te zorgen dat de voorraadniveaus
voor grondstoffen en eindproducten zo laag mogelijk zijn.
- Daarbij helpt MRP nog bij het opmaken van productieplannen, leveringen - en aankoop plannen. Een
goed werkend MRP systeem zorgt voor een laag verlies van producten zonder tekorten te creëren. De juistheid van de data is hierin een grote uitdaging. De data in het systeem moet zeer accuraat zijn anders kunnen er grote problemen ontstaan voor productie en aankoop en tot tekorten in de voorraad leiden.

### 6.1 Prognoses beheren
#### 6.1.1 BS30.200 Productieprognoses beheren
Prognoses worden toegepast voor het maken van een inschatting van de artikelen die zullen worden verkocht of worden verbruikt. Per periode en per artikel kan er bepaald worden hoeveel de verwachte vraag naar het artikel binnen de periode. Op basis van prognoses kunnen planningsvoorstellen in productie worden bijgestuurd. Binnen het sub domein prognoses onderscheiden we het beheer van prognoses voor verkoopartikelen en prognoses voor componenten.

https://learn.microsoft.com/nl-be/dynamics365/business-central/production-how-to-create-a-forecast Prognoses worden ingevoerd in een matrix-scherm met de artikelen als regels en de periode als kolommen. De periode kan ingesteld worden op dag, week, maand, kwartaal, jaar of boekingsperiode. Er is hier geen specifiek onderscheid voor verkoopartikelen of componenten.

Deze prognoses kunnen ook gekopieerd worden op basis van eerdere prognoses, maar niet rechtstreeks op basis van de werkelijke verkoop. De werkelijke verkoop moet in formaat van prognose worden gezet in excel om te kunnen importeren.

### 6.2 Inkoopvoorstellen beheren
#### 6.2.1 BS30.201 Inkoop & planningsvoorstellen berekenen
BC zal vraag (alle uitgaande transacties) en aanbod (alle inkomende transacties) trachten te balanceren voor voorraadartikelen waar een planningsparameters voor is ingesteld te balanceren.

https://learn.microsoft.com/nl-be/dynamics365/business-central/production-about-planning-functionality

##### 6.2.1.1 BC30.201.01 Inkoopvoorstellen berekenen
Inkoopvoorstellen worden gebruikt voor de berekening van de planning van artikelen.

Bij de berekening van de planning via het inkoopvoorstel worden twee soorten suggesties gemaakt:

- Inkoop: voorstel tot inkoop van het artikel
 Ook special order en doorlevering inkooporders worden hier gepland
- Transfer: voorstel om een artikel van een vestiging te transfereren naar een andere vestiging

Voorstellen voor het assembleren of produceren van artikelen kunnen NIET via inkoopvoorstellen gegenereerd worden.

##### 6.2.1.2 BC30.201.02 Planningsvoorstellen berekenen
Ook planningsvoorstellen worden gebruikt voor de berekening van de planning van artikelen.

Bij de berekening van de planning via het planningsvoorstel worden 4 soorten suggesties gemaakt:

- Inkoop: voorstel tot inkoop van het artikel
 special order en doorlevering inkooporders worden hier NIET gepland
- Transfer: voorstel om een artikel van een vestiging te transfereren naar een andere vestiging

- Assemblage: voorstel tot assemblage van het artikel
- Productie: voorstel tot productie van het artikel

#### 6.2.2 BS30.202 Inkoop/planningsvoorstellen beoordelen en fiatteren
https://learn.microsoft.com/nl-be/dynamics365/business-central/production-about-planning-functionality

Inkoop/planningsvoorstellen geven een suggestie voor het inkopen en transfereren van artikelen. Nadat het voorstel is gemaakt, dienen de suggesties gevalideerd te worden. De gefiatteerde suggesties kunnen vervolgens omgezet worden naar een inkooporder of transferorder (afhankelijk van de suggestie).

De inkoopvoorstelregels worden gemaakt rekening houdend met de planningsparameters op de artikelkaart of de SKU indien aanwezig (indien er geen gebruik gemaakt wordt van SKU’s zijn er een aantal beperkingen van toepassing). Deze regels kunnen manueel aangepast worden door de gebruiker (ander aantal, andere leverancier, …). Per regel kan men via het veld “planningsboodschap accepteren” aangeven of de regel moet verwerkt worden. De gefiatteerde suggesties kunnen vervolgens omgezet worden naar een inkooporder, transferorder, productieorder of assemblageorder (afhankelijk van de suggestie).

Merk op: BC plant altijd achterwaarts: de verzochte leverdatum van de behoefte (verkooporder, productieorder, transferorder, …) is het vertrekpunt en BC berekent wanneer productie en/of inkoop zouden moeten gebeuren voor alle benodigde materialen of het finale product aan de klant te leveren. Als de berekende datum hierdoor in het verleden ligt, is dat een indicatie dat iets niet mogelijk is (waarschuwing, noodgeval of uitzondering). Maar het planningsvoorstel gaat geen verkoopdocumenten automatisch naar achter plannen hierdoor.

##### 6.2.2.1 BC30.202.01 Ordertracering
https://learn.microsoft.com/nl-be/dynamics365/business-central/design-details-reservation-order-tracking- and-action-messaging#order-tracking

Via de ordertraceringsfunctie in het inkoopvoorstel kan er geraadpleegd wat de oorsprong is voor een suggestie voor de inkoop, transfer of assemblage van een bepaald artikel. Zo kan men bijvoorbeeld raadplegen dat de suggestie voor het inkopen van een artikel afkomstig is van een verkooporder waarop dit artikel is opgenomen. Commented [NH66]: Is dit een scenario? Is een hulpmiddel in de planning en planningsvoorstel om te kijken waar vraag vandaan komt. Commented [NH67]: Online gevonden: https://www.olofsimren.com/copilot-inventory- queries/ Via copilot kan je vragen waarom deze suggestie wordt gemaakt.
