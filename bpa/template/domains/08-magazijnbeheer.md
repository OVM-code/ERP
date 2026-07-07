## 8. Magazijnbeheer
Het domein "Magazijnbeheer" omvat een uitgebreide set processen om inkomende en uitgaande magazijnbewegingen te beheren. In eerste instantie kunnen de magazijnbewegingen voorbereid worden. Dit zowel voor verzendingen, ontvangsten als transfers, verplaatsingen en tellingen. Daarna kunnen goederen ontvangen en weggezet worden, of gepickt en verzonden worden. Ook kan de aan- en afvoer i.v.m. productie verwerkt worden, en kunnen er interne magazijnprocessen uitgevoerd worden.

De bedoeling van logistiek binnen een bedrijf is om de juiste producten, in de juiste hoeveelheden, op het juiste moment, op de juiste plaats en tegen de juiste kosten beschikbaar te maken — met als doel maximale klanttevredenheid én optimale efficiëntie voor het bedrijf zelf. Logistiek kan niet los gezien worden van de verschillende processen zoals:
- Inkoop: Leveranciers beheren, materiaalbehoeftes inschatten, bestellingen opvolgen.
- Distributie: Orders verzamelen, verpakken en verzenden naar klanten.
- Productie: Grondstoffen tijdig aanleveren aan de productie, halffabricaten beheren.
- Interne logistiek: Verplaatsing en opslag van goederen binnen het bedrijf, beheren van
voorraadniveaus, tellen, optimaliseren.
- Retours: Afhandeling van retours, klachten of herstellingen.

De logistiek binnen BC werkt met verschillende brondocumenten die essentieel zijn om processen correct, traceerbaar en controleerbaar te laten verlopen. Deze documenten ondersteunen zowel de operationele uitvoering als de administratieve verwerking van logistieke activiteiten. Het werken met brondocumenten biedt onder andere volgende voordelen:
- Ze zorgen voor traceerbaarheid (bv. audit trails, ISO -normen).
- Ze maken fouten zichtbaar (bv. afwijkingen tussen bestelling en levering).
- Ze zijn cruciaal voor kwaliteitscontroles en klachtenafhandeling.
- Ze vormen de basis voor boekhoudkundige en ERP-verwerking.

Deze brondocumenten vormen dan ook de opdracht aan logistieke medewerkers om bepaalde taken uit te voeren.

### 8.1 Algemeen overzicht logistieke flows
In een productiebedrijf verlopen verschillende logistieke stromen die samen zorgen voor een efficiënte werking van het hele productieproces. De eerste stroom is de inkomende goederenstroom. Hierbij worden grondstoffen, onderdelen en hulpstoffen van leveranciers geleverd, gecontroleerd en opgeslagen in het magazijn. Deze materialen vormen de basis voor verdere verwerking. Vervolgens is er de interne goederenstroom, waarbij materialen intern worden verplaatst. Denk hierbij aan het picken van componenten uit het magazijn voor productie, het verplaatsen van halffabricaten tussen productiestations of het tijdelijk opslaan van gereed product. Deze stroom ondersteunt de dagelijkse productie en zorgt ervoor dat elk onderdeel op het juiste moment op de juiste plaats is. De kern van het productiebedrijf is de productiestroom, waar grondstoffen en onderdelen worden omgezet in halffabricaten of eindproducten. Dit omvat activiteiten zoals bewerken, assembleren, testen en eventueel verpakken. In sommige gevallen is er ook een project- of assemblageflow, waarbij specifieke materialen en

producten op projectbasis of klantorder worden verwerkt. Deze stroom vereist nauwkeurige planning en afstemming met de klantvraag. Na productie volgt de uitgaande goederenstroom. Hierin worden de eindproducten verzameld, verpakt en verzonden naar klanten. Dit proces omvat orderpicking, verzendklaar maken en transportcoördinatie. Tot slot is er de retourstroom, waarin defecte of ongewenste producten worden teruggestuurd. Deze worden vervolgens gecontroleerd en, afhankelijk van de toestand, opnieuw verwerkt, gerecycleerd of vernietigd. Hieronder een schematisch overzicht van deze flows.

### 8.2 Vestigingen beheren
#### 8.2.1 BS10.003 Vestigingen beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/warehouse-setup-warehouse

Dit scenario beschrijft het beheer van vestigingen. Een vestiging is een logistieke entiteit binnen een bedrijf, zoals een magazijn of een distributiecentrum. Binnen ieder bedrijf kunnen één of meerdere vestigingen ingesteld worden. Vestigingen kunnen toegepast worden bij elke logistieke transactie en worden ook in de historiek van de transacties bewaard.

Een bedrijf kan meerdere vestigingen hebben. Een algemene regel voor bepalen of extra vestiging nodig is: als er een fysiek transport (verzenden + ontvangen) nodig is voor verplaatsen van een plaats naar de andere, dan

zijn het aparte vestigingen. Als er verplaatsing via transpallet/heftruck/… mogelijk is, dan zijn het bij voorkeur geen aparte vestigingen.

- Beheer vestigingen

Deze scenario-variant beschrijft het beheer van vestigingen zonder opslaglocaties (bins).

1 vestiging = 1 locatie = 1 magazijn

Deze variant is de minimum vereiste om stockbeheer te kunnen toepassen.

Voor een eenvoudige magazijnindeling, waarbij geen voorraaddetails op het niveau van opslaglocaties noodzakelijk zijn, kan er gewerkt worden met een vestiging zonder opslaglocaties. Een voorbeeld zijn externe magazijnen , vb consignatie stock. Deze wordt bijgehouden aan de hand van een extra magazijn gekoppeld aan andere voorraadboekingsgroepen indien er integratie is met de boekhouding.

- Vestigingen met opslaglocaties beheren

Deze scenario-variant beschrijft het beheer van vestigingen met opslaglocaties (bins). Opslaglocaties (Bins) duiden het kleinst mogelijke onderdeel van een vestiging aan. Indien er geopteerd wordt voor het gebruik van opslaglocaties moet de opslaglocatie bij elke magazijntransactie mee gegeven worden.

- Vestigingen met gestuurde opslag en pick beheren

