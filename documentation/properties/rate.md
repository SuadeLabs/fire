---
layout:		property
title:		"rate"
schemas:	[account, derivative, loan, security]
---

# rate

---

The **rate** property describes the full interest rate applied to the balance of the account or loan. This is (or should roughly be) the full interest rate used to calculate the [**accrued_interest**][accrued_interest]. For floating rates the credit spread can be obtained by subtracting the [**base_rate**][base_rate] from the **rate**.

The **rate** should be recorded as a percentage in decimal format. ie. 3.5% should be represented as 3.5 and not 0.035. There is no restriction to the precision of the number (number of decimal places).


[accrued_interest]: https://github.com/suadelabs/fire/blob/master/documentation/properties/accrued_interest.md
[base_rate]: https://github.com/suadelabs/fire/blob/master/documentation/properties/base_rate.md
