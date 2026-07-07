# Briefing — workshop Verkoop & Interfaces, 2026-05-12 (demo)

- **Deelnemers verwacht:** key-user verkoop, logistiek verantwoordelijke
- **Domeinen / agenda:** 2 Verkoop, 12 Interfaces
- **Bronnen:** intake.md (2026-05-02), catalog, pack food-manufacturing, LL-001

## 1. Wat we al weten

- Drie kanalen: EDI (2 retailketens), eigen webshop, telefoon/mail (intake §4).
- ±120 orders/dag, 5–15 regels; klantspecifieke prijzen + promoperiodes (intake §4).
- Webshop is eigen bouw en blijft (intake §1) — koppeling wordt een thema.

## 2. Hypothese-scope

| Scenario | Hypothese | Te bevestigen met |
|---|---|---|
| BS25.202 Verkooporders maken | in — standaard, 3 kanalen samenkomend | 1, 2 |
| BS25.101 Verkoopprijzen | in — standaard prijslijsten + promo­regels | 5 |
| BS25.206 Backorders | in — vermoedelijk kanaalafhankelijk (retailboetes) | 3, 4 |
| BS25.328 Ordertoezegging | in — retail-leverdata zijn hard | 4 |
| BS25.200 Offertes | uit — vaste prijslijsten, geen offertetraject | 6 |
| BS25.900 Advanced pricing (Aptean) | uit — tenzij bonus-/staffelafspraken opduiken | 5 |
| BS95.002 EDI framework | in — retail-EDI configuratie + webshop maatwerk? | 7, 8 |

## 3. Vragen

1. Hoe komen orders vandaag per kanaal binnen, en wie corrigeert uitval?
2. Wat moet een orderbevestiging naar retail bevatten (GLN, actiecodes)?
3. ⚠ Deelleveringen: wat verwacht retail vs de rest? (bepaalt verzendadvies-setup)
4. ⚠ Wat kost een gemiste retail-leverdatum? (bepaalt of ordertoezegging must is)
5. Hoe lopen promoprijzen nu — wie beheert ze, hoeveel per jaar, fouten gehad?
6. Bestaat er een offerte-/contracttraject of enkel prijslijsten?
7. ⚠ Webshopkoppeling: welke kant bouwt wat, wie is de leverancier, budget?
8. Moet de webshop voorraad zien? Hoe actueel?

## 4. Lessen die hier spelen

- LL-001-patroon (magazijncomplexiteit bij <50 users zonder scanners): begin niet
  over directed put-away als het magazijn ter sprake komt — fase 2.

## 5. Na de workshop (zelfde dag)

- [x] Transcript in inputs/ (2026-05-12-verkoop-transcript.md) + REQ-001…006
- [x] Hypothese-scope bijgewerkt → coverage.md
- [x] Open punt (INVOIC-spec keten B) → agenda finance-workshop
