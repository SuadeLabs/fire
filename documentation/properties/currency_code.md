---
layout:		property
title:		"currency_code"
schemas:	[account, collateral, derivative_cash_flow, derivative, loan, loan_transaction, security, adjustment, loan_cash_flow, curve, customer, issuer, guarantor]
---

# currency_code

---

The **currency_code** represents the currency of the data object and all the relevant monetary types.

Currencies are represented as 3-letter codes in accordance with [ISO 4217][iso4217] standards.

The following currency codes are deprecated and will be removed from Jan 2026: ANG, CUC, HRK, SLL, USS, ZWL.

---

[acc]: https://github.com/suadelabs/fire/blob/master/documentation/properties/accrued_interest.md
[bal]: https://github.com/suadelabs/fire/blob/master/documentation/properties/balance.md
[iso4217]: https://en.wikipedia.org/wiki/ISO_4217
