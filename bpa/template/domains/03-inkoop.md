## 3. Inkoop
Het domein "Inkoop" omvat de bedrijfsprocessen voor het opvolgen van aankopen van materialen of diensten die nodig zijn voor het uitvoeren van productie, of om aan een vraag van de klant naar goederen of diensten te voldoen.

Het gaat onder meer over het aanvragen van prijsoffertes, aanmaken en verwerken van inkooporders naar leveranciers, verwerken van ontvangsten, tot en met de inkoopfacturatie. De opvolging en afhandeling van de betaling van de inkoopfactuur wordt behandeld bij de financiële processen.

Procure to Pay omvat tevens het klachtenbeheer en de retouren.

Business Scenario's - BPA Proces Inkoop

Nieuw inkooporder aanmaken

Inkooporders: vastleggen van leveranciersafspraken

Een inkooporder legt de overeenkomst vast tussen een organisatie en een leverancier voor de aankoop van producten en/of diensten, onder vooraf bepaalde leverings- en betalingsvoorwaarden. Het vormt de basis voor de opvolging van het volledige inkoopproces.

Hoofding van het inkooporder

De algemene gegevens op de hoofding van een inkooporder worden standaard overgenomen van de leverancier (indien beschikbaar). Deze gegevens kunnen per inkooporder worden aangepast, zonder impact op de stamgegevens van de leverancier.

Leveranciersgegevens

- De leverancier waarmee de overeenkomst wordt gesloten, inclusief een eventuele contactpersoon.

- Het orderadres: dit kan gekozen worden uit de vooraf ingestelde adressen van de leverancier, of als
eenmalig adres worden ingevoerd. Hiermee wordt het adres geselecteerd (of ingevoerd) van waaruit men verwacht dat de leverancier de verzending zal organiseren.

- Facturatiegegevens: bepalen van welke leverancier men de factuur zal ontvangen. Dit kan de leverancier
zelf zijn, een andere leverancier, of een eenmalig aangepast betaaladres.

- Valutacode

- Betalingsvoorwaarde

Logistieke gegevens

- Verzendwijze (bijv. Incoterms)

- De locatie (magazijn) waar de goederen ontvangen zullen worden.

Intrastat-gegevens

- Voor statistische en douanedoeleinden, indien van toepassing.

Datumgegevens

- Belangrijke datums zoals orderdatum, verzochte ontvangstdatum en toegezegde ontvangstdatum.

Regels van het inkooporder

Een inkooporder bevat één of meerdere regels. Elke regel beschrijft een artikel of dienst die van de leverancier wordt aangekocht.

Soorten inkoopregels

- Opmerking

- Grootboekrekening

- Artikel

- Resource

- Vast activum

- Toeslag (artikel):

- Toewijzingsrekening: mogelijkheid om kosten te verdelen over meerdere grootboekrekeningen

Voor elke regel (behalve opmerkingen) moet een hoeveelheid worden ingevoerd.

Prijsbepaling

Voor artikelen en resources wordt de inkoopprijs en eventuele korting bepaald via een inkoopprijslijst of overgenomen van de artikelkaart. De eenheidsprijs en regelkorting kunnen handmatig worden aangepast indien nodig.

Orderbevestiging en status

Wanneer het inkooporder volledig is ingevuld, kan een order naar de leverancier worden verzonden (per e-mail of afgedrukt).

Indien de leverancier de ontvangstdatum bevestigd kan deze ook ingevoerd worden op het inkooporder.

Indien de leverancier dit meedeelt kan ook het ordernummer van de leverancier (het nummer dat het order toegekend kreeg in het systeem van de leverancier) geregistreerd worden op het inkooporder.

De laatste stap in het aanmaken van een inkooporder is het wijzigen van de status van Open naar één van de volgende:

- Vrijgegeven

- Wacht op goedkeuring

- Wacht op vooruitbetaling

Inkooporder wijzigen

Wijzigingen kunnen aangebracht worden op een bestaand inkooporder. Indien het inkooporder een andere status heeft dan Open, moet het eerst heropend worden. Na het aanbrengen van wijzigingen kan het nodig zijn om:

- Een nieuw order naar de leverancier te sturen.

- Een nieuwe goedkeuringsaanvraag te versturen (afhankelijk van de situatie).

- Een (bijkomende) vooruitbetalingsfactuur aan te maken.

Indien er wel al ontvangsten geregistreerd zijn, gelden er uiteraard bepaalde beperkingen over wat aangepast kan worden.

Ontvangsten ongedaan maken

