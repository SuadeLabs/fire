layout:		property
title:		"call_dates"
schemas:	[account]
---

# call_dates
The **call\_dates** represents a list (an array) of dates in the terms of a financial product where a contract can be called by issuer or credit provider depending on the product(see call\_date description in relevant schema). Having an array allows flexibility for the information provider to share just the next call\_date or all future call\_dates.

If there are no call\_dates, the property should be omitted and it is assumed that the product can be called at any time prior to the [**end\_date**][end].

---
[end]: https://github.com/suadelabs/fire/blob/master/documentation/end_date.md