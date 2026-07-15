## 9. Service
Het domein "service" omvat de bedrijfsprocessen voor het ondersteunen van werkzaamheden in herstelwerkplaatsen en servicewerkzaamheden op klantenlocaties:

- Het beheer en de opvolging van verkochte goederen waarvoor service wordt aangeboden
- Het beheer van reserveonderdelen en het plannen van de aanvoer van materialen.
- Het plannen en uitzenden van servicetechnici
- De registratie van verbruikte materialen en uren voor het uitvoeren van de serviceopdrachten.
- Het plannen, uitvoeren en factureren van periodiek onderhoud op basis van contractuele service-
overeenkomsten met klanten

Business Scenario's - BPA Proces Service Commented [CP71]: @Niels Habraken Is 1 flow chart voldoende ? In andere modules zie ik er soms nog meer gedetailleerde. Of liever alleen de gedetailleerde ?

### 9.1 Service instellen
#### 9.1.1 BS60.001 Service management-instellingen
De service management-instellingen bevatten een aantal algemene instellingen en standaardwaarden voor het Commented [CP72]: @Niels Habraken Toch maar domein service. Voor een aantal velden kan aangeduid worden dat deze verplicht zijn. Ook voor aangepast, dan idem term in BC

servicecontracten kunnen een aantal standaardwaarden ingesteld worden. Verder worden in de service Commented [CP73]: Het tabblad “Contracten” omvat management-instellingen de nummerreeksen ingesteld die gebruikt worden binnen de service-module. onder meer tekstcodes die gebruikt worden voor de aansturing van de teksten op facturen voor servicecontracten:
#### 9.1.2 BS60.002 Probleemoplossingen instellen •“Code contractfactuurregeltekst”: hiermee wordt
de code aangeduid van de standaardtekst die https://learn.microsoft.com/en-us/dynamics365/business-central/service-how-setup-fault-reporting gebruikt wordt voor de vermelding van het contractnummer. De omschrijving uit de Probleemoplossingen zijn een onderdeel in de foutrapportage in het domein service. standaardtekst wordt samengevoegd met het contractnummer. Indien er geen De probleemoplossingen bevatten een lijst met codes en omschrijving van mogelijke oplossingen voor het standaardtekstcode wordt ingesteld dan wordt de oplossen van een probleem. De oplossingscodes kunnen worden geregistreerd bij het afwerken van een tekst “Servicecontract:” gevolg door het contractnummer gebruikt. servicetaak en maken het opbouwen van relaties tussen vaak voorkomende problemen en de bijhorende •“Code contractregelfactuurtekst”: de omschrijving oplossing mogelijk. van de tekstcode die hier wordt ingesteld wordt gebruikt voor de tekst op de eerste regel van een servicefactuur voor servicecontracten. Indien er
### 9.2 Service Master Data geen standaardtekstcode wordt ingesteld wordt de
tekst “Servicecontractregel(s) opgenomen in:”
#### 9.2.1 BS60.100 Beheer serviceartikelen gebruikt.

https://learn.microsoft.com/en-us/dynamics365/business-central/service-how-to-create-service-items

In de Service-module van Business Central vormen serviceartikelen de kern van het beheer van servicecontracten, onderhoud en reparaties. Een serviceartikel is een geregistreerd object dat door een klant wordt gebruikt en waarvoor het bedrijf serviceactiviteiten uitvoert. Dit kan een fysiek product zijn, zoals een machine, voertuig of apparaat, maar ook een complex systeem dat uit meerdere onderdelen bestaat.

Belangrijkste kenmerken van een serviceartikel:

- Identificatie: Elk serviceartikel heeft een unieke code en kan gekoppeld worden aan een klant, locatie
en serienummer.

- Structuur: Serviceartikelen kunnen een hiërarchische opbouw hebben, waarbij een hoofdartikel
subcomponenten bevat. Dit maakt het mogelijk om onderhoud op detailniveau te plannen.

- Historiek: Alle serviceactiviteiten, inclusief reparaties, vervangingen en inspecties, worden geregistreerd
op het serviceartikel. Dit biedt inzicht in de levenscyclus en kosten.

- Contractkoppeling: Serviceartikelen kunnen worden opgenomen in servicecontracten, waardoor
preventief onderhoud en SLA-afspraken eenvoudig beheerd worden.

Integratie met voorraad: Onderdelen die nodig zijn voor servicewerkzaamheden kunnen worden gekoppeld aan het serviceartikel, wat zorgt voor een nauwkeurige materiaalplanning.

Serviceartikelen kunnen op 3 manieren gemaakt worden:

- Manueel: Dit zal vooral het geval zijn indien het gaat om artikelen die niet door u verkocht zijn of als
het gaat over zaken die aanvankelijk geen service hadden.

- Automatisch door een verzending van een artikel te boeken..

- Vanuit een service order: Tijdens de uitvoering van een serviceonderhoud, wordt een nieuw
serviceartikel toegevoegd.

