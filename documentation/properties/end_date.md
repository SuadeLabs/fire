---
layout:		property
title:		"end_date"
schemas:	[account, collateral, derivative_cash_flow, derivative, loan, security]
---

# end_date

---

The **end_date** is a widely used property and reflects the contractual maturity date or tenor of the product or relationship.

The **end_date** refers to the final observation or value date for the data in the JSON object. From the recipient's point of view, it is the time stamp for which the data in the JSON object is or will no longer be *true*. Note that it is called date but allows for precision to the nearest second in accordance with the ISO 8601 standard (YYYY-MM-DDTHH:MM:SSZ).

It is possible that for some products, particularly cash-related accounts, there is no end or maturity date. If not provided, it should be assumed that the **end_date** is infinite (ie. perpetual). For fixed-life securities such as bonds, the date will be the maturity date of the underlying asset. Similarly, for security financing transactions, the **end_date** is typically the date the collateral or asset is returned or the financing ends.

See also [**date**][date] and [**maturity_date**][maturity_date]

---

[date]: 		https://github.com/suadelabs/fire/blob/master/documentation/properties/date.md
[maturity_date]:       https://github.com/suadelabs/fire/blob/master/documentation/properties/maturity_date.md
