---
layout:     property
title:      "cb_haircut"
schemas:    [loan, security]
---

# cb_haircut

---

The **cb_haircut** attribute is the haircut applied by the relevant central bank to the asset value when determining how much liquidity or collateral value can be recognised and is a number between 0 and 1.

In the Eurosystem framework, [Guideline (EU) 2016/65, Article 1(1)–(2)][ecb-haircuts] provides for valuation haircuts on eligible marketable assets and identifies the factors used to determine them. FIRE stores the haircut applied by the relevant central bank as a fraction; for example, a 10% haircut is stored as `0.10`.

[ecb-haircuts]: https://eur-lex.europa.eu/eli/guideline/2016/65/2024-05-06/eng#:~:text=Valuation%20haircuts%20applied%20to%20eligible%20marketable%20assets