Indien er toch wijzigingen nodig zijn op een inkooporder waarop al ontvangsten gebeurd zijn, is het mogelijk om één of meerdere ontvangsten ongedaan te maken, op voorwaarde dat deze nog niet gefactureerd zijn. Hierdoor worden de bijbehorende orderregels opnieuw bewerkbaar.

Inkooporder verwijderen Er zijn meerdere geldige redenen om een inkooporder te verwijderen in Business Central:

- Annulering door de leverancier
Wanneer een leverancier een order annuleert, kan het inkooporder verwijderd worden om de administratie op orde te houden.

- Administratieve correctie
Soms is het nodig om een inkooporder te verwijderen om het te vervangen door een nieuw order, bijvoorbeeld bij fouten in leveranciersgegevens, prijzen of leveringsvoorwaarden.

- Backorders en herstructurering
Wanneer artikelen niet beschikbaar zijn op de gewenste ontvangstdatum, ontstaat er een backorder. In sommige gevallen is het dan wenselijk om het bestaande order te verwijderen en de artikelen opnieuw toe te voegen aan een ander of nieuw inkooporder.

Voorwaarden voor het verwijderen van een inkooporder

Een inkooporder kan alleen verwijderd worden als aan de volgende voorwaarden is voldaan:

- Er zijn geen ontvangsten geregistreerd op het order.

- Als er ontvangsten zijn, moeten alle regels volledig gefactureerd zijn.

- Het order mag niet in een goedkeurings-workflow zitten.

- Er mogen geen vooruitbetalingsfacturen aan gekoppeld zijn.

Automatische verwijdering van inkooporders

Inkooporders kunnen automatisch verwijderd worden in de volgende scenario’s:

- Volledig ontvangen en gefactureerd via het inkooporder zelf
Wanneer men de actie Boeken → Ontvangen en factureren of Boeken → Factureren gebruikt, en alle regels zijn ontvangen en gefactureerd, wordt het inkooporder automatisch verwijderd.

- Facturatie via het inkooporderoverzicht of batchboeken
Ook bij het gebruik van Batchboeken of het selecteren van meerdere orders in het overzicht om te factureren, worden volledig afgewerkte inkooporders automatisch verwijderd.

Opmerking: Beide voorgaande methodes voor de facturatie van inkooporders worden in de praktijk zelden toegepast. De meest gebruikte methodes zijn factureren door ontvangstregels ophalen en automatische factuurverwerking met OCR of Peppol.

### 3.1 Inkoop instellen
#### 3.1.1 BS35.001 Inkoop instellen
https://learn.microsoft.com/nl-be/dynamics365/business-central/purchasing-setup-purchasing

De inkoopinstellingen bevatten een aantal algemene instellingen die gelden binnen het domein inkoop. Het gaat onder meer over hoe kortingen geboekt worden, welke afrondingen er toegepast worden, de instellingen van de nummerreeksen die voor de verschillende inkoop gerelateerde documenten worden gebruikt. Verder bevat de inkoopinstellingen ook de parameters voor het archiveren, het boeken in de achtergrond en de rekeningen voor elektronische documenten.

### 3.2 Inkoop master data
#### 3.2.1 BS35.100 Leveranciers beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/purchasing-how-register-new-vendors

Voor leveranciers kunt u algemene gegevens zoals naam, adres, land en diverse telefoonnummers, e- mailadressen etc. registreren. Ook kunnen er andere leveranciersgegevens bijgehouden worden zoals facturatie, ontvangst- en betalingsgegevens die belangrijk zijn binnen het inkoopproces.

Vanuit financieel oogpunt zijn volgende parameters van belang:
- Boekingsgroepen: zorgen voor een juiste sturing naar grootboekrekeningen (controlerekening,
omzet/kostenrekening, BTW rekening).
- Betalingscondities: bepalen de vervaldatum en contant korting
- Betalingswijze
- BTW nr., Ondernemingsnummer

De taalcode is van belang voor de document lay-out van inkoopdocumenten. Standaard wordt een lay-out voorzien in NLB, ENU, FRB.

#### 3.2.2 BS35.101 Inkoopprijzen beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/purchasing-how-record-purchase-price- discount-payment-agreements?tabs=current-experience

Inkoopprijzen worden gebruikt om de prijs te bepalen op inkoopdocumenten (meestal inkooporders). Inkoopprijzen kunnen worden ingesteld vanaf de leverancierskaart of vanaf de artikelkaart.

