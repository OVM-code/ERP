## 1. Bedrijfsinformatie
Dit domein bevat de master data van het bedrijf welke voor verschillende onderdelen van het bedrijf van toepassing zijn, zoals de algemene bedrijfsgegevens, divisies en vestigingen.

**GAP-1 — Voorbeeld GAP**

### 1.1 Algemene bedrijfsinformatie
#### 1.1.1 BS10.001 Beheer organisaties
Deze scenario-variant omvat alle basisinformatie over en verhoudingen tussen de betrokken bedrijven en entiteiten. Deze vertalen zich in de oplossing als companies of bedrijven. BC kan tot 300 bedrijven bevatten.

#### 1.1.2 BS95.001 Gebruikers
Dit scenario omvat de instellingen voor gebruikers van Business Central. Hiermee wordt de toegang tot Business Central, de boekingsinstellingen en divisies en de profielen van de gebruikers geregeld.

Via het venster Gebruikers wordt de toegang tot Business Central geregeld. Hiermee worden de gebruiker die in Business Central kunnen werken ingesteld, en wordt het licentietype (full user, limited user, …) geselecteerd. Via dit venster kunnen aan gebruikers ook groepen en machtigingssets toegekend.

In de gebruikersinstellingen wordt de periode ingesteld waarin de gebruiker verrichtingen kan uitvoeren (via de datumvelden boeken toegestaan vanaf en boeken toegestaan tot). Hier worden ook de verkoop-, inkoop- en servicedivisie ingesteld, en wordt de gebruiker gekoppeld aan een verkoper/inkoper, en wordt bepaald of het boeken van deze documenten toegestaan is voor de gebruiker. Tijd registreren en urenstaten administrator voor projecten kan hier worden ingeschakeld. Verder wordt in dit venster het e-mailadres en telefoonnummer (informatief) van de gebruiker ingesteld.

Via de persoonlijke gebruikersinstellingen kan het rolcentrum ingesteld per gebruiker. Ook de taal en het standaard bedrijf voor de gebruiker worden hier ingesteld. De voorkeur is echter om het rolcentrum per functie/rol in te stellen voor de meeste gebruikers, zodat de gebruikers in eenzelfde rol, ook dezelfde scherm layout hebben.

### 1.2 Divisies instellen
#### 1.2.1 BS10.002 Divisies beheren
Deze scenario-variant behandelt het beheer van divisies. Divisies worden gebruikt om een onderscheid te maken tussen verschillende afdelingen - divisies - binnen een bedrijf. Er kunnen divisies ingesteld worden voor verkoop- , inkoop- en serviceafdelingen. Gebruikers kunnen enkel orders raadplegen en beheren binnen de divisie waarin

de gebruiker is ingedeeld. Elke gebruiker kan in een verkoop-, inkoop- en/of servicedivisie ingedeeld worden. Wanneer een gebruiker een order maakt, wordt dit automatisch aangemaakt binnen de divisie waarin de gebruiker is ingedeeld. Aan een divisie kan optioneel een dimensie (analytische code) toegekend worden.

### 1.3 Algemene bedrijfsfunctionaliteit
Dit domein omvat de master data en processen die over meerdere domeinen heen kunnen toegepast worden.

#### 1.3.1 BS10.009 Masterdata Synchronisatie
https://learn.microsoft.com/en-us/dynamics365/business-central/admin-set-up-data-sync

Het doel is om materdata (zoals klanten, leveranciers, artikelen) consistent en up-to-date te houden tussen meerdere Business Central-omgevingen of bedrijven binnen een groep. Daarnaast kan men ook bepaalde instellingentabellen (vb boekingsgroepen, betalingsmethoden, ...) op deze manier synchroon houden tussen bedrijven.

Dit voorkomt dubbele invoer en fouten bij het beheer van basisgegevens.

