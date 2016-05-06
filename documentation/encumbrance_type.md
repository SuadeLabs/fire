---
layout:		property
title:		"encumbrance_type"
schemas:	[account, loan, collateral]
---

# encumbrance_type
The **encumbrance_type** describes the nature and reason behind the [**encumbrance_amount**][encumbrance_amount].

With regards to asset encumbrance the EBA [mentions][eba-report] repos, covered bonds and derivatives.

For real estate collateral, we include real_estate.

*(Consider further enums, particularly with regards to more specific real estate collateral: liens, easement ...)*

---
[encumbrance_amount]: https://github.com/suadelabs/fire/blob/master/documentation/encumbrance_amount.md
[eba-report]:  https://www.eba.europa.eu/documents/10180/974844/EBA+Report+on+Asset+Encumbrance-+September+2015.pdf/e6e2a6ee-6708-4430-a506-5f68ff70736d
