---
layout:		property
title:		"purpose"
schemas:	[account, loan, security, derivative, derivative_cash_flow]
---

# purpose

---

The **purpose** property describes the reason behind the creation or usage of the financial product or account *as seen from the point of view of the firm*.

## Account
```bash
├── admin
├── cf_hedge
├── ci_service
├── collateral
├── commitments
├── critical_service
├── dealing_revenue
│   ├── dealing_rev_fx
│   │   └── dealing_rev_fx_nse
│   ├── dealing_rev_sec
│   │   └── dealing_rev_sec_nse
│   └── dealing_rev_deriv
│       └── dealing_rev_deriv_nse
├── deposit
├── dgs_contribution
├── dividend
│   └── div_from_cis
│   │   └── div_from_money_mkt
│   └── manufactured_dividend
├── donation
├── employee
├── fees
│   ├── credit_card_fee
│   ├── current_account_fee
│   │   └── overdraft_fee
│   ├── derivative_fee
│   ├── insurance_fee
│   ├── investment_banking_fee
│   ├── loan_and_advance_fee
│   │   ├── mortgage_fee
│   │   └── unsecured_loan_fee
│   ├── other_fs_fee
│   └── other_non_fs_fee
├── fines
├── firm_operating_expenses
│   ├── computer_and_it_cost
│   ├── non_life_ins_premium
│   ├── occupancy_cost
│   ├── other_expenditure
│   ├── rent
│   └── staff
│       ├── annual_bonus_accruals
│       ├── benefit_in_kind
│       ├── employee_stock_option
│       ├── ni_contribution
│       ├── other_social_contrib
│       ├── other_staff_cost
│       ├── other_staff_rem
│       ├── pension
│       ├── redundancy_pymt
│       └── regular_wages
├── fx
├── interest
│   ├── int_on_bond_and_frn
│   ├── int_on_deposit
│   ├── int_on_derivative
│   │   └── int_on_deriv_hedge
│   ├── int_on_loan_and_adv
│   │   ├── int_on_bridging_finance
│   │   ├── int_on_mortgage
│   │   ├── int_on_credit_card
│   │   └── int_on_ecgd_lending
│   ├── int_on_money_mkt
│   └── int_on_sft
├── intra_group_fee
├── inv_in_subsidiary
├── operational
│   ├── cash_management
│   ├── clearing
│   ├── custody
│   ├── ips
│   ├── operational_excess
│   └── operational_escrow
├── other
├── prime_brokerage
├── ppe
├── goodwill
├── property
│   ├── investment_property
│   └── own_property
├── recovery
├── reference
├── release
├── reg_loss
├── restructuring
├── res_fund_contribution
├── revaluation
├── revenue_reserve
├── share_plan
├── share_premium
├── system
├── tax
│   ├── capital_gain_tax
│   └── corporation_tax
└── write_off
```

### dgs_contribution
Describes an account representing the **contributions to deposit guarantee schemes** paid by the reporting entity as defined by Annex 5 Part 2.48i of the [ITS on supervisory reporting][its]

### res_fund_contribution
Describes an account representing the **contributions to resolution funds** paid by the reporting entity as defined by Annex 5 Part 2.48i of the [ITS on supervisory reporting][its]

### deposit
The **deposit** enum value refers to a retail deposit defined in accordance with Article 411 of the [CRR][crr]:

> A liability to a natural person or to an SME, where the natural person or the SME would qualify for the retail exposure class under the Standardised or IRB approaches for credit risk, or a liability to a company which is eligible for the treatment set out in Article 153(4) and where the aggregate deposits by all such enterprises on a group basis do not exceed EUR 1 million.

### ci_service
The **ci_service** enum value refers to accounts covered by central institution services or held within a cooperative network.

Opening paragraph 12 of the [LCR][lcr] states that liquidity calculations should take into account:
> centralised management of liquidity in cooperative and institutional protection scheme networks where the central institution or body plays a role akin to a central bank because the members of the network do not typically have direct access to the latter.
> Appropriate rules should, therefore, recognise as liquid assets the sight deposits which are made by the members of the network with the central institution and other liquidity funding available to those from the central institution.

