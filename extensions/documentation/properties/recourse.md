---
layout:     property
title:      "recourse"
schemas:    [loan]
---

# recourse

---

Whether there is recourse on a loan. Recourse on a loan refers to terms in the mortgage contract that give the owner of the note the right to pursue additional claims against the borrower beyond possession of the property.

For additional details refer to: https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14M

```bash
├── full
├── partial
└── none
```

### full

The lender has full recourse to the borrower. If the borrower defaults, the lender may pursue recovery for the entire outstanding debt beyond the value of the collateral.

### partial

The lender has limited recourse to the borrower. If the borrower defaults, the lender may pursue recovery for only a portion of the outstanding debt beyond the value of the collateral.

### none

The lender has no recourse to the borrower. If the borrower defaults, recovery is limited to the value of the collateral.

--- 