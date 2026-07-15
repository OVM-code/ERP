# Entiteit: Klanten — migratieworkbook

| | |
|---|---|
| BC-tabel(len) | Customer (18) + Customer Bank Account |
| Configuratiepakket | FLX-KLANT |
| Bron | oude ERP (export) + Excel-prijsafspraken · volume: ±420 records |
| Eigenaar (klant) | verkoop binnendienst |
| Status | te starten |

## 1. Veldmapping

| Bronveld | BC-veld (pakketkolom) | Transformatie / regel | Verplicht |
|---|---|---|---|
| KlantNr | No. | overnemen (past in nummerreeks KLA*) | ja |
| Naam | Name | trim, max 100 | ja |
| BTW | VAT Registration No. | formaat BE0999999999, valideren | ja |
| Kanaal | Gen. Bus. Posting Group + Customer Price Group | RETAIL → RETAIL / rest → WEBSHOP of DIRECT | ja |
| Betaalcond | Payment Terms Code | mapping tabel: 30D→30 DAGEN, 8D2%→8D-SKONTO | ja |
| Leveradressen | Ship-to Address (subtabel) | één regel per adres | nee |

## 2. Schoningsregels (vóór het vullen van het pakket)

- [ ] Duplicaten samengevoegd (match: BTW-nummer)
- [ ] Klanten zonder verkoop sinds 2024 niet migreren (± 60 st — lijst bewaren)
- [ ] Verzendadvies per kanaal gezet: retail = volledig, overige = deellevering (BPA BS25.206)
- [ ] GLN-nummers retailketens aangevuld (nodig voor GAP-2)

## 3. Validatiechecklist (na elke load — trial én final)

- [ ] Aantal geladen = aantal in bron (tellen, noteren in log)
- [ ] Import zonder foutregels, of elke foutregel verklaard
- [ ] Steekproef 20 klanten veld-per-veld vergeleken
- [ ] Specifiek: beide retailketens hebben GLN + verzamelfactuur-instelling
- [ ] Functioneel: verkooporder maken op een geladen klant → juiste prijslijst en verzendadvies

## 4. Load-log

| Datum | Omgeving | Records bron | Records geladen | Fouten | Uitgevoerd door |
|---|---|---|---|---|---|