Assets placed as a **ci_service** should be considered unencumbered inaccordance with Artcle 7.2(a) of the [LCR][lcr]:
> assets included in a pool which are available for immediate use as collateral to obtain additional funding under committed but not yet funded credit lines available to the credit institution. This shall include assets placed by a credit institution with the central institution in a cooperative network or institutional protection scheme.

### collateral
The **collateral** enum type identifies an account or deposit received as collateral and hence, not classified as a liability for the purposes of Article 27 and 29 of the [LCR][lcr]. Collateral held in an account should have a corresponding [**id**][id] in the collateral schema

### ips
Within the context of **operational** deposits as defined in Artcle 27.1(d) of the [LCR][lcr], the **ips** enum indicates that the account is maintained by the depositor to obtain cash clearing and central institution services and where the deposit taking institution belongs to an  institutional protection scheme or equivalent network as referred in Article 16 of the [LCR][lcr].

### escrow
*needs definition*

### operational_escrow
*needs definition*

### clearing
The **clearing** enum value indicates that the account or deposit is being maintained for clearing, settlement, custody or cash management services in the context of an **operational** relationship and hence can be treated as a very short term exposure.

Clearing and comparable services from the [CRR][crr] Article 422.4:
> Clearing, custody or cash management or other comparable services referred to in points (a) and (d) of paragraph 3 only covers such services to the extent that they are rendered in the context of an established relationship on which the depositor has substantial dependency. They shall not merely consist in correspondent banking or prime brokerage services and the institution shall have evidence that the client is unable to withdraw amounts legally due over a 30 day horizon without compromising its operational functioning.

### operational
Operational deposit from the [LCR][lcr] Article 27.6:
> 6. In order to identify the deposits referred to in point (c) of paragraph 1, a credit institution shall consider that there is an established operational relationship with a non-financial customer, excluding term deposits, savings deposits and brokered deposits, where all of the following criteria are met:
> (a) the remuneration of the account is priced at least 5 basis points below the prevailing rate for wholesale deposits with comparable characteristics, but need not be negative;
> (b) the deposit is held in specifically designated accounts and priced without creating economic incentives for the depositor to maintain funds in the deposit in excess of what is needed for the operational relationship;
> (c) material transactions are credited and debited on a frequent basis on the account considered;
> (d) one of the following criteria is met:
> (i) the relationship with the depositor has existed for at least 24 months;
> (ii) the deposit is used for a minimum of 2 active services. These services may include direct or indirect access to national or international payment services, security trading or depository services.
> Only that part of the deposit which is necessary to make use of the service of which the deposit is a by-product shall be treated as an operational deposit. The excess shall be treated as non-operational.
Where the depositor is the reporting entity, the loan schema should be used. Where the depositor is the other party, the account schema should be used.

### operational_excess
Excess operational deposits are defined as the part of the operational deposits (as defined in [LCR][lcr] Article 27.6) held in excess of those required for the provision of operational services. The distinction between operational deposits and excess operational deposits is required for the reporting of section 1.1.3 in the ouflows section of the [LCR][lcr]

### custody
As opposed to short-term definition within **operational**, **custody** here refers to the long-term custody of financial assets such as those held for safekeeping by a custodian bank.

### prime_brokerage
Describes an account held for prime brokerage reasons but not including those contained above for operational reasons. These accounts are used for prime brokerage service transactions which are in essence investment activities including securities lending, leveraged trade executions and cash management, among other things.

### investment_property
IAS 40.5 defines **investment property** as:
> property (land or a building - or part of a building - or both) held (by the owner or by the lessee as a right-of-use asset) to earn rentals or for capital appreciation or both, rather than for:
(a) use in the production or supply of goods or services or for administrative purposes; or
(b) sale in the ordinary course of business.

