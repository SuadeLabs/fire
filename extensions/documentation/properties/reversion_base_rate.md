---
layout:     property
title:      "reversion_base_rate"
schemas:    [security]
---

# reversion_base_rate

---

For instruments that convert from paying a fixed rate to paying a coupon/dividend rate that is linked to the rate of a particular index, report the index to which it is linked.

```bash
├── FDTR
├── UKBRBASE
├── ZERO
├── bbsw
│   └── bbsw_3m
├── euribor
│   ├── euribor_1m
│   ├── euribor_3m
│   └── euribor_6m
├── other
├── pboc
└── sofr
    ├── sofr_1m
    ├── sofr_3m
    └── sofr_6m
```

### FDTR
Federal Discount Target Rate - The primary interest rate set by the Federal Reserve Board for lending to depository institutions.

### UKBRBASE
UK Bank Rate Base - The Bank of England's base rate, which is the interest rate at which the Bank of England lends to other banks.

### ZERO
Zero Rate - A fixed rate of zero percent, typically used when the instrument reverts to a fixed rate of zero.

### bbsw
Bank Bill Swap Rate (BBSW) where the tenor is unknown. Refer to: https://www.rba.gov.au/mkt-operations/resources/interest-rate-benchmark-reform.html

### bbsw_3m
3 month Bank Bill Swap Rate (BBSW). Refer to: https://www.rba.gov.au/mkt-operations/resources/interest-rate-benchmark-reform.html

### euribor
Euro Interbank Offered Rate (Euribor) where the tenor is unknown.

### euribor_1m
1 month Euro Interbank Offered Rate (Euribor).

### euribor_3m
3 month Euro Interbank Offered Rate (Euribor).

### euribor_6m
6 month Euro Interbank Offered Rate (Euribor).

### other
A base rate other than one defined within the taxonomy.

### pboc
People’s Bank of China (PBOC) benchmark interest rate, where the specific rate or tenor is unknown

### sofr
Secured Overnight Financing Rate (SOFR) where the tenor is unknown.

#### sofr_1m
1 month Secured Overnight Financing Rate (SOFR).

#### sofr_3m
3 month Secured Overnight Financing Rate (SOFR).

#### sofr_6m
6 month Secured Overnight Financing Rate (SOFR).

--- 