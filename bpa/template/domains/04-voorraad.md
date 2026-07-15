## 4. Voorraad
Het domein "Voorraad" omvat het beheer van de master data van artikelen, en de basisbewerkingen die te maken hebben met voorraadcorrecties, inventarisatie en het blokkeren van goederen.

### 4.1 Voorraad instellen
#### 4.1.1 BS50.001 Voorraad instellen
https://learn.microsoft.com/nl-be/dynamics365/business-central/inventory-setup-inventory

De voorraadinstellingen bevatten instellingen die algemeen gelden voor de voorraadtransacties in de applicatie:

- Instellingen met betrekking tot de integratie van de voorraadwaarde (al dan niet automatisch).
- Standaard in- en uitslagtijd.
- Negatieve voorraad voorkomen.
- Prompt om artikel te maken overslaan.
- Artikelbeschrijving kopiëren naar posten.
- Vestiging verplicht.
- Dimensiecode artikelgroep.
- Nummerreeksen (artikelnummers en reeksen voor voorraad-gerelateerde transacties).

### 4.2 Artikel master data
#### 4.2.1 BS50.100 Artikelen beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/inventory-how-register-new-items

Dit scenario behandelt het beheer (aanmaak, wijziging en uitgebruikname) van de verschillende types artikelen.
- Inkoopartikelen
- Verkoopartikelen
- Niet-voorraadartikelen
- Productieartikelen
- Assemblage artikelen
- Vervangartikelen
- "Bijkomende" artikelen

Merk op dat één artikel, tot meerdere types kan behoren: één artikel kan zowel inkoop & verkoopartikel zijn, productie & verkoopartikel, niet voorraad artikel & verkoopartikel, … De bovenstaande opties behandelen de verschillende masterdata die ingesteld wordt voor bepaalde types van artikelen.

##### 4.2.1.1 BC50.100.01 verkoopartikelen beheren
Deze variant behandelt het beheer van inkoop- & verkoopartikelen. Producten die worden aangekocht en/of verkocht, worden in Business Central vastgelegd in artikelkaarten. In de artikelkaart kunt u alle inkoop & verkoop- specifieke gegevens bijhouden betreffende het inkoopartikel.

Op het ogenblik dat een artikel niet meer actief gebruikt wordt, dan kan dit geblokkeerd worden. Op die manier kunnen er geen boekingen meer uitgevoerd worden op dit artikel.

Verder worden volgende aanvullende gegevens ingesteld vanaf de artikelkaart:

- Eenheden
  - Algemeen advies: maak de kleinste (fysieke) eenheid van het artikel de basiseenheid in BC Commented [NH3]: Iets wat men kan vastnemen en
- Dimensies verplaatsen, gram, kg, liter, meter, … zijn eenheden
maar zelden fysieke eenheden. Deze eenheden als ze
- Kruisverwijzingen gebruikt moeten worden voor facturatie worden best
via catch weight module opgevangen.
- Tekstuitbreiding
- Vertalingen
- Vervangingen
- Artikelleveranciers
- Vooruitbetalingspercentages (inkoop / verkoop)

- Aanvullingsmethode: inkoop vs productie

##### 4.2.1.2 BC50.100.02 inkoopartikelen beheren
Zie verkoopartikelen beheren

##### 4.2.1.3 BC50.100.03 Artikelen (service) beheren
Naast het gebruik van reguliere artikelen kunnen ook diensten gebruikt worden. Dit zijn artikelen die aangeduid zijn als "Service". Dit type artikelen wordt niet op voorraad gevoerd, maar hebben wel (bijna) alle mogelijkheden van de inkoop- en verkoopartikelen.

Opmerking: artikelen van klanten waarop service kan worden uitgevoerd, zoals een printer, installatie, … worden serviceartikelen genoemd in Business Central (<> artikel van type service). Serviceartikelen zijn iets anders dan reguliere artikelen van type service.

##### 4.2.1.4 BC50.100.04 Artikelen (niet-voorraad) beheren
Naast het gebruik van bovenstaande artikelen kunnen ook niet-voorraad-artikelen gebruikt worden. Dit zijn artikelen die aangeduid zijn als "Niet-voorraad". Dit type artikelen wordt niet op voorraad gevoerd. Artikelen van

het type “niet-voorraad” kunnen gebruikt worden in inkoop- en verkooptransacties en kunnen worden verbruikt op projecten, in service, assemblage en productie. Andere transacties zijn niet mogelijk met dit type artikelen.

Voor overzicht verschillende mogelijkheden voorraad vs niet -voorraad vs service

https://learn.microsoft.com/nl-be/dynamics365/business-central/inventory-about-item-types

##### 4.2.1.5 BC50.100.05 Productieartikelen beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/inventory-how-register-new-items#items- used-in-production-orders

Deze variant behandelt het beheer van productieartikelen. Om een productieproces op te zetten, dienen er aan de masterdata van de artikelen, die vaak ook verkoopartikelen zijn, extra gegevens toegevoegd te worden. De aanvullingsmethode van deze artikelen wordt ingesteld op “Prod. Order”. Verder zijn voor een productieorder de volgende velden van toepassing:

