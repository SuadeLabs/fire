---
layout:     property
title:      "hedge_type"
schemas:    [account, derivative, loan, security]
---

# hedge_type

---

The type of hedge (fair value or cash flow hedge) associated with the holding. Whether it is hedging individually or is hedging as part of a portfolio of assets with similar risk that are hedged as a group in line with ASC 815-20-25-12 (b), ASC 815-20-2512A, or ASC 815-10-25-15.

For PRA-regulated entities, this field also supports compliance with Article 123B of the CRR under Basel 3.1, indicating whether an eligible natural and/or financial hedge exists against foreign exchange risk from a currency mismatch.

```bash
├── combined_hedge
├── financial_hedge
│   ├── cf_hedge
│   │   ├── portfolio_cf_hedge
│   │   │   └── portfolio_cf_hedge_eco
│   │   └── cf_hedge_eco
│   └── fv_hedge
│       ├── portfolio_fv_hedge
│       │   └── portfolio_fv_hedge_eco
│       └── fv_hedge_eco  
├── net_inv_hedge 
├── natural_hedge
└── unhedged
```

### combined_hedge
Combined natural and financial hedge.

### financial_hedge
A financial instrument intended to offset financial risk.

### cf_hedge
Cash flow hedge designation.

### cf_hedge_eco
Cash flow with an economic hedge designation.

### fv_hedge
Fair value hedge designation.

### fv_hedge_eco
Fair value with an economic hedge designation.

### net_inv_hedge
hedge of the foreign currency exposure arising from the net investment in a foreign operation.

### portfolio_cf_hedge
Cash flow hedge designation for a portfolio of financial assets or financial liabilities.

### portfolio_cf_hedge_eco
Cash flow with an economic hedge designation for a portfolio of financial assets or financial liabilities.

### portfolio_fv_hedge
Fair value hedge designation for a portfolio of financial assets or financial liabilities.

### portfolio_fv_hedge_eco
Fair value with an economic hedge designation for a portfolio of financial assets or financial liabilities.

### natural_hedge
Risk is reduced through normal business activities or assets that can be used to meet obligations.

### unhedged
No eligible natural or financial hedges exist.

For additional details refer to:
- https://asc.fasb.org/1943274/2147480682/815-20-25-12
- https://asc.fasb.org/1943274/2147480682/815-20-25-12A
- https://asc.fasb.org/1943274/2147480682/815-10-25-15

--- 
