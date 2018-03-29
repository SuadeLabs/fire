---
layout:		property
title:		"accrued_interest"
schemas:	[account, derivative_cash_flow, derivative, loan, security]
---

# accrued_interest

**accrued\_interest** represents the interest accumulated *but unpaid* since the [last\_payment\_date][lpd] and due at the [next\_payment\_date][npd].

Accrued interest is an accounting definition resulting from the [accrual basis][acc] of accounting. Generally speaking, this should be the amount reported on the income statement and the balance sheet (as not yet been paid/received). In other words, it is income earned or expenses incurred but not yet recognised in the revenues.


---

[lpd]: https://github.com/suadelabs/fire/blob/master/documentation/properties/last_payment_date.md
[npd]: https://github.com/suadelabs/fire/blob/master/documentation/properties/next_payment_date.md
[acc]: https://en.wikipedia.org/wiki/Basis_of_accounting#Accrual_basis
