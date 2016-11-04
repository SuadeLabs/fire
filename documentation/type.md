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
│   ├── credit_institution
│   ├── investment_firm
│   ├── sspe
│   ├── ciu
│   ├── ceis
│   ├── pic
│   ├── insurer
│   ├── financial_holding
│   └── other_financial
├── central_bank
├── mdb
├── credit_union
├── deposit_broker
├── pse
│   ├── local_authority
│   ├── regional_govt
│   ├── central_govt
│   └── other_pse
├── sovereign
├── intl_org
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
A public sector entity is defined in the [LCR Regulation][lcr] Article 4:
> 'public sector entity' means a non-commercial administrative body responsible to central governments, regional governments or local authorities, or to authorities that exercise the same responsibilities as regional governments and local authorities, or a non-commercial undertaking that is owned by or set up and sponsored by central governments, regional governments or local authorities, and that has explicit guarantee arrangements, and may include self-administered bodies governed by law that are under public supervision;

### credit_institution
Credit institution is defined in the [LCR Regulation][lcr] Article 4:
> (1) 'credit institution' means an undertaking the business of which is to take deposits or other repayable funds from the public and to grant credits for its own account

### investment_firm
Investment firm is defined in the [LCR Regulation][lcr] Article 4:
> 1) "Investment firm" means any legal person whose regular occupation or business is the provision of one or more investment services to third parties and/or the performance of one or more investment activities on a professional basis;
> Member States may include in the definition of investment firms undertakings which are not legal persons, provided that:
> (a) their legal status ensures a level of protection for third parties' interests equivalent to that afforded by legal persons, and
> (b) they are subject to equivalent prudential supervision appropriate to their legal form.
> However, where a natural person provides services involving the holding of third parties' funds or transferable securities, he may be considered as an investment firm for the purposes of this Directive only if, without prejudice to the other requirements imposed in this Directive and in Directive 93/6/EEC, he complies with the following conditions:
> (a) the ownership rights of third parties in instruments and funds must be safeguarded, especially in the event of the insolvency of the firm or of its proprietors, seizure, set-off or any other action by creditors of the firm or of its proprietors;
> (b) the firm must be subject to rules designed to monitor the firm's solvency and that of its proprietors;
> (c) the firm's annual accounts must be audited by one or more persons empowered, under national law, to audit accounts;
> (d) where the firm has only one proprietor, he must make provision for the protection of investors in the event of the firm's cessation of business following his death, his incapacity or any other such event;

This definition is further refined in the [LCR Regulation][lcr] to exclude:
> (a) credit institutions;
> (b) local firms;
> (c) firms which are not authorised to provide the ancillary service referred to in point (1) of Section B of Annex I to Directive 2004/39/EC, which provide only one or more of the investment services and activities listed in points 1, 2, 4 and 5 of Section A of Annex I to that Directive, and which are not permitted to hold money or securities belonging to their clients and which for that reason may not at any time place themselves in debt with those clients;

### local_firm
Local firm is defined in the [LCR Regulation][lcr] Article 4:
> 'local firm' means a firm dealing for its own account on markets in financial futures or options or other derivatives and on cash markets for the sole purpose of hedging positions on derivatives markets, or dealing for the accounts of other members of those markets and being guaranteed by clearing members of the same markets, where responsibility for ensuring the performance of contracts entered into by such a firm is assumed by clearing members of the same markets

### sspe
*needs definition*

### ciu
A collective investment undertaking is defined in the [LCR Regulation][lcr] Article 4:
> 'collective investment undertaking' or 'CIU' means a UCITS as defined in Article 1(2) of Directive 2009/65/EC of the European Parliament and of the Council of 13 July 2009 on the coordination of laws, regulations and administrative provisions relating to undertakings for collective investment in transferable securities (UCITS) (21), including, unless otherwise provided, third-country entities which carry out similar activities, which are subject to supervision pursuant to Union law or to the law of a third country which applies supervisory and regulatory requirements at least equivalent to those applied in the Union, an AIF as defined in Article 4(1)(a) of Directive 2011/61/EU of the European Parliament and of the Council of 8 June 2011 on Alternative Investment Fund Managers (22), or a non-EU AIF as defined in Article 4(1)(aa) of that Directive;


