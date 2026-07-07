## 5. Projectbeheer
Het domein "Projectbeheer" vult noden in voor bedrijven die project-georiënteerd werken en die de operationele en financiële opvolging van een project willen doen.

Het biedt ondersteuning voor:

- Projectmanagement taken, zoals het configureren van een project en de bijhorende work-breakdown
structure (WBS).
- Het inplannen van werknemers en materialen die nodig zijn bij de uitvoering van een project.
- De registratie van verbruikte materialen, werkuren en onkosten
- Het opstellen van het budget en opvolgen van budget vs actueel verbruik.
- Het maken en opvolgen van project-gerelateerde facturen en creditnota's.
- De opvolging van onderhanden werk (OHW of WIP work in progress).

Commented [CP9]: Flowchart die al op Teams stond, heb ik hier ingevoegd

Flowchart Progressus Commented [CP10]: Flowchart Progressus nog uitwerken + toevoegen

### 5.1 Projectbeheer instellen
#### 5.1.1 BS70.001 Projectbeheer instellen
https://learn.microsoft.com/en-us/dynamics365/business-central/projects-how-setup-jobs?tabs=current- experience#to-set-general-information-for-projects

In de projectinstellingen worden de algemene parameters, standaardwaarden en nummerreeksen van de project-gerelateerde functionaliteiten in Business Central ingesteld.

##### 5.1.1.1 BC70.001.01 Projectinstellingen (Progressus)
https://docs.progressussoftware.com/articles/Project_Setup.html#configure-progressus-project-setup

De “Projectinstellingen Progressus” bepalen de opzet en structuur van de parameters in een project, die het systeem gebruikt voor alle projectgerelateerde activiteiten (oa. budgettering, registratie uren en onkosten, facturering, WIP).

Volgende projectgerelateerde basisentiteiten kan men definiëren, waarna bruikbaar in project en/of projectgerelateerde registraties:

