---
layout:		schema
title:		"security"
---

# Security Schema

---

A security represents a tradable financial instrument held or financed by an institution for investment or collateral.

### Properties

Name | Type | Description
--- | --- | ---
id | The unique identifier for the security within the financial institution. | string 
date | The observation or effective date for the data in this object. Formatted as YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
accounting_treatment | undefined | undefined 
accrued_interest | The accrued interest since the last payment date and due at the next payment date. Monetary type represented as an integer number of cents/pence. | integer 
asset_liability | Is the security (valued at either amortised cost or fair value) an asset or a liability on the firm's balance sheet. | string 
balance | Outstanding amount including accrued interest. Monetary integer number of cents/pence. | integer 
base_rate | The base rate represents the basis of the rate on the balance at the given date as agreed in the terms of the financial product. | string 
break_dates | Dates where this contract can be broken (by either party). Formatted as YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | array 
call_dates | Dates where this contract can be called (by the customer). Formatted as YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | array 
country_code | Two-letter country code for security location/jurisdiction. In accordance with ISO 3166-1. | undefined 
cqs_standardised | The credit quality step for standardised approach. | integer 
cqs_irb | The credit quality step for internal ratings based approach. | integer 
currency_code | Actual currency of the security in accordance with ISO 4217 standards. It should be consistent with balance, accrued_interest, guarantee_amount and other monetary amounts. | undefined 
customer_id | The unique identifier used by the financial institution to identify the customer for this product. | string 
deal_id | The unique identifier used by the financial institution to identify the deal for this product that links it to other products of the same or different type. | string 
encumbrance_amount | The amount of the security that is encumbered by potential future commitments or legal liabilities such as within a repo pool. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
end_date | YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601 | string 
first_payment_date | The first payment date for interest payments. | string 
guarantor_id | The unique identifier for the guarantor within the financial institution. | string 
guarantee_start_date | The first day the security became guaranteed by the guarantor. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601 | string 
hqla_class | What is the HQLA classification of this security? | string 
isin_code | The unique International Securities Identification Number for the security according to ISO 6166. | string 
issuer_id | The unique identifier for the issuer within the financial institution. | string 
last_payment_date | The final payment date for interest payments, often coincides with end_date. | string 
movement | The movement parameter describes how the security arrived to the firm. | string 
mtm_clean | The mark-to-market value of the security excluding interest. Monetary number of cents/pence. | integer 
mtm_dirty | The mark-to-market value of the security including interest. Monetary number of cents/pence. | integer 
next_payment_date | The next date at which interest will be paid or accrued_interest balance returned to zero. | string 
notional_amount | The notional value is the total amount of a security's underlying asset at its spot price. Monetary number of cents. | integer 
on_balance_sheet | Is the security reported on the balance sheet of the financial institution? | boolean 
prev_payment_date | The most recent previous date at which interest was paid or accrued_interest balance returned to zero. | string 
product_name | The name of the product as given by the financial institution to be used for display and reference purposes. | string 
purpose | The purpose for which the security is being held. | string 
rate | The full interest rate applied to the security notional in percentage terms. Note that this therefore includes the base_rate (ie. not the spread). | number 
rehypothecation | Can the security be rehypothecated by the borrower? | boolean 
reporting_lei | The LEI code for the legal entity under which the security is being reported. | string 
reporting_entity_name | The name of the reporting legal entity for display purposes (as LEI code may not be available). | string 
risk_country_code | Two-letter country code describing where the risk for the security resides. In accordance with ISO 3166-1 | undefined 
seniority | The seniority of the security in the event of sale or bankruptcy of the issuer. | string 
sft_type | The sft_type parameter defines the transaction mechanism conducted for the SFT for this security product. | string 
sources | Identifiers for data sources. Useful for analytics and MI purposes. | array 
start_date | The timestamp that the trade or financial product commences. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
type | This is the type of the security with regards to common regulatory classifications. | string 
trade_date | The timestamp that the trade or financial product terms are agreed. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
transferable | Can the security be transferred between parties or negotiated on the capital market? | boolean 
value_date | The timestamp that the trade or financial product was valued. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
