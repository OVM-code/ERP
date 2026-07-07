# Entiteit: <naam> — migratieworkbook

> Eén workbook per entiteit. De assistant genereert de mappingtabel en de
> validatiechecklist; de **klant** vult, schoont en laadt; de consultant keurt op
> de checkpoints. Configuratiepakket: <RapidStart-pakketcode>.

| | |
|---|---|
| BC-tabel(len) | <bv. Customer (18)> |
| Configuratiepakket | <pakketcode + relevante velden> |
| Bron | <systeem/bestand> · volume: <n> records |
| Eigenaar (klant) | |
| Status | te starten |

## 1. Veldmapping

| Bronveld | BC-veld (pakketkolom) | Transformatie / regel | Verplicht |
|---|---|---|---|
| <naam> | Name | trim, max 100 | ja |
| <btwnr> | VAT Registration No. | formaat BE0999999999 | ja |

## 2. Schoningsregels (vóór het vullen van het pakket)

- [ ] Duplicaten samengevoegd (regel: <matchcriterium>)
- [ ] Inactieve records verwijderd (regel: <bv. geen transactie sinds 20XX>)
- [ ] Verplichte velden 100% gevuld; formaten toegepast (postcodes, BTW-nrs, e-mail)
- [ ] Sleutels/nummering afgestemd op de BC-nummerreeks (zie setup-plan)

## 3. Validatiechecklist (na elke load — trial én final)

- [ ] Aantal geladen records = aantal in bronbestand (tel beide, noteer hieronder)
- [ ] Pakketimport zonder foutregels (of: elke foutregel verklaard en opgelost)
- [ ] Steekproef <n> records veld-per-veld vergeleken met de bron
- [ ] Entiteitspecifieke controles: <bv. som openstaande posten = saldo oude boekhouding>
- [ ] Gerelateerde functionaliteit werkt: <bv. order maken op geladen klant lukt>

## 4. Load-log

| Datum | Omgeving | Records bron | Records geladen | Fouten | Uitgevoerd door |
|---|---|---|---|---|---|
