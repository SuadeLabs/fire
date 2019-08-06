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

### securitised
This loan has been packaged or securitised with one or more loans.

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

### other
Needs definition

### debt_issue
(so not use - see *issuance*)

### issuance
A a securities issuance of stocks or bonds (determined by the security - *type*)