#### 9.2.2 BS60.101 Serviceartikelcomponenten beheren
https://learn.microsoft.com/en-us/dynamics365/business-central/service-how-setup-service-items#to-set-up- service-item-components

Een serviceartikel kan bestaan uit meerdere onderdelen die u door reserveonderdelen kunt vervangen wanneer voor het artikel service wordt uitgevoerd.

U kunt een componentenlijst voor serviceartikelen instellen door handmatig een componentenlijst te maken of door componentonderdelen uit een (assemblage) stuklijst te kopiëren. Met het handmatige proces maakt u zelf een componentenlijst. Bij het kopiëren van serviceartikel-componenten van een stuklijst hebt u een serviceartikel nodig dat is gekoppeld aan een voorraadartikel met een assemblagestuklijst. Commented [NH74]: Gedrag van assemblagestuklijsten bij het automatisch aanmaken
#### 9.2.3 BS60.102 Serviceartikelgroepen beheren van serviceartikelen bij een verkoopverzending:
- Indien het verzonden artikel een
https://learn.microsoft.com/en-us/dynamics365/business-central/service-how-setup-service-items#to-set-up- assemblagestuklijst bevat en de assemblagestuklijst wordt niet weergegeven (uitgeklapt) op het service-item-groups verkooporder, worden de componenten van de assemblagestuklijst niet als serviceartikel- Serviceartikelgroepen kunnen worden toegekend aan serviceartikelen en reguliere artikelen. componenten aangemaakt.
- Indien een uitgeklapte assemblagestuklijst
Serviceartikelgroepen bevatten standaardwaarden voor het contractkortingspercentage, de standaard artikelen bevat die op hun beurt ook een serviceprijsgroep en standaard responstijd. assemblagestuklijst hebben, dan worden serviceartikelen aangemaakt voor de componenten In de serviceartikelgroep wordt ook aangegeven of er bij verkoop van een regulier artikel automatisch een als aan volgende voorwaarden voldaan is:
  - Het veld “Geïnstalleerd in artikelnr.” bevat een
serviceartikel moet aangemaakt worden. waarde die verwijst naar een ander artikel (andere regel) uit de assemblagestuklijst. Aan serviceartikelgroepen kunnen ook resourcebekwaamheden, troubleshootinginstellingen en standaard o Op de assemblagestuklijst-component is een serviceartikelgroepcodes toegekend worden. serviceartikelgroep gekoppeld waar het veld “Serviceartikel maken” is ingeschakeld.

#### 9.2.4 BS60.103 Beheer serviceprijsgroepen
https://learn.microsoft.com/en-us/dynamics365/business-central/service-how-setup-service-costs-pricing#set- up-a-service-price-group

Serviceprijsgroepen zijn een mechanisme om flexibele prijsafspraken te beheren voor serviceactiviteiten en onderdelen binnen de Service-module. Ze werken vergelijkbaar met artikelprijsgroepen, maar zijn specifiek gericht op (contract)serviceorders.

Een serviceprijsgroep is een categorie die je kunt toewijzen aan:

- Serviceartikelen (bijv. machines, apparaten)

- Serviceartikelgroepen

- Artikelen

Per serviceprijsgroep kan je verschillende speciale prijsherwaarderingen instellen, door koppeling met

- Klantenprijsgroep (facultatief)

- Valuta

- Begindatum

- Serviceprijsherwaarderingsgroep (facultatief)

- Herwaarderingssoort (vast, maximum, minimum)

- Probleemgebied (facultatief)

#### 9.2.5 BS60.104 Beheer serviceprijsherwaarderingsgroepen
https://learn.microsoft.com/en-us/dynamics365/business-central/service-how-setup-service-costs-pricing#set- up-a-service-price-adjustment-group

Met serviceprijsherwaarderingsgroepen stel je in op “wat” de prijsaanpassing moet toegepast worden:

- Soort = artikelen, resources(groep), servicekosten, grootboekrekening

- Welke = alles uit de “soort”, 1 of meer specifieke definitie uit de “soort”

In de koppeling “serviceprijsgroep – serviceprijsherwaarderingsgroep” definieer je “welke” prijsaanpassing geldig is (herwaarderingssoort, bedrag).

De serviceprijsherwaardering wordt niet automatisch uitgevoerd in een (contract)serviceorder. De gebruiker moet manueel de actie “Serviceprijs herwaarderen” uitvoeren in het (contract)serviceorder. Deze

serviceprijsaanpassingsfunctie is niet van toepassing op service-items die onder servicecontracten vallen, onder garantie staan, of al (gedeeltelijk) zijn gefactureerd.

#### 9.2.6 BS60.105 Servicekosten beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-setup-service-costs-pricing#to- set-up-additional-costs-for-services