- Productiebeleid (op voorraad produceren / op order produceren)
- Bewerkingsplannummer
- Productiestuklijstnummer
- Afrondingsprecisie
- Afboekingsmethode (handmatig / voorwaarts / achterwaarts / pick + voorwaarts / pick + achterwaarts)
- Uitval %
- Lotgrootte

Op het ogenblik dat een artikel niet meer actief gebruikt wordt, dan kan dit geblokkeerd worden. Op die manier kunnen er geen boekingen meer uitgevoerd worden op dit artikel.

##### 4.2.1.6 BC50.100.06 Assemblageartikelen beheren
Assemblage wordt ook wel ooit omschreven als “light productie”. Om een assemblageproces op te zetten, dient er aan het artikel een assemblagestuklijst gekoppeld te worden. Daarin wordt vastgelegd welke componenten en bewerkingen (aan de hand van resources) nodig zijn om een product te assembleren. Verder wordt op het artikel het assemblagebeleid ingesteld (op voorraad assembleren / op order assembleren).

Op het ogenblik dat een artikel niet meer actief gebruikt wordt, dan kan dit geblokkeerd worden. Op die manier kunnen er geen boekingen meer uitgevoerd worden op dit artikel.

##### 4.2.1.7 BC50.100.07 Vervangartikelen beheren Commented [NH4]: Er bestaat en preview versie in
copilot om artikelvervangingen anders te doen: https://learn.microsoft.com/nl-be/dynamics365/business-central/inventory-how-register-new-items#set-up- https://learn.microsoft.com/nl- nl/dynamics365/business-central/suggest-item- item-substitutions substitutions-copilot#about-item-substitution- suggestions

Voor een artikel kan een vervangartikel ingesteld worden. Wanneer er bijvoorbeeld onvoldoende voorraad is, kan voor een artikel een vervangend artikel geselecteerd worden. Vervangartikelen kunnen worden toegepast op verkooporders en in de productieordermaterialen. In beide situaties is er een indicatie aanwezig dat er vervangartikelen beschikbaar zijn. Er kan ook aangegeven worden dat het artikel en het vervangartikel uitwisselbaar zijn. Verder kan er informatief nog een voorwaarde voor het vervangen van een artikel ingesteld worden.

##### 4.2.1.8 BC50.100.08 Verplicht gebruik eenheden of veelvouden van eenheden per klant
(Cegeka) Met deze functionaliteit kan er tegengegaan worden dat er verkopen in kleine hoeveelheden of verpakkingen worden gedaan. Op de klant wordt dan aangegeven in welke eenheden of veelvouden van eenheden de klant zijn goederen mag aankopen.

##### 4.2.1.9 BC50.100.09 Complementaire artikelen (Cegeka)
Bij de verkoop van een artikel is er soms de noodzaak een bijkomend artikel te verkopen (bv. bij koppelverkoop). Stel als je product A verkoopt, dan zal je ook product B willen verkopen. Door product A aan een verkooporder toe te voegen dient product B ook automatisch toegevoegd te worden.

Deze kunnen al dan niet als gratis worden toegevoegd.

##### 4.2.1.10 BC50.100.10 Recupel en Bebat beheren (Cegeka)
Recupel is een bijdrage bestemd voor het financieren van de recyclage van huishoudelijke toestellen.

Bebat is een bijdrage bestemd voor het financieren van de recyclage van batterijen.

Deze functionaliteit is ontwikkeld voor artikelen waarop Bebat en/of Recupel bijdragen van toepassing op zijn. Vanop de artikelkaart kunnen deze bijdragen ingesteld worden.

##### 4.2.1.11 BC50.100.11 Valipac en Fostplus beheren (Cegeka)
De Valipac en Fostplus aangiftes gaan respectievelijk over bedrijfsmatige en huishoudelijke verpakkingen die bedrijven op de markt brengen.

Deze functionaliteit voorziet in een vereenvoudigde verwerking voor de aangifte hiervan, op basis van aangiftes die bij de artikelen kunnen worden ingesteld.

#### 4.2.2 BS50.101 Stockkeeping units (SKU) beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/inventory-how-to-set-up-stockkeeping-units

SKU's vervangen de artikelkaart niet, ze zijn er een uitbreiding op. De SKU’s bevatten dezelfde parameters met betrekking tot aanvulling en planning als op de artikelkaart, maar kunnen per combinatie van vestiging en variant (indien van toepassing) ingesteld worden. Zo kan men bijvoorbeeld voor eenzelfde artikel per vestiging aangeven of ingekocht, getransfereerd (uit een andere vestiging) of geproduceerd moet worden.

#### 4.2.3 BS50.102 Artikelvarianten beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/inventory-item-variants

