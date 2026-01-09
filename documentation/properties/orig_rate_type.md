---
layout:     property
title:      "orig_rate_type"
schemas:    [loan, account]
---

# orig_rate_type


The rate_type at origination.

```bash
├── combined
├── fixed
├── tracker
└── variable
```

### combined
Combined Rate - A hybrid rate structure that combines elements of different rate types. This could include a combination of fixed and variable components, or other rate structures that don't fit into the standard categories.

### fixed
Fixed Rate - The interest rate remains constant throughout the life of the loan. The rate is set at origination and does not change, providing predictable payment amounts for the borrower.

### tracker
Tracker Rate - The interest rate is directly linked to a specific benchmark rate, typically moving in lockstep with changes to that rate. The rate tracks the benchmark rate with a fixed margin above or below it.

### variable
Variable Rate - The interest rate can change over time based on market conditions or other factors. Unlike a tracker rate, the changes may not be directly proportional to changes in a benchmark rate.

--- 