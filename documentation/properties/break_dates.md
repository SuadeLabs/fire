---
layout:     property
title:      "break_dates"
schemas:    [account, derivative, security]
---

# break_dates

---

The **break_dates** represents a list (an array) of dates in the terms of a financial product where a contract can be broken by either party. Having an array allows flexibility for the information provider to share just the next **break_date** or all future **break_dates**.

If there are no **break_dates**, the property should be omitted and it is assumed that the product cannot be broken at any time until the [**end_date**][end].

---

[end]: https://github.com/suadelabs/fire/blob/master/documentation/properties/end_date.md
