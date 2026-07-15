## 12. Interfaces
12.1.1BS 95.002 EDI framework Het basisdoel van het framework is om vergaande functionaliteiten te bieden om een integratie maximaal te verschuiven van programmatie naar configuratie. Op deze manier kan op relatief korte termijn berichtuitwisseling opgezet worden. Ook toekomstige implementaties (nieuwe klanten of leveranciers) kunnen op basis van bestaande flows gekopieerd en aangepast worden.

##### 12.1.1.1 BC95.002.01 EDI inkomende berichten
Het integratieframework is ontworpen om berichten (zoals inkoopfacturen, verkooporders, inkooporders, artikelen, enz.) op een gestandaardiseerde manier te verwerken tussen externe systemen en Microsoft Dynamics 365 Business Central (BC). Hieronder de belangrijkste functionele aspecten:

1. Eén webservice voor alle berichten: Alle soorten berichten voor éénzelfde document worden via één
centrale webservice aangeboden aan BC. De URL-structuur bevat parameters voor tenant, omgeving en het bedrijf waarmee gecommuniceerd wordt.

2. Berichtstructuur en validatie: Elk inkomend bericht moet voldoen aan een vaste JSON-structuur, met
verplichte velden zoals partnercode en messagecode. Deze codes bepalen het type bericht en moeten vooraf geregistreerd zijn in BC (Partner Message list). Er zijn automatische controles op de structuur en inhoud van het bericht, inclusief validatie van verplichte velden en controle of waarden bestaan in BC (zoals een geldige taalcode).

3. Automatische verwerking en mapping: Het framework kan berichten automatisch verwerken en de
gegevens uit het JSON-bericht omzetten naar de juiste velden in BC-objecten (zoals klanten, verkoop- en inkoopdocumenten, dagboeken, artikelen). Voor standaardobjecten is deze verwerking grotendeels geautomatiseerd; voor maatwerkobjecten of -velden is aanpassing van de code nodig.

4. Inbox transacties en foutafhandeling: Elke succesvolle verwerking van een bericht resulteert in een
inbox transactie in BC, bestaande uit een header (met o.a. partnercode, messagecode, status, fouten) en het originele JSON-bericht. Validatiefouten worden volledig gelogd, zodat gebruikers eenvoudig alle fouten kunnen oplossen.

5. Postprocessing en flow fields: Na het inlezen van gegevens kan een extra proces in BC worden gestart
(zoals het vrijgeven of boeken van een order). Dit is niet instelbaar door de eindgebruiker, maar moet geprogrammeerd worden.

6. Flexibiliteit en uitbreidbaarheid: Het framework ondersteunt standaard JSON, maar kan via
maatwerk uitgebreid worden naar andere formaten (CSV, XML). Middleware kan berichten omzetten naar het juiste formaat voor BC.

##### 12.1.1.2 BC95.002.02 EDI uitgaande berichten
Naast inkomende berichten die data in BC gaan aanmaken, biedt het framework ook een oplossing voor uitgaande berichten naar andere partijen, zoals verkoopfacturen, inkooporders, DESADV, printopdrachten, …

De oplossing is ontworpen om in theorie iedere tabel met data van BC te kunnen exporteren in een gewenst formaat naar een klant of leverancier. In praktijk zal hier mogelijk een derde partij (Babelway, Descartes, …) tussen zitten die deze bestanden omvormt naar exact gewenste formaat voor de klant of leverancier (Vb EDIFACT formaat).

In praktijk bestaat de oplossing uit 7 onderdelen, die ervoor zorgen dat een divers aantal van mogelijkheden bestaan om bijna alle exportmogelijkheden af te dekken.

- 1. Mapping: Dit onderdeel dient voor het transformeren van de BC data naar een file formaat. Via de
mapping tools in BC, kan de gebruiker via een visuele hierarchie gegevens uit verschillende tabellen van BC combineren in 1 bericht. Daarnaast beschikt men over de mogelijkheid om transformatie uit te voeren (formatering, berekeningen & opzoeken van gelinkte data).

- 2. Filters & relaties: Dit onderdeel zorgt ervoor dat alleen de juiste data geëxporteerd wordt.
Bijvoorbeeld voor documenten dat alleen de regels van het juiste order geëxporteerd wordt, gecombineerd met enkel regels van type “item”.

- 3. Dynamische vertalingen: Via het framework kunnen op basis mappings, de bron data vertaald
worden naar ander waardes. Deze toegevoegde info kan op zijn beurt gebruikt worden om op een geautomatiseerde manier werkstromen aan te sturen. Vb:

  - Op basis van de klant, bericht naar een ander endpoint sturen

  - Op basis van artikelcategory, de file voor printing naar een ander printer sturen

- 4. Export formaat: De tool laat toe om de bestanden samengesteld in de mapping om te zetten een een
gewenst formaat. De standaard opties zijn: JSON, XML en CSV of TXT files. In combinatie met de mapping tool biedt ook dit een preview functionaliteit waardoor gebruikers snel en eenvoudig het gewenste resultaat kunnen controleren. Ook achteraf formaat aanpassen kan zo snel en eenvoudig gebeuren.

- 5. Endpoints & betrouwbaar multi-channel verzending: De berichten kunnen verstuurd worden naar
een API endpoint, folderstructuuur (Azure BLOB of lokale file storage), of via mail. Op deze manier kan

ieder bericht bezorgd worden op de meest geschikte manier. Daarnaast worden verschillende autenticatiemethodes ondersteund (OAuth2, Bearer tokens, API keys, Managed Identity, SAS tokens, certificates).

- 6. Versturen berichten op basis van events in ERP: De bestanden kunnen automatisch worden
aangemaakt op basis van instelbare triggers (vrijgave order, boeken van de verkoop verzending, …) of op basis van periodieke triggers (vb 1 x per uur).

- 7. Outbox beheer: Ieder uitgaand bericht wordt via een proces in BC verzonden en gelogd. Dit heeft als
doel op aflevering, visibiliteit, archivering en ondersteunen van audit trails voor compliance doeleinden en probleemoplossing.

Op deze manier kan men in BC alle uitgaande communicatie consulteren en bij eventuele fouten analyseren en eventueel bijstellen. Deze functionaliteit biedt ook de mogelijkheid om gefaalde berichten te analyseren, te verbeteren en eventueel opnieuw door te sturen. Hierdoor is een foutopvolging en rapportering van ieder bericht mogelijk.

#### 12.1.2 BC95.002.03 [andere EDI integraties]
[Uiteraard bestaan er diverse andere tools en mogelijkheden om de integraties te doen. Indien deze van toepassing zijn, kan dit hoofdstuk om de gewenste oplossing te beschrijven en documenteren.]