### ceis
*needs definition*

### insurer
*needs definition*

### financial_holding
A financial holding copmany is defined in the [LCR Regulation][lcr] Article 4:
> (20) 'financial holding company' means a financial institution, the subsidiaries of which are exclusively or mainly institutions or financial institutions, at least one of such subsidiaries being an institution, and which is not a mixed financial holding company;

### other_financial
Any other type to be classified as financial but not one of the other types witin financial.

### pic
*needs definition*

### credit_union
*needs definition*

### deposit_broker
A deposit broker is used in some places in the CRR regulation, however is not well defined. In fact, a [2016 EBA Q&A addresses this lack of definition][deposit-broker-qa] directly.


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

```
├── equity
│   ├── share
│   └── share_agg
├── debt
│   ├── bond
│   ├── bond_amortising
│   ├── index_linked_gilt
│   ├── covered_bond
│   ├── frn
│   ├── commercial_paper
│   ├── cd
│   ├── struct_note
│   ├── spv_mortgages
│   ├── spv_other
│   ├── mtn
│   │   └── emtn
│   └── abs
│       ├── abs_auto
│       ├── abs_sme
│       ├── abs_consumer
│       ├── abs_other
│       └── mbs
│           ├── rmbs
│           ├── rmbs_trans
│           └── cmbs
├── cb_reserve
├── cb_facility
├── cash_ratio_deposit
├── cash
└── other
```

### cash
A cash or cash-equivalent security. Consider a securitisation of cash deposits.

### equity
This is a "catch all" term for equity instruments such as *share*, *share_agg* to be used when further granularity is not available or not needed.

### share, share_agg   "cb_reserve", "cash_ratio_deposit",
Denotes if the security is a share (stock) or represents an aggregate for a portfolio or package of shares.

### debt
This is a "catch all" term for debt of any kind, *bond*, *bond_amortising*, *index_linked_gilt*, *covered_bond*, *abs*, *residential_mbs*, *non_residential_mbs*, *frn*, *govt_gteed_frn*, to be used when further granularity is not available or not needed.

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
Commercial paper, in the global financial market, is an unsecured promissory note with a fixed maturity of, typically, not more than 270 days.

The [Money Market Statistics Regulation][mm-stat] defines it in Annex II as:
> A debt instrument that is either unsecured or backed by collateral provided by the issuer, which has a maturity of not more than one year and is either interest-bearing or discounted.

### cd
Certificate of deposit is defined in the [Money Market Statistics Regulation][mm-stat] in Annex II as:
> A fixed-rate debt instrument issued by an MFI (monetary financial institution) entitling the holder to a specific fixed rate of interest over a defined fixed term of up to one year.
> note: "one year" is defined as transactions with a maturity date of not more than 397 days after the trade date

### struct_note
Structured notes (typically a subclass of an EMTN/MTN program)

### spv_mortgages, spv_other
*needs definition*

### abs
Any asset-backed security.
*needs definition*

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
A Floating-rate Note is defined in the [Money Market Statistics Regulation][mm-stat] in Annex II as:
> A debt instrument for which the periodic interest payments are calculated on the basis of the value, i.e. through fixing of an underlying reference rate such as Euribor on predefined dates known as fixing dates, and which has a maturity of not more than one year.
> note: "one year" is defined as transactions with a maturity date of not more than 397 days after the trade date

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

```bash
├── deposit
│   ├── current
│   ├── checking
│   ├── call
│   ├── internet_only
│   ├── time_deposit
│   ├── savings
│   └── cd
├── isa
├── money_market
├── nostro
├── vostro
├── prepaid_card
├── debit_card
├── credit_card
└── other
```

### call
A call account is defined in the [Money Market Statistics Regulation][mm-stat] in Annex II as:
> any unsecured borrowing/lending redeemable at notice,

### cd
A deposit account purely holding certificates of deposit (see *Security* **type**)

### prepaid_card
From the [Interchange Fees for Card-based Payments Regulation][card-fees] Article 2:
> (35) 'prepaid card' means a category of payment instrument on which electronic money, as defined in point 2 of Article 2 of Directive 2009/110/EC, is stored.
NB. see credit_card

