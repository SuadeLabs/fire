---
layout:		property
title:		"date"
schemas:	[account, collateral, customer, derivative_cash_flow, derivative, entity, exchange_rate, guarantor, issuer, loan_cash_flow, loan_transaction, loan, security]
---

# date

---

**date** is a widely used property (in almost every schema) and when combined with ["id"][id] it is generally sufficient to be a primary key in whatever data model you decide to implement.

**date** refers to the observation or value date for the data in the JSON object. From the recipient's point of view, it is the time stamp for which the data in the JSON object is true. Note that it is called date but allows for precision to the nearest second in accordance with the ISO 8601 standard (YYYY-MM-DDTHH:MM:SSZ).

This means that if another data object is received with the same "date" but at a different hour, minute or second, then it will not conflict with the existing data point. It therefore follows that the existing data might be overwritten if the same "date" and "id" are transmitted (depending on the way the back-end/database is implemented).

---

[id]: https://github.com/suadelabs/fire/blob/master/documentation/properties/id.md