De inkoopprijzentabel bevat volgende kenmerken:
- Eenheid: geeft aan in welke eenheid (stuks, kg, karton, …) de prijzen zijn uitgedrukt
- Directe kostprijs: geeft de inkoopprijs aan, uitgedrukt in de eenheid die wordt ingesteld
- Minimum aantal: geeft aan dat de inkoopprijs geldig is vanaf een bepaald aantal (hiermee kunnen
staffelprijzen ingesteld worden).
- Begin- en einddatum: geeft de periode aan waarbinnen de prijs geldig is. Dit geeft de mogelijkheid om
nieuwe prijzen in te voeren die geldig zijn vanaf een bepaalde datum en biedt de mogelijkheid tot het raadplegen van de historiek van de inkoopprijzen.
- Variant
- Valutacode

#### 3.2.3 BS35.102 Inkoopkortingen beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/purchasing-how-record-purchase-price- discount-payment-agreements?tabs=current-experience

Inkoopkortingen kunnen zowel op de leverancier als op de artikelen worden ingesteld. Bij het instellen van een inkoopkorting koppel je aan een bepaalde leverancier voor een bepaald artikel een korting. Zodra een

inkooporder wordt opgesteld voor die artikel/leverancierscombinatie wordt de ingestelde korting automatisch toegepast.

Deze korting kan afhankelijk zijn van een aantal parameters zoals het bestelde aantal of de periode waarin de inkooporder wordt geplaatst.

#### 3.2.4 BS35.103 Artikeltoeslagen inkoop beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/payables-how-assign-item-charges

Artikeltoeslagen kunnen worden toegepast voor het berekenen van bepaalde kosten op orders, zoals transportkosten, administratiekosten, ... of voor het registeren van een inkoopvergoeding (bijvoorbeeld als tegemoetkoming voor een verkeerd geleverd of beschadigd product).

Artikeltoeslagen worden manueel toegevoegd op inkoopdocumenten.

Bij het gebruik van artikeltoeslagen moeten deze worden toegewezen aan andere inkoopontvangstregels (eventueel van andere documenten).

#### 3.2.5 BS35.104 Inkoopfactuurkortingen beheren
Inkoopfactuurkortingen zijn kortingen die gekoppeld worden aan een leverancier. Als er bij deze leverancier een inkooporder wordt geplaatst, dan zal de korting berekend worden op het totale bedrag. Een inkoopfactuurkorting wordt ingegeven als een percentage en kan verschillen afhankelijk van de ingestelde valuta.

#### 3.2.6 BS35.105 Inkoopbestellijsten beheren (purchase codes)
Bij sommige leveranciers worden facturen ontvangen die steeds gelijkaardige informatie bevatten. Vaak gaat het over documenten die slechts één regel bevatten, die steeds hetzelfde bedrag bevatten en steeds op dezelfde wijze geboekt worden (bv. huur van een gebouw).

Om het proces sneller te laten verlopen, is het mogelijk om standaard inkoopcodes aan te maken.

### 3.3 Inkoopoffertes beheren
#### 3.3.1 BS35.200 Inkoopoffertes beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/purchasing-how-request-quotes

Offerteaanvragen worden verzonden naar leveranciers om informatie te ontvangen over prijzen en levertijden. Inkoopoffertes kunnen worden omgezet in een inkooporder.

### 3.4 Inkoopraamcontracten beheren
#### 3.4.1 BS35.201 Inkoopraamcontracten beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/sales-how-to-create-blanket-sales-orders

Op een inkoopraamcontract worden de artikelen vastgelegd met de hoeveelheden die men bij een leverancier wenst af te nemen, tegen een afgesproken prijs. Vanaf een raamcontract kunnen inkooporders worden afgeroepen tot het volledige aantal van het raamcontract is voldaan. Bij elke afroep worden de prijzen en kortingen die op het raamcontract zijn ingesteld overgenomen naar de inkooporder.

De ingevoerde hoeveelheden op een raamcontract zijn niet van invloed op de artikelbeschikbaarheid zolang er geen inkooporders zijn voor aangemaakt. Op raamcontracten kunnen de afgeroepen hoeveelheden steeds geraadpleegd worden.

##### 3.4.1.1 BC35.201.01 Inkoopraamcontract afroepen vanuit inkooporder (Cegeka)
Deze functionaliteit zorgt er voor dat er bij het aanmaken van een inkooporder er melding gegeven wordt van bestaande inkoopraamcontracten, zodat men eenvoudig de bestaande raamcontracten kan gebruiken bij het aanmaken van een inkooporder.

### 3.5 Inkooporders beheren
#### 3.5.1 BS35.202 Inkooporders maken
https://learn.microsoft.com/nl-be/dynamics365/business-central/purchasing-how-record-purchases

