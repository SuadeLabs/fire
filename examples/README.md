---
layout: readme
title: FIRE data examples
---

This README is generated from files in the `examples/` directory.


## Contents

- [Account](#account)
  - [Current Account](#current-account)
  - [Current Account With Guarantee](#current-account-with-guarantee)
  - [Overdraft Account](#overdraft-account)
  - [Pnl Interest Income](#pnl-interest-income)
  - [Pnl Salary Expenses](#pnl-salary-expenses)
  - [Savings Account](#savings-account)
  - [Savings Account With 30Days Notice](#savings-account-with-30days-notice)
  - [Time Deposit 1Year](#time-deposit-1year)
  - [Time Deposit 1Year With 6 Month Withdrawal Option](#time-deposit-1year-with-6-month-withdrawal-option)
- [Derivative](#derivative)
  - [Bermudan Swaption](#bermudan-swaption)
  - [Bond Future](#bond-future)
  - [Bond Future2](#bond-future2)
  - [Cds Index](#cds-index)
  - [Cds Single Name](#cds-single-name)
  - [Commodity Asian Option](#commodity-asian-option)
  - [Commodity Option](#commodity-option)
  - [Eq Index Basket Option](#eq-index-basket-option)
  - [Equity Option](#equity-option)
  - [Equity Total Return Swap](#equity-total-return-swap)
  - [Fra 6X12](#fra-6x12)
  - [Fx Forward](#fx-forward)
  - [Fx Future](#fx-future)
  - [Fx Option](#fx-option)
  - [Fx Option Long Call](#fx-option-long-call)
  - [Fx Option Long Put](#fx-option-long-put)
  - [Fx Option Short Call](#fx-option-short-call)
  - [Fx Option Short Put](#fx-option-short-put)
  - [Fx Spot](#fx-spot)
  - [Fx Swap](#fx-swap)
  - [Interest Rate Swap](#interest-rate-swap)
  - [Interest Rate Swap Amortising](#interest-rate-swap-amortising)
  - [Ir Cap Floor](#ir-cap-floor)
  - [Ir Digital Floor](#ir-digital-floor)
  - [Ir Future](#ir-future)
  - [Margined Netting Agreement](#margined-netting-agreement)
  - [Unmargined Netting Agreement](#unmargined-netting-agreement)
  - [Usd Payer Swaption](#usd-payer-swaption)
  - [Xccy Swap](#xccy-swap)
- [Loan](#loan)
  - [Bbl Loans](#bbl-loans)
  - [Encumbered Loan](#encumbered-loan)
  - [Loan With 2 Customers](#loan-with-2-customers)
  - [Undrawn Committed Loan](#undrawn-committed-loan)
  - [Vostro Account](#vostro-account)
- [Security](#security)
  - [Bank Guarantee Issued](#bank-guarantee-issued)
  - [Cash On Hand](#cash-on-hand)
  - [Cash Payable](#cash-payable)
  - [Cash Receivable](#cash-receivable)
  - [Cet 1 Capital](#cet-1-capital)
  - [Collateral Independent Amount Bond Received](#collateral-independent-amount-bond-received)
  - [Collateral Initial Margin Bond Posted](#collateral-initial-margin-bond-posted)
  - [Collateral Variation Margin Cash Posted](#collateral-variation-margin-cash-posted)
  - [Collateral Variation Margin Cash Received](#collateral-variation-margin-cash-received)
  - [Dividend From Equity](#dividend-from-equity)
  - [Encumbrance Set](#encumbrance-set)
  - [Outright Debt Security](#outright-debt-security)
  - [Repo](#repo)
  - [Rev Repo](#rev-repo)
  - [Security Collateral Posted Ccp Non Deriv](#security-collateral-posted-ccp-non-deriv)
  - [Subordinated Debt](#subordinated-debt)

## Account

#### Current Account

Active GBP current account with accrued interest.

```json
{
  "account": [
    {
      "id": "current_account",
      "date": "2017-06-30T14:03:12Z",
      "trade_date": "2012-02-06T09:30:00Z",
      "start_date": "2012-02-07T00:00:00Z",
      "currency_code": "GBP",
      "balance": 30000,
      "accrued_interest": 2500,
      "type": "current",
      "status": "active",
      "on_balance_sheet": true,
      "asset_liability": "liability",
      "customer_id": "C123456"
    }
  ]
}
```

#### Current Account With Guarantee

GBP current account protected by GB FSCS guarantee up to 8,500 GBP.

```json
{
  "account": [
    {
      "id": "current_account_with_guarantee",
      "date": "2017-06-30T14:03:12Z",
      "trade_date": "2012-02-06T09:30:00Z",
      "start_date": "2012-02-07T00:00:00Z",
      "currency_code": "GBP",
      "balance": 30000,
      "accrued_interest": 2500,
      "guarantee_scheme": "gb_fscs",
      "guarantee_amount": 8500,
      "type": "current",
      "status": "active",
      "on_balance_sheet": true,
      "asset_liability": "liability",
      "customer_id": "C123456"
    }
  ]
}
```

#### Overdraft Account

Overdrawn current account showing negative balance and associated customer record.

```json
{
  "account": [
    {
      "date": "2022-04-20T00:00:00",
      "id": "overdraft",
      "accrued_interest": -50,
      "asset_liability": "asset",
      "balance": -1000,
      "customer_id": "overdraft_customer",
      "on_balance_sheet": true,
      "start_date": "2022-04-20T00:00:00",
      "status": "active",
      "trade_date": "2022-04-20T00:00:00",
      "type": "current"
    }
  ],
  "customer": [
    {
      "date": "2022-04-20T00:00:00",
      "id": "overdraft_customer",
      "country_code": "GB",
      "type": "natural_person"
    }
  ]
}
```

#### Pnl Interest Income

P&L income line item representing GBP interest earned.

```json
{
  "account": [
    {
      "id": "interest_income",
      "date": "2017-06-30T14:03:12Z",
      "currency_code": "GBP",
      "balance": 30000,
      "type": "income",
      "asset_liability": "pnl",
      "purpose": "interest",
      "customer_id": "C123456"
    }
  ]
}
```

#### Pnl Salary Expenses

P&L expense line item for GBP regular wage payments.

```json
{
  "account": [
    {
      "id": "salary_expenses",
      "date": "2017-06-30T14:03:12Z",
      "currency_code": "GBP",
      "balance": 30000,
      "type": "expense",
      "asset_liability": "pnl",
      "purpose": "regular_wages"
    }
  ]
}
```

#### Savings Account

Active GBP savings account with accrued interest.

```json
{
  "account": [
    {
      "id": "savings_account",
      "date": "2017-06-30T14:03:12Z",
      "trade_date": "2012-02-06T09:30:00Z",
      "start_date": "2012-02-07T00:00:00Z",
      "currency_code": "GBP",
      "balance": 30000,
      "accrued_interest": 2500,
      "type": "savings",
      "status": "active",
      "on_balance_sheet": true,
      "asset_liability": "liability",
      "customer_id": "C123456"
    }
  ]
}
```

#### Savings Account With 30Days Notice

GBP savings account that requires 30 days' notice before withdrawal.

```json
{
  "account": [
    {
      "id": "savings_account_with_30days_notice",
      "date": "2017-06-30T14:03:12Z",
      "trade_date": "2012-02-06T09:30:00Z",
      "start_date": "2012-02-07T00:00:00Z",
      "next_withdrawal_date": "2017-07-30T00:00:00Z",
      "currency_code": "GBP",
      "balance": 30000,
      "accrued_interest": 2500,
      "type": "savings",
      "status": "active",
      "on_balance_sheet": true,
      "asset_liability": "liability",
      "customer_id": "C123456"
    }
  ]
}
```

#### Time Deposit 1Year

One-year GBP time deposit maturing on 2018-06-30 with accrued interest.

```json
{
  "account": [
    {
      "id": "time_deposit_1year",
      "date": "2017-06-30T14:03:12Z",
      "trade_date": "2012-02-06T09:30:00Z",
      "start_date": "2012-02-07T00:00:00Z",
      "end_date": "2018-06-30T00:00:00Z",
      "currency_code": "GBP",
      "balance": 30000,
      "accrued_interest": 2500,
      "type": "time_deposit",
      "status": "active",
      "on_balance_sheet": true,
      "asset_liability": "liability",
      "customer_id": "C123456"
    }
  ]
}
```

#### Time Deposit 1Year With 6 Month Withdrawal Option

One-year GBP time deposit with optional withdrawal available after six months.

```json
{
  "account": [
    {
      "id": "time_deposit_1year_with_6_month_withdrawal_option",
      "date": "2017-06-30T14:03:12Z",
      "trade_date": "2012-02-06T09:30:00Z",
      "start_date": "2012-02-07T00:00:00Z",
      "next_withdrawal_date": "2017-12-31T00:00:00Z",
      "end_date": "2018-06-30T00:00:00Z",
      "currency_code": "GBP",
      "balance": 30000,
      "accrued_interest": 2500,
      "type": "time_deposit",
      "status": "active",
      "on_balance_sheet": true,
      "asset_liability": "liability",
      "customer_id": "C123456"
    }
  ]
}
```

## Derivative

#### Bermudan Swaption

Short USD Bermudan swaption on 6M LIBOR with 10,000 notional and physical settlement.

```json
{
  "derivative": [
    {
      "date": "2019-01-01T00:00:00",
      "id": "usd_bermudan_swaption",
      "asset_class": "ir",
      "type": "swaption",
      "leg_type": "put",
      "position": "short",
      "currency_code": "USD",
      "notional_amount": 10000,
      "strike": 0.02,
      "underlying_index": "USD_LIBOR",
      "underlying_index_tenor": "6m",
      "start_date": "2019-01-01T00:00:00",
      "end_date": "2020-01-01T00:00:00",
      "last_payment_date": "2030-01-01T00:00:00",
      "next_exercise_date": "2020-01-01T00:00:00",
      "underlying_price": 0.02,
      "settlement_type": "physical",
      "mtm_dirty": -5
    }
  ]
}
```

#### Bond Future

EUR Bund futures contract with 10,000 notional settling physically in May 2019.

```json
{
  "derivative": [
    {
      "id": "Bund June IMM future",
      "date": "2019-04-30T00:00:00",
      "asset_class": "ir",
      "type": "future",
      "leg_type": "indexed",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "rate": 125.5,
      "underlying_index": "BUND0829",
      "trade_date": "2019-04-01T00:00:00",
      "start_date": "2019-05-02T00:00:00",
      "end_date": "2019-05-04T00:00:00",
      "last_payment_date": "2029-08-15T00:00:00",
      "settlement_type": "physical",
      "mtm_dirty": -25
    }
  ]
}
```

#### Bond Future2

USD Treasury bond future expiring March 2021 with long-dated underlying.

```json
{
  "derivative": [
    {
      "id": "T-Bond Mar21 future",
      "date": "2019-04-30T00:00:00",
      "asset_class": "ir",
      "type": "future",
      "leg_type": "indexed",
      "currency_code": "USD",
      "notional_amount": 100,
      "trade_date": "2019-04-01T00:00:00",
      "start_date": "2019-05-02T00:00:00",
      "end_date": "2021-03-15T00:00:00",
      "last_payment_date": "2041-03-15T00:00:00",
      "underlying_index": "T-bondMar41",
      "settlement_type": "physical"
    }
  ]
}
```

#### Cds Index

Short USD CDX investment-grade index CDS position.

```json
{
  "derivative": [
    {
      "id": "corp_cds_5y",
      "date": "2019-01-01T00:00:00",
      "asset_class": "cr_index",
      "type": "cds",
      "underlying_security_id": "cdx_na_ig",
      "leg_type": "indexed",
      "position": "short",
      "delta": -1,
      "currency_code": "USD",
      "notional_amount": 100,
      "trade_date": "2018-07-01T00:00:00",
      "start_date": "2018-07-03T00:00:00",
      "end_date": "2023-07-03T00:00:00",
      "rate": 0.005,
      "settlement_type": "cash"
    }
  ],
  "security": [
    {
      "id": "cdx_na_ig",
      "date": "2019-01-01T00:00:00",
      "type": "index",
      "currency_code": "USD",
      "cqs_standardised": 3
    }
  ]
}
```

#### Cds Single Name

Short single-name USD corporate CDS referencing a 2028 bond.

```json
{
  "derivative": [
    {
      "id": "corp_cds_5y",
      "date": "2019-01-01T00:00:00",
      "asset_class": "cr_single",
      "type": "cds",
      "underlying_security_id": "Corp_Jul28",
      "leg_type": "indexed",
      "position": "short",
      "delta": -1,
      "currency_code": "USD",
      "notional_amount": 100,
      "trade_date": "2018-07-01T00:00:00",
      "start_date": "2018-07-03T00:00:00",
      "end_date": "2023-07-03T00:00:00",
      "rate": 0.005,
      "settlement_type": "cash"
    }
  ],
  "security": [
    {
      "id": "Corp_Jul28",
      "date": "2019-01-01T00:00:00",
      "type": "bond",
      "underlying_issuer_id": "us_corp",
      "isin_code": "XS1234567890",
      "currency_code": "USD",
      "issue_date": "2018-07-01 00:00:00",
      "maturity_date": "2028-07-01 00:00:00",
      "cqs_standardised": 3
    }
  ],
  "issuer": [
    {
      "id": "us_corp",
      "date": "2019-01-01T00:00:00",
      "type": "corporate",
      "country_code": "US",
      "snp_lt": "a_plus",
      "moodys_lt": "a1"
    }
  ]
}
```

#### Commodity Asian Option

Long USD Asian-style copper put option referencing averaged prices.

```json
{
  "derivative": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "1",
      "asset_class": "metals",
      "type": "option",
      "leg_type": "put",
      "position": "long",
      "currency_code": "USD",
      "underlying_quantity": 100,
      "strike": 9829,
      "underlying_index": "copper average",
      "underlying_price": 9829,
      "supervisory_price": 9766,
      "trade_date": "2020-02-25T00:00:00",
      "start_date": "2020-02-27T00:00:00",
      "end_date": "2021-06-02T00:00:00",
      "last_exercise_date": "2020-12-05T00:00:00",
      "settlement_type": "physical",
      "mtm_dirty": 80
    }
  ]
}
```

#### Commodity Option

Long USD copper put option with physical settlement.

```json
{
  "derivative": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "1",
      "asset_class": "metals",
      "type": "option",
      "leg_type": "put",
      "position": "long",
      "currency_code": "USD",
      "underlying_quantity": 100,
      "strike": 9829,
      "underlying_index": "copper",
      "underlying_price": 9829,
      "trade_date": "2020-02-25T00:00:00",
      "start_date": "2020-02-27T00:00:00",
      "end_date": "2021-06-02T00:00:00",
      "last_exercise_date": "2020-12-05T00:00:00",
      "settlement_type": "physical",
      "mtm_dirty": 193
    }
  ]
}
```

#### Eq Index Basket Option

Equity index basket collar with long and short option legs on a custom index.

```json
{
  "derivative": [
    {
      "id": "1",
      "date": "2021-03-31T00:00:00",
      "asset_class": "eq_index",
      "position": "long",
      "type": "option",
      "leg_type": "call",
      "currency_code": "USD",
      "strike": 100,
      "underlying_security_id": "my_index_basket",
      "trade_date": "2020-03-31T00:00:00",
      "start_date": "2020-03-31T00:00:00",
      "end_date": "2022-03-31T00:00:00",
      "settlement_type": "cash",
      "underlying_price": 100,
      "mtm_dirty": 10,
      "delta": 1.41,
      "vega": 0.021,
      "gamma": 0.014,
      "notional_amount": 1000000
    },
    {
      "id": "2",
      "date": "2021-03-31T00:00:00",
      "asset_class": "eq_index",
      "position": "short",
      "type": "option",
      "leg_type": "call",
      "currency_code": "USD",
      "strike": 131,
      "underlying_security_id": "my_index_basket",
      "trade_date": "2020-03-31T00:00:00",
      "start_date": "2020-03-31T00:00:00",
      "end_date": "2022-03-31T00:00:00",
      "settlement_type": "cash",
      "underlying_price": 100,
      "mtm_dirty": 0,
      "delta": 0.05,
      "vega": 0.001,
      "gamma": 0.004,
      "notional_amount": 1000000
    },
    {
      "id": "3",
      "date": "2021-03-31T00:00:00",
      "asset_class": "eq_index",
      "position": "short",
      "type": "option",
      "leg_type": "put",
      "currency_code": "USD",
      "strike": 85,
      "underlying_security_id": "my_index_basket",
      "trade_date": "2020-03-31T00:00:00",
      "start_date": "2020-03-31T00:00:00",
      "end_date": "2022-03-31T00:00:00",
      "settlement_type": "cash",
      "underlying_price": 100,
      "mtm_dirty": 0,
      "delta": 0.05,
      "vega": 0.001,
      "gamma": 0.004,
      "notional_amount": 1000000
    }
  ],
  "security": [
    {
      "id": "my_index_basket",
      "date": "2021-03-31T00:00:00",
      "type": "index",
      "currency_code": "USD",
      "start_date": "2021-03-31T00:00:00",
      "end_date": "",
      "purpose": "reference",
      "mtm": 100,
      "index_composition": [
        {
          "reference_id": "SX5E",
          "weight": 0.25
        },
        {
          "reference_id": "FTSE100",
          "weight": 0.25
        },
        {
          "reference_id": "TOPIX",
          "weight": 0.25
        },
        {
          "reference_id": "SMI",
          "weight": 0.25
        }
      ]
    }
  ]
}
```

#### Equity Option

Long USD call option on single equity reference EquityABC.

```json
{
  "derivative": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "1",
      "deal_id": "2",
      "asset_class": "eq_single",
      "type": "option",
      "leg_type": "call",
      "position": "long",
      "currency_code": "USD",
      "underlying_quantity": 100.0,
      "strike": 40.0,
      "underlying_security_id": "EquityABC",
      "underlying_price": 25.0,
      "trade_date": "2020-02-25T00:00:00",
      "start_date": "2020-02-27T00:00:00",
      "end_date": "2021-02-27T00:00:00",
      "last_exercise_date": "2020-12-05T00:00:00",
      "settlement_type": "cash",
      "mtm_dirty": 10
    }
  ],
  "security": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "EquityABC",
      "type": "equity",
      "currency_code": "USD",
      "start_date": "2017-01-01T00:00:00",
      "purpose": "reference"
    }
  ]
}
```

#### Equity Total Return Swap

EUR equity total return swap exchanging equity performance for floating EURIBOR.

```json
{
  "derivative": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "eur_equity_trs:equity_leg",
      "deal_id": "eur_equity_trs",
      "asset_class": "eq",
      "type": "vanilla_swap",
      "leg_type": "indexed",
      "position": "short",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "underlying_security_id": "EquityABC",
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2019-02-27T00:00:00",
      "end_date": "2024-02-27T00:00:00",
      "mtm_dirty": 140
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "eur_equity_trs:floating_leg",
      "deal_id": "long_eur_equity_trs",
      "asset_class": "eq",
      "type": "vanilla_swap",
      "leg_type": "floating",
      "position": "long",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "rate": 0.0225,
      "underlying_index": "EURIBOR",
      "underlying_index_tenor": "3m",
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2019-02-27T00:00:00",
      "end_date": "2024-02-27T00:00:00"
    }
  ],
  "security": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "EquityABC",
      "type": "equity",
      "currency_code": "USD",
      "start_date": "2020-03-31T00:00:00",
      "issue_date": "2017-03-01T00:00:00",
      "purpose": "reference"
    }
  ]
}
```

#### Fra 6X12

Short USD 6x12 forward rate agreement referencing 6M LIBOR.

```json
{
  "derivative": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "6x12-fra",
      "asset_class": "ir",
      "type": "fra",
      "leg_type": "indexed",
      "position": "short",
      "currency_code": "USD",
      "notional_amount": 10000,
      "underlying_index": "USD_LIBOR",
      "underlying_index_tenor": "6m",
      "trade_date": "2019-11-25T00:00:00",
      "start_date": "2020-05-27T00:00:00",
      "end_date": "2020-11-27T00:00:00",
      "settlement_type": "cash",
      "rate": 0.005,
      "mtm_dirty": -25
    }
  ]
}
```

#### Fx Forward

AUD/USD FX forward with short AUD leg and long USD leg.

```json
{
  "derivative": [
    {
      "date": "2019-04-30T00:00:00",
      "id": "audusd_swap:aud",
      "deal_id": "audusd_fx_fwd",
      "asset_class": "fx",
      "type": "forward",
      "leg_type": "fixed",
      "position": "short",
      "currency_code": "AUD",
      "notional_amount": 10000,
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2019-02-27T00:00:00",
      "end_date": "2020-02-27T00:00:00",
      "mtm_dirty": -2
    },
    {
      "date": "2019-04-30T00:00:00",
      "id": "audusd_swap:usd",
      "deal_id": "audusd_fx_fwd",
      "asset_class": "fx",
      "type": "forward",
      "leg_type": "fixed",
      "position": "long",
      "currency_code": "USD",
      "notional_amount": 10275,
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2019-02-27T00:00:00",
      "end_date": "2020-02-27T00:00:00"
    }
  ]
}
```

#### Fx Future

Long EUR/CAD FX future with 100 notional and physical delivery.

```json
{
  "derivative": [
    {
      "date": "2019-04-01T00:00:00",
      "id": "eur_cad_future",
      "asset_class": "fx",
      "type": "future",
      "leg_type": "indexed",
      "position": "long",
      "currency_code": "EUR",
      "notional_amount": 100,
      "underlying_currency_code": "CAD",
      "trade_date": "2019-04-01T00:00:00",
      "start_date": "2019-06-15T00:00:00",
      "end_date": "2019-09-15T00:00:00",
      "rate": 1.4,
      "underlying_price": 1.38,
      "settlement_type": "physical",
      "mtm_dirty": -2
    }
  ]
}
```

#### Fx Option

Short USD/JPY call option struck at 130 with March 2020 expiry.

```json
{
  "derivative": [
    {
      "date": "2019-12-31T00:00:00",
      "id": "USDJPY call 130",
      "asset_class": "fx",
      "type": "option",
      "leg_type": "call",
      "position": "short",
      "currency_code": "USD",
      "notional_amount": 100,
      "underlying_currency_code": "JPY",
      "strike": 130,
      "trade_date": "2019-12-01T00:00:00",
      "start_date": "2019-12-05T00:00:00",
      "end_date": "2020-03-05T00:00:00",
      "last_exercise_date": "2020-03-03T00:00:00",
      "underlying_price": 130,
      "mtm_dirty": -2
    }
  ]
}
```

#### Fx Option Long Call

Long USD/JPY call option illustrating positive delta exposure.

```json
{
  "derivative": [
    {
      "date": "2019-12-31T00:00:00",
      "id": "longcall",
      "asset_class": "fx",
      "type": "option",
      "leg_type": "call",
      "position": "long",
      "delta": 1,
      "currency_code": "USD",
      "notional_amount": 100,
      "underlying_currency_code": "JPY",
      "strike": 130,
      "trade_date": "2019-12-01T00:00:00",
      "start_date": "2019-12-05T00:00:00",
      "end_date": "2020-03-05T00:00:00",
      "last_exercise_date": "2020-03-03T00:00:00",
      "underlying_price": 130,
      "mtm_dirty": -2
    }
  ]
}
```

#### Fx Option Long Put

Long USD/JPY put option providing downside protection.

```json
{
  "derivative": [
    {
      "date": "2019-12-31T00:00:00",
      "id": "longput",
      "asset_class": "fx",
      "type": "option",
      "leg_type": "put",
      "position": "long",
      "delta": -1,
      "currency_code": "USD",
      "notional_amount": 100,
      "underlying_currency_code": "JPY",
      "strike": 130,
      "trade_date": "2019-12-01T00:00:00",
      "start_date": "2019-12-05T00:00:00",
      "end_date": "2020-03-05T00:00:00",
      "last_exercise_date": "2020-03-03T00:00:00",
      "underlying_price": 130,
      "mtm_dirty": -2
    }
  ]
}
```

#### Fx Option Short Call

Short USD/JPY call option illustrating negative delta exposure.

```json
{
  "derivative": [
    {
      "date": "2019-12-31T00:00:00",
      "id": "shortcall",
      "asset_class": "fx",
      "type": "option",
      "leg_type": "call",
      "position": "short",
      "delta": -1,
      "currency_code": "USD",
      "notional_amount": 100,
      "underlying_currency_code": "JPY",
      "strike": 130,
      "trade_date": "2019-12-01T00:00:00",
      "start_date": "2019-12-05T00:00:00",
      "end_date": "2020-03-05T00:00:00",
      "last_exercise_date": "2020-03-03T00:00:00",
      "underlying_price": 130,
      "mtm_dirty": -2
    }
  ]
}
```

#### Fx Option Short Put

Short USD/JPY put option generating positive delta exposure.

```json
{
  "derivative": [
    {
      "date": "2019-12-31T00:00:00",
      "id": "shortput",
      "asset_class": "fx",
      "type": "option",
      "leg_type": "put",
      "position": "short",
      "delta": 1,
      "currency_code": "USD",
      "notional_amount": 100,
      "underlying_currency_code": "JPY",
      "strike": 130,
      "trade_date": "2019-12-01T00:00:00",
      "start_date": "2019-12-05T00:00:00",
      "end_date": "2020-03-05T00:00:00",
      "last_exercise_date": "2020-03-03T00:00:00",
      "underlying_price": 130,
      "mtm_dirty": -2
    }
  ]
}
```

#### Fx Spot

EUR/CAD FX spot trade with offsetting legs settling T+2.

```json
{
  "derivative": [
    {
      "date": "2019-04-30T00:00:00",
      "id": "eurcad_spot:eur",
      "deal_id": "eurcad_spot",
      "asset_class": "fx",
      "type": "spot",
      "leg_type": "fixed",
      "position": "long",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "trade_date": "2019-04-30T00:00:00",
      "start_date": "2019-05-02T00:00:00",
      "end_date": "2019-05-02T00:00:00",
      "mtm_dirty": -2
    },
    {
      "date": "2019-04-30T00:00:00",
      "id": "eurcad_spot:cad",
      "deal_id": "eurcad_spot",
      "asset_class": "fx",
      "type": "spot",
      "leg_type": "fixed",
      "position": "short",
      "currency_code": "CAD",
      "notional_amount": 14000,
      "trade_date": "2019-04-30T00:00:00",
      "start_date": "2019-05-02T00:00:00",
      "end_date": "2019-05-02T00:00:00"
    }
  ]
}
```

#### Fx Swap

Legacy AUD/USD FX swap example with fixed legs on both currencies.

```json
{
  "derivative": [
    {
      "date": "2019-04-30T00:00:00",
      "id": "audusd_swap:aud",
      "deal_id": "audusd_swap",
      "asset_class": "fx",
      "type": "vanilla_swap",
      "leg_type": "fixed",
      "position": "short",
      "currency_code": "AUD",
      "notional_amount": 10000,
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2019-02-27T00:00:00",
      "end_date": "2020-02-27T00:00:00",
      "mtm_dirty": -2
    },
    {
      "date": "2019-04-30T00:00:00",
      "id": "audusd_swap:aud",
      "deal_id": "audusd_swap",
      "asset_class": "fx",
      "type": "vanilla_swap",
      "leg_type": "fixed",
      "position": "long",
      "currency_code": "USD",
      "notional_amount": 10275,
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2019-02-27T00:00:00",
      "end_date": "2020-02-27T00:00:00"
    }
  ]
}
```

#### Interest Rate Swap

EUR vanilla interest rate swap receiving fixed and paying floating EURIBOR.

```json
{
  "derivative": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "eur_10y_irs_fixed",
      "deal_id": "eur_10y_irs",
      "asset_class": "ir",
      "type": "vanilla_swap",
      "currency_code": "EUR",
      "leg_type": "fixed",
      "position": "long",
      "notional_amount": 10000,
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2019-02-27T00:00:00",
      "end_date": "2029-02-27T00:00:00",
      "rate": 0.01,
      "mtm_dirty": 70
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "eur_10y_irs_floating",
      "deal_id": "long_eur_10y_irs",
      "asset_class": "ir",
      "type": "vanilla_swap",
      "leg_type": "floating",
      "position": "short",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "rate": 0.0025,
      "underlying_index": "EURIBOR",
      "underlying_index_tenor": "3m",
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2019-02-27T00:00:00",
      "end_date": "2029-02-27T00:00:00"
    }
  ]
}
```

#### Interest Rate Swap Amortising

Amortising EUR interest rate swap with detailed scheduled cash flows.

```json
{
  "derivative": [
    {
      "id": "eur_10y_irs_fixed",
      "deal_id": "eur_10y_irs",
      "date": "2020-03-31T00:00:00",
      "asset_class": "ir",
      "type": "vanilla_swap",
      "leg_type": "fixed",
      "position": "long",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "trade_date": "2020-01-29T00:00:00",
      "start_date": "2020-01-31T00:00:00",
      "end_date": "2022-01-31T00:00:00",
      "rate": 0.01,
      "mtm_dirty": 70
    },
    {
      "id": "eur_10y_irs_floating",
      "deal_id": "long_eur_10y_irs",
      "date": "2020-03-31T00:00:00",
      "asset_class": "ir",
      "type": "vanilla_swap",
      "leg_type": "floating",
      "position": "short",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "trade_date": "2020-01-29T00:00:00",
      "start_date": "2020-01-31T00:00:00",
      "end_date": "2022-01-31T00:00:00",
      "underlying_index": "EURIBOR",
      "underlying_index_tenor": "6m",
      "rate": 0.0025
    }
  ],
  "derivative_cash_flow": [
    {
      "id": "eur_10y_irs_fixed_1",
      "derivative_id": "eur_10y_irs_fixed",
      "date": "2020-03-31T00:00:00",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "reset_date": "2020-01-31T00:00:00",
      "payment_date": "2021-01-31T00:00:00"
    },
    {
      "id": "eur_10y_irs_fixed_2",
      "derivative_id": "eur_10y_irs_fixed",
      "date": "2020-03-31T00:00:00",
      "currency_code": "EUR",
      "notional_amount": 5000,
      "reset_date": "2021-01-31T00:00:00",
      "payment_date": "2022-01-31T00:00:00"
    },
    {
      "id": "eur_10y_irs_floating_1",
      "derivative_id": "eur_10y_irs_floating",
      "date": "2020-03-31T00:00:00",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "reset_date": "2021-01-31T00:00:00",
      "payment_date": "2021_07_31T00:00:00",
      "forward_rate": 0.0075
    },
    {
      "id": "eur_10y_irs_floating_2",
      "derivative_id": "eur_10y_irs_floating",
      "date": "2020-03-31T00:00:00",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "reset_date": "2021-07-31T00:00:00",
      "payment_date": "2022-01-31T00:00:00",
      "forward_rate": 0.0125
    },
    {
      "id": "eur_10y_irs_floating_3",
      "derivative_id": "eur_10y_irs_floating",
      "date": "2020-03-31T00:00:00",
      "currency_code": "EUR",
      "notional_amount": 5000,
      "reset_date": "2022-01-31T00:00:00",
      "payment_date": "2022-07-31T00:00:00",
      "forward_rate": 0.0175
    },
    {
      "id": "eur_10y_irs_floating_4",
      "derivative_id": "eur_10y_irs_floating",
      "date": "2020-03-31T00:00:00",
      "currency_code": "EUR",
      "notional_amount": 5000,
      "reset_date": "2022-07-31T00:00:00",
      "payment_date": "2023-01-31T00:00:00",
      "forward_rate": 0.0225
    }
  ]
}
```

#### Ir Cap Floor

EUR interest rate collar combining a short cap and long floor on 3M EURIBOR.

```json
{
  "derivative": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "short_eur_1y_collar:short_cap",
      "deal_id": "short_eur_1y_collar",
      "asset_class": "ir",
      "type": "cap_floor",
      "leg_type": "call",
      "position": "short",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "underlying_index": "EURIBOR",
      "underlying_index_tenor": "3m",
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2019-02-27T00:00:00",
      "end_date": "2020-02-27T00:00:00",
      "next_exercise_date": "2019-05-25T00:00:00",
      "strike": 0.015,
      "underlying_price": 0.01,
      "mtm_dirty": -40
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "short_eur_1y_collar:long_floor",
      "deal_id": "short_eur_1y_collar",
      "asset_class": "ir",
      "type": "cap_floor",
      "leg_type": "put",
      "position": "long",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "underlying_index": "EURIBOR",
      "underlying_index_tenor": "3m",
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2019-02-27T00:00:00",
      "end_date": "2020-02-27T00:00:00",
      "next_exercise_date": "2019-05-25T00:00:00",
      "strike": 0.005,
      "underlying_price": 0.01,
      "mtm_dirty": 110
    }
  ],
  "derivative_cash_flow": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "short_eur_1y_collar:short_cap 2",
      "derivative_id": "short_eur_1y_collar:short_cap",
      "trade_date": "2019-02-25T00:00:00",
      "asset_class": "ir",
      "leg": "pay",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "balance": 0,
      "reset_date": "2019-05-27T00:00:00",
      "payment_date": "2019-08-27T00:00:00",
      "forward_rate": 0.005
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "short_eur_1y_collar:short_cap 3",
      "derivative_id": "short_eur_1y_collar:short_cap",
      "trade_date": "2019-02-25T00:00:00",
      "asset_class": "ir",
      "leg": "pay",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "balance": 0,
      "reset_date": "2019-08-27T00:00:00",
      "payment_date": "2019-11-27T00:00:00",
      "forward_rate": 0.01
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "short_eur_1y_collar:short_cap 4",
      "derivative_id": "short_eur_1y_collar:short_cap",
      "trade_date": "2019-02-25T00:00:00",
      "asset_class": "ir",
      "leg": "pay",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "balance": 0,
      "reset_date": "2019-11-27T00:00:00",
      "payment_date": "2020-02-27T00:00:00",
      "forward_rate": 0.015
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "short_eur_1y_collar:long_floor 2",
      "derivative_id": "short_eur_1y_collar:long_floor",
      "trade_date": "2019-02-25T00:00:00",
      "asset_class": "ir",
      "leg": "receive",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "balance": 0,
      "reset_date": "2019-05-27T00:00:00",
      "payment_date": "2019-08-27T00:00:00",
      "forward_rate": 0.005
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "short_eur_1y_collar:long_floor 3",
      "derivative_id": "short_eur_1y_collar:long_floor",
      "trade_date": "2019-02-25T00:00:00",
      "asset_class": "ir",
      "leg": "receive",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "balance": 0,
      "reset_date": "2019-08-27T00:00:00",
      "payment_date": "2019-11-27T00:00:00",
      "forward_rate": 0.01
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "short_eur_1y_collar:long_floor 4",
      "derivative_id": "short_eur_1y_collar:long_floor",
      "trade_date": "2019-02-25T00:00:00",
      "asset_class": "ir",
      "leg": "receive",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "balance": 0,
      "reset_date": "2019-11-27T00:00:00",
      "payment_date": "2020-02-27T00:00:00",
      "forward_rate": 0.015
    }
  ]
}
```

#### Ir Digital Floor

EUR digital floor structure with offsetting long and short legs.

```json
{
  "derivative": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "1y digital floor:long floor",
      "deal_id": "1y digital floor",
      "asset_class": "ir",
      "type": "cap_floor",
      "leg_type": "put",
      "position": "long",
      "currency_code": "EUR",
      "notional_amount": 100000,
      "underlying_index": "EURIBOR",
      "underlying_index_tenor": "3m",
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2019-02-27T00:00:00",
      "end_date": "2020-02-27T00:00:00",
      "last_exercise_date": "2019-05-25T00:00:00",
      "strike": 0.0005,
      "mtm_dirty": -40
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "1y digital floor:short floor",
      "deal_id": "1y digital floor",
      "asset_class": "ir",
      "type": "cap_floor",
      "leg_type": "put",
      "position": "short",
      "currency_code": "EUR",
      "notional_amount": 100000,
      "underlying_index": "EURIBOR",
      "underlying_index_tenor": "3m",
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2019-02-27T00:00:00",
      "end_date": "2020-02-27T00:00:00",
      "last_exercise_date": "2019-05-25T00:00:00",
      "strike": -0.0005
    }
  ],
  "derivative_cash_flow": [
    {
      "id": "1y digital floor:long floor_1",
      "derivative_id": "1y digital floor:long floor",
      "date": "2020-03-31T00:00:00",
      "trade_date": "2019-02-25T00:00:00",
      "asset_class": "ir",
      "currency_code": "EUR",
      "notional_amount": 100000,
      "reset_date": "2019-05-27T00:00:00",
      "payment_date": "2019-08-27T00:00:00",
      "forward_rate": 0.0025
    },
    {
      "id": "1y digital floor:long floor_2",
      "derivative_id": "1y digital floor:long floor",
      "date": "2020-03-31T00:00:00",
      "trade_date": "2019-02-25T00:00:00",
      "asset_class": "ir",
      "currency_code": "EUR",
      "notional_amount": 100000,
      "reset_date": "2019-08-27T00:00:00",
      "payment_date": "2019-11-27T00:00:00",
      "forward_rate": 0.005
    },
    {
      "id": "1y digital floor:long floor_3",
      "derivative_id": "1y digital floor:long floor",
      "date": "2020-03-31T00:00:00",
      "trade_date": "2019-02-25T00:00:00",
      "asset_class": "ir",
      "currency_code": "EUR",
      "notional_amount": 100000,
      "reset_date": "2019-11-27T00:00:00",
      "payment_date": "2020-02-27T00:00:00",
      "forward_rate": 0.0075
    },
    {
      "id": "1y digital floor:short floor_1",
      "derivative_id": "1y digital floor:short floor",
      "date": "2020-03-31T00:00:00",
      "trade_date": "2019-02-25T00:00:00",
      "asset_class": "ir",
      "currency_code": "EUR",
      "notional_amount": 100000,
      "reset_date": "2019-05-27T00:00:00",
      "payment_date": "2019-08-27T00:00:00",
      "forward_rate": 0.0025
    },
    {
      "id": "1y digital floor:short floor_2",
      "derivative_id": "1y digital floor:short floor",
      "date": "2020-03-31T00:00:00",
      "trade_date": "2019-02-25T00:00:00",
      "asset_class": "ir",
      "currency_code": "EUR",
      "notional_amount": 100000,
      "reset_date": "2019-08-27T00:00:00",
      "payment_date": "2019-11-27T00:00:00",
      "forward_rate": 0.005
    },
    {
      "id": "1y digital floor:short floor_3",
      "derivative_id": "1y digital floor:short floor",
      "date": "2020-03-31T00:00:00",
      "trade_date": "2019-02-25T00:00:00",
      "asset_class": "ir",
      "currency_code": "EUR",
      "notional_amount": 100000,
      "reset_date": "2019-11-27T00:00:00",
      "payment_date": "2020-02-27T00:00:00",
      "forward_rate": 0.0075
    }
  ]
}
```

#### Ir Future

Long Eurodollar interest rate future settled in cash.

```json
{
  "derivative": [
    {
      "date": "2019-04-30T00:00:00",
      "id": "june_eurodollar_future",
      "asset_class": "ir",
      "type": "future",
      "leg_type": "indexed",
      "position": "long",
      "currency_code": "EUR",
      "notional_amount": 100,
      "underlying_currency_code": "USD",
      "trade_date": "2018-04-01T00:00:00",
      "start_date": "2019-05-02T00:00:00",
      "end_date": "2019-05-04T00:00:00",
      "last_payment_date": "2019-08-02T00:00:00",
      "mtm_dirty": -2,
      "settlement_type": "cash"
    }
  ]
}
```

#### Margined Netting Agreement

Margined IRS under ISDA and CSA including variation and initial margin collateral.

```json
{
  "derivative": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "eur_10y_irs_fixed",
      "deal_id": "eur_10y_irs",
      "customer_id": "ccp_1",
      "mna_id": "isda_master_agreement",
      "csa_id": "csa_daily_margined",
      "asset_class": "ir",
      "type": "vanilla_swap",
      "leg_type": "fixed",
      "position": "long",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2020-02-27T00:00:00",
      "end_date": "2029-02-27T00:00:00",
      "rate": 0.01,
      "mtm_dirty": 70
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "eur_10y_irs_floating",
      "deal_id": "long_eur_10y_irs",
      "customer_id": "counterparty_1",
      "mna_id": "isda_master_agreement",
      "csa_id": "csa_daily_margined",
      "asset_class": "ir",
      "type": "vanilla_swap",
      "leg_type": "floating",
      "position": "short",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "rate": 0.0025,
      "underlying_index": "EURIBOR",
      "underlying_index_tenor": "3m",
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2020-02-27T00:00:00",
      "end_date": "2029-02-27T00:00:00"
    }
  ],
  "customer": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "ccp_1",
      "type": "ccp",
      "currency_code": "GBP",
      "country_code": "GB"
    }
  ],
  "agreement": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "isda_master_agreement",
      "type": "isda",
      "base_currency_code": "GBP",
      "incurred_cva": 0,
      "country_code": "GB"
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "csa_daily_margined",
      "type": "isda",
      "base_currency_code": "EUR",
      "credit_support_type": "scsa_isda_2013",
      "margin_frequency": "daily",
      "threshold": 10,
      "minimum_transfer_amount": 5,
      "country_code": "GB"
    }
  ],
  "security": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "vm_eur_received",
      "customer_id": "ccp_1",
      "mna_id": "isda_master_agreement",
      "csa_id": "csa_daily_margined",
      "type": "cash",
      "purpose": "variation_margin",
      "asset_liability": "liability",
      "currency_code": "EUR",
      "notional_amount": 55,
      "balance": 55,
      "trade_date": "2020-03-31T00:00:00",
      "start_date": "2020-03-31T00:00:00"
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "im_bond_posted",
      "customer_id": "ccp_1",
      "mna_id": "isda_master_agreement",
      "csa_id": "csa_daily_margined",
      "type": "bond",
      "issuer_id": "French Republic",
      "isin_code": "XS1234567890",
      "issue_date": "2018-07-01 00:00:00",
      "maturity_date": "2028-07-01 00:00:00",
      "purpose": "independent_collateral_amount",
      "asset_liability": "asset",
      "currency_code": "EUR",
      "notional_amount": 8,
      "mtm_dirty": -10,
      "trade_date": "2020-03-31T00:00:00",
      "start_date": "2020-03-31T00:00:00",
      "cqs_standardised": 1
    }
  ],
  "issuer": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "French Republic",
      "lei_code": "9695006J0AWHMYNZAL19",
      "type": "central_govt",
      "country_code": "FR",
      "snp_lt": "aa_plus",
      "moodys_lt": "aa1"
    }
  ]
}
```

#### Unmargined Netting Agreement

IRS under ISDA netting set without CSA, showing independent collateral posting.

```json
{
  "derivative": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "eur_10y_irs_fixed",
      "deal_id": "eur_10y_irs",
      "customer_id": "ccp_1",
      "mna_id": "isda_master_agreement",
      "csa_id": "csa_daily_margined",
      "asset_class": "ir",
      "type": "vanilla_swap",
      "leg_type": "fixed",
      "position": "long",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2020-02-27T00:00:00",
      "end_date": "2029-02-27T00:00:00",
      "rate": 0.01,
      "mtm_dirty": 70
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "eur_10y_irs_floating",
      "deal_id": "long_eur_10y_irs",
      "customer_id": "counterparty_1",
      "mna_id": "isda_master_agreement",
      "csa_id": "csa_daily_margined",
      "asset_class": "ir",
      "type": "vanilla_swap",
      "leg_type": "floating",
      "position": "short",
      "currency_code": "EUR",
      "notional_amount": 10000,
      "rate": 0.0025,
      "underlying_index": "EURIBOR",
      "underlying_index_tenor": "3m",
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2020-02-27T00:00:00",
      "end_date": "2029-02-27T00:00:00"
    }
  ],
  "customer": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "ccp_1",
      "type": "ccp",
      "currency_code": "GBP",
      "country_code": "GB"
    }
  ],
  "agreement": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "isda_master_agreement",
      "type": "isda",
      "base_currency_code": "GBP",
      "incurred_cva": 0,
      "country_code": "GB"
    }
  ],
  "security": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "im_bond_posted",
      "customer_id": "ccp_1",
      "mna_id": "isda_master_agreement",
      "type": "bond",
      "issuer_id": "French Republic",
      "isin_code": "XS1234567890",
      "issue_date": "2018-07-01 00:00:00",
      "maturity_date": "2028-07-01 00:00:00",
      "purpose": "independent_collateral_amount",
      "asset_liability": "asset",
      "currency_code": "EUR",
      "notional_amount": 8,
      "mtm_dirty": -10,
      "trade_date": "2020-03-31T00:00:00",
      "start_date": "2020-03-31T00:00:00",
      "cqs_standardised": 1
    }
  ],
  "issuer": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "French Republic",
      "lei_code": "9695006J0AWHMYNZAL19",
      "type": "central_govt",
      "country_code": "FR",
      "snp_lt": "aa_plus",
      "moodys_lt": "aa1"
    }
  ]
}
```

#### Usd Payer Swaption

Short USD payer swaption on 6M LIBOR with physical settlement.

```json
{
  "derivative": [
    {
      "date": "2019-01-01T00:00:00",
      "id": "usd_payer_swaption",
      "asset_class": "ir",
      "type": "swaption",
      "leg_type": "call",
      "position": "short",
      "currency_code": "USD",
      "notional_amount": 10000,
      "strike": 0.02,
      "underlying_index": "USD_LIBOR",
      "underlying_index_tenor": "6m",
      "start_date": "2019-01-01T00:00:00",
      "end_date": "2020-01-01T00:00:00",
      "last_payment_date": "2030-01-01T00:00:00",
      "last_exercise_date": "2020-01-01T00:00:00",
      "underlying_price": 0.02,
      "settlement_type": "physical",
      "mtm_dirty": -5
    }
  ]
}
```

#### Xccy Swap

AUD/USD cross-currency swap with fixed AUD leg, floating USD leg, and principal exchanges.

```json
{
  "derivative": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "AUDUSD_xccy:AUD",
      "deal_id": "AUDUSD_xccy",
      "asset_class": "fx",
      "type": "xccy",
      "leg_type": "fixed",
      "position": "long",
      "currency_code": "AUD",
      "notional_amount": 14000,
      "rate": 0.01,
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2020-02-27T00:00:00",
      "end_date": "2030-02-27T00:00:00",
      "mtm_dirty": 1140
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "AUDUSD_xccy:USD",
      "deal_id": "AUDUSD_xccy",
      "asset_class": "fx",
      "type": "xccy",
      "position": "short",
      "leg_type": "floating",
      "currency_code": "USD",
      "notional_amount": 10000,
      "underlying_index": "USD_LIBOR_BBA",
      "underlying_index_tenor": "3m",
      "trade_date": "2019-02-25T00:00:00",
      "start_date": "2020-02-27T00:00:00",
      "end_date": "2030-02-27T00:00:00"
    }
  ],
  "derivative_cash_flow": [
    {
      "id": "1",
      "date": "2020-03-31T00:00:00",
      "derivative_id": "AUDUSD_xccy:AUD",
      "currency_code": "AUD",
      "notional_amount": 14000,
      "reset_date": "2019-02-27T00:00:00",
      "payment_date": "2019-02-27T00:00:00",
      "balance": -14000,
      "purpose": "principal"
    },
    {
      "id": "2",
      "date": "2020-03-31T00:00:00",
      "derivative_id": "AUDUSD_xccy:AUD",
      "currency_code": "AUD",
      "notional_amount": 14000,
      "reset_date": "2029-02-27T00:00:00",
      "payment_date": "2029-02-27T00:00:00",
      "balance": 14000,
      "purpose": "principal"
    },
    {
      "id": "3",
      "date": "2020-03-31T00:00:00",
      "derivative_id": "AUDUSD_xccy:USD",
      "currency_code": "USD",
      "notional_amount": 10000,
      "reset_date": "2019-02-27T00:00:00",
      "payment_date": "2019-02-27T00:00:00",
      "balance": 10000,
      "purpose": "principal"
    },
    {
      "id": "4",
      "date": "2020-03-31T00:00:00",
      "derivative_id": "AUDUSD_xccy:USD",
      "currency_code": "USD",
      "notional_amount": 10000,
      "reset_date": "2029-02-27T00:00:00",
      "payment_date": "2029-02-27T00:00:00",
      "balance": -10000,
      "purpose": "principal"
    },
    {
      "id": "5",
      "date": "2020-03-31T00:00:00",
      "derivative_id": "AUDUSD_xccy:AUD",
      "currency_code": "USD",
      "reset_date": "2020-02-27T00:00:00",
      "payment_date": "2021-02-27T00:00:00",
      "notional_amount": 14000,
      "balance": 140,
      "purpose": "interest"
    },
    {
      "id": "6",
      "date": "2020-03-31T00:00:00",
      "derivative_id": "AUDUSD_xccy:AUD",
      "currency_code": "USD",
      "reset_date": "2028-02-27T00:00:00",
      "payment_date": "2029-02-27T00:00:00",
      "notional_amount": 14000,
      "balance": 140,
      "purpose": "interest"
    },
    {
      "id": "7",
      "date": "2020-03-31T00:00:00",
      "derivative_id": "AUDUSD_xccy:USD",
      "currency_code": "USD",
      "reset_date": "2020-02-27T00:00:00",
      "payment_date": "2020-05-27T00:00:00",
      "notional_amount": 10000,
      "forward_rate": 0.01,
      "balance": -2466,
      "purpose": "interest"
    },
    {
      "id": "8",
      "date": "2020-03-31T00:00:00",
      "derivative_id": "AUDUSD_xccy:USD",
      "currency_code": "USD",
      "reset_date": "2028-11-27T00:00:00",
      "payment_date": "2029-02-27T00:00:00",
      "notional_amount": 10000,
      "forward_rate": 0.02,
      "balance": -5042,
      "purpose": "interest"
    }
  ]
}
```

## Loan

#### Bbl Loans

Portfolio of GBP Bounce Back Loan exposures including netting, interest-only, and amortising positions.

```json
{
  "loan": [
    {
      "date": "2020-08-08T00:00:00+00:00",
      "id": "BBL_netting",
      "asset_liability": "asset",
      "balance": -2500000,
      "currency_code": "GBP",
      "end_date": "2021-08-01T00:00:00+00:00",
      "on_balance_sheet": true,
      "purpose": "other",
      "rate": 10.0,
      "repayment_frequency": "at_maturity",
      "repayment_type": "repayment",
      "start_date": "2021-08-01T00:00:00+00:00",
      "trade_date": "2020-05-11T00:00:00+00:00",
      "type": "commercial"
    },
    {
      "date": "2020-08-08T00:00:00+00:00",
      "id": "BBL1",
      "asset_liability": "asset",
      "balance": 2500000,
      "currency_code": "GBP",
      "end_date": "2021-08-01T00:00:00+00:00",
      "interest_repayment_frequency": "quarterly",
      "on_balance_sheet": true,
      "purpose": "other",
      "rate": 10.0,
      "repayment_frequency": "at_maturity",
      "repayment_type": "interest_only",
      "start_date": "2020-08-01T00:00:00+00:00",
      "trade_date": "2020-05-11T00:00:00+00:00",
      "type": "commercial"
    },
    {
      "date": "2020-08-08T00:00:00+00:00",
      "id": "BBL2",
      "asset_liability": "asset",
      "balance": 2500000,
      "currency_code": "GBP",
      "end_date": "2026-08-01T00:00:00+00:00",
      "on_balance_sheet": true,
      "purpose": "other",
      "rate": 10.0,
      "repayment_frequency": "monthly",
      "repayment_type": "repayment",
      "start_date": "2021-08-01T00:00:00+00:00",
      "trade_date": "2020-05-11T00:00:00+00:00",
      "type": "commercial"
    }
  ]
}
```

#### Encumbered Loan

Mortgage loan partially encumbered by 50,000 GBP until 2022-10-20.

```json
{
  "loan": [
    {
      "id": "encumbered_loan",
      "date": "2022-04-20T00:00:00Z",
      "accounting_treatment": "amortised_cost",
      "asset_liability": "asset",
      "balance": 150000,
      "currency_code": "GBP",
      "customer_id": "encumbered_loan_customer",
      "encumbrance_amount": 50000,
      "encumbrance_end_date": "2022-10-20T00:00:00Z",
      "end_date": "2023-04-20T00:00:00Z",
      "on_balance_sheet": true,
      "start_date": "2021-04-20T00:00:00Z",
      "trade_date": "2021-04-20T00:00:00Z",
      "type": "mortgage"
    }
  ],
  "customer": [
    {
      "id": "encumbered_loan_customer",
      "date": "2022-04-20T00:00:00Z",
      "country_code": "GB",
      "type": "natural_person"
    }
  ]
}
```

#### Loan With 2 Customers

Loan shared by two customers who each provide income information.

```json
{
  "loan": [
    {
      "id": "loan_with_2_customers",
      "date": "2021-09-30",
      "balance": 10000,
      "customers": [
        {
          "id": "CUST123",
          "income_amount": 5000000
        },
        {
          "id": "CUST234",
          "income_amount": 5000000
        }
      ],
      "repayment_frequency": "monthly"
    }
  ]
}
```

#### Undrawn Committed Loan

Off-balance-sheet committed personal loan limit of 100 GBP for a natural person customer.

```json
{
  "loan": [
    {
      "date": "2022-04-20T00:00:00+00:00",
      "id": "undrawn_committed_loan",
      "accrued_interest_balance": 0,
      "asset_liability": "liability",
      "balance": 100,
      "currency_code": "GBP",
      "customer_id": "undrawn_loan_customer",
      "on_balance_sheet": false,
      "purpose": "other",
      "start_date": "2022-04-20T00:00:00+00:00",
      "status": "committed",
      "trade_date": "2021-04-20T00:00:00+00:00",
      "type": "personal"
    }
  ],
  "customer": [
    {
      "date": "2022-04-20T00:00:00+00:00",
      "id": "undrawn_loan_customer",
      "country_code": "GB",
      "type": "natural_person"
    }
  ]
}
```

#### Vostro Account

Vostro account capturing another bank's cash held as our asset.

```json
{
  "account": [
    {
      "id": "Vostro account at your bank",
      "date": "2017-06-30T14:03:12Z",
      "currency_code": "GBP",
      "balance": 100000,
      "type": "vostro",
      "asset_liability": "asset",
      "customer_id": "bank_123_id",
      "on_balance_sheet": true
    }
  ]
}
```

## Security

#### Bank Guarantee Issued

Off-balance-sheet financial guarantee issued for a corporate client in GBP.

```json
{
  "security": [
    {
      "id": "bank_guarantee",
      "date": "2019-01-01T00:00:00",
      "balance": 100000,
      "currency_code": "GBP",
      "asset_liability": "liability",
      "on_balance_sheet": false,
      "type": "financial_guarantee",
      "customer_id": "corp_123_id"
    }
  ]
}
```

#### Cash On Hand

On-balance-sheet GBP cash holding classified as an asset.

```json
{
  "security": [
    {
      "id": "cash_on_hand",
      "date": "2019-01-01T00:00:00",
      "balance": 100000,
      "currency_code": "GBP",
      "asset_liability": "asset",
      "type": "cash"
    }
  ]
}
```

#### Cash Payable

Short-term GBP cash payable liability settling on 2020-08-01.

```json
{
  "security": [
    {
      "id": "cash_payable",
      "date": "2020-07-30T00:00:00",
      "balance": 100000,
      "currency_code": "GBP",
      "asset_liability": "liability",
      "type": "cash",
      "end_date": "2020-08-01T00:00:00+00:00",
      "isin_code": "DUMMYISIN123"
    }
  ]
}
```

#### Cash Receivable

Short-term GBP cash receivable asset settling on 2020-08-01.

```json
{
  "security": [
    {
      "id": "cash_receivable",
      "date": "2020-07-30T00:00:00",
      "balance": -100000,
      "currency_code": "GBP",
      "asset_liability": "asset",
      "type": "cash",
      "end_date": "2020-08-01T00:00:00+00:00",
      "isin_code": "DUMMYISIN123"
    }
  ]
}
```

#### Cet 1 Capital

Core Equity Tier 1 share capital that is fully paid up.

```json
{
  "security": [
    {
      "id": "Core Equity Tier one capital",
      "date": "2019-01-01T00:00:00",
      "balance": 100000,
      "currency_code": "GBP",
      "asset_liability": "equity",
      "type": "share",
      "capital_tier": "ce_tier_1",
      "purpose": "share_capital",
      "status": "paid_up"
    }
  ]
}
```

#### Collateral Independent Amount Bond Received

NZD bond received as independent amount collateral under an ISDA agreement.

```json
{
  "security": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "independent_amount",
      "customer_id": "corporate",
      "mna_id": "master_agreement",
      "type": "bond",
      "issuer_id": "Asian Development Bank",
      "isin_code": "NZADBDT007C4",
      "issue_date": "2017-05-30T00:00:00",
      "maturity_date": "2024-05-30T00:00:00",
      "purpose": "independent_collateral_amount",
      "asset_liability": "liability",
      "currency_code": "NZD",
      "notional_amount": 100,
      "mtm_dirty": 17,
      "trade_date": "2020-03-31T00:00:00",
      "start_date": "2020-03-31T00:00:00",
      "cqs_standardised": 1
    }
  ],
  "issuer": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "Asian Development Bank",
      "lei_code": "549300X0MVH42CY8Q105",
      "type": "mdb",
      "country_code": "PH",
      "snp_lt": "aaa",
      "moodys_lt": "aaa"
    }
  ],
  "customer": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "corporate",
      "type": "corporate",
      "currency_code": "SGD",
      "country_code": "SG"
    }
  ],
  "agreement": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "master_agreement",
      "type": "isda",
      "base_currency_code": "SGD",
      "netting_restriction": "restrictive_covenant",
      "incurred_cva": 10,
      "country_code": "SG"
    }
  ]
}
```

#### Collateral Initial Margin Bond Posted

EUR sovereign bond posted as initial margin under a CSA.

```json
{
  "security": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "im_posted_bond",
      "customer_id": "credit_insitution",
      "mna_id": "isda_master_agreement",
      "csa_id": "csa_agreement",
      "type": "bond",
      "issuer_id": "French Republic",
      "isin_code": "FR0000571218",
      "issue_date": "1998-03-12T00:00:00",
      "maturity_date": "2025-04-29T00:00:00",
      "purpose": "independent_collateral_amount",
      "asset_liability": "asset",
      "currency_code": "EUR",
      "notional_amount": 100,
      "mtm_dirty": -145,
      "trade_date": "2020-03-31T00:00:00",
      "start_date": "2020-03-31T00:00:00",
      "cqs_standardised": 1
    }
  ],
  "issuer": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "French Republic",
      "lei_code": "9695006J0AWHMYNZAL19",
      "type": "central_govt",
      "country_code": "FR",
      "snp_lt": "aa_plus",
      "moodys_lt": "aa1"
    }
  ],
  "customer": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "credit_insitution",
      "type": "credit_institution",
      "currency_code": "GBP",
      "country_code": "GB"
    }
  ],
  "agreement": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "isda_master_agreement",
      "type": "isda",
      "base_currency_code": "GBP",
      "country_code": "GB"
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "csa_agreement",
      "type": "isda",
      "base_currency_code": "EUR",
      "credit_support_type": "scsa_isda_2013",
      "margin_frequency": "daily",
      "threshold": 10,
      "minimum_transfer_amount": 5,
      "country_code": "GB"
    }
  ]
}
```

#### Collateral Variation Margin Cash Posted

USD variation margin cash posted to a QCCP under the margin agreement.

```json
{
  "security": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "vm_cash_posted",
      "customer_id": "qccp",
      "mna_id": "ccp_master_agreement",
      "csa_id": "ccp_margin_agreement",
      "type": "cash",
      "purpose": "variation_margin",
      "asset_liability": "asset",
      "currency_code": "USD",
      "notional_amount": 25,
      "balance": -25,
      "trade_date": "2020-03-31T00:00:00",
      "start_date": "2020-03-31T00:00:00"
    }
  ],
  "customer": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "qccp",
      "type": "qccp",
      "currency_code": "GBP",
      "country_code": "GB"
    }
  ],
  "agreement": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "ccp_master_agreement",
      "type": "isda",
      "base_currency_code": "GBP",
      "incurred_cva": 0,
      "country_code": "GB"
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "ccp_margin_agreement",
      "type": "isda",
      "base_currency_code": "GBP",
      "credit_support_type": "csa_isda_1995",
      "margin_frequency": "daily_settled",
      "country_code": "GB"
    }
  ]
}
```

#### Collateral Variation Margin Cash Received

EUR variation margin cash received from a QCCP under the margin agreement.

```json
{
  "security": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "vm_cash_received",
      "customer_id": "qccp",
      "mna_id": "ccp_master_agreement",
      "csa_id": "ccp_margin_agreement",
      "type": "cash",
      "purpose": "variation_margin",
      "asset_liability": "liability",
      "currency_code": "EUR",
      "notional_amount": 100,
      "balance": 100,
      "trade_date": "2020-03-31T00:00:00",
      "start_date": "2020-03-31T00:00:00"
    }
  ],
  "customer": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "qccp",
      "type": "qccp",
      "currency_code": "GBP",
      "country_code": "GB"
    }
  ],
  "agreement": [
    {
      "date": "2020-03-31T00:00:00",
      "id": "ccp_master_agreement",
      "type": "isda",
      "base_currency_code": "GBP",
      "incurred_cva": 0,
      "country_code": "GB"
    },
    {
      "date": "2020-03-31T00:00:00",
      "id": "ccp_margin_agreement",
      "type": "isda",
      "base_currency_code": "GBP",
      "credit_support_type": "csa_isda_1995",
      "margin_frequency": "daily_settled",
      "country_code": "GB"
    }
  ]
}
```

#### Dividend From Equity

GBP dividend receivable from an equity position recorded in the trading book.

```json
{
  "security": [
    {
      "date": "2022-12-31T00:00:00+00:00",
      "id": "dividend_from_equity",
      "asset_liability": "asset",
      "balance": 100000,
      "currency_code": "GBP",
      "hqla_class": "ineligible",
      "isin_code": "123456789012",
      "issuer_id": "equity_issuer",
      "on_balance_sheet": true,
      "product_name": "dividend",
      "regulatory_book": "trading_book",
      "reporting_id": "equity_reporter",
      "reporting_entity_name": "equity_entity",
      "start_date": "2022-12-31T00:00:00+00:00",
      "type": "dividend",
      "next_payment_date": "2023-01-25T00:00:00+00:00",
      "trade_date": "2016-01-25T00:00:00+00:00"
    }
  ]
}
```

#### Encumbrance Set

Linked bond, repo, reverse repo, and margin trades illustrating an encumbrance chain.

```json
{
  "security": [
    {
      "id": "outright_debt_security",
      "date": "2022-04-20T00:00:00Z",
      "accounting_treatment": "amortised_cost",
      "asset_liability": "asset",
      "balance": 10000,
      "currency_code": "GBP",
      "end_date": "2022-05-20T00:00:00Z",
      "isin_code": "123456789XYZ",
      "issuer_id": "debt_security_issuer",
      "mtm_dirty": 10000,
      "on_balance_sheet": true,
      "regulatory_book": "trading_book",
      "start_date": "2021-04-20T00:00:00Z",
      "trade_date": "2021-04-20T00:00:00Z",
      "type": "bond"
    },
    {
      "id": "repo_cash",
      "date": "2022-04-20T00:00:00Z",
      "accounting_treatment": "amortised_cost",
      "asset_liability": "liability",
      "balance": 8500,
      "currency_code": "GBP",
      "customer_id": "repo_customer",
      "deal_id": "repo_deal",
      "end_date": "2022-05-20T00:00:00Z",
      "isin_code": "123456789XYZ",
      "movement": "cash",
      "on_balance_sheet": true,
      "regulatory_book": "trading_book",
      "sft_type": "repo",
      "start_date": "2021-04-20T00:00:00Z",
      "trade_date": "2021-04-20T00:00:00Z",
      "type": "bond"
    },
    {
      "id": "repo_collateral",
      "date": "2022-04-20T00:00:00Z",
      "accounting_treatment": "amortised_cost",
      "asset_liability": "asset",
      "currency_code": "GBP",
      "customer_id": "repo_customer",
      "deal_id": "repo_deal",
      "end_date": "2022-05-20T00:00:00Z",
      "isin_code": "123456789XYZ",
      "issuer_id": "debt_security_issuer",
      "movement": "asset",
      "mtm_dirty": -9000,
      "on_balance_sheet": true,
      "regulatory_book": "trading_book",
      "sft_type": "repo",
      "start_date": "2021-04-20T00:00:00Z",
      "trade_date": "2021-04-20T00:00:00Z",
      "type": "bond"
    },
    {
      "id": "reverse_repo_cash",
      "date": "2022-04-20T00:00:00Z",
      "accounting_treatment": "amortised_cost",
      "asset_liability": "asset",
      "balance": -9500,
      "currency_code": "GBP",
      "customer_id": "reverse_repo_customer",
      "deal_id": "reverse_repo_deal",
      "end_date": "2022-05-20T00:00:00Z",
      "isin_code": "123456789XYZ",
      "movement": "cash",
      "on_balance_sheet": true,
      "regulatory_book": "trading_book",
      "sft_type": "rev_repo",
      "start_date": "2021-04-20T00:00:00Z",
      "trade_date": "2021-04-20T00:00:00Z",
      "type": "bond"
    },
    {
      "id": "reverse_repo_collateral",
      "date": "2022-04-20T00:00:00Z",
      "accounting_treatment": "amortised_cost",
      "asset_liability": "liability",
      "currency_code": "GBP",
      "customer_id": "reverse_repo_customer",
      "deal_id": "repo_deal",
      "end_date": "2022-05-20T00:00:00Z",
      "isin_code": "123456789XYZ",
      "issuer_id": "debt_security_issuer",
      "movement": "asset",
      "mtm_dirty": 10000,
      "on_balance_sheet": true,
      "regulatory_book": "trading_book",
      "sft_type": "rev_repo",
      "start_date": "2021-04-20T00:00:00Z",
      "trade_date": "2021-04-20T00:00:00Z",
      "type": "bond"
    },
    {
      "id": "initial_margin_posted",
      "date": "2022-04-20T00:00:00Z",
      "accounting_treatment": "amortised_cost",
      "asset_liability": "asset",
      "csa_id": "csa_agreement",
      "currency_code": "GBP",
      "customer_id": "derivative_customer",
      "deal_id": "derivative_deal",
      "end_date": "2022-05-20T00:00:00Z",
      "isin_code": "123456789XYZ",
      "issuer_id": "debt_security_issuer",
      "mna_id": "isda_master_agreement",
      "movement": "asset",
      "mtm_dirty": -9000,
      "purpose": "independent_collateral_amount",
      "regulatory_book": "trading_book",
      "start_date": "2021-04-20T00:00:00Z",
      "trade_date": "2021-04-20T00:00:00Z",
      "type": "bond"
    }
  ],
  "issuer": [
    {
      "id": "debt_security_issuer",
      "date": "2022-04-20T00:00:00Z",
      "country_code": "GB",
      "type": "central_govt"
    }
  ],
  "customer": [
    {
      "id": "repo_customer",
      "date": "2022-04-20T00:00:00Z",
      "country_code": "GB",
      "type": "credit_institution"
    },
    {
      "id": "reverse_repo_customer",
      "date": "2022-04-20T00:00:00Z",
      "country_code": "GB",
      "type": "credit_institution"
    },
    {
      "id": "derivative_customer",
      "date": "2022-04-20T00:00:00Z",
      "country_code": "GB",
      "type": "investment_firm"
    }
  ],
  "agreement": [
    {
      "id": "isda_master_agreement",
      "date": "2022-04-20T00:00:00Z",
      "base_currency_code": "GBP",
      "country_code": "GB",
      "type": "isda"
    },
    {
      "id": "csa_agreement",
      "date": "2022-04-20T00:00:00Z",
      "base_currency_code": "EUR",
      "country_code": "GB",
      "credit_support_type": "scsa_isda_2013",
      "marging_frequency": "daily",
      "minimum_transfer_amount": 50,
      "threshold": 10
    }
  ]
}
```

#### Outright Debt Security

GBP trading book bond position held on balance sheet.

```json
{
  "security": [
    {
      "id": "outright_debt_security",
      "date": "2022-04-20T00:00:00Z",
      "accounting_treatment": "amortised_cost",
      "asset_liability": "asset",
      "balance": 10000,
      "currency_code": "GBP",
      "end_date": "2022-05-20T00:00:00Z",
      "issuer_id": "debt_security_issuer",
      "mtm_dirty": 10000,
      "on_balance_sheet": true,
      "regulatory_book": "trading_book",
      "start_date": "2021-04-20T00:00:00Z",
      "trade_date": "2021-04-20T00:00:00Z",
      "type": "bond"
    }
  ],
  "issuer": [
    {
      "id": "debt_security_issuer",
      "date": "2022-04-20T00:00:00Z",
      "country_code": "GB",
      "type": "credit_institution"
    }
  ]
}
```

#### Repo

GBP repo transaction with a cash liability leg and encumbered bond asset.

```json
{
  "security": [
    {
      "id": "repo_cash_leg",
      "date": "2021-06-15T00:00:00",
      "currency_code": "GBP",
      "end_date": "2021-07-01T00:00:00Z",
      "balance": 15000,
      "cqs_standardised": 1,
      "hqla_class": "i",
      "issuer_id": "uk_central_government_id",
      "movement": "cash",
      "sft_type": "repo",
      "start_date": "2021-06-01T00:00:00Z",
      "type": "bond",
      "trade_date": "2021-06-01T00:00:00Z",
      "asset_liability": "liability"
    },
    {
      "id": "repo_asset_leg",
      "date": "2021-06-15T00:00:00",
      "currency_code": "GBP",
      "end_date": "2021-07-01T00:00:00Z",
      "cqs_standardised": 1,
      "hqla_class": "i",
      "mtm_dirty": -14000,
      "movement": "asset",
      "sft_type": "repo",
      "start_date": "2021-06-01T00:00:00Z",
      "type": "bond",
      "trade_date": "2021-06-01T00:00:00Z",
      "asset_liability": "asset",
      "issuer_id": "uk_central_government_id",
      "maturity_date": "2030-01-01T00:00:00Z"
    }
  ]
}
```

#### Rev Repo

GBP reverse repo transaction with a cash asset leg and bond collateral liability.

```json
{
  "security": [
    {
      "id": "rev_repo_cash_leg",
      "date": "2021-06-15T00:00:00",
      "currency_code": "GBP",
      "end_date": "2021-07-01T00:00:00Z",
      "cqs_standardised": 1,
      "hqla_class": "i",
      "issuer_id": "uk_central_government_id",
      "balance": -15000,
      "movement": "cash",
      "sft_type": "rev_repo",
      "start_date": "2021-06-01T00:00:00Z",
      "type": "bond",
      "trade_date": "2021-06-01T00:00:00Z",
      "asset_liability": "asset"
    },
    {
      "id": "rev_repo_asset_leg",
      "date": "2021-06-15T00:00:00",
      "currency_code": "GBP",
      "end_date": "2021-07-01T00:00:00Z",
      "cqs_standardised": 1,
      "hqla_class": "i",
      "mtm_dirty": 14000,
      "movement": "asset",
      "sft_type": "rev_repo",
      "start_date": "2021-06-01T00:00:00Z",
      "type": "bond",
      "trade_date": "2021-06-01T00:00:00Z",
      "asset_liability": "liability",
      "issuer_id": "uk_central_government_id",
      "maturity_date": "2030-01-01T00:00:00Z"
    }
  ]
}
```

#### Security Collateral Posted Ccp Non Deriv

GBP bond collateral posted to a CCP against non-derivative exposure.

```json
{
  "agreement": [
    {
      "id": "MNA1",
      "date": "2018-12-31 00:00:00",
      "start_date": "2017-01-31 00:00:00",
      "country_code": "GB",
      "type": "isda"
    }
  ],
  "customer": [
    {
      "id": "customer_ccp",
      "date": "2018-12-31 00:00:00",
      "type": "ccp",
      "country_code": "GB"
    }
  ],
  "security": [
    {
      "id": "collat_cash_posted_50",
      "date": "2018-12-31 00:00:00",
      "trade_date": "2018-12-31 00:00:00",
      "start_date": "2018-12-31 00:00:00",
      "asset_liability": "asset",
      "currency_code": "GBP",
      "balance": 5000,
      "mtm_dirty": 5000,
      "type": "bond",
      "purpose": "collateral",
      "mna_id": "MNA1",
      "customer_id": "customer_ccp"
    }
  ]
}
```

#### Subordinated Debt

Tier 2 subordinated debt issuance of 1,000,000 GBP with quarterly coupons.

```json
{
  "security": [
    {
      "date": "2022-04-20T00:00:00+00:00",
      "id": "subordinated_debt",
      "accounting_treatment": "fv_oci",
      "asset_liability": "liability",
      "balance": 1000000,
      "capital_tier": "tier_2",
      "currency_code": "GBP",
      "end_date": "2027-04-20T00:00:00+00:00",
      "interest_repayment_frequency": "quarterly",
      "issuer_id": "subordinated_debt_issuer",
      "movement": "issuance",
      "notional_amount": 1000000,
      "rate": 10,
      "seniority": "subordinated_unsecured",
      "start_date": "2022-04-20T00:00:00+00:00",
      "type": "equity",
      "trade_date": "2022-04-20T00:00:00+00:00"
    }
  ],
  "issuer": [
    {
      "date": "2022-04-20T00:00:00+00:00",
      "id": "subordianted_debt_issuer",
      "country_code": "GB",
      "type": "credit_institution"
    }
  ]
}
```