In standaard BC is een best practice om 1 bronbedrijf te hebben waarvan de andere bedrijven de data overnemen. Voor iedere tabel en veld van deze tabel kan bepaald worden of deze gesynchroniseerd moet worden.

##### 1.3.1.1 BC10.009.01 Masterdata Sync (IT Integro)
De IT integro extensie biedt meer mogelijkheden voor masterdata synchronisatie. De voornaamste toevogeingen op de standaard werking van de msterdata sync:

- Synchronisatie tussen verschillende BC omgevingen (tenants)

- Meer geavanceerde regels qua synchronisatie:

  - Vertalingen van een bedrijf naar een ander

  - Uitgebreidere validatie & trigger van goedkeuringsflows

- Mogelijkheid om samengestelde tabellen te synchen: vb artikel artikelcategorie, artikel
attributen, artikeleenheden, verkoopprijslijst en inkooppprijslijst.

#### 1.3.2 Rapport- en documentparameters

##### 1.3.2.1 BS10.006 Verzendprofielen beheren
Verzendprofielen geven aan op welke wijze documenten worden afgeleverd aan klanten en leveranciers.

Per klant - leverancier kunt u een verzendprofiel toewijzen. In het verzendprofiel geeft u aan hoe documenten verzonden moeten worden.

U kunt ook aangeven welk verzendprofiel (bv. E-mail) als standaard verzendprofiel moet worden genomen indien er geen verzendprofiel is ingesteld voor een klant/leverancier.

#### 1.3.3 Resources

##### 1.3.3.1 BS10.005 Resources beheren
Een resource kan zowel een persoon zijn als een machine. Via de resourceplanning kunnen resources ingepland worden voor projecttaken, assemblageorders en serviceorders.

Resources kunnen ook verkocht of ingekocht worden op een order en/of factuur.

Op een resource kan de algemene kostprijs en verkoopprijs worden opgegeven.

##### 1.3.3.2 BC10.005.01 Beheren resource verkoopprijzen en kosten
Voor resources kunnen kostprijzen en verkoopprijzen op 2 niveaus bepaald worden:
- Via de resourcekaart

- Via de alternatieve resource kost- en verkoopprijzen

Op basis hiervan stelt het systeem de kostprijs/verkoopprijs voor in een bepaalde transactie.

Resourceprijzen kunnen worden ingesteld voor één specifieke resource, voor een resourcegroep of voor alle resources. Resourceprijzen kunnen per werksoort en in de gewenste valuta ingesteld worden. De resourceprijzen worden toegepast in verkoop, projecten en service.

Resourcekostprijzen kunnen worden ingesteld voor één specifieke resources, voor een resourcegroep of voor alle resources. Resourcekostprijzen worden ingesteld als een vaste kostprijs of indien er gebruik gemaakt wordt van werksoorten als een toeslag (percentage of vaste toeslag) boven op de ingestelde resourcekostprijs. De Resourcekostprijzen worden toegepast in verkoop, projecten en service.

#### 1.3.4 BS45.201 Artikeltracering
Via artikeltracering kan nagegaan worden waar en met welke hoeveelheid een artikel met tracering (lotnummers en/of serienummers) is ontvangen of geproduceerd, overgebracht, verkocht, verbruikt of geretourneerd is.

Op basis van de geregistreerde lotnummers tijdens de logistieke processen (aankoop, productie, transfer, verkoop) is het mogelijk om een tracering uit te voeren. Deze tracering is zowel voorwaarts als terugwaarts. Bij voorwaartse tracering wordt er vertrokken van de oorsprong van de goederen om dan te kijken naar wat er verbruikt is. Achterwaartse tracering vertrekt op zijn beurt vanaf het verbruik en kijkt naar de oorsprong van de goederen.

##### 1.3.4.1 BC45.201.01 Sublot management (Aptean)
https://fnbdocs.apteancloud.com/bc/SUL/contents/

