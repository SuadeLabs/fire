---
layout:		schema
title:		"loan"
---

# Loan Schema

---

Data schema defining the characteristics of a loan product.

### Properties

Name | Type | Description
--- | --- | ---
id | The unique identifier for the loan within the financial institution. | string 
date | YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
accounting_treatment | undefined | undefined 
accrued_interest_balance | The accrued interest due at the next payment date. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
administration | How the loan was administered by the lender. | string 
arrears_arrangement | The arrangement the lender has made with the borrower regarding the amount referenced in the arrears_balance. | string 
arrears_balance | The balance of the loan or capital amount that is considered to be in arrears. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
asset_liability | Is the loan an asset or a liability on the firm's balance sheet? | string 
balance | The balance of the loan or capital still to be repaid. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
base_rate | The base rate represents the basis of the repayment rate on the borrowed funds at the given date as agreed in the terms of the loan. | string 
currency_code | undefined | undefined 
customers | undefined | array 
encumbrance_amount | The amount of the loan that is encumbered by potential future commitments or legal liabilities. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
end_date | YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601 | string 
facility_currency_code | The currency of the credit facility if not the same as loan currency_code. | undefined 
first_payment_date | The first payment date for interest payments. | string 
guarantee_amount | The amount of the loan that is guaranteed by the guarantor. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
guarantor_id | The unique identifier for the guarantor of the loan. | string 
impairment_amount | The impairment amount for a loan is the allowance for loan impairments set aside by the firm that accounts for the event that the loan becomes impaired in the future. | integer 
impairment_type | The loss event resulting in the impairment of the loan. | string 
issuer_id | The unique identifier for the issuer of the loan. | string 
last_payment_date | The final payment date for interest payments, often coincides with end_date. | string 
limit_amount | The total credit limit on the loan. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
lnrf_amount | The total amount of non-recourse funding linked to the loan. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
movement | The movement parameter describes how the loan arrived to the firm. | string 
next_payment_date | The next date at which interest will be paid or accrued_interest balance returned to zero. | string 
notional_amount | The original notional amount of the loan. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
on_balance_sheet | Is the loan reported on the balance sheet of the financial institution? | boolean 
originator_id | The unique identifier used by the financial institution to identify the originator of the loan product. | string 
originator_type | The type of financial institution that acted as the originator of the loan product. | string 
prev_payment_date | The most recent previous date at which interest was paid or accrued_interest balance returned to zero. | string 
product_name | The name of the product as given by the financial institution to be used for display and reference purposes. | string 
provision_amount | The amount of reserves that is provisioned by the financial institution to cover the potential loss on the loan. Monetary type represented as a naturally positive integer number of cents/pence. | integer 
provision_type | The provision type parameter details the provisions the issuing firm has allocated to cover potential losses from issuing a loan. | string 
purpose | The underlying reason the borrower has requested the loan. | string 
rate | The full interest rate applied to the loan balance. Note that for tracker rates this includes the benchmark (ie. not the credit spread). Percentages represented as a decimal/float such that 1.5% is 0.015. | number 
rate_type | Describes the type of interest rate applied to the loan. | string 
regulated | Is this loan regulated or unregulated? | boolean 
repayment_frequency | Repayment frequency of the loan refers to how often the repayments occur. | string 
repayment_type | Repayment type of the loan refers to whether the customer will be repaying capital + interest, just interest or a combination of the two. | string 
reporting_lei | The LEI code for the legal entity under which the loan is being reported. | string 
reporting_entity_name | The name of the reporting legal entity for display purposes (as LEI code may not be available). | string 
risk_country_code | Two-letter country code describing where the risk for the security resides. In accordance with ISO 3166-1 | undefined 
secured | Is this loan secured or unsecured? | boolean 
securitised | Is this loan securitised? | boolean 
sources | Identifiers for data sources. Useful for analytics and MI purposes. | array 
start_date | The timestamp that the trade or financial product commences. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
status | Describes if the loan is active or been cancelled. | string 
trade_date | The timestamp that the trade or financial product terms are agreed. YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
type | The form of the loan product administered by the financial institution, with regards to common regulatory classifications. | string 
count | Describes the number of loans aggregated into a single row. | integer 
minimum_balance_eur | Indicates the minimum balance, in Euros, of each loan within the aggregate. | integer 
