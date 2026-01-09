---
layout:     property
title:      "joint_liability_structure"
schemas:    [loan]
---

# joint_liability_structure

Use with [**customer_ids**][customer_ids] to capture the outstanding nominal amount for a single instrument where there are two or more debtors.

The **joint_liability_structure** represents a list (an array) of allocated portion of the single instrument. See example below.

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



[customer_ids]: https://suade.org/fire/book/documentation/properties/customer_ids.html