### own_property
IAS 40.5 defines **owner occupied property** as:
> property held (by the owner or by the lessee as a right-of-use asset) for use in the production or supply of goods or services or for administrative purposes.

For example, for the reporting of Notice MAS 610/1003, **owner occupied property** includes bank premises.

### property
This refers to other **immovable property** not included in investment property or owner occupied property,

### revenue_reserve
A type of reserve account. This is created when an entity retains an amount of its distributable profit.

### share_plan
This is a reserve account where funds are held with the purpose of share plans and other equity based compensation.

### share_premium
This is a reserve account whose funds can only be used for purposes provided in the corporate bylaws, such as for share issue costs or issuance of bonus shares, but cannot be used for dividends.

### reg_loss
This is a reserve that is created when an entity allocates funds to a reserve account for the purpose of complying with requirements for minimum **regulatory loss allowances**.

For example, [MAS Notice 612][MAS612] (section 6.3.7) requires locally incorporated domestic systemically important banks to maintain a minimum level of loss allowance equivalent to 1% of the gross carrying amount of selected credit exposures net of collateral. This is referred to as the Minimum Regulatory Loss Allowance. Where the entity's Accounting Loss Allowance (calculated in accordance with the impairment requirements under FRS 109) falls below the Minimum Regulatory Loss Allowance, the entity shall maintain the difference in a non-distributable regulatory loss allowance reserve which shall be appropriated from retained earnings.

[MAS612]: https://www.mas.gov.sg/regulation/notices/notice-612

### cf_hedge
IFRS 9.6.5.2 defines a **cash flow hedge** as follows:
 > a hedge of the exposure to variability in cash flows that is attributable to a particular risk associated with all, or a component of, a  recognised asset or liability (such as all or some future interest payments on variable-rate debt) or a highly probable forecast transaction, and could affect profit or loss.

IFRS 9 refers to the **cash flow hedge reserve** as the separate equity component associated with the hedged item. In hedge accounting under IFRS, this account is a key component of the recognition of a hedging relationship.

For example, in the EBA's FINREP F.1.3 report, the effective portion of the variation in fair value of hedging derivatives in a cash flow hedge, both for ongoing cash flow hedges and cash flow hedges that no longer apply, is reported as the **cash flow hedge reserve**.

### fees
Describes an account that holds the amount of fee/commission receivables/payables as reported in a Profit and Loss report.

### credit_card_fee
Describes an account that holds the amount of fees receivables originating from **credit cards**.

### current_account_fee
Describes an account that holds the amount of fees receivables/payables originating from **current accounts**.

### derivative_fee
Describes an account that holds the amount of fees receivables/payables originating from **overdraft accounts**.

### mortgage_fee
Describes an account that holds the amount of fees receivables originating from **mortgage products**.

### overdraft_fee
Describes an account that holds the amount of fees receivables originating from **overdraft accounts**.

### unsecured_loan_fee
Describes an account that holds the amount of fees receivables originating from **unsecured personal loans**.

### insurance_fee
Describes an account that holds the amount of fees receivables originating from **insurance** activities.

### investment_banking_fee
Describes an account that holds the amount of fees receivables/payables originating from **investment banking** activities. This includes advisory, brokerage and underwriting activities.

### other_fs_fee
Describes an account that holds the amount of fees receivables/payables originating from **financial services** and that do not fall under any of the other categories of fees. These could include fees receivable for guarantees payable under break clauses, fees for administering loans on behalf of other lenders.

### other_non_fs_fee
Describes an account that holds the amount of fees receivables/payables originating from **services that cannot be classified as financial**. These could include executor and trustee services, computer bureau services.

### pension
*needs definition*

### restructuring
*needs definition*

### commitments
*needs definition*

### tax
Describes an account representing the amount of tax paid, received or deferred for the reporting period by the reporting entity.

### capital_gain_tax
Describes an account representing the amount of **capital gain tax** paid, received or deferred for the reporting period by the reporting entity.