Bij het aanmaken van servicekosten kan de kostensoort ingesteld worden op “Andere”, “Ondersteuning” en “Vervoerskosten”. Aan vervoerskosten kan ook een serviceregio toegekend worden, zodat de kost afhankelijk is van de regio waar de klant zich bevindt. Verder kunnen aan de servicekosten worden toegekend: grootboekrekeningnummer, eenheid, standaard aantal, standaard kostprijs en standaard eenheidsprijs. Ook in verkoopprijslijsten kunnen servicekosten opgenomen worden voor definitie van specifieke verkoopprijs en/of korting. Indien men gebruik wil maken van een starttarief kan men deze aanmaken als een servicekost en deze servicekost selecteren in de service management-instellingen.

#### 9.2.7 BS60.106 Standaardservicecodes beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-setup-service-coding

In de definitie van een standaardservicecode bepaalt men een set aan standaard verwachte benodigde artikelen/resources/kosten, het is eigenlijk een predefinitie van serviceregels voor die service (vb. periodiek onderhoud). Op niveau van serviceartikelgroep is het mogelijk om >1 standaardservicegroep te koppelen. In een service-offerte/-order is functie “Std.servicecodes ophalen” beschikbaar, zodat de gebruiker voor de geselecteerde serviceartikelregel dan 1 of meer standaardservicecodes kan ophalen met als resultaat ingevoegde serviceregels in overeenstemming met set in deze standaardservicecode.

#### 9.2.8 BS60.107 Serviceordersoorten beheren
Serviceordersoorten maken het mogelijk om onderscheid te maken in verschillende types van serviceopdrachten. In elke servicetransactie (offerte, order, factuur, creditnota) kan men serviceordersoort invullen (op kopniveau), via parameter in service management-instellingen kan het zelfs verplicht worden. In servicecontract kan men serviceordersoort ook invullen, dit is dan geldig voor alle servicecontractregels. Serviceorders gekoppeld aan een servicecontract (manueel of via functie “contractserviceorders aanmaken”) erven de serviceordersoort van het gekoppelde servicecontract.

### 9.3 Serviceoffertes maken
#### 9.3.1 BS60.200 Aanmaken van service offertes
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-create-service-quotes

De serviceofferte bevat de basisgegevens (responstijd, orderstatus, naam, adres, telefoonnummer van de klant), maar ook gedetailleerde informatie over de serviceartikelen die service nodig hebben (bijvoorbeeld serienummer, garantie en probleemopmerkingen). U kunt een serviceofferte maken voor iedere nieuwe servicebehoefte die de klant heeft.

De hoofding van een serviceofferte bestaat uit algemene gegevens, zoals het klantnummer, de verzendcode (installatieadres), betalingsgegevens enz. De regels van een serviceofferte bevatten de serviceartikelen waarvoor de service wordt aangeboden. Aan elke regel kunnen een of meerdere serviceregels gekoppeld worden welke een gedetailleerde beschrijving bevat van de aangeboden artikelen, diensten en eventuele kosten.

#### 9.3.2 BS60.201 Opvolgen van service offertes
Een serviceofferte wordt omgezet naar een serviceorder via de functie “Order maken” vanaf het overzicht van de serviceoffertes of vanaf de serviceofferte-kaart. Nadat een offerte is omgezet wordt deze verwijderd. Het serviceorder dat wordt aangemaakt bevat het offertenummer. In service management instellingen kan men sturen dat serviceofferte eerst gearchiveerd wordt alvorens te verwijderen.

### 9.4 Serviceorders beheren
#### 9.4.1 BS60.202 Aanmaken van een serviceorder
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-create-service-orders#to- create-a-service-order

https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-create-service-orders#to- convert-a-service-quote-to-a-service-order

Het serviceorder bevat de basisgegevens (responstijd, orderstatus, naam, adres, telefoonnummer van de klant), maar ook gedetailleerde informatie over de serviceartikelen die service nodig hebben (bijvoorbeeld serienummer, garantie en probleemopmerkingen) en de artikelen of resources die worden gebruikt in het servicewerk.

- Aanmaken van een serviceorder (manueel): Een serviceorder kan manueel aangemaakt worden,
bijvoorbeeld bij een vraag van een klant voor het uitvoeren van een herstelling. Voor het aanmaken van een serviceorder wordt de klant en verzendcode geselecteerd en wordt op de regels een of meerdere serviceartikelen geselecteerd.

- Aanmaken van een serviceorder vanuit een service offerte: Een vraag van een klant voor een prijsopgave
voor het uitvoeren van service kan worden geregistreerd aan de hand van een serviceofferte. Wanneer de klant de serviceofferte goedkeurt kan deze omgezet worden naar een serviceorder.

#### 9.4.2 BS60.203 Aanmaken van een contract-serviceorder
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-create-service-orders#to- create-a-service-order-from-a-contract

