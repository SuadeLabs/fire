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
├── adj_syn_inv_own_shares
├── adj_syn_inv_decon_subs
├── adj_syn_other_inv_fin
├── adj_syn_nonsig_inv_fin
├── adj_syn_mtg_def_ins
├── admin
├── capital_reserve
├── cf_hedge
│ └── cf_hedge_reclass
├── ci_service
├── collateral
├── commitments
├── critical_service
├── dealing_revenue
│   ├── dealing_rev_fx
│   │   └── dealing_rev_fx_nse
│   ├── dealing_rev_sec
│   │   └── dealing_rev_sec_nse
│   ├── dealing_rev_ir
│   └── dealing_rev_deriv
│       └── dealing_rev_deriv_nse
├── defined_benefit
├── deposit
│   └── third_party_interest
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
│   │   └── underwriting_fee
│   ├── loan_and_advance_fee
│   │   ├── mortgage_fee
│   │   └── unsecured_loan_fee
│   ├── other_fs_fee
│   └── other_non_fs_fee
├── fines
├── firm_operating_expenses
│   ├── computer_and_it_cost
│   ├── computer_software
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
│   └── int_unallocated
├── intra_group_fee
├── inv_in_subsidiary
├── mtg_insurance
│   ├── mtg_ins_nonconform
├── operational
│   ├── cash_management
│   ├── clearing
│   ├── custody
│   ├── ips
│   └── operational_escrow
├── operational_excess
├── other
├── prime_brokerage
├── ppe
│   ├── computer_peripheral
│   ├── furniture
│   ├── land
│   ├── machinery
│   ├── property
│   │   ├── investment_property
│   │   └── own_property
│   ├── telecom_equipment
│   └── vehicle
├── general_credit_risk
├── goodwill
├── pv_future_spread_inc
├── recovery
├── rec_unidentified_cpty
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
│   ├── corporation_tax
│   ├── ded_fut_prof
│   ├── ded_fut_prof_temp_diff
│   ├── fut_prof
│   ├── fut_prof_temp_diff
│   ├── not_fut_prof
│   ├── oth_tax_excl_temp_diff
│   └── reclass_tax
└── write_off
```

### dgs_contribution
Describes an account representing the **contributions to deposit guarantee schemes** paid by the reporting entity as defined by Annex 5 Part 2.48i of the EBA ITS on supervisory reporting.

### res_fund_contribution
Describes an account representing the **contributions to resolution funds** paid by the reporting entity as defined by Annex 5 Part 2.48i of the EBA ITS on supervisory reporting.

### deposit
The **deposit** enum value refers to a retail deposit defined in accordance with Article 411 of the [CRR][crr]:

### third_party_interest
Subcategory of deposits for which the interest is paid in a separate account held at a third party bank.

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

### cash_management
*Needs definition*

### critical_service
*Needs definition*

### div_from_cis
*Needs definition*

### div_from_money_mkt
*Needs definition*

### firm_operating_expenses
*Needs definition*

### firm_operations
*Needs definition*

### int_on_derivative
*Needs definition*

### loan_and_advance_fee
*Needs definition*

### retained_earnings
*Needs definition*

### system
*Needs definition*

### operational_excess
Excess operational deposits are defined as the part of the operational deposits (as defined in [LCR][lcr] Article 27.6) held in excess of those required for the provision of operational services. The distinction between operational deposits and excess operational deposits is required for the reporting of section 1.1.3 in the ouflows section of the [LCR][lcr]

### custody
As opposed to short-term definition within **operational**, **custody** here refers to the long-term custody of financial assets such as those held for safekeeping by a custodian bank.

### defined_benefit
A workplace pension based on your salary and how long you’ve worked for your employer. They’re sometimes called ‘final salary’ or ‘career average’ pension schemes. https://www.gov.uk/pension-types

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

### pv_future_spread_inc
Present value of future spread income subject to prepayment risk, such as non-credit enhancing interest-only strips and deferred mortgage placement fees receivable.  Required for BCAR risk weight and reporting.

### rec_unidentified_cpty
Corporate and retail receivables with unidentified counterparties.  Required for BCAR risk weight and reporting.

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

### cf_hedge_reclass
**Cash flow hedge reclass** describes an account that is the same as the standard cash flow hedge account, but one in which the profit and loss arising from the cashflow hedge is to be reclassified. It can be taken to equity, transferred to carry amount of hedged items or other reclassifications of the profit and losses.

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

### underwriting_fee
The fee owed to underwriters for their services.

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

### ded_fut_prof
Describes an account representing the amount of **deferred tax** deductible, reliant on future profitability and do not arise from temporary differences.

### ded_fut_prof_temp_diff
Describes an account representing the amount of **deferred tax** deductible, reliant on future profitability, arising due to temporary differences.

### fut_prof
Describes an account representing the amount of **deferred tax** non-deductible, reliant on future profitability and do not arise from temporary differences.

### fut_prof_temp_diff
Describes an account representing the amount of **deferred tax** non-deductible, reliant on future profitability, arising due to temporary differences.

### not_fut_prof
Describes an account representing the amount of **deferred tax** that do not rely on future profitability.

### reclass_tax
Describes an account representing the amount of **reclassified pnl tax** paid, received or deferred for the reporting period by the reporting entity.

### oth_tax_excl_temp_diff
Deferred tax assets excluding those arising from temporary differences.  Required for BCAR rwa calculations and BCAR reporting.

### dealing_revenue
Describes an account that holds the amount of profits or losses arising from the purchase, sale and holdings of tradable instruments.

### dealing_rev_fx
Describes an account that holds the amount of profits or losses arising from the purchase, sale and holdings of **fx instruments**.

### dealing_rev_sec
Describes an account that holds the amount of profits or losses arising from the purchase, sale and holdings of **securities**.

### dealing_rev_ir
Describes an account that holds the amount of profits or losses arising from the purchase, sale and holdings of **interest-rated related balance sheet securities**.

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

### int_unallocated
Describes an account that holds accrued interest that is unallocated.  Required for BCAR RWA calculation and reporting.

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

### general_credit_risk
Account which has an amount of general loan loss provision for credit risks that has been recognised in the financial statements of the institution in accordance with the applicable accounting framework.

### goodwill
**Goodwill** is a type of intangible asset. IFRS3, Appendix A, defines **goodwill** as:
> an asset representing the future economic benefits arising from other assets acquired in a business combination that are not individually identified and separately recognised.

### ppe
IAS 16(6) defines **property plant and equipment** as:
> tangible items that:
(a) are held for use in the production or supply of goods or services, for rental to others, or for administrative purposes; and
(b) are expected to be used during more than one period.

### computer_peripheral
Additional hardware used whilst connected to a computer e.g. printer, keyboard etc.

### furniture
Fixed tangible assets used to furnish an office.

### land
A solid surface of the earth, or an area, not covered by water which is designated for a specific purpose or otherwise.

### machinery
Fixed long-term tangible assets used by companies in its business operations, in particular, the creation of the goods or services.

### telecom_equipment
Hardware used for the purposes of telecommunications.

### vehicle
Fixed long-term assets of the company derived from trucks, vans, motorcycles and cars.

### other
The **other** enum value can be used when it is known that none of the other enum values apply.

### rent
Describes an account representing the amount of **rent** to be paid or received by the reporting entity.

### annual_bonus_accruals
Describes an account representing the part of staff expenses corresponding to the **annual_bonus_accruals** paid by the reporting entity.

### computer_and_it_costs
Describes an account representing the part of operating expenses corresponding to the **computer_and_it_costs** paid by the reporting entity.

### computer_software
Computer software intangibles. Required for BCAR RWA calculation and Reporting.  Ref: BCAR 40.290; Chapter 4, P164

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

### mtg_insurance
Prepaid portfolio mortgage insurance conforming to OSFI's 5 year amortization requirements.  Ref: BCAR 40.290; Chapter 4, P164

### mtg_ins_nonconform
Prepaid portfolio mortgage insurance that does not conform to OSFI's 5 year amortization requirements.  Ref: BCAR 40.290; Chapter 4, P164

### adj_syn_inv_own_shares
Adjustments of Synthetic positions - investments in own shares.  Required for BCAR RWA calculation and Reporting.  Ref: BCAR 40.290; Chapter 4, P164

### adj_syn_inv_decon_subs
Adjustments of Synthetic positions - investments in deconsolidated subsidiaries.  Required for BCAR RWA calculation and Reporting.  Ref: BCAR 40.290; Chapter 4, P164

### adj_syn_other_inv_fin
Adjustments of Synthetic positions - other significant investments in financials and joint ventures.  Required for BCAR RWA calculation and Reporting.  Ref: BCAR 40.290; Chapter 4, P164

### adj_syn_nonsig_inv_fin
Adjustments of Synthetic positions - non-significant investments in financials.  Required for BCAR RWA calculation and Reporting.  Ref: BCAR 40.290; Chapter 4, P164

### adj_syn_mtg_def_ins
Adjustments of Synthetic positions - adj_syn_mtg_def_ins.  Required for BCAR RWA calculation and Reporting.  Ref: BCAR 40.290; Chapter 4, P164

### capital_reserve
An account in the equity section of a company's balance sheet that indicates the cash on hand that can be used for future expenses or to offset any capital losses.

## Derivative
```bash
├── reference
├── client_execution
├── client_transmission
├── cva_hedge
└── back_to_back
```
### reference
Use this enumeration value to refer to derivatives which are underlyings of other derivative positions (e.g. swaptions).
In the context of [CRR][crr] Article 329, a reference derivative would be the underlying swap of a swaption.

### client_execution
Derivatives given this purpose value represent execution of orders on behalf of clients.
‘Execution of orders on behalf of clients’ means acting to conclude agreements to buy or sell one or more financial instruments
on behalf of clients and includes the conclusion of agreements to sell financial instruments issued by an investment firm or a credit institution at the moment of their issuance. [Article 4(1)(5) of Directive 2014/65/EU (MiFID].

### client_transmission
[FCA Handbook: PERG 13.3 Investment Services and Activities](https://www.handbook.fca.org.uk/handbook/PERG/13/3.html)
> Transmission pertains to the receiving and communucation of instructions or orders from the client in respect of investment services or financial instruments to another party for execution, such as an operator of a collective investment undertaking or agency broker.

More broadly, transmission is discussed in [MiFID 2](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014L0065) in reference to a 'tied agent':
> (29) 'tied agent' means a natural or legal person who, under the full and unconditional responsibility of only one investment firm on whose behalf it acts, promotes investment and/or ancillary services to clients or prospective clients, receives and transmits instructions or orders from the client in respect of investment services or financial instruments, places financial instruments or provides advice to clients or prospective clients in respect of those financial instruments or services;

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
│   ├── buy_to_let_other
│   ├── buy_to_let_construct
│   └── consumer_buy_to_let
├── ips
├── lifetime_mortgage
├── operational
├── promotional
├── reference
├── remortgage
├── remortgage_other
├── speculative_property
├── further_advance
├── non_b20
├── agriculture
├── construction
├── project_finance
│   ├── project_pre_op
│   └── project_hq_phase
├── object_finance
│   └── object_finance_hq
├── commodities_finance
└── other
```

