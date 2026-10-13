---
layout:     property
title:      "next_reset_date"
schemas:    [derivative]
---

# next_reset_date

---

The **next_reset_date** attribute is the next contractual date on which the derivative's periodic terms are reset and is a date-time string in ISO 8601 format.

For contracts that settle exposure and reset their market value to zero on specified dates, [CRR Article 279c(1)(a), definition of M][crr-eur-lex] uses the time to the next reset when determining remaining maturity. This treatment applies to those contracts; an ordinary floating-rate fixing does not necessarily reset the contract's market value to zero.

Read the [EUR-Lex consolidated text (1 January 2026)][crr-eur-lex] or the corresponding [EBA Single Rulebook entry][crr].

[crr]: https://www.eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/12274
[crr-eur-lex]: https://eur-lex.europa.eu/eli/reg/2013/575/2026-01-01/eng#:~:text=the%20remaining%20maturity%20of%20the%20transaction%20shall%20be%20equal%20to%20the%20time%20until%20the%20next%20reset%20date