Deze scenario-variant beschrijft het beheer van vestigingen met opslaglocaties (bins). Opslaglocaties (Bins) duiden het kleinst mogelijke onderdeel van een vestiging aan. Indien er geopteerd wordt voor het gebruik van opslaglocaties moet de opslaglocatie bij elke magazijntransactie meegegeven worden. De keuze voor een vestiging met gestuurde opslag en pick zorgt ervoor dat de opslaglocatie automatisch wordt voorgesteld bij het wegzetten en picken van artikelen, op basis van criteria zoals vaste opslaglocaties en opslaglocatievolgorde (bin ranking). Voor het wegzetten van artikelen wordt gebruik gemaakt van opslagsjablonen waarin de prioriteit van de te gebruiken criteria worden beschreven. Vestigingen met gestuurde opslag en pick maakt het ook mogelijk om een voorstel te maken voor het aanvullen van opslaglocaties, bijvoorbeeld vanaf bulk-opslaglocaties. Verder wordt er ook gebruik gemaakt van zones en magazijnklasses (bijv. gekoeld magazijn).

Opmerking: recent zijn er heel wat functionaliteiten die in verleden enkel bij gestuurde opslag en pick beschikbaar waren, ook beschikbaar voor andere instellingen.

De functionaliteiten die voorlopig enkel beschikbaar zijn bij gestuurde opslag en pick:

- Opslaglocatiesoorten
- Magazijninventarisdagboek waarbij regels worden voorgesteld met bijhorende lotnummers
- Opslaan in opslag eenheid, bij niet gestuurde opslag en pick is pick altijd in basiseenheid
- Cross docken: opslag naar specifieke cross dock bin berekenen vanuit ontvangstdocument

Hieronder schematisch welke documenten gebruikt worden voor verkoop en welke posten gemaakt worden afhankelijk van de instellingen van de vestiging.

Zie Standaard documenten en flows BC.drawio voor selectie tekening voor gekozen scenario

### 8.3 Magazijn master data
#### 8.3.1 BS50.103 Zones/opslaglocaties/magazijnklasse/opslagsjabloon
beheren https://learn.microsoft.com/nl-be/dynamics365/business-central/warehouse-how-to-set-up-locations-to-use- bins

https://learn.microsoft.com/nl-be/dynamics365/business-central/design-details-warehouse-management

Een vestiging kan ingedeeld worden in meerdere zones, bijvoorbeeld de ontvangstzone, bulkzone, productiezone, pickzone en verzendzone. Het gebruik van zones is optioneel voor vestigingen zonder gestuurde opslag en -pick. Voor vestigingen met gestuurde opslag en pick is het gebruik van zones verplicht (er moet minstens één zone gedefinieerd worden).

Opslaglocaties (Bins) duiden het kleinst mogelijke onderdeel van een vestiging aan. Het gebruik van opslaglocaties is eveneens optioneel (instelbaar per vestiging). Het is mogelijk om de ene vestiging in te stellen voor gebruik met opslaglocaties en een andere vestiging zonder.

Een magazijnklasse kan als een extra kenmerk aan opslaglocaties toegekend worden en geldt als een conditie die als vereiste aan de opslaglocatie wordt gesteld, bijvoorbeeld diepvries of gekoeld. Artikelen met een bepaalde magazijnklasse kunnen alleen in opslaglocaties gestockeerd worden die dezelfde magazijnklasse hebben.

Opslagsjablonen bevatten een set regels die bepalen op welke wijze de opslaglocatie wordt geselecteerd waarop een artikel na ontvangst wordt weggezet. BC gaat dan bij het maken van de opslag verplaatsing, zich baseren op deze parameters om de beste locatie voor te stellen. De criteria die hiervoor kunnen gebruikt worden zijn:

- Vaste opslaglocatie zoeken
- Vrije opslaglocatie zoeken
- Zelfde artikel zoeken
- Overeenkomstige eenheid zoeken
- Opslaglocatie met minimumaantal zoeken
- Lege opslaglocatie zoeken
Bij het instellen van een opslagsjabloon kiest men zelf welke criteria en in welke volgorde ze moeten worden toegepast. Het voorstel van BC kan ook altijd overruled worden door de gebruikers, goederen kunnen opgeslagen worden op een andere plaats.

#### 8.3.2 BS50.116 Magazijnwerknemers instellen
Magazijnwerknemers zijn de personen die logistieke bewegingen verwerken in het magazijn, zoals het ontvangen, wegzetten, picken en verzenden van artikelen.

Elke gebruiker die magazijnactiviteiten uitvoert, moet als magazijnmedewerker worden ingesteld op één standaardlocatie en eventueel meer niet-standaardlocaties.

### 8.4 Artikelen ontvangen
De volgende brondocumenten initiëren een inkomende magazijnflow. Elk van deze documenten vormt de basis voor een inkomende goederenstroom, waarbij de logistieke afhandeling grotendeels op gelijkaardige wijze verloopt:

- Inkooporder
- Verkoopretourorder
- Transferorder (ontvangende zijde)

Afhankelijk van de complexiteit van opzet van de magazijnen worden er in BC aparte flows gevolgd, maar uiteindelijk gebeurt voor al deze brondocumenten hetzelfde: er is een opdrachtdocument, een logistieke handeling (in dit geval de eigenlijke ontvangst) en het resultaat is dat er voorraad wordt aangemaakt in het magazijn. De laatste stap in dit inkomende proces is eventueel het wegzetten van de voorraad in de rekken (het verplaatsen van de ontvangstzone naar de specifieke opslaglocaties).

#### 8.4.1 BS50.202 Maak magazijnontvangst
https://learn.microsoft.com/nl-be/dynamics365/business-central/walkthrough-receiving-and-putting-away-in- advanced-warehousing

De magazijnontvangst is een document dat toelaat goederen te ontvangen, net zoals men op een inkooporder kan. Door het werken met magazijnontvangsten als een apart document, kunnen 2 doelstellingen bereikt worden:

- Splitsen van logistiek en finance: magazijndocumenten bevatten immers geen prijzen. De magazijnier
geeft enkel aan wat hij ontvangen heeft, zonder zich te moeten concentreren op de prijs van deze artikelen

- Mogelijkheid tot splitsen en vooral samenvoegen van verschillende inkooporder(regels): in praktijk
worden artikelen van verschillende bestellingen soms samen geleverd. Via magazijnontvangsten kan men de splitsing of samenvoeging van orders uitvoeren.

Merk op: inkooporder kan ook vervangen worden door transferorder en verkoopretourorder: ook voor deze documenten kan de ontvangst van de goederen gebeuren via de magazijnontvangst.

##### 8.4.1.1 BC50.202.01 Inkooporders ontvangen op inkooporder
Indien er geen nood is aan het beheren van de magazijnprocessen voor de ontvangst en opslag van de artikelen, kan een ontvangst rechtstreeks vanaf de inkooporder uitgevoerd worden.

Bijvoorbeeld:

- Eén persoon is verantwoordelijk voor zowel de orderadministratie als voor de magazijnadministratie

- Indien de magazijnprocessen eenvoudig zijn en er geen nood is aan real-time registratie

