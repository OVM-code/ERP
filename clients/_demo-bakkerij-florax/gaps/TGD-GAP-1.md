# TGD-GAP-1 — Webshop integration: orders in, stock feed out (Technical Gap Design)

| | |
|---|---|
| Client / GAP | _demo-bakkerij-florax / GAP-1 |
| Source FGD | FGD-GAP-1 v1.0 (**approved** on 2026-06-18 by O. Vanmalleghem) |
| Status | **draft** |
| Target platform | BC24 SaaS (BE localization) · Cegeka EDI framework · Aptean F&B (lot status) |
| Author / Reviewer | assistant / <architect> |

## 1. Project context for the developer

Bakkerij Florax is an industrial bakery running BC24 SaaS with the Cegeka EDI
framework (a configurable message-integration app already installed) and Aptean
Food & Beverage (lot management with quality statuses). Their own webshop must (a)
push sales orders into BC through the framework and (b) receive a sellable-stock
feed every 15 minutes. You build two small extension pieces around the framework;
you do NOT modify the framework or the base app.

| Term | Meaning here |
|---|---|
| Framework | Cegeka EDI framework app: one inbound webservice, Partner Messages config, inbox/outbox transaction log with retry |
| Webshop order | JSON per fixed schema (§6.1), identified by `webshopOrderNo` |
| Sellable stock | physical inventory at location HOOFD minus QC-blocked lots minus reservations; lots blocked only by the retail shelf-life rule DO count (FGD §3.3) |
| QC-blocked | Aptean lot status `GEBLOKKEERD-QC` or `AFGEKEURD` |

## 2. Solution overview

Inbound: webshop → framework webservice (message code `WEBSHOP-ORDER`) → framework
mapping creates the sales order → our subscriber sets origin and runs extra
validations, writing failures back as framework inbox errors. Outbound: a codeunit
computes sellable stock per item and hands the dataset to a framework outbound
message (`WEBSHOP-STOCK`) on a 15-minute job queue; delivery, retry and error
notification are framework behaviour.

## 3. Objects

> Number range: 50100–50149. Prefix: `FLX`.

| Object | Type | New/Extend | Purpose |
|---|---|---|---|
| FLX Webshop Setup (50100) | Table + Page | New | endpoint URL of stock feed, location filter, job queue on/off |
| FLX Sales Header Ext (50101) | TableExtension (Sales Header) | Extend | field `FLX Origin` (Option: " ",WEBSHOP,EDI) |
| FLX Webshop Order Mgt (50110) | Codeunit | New | inbound validations: duplicate `webshopOrderNo`, SKU mapping, customer blocked |
| FLX Stock Feed Mgt (50111) | Codeunit | New | compute sellable stock, build outbound dataset |
| FLX Stock Feed JQ (50112) | Codeunit (job queue entry point) | New | 15-min trigger calling 50111 |
| FLX Order List Ext (50120) | PageExtension (Sales Order List) | Extend | show/filter `FLX Origin` |

## 4. Data model

Sales Header extension: `FLX Origin` (Option, editable=false, captions NL
"Herkomst"/EN "Origin"). Duplicate detection uses standard `External Document No.`
(webshopOrderNo is written there by the framework mapping) — key exists; no new
table for order state, the framework inbox is the state record.

## 5. Logic

**Inbound (50110)**, subscribed to the framework's post-processing event for
message code `WEBSHOP-ORDER` (publisher: framework codeunit "Inbox Dispatcher",
event `OnAfterCreateDocument` — confirm exact name against the installed framework
version):
1. Find created Sales Header; set `FLX Origin` := WEBSHOP.
2. If another non-cancelled sales order exists with same `Sell-to Customer No.` +
   `External Document No.` → raise framework inbox error `DUPLICATE_ORDER`,
   delete the created order (AC-4).
3. Requested delivery date < tomorrow and creation time ≥ 14:00 → set to next
   working day (company calendar), matching FGD §3.3.
4. Never bypass standard sales-order validation; all field validation errors must
   surface as inbox errors, not silent defaults (AC-2 is handled by the framework
   mapping itself: unmapped SKU aborts the whole message).

**Outbound (50111)**: for each item in location HOOFD:
`sellable := Item Inventory (location) − Σ qty of lot entries with Aptean status in
{GEBLOKKEERD-QC, AFGEKEURD} − Reserved Qty on Inventory`. Lots whose only block is
the Aptean customer-shelf-life (retail) rule are NOT subtracted (AC-3). Emit
`{itemNo, sku, sellableQty, timestamp}` per item; hand to framework outbound message
`WEBSHOP-STOCK`. Retry/notification: framework outbox config, 3 retries (AC-5).

## 6. Integrations & error handling

6.1 Inbound JSON schema: framework standard envelope; `messagecode="WEBSHOP-ORDER"`,
`partnercode="WEBSHOP"`; body: customerNo, webshopOrderNo, requestedDeliveryDate,
lines[{sku, qty}]. 6.2 Outbound: HTTPS POST to Webshop Setup endpoint, auth =
API key header (stored in isolated storage, configured on the setup page, never in
code). All failures visible in framework inbox/outbox; error texts in NL and EN
captions.

## 7. Permissions

Permission set `FLX WEBSHOP` (read setup, edit via framework pages) → roles
"Verkoop binnendienst" and "Applicatiebeheer". Setup page write: Applicatiebeheer
only.

## 8. Upgrade & localization considerations

Extension objects + event subscribers only; no base-app or framework modification.
The Aptean lot-status option values are configuration — read them from setup, do
not hardcode (values per FGD §3.3 are the go-live configuration). BE localization
only; no multi-company.

## 9. Test plan

| Test | Covers FGD AC | Steps | Expected result |
|---|---|---|---|
| T-1 | AC-1 | POST valid order JSON (fixture 1) | sales order exists ≤ 2 min, External Document No. = webshopOrderNo, Origin = WEBSHOP |
| T-2 | AC-2 | POST order with SKU `XX-DOES-NOT-EXIST` | no sales order; 1 inbox transaction, error "SKU onbekend" |
| T-3 | AC-3 | Seed item: 1200 phys / 200 QC-blocked / 150 reserved / 100 retail-only-blocked; run 50111 | feed shows 850 |
| T-4 | AC-4 | POST fixture 1 twice | one sales order; second message → inbox error DUPLICATE_ORDER |
| T-5 | AC-5 | Point endpoint at a dead URL; run job queue | 3 retries then outbox error status + notification mail |
| T-6 | AC-1 | 500 orders in one hour (load fixture) | all processed < 15 min, no deadlocks |

## 10. Deployment

App `FLX Webshop Link` depends on: base app, Cegeka EDI framework, Aptean F&B.
Publish to FLORAX-DEV → TEST. After publish: fill FLX Webshop Setup, create job
queue entry (50112, 15 min), configure framework messages `WEBSHOP-ORDER`
(inbound mapping to Sales Header/Lines) and `WEBSHOP-STOCK` (outbound). Unlocks
setup-plan step 4.1.

## 11. Assumptions

- A1: webshop customer numbers equal BC customer numbers (data alignment before
  go-live — owned by the webshop vendor).
- A2: webshop hosts the stock-feed REST endpoint with API-key auth (confirmed
  2026-06-10).
- A3: exact framework event names verified against the installed framework version
  at development start (§5) — if absent, the framework's post-processing codeunit
  hook is the fallback.
- A4: SKU↔item mapping is maintained in the framework's translation tables, not in
  this app.
