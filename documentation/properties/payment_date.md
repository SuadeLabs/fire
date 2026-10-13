---
layout:     property
title:      "payment_date"
schemas:    [derivative_cash_flow, loan_cash_flow]
---

# payment_date

---

The **payment_date** attribute is the contractual or actual date on which the cash flow is due or was paid and is a date-time string in ISO 8601 format.

FIRE records the cash-flow payment date separately from the reset date. For a derivative reporting example, [ESMA Guidelines for reporting under EMIR, Section 6.2.2.4.3, Table 84, page 279][emir] includes field 2.76 for the date of a notional exchange. The FIRE field also applies to loan cash flows.

[emir]: https://www.esma.europa.eu/sites/default/files/library/esma74-362-2281_final_report_guidelines_emir_refit.pdf#page=280
