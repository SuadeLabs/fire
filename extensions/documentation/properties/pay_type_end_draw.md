---
layout:     property
title:      "pay_type_end_draw"
schemas:    [loan]
---

# pay_type_end_draw

---

How borrowers are required to repay any principal outstanding at the end of the allowable draw period.

For additional details refer to: https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14M

```bash
├── amortising
├── balloon
├── interest_only
└── other
```

### amortising
Amortising Payment - The borrower is required to make regular payments that include both principal and interest components after the draw period ends. These payments are designed to fully repay the loan over a specified term.

### balloon
Balloon Payment - The borrower is required to make a large, lump-sum payment of the remaining principal balance at the end of the draw period. This payment is significantly larger than the regular payments made during the draw period.

### interest_only
Interest Only - The borrower is only required to pay the interest portion of the loan after the draw period ends. No principal is being repaid during this period, and the loan balance remains unchanged until a later date.

### other
Other Payment Type - A payment structure that doesn't fit into the standard categories. This could include specialized or custom payment arrangements that are unique to specific loan products or borrower circumstances.

--- 