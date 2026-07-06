# Extending the system: new ERP systems and add-ons

The Business Central + Aptean content is just the first instance. The same structure
carries any ERP stack. Adding one is content work, not development work — and the
assistant does most of the writing for you.

## Add a new ERP system

1. Create `knowledge/erp/<system-slug>/` (e.g. `dynamics-f-o/`, `sap-b1/`, `odoo/`).
2. Decide the functional area files. Reuse the BC split where it fits
   (general-setup, finance, sales, purchasing, inventory, warehouse, manufacturing, …) —
   consistent area names keep cross-ERP comparisons possible.
3. For each area, copy `knowledge/_templates/erp-area-template.md` and fill one block
   per setup decision.
4. Fastest path: ask the assistant *"Scaffold the knowledge folder for <system>, areas
   X/Y/Z, using the template — ground it in the vendor's official documentation and
   mark anything unverified."* Then review; you are the expert, the assistant drafts.

## Add a new add-on

1. Create `knowledge/addons/<addon-slug>/` with an `overview.md` (what it is, who needs
   it, module map) and one file per module from
   `knowledge/_templates/addon-module-template.md`.
2. Each module file has two parts — keep them strictly separated:
   - **Changes to standard setup decisions** — link every changed decision back to the
     standard file so the layering rule works.
   - **New setup decisions** the add-on introduces.
3. In the affected standard ERP files, add one line under **Add-on impact** linking to
   the new module file. This is what makes the assistant fetch the overlay.
4. If vendor documentation is partner-gated (common), write the decision blocks
   functionally and mark uncertain details with
   `> ⚠️ Verify against current vendor documentation.` — a flagged gap is useful,
   an invented field name is poison.

## Quality bar for knowledge content

- One block = one decision the consultant actually has to make.
- "When it fits / When to avoid" must be argued from client characteristics, not
  feature marketing.
- Every block lists the client info required to decide — the intake template feeds on
  these.
- Flag irreversibility honestly; it drives how much argumentation a decision deserves.
- Stamp `Last reviewed` and keep expertise tags consistent (grep existing tags before
  inventing new ones).