Soms is het aangewezen om te werken met varianten op een artikel. Hierbij kunnen kleine variaties in een artikel worden opgevangen (vb andere kleur, maat, …), zonder dat hiervoor een afzonderlijke artikelkaart dient aangemaakt te worden. Bijna alle gegevens van een artikel, kunnen ook beheerd worden per variant. Uitzonderingen hierop zijn artikelafbeeldingen, artikelomschrijving, artikelcategorie en artikelattributen.

#### 4.2.4 BS50.104 Artikeltraceringscodes beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/inventory-how-work-item-tracking

Binnen Business Central is het mogelijk om aan artikeltracering te doen vanaf het moment van binnenkomen tot het moment van verzending. Hiervoor worden serie- enof lotnummers gebruikt om de voorraad te traceren. Om deze tracering te doen, moet er op de artikelen aangegeven worden

- welke vorm van tracering er van toepassing is (lottracering, serienummertracering en/of pallettracering)

  - deze kunnen ook gecombineerd worden

- op welke transacties deze tracering moet ingegeven worden.

  - Inkomend

▪ Inkoop

▪ Verkoop

▪ Positieve correcties

▪ Negatieve correcties

▪ Productie

▪ Assemblage

  - Uitgaand: zelfde als bij inkomende transacties

Merk op:

1) de positieve en negatieve mutaties van een tracering worden alleen gecontroleerd of deze in balans zijn in BC als deze wordt gedaan op alle transacties. Als er 1 of meerdere transacties niet getraceerd worden, laat BC toe dat er meer uitgaande transacties zijn voor een bepaalde tracering dan inkomende.

Indien dit sluitend moet zijn, gebruiken we tracering op alle transacties (specifieke tracering)

2) Bovenstaande heeft alleen impact op de artikelposten: de transacties die zorgen voor positieve of negatieve voorraadbewegingen in het gehele bedrijf. Een nog gedetailleerdere tracering bestaat ook via de magazijntracering. Als deze actief is, moet men ook voor iedere interne verplaatsing, pick of opslag aangeven welke traceringscode verplaatst wordt. Op deze manier weet BC ook op ieder moment welk lot/pakket/serienummer op welke locatie ligt of heeft gelegen in BC. Commented [NH5]: Dit is misschien eerder technische kant, kan verwijderd worden als de klant meer 3) Tracering is voor kwaliteitsredenen soms vereist en soms gewenst, afhankelijk van de sector. Het is verward dan helpt om tracering uit te leggen. een heel erg krachtig hulpmiddel voor kwaliteitsopvolging. Maar al deze info moet wel worden ingegeven: manueel, via scanning of vanuit het systeem (vb automatisch toekennen lotnummer bij productieoutput). Dit kan arbeidsintensief zijn, en is ook de reden waarom specifieke tracering + magazijntracering niet de enige optie is in BC.

#### 4.2.5 BS50.115 Catalogusartikelen beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/inventory-how-work-nonstock-items

Catalogusartikelen kunnen toegepast worden voor artikelen die men wenst aan te bieden op verkoopoffertes of verkooporders, maar waar men op voorhand geen (volledig) artikel voor wenst aan te maken (wegens een te grote lijst artikelen om te beheren). Op het ogenblik dat een catalogusartikel wordt geselecteerd op een verkoopofferte of verkooporder wordt er automatisch een artikel aangemaakt, en moet de bijkomende info worden aangevuld.

#### 4.2.6 BS40.900 Catch weight (Aptean)
https://fnbdocs.apteancloud.com/bc/CAW/introduction/

In de voedingsindustrie kunnen producten zoals stukken vlees variëren in gewicht. Artikelen worden meestal verkocht per eenheid zoals een stuk vlees maar deze zijn geprijsd per gewichtseenheid (kg). Zo kunnen 10 stukken vlees tegen verschillende prijzen worden verkocht omdat elk stuk vlees een uniek gewicht heeft. Catch weight artikelen gebruiken 2 meeteenheden: een basiseenheid en een catch weight gewichtseenheid. De basismaateenheid kan standaard worden gebruikt bij de verkoop, ontvangst, overdracht, oogst en verzending van het product. De catch weight meeteenheid kan worden gebruikt wanneer het artikel ergens in het bedrijfsproces wordt gewogen zoals bij ontvangst, verzending en facturering. Voor de basiseenheid wordt het nominale of standaardgewicht gedefinieerd zodat gemakkelijk kan worden bepaald of een werkelijk geregistreerd gewicht binnen de tolerantie valt.

De Aptean Catch Weight-uitbreiding maakt het gebruik van Catch Weight-artikelen in de toeleveringsketen mogelijk, wat betekent dat transacties worden geregistreerd met een dubbele meeteenheid (bijvoorbeeld Stuks en KG). Hierdoor kunt u deze artikelen verwerken volgens een fysieke eenheid, maar ze prijzen volgens hun gewicht. Om deze extensie te kunnen gebruiken moet ‘Advanced pricing’ zijn geïnstalleerd. Commented [NH6]: Leuke feature, maar in praktijk nog maar zelfde zien toepassen. Voegt ook weinig echte functionaliteit toe.

### 4.3 Voorraad corrigeren
#### 4.3.1 BS50.200 Voorraad corrigeren
Om diverse redenen kan het nodig zijn om de voorraad in een magazijn te corrigeren.

