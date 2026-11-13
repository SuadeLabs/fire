---
layout:     property
title:      "vol_adj_fx"
schemas:    [collateral]
---

# vol_adj_fx

---

The **vol_adj_fx** attribute is the supervisory volatility adjustment applied for currency mismatch between the collateral and the protected exposure and is a numeric field.

Under the financial collateral comprehensive method, [CRR Article 223(1), second and third subparagraphs][crr-eur-lex] requires a currency-volatility adjustment for a mismatch between collateral and exposure currencies, or the settlement currency for the specified netted OTC derivatives. FIRE stores this collateral-valuation input directly.

Read the [EUR-Lex consolidated text (1 January 2026)][crr-eur-lex] or the corresponding [EBA Single Rulebook entry][crr].

[crr]: https://www.eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/12349
[crr-eur-lex]: https://eur-lex.europa.eu/eli/reg/2013/575/2026-01-01/eng#:~:text=Where%20collateral%20is%20denominated%20in%20a%20currency%20that%20differs%20from%20the%20currency%20in%20which%20the%20underlying%20exposure%20is%20denominated
