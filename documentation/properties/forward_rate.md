---
layout:     property
title:      "forward_rate"
schemas:    [derivative_cash_flow]
---

# forward_rate

---

The **forward_rate** attribute is the contractual or observed rate used on the reset date to determine a floating derivative cash flow and is a numeric field.

FIRE stores the rate used for the specific cash flow, as defined in the [derivative cash-flow schema, `forward_rate` property][schema]. For related reporting context, [ESMA Guidelines for reporting under EMIR, Section 5.2.1, paragraph 414 and Table 28, pages 191–193][emir] distinguishes the floating-rate reference, payment frequency and reset frequency.

[schema]: https://github.com/SuadeLabs/fire/blob/master/schemas/derivative_cash_flow.json#:~:text=Rate%20used%20to%20set%20a%20variable%20cash%20flow%20on%20the%20reset_date
[emir]: https://www.esma.europa.eu/sites/default/files/library/esma74-362-2281_final_report_guidelines_emir_refit.pdf#page=192