Voor vestigingen zonder gestuurde opslag en pick kan een voorraadcorrectie uitgevoerd worden via het artikeldagboek door middel van een positieve of negatieve correctie. Deze correctie gebeurd altijd aan de kostprijs die op de artikelkaart staat.

Voor vestigingen met gestuurde opslag en pick kan een voorraadcorrectie uitgevoerd worden via het magazijn- artikeldagboek. Daarna moet deze logistieke aanpassing nog financieel verwerkt worden via het artikldagboek. Idee hierachter is dat magazijnier via magazijnartikeldagboek de aantallen corrigeert en dat finance via het artikeldagboek aangeeft aan welke waarde deze herwaardering moet gebeuren.

##### 4.3.1.1 BS50.233 Corrigeer stock met scanner (tasklet)
Er zijn verschillende redenen om de voorraad te corrigeren. Het kan bv. zijn dat de goederen in het magazijn onherstelbaar beschadigd zijn geraakt of dat ze verbruikt worden, zonder dat ze verkocht worden (denk bv. aan kartonnen verpakkingen).

Via de scanner kan dan een voorraadaanpassing gebeuren. Indien zo opgezet, moet ook een reden van de aanpassing ingegeven worden.

Let op: dit is verschillend van het maken van een inventaris, wat normaal een gestuurd proces is.

##### 4.3.1.2 BS50.234 Stocktelling met scanner (tasklet)
- Geplande stocktelling met scanner: Alhoewel normaal alle inkomende en uitgaande bewegingen in een
ERP-systeem worden geregistreerd, en de voorraad dus automatisch kan ge-update worden, is het toch nodig om periodiek te controleren of de voorraad in het ERP systeem de werkelijke voorraad weerspiegelt. Het is namelijk mogelijk dat deze kan afwijken door een teveel aan verbruik, verkeerde registratie door menselijke fouten of zelfs diefstal. Een dergelijke geplande telling wordt geïnitieerd vanuit het ERP-systeem. De berekende voorraad wordt dan vergeleken met de voorraad die op de scanner door de magazijnier werd ingegeven. Het verschil wordt dan als voorraadaanpassing geboekt.

- Ongeplande stocktelling met scanner: Een ongeplande stocktelling kan tussentijds worden uitgevoerd
voor bv. specifieke artikelen, of als er twijfel is of de inkomende en uitgaande bewegingen wel juist werden geregistreerd. Let er daarbij zeker op dat de in de op de scanner getoonde voorraad wel degelijk alle inkomende en uitgaande bewegingen verwerkt zijn. Afhankelijk van de magazijninstellingen, kan zich de situatie voordoen dat een picking fysisch al wel is gebeurd, maar nog niet in het systeem geregistreerd is. De magazijnier zit dan op de pickplaats geen voorraad meer liggen, en boekt de voorraad af. Als dan de picking ook geregistreerd wordt, is er een dubbele afboeking gebeurd.

### 4.4 Inventarisatie
#### 4.4.1 BS50.201 Inventarisatie
https://learn.microsoft.com/nl-be/dynamics365/business-central/inventory-how-count-inventory-with- documents

Op periodieke basis kan een stocktelling (inventarisatie) uitgevoerd worden, bijvoorbeeld op jaarlijkse basis.

Hiervoor wordt een overzicht opgemaakt van de berekende voorraad per artikel. Na het tellen van de fysiek aanwezige voorraad kunnen de getelde hoeveelheden ingevoerd worden. De verschillen tussen de berekende en getelde voorraad worden vervolgens bijgewerkt door middel van positieve of negatieve correcties.

Indien gebruik gemaakt wordt van mobiele apparaten (scanners) kan het inventarisatieproces vereenvoudigd worden en kan de telling via scanner geregistreerd worden.

- Periodieke inventarisatie uitvoeren: Aan de hand van voorraadtellingsperioden kunt u bepalen met
welke frequentie u fysieke stock van een artikel wenst te tellen. Op de voorraadtellingsperiode geeft men aan hoeveel keer per jaar de voorraad moet geteld worden, bijv. 1 x per jaar, 2 x per jaar enz. Per artikel of SKU kan een voorraadtellingsperiode ingesteld worden. Het inventarisatiedagboek bevat een functie voor het selecteren van de artikelen waarvoor op basis van de laatste telling en de ingestelde voorraadtellingsperiode een telling vereist is.
- Periodieke inventarisatie uitvoeren (gestuurde opsl. & pick): Aan de hand van voorraadtellingsperioden
kunt u bepalen met welke frequentie u fysieke stock van een artikel wenst te tellen. Op de voorraadtellingsperiode geeft men aan hoeveel keer per jaar de voorraad moet geteld worden, bijv. 1 x per jaar, 2 x per jaar enz. Per artikel of SKU kan een voorraadtellingsperiode ingesteld worden. Het magazijn-inventarisatiedagboek bevat een functie voor het selecteren van de artikelen waarvoor op basis van de laatste telling en de ingestelde voorraadtellingsperiode een telling vereist is. Nadat een inventarisatie is uitgevoerd in een magazijn-inventarisatiedagboek moet er een magazijnherwaardering berekend worden in een artikeldagboek (om de artikelposten in overeenstemming te brengen met de magazijnposten).
- Algemene inventarisatie uitvoeren (gestuurde opsl. & pick): Indien er geen gebruik gemaakt wordt van
voorraadtellingsperioden kan er op elk ogenblik een voorraadtelling uitgevoerd worden via een

