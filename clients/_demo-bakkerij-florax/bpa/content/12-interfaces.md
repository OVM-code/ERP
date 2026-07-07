# 12. Interfaces

Florax koppelt Business Central met de twee retailketens (EDI) en met de eigen
webshop. Beide lopen over het EDI/integratieframework, maar de webshopkoppeling
vraagt maatwerkmapping in twee richtingen.

## BS95.002 EDI framework
- **Invulling:** gap: GAP-1
- **Requirements:** REQ-001, REQ-006

Het integratieframework verwerkt de inkomende berichten:

- **Retail-EDI (ORDERS)**: de bestaande berichten van beide ketens worden gemapt
  naar verkooporders. Bestaande flows kunnen per keten gekopieerd en bijgestuurd
  worden — dit is configuratie binnen het framework.
- **Webshoporders**: de webshop (eigen bouw) levert orders aan in JSON via de
  centrale webservice; na validatie worden ze automatisch verkooporders.
- **Uitgaand — voorraadstanden naar de webshop**: periodieke export (per kwartier)
  van beschikbare voorraad per artikel naar de webshop, en EDI INVOIC naar de
  retailketens.

De koppeling met de webshop vraagt maatwerk aan webshopzijde én een specifieke
mapping/exportprofiel in BC — omvang en aannames staan in **GAP-1**. De
foutafhandeling loopt via de inbox-/outboxtransacties van het framework: uitval is
zichtbaar, corrigeerbaar en herverwerkbaar zonder tussenkomst van IT.
