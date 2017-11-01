---
layout:		property
title:		"source"
schemas:	[account, collateral, customer, derivative_cash_flow, derivative, loan_transaction, loan, security]
---

# source
Similar to the [**product_name**][product_name] property, the **source** property is designed to aid the institution with principles of data control and governance as outlined by the [Basel Committee on Banking Supervision][bcbs239]. It is a strong value for the firm to indicate the source system for the data attribute.

Note that this is different from the "source" that can be obtained in the transmission and can be used to indicate the original source system of the data item.

*consider a list attribute where each subsequent source system can append to list*

---
[product_name]: https://github.com/suadelabs/fire/blob/master/documentation/product_name.md
[bcbs239]: http://www.bis.org/publ/bcbs239.pdf