Indien met een klant een servicecontract overeengekomen is, kunnen er op basis van het contract serviceorders gemaakt worden door middel van een periodieke activiteit. Op het servicecontract kan het interval voor het uitvoeren van de service worden vastgelegd (bijv. jaarlijks, 6-maandelijks enz.). Op basis van de volgende geplande servicedatum die op de contracten (op regelniveau) wordt bijgehouden, worden er door de periodieke activiteit serviceorders aangemaakt. Een globale instelling in service management-instellingen geeft aan of de nieuwe volgende geplande servicedatum wordt berekend op basis van de huidige geplande servicedatum of op basis van de datum dat de service werkelijk werd uitgevoerd.

- Aanmaken van een contract-serviceorder in batch, alleen afdrukken: Dit kan gebruikt worden voor het
afdrukken van een lijst met een overzicht van de serviceorders die zouden worden aangemaakt. Bij het uitvoeren van de periodieke activiteit geeft men de begin- en einddatum in en kunnen er aanvullende filters ingesteld worden op basis van de contractkop-tabel. Alle contractregels (van actieve contracten) waarvan de volgende geplande servicedatum tussen de ingevoerde begin- en einddatum vallen worden opgenomen.

- Aanmaken van een contract-serviceorder in batch, serviceorders maken: Dit kan gebruikt worden voor
het aanmaken van serviceorders op basis van servicecontracten. Bij het uitvoeren van de periodieke activiteit geeft men de begin- en einddatum in en kunnen er aanvullende filters ingesteld worden op basis van de contractkop-tabel. Alle contractregels (van actieve contracten) waarvan de volgende geplande servicedatum tussen de ingevoerde begin- en einddatum vallen worden opgenomen.

- Aanmaken van een contract-serviceorder (manueel): Een serviceorder kan manueel gekoppeld worden
aan een contract. De koppeling kan op de hoofding of op de regels van het serviceorder geselecteerd worden. Wanneer de koppeling op de hoofding gemaakt wordt, wordt de volgende geplande servicedatum op het gekoppelde contract bijgewerkt. Dit gebeurt niet wanneer de koppeling op de regels wordt gemaakt. In beide gevallen wordt de contractkorting van het gekoppelde contract toegepast.

#### 9.4.3 BS60.204 Registreren verbruik op serviceorders
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-post-service-orders#to-post- consumption-from-a-service-order

Op een service order is er ook de mogelijkheid om goederen te verbruiken in plaats van te factureren. Dit kan als de service een dienst is die bv. onder garantie of in een omniumcontract valt, of als er geopteerd wordt om niet

alle verbruikte goederen te factureren. Als er artikelen/uren of kosten verbruikt worden in een service order worden deze financieel afgesloten, maar dus niet gefactureerd.

Volgende types van verbruik kan je registreren op een serviceorder, in de serviceregels: artikelen, resources (uren), kosten, grootboekrekening.

#### 9.4.4 BS60.205 Serviceverzending boeken
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-post-service-orders#to-post- shipments-from-service-orders

Het verzenden van een serviceorder geeft aan dat de materialen en resources op het serviceorder zijn gebruikt. Bij de boeking van de verzending van artikelen wordt de voorraad van de artikelen verminderd met het verzonden aantal. Het verzenden van een serviceorder kan dus toegepast worden om de voorraad van de artikelen (bijvoorbeeld wisselstukken) aan te passen en om aan te geven dat de geregistreerde werkzaamheden zijn uitgevoerd. Bij de verzending kan ook een verzendnota (geboekte serviceverzending) afgedrukt worden.

- Serviceverzending boeken vanuit het serviceorder: Indien er geen nood is aan uitgebreide
magazijnbewerkingen, bijvoorbeeld wanneer de artikelen verbruikt worden uit de servicewagen, kan de verzending rechtstreeks vanaf een serviceorder geregistreerd worden.

- Serviceverzending boeken via magazijnverzending: Indien er nood is aan magazijnbewerkingen,
bijvoorbeeld voor het picken en verzendklaar maken van de artikelen die nodig zijn voor het uitvoeren van de servicewerkzaamheden, kan er een magazijnverzending aangemaakt worden vanaf het serviceorder.

#### 9.4.5 BS60.206 Serviceverzending ongedaan maken
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-post-service-orders#to-undo- posted-consumption

Dit scenario behandelt het corrigeren van een geboekte serviceverzending. Er zijn 2 mogelijkheden:

- Serviceverzending ongedaan maken: Een geboekte serviceverzending (op niveau van regel) ongedaan
maken, heeft als resultaat dat geboekte regel(s) in die geboekte serviceverzending worden tegengeboekt met een negatief aantal. In de serviceregel(s) van het serviceorder resulteert dit in verhoging van “te verzenden aantal” en verlaging van “verzonden aantal”.

