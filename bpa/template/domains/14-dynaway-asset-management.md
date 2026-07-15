## 14. Dynaway Asset Management
Dynaway EAM voor Business Central is een Enterprise Asset Management (EAM) module die helpt bij het beheren van activa (Assets) en onderhoudstaken binnen D365BC. De oplossing is ontwikkeld door Dynaway en integreert met verschillende modules in D365BC. EAM-BC maakt het mogelijk om onderhoud en service van verschillende soorten apparatuur in een bedrijf efficiënt te beheren.

Assets kunnen in een hiërarchische structuur worden aangemaakt en gekoppeld aan locaties. Onderhoudstaken (werkorders) kunnen op elk niveau in de asset-hiërarchie worden gepland.

### 14.1 General Setup
#### 14.1.1 Installatie en licentiebeheer
Dynaway EAM kan worden geïnstalleerd vanuit Microsoft AppSource of vanuit Business Central in een cloud omgeving (zie Installation and License).

Via Dynaway EAM Licenietinformatie in Business Central kan je licentiegegevens instellen en beheren, zoals contactinformatie en het aantal gelicentieerde gebruikers.

Dynaway biedt verschillende licentieplannen, afhankelijk van je vereisten voor het aantal gebruikers, assets en extra functionaliteiten (zie Licentieplannen).

#### 14.1.2 Vereisten in Business Central
Om aan de slag te gaan met het beheren van Assets en Work Orders (werkorders) in Dynaway EAM voor Business Central, is een basisconfiguratie in het systeem noodzakelijk. Afhankelijk van de gewenste onderhoudsworkflow zijn er verschillende scenario’s mogelijk. Deze instellingen zijn te vinden via de volgende link: Basic setup requirements in Business Central.

#### 14.1.3 Begeleide instelling (Assisted Setup)
De Assisted Setup-wizards van Dynaway helpen bij een snelle en gestructureerde opstart van Dynaway EAM in Business Central. Deze stap is essentieel bij een eerste implementatie en maakt het eenvoudig om basisgegevens in te stellen of bestaande data te migreren (zoals assets, werkorders en gebruikers).

#### 14.1.4 Gebruikersbeheer
Profielen, Gebruikers en Machtigingensets

Er zijn verschillende standaard Dynaway profielen beschikbaar (bijvoorbeeld: Asset Manager, Asset Technieker, …). Deze zijn net zoals in standaard Business Central aanpasbaar via personaliseren.

Stel gebruikers en gebruikersgroepen in die gemachtigd zijn om Dynaway EAM voor Business Central te gebruiken. Gebruikers hebben specifieke machtigingssets op hun gebruikerskaart. Er bestaan standaardsets per rol, maar je kan zelf aangepaste sets maken via standaard Business Central.

Light Users hebben beperkte toegang, bv. alleen registreren van downtime of werkorders, maar geen bewerkingen/boekingen.

Resources en resourcegroepen

Stel via standaard Business Central de resources (personen of machines) in die beschikbaar moeten zijn voor het werkplanningsproces binnen de onderhoudsafdeling:

- Minstens één resourcegroep, bijvoorbeeld "Onderhoudsteam", voor interne resources (Asset
Techniekers). Indien nodig kun je de Asset Techniekers onderverdelen in meerdere groepen of teams. Als je externe aannemers inschakelt voor onderhoudswerkzaamheden, kun men ook een specifieke groep voor dat doel aanmaken.

- De dagelijkse capaciteit (beschikbare werkuren) per resource.

Onderhoudswerknemers (Maintenance Employees)

Onderhoudsmedewerkers zijn de werknemers in het bedrijf die verantwoordelijk zijn voor het uitvoeren van onderhoudswerkzaamheden. Onderhoudswerknemers kunnen ingesteld worden als individuele gebruikers of als gebruikersgroepen. Het gebruik van een gebruikersgroep maakt het mogelijk om werk toe te wijzen aan een hele groep, bijvoorbeeld als werk gepland dient te worden voor een groep lassers die allemaal over een specifiek lascertificaat beschikken. Werkorders kunnen ook toegewezen worden aan specifieke gebruikers, zoals techniekers.