Inkooporders leggen de overeenkomst met een leverancier vast om producten en/of diensten tegen bepaalde leverings- en betalingsvoorwaarden in te kopen. In dit scenario worden de verschillende methodes beschreven voor het aanmaken en opvolgen van inkooporders.

- Maak een inkooporder aan: De registratie van een bestelling bij een leverancier gebeurt door middel
van een inkooporder. Naast de algemene gegevens zoals het leveranciersnummer, het orderadres, de verzendwijze enz. wordt er geregistreerd welke artikelen met hun aantal en ontvangstdatum er gewenst zijn. Het vastleggen van de inkoopprijzen en eventuele toeslagen (transport en andere) is eveneens een essentieel onderdeel bij de opmaak van een inkooporder.
- Maak een inkooporder vanaf een raamcontract: Een inkoopraamcontract wordt gebruikt voor het
vastleggen van een bepaalde hoeveelheid artikelen tegen een afgesproken prijs. Vanaf een raamcontract kunnen meerdere inkooporders aangemaakt worden ("afroepen"), waarbij telkens het aantal kan gekozen worden, tot het volledige aantal van het raamcontract bereikt is.
- Maak een inkooporder vanaf een inkoopofferte: Een inkoopofferte wordt gebruikt voor het aanmaken
en opvolgen van een prijsaanvraag bij een leverancier. Wanneer het voorstel van de leverancier geaccepteerd wordt, kan de inkoopofferte worden omgezet naar een inkooporder.

##### 3.5.1.1 BC35.202.01 Vendor item catalog (Aptean)
https://fnbdocs.apteancloud.com/bc/VIC/contents/

De Vendor Item Catalog-extensie heeft als belangrijkste doel om op een snelle, gestructureerde en gecontroleerde manier inkooporders in te voeren. In de Vendor Item Catalog zijn verschillende combinaties van Item No. en Variant Code beschikbaar. Met behulp van deze instellingen kan een inkooporder worden gebruikt om de Purchase Item Catalog-pagina te openen en de bestelde hoeveelheden in te voeren. Zo zijn de artikelen zichtbaar die er bij een specifieke leverancier besteld kunnen worden. Het is hierbij enkel mogelijk om de hoeveelheden op een snelle manier in te vullen en deze om te zetten naar een inkooporder.

#### 3.5.2 BS25.203 Doorverzendingen en speciale orders
Zie ook verkoop: “BS25.203 Doorverzendingen en speciale orders”

Doorverzendingen en speciale orders zijn twee concepten om een bestelling van een klant rechtstreeks bij de leverancier te bestellen.

#### 3.5.3 BS35.204 Reserveer voorraad op een inkooporder
Zie 2.5.3 BS25.204 Reserveer voorraad op een verkooporder. Hierbij kan voorraad gereserveerd worden op bestaande voorraad of op bestaande inkooporders. Proces wordt gestart vanuit het verkooporder.

#### 3.5.4 BS35.205 Inkooporders ontvangen
https://learn.microsoft.com/nl-be/dynamics365/business-central/purchasing-how-record-purchases

Indien er geen nood is aan het beheren van de magazijnprocessen voor de ontvangst en opslag van de artikelen, kan een ontvangst rechtstreeks vanaf de inkooporder uitgevoerd worden.

Bijvoorbeeld:

- Eén persoon is verantwoordelijk voor zowel de orderadministratie als voor de magazijnadministratie
- Indien de magazijnprocessen eenvoudig zijn en er geen nood is aan real-time registratie

Indien er wel magazijnprocessen gebruikt worden in BC, zal de ontvangst gebeuren via deze magazijndocumenten. Zie BS50.204 Artikelen ontvangen.

#### 3.5.5 BS35.206 Beheer van backorders
Wanneer slechts een deel van de goederen in een order geleverd kan worden, dringt de keuze zich op wat er met de overige goederen dient te gebeuren:
- Annuleren
- Naleveren op een andere datum

##### 3.5.5.1 BC35.206.01 Beheer van backorders (Cegeka)
Via deze functionaliteit is het mogelijk om in te stellen op de leverancier of het toegelaten is om backorders bij te houden of niet. Indien het niet toegelaten is dan gaat deze functionaliteit ervoor zorgen dat deze gemakkelijk verwijderd kunnen worden. Dit kan belangrijk zijn aangezien orders die nog op 'te ontvangen' staan meegerekend worden in de berekening van de beschikbare voorraad.

