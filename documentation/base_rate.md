---
layout:		property
title:		"base_rate"
schemas:	[account, loan]
---

# base_rate
The **base\_rate** represents the [basis][basis] of the [**rate**][ir] on the [**balance**][balance] at the given [**date**][date] as agreed in the terms of the financial product. 

Basis can be defined as "the difference between the spot price of a given cash market asset and the price of its related futures contract." Therefore, the base\_rate can be viewed as the time value of the money referred to in the financial product and the difference between the interest\_rate and the base\_rate can be viewed as the [yield spread][ys] of the financial product over a defined index.

In practice, the base\_rate conveys the information that the interest\_rate is directly or indirectly linked to another rate or index. For the purposes of consistency, the relevant Bloomberg Index ticker is used with "ZERO" used to indicate that there is no related base\_rate used for the determination of the interest\_rate.


---
[date]: https://github.com/suadelabs/fire/blob/master/documentation/date.md
[basis]: https://en.wikipedia.org/wiki/Basis_trading
[ir]: https://github.com/suadelabs/fire/blob/master/documentation/rate.md
[balance]: https://github.com/suadelabs/fire/blob/master/documentation/balance.md
[ys]: https://en.wikipedia.org/wiki/Yield_spread