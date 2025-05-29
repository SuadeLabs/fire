---
layout:     property
title:      "loss_mitig_status"
schemas:    [loan]
---

# loss_mitig_status

---

Identifies whether a loan is being actively handled by the servicer's loss mitigation department. Refers to all loans where the servicer has initiated loss mitigation procedures whether or not a particular course of action or workout type has been executed. Active loss mitigation refers to instances where the loan is currently in loss mitigation, and the servicer is actively pursuing loss mitigation.

For additional details refer to: https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14M

```bash
├── active_non_performing
├── active_performing
├── broken
└── none
```

### active_non_performing
Active Non-Performing - The loan is currently in loss mitigation and is not performing according to its original terms. The servicer is actively working with the borrower to find a solution, but the loan is in default or experiencing payment issues.

### active_performing
Active Performing - The loan is currently in loss mitigation but is still performing according to its terms. The servicer is actively working with the borrower to prevent future default or to modify the loan terms while the borrower remains current on payments.

### broken
Broken - The loss mitigation process has been terminated or failed. This could occur if the borrower did not complete required actions, failed to meet modification terms, or if the servicer determined that loss mitigation was no longer viable.

### none
None - No loss mitigation activities are currently in progress. The loan is either not in need of loss mitigation or has not yet been referred to the loss mitigation department.

--- 