Met de extensie sublot beheer is het mogelijk om een deel van een "parent" lot af te splitsen en een nieuwe sublot te creëren met een nieuw of bestaand lotnummer. Het sublot kan bijvoorbeeld worden gebruikt voor assemblage, productie of een andere transactie, los van het parent lot. Als er een nieuw lotnummer wordt toegewezen, wordt er een nieuwe lot informatie kaart aangemaakt.

#### 1.3.5 BS10.900 Advanced comments (Aptean)
https://fnbdocs.apteancloud.com/bc/ACM/contents/

Deze extensie biedt de mogelijkheid om extra informatie toe te voegen aan documenten om uitzonderingen of speciale informatie mee te delen aan gebruikers, verkopers en klanten. Er is de mogelijkheid om standaard verkoop- en inkoopcommentaren aan te maken die automatisch worden toegevoegd aan verkoop- en inkoopdocumenten wanneer deze worden aangemaakt. Een voorbeeld hiervan is bijvoorbeeld ‘vrolijk kerstfeest’ tijdens de feestdagen of een opmerking voor de magazijnmedewerker als ‘Vergeet niet een extra etiket toe te voegen’.nDeze standaard commentaren kunnen toegevoegd worden op zowel header niveau als op lijnniveau. Standaard opmerkingen op header niveau kunnen ingesteld worden voor:
- Alle klanten en leveranciers
- Een specifieke klant of leverancier
- Een specifieke klant of leverancier gecombineerd met een ship-to of order adres

Standaard commentaren op lijnniveau kunnen ingesteld worden voor:
- Alle artikelen
- Artikel categorie
- Specifiek artikel
Het is mogelijk om een notificatie te sturen naar een gebruiker wanneer er commentaren bestaan voor een bepaald document. Deze notificatie wordt weergegeven wanneer het document wordt geopend.

#### 1.3.6 BS10.901 Advanced attributes (Aptean)
Het hoofddoel van de ‘advanced attributes’ extensie is het mogelijk maken om gebruiker gedefinieerde attributen te koppelen aan artikelen, klanten, leveranciers en lotnummers. De extensie biedt de mogelijkheid om attributen verplicht te maken bij bepaalde artikelen, klanten, leveranciers en lotnummers. Zo kan er ook ingesteld worden dat maar een select aantal waardes van een attribuut mogelijk zijn voor een bepaald artikel, klant, leverancier en lotnummer. Deze attributen kunnen gebruikt worden voor informatie doeleinden, filteren en rapporteren. Ze kunnen zichtbaar gemaakt worden op inkomende en uitgaande documenten.

##### 1.3.6.1 BC10.901.01 Lot attributen
Deze extensie maakt het mogelijk om eigen gekozen attributen zoals bijvoorbeeld rijpheid of kwaliteit toe te wijzen aan een lotnummer. De functionaliteit om een lot attribuut sjabloon te creëren is ook aanwezig binnen deze extensie. Dit betekent dat elke keer wanneer er een nieuw lotnummer beschikbaar is voor een specifiek product, een vooringesteld aantal lot attributen ingevuld worden wanneer deze vaste waarden hebben. Dit is ook mogelijk per productgroep.

Er is een mogelijkheid om tot 8 lot attributen zichtbaar te maken op inkoop- & verkoopdocumenten zoals orders, return orders, facturen, offertes, credit nota’s en blanket orders. Dit zijn de globale lot attributen die zijn ingesteld op de advanced attributes setup. Deze globale attributen zijn zichtbaar op de lijnen.

##### 1.3.6.2 BC10.901.02 Audit trail
De ‘Audit trail’ geeft een historisch overzicht van de wijzigingen aan de lot attributen. Dit houdt details bij over de datum, tijd, gebruiker en type wijziging.