##### 8.4.1.2 BC50.202.02 Ontvang goederen (tasklet)
Voor het ontvangen van goederen met de scanner blijft het uiteindelijke doel om inkomende goederen te registreren op basis van een document (magazijnontvangst, retour, transfer...). De ontvangsten die gedaan worden met de scanner worden rechtstreeks geregistreerd in Business Central. Er zijn een aantal varianten te onderscheiden bij het werken met de scanner, namelijk het ontvangen van goederen zonder ordertracering, ontvangsten van goederen met serienummertracering en goederen met lot tracering.

Let op: het artikelnummer dat in barcodevorm afgedrukt staat, moet gekend zijn in Business Central. Er zijn verschillende soorten van barcodes die hier kunnen gebruikt worden. Indien u deze functionaliteit wil gebruiken, moet u nagaan of de barcodes die door de leveranciers worden aangeleverd, wel degelijk leesbaar zijn voor uw scanner. Indien dat niet het geval is, kunt u zelf barcodes afdrukken, op de binnengekomen goederen kleven, zodat in de rest van de processen een "betrouwbare" barcode gebuikt wordt.

#### 8.4.2 BS50.217 Maak voorraadopslag
https://learn.microsoft.com/nl-be/dynamics365/business-central/warehouse-how-to-put-items-away-with- inventory-put-aways

De opslag is de (optionele) actie om goederen vanuit de ontvangstzone naar het magazijn te verplaatsen. Afhankelijk van de instelling van het magazijn kan deze actie nodig zijn of niet. Alternatief is dat de artikelen bij ontvangst onmiddellijk worden ontvangen per artikel op één in te stellen standaardlocatie.

- Maak voorraadopslag via push: Wanneer er geen behoefte is om het ontvangen van goederen en het
wegzetten in het magazijn als een afzonderlijke transactie te registreren kan er gebruik gemaakt worden van een voorraadopslag. Via deze methode wordt per inkooporder (of transferorder) een voorraadopslag aangemaakt. Hiervoor wordt het inkooporder (of transferorder) geopend en moet de status worden gewijzigd naar “vrijgegeven”. Via de actie “Voorraadopslag/-pick maken” wordt een voorraadopslag aangemaakt voor de inkooporder (of transferorder).
- Maak voorraadopslag aan in batch: Via de periodieke activiteit “Voorraadopslag/-pick/-verplaatsing
maken” kunnen er voorraad-documenten aangemaakt worden voor meerdere orders in één beweging. Om een voorraadopslag voor inkooporders aan te maken moet hiervoor het veld “Voorraadopslag

maken” ingeschakeld worden. De periodieke activiteit maakt hierbij één voorraadopslag per inkooporder (1 op 1).
- Maak voorraadopslag via pull: Het ontvangen van goederen kan door de magazijnier geïnitieerd worden
vanaf een voorraadopslag. Hierbij kan een inkomend document geselecteerd worden (zoals een inkooporder, transferorder of productieorder). Op basis van het geselecteerde inkomende document worden de regels op de voorraadopslag aangemaakt en kunnen de ontvangen aantallen geregistreerd worden. Op een voorraadopslag kan slechts 1 inkomend document verwerkt worden. Om gebruik te maken van voorraadopslag zijn op de vestiging volgende instellingen vereist:
- Ontvangst vereist = Nee
- Opslag vereist = Ja

#### 8.4.3 BS50.205 Cross docking artikelen ontvangen
https://learn.microsoft.com/en-us/dynamics365/business-central/warehouse-how-to-cross-dock-items

Cross-docking is het proces waarbij goederen niet (volledig) worden opgeslagen in het magazijn, maar rechtstreeks naar de verzendlocatie worden verplaatst om te worden verstuurd naar een of meerdere klanten. Cross-docking kan ook toegepast worden voor goederen die nodig zijn voor productieorders.

- Ontvang goederen voor onmiddellijke verzending (cross docking)
- Ontvang goederen voor productie (cross docking)
Cross-docking wordt berekend vanaf een magazijnontvangst. Hierbij wordt nagegaan welke goederen en welk aantal dat in aanmerking komt voor cross-docking voor verzending of productieorders. Materialen komen in aanmerking voor cross-docking als cross-docking is geactiveerd op de vestiging van de materiaal- of ontvangstregels.

#### 8.4.4 BS50.206 Artikelen opslaan (put away)
Na het ontvangen van goederen moeten deze weggezet worden in het magazijn. Dit proces is de opslag (put- away). Ook voor geproduceerde goederen die in het magazijn moeten worden weggezet, kan de opslag toegepast worden. Uit welke documenten er goederen moeten worden opgeslagen, kan manueel of aan de hand van een opslagvoorstel bepaald worden.

- Artikelen opslaan met magazijnopslag: Deze variant behandelt het tweede deel van het proces waarbij
goederen worden ontvangen en opgeslagen in het magazijn in twee stappen. Bij de registratie van de goederen aan de hand van een magazijnontvangst wordt een magazijnopslag aangemaakt. De magazijnopslag is een document met instructies voor de magazijnwerknemer om de ontvangen artikelen te nemen op de ontvangstopslaglocatie en te plaatsen op de daartoe bestemde opslaglocatie in het magazijn. Bij deze variant wordt voor elke magazijnontvangst een afzonderlijke magazijnopslag gemaakt.
- Artikelen opslaan met opslagvoorstel: Indien u het wegzetten van de ontvangen goederen in het
magazijn wenst te groeperen, kan gebruik gemaakt worden van het opslagvoorstel. In plaats van voor elke magazijnontvangst een afzonderlijke magazijnopslag te maken, kunnen met deze variant verschillende ontvangsten gecombineerd worden op één of meerdere magazijnontvangsten. Dit wordt

geïnitieerd van uit het opslagvoorstel, waarbij magazijndocumenten kunnen worden opgehaald en van waaruit een of meerdere magazijnopslag-documenten kunnen worden gemaakt.

##### 8.4.4.1 BC50.206.01 Opslag (tasklet)
Nadat de goederen ontvangen zijn op de loskade en er een controle is gebeurd of de juiste artikelen zijn geleverd in de juiste hoeveelheden, kunnen de goederen weggezet worden in het magazijn.

Afhankelijk van de setup van het magazijn, zal op de scanner een reknummer worden voorgesteld waar de goederen bij voorkeur worden weg gezet.

### 8.5 Artikelen verplaatsen
#### 8.5.1 BS50.207 Artikelen verplaatsen
https://learn.microsoft.com/nl-be/dynamics365/business-central/warehouse-move-items

