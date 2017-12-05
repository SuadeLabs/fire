---
layout:		schema
title:		"loan_transaction"
---

# Loan Transaction Schema

---

A Loan Transaction is an event that has an impact on a loan, typically the balance.

### Properties

Name | Type | Description
--- | --- | ---
id | The unique identifier for the loan transaction within the financial institution. | string 
date | YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
amount | The size of the transaction in the loan transaction event. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
currency_code | undefined | undefined 
loan_id | The unique identifier for the affected loan/s within the financial institution. | string 
movement | The movement parameter describes how the loan arrived to the firm. | string 
sources | Identifiers for data sources. Useful for analytics and MI purposes. | array 
type | The type of impact on the balance of the loan. | string 
value_date | The timestamp that the transaction was valued or took place. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
