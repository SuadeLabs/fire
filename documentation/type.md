---
layout:     property
title:      "type"
schemas:    [account, collateral, customer, derivative_cash_flow, derivative, entity, guarantor, issuer, loan_aggregate, loan_transaction, loan, security]
---


# type

# Customer, Issuer, Guarantor, Entity
Customer, issuer, guarantor and entity schemas share a lot of common type attributes so they are grouped together here. Also, due to the complexity of this property, the variety of reporting granularity and the larger issue of data quality at firms, the fields are not all mutually exclusive and should be thought of more as a tree rather than unique items:

```bash
├── individual
│   ├── partnership
│   └── natural_person
├── corporate
│   └── sme
├── financial
│   ├── central_bank
│   ├── credit_institution
│   ├── investment_firm
│   ├── sspe
│   ├── ciu
│   ├── ceis
│   ├── pic
│   ├── insurer
│   ├── financial_holding
│   └── other_financial
├── pse
│   ├── local_authority
│   ├── regional_govt
│   ├── central_govt
│   └── other_pse
├── sovereign
├── intl_org
├── mdb
├── credit_union
├── deposit_broker
└── other
```

### individual
Individual is a UK specific definition which is slightly broader than a natural person and defined in the FCA Handbook Glossary under [individual][fca-indiv]:
> (a) a natural person; or
> (b) a partnership consisting of two or three persons not all of whom are bodies corporate; or
> (c) an unincorporated body of persons which does not consist entirely of bodies corporate and is not a partnership.

### natural_person
Natural person refers to a human being as you would expect. It is further defined in the [Data Protection Directive][dpd]:
> Article 2(a):
> (a) ... an identifiable person is one who can be identified, directly or indirectly, in particular by reference to an identification number or to one or more factors specific to his physical, physiological, mental, economic, cultural or social identity

### partnership
As defined in the FCA Handbook referencing the Financial Securities and Markets Act:
> (in accordance with section 417(1) of the Act (Definitions)) any partnership, including a partnership constituted under the law of a country or territory outside the United Kingdom, but not including a limited liability partnership.

### sme
Definition of an SME is based on a set of criteria, while in theory it is possible for this to be a dynamic field based on other relevant data provided (employee count, turnover etc.), often times the data is unavailable or not current and hence firm may wish to identify SMEs directly.
In this scenario, an SME type will be assumed to comply with the [EU SME Recommendation][sme], further explained in [What is an SME?][sme-what] broadly as:

Company category | Staff headcount | Turnover (or) | Balance sheet total
-----------------|-----------------|---------------|--------------------
Medium-sized     | < 250           | ≤ € 50 m      | ≤ € 43 m            
Small            | < 50            | ≤ € 10 m      | ≤ € 10 m            
Micro            | < 10            | ≤ € 2 m       | ≤ € 2 m             


### other
Other means it is known to **not** be one of the other types. If type is unknown it should just be left blank.

### intl_org
This is a list, CRR 118, referenced in LCR 10(g)


### financial
Article 411 of the [CRR][crr]:
> financial customer‧ means a customer that performs one or more of the activities listed in Annex I to Directive 2013/36/EU as its main business, or is one of the following:
> (a) a credit institution;
> (b) an investment firm;
> (c) an SSPE;
> (d) a CIU;
> (e) a non-open ended investment scheme;
> (f) an insurance undertaking;
> (g) a financial holding company or mixed-financial holding company.

> 'financial sector entity' means any of the following:
> (a) an institution;
> (b) a financial institution;
> (c) an ancillary services undertaking included in the consolidated financial situation of an institution;
> (d) an insurance undertaking;
> (e) a third-country insurance undertaking;
> (f) a reinsurance undertaking;
> (g) a third-country reinsurance undertaking;
> (h) an insurance holding company;
> (i) a mixed-activity holding company
> (j) a mixed-activity insurance holding company as defined in point (g) of Article 212(1) of Directive 2009/138/EC;
> (k) an undertaking excluded from the scope of Directive 2009/138/EC in accordance with Article 4 of that Directive;
> (l) a third-country undertaking with a main business comparable to any of the entities referred to in points (a) to (k);

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


### corporate
*needs definition*
### sovereign  
*needs definition*
### central_bank
*needs definition*
### regional_govt
*needs definition*
### central_govt
*needs definition*
### pse
*needs definition*
### credit_institution
*needs definition*
### investment_firm
*needs definition*
### sspe
*needs definition*
### ciu
*needs definition*
### ceis
*needs definition*
### insurer
*needs definition*
### financial_holding
*needs definition*
### other_financial
*needs definition*
### pic
*needs definition*
### credit_union
*needs definition*
### deposit_broker
*needs definition*


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




# Security