- Serviceverzending ongedaan maken (verbruik): Een geboekte serviceverzending (op niveau van regel)
ongedaan maken voor “verbruik”, heeft als resultaat dat geboekte regel(s) in die geboekte serviceverzending worden tegengeboekt met een negatief aantal. In de serviceregel(s) van het serviceorder resulteert dit in verhoging van “te verzenden aantal” en verlaging van “verbruikt aantal”.

#### 9.4.6 BS60.207 Herstelstatus beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-order-repair-status

https://learn.microsoft.com/nl-be/dynamics365/business-central/service-service-order-status-and-repair- status

De herstelstatus geeft aan in welke fase een serviceartikel zich bevindt binnen een serviceorder. Elke herstelstatus is gekoppeld aan een serviceorderstatus.

Telkens wanneer de herstelstatus van een serviceartikel wordt gewijzigd in een serviceorder, wordt de orderstatus bijgewerkt, het order krijgt de “laagste” status van alle lijnen. In praktijk: een order is afgehandeld als alle serviceartikelen zijn afgewerkt.

#### 9.4.7 BS60.222 Serviceorders archiveren
Een serviceorder (al dan niet afgewerkt) kan men manueel archiveren, meermaals archiveren is mogelijk. In Commented [CP75]: @Niels Habraken Oorspronkelijke service-instellingen is het mogelijk om automatisch archiveren te activeren, zodat het systeem eerst het tekst is correct => serviceorder kan >1 keer gearchiveerd worden serviceorder archiveert alvorens het te verwijderen (manueel of automatisch bv na volledig boeken).

Vergelijkbaar met archiveren van andere documenten (verkoop, inkoop) is het doel om enkel de documenten waar nog op gewerkt moet worden in de actieve lijst van serviceorders te tonen. Orders die zijn afgewerkt worden ergens anders bewaard, wat zowel de performantie van het systeem als deze van de dagelijkse opvolging vereenvoudigd.

### 9.5 Service plannen
Dit subdomein omvat scenario's voor het inplannen van resources (techniekers) op serviceorders en het voorzien van de nodige materialen voor de uitvoer van service.

#### 9.5.1 BS60.208 Resource plannen op serviceorder
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-allocate-resources

Resources kunnen worden ingepland op serviceorders. Hiermee wordt aangegeven welke resource een bepaalde werkzaamheid zal uitvoeren, op welke datum en hoeveel tijd hiervoor voorzien is. De toegewezen capaciteit wordt in mindering gebracht van de beschikbare resource-capaciteit.

##### 9.5.1.1 BC60.208.01 Resource plannen op serviceorder via servicetaken
Het overzicht servicetaken geeft een overzicht van alle servicetaken van serviceorders op regelniveau. Indien een serviceorder meerdere regels met serviceartikelen bevat worden deze als afzonderlijke regels weergegeven in het overzicht servicetaken. Via filters kan geselecteerd worden welke regels er in het overzicht worden getoond

(bijvoorbeeld alle regels met een bepaalde responsdatum of herstelstatus). Vanaf het overzicht kan het serviceorder van de geselecteerde regel geopend worden en kunnen resourcetoewijzingen op het serviceorder gemaakt worden.

##### 9.5.1.2 BC60.208.02 Resource plannen op een serviceorder via planbord
Het planbord geeft een globaal overzicht van de serviceorders: indien een serviceorder meerdere serviceartikelregels bevat wordt dit als één regel in het planbord getoond. Via filters kan geselecteerd worden welke serviceorders er in het overzicht worden getoond (bijvoorbeeld alle serviceorders met een bepaalde responsdatum, alle serviceorders van een bepaalde klant enz.). De resourcetoewijzingen kunnen rechtstreeks vanaf het planbord geopend worden.

##### 9.5.1.3 BC60.208.03 Resource plannen via DIME scheduler
https://www.dimescheduler.com/ Field Code Changed

https://docs.dimescheduler.com/administration/guides/implementation-checklist Field Code Changed

Dime Scheduler is een planningstool die naadloos integreert met Dynamics 365 Business Central en andere ERP- systemen. Het biedt geavanceerde functionaliteit voor het plannen en beheren van resources, taken en projecten.

- Resourceplanning: Plan medewerkers, voertuigen, machines en andere middelen op basis van
beschikbaarheid, vaardigheden en locatie.

- Visuele planning: Gebruik een drag-and-drop interface om taken eenvoudig toe te wijzen aan
resources in een grafische planningstabel.

- Integratie met ERP: Synchroniseert automatisch met Business Central voor serviceorders

- Kaartintegratie: Optimaliseer routes en bekijk resource- en taaklocaties via geïntegreerde kaarten.

- Capaciteitsbeheer: Controleer bezettingsgraad en beschikbaarheid van resources om over- of
onderplanning te voorkomen.

- Real-time updates: Wijzigingen in planning worden direct doorgevoerd en zichtbaar voor alle
gebruikers.

#### 9.5.2 BS60.209 Reserveer voorraad op een serviceorder
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-create-service-orders#to- reserve-an-item-for-a-service-order