### corporation_tax
Describes an account representing the amount of **corporation tax** paid, received or deferred for the reporting period by the reporting entity.

### dealing_revenue
Describes an account that holds the amount of profits or losses arising from the purchase, sale and holdings of tradable instruments.

### dealing_rev_fx
Describes an account that holds the amount of profits or losses arising from the purchase, sale and holdings of **fx instruments**.

### dealing_rev_sec
Describes an account that holds the amount of profits or losses arising from the purchase, sale and holdings of **securities**.

### dealing_rev_deriv
Describes an account that holds the amount of profits or losses arising from the purchase, sale and holdings of **derivative instruments**.

### dealing_rev_fx_nse
Describes an account that holds the Net Spread Earnings (NSE) amount arising from the purchase and sale of **fx instruments**. The NSE is indentified as the difference between the price paid/offered by the reporting entity and the price available in the open market (mid-market price) at the time of the transaction.

### dealing_rev_sec_nse
Describes an account that holds the Net Spread Earnings (NSE) amount arising from the purchase and sale of **securities**. The NSE is indentified as the difference between the price paid/offered by the reporting entity and the price available in the open market (mid-market price) at the time of the transaction.

### dealing_rev_deriv_nse
Describes an account that holds the Net Spread Earnings (NSE) amount arising from the purchase and sale of **derivative instruments**. The NSE is indentified as the difference between the price paid/offered by the reporting entity and the price available in the open market (mid-market price) at the time of the transaction.

### dividend
Describes an account that holds the amount of dividends paid or received as reported in a Profit and Loss report.

### dividend_from_cis
Describes an account that holds the amount of dividends received from **collective investment schemes**.

### dividend_from_money_mkt
Describes an account that holds the amount of dividends received from **money market funds**.

### interest
Describes an account that holds the amount of interests receivable/payable as reported in a Profit and Loss report

### int_on_money_mkt
Describes an account that holds the amount of interests receivable/payable as reported in a Profit and Loss report and where the interest amount originates from **money market instruments**.

### int_on_deriv
Describes an account that holds the amount of interests receivable/payable as reported in a Profit and Loss report and where the interest amount originates from **derivative instruments**.

### int_on_deriv_hedge
Describes an account that holds the amount of interests receivable/payable as reported in a Profit and Loss report and where the interest amount originates from **derivative instruments** used as hedging instruments and where the hedged items generate interest.

### int_on_loan_and_adv
Describes an account that holds the amount of interests receivable/payable as reported in a Profit and Loss report and where the interest amount originates from **loans and advances**.

### int_on_ecgd_lending
Describes an account that holds the amount of interests receivable/payable where the interest amount originates from **loans** guaranteed by the Export Credits Guarantee Department (ECGD) also known as UK Export Finance.

### int_on_deposit
Describes an account that holds the amount of interests receivable/payable as reported in a Profit and Loss report and where the interest amount originates from **deposits**.

### int_on_sft
Describes an account that holds the amount of interests receivable/payable as reported in a Profit and Loss report and where the interest amount originates from **Securities Financing Transactions**.

### int_on_bond_and_frn
Describes an account that holds the amount of interests receivable/payable as reported in a Profit and Loss report and where the interest amount originates from **bonds and Floating Rate Notes**.

### int_on_bridging_loan
Describes an account that holds the amount of interests receivable/payable as reported in a Profit and Loss report and where the interest amount originates from **bridging finance loans**.

### int_on_mortgage
Describes an account that holds the amount of interests receivable/payable as reported in a Profit and Loss report and where the interest amount originates from **loans secured on dwellings**.

### int_on_credit_card
Describes an account that holds the amount of interests receivable/payable as reported in a Profit and Loss report and where the interest amount originates from **credit card lending**.

### intra_group_fee
Describes an account that holds the amount of:
    - Intra-group fees receivable and payable where the counterparty is an intra-group entity. Or;
    - Cost recharges that are costs of a centrally managed service allocated
    and charged to each group entity (e.g. IT support).