magazijn-inventarisatiedagboek. Nadat een inventarisatie is uitgevoerd in een magazijn- inventarisatiedagboek moet er een magazijnherwaardering berekend worden in een artikeldagboek (om de artikelposten in overeenstemming te brengen met de magazijnposten).
- uitvoeren (inventarisatieorder): Met behulp van een inventarisatieorder en inventarisatie-
registratiedocumenten kan een specifieke inventarisatie van artikelen georganiseerd worden, bijvoorbeeld één inventarisatie per vestiging, per opslaglocatie. Het venster inventarisatieregistratie wordt gebruikt om de werkelijke telling van artikelen te communiceren en vast te leggen. Voor één inventarisatieorder kunnen meerdere registraties gemaakt worden, bijvoorbeeld om groepen artikelen naar verschillende werknemers te distribueren (de functie voor het aanmaken van de registraties voorziet in een optie voor het voorkomen van dubbele registraties, om dus te voorkomen dat artikelen dubbel geteld worden). Inventarisatieorders bieden ook de mogelijkheid om de regels te selecteren op basis van de voorraadtellingsperiode van artikelen.

### 4.5 Kwaliteit
#### 4.5.1 BS45.200 Artikelen blokkeren
https://learn.microsoft.com/nl-be/dynamics365/business-central/inventory-how-block-items

Artikelen kunnen geblokkeerd worden vanaf de artikelkaart. Er zijn 4 opties om een artikel te blokkeren:

- Geblokkeerd: alle transacties met het artikel worden geblokkeerd. Geblokkeerde artikelen worden
getoond in het algemeen artikeloverzicht, maar niet in opzoekvensters.
- Verkoop geblokkeerd: het artikel kan niet gebruikt worden op verkoopdocumenten (orders etc.). Voor
verkoop geblokkeerde artikelen worden niet getoond in opzoekvensters binnen verkoop.
- Inkoop geblokkeerd: het artikel kan niet gebruikt worden op inkoopdocumenten (orders etc.). Voor
inkoop geblokkeerde artikelen worden niet getoond in opzoekvensters binnen inkoop.

- Productie geblokkeerd: er kan geen productieoutput van het artikel geboekt worden of artikel kan niet
gekozen worden bij manuele creatie productieorder. Commented [NH7]: Kan wel in planningsvoorstel staan, maar misschien niet mogelijk om
##### 4.5.1.1 BC45.200.01 Artikelen blokkeren op lotniveau productieorder te maken vanuit planningsvoorstel?
In Business Central is het mogelijk om artikelen op lotniveau te blokkeren. Dit kan gedaan worden via de lotnummer-informatiekaart. Bij inkomende transacties (bijv. ontvangst op een inkooporder) kan de lotnummerinformatie aangemaakt worden via het venster artikeltraceringsregels. Indien er lotnummer- informatie aanwezig is, kan de lotnummer-informatiekaart geopend worden via Dril Down in het veld lotnummer in het venster artikelposten. Wanneer er bij de ontvangst van een artikel geen lotnummer-informatie is toegekend is het lastig om nadien de lotnummer-informatie toe te voegen. Indien men gebruik wenst te maken van de mogelijkheid om op lotniveau te blokkeren is het aangewezen om de lotnummerinformatie verplicht te maken via de instelling op de artikeltraceringscode.

##### 4.5.1.2 BC45.200.02 Artikelen blokkeren op opslaglocatie
In Business Central is het mogelijk om verplaatsingen vanuit een bepaalde opslaglocatie te blokkeren.

Dit kan vanaf het venster opslaglocaties (vanaf de vestigingskaart) of via venster opslaglocatie-inhoud.

Er kan gekozen worden om alle inkomende verplaatsingen, alle uitgaande verplaatsingen of beide te blokkeren.

##### 4.5.1.3 BC45.200.03 Inspection status (Aptean)
https://fnbdocs.apteancloud.com/bc/ISS/contents/

Met de inspectiestatus functionaliteit kunt u een lotnummer een inspectiestatus toekennen in de gehele (of een deel van de) goederenstroom door de organisatie. Per inspectiestatus kunnen één of meer uitgaande transactietypen (bv: verkoop pick, verkoop beschikbaarheid, productie consumptie pick, etc.) worden geblokkeerd.

