---
layout:     property
title:      "disposition_type"
schemas:    [loan]
---

# disposition_type

---

The disposition method for any credit facility that was disposed during the period. Also see [disposition_date].

For additional details refer to: https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14Q

```bash
├── payoff
├── involuntary_payoff
├── liquidation
├── sold
├── fully_participated
└── fully_syndicated
```

### payoff
Voluntary Payoff - The borrower has voluntarily paid off the loan in full, typically through refinancing with another lender or using other funds to satisfy the debt obligation.

### involuntary_payoff
Involuntary Payoff - The loan has been paid off through non-voluntary means, such as through insurance proceeds, guarantor payments, or other forced liquidation events.

### liquidation
Liquidation - The loan has been terminated through the sale of collateral or other assets to recover the outstanding debt, typically occurring after default or foreclosure proceedings.

### sold
Sold - The loan has been sold to another financial institution or investor, transferring all rights and obligations to the new owner.

### fully_participated
Fully Participated - The loan has been fully participated out to other financial institutions, where the original lender retains the servicing rights but shares the credit risk with participating institutions.

### fully_syndicated
Fully Syndicated - The loan has been fully syndicated to a group of lenders, where the original lender may retain a portion of the loan but has distributed the majority of the credit risk to the syndicate members.

--- 