Indien er nood is aan een bepaald artikel voor de uitvoering van de servicewerkzaamheden kan er een reservering van het artikel voorzien worden.

Het reserveren van artikelen op serviceorders gebeurt vanaf de serviceregels. Voor regels met soort “Artikel” kan het reserveringsscherm geopend worden en kan op basis van het beschikbare aantal een reservering gemaakt worden.

### 9.6 Serviceorders factureren
#### 9.6.1 BS60.210 Servicefacturen maken
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-create-invoices#to-post-an- invoice-from-a-service-order

https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-create-invoices#to-create-an- invoice-that-combines-posted-shipment-lines-from-one-or-more-service-orders

https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-create-invoices#to-create-a- service-invoice-manually

Dit scenario behandelt de verschillende wijzen waarop een servicefactuur kan gemaakt worden. Het betreft hier manuele facturen of facturen die voor een serviceorder gemaakt worden, dus geen facturen voor servicecontracten.

- Servicefacturen maken vanuit serviceorder: Wanneer een of meerdere verzendingen voor een
serviceorder geregistreerd zijn kan er een servicefactuur gemaakt worden. Indien nodig kunnen bijkomende kosten (bijv. transportkosten) toegevoegd worden. Bij het boeken van een serviceorder zorgt de optie “Factureren” ervoor dat de regels waar reeds een verzending voor geboekt is, worden gefactureerd. Voor regels waar nog geen verzending voor geboekt is, kan de optie “Verzenden en factureren” gebruikt worden. De prijzen en kortingen worden van het serviceorder overgenomen.

- Servicefacturen maken met ophalen serviceverzendregels: Bij het maken van servicefacturen via het
ophalen van verzendregels wordt eerst een manuele factuur gemaakt waarop de klant en verzendadres (indien van toepassing) worden geselecteerd. Vervolgens wordt een overzicht geopend van alle verzonden-niet gefactureerde verzendingen voor de klant op het gekozen verzendadres. Uit dit overzicht worden de regels geselecteerd die men wenst te factureren.

- Servicefacturen maken (manueel): Een servicefactuur kan manueel aangemaakt worden zonder dat er
een serviceorder voor bestaat. Bij het manueel aanmaken van een servicefactuur worden de kop- en regeldetails manueel ingevoerd.

### 9.7 Servicecontractoffertes maken
#### 9.7.1 BS60.211 Servicecontractoffertes maken
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-create-service-contracts-and- service-contract-quotes#to-create-a-service-contract-or-service-contract-quote

Servicecontractoffertes worden toegepast voor het aanbieden aan de klant van periodieke service op toestellen of installatie van klanten. Op de hoofding van de contractofferte worden de algemene gegevens (zoals klantnummer, installatieadres (verzendcode) en betalingsgegevens) ingesteld. Op de regels registreer je de serviceartikelen met de prijs waarvoor men de service wil aanbieden in de servicecontractofferte.

Indien er servicecontractsjablonen zijn gedefinieerd, dan wordt er voorgesteld om de servicecontractofferte aan te maken op basis van een sjabloon, zo wordt een deel van de gegevens in de hoofding al automatisch ingevuld. Via de actie “Contractofferteregels selecteren” kunnen meerdere serviceartikelen in één beweging aan de servicecontractofferte worden toegevoegd.

### 9.8 Servicecontracten beheren
Een servicecontract is een formeel document waarmee je afspraken vastlegt tussen jouw organisatie en een klant over het leveren van service en onderhoud voor specifieke (service)artikelen, toestellen of installaties. Het is een kernonderdeel van de servicemodule en biedt structuur voor langdurige klantrelaties. In het document worden de periodieke serviceactiviteiten (bijv. onderhoud, inspecties, reparaties) en de financiële afspraken (bijv. vaste prijzen, factureringsschema’s en contractduur) vastgelegd.

#### 9.8.1 BS60.213 Servicecontracten maken
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-create-service-contracts-and- service-contract-quotes#to-create-a-service-contract-or-service-contract-quote

https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-create-service-contracts-and- service-contract-quotes#to-convert-a-service-contract-quote-to-service-contract

Op de hoofding van het servicecontract worden de algemene gegevens (zoals klantnummer, installatieadres (verzendcode) en betalingsgegevens) ingesteld. Op de regels registreer je de serviceartikelen met de prijs waarvoor men de service vastlegt in het servicecontract.

Indien er servicecontractsjablonen zijn gedefinieerd, dan wordt er voorgesteld om het servicecontract aan te maken op basis van een sjabloon, zo wordt een deel van de gegevens in de hoofding al automatisch ingevuld. Via de actie “Contractregels selecteren” kunnen meerdere serviceartikelen in één beweging aan het servicecontract worden toegevoegd.

Voor het servicecontract kan bepaald worden of de betaling vooraf moet gebeuren of niet.