Dit scenario omvat het verplaatsen van artikelen binnen eenzelfde vestiging (magazijn) of tussen verschillende vestigingen. De nood aan het verplaatsen van artikelen kan op verschillende manier ontstaan:
- Fysieke verplaatsing, bijvoorbeeld wanneer de artikelen moeten verplaatst worden om plaats te maken
voor andere artikelen, of wanneer de artikelen op een andere locatie nodig zijn. Administratieve verplaatsing, bijvoorbeeld wanneer de fysieke voorraad zich op een andere locatie bevindt dan de locatie die door Business Central wordt getoond.

- Artikelen verplaatsen via voorraadverplaatsing: Voor het verplaatsen van artikelen in een vestiging
(magazijn) zonder gestuurde opslag en pick kan een voorraadverplaatsing gebruikt worden. Een voorraadverplaatsing vormt een instructie voor een magazijnmedewerker om artikelen te nemen op een opslaglocatie en ze te plaatsen op een andere opslaglocatie. Een voorraadverplaatsing kan worden aangemaakt vanaf het venster interne verplaatsingen.
- Artikelen verplaatsen via herindelingsdagboek:
https://learn.microsoft.com/nl-be/dynamics365/business-central/warehouse-how-to-move-items-ad- Field Code Changed hoc-in-basic-warehousing Via een herindelingsdagboek kunnen artikelen verplaatst worden tussen verschillende vestigingen (magazijnen) of tussen verschillende opslaglocaties binnen eenzelfde vestiging. Een verplaatsing van artikelen via het herindelingsdagboek verloopt via een journaal (er zijn dus geen bijkomende documenten zoals een magazijnverplaatsing vereist). Herindelingsdagboeken kunnen enkel toegepast worden voor vestigingen zonder gestuurde opslag en pick.
- Artikelen verplaatsen via magazijnverplaatsing:
https://learn.microsoft.com/nl-be/dynamics365/business-central/warehouse-how-to-move-items-in- advanced-warehousing Voor het verplaatsen van artikelen in een vestiging (magazijn) met gestuurde opslag en pick wordt een magazijnverplaatsing gebruikt. Een magazijnverplaatsing vormt een instructie voor een magazijnmedewerker om artikelen te nemen op een opslaglocatie en ze te plaatsen op een andere opslaglocatie. Magazijnverplaatsingen kunnen worden aangemaakt vanaf een verplaatsingsvoorstel.

##### 8.5.1.1 BC50.207.01 Verplaats goederen met scanner (tasklet)
Binnen het magazijn worden goederen regelmatig verplaatst.

In dit scenario wordt de verplaatsing gedaan met behulp van de Tasklet scanner.

- Geplande verplaatsing met scanner: Indien goederen in het magazijn verplaatst moeten worden, kan
dat gebeuren via een geplande verplaatsing. D.w.z. dat er iemand is die de opdracht geeft om de verplaatsing te doen en dat er een specifiek magazijndocument is, dat op de scanner kan uitgekozen worden. Een voorbeeld van een geplande verplaatsingen is het aanvullingsproces waarbij artikelen uit het magazijn naar de pick zone worden verplaatst.

- Ongeplande verplaatsing met scanner: Indien goederen in het magazijn verplaatst moeten worden, kan
dat gebeuren via een ongeplande verplaatsing. In dat geval is er geen specifieke opdracht om de verplaatsing te doen en is er geen specifiek magazijndocument, dat op de scanner kan uitgekozen worden. Een voorbeeld van een ongeplande verplaatsingen is het verplaatsen van een pallet met defecte artikelen naar een quarantaine zone.

- Verplaatsing in bulk met scanner: Indien alle artikelen die op een bin staan verplaatst moeten worden,
kan dat in bulk gebeuren, door de inhoud van een bin op te vragen en deze in zijn geheel te verplaatsen naar een andere bin.

#### 8.5.2 BS50.208 Transferorders maken
https://learn.microsoft.com/nl-be/dynamics365/business-central/inventory-how-transfer-between-locations

Deze variant beschrijft het verplaatsten van goederen tussen verschillende vestigingen (magazijnen) aan de hand van transferorders. Op een transferorder worden steeds de vestigingen vermeld van waar de goederen worden verzonden (uit) en deze waar de goederen worden ontvangen (in). Een transferorder kan niet worden toegepast voor verplaatsingen binnen eenzelfde vestiging.

#### 8.5.3 BS50.209 Productieordermaterialen terugzetten
Voor de uitvoering van productie worden goederen naar de productie-opslaglocatie verplaatst. Nadat het verbruik van de artikelen geregistreerd werd, moet in sommige situaties de resterende aantallen teruggebracht worden naar het magazijn.

- Productieordermaterialen terugzetten via magazijnverplaatsing: Voor het verplaatsen van artikelen in
een vestiging (magazijn) met gestuurde opslag en pick wordt een magazijnverplaatsing gebruikt. Een magazijnverplaatsing vormt een instructie voor een magazijnmedewerker om artikelen te nemen op een opslaglocatie en ze te plaatsen op een andere opslaglocatie. Magazijnverplaatsingen kunnen worden aangemaakt vanaf een verplaatsingsvoorstel.

- Productieordermaterialen terugzetten via voorraadverplaatsing: Voor het verplaatsen van artikelen in
een vestiging (magazijn) zonder gestuurde opslag en pick kan een voorraadverplaatsing gebruikt worden. Een voorraadverplaatsing vormt een instructie voor een magazijnmedewerker om artikelen te nemen op een opslaglocatie en ze te plaatsen op een andere opslaglocatie. Een voorraadverplaatsing kunnen worden aangemaakt vanaf een het venster interne verplaatsingen.

### 8.6 Artikelen verzenden
De volgende brondocumenten initiëren een uitgaande magazijnflow. Elk van deze documenten vormt de basis voor een uitgaande goederenstroom, waarbij de logistieke afhandeling grotendeels op gelijkaardige wijze verloopt:
- Verkooporder
- Inkoopretourorder
- Transferorder (verzend zijde)
- Serviceorder

Afhankelijk van de complexiteit van opzet van de magazijnen worden er in BC aparte flows gevolgd, maar uiteindelijk gebeurt voor al deze brondocumenten hetzelfde: er is een opdrachtdocument, één of meerdere logistieke handelingen (in dit geval bv. het picken, de verzending, het afdrukken van documenten) en het resultaat is dat er voorraad wordt afgeboekt van het magazijn.

#### 8.6.1 BS50.213 Artikelen picken
https://learn.microsoft.com/nl-be/dynamics365/business-central/warehouse-pick-items

