# Client Intake — Bakkerij Florax (DEMO)

> **This is a fictional demo client**, used to demonstrate the BPA pipeline end-to-end.
> Copy `clients/_template/`, not this folder, for real clients.

## 1. Identity & stack

| Field | Value |
|---|---|
| Client (slug used for folder) | _demo-bakkerij-florax |
| Industry / sub-sector | food manufacturing — industrial bakery (frozen pastry) |
| ERP system + version | Business Central SaaS, current |
| Add-ons (exact products + modules licensed) | Aptean F&B ERP: lot management; Continia Document Capture |
| Other ISV apps / integrations | Webshop (custom), EDI with 2 retail chains |
| Localization / country version | Belgium (BE) |
| Go-live target | 2027-01 |
| Implementation partner constraints | fixed budget, single phase |

## 2. Organisation

- Legal entities & companies needed (now / in 3 years): 1 / 1
- Countries, currencies, VAT registrations: BE, EUR, BE VAT
- Users: 35 total — finance 5, sales 6, purchasing 3, warehouse 12, production 9
- Locations / warehouses / production sites: 1 site, 1 warehouse (ambient + frozen zone)

## 4. Sales

- Sales channels: EDI (retail), webshop, phone/mail
- Order volume per day & order lines profile: ~120 orders/day, 5–15 lines
- Pricing complexity: customer-specific prices + promo periods
- Returns volume & policy: low; only for quality complaints

## 6. Inventory & warehouse

- Lot / serial / expiry tracking requirements: full lot traceability + THT (BBD), recall obligation (FAVV)
- Valuation preference or requirement: FIFO
- Warehouse process today: paper, no scanners at go-live

## 9. Non-functional

- Compliance: IFS certification, FAVV recall test 2×/year, Peppol e-invoicing mandate
- Client's change appetite: adopt standard where possible
