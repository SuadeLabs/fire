---
layout:     property
title:      "balance"
schemas:    [account, derivative_cash_flow, derivative, loan, security]
---

# balance

---

The **balance** represents the contractual amount outstanding, deliverable or available at the given [**date**][date] as agreed in the terms of the financial product. The balance is sometimes referred to as the [face value][face] or [par value][par] of the product. 

More precisely, from an [IFRS 9][ifrs9] accounting point of view, the balance is equivalent to the *gross carrying amount* which is the *carrying amount* including *accrued interest* but before *impairment* and any *hedge accounting* has been taken into consideration in accordance with Appendix A:
> The amortised cost of a financial asset, before adjusting for
any loss allowance.

This is a *monetary type* and as [it is impossible to squeeze infinitely many Real numbers into a finite number of bits][floats], we represent monetary types as integer numbers of cents/pence to reduce potential rounding errors. So $10.35 becomes 1035.
Don't forget to divide by 100 (or the relevant minor unit denomination) when presenting information to a user. The relevant minor unit denomination should be determined from the currency's corresponding ['E'][E] value.


---

[date]: https://github.com/suadelabs/fire/blob/master/documentation/properties/date.md
[face]: https://en.wikipedia.org/wiki/Face_value
[par]: https://en.wikipedia.org/wiki/Par_value
[floats]: https://en.wikipedia.org/wiki/Floating_point#Accuracy_problems
[E]: https://en.wikipedia.org/wiki/ISO_4217#Active_codes
[ifrs9]: https://www.iasplus.com/en-gb/standards/ifrs-en-gb/ifrs9
