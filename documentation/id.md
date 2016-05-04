---
layout:		property
title:		"id"
schemas:	[account, collateral, customer, loan]
---

# id
The **id** property appears in almost every schema and is the unique an identifier for that product, customer, transaction etc. within the financial institution. This field is important because it serves as the common identifier that is retained as data passes from one system to another.

Users should be careful that when aggregating similar data from different sources, that unique ids are maintained to avoid conflicts or overwriting of data.
