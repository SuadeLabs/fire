---
layout:     property
title:      "supervisory_price"
schemas:    [derivative]
---

# supervisory_price

---

The **supervisory_price** is used to calculate the SACCR supervisory delta for non-standard options as per Art. 279a 1(a) CRR, when the payoff is a function of the average value of the price of the underlying instrument. In this case, supervisory_price shall be equal to the observed average value on the calculation date.
When supervisory_price is not provided, the supervisory delta will be calculated with hunderlying_price.
Like underlying_price, supervisory_price is denominated in the derivative currency_code.
