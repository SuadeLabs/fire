---
layout:     property
title:      "type"
schemas:    [account, collateral, customer, loan]
---

# type


## Account
"call", "cd", "checking", "current", "internet_only", "isa", "money_market", "nostro", "savings", "time_deposit", "vostro", "other"

## Customer
Article 411 of the [CRR][crr]:
> financial customer‧ means a customer that performs one or more of the activities listed in Annex I to Directive 2013/36/EU as its main business, or is one of the following:
> (a) a credit institution;
> (b) an investment firm;
> (c) an SSPE;
> (d) a CIU;
> (e) a non-open ended investment scheme;
> (f) an insurance undertaking;
> (g) a financial holding company or mixed-financial holding company.


## Loan
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
> It is lending to individuals secured by mortgage on land and buildings where the lender has either a first or second (or subsequent) charge, where at least 40% of the land and buildings is used for residential purposes, and where the premises are for occupation by either the borrower (or dependant), or any other third party (e.g. it includes ‘buy to let’ lending to individuals).
Only loans where there is a one-to-one correspondence between the loan and a specific security should be included within ‘residential loans to individuals’. 
 
### credit_card
A **credit_card** is credit facility typically secured by a deposit account or equity in the borrower's property.

### other_credit_facility

### overdraft
*put as loan type or deduce from a negative balance?*

---
[crr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013R0575
[lcr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0061
[mlar]: http://www.bankofengland.co.uk/pra/documents/regulatorydata/mlar/sup_chapter16_annex19bg_20120401.pdf
