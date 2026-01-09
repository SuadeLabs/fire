---
layout:     property
title:      "loan_share"
schemas:    [collateral]
---

# loan_share

Use with **loan_ids** to capture the allocated protection value if a collateral is pledged for multiple loans. 

The **loan_share** represents a list (an array) of allocated portion of the collateral. See example below.

| collateral |          |           |              |
|------------|----------|-----------|--------------|
| id         | **loan_ids** | **loan_share** | value        |
| col1       | [loan1, loan2] | [0.67, 0.33] | 15,000,000.00 |

| Output |     |     |
|---------------|--------------------------|----------------------------|
| Instrument ID | Counterparty identifier | Protection allocated value |
| loan1         | cust1                    | 10,000,000.00              |
| loan2         | cust1                    | 5,000,000.00               |

