---
layout:		property
title:		"purpose"
schemas:	[account, loan, security]
---

# purpose
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
The **collateral** enum type identifies an account or deposit received as collateral and hence, not classified as a liability for the purposes of Article 27 and 29 of the [LCR][lcr]. Collateral held in an account should have a corresponding [**account_id**][account_id] in the collateral schema.

### operational
The **clearing** enum value indicates that the account or deposit is being maintained for clearing, settlement, custody or cash_management services in the context of an operational relationship and hence can be treated as a very short term exposure. *(further granularity needed or  exists?)*

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
Describes an account held for prime brokerage reasons but not including those contained above for operational reasons.

### other
The **other** enum value can be used when none of the other enum values apply or the value is *unknown*.

## Loan
### house_purchase
The **house_purchase** value indicates that the purpose of the loan is for the purchase of residential property for occupation by the borrower.

### first_time_buyer
The **first_time_buyer** value is a term used in British and Irish property markets and defined in the Bank of England's [Mortgage Lending & Administration (MLAR) Definitions][mlardef]. It is a sub-category of a **house_purchase** where "the tenure of the main borrower immediately before this advance was not owner-occupier."

### buy_to_let
The **buy_to_let** value is a term used in British property markets where the borrower is purchasing the property with a view of renting it out on a commercial basis to an *unrelated third party*. See [MLAR Definitions][mlardef] section E6.2.

### remortgage
The **remortgage** value indicates a re-mortgage or refinancing of an existing property by an existing customer of the firm who had a loan with a **house_purchase** purpose. Note that this does not include re-mortgages of **first_time_buyer** and **buy_to_let** loans which should retain their respective purposes in the event of a re-mortgage. See [MLAR Definitions][mlardef] section E6.4/5.

### remortgage_other
The **remortgage_other** value indicates a re-mortgage by a new customer who is refinancing a loan from another lender.

### lifetime_mortgage
A **lifetime_mortgage** is a very specific kind of British mortgage contract and is defined in the [FCA Handbook](https://www.handbook.fca.org.uk/handbook/glossary/G1294.html). It is geared towards customers of a certain age in order to release equity and typically repayment occurs at the time of the customers death when the property is sold.

### bridging_loan
A **bridging_loan** is a short-term financing option used typically used for property owners to finance the period between buying a new property and selling an old one when the timing of the two does not match. It can also be used by property developers or investors who value speed over cost.

### other
The **other** enum value can be used when none of the other enum values apply or the value is *unknown*.

### speculative_property
From [CRR][crr] definitions (79):
> speculative immovable property financing‧ means loans for the purposes of the acquisition of or development or construction on land in relation to immovable property, or of and in relation to such property, with the intention of reselling for profit;

### repo / reverse_repo
From [CRR][crr] definitions (82):
> repurchase agreement‧ and ‧reverse repurchase agreement‧ mean any agreement in which an institution or its counterparty transfers securities or commodities or guaranteed rights relating to either of the following:
> (a) title to securities or commodities where that guarantee is issued by a recognised exchange which holds the rights to the securities or commodities and the agreement does not allow an institution to transfer or pledge a particular security or commodity to more than one counterparty at one time, subject to a commitment to repurchase them;
> (b) substituted securities or commodities of the same description at a specified price on a future date specified, or to be specified, by the transferor, being a repurchase agreement for the institution selling the securities or commodities and a reverse repurchase agreement for the institution buying them;

### internal_hedge
From [CRR][crr] definitions (96):
> internal hedge means a position that materially offsets the component risk elements between a trading book and a non-trading book position or sets of positions;


---
[crr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013R0575
[lcr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0061
[account_id]: https://github.com/suadelabs/fire/blob/master/documentation/account_id.md
[mlardef]: http://www.bankofengland.co.uk/pra/documents/regulatorydata/mlar/sup_chapter16_annex19bg_20120401.pdf