```bash
├── equity_held
│   ├── share
│   └── share_agg
├── cb_reserve
├── cb_facility
├── cash_ratio_deposit
├── debt_held
│   ├── bond
│   ├── bond_amortising
│   ├── index_linked_gilt
│   ├── covered_bond
│   ├── frn
│   └── abs
│       ├── abs_auto
│       ├── abs_sme
│       ├── abs_consumer
│       ├── abs_other
│       └── mbs
│           ├── rmbs
│           ├── rmbs_trans
│           └── cmbs
├── sft
│   ├── margin_loan
│   ├── repo
│   │   ├── cash_loan
│   │   ├── bond_loan
│   │   ├── stock_loan
│   │   └── sell_buy_back
│   └── rev_repo
│       ├── cash_borrow
│       ├── bond_borrow
│       ├── stock_borrow
│       └── buy_sell_back
├── debt_issue
│   ├── commercial_paper
│   ├── cd
│   ├── covered_bond_issue
│   ├── struct_note
│   ├── spv_mortgages
│   ├── spv_other
│   └── mtn
│       └── emtn
├── cash
└── other
```

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
*needs definition*
### index_linked_gilt
*needs definition*
### covered_bond
From the [LCR][lcr] introduction (9):
Covered bonds are debt instruments issued by credit institutions and secured by a cover pool of assets which typically consist of mortgage loans or public sector debt to which investors have a preferential claim in the event of default. Their secured nature and certain additional safety features, such as the requirement on the issuer to replace non-performing assets in the cover pool and maintain the cover pool at a value exceeding the par value of the bonds (‘asset coverage requirement’), have contributed to make covered bonds relatively low-risk, yield-bearing instruments with a key funding role in mortgage markets of most Member States. In certain Member States outstanding covered bond issuance exceeds the pool of outstanding government bonds. Certain covered bonds of credit quality step 1, in particular, exhibited an excellent liquidity performance during the period from 1 January 2008 to 30 June 2012 analysed by the EBA in its report. Nevertheless the EBA recommended treating these covered bonds as level 2A assets to align with BCBS standards. However, in the light of the considerations made above about their credit quality, liquidity performance and role in the funding markets of the Union, it is appropriate for these credit quality step 1 covered bonds to be treated as level 1 assets. In order to avoid excessive concentration risks and unlike other level 1 assets, the holdings of credit quality step 1 covered bonds in the liquidity buffer should be subject to a 70 % cap of the overall buffer, a minimum 7 % haircut and to the diversification requirement.

### emtn, mtn
*needs definition*

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

##### underlying_type
The **receivables or assets underlying the securitisation** must be credit claims or receivables with defined terms relating to rental payments or principal and interest payment. Any referenced interest payments should be based on commonly encountered market interest rates and may include terms for caps and floors, but should not reference complex formulae or exotic derivatives.
A non-exhaustive list of [examples][ecbexamples] of underlying assets that may comply with the above principles, (subject to meeting all other criteria) could include:
- residential mortgages,
- certain commercial real estate mortgages,
- loans to SMEs,
- automobile loans/leases,
- consumer finance loans,
- credit card receivables, and
- leasing receivables.

[ecbexamples]: https://www.ecb.europa.eu/pub/pdf/other/ecb-boe_case_better_functioning_securitisation_marketen.pdf

# Account
### call
*needs definition*
### cd
*needs definition*
### credit_card
*needs definition*
### checking
*needs definition*
### current
*needs definition*
### internet_only
*needs definition*
### isa
*needs definition*
### money_market
*needs definition*
### nostro
*needs definition*
### savings
*needs definition*
### time_deposit
*needs definition*
### vostro
*needs definition*
### other
*needs definition*


---
[crr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013R0575
[lcr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0061
[mlar]: http://www.bankofengland.co.uk/pra/documents/regulatorydata/mlar/sup_chapter16_annex19bg_20120401.pdf
[sftr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R2365
[contributing]: https://github.com/SuadeLabs/fire/blob/master/CONTRIBUTING.md
[dpd]: http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=CELEX:31995L0046:en:HTML
[fca-indiv]: https://www.handbook.fca.org.uk/handbook/glossary/G3173.html
[sme]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32003H0361
[sme-what]: http://ec.europa.eu/growth/smes/business-friendly-environment/sme-definition/index_en.htm

# collateral

The [provision of assets][arrangement] to secure the performance of an obligation, whereby the assets can be provided: either by transfer of full ownership from a collateral provider to a collateral taker; or by the transfer of possession from a collateral provider to a collateral taker under a security right (e.g. pledge, charge or lien), where the full ownership of the assets remains with the collateral provider.

 The collateral type defines the form of the collateral, such as property, shares, cash etc.

[arrangement]: http://ec.europa.eu/internal_market/financial-markets/docs/collateral/directive-presentation_en.pdf