### fx
*needs definition*

### admin
*needs definition*

### staff
*needs definition*

### goodwill
**Goodwill** is a type of intangible asset. IFRS3, Appendix A, defines **goodwill** as:
> an asset representing the future economic benefits arising from other assets acquired in a business combination that are not individually identified and separately recognised.

### ppe
IAS 16(6) defines **property plant and equipment** as:
> tangible items that:
(a) are held for use in the production or supply of goods or services, for rental to others, or for administrative purposes; and
(b) are expected to be used during more than one period.

### other
The **other** enum value can be used when it is known that none of the other enum values apply.

### rent
Describes an account representing the amount of **rent** to be paid or received by the reporting entity.

### annual_bonus_accruals
Describes an account representing the part of staff expenses corresponding to the **annual_bonus_accruals** paid by the reporting entity.

### computer_and_it_costs
Describes an account representing the part of operating expenses corresponding to the **computer_and_it_costs** paid by the reporting entity.

### benefit_in_kind
Describes an account representing the part of staff expenses corresponding to the **benefits_in_kind** paid by the reporting entity.
Bank Of England defines **benefits_in_kind** as items where the cost is separately identifiable and would normally fall within expenditure, such as staff canteens, luncheon vouchers, sports club membership, nurseries, health care and staff savings schemes that do not form part of employee stock options
BoE Form PL definitions: https://www.bankofengland.co.uk/statistics/data-collection/osca/forms-definitions-validations

### employee_stock_options
Describes an account representing the part of staff expenses corresponding to the **employee_stock_options** paid by the reporting entity.

### ni_contributions
Describes an account representing the part of staff expenses corresponding to the **national_insurance_contributions** paid by the reporting entity.

### non_life_ins_premium
Describes an account representing the part of operating expenses corresponding to the **non_life_insurance_premiums** paid by the reporting entity.
Bank Of England defines **non_life_insurance_premiums** as premiums payable to provide cover against various events or accidents resulting in damage to goods or property, or harm to persons as a result of natural or human causes (fires,floods, crashes, collisions, sinkings, theft, violence, accidents, sickness, etc.) or against financial losses resulting from events such as sickness, unemployment, accidents, etc.
BoE Form PL definitions: https://www.bankofengland.co.uk/statistics/data-collection/osca/forms-definitions-validations

### occupancy_cost
Describes an account representing the part of operating expenses corresponding to the **occupancy_costs** paid by the reporting entity. As per the Bank of England definition, this would inlcude costs relating to land and other buildings, such as rent, non-domestic rates and energy costs. It would also include any costs relating to moving or vacating buildings.
BoE Form PL definitions: https://www.bankofengland.co.uk/statistics/data-collection/osca/forms-definitions-validations

### other_expenditure
Describes an account representing the part of operating expenses that would not fall in any of the other available categories for operating expenses.

### other_social_contrib
Describes an account representing the part of staff expenses corresponding to social contributions not included in any of the other available categories for staff expenses.

### other_staff_rem
Describes an account representing the part of staff expenses corresponding to staff remuneration not included in any of the other available categories for staff expenses.

### other_staff_cost
Describes an account representing the part of staff expenses corresponding to staff costs not included in any of the other available categories for staff expenses.

### redundancy_pymt
Describes an account representing the part of staff expenses corresponding to redundancy and severance payments made by the reporting entity.

### regular_wages
Describes an account representing the part of staff expenses corresponding to regular compensation payable to all employees. As per the Bank Of England definition this includes overtime payments, commissions and any other cash benefit payments. It Also includes any one-off bonuses that relate to a specific piece of work or performance in the current period. One-off bonuses could include any other non-regular bonus or cash remuneration paid to employees that is not part of the annual bonus accrual.
BoE Form PL definitions: https://www.bankofengland.co.uk/statistics/data-collection/osca/forms-definitions-validations

### fine
Describes an account representing the amount of fines or compensation payments paid or provisioned by the reporting entity.

