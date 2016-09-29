---
layout:		property
title:		"balance"
schemas:	[account, derivative_cash_flow, derivative, loan, security]
---

# balance
The **balance** represents the contractual amount outstanding, deliverable or available at the given [**date**][date] as agreed in the terms of the financial product. The balance is typically the [face value][face] or [par value][par] of the product from an accounting perspective. The balance times the **interest\_rate** should also be the basis of calculation for the **accrued\_interest**.

This is a *monetary type* and as [it is impossible to squeeze infinitely many Real numbers into a finite number of bits][floats], we represent monetary types as integer numbers of cents/pence to reduce potential rounding errors. So $10.35 becomes 1035.
Don't forget to divide by 100 (or the relevant minor unit denomination) when presenting information to a user. The relevant minor unit denomination should be determined from the [**currency**][ccy]'s corresponding ['E'][E] value.


---
[date]: https://github.com/suadelabs/fire/blob/master/documentation/date.md
[face]: https://en.wikipedia.org/wiki/Face_value
[par]: https://en.wikipedia.org/wiki/Par_value
[floats]: https://en.wikipedia.org/wiki/Floating_point#Accuracy_problems
[ccy]: https://github.com/suadelabs/fire/blob/master/documentation/currency.md
[E]: https://en.wikipedia.org/wiki/ISO_4217#Active_codes