- Werksoorten: aanduiding van type werk, geleverde prestatie
(https://docs.progressussoftware.com/articles/Projects-Work_Types.html )

- Kostensoorten: aanduiding van type onkosten
(https://docs.progressussoftware.com/articles/Projects-Cost_Types.html )

- Projectcodes: de projectcodes zelf liggen vast (oa onderaannemingssoort, verzekeringsoort) en kunnen
niet gewijzigd worden, de waarden/subcategorie per projectcode zijn wel zelf te definiëren (https://docs.progressussoftware.com/articles/Projects-Project_Codes.html )

- Facturatiecyclussen: specificatie van facturatiefrequentie van een project
(https://docs.progressussoftware.com/articles/Projects-Billing_Cycle.html )

- Projectboekingsgroepen: per projectboekingsgroep instellen van een aantal grootboekrekeningen
waarop geboekt wordt bij bepaalde project activiteiten, minstens 1 projectboekingsgroep moet gedefineerd zijn (verplicht veld in projectdefinitie) (https://docs.progressussoftware.com/articles/Projects-Project_Posting_Groups.html )

#### 5.1.2 BS70.238 Projectsjablonen (Progressus)
Sjablonen worden gebruikt om:

- De productiviteit door hergebruik te verhogen

- Te zorgen voor consistentie in de organisatie

- De gebruikers in staat te stellen zelfstandig projecten op te zetten

Progressus Advanced Projects werkt bewust niet met het kopiëren van projecten om te voorkomen dat er onjuiste gegevens in projecten terecht komen.

Voor de volgende projectgerelateerde topics kan men sjablonen definiëren:

- Projectsjablonen
(https://docs.progressussoftware.com/articles/Projects-Project_Templates.html )

- Projecttaaksjablonen
(https://docs.progressussoftware.com/articles/Projects-Task_Templates.html )

- Factuurinstellingssjablonen
(https://docs.progressussoftware.com/articles/Projects-Invoice_Setup_Templates-v2.html )

- Verkoopprijssjablonen
(https://docs.progressussoftware.com/articles/Projects-Sales_Price_Templates.html )

- Sjablonen voor projectmachtigingen

#### 5.1.3 BS70.242 Projectcontractsjablonen (Progressus)
Ook voor de volgende projectcontract gerelateerde topics kan men sjablonen definiëren

- Contracttaaksjablonen
(https://docs.progressussoftware.com/articles/Contracts-Contracts_Task_Templates.html )

- Sjablonen voor contractfactuurinstellingen
(https://docs.progressussoftware.com/articles/Projects-Invoice_Setup_Templates- v2.html#invoice-setup-template-setup-for-projects-and-contracts )

#### 5.1.4 BS70.245 Budgetinstellingen (Progressus)
Volgende instellingen kan men definiëren op vlak van projectbudget:

- Budgetversies
(https://docs.progressussoftware.com/articles/Projects- Budget_Setup.html?q=budget%20setup#budget-versions )

- G/L budget integratie instellingen: koppeling tussen projectbudget en grootboekbudget

(https://docs.progressussoftware.com/articles/Projects- Budget_Setup.html?q=budget%20setup#gl-budget-integration-setup )

- Pipeline: indicatie van verwacht slagingspercentage, dit percentage wordt ook toegepast bij
grootboekintegratie (https://docs.progressussoftware.com/articles/Projects- Budget_Setup.html?q=budget%20setup#pipeline )

#### 5.1.5 BS70.248 Resource instellingen – algemeen
In resource-instellingen worden standaardinstellingen geconfigureerd op vlak van nummerreeksen en urenstaten.

##### 5.1.5.1 BC70.24801 Resource instellingen – algemeen (Progressus)
In resource-instellingen bij Progressus worden nog meer standaardinstellingen geconfigureerd in functie van Progressus functionaliteit. Deze extra setup is voornamelijk op vlak van specificatie tijdzone, uitschakelen bepaalde standaard BC functies voor resources, e-mail notificaties binnen ganse flow van urenstaat en onkostenregistratie.

Ook het configureren van projectresourceboekingsgroepinstellingen kan nodig zijn afhankelijk van gebruikte Progressus functionaliteit. In deze boekingsgroepinstellingen bepaalt men de correcte grootboekrekeningen.

https://docs.progressussoftware.com/articles/Resources- Project_Resource_Posting_Setup.html?q=resource%20posting%20setup

#### 5.1.6 BS70.249 Resource instellingen – ivm tijdsregistratie (Progressus)
In verband met tijdsregistratie zijn volgende instellingen, bouwstenen op te zetten:

- Werkregime (Norm Time): per werkregime instellen van normaal te presteren aantal uren
(https://docs.progressussoftware.com/articles/Resources-Norm_Time.html )

- Werkregime uitzonderingen (Norm Time Exceptions): instellen van uitzonderingen op een werkregime,
dit kan een algemene uitzondering zijn alsook specifiek in combinatie met resource – datum (vb wettelijke feestdag) (https://docs.progressussoftware.com/articles/Resources-Norm_Time_Exceptions.html )

- Werktijden: instellen van begin- en eindtijd per weekdag binnen een bepaalde werktijdcode
(https://docs.progressussoftware.com/articles/Resources-Norm_Working_Hours.html )

- Urenstaatconfiguraties: per configuratie stel je het werkregime in en ook heel wat parameters op vlak
van tijdsregistratie (periode, goedkeuringen, begindag voor werkweek), onkostenregistratie, e-mail verkeer ifv opvolging tijd- en onkostenregistratie (https://docs.progressussoftware.com/articles/Resources-Timesheet_Config_List.html )

- Factuur specificatie instellingen: definiëren van verschillende factuurspecificaties met instellen van
welke data, details moeten weergegeven worden op het specificatie rapport (= factuurbijlage met detail van tijd- en onkostenregistratie). (https://docs.progressussoftware.com/articles/Resources- Invoice_Resource_Specifications.html )

#### 5.1.7 BS70.253 Resource instellingen – ivm planning (Progressus)
In verband met planning zijn volgende instellingen, bouwstenen op te zetten:

- Resource kwalificatiesoorten: definiëren van verschillende soorten kwalificatiepunten
(https://docs.progressussoftware.com/articles/Resources- Qualifications_Types.html?q=qualification#qualifications-types )

- Werkpermissiesets: bepalen van permissies voor specifieke acties op werktoewijzingen, een resource
moet toegewezen worden aan 1 of meer werkpermissiesets om te kunnen ingrijpen op werktoewijzingen (https://docs.progressussoftware.com/articles/PP_budget-plan-work- permissions.html#work-permission-sets )

#### 5.1.8 BS70.257 Onkosten instellingen
In verband met onkosten zijn volgende instellingen, bouwstenen op te zetten:

- Projectkostenboekingsgroepinstellingen: instellen van grootboekrekeningen te gebruiken bij boekingen
in onkostenflow, maw per combinatie onkosten – betalingssoort en eventueel project(taak) specifiek (https://docs.progressussoftware.com/articles/Projects- Expense_Posting_Setup.html?q=expense )

- Onkosten betalingssoorten: bepalen hoe uitgaven worden betaald en verrekend (vb betaling door het
bedrijf, door werknemer) (https://docs.progressussoftware.com/articles/Projects- Expense_Payment_Types.html?q=expense )

- Kredietkaarten: instellen van informatie mbt kredietkaarten van het bedrijf en door welke resource in
gebruik (https://docs.progressussoftware.com/articles/Projects-Credit_Cards.html?q=credit%20ca )

#### 5.1.9 BS70.244 Dagboeksjabloon-batch instellingen
Om verschillende transacties (vb. artikelverbruik op project, tijdsregistratie goedkeuren en boeken) binnen de projectflow verder te verwerken, is er nood aan dagboeken en batches.

Opsomming van deze dagboek/batch-sjablonen:

- Projectdagboeksjabloon

(https://docs.progressussoftware.com/articles/Projects- Field Code Changed Project_Journals.html?q=journal%20template )

- Tijd-/kostendagboeksjablonen

(https://docs.progressussoftware.com/articles/Projects- Field Code Changed Time_Expense_Journal_Templates.html?q=journal%20template )

- Resourcedagboeksjablonen

(https://docs.progressussoftware.com/articles/Projects- Field Code Changed Resource_Journal_Template.html?q=journal%20template )

- Projectbudgetdagboeksjablonen

(https://docs.progressussoftware.com/articles/Projects- Field Code Changed Budget_Journals.html?q=journal%20template )

- Prognosedagboeksjablonen (= forecast dagboeksjablonen)

(https://docs.progressussoftware.com/articles/Projects- Field Code Changed Forecast_Journal_Templates.html?q=journal%20template )

- Verkoopprijsaanpassingssjablonen
(https://docs.progressussoftware.com/articles/Projects-Sales_Price_Update_Template.html )

### 5.2 Project master data
#### 5.2.1 BS70.200 Projecten maken
In de projectdefinitie maakt men onderscheid tussen:

- Algemene projectgegevens: projectnummer, projectomschrijving, order-/factuurklant, verzendadres,
boekingsgroep, OHW, projectmanager, status
- Takenlijst (WBS = Work Breakdown Structure): verschillende taken met hiërachiestructuur binnen het
project, per taak specificatie van taaknummer, omschrijving en parameters die algemene definitie op projectniveau overrulen, er is minstens één projecttaak nodig omdat alle registraties/boekingen naar een projecttaak moeten verwijzen

##### 5.2.1.1 BC70.200.01 Projecten maken – manueel
https://learn.microsoft.com/en-us/dynamics365/business-central/projects-how-create-jobs

De registratie van een project, zowel algemene projectgegevens als projecttaken, kan volledig manueel gebeuren.

##### 5.2.1.2 BC70.200.02 Projecten maken via kopiëren projecttaken
De registratie van een project kan ook door gebruik te maken van kopieerfunctie, zodat bestaande projectdefinities kunnen hergebruikt worden en manuele registratie kan beperkt worden.

##### 5.2.1.3 BC70.200.03 Projecten maken - manueel (Progressus)
https://docs.progressussoftware.com/articles/Projects-Create_Projects.html#how-to-create-a-project-card

https://docs.progressussoftware.com/articles/Projects-Create_Projects.html#how-to-create-tasks-for-a-project

In Progressus bestaat een projectdefinitie ook uit 2 niveau’s zoals in standaard BC, nl project en projecttaken, maar deze definities zijn nog veel uitgebreider.

##### 5.2.1.4 BC70.200.04 Project maken via wizard (Progressus)
https://docs.progressussoftware.com/articles/Projects-Create_Projects.html#create-a-project-using-project- wizard

Met de Create Project Wizard word je door verschillende stappen geleid om het project op te zetten, waarbij het aanbevolen is om zoveel mogelijk sjablonen te gebruiken (sjabloon voor project, projecttaken, facturatie- instelling, machtigingen).

##### 5.2.1.5 BC70.200.05 Project maken via Quick Guide (Progressus)
https://docs.progressussoftware.com/articles/Projects-Create_Projects.html#create-a-project-using-quick- project-guide

De Quick Guide werkt naar analogie met de Create Project Wizard, maar is veel minder uitgebreid en bevat dus minder stappen en opties.

##### 5.2.1.6 BC70.200.06 Project maken o.b.v. project(taak)sjabloon (Progressus)
https://docs.progressussoftware.com/articles/Projects-Create_Projects.html#create-tasks-from-template

Projecttaken kunnen manueel toegevoegd worden in een bestaand project met behulp van een projecttaaksjabloon.

#### 5.2.2 BS70.264 Projectgerelateerde masterdata (Progressus)

##### 5.2.2.1 BC70.264.01 Project facturatie-instelling
De facturatie-instelling op een project bepaalt hoe de inhoud van project(verkoop)factuurregels zal opgevuld en weergegeven worden. Het bepaalt deze inhoud op basis van wat gefactureerd wordt (artikelen, onkosten, geplande schijffacturatie, resources(groepen) en hoe gefilterd en/of gegroepeerd moet worden. Vaste rubrieken of teksten kunnen ook gespecificeerd worden in de facturatie-instelling.

In de facturatie-instelling op een project kan men de regels manueel aanmaken, via manueel ophalen van facturatie-instelling sjabloon of gekozen sjabloon toepassen bij projectaanmaak via wizard/quick guide.

##### 5.2.2.2 BC70.264.02 Project(taak) standaard dimensies
Er kunnen dimensies toegewezen worden aan een project en projecttaken. Net zoals in standaard Business Central zijn dimensies tags die toegewezen worden bij het boeken van (project)transacties. Deze dienen om het inzicht in de financiële data te vergroten en worden dus vooral ifv rapportering gebruikt.

##### 5.2.2.3 BC70.264.03 Project teamleden
Projectteamleden is een opsomming van de resources die meewerken in het project, met toewijzing van hun rol binnen het project.

##### 5.2.2.4 BC70.264.04 Project contactenlijst
De project contactenlijst bevat de contacten voor het project, met toewijzing van hun zakenrelatie (leverancier, onderaannemer) binnen het project.

##### 5.2.2.5 BC70.264.05 Project attributenlijst
https://docs.progressussoftware.com/articles/Projects-Project_Attributes.html?q=project%20attributes

Projectattributen kunnen worden gebruikt om op een eenvoudige manier informatie of specificaties mbt het project op te slaan en te beheren. Er kunnen meerdere projectattributen aangemaakt worden.

##### 5.2.2.6 BC70.264.06 Project milestones
https://docs.progressussoftware.com/articles/Processing-Milestone_Processing.html?q=milestone

Binnen een project kan men milestones definiëren en koppelen aan een projecttaak. De voortgang voor het bereiken van de milestone kan men ook registreren: voltooiings%, uitgesteld, geannuleerd, gereedgemeld.

Bij vaste prijs projecten kan het werken met milestones ook interessant zijn op vlak van facturatie. Wanneer een schijffacturatie gekoppeld is aan een projecttaak met een milestone, dan kan deze schijffacturatie pas verwerkt worden wanneer de milestone gereedgemeld is.

##### 5.2.2.7 BC70.264.07 Project machtigingen
Op een project kan men machtigingen instellen om bepaalde acties op dat project af te schermen:

- Voor het ganse project of een specifieke projecttaak

- Voor een resourcegroep of een specifieke resource

- Voor de acties: definiëren projecttaken, definiëren projectbudget, registreren tijd/onkosten,
goedkeuren tijd/onkosten

#### 5.2.3 BS70.276 Resource master data
https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-setup-resources#to-set-up-a- resource

https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-setup-resources#to-set-up-a- resource-group

Een resource definieert men zowel voor een persoon als voor een machine, dit onderscheid duidt men aan in de parameter “soort”. Een resourcedefinitie bestaat uit de volgende data: algemene gegevens (nr, naam,

basiseenheid), factureringsgegevens (standaard kostprijs/verkoopprijs, (BTW) productboekingsgroep) en eventueel ook persoonlijke gegevens. Standaard dimensies kan men instellen op een resource.

Men kan ook resourcegroepen definiëren, elke resourcegroep stelt een verzameling van resources voor (meestal met dezelfde bekwaamheden, vb ingenieur bouwkunde). Elke resource kan men toewijzen aan 1 resourcegroep.

##### 5.2.3.1 BC70.276.01 Resource definiëren (Progressus)
De resourcedefinitie in Progressus is uitgebreider dan in standaard BC. De extra gegevens zijn vooral op vlak van: aanduiding als projectmanager/project executive en/of externe resource (vb onderaannemer), sturing ifv registratie en goedkeuring urenstaat/onkostenstaat, sturing ifv toegang tot consulteren resource kost- /verkoopprijzen.

##### 5.2.3.2 BC70.276.02 Resourcesubgroep definiëren (Progressus)
https://docs.progressussoftware.com/articles/Resources- Resource_Groups_SubGroups.html?q=resource%20group

Progressus kent niet alleen de entiteit resourcegroep maar ook nog resourcesubgroep. Dit niveau van resourcesubgroep is eigenlijk nog een onderverdeling van resourcegroep en wordt in praktijk veelal gebruikt voor aanduiding junior, medior of senior profiel. Elke resource kan men toewijzen aan 1 resourcesubgroep van de toegewezen resourcegroep aan deze resource.

#### 5.2.4 BS70.100 Projectgerelateerde resourceprijzen beheren Commented [CP11]: Std BC prijslijsten functionaliteit
wordt verplicht te gebruiken (vanaf spring release https://learn.microsoft.com/en-us/dynamics365/business-central/across-prices-and-discounts 2026) => dus sowieso ook altijd al gebruiken in nieuwe implementaties (maw activatie van new sales prices in Het is mogelijk om voor resources project specifieke verkoopprijzen/kortingen te definiëren in project functiebeheer van BC) => in Progressus v12.8 is definiëren resourceprijzen afh van activatie new sales verkoopprijslijsten (standaard Business Central). Deze project specifieke verkoopprijzen/kortingen zijn geldig prices in functiebeheer van Progressus => bijgevolg binnen het project en overrulen dan de andere niveaus van resource verkoopprijs/korting definitie. hier nog wel aparte business case voor projspecifieke artikelprijzen Progressus Concept van resource verkoopprijzen/kortingen in project verkoopprijslijsten:

- Verkoopprijslijst toegewezen aan alle projecten/1 project/1 projecttaak en geldig voor 1 valuta + van
begin- tem einddatum

- Prijslijstregels met eenheidsprijs/regelkorting%/kostenfactor geldig voor combinatie resource(groep) +
werksoort + minimum aantal + eenheidscode

Definities in project verkoopprijslijsten overrulen dan de volgende niveaus:

- Specifieke resource verkoopprijs/korting = definities in verkoopprijslijst toegewezen aan alle klanten/1
klant/1 klantprijsgroep/1 klantkortingsgroep en geldig voor 1 valuta + van begin- tem einddatum

- Standaard resource verkoopprijs = eenheidsprijs gedefinieerd in resourcegroep/resource

##### 5.2.4.1 BC70.100.01 Project gerelateerde resourceprijzen beheren (Progressus)
In Progressus zijn er 2 mogelijkheden om project specifieke resourceprijzen te definiëren, dit afhankelijk van de instelling “Use new sales pricing experience for resources” in “Functiebeheer Progressus”.

Deze 2 mogelijkheden zijn:

- Igv “Use new sales pricing experience for resources” = “Ja” => functionaliteit van standaard BC project
verkoopprijslijsten, zie paragraaf BS70.100

- Igv “Use new sales pricing experience for resources” = “Nee” => functionaliteit van Progressus

Voor de project resource verkoopprijzen werkt Progressus Advanced Projects met een prijshiërarchie om de relevante verkoopprijs te gebruiken. Er kan een verkoopprijssjabloon (prijslijst) toegewezen zijn aan een project. De project resource verkoopprijzen kunnen worden geüpdatet, ofwel rechtstreeks in het project ofwel via het verkoopprijssjabloon.

https://docs.progressussoftware.com/articles/Resources-Setting_up_Resources.html#set-up- resource-prices

#### 5.2.5 BS70.272 Projectgerelateerde resource-kostprijzen beheren Commented [CP12]: Std BC prijslijsten functionaliteit
wordt verplicht te gebruiken (vanaf spring release https://learn.microsoft.com/en-us/dynamics365/business-central/across-prices-and-discounts 2026) => dus sowieso ook altijd al gebruiken in nieuwe implementaties (maw activatie van new sales prices in Het is mogelijk om voor resources project specifieke inkoopprijzen/kortingen te definiëren in project functiebeheer van BC) => in Progressus v12.8 is definiëren resourceprijzen afh van activatie new sales inkoopprijslijsten (standaard Business Central). Deze zijn geldig binnen het project en overrulen dan de andere prices in functiebeheer van Progressus => bijgevolg niveaus van resource inkoopprijs/korting definitie. hier nog wel aparte business case voor projspecifieke artikelkostprijzen Progressus

Concept van resource inkoopprijzen/kortingen in project inkoopprijslijsten:

- Inkoopprijslijst toegewezen aan alle projecten/1 project/1 projecttaak en geldig voor 1 valuta + van
begin- tem einddatum

- Prijslijstregels met kostprijs/regelkorting% geldig voor combinatie resource(groep) + werksoort +
minimum aantal + eenheidscode

Definities in project inkoopprijslijsten overrulen dan de volgende niveaus:

- Specifieke resource inkoopprijs/korting = definities in inkoopprijslijst toegewezen aan alle
leveranciers/1 leverancier en geldig voor 1 valuta + van begin- tem einddatum

- Standaard resource inkoopprijs = kostprijs gedefinieerd in resourcegroep/resource

##### 5.2.5.1 BC70.272.01 Projectgerelateerde resource-kostprijzen beheren
(Progressus) In Progressus zijn er 2 mogelijkheden om project specifieke resource-kostprijzen te definiëren, dit afhankelijk van de instelling “Use new sales pricing experience for resources” in “Functiebeheer Progressus”.

Deze 2 mogelijkheden zijn:

- Igv “Use new sales pricing experience for resources” = “Ja” => functionaliteit van standaard BC project
inkoopprijslijsten, zie paragraaf BS70.272

- Igv “Use new sales pricing experience for resources” = “Nee” => functionaliteit van Progressus

Ook voor de project resource kostprijzen werkt Progressus Advanced Projects met een hiërarchie om de relevante inkoopprijs te gebruiken. Hier wordt geen rekening gehouden met taken. Voor de rest wordt dezelfde logica gevolgd dan bij de verkoopprijzen.

De mogelijkheden die er bij de verkoopprijzen zijn om prijzen te updaten, bestaan niet voor kostprijzen.

https://docs.progressussoftware.com/articles/Resources-Setting_up_Resources.html#set-up- resource-costs

#### 5.2.6 BS70.101 Projectgerelateerde artikelprijzen beheren Commented [CP13]: Std BC prijslijsten functionaliteit
wordt verplicht te gebruiken (vanaf spring release https://learn.microsoft.com/en-us/dynamics365/business-central/across-prices-and-discounts 2026) => dus sowieso ook altijd al gebruiken in nieuwe implementaties (maw activatie van new sales prices in Het is mogelijk om voor artikelen project specifieke verkoopprijzen/kortingen te definiëren in project functiebeheer van BC) => Progressus werkt dan ook met std BC prijslijsten voor prijsbepaling van artikelen, verkoopprijslijsten (standaard Business Central). Deze project specifieke verkoopprijzen/kortingen zijn geldig dit onafhankelijk van activatie new sales prices in binnen het project en overrulen dan de andere niveaus van artikel verkoopprijs/korting definitie. functiebeheer van Progressus => bijgevolg ook geen aparte business case voor projspecifieke artikelprijzen Concept van artikel verkoopprijzen/kortingen in project verkoopprijslijsten: Progressus

- Verkoopprijslijst toegewezen aan alle projecten/1 project/1 projecttaak en geldig voor 1 valuta + van
begin- tem einddatum

- Prijslijstregels met eenheidsprijs/regelkorting%/kostenfactor geldig voor combinatie
artikel/artikelkortingsgroep + variant + minimum aantal + eenheidscode

Definities in project verkoopprijslijsten overrulen dan de volgende niveaus:

- Specifieke artikel verkoopprijs/korting = definities in verkoopprijslijst toegewezen aan alle klanten/1
klant/1 klantprijsgroep/1 klantkortingsgroep en geldig voor 1 valuta + van begin- tem einddatum

- Standaard artikel verkoopprijs = eenheidsprijs gedefinieerd in artikelkaart

#### 5.2.7 BS70.104 Projectgerelateerde artikelkostprijzen beheren Commented [CP14]: Std BC prijslijsten functionaliteit
wordt verplicht te gebruiken (vanaf spring release 2026) => dus sowieso ook altijd al gebruiken in nieuwe https://learn.microsoft.com/en-us/dynamics365/business-central/across-prices-and-discounts implementaties (maw activatie van new sales prices in functiebeheer van BC) => Progressus werkt dan ook Het is mogelijk om voor artikelen project specifieke inkoopprijzen/kortingen te definiëren in project met std BC prijslijsten voor kostprijsbepaling van inkoopprijslijsten (standaard Business Central). Deze zijn geldig binnen het project en overrulen dan de andere artikelen, dit onafhankelijk van activatie new sales prices in functiebeheer van Progressus => bijgevolg niveaus van artikel inkoopprijs/korting definitie. ook geen aparte business case voor projspecifieke artikelkostprijzen Progressus

Concept van artikel inkoopprijzen/kortingen in project inkoopprijslijsten:

- Inkoopprijslijst toegewezen aan alle projecten/1 project/1 projecttaak en geldig voor 1 valuta + van
begin- tem einddatum

- Prijslijstregels met kostprijs/regelkorting% geldig voor combinatie artikel/artikelkortingsgroep + variant
+ minimum aantal + eenheidscode

Definities in project inkoopprijslijsten overrulen dan de volgende niveaus:

- Specifieke artikel inkoopprijs/korting = definities in inkoopprijslijst toegewezen aan alle leveranciers/1
leverancier en geldig voor 1 valuta + van begin- tem einddatum

- Standaard artikel inkoopprijs = kostprijs gedefinieerd in artikelkaart

#### 5.2.8 BS70.275 Onkosten definiëren (Progressus)
Binnen een project kunnen er ook algemene onkosten gemaakt worden. In Progressus Advanced Projects kan men deze onkosten als masterdata definiëren in plaats van met grootboekrekeningen te werken.

Definitie van een onkosten is vrij eenvoudig:

- Algemene gegevens: unieke code, omschrijving, basiseenheid, kostensoort

- Prijzen: kostprijs, verkoopprijs met opties = idem kostprijs, surplus%, surplus bedrag, vast bedrag

- Facturatie: boekingsgroepen ifv sturing juiste grootboekrekeningen, koppelen van dimensiewaarden

#### 5.2.9 BS70.102 Projectgerelateerde diverse prijzen beheren
https://learn.microsoft.com/en-us/dynamics365/business-central/across-prices-and-discounts

Het is mogelijk om voor grootboekrekeningen project specifieke verkoopprijzen/kortingen te definiëren in project verkoopprijslijsten (standaard Business Central). Deze project specifieke verkoopprijzen/kortingen zijn geldig binnen het project en overrulen dan de andere niveaus van grootboekrekening verkoopprijs/korting definitie.

Concept van grootboekrekening verkoopprijzen/kortingen in project verkoopprijslijsten:

- Verkoopprijslijst toegewezen aan alle projecten/1 project/1 projecttaak en geldig voor 1 valuta + van
begin- tem einddatum

- Prijslijstregels met eenheidsprijs/regelkorting%/kostenfactor geldig voor combinatie
grootboekrekening + minimum aantal + eenheidscode

Definities in project verkoopprijslijsten overrulen dan de volgende niveaus:

- Specifieke artikel verkoopprijs/korting = definities in verkoopprijslijst toegewezen aan alle klanten/1
klant/1 klantprijsgroep/1 klantkortingsgroep en geldig voor 1 valuta + van begin- tem einddatum

- Standaard artikel verkoopprijs = eenheidsprijs gedefinieerd in artikelkaart

##### 5.2.9.1 BC70.102.01 Projectgerelateerde diverse kostprijzen beheren
https://learn.microsoft.com/en-us/dynamics365/business-central/across-prices-and-discounts

Het is mogelijk om voor grootboekrekeningen project specifieke inkoopprijzen/kortingen te definiëren in project inkoopprijslijsten (standaard Business Central). Deze zijn geldig binnen het project en overrulen dan de andere niveaus van grootboekrekening inkoopprijs/korting definitie.

Concept van grootboek inkoopprijzen/kortingen in project inkoopprijslijsten:

- Inkoopprijslijst toegewezen aan alle projecten/1 project/1 projecttaak en geldig voor 1 valuta + van
begin- tem einddatum

- Prijslijstregels met kostprijs/regelkorting% geldig voor combinatie grootboekrekenine + minimum
aantal + eenheidscode

Definities in project inkoopprijslijsten overrulen dan de volgende niveaus:

- Specifieke grootboekrekening inkoopprijs/korting = definities in inkoopprijslijst toegewezen aan alle
leveranciers/1 leverancier en geldig voor 1 valuta + van begin- tem einddatum

##### 5.2.9.2 BC70.102.02 Projectgerelateerde onkosten-prijzen beheren (Progressus)
https://docs.progressussoftware.com/articles/Projects-Expense_Prices.html?q=expense

Het is mogelijk om voor onkosten project specifieke verkoop- en kostprijzen te definiëren in Progressus Advanced Projects. Deze zijn geldig binnen het project en overrulen dan de standaard verkoop-/kostprijs geregistreerd in de onkosten-definitie.

Concept van project specifieke verkoop- en kostprijzen in project-onkosten-prijzen:

- Parameters die hiërarchie bepalen: project, projecttaak, begindatum, eenheid, valuta

- Definitie van kostprijs en daarbijhorende verkoopprijs (opties = idem kostprijs, surplus%, surplus vast
bedrag, vast bedrag)

##### 5.2.9.3 BC70.102.03 Projectgerelateerde onkosten-kostprijzen beheren
(Progressus) In Progressus Advanced Projects zit het beheer van kostprijzen en verkoopprijzen voor onkosten tezamen in zelfde definitie. Zie paragraaf BS70.102.01

Commented [CP15]: @Niels Habraken Verplaatst naar paragraaf “Project masterdata”
### 5.3 Projectbudgetten beheren Commented [CP16]: @Niels Habraken verplaatst naar
paragraaf “Project master data”
#### 5.3.1 BS70.203 Projectbudget beheren Commented [CP17]: @Niels Habraken verplaatst naar
aparte paragraaf ivm opening project https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-manage-budgets

In een project kan voor iedere taak een budget opgesteld worden. Dit budget bepaalt eigenlijk de ingeschatte behoeften en dus ook kosten, zowel voor resources als artikelen en diverse kosten. Het budget kan dan ook verder gebruikt worden in de operationele flow, vooral om resources in te plannen op het project. Aan de hand van het budget kan ook steeds gekeken worden naar hoeveel de geregistreerde verbruiken al ingenomen hebben van het vooropgestelde budget. Dit kan helpen om in de toekomst onderschatting van budgetten te vermijden.

Een projectbudget legt men manueel vast op het niveau van de projectplanningsregels van het project. Drie pijlers bepalen eigenlijk het budget: resources, artikelen, diverse kosten (grootboekrekening). Deze 3 soorten zijn ook aanwezig in de definitie van een projectplanningsregel. In het kader van projectbudget verwijst de regelsoort van de projectplanningsregel dan ook naar "budget" of "budget en factureerbaar". De som van deze budget verwijzende projectplanningsregels bepalen het totale projectbudget, uitgedrukt in kostprijs of verkoopprijs. Commented [CP18]: @Niels Habraken Kopieerfunctie bestaat niet Het herzien en herwerken van een projectbudget gebeurt op dezelfde manier als voor het initieel projectbudget. Men legt dit ook vast op niveau van projectplanningsregels: bestaande projectplanningsregels aanpassen en/of nieuwe projectplanningsregels toevoegen. Door eerst het project manueel te archiveren alvorens het projectbudget aan te passen, simuleert men op eenvoudige manier het bewaren van vorige budgetversies.

##### 5.3.1.1 BC70.203.01 Projectbudgetten beheren (Progressus)
https://docs.progressussoftware.com/articles/Manage_Project_Budgets.html#create-new-budget-versions

https://docs.progressussoftware.com/articles/Manage_Project_Budgets.html#create-a-budget

In Progressus Advanced Projects is het verplicht om met budgetversies te werken, maw elk project heeft minstens 1 budgetversie. Er is een onbeperkt aantal budgetversies op elk project mogelijk, waardoor verschillende berekening/inhoud voor elk projectbudget kan gecreëerd worden. Er kan maar 1 budgetversie actief staan op het project, maar een andere budgetversie actief zetten kan altijd doorheen ganse projectflow. De identificatiecode en benaming van een budgetversie definieert men in entiteit “budgetversie”.

Het projectbudget bepaalt eigenlijk de ingeschatte behoeften en dus ook kosten, zowel voor resources als artikelen en onkosten. Er zijn verschillende manieren om een projectbudget te definiëren, maar uiteindelijk zit de informatie in “budgetposten”.

Verschillende manieren om projectbudget te definiëren/wijzigen/beheren:

- Via budget matrix: invoerscherm met matrix waarin projecttaken op de rijen en periodes in de
kolommen, selectie van artikel/resource(sub/groep)/onkosten waarvoor budgetdefinitie (https://docs.progressussoftware.com/articles/Manage_Project_Budgets.html#budget-matrix )

  - Variant “agenda weergeven”: met extra matrix waarin agenda per resource weergegeven

  - Variant “capaciteit weergeven”: met extra matrix waarin resourcecapaciteit weergegeven

  - Variant “agenda + capaciteit weergeven”: met extra matrix waarin agenda per resource
weergegeven + extra matrix waarin resourcecapaciteit weergegeven

- Via budget matrix per resource: invoerscherm met matrix waarin resources op de rijen en periodes in
de kolommen, selectie van projecttaak waarvoor budgetdefinitie (https://docs.progressussoftware.com/articles/PP_budget-plan-matrix-by-resource.html )

  - Variant “agenda weergeven”: met extra matrix waarin agenda per resource weergegeven

  - Variant “capaciteit weergeven”: met extra matrix waarin resourcecapaciteit weergegeven

  - Variant “agenda + capaciteit weergeven”: met extra matrix waarin agenda per resource
weergegeven + extra matrix waarin resourcecapaciteit weergegeven

- Via budget herhalen: creatie van terugkerende budgetposten voor geselecteerde projecttaak met een
ingesteld interval (https://docs.progressussoftware.com/articles/Manage_Project_Budgets.html#budget- repeating )

- Via splitsen resourcegroepbudget: een budget dat gemaakt is op basis van een resourcegroep splitsen
naar specifieke resources (https://docs.progressussoftware.com/articles/Manage_Project_Budgets.html#to-split- resource-group-budget-to-individual-resources )

- Via kopiëren van ander project: gefilterde budgetposten kopiëren naar ander project/projecttaak
(https://docs.progressussoftware.com/articles/Manage_Project_Budgets.html#copy-budget- from-another-project )

- Via budgetposten overbrengen: gefilterde budgetposten transfereren naar ander project/projecttaak
(https://docs.progressussoftware.com/articles/Manage_Project_Budgets.html#transfer-a- budget )

- Via rolling budget: aanmaken nieuwe budgetversie op basis van vorige budgetversie en update met
actueel verbruik (https://docs.progressussoftware.com/articles/PP_budget-plan-rolling-budget.html )

- Via resource omwisselen: in gefilterde budgetposten resource(sub/groep) wijzigen
(https://docs.progressussoftware.com/articles/PP_budget-plan-swap-budget-resource.html)

- Via projectbudgetdagboek
(https://docs.progressussoftware.com/articles/Projects-Budget_Journals.html )

#### 5.3.2 BS70.288 Projectbudgetten goedkeuren (Progressus)
https://docs.progressussoftware.com/articles/Manage_Project_Budgets.html#project---budget-approvals

Goedkeuren van projectbudgetten is geen verplichte stap. In de projectdefinitie activeert men de budgetkeuring en benoemd men maximaal 3 goedkeurders in volgorde van goedkeuring.

Verschillende stappen in goedkeuringsflow van projectbudget:

- Definiëren van projectbudget

- Vrijgeven van projectbudget ter goedkeuring Commented [CP19]: Waar dit vrijgeven terugvinden ?
In project > budget > used budgetversions
- Goedkeuren of afkeuren van projectbudget (= ganse budget), door de verschillende opgegeven en
opeenvolgende goedkeurders in projectdefinitie

#### 5.3.3 BS70.294 Projectbudget syncen naar boekhouding (Progressus)
https://docs.progressussoftware.com/articles/Manage_Project_Budgets.html#gl-budget-integration

https://docs.progressussoftware.com/articles/Manage_Project_Budgets.html#update-gl-budget

In grootboek-budgetintegratie (GB-budgetintegratie) stel je per project de koppeling in tussen projectbudgetversie en grootboekbudget. Via de taak “budget bijwerken” start je het syncen van projectbudget naar grootboekbudget, filters op project en projectbudgetversie kunnen hierbij ingesteld worden. Bij dit syncen naar grootboekbudget wordt het percentage ingevuld in “pipeline” van het project toegepast op het projectbudget.

### 5.4 Project verkoopofferte
#### 5.4.1 BS70.295 Project verkoopofferte maken
Vanuit projectkaart kan men projectofferte weergeven of verzenden naar de klant, dit op basis van het standaard of geselecteerde rapportlay-out en de info in de projectplanningsregel ifv budgetbepaling (= met “regelsoort” = “budget” of “budget en factureerbaar”).

##### 5.4.1.1 BC70.295.01 Project verkoopofferte maken (Progressus)
https://docs.progressussoftware.com/articles/Manage_Project_Budgets.html#project-quote

Vanuit de projectkaart kan men via actie “projectofferte maken” het systeem een projectofferte als transactie laten aanmaken. Deze actie gebruikt hiervoor de info in de actieve budgetversie van het project en de facturatie- instelling van het project om de offerteregels op te bouwen. De projectofferte is dan eigenlijk een verkoopofferte met koppeling naar project, van waaruit de offerte documentlay-out kan worden verzonden/afgedrukt.

### 5.5 Project verkooporder
#### 5.5.1 BS70.296 Project verkooporderbevestiging maken (Progressus)
Indien je na goedkeuring van de projectofferte door de klant, ook nog een projectorderbevestiging moet versturen naar de klant, dan kan je deze verkoop(project)offerte (zie BC70.295.01) omzetten in een verkooporder en van daaruit dan de orderbevestiging documentlay-out versturen.

Wanneer je via normale projectfacturering werkt (maw vanuit het project ongeboekte verkoopfacturen aanmaken), dan gaat het verkooporder aangemaakt voor projectorderbevestiging niet verder verwerkt worden en kan men het gewoon archiveren om daarna te verwijderen.

### 5.6 Projectplanning
#### 5.6.1 BS70.205 Artikelen voor project plannen

https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-manage-project-supplies

De initieel budget gerelateerde projectplanningsregels kan men ifv de planning verder verfijnen en/of verder operationeel verwerken.De projectplanningsregels met soort "artikel" zijn het vertrekpunt voor de effectieve planning van artikelbehoefte. Deze regels leggen namelijk vast welk artikel, hoeveelheid en tegen welke datum.

Verfijnen van projectplanningsregels met soort “artikel” kan op verschillende manieren:

- Artikelen voor project plannen in projectplanningsregel

In deze flow registreert men de planning/behoefte van artikelen direct in de projectplanningsregel: specificatie van juiste artikel en aantal op voorziene verbruiksdatum (planningsdatum).

- Artikelen voor project plannen via projectplanningsregeldatum wijzigen

In een projectplanningsregel legt "planningsdatum" eigenlijk de concrete uitvoeringsdatum vast. Het kan nodig zijn om artikelen te herplannen en dus "planningsdatum" aan te passen. Via de actie “planningsregeldatums voor project wijzigen” kan men de planningsdatum wijzigen in één of meer projectplanningsregels. Manueel de planningsdatum in een projectplanningsregel aanpassen, is ook mogelijk.

De verdere operationele planning kan op verschillende manieren:

- Artikelen plannen voor project via project specifiek inkooporder (manueel)
Vanuit projectplanningsregel(s) of vanuit het project zelf kan men via functie “inkooporder maken” een Commented [CP20]: Functie uitvoeren vanuit project specifiek inkooporder maken. projectplanningsregel => systeem houdt geen rekening met aanwezige voorraad van het artikel Dit inkooporder is project specifiek door het koppelen van de inkooporderlijnen aan een project en Functie uitvoeren vanuit project (maw vanuit projecttaak. Net zoals in een gewoon inkooporder bepaalt ook hier "verzochte ontvangstdatum" de projectkaart zelf) => systeem houdt wel rekening met planning van de artikelbehoefte. aanwezige voorraad van het artikel

Dit inkooporder boeken voor ontvangst resulteert logistiek gezien in een nuloperatie (artikelpost voor ontvangst onmiddellijk vereffend met artikelpost voor verbruik), geen aanmaak van projectpost, geen update in projectplanningsregels, kost wel zichtbaar in projecttaakregels onder “ontvangen/niet gefact.bedrag”. Inkooporder boeken voor facturatie resulteert dan wel in projectpost (type verbruik) en update in projectplanningsregels.

- Artikelen plannen voor project via inkoop-/planningsvoorstel

Projectplanningsregels met status "order" zijn een behoefte, zodat de artikelbehoefte (igv artikel met “soort = voorraad”) ook zichtbaar is in inkoopvoorstellen of planningsvoorstellen.

Het resultaat van de artikelplanningsberekening (inkoopvoorstel of planningsvoorstellen) is in geval van aanvulling via inkoop, een inkooporder zonder koppeling naar project(taak) maar wel met reservatie tussen aanvullingsvoorstelregel en projectplanningsregel.

Dit inkooporder boeken voor ontvangst/facturatie heeft geen impact op het project, er wordt geen projectpost (type verbruik) aangemaakt. Het artikelverbruik moet dan verwerkt worden via projectdagboek (mogelijk via functies vanuit projectplanningsregel).

- Artikelen plannen voor project via reservatie op voorraad

Projectplanningsregels voor artikelen (igv “soort = voorraad”) kunnen gereserveerd worden, reservatie van aanwezige voorraad voor artikelbehoefte in het project.

##### 5.6.1.1 BC70.205.01 Artikelen voor project plannen (Progressus)
https://docs.progressussoftware.com/articles/Inventory-Budget_Reservations_Planning_Lines.html#create- update-or-delete-purchase-orders-or-sales-orders-from-planning-lines

De projectplanningsregels met soort "artikel" zijn ook in Progressus het vertrekpunt voor de effectieve planning van artikelbehoefte. Vermits de budgettering in Progressus wordt vastgelegd in budgetposten, gaat men deze info updaten naar projectplanningslijnen via het uitvoeren van de functie “update budgetplanning”.

Verfijnen van projectplanningsregels met soort “artikel” kan op verschillende manieren, idem aan standaard Business Central:

- Artikelen voor project plannen in projectplanningsregel (manueel)

- Artikelen voor project plannen via projectplanningsregeldatum wijzigen

De verdere operationele planning kan op verschillende manieren (via functies):

- Artikelen plannen voor project via inkooporderacties verwerken

- Artikelen plannen voor project via inkooporders maken

- Artikelen plannen voor project via orders maken

- Artikelen plannen voor project via orderplanning

- Artikelen plannen voor project via reserveren

- Artikelen plannen voor project via project specifiek inkooporder (manueel, idem standaard Business
Central)

#### 5.6.2 BS70.206 Resources voor project toewijzen en plannen Commented [CP21]: In praktijk adviseren wij/Cegeka
en/of kiest klant voor een grafische planningstool (ons https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-create-jobs#to-create- advies/voorkeur = Dime Scheduler)

planning-lines-for-a-project

De projectplanningsregels met soort "resource" zijn het vertrekpunt voor de effectieve planning van resources. De initiële projectplanningsregels ifv benodigde resources zijn meestal vrij algemeen: welk type resource(groep) + totaal aantal uren. Voor een effectieve planning moet dit verfijnd worden: toewijzen van concrete resource en aantal uren op geplande datum.

De verdere operationele planning definiëren kan op verschillende manieren:

- Resources voor project toewijzen en plannen in projectplanningsregel

In deze flow registreert men de resourceplanning direct in de projectplanningsregel: specificatie van juiste resource en aantal uren op effectieve uitvoeringsdatum (planningsdatum). Commented [CP22]: @Niels Habraken Deze paragraaf is onjuist, functie heeft ander doel => dan ook in ander
- Resources voor project plannen via projectplanningsregeldatum wijzigen BS onder proj-verkoopfacturen functie correct
beschreven In een projectplanningsregel legt "planningsdatum" eigenlijk de concrete uitvoeringsdatum vast. Het kan nodig zijn om activiteiten te herplannen en dus "planningsdatum" aan te passen. Via de actie “planningsregeldatums voor project wijzigen” kan men de planningsdatum wijzigen in één of meer projectplanningsregels. Manueel de planningsdatum in een projectplanningsregel aanpassen, is ook mogelijk.

##### 5.6.2.1 BC70.206.01 Resources voor project toewijzen en plannen (Progressus)
TO DO = nog uitwerken, onderstaande = beschrijving zoals aanwezig in BPA template v2.9 Commented [CP23]: @Niels Habraken Ik heb geen kennis van planningstool in Progressus zelf => dit stuk OPGELET : BS nummers zullen minstens BC nummers worden of gewoon zonder BC nummer en dan opsomming dus best door collega met deze kennis laten uitwerken van de versch mogelijkheden => dit zijn momenteel Matthias (meeste kennis), misschien ook al ChristofV

##### 5.6.2.2 BC70.206.02 Projectplanningslijnen beheren via "budget planning update"
Met budget planning update worden de projectplanningslijnen geüpdatet met informatie van de budget boekingen. De projectplanningslijnen zijn de basis voor de verdere projectflow, voornamelijk voor planning behoefte van artikelen en voor verwerken van de artikel- en logistieke flow.

##### 5.6.2.3 BC70.206.03 Projectplanning via "Gantt chart"
De Gantt Chart maakt een grafische planning van taken mogelijk met drag en drop functionaliteit en kleurenvisualisatie voor verbruik vs. budget.

Elke taak wordt in een grafisch formaat gepresenteerd. De taken kunnen in de Gantt Chart zelf worden verplaatst of door het instellen van de startdatum en einddatum op de taakkaart.

Taken van het type posting kunnen worden verplaatst/gewijzigd in de tijd en worden gevisualiseerd als getotaliseerde balk voor het verbruikte percentage t.o.v. het budget in verschillende kleuren. Verwante taken worden getoond als link tussen deze taken.

Taken van het type begin/eind totaal kunnen indien nodig worden samengevouwen/uitgevouwen.

### 5.7 BS70.299 Resourceplanning beheren
Het resource board toont opdrachttoewijzingen in een kalenderweergave voor alle resources en kan worden weergegeven voor een individuele resource, een specifiek project of voor alle resources in de organisatie.

Er is geen directe link tussen het budget en de resource board. Maar je kan een budget wel importeren in het resource board om als startpunt te gebruiken om uit te plannen in het resource board door zaken te verschuiven en te verfijnen.

#### 5.7.1 BC70.299.01 Resource board beheren via "importeren budget"
Het resource board toont opdrachttoewijzingen in een kalenderweergave voor alle resources en kan worden weergegeven voor een individuele resource, een specifiek project of voor alle resources in de organisatie.

Er is geen directe link tussen het budget en de resource board. Maar je kan een budget wel importeren in het resource board om als startpunt te gebruiken om uit te plannen in het resource board door zaken te verschuiven en te verfijnen.

Het budget wordt immers vaak per week, maand of jaar opgemaakt, voor de planning is het waarschijnlijker om per dag te werken. De informatie in het budget is vaak niet gedetailleerd genoeg.

#### 5.7.2 BC70.299.02 Resource board beheren via "wijzigen opdrachttoewijzing"
Met wijzigen opdrachttoewijzing in het resource board kan je een andere resource of resource groep toewijzen aan bestaande opdrachttoewijzigen. Je kan een startdatum en tijd instellen en andere filters instellen als je dit uitvoert.

#### 5.7.3 BC70.299.03 Resource board beheren via "kopiëren
opdrachttoewijzing" Met kopiëren opdrachttoewijzing kan je meerdere opdrachttoewijzingen tegelijk kopiëren. Ook hier kan je filters instellen om deze opdracht te verfijnen.

BS70.302 Resource board beheren via "annuleren opdrachttoewijzing"

Met annuleren opdrachttoewijzing kan je een selectie van opdrachttoewijzingen tegelijk annuleren. Ook hier kan je filters instellen om deze opdracht te verfijnen.

#### 5.7.4 BC70.299.04 Resource board beheren via "aanpassing datum in
opdrachttoewijzing" Met aanpassing datum in opdrachttoewijzing in het resource board kunnen de data van meerdere werktoewijzingen aangepast worden met behulp van een formule. Ook hier kan je filters instellen om deze opdracht te verfijnen.

#### 5.7.5 BC70.299.05 Resource board beheren via drag & drop
In het resource board kan je een werkopdracht slepen naar de rij van de gewenste resource en/of naar een andere dag.

### 5.8 Project & integratie Outlook
#### 5.8.1 BS70.305 Opdrachttoewijzing in resource board syncen naar Outlook
Opdrachttoewijzingen kunnen worden gesynchroniseerd met de Outlook agenda van elke resource.

Op deze manier kan een resource eenvoudig zijn persoonlijke planning samenvoegen met de projectplanning in Outlook en zo de dagplanning zien. Bovendien kan de resource dan ook vanuit deze Outlook afspraken zijn tijdsregistratie doen en syncen naar Business Central.

#### 5.8.2 BS70.207 Onkosten voor project plannen
https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-create-jobs#to-create- planning-lines-for-a-project

Het kan ook nuttig zijn om bepaalde onkosten te plannen binnen een project. Dit is voornamelijk van toepassing voor kosten/diensten die men gaat inkopen. Projectplanningsregels met soort “grootboekrekening” gedefinieerd ifv projectbudget, zijn richtinggevend voor effectieve planning.

Verfijnen van projectplanningsregels met soort “grootboekrekening” kan op verschillende manieren:

- Onkosten voor project plannen in projectplanningsregel

In deze flow registreert men de planning/behoefte van onkosten direct in de projectplanningsregel: specificatie van juiste grootboekrekening en aantal op voorziene verbruiksdatum (planningsdatum).

- Onkosten voor project plannen via projectplanningsregeldatum wijzigen

In een projectplanningsregel legt "planningsdatum" eigenlijk de concrete uitvoeringsdatum vast. Het kan nodig zijn om onkosten te herplannen en dus "planningsdatum" aan te passen. Via de actie “planningsregeldatums voor project wijzigen” kan men de planningsdatum wijzigen in één of meer projectplanningsregels. Manueel de planningsdatum in een projectplanningsregel aanpassen, is ook mogelijk.

De verdere operationele planning definiëren kan op volgende manier:

- Onkosten plannen voor project via project specifiek inkooporder (manueel)

Men registreert volledig manueel een project specifiek inkooporder voor de benodigde dienst/kost.

Een inkooporder is project specifiek door het koppelen van de inkooporderlijnen aan een project en projecttaak. Net zoals in een gewoon inkooporder bepaalt ook hier "verzochte ontvangstdatum" de planning van de behoefte.

Opmerking: Vanuit projectplanningsregel met soort “grootboekrekening” kan geen inkooporder (via functie) aangemaakt worden, bijgevolg moet dit manueel gebeuren.

##### 5.8.2.1 BC70.207.01 Onkosten voor project plannen (Progressus)
https://docs.progressussoftware.com/articles/Inventory-Budget_Reservations_Planning_Lines.html#create- update-or-delete-purchase-orders-or-sales-orders-from-planning-lines

De projectplanningsregels met soort "grootboekrekening" en specificatie van “onkostencode” (expense) zijn ook in Progressus het vertrekpunt voor de effectieve planning van onkosten. Vermits de budgettering in Progressus

wordt vastgelegd in budgetposten, gaat men deze info updaten naar projectplanningslijnen via het uitvoeren van Commented [CP24]: Inkooporder met orderlijnen type de functie “update budgetplanning”. "artikel" (artikel met soort "voorraad") gekoppeld aan project + projecttaak Verfijnen van projectplanningsregels met soort “grootboekrekening” kan op verschillende manieren, idem aan
- Boeken voor ontvangst => generatie van geboekte
standaard Business Central: inkoopontvangst, artikelpost voor ontvangst + negatieve correctie, waardeposten
- Onkosten voor project plannen in projectplanningsregel (manueel) •Artikel wordt dus logistiek onmiddellijk afgeboekt,
project gerelateerde ontvangst van artikelen heeft
- Onkosten voor project plannen via projectplanningsregeldatum wijzigen geen impact op de voorraad
- Geen projectpost, dus operationeel nog geen kost
De verdere operationele planning kan op verschillende manieren: op het project, wel een verwachte kost
- Boeken voor ontvangst => bij project met
- Onkosten plannen voor project via inkooporderacties verwerken (functie) "gebruikslink = ja" geen update van
projectplanningsregel(s) ...
- Onkosten plannen voor project via projectspecifiek inkooporder (manueel, idem standaard Business
Commented [CP25]: Scenario voor registreren Central) verbruik van artikelen (artikel met soort "voorraad")
- Projectplanningsregel (normaal bestaande na
budgettering): regelsoort = "budget" i.g.v vaste prijs project, regelsoort = "budget en factureerbaar" i.g.v
### 5.9 Project verbruiken in regie project), aantal = positief, kostprijs =
positief, aantal te verplaatsen naar dagboek = invullen van verbruikt aantal
#### 5.9.1 BS70.208 Project verbruiken artikelen •Vanuit projectplanningsregel dan functie
"projectdagboekregels maken" => https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-record-job-usage projectdagboekregels erven dezelfde "regelsoort" als in projectplanningsregel. ... https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-record-job-usage#to-view- Commented [CP26]: Scenario voor registreren project-usage-estimates-and-post-updates verbruik van artikelen
- In projectdagboek uitvoeren functie "resterend
Tijdens de uitvoering van activiteiten op een project kan men artikelen verbruiken en wordt het verbruik (of gebruik berekenen" gebruik) vastgelegd op dit project. •Systeem genereert projectdagboekregel(s) op basis van projectplanningsregel(s) met nog resterend Verschillende flows om verbruik van artikelen te registeren en verwerken: aantal => het resterend aantal (= nog niet verbruikt aantal) wordt voorgesteld als aantal in de
- Verbruik van artikelen voor project via project specifieke inkoop (manueel of via functie “inkooporder projectplanningsregel
- Projectdagboek boeken => projectdagboekregels
maken”) erven dezelfde "regelsoort" als in projectplanningsregel. ...
- Verbruik van artikelen voor project via projectdagboek vanuit projectplanningsregel
Commented [CP27]: Scenario voor registreren
- Verbruik van artikelen voor project via projectdagboek obv resterend gebruik berekenen verbruik van artikelen
- Projectdagboekregel registreren : regelsoort =
- Verbruik van artikelen voor project via projectdagboek (manueel) "budget" i.g.v vaste prijs project, regelsoort =
"factureerbaar" i.g.v in regie project, aantal =
- Verbruik van artikelen voor project via voorraadpick positief, kostprijs = positief
- Projectdagboek boeken
- Verbruik van artikelen voor project via magazijnpick •Resultaat : artikelpost (type = negatieve correctie,
aantal = negatief, kost = negatief)), projectpost (type Artikelverbruik op een project resulteert in het volgende: = usage, aantal = positief, kost = positief), update van verbruik in projectplanningsregel (o.a. geboekt aantal, resterend aantal) of indien geen ...

- Projectpost van soort “gebruik”, wat dan ook actuele kost op het project vertegenwoordigt (via
inkoopflow pas bij facturatie)

- Update van verbruik in projectplanningsregel (afhankelijk van instelling “gebruikslink”)

- Artikelpost negatieve mutatie

##### 5.9.1.1 BC70.208.01 Project verbruiken artikelen (Progressus)
https://docs.progressussoftware.com/articles/Inventory- Budget_Reservations_Planning_Lines.html#reservations

https://docs.progressussoftware.com/articles/Inventory-Budget_Reservations_Planning_Lines.html#create- update-or-delete-purchase-orders-or-sales-orders-from-planning-lines

https://docs.progressussoftware.com/articles/Inventory-Sales_Order-Invoice-Create_Usage.html

In vergelijking met standaard Business Central, ondersteunt Progressus nog meer mogelijkheden om artikelbehoeften te verwerken, ook met meer directe acties/opvolging vanuit de planningsregels.

Verschillende flows om verbruik van artikelen te registreren en verwerken:

- Verbruik van artikelen voor project vanuit stock

  - Via projectspecifiek verkooporder (functie “verwerken verkooporder acties (maken)” vanuit
projectplanningsregels)

  - Via projectdagboek vanuit projectplanningsregel (idem standaard BC)

  - Via projectdagboeken obv resterend gebruik berekenen (idem standaard BC)

  - Via projectdagboek (manueel) (idem standaard BC)

  - Verbruik van artikelen voor project via voorraadpick (idem standaard BC)

  - Verbruik van artikelen voor project via magazijnpick (idem standaard BC)

- Verbruik van artikelen voor project via projectspecifiek inkooporder (functie “verwerken inkooporder
acties (maken)” of via “planningsvoorstel”) vanuit projectplanningsregels

- Verbruik van artikelen voor project via projectspecifieke assemblage (via “planningsvoorstel”) vanuit
projectplanningsregels

- Verbruik van artikelen voor project via projectspecifieke productie (via “planningsvoorstel”) vanuit
projectplanningsregels

Artikelverbruik op een project resulteert in de volgende posten: Commented [CP28]: Scenario tijdsregistratie (std
- Projectpost en detailprojectpost van soort “gebruik”, wat dan ook actuele kost op het project Business Central tijdsregistratie)
- Aanmaken urenstaten per resource
vertegenwoordigt
- Invullen van urenstaat
- Versturen van urenstaat (= afsluiten registratie,
- Update van verbruik in projectplanningsregel
goedkeuring kan dan starten)
- Goedkeuren van urenstaat
- Artikelpost negatieve mutatie
- Ophalen van urenstaat in projectdagboek
- Boeken van projectdagboek met de opgehaalde
urenstaat
- Resultaat : resourcepost (boekingssoort = gebruik,
#### 5.9.2 BS70.209 Project verbruiken resources aantal = positief, kost = positief), projectpost (type =
usage, aantal = positief, kost = positief), update van https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-use-time-sheets verbruik in projectplanningsregel (o.a. geboekt ... Commented [CP29]: Scenario voor registreren https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-use-resources#to-record- verbruik van resources resource-usage-for-a-project •Projectplanningsregel (normaal bestaande na budgettering): regelsoort = "budget" i.g.v vaste prijs https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-record-job-usage#to-view- project, regelsoort = "budget en factureerbaar" i.g.v project-usage-estimates-and-post-updates in regie project, aantal = positief, kostprijs = positief, aantal te verplaatsen naar dagboek = invullen van Tijdens de uitvoering van activiteiten op een project verbruiken resources tijd en wordt het verbruik (of gebruik) verbruikt aantal
- Vanuit projectplanningsregel dan functie
vastgelegd op dit project. "projectdagboekregels maken" => projectdagboekregels erven dezelfde "regelsoort" Verschillende flows om verbruik van resources te registeren en verwerken: als in projectplanningsregel. ...

- Verbruik van resources voor project via tijdsregistratie (manuele registratie – vrijgeven tijdsregistratie - Commented [CP30]: Scenario voor registreren
verbruik van resources goedkeuring/afkeuring - boeken projectdagboek) •In projectdagboek uitvoeren functie "resterend gebruik berekenen"
- Verbruik van resources voor project via projectdagboek vanuit projectplanningsregel •Systeem genereert projectdagboekregel(s) op basis
van projectplanningsregel(s) met nog resterend
- Verbruik van resources voor project via projectdagboek obv resterend gebruik berekenen aantal => het resterend aantal (= nog niet verbruikt
aantal) wordt voorgesteld als aantal in de
- Verbruik van resources voor project via projectdagboek (manueel) projectplanningsregel
- Projectdagboek boeken => projectdagboekregels
Resourceverbruik op een project resulteert in het volgende: erven dezelfde "regelsoort" als in projectplanningsregel. ...
- Projectpost van soort “gebruik”, wat dan ook actuele kost op het project vertegenwoordigt
Commented [CP31]: Scenario voor registreren verbruik van resources
- Update van verbruik in projectplanningsregel (afhankelijk van instelling “gebruikslink”)
- Projectdagboekregel manueel registreren :
regelsoort = "budget" i.g.v vaste prijs project,
- Resourcepost
regelsoort = "factureeerbaar" i.g.v in regie project, aantal = positief, kostprijs = positief
- Projectdagboek boeken
- Resultaat : resourcepost (boekingssoort = gebruik,
##### 5.9.2.1 BC70.209.01 Project verbruiken resources (Progressus) aantal = positief, kost = positief), projectpost (type =
https://docs.progressussoftware.com/articles/Timesheet_Entry.html usage, aantal = positief, kost = positief), update van verbruik in projectplanningsregel (o.a. geboekt aantal, resterend aantal) of indien geen ...

https://docs.progressussoftware.com/articles/TM-Create_Time_Periods.html Commented [CP32]: Tijdsregistraties kunnen als lijnen https://docs.progressussoftware.com/articles/PP_outlook-time-entry-in-outlook.html of als matrix weergegeven worden.
- In de timesheet matrix kunnen tijdsregistraties
In vergelijking met standaard Business Central, ondersteunt Progressus nog meer en uitgebreidere functionaliteit manueel lijn per lijn ingevoerd worden, met de projectnummers en taakcodes als rijen en de dagen voor urenregistratie van resources. van de geselecteerde periode als kolommen.
- Via de dag op een lijn worden de nodige gegevens
Verschillende flows om verbruik van resources te registeren en verwerken: ingevoerd, zoals de hoeveelheid uren en eventueel een aangepaste omschrijving.
- Verbruik van resources voor project via tijdsregistratie van Progressus (manuele registratie, kopiëren
tijdsregistratie, updaten met budget – vrijgeven timesheet (met ingestelde controles, notificaties) - Met updaten van budget worden lijnen in de timesheet matrix gecreëerd o.b.v. budgetposten. De goedkeuringsflow (max 3 niveau’s, goedkeuren/afkeuren, notificaties) - review in projecttijdsdagboek waardes van de budgetposten worden niet (facultatief)) gekopieerd.

- Verbruik van resources voor project via tijdsregistratie in Outlook (registratie via Outlook agenda, via Met kopiëren van tijdsregistratie in de timesheet
matrix kunnen tijdsregistraties van jezelf of andere Outlook email – vrijgeven timesheet (met ingestelde controles, notificaties) – goedkeuringsflow (max 3 resources gekopieerd worden. niveau’s, goedkeuren/afkeuren, notificaties) – review in projecttijdsdagboek (facultatief)) ... Commented [CP33]: In goedkeuring van
- Verbruik van resources voor project via projecttijddagboek (manueel) (vergelijkbaar met via tijdsregistratie heeft men:
projectdagboek in standaard BC) •stap 1 = manueel goedkeuren/afkeuren
- stap 2 = review en eventuele finale aanpassing in
- Verbruik van resources voor project via projectdagboek vanuit projectplanningsregel (idem standaard projectdagboek
Stap 2 is een facultatieve stap en kan dus ingesteld BC) worden om niet uit te voeren.

- Verbruik van resources voor project via projectdagboek obv resterend gebruik berekenen (idem Via tijdsregistratie goedkeuren worden
standaard BC) tijdsregistraties goedgekeurd. Deze goedkeuring kan opgezet worden voor maximaal Resourceverbruik op een project resulteert in de volgende posten: 3 goedkeuringsniveaus. Het veld “weergeven als” geeft alle tijdsregistraties weer die wachten op
- Projectpost en detailprojectpost van soort “gebruik”, wat dan ook actuele kost op het project goedkeuring op één van de 3 niveaus. De opties
omvatten: ... vertegenwoordigt Commented [CP34]: De gebruiker kan de
- Update van verbruik in projectplanningsregel tijdsregistratie doen vanuit de Outlook agenda, wat
voorkomt dat werk wordt vergeten of gemist. Door dit
- Resourcepost op regelmatige, gestructureerde manier uit te voeren,
is het mogelijk om snel een urenstaat te controleren en in te dienen.

De tijdsregistraties kunnen ook ingevoerd worden
#### 5.9.3 BS70.210 Project verbruiken onkosten vanuit Outlook e-mail. De tijdsregistratie add-in
herkent de datum en onderwerp. De tijdregistratie https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-record-job-usage moet dan nog aangevuld worden met het projectnummer, de project taakcode en de https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-record-job-usage#to-view- hoeveelheid. project-usage-estimates-and-post-updates De tijdsregistratie zal onmiddellijk geüpdatet worden in Business Central. ...

Tijdens de uitvoering van activiteiten op een project kan men onkosten maken en wordt het verbruik (of gebruik) Commented [CP35]: Inkooporder met orderlijnen type vastgelegd op dit project. "grootboekrekening" gekoppeld aan project + projecttaak Verschillende flows om verbruik van onkosten te registeren en verwerken: •Boeken voor ontvangst => generatie van geboekte inkoopontvangst
- Verbruik van onkosten voor project via project specifieke inkoop (manueel) •Geen projectpost, dus operationeel nog geen kost
op het project, wel een verwachte kost
- Verbruik van onkosten voor project via projectdagboek vanuit projectplanningsregel •Boeken voor ontvangst => bij project met
"gebruikslink = ja" geen update van
- Verbruik van onkosten voor project via projectdagboek obv resterend gebruik berekenen projectplanningsregel(s)
- Boeken voor facturatie => generatie van geboekte
- Verbruik van artikelen voor project via projectdagboek (manueel) inkoopfactuur, grootboekpost, BTW post,
(gedetailleerde) leverancierspost, projectpost ... Onkostenverbruik op een project resulteert in het volgende: Commented [CP36]: Scenario voor registreren verbruik van onkosten via "grootboekrekening"
- Projectpost van soort “gebruik”, wat dan ook actuele kost op het project vertegenwoordigt (via •Projectplanningsregel (normaal bestaande na
inkoopflow pas bij facturatie) budgettering): regelsoort = "budget" i.g.v vaste prijs project, regelsoort = "budget en factureerbaar" i.g.v
- Update van verbruik in projectplanningsregel (afhankelijk van instelling “gebruikslink”) in regie project, aantal = positief, kostprijs =
positief, aantal te verplaatsen naar dagboek =
- Grootboekpost invullen van verbruikt aantal ...
Commented [CP37]: Scenario voor registreren verbruik van onkosten via “grootboekrekening”
- In projectdagboek uitvoeren functie "resterend
##### 5.9.3.1 BC70.210.01 Project verbruiken onkosten (Progressus) gebruik berekenen"
- Systeem genereert projectdagboekregel(s) op basis
https://docs.progressussoftware.com/articles/TM-Expense_Sheet_Entry_Approval.html van projectplanningsregel(s) met nog resterend aantal => het resterend aantal (= nog niet verbruikt... In vergelijking met standaard Business Central, ondersteunt Progressus het onkostenverbruik veel duidelijker en Commented [CP38]: Scenario voor registreren eenvoudiger via onkWeightscostennota-functionaliteit, gebruikmakend van masterdata “onkosten” en zo ook verbruik van onkosten via "grootboekrekening" vergelijkbaar met tijdsregistratie. •Projectdagboekregel registreren : regelsoort = "budget" i.g.v vaste prijs project, regelsoort = Verschillende flows om verbruik van onkosten te registeren en verwerken: "factureerbaar" i.g.v in regie project, aantal = positief, kostprijs = positief
- Verbruik van onkosten voor project via onkostennota (registratie, onkosten-bijlage – vrijgeven •Projectdagboek boeken ...
onkostennota (met notificaties) - goedkeuringsflow (max 3 niveau’s, goedkeuren/afkeuren, notificaties) Commented [CP39]: Met onkostennota's kunnen werknemers gemaakte onkosten tijdens hun zakelijke
- review in project-onkostendagboek (facultatief))
activiteiten invoeren. Er kan per onkostennota één of meerdere onkosten geregistreerd worden.
- Verbruik van onkosten voor project via projectspecifieke inkoop (manueel) (vergelijkbaar met via Via de open onkostennota lijst kunnen open
projectspecifieke inkoop in standaard BC, maar ook specificatie van onkosten-code) onkostennota's bekeken en bewerkt worden. Het veld status onkostennota geeft de huidige status weer
- Verbruik van onkosten voor project via project-onkostendagboek (manueel) (vergelijkbaar met via (open, wachtend goedkeuring, geboekt). ...
projectdagboek in standaard BC, maar ook specificatie van onkosten-code) Commented [CP40]: Met het onkostendagboek kunnen batches van onkostendagboeken aangemaakt
- Verbruik van onkosten voor project via projectdagboek vanuit projectplanningsregel (idem standaard en bewerkt worden die enkel de velden bevatten die
nodig zijn voor het boeken van onkosten transacties. BC, maar ook specificatie van onkosten-code) Transacties m.b.t. onkosten kunnen ook geïmporteerd worden in het onkostendagboek vanuit een Excel- bestand. ...

- Verbruik van onkosten voor project via projectdagboek obv resterend gebruik berekenen (idem
Commented [CP41]: Inkoopretourorder met standaard BC, maar ook specificatie van onkosten-code) orderlijnen type "artikel" (artikel met soort "voorraad") gekoppeld aan project + projecttaak Onkostenverbruik op een project resulteert in de volgende posten: •Boeken voor verzending => generatie van geboekte inkoopretourverzending, artikelpost voor
- Projectpost en detailprojectpost van soort “gebruik”, wat dan ook actuele kost op het project verzending + positieve correctie, waardeposten
- Artikel wordt dus logistiek onmiddellijk afgeboekt,
vertegenwoordigt project gerelateerde verzending van artikelen heeft geen impact op de voorraad
- Update van verbruik in projectplanningsregel
- Geen projectpost, dus operationeel nog geen
kostvermindering op het project, wel vermindering
- Grootboekpost
van verwachte kost
- Boeken voor verzending => bij project met
"gebruikslink = ja" geen update van projectplanningsregel(s) 5.10Verbruik voor projecten corrigeren •Boeken voor facturatie => generatie van geboekte inkoopcreditnota, grootboekpost, BTW post, 5.10.1BS70.211 Verbruik artikelen voor project corrigeren (gedetailleerde) leverancierspost, waardepost (i.g.v... Commented [CP42]: Scenario voor corrigeren https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-record-job-usage (verminderen) verbruik van artikelen (artikel met soort "voorraad") https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-record-job-usage#to-view- •Projectplanningsregel: regelsoort = "budget" i.g.v project-usage-estimates-and-post-updates vaste prijs project, regelsoort = "budget en factureerbaar" i.g.v in regie project), aantal = Tijdens een projectuitvoering kan het nodig zijn om geregistreerde artikelverbruiken te corrigeren. negatief, kostprijs = positief, aantal te verplaatsen naar dagboek = invullen van verbruikt aantal Correctie van een meerverbruik van een artikel op een project = dezelfde werkwijze als beschreven in paragraaf •Vanuit projectplanningsregel dan functie "projectdagboekregels maken" => BS70.208 Project verbruiken artikelen. projectdagboekregels erven dezelfde "regelsoort" als in projectplanningsregel. Verschillende flows om correctie van een minderverbruik van een artikel te registeren en verwerken: •Vanuit projectplanningsregel dan functie "projectdagboek openen" + het projectdagboek
- Correctie artikelverbruik voor project via project specifieke inkoopretour (manueel) boeken.
- Resultaat : artikelpost (type = negatieve correctie,
- Correctie artikelverbruik voor project via projectdagboek vanuit projectplanningsregel aantal = positief, kost = positief)), projectpost (type...

- Correctie artikelverbruik voor project via projectdagboek (manueel) Commented [CP43]: Scenario voor corrigeren
(verminderen) verbruik van artikelen Correctie van een minderverbruik van een artikel op een project resulteert in het volgende: •Projectdagboekregel registreren : regelsoort = "budget" i.g.v vaste prijs project, regelsoort =
- Projectpost van soort “gebruik”, wat dan ook actuele kostvermindering op het project vertegenwoordigt "factureerbaar" i.g.v in regie project, aantal =
negatief, kostprijs = positief (via inkoopretour-flow pas bij facturatie) •Projectdagboek boeken
- Resultaat : artikelpost (type = negatieve correctie,
- Update van verbruik in projectplanningsregel (afhankelijk van instelling “gebruikslink”) aantal = positief, kost = positief)), projectpost (type
= usage, aantal = negatief, kost = positief), update
- Artikelpost positieve mutatie van verbruik in projectplanningsregel (o.a. geboekt
aantal, resterend aantal) of indien geen overeenstemmende projectplanningsregel(s) gevonden aanmaak van nieuwe projectplanningsregel (bij "gebruikslink = ja", regelsoort in nieuwe projectplanningsregel = ...

##### 5.10.1.1 BC70.211.01 Verbruik artikelen voor project corrigeren (Progressus)
https://docs.progressussoftware.com/articles/Inventory- Budget_Reservations_Planning_Lines.html#reservations

https://docs.progressussoftware.com/articles/Inventory-Budget_Reservations_Planning_Lines.html#create- update-or-delete-purchase-orders-or-sales-orders-from-planning-lines

https://docs.progressussoftware.com/articles/Inventory-Sales_Order-Invoice-Create_Usage.html

Tijdens een projectuitvoering kan het nodig zijn om geregistreerde artikelverbruiken te corrigeren.

In Progressus zijn de opties voor corrigeren van artikelverbruik vrij identiek aan standaard BC en ook veelal manueel te registreren.

Correctie van een meerverbruik van een artikel op een project = dezelfde werkwijze als beschreven in paragraaf BC70.208.01 Project verbruiken artikelen (Progressus).

Verschillende flows om correctie van een minderverbruik van een artikel te registeren en verwerken:

- Correctie artikelverbruik voor project via project specifieke inkoopretour (manueel)

- Correctie artikelverbruik voor project via project specifieke verkoopretour (manueel)

- Correctie artikelverbruik voor project via projectdagboek vanuit projectplanningsregel

- Correctie artikelverbruik voor project via projectdagboek (manueel)

Correctie van een minderverbruik van een artikel op een project resulteert in het volgende:

- Projectpost van soort “gebruik”, wat dan ook actuele kostvermindering op het project vertegenwoordigt

- Update van verbruik in projectplanningsregel

- Artikelpost positieve mutatie

5.10.2BS70.212 Verbruik resources voor project corrigeren https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-use-time-sheets

https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-use-resources#to-record- resource-usage-for-a-project

https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-record-job-usage#to-view- project-usage-estimates-and-post-updates

Tijdens een projectuitvoering kan het nodig zijn om geregistreerde resourceverbruiken te corrigeren.

Correctie van een meerverbruik van een resource op een project = dezelfde werkwijze als beschreven in paragraaf BS70.209 Project verbruiken resources.

Verschillende flows om correctie van een minderverbruik van een resource te registeren en verwerken:

- Correctie resourceverbruik voor project via projectdagboek vanuit projectplanningsregel Commented [CP44]: Scenario voor verminderen
verbruik van resources
- Correctie resourceverbruik voor project via projectdagboek (manueel) •Projectplanningsregel: regelsoort = "budget" i.g.v
vaste prijs project, regelsoort = "budget en Correctie van een minderverbruik van een resource op een project resulteert in het volgende: factureerbaar" i.g.v in regie project, aantal = negatief, kostprijs = positief, aantal te verplaatsen
- Projectpost van soort “gebruik”, wat dan ook actuele kostvermindering op het project naar dagboek = invullen van aantal te verminderen
vertegenwoordigt •Vanuit projectplanningsregel dan functie "projectdagboekregels maken" =>
- Update van verbruik in projectplanningsregel (afhankelijk van instelling “gebruikslink”) projectdagboekregels erven dezelfde "regelsoort"
als in projectplanningsregel.
- Resourcepost (aantal = negatief) •Vanuit projectplanningsregel dan functie
"projectdagboek openen" + het projectdagboek boeken.
- Resultaat : resourcepost (boekingssoort = gebruik,
aantal = negatief, kost = positief), projectpost (type
##### 5.10.2.1 BC70.212.01 Verbruik resources voor project corrigeren (Progressus)
= usage, aantal = negatief, kost = positief), update Tijdens een projectuitvoering kan het nodig zijn om geregistreerde resourceverbruiken te corrigeren. van verbruik in projectplanningsregel (o.a. geboekt aantal, resterend aantal) of indien geen In Progressus zijn de opties voor corrigeren van resourcesverbruik vrij identiek aan standaard BC en ook veelal overeenstemmende projectplanningsregel(s) gevonden aanmaak van nieuwe manueel te registreren. projectplanningsregel (bij "gebruikslink = ja", regelsoort in nieuwe projectplanningsregel = Correctie van een meerverbruik van een resource op een project = dezelfde werkwijze als beschreven in "budget" (vaste prijs project) of "budget en paragraaf BC70.209.01 Project verbruiken resources (Progressus). factureerbaar" (in regie project)). Commented [CP45]: Scenario voor verminderen Verschillende flows om correctie van een minderverbruik van een resource te registeren en verwerken: verbruik van resources
- Projectdagboekregel manueel registreren :
- Correctie resourceverbruik voor project via projectdagboek vanuit projectplanningsregel (idem regelsoort = "budget" i.g.v vaste prijs project,
standaard BC) regelsoort = "factureeerbaar" i.g.v in regie project, aantal = negatief, kostprijs = positief
- Correctie resourceverbruik voor project via projecttijddagboek (manueel) (vergelijkbaar met via •Projectdagboek boeken
- Resultaat : resourcepost (boekingssoort = gebruik,
projectdagboek in standaard BC) aantal = negatief, kost = positief), projectpost (type = usage, aantal = negatief, kost = positief), update Correctie van een minderverbruik van een resource op een project resulteert in het volgende: van verbruik in projectplanningsregel (o.a. geboekt aantal, resterend aantal) of indien geen
- Projectpost van soort “gebruik”, wat dan ook actuele kostvermindering op het project
overeenstemmende projectplanningsregel(s) vertegenwoordigt gevonden aanmaak van nieuwe projectplanningsregel (bij "gebruikslink = ja",
- Update van verbruik in projectplanningsregel regelsoort in nieuwe projectplanningsregel =
"budget" (vaste prijs project) of "budget en
- Resourcepost (aantal = negatief) factureerbaar" (in regie project)).

5.10.3BS70.213 Verbruik onkosten voor project corrigeren Commented [CP46]: Inkoopretourorder met orderlijnen type "grootboekrekening" gekoppeld aan https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-record-job-usage project + projecttaak
- Boeken voor verzending => generatie van geboekte
https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-record-job-usage#to-view- inkoopverzending
- Geen projectpost, dus operationeel nog geen kost
project-usage-estimates-and-post-updates op het project, wel een verwachte kostvermindering
- Boeken voor verzending => bij project met
Tijdens een projectuitvoering kan het nodig zijn om geregistreerde onkostenverbruiken te corrigeren. "gebruikslink = ja" nog geen update van Correctie van een meerverbruik van onkosten op een project = dezelfde werkwijze als beschreven in paragraaf projectplanningsregel(s)
- Boeken voor facturatie => generatie van geboekte
BS70.210 Project verbruiken onkosten. inkoopcreditnota, grootboekpost, BTW post, (gedetailleerde) leverancierspost, projectpost Verschillende flows om correctie van een minderverbruik van onkosten te registeren en verwerken: •Wel projectpost, dus operationeel dan kostvermindering op het project
- Correctie onkostenverbruik voor project via project specifieke inkoopretour/creditnota (manueel) •Boeken voor facturatie => update van verbruik in
projectplanningsregel (o.a. geboekt aantal, ...
- Correctie onkostenverbruik voor project via projectdagboek vanuit projectplanningsregel
Commented [CP47]: Scenario voor verminderen verbruik van onkosten via "grootboekrekening"
- Correctie onkostenverbruik voor project via projectdagboek (manueel)
- Projectplanningsregel: regelsoort = "budget" i.g.v
Correctie van een minderverbruik van onkosten op een project resulteert in het volgende: vaste prijs project, regelsoort = "budget en factureerbaar" i.g.v in regie project, aantal =
- Projectpost van soort “gebruik”, wat dan ook actuele kost op het project vertegenwoordigt (via negatief, kostprijs = positief, aantal te verplaatsen
naar dagboek = invullen van aantal te verminderen inkoopflow pas bij facturatie) •Vanuit projectplanningsregel dan functie "projectdagboekregels maken"=>
- Update van verbruik in projectplanningsregel (afhankelijk van instelling “gebruikslink”) projectdagboekregels erven dezelfde "regelsoort"
als in projectplanningsregel.
- Grootboekpost •Vanuit projectplanningsregel dan functie
"projectdagboek openen" + het projectdagboek boeken.
- Resultaat : grootboekpost, projectpost (type =
##### 5.10.3.1 BC70.213.01 Verbruik onkosten voor project corrigeren (Progressus)
usage, aantal = negatief, kost = positief), update van Tijdens een projectuitvoering kan het nodig zijn om geregistreerde onkostenverbruiken te corrigeren. verbruik in projectplanningsregel (o.a. geboekt ... Commented [CP48]: Scenario voor verminderen In Progressus zijn de opties voor corrigeren van onkostenverbruik vrij identiek aan standaard BC en ook veelal verbruik van onkosten via "grootboekrekening" manueel te registreren. •Projectdagboekregel registreren : regelsoort = "budget" i.g.v vaste prijs project, regelsoort = Correctie van een meerverbruik van onkosten op een project = dezelfde werkwijze als beschreven in paragraaf "factureerbaar" i.g.v in regie project, aantal = negatief, kostprijs = positief BC70.210.01 Project verbruiken onkosten (Progressus).
- Projectdagboek boeken
- Resultaat : projectpost (type = usage, aantal =
Verschillende flows om correctie van een minderverbruik van onkosten te registeren en verwerken: negatief, kost = positief), update van verbruik in projectplanningsregel (o.a. geboekt aantal,
- Correctie onkostenverbruik voor project via project specifieke inkoopretour/creditnota (manueel)
resterend aantal) of indien geen (idem standaard BC, maar ook specificatie van onkosten-code) overeenstemmende projectplanningsregel(s) gevonden aanmaak van nieuwe
- Correctie onkostenverbruik voor project via projectdagboek vanuit projectplanningsregel (idem projectplanningsregel (bij "gebruikslink = ja",
regelsoort in nieuwe projectplanningsregel = standaard BC, maar ook specificatie van onkosten-code) "budget" (vaste prijs project) of "budget en factureerbaar" (in regie project)). ...

- Correctie onkostenverbruik voor project via project-onkostendagboek (manueel) ((vergelijkbaar met via
projectdagboek in standaard BC, maar ook specificatie van onkosten-code)

Correctie van een minderverbruik van onkosten op een project resulteert in het volgende:

- Projectpost van soort “gebruik”, wat dan ook actuele kost op het project vertegenwoordigt (via
inkoopflow pas bij facturatie)

- Update van verbruik in projectplanningsregel (afhankelijk van instelling “gebruikslink”)

- Grootboekpost

5.11Project-OHW berekenen Commented [CP49]: @Niels Habraken ik heb geen kennis van project WIP => laten reviewen/updaten door collega met kennis => kennis zit momenteel 5.11.1BS70.214 Project-OHW vooral bij ChristopheN

Naarmate een project vordert, worden materialen, resources en overige zaken verbruikt en moeten hiervoor boekingen plaatsvinden op het project. Onderhanden werk (OHW) is een functie waarmee u de financiële waarde van projecten in het grootboek kunt schatten gedurende de projectuitvoering. In veel gevallen kunt u kosten voor een project boeken voordat u het project factureert. Wanneer alleen kosten zijn geboekt, klopt het financiële afschrift niet. Als u de waarde in het grootboek wilt volgen, kunt u het OHW-bedrag berekenen en de waarde boeken in het grootboek.

U kunt het OHW-bedrag bepalen dat moet worden geboekt naar balansrekeningen voor eindrapportage van een periode. U gebruikt hiervoor de batchverwerking "OHW voor project berekenen".

U kunt het OHW-bedrag berekenen op basis van de volgende zaken:

- Kostprijs

- Verkoopprijs

- Kostprijs van omzet

- Percentage voltooid

- Contract voltooid

OHW-methode Formules Uitleg bij de berekening

Kostprijs • Verantwoorde omzet = Contract Het berekenen van de kostenwaarde wordt (gefactureerd bedrag) gestart door de waarde te berekenen van wat er is aangeleverd, door een deel van de geschatte

- Geschatte totale kostprijs = Contract totale kosten op basis van percentage voltooid te
(totale kostprijs) * Planning (kostenverhouding) nemen. De gefactureerde kosten worden afgetrokken door een deel van de geschatte totale
- OHW-kosten = (Percentage voltooid -
kosten op basis van het gefactureerde percentage Gefactureerd %) * Geschatte totale kostprijs te nemen. Hiervoor moeten de totale kostprijs
  - Percentage voltooid = Gebruik (totale
van het contract, de totale kostprijs van de kostprijs) / Planning (totale kostprijs) planning en de totale kosten van de planning voor
  - Gefactureerd % = Contract (gefactureerd het gehele project worden ingevoerd, omdat
bedrag) / Contract (totale kostprijs) anders de berekeningen niet kloppen.

- Verantwoorde kosten = (Gebruik
(totale kostprijs) - OHW)

Kostprijs van • Verantwoorde omzet = Contract Het berekenen van de verkoopprijs wordt gestart omzet (gefactureerd bedrag) door de verantwoorde kosten te berekenen. Kosten worden proportioneel verantwoord op
- Verantwoorde kosten = Planning
basis van de totale kosten van de planning. (totale kostprijs) * Gefactureerd percentage Hiervoor moeten de totale verkoopprijs van het
  - Gefactureerd % = Contract (gefactureerd
contract en de totale kosten van de planning voor bedrag) / Contract (totale verkoopprijs) het gehele project worden ingevoerd, omdat
  - (Gefactureerd % is een kolom in anders de berekeningen niet kloppen.
Projecttaakregels)

- OHW-kosten = Gebruik (totale kosten)
- Verantwoorde kosten

Verkoopprijs • Verantwoorde kosten = Gebruik Bij het berekenen van de verkoopprijs wordt de (totale kosten) omzet proportioneel verantwoord op basis van de totale kosten van het gebruik en de verwachte
- Verantwoorde omzet = Gebruik totale
kosten van de recovery-verhouding. Hiervoor kosten * Verwachten factuurverhouding moeten de totale verkoopprijs van het contract en
  - Cost Recovery % = Contract (totale
de totale kosten van de planning voor het gehele verkoopprijs) * Planning (totale verkoopprijs) project worden ingevoerd, omdat anders de
- OHW-omzet = Verantwoorde omzet - berekeningen niet kloppen.
Contract (gefactureerd bedrag)

Percentage • Verantwoorde kosten = Gebruik Bij het berekenen van het percentage voltooid voltooid (totale kosten), m.a.w. de werkelijke kosten. worden de inkomsten proportioneel verantwoord op basis van het percentage voltooid, dat wil
- Verantwoorde omzet = Contract
zeggen de totale kosten van het gebruik versus de (totale verkoopprijs) * Percentage voltooid planningskosten. Hiervoor moeten de totale
- Percentage voltooid = Gebruik (totale verkoopprijs van het contract en de totale kosten
kostprijs) / Planning (totale kostprijs) van de planning voor het gehele project worden (Wordt Kosten percentage voltooid in ingevoerd, omdat anders de berekeningen niet Projecttaakregels genoemd) kloppen.

- OHW-omzet = Verantwoorde omzet -
Contract (gefactureerd bedrag), m.a.w.

Contract OHW-bedrag = Totale OHW-kosten = Gebruik Bij Contract voltooid worden de inkomsten en de voltooid (totale kostprijs) kosten pas verantwoord als het project is voltooid. U kunt hiervoor kiezen als de geschatte Omzet OHW = Contract (gefactureerd bedrag) kosten en inkomsten van het project nog niet zeker zijn.

Al het gebruik wordt op de Rekening OHW-kosten geboekt, terwijl alle gefactureerde omzet op de Rekening gefactureerde omzet OHW (passief) wordt geboekt totdat het project is voltooid.

Als u het resultaat met een andere methode wilt bekijken, kunt u de methode wijzigen en het OHW-bedrag nogmaals berekenen. U kunt net zo vaak het OHW-bedrag berekenen als u wilt. Het OHW-bedrag wordt alleen berekend en wordt niet geboekt in het grootboek.

Wanneer u OHW hebt berekend, kunt u het boeken naar balansrekeningen voor de einddatumrapportage. Hiervoor gebruikt u de batchverwerking "Project-OHW naar GB boeken".

##### 5.11.1.1 BC70.214.01 Project WIP (Progressus)
Naarmate een project vordert, worden materialen, middelen en onkosten verbruikt en moeten deze op de taak worden geboekt. Werk in uitvoering (WIP) is een functie waarmee de financiële waarde van projecten in het grootboek kunnen ingeschat worden terwijl de projecten nog lopen.

Het WIP-proces is ontworpen om records te genereren op een rekening voor niet-gefactureerde vorderingen of een WIP-rekening en wordt gewoonlijk minimaal maandelijks uitgevoerd.

In veel gevallen worden uitgaven geboekt voor een opdracht voordat een opdracht gefactureerd wordt. Als alleen uitgaven worden geboekt, is het financieel overzicht onnauwkeurig. WIP wordt in de projectboekhouding gebruikt om te verwijzen naar factureerbare tijd en uitgaven die nog niet zijn gefactureerd werden op een klantfactuur. Het is werk dat al is voltooid of kosten die gemaakt werden, maar wat nog moet worden gefactureerd.

Goede boekhoudpraktijken hebben tot doel de inkomsten en de bijbehorende uitgaven (of onkosten) in dezelfde boekhoudperiode met elkaar in overeenstemming te brengen. Commented [CP50]: Scenario voor maken verkoopfacturen vanuit projectplanningsregels - vaste prijs project:
- projectplanningsregel(s) manueel registreren :
### 5.12 Project-verkoopfacturen beheren regelsoort = "factureerbaar", aantal = positief
meestal 1, eenheidsprijs = te factureren
#### 5.12.1 BS70.216 Projectfacturen maken - vaste prijs verkoopprijs (positief)
- projectplanningsregel per schijf van facturatie
https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-invoice-jobs aanmaken
- projectplanningsregels die men wenst te
Bij vaste prijs projecten is er een overeenkomst om het project op te leveren aan een vaste prijs. Er is dan geen factureren selecteren, veld "aantal te verplaatsen naar factuur" duidt te factureren aantal aan nood aan het factureren op basis van de effectief gepresteerde uren door de resources, effectief aangekochte (normaal 1 bij vaste prijs facturatie, 0 = nog niet materialen en effectief gemaakte onkosten. factureren)
- functie "verkoopfactuur maken" uitvoeren =>
In standaard Business Central ligt de basis voor facturatie in projectplanningsregels met regelsoort resultaat = ongeboekte verkoopfactuur, in projectplanningsregel update van veld "aantal “factureerbaar” en “budget en factureerbaar”, in de velden “aantal te verplaatsen naar factuur” (positief, overgebracht naar factuur" en mogelijkheid tot meestal 1) en “eenheidsprijs”. In de praktijk definieert men meestal per vaste prijs facturatieschijf een aparte doorklikken naar (on)geboekte verkoopfactuur
- boeken van ongeboekte verkoopfactuur =>
projectplanningsregel. resultaat = geboekte verkoopfactuur, projectpost (type = verkoop), grootboekposten, BTW post, Verschillende flows voor projectfacturatie – vaste prijs: (gedetailleerde) klantenpost, update van facturatie in projectplanningsregel (o.a. gefactureerd aantal).
- Projectfacturatie voor 1 project vanuit projectplanningsregels (correct invullen “aantal te verplaatsen
Commented [CP51]: Scenario voor maken naar factuur” – uitvoeren functie “verkoopfactuur maken” resulterend in ongeboekte verkoopfacturen via facturatiebatch - vaste prijs projectverkoopfactuur – boeken van projectverkoopfactuur) project:
- projectplanningsregel(s) manueel registreren :
- Projectfacturatie voor >1 factuur via batch “verkoopfactuur project maken” (correct invullen “aantal te regelsoort = factureerbaar, aantal = positief meestal
1, eenheidsprijs = te factureren verkoopprijs verplaatsen naar factuur” in projectplanningsregels – uitvoeren batch functie resulterend in (positief) verschillende ongeboekte projectverkoopfacturen – boeken van projectverkoopfacturen) •projectplanningsregel per schijf van facturatie aanmaken
- Opmerking : Manueel aanmaken van verkoopfactuur en regels koppelen aan project/taak is niet •projectplanningsregels die men wenst te
factureren : correct invullen veld "aantal te mogelijk (velden niet editeerbaar). Projectfacturatie is verplicht op basis van projectplanningsregels. verplaatsen naar factuur" (normaal 1 bij vaste prijs facturatie, 0 = nog niet factureren). Opmerking : via
##### 5.12.1.1 BC70.216.01 Projectfacturen maken - vaste prijs (Progressus) filtering in facturatiebatch kan men ook selectie
maken van te factureren projectplanningsregels. https://docs.progressussoftware.com/articles/Projects-how-invoice-projects.html#fixed-price
- batch "verkoopfactuur project maken" uitvoeren,
In Progressus zijn projectposten van soort “verkoop” en “factureerbaar = Ja” de basis voor projectfacturatie vaste eventueel filters invullen => resultaat = ongeboekte verkoopfacturen, in projectplanningsregel update prijs. van veld "aantal overgebracht naar factuur" en mogelijkheid tot doorklikken naar (on)geboekte Bij vaste prijs facturatie definieert men eerst de geplande (schijf)facturatie(s) met respectievelijk te factureren verkoopfactuur vaste prijs. Vanuit deze geplande (schijf)facturaties maakt men dan de projectposten soort “verkoop” aan, via •boeken van ongeboekte verkoopfacturen => resultaat = geboekte verkoopfactuur, projectpost functie “geplande (schijf)facturatie boeken”. Door geplande (schijf)facturatie te koppelen aan mijlpaal (type = verkoop), grootboekposten, BTW post, (milestone), kan die pas geboekt worden op voorwaarde dat de mijlpaal volledig voltooid is. (gedetailleerde) klantenpost, update van facturatie in projectplanningsregel (o.a. gefactureerd aantal).

Het aanmaken van projectfactuur kan dan op verschillende manieren:

- Via facturatievoorstel, met mogelijkheid om nog aanpassingen te doen (oa. uitstellen facturatie door
“goedgekeurd = Nee” zetten, aanpassen aantal te factureren, wijzigen “factureerbaar”)

- Direct via functie “projectfactuur maken”

- Ophalen van projectverbruik in ongeboekte verkoopfactuur

Het aangemaakte projectfactuur is een ongeboekte verkoopfactuur (met regels in overeenstemming met facturatie-instelling in het project). Deze ongeboekte verkoopfactuur kan indien nodig nog terug verwijderd worden, het boeken resulteert dan weer in een geboekte (project)verkoopfactuur en daarbijhorende posten (oa. klantenpost, projectpost met soort “verkoop”).

Projectfacturatie ondersteunt ook retentie, op basis van instelling retentie% in project(taak).

Schematische voorstelling van concept projectfacturatie vaste prijs:

#### 5.12.2 BS70.217 Projectfacturen maken - in regie
https://learn.microsoft.com/nl-be/dynamics365/business-central/projects-how-invoice-jobs

Bij in regie projecten is er nood aan het factureren op basis van de effectief gepresteerde uren door de resources, Commented [CP52]: Scenario voor maken effectief aangekochte materialen en effectief gemaakte onkosten. verkoopfacturen vanuit projectplanningsregels - in regie project: In standaard Business Central ligt de basis voor facturatie in projectplanningsregels met regelsoort •projectplanningsregel(s) manueel/automatisch registreren : regelsoort = "factureerbaar" of "budget “factureerbaar” en “budget en factureerbaar”, in de velden “aantal te verplaatsen naar factuur” (positief) en en factureerbaar", aantal = positief, eenheidsprijs = “eenheidsprijs”. te factureren verkoopprijs (positief)
- projectplanningsregels die men wenst te
Verschillende flows voor projectfacturatie – in regie: factureren selecteren, veld "aantal te verplaatsen naar factuur" duidt te factureren aantal aan ( 0 =
- Projectfacturatie voor 1 project vanuit projectplanningsregels (“aantal te verplaatsen naar factuur” nog niet factureren)
- functie "verkoopfactuur maken" uitvoeren =>
normaal niet aan te passen (automatisch ingevuld met effectief verbruik in “aantal”) – uitvoeren functie resultaat = ongeboekte verkoopfactuur, in “verkoopfactuur maken” resulterend in ongeboekte projectverkoopfactuur – boeken van projectplanningsregel update van veld "aantal overgebracht naar factuur" en mogelijkheid tot projectverkoopfactuur) doorklikken naar (on)geboekte verkoopfactuur
- boeken van ongeboekte verkoopfactuur =>
- Projectfacturatie voor >1 factuur via batch “verkoopfactuur project maken” (“aantal te verplaatsen naar resultaat = geboekte verkoopfactuur, projectpost
factuur” in projectplanningsregels normaal niet aan te passen (automatisch ingevuld met effectief (type = verkoop), grootboekposten, BTW post, (gedetailleerde) klantenpost, update van facturatie verbruik in “aantal”) – uitvoeren batch functie resulterend in verschillende ongeboekte in projectplanningsregel (o.a. gefactureerd aantal). projectverkoopfacturen – boeken van projectverkoopfacturen) Opmerking : Standaard is er geen controle tussen
- Opmerking : Manueel aanmaken van verkoopfactuur en regels koppelen aan project/taak is niet "geboekt aantal" (= verbruikt aantal) en "aantal te
verplaatsen naar factuur" + "aantal gefactureerd". Het mogelijk (velden niet editeerbaar). Projectfacturatie is verplicht op basis van projectplanningsregels. is dus mogelijk om meer te factureren dan verbruikt. Commented [CP53]: Scenario voor maken verkoopfacturen via facturatiebatch - in regie project:
- projectplanningsregel(s) manueel/automatisch
##### 5.12.2.1 BC70.217.01 Projectfacturen maken - in regie (Progressus)
registreren : regelsoort = "factureerbaar” of "budget https://docs.progressussoftware.com/articles/Projects-how-invoice-projects.html#time--material-tm en factureerbaar, aantal = positief, eenheidsprijs = te factureren verkoopprijs (positief) In Progressus zijn projectposten van soort “verkoop” en “factureerbaar = Ja” de basis voor projectfacturatie in •projectplanningsregels die men wenst te factureren : correct invullen veld "aantal te regie. verplaatsen naar factuur" (normaal 1 bij vaste prijs facturatie, 0 = nog niet factureren). Opmerking : via Bij in regie project genereert het systeem deze projectposten op basis van de projectverbruiken (artikelen, filtering in facturatiebatch kan men ook selectie resources, expenses). maken van te factureren projectplanningsregels.
- batch "verkoopfactuur project maken" uitvoeren,
Het aanmaken van projectfactuur kan dan op verschillende manieren: eventueel filters invullen => resultaat = ongeboekte verkoopfactuur, in projectplanningsregel update van
- Via facturatievoorstel, met mogelijkheid om nog aanpassingen te doen (oa. uitstellen facturatie door veld "aantal overgebracht naar factuur" en
mogelijkheid tot doorklikken naar (on)geboekte “goedgekeurd = Nee” zetten, aanpassen aantal te factureren, wijzigen “factureerbaar”) verkoopfactuur
- boeken van ongeboekte verkoopfactuur =>
- Direct via functie “projectfactuur maken”
resultaat = geboekte verkoopfactuur, projectpost (type = verkoop), grootboekposten, BTW post,
- Ophalen van projectverbruik in ongeboekte verkoopfactuur
(gedetailleerde) klantenpost, update van facturatie in projectplanningsregel (o.a. gefactureerd aantal). Het aangemaakte projectfactuur is een ongeboekte verkoopfactuur (met regels in overeenstemming met facturatie-instelling in het project). Deze ongeboekte verkoopfactuur kan indien nodig nog terug verwijderd Opmerking : Standaard is er geen controle tussen "geboekt aantal" (= verbruikt aantal) en "aantal te ...

worden, het boeken resulteert dan weer in een geboekte (project)verkoopfactuur en daarbijhorende posten (oa. klantenpost, projectpost met soort “verkoop”).

Projectfacturatie ondersteunt ook retentie, op basis van instelling retentie% in project(taak).

Schematische voorstelling van concept projectfacturatie in regie:

#### 5.12.3 BS70.319 Projectfacturatie volgens voortgang (meetstaten)
(Progressus) https://docs.progressussoftware.com/articles/Projects-how-invoice-projects.html#create-aia-compliant-billing- with-progress-billing

Progressus ondersteunt facturatie volgens voortgang.

Facturatie volgens voortgang omvat de volgende stappen:

- Definitie van meetstaat(regels), verschillende versies per meetstaatnr zijn mogelijk. Opeenvolgende
versies en meetstaatnummers starten met vorige meetstaatversie als basis.

- Vervolledigen van info in meetstaatregels in functie van facturatie (= %voltooiing, aantal voltooiing).

- Meetstaatdocument opleveren aan klant ter evaluatie/goedkeuring.

- Na goedkeuring meetstaat door klant, updaten status in meetstaat (= status “goedgekeurd”).

- Aanmaken van projectfactuur door uitvoeren functie “aanmaken factuur” vanuit meetstaat.

Het aangemaakte projectfactuur is een ongeboekte verkoopfactuur (met regels in overeenstemming met meetstaatregels). Deze ongeboekte verkoopfactuur kan indien nodig nog terug verwijderd worden, het boeken resulteert dan weer in een geboekte (project)verkoopfactuur en daarbijhorende posten (oa. klantenpost, projectpost met soort “verkoop”).

Projectfacturatie ondersteunt ook retentie, op basis van instelling retentie% in project(taak).

Schematische voorstelling van concept projectfacturatie volgens voortgang:

#### 5.12.4 BS70.320 Projectfacturatie volgens %voltooiing (Progressus)
https://docs.progressussoftware.com/articles/Projects-how-invoice-projects.html#percent-complete

Progressus ondersteunt facturatie volgens %voltooiing met de volgende opties:

- Niveau voor berekening van %voltooiing: project samenvatting, project detail, projecttaak
samenvatting, projecttaak detail

- Basis voor berekening van %voltooiing: kost in actieve budgetversie tov actuele gerealiseerde kost,
aantal in actieve budgetversie tov actueel gerealiseerd aantal

Het aanmaken van projectfactuur verloopt dan in de volgende stappen:

- Uitvoeren van functie “%voltooiing berekenen”

- Indien toegelaten kan dit berekend %voltooiing nog manueel aangepast worden

- Genereren van projectfactuur door uitvoeren van functie “aanmaken %voltooiing factuur”

Het aangemaakte projectfactuur is een ongeboekte verkoopfactuur (met regels in overeenstemming met ingestelde niveau voor berekening %voltooiing). Deze ongeboekte verkoopfactuur kan indien nodig nog terug verwijderd worden, het boeken resulteert dan weer in een geboekte (project)verkoopfactuur en daarbijhorende posten (oa. klantenpost, projectpost met soort “verkoop”).

Projectfacturatie ondersteunt ook retentie, op basis van instelling retentie% in project(taak).

Schematische voorstelling van concept projectfacturatie %voltooiing

Project %complete

Proj ledger entries (usage) Ac ve budget version

Calculate %complete

Generate %complete invoice

Sales invoice (unposted)

Posted sales invoice Proj ledger entries (sale) Proj ledger entries (sale + marked eten on invoicing as open reten on)

### 5.13 Project-verkoopcreditnota’s beheren Commented [CP54]: Deze paragraaf nog volledig te
herwerken.
#### 5.13.1 BS70.218 Project-creditnota's maken - vaste prijs
Het concept voor aanmaken van verkoopcreditnota voor een vaste prijs project is identiek aan projectverkoopfacturen: de projectplanningsregel(s) ifv creditering manueel registreren en dan verder verwerken in flow verkoopcreditnota.

Project-creditnota's maken - vanuit projectplanningsregels (vaste prijs)

De basis voor het genereren van project-verkoopcreditnota's zijn de projectplanningsregels met regelsoort "factureerbaar" en "budget en factureerbaar". Bij deze regelsoort zijn de volgende velden van toepassing:

- te factureren aantal = theoretisch aantal te factureren/crediteren, gelijk aan "aantal"

- aantal te verplaatsen naar factuur = aantal dat men wenst te factureren/crediteren bij facturatierun

- aantal overgebracht naar factuur = aantal dat aanwezig is in een ongeboekte of geboekte
verkoopfactuur/creditnota

- aantal gefactureerd = aantal dat effectief gefactureerd/gecrediteerd is, dus in geboekte
verkoopfactuur(en)/creditnota('s)

Scenario voor maken verkoopcreditnota vanuit projectplanningsregels - vaste prijs project:
- projectplanningsregel(s) manueel registreren : regelsoort = "factureerbaar", aantal = negatief meestal -
1, eenheidsprijs = te crediteren verkoopprijs (positief)

- projectplanningsregels die men wenst te crediteren selecteren, veld "aantal te verplaatsen naar
factuur" duidt te crediteren aantal aan (normaal -1 bij vaste prijs facturatie, 0 = nog niet factureren)

- functie "verkoopcreditnota maken" uitvoeren => resultaat = ongeboekte verkoopcreditnota en
mogelijkheid tot doorklikken naar (on)geboekte verkoopcreditnota

- boeken van ongeboekte verkoopcreditnota=> resultaat = geboekte verkoopcreditnota, projectpost
(type = verkoop, aantal = positief, kost = positief, eenheidsprijs = positief), grootboekposten, BTW post, (gedetailleerde) klantenpost, update van facturatie in projectplanningsregel (o.a. gefactureerd aantal).

Opmerking : Batch "verkoopfactuur project aanmaken" zal ook projectplanningsregels met negatief "aantal te verplaatsen naar factuur" verwerken, d.w.z. systeem genereert hiervoor ook een regel in de aangemaakte verkoopfactuur maar met omkering van het aantal. Indien het totaal van de gegenereerde project- verkoopfactuur positief is, dan zorgen de negatieve factuurregels voor vermindering van het factuurbedrag. Indien het totaal van de gegenereerde project-verkoopfactuur negatief is, dan kan dit factuur niet geboekt worden maar moeten de negatieve regels via functie "negatieve regels verplaatsen" getransfereerd worden in

een project-verkoopcreditnota. De batch "verkoopfactuur project aanmaken" dient dus niet om direct een project-verkoopcreditnota aan te maken.

Opmerking : Manueel aanmaken van verkoopcreditnota en regels koppelen aan project/taak is niet mogelijk (velden niet editeerbaar). Projectcreditering is verplicht op basis van projectplanningsregels.

##### 5.13.1.1 BC70.218.01 Project-creditnota’s maken – vaste prijs (Progressus)

#### 5.13.2 BS70.219 Project-creditnota's maken - in regie
Het concept voor aanmaken van verkoopcreditnota voor een in regie project is identiek aan projectverkoopfacturen: de projectplanningsregel(s) ifv creditering manueel registreren volgens het gewenste detailniveau en dan verder verwerken in flow verkoopcreditnota.

Project-creditnota's maken - vanuit projectplanningsregels (in regie)

De basis voor het genereren van project-verkoopcreditnota's zijn de projectplanningsregels met regelsoort "factureerbaar" en "budget en factureerbaar". Bij deze regelsoort zijn de volgende velden van toepassing: te factureren aantal = theoretisch aantal te factureren/crediteren, gelijk aan "aantal"

- aantal te verplaatsen naar factuur = aantal dat men wenst te factureren/crediteren bij facturatierun

- aantal overgebracht naar factuur = aantal dat aanwezig is in een ongeboekte of geboekte
verkoopfactuur/creditnota

- aantal gefactureerd = aantal dat effectief gefactureerd/gecrediteerd is, dus in geboekte
verkoopfactuur(en)/creditnota('s)

Scenario voor maken verkoopcreditnota vanuit projectplanningsregels - in regie project:
- projectplanningsregel(s) manueel registreren : regelsoort = "factureerbaar" of "budget en
factureerbaar", aantal = positief, eenheidsprijs = te factureren verkoopprijs (positief)

- projectplanningsregels die men wenst te crediteren selecteren, veld "aantal te verplaatsen naar
factuur" duidt te factureren aantal aan ( 0 = nog niet factureren)

- functie "verkoopcreditnota maken" uitvoeren => resultaat = ongeboekte verkoopcreditnota, in
projectplanningsregel update van veld "aantal overgebracht naar factuur" en mogelijkheid tot doorklikken naar (on)geboekte verkoopfactuur

- boeken van ongeboekte verkoopcreditnota => resultaat = geboekte verkoopcreditnota, projectpost
(type = verkoop, aantal = positief, kost = positief, eenheidsprijs = positief), grootboekposten, BTW post, (gedetailleerde) klantenpost, update van facturatie in projectplanningsregel (o.a. gefactureerd aantal).

Opmerking : Standaard is er geen controle tussen "geboekt aantal" (= verbruikt aantal) en "aantal te verplaatsen naar factuur" + "aantal gefactureerd". Het is dus mogelijk om meer te factureren/crediteren dan verbruikt/geretourneerd.

Opmerking: Batch "verkoopfactuur project aanmaken" zal ook projectplanningsregels met negatief "aantal te verplaatsen naar factuur" verwerken, d.w.z. systeem genereert hiervoor ook een regel in de aangemaakte verkoopfactuur maar met omkering van het aantal. Indien het totaal van de gegenereerde project- verkoopfactuur positief is, dan zorgen de negatieve factuurregels voor vermindering van het factuurbedrag. Indien het totaal van de gegenereerde project-verkoopfactuur negatief is, dan kan deze factuur niet geboekt worden maar moeten de negatieve regels via functie "negatieve regels verplaatsen" getransfereerd worden in een project-verkoopcreditnota. De batch "verkoopfactuur project aanmaken" dient dus niet om direct een project-verkoopcreditnota aan te maken.

Opmerking : Manueel aanmaken van verkoopcreditnota en regels koppelen aan project/taak is niet mogelijk (velden niet editeerbaar). Projectcreditering is verplicht op basis van projectplanningsregels.

##### 5.13.2.1 BC70.219.01 Projectcreditnota’s maken – in regie (Progressus)

#### 5.13.3 BS70.321 Projectcreditnota’s maken – volgens voortgang (Progressus)

#### 5.13.4 BS70.322 Projectcreditnota’s maken - %voltooiing (Progressus)

5.14Project-inkoopfacturen beheren Commented [CP55]: Deze paragraaf nog volledig herwerken
#### 5.14.1 BS70.220 Inkoopfacturen maken gekoppeld aan projecten
(vaste prijs) Inkoopfacturen worden gekoppeld aan een vaste prijs project door het invullen van project en projecttaak in een inkoopfactuurlijn.

Inkoopfacturen maken gekoppeld aan projecten (manueel) (vaste prijs)

Een inkoopfactuur die gerelateerd is aan een project, betekent ook dat deze kosten op het desbetreffende project moeten komen. Indien er geen inkooporder aan vooraf is gegaan, registreert men de inkoopfactuur manueel.

Scenario voor maken van inkoopfactuur gekoppeld aan een project (vaste prijs):

- Registreren van inkoopfactuurkop

- Registreren van inkoopfactuurregel : omwille van koppeling met project, in de regel ook invullen van

  - Project en projecttaak

  - Projectregelsoort = "budget" i.g.v vaste prijs project

  - Eenheidsprijs project : indien kost door te factureren aan klant van project, kan hier de
eenheidsprijs ingevuld worden

- Boeken van inkoopfactuur

- Resultaat : geboekte inkoopfactuur, grootboekposten, BTW post, (gedetailleerde) leverancierspost,
projectpost (type = verbruik, aantal = positief, totale kost = positief, totale verkoopprijs = positief), update van verbruik in projectplanningsregel (o.a. geboekt aantal, resterend aantal) of indien geen overeenstemmende projectplanningsregel(s) gevonden aanmaak van nieuwe projectplanningsregel (bij "gebruikslink = ja", regelsoort in nieuwe projectplanningsregel = "budget" (vaste prijs project) of "budget en factureerbaar" (in regie project)

Inkoopfacturen maken gekoppeld aan projecten via ophalen ontvangstregels (vaste prijs)

Een inkoopfactuur die gerelateerd is aan een project, betekent ook dat deze kosten op het desbetreffende project moeten komen. Indien er wel een inkooporder aan vooraf is gegaan dat eveneens gekoppeld is het project, kan men de ontvangstregels hiervan ophalen om de factuurregels te genereren.

Scenario voor maken van inkoopfactuur gekoppeld aan een project (vaste prijs), op basis van ophalen ontvangstregels
- Registreren van inkoopfactuurkop

- Registreren van inkoopfactuurregel : uitvoeren functie "ontvangstregels ophalen" => ook info m.b.t.
koppeling project uit geboekte inkoopontvangstregels wordt opgehaald voor generatie van inkoopfactuurregels

  - Project en projecttaak

  - Projectregelsoort = zelfde waarde als in geboekte inkoopontvangst, d.w.z. "budget"

  - Boeken van inkoopfactuur

- Resultaat : geboekte inkoopfactuur, grootboekposten, BTW post, (gedetailleerde) leverancierspost,
projectpost (type = verbruik, aantal = positief, totale kost = positief, totale verkoopprijs = positief), update van verbruik in projectplanningsregel (o.a. geboekt aantal, resterend aantal) of indien geen overeenstemmende projectplanningsregel(s) gevonden aanmaak van nieuwe projectplanningsregel (bij "gebruikslink = ja", regelsoort in nieuwe projectplanningsregel = "budget" (vaste prijs project) of "budget en factureerbaar" (in regie project)

#### 5.14.2 BS70.221 Inkoopfacturen maken gekoppeld aan projecten (in
regie) Inkoopfacturen worden gekoppeld aan een in regie project door het invullen van project en projecttaak in een inkoopfactuurlijn.

Inkoopfacturen maken gekoppeld aan projecten (manueel) (in regie)

Een inkoopfactuur die gerelateerd is aan een project, betekent ook dat deze kosten op het desbetreffende project moeten komen. Indien er geen inkooporder aan vooraf is gegaan, registreert men de inkoopfactuur manueel.

Scenario voor maken van inkoopfactuur gekoppeld aan een project (in regie):

- Registreren van inkoopfactuurkop

- Registreren van inkoopfactuurregel : omwille van koppeling met project, in de regel ook invullen van

  - Project en projecttaak

  - Projectregelsoort = "factureerbaar"

  - Eenheidsprijs project : indien kost door te factureren aan klant van project, kan hier de
eenheidsprijs ingevuld worden

- Boeken van inkoopfactuur

- Resultaat : geboekte inkoopfactuur, grootboekposten, BTW post, (gedetailleerde) leverancierspost,
projectpost (type = verbruik, aantal = positief, totale kost = positief, totale verkoopprijs = positief), update van verbruik in projectplanningsregel (o.a. geboekt aantal, resterend aantal) of indien geen overeenstemmende projectplanningsregel(s) gevonden aanmaak van nieuwe projectplanningsregel (bij "gebruikslink = ja", regelsoort in nieuwe projectplanningsregel = "budget" (vaste prijs project) of "budget en factureerbaar" (in regie project)

Inkoopfacturen maken gekoppeld aan projecten via ophalen ontvangstregels (in regie)

Een inkoopfactuur die gerelateerd is aan een project, betekent ook dat deze kosten op het desbetreffende project moeten komen. Indien er wel een inkooporder aan vooraf is gegaan dat eveneens gekoppeld is het project, kan men de ontvangstregels hiervan ophalen om de factuurregels te genereren.

Scenario voor maken van inkoopfactuur gekoppeld aan een project (in regie), op basis van ophalen ontvangstregels
- Registreren van inkoopfactuurkop

- Registreren van inkoopfactuurregel : uitvoeren functie "ontvangstregels ophalen" => ook info m.b.t.
koppeling project uit geboekte inkoopontvangstregels wordt opgehaald voor generatie van inkoopfactuurregels

  - Project en projecttaak

  - Projectregelsoort = zelfde waarde als in geboekte inkoopontvangst, d.w.z. "factureerbaar"

  - Eenheidsprijs project : indien kost door te factureren aan klant van project, kan hier de
eenheidsprijs ingevuld worden

- Boeken van inkoopfactuur

- Resultaat : geboekte inkoopfactuur, grootboekposten, BTW post, (gedetailleerde) leverancierspost,
projectpost (type = verbruik, aantal = positief, totale kost = positief, totale verkoopprijs = positief), update van verbruik in projectplanningsregel (o.a. geboekt aantal, resterend aantal) of indien geen overeenstemmende projectplanningsregel(s) gevonden aanmaak van nieuwe projectplanningsregel (bij "gebruikslink = ja", regelsoort in nieuwe projectplanningsregel = "budget" (vaste prijs project) of "budget en factureerbaar" (in regie project)

### 5.15 Project-inkoopcreditnota’s beheren Commented [CP56]: Deze paragraaf nog volledig
herwerken
#### 5.15.1 BS70.222 Inkoopcreditnota's maken gekoppeld aan projecten
(vaste prijs) Inkoopcreditnota's worden gekoppeld aan een vaste prijs project door het invullen van project en projecttaak in een inkoopfactuurlijn.

Inkoopcreditnota's maken gekoppeld aan projecten (manueel) (vaste prijs)

Een inkoopcreditnota die gerelateerd is aan een project, betekent ook dat deze kostenvermindering op het desbetreffende project moet komen. Indien er geen inkoopretourorder aan vooraf is gegaan, registreert men de inkoopcreditnota manueel.

Scenario voor maken van inkoopcreditnota gekoppeld aan een project (vaste prijs):

- Registreren van inkoopcreditnota-kop

- Registreren van inkoopcreditnotaregel: omwille van koppeling met project, in de regel ook invullen van

  - Project en projecttaak

  - Projectregelsoort = budget

- Boeken van inkoopcreditnota

- Resultaat : geboekte inkoopcreditnota, grootboekposten, BTW post, (gedetailleerde) leverancierspost,
projectpost (type = verbruik, aantal = negatief, totale kost = negatief, totale verkoopprijs = negatief), update van verbruik in projectplanningsregel (o.a. geboekt aantal, resterend aantal) of indien geen overeenstemmende projectplanningsregel(s) gevonden aanmaak van nieuwe projectplanningsregel (bij "gebruikslink = ja", regelsoort in nieuwe projectplanningsregel = "budget" (vaste prijs project) of "budget en factureerbaar" (in regie project)

Inkoopcreditnota's maken gekoppeld aan projecten via ophalen retourverzendregels (vaste prijs)

Een inkoopcreditnota die gerelateerd is aan een project, betekent ook dat deze kostenvermindering op het desbetreffende project moet komen. Indien er wel een inkoopretourorder aan vooraf is gegaan dat eveneens gekoppeld is het project, kan men de retourverzendregels hiervan ophalen om de creditnotaregels te genereren.

Scenario voor maken van inkoopcreditnota gekoppeld aan een project (vaste prijs), op basis van ophalen retourverzendregels

- Registreren van inkoopcreditnota-kop

- Registreren van inkoopcreditnotaregel: uitvoeren functie "retourverzendregels ophalen" => ook info
m.b.t. koppeling project uit geboekte inkoopretourverzending wordt opgehaald voor generatie van inkoopcreditnotaregels

  - Project en projecttaak

  - Projectregelsoort = zelfde waarde als in geboekte inkoopretourverzending, d.w.z. "budget"

- Boeken van inkoopcreditnota

- Resultaat : geboekte inkoopcreditnota, grootboekposten, BTW post, (gedetailleerde) leverancierspost,
projectpost (type = verbruik, aantal = negatief, totale kost = negatief, totale verkoopprijs = negatief), update van verbruik in projectplanningsregel (o.a. geboekt aantal, resterend aantal) of indien geen overeenstemmende projectplanningsregel(s) gevonden aanmaak van nieuwe projectplanningsregel (bij "gebruikslink = ja", regelsoort in nieuwe projectplanningsregel = "budget" (vaste prijs project) of "budget en factureerbaar" (in regie project)

#### 5.15.2 BS70.223 Inkoopcreditnota's maken gekoppeld aan projecten
(in regie) Inkoopcreditnota's worden gekoppeld aan een in regie project door het invullen van project en projecttaak in een inkoopfactuurlijn.

Inkoopcreditnota's maken gekoppeld aan projecten (manueel) (in regie)

Een inkoopcreditnota die gerelateerd is aan een project, betekent ook dat deze kostenvermindering op het desbetreffende project moet komen. Indien er geen inkoopretourorder aan vooraf is gegaan, registreert men de inkoopcreditnota manueel.

Scenario voor maken van inkoopcreditnota gekoppeld aan een project (in regie):

- Registreren van inkoopcreditnota-kop

- Registreren van inkoopcreditnotaregel: omwille van koppeling met project, in de regel ook invullen van

  - Project en projecttaak

  - Projectregelsoort = "factureerbaar"

  - Eenheidsprijs project : indien kost door te crediteren aan klant van project, kan hier de
eenheidsprijs ingevuld worden

- Boeken van inkoopcreditnota

- Resultaat : geboekte inkoopcreditnota, grootboekposten, BTW post, (gedetailleerde) leverancierspost,
projectpost (type = verbruik, aantal = negatief, totale kost = negatief, totale verkoopprijs = negatief), update van verbruik in projectplanningsregel (o.a. geboekt aantal, resterend aantal) of indien geen overeenstemmende projectplanningsregel(s) gevonden aanmaak van nieuwe projectplanningsregel (bij "gebruikslink = ja", regelsoort in nieuwe projectplanningsregel = "budget" (vaste prijs project) of "budget en factureerbaar" (in regie project)

Inkoopcreditnota's maken gekoppeld aan projecten via ophalen retourverzendregels (in regie)

Een inkoopcreditnota die gerelateerd is aan een project, betekent ook dat deze kostenvermindering op het desbetreffende project moet komen. Indien er wel een inkoopretourorder aan vooraf is gegaan dat eveneens gekoppeld is het project, kan men de retourverzendregels hiervan ophalen om de creditnotaregels te genereren.

Scenario voor maken van inkoopcreditnota gekoppeld aan een project (in regie), op basis van ophalen retourverzendregels

- Registreren van inkoopcreditnota-kop

- Registreren van inkoopcreditnotaregel: uitvoeren functie "retourverzendregels ophalen" => ook info
m.b.t. koppeling project uit geboekte inkoopretourverzending wordt opgehaald voor generatie van inkoopcreditnotaregels

  - Project en projecttaak

  - Projectregelsoort = zelfde waarde als in geboekte inkoopretourverzending, d.w.z. "factureerbaar"

  - Eenheidsprijs project : indien kost door te crediteren aan klant van project, kan hier de
eenheidsprijs ingevuld worden

- Boeken van inkoopcreditnota

- Resultaat : geboekte inkoopcreditnota, grootboekposten, BTW post, (gedetailleerde) leverancierspost,
projectpost (type = verbruik, aantal = negatief, totale kost = negatief, totale verkoopprijs = negatief), update van verbruik in projectplanningsregel (o.a. geboekt aantal, resterend aantal) of indien geen overeenstemmende projectplanningsregel(s) gevonden aanmaak van nieuwe projectplanningsregel (bij "gebruikslink = ja", regelsoort in nieuwe projectplanningsregel = "budget" (vaste prijs project) of "budget en factureerbaar" (in regie project)

### 5.16 Projectcontracten (Progressus) Commented [CP57]: Deze paragraaf nog volledig te
herwerken
#### 5.16.1 BS70.322 Projectcontracten – algemeen
Een contract kan worden gebruikt om meerdere projecten samen te factureren of kan worden gebruikt om projecten te groeperen voor rapportering. Dit maakt het mogelijk om o.a. zeer grote projecten op een overzichtelijke manier te beheren.

Er is het niveau van de contracten en dat van de projecten, niet meer of minder.

Aan een contract worden één of meerdere projecten toegewezen.

Het project wordt op de projectkaart toegewezen aan het contract en de contracttaak. Er kunnen meerdere projecten toegewezen worden aan één taakregel van een contract. Dit is ook een manier om meerdere projecten te groeperen.

Er kunnen goedkeuringsregels ingesteld worden op een contract met één of meer goedkeurders voor wijzigingen aan het contract zelf.

De startdatum wordt handmatig ingesteld op het contract. De reden hiervoor is dat een contract vaak een wettelijke overeenkomst met de klant vertegenwoordigt. He contract kan bijv. starten op 01/01, maar de projecten zelf later.

Op de contractkaart worden individuele contractinstellingen geconfigureerd. De velden op de contractkaart hebben naast op de begin- en einddatum van contracten invloed op de revisiedata, contractbudgetten en - goedkeurders, contractgoedkeuringen, contractbedragen, configuratieopties voor buitenlandse handel, facturatie- en boekingsopties en de instelling van contractrechten.

Op het contractplan zijn de zaken te zien die te maken hebben met het contract- en contracttaakconfiguratie. Specifieke zaken zijn contracttaken, budgetbedragen, bedragen van verbruiken, totaal voltooiingspercentage, enz. Dit is een van de belangrijkste schermen die managers en accountants gebruiken om de status van de contracten te bekijken.

#### 5.16.2 BS70.323 Projectcontractbudgetten
Voor contracten kunnen budgetversies opgesteld worden. Deze kunnen een goedkeuringshiërarchie hebben, zodat wijzigingen in budgetten goedkeuring vereisen.

Zodra een budget is aangemaakt en ter goedkeuring is ingediend, kunnen de goedkeurders het contractbudget goedkeuren of afkeuren.

#### 5.16.3 BS70.324 Projectcontracten & change order
Voor wijzigingen aan het contract kan een contract change order verstuurd worden. Er kunnen contracttaken worden toegewezen aan dit contract change order.

Zodra de change order is voltooid, kan worden verdergegaan met de verwerking van de geselecteerde change order: opmerkingen of bijlagen toevoegen / budgetmatrix, budgetmatrix met capaciteit of het budgetjournaal aanpassen / indienen ter goedkeuring of de goedkeuringsgeschiedenis bekijken.

De status op de change order kaart specifieert of deze is goedgekeurd, afgewezen of in behandeling is.

Als een contract is geconfigureerd om goed te keuren, lopen goedkeuringen of afkeuringen via de contract change order goedkeuringspagina. Het goedkeuringsproces werkt op een vergelijkbare manier als het goedkeuren van tijdsregistraties of onkosten. Wanneer u de pagina opent, kunt u filters invoeren om de change orders te beperken die in het onderste gedeelte van de pagina verschijnen.

Terwijl u boven aan de pagina criteria selecteert, worden de resultaten onder aan de pagina dynamisch bijgewerkt. U kunt dan de opties in het lint bovenaan de pagina gebruiken om de change orders verder te verwerken (selectie goedkeuren / alles goedkeuren / selectie afwijzen / alles afwijzen / opmerkingen en/of bijlagen toevoegen).

#### 5.16.4 BS70.325 Projectcontractfacturatie
Er kunnen gecombineerde facturen gemaakt worden voor alle projecten in het contract, met alle boekingen voor de verschillende projecten in één factuur.

Het niveau van detail of groepering op een factuur kan bepaald worden.

### 5.17 Projecten & onderaanneming Commented [CP58]: Deze paragraaf nog volledig te
herwerken. Aan bod gekomen in BPA fase bij SBE (maar wat in SBE
#### 5.17.1 BS70.326 Projecten & onderaanneming (Progressus) BPA doc uitgeschreven = niet te gebruiken in BPA
template)

### 5.18 Projecten & subscriptie Commented [CP59]: Deze paragraaf nog volledig te
herwerken Nog niet aan bod gekomen in BPA fase, dus ook nog
#### 5.18.1 BS70.327 Projecten & subscriptie niet geïmplementeerd

### 5.19 Projecten afsluiten
#### 5.19.1 BS70.224 Projecten afsluiten
Eenmaal het project is afgerond, alle taken uitgevoerd en alles gefactureerd, dan moet het project afgesloten worden. Alle OHW die al geboekt is op het grootboek moet op dit moment ook gecorrigeerd worden.

U sluit een project af door de status ervan op "voltooid" te zetten. Het systeem maakt de gebruiker dan ook attent op acties uit te voeren in kader van OHW.

### 5.20 Beheer periodieke taken
#### 5.20.1 BS70.225 Artikelkosten project bijwerken
De kostprijs van een artikel bij inkoopontvangst kan verschillen van de kostprijs bij facturatie, welke uiteindelijk de juiste kostprijs is. Om een juiste kost op projectniveau te hebben, is het nodig om de bestaande projectpost te updaten met de kostprijs bij facturatie. Deze update is gekoppeld aan "kostprijs herwaarderen - artikelposten": resulteert deze batch in update van kost in artikelpost die verbruikt is in project, dan moet de projectpost ook

die kostupdate krijgen. De batch "artikelkosten project bijwerken" zorgt voor update van artikelkost in projectposten in overeenstemming met de kost in artikelpost.

Opmerking : In projectinstellingen, parameter "artikelkosten project automatisch bijwerken" : hier kan je instellen of artikelkosten op project wel of niet automatisch moeten bijgewerkt worden, bij wijziging van kost in batch "kostprijs herwaarderen - artikelposten". Toch blijft het aanbevolen om voor maandafsluiting/rapportering, deze batch ook nog eens manueel uit te voeren. Commented [CP60]: @Niels Habraken Ik heb dit geschrapt => zit nu al in BS70.216+217 Commented [CP61]: @Niels Habraken Ik heb dit
### 5.21 Projecten & opstartsituatie openen geschrapt => zit nu al in BS70.206
Commented [CP62]: @Niels Habraken Ik heb dit
#### 5.21.1 BS70.202 Projecten opstartsituatie openen geschrapt => zit nu al in BS70.206

Voor lopende projecten waarop al verbruiken en/of facturaties zijn uitgevoerd, moet het project niet alleen aangemaakt worden maar ook "geopend" worden. Door deze projectopening legt men de situatie van verbruiken, facturaties, verwachte kosten (project gerelateerde inkooptransacties) vast, zodat projectopvolging verder kan gezet worden onder nieuwe projectdefinitie.

De opstartsituatie van een project voor verbruiken en uitgevoerde facturaties, meestal gesplitst over artikelen, resources, diverse kosten, kan geregistreerd worden met totale waarden maar ook meer gedetailleerd. De projectopening verloopt altijd via een projectdagboek, na registratie en boeking van de projectdagboekregels genereert het systeem dan de overeenkomstige projectposten (zonder grootboekposten).

### 5.22 Projectrapportering
#### 5.22.1 BS70.331 Projectrapportering in Business Central Commented [CP63]: Deze paragraaf nog volledig te
herwerken. Volgende rapporten zijn beschikbaar: Opsomming van rapporten nog correct ? Eigenlijk wel nodig om deze rapporten op te lijsten ? Ik zou het Project detailrapporten zeker niet zo uitgebreid doen.

· Actieve Projecten: rapport om een lijst te krijgen van projecten waarvan de status is ingesteld op Actief.

· Milestones: rapport om een lijst met milestones voor alle projecten te krijgen.

· Project - Journaal: rapport om de projectjournaalposten te bekijken.

· Taakdetail Grootboek: rapport om gedetailleerde boekingen per taak te zien.

· Uitbetalingsverzoeken: rapport uit om alle uitbetalingsverzoeken van onderaannemers te bekijken.

Project overzichtsrapporten

· Winstoverzicht: rapport om een winstoverzicht per project te bekijken.

· Taakoverzicht: rapport om een winstoverzicht per taak te bekijken.

· Arbeidskostenoverzicht: rapport uit om een samenvatting van de kosten van resources te zien.

· Inkomstenoverzicht: rapport om inkomsten per project te bekijken.

Contracten

· Contracttaakoverzicht: rapport om samengevatte projectinformatie per contracttaak te bekijken.

Projectbudget

· Budgetvergelijking: rapport om resultaten voor verschillende budgetversies te vergelijken.

· Budgethoeveelheid: rapport om de budgethoeveelheid per project te zien.

Project facturatie

· Facturatievoorstel: rapport om artikelen te tonen die klaar zijn om te factureren per project. Items die in dit rapport verschijnen kunnen bijvoorbeeld in rekening te brengen onkosten of invoer van tijdsregistraties bevatten.

· De resultaten worden verder uitgesplitst naar facturen op basis van tijd en materiaal versus geplande facturen.

· Niet gefactureerd rapport: rapport om alle niet gefactureerde artikelen per project weer te geven. Niet gefactureerde artikelen kunnen transacties omvatten die eerder gedeeltelijk werden gefactureerd.

· Verkoop retentie: rapport om verkoop retentie boekingen te bekijken. Deze worden gegenereerd uit geboekte verkoopfacturen waar een retentie percentage is gespecificeerd voor het boeken. Zodra de verkoopfactuur is geboekt, verschijnt de retentieregel in dit rapport.

· Ongeboekte geplande facturen: rapport om alle geplande facturen te tonen die nog niet werden geboekt.

· Projecten zonder facturatie instellingen: rapport om alle projecten te tonen waarvoor de facturatie nog niet is voltooid.

Tijdsregistratie rapporten

· Tijdsregistratie rapport: rapport om de tijdsregistraties van resources te bekijken.

· Tijdsregistratie goedkeuring rapport: rapport om informatie over de goedkeuring van tijdsregistraties te bekijken:

  - Status: hier kan je zien op welk goedkeuringsniveau de tijdsregistratie nog wacht op goedkeuring

  - Goedgekeurd: hier zie je op welk goedkeuringsniveau de tijdsregistratie reeds werd goedgekeurd.

· Tijdsregistratie factureerbaar vs. niet-factureerbaar: rapport om data van tijdsregistraties te vergelijken van resources m.b.t. het factureerbaar zijn of niet.

Onkosten rapporten

· Project onkostendetails: rapport om de details van project onkosten te bekijken.

· Goedgekeurde onkosten: rapport om goedgekeurde onkosten per resource te bekijken.

· Goedgekeurde onkosten MC: rapport om goedgekeurde onkosten per resource in meerdere valuta (Multi Currency) te bekijken.

Via resource rapporten zijn deze rapporten beschikbaar:

· Resource lijst: rapport om een lijst met resources te bekijken.

· Resource statistieken: rapport om eenheid- en dollar statistieken per resource te bekijken.

· Kostenuitsplitsing: rapport om de kosten per resource te bekijken.

· Budget vs. Werkelijk: rapport om een vergelijking van het projectbudget met de werkelijke bedragen te bekijken.

· Resterende capaciteit: rapport om de resterende resource capaciteit te bekijken in vergelijking met de gebudgetteerde eenheden.

· Resource capaciteit t.o.v. budget: rapport om de resource capaciteit te tonen in vergelijking met gebudgetteerde eenheden.

· Matrix resource planning: rapport om de resource planning te tonen, waarbij kan gefilterd worden op de velden in de matrix met resource capaciteit.

· Tijdsregistratie status analyse: rapport om de invoer per tijdsregistratie status te analyseren, gepresenteerd in een resource matrix overzicht.

· Verbruik analyse: rapport om geboekte tijdsregistraties te analyseren, gepresenteerd in een resource matrix.

· Werklast & Beschikbaarheid: rapport om budget- en planningsboekingen te analyseren met extra filters om de weergave te beperken.

Commented [CP64]: Deze paragraaf nog volledig te
#### 5.22.2 BS70.332 Projectrapportering met Power BI herwerken.
Opsomming van BI rapporten nog correct ? Eigenlijk Progressus Advanced Projects voorziet standaard een aantal Power BI dashboards: wel nodig om deze rapporten op te lijsten ?

· Project Overview

· Resource Overview

· Overall Business Report

· S-curve

· TT_Hours by task

· TT_Time entry by resource

· TT_Backlog and Pipeline

Uiteraard moet een Power BI licentie beschikbaar zijn om van deze functionaliteit gebruik te kunnen maken.

Ifv de perfomantie is het best om Business Central ’s nachts automatisch te laten updaten. Dit betekent dan ook dat de beschikbare data max. een dag oud is.

### 5.23 Project Document Lay-outs Commented [CP65]: Deze paragraaf nog volledig te
herwerken
#### 5.23.1 Inkooporder
Document lay-out voor project specifiek inkooporder = idem lay-out gewoon inkooporder, zie hoofdstuk “Inkoop”.

#### 5.23.2 Projectofferte

#### 5.23.3 Projectorderbevestiging

#### 5.23.4 Vorderingsstaat

#### 5.23.5 Projectfactuur

#### 5.23.6 Projectcreditnota