### donation
Describes an account representing the amount of voluntary contributions made to non-profit institutions.

### inv_in_subsidiary
Describes an account representing the profit or loss made on investments in subsidiaries, associates and special purpose entities.

### manufactured_dividend
Describes an account representing the manufactured dividends paid or received by the reporting entity.
The Bank of England defines manufactured dividends as payments that can arise when an institution borrows a security from a security lender or client and that security pays a dividend while on loan. As the security lender customarily maintains the right to payments which accrue on the security, the borrower will ‘manufacture’ a dividend payment back to the lender.
BoE Form PL definitions: https://www.bankofengland.co.uk/statistics/data-collection/osca/forms-definitions-validations

### revaluation
Describes an account representing the revaluation made to reserves or provisions.

### recovery
Describes an account representing the amount recovered made to reserves or provisions.

### release
Describes an account representing the amount of a provision beeing released as a risk subsides (e.g. the loan for which the provision was originally registered is repaid).

### write_off
Describes an account representing the amount of a provision beeing written-off as a risk materialised (e.g. the loan for which the provision was originally registered is deemed irrecoverable).

## Derivative
```bash
├── reference
├── client_order_execution
├── client_order_transmission
├── cva_hedge
└── back_to_back
```
### reference
Use this enumeration value to refer to derivatives which are underlyings of other derivative positions (e.g. swaptions).
In the context of [CRR][crr] Article 329, a reference derivative would be the underlying swap of a swaption.

### client orders handled 
client order execution vs client order transmission:
‘client orders handled’ or ‘COH’ means the value of orders that an investment firm handles for clients, through the
reception and transmission of client orders and through the execution of orders on behalf of clients; [IFR] Article 4

### cva_hedge
Use this enumeration value to refer to derivatives booked in order to hedge CVA as defined in [CRR][crr] Article 386.

### back_to_back
Use this enumeration value to highlight back to back trades defined as "exactly matching" in [Pruval Delegated Regulation][pruval] Article 4 (2)

## Derivative Cash Flow
```bash
├── reference
├── principal
└── interest
```
### reference
Use this enumeration value to refer to derivative cash flows which are calculated in order to decompose derivatives in combinations of long and short flows. See [CRR][crr] Articles 328 to 331.

### principal
Use this enumeration value when derivative cashflows data are uploaded as two
distinct batches, one for principal and one for interest cashflows.
For rows uploaded as "principal", the values populated in the "balance" column
refer to principal cashflows (accreting and/or amortising) only, and do not
include any interest flows


### interest
Use this enumeration value when derivative cashflows data are uploaded as two
distinct batches, one for principal and one for interest cashflows.
For rows uploaded as "interest", the values populated in the "balance" column
refer to interest cashflows only, and do not include any principal flows

## Loan
```bash
├── house_purchase
├── first_time_buyer
├── bridging_loan
├── buy_to_let
│   ├── buy_to_let_house_purchase
│   ├── buy_to_let_remortgage
│   ├── buy_to_let_further_advance
│   └── buy_to_let_other
├── ips
├── lifetime_mortgage
├── operational
├── promotional
├── remortgage
├── remortgage_other
├── speculative_property
├── consumer_buy_to_let
├── further_advance
├── agriculture
├── construction
├── project_finance
└── other
```
### house_purchase
>The **house_purchase** value indicates that the purpose of the loan is for the purchase of residential property for occupation by the borrower.

### first_time_buyer
>The **first_time_buyer** value is a term used in the British and Irish property markets and defined in the Bank of England's [Mortgage Lending & Administration (MLAR) Definitions][mlardef] section E6.1/2 It is a sub-category of a **house_purchase** where "the tenure of the main borrower immediately before this advance was not owner-occupier."

### bridging_loan
>A **bridging_loan** is a short-term financing option used typically used for property owners to finance the period between buying a new property and selling an old one when the timing of the two does not match. It can also be used by property developers or investors who value speed over cost.

