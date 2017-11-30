---
layout:		property
title:		"charge_on_collateral"
schemas:	[collateral]
---

# charge_on_collateral

---

The **charge_on_collateral** property indicates the charge that the lender has on the collateral of the loan. To avoid an open-ended enum value, we use integers to represent the order of charge:

* 0 = mixed/combination of charge levels
* 1 = first charge
* 2 = second charge
* 3 = third charge
* ... and so on

The absence of the **charge_on_collateral** property indicates that the lender has no charge on the collateral and/or that the loan is unsecured.