#### 3.5.6 BS35.207 Inkooporders annuleren
Op voorwaarde dat er nog geen ontvangsten zijn geboekt voor de inkooporder kan de inkooporder steeds geannuleerd worden door het te verwijderen. Wanneer wel al ontvangsten geboekt zijn, moeten de ontvangstregels eerst ongedaan gemaakt worden en kan het order vervolgens verwijderd worden. Indien de ontvangst al gefactureerd is, moet een retourproces gestart worden.

#### 3.5.7 BS35.208 Verwerk Intercompany aankooporders
Zie ook BS25.208 Verwerk intercompany verkooporders

Wanneer een onderneming uit verschillende legale entiteiten (bedrijven) bestaat, en er tussen de bedrijven onderling verkoop- en inkooptransacties plaatsvinden, kan er gebruik gemaakt worden van intercompany (IC).

Indien intercompany is ingesteld tussen de verschillende bedrijven kan een verkooporder dat in het ene bedrijf is aangemaakt, worden omgezet naar een inkooporder in een ander bedrijf. In deze zin is dit dus het spiegelbeeld van intercompany verkooporders. Het belangrijkste doel van de IC module is om repetitieve orderingave te vereenvoudigen en zo fouten te vermijden.

Deze IC module kan in beide richtingen werken:

- Inkooporder van bedrijf A naar B (In B wordt het een verkooporder)

- Verkooporder van Bedrijf A naar B (In B wordt het een inkooporder)

#### 3.5.8 BS35.209 Goedkeuringsaanvraag verzenden
https://learn.microsoft.com/nl-be/dynamics365/business-central/walkthrough-setting-up-and-using-a- purchase-approval-workflow

In bepaalde situaties kan het voorvallen dat er een goedkeuring vereist is van een andere persoon alvorens er een inkooporder kan geboekt worden. Indien dit het geval is, stuurt de gebruiker een aanvraag tot goedkeuring naar de gebruiker die hierover kan beslissen. Die kan indien nodig ook op zijn beurt een goedkeuringsaanvraag versturen naar een andere bevoegde gebruiker. Dit kan via:

- Ingebouwde BC goedkeuringsstromen

- Power automate geïntegreerde goedkeuringsstromen

#### 3.5.9 BS35.210 Inkooporder goedkeuren
Elke goedkeurder heeft een overzicht van de door hem goed te keuren inkooporders. Een inkooporder kan goedgekeurd of geweigerd worden. Van zodra de inkooporder goedgekeurd is, krijgt het de status 'Vrijgegeven' en kan het geboekt worden.

#### 3.5.10 BS35.235 Inkoopontvangst ongedaan maken
https://learn.microsoft.com/nl-be/dynamics365/business-central/finance-how-reverse-journal-posting

Een ontvangst kan ongedaan gemaakt worden vanaf de geboekte inkoopontvangst. Hiervoor selecteert men de regel die ongedaan gedaan moeten worden en kies men de actie “Ontvangst ongedaan maken”. Enkel regels met soort “Artikel” kunnen ongedaan gemaakt worden. Door het ongedaan maken gaan de artikelen opnieuw uit voorraad.

### 3.6 Inkoopretourorders beheren
#### 3.6.1 BS35.217 Inkoopretourorders beheren
https://learn.microsoft.com/nl-be/dynamics365/business-central/purchasing-how-process-purchase-returns- cancellations

Inkoopretour orders stellen we op om goederen die in eerder stadium ontvangen zijn met een retourreden terug te sturen naar de leverancier middels een op te stellen document. In dit scenario wordt toegelicht hoe retourorders worden aanmaakt.

- Inkoopretourorders maken met fysieke verzending: Bij het verwerken van een inkoopretourorder met
fysieke verzending is het de bedoeling dat voor het afhandelen van de retour (om welke reden dan ook) de aangekochte artikelen terug moeten gestuurd worden naar de leverancier van herkomst. Het gevolg hiervan is dat er naast het inkoopretourorder ook een verzending moet geboekt worden.

- Inkoopretourorders maken zonder fysieke verzending: Bij het verwerken van een inkoopretourorder
zonder fysieke verzending is het de bedoeling dat voor het afhandelen van de retour (om welke reden dan ook) de aangekochte artikelen niet terug moeten gestuurd worden naar de leverancier van herkomst. In dit geval wordt geen gebruik gemaakt van artikelen, maar van artikeltoeslagen of grootboekrekeningen.

### 3.7 Document Lay-outs Inkoop
#### 3.7.1 BS35.800 Inkoopofferte
Microsoft Lay-out.

#### 3.7.2 BS35.801 Inkooporder
Cegeka Lay-out:

#### 3.7.3 BS35.802 Inkoopretourorder
Microsoft Lay-out.