Standaard wordt in BC de partijblokkering handmatig beheerd. De inspectiestatus van Aptean voegde in een paar gevallen de mogelijkheid toe om dit te automatiseren:
- Wijzig de inspectiestatus wanneer de vervaldatum (Verkoop) is verlopen via een taakwachtrij
- standaard inspectiestatus per triggertype (Quality Control triggers): bijv. inkoopontvangst,
retourontvangst verkoop, productie-output, …

Of op basis van het resultaat van de kwaliteitscontrole (zie Aptean QC-app) De kwaliteitstriggers (wanneer wordt een QC-controle getriggerd) kunnen worden ingesteld door: https://fnbdocs.apteancloud.com/bc/QCA/quality-control-triggers/ Field Code Changed
- Documenttype (Aankooporders/ontvangstbewijs, verkooporders/verzending, productieorder, ...)
- Documentactie: afhankelijk van het documenttype maar in het algemeen van het aanmaken of boeken
van het document, voor productieorders zijn er meer triggers (opstart tijdregistratie, periodiek, op basis van output qty, ...)
- Op locatie
- Type kwaliteitscontrole: per artikel, artikelkenmerk of algemeen
- Brontype: voor specifieke of alle leveranciers- of leverancierskenmerken, voor specifieke of alle klant-
of klantkenmerken, voor afdelingen (productie)

De kwaliteitstriggers maken vervolgens kwaliteitscontroleplannen, de daadwerkelijke kwaliteitsmetingen die door het toegewezen team moeten worden uitgevoerd.

##### 4.5.1.4 BC45.200.08 Levenscyclus artikelen beheren (Cegeka)
Met deze functionaliteit wordt de flexibiliteit van artikelen blokkeren verhoogd. Het is mogelijk om artikelen te blokkeren voor bepaalde documenten/functies. De volgende blokkeringen zijn mogelijk:
- Ingeven op verkoopoffertes
- Ingeven op verkooporders
- Ingeven op verkoopretourorders
- Boeken van verkoopverzending
- Boeken van verkoopretourontvangst
- Ingeven van inkoopoffertes
- Ingeven van inkooporders
- Ingeven van inkoopretourorders
- Boeken van inkoopfactuur
- Boeken van inkoopretourverzending

##### 4.5.1.5 BC45.200.04 Quality Control Plan
https://fnbdocs.apteancloud.com/bc/QCA/quality-control-plans/

Een kwaliteitsactieplan bepaalt welke kwaliteitscontroles moeten worden uitgevoerd. In het QC-plan kunnen één of meerdere metingen/kwaliteitscontrolevragen worden ingesteld.

Elk van deze metingen kan doelen opleveren, met een onder- en een bovengrens, eventueel gecombineerd met een waarschuwingsbereik.

En op basis van de antwoorden op de kwaliteitsvragen zal het plan slagen of mislukken. Op basis van de slagen of falen kan de inspectiestatus van de partij automatisch worden gewijzigd in een specifieke waarde.

Wanneer de antwoorden op de kwaliteitscontrolevragen afwijken van het opgegeven doelbereik, wat resulteert in een 'Fail', worden de kwaliteitscontroleacties gemaakt.

##### 4.5.1.6 BC45.200.05 Quality Control Action plans
De kwaliteitscontroleacties worden automatisch gemaakt wanneer een kwaliteitscontrole mislukt op basis van het actieplan voor kwaliteitscontrole dat oorspronkelijk was toegewezen aan de kwaliteitscontroleplanregel. Wanneer de kwaliteitscontrole mislukt, moet de gebruiker van de kwaliteitscontrole een kwaliteitscontroleactie initiëren en voltooien, een reeks vragen en taken voor het kwaliteitsteam. Elk van deze vragen of taken kan ook een vervaldatum krijgen, die aangeeft binnen hoeveel tijd het plan moet zijn voltooid.

##### 4.5.1.7 BC45.200.07 Quality control app (Aptean)
https://fnbdocs.apteancloud.com/bc/QCA/introduction/ Field Code Changed

The quality control app is een user interface die the onderdelen hierboven toepast, met als resultaat kwaliteitschecks en/of kwaliteitsacties. Op basis van de instellingen van de kwaliteitschecks en kwaliteitsacties, wordt er een taak aangemaakt in BC en getoond op deze app. Deze wordt dan automatisch aan het ingestelde team toegewezen.

De gebruikers kunnen dan via een terminal op de werkvloer, ontvangst- of verzendzone deze acties uitvoeren. Via de interface krijgen ze de kwaliteitschecks aangeboden en kunnen ze de nodige registraties doen. Daarnaast biedt de app mogelijkheden om foto’s, opmerkingen of attachments toe te voegen om de meting te ondersteunen.

Zoals hierboven aangehaald, zal het falen van een kwaleitscheck leiden tot een kwaliteitsactie. Indien gewenst, zal de inspectiestatus van het artikel ook aangepast worden op basis van het resultaat van de kwaliteitscheck. Het maken van een dergelijke QC-actie of het wijzigen van de inspectiestatus van een partij kan ook een e-mail of teambericht naar het betreffende QC-team activeren, door business central te combineren met een Power Automate-stroom. Opmerking: de kwaliteitscontrole app is ook geïntegreerd met de winkelvloer app. Voor kwaliteitscontroles die gekoppeld zijn aan productieorderwerkcentra, kunnen de kwaliteitscontroles worden uitgevoerd via de