Een magazijnpick vormt de instructie voor een magazijnwerknemer om goederen te nemen op een bepaalde locatie in het magazijn, en deze te plaatsen op een verzendopslaglocatie of productieopslaglocaties. Magazijnpicks kunnen worden toegepast voor het picken voor verkooporders, transferorders, productieorders en serviceorders. Magazijnpicks worden gebruikt in een vestiging waar verzending vereist en pick vereist zijn ingeschakeld en kunnen zowel in vestigingen met als zonder gestuurde opslag en pick worden gebruikt.

- Maak magazijnpick aan vanaf magazijnverzending: Een magazijnpick kan worden aangemaakt vanaf een
magazijnverzending. In dat geval wordt er één magazijnpick aangemaakt voor de volledige verzending. Wanneer de vestiging (magazijn) is ingesteld als een vestiging met gestuurde opslag en pick is het mogelijk om op de vestigingkaart in te stellen dat er altijd pickregels moeten worden aangemaakt, ook wanneer artikelen niet op voorraad zijn. In het andere geval (vestiging zonder gestuurde opslag en pick) wordt enkel pickregels aangemaakt voor de artikelen op voorraad.
- Maak magazijnpick aan via pickvoorstel:
https://learn.microsoft.com/nl-be/dynamics365/business-central/warehouse-how-to-plan-picks-in- Field Code Changed worksheets Via het pickvoorstel is het mogelijk om magazijnpicks te maken voor meerdere magazijnverzendingen. Op deze manier kunnen picks voor meerdere orders gecombineerd worden tot één instructie voor de magazijnmedewerker. Via het pickvoorstel heeft u de volledige controle over welke regels op welke magazijnpick worden toegevoegd.

##### 8.6.1.1 BC50.213.02 Maak pick voor productieorder aan
Een pick vormt de instructie voor een magazijnwerknemer om goederen te nemen op een bepaalde locatie in het magazijn, en deze te plaatsen op een verzendopslaglocatie of productieopslaglocatie. Picks kunnen worden toegepast voor het picken voor verkooporders, transferorders en productieorders. Dit scenario behandelt het picken voor productieorders.

- Maak voorraadpick voor productieorder aan (standaardmagazijnconfiguratie): In een vestiging
(magazijn) met een eenvoudige magazijnconfiguratie (ontvangst vereist = nee, opslag vereist = ja), wordt gebruikt gemaakt van een voorraadpick om de artikelen te nemen op de magazijnlocatie. Een voorraadpick voor productie wordt aangemaakt vanaf een vrijgegeven productieorder. Bij de registratie van de voorraadpick worden de gepickte artikelen verbruikt op de productieorder.
- Maak magazijnpick voor productieorder aan (geavanceerde magazijnconfiguratie): In een vestiging
(magazijn) met geavanceerde magazijnconfiguratie (ontvangst vereist = ja, opslag vereist = ja), wordt gebruikt gemaakt van een magazijnpick om de artikelen te nemen op de magazijnlocatie en te plaatsen in de productie-opslaglocatie. Een magazijnpick voor productie wordt aangemaakt vanaf een vrijgegeven productieorder.

##### 8.6.1.2 BC50.213.03 Maak voorraadpick aan
https://learn.microsoft.com/nl-be/dynamics365/business-central/warehouse-how-to-pick-items-with- inventory-picks

Een voorraadpick vormt de instructie voor een magazijnwerknemer om de goederen te nemen op de magazijnlocatie en in de verzendzone te plaatsten. Anders dan bij een magazijnpick, waarbij zowel de opslaglocatie waar de artikelen moeten genomen als deze waar de artikelen moeten geplaatst worden vermeld wordt, is er bij een voorraadpick enkel vermelding van de opslaglocatie waar de artikelen moeten genomen worden.

Voorraadpicks kunnen worden toegepast in vestigingen waar pick vereist is ingeschakeld en verzending vereist is uitgeschakeld.

- Maak voorraadpick aan vanaf verkooporder: Deze variant behandelt het aanmaken van een
voorraadpick vanaf een verkooporder. Het verkooporder moet de status vrijgegeven hebben vooraleer een voorraadpick kan aangemaakt worden. Er worden enkel pickregels aangemaakt voor artikelen waarvoor voldoende voorraad beschikbaar is.
- Maak voorraadpick aan vanaf transferorder: Deze variant behandelt het aanmaken van een
voorraadpick vanaf een transfer. Het transferorder moet de status vrijgegeven hebben vooraleer een voorraadpick kan aangemaakt worden. Er worden enkel pickregels aangemaakt voor artikelen waarvoor voldoende voorraad beschikbaar is.
- Maak voorraadpick aan in batch: Via de batch-routine voorraadopslag/-pick maken kunnen meerdere
voorraadpicks in één beweging worden aangemaakt. Hierbij wordt nog steeds één voorraadpick per verkooporder, transferorder of productieorder aangemaakt (net zoals bij het manueel aanmaken van voorraadpicks).

##### 8.6.1.3 BC50.213.04 Pick goederen met scanner (tasklet)
Om ervoor te zorgen dat de juiste artikelen worden gepickt in de juiste aantallen, worden op de scanner de te picken orders en orderlijnen getoond.

De magazijnier scant de barcode van het artikel en geeft het aantal in. Indien een verkeerd artikel wordt genomen, verschijnt een foutboodschap op de scanner.

Afhankelijk van de instellingen van het magazijn, worden de meest logische reknummers getoond waar dit artikel kan gepickt worden. Zo kunnen bv. de picklocaties een hogere ranking hebben dan de bulklocaties, waardoor de picklocaties eerst worden voorgesteld, tot de beschikbare voorraad daar op is.

##### 8.6.1.4 BC50.213.05 Tote picking met scanner:
Indien tijdens het pick proces artikelen al in een doos gestopt worden (bv. een doos per klant, indien men voor meerdere klanten aan het picken is), kan de magazijnier op de scanner aangeven in welke doos het artikel gepickt werd.

Zo kunnen, tijdens één route door het magazijn, meerdere orders door elkaar gepickt worden. Tijdens deze pickopdracht worden de verschillende orders gesorteerd in verschillende dragers (doos, bak, ...) (= totes), die op een kar of een handpallettruck staan. Elke drager beschikt over een unieke barcode die tijdens het pickproces kan worden gescand. De barcode kan een doorlopende reeks voorgedrukte barcodes zijn die op een doos worden gekleefd of het kan een barcode zijn die op een plastiek bak bevestigd is die later opnieuw kan gebruikt worden.

#### 8.6.2 BS50.214 Magazijnverzending maken
https://learn.microsoft.com/nl-be/dynamics365/business-central/warehouse-how-ship-items

