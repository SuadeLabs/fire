---
layout:     property
title:      "underlying_price"
schemas:    [derivative]
---

# underlying_price

---

The **underlying_price** is the current price per unit of the underlying Equity or Commodity on the reporting date. It is denominated in the derivative currency_code and can be multiplied by the derivative underlying_quantity.

## Equity derivatives
It represents the number of shares/units allocated to the contract.
Example of a derivative referencing 10 shares, each with a current price of $50:
* currency_code = "USD"
* underlying_price = 50
* underlying_quantity = 10
* notional_amount = 50 * 10 = 500

## Commodity derivatives
It represents the number of the relevant underlying quantity (barrels, tons etc...).
Example of a derivative referencing 10 barrels of oil, each with a current price of $125:
* currency_code = "USD"
* underlying_price = 125
* underlying_quantity = 10
* notional_amount = 125 * 10 = 1250
