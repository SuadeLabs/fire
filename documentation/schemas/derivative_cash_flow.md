---
layout:		schema
title:		"derivative_cash_flow"
---

# Derivative Cash Flow Schema

---

A derivative cash flow where two parties exchange cash flows (or assets) derived from an underlying reference index, security or financial instrument.

### Properties

Name | Type | Description
--- | --- | ---
id | The unique identifier for the derivative within the financial institution. | string 
date | The observation or effective date for the data in this object. Formatted as YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
accrued_interest | The accrued interest/premium due at the next payment date. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
asset_class | The asset class to which the derivative belongs. | string 
asset_liability | A derivative cash flow exchange that results in a net positive value after the transaction is an asset on the firm's balance sheet. A derivative cash flow exchange that results in a net negative value after the transaction is a liability on the firm's balance sheet. | string 
balance | The contractual balance due on the payment date in the currency given. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
currency_code | Actual currency of the security in accordance with ISO 4217 standards. It should be consistent with balance, accrued_interest, guarantee_amount and other monetary amounts. | undefined 
customer_id | Counterparty to the cash flow | string 
derivative_id | Unique identifier to the derivative to which this cash flow relates | string 
leg | The type of the payment leg. | string 
mna_id | The unique identifier of the Master Netting Agreement for this derivative cash flow. | string 
mtm_clean | The mark-to-market value of the derivative cash flow excluding interest/premium/coupons. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
mtm_dirty | The mark-to-market value of the derivative cash flow including interest/premium/coupons. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
notional_amount | The notional value is the total value with regard to a derivative's underlying index, security or asset at its spot price in accordance with the specifications (i.e. leverage) of the derivative product. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
on_balance_sheet | Is the financial product reported on the balance sheet of the financial institution? | boolean 
payment_date | The timestamp that the cash flow will occur or was paid. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
product_name | The name of the product as given by the financial institution to be used for display and reference purposes. | string 
reporting_lei | The LEI code for the legal entity under which the security is being reported. | string 
reporting_entity_name | The name of the reporting legal entity for display purposes (as LEI code may not be available). | string 
settlement_type | The type of settlement for the contract. | string 
sources | Identifiers for data sources. Useful for analytics and MI purposes. | array 
trade_date | The date that the derivative cash flow terms were agreed. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
value_date | The timestamp that the cash flow was valued. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