##### 1.3.6.3 BC10.901.03 Item attributen
Item attributen zijn ook een functionaliteit in standaard BC. Deze extensie breidt dit uit door vooropgestelde lot attributen met bijhorende waarden van een lot attribuut sjabloon te linken met een productcategorie code. Wanneer een item is toegewezen aan een productcategorie code, dan gaan de lot attributen die gelinkt zijn met deze productcategorie code worden overgenomen bij alle toekomstige lotnummers van dit item.

#### 1.3.7 BS10.903 Filter groups (Aptean)
Deze extensie maakt het mogelijk om meerdere filters in te stellen op een bepaalde tabel binnen BC en deze filterinstellingen op te slaan zodat ze gebruikt kunnen worden bij andere extensies. Het is mogelijk om meerdere filters in te stellen op de veldnummers die gekoppeld zijn aan het geselecteerde tabelnummer in de filter group header. Deze filterinstellingen worden toegepast wanneer de filtergroep wordt geselecteerd in bijvoorbeeld een status management flow.

#### 1.3.8 BS10.904 Status management (Aptean)
Vaak bieden de statusvelden van entiteiten in Microsoft Dynamics 365 Business Central onvoldoende ondersteuning voor complexe bedrijfsprocessen. Bijvoorbeeld, de status van een verkooporder kan alleen "Open" of "Vrijgegeven" zijn, terwijl er in werkelijkheid meerdere tussenstappen zijn voordat de order kan worden vrijgegeven, zoals controles op klantgelijkwaardigheid en vereiste documentatie. Hetzelfde geldt voor belangrijke mastergegevensrecords, zoals klanten en items, waarbij meerdere personen of rollen betrokken zijn voordat ze worden goedgekeurd voor gebruik in transacties. De extensie Statusbeheer biedt een oplossing door de mogelijkheid te bieden om flexibele definities van statussen te maken voor subsets van Business Central-entiteiten voordat ze algemeen worden vrijgegeven voor gebruik in het systeem. Per ondersteund recordtype (artikel, klant, productie stuklijst etc.) kunnen subsets worden gedefinieerd in de vorm van filtergroepen, waarna meerdere stadia per subset kunnen worden gedefinieerd. U kunt ook per status verplichte velden instellen en velden vergrendelen die vanuit eerdere statussen zijn ingevuld. Er bestaat ook een link met Dynamics 365 Business Central-toestemmingssets, waardoor het mogelijk is te definiëren welke gebruikers de record naar de volgende status mogen bevorderen. Naast de mogelijkheid om statussen toe te wijzen aan de gedefinieerde entiteiten, biedt de functionaliteit in de vorm van statusbeheerwaarschuwingen, statusbeheerlogboeken en een meldingssysteem de mogelijkheid om volledig aangepaste workflows te ontwerpen.

### 1.4 Relatiebeheer
Het domein "Relatiebeheer" omvat de processen die een bedrijf ondersteunen om haar interacties te managen met huidige en potentieel toekomstige klanten en leveranciers, de zogenaamde contacten. Deze module is een basis CRM module in BC.

Deze contacten kunnen geclassificeerd worden, er kunnen interacties geregistreerd worden en er kunnen taken gedefinieerd worden. Ook kunnen contacten opgedeeld worden in segmenten, en kunnen campagnes en opportuniteiten opgesteld worden.

#### 1.4.1 BS15.001 Relatiebeheer instellen
Deze scenario-variant omvat de beschrijving van de instellingen van het relatiebeheer. De algemene instellingen van het relatiebeheer worden binnen Dynamics 365 Business Central gemaakt in de marketinginstellingen.

#### 1.4.2 BS15.105 Contacten beheren
Alle externe entiteiten waarmee een zakelijke relatie wordt onderhouden (bijvoorbeeld klanten, potentiële klanten, leveranciers, advocaten en consultants), kunnen als contact worden geregistreerd. Als deze gegevens op één centrale locatie worden geregistreerd, kan elke afdeling in het bedrijf de informatie gebruiken. Ook kunnen er andere contact-gegevens bijgehouden worden zoals sectoren, mailinggroepen of andere belangrijke informatie die interessant kan zijn binnen het CRM-proces.

