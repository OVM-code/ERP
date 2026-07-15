# RapidStart-training — migratie in eigen handen (sessievoorbereiding)

> De training die de klant in staat stelt de eigen datamigratie uit te voeren.
> Zelfde formaat als een gewone sessieprep; hoort bij module "migratie" in het
> trainingstraject.

| | |
|---|---|
| Doelgroep | data-eigenaars klant (per entiteit) + eindverantwoordelijke |
| Duur | 3u (1u concept + 2u hands-on met eigen data) |
| Omgeving | FLORAX-TEST — bedrijf FLORAX |
| Status | voor te bereiden |

## 1. Leerdoelen

Na deze sessie kan elke data-eigenaar zelfstandig: een configuratiepakket
exporteren naar Excel, vullen volgens het entity-workbook, importeren, foutregels
lezen en oplossen, en de validatiechecklist van het workbook uitvoeren.

## 2. Voor te bereiden (consultant)

- [ ] Configuratiepakketten aangemaakt per entiteit in scope (kolommen = workbook-mapping)
- [ ] Entity-workbooks (`entities/*.md`) gereviewd en gedeeld met de eigenaars
- [ ] Bronbestand-extracten van de klant ontvangen (echte data — geen oefendata)
- [ ] Sandbox-kopie waarin fouten maken veilig is

## 3. Te doorlopen (demo-script)

| # | Wat tonen | Let op |
|---|---|---|
| 1 | Pakket exporteren → Excel-structuur uitleggen (kolommen = workbookmapping) | kolommen nooit hernoemen |
| 2 | 10 records van de eigen bron invullen volgens de mapping | transformatieregels uit het workbook |
| 3 | Importeren → validatiefouten tonen en één samen oplossen | foutregels lezen = de kernvaardigheid |
| 4 | Toepassen → record in BC openen en controleren | koppeling met validatiechecklist |

## 4. Oefeningen

| # | Opdracht | Verwacht resultaat |
|---|---|---|
| O1 | Laad 25 records van je eigen entiteit uit het echte bronbestand | import zonder foutregels |
| O2 | Introduceer bewust 2 fouten (leeg verplicht veld, fout formaat) en los ze op | foutregels begrepen en opgelost |
| O3 | Voer §3 van je workbook (validatiechecklist) uit op je 25 records | checklist afgevinkt, afwijkingen genoteerd |

## Logboek (na de sessie)

- Aanwezig: | Parkeerpunten: | Afspraken per entiteit (deadlines trial load):
