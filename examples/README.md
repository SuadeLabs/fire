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
    - [Overdraft account](#overdraft-account)
    - [Vostro account](#vostro-account)
    - [Regular time deposit](#regular-time-deposit)
    - [Transactional time deposit](#transactional-time-deposit)
    - [ISA time deposit](#isa-time-deposit)
    - [Retail bonds](#retail-bonds)
    - [Fees income received](#fees-income-received)
    - [Expense account](#expense-account)
    - [Firm operating expenses](#firm-operating-expenses)
    - [Other expense](#other-expense)
    - [Recurring non-ordinary expenses](#recurring-non-ordinary-expenses)
    - [Unknown expenses](#unknown-expenses)
  - [Loan examples](#loan-examples)
    - [BBL/CBIL](#bblcbil)
    - [Loan with two customers](#loan-with-two-customers)
    - [Nostro account](#nostro-account)
    - [Operational nostro account](#operational-nostro-account)
    - [Buy to let commercial loan](#buy-to-let-commercial-loan)
    - [Buy to let commercial loan high risk](#buy-to-let-commercial-loan-high-risk)
    - [Other commercial loan](#other-commercial-loan)
    - [Speculative property commercial loan](#speculative-property-commercial-loan)
    - [Further advance commercial loan](#further-advance-commercial-loan)
    - [Bridging commercial property loan](#bridging-commercial-property-loan)
    - [Remortgage commercial property loan](#remortgage-commercial-property-loan)
    - [Other remortgage commercial property loan](#other-remortgage-commercial-property-loan)
    - [Buy to let mortgage](#buy-to-let-mortgage)
    - [Other mortgage](#other-mortgage)
    - [Speculative property mortgage](#speculative-property-mortgage)
    - [Remortgage](#remortgage)
    - [First time buyer mortgage](#first-time-buyer-mortgage)
    - [House purchase mortgage](#house-purchase-mortgage)
    - [Other remortgage](#other-remortgage)
    - [Further advance mortgage](#further-advance-mortgage)
    - [Construction mortgage](#construction-mortgage)
    - [Buy to let construction mortgage](#buy-to-let-construction-mortgage)
    - [Personal buy to let loan](#personal-buy-to-let-loan)
    - [Other personal loan](#other-personal-loan)
    - [Other loan](#other-loan)
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
    - [USD Payer Swaption](#usd_payer_swaption)
    - [Unmargined netting agreement](#unmargined-netting-agreement)
    - [Commodity asian option](#commodity-asian-option)
    - [Single stock forward](#single-stock-forward)
    - [Single stock forward in stocks](#single-stock-forward-in-stocks)
    - [Commodity forward](#commodity-forward)
    - [Commodity forward in units](#commodity-forward-in-units)
    - [Interest rate swap forward starting](#interest-rate-swap-forward-starting)
    - [Overnight index swap](#overnight-index-swap)
    - [Interest rate basis swap](#interest-rate-basis-swap)
    - [Cancellable swap](#cancellable-swap)
    - [Inflation linked swap](#inflation-linked-swap)
    - [Commodity swap](#commodity-swap)
    - [Equity index option](#equity-index-option)
    - [FX barrier option](#fx-barrier-option)
    - [FX ndf](#fx-ndf)
    - [FX ndf forward starting](#fx-ndf-forward-starting)
    - [IR overnight index future](#ir-overnight-index-future)
    - [BTP future](#btp-future)
    - [Equity index future](#equity-index-future)
    - [Equity single name future](#equity-single-name-future)
    - [Commodity future](#commodity-future)
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
    - [Firm capital](#firm-capital)
    - [ABS sts securitisation](#abs-sts-securitisation)
    - [ABS traditional subordinated](#abs-traditional-subordinated)
    - [ABS traditional senior](#abs-traditional-senior)
    - [Share](#share)
    - [Share hqla level 2b](#share-hqla-level-2b)
    - [Covered bond](#covered-bond)
    - [Regional government bond](#regional-government-bond)
    - [Guaranteed corporate bond](#guaranteed-corporate-bond)
    - [Corporate bond](#corporate-bond)
    - [Debt security issued liability](#debt-security-issued-liability)
    - [Debt security issued capital](#debt-security-issued-capital)
    - [Medium term note issued](#medium-term-note-issued)
    - [Bankruptcy remote bond](#bankruptcy-remote-bond)
    - [Rev repo bond](#rev-repo-bond)
    - [Repo liability](#repo-liability)
    - [Repo asset](#repo-asset)
    - [Term funding scheme](#term-funding-scheme)
    - [Unsettled repo](#unsettled-repo)
    - [Central bank required reserves](#central-bank-required-reserves)
    - [Bank of england levy](#bank-of-england-levy)
    - [Certificate of deposit](#certificate-of-deposit)
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
{{#include savings_account_with_30days_notice.json:5:}}
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
#### Overdraft account
A current account which is in overdraft
```json
{{#include overdraft_account.json:5:}}
```
#### Vostro account
A bank account held by a foreign bank to conduct transactions in the same currency as the domestic reporter bank
```json
{{#include vostro_account.json:5:}}
```
#### Regular time deposit
A time_deposit account is a fixed term deposit with an end_date. It must have a maturity of at least 7 days.
```json
{{#include regular_time_deposit.json:5:}}
```
#### Transactional time deposit
A time_deposit account is a fixed term deposit with an end_date. It must have a maturity of at least 7 days. This account is status = transactional.  A retail deposit shall be considered as being held in a transactional account where salaries, income or transactions are regularly credited and debited respectively against that account.
```json
{{#include time_deposit_transactional.json:5:}}
```
#### ISA time deposit
An isa_time_deposit is an individual savings account which is a scheme of investment satisfying the conditions prescribed in the UK’s ISA Regulations. This account type has an end_date which allows for future cashflow calculations to be done by Suade
```json
{{#include isa_time_deposit.json:5:}}
```
#### Retail bonds
Any account containing notes, bonds and other securities issued which are sold exclusively in the retail market and held in a retail account.
```json
{{#include retail_bonds.json:5:}}
```
#### Fees income received
A fee income record, comprising the income generated by the institution through its products and services
```json
{{#include fees_income_received.json:5:}}
```
#### Expense account
An expense account is an expense incurred by the institution during the reporting period. Example: Wages, admin charge, ppe, etc.
```json
{{#include expense_account.json:5:}}
```
#### Firm operating expenses
Normal operating expenses incurred by the reporting institution
```json
{{#include firm_operating_expenses.json:5:}}
```
#### Other expense
Other expenses incurred where the purpose differs from those already specified
```json
{{#include other_expense.json:5:}}
```
#### Recurring non-ordinary expenses
Recurring expenses incurred from outside of the reporting institution's ordinary business activities
```json
{{#include recurring_expenses_non_ordinary.json:5:}}
```
#### Unknown expenses
Expenses recorded where the purpose has not yet been determined
```json
{{#include unknown_expenses.json:5:}}
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
#### Loan with two customers
A loan example showing what the json looks like for loans with two customers
```json
{{#include loan_with_2_customers.json:5:}}
```
#### Nostro account
Nostro loans are the firm’s accounts at other financial institutions which are in effect loans to other firms where purpose is not defined
```json
{{#include nostro_account.json:5:}}
```
#### Operational nostro account
Nostro loans are the firm’s accounts at other financial institutions which are in effect loans to other firms. where purpose = operational meaning that its an operational account to meet the institution's expenses
```json
{{#include operational_nostro_account.json:5:}}
```
#### Buy to let commercial loan
Commercial loan for buy_to_let refers to a real estate loan where the borrower is purchasing the property with a view of renting it out on a commercial basis to an unrelated third party.
```json
{{#include buy_to_let_commercial_loan.json:5:}}
```
#### Buy to let commercial loan high risk
High risk commercial loan for buy_to_let refers to a real estate loan where the borrower is purchasing the property with a view of renting it out on a commercial basis to an unrelated third party. Receives 100% risk weight.
```json
{{#include buy_to_let_commercial_loan_high_risk.json:5:}}
```
#### Other commercial loan
Commercial loan others refers to a real estate loan where the current purpose enums donot fit the definition
```json
{{#include other_commercial_loan.json:5:}}
```
#### Speculative property commercial loan
Commercial loans for the purposes of the acquisition of or development or construction on land in relation to immovable property, or of and in relation to such property, with the intention of reselling for profit;
```json
{{#include speculative_property_commercial_loan.json:5:}}
```
#### Further advance commercial loan
A further advance commercial loan is a way to borrow more money from your current mortgage lender. It runs alongside your original commercial loan, often acting as a separate sub-account with its own interest rate and repayment term
```json
{{#include further_advance_commercial_loan.json:5:}}
```
#### Bridging commercial property loan
A commercial bridging loan is a short-term, secured by commercial property, used for temporary funding gap when buying or developing a business property. Borrowers typically use these loans to quickly secure a property, fund urgent refurbishments, or cover cash flow shortages while arranging permanent financing or selling another asset
```json
{{#include bridging_commercial_property_loan.json:5:}}
```
#### Remortgage commercial property loan
A commercial property remortgage is the process of replacing an existing commercial mortgage with a new loan on the same property, either with the current lender or a new one.
```json
{{#include remortgage_commercial_property_loan.json:5:}}
```
#### Other remortgage commercial property loan
A commercial property remortgage is the process of replacing an existing commercial mortgage with a new loan on the same property, either with the current lender or a new one but for a different purpose
```json
{{#include other_remortgage_commercial_property_loan.json:5:}}
```
#### Buy to let mortgage
A buy-to-let mortgage is a specialized loan for purchasing or refinancing a property intended for rental income rather than personal occupation
```json
{{#include buy_to_let_mortgage.json:5:}}
```
#### Other mortgage
Mortgage loans with purpose = other, where specific purpose is not present in FIRE
```json
{{#include other_mortgage.json:5:}}
```
#### Speculative property mortgage
Speculative property mortgage loans are financing agreements used when a borrower,often a property developer, acquires land or constructs a building without having any pre-secured buyers or tenants. The property is developed solely relying on anticipated market demand with the goal of selling or leasing it for a profit
```json
{{#include speculative_property_mortgage.json:5:}}
```
#### Remortgage
A remortgage loan is the process of paying off an existing mortgage on your property with a brand new loan
```json
{{#include remortgage.json:5:}}
```
#### First time buyer mortgage
First-time buyer mortgage loans are financial products tailored for individuals with no prior history of property ownership.
```json
{{#include first_time_buyer_mortgage.json:5:}}
```
#### House purchase mortgage
A house purchase mortgage loan is a secured loan used to buy real estate, where the property itself serves as collateral
```json
{{#include house_purchase_mortgage.json:5:}}
```
#### Other remortgage
A remortgage loan is the process of paying off an existing mortgage on your property with a brand new loan with purpose = other where a specific enum is not defined in FIRE
```json
{{#include other_remortgage.json:5:}}
```
#### Further advance mortgage
A further advance is an additional loan from your existing mortgage lender, secured against your home's equity. It acts as a separate sub-account
```json
{{#include further_advance_mortgage.json:5:}}
```
#### Construction mortgage
Construction mortgage loans are short-term loans designed to finance the building or major renovation of a property
```json
{{#include construction_mortgage.json:5:}}
```
#### Buy to let construction mortgage
Buy-to-let construction mortgages are specialized loans used by property investors to finance the building or extensive renovation of a residential property intended for rental.
```json
{{#include buy_to_let_construction_mortgage.json:5:}}
```
#### Personal buy to let loan
loans and credit facilities to individuals, who are purchasing properties with a view of renting it out for income purposes
```json
{{#include personal_buy_to_let_loan.json:5:}}
```
#### Other personal loan
loans and credit facilities to individuals, where loan purpose is not defined. (Loan purpose = other)
```json
{{#include other_personal_loan.json:5:}}
```
#### Other loan
Trading for borrowing against various positions, i.e. funding for a short position. This can be asset/liability dependant on who is faciliating the trade.
```json
{{#include other_loan.json:5:}}
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
A swap exchanging cash flows in two different currencies, providing long exposure to the underlying position.
```json
{{#include xccy_swap.json:5:}}
```
#### Commodity option
An option giving exposure to the price of an underlying commodity.
```json
{{#include commodity_option.json:5:}}
```
#### Credit default swap  - Index
A credit default swap referencing a basket or index of underlying credit entities.
```json
{{#include cds_index.json:5:}}
```
#### Credit default swap - Single name
Single name CDS; reference obligation US corporate bond with July 2028 maturity
```json
{{#include cds_single_name.json:5:}}
```
#### Equity option
An option contract whose underlying asset is an individual company's stock.
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
An FX forward to sell one currency and buy another at a predetermined exchange rate on a future date.
```json
{{#include fx_forward.json:5:}}
```
#### FX future
A futures contract to exchange one currency for another at a predetermined rate on a future date.
```json
{{#include fx_future.json:5:}}
```
#### FX option
Short USD call YEN put FX option, exercise on Match 2020
```json
{{#include fx_option.json:5:}}
```
#### FX spot
A spot FX transaction involving the sale of one currency and purchase of another.
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
A futures contract whose underlying asset or reference is an interest rate.
```json
{{#include ir_future.json:5:}}
```
#### Interest rate swap
An interest rate swap where the position pays the fixed interest rate and receives the floating rate.
```json
{{#include interest_rate_swap.json:5:}}
```
#### Interest rate swap amortising
An interest rate swap with notional amount that decreases over the life of the contract.
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
{{#include usd_payer_swaption.json:5:}}
```
#### Unmargined netting agreement
Unmargined netting agreement, collateralised with initial collateral amount
```json
{{#include unmargined_netting_agreement.json:5:}}
```
#### Commodity asian option
A commodity option whose payoff is based on an average underlying commodity price over a specified period.
```json
{{#include commodity_asian_option.json:5:}}
```
#### Single stock forward
A forward contract to buy or sell a specific individual stock at a predetermined price on a future date.
```json
{{#include single_stock_forward.json:5:}}
```
#### Single stock forward in stocks
A forward contract on a specific individual stock, with the underlying quantity specified in shares.
```json
{{#include single_stock_forward_in_stocks.json:5:}}
```
#### Commodity forward
A forward contract to buy or sell a commodity at a predetermined price on a future date.
```json
{{#include commodity_forward.json:5:}}
```
#### Commodity forward in units
A commodity forward with the underlying quantity specified in physical units.
```json
{{#include commodity_forward_in_units.json:5:}}
```
#### Interest rate swap forward starting
An interest rate swap agreed today that begins on a future date.
```json
{{#include interest_rate_swap_forward_starting.json:5:}}
```
#### Overnight index swap
An overnight index swap involving a fixed interest rate leg.
```json
{{#include overnight_index_swap.json:5:}}
```
#### Interest rate basis swap
An interest rate swap exchanging two different floating interest rates.
```json
{{#include interest_rate_basis_swap.json:5:}}
```
#### Cancellable swap
An interest rate swap containing an option allowing the contract to be cancelled before maturity.
```json
{{#include cancellable_swap.json:5:}}
```
#### Inflation linked swap
A swap with cash flows linked to an inflation index.
```json
{{#include inflation_linked_swap.json:5:}}
```
#### Commodity swap
A swap providing exposure to the price of an underlying commodity.
```json
{{#include commodity_swap.json:5:}}
```
#### Equity index option
An option contract whose underlying asset is an equity index.
```json
{{#include equity_index_option.json:5:}}
```
#### FX barrier option
A short call option on an FX rate with a specified barrier level that can activate or terminate the option.
```json
{{#include fx_barrier_option.json:5:}}
```
#### FX ndf
A short non-deliverable FX forward settled using the difference between the contracted and prevailing exchange rates.
```json
{{#include fx_ndf.json:5:}}
```
#### FX ndf forward starting
A forward-starting non-deliverable FX forward that begins at a future date, with a short position.
```json
{{#include fx_ndf_forward_starting.json:5:}}
```
#### IR overnight index future
A futures contract referencing an overnight interest rate index.
```json
{{#include ir_overnight_index_future.json:5:}}
```
#### BTP future
A futures contract referencing Italian government bonds (BTPs).
```json
{{#include btp_future.json:5:}}
```
#### Equity index future
A futures contract whose underlying asset is an equity index.
```json
{{#include equity_index_future.json:5:}}
```
#### Equity single name future
A futures contract whose underlying asset is an individual company's stock.
```json
{{#include equity_single_name_future.json:5:}}
```
#### Commodity future
A futures contract whose underlying asset is a commodity.
```json
{{#include commodity_future.json:5:}}
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
#### Firm capital
Capital Resources - Tier 1
```json
{{#include firm_capital.json:5:}}
```
#### ABS sts securitisation
Sts Securitisations Eligible For Preferential Capital Treatment , Traditional Or Synthetic Securitisations
```json
{{#include abs_sts_securitisation.json:5:}}
```
#### ABS traditional subordinated
‘Traditional Securitisation’: Involves The Transfer Of The Economic Interest In The Exposures Being Securitised Through The Transfer Of Ownership
```json
{{#include abs_traditional_subordinated.json:5:}}
```
#### ABS traditional senior
‘Traditional Securitisation’: Involves The Transfer Of The Economic Interest In The Exposures Being Securitised Through The Transfer Of Ownership
```json
{{#include abs_traditional_senior.json:5:}}
```
#### Share
Equity Shares Held By The Firm
```json
{{#include share.json:5:}}
```
#### Share hqla level 2b
Common Equity Shares Held By The Firm That Are Hqla Eligible
```json
{{#include share_hqla_level_2b.json:5:}}
```
#### Covered bond
Debt Instruments Issued By Credit Institutions And Secured By A Cover Pool Of Assets Which Typically Consist Of Mortgage Loans Or Public Sector Debt
```json
{{#include covered_bond.json:5:}}
```
#### Regional government bond
Debt Instruments Issued By A Regional Government
```json
{{#include regional_government_bond.json:5:}}
```
#### Guaranteed corporate bond
Guaranteed Debt Instruments Issued By A Corporate
```json
{{#include guaranteed_corporate_bond.json:5:}}
```
#### Corporate bond
Debt Instruments Issued By A Corporate
```json
{{#include corporate_bond.json:5:}}
```
#### Debt security issued liability
A Securities Issuance Of Stocks Or Bonds (Determined By The Security - Type)
```json
{{#include debt_security_issued_liability.json:5:}}
```
#### Debt security issued capital
A Securities Issuance Of Stocks Or Bonds (Determined By The Security - Type)
```json
{{#include debt_security_issued_capital.json:5:}}
```
#### Medium term note issued
Debt Instrument Issued By A Company, Typically With Maturities Ranging From One To Ten Years
```json
{{#include medium_term_note_issued.json:5:}}
```
#### Bankruptcy remote bond
A Debt Instrument That Will Not Be Available To An Entity’S Creditors In The Event Of The Insolvency Of That Entity
```json
{{#include bankruptcy_remote_bond.json:5:}}
```
#### Rev repo bond
An Agreement In Which One Party Purchases Securities Or Commodities And Commits To Resell Equivalent Assets To The Original Seller At A Specified Future Date And Price.
```json
{{#include rev_repo_bond.json:5:}}
```
#### Repo liability
An Agreement In Which One Party Purchases Securities Or Commodities And Commits To Resell Equivalent Assets To The Original Seller At A Specified Future Date And Price.
```json
{{#include repo_liability.json:5:}}
```
#### Repo asset
An Agreement In Which One Party Purchases Securities Or Commodities And Commits To Resell Equivalent Assets To The Original Seller At A Specified Future Date And Price.
```json
{{#include repo_asset.json:5:}}
```
#### Term funding scheme
An Agreement In Which One Party Purchases Securities Or Commodities And Commits To Resell Equivalent Assets To The Original Seller At A Specified Future Date And Price.
```json
{{#include term_funding_scheme.json:5:}}
```
#### Unsettled repo
This trade represents a repurchase agreement which is pending settlement
```json
{{#include unsettled_repo.json:5:}}
```
#### Central bank required reserves
Reserves held by the credit institution in a central bank
```json
{{#include central_bank_required_reserves.json:5:}}
```
#### Bank of england levy
The Bank of England levy, which replaced the former Cash Ratio Deposit Scheme, is a levy which covers the BoE's operational costs
```json
{{#include bank_of_england_levy.json:5:}}
```
#### Certificate of deposit
A certificate of deposit is also a promissory note, however can only be issued by a bank. It has a fixed maturity and specified fixed interest rate.
```json
{{#include certificate_of_deposit.json:5:}}
```