De magazijnverzending wordt gebruikt voor de logistieke verzending van de activiteiten die nodig zijn voor het orderbeheer. Afhankelijk van de instellingen van het magazijn moeten goederen Dit scenario behandelt de verschillende methodes om magazijnverzendingen voor verkooporders of transferorders aan te maken.

  - Magazijnverzending maken vanaf verkooporder (push): De magazijnverzending wordt gebruikt voor de
logistieke afhandeling van de activiteiten die nodig zijn voor het orderbeheer. Bij het verzenden van goederen naar een andere vestiging via push wordt een magazijnverzending aangemaakt vanaf een vrijgegeven order. Hierbij worden alle artikelen van het order vermeld op de magazijnverzending. Magazijnverzendingen die op deze manier worden aangemaakt bevatten slechts de artikelen van één transferorder. Afhankelijk van het verzendadvies waarvoor werd gekozen (geheel of gedeeltelijk) moet de verzending in één keer uitgevoerd worden, of kan deze in deelleveringen gebeuren.

  - Magazijnverzending via ophalen brondocumenten (pull): Het verzenden van goederen kan door de
magazijnier geïnitieerd worden vanaf een magazijnverzending. Hierbij kan een selectie gemaakt worden op basis van een lijst met uitgaande documenten (zoals verkooporders of transferorders). Op basis van de geselecteerde uitgaande documenten (1 of meerdere documenten) worden de regels op de magazijnverzending aangemaakt. Nadat de picking is uitgevoerd kan de verzending geregistreerd worden.

  - Magazijnverzending via ophalen brondocumenten met filters (pull): Bij deze variant wordt het
aanmaken van de magazijnverzending eveneens geïnitieerd door de magazijnmedewerker door het aanmaken van een magazijnverzending. Hierbij wordt gebruik gemaakt worden van filters om aan de hand van criteria de gewenste documenten op te halen. De filters kunnen als een vooraf gedefinieerde set criteria worden ingesteld, of kunnen aangepast worden op basis van de actuele behoeften bij het maken van de selectie van te verzenden documenten (bijvoorbeeld alle orders van een bepaalde klant, de documentsoort of de expediteur).

Nadat de picking is uitgevoerd, kan de verzending geregistreerd worden.

##### 8.6.2.1 BC50.214.01 Shop floor logistics (Aptean)
https://fnbdocs.apteancloud.com/bc/SFL/contents/ Field Code Changed

Met de Shop Floor Logistics-extensie krijg je een overzichtspagina van alle inkomende en uitgaande logistieke activiteiten, waardoor het gemakkelijker wordt om de planning in het magazijn te ondersteunen. Op de Shop Floor Activities-pagina wordt een logistieke datum/tijd weergegeven om alle inkomende en uitgaande logistieke activiteiten chronologisch te tonen. Er wordt een logistieke status weergegeven per documenttype, die de logistieke voortgang aangeeft. Er zijn drie statussen die aangeven of de logistieke activiteit is gemaakt, of deze in uitvoering is en of deze gereed is om te posten. Dit maakt het gemakkelijker om shop floor-activiteiten te prioriteren op basis van een combinatie van tijd en huidige status. Bovendien is het mogelijk om voorraad te ontvangen en/of voorraad uitgifte documenten te maken, te openen en te posten. De Shop Floor Activities- pagina dient als handig startpunt voor alle magazijnactiviteiten. Met de Shop Floor Logistics-extensie krijg je ook een overzichtspagina met informatie over welke en hoeveel artikelen per locatie op voorraad zijn. Het biedt inzicht in de voorraad van het hele bedrijf over alle locaties heen, ongeacht eventuele filters. Dit kan helpen bij het beslissen welke artikelen moeten worden bijbesteld, geproduceerd of overgebracht, om problemen met niet-op-voorraad te voorkomen. De pagina's Gedetailleerd Voorraadoverzicht en Voorraaddetails kunnen worden gebruikt voor verschillende doeleinden, zoals het

handhaven van een balans tussen te veel en te weinig voorraad en het bijhouden van de totale voorraad over locaties heen. Het geeft ook inzicht in de voorraad van een specifiek artikel op locatie-, bin- en lotniveau.

##### 8.6.2.2 BC50.214.02 Beheren ritten (Cegeka)
Een rit maakt het mogelijk om lijnen te verzamelen die niet geboekt of slechts gedeeltelijk geboekt zijn vanuit een verkooporder, inkooporder, verkoopretourorder en transferorder.

Deze kunnen dan verzameld worden in een 'rit'. De nieuwe rit zal manueel aangemaakt worden gebaseerd op een combinatie van route en datum wanneer deze zal plaatsvinden.

Op deze rit komen dan de verkoop en/of inkooporderlijnen terecht, die met deze rit moeten getransporteerd worden.

##### 8.6.2.3 BS50.214.03 Transport (Aptean)
Met de Transport-extensie kun je de inkomende en uitgaande transporten beheren. Transportverzoeken kunnen gepland worden in het transportplanningsproces en transportorders kunnen gecreëerd worden en doorgestuurd worden naar je verzendingsagent. Met deze extensie kun je transportverzoeken creëren bij het vrijgeven van de volgende documenten:
- Inkooporder
- Verkooporder
- Inkoopretourorder
- Verkoopretourorder
- Transferorder
Bij het vrijgeven van een order wordt automatisch een transportverzoek gecreëerd voor elke locatie/verzenddatum combinatie. De pagina transportplanning biedt een overzicht van alle transportverzoeken, waardoor het eenvoudiger wordt om meerdere verzoeken te combineren in één transportorder. Aangezien de bron documenten van een transportverzoek in de loop van de tijd kunnen veranderen, kan het inplannen van het transport een uitdagende taak zijn. Met handige functies en inzichten helpt de transportplanning pagina je bij het volgen van wijzigingen en het schatten van de vloeroppervlakte voor een transportorder. De transportroutes bieden de mogelijkheid om routes te creëren voor specifieke periodes en verder naar een specifieke klant via de pagina transportroute toewijzing. Verder geeft de extensie inzicht in de transportkosten door het creëren van inkooporders voor de verzendingsagent.

#### 8.6.3 BS50.215 Artikelen verzenden
Dit scenario behandelt de verschillende methodes waarop goederen kunnen verzonden worden in het magazijn.

  - Magazijnverzending boeken: Het boeken van de magazijnverzending is de laatste stap in het logistieke
proces. Hiermee verlaten de goederen definitief het magazijn. Bij de registratie van de magazijnverzending wordt ook de verzendnota afgedrukt.

  - Transferorder verzenden: Indien er geen nood is aan het beheren van de magazijnprocessen voor het
