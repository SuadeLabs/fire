---
layout:		property
title:		"customer_id"
schemas:	[account, derivative_cash_flow, security]
---

# customer_id

---

The **customer_id** is the unique an identifier for the customer within the financial institution. Where applicable, we would encourage the use of a [Legal Entity Identifier][lei]. This field is important because it serves as the common identifier that is retained as data passes from one system to another.

Users should be careful that when aggregating similar data from different sources, that unique ids are maintained to avoid conflicts or overwriting of data.


[lei]: https://www.gleif.org/
