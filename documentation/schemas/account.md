---
layout:		schema
title:		"account"
---

# Account Schema

---

An Account represents a financial account that describes the funds that a customer has entrusted to a financial institution in the form of deposits or credit balances.

### Properties

Name | Type | Description
--- | --- | ---
id | The unique identifier for the account within the financial institution. | string 
date | The observation or value date for the data in this object. Formatted as YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
accounting_treatment | undefined | undefined 
accrued_interest | The accrued interest since the last payment date and due at the next payment date. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
arrears_balance | The balance of the capital amount that is considered to be in arrears (for overdrafts/credit cards). Monetary type represented as a naturally positive integer number of cents/pence. | integer 
asset_liability | Is the account an asset or a liability on the firm's balance sheet? | string 
balance | The contractual balance on the date and in the currency given. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
base_rate | The base rate represents the basis of the rate on the balance at the given date as agreed in the terms of the account. | string 
break_dates | Dates where this contract can be broken (by either party). Formatted as YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | array 
call_dates | Dates where this contract can be called (by the customer). Formatted as YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | array 
country_code | Two-letter country code for account location/jurisdiction. In accordance with ISO 3166-1. | undefined 
currency_code | Actual currency of the Account in accordance with ISO 4217 standards. It should be consistent with balance, accrued_interest, guarantee_amount and other monetary amounts. | undefined 
customer_id | The unique identifier used by the financial institution to identify the customer that owns the account. | string 
end_date | The end or maturity date of the account. Format should be YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601 | string 
encumbrance_amount | The amount of the account that is encumbered by potential future commitments or legal liabilities. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
encumbrance_type | The type of the encumbrance causing the encumbrance_amount. | string 
first_payment_date | The first payment date for interest payments. | string 
guarantee_amount | The amount of the account that is guaranteed under a Government Deposit Guarantee Scheme. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
guarantee_scheme | The Government Deposit Scheme scheme under which the guarantee_amount is guaranteed. | string 
last_payment_date | The final payment date for interest payments, often coincides with end_date. | string 
next_payment_date | The next date at which interest will be paid or accrued_interest balance returned to zero. | string 
next_withdrawal_date | The next date at which customer is allowed to withdraw money from this account. | string 
on_balance_sheet | Is the account or deposit reported on the balance sheet of the financial institution? | boolean 
prev_payment_date | The most recent previous date at which interest was paid or accrued_interest balance returned to zero. | string 
product_name | The name of the product as given by the financial institution to be used for display and reference purposes. | string 
purpose | The purpose for which the account was created or is being used. | string 
rate | The full interest rate applied to the account balance in percentage terms. Note that this therefore includes the base_rate (ie. not the spread). | number 
rate_type | Describes the type of interest rate applied to the account. | string 
reporting_lei | The LEI code for the legal entity under which the account is being reported. | string 
reporting_entity_name | The name of the reporting legal entity for MI purposes (as LEI code may not be available). | string 
risk_country_code | Two-letter country code describing where the risk for the account resides. In accordance with ISO 3166-1 | undefined 
sources | Identifiers for data sources. Useful for analytics and MI purposes. | array 
start_date | The timestamp that the trade or financial product commences. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
status | Describes if the Account is active or been cancelled. | string 
type | This is the type of the account with regards to common regulatory classifications. | string 
trade_date | The timestamp that the trade or financial product terms are agreed. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
withdrawal_penalty | This is the penalty incurred by the customer for an early withdrawal on this account. An early withdrawal is defined as a withdrawal prior to the next_withdrawal_date. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
count | Describes the number of accounts aggregated into a single row. | integer 
minimum_balance_eur | Indicates the minimum balance, in Euros, of each account within the aggregate. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
