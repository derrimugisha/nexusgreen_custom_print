# nexusgreen_custom_print

Odoo 19 custom print module for purchase orders and payslips.

- QWeb report templates live in `views/`.
- Python model extensions live in `models/`; controllers live in `controllers/`.
- Keep report styling scoped to the relevant template and preserve valid Odoo 19 XML.
- Validate edited XML with `xmllint --noout` and upgrade the module in Odoo when runtime verification is available.
- Update `IMPLEMENTATION.md` whenever code or report behavior changes.
