---
layout:     property
title:      "type"
schemas:    [account, collateral, customer, derivative_cash_flow, derivative, entity, guarantor, issuer, loan_transaction, loan, security]
---

# type

---

# customer, issuer, guarantor, entity
Customer, issuer, guarantor and entity schemas share a lot of common type attributes so they are grouped together here. Also, due to the complexity of this property, the variety of reporting granularity and the larger issue of data quality at firms, the fields are not all mutually exclusive and should be thought of more as a tree rather than unique items:

```bash
├── individual
│   ├── partnership
│   └── natural_person
├── corporate
│   └── sme
├── financial
│   ├── credit_institution
│   │   └── promotional_lender
│   ├── investment_firm
│   ├── sspe
│   ├── ciu
│   ├── ceis
│   ├── pic
│   ├── insurer
│   ├── financial_holding
│   └── other_financial
├── ccp
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
Individual is a UK specific definition which is slightly broader than a natural person and defined in the [FCA Handbook Glossary][fca-indiv] under individual:
> (a) a natural person; or
>
> (b) a partnership consisting of two or three persons not all of whom are bodies corporate; or
>
> (c) an unincorporated body of persons which does not consist entirely of bodies corporate and is not a partnership.

### natural_person
Natural person refers to a human being, as you would expect. It is further defined in the [Data Protection Directive][dpd]:
> Article 2(a):
> (a) ... an identifiable person is one who can be identified, directly or indirectly, in particular by reference to an identification number or to one or more factors specific to his physical, physiological, mental, economic, cultural or social identity

### partnership
As defined in the [FCA Handbook](https://www.handbook.fca.org.uk/handbook/glossary/G843.html):
> (in accordance with section 417(1) of the Act (Definitions)) any partnership, including a partnership constituted under the law of a country or territory outside the United Kingdom, but not including a limited liability partnership.

### sme
The definition of an SME is based on a set of criteria, while in theory it is possible for this to be a dynamic field based on other relevant data provided (employee count, turnover etc.), often times the data is unavailable or not current and hence firm may wish to identify SMEs directly.
In this scenario, an SME type will be assumed to comply with the [EU SME Recommendation][sme], further explained in [What is an SME?][sme-what] broadly as:

Company category | Staff headcount | Turnover (or) | Balance sheet total
-----------------|-----------------|---------------|--------------------
Medium-sized     | < 250           | ≤ € 50 m      | ≤ € 43 m            
Small            | < 50            | ≤ € 10 m      | ≤ € 10 m            
Micro            | < 10            | ≤ € 2 m       | ≤ € 2 m 


### other
Other means it is known to **not** be one of the other types. If type is unknown it should just be left blank.

### ccp
As defined in the [FCA Handbook](https://www.handbook.fca.org.uk/handbook/glossary/G2979.html) 
> A legal person that interposes itself between the counterparties to the contracts traded on one or more financial markets, becoming the buyer to every seller and the seller to every buyer, as defined in article 2(1) of EMIR.

### financial
Article 411 of the [CRR][crr]:
> financial customer means a customer that performs one or more of the activities listed in Annex I to Directive 2013/36/EU as its main business, or is one of the following:
> (a) a credit institution;
>
> (b) an investment firm;
>
> (c) an SSPE;
>
> (d) a CIU;
>
> (e) a non-open ended investment scheme;
>
> (f) an insurance undertaking;
>
> (g) a financial holding company or mixed-financial holding company.
>
> 'financial sector entity' means any of the following:
> (a) an institution;
>
> (b) a financial institution;
>
> (c) an ancillary services undertaking included in the consolidated financial situation of an institution;
>
> (d) an insurance undertaking;
>
> (e) a third-country insurance undertaking;
>
> (f) a reinsurance undertaking;
>
> (g) a third-country reinsurance undertaking;
>
> (h) an insurance holding company;
>
> (i) a mixed-activity holding company
>
> (j) a mixed-activity insurance holding company as defined in point (g) of Article 212(1) of Directive 2009/138/EC;
>
> (k) an undertaking excluded from the scope of Directive 2009/138/EC in accordance with Article 4 of that Directive;
>
> (l) a third-country undertaking with a main business comparable to any of the entities referred to in points (a) to (k);

### mdb
Multilateral Development Banks are defined in the [CRR][crr] Article 117 as:
> The Inter-American Investment Corporation, the Black Sea Trade and Development Bank, the Central American Bank for Economic Integration and the CAF-Development Bank of Latin America shall be considered multilateral development banks.
> ...
> (a) the International Bank for Reconstruction and Development;
>
> (b) the International Finance Corporation;
>
> (c) the Inter-American Development Bank;
>
> (d) the Asian Development Bank;
>
> (e) the African Development Bank;
>
> (f) the Council of Europe Development Bank;
>
> (g) the Nordic Investment Bank;
>
> (h) the Caribbean Development Bank;
>
> (i) the European Bank for Reconstruction and Development;
>
> (j) the European Investment Bank;
>
> (k) the European Investment Fund;
>
> (l) the Multilateral Investment Guarantee Agency;
>
> (m) the International Finance Facility for Immunisation;
>
> (n) the Islamic Development Bank.

### intl_org
International Organisations are defined in [CRR][crr] Article 118:
> (a) the Union;
>
> (b) the International Monetary Fund;
>
> (c) the Bank for International Settlements;
>
> (d) the European Financial Stability Facility;
>
> (e) the European Stability Mechanism;
>
> (f) an international financial institution established by two or more Member States, which has the purpose to mobilise funding and provide financial assistance to the benefit of its members that are experiencing or threatened by severe financing problems.

### corporate
An organisation with government approval to conduct business (or other activities).

### sovereign  
As defined in the [FCA handbook](https://www.handbook.fca.org.uk/handbook/glossary/G2971.html), a sovereign is:

>(a) the EU; or
>
>(b) a Member State including a government department, an agency, or a special purpose vehicle of the Member State; or
>
>(c) in the case of a federal Member State, a member of the federation; or
>
>(d) a special purpose vehicle for several Member States; or
>
>(e) an international financial institution established by two or more Member States which has the purpose of mobilising funding and provide financial assistance to the benefit of its members that are experiencing or threatened by severe financing problems; or
>
>(f) the European Investment Bank.

### central_bank
A **central bank** is often a nationalised institution in charge of the production and distribution of money and credit in the system it resides over. It is usually responsible for monetary policy and the regulation of member banks.

### regional_govt
A **regional government** is a government entity that only has control on a specific geographic area. 

### central_govt
A **central government** is the government of a nation-state. While some countries may have **regional governments** that operate autonomously, the **central goverment** is the governing system that is concerned with issues that affect the entire nation.

### pse  
A public sector entity is defined in the [FCA handbook](https://www.handbook.fca.org.uk/handbook/glossary/G2242.html) as any of the following:

>(a) non-commercial administrative bodies responsible to central governments, regional governments or local authorities; or
>
>(b) authorities that exercise the same responsibilities as regional and local authorities; or
>
>(c) non commercial undertakings owned by central governments that have explicit guarantee arrangements; or
>
>(d) self administered bodies governed by law that are under public supervision.

### credit_institution
Credit institution is defined in Article 4 of [CRR][crr]:
> (1) 'credit institution' means an undertaking the business of which is to take deposits or other repayable funds from the public and to grant credits for its own account

### promotional_lender
A promotional lender is defined by the EU [here][lcr] Article 10.1(e):
> (ii) any credit institution whose purpose is to advance the public policy objectives of the Union or of the central or regional government or local authority in a Member State predominantly through the provision of promotional loans on a non-competitive, not for profit basis, provided that at least 90 % of the loans that it grants are directly or indirectly guaranteed by the central or regional government or local authority and that any exposure to that regional government or local authority, as applicable, is treated as an exposure to the central government of the Member State in accordance with Article 115(2) of Regulation (EU) No 575/2013;

### investment_firm
Investment firm is defined in the [FCA Handbook](https://www.handbook.fca.org.uk/handbook/glossary/G596.html) as:
>(1) any person whose regular occupation or business is the provision of one or more investment services to third parties and/or the performance of one or more investment activities on a professional basis.
[Note: article 4(1)(1) of MiFID]
>
>(2) (in REC) a MiFID investment firm, or a person who would be a MiFID investment firm if it had its head office in the EEA.
>
>(3) (in IFPRU and BIPRU 12) has the meaning in article 4(1)(2) of the EU CRR.
>
>(4) (in GENPRU (except GENPRU 3) and BIPRU (except BIPRU 12) any of the following:
>(a) a firm in (3); and
>(b) a BIPRU firm.
>
>(5) (in SYSC 19A(IFPRU Remuneration Code)) a firm in (3).
>
>(6)	(in SYSC 19D (Dual-regulated firms Remuneration Code)) a firm in (3) that is a UK designated investment firm.

### local_firm
Local firm is defined by the EU [here][lcr] Article 4(1)(4):
> 'local firm' means a firm dealing for its own account on markets in financial futures or options or other derivatives and on cash markets for the sole purpose of hedging positions on derivatives markets, or dealing for the accounts of other members of those markets and being guaranteed by clearing members of the same markets, where responsibility for ensuring the performance of contracts entered into by such a firm is assumed by clearing members of the same markets

### sspe
A securitisation special purpose entity is defined in the [FCA Handbook](https://www.handbook.fca.org.uk/handbook/glossary/G2277.html) as: 

>(1) (in accordance with Article 4(44) of the Banking Consolidation Directive (Definitions) and for the purposes of BIPRU) a corporation, trust or other entity, other than a credit institution, organised for carrying on a securitisation or securitisations (within the meaning of paragraph (2) of the definition of securitisation), the activities of which are limited to those appropriate to accomplishing that objective, the structure of which is intended to isolate the obligations of the SSPE from those of the originator, and the holders of the beneficial interests in which have the right to pledge or exchange those interests without restriction.
>
>(2) (in MIPRU) a corporation, trust or other entity that has the following characteristics:
> (a) it is organised for carrying on a securitisation or securitisations (within the meaning of paragraph (2) of the definition of securitisation);
> (b) its activities are limited to those appropriate to accomplishing such securitisation or securitisations; and
> (c) its structure is intended to isolate its obligations from those of the originator.

### ciu
A collective investment undertaking is defined by the EU [here][lcr] Article 4(1)(7):
> 'collective investment undertaking' or 'CIU' means a UCITS as defined in Article 1(2) of Directive 2009/65/EC of the European Parliament and of the Council of 13 July 2009 on the coordination of laws, regulations and administrative provisions relating to undertakings for collective investment in transferable securities (UCITS) (21), including, unless otherwise provided, third-country entities which carry out similar activities, which are subject to supervision pursuant to Union law or to the law of a third country which applies supervisory and regulatory requirements at least equivalent to those applied in the Union, an AIF as defined in Article 4(1)(a) of Directive 2011/61/EU of the European Parliament and of the Council of 8 June 2011 on Alternative Investment Fund Managers (22), or a non-EU AIF as defined in Article 4(1)(aa) of that Directive;

### ceis
*needs definition*

### insurer
The [FCA Handbook](https://www.handbook.fca.org.uk/handbook/glossary/G569.html?date=2015-12-31) defines an **insurer** as: 
>a firm with permission to effect or carry out contracts of insurance (other than a UK ISPV ).
Where [insurance](https://www.handbook.fca.org.uk/handbook/glossary/G218.html?date=2015-12-31) consists of:
>(1) (in relation to a specified investment) the investment, specified in article 75 of the Regulated Activities Order (Contracts of insurance), which is rights under a contract of insurance in (2).
>
>(2) (in relation to a contract) (in accordance with article 3(1) of the Regulated Activities Order (Interpretation)) any contract of insurance which is a long-term insurance contract or a general insurance contract, including:
>
> (a) fidelity bonds, performance bonds, administration bonds, bail bonds, customs bonds or similar contracts of guarantee, where these are:
>
>   (i) effected or carried out by a person not carrying on a banking business;
>
>   (ii) not effected merely incidentally to some other business carried on by the person effecting them; and
>
>   (iii) effected in return for the payment of one or more premiums;
>
> (b) tontines;
>
> (c) capital redemption contracts or pension fund management contracts, where these are effected or carried out by a person who:
>
>   (i) does not carry on a banking business; and
>
>   (ii) otherwise carries on the regulated activity of effecting or carrying out contracts of insurance;
>
> (d) contracts to pay annuities on human life;
>
> (e) contracts of a kind referred to in article 2(2)(e) of the Consolidated Life Directive (Collective insurance etc); and
>
> (f) contracts of a kind referred to in article 2(3) of the Consolidated Life Directive (Social insurance);
>
>but not including a funeral plan contract (or a contract which would be a funeral plan contract but for the exclusion in article 60 of the Regulated Activities Order (Plans covered by insurance or trust arrangements)); in this definition, "annuities on human life" does not include superannuation allowances and annuities payable out of any fund applicable solely to the relief and maintenance of persons engaged, or who have been engaged, in any particular profession, trade or employment, or of the dependants of such persons.

### financial_holding
A financial holding copmany is defined by the EU [here][lcr] Article 4(1)(20):
> (20) 'financial holding company' means a financial institution, the subsidiaries of which are exclusively or mainly institutions or financial institutions, at least one of such subsidiaries being an institution, and which is not a mixed financial holding company;

### other_financial
Any other type to be classified as financial but not one of the other types witin financial.

### pic
A financial holding copmany is defined by the EU [here](http://eur-lex.europa.eu/eli/reg_del/2015/61/oj) Article 3:
> 'personal investment company' (‘PIC’) means an undertaking or a trust whose owner or beneficial owner, respectively, is a natural person or a group of closely related natural persons, which was set up with the sole purpose of managing the wealth of the owners and which does not carry out any other commercial, industrial or professional activity. The purpose of the PIC may include other ancillary activities such as segregating the owners' assets from corporate assets, facilitating the transmission of assets within a family or preventing a split of the assets after the death of a member of the family, provided these are connected to the main purpose of managing the owners' wealth;

### credit_union
A **credit union** is defined by the [FCA](https://www.fca.org.uk/firms/credit-unions) as:
>A credit union is a financial co-operative owned by its members.
>The services that credit unions can offer include:
> deposit-taking
>
> savings
>
> lending
These services are regulated activities.

### deposit_broker
A **deposit broker** can be an individual or a firm that facilitates the placement of deposits with insured depository institutions. Deposit brokers offer investors an assortment of fixed-term investment products, which earn low-risk returns.

# Loan
### trade_finance
From [CRR][crr] definitions (80):
> Trade finance means financing, including guarantees, connected to the exchange of goods and services through financial products of fixed short-term maturity, generally of less than one year, without automatic rollover;

### trade_credit_insurance
From the [EBA's][eba-nsfr-report] report on the NSFR, section 6.2.1 outlines what **trade credit insurance** is:
> A seller providing trade credit is exposed to the credit risk of the buyer. Trade credit insurance provides the seller with protection against the risk of non-payment by the buyer. The nonpayment may be due to the insolvency of the buyer or, in an international trade, due to political risks that prevent payment.

### letter_of_credit
From the [EBA's][eba-nsfr-report] report on the NSFR, section 6.2.2, a **letter of credit** is:
> When goods are traded, the seller and the buyer need to agree on the process of how to pay for the goods. While the buyer may be reluctant to prepay for the traded goods, the seller may also be unwilling to ship the goods before payment is made. In this situation, a bank can intermediate between the trading partners by providing an import letter of credit (L/C) to the buyer of the goods, which guarantees payment to the seller. 
> A L/C is a contingent liability and payment is only made by the bank to the seller from funds in the buyer’s account when the documentation of shipping is presented.

### project_finance
As defined in [Supervisory Reporting][sup-rep] part 2(5)(41)(l):
> 'Project finance loans' include loans that are recovered solely from the income of the projects financed by them.

### auto
As outlined in [LCR][lcr] Article 13(2)(g)(iv):
> loans or leases for the financing of motor vehicles or trailers (see Article 3 of Directive 2007/46/EC).
> agricultural or forestry tractors (see Directive 2003/37/EC)
> tracked vehicles (see Directive 2007/46/EC)
> Such loans or leases may include ancillary insurance and service products or additional vehicle parts, and in the case of leases, the residual value of leased vehicles.

### personal
As outlined in [LCR][lcr] Article 13(2)(g)(v):
> loans and credit facilities to individuals resident in a Member State for personal, family or household consumption purposes.

### commercial
As outlined in [LCR][lcr] Article 13(2)(g)(iii):
> commercial loans, leases and credit facilities to undertakings established in a Member State to finance capital expenditures or business operations other than the acquisition or development of commercial real estate

### commercial_property
This includes commercial loans or mortgages that do not fall under **commercial** due to their real estate connection and do not classify as **mortgage** either due to the customer not being an individual or the occupation of the property not being residential.

### liquidity_facility
A **liquidity_facility** means the securitisation position arising from a contractual agreement to provide funding to ensure timeliness of cash flows to investors, as outlined in Article 242(3) in [CRR][crr].

### margin
**Margin** is defined in [LCR][lcr] Article 3(12):
> margin loans means collateralised loans extended to customers for the purpose of taking leveraged trading positions.

### mortgage
A **mortgage** is a residential loan to a individuals secured with a one-to-one correspondence to land or property.

As outlined in [LCR][lcr] Article 13(2)(g)(i)
> loans secured with a first-ranking mortgage granted to individuals for the acquisition of their main residence

### credit_card
A **credit_card** is credit facility typically secured by a deposit account or equity in the borrower's property.

### credit_facility, multiccy_facility
From Annex I of the [CRR][crr], credit facilities are:
> agreements to lend, purchase securities, provide guarantees or acceptance facilities

### nostro
Nostro loans are the firm's accounts at other financial institutions which are in effect loans to other firms. Nostros are used in the context of correspondent banking operations which are described by the [ECB](https://www.ecb.europa.eu/paym/t2/shared/pdf/target2_glossary.pdf):
> Correspondent banking: an arrangement under which one credit institution provides payment and other services to another credit institution. Payments through correspondents are often executed through reciprocal accounts (nostro and loro accounts) to which standing credit lines may be attached. Correspondent banking services are primarily provided across international boundaries but are also known as agency relationships in some domestic contexts. 
> A loro (vostro) account is the term used by a correspondent to describe an account held on behalf of a foreign credit institution; the foreign credit institution would in turn regard this account as its nostro account.

### other
Other refers to a type of security not covered by the above. If you find yourself using this often, please [contribute][contributing].


# Security

```
├── equity
│   ├── share
│   │   └── preference_share
│   └── share_agg
├── debt
│   ├── bond
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
A **cash** or cash-equivalent security such as a securitisation of cash deposits. Within [Finrep Annex V part (2)(1)(1.1)(1)](https://www.eba.europa.eu/documents/10180/359626/Annex+V_Instructions_FINREP.docx/26727402-6339-4c33-bb5a-d8e659c27371):
> "Cash on hand" includes holdings of national and foreign banknotes and coins in circulation that are commonly used to make payments.

### equity
This is a "catch all" term for equity instruments such as *share*, *share_agg* to be used when further granularity is not available or not needed.

### share, share_agg 
Denotes if the security is a share (stock) or represents an aggregate for a portfolio or package of shares.

### preference_share
The [FCA](https://www.handbook.fca.org.uk/handbook/glossary/G1587.html) defines a **preference share** as:
> A share conferring preference as to income or return of capital which does not form part of the equity share capital of a company

### debt
This is a "catch all" term for debt of any kind, *bond*, *bond_amortising*, *index_linked_gilt*, *covered_bond*, *abs*, *residential_mbs*, *non_residential_mbs*, *frn*, *govt_gteed_frn*, to be used when further granularity is not available or not needed.

### bond
A **bond** is a type of loan whereby an investor lends money to an entity for a defined period of time at a fixed or floating interest rate. 

### covered_bond
From the [LCR][lcr] Introduction (8):
> Covered bonds are debt instruments issued by credit institutions and secured by a cover pool of assets which typically consist of mortgage loans or public sector debt to which investors have a preferential claim in the event of default. Their secured nature and certain additional safety features, such as the requirement on the issuer to replace non-performing assets in the cover pool and maintain the cover pool at a value exceeding the par value of the bonds (‘asset coverage requirement’), have contributed to make covered bonds relatively low-risk, yield-bearing instruments with a key funding role in mortgage markets of most Member States. In certain Member States outstanding covered bond issuance exceeds the pool of outstanding government bonds. Certain covered bonds of credit quality step 1, in particular, exhibited an excellent liquidity performance during the period from 1 January 2008 to 30 June 2012 analysed by the EBA in its report. Nevertheless the EBA recommended treating these covered bonds as level 2A assets to align with BCBS standards. However, in the light of the considerations made above about their credit quality, liquidity performance and role in the funding markets of the Union, it is appropriate for these credit quality step 1 covered bonds to be treated as level 1 assets. In order to avoid excessive concentration risks and unlike other level 1 assets, the holdings of credit quality step 1 covered bonds in the liquidity buffer should be subject to a 70 % cap of the overall buffer, a minimum 7 % haircut and to the diversification requirement.

### emtn, mtn
A Euro medium-term note is a medium-term (less than 5 years), flexible debt instrument that is traded and issued outside of the US and Canada. A medium-term note is the same but is traded in the US and Canada.

### commercial_paper
Commercial paper is an unsecured promissory note with a fixed maturity of, typically, not more than 270 days.

### cd
A certificate of deposit is also a promissory note, however can only be issued by a bank. It has a fixed maturity and specified fixed interest rate.

### struct_note
The [FCA](https://www.fca.org.uk/consumers/structured-products) defines structured notes as:
> a type of fixed-term investment where the amount you earn depends on the performance of a specific market (such as the FTSE 100) or specific assets (such as shares in individual companies)

### spv_mortgages, spv_other
A special purpose vehicle is a separate legal entity created to fulfil a certain purpose for the parent.

### abs
An asset-backed security is a security whose income payments and hence value are derived from and collateralised (or "backed") by a specified pool of underlying assets. The pool of assets is typically a group of small and illiquid assets which are unable to be sold individually. Pooling the assets into financial instruments allows them to be sold to general investors, a process called securitisation. This allows the risk of investing in the underlying assets to be diversified because each security will represent a fraction of the total value of the diverse pool of underlying assets. The pools of underlying assets can include common payments from credit cards, auto loans, and mortgage loans, to esoteric cash flows from aircraft leases, royalty payments and movie revenues.

### rmbs
A residential mortgage-backed security (a subclass of an ABS).

### rmbs_trans
This type value is in order to indicate whether the security is subject to transitional provisions for securitisations backed by residential loans:  
[LCR][lcr] Article 37:
> 1.   By derogation from Article 13, securitisations issued before 1 October 2015, where the underlying exposures are residential loans as referred to in point (g)(i) of Article 13(2), shall qualify as Level 2B assets if they meet all the requirements set out in Article 13 other than the loan-to-value or loan-to-income requirements set out in that point (g)(i) of Article 13(2).

> 2.   By derogation from Article 13, securitisations issued after 1 October 2015, where the underlying exposures are residential loans as referred to in point (g)(i) of Article 13(2) that do not meet the average loan-to-value or the loan-to-income requirements set out in that point, shall qualify as Level 2B assets until 1 October 2025, provided that the underlying exposures include residential loans that were not subject to a national law regulating loan-to-income limits at the time they were granted and such residential loans were granted at any time prior to 1 October 2015.

### cmbs
A commercial mortgage-backed security (a subclass of an abs).

### frn
A floating-rate note is defined in the [Money Market Statistics Regulation][mm-stat] in Annex II as:
> A debt instrument for which the periodic interest payments are calculated on the basis of the value, i.e. through fixing of an underlying reference rate such as Euribor on predefined dates known as fixing dates, and which has a maturity of not more than one year.
> note: "one year" is defined as transactions with a maturity date of not more than 397 days after the trade date

### govt_gteed_frn
A government guaranteed floating-rate note.

### cb_reserve 
As defined in [Finrep Annex V part (2)(1)(1.1)(2)](https://www.eba.europa.eu/documents/10180/359626/Annex+V_Instructions_FINREP.docx/26727402-6339-4c33-bb5a-d8e659c27371)
> include balances receivable on demand at central banks.

### cash_ratio_deposit
The [BofE](http://www.bankofengland.co.uk/statistics/Documents/faq/crds.pdf) defines this as:
> non-interest bearing deposits lodged with the Bank of England by eligible institutions (ie. banks and building societies), who have reported average eligible liabilities (ELs) of over £600 million over a calculation period. The level of each institution's CRD is currently calculated twice-yearly (currently in May and November) at 0.18% of average ELs, over the previous six end-calendar months, in excess of £600mn. The value bands and ratios were specified by HM Treasury in the Cash Ratio Deposits (Value Bands and Ratios) Order (2013 No 1189).

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
├── vostro
├── prepaid_card
├── debit_card
├── credit_card
└── other
```

### call
A call account is defined in the [Money Market Statistics Regulation][mm-stat] in Annex II as:
> A debt instrument in which the issuer has a call option, i.e. an option to redeem the instrument early, with a final repayment date of not more than one year from the date of issuance.

### cd
A deposit account purely holding certificates of deposit (see *cd* *Security* **type**)

### prepaid_card
From the [Interchange Fees for Card-based Payments Regulation][card-fees] Article 2(35):
> prepaid card means a category of payment instrument on which electronic money, as defined in point 2 of Article 2 of Directive 2009/110/EC, is stored.
NB. see **credit_card**

### debit_card
From the [Interchange Fees for Card-based Payments Regulation][card-fees] Article 2(33) and (4):
> debit card means a category of payment instrument that enables the payer to initiate a debit card transaction excluding those with prepaid cards;
> debit card transaction means a card-based payment transaction, including those with prepaid cards that is not a credit card transaction;

NB. see **credit_card**

### credit_card
A credit card is typically an off-balance sheet, contingent funding obligation whereby a customer has a certian credit limit and may borrow funds at any point, up to that limit, similar to a card-based credit facility.

The [Interchange Fees for Card-based Payments Regulation][card-fees] states that:
> There are two main types of credit cards available on the market. With deferred debit cards, the total amount of transactions is debited from the cardholder account at a pre-agreed specific date, usually once a month, without interest to be paid. With other credit cards, the cardholder can use a credit facility in order to reimburse part of the amounts due at a later date than specified, together with interest or other costs.

A credit card is then defined in Article 2 (34) and (5) as:
> credit card means a category of payment instrument that enables the payer to initiate a credit card transaction;
> credit card transaction means a card-based payment transaction where the amount of the transaction is debited in full or in part at a pre agreed specific calendar month date to the payer, in line with a prearranged credit facility, with or without interest;

### current (checking, demand)
Any transactional account .

### internet_only
An internet-only account is one that is offered and only accessible via the internet. The [FCA][fca-internet] defines the internet in their handbook as:
> a unique medium for communicating financial promotions as it provides easy access to a very wide audience. At the same time, it provides very little control over who is able to access the financial promotion.

The distinction here linked to financial promotions suggests that internet-only accounts are sold and managed through a higher risk channel and therefore should be regulated spearately to other accounts.

### isa
An ISA is an individual savings account which is a scheme of investment satisfying the conditions prescribed in the UK's [ISA Regulations][uk-isa].

### money_market
A money market account is an interest-bearing account that typically pays a higher interest rate than a savings account, and which provides the account holder with limited check-writing ability. 

Money market accounts are accounts where the customer's money has been invested in the "money markets" either directly in money market instruments or money market funds which are described in the [2013 Proposal for the Regulation of Money Market Funds][mmf-prpposal] as providing a key component of corporate banking:
> On the demand side, MMFs offer a short-term cash management tool that provides a high degree of liquidity, diversification, stability of value combined with a market-based yield. MMFs are mainly used by corporations seeking to invest their excess cash for a short time frame, for example until a major expenditure, such as the payroll, is due.

Money market deposits are mentioned in association with definitions of cash in that they represent *claims for the repayment of money*.

### vostro (loro)
Nostro and vostro (loro) accounts are used in the context of correspondent banking operations which are described in [ECB guidelines on monetary policy instruments][ecb-guidelines] from 2003:
> Correspondent banking: an arrangement under which one credit institution provides payment and other services to another credit institution. Payments through correspondents are often executed through reciprocal accounts (nostro and loro accounts) to which standing credit lines may be attached. Correspondent banking services are primarily provided across international boundaries but are also known as agency relationships in some domestic contexts. 
> A loro account is the term used by a correspondent to describe an account held on behalf of a foreign credit institution; the foreign credit institution would in turn regard this account as its nostro account.

### savings
An account subject to the European Council [Directive on taxation of savings][eur-savings-tax]. A savings account essentially does not allow the customer to use funds in the account as a "medium of exchange" such as writing checks or for making ATM withdrawals. Hence, funds are typically not callable immediately and/or incur a withdrawal penalty such as loss of interest.
In the US, [Regulation D][reg-d] uses the characteristics of the 'reservation of right' and 'convenient' withdrawals to describe savings accounts:
> In order to classify an account as a 'savings deposit,' the institution must in its account agreement with the customer reserve the right at any time to require seven days’ advance written notice of an intended withdrawal. In practice, this right is never exercised, but the institution must nevertheless reserve that right in the account agreement. In addition, for an account to be
classified as a 'savings deposit,' the depositor may make no more than six 'convenient' transfers or withdrawals per month from the account.

### time_deposit
A fixed-term deposit with a specific [**end_date**][end-date].
The [US Regulation D][reg-d] describes time deposits as having the following characteristics:
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

The [EC Collateral Directive][arrangement] states:
> The assets can be provided: either by transfer of full ownership from a collateral provider to a collateral taker; or by the transfer of possession from a collateral provider to a collateral taker under a security right (e.g. pledge, charge or lien), where the full ownership of the assets remains with the collateral provider.


[crr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013R0575

[card-fees]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2015.123.01.0001.01.ENG

[lcr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0061

[mlar]: http://www.bankofengland.co.uk/pra/documents/regulatorydata/mlar/sup_chapter16_annex19bg_20120401.pdf

[sftr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015R2365

[contributing]: https://github.com/suadelabs/fire/blob/master/CONTRIBUTING.md

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
[end-date]: https://github.com/suadelabs/fire/blob/master/documentation/properties/end_date.md
[reg-d]: http://www.federalreserve.gov/boarddocs/supmanual/cch/int_depos.pdf
[eba-nsfr-report]: https://www.eba.europa.eu/documents/10180/983359/EBA-Op-2015-22+NSFR+Report.pdf
[fca-covered-bond]: https://www.handbook.fca.org.uk/handbook/glossary/G2083.html
[ucits]: http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ:L:2009:302:0032:0096:en:PDF
[eu-covered-bonds-info]: http://ec.europa.eu/finance/investment/legal_texts/index_en.htm
[sup-rep]: http://publications.europa.eu/resource/cellar/37c79802-fe90-11e3-831f-01aa75ed71a1.0006.03/DOC_1
