---
layout:     property
title:      "call_dates"
schemas:    [account, derivative, security]
---

# call_dates

---

The **call_dates** represents a list (an array) of dates in the terms of a financial product where a contract can be called by issuer or credit provider depending on the product. Having an array allows flexibility for the information provider to share just the next **call_date** or all future **call_dates**.

If there are no **call_date**s, the property should be omitted and it is assumed that the product can be called at any time prior to the [**end_date**][end].

---

[end]: https://github.com/suadelabs/fire/blob/master/documentation/properties/end_date.md