### buy_to_let
>The **buy_to_let** value is a term used in the British property market where the borrower is purchasing the property with a view of renting it out on a commercial basis to an *unrelated third party*. See [MLAR Definitions][mlardef] section E6.2.

### internal_hedge
>From [CRR][crr] definitions (96):
> internal hedge means a position that materially offsets the component risk elements between a trading book and a non-trading book position or sets of positions;

### ips
From [CRR][crr] Article 113(7):
> An **institutional protection scheme** is a contractual or statutory liability arrangement which protects those institutions and in particular ensures their liquidty and solvency where necessary;

### lifetime_mortgage
>A **lifetime_mortgage** is a very specific kind of British mortgage contract and is defined in the [FCA Handbook](https://www.handbook.fca.org.uk/handbook/glossary/G1294.html). It is geared towards customers of a certain age in order to release equity and typically repayment occurs at the time of the customers death when the property is sold;

### operational 
*(see operational under account)*

### promotional
As outlined in [LCR][lcr] Article 31(9), a **promotional loan**
> shall be available only to persons who are not financial customers on a non-competitive, not for profit basis in order to promote public policy objectives of the Union or that Member State's central or regional government. It shall only be possible to draw on such facilities following the reasonably expected demand for a promotional loan and up to the amount of such demand provided there is a subsequent reporting on the use of the funds distributed;

### remortgage
>The **remortgage** value indicates a re-mortgage or refinancing of an existing property by an existing customer of the firm who had a loan with a **house_purchase** purpose. Note that this does not include re-mortgages of **first_time_buyer** and **buy_to_let** loans which should retain their respective purposes in the event of a re-mortgage. See [MLAR Definitions][mlardef] section E6.4/5.

### speculative_property
From [CRR][crr] definitions (79):
> speculative immovable property financing‧ means loans for the purposes of the acquisition of or development or construction on land in relation to immovable property, or of and in relation to such property, with the intention of reselling for profit;

### remortgage_other
>The **remortgage_other** value indicates a re-mortgage by a new customer who is refinancing a loan from another lender.

### agriculture
Loans given for the purpose of financing agriculture development or production.
FFEIC definition:
> loans to finance agricultural production and other loans to farmers:
(1) Loans and advances made for the purpose of financing agricultural production, including
the growing and storing of crops, the marketing or carrying of agricultural products by the
growers thereof, and the breeding, raising, fattening, or marketing of livestock.
(2) Loans and advances made for the purpose of financing fisheries and forestries, including
loans to commercial fishermen.
(3) Agricultural notes and other notes of farmers that the bank has discounted for, or
purchased from, merchants and dealers, either with or without recourse to the seller.
(4) Loans to farmers that are guaranteed by the Farmers Home Administration (FmHA) or by
the Small Business Administration (SBA) and that are extended, serviced, and collected
by a party other than the FmHA or SBA. Include SBA “Guaranteed Interest Certificates,”
which represent a beneficial interest in the entire SBA-guaranteed portion of an individual
loan, provided the loan is for the financing of agricultural production or other lending to
farmers. (Exclude SBA “Guaranteed Loan Pool Certificates,” which represent an
undivided interest in a pool of SBA-guaranteed portions of loans. SBA “Guaranteed Loan
Pool Certificates” should be reported as securities in Schedule RC-B, item 2, or, if held
for trading, in Schedule RC, item 5.)
(5) Loans and advances to farmers for purchases of farm machinery, equipment, and
implements.
(6) Loans and advances to farmers for all other purposes associated with the maintenance or
operations of the farm, including purchases of private passenger automobiles and other
retail consumer goods and provisions for the living expenses of farmers or ranchers and
their families.

### construction
Loans given for the purpose of construction, development or re-development of a site.
FFEIC definition:
> loans secured by real estate made to finance (a) land development (i.e., the process of improving land – laying sewers, water pipes, etc.) preparatory to erecting new structures or (b) the on-site construction of industrial, commercial, residential, or farm buildings.

### project_finance
As defined in [Supervisory Reporting][sup-rep] part 2(5)(41)(l):
> 'Project finance loans' include loans that are recovered solely from the income of the projects financed by them.

### other
The **other** enum value can be used when none of the other enum values apply or the value is *unknown*.

## Security
```bash
├── collateral
│    ├──  derivative_collateral
│    ├──  independent_collateral_amount
│    ├──  custody
│    └──  default_fund
├── reference
├── share_capital
│    └──  non_controlling
├── investment
│    ├──  investment_advice
│    └──  portfolio_management
├── trade_finance
├── aircraft_finance
├── insurance
├── back_to_back
└── other
```
### investment_advice
The [Mifid Directive][midifdir] defines in Article 4(4) investment advice as:
> provision of personal recommendations to a client, either upon its request or at the initiative of the investment firm, in respect of one or more transactions relating to financial instruments.
### portfolio_management
The [Mifid Directive][midifdir] defines in Article 4(8) portfolio management as:
> managing portfolios in accordance with mandates given by clients on a discretionary client-by-client basis where such portfolios include one or more financial instruments.
### trade_finance
From [CRR][crr] definitions (80):
> **Trade finance** means financing, including guarantees, connected to the exchange of goods and services through financial products of fixed short-term maturity, generally of less than one year, without automatic rollover;

### derivative_collateral
Defined in accordance with Article 30(1) of the [LCR][lcr] regulation:
> "collateral posted for contracts listed in [Annex II of Regulation (EU) No. 575/2013](http://eur-lex.europa.eu/legal-content/en/TXT/?uri=celex%3A32013R0575) and credit derivatives".

### independent_collateral_amount (ICA)
Defined in accordance with [SA-CCR][bis_sa_ccr].
> ICA represents (i) collateral (other than VM) posted by the counterparty that the bank may seize upon default of the counterparty, the amount of which does not change in response to the value of the transaction it secures and/or (ii) the Independent Amount (IA) parameter as defined in standard industry documentation.

### default_fund
Defined in accordance with [[CRR]], A CCP's default fund is a mechanism that allows the sharing (mutualisation) of losses among the CCP's clearing members.
default fund' means a fund established by a CCP in accordance with Article 42 of Regulation (EU) No 648/2012 and used in accordance with Article 45 of that Regulation

### reference
Use this enumeration value to refer to securities which are underlyings of derivative positions (e.g. bond futures).
In the context of [CRR][crr] Article 328, a reference security would be the underlying bond of a bond future position.

### share_capital
This indicates shares that have been [issued][issued] for the purpose of raising capital for the company.

[issued]: https://www.investopedia.com/terms/s/sharecapital.asp

### non_controlling
[Commission Regulation (EC) No 494/2009][reg] defines **non-controlling interest** as:
> the equity in a subsidiary not attributable, directly or indirectly, to a parent.

### back_to_back
Use this enumeration value to highlight back to back trades defined as "exactly matching" in [Pruval Delegated Regulation][pruval] Article 4 (2)

---

[reg]: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32009R0494&from=EN
[midifdir]: https://eur-lex.europa.eu/legal-content/en/TXT/?uri=CELEX:32014L0065
[crr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013R0575
[lcr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0061
[id]: https://github.com/suadelabs/fire/blob/master/documentation/properties/id.md
[mlardef]: http://www.bankofengland.co.uk/pra/documents/regulatorydata/mlar/sup_chapter16_annex19bg_20120401.pdf
[pruval]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:JOL_2016_021_R_0005
[bis_sa_ccr]: https://www.bis.org/publ/bcbs279.pdf
[its]: https://www.eba.europa.eu/sites/default/documents/files/document_library/Risk%20Analysis%20and%20Data/Reporting%20Frameworks/Reporting%20framework%203.0/3.0%20phase%202/972659/ITS%20on%20supervisory%20reporting%20-%20corrigendum.zip
