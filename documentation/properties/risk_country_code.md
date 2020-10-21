---
layout:		property
title:		"risk_country_code"
schemas:	[account, derivative, entity, loan, security]
---

# risk_country_code

---

The **risk_country_code** represents location or jurisdiction of where the risk of the product or entity resides (trading location). This can be a subjective field and can depend on a number of factors such as country of domicile, the primary stock exchange on which a product trades, the location from which the majority of its revenue comes, its reporting currency or other factors.

Countries are represented as 2-letter codes in accordance with [ISO 3166-1][iso3166].

See also [**country_code**][cc].

[cc]: https://github.com/suadelabs/fire/blob/master/documentation/properties/country_code.md
[iso3166]: https://en.wikipedia.org/wiki/ISO_3166-1
