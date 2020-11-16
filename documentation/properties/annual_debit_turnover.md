---
layout:     property
title:      "annual_debit_turnover"
schemas:    [customer]
---

# annual_debit_turnover

---

The annual_debit_turnover of a customer is the sum of the debit transactions through an customer's business account(s) during the last year since the given [**date**][date]. 

The debit turnover of a customer that holds an account with the reporting entity is represented by the monetary outflows from the relevant account(s). This is separate to credit turnover, which is represented by monetary inflows to the account(s).

The relationship between opening balance, closing balance, debit turnover and credit turnover of an account between two dates is represented by the following:

Closing Balance = Opening Balance + Credit Turnover - Debit Turnover

This is a *monetary type* and as [it is impossible to squeeze infinitely many Real numbers into a finite number of bits][floats], we represent monetary types as integer numbers of cents/pence to reduce potential rounding errors. So $10.35 becomes 1035.
Don't forget to divide by 100 (or the relevant minor unit denomination) when presenting information to a user. The relevant minor unit denomination should be determined from the currency's corresponding ['E'][E] value.


---

[date]: https://github.com/suadelabs/fire/blob/master/documentation/properties/date.md
[floats]: https://en.wikipedia.org/wiki/Floating_point#Accuracy_problems
[E]: https://en.wikipedia.org/wiki/ISO_4217#Active_codes
