---
layout:		property
title:		"status"
schemas:	[account, customer, loan]
---

# status

---

The **status** property indicates the current state of the financial product. A product can be active, cancelled, defaulted, committed etc. This is generally used to differentiate potential offers committed by the institution (lending decision taken) but not yet accepted by a customer. The status could also indicate liabilities which have been cancelled but are still being held within the dataset (until maturity or otherwise).

# account
### active
The account is active and in use by the customer.

### transactional
The account is active in a transactional way, *transactional* being defined in accordance with the [Liquidity Regulations][lcr]:
> LCR Article 24(3):
> For the purposes of paragraph 1(b) a retail deposit shall be considered
> as being held in a transactional account where salaries, income or
> transactions are regularly credited and debited respectively against
> that account.

### cancelled
The account has been cancelled but funds will be rolled-over in to another account on the [**end_date**](https://github.com/SuadeLabs/fire/blob/master/documentation/properties/end_date.md).

### cancelled_payout_agreed
The account has been cancelled and the funds are known to be leaving the financial institution.

# loan
### actual
This is a live loan.

### committed
This is a loan offer or commitment to a customer that a customer could draw down (typically also denoted as off balance sheet).

### cancelled
This is a loan that was committed but then later cancelled due to refusal by customer or expiry of offer.

### defaulted
This is a loan where the customer has defaulted or is non-performing.


[lcr]:  http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0061
