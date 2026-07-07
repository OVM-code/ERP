# Scope matrix — Bakkerij Florax (demo)

> Scenario's uit de workshops. Gedocumenteerde scenario's (content/) worden bij de
> build automatisch aangevuld; onderstaande tabel bevat de expliciete beslissingen,
> inclusief wat **buiten scope** valt en waarom.

| Code | Scenario | Domein | Scope | Invulling | Toelichting |
|---|---|---|---|---|---|
| BS25.101 | Beheren verkoopprijzen | 2 | in | standaard | Prijslijsten + promoperiodes vervangen Excel |
| BS25.202 | Verkooporders maken | 2 | in | standaard | Drie kanalen, één orderstroom |
| BS25.328 | Ordertoezegging | 2 | in | standaard | Haalbaarheid leverdatum retail bij ingave |
| BS25.206 | Beheer van backorders | 2 | in | standaard | Kanaalafhankelijk via verzendadvies |
| BS25.213 | Verkoopfacturen maken | 2 | in | standaard | Verzamelfactuur retail wekelijks; lay-out zie GAP-2 |
| BS25.200 | Verkoopoffertes maken | 2 | uit | | Geen offertetraject: vaste prijslijsten |
| BS25.900 | Advanced pricing (Aptean) | 2 | uit | | Standaard prijslijsten volstaan (herbekijken bij bonusafspraken) |
| BS50.100 | Artikelen beheren | 4 | in | standaard | FIFO, houdbaarheidsformules |
| BS50.104 | Artikeltraceringscodes beheren | 4 | in | standaard | LOT-VOLLEDIG voor traceerplichtige artikelen |
| BS45.904 | Lot management | 4 | in | add-on: Aptean Food & Beverage | Traceringscockpit; recall < 4 u |
| BS45.902 | Expiration management | 4 | in | add-on: Aptean Food & Beverage | FEFO + 2/3-resthoudbaarheidsregel retail |
| BS45.200 | Artikelen blokkeren | 4 | in | workaround | QC-vrijgave via lotstatussen, geen labomodule |
| BS40.900 | Catch weight | 4 | uit | | Alles op stuks/dozen — geen variabel gewicht |
| BS65.200 | Inkoopfacturen maken | 10 | in | standaard | Via OCR-variant (BC65.200.04) |
| BS65.204 | Inkoopfacturen boeken | 10 | in | standaard | Skonto's halen dankzij kortere doorlooptijd |
| BS95.002 | EDI framework | 12 | in | gap: GAP-1 | Retail-EDI = configuratie; webshop = maatwerk |
| BS65.253 | Verwerken binnenkomende facturen met OCR | 15 | in | add-on: Continia Document Capture | ±250 facturen/maand |
| BS65.254 | Goedkeuring van documenten | 15 | in | add-on: Continia Document Capture | Web Approval Portal voor zaakvoerder |
| BS65.256 | PEPPOL | 15 | in | add-on: Continia Document Output | Mandaat vanaf go-live |
| BS60.202 | Aanmaken van een serviceorder | 9 | uit | | Geen serviceactiviteiten |
