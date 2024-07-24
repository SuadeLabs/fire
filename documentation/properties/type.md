---
layout:     property
title:      "type"
schemas:    [account, agreement, collateral, customer, derivative_cash_flow, derivative, entity, guarantor, issuer, loan_cash_flow, loan_transaction, loan, security]
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
│   ├── charity
│   │   └── community_charity
│   └── sme
│       └── supported_sme
├── financial
│   ├── credit_institution
│   │   ├── merchant_bank
│   │   ├── building_society
│   │   ├── state_owned_bank
│   │   └── promotional_lender
│   │       ├── promo_fed_reserve
│   │       └── promo_fed_home_loan
│   ├── investment_firm
│   │   ├── fund
│   │   ├── private_fund
│   │   │   ├── hedge_fund
│   │   │   └── private_equity_fund
│   │   ├── mmkt_fund
│   │   └── real_estate_fund
│   ├── pension_fund
│   ├── ciu
│   ├── sspe
│   ├── pic
│   ├── insurer
│   ├── financial_holding
│   ├── pmi
│   ├── unregulated_financial
│   └── other_financial
├── ccp
│   └── qccp
├── central_bank
├── mdb
├── credit_union
├── deposit_broker
├── pse
│   ├── local_authority
│   ├── regional_govt
│   ├── central_govt
│   ├── public_corporation
│   ├── social_security_fund
│   ├── statutory_board
│   └── other_pse
├── sovereign
├── intl_org
├── export_credit_agency
├── unincorporated_biz
└── other
```

### individual
Individual is a UK specific definition which is slightly broader than a natural person and defined in the [FCA Handbook Glossary][fca-indiv] under individual:
> (a) a natural person; or
> (b) a partnership consisting of two or three persons not all of whom are bodies corporate; or
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

### supported_sme
An SME with special treatment under the capital adequacy rules, invoking a special multiplier for RWAs

### other
Other means it is known to **not** be one of the other types. If type is unknown it should just be left blank.

### ccp
As defined in Article 2(1) of [EMIR][emir] and the [FCA Handbook](https://www.handbook.fca.org.uk/handbook/glossary/G2979.html):
> "CCP" means a legal person that interposes itself between the counterparties to the contracts traded on one or more financial markets, becoming the buyer to every seller and the seller to every buyer

From the [US FDIC Regulatory Capital Rules](https://www.fdic.gov/regulations/laws/federal/2013/2013-09-10_final-rule-interim.pdf):
> Central counterparty (CCP) means a counterparty (for example, a clearing house) that facilitates trades between counterparties in one or more financial markets by either guaranteeing trades or novating contracts.

### qccp
Article 4 (88) of the [CRR][crr]:
> Qualifying central counterparty (QCCP) means a central counterparty that has been either authorised in accordance with Article 14 of Regulation (EU) No 648/2012 or recognised in accordance with Article 25 of that Regulation

### financial
Article 411 of the [CRR][crr]:
> financial customer means a customer that performs one or more of the activities listed in Annex I to Directive 2013/36/EU as its main business, or is one of the following:
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
> (m) a building society

### unregulated_financial
In the Basel guidelines for Credit Risk under exposures to securties firms and financial institutions, [CRE 20.40](https://www.bis.org/basel_framework/chapter/CRE/20.htm?tldate=20220101&inforce=20230101&published=20201126#:~:text=provided%20that%20these,their%20own%20jurisdictions.) it allows for these exposures to be treated like exposures to banks on the basis that they fall under the same regulated regime (and similar supervisory requirements) that banks in that jurisdiction are subject to.
So 'unregulated_financial' is to clearly define those firms *that do not* meet these regulatory requirements.

As defined by OSFI chapter 4, P56 and chapter 5, P68:
> Unregulated financial institutions are institutions that are not supervised by a regulator, and therefore NOT subject to prudential standards or any level of supervision equivalent to those applied to banks under the Basel III framework (including, in particular, capital and liquidity requirements).

Unregulated financial institutions would be not be qualified for "bank" treatment under standardized and/or subject to 1.25 correlation factor under IRB.

### mdb
Multilateral Development Banks are defined in the [CRR][crr] Article 117 as:
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

### export_credit_agency
An official export credit agency facilitates international exports, and must be one of the entities listed in this document, maintained by the oecd: https://www.oecd.org/trade/topics/export-credits/documents/links-of-official-export-credit-agencies.pdf

### corporate
An organisation with government approval to conduct business (or other activities).

### sovereign
As defined in the [FCA handbook](https://www.handbook.fca.org.uk/handbook/glossary/G2971.html), a sovereign is:

>(a) the EU; or
>(b) a Member State including a government department, an agency, or a special purpose vehicle of the Member State; or
>(c) in the case of a federal Member State, a member of the federation; or
>(d) a special purpose vehicle for several Member States; or
>(e) an international financial institution established by two or more Member States which has the purpose of mobilising funding and provide financial assistance to the benefit of its members that are experiencing or threatened by severe financing problems; or
>(f) the European Investment Bank.

### central_bank
A **central bank** is often a nationalised institution in charge of the production and distribution of money and credit in the system it resides over. It is usually responsible for monetary policy and the regulation of member banks.

### regional_govt
A **regional government** is a government entity that only has control on a specific geographic area.

### central_govt
A **central government** is the government of a nation-state. While some countries may have **regional governments** that operate autonomously, the **central goverment** is the governing system that is concerned with issues that affect the entire nation.

### local_authority


### pse
A public sector entity is defined in the [FCA handbook](https://www.handbook.fca.org.uk/handbook/glossary/G2242.html) as any of the following:

>(a) non-commercial administrative bodies responsible to central governments, regional governments or local authorities; or
>(b) authorities that exercise the same responsibilities as regional and local authorities; or
>(c) non commercial undertakings owned by central governments that have explicit guarantee arrangements; or
>(d) self administered bodies governed by law that are under public supervision.

### other_pse


### statutory_board
>A specific distinction for Singaporean public sector entities. The statutory boards of the Singapore Government are organisations that have been given autonomy to perform an operational function by legal statutes passed as Acts in parliament. The statutes define the purpose, rights and powers of the authority. They usually report to one specific ministry.
A more comprehensive list can be found here:
[Singaporean Statutory Boards][sg-stat-boards]


### public_corporation
In the UK, public corporations are corporate bodies, sometimes with plc or Ltd in their title. Ownership by government
may be total, as in the case of those corporations established by Act of Parliament, or through majority share-holdings.
Public control is over broad aspects of policy; public corporations are free to manage their day to day operations independently.
Trust ports in Northern Ireland and ports belonging to public corporations continue to be classed as ‘public corporations’, as do certain airport companies, which were set up by local authorities under the terms of the 1986 Airports Act.
A list of these entities can be found at www.ons.gov.uk/economy/nationalaccounts/uksectoraccounts/datasets/publicsectorclassificationguide.

### social_security_fund
Social security funds are social insurance programmes covering the community as a whole or large sections of the community that are imposed and controlled by a government unit. They generally involve compulsory contributions by employees or employers or both, and the terms on which benefits are paid to recipients are determined by a government unit.
Social security funds have to be distinguished from other social insurance programmes which are determined by mutual agreement between individual employers and their employees.
Note: This item corresponds to HF.1.2 in the ICHA-HF classification of health care financing (see SHA, chapters 6 and 11).
Source Publication: OECD Health Data 2001: A Comparative Analysis of 30 Countries, OECD, Paris, 2001, data sources, definitions and methods.
Cross References: Social security funds - SNA

### credit_institution
Credit institution is defined in Article 4 of [CRR][crr]:
> (1) 'credit institution' means an undertaking the business of which is to take deposits or other repayable funds from the public and to grant credits for its own account

### promotional_lender
A promotional lender is defined by the EU [here][lcr] Article 10.1(e):
> (ii) any credit institution whose purpose is to advance the public policy objectives of the Union or of the central or regional government or local authority in a Member State predominantly through the provision of promotional loans on a non-competitive, not for profit basis, provided that at least 90 % of the loans that it grants are directly or indirectly guaranteed by the central or regional government or local authority and that any exposure to that regional government or local authority, as applicable, is treated as an exposure to the central government of the Member State in accordance with Article 115(2) of Regulation (EU) No 575/2013;

This would also include any national legislated government programmes. For example, in OSFI BCAR template schedule 40.120 and Chapter 4, P77, equity issued related by any level of government related to programmes that provide significant subsidies for the investment to the institution and involve government oversight and restrictions on the equity investments.

### promo_fed_reserve
Equity issued, guaranteed or related to the US Federal Reserve Bank that obtain favour risk weight treatment.  Reference OSFI BCAR template schedule 40.120.

### promo_fed_home_loan
Equity issued, guaranteed or related to US Federal Home Loan Bank that obtain favour risk weight treatment.  Reference OSFI BCAR template schedule 40.120.


### merchant_bank
**merchant bank** means:
> a merchant bank approved under section 28 of the Monetary Authority of Singapore Act (Cap. 186);

### state_owned_bank
Financial institutions where there is majority ownership or control by a government or state.

### investment_firm
*Investment firm* is defined under the Markets in Financial Instruments Directive (MiFID) Article 4(1):
> any legal person whose regular occupation or business is the provision of one or more investment services to third parties and/or the performance of one or more investment activities on a professional basis.

> Member States may include in the definition of investment firms undertakings which are not legal persons, provided that:
(a) their legal status ensures a level of protection for third parties' interests equivalent to that afforded by legal persons; and
(b) they are subject to equivalent prudential supervision appropriate to their legal form.
However, where a natural person provides services involving the holding of third party funds or transferable securities, that person may be considered to be an investment firm for the purposes of this Directive and of Regulation (EU) No 600/2014 only if, without prejudice to the other requirements imposed in this Directive, in Regulation (EU) No 600/2014, and in Directive 2013/36/EU, that person complies with the following conditions:
(a) the ownership rights of third parties in instruments and funds must be safeguarded, especially in the event of the insolvency of the firm or of its proprietors, seizure, set-off or any other action by creditors of the firm or of its proprietors;
(b) the firm must be subject to rules designed to monitor the firm's solvency and that of its proprietors;
(c) the firm's annual accounts must be audited by one or more persons empowered, under national law, to audit accounts;
(d) where the firm has only one proprietor, that person must make provision for the protection of investors in the event of the firm's cessation of business following the proprietor's death or incapacity or any other such event.

> Organisational requirements under Article 16 of MiFID 2
An investment firm should:
a) maintain and operate an effective organisational and administrative arrangements to taking all reasonable steps designed to prevent conflicts of interest affecting the interests of its clients;
b) Maintain, operate and review a process for the approval of financial instruments before marketed or distributed to clients, including target market, relevant risks and distribution strategy;
c) review regularly the financial instruments offered;
d) make available appropriate information on the financial instrument and the product approval process, including target market;
e) have in place adequate arrangements to obtain the above information if offers financial instruments that they do not manufacture;
f) take reasonable steps to ensure continuity and regularity in the performance of investment services and activities (appropriate and proportionate system, resources and procedures);
g) ensure it takes reasonable steps to avoid undue operational risk in the case of outsourcing of critical functions (internal control and ability to monitor the firms compliance with all obligations needs to remain at the firm);
h) have sound administrative and accounting procedures, internal control mechanisms, effective procedures for risk assessment and effective control and safeguard arrangements for information processing systems;
i) have sound security mechanisms to guarantee the security and authentication of the means of transfer of information, minimise risk of data corruption and unauthorized access and to prevent information leakage maintaining the confidentiality of the data at all times;
j) arrange for records to be kept of all services, activities and transactions undertaken which are sufficient to enable the competent authority to fulfil its supervisory tasks to ascertain the investment firm has complied with all relevant obligations;
k) records shall include the recording of telephone conversations or electronic communications relate to transactions concluded when dealing on own account and the provision of client order services that relate to the receptions transmission and execution of client orders.

Investment firm is defined in the [FCA Handbook](https://www.handbook.fca.org.uk/handbook/glossary/G596.html) as:
>(1) any person whose regular occupation or business is the provision of one or more investment services to third parties and/or the performance of one or more investment activities on a professional basis.
[Note: article 4(1)(1) of MiFID]
>(2) (in REC) a MiFID investment firm, or a person who would be a MiFID investment firm if it had its head office in the EEA.
>(3) (in IFPRU and BIPRU 12) has the meaning in article 4(1)(2) of the EU CRR.
>(4) (in GENPRU (except GENPRU 3) and BIPRU (except BIPRU 12) any of the following:
>(a) a firm in (3); and
>(b) a BIPRU firm.
>(5) (in SYSC 19A(IFPRU Remuneration Code)) a firm in (3).
>(6) (in SYSC 19D (Dual-regulated firms Remuneration Code)) a firm in (3) that is a UK designated investment firm.

### ciu
A collective investment undertaking is defined by the EU [here][lcr] Article 4(1)(7):
> 'collective investment undertaking' or 'CIU' means a UCITS as defined in Article 1(2) of Directive 2009/65/EC of the European Parliament and of the Council of 13 July 2009 on the coordination of laws, regulations and administrative provisions relating to undertakings for collective investment in transferable securities (UCITS) (21), including, unless otherwise provided, third-country entities which carry out similar activities, which are subject to supervision pursuant to Union law or to the law of a third country which applies supervisory and regulatory requirements at least equivalent to those applied in the Union, an AIF as defined in Article 4(1)(a) of Directive 2011/61/EU of the European Parliament and of the Council of 8 June 2011 on Alternative Investment Fund Managers (22), or a non-EU AIF as defined in Article 4(1)(aa) of that Directive;


### fund
A general term for collective investment vehicles and management companies. For example, those defined under the [US Investment Company Act 1940][inv-co-act] but not qualifying as an EU CIU. There does not appear to be a cross-jurisdictional, unified classification of types of funds


### private_fund
A private fund is a pooled investment vehicle excluded from the definition of an investment company in the [US Investment Company Act 1940][inv-co-act]
[Private Fund](https://www.sec.gov/education/glossary/jargon-z#PEF:~:text=Private%20Equity%20Funds-,Private%20Fund,applicable%20registration%20requirements%20(for%20example%2C%20as%20an%20exempt%20reporting%20adviser).,-Want%20to%20learn)

### private_equity_fund
A private equity fund is a type of private fund distinguished by its objective to take mainly controlling interests in business to actively increase their value. See SEC glossary: [Private Equity Fund glossary](https://www.sec.gov/education/glossary/jargon-z#PEF:~:text=is%20the%20SEC%3F-,Private%20Equity%20Fund,specialize%20in%20making%20minority%20investments%20in%20fast%2Dgrowing%20businesses%20or%20startups,-.%C2%A0%C2%A0%C2%A0)


### hedge_fund
A hedge fund is a type of private fund that generally invests in a diverse range of securities and typically has more flexible investment strategies than mutual funds. Many hedge funds seek to profit by using leverage (borrowing to increase investment exposure as well as risk), short-selling, and other speculative investment practices. [SEC glossary](https://www.sec.gov/education/glossary/jargon-z#PEF:~:text=Hedge%20Fund,speculative%20investment%20practices.)

See also: [SEC Hedge fund bulletin][hedge-fund2]


### real_estate_fund
Real estate funds or [REITS](https://www.investor.gov/introduction-investing/investing-basics/investment-products/real-estate-investment-trusts-reits).


### pension_fund
A pension fund is defined in the [EU Pension Fund Statistical Reporting Requirements Regulation][https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32018R0231#:~:text=%E2%80%98pension%20fund%20(PF,death%20and%20disability.]


### mmkt_fund
Money Market Funds are well defined under the EU legislation for [Money Market Funds][mmfr] (MMFR):
> This Regulation applies to collective investment undertakings that:
(a) require authorisation as UCITS or are authorised as UCITS under Directive 2009/65/EC or are AIFs under Directive 2011/61/EU;
(b) invest in short-term assets; and
(c) have distinct or cumulative objectives offering returns in line with money market rates or preserving the value of the investment.

In other jurisdictions, money market funds are identifiable based on their investments into 'money market instruments' which are typically short-term (< 1 year) and/or undergo regular yield adjustments in line with money markets conditions once per year.

From Directive 2009/65/EC:
> Money market instruments comprise transferable instru­ments which are normally dealt in on the money market rather than on the regulated markets, for example treasury and local authority bills, certificates of deposit, commer­cial papers, medium-term notes and bankers’ acceptances.

### local_firm (inactive)
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

### pmi
Private Mortgage Insurer is financial institution that provides insurance to residential mortgages that may get part of guaranteed amount backed by federal government.  Under OSFI rules, PMI guaranteed amounts may get split between a backstop and a deductiable portion.

Reference:  OSFI Chapter 4, P272-274;  Chapter 5, P146-148


### other_financial
Any other type to be classified as financial but not one of the other types witin financial.


### pic
A financial holding copmany is defined by the EU [here](http://eur-lex.europa.eu/eli/reg_del/2015/61/oj) Article 3:
> 'personal investment company' (‘PIC’) means an undertaking or a trust whose owner or beneficial owner, respectively, is a natural person or a group of closely related natural persons, which was set up with the sole purpose of managing the wealth of the owners and which does not carry out any other commercial, industrial or professional activity. The purpose of the PIC may include other ancillary activities such as segregating the owners' assets from corporate assets, facilitating the transmission of assets within a family or preventing a split of the assets after the death of a member of the family, provided these are connected to the main purpose of managing the owners' wealth;


### credit_union
A **credit union** is defined by the [FCA](https://www.fca.org.uk/firms/credit-unions) as:
>A credit union is a financial co-operative owned by its members.
> The services that credit unions can offer include:
>
> - deposit-taking
> - savings
> - lending
>
> These services are regulated activities.

### deposit_broker
A **deposit broker** can be an individual or a firm that facilitates the placement of deposits with insured depository institutions. Deposit brokers offer investors an assortment of fixed-term investment products, which earn low-risk returns.

### building_society
A financial institution that offers a variety of savings accounts to attract deposits, mainly from the general public, and which specializes in the provision of long-term mortgage loans used to purchase property. They have entered into arrangements with other financial institutions that have enabled them to provide their depositors with limited banking facilities (the use of cheque books and credit cards, for instance) and other financial services, a development that has been given added impetus by the BUILDING SOCIETIES ACT 1986.

### unincorporated_biz
Unincorporated business other than unlimited liability partnerships. Sole traders would fall in this category.

### charity
A non-profit institution.

### community_charity
Charity serving communities and individuals. Includes non-profit institutions serving households.


# Loan
```
├── mortgage
│   ├── reverse_mortgage
│   │   └── q_reverse_mortgage
│   └── mortgage_charter
├── commercial_property
├── personal
├── auto
├── commercial
├── credit_card
│   ├── charge_card
│   └── corporate_card
├── financial_lease
├── heloc
├── trade_finance
├── credit_facility
├── liquidity_facility
├── multiccy_facility
├── nostro
└── other
```

### trade_finance
From [CRR][crr] definitions (80):
> Trade finance means financing, including guarantees, connected to the exchange of goods and services through financial products of fixed short-term maturity, generally of less than one year, without automatic rollover

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

### multiccy_facility
*Needs definition*

### margin
**Margin** is defined in [LCR][lcr] Article 3(12):
> margin loans means collateralised loans extended to customers for the purpose of taking leveraged trading positions.

### mortgage
A **mortgage** is a residential loan to a individuals secured with a one-to-one correspondence to land or property.

As outlined in [LCR][lcr] Article 13(2)(g)(i)
> loans secured with a first-ranking mortgage granted to individuals for the acquisition of their main residence

### q_reverse_mortgage
A **q_reverse_mortgage** is a qualified reverse mortgage which adheres to the stipulations defined in OSFI BCAR Chapter 4 P 116, and therefore qualifies for preferential risk weight treatment

### reverse_mortgage
A **reverse_mortgage** is a non-recourse loan secured by property that has no defined term and no monthly repayment of principal and interest.

As outlined in OSFI BCAR Chapter 4, P 116

### mortgage_charter
From the [UK Gov](https://www.gov.uk/government/publications/mortgage-charter/mortgage-charter#:~:text=A%20new%20deal,contacting%20their%20lender), the **mortgage_charter** is an agreement between UK lenders and the UK Government to help regulated residential mortgage borrowers manage their mortgage during the period of heightened interest rates. This is done by restructuring their mortgages to interest only (for a short period) or extending the maturity of their loans.

### credit_card
A **credit_card** is credit facility typically secured by a deposit account or equity in the borrower's property.

### charge_card
A **charge_card** is a type of credit card that requires the owner to pay the statement balance in full, usually monthly. See common differences with a standard credit card [here](https://www.capitalone.com/learn-grow/money-management/charge-cards-credit-cards/)

### corporate_card
**corporate_card** is an employer-sponsored credit card for use by a company’s employee. The employee is liable to repay the balance in full and the employer is not ultimately responsible for the repayment of credit losses. 

### credit_facility, multiccy_facility
From Annex I of the [CRR][crr], credit facilities are:
> agreements to lend, purchase securities, provide guarantees or acceptance facilities

### heloc
From the CFPB's ["What you should know about home equity lines of credit"][cpfb-heloc-you-should-know]:

> A home equity line of credit is a form of revolving credit in which your home serves as collateral. Because a home often is a consumer’s most valuable asset, many homeowners use home equity credit lines only for major items, such as education, home improvements, or medical bills, and choose not to use them for day-to-day expenses.

See also: [HELOC on Investopedia][investopedia-heloc] for a more practical reference

### nostro
Nostro loans are the firm's accounts at other financial institutions which are in effect loans to other firms. Nostros are used in the context of correspondent banking operations which are described by the [ECB](https://www.ecb.europa.eu/paym/t2/shared/pdf/target2_glossary.pdf):
> Correspondent banking: an arrangement under which one credit institution provides payment and other services to another credit institution. Payments through correspondents are often executed through reciprocal accounts (nostro and loro accounts) to which standing credit lines may be attached. Correspondent banking services are primarily provided across international boundaries but are also known as agency relationships in some domestic contexts.
> A loro (vostro) account is the term used by a correspondent to describe an account held on behalf of a foreign credit institution; the foreign credit institution would in turn regard this account as its nostro account.

### financial_lease
From the [UK Gov](https://www.gov.uk/hmrc-internal-manuals/business-leasing-manual/blm00040), a finance lease is an arrangement under which one person (the lessor) provides the money to buy an asset which is used by another (the lessee) in return for an interest charge. The lessor has security because they own the asset. The terms of the leasing arrangements aim to give the lessor an interest like turn and no more or less – however good or bad the asset proves to be for the end user.

### other
Other refers to a type of security not covered by the above. If you find yourself using this often, please [contribute][contributing].


# Security

```
├── equity
│   ├── dividend
│   ├── share
│   │   ├── treasury
│   │   └── pref_share
│   ├── share_agg
│   └── speculative_unlisted
│   └── main_index_equity
├── debt
│   ├── bond
│   ├── covered_bond
│   ├── convertible_bond
│   ├── frn
│   ├── commercial_paper
│   ├── cd
│   ├── struct_note
│   ├── spv_mortgages
│   ├── spv_other
│   ├── mtn
│   │   └── emtn
│   ├── pibs
│   └── abs
│       ├── abs_lease
│       │   └── abs_auto
│       ├── abs_cc
│       ├── abs_consumer
│       ├── abs_corp
│       ├── abs_sme
│       │   ├── abs_sme_corp
│       │   └── abs_sme_retail
│       ├── abs_trade_rec
│       ├── abs_wholesale
│       ├── abs_other
│       └── mbs
│           ├── rmbs
│           │   └── rmbs_income
│           ├── rmbs_trans
│           ├── cmbs
│           │   └── cmbs_income
│           └── nha_mbs
├── guarantee
│   ├── financial_guarantee
│   │   └── financial_sloc
│   └── performance_guarantee
│       ├── warranty
│       ├── performance_bond
│       └── performance_sloc
├── letter_of_credit
├── bill_of_exchange
│   └── acceptance
├── cb_reserve
├── cb_facility
├── cash_ratio_deposit
├── cash
├── index
└── other
```

### cash
A **cash** or cash-equivalent security such as a securitisation of cash deposits. Within [Finrep Annex V part (2)(1)(1.1)(1)](https://www.eba.europa.eu/sites/default/files/document_library/Publications/Draft%20Technical%20Standards/2020/ITS/ITS%20on%20supervisory%20reporting%20changes%20related%20to%20CRR2%20and%20Backstop%20Regulation/Annexes/886555/Annex%205%20%28FINREP%29.pdf):
> "Cash on hand" includes holdings of national and foreign banknotes and coins in circulation that are commonly used to make payments.

### equity
This is a "catch all" term for equity instruments such as *share*, *share_agg* to be used when further granularity is not available or not needed.

### dividend
A distribution of a company's post-tax profits made to its shareholders. Dividends are usually paid in cash but can also be satisfied by the transfer of non-cash assets or by shares in the company itself.
[dividend]: https://uk.practicallaw.thomsonreuters.com/1-107-6135?transitionType=Default&contextData=(sc.Default)&firstPage=true

### share, share_agg
Denotes if the security is a share (stock) or represents an aggregate for a portfolio or package of shares.

### pref_share
The [FCA](https://www.handbook.fca.org.uk/handbook/glossary/G1587.html) defines a **preference share** as:
> A share conferring preference as to income or return of capital which does not form part of the equity share capital of a company

### speculative_unlisted
As per OSFI and BCBS, a Speculative unlisted equity is defined as "an equity investments in unlisted companies that are invested for short-term resale purposes, or are considered venture capital or similar investments which are subject to price volatility and are acquired in anticipation of significant future capital gains, or are held with trading intent. Investments in unlisted equities of corporate clients with which the institution has or intends to establish a long-term business relationship and debt-equity swaps for corporate restructuring purposes would be excluded."  OSFI Chapter 4 P76.

### treasury
According to IAS 32.33, if an entity reacquires its own equity instruments, those instruments shall be considered **treasury shares**, and shall be deducted from equity.

### main_index_equity
The main_index_equity identifies equities that are constituents of a main index for the purposes of applying a volatility adjustment in line with [Article 224](https://www.eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/16006).

### debt
This is a "catch all" term for debt of any kind, *bond*, *bond_amortising*, *covered_bond*, *abs*, *residential_mbs*, *non_residential_mbs*, *frn*, *govt_gteed_frn*, to be used when further granularity is not available or not needed.

### bond
A **bond** is a type of loan whereby an investor lends money to an entity for a defined period of time at a fixed or floating interest rate.

### covered_bond
From the [LCR][lcr] Introduction (8):
> Covered bonds are debt instruments issued by credit institutions and secured by a cover pool of assets which typically consist of mortgage loans or public sector debt to which investors have a preferential claim in the event of default. Their secured nature and certain additional safety features, such as the requirement on the issuer to replace non-performing assets in the cover pool and maintain the cover pool at a value exceeding the par value of the bonds (‘asset coverage requirement’), have contributed to make covered bonds relatively low-risk, yield-bearing instruments with a key funding role in mortgage markets of most Member States. In certain Member States outstanding covered bond issuance exceeds the pool of outstanding government bonds. Certain covered bonds of credit quality step 1, in particular, exhibited an excellent liquidity performance during the period from 1 January 2008 to 30 June 2012 analysed by the EBA in its report. Nevertheless the EBA recommended treating these covered bonds as level 2A assets to align with BCBS standards. However, in the light of the considerations made above about their credit quality, liquidity performance and role in the funding markets of the Union, it is appropriate for these credit quality step 1 covered bonds to be treated as level 1 assets. In order to avoid excessive concentration risks and unlike other level 1 assets, the holdings of credit quality step 1 covered bonds in the liquidity buffer should be subject to a 70 % cap of the overall buffer, a minimum 7 % haircut and to the diversification requirement.

### convertible_bond
Generally, a **convertible_bond** is a security which gives the investor the right to convert the security into shares at an agreed price on an agreed basis.

From the [European system of national and regional accounts][2013-549]
> bonds, which may, at the option of the holder, be converted into the equity of the issuer, at which point they are classified as shares;

### emtn, mtn
A Euro medium-term note is a medium-term (less than 5 years), flexible debt instrument that is traded and issued outside of the US and Canada. A medium-term note is the same but is traded in the US and Canada.

### commercial_paper
Commercial paper is an unsecured promissory note with a fixed maturity of, typically, not more than 270 days.

### cd
A certificate of deposit is also a promissory note, however can only be issued by a bank. It has a fixed maturity and specified fixed interest rate.

### bill_of_exchange
From [UK Legislation](https://www.legislation.gov.uk/ukpga/Vict/45-46/61), a bill of exchange is an unconditional order in writing, addressed by one person to another, signed by the person giving it, requiring the person to whom it is addressed to pay on demand or at a fixed or determinable future time a sum certain in money to or to the order of a specified person, or to bearer.

### cb_facility
*Needs definition*

### struct_note
Structure notes shall comprise contracts with embedded derivatives that are not covered bonds, asset backed securities, or classified as convertible compound financial instruments. They are a type of fixed-term investment where the amount you earn depends on the performance of a specific market (such as the FTSE 100) or specific assets (such as shares in individual companies).(https://www.fca.org.uk/consumers/structured-products)

### spv_mortgages, spv_other
A special purpose vehicle is a separate legal entity created to fulfil a certain purpose for the parent.

### abs
An asset-backed security is a security whose income payments and hence value are derived from and collateralised (or "backed") by a specified pool of underlying assets. The pool of assets is typically a group of small and illiquid assets which are unable to be sold individually. Pooling the assets into financial instruments allows them to be sold to general investors, a process called securitisation. This allows the risk of investing in the underlying assets to be diversified because each security will represent a fraction of the total value of the diverse pool of underlying assets. The pools of underlying assets can include common payments from credit cards, auto loans, and mortgage loans, to esoteric cash flows from aircraft leases, royalty payments and movie revenues.

The receivables or assets underlying the securitisation must be credit claims or receivables with defined terms relating to rental payments or principal and interest payment. Any referenced interest payments should be based on commonly encountered market interest rates and may include terms for caps and floors, but should not reference complex formulae or exotic derivatives.
A non-exhaustive list of [examples][ecbexamples] of underlying assets that may comply with the above principles, (subject to meeting all other criteria) could include:
- residential mortgages,
- certain commercial real estate mortgages,
- loans to SMEs,
- automobile loans/leases,
- consumer finance loans,
- credit card receivables, and
- leasing receivables.

### abs_lease
Asset-backed securities backed by leases.

### abs_auto
Auto loans and leases encompass a wide group of cars, motorcycles and other vehicles more fromally defined [here]( https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32015R0061#:~:text=auto%20loans%20and,of%20title%20provision):

### abs_cc
Asset-backed securities backed by credit card receivables.

### abs_corp
Asset-backed securities backed by corporate loans.

### abs_trade_rec
Asset-backed securities backed by trade receivables.

### abs_sme
Asset-backed securities backed by SME loans.

### abs_sme_corp
Asset-backed securities backed by SME loans considered as corporate.

### abs_sme_retail
Asset-backed securities backed by SME loans considered as retail.

### abs_consumer
Asset-backed securities backed by consumer credit.

### abs_wholesale
Asset-backed securities backed by wholesale credit.

### abs_other
Any other asset-backed securitisation not encompassed by one of the other classifications.

### mbs
Asset-backed securities specifically backed by mortgages.

### mtn
Medium-term notes

### pibs
[Building Societies Association](https://www.bsa.org.uk/information/consumer-factsheets/general-information/what-are-pibs) defines Permanent interest bearing shares (PIBS) as fixed-interest securities issued by building societies, and quoted on the stock market.  They are bond like instruments in that they pay interest, but they have no maturity date - PIBS typically exist as long as their issuer does.

### performance_bond
*Needs definition*

### rmbs
A residential mortgage-backed security (a subclass of an ABS/MBS).

### rmbs_income
A residential mortgage-backed security secured by a pool of mortages that are deemed to be income producing. Income producing mortages are defined as loans whose prospects for servicing them materially depend on the cash flows generated by the properties securing the loans rather than on the underlying capacity of the borrower to service the debt from other sources.

Reference: [OSFI BCAR, section 4.1.11](https://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/CAR22_chpt4.aspx#:~:text=Income%20producing%20residential%20real%20estate%3A%20exposures%20where%20the%20criteria%20in%20paragraph%20100%20are%20met%2C%20but%20those%20in%20paragraph%20110%20(land%20acquisition%2C%20development%20and%20construction)%20are%20not%20applicable.)

### rmbs_trans
This type value is in order to indicate whether the security is subject to transitional provisions for securitisations backed by residential loans:
[LCR][lcr] Article 37:
> 1.   By derogation from Article 13, securitisations issued before 1 October 2015, where the underlying exposures are residential loans as referred to in point (g)(i) of Article 13(2), shall qualify as Level 2B assets if they meet all the requirements set out in Article 13 other than the loan-to-value or loan-to-income requirements set out in that point (g)(i) of Article 13(2).

> 2.   By derogation from Article 13, securitisations issued after 1 October 2015, where the underlying exposures are residential loans as referred to in point (g)(i) of Article 13(2) that do not meet the average loan-to-value or the loan-to-income requirements set out in that point, shall qualify as Level 2B assets until 1 October 2025, provided that the underlying exposures include residential loans that were not subject to a national law regulating loan-to-income limits at the time they were granted and such residential loans were granted at any time prior to 1 October 2015.

### cmbs
A commercial mortgage-backed security (a subclass of an abs).

### cmbs_income
A commercial mortgage-backed security secured by a pool of mortages that are deemed to be income producing. Income producing mortages are defined as loans whose prospects for servicing them materially depend on the cash flows generated by the properties securing the loans rather than on the underlying capacity of the borrower to service the debt from other sources.

Reference: [OSFI BCAR, section 4.1.12](https://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/CAR22_chpt4.aspx#:~:text=Income%20producing%20commercial%20real%20estate%3A%20exposures%20where%20the%20criteria%20in%20paragraph%20108%20are%20met%2C%20but%20those%20in%20paragraph%20110%20(land%20acquisition%2C%20development%20and%20construction)%20are%20not%20applicable.)

### nha_mbs
National Housing Act (NHA) MBS that are guaranteed by the Canada Mortgage and Housing Corporation (CMHC), will receive a risk weight of 0% in recognition of the fact that obligations incurred by CMHC are legal obligations of the Government of Canada.

Reference: [OSFI BCAR Chapter 4, P120](https://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/CAR22_chpt4.aspx#:~:text=National%20Housing%20Act%20(NHA)%20MBS%20that%20are%20guaranteed%20by%20the%20Canada%20Mortgage%20and%20Housing%20Corporation%20(CMHC)%2C%20will%20receive%20a%20risk%20weight%20of%200%25%20in%20recognition%20of%20the%20fact%20that%20obligations%20incurred%20by%20CMHC%20are%20legal%20obligations%20of%20the%20Government%20of%20Canada.)

### frn
A floating-rate note is defined in the [Money Market Statistics Regulation][mm-stat] in Annex II as:
> A debt instrument for which the periodic interest payments are calculated on the basis of the value, i.e. through fixing of an underlying reference rate such as Euribor on predefined dates known as fixing dates, and which has a maturity of not more than one year.
> note: "one year" is defined as transactions with a maturity date of not more than 397 days after the trade date

### govt_gteed_frn
A government guaranteed floating-rate note.

### cb_reserve
As defined in [LCR Regulations Article 10 on Liquid Assets][lcr]:
> reserves held by the credit institution in a central bank referred to in points (i) and (ii) provided that the credit institution is permitted to withdraw such reserves at any time during stress periods and the conditions for such withdrawal have been specified in an agreement between the relevant competent authority and the ECB or the central bank;

> include balances receivable on demand at central banks.

### cash_ratio_deposit
The [BofE](https://www.bankofengland.co.uk/statistics/notice/2024/statistical-notice-2024-08) defines this as:
> The Levy will be applied on a proportional basis, which means that the Bank will allocate the policy costs to be recovered by the Levy in proportion to an eligible institution’s liability base. Eligible liabilities are defined in the Glossary. This will be a continuation of how the CRD scheme operated. The policy rationale for using the eligible liability base is the link between the size of a financial institution’s liabilities and its potential impact on the Bank’s financial stability and monetary policy functions.

### guarantee
From EU [Supervisory Reporting][sup-rep] part 2(9):
> 'Financial guarantees' are contracts that require the issuer to make specified payments to reimburse the holder of a loss it incurs, because a specified debtor fails to make payment when due in accordance with the original or modified terms of a debt instrument. Under IFRS or compatible National GAAP, these contracts meet the IAS 39.9 and IFRS 4.A definition of financial guarantee contracts. The following items of Annex I of the CRR shall be classified as 'financial guarantees':
> (a) Guarantees having the character of credit substitute.
> (b) Credit derivatives that meet the definition of financial guarantee.
> (c) Irrevocable standby letters of credit having the character of credit substitutes.

### trade_credit_insurance
From the [EBA's][eba-nsfr-report] report on the NSFR, section 6.2.1 outlines what **trade credit insurance** is:
> A seller providing trade credit is exposed to the credit risk of the buyer. Trade credit insurance provides the seller with protection against the risk of non-payment by the buyer. The nonpayment may be due to the insolvency of the buyer or, in an international trade, due to political risks that prevent payment.

### letter_of_credit
From the [EBA's][eba-nsfr-report] report on the NSFR, section 6.2.2, a **letter of credit** is:
> When goods are traded, the seller and the buyer need to agree on the process of how to pay for the goods. While the buyer may be reluctant to prepay for the traded goods, the seller may also be unwilling to ship the goods before payment is made. In this situation, a bank can intermediate between the trading partners by providing an import letter of credit (L/C) to the buyer of the goods, which guarantees payment to the seller.
> A L/C is a contingent liability and payment is only made by the bank to the seller from funds in the buyer’s account when the documentation of shipping is presented.

### acceptance
From EU [Supervisory Reporting][sup-rep] part 2(5)(60)(b):
> “Acceptances” are obligations by an institution to pay on maturity the face value of a bill of exchange, normally covering the sale of goods. Consequently, they are classified as “trade receivables” on the balance sheet

### financial_guarantee
From EU [Supervisory Reporting][sup-rep] part 2(9):
> 'Financial guarantees' are contracts that require the issuer to make specified payments to reimburse the holder of a loss it incurs, because a specified debtor fails to make payment when due in accordance with the original or modified terms of a debt instrument. Under IFRS or compatible National GAAP, these contracts meet the IAS 39.9 and IFRS 4.A definition of financial guarantee contracts. The following items of Annex I of the CRR shall be classified as 'financial guarantees':
> (a) Guarantees having the character of credit substitute.
> (b) Credit derivatives that meet the definition of financial guarantee.
> (c) Irrevocable standby letters of credit having the character of credit substitutes.

### financial_sloc
Financial standby letter of credit

### performance_sloc
Performance standby letter of credit

### performance_guarantee
*Needs definition*

### share_agg
*Needs definition*

### spv_other
*Needs definition*

### urp
*Needs definition*

### warranty
*Needs definition*

### other
Other refers to a type of security not covered by the above. If you find yourself using this often, please [contribute][contributing].

### index_linked
Index-linked securities are securities whose notional amount and interest amount are linked on the intial and final values of an index, generally an inflation index.

### index
Index securities are reference records recording the details of an index using the index_composition field.


# Account

```bash
├── bonds
├── call
├── cd
├── credit_card
├── current
│   └── current_io
├── debit_card (pending)
├── internet_only
├── ira
├── isa
│   ├── isa_time_deposit
│   │   └── isa_time_deposit_io
│   ├── isa_current
│   │   └── isa_current_io
│   └── isa_io
├── money_market
├── non_product
│   ├── accruals
│   ├── amortisation
│   ├── deferred
│   │   └── deferred_tax
│   ├── depreciation
│   ├── expense
│   ├── income
│   ├── intangible
│   ├── non_deferred
│   ├── prepayments
│   ├── provision
│   ├── reserve
│   ├── suspense
│   └── tangible
├── prepaid_card
├── retail_bonds
├── savings
│   └── savings_io
├── time_deposit
│   └── time_deposit_io
├── third_party_savings
├── vostro
└── other
```

### call
A call account is defined in the [Money Market Statistics Regulation][mm-stat] in Annex II as:
> A debt instrument in which the issuer has a call option, i.e. an option to redeem the instrument early, with a final repayment date of not more than one year from the date of issuance.

### cd
A deposit account purely holding certificates of deposit (see *cd* *Security* **type**)

### prepaid_card
From the [Interchange Fees for Card-based Payments Regulation][card-fees] Article 2(35):
> prepaid card means a category of payment instrument on which electronic money, as defined in point 2 of Article 2 of Directive 2009/110/EC, is stored. This can also include cash-loaded smart cards or electronic money schemes, for which pre-payment has been received.

### debit_card
From the [Interchange Fees for Card-based Payments Regulation][card-fees] Article 2(33) and (4):
> debit card means a category of payment instrument that enables the payer to initiate a debit card transaction excluding those with prepaid cards;
> debit card transaction means a card-based payment transaction, including those with prepaid cards that is not a credit card transaction;

### credit_card
A credit card is typically an off-balance sheet, contingent funding obligation whereby a customer has a certian credit limit and may borrow funds at any point, up to that limit, similar to a card-based credit facility.

The [Interchange Fees for Card-based Payments Regulation][card-fees] states that:
> There are two main types of credit cards available on the market. With deferred debit cards, the total amount of transactions is debited from the cardholder account at a pre-agreed specific date, usually once a month, without interest to be paid. With other credit cards, the cardholder can use a credit facility in order to reimburse part of the amounts due at a later date than specified, together with interest or other costs.

A credit card is then defined in Article 2 (34) and (5) as:
> credit card means a category of payment instrument that enables the payer to initiate a credit card transaction;
> credit card transaction means a card-based payment transaction where the amount of the transaction is debited in full or in part at a pre agreed specific calendar month date to the payer, in line with a prearranged credit facility, with or without interest;

### current (checking, demand)
Any transactional account.

### current_io
A current account that is offered and only accessible via the internet.

### bonds
Any account containing notes, bonds or other securities instruments.

### retail_bonds
As referenced in the [LCR][lcr] Regulation Article 28 (6) as any account:
> containing notes, bonds and other securities issued which are sold exclusively in the retail market and held in a retail account. Limitations shall be placed such that those instruments cannot be bought and held by parties other than retail customers.


### internet_only
An internet-only account is one that is offered and only accessible via the internet. The [FCA][fca-internet] defines the internet in their handbook as:
> a unique medium for communicating financial promotions as it provides easy access to a very wide audience. At the same time, it provides very little control over who is able to access the financial promotion.

The distinction here linked to financial promotions suggests that internet-only accounts are sold and managed through a higher risk channel and therefore should be regulated spearately to other accounts.

### isa
An ISA is an individual savings account which is a scheme of investment satisfying the conditions prescribed in the UK's [ISA Regulations][uk-isa].

### isa_io
An isa account that is offered and only accessible via the internet.

### isa_time_deposit
An [**isa**][uk-isa] which is also a **time_deposit** account.

### isa_time_deposit_io
An isa time deposit account that is offered and only accessible via the internet.

### isa_current
An [**isa**][uk-isa] current account.

### isa_current_io
An [**isa**][uk-isa] current account that is offered and only accessible via the internet.

### ira
A trust created or organized in the United States for the exclusive benefit of an individual or his beneficiaries. See [US Code Title 26, S.408][ira]

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

### savings_io
A saving account that is offered and only accessible via the internet.

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

### time_deposit_io
A time deposit account that is offered and only accessible via the internet.

### third_party_savings
Subset of savings accounts for which the interest is paid in a separate account held at a third party bank.

### deposit
Deposit or depository account is defined in the [Directive regarding the mandatory exchange of tax information][exch-tax-info] section 8:
> The term “Depository Account” includes any commercial, checking, savings, time, or thrift account, or an account that is evidenced by a certificgitcheckoutate of deposit, thrift certificate, investment certificate, certificate of indebtedness, or other similar instrument maintained by a Financial Institution in the ordinary course of a banking or similar business. A Depository Account also includes an amount held by an insurance company pursuant to a guaranteed investment contract or similar agreement to pay or credit interest thereon.

### non_product
This is an overarching term used to define any non-product accounts that may exist on the balance sheet, ledger or other income/P&L accounts.

### accruals
accruals are liabilities to pay for goods or services that have been received or supplied but have not been paid, invoiced or formally agreed with the supplier, including amounts due to employees (for example, amounts relating to accrued vacation pay). https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2022/issued/part-a/ias-37-provisions-contingent-liabilities-and-contingent-assets.pdf

### amortisation
An account which holds the **amortisation amount** of intangible assets measured at cost model. IAS 38.74 defines cost model measurement of intangible assets as follow:
> After initial recognition intangible assets should be carried at cost less accumulated **amortisation** and impairment losses

### depreciation
An account representing the change in value attributable (over a period) to assets where depreciation must be accounted for.

### deferred
A **deferred** account is an account in which the recognition of certain revenue or expenses on the income statement is delayed for a certain period of time. For example, a deferred tax asset, which is reported in F1.01 of FINREP,  is defined by IAS 12.5 as follows:
> the amounts of income taxes recoverable in future periods in respect of:
(a) deductible temporary differences;
(b) the carryforward of unused tax losses; and
(c) the carryforward of unused tax credits.

### deferred_tax
Deferred tax liabilities are the amounts of income taxes payable in future periods in respect of taxable temporary differences.
Deferred tax assets are the amounts of income taxes recoverable in future periods in respect of:

(a) deductible temporary differences;
(b) the carry forward of unused tax losses; and
(c) the carry forward of unused tax credits.
[deferred_tax]: https://www.ifrs.org/issued-standards/list-of-standards/ias-12-income-taxes/

### non_deferred
Undeferred is used to avoid confusion with a customer current account. This is in reference to a current asset or current liability eg. (current tax liability) where it is recognised typically within the next 12 months.

### intangible
An account which holds intangible assets. IAS 38 defines an **intangible asset** as:
> an identifiable non-monetary asset without physical substance.

### tangible
An account that holds tangible assets. From the definition of an **intangible asset**, we can infer that tangible assets refers to an asset has physical substance, for example, property or machinery.

### suspense
Transactions will be considered to be in [**suspense**][suspense] if there is some doubt at the time of reporting regarding how the transaction  should be classified and reported, for example, which ledger should it be posted to.

MAS Notice 610 and Notice 1003 refers to **suspense** accounts as all outstanding unreconciled amounts that are kept in suspense.

[suspense]: https://www.investopedia.com/terms/s/suspenseaccount.asp


### prepayments
A prepaid expense is an expenditure paid for in one accounting period, but for which the underlying asset will not be consumed until a future period. https://www.accountingtools.com/articles/prepaid-expenses-accounting

### provision
IAS 37.10 defines a **provision** as:
> a liability of uncertain timing or amount

### income
An account representing monies received (over a period).

### expense
An account representing monies spent (over a period).

### reserve
An account holding reserves. [Reserves][reserve] are created from profit or from capital gains and are retained by an entity for a specific or more general purpose. Reserves are essentially anything on the equity side of the balance sheet that is not capital.

[reserve]:  https://en.wikipedia.org/wiki/Reserve_(accounting)

### other
Any other account type that cannot be classified as one of the other types.

# derivative_type
```bash
├── vanilla_swap
├── mtm_swap
├── cds
│   └── ccds
├── ois
├── xccy
├── nds
├── option
│   ├── swaption
│   └── cap_floor
├── forward
│   ├── future
│   └── ndf
├── fra
├── spot
└── variance_swap
```

### option

### cap_floor
Options with multiple exercise and payment periods, generally used in relation to interest rate indices, but also in other asset classes

### swaption
Options which give the buyer the right to enter into an interest rate swap with the option seller, with either a physical settlement or a cash-settlement.

### ois
Overnight Index Swap

### cds
A [**credit default swap**][cds] means a derivative contract in which one party pays a fee to another party in return for a payment or other benefit in the case of a credit event relating to a reference entity and of any other default, relating to that derivative contract, which has a similar economic effect;

[cds]:  https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32012R0236


### ccds
A [**contingent credit default swap**][ccds] (CCDS) is a variation of a credit default swap (CDS) where an additional triggering event is required.

[ccds]: https://www.investopedia.com/terms/c/contingent-credit-default-swap.asp


### spot
Spot Exchange

### ndf
A [**non-deliverable forward**][ndf] is a cash-settled, and usually short-term, forward contract. The notional amount is never exchanged, hence the name "non-deliverable." Two parties agree to take opposite sides of a transaction for a set amount of money - at a contracted rate, in the case of a currency NDF. This means that counterparties settle the difference between contracted NDF price and the prevailing spot price. The profit or loss is calculated on the notional amount of the agreement by taking the difference between the agreed-upon rate and the spot rate at the time of settlement.
NDFs are also known as forward contracts for differences (FCD).

[ndf]: https://www.investopedia.com/terms/n/ndf.asp

### nds
A [**non-deliverable swap**][nds] is a variation on a currency swap between major and minor currencies that is restricted or not convertible. This means that there is no actual delivery of the two currencies involved in the swap, unlike a typical currency swap where there is physical exchange of currency flows. Instead, periodic settlement of a NDS is done on a cash basis, generally in U.S. dollars.

The settlement value is based on the difference between the exchange rate specified in the swap contract and the spot rate, with one party paying the other the difference. A non-deliverable swap can be viewed as a series of non-deliverable forwards bundled together.

[nds]: https://www.investopedia.com/terms/n/nondeliverableswap.asp

### fra
A [**forward rate agreement**][fra] is an interest rate forward contract in which the rate to be paid or received on a specific obligation for a set period of time, beginning at some time in the future, is determined at contract initiation.

[fra]: https://www.bis.org/statistics/glossary.htm?&selection=315&scope=Statistics&c=a&base=term

### variance_swap
A variance swap is an instrument which allows investors to trade future realized (or historical) volatility against current implied volatility.

### forward
A forward is a non-standardized contract between two parties to buy or sell an asset at a specified future time at a price agreed on at the time of conclusion of the contract, making it a type of derivative instrument. The party agreeing to buy the underlying asset in the future assumes a long position, and the party agreeing to sell the asset in the future assumes a short position. The price agreed upon is called the delivery price, which is equal to the forward price at the time the contract is entered into.
The price of the underlying instrument, in whatever form, is paid before control of the instrument changes.

### future
A futures contract (sometimes called futures) is a standardized legal agreement to buy or sell something at a predetermined price at a specified time in the future, between parties not known to each other. The asset transacted is usually a commodity or financial instrument. The predetermined price the parties agree to buy and sell the asset for is known as the forward price. The specified time in the future—which is when delivery and payment occur—is known as the delivery date. Because it is a function of an underlying asset, a futures contract is a derivative product.

Contracts are negotiated at futures exchanges, which act as a marketplace between buyers and sellers. The buyer of a contract is said to be the long position holder and the selling party is said to be the short position holder.

### mtm_swap

### vanilla_swap

### xccy
A derivative contract, agreed between two counterparties, which specifies the nature of an exchange of payments benchmarked against two interest rate indexes denominated in two different currencies. It also specifies an initial exchange of notional currency in each different currency and the terms of that repayment of notional currency over the life of the swap.

The most common XCS, and that traded in interbank markets, is a mark-to-market (MTM) XCS, whereby notional exchanges are regularly made throughout the life of the swap according to FX rate fluctuations. This is done to maintain a swap whose MTM value remains neutral and does not become either a large asset or liability (due to FX rate fluctuations) throughout its life.



# collateral
```bash
├── residential_property
│   └── multifamily
├── farm
├── commercial_property
│   └── commercial_property_hr
├── immovable_property
├── guarantee
├── debenture
├── life_policy
├── cash
├── security
└── other
```
The collateral type defines the form of the collateral, such as property or other assets used to secure an obligation.

The [EC Collateral Directive][arrangement] states:
> The assets can be provided: either by transfer of full ownership from a collateral provider to a collateral taker; or by the transfer of possession from a collateral provider to a collateral taker under a security right (e.g. pledge, charge or lien), where the full ownership of the assets remains with the collateral provider.

### residential_property
Immovable property whose occupation is primarily for residential use. Specific regulatory definitions can be found below:

From EBA [Closing Real Estate Data Gaps](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32017Y0131%2801%29) Section 2 (1)(1)(38):

‘Residential real estate’ (RRE) means any immovable property located in the domestic territory, available for dwelling purposes, acquired, built or renovated by a private household and that is not qualified as a CRE property. If a property has a mixed use, it should be considered as different properties (based for example on the surface areas dedicated to each use) whenever it is feasible to make such breakdown; otherwise, the property can be classified according to its dominant use.

### commercial_property

Immovable property whose occupation is primarily for non-residential use (e.g. used for business activities and profit generation). Specific regulatory definitions can be found below:

From EBA [Closing Real Estate Data Gaps](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32017Y0131%2801%29) Section 2 (1)(1)(4):

‘Commercial real estate’ (CRE) means any income-producing real estate, either existing or under development, and excludes:

    (a) social housing;
    (b) property owned by end-users;
    (c) buy-to-let housing.

If a property has a mixed CRE and RRE use, it should be considered as different properties (based for example on the surface areas dedicated to each use) whenever it is feasible to make such breakdown; otherwise, the property can be classified according to its dominant use;

From [OSFI Financial Reporting Instructions: Data Definitions for BH](https://www.osfi-bsif.gc.ca/en/data-forms/reporting-returns/filing-financial-returns/financial-reporting-instructions?title=BH&field_industry_target_id=All&field_publication_type_target_id=All&field_return_target_id=All):

Completed retail, office/commercial, industrial, mixed use (with less than 50%  residential), warehouse and special purpose properties with > 50% of the space leased/rented to tenants not related to the owner or affiliates.  Includes long term care facilities.

### commercial_property_hr
Commercial property collateral that does not provide the lender with an adequate level of security and may attract a higher risk weight, i.e. one or more of the conditions laid out in Article 126 (2) of CRR 275/2013 is not met.

As per Article 126 (2) of CRR 275/2013:
>Institutions shall consider an exposure or any part of an exposure as fully and completely secured only if all the following conditions are met:
>
>(a) the value of the property shall not materially depend upon the credit quality of the borrower. Institutions may exclude situations where purely macro-economic factors affect both the value of the property and the performance of the borrower from their determination of the materiality of such dependence;
>
>
>(b) the risk of the borrower shall not materially depend upon the performance of the underlying property or project, but on the underlying capacity of the borrower to repay the debt from other sources, and as a consequence, the repayment of the facility shall not materially depend on any cash flow generated by the underlying property serving as collateral;
>
>
>(c) the requirements set out in Article 208 and the valuation rules set out in Article 229(1) are met; and
>
>
>(d) the 50 % risk weight unless otherwise provided under Article 124(2) shall be assigned to the part of the loan that does not exceed 50 % of the market value of the property or 60 % of the mortgage lending value unless otherwise provided under Article 124(2) of the property in question in those Member States that have laid down rigorous criteria for the assessment of the mortgage lending value in statutory or regulatory provisions.

For the purposes of this definition of commercial_property_hr, if the collateral does not meet condition (d) (e.g. has a loan-to-value ratio higher than 60%) but meets conditions (a) to (c), the collateral is not considered to be commercial_property_hr (which is allocated for those exposures with a RW of 100%) but is still classified as ordinary commercial_property collateral.


### multifamily
Property composed of five or more residential dwellings.
[US Census Bureau definition][us-census-multifamily]:
> buildings with five units or more

[OSFI Financial Reporting Instructions: Data Definitions for BH](https://www.osfi-bsif.gc.ca/en/data-forms/reporting-returns/filing-financial-returns/financial-reporting-instructions?title=BH&field_industry_target_id=All&field_publication_type_target_id=All&field_return_target_id=All):

> Completed rental apartment buildings (> 4 units). Includes mixed use properties where residential space represents more than 50% of total space.

### immovable_property
As per Artcile 124(1) [CRR][crr], this identifies **immovable property**
collateral that cannot be classified as residential or commercial property.

### farm
*NEEDS Definition*

### guarantee
*NEEDS Definition*

### debenture
*NEEDS Definition*

### life_policy
From Article 212(2) [CRR](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32013R0575), life insurance policies pledged as collateral will be considered if it meets certain criteria outlined in the article. These conditions include ,**but not limited to**, the credit institutions openly being assigned as the beneficiary and the life insurance company being notified of the pledge to the lending institution. Providing the conditions outlined in the article are met, the life insurance is eligble for use as collateral and the lender has a claim to some or all of the death benefit until the loan is repaid.
### cash
*NEEDS Definition*

### security
This identifies that the piece of collateral used is a security, as mapped via the security schema and linked to the collateral schema using the collateral's `security_id` property.

### other
*NEEDS Definition*


# Agreement

```bash
├── ema
├── gmra
│   ├── icma_1992
│   ├── icma_1995
│   ├── icma_2000
│   ├── icma_2011
│   └── other_gmra
├── gmsla
├── isda
│   ├── isda_1985
│   ├── isda_1986
│   ├── isda_1987
│   ├── isda_1992
│   ├── isda_2002
│   ├── drv
│   ├── fbf
│   │   └── afb
│   └── other_isda
└── other
```

### ema
The Euro Master Agreement - a master agreement for both domestic and cross-border transactions. The EMA should initially cover repurchase agreements as well as securities lending transactions.
https://www.ebf.eu/home/european-master-agreement-ema/

### gmra
From the [ICMA website][icma-web]:
Global Master Repurchase Agreement. Covers SFTs like repos, reverse repos, stock lending etc.
Since the early 1990s ICMA has devoted considerable resources to developing a standard master agreement for repo transactions in conjunction with the Securities Industry and Financial Markets Association (SIFMA). The first version of the GMRA was published in 1992 and followed by substantially revised versions in 1995, 2000 and 2011.

ICMA obtains and annually updates opinions from numerous jurisdictions worldwide on the GMRA 1995, 2000 and 2011 versions.

**The ERCC recently took a decision to discontinue coverage of the GMRA 1995 in the ICMA GMRA legal opinions from 2019 onwards. For further information contact legalhelpdesk@icmagroup.org**

### icma_1992
The 1992 version of the GMRA agreement.

### icma_1995
The 1995 version of the GMRA agreement.

### icma_2000
The 2000 version of the GMRA agreement.

### icma_2011
The 2011 version of the GMRA agreement.

### other_gmra
Any other repurchase agreement.

### gmsla
Global Master for Securities Lending Agreements
https://www.icmagroup.org/events/icma-workshop-repo-and-securities-lending-under-the-gmra-and-gmsla/

### isda
From [Investopedia][isda-investo]:
> An ISDA Master Agreement is the standard document regularly used to govern over-the-counter derivatives transactions. The agreement, which is published by the International Swaps and Derivatives Association (ISDA), outlines the terms to be applied to a derivatives transaction between two parties, typically a derivatives dealer and a counterparty. The ISDA Master Agreement itself is standard, but it is accompanied by a customized schedule and sometimes a credit support annex, both of which are signed by the two parties in a given transaction.

More info can be found from [ISDA][isda] itself.

### isda_1985
The 1985 version of the ISDA agreement.

### isda_1986
The 1986 version of the ISDA agreement.

### isda_1987
The 1987 version of the ISDA agreement.

### isda_1992
The 1992 version of the ISDA agreement.

### isda_2002
The 2002 version of the ISDA agreement.

### drv
German variation of ISDA - rahmenvertrag
https://www.mayerbrown.com/en/perspectives-events/blogs/2020/11/documenting-benchmark-transition-under-the-german-master-agreement-for-financial-derivatives-transactions

### fbf
Federation Bancaire Francaise - French variation of ISDA
https://www.fbf.fr/en/fbf-master-agreement-relating-to-transactions-on-forward-financial-instruments-published-on-february-5-2020-last-update-on-june-16-2020/

### afb
Association Francaise de Banques - ancestor of the FBF
https://theotcspace.com/knowledge_item/afb-agreement-federation-bancaire-francais-afba-fbf/

### other_isda
Any other ISDA agreement.

### other
Any other agreement. If you use this a lot, get in touch, maybe we need more types!



# curve

### behavioral
A curve describing the behavior of a product or customer segment under certain (stress) conditions

### rate
An interest rate curve

### volatility
A volatility curve (smile)


# loan_cash_flow

### interest
A repayment that covers only the interest section of the loan, the principal borrowed amount in this case is left unchanged

### principal
A repayment that reduces the principal amount borrowed and does not include any interest component


# loan_transaction

### advance
A loan amount sent to the borrower from the lender

### capital_repayment
A repayment that reduces the principal amount borrowed

### capitalisation
From F3.1 of [MLAR](https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/crd-iv/mlar-notes-may-2022.pdf):
>By 'capitalisation' we mean a formal arrangement agreed with the borrower to add all or part of a borrower's arrears to the amount of outstanding principal (i.e. advance of principal including further advances less capital repayments received during the period of the loan) and then treating that amount of overall debt as the enlarged principal. This enlarged principal is then used as the basis for calculating future monthly payments over the remaining term of the loan.


### due
From F6.1i of [MLAR](https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/crd-iv/mlar-notes-may-2022.pdf):
>'Payments due' means amounts due under normal commercial
terms (and not the lesser amounts which may have been agreed
as part of any temporary arrangement) fully to service the loans:
that is the balances outstanding including insurance, fees and fines etc.

### further_advance
From the Annex of the PS22/19 FCA policy [statement](https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/policy-statement/2019/ps2219.pdf):
>A “further advance” means a further loan to an existing borrower of
the firm and which is secured on the same property/collateral, whether under a new loan contract, or by variation to an existing loan
contract.

### interest
Interest due in line with loan conditions

### interest_repayment
 A repayment that covers only the interest section of the loan, the principal borrowed amount in this case is left unchanged

### other
Any other loan transaction type

### received
From F6.1ii of [MLAR](https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/crd-iv/mlar-notes-may-2022.pdf):
>Payments recieved should be limited to regular repayment of
interest, capital and other sundry charges to the loan account,
and should exclude abnormal repayments (e.g. sale proceeds
of property in possession, and large lump sum repayment of
part or all of the outstanding balance). The reasoning behind
this is that excess payments on one or more arrears cases
would otherwise have the effect of compensating for
underpayment on other arrears cases and, as a result, give an
overstated performance measure. Therefore, in compiling
aggregate payment received figures (as part of the payment
performance ratio) the contribution from an individual loan in
arrears should be limited to no more than the 'payment due'
amount.

### sale
Sale of the loan

### write_off
From D1 of [MLAR](https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/crd-iv/mlar-notes-may-2022.pdf):

>This is the amount written off loan balances (and
off provisions charged to the income and expenditure account) and is
to be on a basis consistent with amounts shown in the firm's
published accounts as 'written off' within the analysis of changes in
loss provision.
The amount written off may arise for example from:
>- sale of a property/collateral in possession where there is a shortfall; or
>- a decision to write down the debt on a loan still on
the books. This may arise where the firm has taken the view
that it is certain that a loss will arise and that it is prudent to
write down
>- the debt rather than carry the full debt and an
offsetting provision. Examples might include certain fraud
cases, or where
>- arrangements have been reached with the borrower to reduce
the debt repayable.


---

[crr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013R0575
[card-fees]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv%3AOJ.L_.2015.123.01.0001.01.ENG
[emir]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32012R0648
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
[arrangement]: https://finance.ec.europa.eu/capital-markets-union-and-financial-markets/financial-markets/post-trade-services/financial-collateral-arrangements_en
[uk-isa]: http://www.legislation.gov.uk/uksi/1998/1870/contents/made
[end-date]: https://github.com/suadelabs/fire/blob/master/documentation/properties/end_date.md
[reg-d]: http://www.federalreserve.gov/boarddocs/supmanual/cch/int_depos.pdf
[eba-nsfr-report]: https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-analysis-specific-aspects-net-stable-funding
[fca-covered-bond]: https://www.handbook.fca.org.uk/handbook/glossary/G2083.html
[ucits]: http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ:L:2009:302:0032:0096:en:PDF
[eu-covered-bonds-info]: http://ec.europa.eu/finance/investment/legal_texts/index_en.htm
[sup-rep]: http://publications.europa.eu/resource/cellar/37c79802-fe90-11e3-831f-01aa75ed71a1.0006.03/DOC_1
[2013-549]: https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32013R0549
[sg-stat-boards]: https://www.sgdi.gov.sg/statutory-boards
[mmfr]: https://eur-lex.europa.eu/eli/reg/2017/1131/oj
[us-census-multifamily]: https://www.census.gov/construction/nrc/index.html
[icma-web]: http://dev.icmagroup.org/Regulatory-Policy-and-Market-Practice/repo-and-collateral-markets/legal-documentation/global-master-repurchase-agreement-gmra/
[isda-investo]: https://www.investopedia.com/terms/i/isda-master-agreement.asp
[isda]: https://isda.org
[ira]: https://www.law.cornell.edu/uscode/text/26/408
[cpfb-heloc-you-should-know]: https://files.consumerfinance.gov/f/201401_cfpb_booklet_heloc.pdf
[investopedia-heloc]: https://www.investopedia.com/mortgage/heloc/
[inv-co-act]: https://en.wikipedia.org/wiki/Investment_Company_Act_of_1940
[reits]: https://www.sec.gov/files/reits.pdf
[hedge-fund]: https://www.sec.gov/spotlight/hedgefunds/hedge-vaughn.htm
[hedge-fund2]: https://www.google.com/url?esrc=s&q=&rct=j&sa=U&url=https://www.sec.gov/files/ib_hedgefunds.pdf&ved=2ahUKEwjSgp-x-dn9AhVhoFwKHYbQDrMQFnoECAgQAg&usg=AOvVaw3y7wSB8gmaTml65eMxKBpD
[ecbexamples]: https://www.ecb.europa.eu/pub/pdf/other/ecb-boe_case_better_functioning_securitisation_marketen.pdf
