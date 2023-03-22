---
layout: readme
title: FIRE data examples
---

The following are a few examples of common financial trades.

- [Individual element examples](#individual-element-examples)
  - [Account examples](#account-examples)
    - [Current account](#current-account)
    - [Current account with guarantee](#current-account-with-guarantee)
    - [Savings account](#savings-account)
    - [Savings account with notice](#savings-account-with-notice)
    - [1-year time deposit](#1-year-time-deposit)
    - [1-year time deposit with 6-month withdrawal option](#1-year-time-deposit-with-6-month-withdrawal-option)
    - [PNL interest income](#pnl-interest-income)
    - [PNL salary expenses](#pnl-salary-expenses)
  - [Loan examples](#loan-examples)
    - [BBL/CBIL](#bblcbil)
    - [Nostro account](#nostro-account)
    - [Loan with two customers](#loan-with-two-customers)
  - [Derivative examples](#derivative-examples)
    - [Bermudan swaption](#bermudan-swaption)
    - [Bond future](#bond-future)
    - [Cross-currency swap](#cross-currency-swap)
    - [Commodity option](#commodity-option)
    - [Credit default swap  - Index](#credit-default-swap----index)
    - [Credit default swap - Single name](#credit-default-swap---single-name)
    - [Equity option](#equity-option)
    - [Equity total return swap](#equity-total-return-swap)
    - [Forward rate agreement](#forward-rate-agreement)
    - [FX forward](#fx-forward)
    - [FX future](#fx-future)
    - [FX option](#fx-option)
    - [FX spot](#fx-spot)
    - [FX swap](#fx-swap)
    - [Interest rate cap floor](#interest-rate-cap-floor)
    - [Interest rate digital floor](#interest-rate-digital-floor)
    - [Interest rate future](#interest-rate-future)
    - [Interest rate swap](#interest-rate-swap)
    - [Interest rate swap amortising](#interest-rate-swap-amortising)
    - [Margined netting agreement](#margined-netting-agreement)
    - [Swaption](#swaption)
    - [Unmargined netting agreement](#unmargined-netting-agreement)
  - [Security examples](#security-examples)
    - [Bank guarantee issued](#bank-guarantee-issued)
    - [Core equity tier-1 capital](#core-equity-tier-1-capital)
    - [Cash on-hand](#cash-on-hand)
    - [Cash receivable](#cash-receivable)
    - [Cash payable](#cash-payable)
    - [Collateral posted to ccp on non-derivatives](#collateral-posted-to-ccp-on-non-derivatives)
    - [Initial margin posted](#initial-margin-posted)
    - [Independent amount received](#independent-amount-received)
    - [Reverse repo](#reverse-repo)
    - [Repo](#repo)
    - [Variation margin cash posted](#variation-margin-cash-posted)
    - [Variation margin cash received](#variation-margin-cash-received)
## Individual element examples
### Account examples
#### Current account
```json
{{#include current_account.json:5:}}
```
#### Current account with guarantee
```json
{{#include current_account_with_guarantee.json:5:}}
```
#### Savings account
```json
{{#include savings_account.json:5:}}
```
#### Savings account with notice
```json
{{#include savings_account_with_notice.json:5:}}
```
#### 1-year time deposit
```json
{{#include time_deposit_1year.json:5:}}
```
#### 1-year time deposit with 6-month withdrawal option
```json
{{#include time_deposit_1year_with_6_month_withdrawal_option.json:5:}}
```
#### PNL interest income
```json
{{#include pnl_interest_income.json:5:}}
```
#### PNL salary expenses
```json
{{#include pnl_salary_expenses.json:5:}}
```
### Loan examples
#### BBL/CBIL
These loans can be represented as a combination of two independent loans.

The first loan is a 25K GBP payable quarterly during 1 year (From Aug 1st, 2020 to Aug 1st, 2021).
```json
{
    "id": "BBL1",
    "date": "2020-08-08T00:00:00+00:00",
    "balance": 2500000,
    "currency_code": "GBP",
    "end_date": "2021-08-01T00:00:00+00:00",
    "interest_repayment_frequency": "quarterly",
    "repayment_frequency": "at_maturity",
    "repayment_type": "interest_only",
    "start_date": "2020-08-01T00:00:00+00:00",
    "trade_date": "2020-05-11T00:00:00+00:00"
}
```
The second loan is a 25K GBP payable monthly during 5 years (From Aug 1st, 2021 to Aug 1st, 2026).
```json
{
    "id": "BBL2",
    "date": "2020-08-08T00:00:00+00:00",
    "balance": 2500000,
    "currency_code": "GBP",
    "end_date": "2026-08-01T00:00:00+00:00",
    "repayment_frequency": "monthly",
    "repayment_type": "repayment",
    "start_date": "2021-08-01T00:00:00+00:00",
    "trade_date": "2020-05-11T00:00:00+00:00"
}
```
BBL_1 will create an inflow of 25K GBP, and BBL_2 will create an outflow of 25K GBP on Aug 1st, 2021.

If you are working with reports that separates inflows from outflows, you will get an excess on the inflow and an excess of the outflow.

To eliminate this excess, we can introduce a third loan.
```json
{
    "id": "BBL_netting",
    "date": "2020-08-08T00:00:00+00:00",
    "balance": -2500000,
    "currency_code": "GBP",
    "end_date": "2021-08-01T00:00:00+00:00",
    "repayment_frequency": "at_maturity",
    "repayment_type": "repayment",
    "start_date": "2021-08-01T00:00:00+00:00"
}
```
**Please download the complete [examples](bbl_loans.json)**
#### Nostro account
Nostro account, of 1000 GBP, held at another credit institution
```json
{{#include nostro_account.json:5:}}
```
#### Loan with two customers
A loan example showing what the json looks like for loans with two customers
```json
{{#include_loan_with_2_customers.json:5:}}
```
### Derivative examples
#### Bermudan swaption
Short USD 1y into 10y receiver swaption exercisable annually with physical settlement
```json
{{#include bermudan_swaption.json:5:}}
```
#### Bond future
June IMM Bund future (underlying index is the expected CTD on the reporting date)
```json
{{#include bond_future.json:5:}}
```
Futures on 20-year treasury bond that matures in 2 years
```json
{{#include bond_future2.json:5:}}
```
#### Cross-currency swap
Long 10-year forward_starting AUD/EUR cross-currency swap
```json
{{#include xccy_swap.json:5:}}
```
#### Commodity option
Long 100 June21 at-the-money copper put
```json
{{#include commodity_option.json:5:}}
```
#### Credit default swap  - Index
Index CDS; CDS on the cdx_na_ig index
```json
{{#include cds_index.json:5:}}
```
#### Credit default swap - Single name
Single name CDS; reference obligation US corporate bond with July 2028 maturity
```json
{{#include cds_single_name.json:5:}}
```
#### Equity option
Long 100 1-year 40 call on EquityABC.
```json
{{#include equity_option.json:5:}}
```
#### Equity total return swap
Short 5y EUR total return swap on EquityABC
```json
{{#include equity_total_return_swap.json:5:}}
```
#### Forward rate agreement
Short 6x12 USD FRA
```json
{{#include fra_6x12.json:5:}}
```
#### FX forward
Short AUDUSD forward
```json
{{#include fx_forward.json:5:}}
```
#### FX future
Long June EURCAD future
```json
{{#include fx_future.json:5:}}
```
#### FX option
Short USD call YEN put FX option, exercise on Match 2020
```json
{{#include fx_option.json:5:}}
```
#### FX spot
Long EURCAD spot (100 EUR for 140 CAD spot trade)
```json
{{#include fx_spot.json:5:}}
```
#### FX swap
Short 1-year AUDUSD fx swap. The notional amounts are used to calculate the spot rate (occuring on the start date).
```json
{{#include fx_swap.json:5:}}
```
#### Interest rate cap floor
Short 1y collar vs Euribor 3M
```json
{{#include ir_cap_floor.json:5:}}
```
#### Interest rate digital floor
Long EUR 1y 0% digital floor vs Euribor 3M
```json
{{#include ir_digital_floor.json:5:}}
```
#### Interest rate future
June three-month cash-settled interest rate future.
```json
{{#include ir_future.json:5:}}
```
#### Interest rate swap
Long 10y EUR irs vs Euribor 3M, bullet
```json
{{#include interest_rate_swap.json:5:}}
```
#### Interest rate swap amortising
Long 2y EUR irs vs Euribor 6M, amortising annually
```json
{{#include interest_rate_swap_amortising.json:5:}}
```
#### Margined netting agreement
Margined netting agreement, collateralised with initial collateral amount and variation margin
```json
{{#include margined_netting_agreement.json:5:}}
```
#### Swaption
Short USD 1y into 10y payer swaptionwith physical settlement
```json
{{#include swaption.json:5:}}
```
#### Unmargined netting agreement
Unmargined netting agreement, collateralised with initial collateral amount
```json
{{#include unmargined_netting_agreement.json:5:}}
```
### Security examples
#### Bank guarantee issued
Guarantee of 1000 GBP issued by the bank for a customer
```json
{{#include bank_guarantee_issued.json:5:}}
```
#### Core equity tier-1 capital
Core equity tier 1 capital of 1000 GBP
```json
{{#include cet_1_capital.json:5:}}
```
#### Cash on-hand
Cash balance representing 1000 GBP.
```json
{{#include cash_on_hand.json:5:}}
```
#### Cash receivable
Cash receivable representing a 1000 GBP claim expiring on August 1st 2020 on a security with isin 'DUMMYISIN123'.
```json
{{#include cash_receivable.json:5:}}
```
#### Cash payable
Cash payable representing a 1000 GBP claim expiring on August 1st 2020 on a
security with isin 'DUMMYISIN123'.
```json
{{#include cash_payable.json:5:}}
```
#### Collateral posted to ccp on non-derivatives
Non-derivatives IM posted to a CCP (e.g. RepoClear)
> Security has "purpose" = "collateral" which signals it is not linked to derivative transactions.
```json
{{#include security_collateral_posted_ccp_non_deriv.json:5:}}
```
#### Initial margin posted
Bond collateral used as initial margin posted
```json
{{#include collateral_initial_margin_bond_posted.json:5:}}
```
#### Independent amount received
Bond collateral used as independent amount received
```json
{{#include collateral_independent_amount_bond_received.json:5:}}
```
#### Reverse repo
Reverse repo transaction with a cash leg of 150 GBP, and a security leg of 140
GBP, starting on June 1st, 2021 and ending on July 1st, 2021. The maturity date
on the security leg refers to the maturity of the bond received as collateral.
```json
{{#include rev_repo.json:5:}}
```
#### Repo
Repo transaction with a cash leg of 150 GBP, and a security leg of 140
GBP, starting on June 1st, 2021 and ending on July 1st, 2021. The maturity date
on the security leg refers to the maturity of the bond posted as collateral.
```json
{{#include repo.json:5:}}
```
#### Variation margin cash posted
Cash collateral used as variation margin posted
```json
{{#include collateral_variation_margin_cash_posted.json:5:}}
```
#### Variation margin cash received
Cash collateral used as variation margin received
```json
{{#include collateral_variation_margin_cash_received.json:5:}}
```
---