Contacten worden opgedeeld in:
- Bedrijven: Voor elke klant, leverancier en prospect kan een contact gemaakt worden. Klanten- en
leverancierscontactgegevens (als bedrijf) worden synchroon gehouden met de respectievelijke klanten- en leveranciersgegevens.

- Contactpersonen: Aan een bedrijfscontact kunnen één of meerdere contactpersonen worden
gekoppeld met hun eigen gegevens. Op die manier kunt u specifieke contactpersoon informatie bijhouden.

Sommige gegevens uit de contacttabellen zijn alleen geldig voor bedrijven of personen, andere gegevens zijn zowel geldig voor bedrijven als voor personen. Bij het aanmaken van een nieuw contact dient men aan te geven of het een nieuw bedrijf betreft of een nieuwe persoon die voor een bedrijf werkt dat al is vastgelegd als contact. Gegevens van een bedrijf worden automatisch bijgewerkt voor een persoon in dat bedrijf (indien het veld Overnemen is ingeschakeld in het venster Marketinginstellingen).

Contacten die niet meer nodig zijn in het systeem kunnen verwijderd worden indien er nog geen interactielogposten zijn aangemaakt voor het betreffende contact.

#### 1.4.3 BS15.201 Contacten classificeren
Het classificeren van een contact omvat het instellen van de functiegroepen, sectoren, zakenrelaties en mailinggroepen waartoe een contact behoort.

Contactenbedrijven kunnen geclassificeerd worden in verschillende soorten groepen:

- Sectoren

- Zakenrelaties

- Mailinggroepen

Contactenpersonen kunnen geclassificeerd worden in verschillende soorten groepen:

- Functiegroepen

- Mailinggroepen

- Sectoren

Voor contactpersonen kan bovendien ook de niveaucode binnen de organisatie ingesteld worden (bijv. CEO, financieel directeur, …).

#### 1.4.4 BS15.202 Profielvragenlijsten beheren
Profielvragenlijsten kunnen worden gebruikt voor het registreren van informatie over contacten. Binnen elke vragenlijst kunnen verschillende vragen ingesteld worden die u aan uw contacten wilt stellen.

Er kunnen ook vragenlijsten ingesteld worden om automatisch een aantal vragen te beantwoorden op basis van de contact-, klant- of leveranciersgegevens.

#### 1.4.5 BS15.203 Interacties registeren
Registratie van communicatie (e-mails, telefoongesprekken, afspraken) gestart vanuit BC of Outlook. Aan de hand van instellingen kan u ervoor zorgen dat het aanmaken van een document automatisch geregistreerd wordt in de interactielogposten.

U kunt activiteiten die u gedaan heeft voor een klant (klantenbezoek, workshop, evenement...) registeren als interactie. Bij het voltooien van deze activiteit-interactie wordt dit als interactie geregistreerd in de interactielogposten.

#### 1.4.6 BS15.209 Verkopers/Inkopers
Verkopers en inkopers kunnen worden geregistreerd in Business Central, naast de gewoonlijke gebruiker. De verkopers/inkopers functionaliteit in Business Central zorgt ervoor dat berekeningen van verkoopscommissies of bonussen sneller kan verlopen.

Een verkoper/inkoper kan worden gekoppeld aan een contact en/of klant, waarna deze wordt overgenomen op alle relevante records zoals orders, facturen, creditnota’s,…

#### 1.4.7 BS15.204 Taken beheren
Dit scenario behandelt het beheer van taken gekoppeld aan contacten, verkopers, campagnes, opportuniteiten of teams.