Tenslotte kan de status van het servicecontract worden aangepast. Een actief servicecontract heeft de status “Ondertekend” en vergrendelingsstatus “Vergrendeld”, zodat er niets meer gewijzigd kan worden.

Opties voor aanmaken van servicecontract:

- Aanmaken van een servicecontract (manueel): Een servicecontract kan manueel aangemaakt worden.

- Aanmaken van een servicecontract vanuit een servicecontractofferte: Na goedkeuring van
servicecontractofferte, kan deze omgezet worden in een servicecontract met directe toewijzing van status “Ondertekend” en vergrendelingsstatus “Vergrendeld”.

#### 9.8.2 BS60.214 Servicecontracten bijwerken
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-create-service-contracts-and- service-contract-quotes#to-change-the-owner-of-a-service-contract

https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-create-service-contracts-and- service-contract-quotes#to-remove-contract-lines

https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-create-service-contracts-and- service-contract-quotes#to-add-a-contract-line-to-a-service-contract-or-contract-quote

Uiteraard kunnen wijzigingen in een ondertekend servicecontract achteraf nodig zijn: looptijd aanpassen of verlengen, nieuwe artikelen toevoegen in een contract, …

Vooraleer men wijzigingen aan een lopend, ondertekend servicecontract kan aanbrengen dient men het servicecontract opnieuw te openen. Daarna kan men de nodige wijzigingen registreren en vervolgens het servicecontract terug vergrendelen.

Volgende bepalingen kunnen gewijzigd worden in een ondertekend servicecontract:

- Eigenaar van het servicecontract (= via actie “klant wijzigen”)

- Verwijderen van contractregels

- Toevoegen van contractregels

Volgende bepalingen kunnen niet gewijzigd worden in een ondertekend servicecontract:

- Serviceperiode
- Vooruitbetaald

#### 9.8.3 BS60.215 Servicecontracten beëindigen
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-create-service-contracts-and- service-contract-quotes#to-cancel-a-service-contract

Een servicecontract kan beëindigd worden, bijvoorbeeld omdat de met de klant afgesproken contracttermijn verlopen is, of omdat de klant het contract wenst stop te zetten.

Mogelijke opties:

- Servicecontract beëindigen, alle regels: Om aan te geven dat het globale servicecontract ten einde loopt
op een specifieke datum in de toekomst, vul je deze datum in op de hoofding van het servicecontract (in veld “verloopdatum). Deze verloopdatum wordt dan automatisch ingevuld in alle nog actieve servicecontractregels, zodat deze regels ook dezelfde verloopdatum krijgen.

- Servicecontract beëindigen, selectie regels: Om één of meer regels (maar niet alle regels) in een
servicecontract op een specifieke datum te beëindigen, vul je deze datum in desbetreffende servicecontractregel(s) in (in veld “verloopdatum van het contract”). Het contract blijft actief voor de andere serviceartikelen.

- Servicecontract annuleren: Om een servicecontract globaal te annuleren, wijzig je de status in
“Geannuleerd”. Deze annulatie gaat dan onmiddellijk in, verloopdatum wordt niet ingevuld want status is hier bepalend.

#### 9.8.4 BS60.216 Vooruitbetaalde servicecontractposten boeken
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-create-service-contracts-and- service-contract-quotes#to-post-prepaid-contract-entries

Bij een vooruitbetaald servicecontract wordt de factuur aangemaakt aan het begin van de factuurperiode. Het factuurbedrag wordt daarbij op een tijdelijke grootboekrekening geboekt. Op periodieke basis (bijv. elke maand) wordt een deel van het vooruitbetaalde bedrag naar omzet geboekt.

- Vooruitbetaalde servicecontractposten boeken, alleen afdrukken: met de optie “Alleen afdrukken”
worden de posten nog niet geboekt maar krijgt men een overzicht van de servicecontractposten die in aanmerking komen om overgeboekt te worden.
- Vooruitbetaalde servicecontractposten boeken, transacties boeken: met de optie “Vooruitbetaalde
transacties boeken” worden de posten van de tijdelijke grootboekrekening naar de omzetrekening geboekt.

#### 9.8.5 BS60.217 Servicecontractprijzen bijwerken
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-to-create-service-contracts-and- service-contract-quotes#to-update-a-service-contract-price

De servicecontractprijzen kunnen worden bijgewerkt door middel van de periodieke activiteit “Servicecontractprijzen bijwerken”.

Bij het uitvoeren van deze periodieke activiteit geeft men de volgende opties in:

- Datum tot waar de servicecontractprijzen moeten bijgewerkt worden.

- Percentage waarmee de contractprijzen moeten worden verhoogd (of verlaagd).

- Effectieve actie die moet uitgevoerd worden:

  - “Alleen afdrukken”: de prijzen in de servicecontractregels worden nog niet gewijzigd, maar
men krijgt een overzicht van de servicecontractprijzen die in aanmerking komen om aangepast te worden.

  - “Contractprijzen aanpassen”: de regelwaarde in de servicecontractregels worden aangepast.

