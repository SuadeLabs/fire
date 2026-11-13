---
layout:     property
title:      "values"
schemas:    [curve]
---

# values

---

The **values** attribute is the ordered list of nodes that make up a curve and is an array of objects containing `reference` and `value`.

Each entry combines an x-axis reference, such as tenor, with its y-axis value. As a financial example, the [ECB explanation of euro area yield curves, Background section][ecb-curves] relates interest rates to remaining maturity. The [FIRE curve schema, `values` property][schema] defines the node format and allowed reference points.

[ecb-curves]: https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_area_yield_curves/html/index.en.html#:~:text=A%20yield%20curve
[schema]: https://github.com/SuadeLabs/fire/blob/master/schemas/curve.json#:~:text=The%20list%20of%20values%20for%20this%20curve.