shopfloor-app.

#### 4.5.2 BS45.901 Compliance documents (Aptean) Commented [NH8]: Waar hoort dit beter onder? Is
wel los gelinkt met voorraad of quality? Op de pagina compliance documents kunt u alle typen compliance documenten instellen, zodat deze later kunnen worden gebruikt bij het maken van deze documenten voor bedrijven, leveranciers, klanten, artikelen, inkoopnalevingsdocumenten of verkoopnalevingsdocumenten. Deze documenten kunnen verschillende doeleinden dienen, zoals een douanedocument, een kwaliteitsdocument met of zonder certificaat, of een geldig transportdocument. Het is mogelijk om een vervaldatum aan deze documenten toe te voegen. Deze extensie geeft inzicht in verlopen nalevingsdocumenten die worden gebruikt in het inkooporderproces en documenten die binnen een bepaalde periode vervallen. Voor elk nalevingsdocument moet u aangeven of het nodig is om een controle uit te voeren tijdens het aan- en verkoopproces. Wanneer deze controle is ingeschakeld, controleert het systeem tijdens het proces of het nalevingsdocument is goedgekeurd. Als het document nog niet is goedgekeurd, zal het systeem de gebruiker informeren om het nalevingsdocument goed te keuren voordat hij/zij verder kan gaan met de verwerking van het document (in het geval dat het nalevingsdocument van toepassing is op dit inkoop- en verkoopdocument op basis van het artikelnummer en de attributen)..

##### 4.5.2.1 BC45.901.01 Document link (Aptean)
https://fnbdocs.apteancloud.com/bc/DCL/09-dil_import/

Met deze extensie is het mogelijk om allerlei soorten documenten en bijlagen te koppelen aan Microsoft Dynamics 365 Business Central entiteiten (bijvoorbeeld compliance documenten) en deze documenten buiten Business Central opslaan met behulp van Azure Storage.

#### 4.5.3 BS45.902 Expiration management (Aptean)
https://fnbdocs.apteancloud.com/bc/EXM/contents/

Loten kunnen een vervaldatum hebben in BC als een vervaldatum vereistis op basis van de traceringscode van BC. Maar in de standaard BC wordt deze datum beperkt gebruikt. Het kan alleen worden gebruikt om verkooptransacties met een vervaldatum te voorkomen en te helpen bij het picken volgens FEFO.

Deze extensie van Aptean heeft extra functies toegevoegd aan de geregistreerde vervaldata.

- Berekening van de vervaldatum: Met de extensie Expiration Management kunt u
informatieve datums berekenen die verband houden met de vervaldatum van een partij. Met deze functie kunnen gebruikers de houdbaarheidsdatum bepalen op basis van specifieke criteria, zoals productiedatum, houdbaarheid of andere factoren.

- FEFO-inventarisvereiste: De module faciliteert ook de naleving van de First-Expired-First-
Out (FEFO)-inventarisvereiste. Standaard BC kan helpen bij het plukken volgens FEFO. Aptean breidt dit uit door aanvullende eisen te stellen met betrekking tot de houdbaarheid, zowel voor inkoop- als voor verkoopstromen. De houdbaarheid kan per verkoper en klant per artikel worden ingesteld. Standaard BC biedt de mogelijkheid om artikelen te picken met behulp van FEFO (First Expired First Out). Deze uitbreiding bouwt daarop voort door de uitsluiting mogelijk te maken van lotnummers die niet voldoen aan de eis met betrekking tot minimale houdbaarheid (hoe lang een product in de schappen te koop mag worden aangeboden voordat het houdbaar is).

Let op: de houdbaarheidsvereiste genereert alleen waarschuwingen, het zal gebruikers nooit blokkeren om loten te kiezen die niet aan de minimale houdbaarheid voldoen. Het zal wel de voorgestelde loten wijzigen op basis van een keuze, om ervoor te zorgen dat de minimale houdbaarheid wordt gerespecteerd.

Dit kan ertoe leiden dat het systeem niet altijd de oudste partijen kiest.

- Wijzig de inspectiestatus voor verlopen loten: loten met een vervaldatum (of bijna
vervallen) worden niet automatisch geblokkeerd in BC. Aptean biedt een taak die de inspectiestatus van deze loten kan wijzigen.

#### 4.5.4 BS45.904 Lot management (Aptean)
https://fnbdocs.apteancloud.com/bc/LMT/contents/

De lot management extensie maakt het mogelijk om automatisch samengestelde lotnummers te genereren via lotnummerprofielen. De bijbehorende informatie kan eenvoudig opgezocht worden in de lotnummerinformatie lijst.

Via de lotnummer profielen is het mogelijk om lotnummers te creëren met verschillende elementen zoals een (verval)datum, leverancier element, document nummer, itemnummer, machinenummer etc. Ook kan er een maximumaantal tekens ingesteld worden voor lotnummers. Dit om compatibel te zijn met bv externe systemen.

