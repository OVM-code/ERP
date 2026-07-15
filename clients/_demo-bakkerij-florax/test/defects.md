# Defect register — Bakkerij Florax (demo)

## DEF-001 — Actieprijs blijft staan na wijziging leverdatum
- **Gevonden in:** TS-2.01, ronde R1, 2026-11-04
- **Scenario:** BS25.101
- **Severity:** middel
- **Status:** gesloten
- **Toegewezen aan:** consultant

Symptoom: stap 2 van TS-2.01 toonde nog de actieprijs na datumwijziging. Oorzaak:
prijsherberekening stond uit bij datumwijziging (setup-keuze). Fix: instelling
aangepast conform BPA BS25.101; hertest in R1 geslaagd.

**Voeding:** kennisbankwaarschuwing toegevoegd aan het food-pack (prijsherberekening
bij datumwijziging expliciet instellen).

<!-- Next ID: DEF-002 -->
