---
layout:     property
title:      "base_rate"
schemas:    [account, derivative, loan, security]
---

# base_rate

---

# account
The base rate set by the bank that offers the account facility, which typically follows the official central bank interest rate - but it is not guaranteed to do so. The base rate represents the basis of the rate on the balance at the given date as agreed in the terms of the account.

The [official interest rate][official] is the interest rate paid on commercial bank reserves by the central bank of an area or region.

[official]: http://www.bankofengland.co.uk/statistics/pages/iadb/notesiadb/wholesale_baserate.aspx

---

# derivative
The **base rate** represents the [basis][basis] of the [**rate**][ir] on the [**balance**][balance] at the given [**date**][date] as agreed in the terms of the financial product.

Basis can be defined as "the difference between the spot price of a given cash market asset and the price of its related futures contract." Therefore, the base rate can be viewed as the time value of the money referred to in the financial product and the difference between the interest rate and the base rate can be viewed as the [yield spread][ys] of the financial product over a defined index.

In practice, the base rate conveys the information that the interest rate is directly or indirectly linked to another rate or index. For the purposes of consistency, the relevant Bloomberg Index ticker is used with "ZERO" used to indicate that there is no related base rate used for the determination of the interest rate.

[date]: https://github.com/suadelabs/fire/blob/master/documentation/properties/date.md
[basis]: https://en.wikipedia.org/wiki/Basis_trading
[ir]: https://github.com/suadelabs/fire/blob/master/documentation/properties/rate.md
[balance]: https://github.com/suadelabs/fire/blob/master/documentation/properties/balance.md
[ys]: https://en.wikipedia.org/wiki/Yield_spread

---

# loan
The base rate set by the bank that offers the loan product, which typically follows the official central bank interest rate - but it is not guaranteed to do so. The base rate represents the basis of the repayment rate on the borrowed funds at the given date as agreed in the terms of the loan.

he [official interest rate][official] is the interest rate paid on commercial bank reserves by the central bank of an area or region.

[official]: http://www.bankofengland.co.uk/statistics/pages/iadb/notesiadb/wholesale_baserate.aspx

---

# security
The **base rate** represents the [basis][basis] of the [**rate**][ir] on the [**balance**][balance] at the given [**date**][date] as agreed in the terms of the financial product.

Basis can be defined as "the difference between the spot price of a given cash market asset and the price of its related futures contract." Therefore, the base rate can be viewed as the time value of the money referred to in the financial product and the difference between the interest rate and the base rate can be viewed as the [yield spread][ys] of the financial product over a defined index.

In practice, the base rate conveys the information that the interest rate is directly or indirectly linked to another rate or index. For the purposes of consistency, the relevant Bloomberg Index ticker is used with "ZERO" used to indicate that there is no related base rate used for the determination of the interest rate.

### FDTR
Fed funds rate

### UKBRBASE
UK BoE base rate

### ZERO
0

---

[date]: https://github.com/suadelabs/fire/blob/master/documentation/properties/date.md
[basis]: https://en.wikipedia.org/wiki/Basis_trading
[ir]: https://github.com/suadelabs/fire/blob/master/documentation/properties/rate.md
[balance]: https://github.com/suadelabs/fire/blob/master/documentation/properties/balance.md
[ys]: https://en.wikipedia.org/wiki/Yield_spread
