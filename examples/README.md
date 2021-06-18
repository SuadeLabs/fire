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
  - [Agreement examples](#agreement-examples)
    - [Master netting agreement with csa](#master-netting-agreement-with-csa)
    - [Master netting agreement without csa](#master-netting-agreement-without-csa)
  - [Loan examples](#loan-examples)
    - [BBL/CBIL](#bblcbil)
  - [Derivative examples](#derivative-examples)
    - [Bermudan swaption](#bermudan-swaption)
    - [Credit default swap](#credit-default-swap)
    - [Derivative with initial margin](#derivative-with-initial-margin)
    - [Equity option](#equity-option)
    - [Forward rate agreement](#forward-rate-agreement)
    - [FX option](#fx-option)
    - [FX spot](#fx-spot)
    - [FX swap](#fx-swap)
    - [IR cap floor](#ir-cap-floor)
    - [IR digital floor](#ir-digital-floor)
    - [IR swap](#ir-swap)
    - [Swaption](#swaption)
  - [Security examples](#security-examples)
    - [Cash on-hand](#cash-on-hand)
    - [Cash receivable](#cash-receivable)
    - [Cash payable](#cash-payable)
    - [Reverse repo](#reverse-repo)
    - [Variation margin cash posted](#variation-margin-cash-posted)
    - [Variation margin cash received](#variation-margin-cash-received)
    - [Variation margin bond posted](#variation-margin-bond-posted)
    - [Variation margin bond received](#variation-margin-bond-received)
- [Test case examples](#test-case-examples)
  - [Derivatives with Variation Margin (VM)](#derivatives-with-variation-margin-vm)
    - [Gross receivables with VM received](#gross-receivables-with-vm-received)
    - [Gross receivables with VM posted/given](#gross-receivables-with-vm-postedgiven)
  - [Derivatives with Initial Margin (IM)](#derivatives-with-initial-margin-im)
    - [Derivatives facing credit institution](#derivatives-facing-credit-institution)
    - [Derivatives facing central clearing party (CCP)](#derivatives-facing-central-clearing-party-ccp)
  - [Non-margined derivatives](#non-margined-derivatives)
    - [In-the-money derivatives](#in-the-money-derivatives)
    - [Out-the-money derivatives](#out-the-money-derivatives)
  - [Non-derivatives IM posted to a CCP (e.g. RepoClear)](#non-derivatives-im-posted-to-a-ccp-eg-repoclear)
    - [Collateral posted to ccp on non-derivatives](#collateral-posted-to-ccp-on-non-derivatives)
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
### Agreement examples
#### Master netting agreement with csa
```json
{{#include master_netting_agreement_with_csa.json:5:}}
```
#### Master netting agreement without csa
```json
{{#include master_netting_agreement_without_csa.json:5:}}
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
### Derivative examples
#### Bermudan swaption
Cash-settled Bermudan swaption with annual exercise dates referencing 5-year interest rate swap.
```json
{{#include bermudan_swaption.json:5:}}
```
#### Credit default swap
Corporate CDS maturing in 5 years. Protection seller
```json
{{#include corp_cds.json:5:}}
```
#### Derivative with initial margin
```json
{{#include derivative_with_initial_margin.json:5:}}
```
#### Equity option
1Y European Option on a stock.
```json
{{#include eq_option.json:5:}}
```
#### Forward rate agreement
Short 6x12 forward rate agreement; starting in 6 months and ending in 12 months.
```json
{{#include fra_6x12.json:5:}}
```
#### FX option
3m ATM USD Call JPY Put (European).
```json
{{#include fx_option.json:5:}}
```
#### FX spot
100 EUR for 140 CAD spot trade.
```json
{{#include fx_spot.json:5:}}
```
#### FX swap
1Y AUD/USD fx swap. The notional amounts represent the spot exchange occuring on the start date. The rate is used to derive the forward notional on each leg and is exchanged on the end date (80k AUD vs 84k USD).
```json
{{#include fx_swap.json:5:}}
```
#### IR cap floor
1-year EUR collar vs euribor_3m, spot starting.
```json
{{#include ir_cap_floor.json:5:}}
```
#### IR digital floor
1-year EUR 100 0% digital floor vs euribor_3m, spot starting.
```json
{{#include ir_digital_floor.json:5:}}
```
#### IR swap
5-year EUR interest rate swap, forward starting in 5 years.
```json
{{#include ir_swap.json:5:}}
```
#### Swaption
1-year European payer swaption on a 10-year swap, physical settlement.
```json
{{#include swaption.json:5:}}
```
### Security examples
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
#### Reverse repo
Reverse repo transaction with a cash leg on 150 GBP, and a security leg of 140
GBP, starting on June 1st, 2021 and ending on July 1st, 2021.
```json
{{#include rev_repo.json:5:}}
```
#### Variation margin cash posted
```json
{{#include variation_margin_cash_posted.json:5:}}
```
#### Variation margin cash received
```json
{{#include variation_margin_cash_received.json:5:}}
```
#### Variation margin bond posted
```json
{{#include variation_margin_bond_posted.json:5:}}
```
#### Variation margin bond received
```json
{{#include variation_margin_bond_received.json:5:}}
```
---
## Test case examples
### Derivatives with Variation Margin (VM)
#### Gross receivables with VM received
> 2 Derivatives: one is receivable at 200 GBP and the other payable at 100 GBP so the overall gross position is +100 GBP.

> 1 Security: 50 GBP cash collateral received as variation margin.
```json
{{#include derivative_receivables_with_vm_received.json:5:}}
```
> Note the derivatives and the security are linked through the mna_id which matches the agreement id.
#### Gross receivables with VM posted/given
> 2 Derivatives: one is payable at 200 GBP and the other receivable at 100 GBP so the overall gross position is -100 GBP.

> 1 Security: 50 GBP cash collateral posted as variation margin.
```json
{{#include derivative_payables_with_vm_posted.json:5:}}
```
> Note the derivatives and the security are linked through the mna_id which matches the agreement id.

### Derivatives with Initial Margin (IM)
#### Derivatives facing credit institution
> Note IM is directly populated on the derivative schema.
```json
{{#include derivative_with_im_facing_ci.json:5:}}
```
#### Derivatives facing central clearing party (CCP)
> Note IM is directly populated on the derivative schema.
```json
{{#include derivative_with_im_facing_ccp.json:5:}}
```
### Non-margined derivatives
#### In-the-money derivatives
> 2 Derivatives with positive mtm.
```json
{{#include derivative_unmargined_itm.json:5:}}
```
> Note the MNA does not have the "credit_support_type" property.
#### Out-the-money derivatives
> 2 Derivatives with negative mtm.
```json
{{#include derivative_unmargined_otm.json:5:}}
```
> Note the MNA does not have the "credit_support_type" property.
### Non-derivatives IM posted to a CCP (e.g. RepoClear)
#### Collateral posted to ccp on non-derivatives
> Security has "purpose" = "collateral" which signals it is not linked to derivative transactions.
```json
{{#include security_collateral_posted_ccp_non_deriv.json:5:}}
```
