---
layout:     property
title:      "reset_date"
schemas:    [derivative_cash_flow]
---

# reset_date

---

The **reset_date** attribute is the date on which the variable cash-flow amount is set for the relevant derivative leg and is a date-time string in ISO 8601 format.

This is distinct from the payment date: the variable cash-flow amount is set on this date, as defined in the [FIRE derivative cash-flow schema, `reset_date` property][schema]. For related reporting context, [ESMA Guidelines for reporting under EMIR, Section 5.2.1, paragraph 414 and Table 28, pages 191–193][emir] records payment and reset frequencies separately.

[schema]: https://github.com/SuadeLabs/fire/blob/master/schemas/derivative_cash_flow.json#:~:text=Date%20on%20which%20a%20variable%20cash%20flow%20amount%20is%20set.
[emir]: https://www.esma.europa.eu/sites/default/files/library/esma74-362-2281_final_report_guidelines_emir_refit.pdf#page=192
