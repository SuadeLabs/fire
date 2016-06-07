---
layout:     property
title:      "type"
schemas:    [account, collateral, customer, loan]
---

# type


# Account
"call", "cd", "checking", "current", "internet_only", "isa", "money_market", "nostro", "savings", "time_deposit", "vostro", "other"

---

# Customer, Issuer, Guarantor, Entity
Article 411 of the [CRR][crr]:
> financial customer‧ means a customer that performs one or more of the activities listed in Annex I to Directive 2013/36/EU as its main business, or is one of the following:
> (a) a credit institution;
> (b) an investment firm;
> (c) an SSPE;
> (d) a CIU;
> (e) a non-open ended investment scheme;
> (f) an insurance undertaking;
> (g) a financial holding company or mixed-financial holding company.

### mdb
Multilateral Development Banks are defined in the [CRR][crr] Article 117:
> The Inter-American Investment Corporation, the Black Sea Trade and Development Bank, the Central American Bank for Economic Integration and the CAF-Development Bank of Latin America shall be considered multilateral development banks.
> ...
> (a) the International Bank for Reconstruction and Development;
> (b) the International Finance Corporation;
> (c) the Inter-American Development Bank;
> (d) the Asian Development Bank;
> (e) the African Development Bank;
> (f) the Council of Europe Development Bank;
> (g) the Nordic Investment Bank;
> (h) the Caribbean Development Bank;
> (i) the European Bank for Reconstruction and Development;
> (j) the European Investment Bank;
> (k) the European Investment Fund;
> (l) the Multilateral Investment Guarantee Agency;
> (m) the International Finance Facility for Immunisation;
> (n) the Islamic Development Bank.

### intl_org
International Organisations are defined in the [CRR][crr] Article 118:
> (a) the Union;
> (b) the International Monetary Fund;
> (c) the Bank for International Settlements;
> (d) the European Financial Stability Facility;
> (e) the European Stability Mechanism;
> (f) an international financial institution established by two or more Member States, which has the purpose to mobilise funding and provide financial assistance to the benefit of its members that are experiencing or threatened by severe financing problems.

---

# Loan
### trade_finance
From [CRR][crr] definitions (80):
> trade finance‧ means financing, including guarantees, connected to the exchange of goods and services through financial products of fixed short-term maturity, generally of less than one year, without automatic rollover;

### auto
LCR Article 13: 
> loans or leases for the financing of motor vehicles or trailers (see Article 3 of Directive 2007/46/EC).
> agricultural or forestry tractors (see Directive 2003/37/EC)
> tracked vehicles (see Directive 2007/46/EC)
> Such loans or leases may include ancillary insurance and service products or additional vehicle parts, and in the case of leases, the residual value of leased vehicles.

### personal
LCR Article 13: 
> loans and credit facilities to individuals resident in a Member State for personal, family or household consumption purposes.

### commercial 
LCR Article 13: 
> commercial loans, leases and credit facilities to undertakings established in a Member State to finance capital expenditures or business operations other than the acquisition or development of commercial real estate

### commercial_property
This includes commercial loans or mortgages that do not fall under **commercial** due to their real estate connection and do not classify as **mortgage** either due to the customer not being an individual or the occupation of the property not being residential.

### margin
From LCR Article 3 Definitions:
> margin loans means collateralised loans extended to customers for the purpose of taking leveraged trading positions.

### mortgage
A **mortgage** is a residential loan to a individuals secured with a one-to-one correspondence to land or property.

LCR Article 13:
> loans secured with a first-ranking mortgage granted to individuals for the acquisition of their main residence

From the Bank of England's [MLAR Definitions][mlar]
> It is lending to individuals secured by mortgage on land and buildings where the lender has either a first or second (or subsequent) charge, where at least 40% of the land and buildings is used for residential purposes, and where the premises are for occupation by either the borrower (or dependant), or any other third party (e.g. it includes 'buy to let' lending to individuals).
Only loans where there is a one-to-one correspondence between the loan and a specific security should be included within 'residential loans to individuals'. 
 
### credit_card
A **credit_card** is credit facility typically secured by a deposit account or equity in the borrower's property.

### credit_facility, multiccy_facility
From Annex I of the [CRR][crr]:
> agreements to lend, purchase securities, provide guarantees or acceptance facilities

### other
Other refers to a type of security not covered by the above. If you find yourself using this often, please [contribute][contributing].

### overdraft
*put as loan type or deduce from a negative balance?*

---

# Security

### cash
A cash or cash-equivalent security. Consider a securitisation of cash deposits.

### equity_held, 
This is a "catch all" term for *share*, *share_agg* to be used when further granularity is not available or not needed.

### share, share_agg   "cb_reserve", "cash_ratio_deposit",
Denotes if the security is a share (stock) or represents an aggregate for a portfolio or package of shares.

