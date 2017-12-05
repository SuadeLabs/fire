---
layout:		schema
title:		"customer"
---

# Customer Schema

---

Data schema to define a customer or legal entity related to a financial product or transaction.

### Properties

Name | Type | Description
--- | --- | ---
product_count | The number of active non-loan products/trades this customer has with the firm. | integer 
start_date | The date that the customer first became a customer. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
status | The status of the relationship with the customer from the firm's point of view. | string 