picken en verzendklaar maken van de artikelen, kan een verzending heel eenvoudig rechtstreeks vanaf het transferorder uitgevoerd worden. Bijvoorbeeld:
- Eén persoon is verantwoordelijk voor zowel de orderadministratie als voor de magazijnadministratie.
- Indien de magazijnprocessen eenvoudig zijn en er geen nood is aan real-time registratie.
- Indien de registratie gebeurt voor een extern magazijn, bijvoorbeeld van een onderaannemer.

  - Transferorder verzenden (directe transfer): Met een “directe transfer” transferorder worden
verzending van de uitgaande vestiging en ontvangst in de inkomende vestiging in één beweging geboekt. Een directe vestiging is enkel mogelijk tussen vestigingen waar verzending en pick zijn uitgeschakeld voor de uitgaande vestiging en ontvangst en opslag zijn uitgeschakeld voor de inkomende vestiging.

  - Verkooporder verzenden op verkooporder: Indien er geen nood is aan het beheren van de
magazijnprocessen voor het picken en verzendklaar maken van de artikelen, kan een verzending heel eenvoudig rechtstreeks vanaf het verkooporder uitgevoerd worden. Bijvoorbeeld:

- Eén persoon is verantwoordelijk voor zowel de orderadministratie als voor de magazijnadministratie

- Indien de magazijnprocessen eenvoudig zijn en er geen nood is aan real-time registratie

##### 8.6.3.1 BC50.215.01 Verzend goederen met scanner (tasklet)
In dit business scenario worden artikelen verzonden met behulp van een mobiele scanner.

De artikelen kunnen gescand worden bij de verzending, zodat er een laatste controle is vooraleer de artikelen de firma verlaten. Hier wordt gecontroleerd of de juiste artikelen in de juiste hoeveelheid aan de juiste klanten worden geleverd.

##### 8.6.3.2 BC50.215.02 Tote shipping (tasklet)
Na picking moeten de artikelen nog een keer gescand worden voor de verzending. Indien er een “tote picking” is gebeurd moet alleen de doos gescand te worden, en niet meer de individuele artikelen, om alles wat in de doos zit te verzenden. Er gebeurt wel een controle of deze doos wel bestemd is voor de uitgekozen verzending.

### 8.7 Herbevoorraden opslaglocaties
#### 8.7.1 BS50.216 Herbevoorraden opslaglocaties
https://learn.microsoft.com/nl-be/dynamics365/business-central/warehouse-how-to-plan-warehouse- movements-in-worksheets

Dit scenario behandelt het herbevoorraden van pick-opslaglocaties vanaf bulk-opslaglocaties. Er kan gebruik gemaakt worden van bulk-opslaglocaties indien de vestiging (magazijn) zo is ingedeeld dat in de bulk-zone doorgaans volledige logistieke eenheden (bijvoorbeeld paletten) worden gestockeerd, terwijl in de pickzone kleinere hoeveelheden worden gestockeerd, voldoende om aan de vraag van verkooporders, transferorders of productieorders te voldoen. Wanneer de beschikbare voorraad in de pickzone onder een gewenst niveau daalt, kan de voorraad aangevuld worden aan de hand van een herbevoorrading.

### 8.8 Document Lay-outs Magazijn
#### 8.8.1 BS50.800 Verkoopverzending
Cegeka Lay-out:

#### 8.8.2 BS50.801 Magazijnverzending/CMR

### 8.9 Tasklet Factory Mobile WMS
Tasklet is een oplossing, waarmee zo goed als alle magazijntransacties hierboven beschreven, kunnen worden uitgevoerd via een mobiele scanner, waardoor deze handeling efficiënter wordt met en lagere kans op fouten. Daarnaast zijn er bepaalde gevallen waar features enkel beschikbaar zijn via tasklet (tote picking).

https://taskletfactory.com/solutions/mobile-wms-365-bc-nav/

#### 8.9.1 BS50.240 Instellen Tasklet Factory
Om met de scanner te kunnen werken, moeten meerdere instellingen gebeuren,

Of je het aantal van een artikel zelf ingeeft, of dat per scan automatisch 1 eenheid van het artikel geregistreerd wordt.

Verder kan bv. aangegeven worden welk soort "tote picking" mogelijk is.
- Of je artikelen voor meerdere klanten in dezelfde doos mag picken of niet.
- Of je artikelen van meerdere orders in dezelfde doos mag picken of niet.

#### 8.9.2 Magazijn activiteiten

#### 8.9.3 BS50.242 Pakkettracering tijdens WMS activiteiten

##### 8.9.3.1 BC50.242.01 Pakkettracering tijdens WMS activiteiten (tasklet)
https://taskletfactory.atlassian.net/wiki/spaces/TFSK/pages/531726337/License+Plating

Tasklet heeft een aantal features toegevoegd in tasklet, om ontvangen op een pakket, opslag van het pakket & picken van een pakket mogelijk te maken.

##### 8.9.3.2 BC50.242.02 Pakkettracering tijdens WMS activiteiten (Cegeka)
De pakketracering die standaard Business Central voorziet, maakt het mogelijk om goederen te traceren op een pakket/SSCC. Maar standaard zitten daar geen verdere functionaliteiten achter.

Met deze extensie, geven we de mogelijkheid om de info op een pakket te gebruiken en andere logistieke handelingen (picken, verplaatsen of verzenden) te vereenvoudigen, ook in de tasklet oplossing. Het idee is dat we via de inhoud van een pallet (artikel, aantal, lotnummer, bin waarop deze pallet staat) ophalen uit de info van BC, in plaats van al deze info manueel te laten bevestigen door de gebruiker via de scanner.

Onderstaande afbeeldingen geven dit visueel weer:

Er staan 9 dozen van verschillende artikelen en loten op 1 locatie in en magazijn. Als we deze willen verplaatsen van locatie A-01-01 naar A-01-02, hebben we 9 individuele registraties nodig, waarbij iedere keer artikel + lot + aantal + take bin + place bin ingevoerd moet worden zonder de SSCC add-on (9*5).

Bin A-01-01 Bin A-01-02

Item 1 Item 2 Item 3 Item 1 Item 2 Item 3 Lot A LOT X Lot R Lot A LOT X Lot R 40 PCS 80 PCS 20 PCS 40 PCS 80 PCS 20 PCS

Item 1 Item 1 Item6 Item 1 Item 1 Item6 LOT B Lot C LOT H LOT B Lot C LOT H Bin A-01-02 40 PCS 20 PCS 15 PCS 40 PCS 20 PCS 15 PCS

