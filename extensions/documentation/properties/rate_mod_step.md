---
layout:     property
title:      "rate_mod_step"
schemas:    [loan]
---

# rate_mod_step

---

Identifies whether a rate modification or arrears arrangement has a 'stepped' or gradual return to non-modified rate. If the rate drop is gradual (stepped), even to a rate that is different from the contract rate, this field should be populated with TRUE. If the rate drop is immediate, even to a rate that is different from the contract rate, this field should be populated with FALSE. Similarly, FALSE will be reported if the loan immediately returns to the contract rate at expiration of the modification.

For additional details refer to: https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14M

--- 