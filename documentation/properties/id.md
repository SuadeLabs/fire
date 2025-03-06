---
layout:		property
title:		"id"
schemas:	[account, agreement, collateral, derivative_cash_flow, derivative, exchange_rate, loan_cash_flow, loan_transaction, loan, security, risk_rating, adjustment, curve, customer, issuer, guarantor]
---

# id

---

The **id** property appears in almost every schema and is the unique identifier for that product, customer, transaction etc. within the financial institution. This field is important because it serves as the common identifier that is retained as data passes from one system to another.

A [unique identifier][unid] allows a transaction to be traced back to the payer or originator, by accompanying transfers of funds.

Users should be careful that when aggregating similar data from different sources, that unique ids are maintained to avoid conflicts or overwriting of data.

[unid]: http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ:L:2006:345:0001:0009:EN:PDF
