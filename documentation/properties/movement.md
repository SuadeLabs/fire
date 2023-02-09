---
layout:		property
title:		"movement"
schemas:	[loan_transaction, loan, security]
---
# movement

---

The **movement** parameter describes how an asset or liability arrived to the firm.

# loan

### acquired

This loan has been acquired on its own or part of a larger portfolio acquisition from another firm or has been acquired due to a group restructuring or acquisition.

### acquired_impaired

These assets are those which are "credit impaired" at the time of purchase. For these assets, events that have a detrimental impact on the estimated future cash flows have already occurred. Also known as "Purchased or Originated credit-impaired" assets

### securitised

This loan has been packaged or securitised with one or more loans.

**The [REGULATION OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL][eu] laying down common rules on securitisation and creating a European framework for simple, transparent and standardised securitisation and amending Directives 2009/65/EC, 2009/138/EC, 2011/61/EU and Regulations (EC) No 1060/2009 and (EU) No 648/2012 states that**:

> "Securitisation refers to transactions that enable a lender or other originator of assets – typically a credit institution – to refinance a set of loans or assets (e.g. mortgages, auto leases, consumer loans, credit cards) by converting them into securities. The lender or originator organises a portfolio of its loans into different risk categories, tailored to the risk/reward appetite of investors. Returns to investors are generated from the cash flows of the underlying loans. These markets are not aimed at retail investors."


### sold
This loan has been sold to another firm and has left the balance sheet. Data may continue to be kept for record-keeping or reporting purposes.

### syndicated
A syndicated loan is one that is provided by a group of lenders and is structured, arranged, and administered by one or several commercial banks or investment banks known as lead arrangers.

### syndicated_lead
The lead bank on a syndicated loan. (see *syndicated*)

### other
None of the above.


# security

### cash
The cash leg of a securities financing transaction such as a repo or reverse repo.

### asset
The stock/asset leg of a securities financing transaction such as a repo or reverse repo.

### cb_omo
From Central Bank Open Market Operations

### debt_issue
(do not use - see *issuance*)

### issuance
A a securities issuance of stocks or bonds (determined by the security - *type*)

### other
*Needs definition*

[eu]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52015PC0472