### debt_held
This is a "catch all" term for holding any of *bond*, *bond_amortising*, *index_linked_gilt*, *covered_bond*, *abs*, *residential_mbs*, *non_residential_mbs*, *frn*, *govt_gteed_frn*, to be used when further granularity is not available or not needed.

### debt_issue
This is a "catch all" term for issuance any of *bond*, *bond_amortising*, *index_linked_gilt*, *covered_bond*, *abs*, *residential_mbs*, *non_residential_mbs*, *frn*, *govt_gteed_frn*, to be used when further granularity is not available or not needed.

### bond, bond_amortising
### index_linked_gilt
### covered_bond
### emtn, mtn 

### commercial_paper
Commercial paper, in the global financial market, is an unsecured promissory note with a fixed maturity of no more than 270 days.

### cd
Certificate of deposit

### struct_note
Structured notes (typically a subclass of an EMTN/MTN program)

### spv_mortgages, spv_other

### abs
Any asset-backed security.

### rmbs
A residential mortgage-backed security (a subclass of an abs).

### rmbs_trans
This type value is in order to indicate whether a the security is subject to transitional provisions for securitisations backed by residential loans:

[LCR][lcr] Article 37:
> 1.   By derogation from Article 13, securitisations issued before 1 October 2015, where the underlying exposures are residential loans as referred to in point (g)(i) of Article 13(2), shall qualify as Level 2B assets if they meet all the requirements set out in Article 13 other than the loan-to-value or loan-to-income requirements set out in that point (g)(i) of Article 13(2).

> 2.   By derogation from Article 13, securitisations issued after 1 October 2015, where the underlying exposures are residential loans as referred to in point (g)(i) of Article 13(2) that do not meet the average loan-to-value or the loan-to-income requirements set out in that point, shall qualify as Level 2B assets until 1 October 2025, provided that the underlying exposures include residential loans that were not subject to a national law regulating loan-to-income limits at the time they were granted and such residential loans were granted at any time prior to 1 October 2015.

### cmbs
A commercial mortgage-backed security (a subclass of an abs).

### frn
A floating-rate note.

### govt_gteed_frn
A government guaranteed floating-rate note.

### stock_loan, stock_borrow, bond_loan, bond_borrow
[SFT Regulation][sftr] Article 3(7):
> 'securities or commodities lending' or 'securities or commodities borrowing' means a transaction by which a counterparty transfers securities or commodities subject to a commitment that the borrower will return equivalent securities or commodities on a future date or when requested to do so by the transferor, that transaction being considered as securities or commodities lending for the counterparty transferring the securities or commodities and being considered as securities or commodities borrowing for the counterparty to which they are transferred;

### buy_sell_back, sell_buy_back
[SFT Regulation][sftr] Article 3(8):
> 'buy-sell back transaction' or 'sell-buy back transaction' means a transaction by which a counterparty buys or sells securities, commodities, or guaranteed rights relating to title to securities or commodities, agreeing, respectively, to sell or to buy back securities, commodities or such guaranteed rights of the same description at a specified price on a future date, that transaction being a buy-sell back transaction for the counterparty buying the securities, commodities or guaranteed rights, and a sell-buy back transaction for the counterparty selling them, such buy-sell back transaction or sell-buy back transaction not being governed by a repurchase agreement or by a reverse-repurchase agreement within the meaning of point (9);

### repo, rev_repo
[SFT Regulation][sftr] Article 3(9):
> 'repurchase transaction' means a transaction governed by an agreement by which a counterparty transfers securities, commodities, or guaranteed rights relating to title to securities or commodities where that guarantee is issued by a recognised exchange which holds the rights to the securities or commodities and the agreement does not allow a counterparty to transfer or pledge a particular security or commodity to more than one counterparty at a time, subject to a commitment to repurchase them, or substituted securities or commodities of the same description at a specified price on a future date specified, or to be specified, by the transferor, being a repurchase agreement for the counterparty selling the securities or commodities and a reverse repurchase agreement for the counterparty buying them;

### margin_loan
[SFT Regulation][sftr] Article 3(10):
>'margin lending transaction' means a transaction in which a counterparty extends credit in connection with the purchase, sale, carrying or trading of securities, but not including other loans that are secured by collateral in the form of securities;

### sft
[SFT Regulation][sftr] Article 3(11):
> 'securities financing transaction' or 'SFT' means:
> (a) a repurchase transaction;
> (b) securities or commodities lending and securities or commodities borrowing;
> (c) a buy-sell back transaction or sell-buy back transaction;
> (d) a margin lending transaction;

### other
Other refers to a type of security not covered by the above. If you find yourself using this often, please [contribute][contributing].

---
[crr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013R0575
[lcr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0061
[mlar]: http://www.bankofengland.co.uk/pra/documents/regulatorydata/mlar/sup_chapter16_annex19bg_20120401.pdf
[sftr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R2365
[contributing]: https://github.com/SuadeLabs/fire/blob/master/CONTRIBUTING.md