### house_purchase
>The **house_purchase** value indicates that the purpose of the loan is for the purchase of residential property for occupation by the borrower.

### first_time_buyer
>The **first_time_buyer** value is a term used in the British and Irish property markets and defined in the Bank of England's [Mortgage Lending & Administration (MLAR) Definitions][mlardef] section E6.1/2 It is a sub-category of a **house_purchase** where "the tenure of the main borrower immediately before this advance was not owner-occupier."

### bridging_loan
>A **bridging_loan** is a short-term financing option used typically used for property owners to finance the period between buying a new property and selling an old one when the timing of the two does not match. It can also be used by property developers or investors who value speed over cost.

### buy_to_let
The **buy_to_let** refers to a real estate loan where the borrower is purchasing the property with a view of renting it out on a commercial basis to an *unrelated third party*. See [MLAR Definitions][mlardef] section E6.2.

This also encompasses "income-producing" real estate and Specialised Lending exposures.
e.g. [OSFI CAR 4.1.11][osfi-income-producing]
> Exposures where (...) the prospects for servicing the loan materially depend on the cash flows generated by the property securing the loan rather than on the underlying capacity of the borrower to service the debt from other sources,
e.g. OSFI Chapter 5, P17


### buy_to_let_house_purchase
Buy-to-let *and* house_purchase. See: **house_purchase**

