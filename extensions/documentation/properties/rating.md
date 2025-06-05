---
layout:     property
title:      "rating"
schemas:    [risk_rating]
---

# rating

---

The internal obligor rating that addresses the probability of default of the loan. Suppose the credit is entirely rated AAA. The bank would supply this value:
AAA:1
Suppose a different case where half the credit's dollar value has a rating A and the other has C. The bank would supply:
A:0.5;C:0.5
All the decimal amounts must sum to 1.

For additional details refer to: https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14Q

--- 