Item 1 Item 2 Item 6 Item 1 Item 2 Item 6 LOT C LOT Y LOT K LOT C LOT Y LOT K 20PCS 20 PCS 8 PCS 20PCS 20 PCS 8 PCS

Met de SSCC add-on, waarbij de 9 dozen verdeeld staan over 3 paletten met een uniek SSCC nummer, zijn er maar 3 registraties nodig, waarbij enkel de SSCC nummer + place bin ingevoerd moet worden (3*2)

Bin A-01-01 Bin A-01-02

Item 1 Item 2 Item 3 Item 1 Item 2 Item 3 Lot A LOT X Lot R Lot A LOT X Lot R 40 PCS 80 PCS 20 PCS 40 PCS 80 PCS 20 PCS

Item 1 Item 1 Item6 Item 1 Item 1 Item6 LOT B Lot C LOT H LOT B Lot C LOT H Bin A-01-02 40 PCS 20 PCS 15 PCS 40 PCS 20 PCS 15 PCS

Item 1 Item 2 Item 6 Item 1 Item 2 Item 6 LOT C LOT Y LOT K LOT C LOT Y LOT K 20PCS 20 PCS 8 PCS 20PCS 20 PCS 8 PCS

SSCC 1 SSCC 2 SSCC 3

Verschillen ten opzichte van de tasklet feature:

- We gebruiken de tracering van BC & we hebben specifieke pakkettracering nodig

- Geïntegreerd met standaard werking binnen BC. Oplossing tasklet werkt alleen op transacties via de
scanner

- Via deze werkwijze ben je verplicht op ieder moment pakket in te voeren (indien de
artikeltraceringscode dit vereist), maar zo weet je ook altijd wat er op welk pakket staat. In de tasklet oplossing heb je meer vrijheid, een artikel kan soms wel of niet op een pakket staan.

- Cegeka oplossing is al beschikbaar in alle processen, tasklet voorlopig alleen bij ontvangen en picken
(preview).

### 8.10 BS50.900 Advanced warehousing (Aptean)
Ook Aptean heeft een mobiele scan applicatie voor beheer van magazijn processen. Deze ondersteund echter (nog) geen gestuurde opslag en pick scenario’s.

https://fnbdocs.apteancloud.com/bc/AWH/introduction/

#### 8.10.1 BC 50.242.03 License plating (Aptean)
Ook Aptean heeft een oplossing die pakkettracering tijdens WMS activiteiten ondersteund. Het hoofddoel van de Aptean License Plating-extensie is om alle logistieke transacties in de toeleveringsketen te kunnen traceren naar een specifiek license plate nummer. License plating verwijst naar het toewijzen en volgen van voorraadartikelen die samen worden opgeslagen om de beweging binnen, buiten en door een magazijnlocatie te vergemakkelijken. Hierbij wordt gebruik gemaakt van een license plate die bijvoorbeeld een pallet of een rolcontainer kan zijn waarin gestapelde handelseenheden zijn opgeslagen, zoals dozen of kratten. Door license plating te combineren met een locatie- en bin system, is het mogelijk om in realtime te zien waar een license plate zich in het magazijn bevindt. Het tracken van voorraadartikelen via license plating in de toeleveringsketen zorgt voor een betere groepering en beheer van de voorraad. Het toewijzen van een uniek nummer aan elke inhoudseenheid maakt het mogelijk om transacties in te voeren zonder dat er veel scans nodig zijn. Hiervoor wordt een license plate kaart gemaakt waarop alle artikelen die aan de license plate zijn toegewezen als inhoud, worden vermeld. Hierbij worden ook unieke details per artikel, zoals lotnummer, locatiecode en bin code, geregistreerd. De Aptean License Plating-extensie is geïntegreerd met de Aptean Food and Beverage Packaging and Returnable Packaging-extensie, waardoor het mogelijk is om een verzendcontainercode aan het license plate nummer toe te wijzen. Dit maakt het tracken van voorraadartikelen nog eenvoudiger en efficiënter. Met name in omgevingen waarbij gebruik wordt gemaakt van mobiele gegevensverwerking via handscanners met barcode-scannerfunctionaliteit, is license plating een effectieve manier om de voorraad te beheren en te tracken.

#### 8.10.2 BS50.902 Mobile warehouse registration (Aptean)
/

#### 8.10.3 BS50.903 Over and under delivery (Aptean)
In standaard business central is het niet mogelijk om meer of minder te ontvangen/verzenden dan de hoeveelheid op een order. Deze extensie maakt het mogelijk om meer of minder te ontvangen/verzenden dan de originele hoeveelheid op het order. Dit is mogelijk op volgende documenten:
- Inkooporder
- Magazijnontvangst
- Voorraad wegzetting
- Verkooporder

- Magazijnverzending
- Voorraad pick
- Magazijn pick
#### 8.10.4 BS50.905 Weighbridge Receiving (Aptean)
https://fnbdocs.apteancloud.com/bc/WBR/introduction/

De Aptean Weighbridge Receiving-extensie legt het nauwkeurige gewicht van de ontvangen items vast en maakt het systeem betrouwbaarder. Hiermee worden problemen zoals weegfraude en onnauwkeurigheid opgelost, die op hun beurt de klantrelatie kunnen beïnvloeden. Omdat de apparatuur die bij dit weegproces betrokken is wettelijk moet zijn en onder toezicht van de wet moet staan, zijn weegbruggensystemen van het grootste belang. Deze extensie berekent het gewicht van de ontvangen items intern door de gewichten van de geladen en geloste vrachtwagens te registreren. Hierdoor wordt het weegproces efficiënter en nauwkeuriger doordat fouten worden geëlimineerd.

8.10.5BS50.907 Labeling (Aptean) De labeling extensie maakt het mogelijk om etiketten in te stellen die vanuit verschillende pagina’s kunnen worden afgedrukt. Wanneer een etiket moet worden afgedrukt, wordt de inhoudt van het etiket gegenereerd en doorgestuurd naar een extern programma dat het etiket gaat printen. Deze extensie zorgt ervoor dat informatie vanop alle schermen van Business Central op een etiket geprint kan worden. De label output file bevat inzichten over welke labels geprint zijn. Het houdt de informatie bij over het waar en wanneer de labels zijn afgedrukt. Ook wordt de informatie die op de labels staat hierin bijgehouden. Vanuit dit scherm kunnen we de labels ook opnieuw afdrukken. De labels kunnen afgedrukt worden voor een bepaalde klant, leverancier, item of een combinatie van deze. Het is ook mogelijk om klanten/leveranciers/artikelen te bundelen in een label categorie waardoor ze hetzelfde label krijgen.
