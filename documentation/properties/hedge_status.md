---
layout:     property
title:      "hedge_status"
schemas:    [loan]
---

# hedge_status

---

Specifies the type of eligible hedge applied to the loan. 

For PRA-regulated entities, this field supports compliance with Article 123B of the CRR under Basel 3.1, indicating whether an eligible natural and/or financial hedge exists against foreign exchange risk from a currency mismatch, meeting the 90% instalment coverage requirement.

```bash
├── combined_hedge
├── financial_hedge
├── natural_hedge
└── unhedged
```

### combined_hedge
Both natural and financial hedges exist.

### financial_hedge
The obligor has a financial instrument intended to offset financial risk associated with the exposure.

### natural_hedge
The obligor reduces risk through normal business activities or assets that can be used to meet obligations, without using derivatives.

### unhedged
No eligible natural or financial hedges exist.

--- 