### buy_to_let_remortgage
Buy-to-let *and* remortgage. See: **remortgage**

### buy_to_let_further_advance
Buy-to-let *and* further_advance. See: **further_advance**

### buy_to_let_other
Buy-to-let *and* other. See: **other**

### buy_to_let_construct
Buy-to-let *and* construction. See: **construction**

### consumer_buy_to_let
*Needs description*

### reference
Use this enumeration to refer to a loan that is not in the books of the reporting entity and represents parts, or the entirety, of a pool of loans backing a security that is in the books of the reporting entity (e.g. securities representing the reporting entity investments in rmbs)

### further_advance
*Needs description*

### non_b20
Those Loans not complying with the guidelines and expectations set out in OSFI's [Guideline B-20: Residential Mortgage Insurance Underwriting Practices and Procedures][osfi-b20].

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

Also used to categorize Specialised Lending exposures for High-volatility Commercial Real Estate, as per OSFI definition Chapter 5, P18

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
Loans given for the purpose of land, construction, development or re-development of a site.

FFEIC definition:
> loans secured by real estate made to finance (a) land development (i.e., the process of improving land – laying sewers, water pipes, etc.) preparatory to erecting new structures or (b) the on-site construction of industrial, commercial, residential, or farm buildings.

See also: [OSFI CAR Chapter 4.1.13][osfi-adc]


