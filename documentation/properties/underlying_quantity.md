---
layout:     property
title:      "underlying_quantity"
schemas:    [derivative]
---

# underlying_quantity

---

The **underlying_quantity** is the number of underlyings related to the underlying_price or the strike.
It should be populated such that this equality holds true: notional_amount = underlying_quantity * underlying_price.
It is mostly relevant for Equity and Commodity derivatives.

## Equity derivatives
It represents the number of shares/units allocated to the contract.
Example of a derivative referencing 10 shares, each with a current price of $50:
* currency_code = "USD"
* underlying_price = 50
* underlying_quantity = 10
* notional_amount = 50 * 10 = 500

## Commodity derivatives
It represents the number of the relevant underlying quantity (barrels, tons etc...).
Example of a derivative referencing 10 barrels of oil, each with a current price of $25:
* currency_code = "USD"
* underlying_price = 25
* underlying_quantity = 10
* notional_amount = 25 * 10 = 250
