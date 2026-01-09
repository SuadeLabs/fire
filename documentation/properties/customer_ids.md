---
layout:     property
title:      "customer_ids"
schemas:    [customer, issuer, guarantor]
---

# customer_ids



Use with [**joint_liability_structure**][joint_liability_structure] to capture the outstanding nominal amount for a single instrument where there are two or more debtors.

The **customer_ids** represents the list (an array) of debtors of the single instrument. See example below.

Example:
| customer |        |              |
|----------|--------|--------------|
| id       | type   | **customer_ids** |
| cust1    | credit_institution |              |
| cust2    | credit_institution |              |
| joint1   |        | [cust1, cust2] |

| loan  |         |          |                         |        |
|------|---------|----------|-------------------------|--------|
| id   | customer_id | balance  | **joint_liability_structure** | fees   |
| loan1 | joint1     | 90,000.00 | [0.7, 0.4]              | 10,000.00 |

|Output|               |             |
|---------------|--------------------------|------------------------|
| Instrument ID | Counterparty identifier | Joint Liability Amount |
| loan1         | cust1                    | 70,000.00              |
| loan1         | cust2                    | 40,000.00              |



[joint_liability_structure]: https://suade.org/fire/book/documentation/properties/joint_liability_structure.html

