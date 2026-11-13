---
layout:     property
title:      "pd_calc_method"
schemas:    [risk_rating]
---

# pd_calc_method

---

The calculation method used to determine the associated probabilities of default.

For additional details refer to: https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14Q

```bash
├── hybrid
├── point_in_time
└── through_cycle
```

### hybrid
A probability of default calculation method that combines elements of both point-in-time and through-the-cycle approaches, allowing for both short-term economic conditions and long-term structural risk factors to influence the rating.

### point_in_time
A probability of default calculation method that reflects the current economic conditions and borrower-specific circumstances at a specific point in time, making it more sensitive to short-term changes in the economic environment.

### through_cycle
A probability of default calculation method that aims to remain stable across economic cycles by focusing on long-term structural risk factors rather than temporary economic conditions, providing a more stable rating over time.

--- 