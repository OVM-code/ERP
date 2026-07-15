# Entiteit: Openstaande posten — migratieworkbook

| | |
|---|---|
| BC-tabel(len) | via dagboeken (Gen. Journal) — klant- en leveranciersposten |
| Configuratiepakket | FLX-OPEN (dagboekregels) |
| Bron | oude boekhouding, saldilijst per cutoverdatum · volume: ±380 posten |
| Eigenaar (klant) | hoofdboekhouder |
| Status | te starten |

## 1. Veldmapping

| Bronveld | BC-veld (pakketkolom) | Transformatie / regel | Verplicht |
|---|---|---|---|
| Relatie | Account No. | moet bestaan (klanten/leveranciers eerst geladen) | ja |
| Factuurnr | External Document No. | overnemen | ja |
| Factuurdatum / vervaldatum | Posting Date / Due Date | origineel behouden (aging correct) | ja |
| Openstaand bedrag | Amount | saldo per cutover, niet oorspronkelijk bedrag | ja |
| Tegenrekening | Bal. Account No. | migratietussenrekening <rek> | ja |

## 2. Schoningsregels

- [ ] Saldilijst getrokken op de afgesproken cutoverdatum, afgestemd met accountant
- [ ] Disputen/oninbare posten gemarkeerd en apart beslist (niet stilzwijgend mee)
- [ ] Creditnota's gekoppeld aan hun factuur waar mogelijk

## 3. Validatiechecklist

- [ ] Som geladen klantposten = saldo debiteuren oude boekhouding (op de cent)
- [ ] Som geladen leveranciersposten = saldo crediteuren oude boekhouding
- [ ] Migratietussenrekening loopt op nul na beide loads
- [ ] Aging-rapport BC ≈ aging oude boekhouding (steekproef 10 oudste posten)
- [ ] Functioneel: betaling afpunten op een geladen post lukt

## 4. Load-log

| Datum | Omgeving | Records bron | Records geladen | Fouten | Uitgevoerd door |
|---|---|---|---|---|---|