#### 4.5.5 BS45.905 Non conformances

##### 4.5.5.1 BC45.905.01 Non Conforomances (Aptean)
https://fnbdocs.apteancloud.com/bc/NCF/contents/

De non-conformiteit functionaliteit maakt het mogelijk om klachten te registreren en op te volgen. De klachten kunnen voor

- Verkoop: non-conformiteit van de klant

- Aankoop: leverancier non-conformiteit

- Algemeen: Interne non-conformiteit

De non-conformiteiten kunnen worden gecategoriseerd in verschillende categorieën (te kiezen door de klant). De non-conformiteit kan handmatig worden gemaakt of door een actie waarbij de non-conformiteit wordt gemaakt op basis van geboekte documentregels (verzendingen voor verkoop, ontvangstbewijzen voor aankoop). Het non-conformiteitsdocument kan worden verrijkt met externe documentnummers, bijlagen, opmerkingen en andere relevante gegevens. Voor een non-conformiteit kunnen er ook vervolgacties worden aangemaakt. Deze vervolgacties kunnen worden aangemaakt op basis van de non-conformiteitscategorie/subcategorie.

##### 4.5.5.2 BC45.905.02 Beheren klachten (Cegeka)
De functionaliteit voor het beheren van klachten is ontwikkeld om alle klachten vanuit een aparte centrale functie te kunnen behandelen. Klachtenbeheer is zo opgesteld dat het standaard mogelijk is om klachten te linken aan volgende documenten:
- verkoopoffertes
- verkooporders
- verkoopfacturen
- verkoopcreditnota's
- verkoopraamcontracten
- verkoopretourorders
- verkoopverzendingen
- inkoopoffertes
- inkooporders
- inkoopfacturen
- inkoopcreditnota's

- inkoopraamcontracten
- inkoopretourorders
- inkoopontvangsten
- geboekte verkoopfacturen
- geboekte verkoopcreditnota's
- geboekte inkoopfacturen
- geboekte inkoopcreditnota's

Met deze functionaliteit heb je de mogelijkheid om in het rollencentrum een overzicht te geven van de openstaande klachten en de acties die nog dienen genomen te worden om de klachten te verhelpen.

Oplossen klacht Het tabblad “Acties” op de klachtenkaart geeft de mogelijkheid om acties aan te maken waardoor de initiële klacht opgelost kan worden. Voorbeeld: Indien er een klacht was op een bepaald verkooporder kan onder deze tab een creditnota worden opgesteld om de klant tevreden te stellen. Er kan gekozen worden uit volgende standaard acties om een document te maken:

- Inkooporder
- Inkoopretourorder
- Inkoopcreditnota
- Verkooporder
- Verkoopretourorder
- Verkoopcreditnota

Afsluiten klacht Wanneer een klacht afgehandeld is kan deze afgesloten worden. Hiervoor kiest u de actie “Afsluiten”.

Er wordt ook geregistreerd door wie en op welk tijdstip (datum / tijd) de klacht werd afgesloten.

#### 4.5.6 BS45.906 Product specification (Aptean)
https://fnbdocs.apteancloud.com/bc/PRS/contents/

Door het aantal wetgevingen inzake voedselveiligheid en kwaliteit kan het beheer van productspecificaties en ingrediëntendeclaraties al snel complex worden voor de levensmiddelen- en drankenindustrie. De Aptean Product Specification for Food and Beverage app, met zijn robuuste instel-, berekenings- en rapporteringsmogelijkheden, maakt het mogelijk om naadloos productspecificaties te berekenen, te creëren en af te drukken. Gebruik de Aptean Product Specification app om productspecificaties te creëren voor de volgende klasse van items:

- Grondstoffen
- Halve producten
- Verpakkingsartikelen
- Eindproducten

Door de stuklijst-structuur te definiëren in de productiemodule, de geclassificeerde items te koppelen en de grondstof- en verpakkingsartikel specificaties in te voeren, kan de productspecificatie voor het halfproduct of het eindproduct worden berekend. Dit zijn enkele van de belangrijkste onderdelen van een productspecificatieverslag dat wordt gegenereerd met de Aptean Product Specification app:
- Algemene productinformatie
- Ingrediëntendeclaratie
- Voedingswaarden
- Allergenenverklaring LEDA
- Normen voor productspecificatie
- Productspecificatiemethoden
- Microbiologische grenswaarden
- Microwaarden voor besmetting
- Organoleptische eigenschappen
- CLITRAVI berekeningen
- Voedingsinformatie en keurmerken
- Verpakkingsgegevens
- Logistiek
- Opsporing en tracering

Het is eveneens mogelijk om specifieke informatie zoals ingrediënten, voedingswaarden en allergenen op etiketten af te drukken. Deze extensie maakt het mogelijk om de productspecificatiegegevens te definiëren, productspecificaties voor verschillende klassen van artikelen te creëren, het productspecificatieverslag af te drukken en de productspecificatieanalyse uit te voeren.
