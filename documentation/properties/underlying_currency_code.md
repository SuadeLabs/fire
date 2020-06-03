---
layout:     property
title:      "underlying_currency_code"
schemas:    [derivative]
---

# underlying_currency_code

---

The **underlying_currency_code** is used to reference an additional currency in a derivative transaction.
It is particularly relevant for FX Options.
For example, on a long EURUSD call option the relevant currency fields on the derivative schema would be:
* currency_code = "EUR": the currency bought if the option is exercised
* underlying_currency_code = "USD": the currency sold if the option is exercised