### debit_card
From the [Interchange Fees for Card-based Payments Regulation][card-fees] Article 2:
> (33) 'debit card' means a category of payment instrument that enables the payer to initiate a debit card transaction excluding those with prepaid cards;
> (4) 'debit card transaction' means a card-based payment transaction, including those with prepaid cards that is not a credit card transaction;

NB. see credit_card

### credit_card
A credit card is typically an off-balance sheet, contingent funding obligation whereby a customer has a certian credit limit and may borrow funds at any point, up to that limit, similar to a card-based credit facility.

in the [Interchange Fees for Card-based Payments Regulation][card-fees] they discuss credit and debit cards:
> There are two main types of credit cards available on the market. With deferred debit cards, the total amount of transactions is debited from the cardholder account at a pre-agreed specific date, usually once a month, without interest to be paid. With other credit cards, the cardholder can use a credit facility in order to reimburse part of the amounts due at a later date than specified, together with interest or other costs.

A credit card is then defined in Article 2 as:
> (34) 'credit card' means a category of payment instrument that enables the payer to initiate a credit card transaction;
> (5) 'credit card transaction' means a card-based payment transaction where the amount of the transaction is debited in full or in part at a pre agreed specific calendar month date to the payer, in line with a prearranged credit facility, with or without interest;

### current (checking, demand)
Any transactional account 

### internet_only
An internet-only account is one that is offered and only accessible via the internet. The [FCA defines the internet][fca-internet] in their handbook as:
> The Internet is a unique medium for communicating financial promotions as it provides easy access to a very wide audience. At the same time, it provides very little control over who is able to access the financial promotion.

The distinction here linked to financial promotions suggests that internet-only accounts are sold and managed through a higher risk channel and therefore should be regulated spearately to other accounts.

### isa
An ISA is an individual savings account which is a scheme of investment satisfying the conditions prescribed in the UK's [ISA Regulations][uk-isa].

### money_market
A money market account is an interest-bearing account that typically pays a higher interest rate than a savings account, and which provides the account holder with limited check-writing ability. 

Money market accounts are accounts where the customer's money has been invested in the "money markets" either directly in money market instruments or money market funds which are described in the [2013 Proposal for the Regulation of Money Market Funds][mmf-prpposal] as providing a key component of corporate banking:
> On the demand side, MMFs offer a short-term cash management tool that provides a high degree of liquidity, diversification, stability of value combined with a market-based yield. MMFs are mainly used by corporations seeking to invest their excess cash for a short time frame, for example until a major expenditure, such as the payroll, is due.

Money market deposits are mentioned in association with definitions of cash in that they represent *claims for the repayment of money*.

The [Money Market Statistics Regulation][mm-stat] specifically states in Article 1:
> (10) 'money market instrument' means any of the instruments listed in Annexes I, II and III;
> (11) 'money market fund' means a collective investment undertaking that requires authorisation as an undertaking for collective investment in transferable securities under Directive 2009/65/EC of the European Parliament and of the Council (6) or is an alternative investment fund under Directive 2011/61/EU of the European Parliament and of the Council (7), invests in short term assets and has as distinct or cumulative objectives offering returns in line with money market rates or preserving the value of an investment;

### nostro and vostro (loro)
Nostro and vostro (loro) accounts are used in the context of correspondent banking operations which are described in [ECB guidelines on monetary policy instruments][ecb-guidleines] from 2003:
> Correspondent banking: an arrangement under which one credit institution provides payment and other services to another credit institution. Payments through correspondents are often executed through reciprocal accounts (nostro and loro accounts) to which standing credit lines may be attached. Correspondent banking services are primarily provided across international boundaries but are also known as agency relationships in some domestic contexts. 
> A loro account is the term used by a correspondent to describe an account held on behalf of a foreign credit institution; the foreign credit institution would in turn regard this account as its nostro account.

### savings
An account subject to the European Council [Directive on taxation of savings][eur-savings-tax]. A savings account essentially does not allow the customer to use funds in the account as a "medium of exchange" such as writing checks or for making ATM withdrawals. Hence, funds are typically not callable immediately and/or incur a withdrawal penalty such as loss of interest.
In the US, [Regulation D][reg-d] uses the characteristics of the 'reservation of right' and 'convenient' withdrawals to describe savings accounts:
> In order to classify an account as a 'savings deposit,' the institution must in its account agreement with the customer reserve the right at any time to require seven days’ advance written notice of an intended withdrawal. In practice, this right is never exercised, but the institution must nevertheless reserve that right in the account agreement. In addition, for an account to be
classified as a 'savings deposit,' the depositor may make no more than six 'convenient' transfers or withdrawals per month from the account.


