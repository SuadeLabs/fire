---
layout:		property
title:		"purpose"
schemas:	[account, loan, security, derivative, derivative_cash_flow]
---

# purpose

---

The **purpose** property describes the reason behind the creation or usage of the financial product *as seen from the point of view of the financial institution*.

## Account

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
The **collateral** enum type identifies an account or deposit received as collateral and hence, not classified as a liability for the purposes of Article 27 and 29 of the [LCR][lcr]. Collateral held in an account should have a corresponding [**id**][id] in the collateral schema.

### operational
The **clearing** enum value indicates that the account or deposit is being maintained for clearing, settlement, custody or cash management services in the context of an **operational** relationship and hence can be treated as a very short term exposure.

Clearing and comparable services from the [CRR][crr] Article 422.4:
> Clearing, custody or cash management or other comparable services referred to in points (a) and (d) of paragraph 3 only covers such services to the extent that they are rendered in the context of an established relationship on which the depositor has substantial dependency. They shall not merely consist in correspondent banking or prime brokerage services and the institution shall have evidence that the client is unable to withdraw amounts legally due over a 30 day horizon without compromising its operational functioning.

Operational deposit from the [CRR][crr] Article 27.6:
> 6. In order to identify the deposits referred to in point (c) of paragraph 1, a credit institution shall consider that there is an established operational relationship with a non-financial customer, excluding term deposits, savings deposits and brokered deposits, where all of the following criteria are met:
> (a) the remuneration of the account is priced at least 5 basis points below the prevailing rate for wholesale deposits with comparable characteristics, but need not be negative;
> (b) the deposit is held in specifically designated accounts and priced without creating economic incentives for the depositor to maintain funds in the deposit in excess of what is needed for the operational relationship;
> (c) material transactions are credited and debited on a frequent basis on the account considered;
> (d) one of the following criteria is met:
> (i) the relationship with the depositor has existed for at least 24 months;
> (ii) the deposit is used for a minimum of 2 active services. These services may include direct or indirect access to national or international payment services, security trading or depository services.
> Only that part of the deposit which is necessary to make use of the service of which the deposit is a by-product shall be treated as an operational deposit. The excess shall be treated as non-operational.

### custody
As opposed to short-term definition within **operational**, **custody** here refers to the long-term custody of financial assets such as those held for safekeeping by a custodian bank.

### prime_brokerage
Describes an account held for prime brokerage reasons but not including those contained above for operational reasons. These accounts are used for prime brokerage service transactions which are in essence investment activities including securities lending, leveraged trade executions and cash management, among other things.

### other
The **other** enum value can be used when none of the other enum values apply or the value is *unknown*.

## Derivative
### reference
Use this enumeration value to refer to derivatives which are underlyings of other derivative positions (e.g. swaptions).
In the context of [CRR][crr] Article 329, a reference derivative would be the underlying swap of a swaption.

## Derivative Cash Flow
### reference
Use this enumeration value to refer to derivative cash flows which are calculated in order to decompose derivatives in combinations of long and short flows. See [CRR][crr] Articles 328 to 331.

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
├── promotional
├── remortgage
├── remortgage_other
├── consumer_buy_to_let
├── further_advance
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

### other
The **other** enum value can be used when none of the other enum values apply or the value is *unknown*.

## Security
```bash
├── investment
├── collateral
|    └──  derivative_collateral
├── reference
├── share_capital
|    └──  non_controlling
├── trade_finance
├── aircraft_finance
└──   other
```
### trade_finance
From [CRR][crr] definitions (80):
> **Trade finance** means financing, including guarantees, connected to the exchange of goods and services through financial products of fixed short-term maturity, generally of less than one year, without automatic rollover;

### derivative_collateral
Defined in accordance with Article 30(1) of the [LCR][lcr] regulation:
> "collateral posted for contracts listed in [Annex II of Regulation (EU) No. 575/2013](http://eur-lex.europa.eu/legal-content/en/TXT/?uri=celex%3A32013R0575) and credit derivatives".

### reference
Use this enumeration value to refer to securities which are underlyings of derivative positions (e.g. bond futures).
In the context of [CRR][crr] Article 328, a reference security would be the underlying bond of a bond future position.

### share_capital
This indicates shares that have been [issued][issued] for the purpose of raising capital for the company.     

[issued]: https://www.investopedia.com/terms/s/sharecapital.asp

### non_controlling 
[Commission Regulation (EC) No 494/2009][reg] defines **non-controlling interest** as:
> the equity in a subsidiary not attributable, directly or indirectly, to a parent.


[reg]: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32009R0494&from=EN
---
[crr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013R0575
[lcr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0061
[id]: https://github.com/suadelabs/fire/blob/master/documentation/properties/id.md
[mlardef]: http://www.bankofengland.co.uk/pra/documents/regulatorydata/mlar/sup_chapter16_annex19bg_20120401.pdf
