#!/usr/bin/env python3
"""One-off migration: turn plain Dutch labels in bpa/processes/*.process.json into
bilingual {nl, en} objects, using official Business Central (EN-US) terminology.

Kept in the repo as the reference NL->EN map for standard flow labels; extend the map
and re-run when new standard flows are added with plain-string labels. Client process
files are NOT touched — translate those per client (they are client wording anyway).
"""
from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Official BC terminology (EN-US). Where a label is process narrative rather than a
# BC object, the translation is plain English but keeps BC terms embedded.
T = {
    # flow labels
    "ja": "yes", "nee": "no", "afwijking": "adjustment", "telling": "physical count",
    "kwaliteitsissue": "quality issue", "nee, afboeken": "no — write off",
    "nee, volgende periode": "no — next period", "per order": "per order",
    "restlevering": "remaining quantity", "vaste prijs": "fixed price",
    "in regie": "time & materials", "via contract": "via contract",
    "nalevering": "back order shipment", "EDI / webshop": "EDI / webshop",
    "telefoon / mail": "phone / mail",
    # lanes
    "Applicatiebeheer": "Application management", "Boekhouding": "Accounting",
    "Commercieel": "Commercial", "Crediteuren": "Accounts payable",
    "Debiteuren": "Accounts receivable", "Finance": "Finance", "Inkoop": "Purchasing",
    "Inkoop (uitbesteding)": "Purchasing (subcontracting)", "Kwaliteit": "Quality",
    "Magazijn": "Warehouse", "Ontvangst": "Receiving", "Planning": "Planning",
    "Productieplanning": "Production planning", "Projectleider": "Project manager",
    "Servicedesk": "Service desk", "Techniek": "Field service", "Uitvoering": "Execution",
    "Verkoop": "Sales", "Verzending": "Shipping", "Voorraadbeheer": "Inventory management",
    "Werkvloer": "Shop floor",
    # nodes — bedrijfsinformatie
    "Inrichting / nieuwe relatie": "Setup / new contact",
    "Organisaties beheren": "Manage companies", "Gebruikers beheren": "Manage users",
    "Divisies beheren": "Manage divisions", "Resources beheren": "Manage resources",
    "Artikeltracering instellen": "Set up item tracking",
    "Contacten beheren": "Manage contacts", "Contacten classificeren": "Classify contacts",
    "Interacties registreren": "Record interactions",
    "Opportuniteiten beheren": "Manage opportunities",
    "Master data operationeel": "Master data operational",
    # nodes — verkoop
    "Klantvraag ontvangen": "Customer request received",
    "Verkoopofferte maken": "Create sales quote", "Klant akkoord?": "Customer accepts?",
    "Offerte verloren": "Quote lost", "Verkooporder maken": "Create sales order",
    "Goedkeuring vereist?": "Approval required?",
    "Goedkeuringsaanvraag verzenden": "Send approval request",
    "Verkooporder goedkeuren": "Approve sales order",
    "Voorraad reserveren": "Reserve inventory",
    "Order picken en verzenden": "Pick and ship order",
    "Volledig geleverd?": "Fully shipped?", "Backorder opvolgen": "Manage back order",
    "Verkoopfactuur maken": "Create sales invoice",
    "Verkoopfactuur boeken": "Post sales invoice", "Retour gemeld?": "Return reported?",
    "Verkoopretourorder maken": "Create sales return order",
    "Verkoopcreditnota maken": "Create sales credit memo",
    "Order afgehandeld": "Order completed",
    # nodes — inkoop
    "Inkoopbehoefte (MRP-voorstel of manueel)": "Purchase demand (MRP proposal or manual)",
    "Offerte nodig?": "Quote needed?", "Inkoopofferte aanvragen": "Request purchase quote",
    "Inkooporder maken": "Create purchase order",
    "Inkooporder goedkeuren": "Approve purchase order",
    "Goederen ontvangen": "Receive goods", "Levering conform?": "Delivery as ordered?",
    "Inkoopretourorder maken": "Create purchase return order",
    "Volledig ontvangen?": "Fully received?",
    "Inkoopfactuur registreren": "Record purchase invoice",
    "Inkoopfactuur goedkeuren": "Approve purchase invoice",
    "Inkoopfactuur boeken": "Post purchase invoice",
    "Inkoop afgehandeld": "Purchase completed",
    # nodes — voorraad
    "Nieuw artikel of voorraadgebeurtenis": "New item or inventory event",
    "Artikel beheren": "Manage item", "Stockkeeping units beheren": "Manage stockkeeping units",
    "Artikeltraceringscode toekennen": "Assign item tracking code",
    "Welke gebeurtenis?": "Which event?", "Voorraad corrigeren": "Adjust inventory",
    "Inventarisatie uitvoeren": "Run physical inventory",
    "Artikel/lot blokkeren": "Block item/lot",
    "Lot management & traceability": "Lot management & traceability",
    "Non-conformance registreren": "Record non-conformance",
    "Lot vrijgegeven?": "Lot released?",
    "Voorraad correct en beschikbaar": "Inventory correct and available",
    # nodes — projectbeheer
    "Project gegund": "Project awarded", "Project maken": "Create project",
    "Projectmasterdata en -structuur beheren": "Manage project master data and structure",
    "Projectbudget beheren": "Manage project budget",
    "Artikelen plannen": "Plan items", "Resources toewijzen en plannen": "Assign and plan resources",
    "Artikelverbruik registreren": "Post item usage",
    "Resource-uren registreren": "Post resource hours",
    "Onkosten registreren": "Post expenses",
    "Inkoopfacturen koppelen aan project": "Link purchase invoices to project",
    "Facturatievorm?": "Invoicing method?",
    "Projectfactuur maken (vaste prijs)": "Create project invoice (fixed price)",
    "Projectfactuur maken (in regie)": "Create project invoice (time & materials)",
    "Project afgerond?": "Project finished?", "Project afsluiten": "Close project",
    "Project afgesloten": "Project closed",
    # nodes — planning
    "Periodieke planningsrun": "Periodic planning run",
    "Productieprognoses beheren": "Manage demand forecasts",
    "Inkoop- & planningsvoorstellen berekenen": "Calculate requisition & planning worksheets",
    "Voorstellen beoordelen en fiatteren": "Review and carry out worksheet lines",
    "Inkooporders aanmaken": "Create purchase orders",
    "Productieorders aanmaken": "Create production orders",
    "Transferorders aanmaken": "Create transfer orders",
    "Voorstellen omgezet in orders": "Worksheet lines converted to orders",
    # nodes — productie
    "Productiebehoefte (planning of verkooporder)": "Production demand (planning or sales order)",
    "Productieorder maken": "Create production order",
    "Productieorder plannen": "Schedule production order",
    "Ordermaterialen beheren": "Manage order components",
    "Uitbesteding nodig?": "Subcontracting needed?",
    "Uitbestedingsvoorstel berekenen": "Calculate subcontracting worksheet",
    "Uitbestedingsinkooporder boeken": "Post subcontracting purchase order",
    "Materialen klaarzetten": "Stage components",
    "Verbruik en output registreren": "Post consumption and output",
    "Uitval?": "Scrap?", "Uitval boeken": "Post scrap",
    "Capaciteit boeken": "Post capacity",
    "Kostprijs bijwerken": "Adjust cost", "Productieorder afsluiten": "Finish production order",
    "Order geproduceerd": "Order produced",
    # nodes — magazijn
    "Goederen aangemeld (inkoop/productie/transfer)": "Goods announced (purchase/production/transfer)",
    "Magazijnontvangst maken": "Create warehouse receipt",
    "Cross-docking?": "Cross-docking?", "Cross-dock artikelen": "Cross-dock items",
    "Voorraadopslag uitvoeren": "Execute put-away",
    "Artikelen verplaatsen": "Move items",
    "Opslaglocaties herbevoorraden": "Replenish bins",
    "Artikelen picken": "Pick items",
    "Magazijnverzending maken": "Create warehouse shipment",
    "Artikelen verzenden": "Ship items", "Goederen verzonden": "Goods shipped",
    # nodes — service
    "Servicemelding klant": "Customer service request",
    "Onder servicecontract?": "Under service contract?",
    "Contract-serviceorder maken": "Create contract service order",
    "Serviceorder maken": "Create service order",
    "Resource plannen op serviceorder": "Allocate resource to service order",
    "Verbruik registreren": "Post usage",
    "Herstelstatus beheren": "Manage repair status",
    "Serviceverzending boeken": "Post service shipment",
    "Facturabel?": "Billable?", "Servicefactuur maken": "Create service invoice",
    "Servicecontract factureren (periodiek)": "Invoice service contract (periodic)",
    "Service afgehandeld": "Service completed",
    # nodes — finance
    "Financiële verwerking": "Financial processing",
    "Inkoopfacturen registreren": "Record purchase invoices",
    "Inkoopfacturen boeken": "Post purchase invoices",
    "Leveranciersbetalingen uitvoeren": "Process vendor payments",
    "Manuele verkoopfacturen registreren": "Record manual sales invoices",
    "Openstaande vorderingen opvolgen": "Follow up open receivables",
    "Aanmaningen beheren": "Manage reminders",
    "Dagafschriften verwerken en boeken": "Process and post bank statements",
    "Diverse boekingen registreren": "Post general journal entries",
    "Periodieke BTW-aangifte aanmaken": "Create periodic VAT return",
    "Financiële rapporten aanmaken": "Create financial reports",
    "Boekjaar/periode afsluiten": "Close fiscal year/period",
    "Periode afgesloten": "Period closed",
    # titles
    "Bedrijfsinformatie & relatiebeheer": "Company information & relationship management",
    "Verkoop": "Sales", "Inkoop": "Purchasing", "Voorraad": "Inventory",
    "Projectbeheer": "Project management", "Planning (MPS/MRP)": "Planning (MPS/MRP)",
    "Productie": "Manufacturing", "Magazijnbeheer": "Warehouse management",
    "Service": "Service", "Finance": "Finance",
    # subtitles
    "Organisatie-masterdata en CRM": "Organisation master data and CRM",
    "Van klantvraag tot betaalde factuur": "From customer request to paid invoice",
    "Van inkoopbehoefte tot geboekte inkoopfactuur": "From purchase demand to posted purchase invoice",
    "Artikelbeheer, correcties en kwaliteit": "Item management, adjustments and quality",
    "Van projectaanmaak tot afsluiting": "From project creation to closure",
    "Van prognose tot gefiatteerde voorstellen": "From forecast to carried-out worksheets",
    "Van productieorder tot afgesloten order": "From production order to finished order",
    "Van ontvangst tot verzending": "From receipt to shipment",
    "Van servicemelding tot servicefactuur": "From service request to service invoice",
    "Crediteuren, debiteuren en periodieke afsluiting": "Payables, receivables and period-end closing",
}


def bi(v):
    if isinstance(v, dict) or not v:
        return v  # already bilingual or empty
    en = T.get(v)
    if en is None:
        print(f"  ! geen vertaling voor: {v!r} — NL behouden voor beide talen")
        en = v
    return {"nl": v, "en": en}


def main() -> None:
    for f in sorted((REPO / "bpa" / "processes").glob("*.process.json")):
        p = json.loads(f.read_text(encoding="utf-8"))
        p["title"] = bi(p.get("title"))
        p["subtitle"] = bi(p.get("subtitle"))
        for lane in p["lanes"]:
            lane["label"] = bi(lane["label"])
        for n in p["nodes"]:
            n["label"] = bi(n.get("label"))
        for fl in p["flows"]:
            if fl.get("label"):
                fl["label"] = bi(fl["label"])
        f.write_text(json.dumps(p, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"vertaald: {f.name}")


if __name__ == "__main__":
    main()
