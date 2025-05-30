---
layout:     property
title:      "liq_method"
schemas:    [loan]
---

# liq_method

---

The liquidation method for the loan.

For additional details refer to: https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14M

```bash
├── involuntary_liquidation
├── not_paid_in_full
├── servicing_transfer
└── voluntary_payoff
```

### involuntary_liquidation
Involuntary Liquidation - The loan has been terminated through forced means, such as foreclosure, repossession, or other legal proceedings initiated by the lender due to borrower default or other contractual violations.

### not_paid_in_full
Not Paid in Full - The loan has been terminated without receiving full payment of the outstanding balance, typically resulting in a loss to the lender. This may occur through various means including short sales, deed-in-lieu of foreclosure, or other negotiated settlements.

### servicing_transfer
Servicing Transfer - The loan has been transferred to another servicer while maintaining the same ownership. This represents a change in the entity responsible for collecting payments and managing the loan, but not a termination of the loan itself.

### voluntary_payoff
Voluntary Payoff - The loan has been paid off in full through the borrower's voluntary actions, such as refinancing with another lender, selling the property, or using other funds to satisfy the debt obligation.

--- 