---
layout:     property
title:      "next_receive_date"
schemas:    [derivative]
---

# next_receive_date

---

The **next_receive_date** attribute is the next contractual date on which cash is expected to be received on the derivative and is a date-time string in ISO 8601 format.

FIRE stores the date of the next incoming cash flow. For related regulatory context, [ESMA Guidelines for reporting under EMIR, Section 6.2.2.4.3, Table 84, page 279][emir] records a payment date and receiver separately for notional exchanges. That example does not define a generic next-receipt field.

[emir]: https://www.esma.europa.eu/sites/default/files/library/esma74-362-2281_final_report_guidelines_emir_refit.pdf#page=280