De periodieke activiteit houdt rekening met de volgende prijsaanpassingsdatum op de servicecontracten. Wanneer de geselecteerde datum in de periodieke activiteit op of na de volgende prijsaanpassingsdatum van een servicecontract valt, komt het contract in aanmerking voor een prijsverhoging.

### 9.9 Servicecontracten factureren
#### 9.9.1 BS60.619 Servicecontracten factureren Commented [CP76]: @Niels Habraken Ik ken logica
van BS nummering niet => in flowchart stond hier wel https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-create-invoices#to-invoice- 60.219 => dus ik heb nummer in flowchart dan aangepast in 60.619 several-service-contracts

https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-create-invoices#to-invoice-a- service-contract-from-the-service-contract-page

Het factureren van servicecontracten houdt in dat er een servicefactuur gemaakt wordt voor de serviceartikelen die op het contract zijn opgenomen met de afgesproken prijzen en kortingen voor de factuurperiode. De factuur die gemaakt wordt omvat het bedrag voor de service die met de klant werd overeengekomen voor een bepaalde periode.

- Servicecontractfacturen maken vanaf servicecontract: Servicefacturen kunnen rechtstreeks vanaf het
servicecontract worden aangemaakt, bijvoorbeeld wanneer men de eerste periode wenst te factureren nadat het contract werd aangemaakt en ondertekend. Bij het aanmaken van een servicefactuur vanaf

een contract wordt de eerstvolgende factuurperiode gefactureerd, en wordt de volgende factuurperiode op het contract bijgewerkt.
- Servicecontractfacturen maken in batch, alleen afdrukken: Via de periodieke taak
“Servicecontractfacturen maken” kunnen facturen voor meerdere contracten in batch worden aangemaakt. Via filters kan er geselecteerd worden welke contracten er opgenomen worden in de facturatie. Bij het uitvoeren van de periodieke taak geeft men ook aan tot welke datum men wenst te factureren. Via de optie “Alleen afdrukken” worden de facturen nog niet gemaakt, maar krijgt men een overzicht van de contracten, bedragen en periodes die zouden gefactureerd worden.
- Servicecontractfacturen maken in batch, facturen maken: Via de periodieke taak
“Servicecontractfacturen maken” kunnen facturen voor meerdere contracten in batch worden aangemaakt. Via filters kan er geselecteerd worden welke contracten er opgenomen worden in de facturatie. Bij het uitvoeren van de periodieke taak geeft men ook aan tot welke datum men wenst te factureren. Via de optie “Facturen maken” worden de facturen ook effectief gemaakt en de volgende factuurperiode in het contract bijgewerkt.

### 9.10 Servicecreditnota's beheren
#### 9.10.1 BS60.620 Servicecontract-creditnota maken
Een servicecontract-creditnota wordt gemaakt om de gefactureerde periodes van een servicecontract te compenseren.

Voor het aanmaken van een servicecreditnota moet de vergrendelingsstatus van het contract terug op “Open” gezet worden. Vervolgens dient op de contractregels die men wenst te crediteren een verloopdatum (is dan ook creditnotadatum) ingevoerd worden. Via de actie “Servicecreditnota maken” wordt een servicecreditnota gemaakt voor de periode vanaf de ingevoerde verloopdatum tot de einddatum van de laatst gefactureerde periode. De ongeboekte servicecreditnota moet daarna nog worden geboekt.

#### 9.10.2 BS60.621 Servicecreditnota's maken
https://learn.microsoft.com/nl-be/dynamics365/business-central/service-how-create-invoices#to-create-a- service-credit-memo

Een servicecreditnota kan manueel aangemaakt worden, om een foutieve factuur te corrigeren. Hierbij worden de kop- en regeldetails manueel ingevoerd.

### 9.11 Document Lay-outs Service
#### 9.11.1 Service offerte Commented [CP77]: Geen Cegeka lay-out beschikbaar

#### 9.11.2 Service orderbevestiging Commented [CP78]: Geen Cegeka lay-out beschikbaar

#### 9.11.3 Service werkbon Commented [CP79]: Geen Cegeka lay-out beschikbaar

#### 9.11.4 Servicefactuur Commented [CP80]: Geen Cegeka lay-out beschikbaar

#### 9.11.5 Servicecreditnota Commented [CP81]: Geen Cegeka lay-out beschikbaar

#### 9.11.6 Servicecontractofferte Commented [CP82]: Geen Cegeka lay-out beschikbaar

#### 9.11.7 Servicecontract Commented [CP83]: Geen Cegeka lay-out beschikbaar

#### 9.11.8 Servicecontractfactuur Commented [CP84]: Geen Cegeka lay-out beschikbaar

#### 9.11.9 Servicecontractcreditnota Commented [CP85]: Geen Cegeka lay-out beschikbaar
