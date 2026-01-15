---
layout:     property
title:      "joint_customer_ids"
schemas:    [customer, issuer, guarantor]
---

# joint_customer_ids



Use with **joint_customer_structure** to capture the outstanding nominal amount for a single instrument where there are two or more debtors.

The **joint_customer_ids** represents the list (an array) of debtors of the single instrument. See example below.

Example:
| customer |        |              |
|----------|--------|--------------|
| id       | type   | **joint_customer_ids** |
| cust1    | credit_institution |              |
| cust2    | credit_institution |              |
| joint1   |        | [cust1, cust2] |

| loan  |         |          |                         |        |
|------|---------|----------|-------------------------|--------|
| id   | customer_id | balance  | **joint_customer_structure** | fees   |
| loan1 | joint1     | 90,000.00 | [0.7, 0.4]              | 10,000.00 |

|Output|               |             |
|---------------|--------------------------|------------------------|
| Instrument ID | Counterparty identifier | Joint Liability Amount |
| loan1         | cust1                    | 70,000.00              |
| loan1         | cust2                    | 40,000.00              |


