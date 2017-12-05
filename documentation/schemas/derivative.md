---
layout:		schema
title:		"derivative"
---

# Derivative Schema

---

A derivative is a contract which derives its value from an underlying reference index, security or asset.

### Properties

Name | Type | Description
--- | --- | ---
id | The unique identifier for the derivative within the financial institution. | string 
date | The observation or effective date for the data in this object. Formatted as YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
deal_id | The unique identifier used by the financial institution for the deal to which this derivative belongs. | string 
accounting_treatment | undefined | undefined 
accrued_interest | The accrued interest since the last payment date and due at the next payment date. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
asset_class | The asset class to which the derivative belongs. | string 
asset_liability | Is the derivative a financial asset or a financial liability on a firm's balance sheet? | string 
balance | Outstanding amount including accrued interest. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
base_rate | The base rate represents the basis of the rate on the balance at the given date as agreed in the terms of the financial product. | string 
break_dates | Dates where this contract can be broken (by either party). Formatted as YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | array 
call_dates | Dates where this contract can be called (by the customer). Formatted as YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | array 
currency_code | Actual currency of the underlying reference index, security or asset for the derivative in accordance with ISO 4217 standards. It should be consistent with balance, accrued_interest, guarantee_amount and other monetary amounts. | undefined 
customer_id | The unique identifier used by the financial institution to identify the customer for this product. | string 
end_date | YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601 | string 
first_payment_date | The first payment date for interest payments. | string 
last_payment_date | The final payment date for interest payments, often coincides with end_date. | string 
mna_id | The unique identifier of the Master Netting Agreement for this derivative cash flow. | string 
mtm_clean | The mark-to-market value of the derivative excluding interest. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
mtm_dirty | The mark-to-market value of the derivative including interest. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
next_exercise_date | The next date at which the option can be exercised. | string 
next_payment_amount | The amount that will need to be paid at the next_payment_date. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
next_payment_date | The next date at which interest will be paid or accrued_interest balance returned to zero. | string 
next_receive_amount | The amount that is expected to be received at the next_receive_date. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
next_receive_date | The next date at which interest will be received or accrued_interest balance returned to zero. | string 
next_reset_date | The date on which the periodic payment term and conditions of a contract agreement are reset/re-established. | string 
notional_amount | The notional value is the total value with regard to a derivative's underlying index, security or asset at its spot price in accordance with the specifications (i.e. leverage) of the derivative product. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
on_balance_sheet | Is the derivative reported on the balance sheet of the financial institution? | boolean 
payment_type | The type of the payment leg. | string 
prev_payment_date | The most recent previous date at which interest was paid or accrued_interest balance returned to zero. | string 
product_name | The name of the product as given by the financial institution to be used for display and reference purposes. | string 
rate | The full interest rate applied to the derivative notional in percentage terms. Note that this therefore includes the base_rate (ie. not the spread). | number 
receive_type | The type of the receive leg. | string 
reporting_lei | The LEI code for the legal entity under which the derivative is being reported. | string 
reporting_entity_name | The name of the reporting legal entity for display purposes (as LEI code may not be available). | string 
risk_country_code | Two-letter country code describing where the risk for the derivative product resides. In accordance with ISO 3166-1 | undefined 
settlement_type | The type of settlement for the contract. | string 
sources | Identifiers for data sources. Useful for analytics and MI purposes. | array 
start_date | The timestamp that the trade or financial product commences. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
type | This is the type of the derivative with regards to common regulatory classifications. | string 
trade_date | The timestamp that the trade or financial product terms are agreed. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
underlying_id | The unique identifier used by the financial institution to identify the underlying instrument for this product. | string 
value_date | The timestamp that the derivative was valued. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
