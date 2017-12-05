---
layout:		schema
title:		"collateral"
---

# Collateral Schema

---

Data schema to define collateral (currently can reference loans or accounts).

### Properties

Name | Type | Description
--- | --- | ---
id | The unique identifier for the collateral within the financial institution. | string 
date | YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601 | string 
loan_ids | The unique identifiers for the loans within the financial institution. | array 
account_ids | The unique identifier/s for the account/s within the financial institution. | array 
charge | Lender charge on collateral, 1 indicates first charge, 2 second and so on. 0 indicates a combination of charge levels. | integer 
currency_code | undefined | undefined 
encumbrance_amount | The amount of the collateral that is encumbered by potential future commitments or legal liabilities. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
encumbrance_type | The type of the encumbrance causing the encumbrance_amount. | string 
end_date | The end date for recognition of the collateral | string 
sources | Identifiers for data sources. Useful for analytics and MI purposes. | array 
start_date | The start date for recognition of the collateral | string 
type | The collateral type defines the form of the collateral provided | string 
value | The valuation as used by the bank for the collateral on the value_date. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
value_date | The timestamp that the collateral was valued. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