### project_finance
As defined in [Supervisory Reporting][sup-rep] part 2(5)(41)(l):
> 'Project finance loans' include loans that are recovered solely from the income of the projects financed by them.

As defined by OSFI Chapter 4, P66 and Chapter 5, P12:
>'Project finance refers to the method of funding in which the lender looks primarily to the revenues generated by a single project, both as the source of repayment and as security for the loan. This type of financing is usually for large, complex and expensive installations such as power plants, chemical processing plants, mines, transportation infrastructure, environment, media, and telecoms. Project finance may take the form of financing the construction of a new capital installation, or refinancing of an existing installation, with or without improvements.'

### project_pre_op
Project Finance early pre-operational phase that gets higher risk weight than other project finance in later phases.

Pre-operational is defined referencing the definition of a normal 'operational' phase project in [Basel 20.51](https://www.bis.org/basel_framework/chapter/CRE/20.htm?tldate=20220101&inforce=20230101&published=20201126#:~:text=For%20this%20purpose%2C%20operational,declining%20long%2Dterm%20debt.):
> For this purpose, operational phase is defined as the phase in which the entity that was specifically created to finance the project has
> (a)	a positive net cash flow that is sufficient to cover any remaining contractual obligation, and
> (b)	declining long-term debt.

Reference: [OSFI Chapter 4, P68](https://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/CAR22_chpt4.aspx#4.1.21:~:text=Project%20finance%20exposures,long%20term%20debt.)

### project_hq_phase
Project Finance that are deemed high-quality will get preferential risk weight than other project finance with lower quality.

[Basel CRE 20.52](https://www.bis.org/basel_framework/chapter/CRE/20.htm?tldate=20220101&inforce=20230101&published=20201126#:~:text=A%20high%20quality,of%20its%20default.):
> A high quality project finance exposure refers to an exposure to a project finance entity that is able to meet its financial commitments in a timely manner and its ability to do so is assessed to be robust against adverse changes in the economic cycle and business conditions. The following conditions must also be met:

> (1)	The project finance entity is restricted from acting to the detriment of the creditors (eg by not being able to issue additional debt without the consent of existing creditors);

> (2)	The project finance entity has sufficient reserve funds or other financial arrangements to cover the contingency funding and working capital requirements of the project;

> (3)	The revenues are availability-based19 or subject to a rate-of-return regulation or take-or-pay contract;

> (4)	The project finance entity’s revenue depends on one main counterparty and this main counterparty shall be a central government, PSE or a corporate entity with a risk weight of 80% or lower;

> (5)	The contractual provisions governing the exposure to the project finance entity provide for a high degree of protection for creditors in case of a default of the project finance entity;

> (6)	The main counterparty or other counterparties which similarly comply with the eligibility criteria for the main counterparty will protect the creditors from the losses resulting from a termination of the project;

> (7)	All assets and contracts necessary to operate the project have been pledged to the creditors to the extent permitted by applicable law; and

> (8)	Creditors may assume control of the project finance entity in case of its default.



Reference: [OSFI Chapter 4, P68-69](https://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/CAR22_chpt4.aspx#4.1.21:~:text=Project%20finance%20exposures,long%20term%20debt.)

### object_finance
As defined by OSFI Chapter 4, P66 and Chapter 5, P14:
>'Object finance refers to the method of funding the acquisition of equipment (e.g., ships, aircraft, satellites, railcars, and fleets) where the repayment of the loan is dependent on the cash flows generated by the specific assets that have been financed and pledged or assigned to the lender.'

### object_finance_hq
Object Finance that are deemed high-quality will get preferential risk weight than other object finance with lower quality.


According to [Basel 3.1](https://www.europarl.europa.eu/doceo/document/A-9-2023-0030_EN.html) object finance shall be deemed high quality when taking into account all of the following criteria:

> (1) The obligor can meet its financial obligations even under severely stressed conditions due to the presence of all of the following features:

>   adequate exposure-to-value of the exposure;

>   conservative repayment profile of the exposure;

>   commensurate remaining lifetime of the assets upon full pay-out of the exposure or alternatively recourse to a protection provider with high creditworthiness;

>   low refinancing risk of the exposure by the obligor or that risk is adequately mitigated by a commensurate residual asset value or recourse to a protection provider with high creditworthiness;

>   the obligor has contractual restrictions over its activity and funding structure;

>   the obligor uses derivatives only for risk-mitigation purposes;

>   material operating risks are properly managed;

> (2) the contractual arrangements on the assets provide lenders with a high degree of protection including the following features:

>   the lenders have a legally enforceable first-ranking right over the assets financed, and, where applicable, over the income that they generate;

>   there are contractual restrictions on the ability of the obligor to change anything to the asset which would have a negative impact on its value;

>   where the asset is under construction, the lenders have a legally enforceable first-ranking right over the assets and the underlying construction contracts;

> (3) the assets being financed meet all of the following standards to operate in a sound and effective manner:

>   the technology and design of the asset are tested;

>   all necessary permits and authorisations for the operation of the assets have been obtained;

>   where the asset is under construction, the obligor has adequate safeguards on the agreed specifications, budget and completion date of the asset, including strong completion guarantees or the involvement of an experienced constructor and adequate contract provisions for liquidated damages;

### commodities_finance
As defined by OSFI Chapter 4, P66 and Chapter 5, P15:
> 'Commodities finance refers to short-term lending to finance reserves, inventories, or receivables of exchange-traded commodities (e.g., crude oil, metals, or crops), where the loan will be repaid from the proceeds of the sale of the commodity and the borrower has no independent capacity to repay the loan.

### other
The **other** enum value can be used when none of the other enum values apply or the value is *unknown*.

## Security
```bash
├── collateral
│    ├──  variation_margin
│    ├──  independent_collateral_amount
│    ├──  custody
│    ├──  default_fund
│    └──  single_collateral_pool
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
├── ocir
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

### variation_margin
Defined in accordance with Article 30(1) and Article 30(3) of the [LCR][lcr] regulation:
> 30(1) "collateral posted for contracts listed in [Annex II of Regulation (EU) No. 575/2013](http://eur-lex.europa.eu/legal-content/en/TXT/?uri=celex%3A32013R0575) and credit derivatives".

> 30(3) "collateral needs that would result from the impact of an adverse market scenario on the credit institution's derivatives transactions, financing transactions and other contracts"

### derivative_collateral
(do not use - see *variation_margin*)

### independent_collateral_amount (ICA)
Defined in accordance with [SA-CCR][bis_sa_ccr].
> ICA represents (i) collateral (other than VM) posted by the counterparty that the bank may seize upon default of the counterparty, the amount of which does not change in response to the value of the transaction it secures and/or (ii) the Independent Amount (IA) parameter as defined in standard industry documentation.

### default_fund
Defined in accordance with [CRR], A CCP's default fund is a mechanism that allows the sharing (mutualisation) of losses among the CCP's clearing members.
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

### aircraft_finance
*Needs definition*

### single_collateral_pool
Use this enumeration value to identify to securities which are placed into a central bank single collateral pool. A list of eligible security types for the Bank of England SCP can be found [here][scp]

[scp]: https://www.bankofengland.co.uk/markets/eligible-collateral

### ocir
Use this enum to refer to funds reserved for the purpose of implementing, from an operational point of view, the resolution strategy and, consequently, to stabilise and restructure the bank.

[Bank of England OCIR][ocir]

[ocir]: https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/supervisory-statement/2021/ss421-may-2021.pdf

---

[reg]: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32009R0494&from=EN
[midifdir]: https://eur-lex.europa.eu/legal-content/en/TXT/?uri=CELEX:32014L0065
[crr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013R0575
[lcr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0061
[id]: https://github.com/suadelabs/fire/blob/master/documentation/properties/id.md
[mlardef]: http://www.bankofengland.co.uk/pra/documents/regulatorydata/mlar/sup_chapter16_annex19bg_20120401.pdf
[pruval]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:JOL_2016_021_R_0005
[bis_sa_ccr]: https://www.bis.org/publ/bcbs279.pdf
[osfi-adc]: https://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/CAR22_chpt4.aspx#fnb49:~:text=Land%20acquisition%2C%20development%20and%20construction%20(ADC,of%20any%20residential%20or%20commercial%20property.
[osfi-income-producing]: https://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/CAR22_chpt4.aspx#fnb49:~:text=CRE%2020.88%2D20.89%5D-,When%20the%20prospects%20for%20servicing%20the%20loan%20materially%20depend,capacity%20of%20the%20borrower%20to%20service%20the%20debt%20from%20other%20sources,-%2C%20and%20provided%20that
[osfi-b20]: https://www.osfi-bsif.gc.ca/Eng/Docs/b20_dft.pdf

