---
layout:     property
title:      "accrual_status"
schemas:    [loan]
---

# accrual_status

---

```bash
├── accrual
├── non_accrual
├── securitised
└── serviced_for_others
```

Indicates whether interest on the loan is currently being accrued. A loan is typically placed on non-accrual status when it becomes impaired or when there is reasonable doubt about the collectability of principal or interest.

### accrual

The loan is currently accruing interest in the normal course of business. Interest income is being recognized as it is earned, and the loan is performing according to its terms.

### non_accrual

The loan has been placed on non-accrual status, meaning interest is no longer being recognized as income. This typically occurs when the loan becomes impaired, when there is reasonable doubt about collectability, or when the loan is past due by a certain number of days (typically 90 days or more).

### securitised

The loan has been securitized, meaning it has been packaged into a security and sold to investors. The loan is now part of a securitization structure.

### serviced_for_others

The loan is being serviced on behalf of another entity. The reporting institution is acting as a servicer but does not own the loan. 