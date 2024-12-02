---
layout:     property
title:      "orig_notional"
schemas:    [loan]
---

# orig_notional

---

The **orig_notional** is the notional amount of the loan at the origination.

It is used to assess the orignal Loan-To-Value (LTV) as required in some regulatory returns such as the [FR Y-14Q][FRY14Q] schedule A.

This is a *monetary type* and as [it is impossible to squeeze infinitely many Real numbers into a finite number of bits][floats], we represent monetary types as integer numbers of cents/pence to reduce potential rounding errors. So $10.35 becomes 1035.
Don't forget to divide by 100 (or the relevant minor unit denomination) when presenting information to a user. The relevant minor unit denomination should be determined from the currency's corresponding ['E'][E] value.

---

[floats]: https://en.wikipedia.org/wiki/Floating_point#Accuracy_problems
[E]: https://en.wikipedia.org/wiki/ISO_4217#Active_codes
[FRY14Q]:https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14Q