### time_deposit
A fixed-term deposit with a specific [*end_date*][end-date].
The US Regulation D describes time deposits as having the following characteristics:
> Time deposit accounts have the following characteristics:
> - must have a maturity of at least seven days from
the date of deposit
> - may require at least seven days’ prior written
notice of intent to withdraw funds
> - must be subject to early withdrawal penalties if
funds are withdrawn within six days of the date of
deposit or within six days of the date of the
immediately preceding partial withdrawal
> - may be interest-bearing
> - may be evidenced by a negotiable or nonnegotiable,
transferable or nontransferable certificate,
instrument, passbook, book entry, or
other similar instrument
> - include club accounts (such as Christmas club or
vacation club accounts)
> - no eligibility requirements

### deposit
Deposit or depository account is defined in the [Directive regarding the mandatory exchange of tax information][exch-tax-info] section 8:
> The term “Depository Account” includes any commercial, checking, savings, time, or thrift account, or an account that is evidenced by a certificate of deposit, thrift certificate, investment certificate, certificate of indebtedness, or other similar instrument maintained by a Financial Institution in the ordinary course of a banking or similar business. A Depository Account also includes an amount held by an insurance company pursuant to a guaranteed investment contract or similar agreement to pay or credit interest thereon.

### other
Any other account type that cannot be classified as one of the other types. 


# collateral
The collateral type defines the form of the collateral, such as property or other assets used to secure an obligation.

The [provision of assets][arrangement] to secure the performance of an obligation, whereby the assets can be provided: either by transfer of full ownership from a collateral provider to a collateral taker; or by the transfer of possession from a collateral provider to a collateral taker under a security right (e.g. pledge, charge or lien), where the full ownership of the assets remains with the collateral provider.




---
[crr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013R0575

[card-fees]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2015.123.01.0001.01.ENG

[lcr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0061

[mlar]: http://www.bankofengland.co.uk/pra/documents/regulatorydata/mlar/sup_chapter16_annex19bg_20120401.pdf

[sftr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R2365

[contributing]: https://github.com/SuadeLabs/fire/blob/master/CONTRIBUTING.md

[dpd]: http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=CELEX:31995L0046:en:HTML

[fca-indiv]: https://www.handbook.fca.org.uk/handbook/glossary/G3173.html
[fca-internet]: https://www.handbook.fca.org.uk/handbook/PERG/8/22.html

[mm-stat]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R1333
[mmf-prpposal]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52013PC0615

[ecb-eurosystem-procedures]: https://www.ecb.europa.eu/ecb/legal/pdf/l_06920040308en00010085.pdf
[eur-savings-tax]: http://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1477869014542&uri=CELEX:32003L0048

[exch-tax-info]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32014L0107

[sme]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32003H0361
[sme-what]: http://ec.europa.eu/growth/smes/business-friendly-environment/sme-definition/index_en.htm

[deposit-broker-qa]: http://www.eba.europa.eu/single-rule-book-qa?p_p_id=questions_and_answers_WAR_questions_and_answersportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_pos=1&p_p_col_count=2&_questions_and_answers_WAR_questions_and_answersportlet_jspPage=%2Fhtml%2Fquestions%2Fviewquestion.jsp&_questions_and_answers_WAR_questions_and_answersportlet_viewTab=1&_questions_and_answers_WAR_questions_and_answersportlet_questionId=1382163&_questions_and_answers_WAR_questions_and_answersportlet_statusSearch=1

[arrangement]: http://ec.europa.eu/internal_market/financial-markets/docs/collateral/directive-presentation_en.pdf

[uk-isa]: http://www.legislation.gov.uk/uksi/1998/1870/contents/made
[end-date]: https://github.com/SuadeLabs/fire/blob/master/documentation/end_date.md
[reg-d]: http://www.federalreserve.gov/boarddocs/supmanual/cch/int_depos.pdf
