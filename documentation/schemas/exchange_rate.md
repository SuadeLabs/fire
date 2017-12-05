---
layout:		schema
title:		"exchange_rate"
---

# Exchange Rate Schema

---

An Exchange Rate represents the conversion rate between two currencies.

### Properties

Name | Type | Description
--- | --- | ---
id | The unique identifier for the exchange rate within the financial institution. | string 
date | The observation or value date for the data in this object. Formatted as YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
base_currency_code | The base currency in accordance with ISO 4217 standards. | undefined 
quote | The amount of the quote currency received in exchange for 1 unit of the base currency. | number 
quote_currency_code | The quoted currency in accordance with ISO 4217 standards. | undefined 
