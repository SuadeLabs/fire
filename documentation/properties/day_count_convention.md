---
layout:     property
title:      "day_count_convention"
schemas:    [account, loan, security]
---

# day_count_convention

---

The **day count convention** is the standardised methodology for calculating the number of days between two dates. It is used to calculate the amount of accrued interest or the present value.

```bash
├── standardised_30_360
├── standardised_30_365
├── actual_360
├── actual_365
└── actual_actual
```

### standardised_30_360
Calculate the daily interest using a 360-day year and then multiplies that by 30 (standardised month).

### standardised_30_365
Calculate the daily interest using a 365-day year and then multiplies that by 30 (standardised month).

### actual_360
Calculate the daily interest using a 360-day year and then multiplies that by the actual number of days in each time period.

### actual_365
Calculate the daily interest using a 365-day year and then multiplies that by the actual number of days in each time period.

### actual_actual
Calculate the daily interest using the actual number of days in the year and then multiplies that by the actual number of days in each time period.