Afhankelijk van in welk venster u het taakvenster opent, kunnen taken voor contacten, verkopers, campagnes of teams aangemaakt worden. U kunt een start en einddatum (deadline) voor een taak op te geven. U heeft de mogelijkheid om taken te maken voor telefoongesprekken die u dient te voeren, algemene taken, of vergaderingen. Het is eveneens mogelijk om meerdere taken voor eenzelfde opportuniteit op een bepaald moment open te hebben. Bij afwezigheid kunnen de taken op uw naam, snel en eenvoudig worden gewijzigd naar een andere collega. Het is mogelijk om vanuit een verkoopofferte een aantal taken aan te maken die moeten uitgevoerd worden.

#### 1.4.8 BS15.205 Segmenten beheren
Dit scenario behandelt segmenten: het maken van selecties van contacten op basis van zelf te bepalen criteria.

Een segment is een selectie van een groep contacten op basis van specifieke criteria, bijvoorbeeld de contacten die behoren tot een bepaalde sector, of de contacten met een bepaalde zakenrelatie.

De hoofdtaken bij het aanmaken van segmenten zijn:
- Het aanvullen van de algemene informatie over het segment.
- Contacten toevoegen aan het segment op basis van geselecteerde criteria.

Segmenten kunnen gebruikt worden om een mailing te maken voor de contacten die in het segment zijn geselecteerd. Segmenten kunnen ook toegepast worden voor het selecteren van de doelgroep van campagnes, en voor de registratie van de respons op campagnes.

#### 1.4.9 BS15.206 Campagnes beheren
Een campagne kan toegepast worden voor alle soorten van activiteiten waarbij meerdere contacten betrokken zijn. Een belangrijk onderdeel van het opzetten van een campagne is het selecteren van de doelgroep voor uw campagne.

De campagnedoelgroep wordt geselecteerd d.m.v. het aanmaken van een segment. In dit segment kunnen alle contacten geselecteerd worden die gebruikt zullen worden in de campagne. Er kunnen voor een campagne specifieke prijzen en of kortingen worden ingesteld. Indien er specifieke campagneprijzen en of -kortingen werden ingesteld, dienen deze geactiveerd te worden vooraleer ze kunnen gebruikt worden.

Als u het segment aangemaakt heeft met als doel dat te gebruiken in een campagne, kan u het segment koppelen aan een campagne. Indien gewenst kunnen er taken gedefinieerd worden binnen de campagne.

Het eerder gemaakte segment kan gebruikt worden om een mailing (e-mail of afdruk) te versturen naar de contactpersonen in het segment.

Na het lanceren van de campagne volgt er respons van de contacten. Deze respons kan verwerkt worden binnen het segment venster.

1.4.10BS15.207 Opportuniteiten beheren Opportuniteiten kunnen in Dynamics 365 Business Central worden toegepast voor het opvolgen van het verkoopproces.

Opportuniteiten maken gebruik van vooraf bepaalde verkoopcycli, waaruit kan gekozen worden bij het aanmaken van een opportuniteit, met als doel het opvolgen van levenscyclus van lead tot een deal.

Telkens wanneer naar een volgende stap uit de verkoopcyclus wordt overgegaan, worden de wijzigingsdatum, de geschatte sluitdatum, geschatte waarde, voltooid % en slagingskans % geregistreerd. Hieruit worden de huidige waarde en het kans % berekend en geregistreerd, zodat de historiek van het verloop van het verkooptraject kan gevolgd worden. Tijdens de uitvoering van de verkoopcyclus kunnen op elk moment taken en interacties geregistreerd worden.

#### 1.4.11 BS15.208 Outlook integratie
https://learn.microsoft.com/nl-be/dynamics365/business-central/admin-outlook

De contacten en verkoopdocumenten (offertes, orders, facturen, creditnota’s, …) kunnen vanuit outlook aangemaakt en opgevolgd worden.

Zo kan wanneer je een e-mail ontvangt van een klant, je direct:

- Zien wie de klant is.

- Bekijken wat hun openstaande facturen, offertes of orders zijn

- Controleren of er nog betalingen of afspraken lopen

- Contacten en afspraken synchroniseren

- Nieuwe documenten aanmaken
