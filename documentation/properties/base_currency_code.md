---
layout:		property
title:		"base_currency_code"
schemas:	[agreement, exchange_rate]
---

# base_currency_code

---

## agreement
The base currency referred to in an [ISDA CSA][isda_csa]. It is relevant to the [MTA][mta] and [Threshold][th].

## exchange_rate
When quoting the price of currency it is done on a relative basis with currency pairs. The base currency is the first currency in a pair with the quote currency being the second. The price quoted represents how much one unit of the base currency can buy you of the quote currency. For example, if you were looking at the GBP/USD currency pair, the Britsh pound would be the base currency and the U.S. dollar would be the quote currency.

The International Organization for Standardization (ISO) set the standard (ISO standard 4217) of the three letter abbreviations used for currencies.

See also [**quote_currency_code**][quote_ccy]

---
[quote_ccy]: https://github.com/suadelabs/fire/blob/master/documentation/properties/quote_currency_code.md
[mta]: https://github.com/suadelabs/fire/blob/master/documentation/properties/minimum_transfer_amount.md
[th]: https://github.com/suadelabs/fire/blob/master/documentation/properties/threshold.md
[isda_csa]: https://www.isda.org/a/mDKDE/5english-law-new-csa-exhibit.pdf
