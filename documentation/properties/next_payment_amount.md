---
layout:     property
title:      "next_payment_amount"
schemas:    [derivative]
---

# next_payment_amount

---

The **next_payment_amount** attribute is the next known outgoing contractual cash amount on the derivative and is an integer monetary field stored in the smallest currency unit.

FIRE stores the next outgoing cash amount separately from its date and from cash flows in the opposite direction. For related regulatory context, [ESMA Guidelines for reporting under EMIR, Section 6.2.2.4.3, Table 84, page 279][emir] records amounts, dates, payers and receivers separately for notional exchanges. Those EMIR fields illustrate payment details; they do not define a generic next-payment field.

[emir]: https://www.esma.europa.eu/sites/default/files/library/esma74-362-2281_final_report_guidelines_emir_refit.pdf#page=280
