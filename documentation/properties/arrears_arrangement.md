---
layout:		property
title:		"arrears_arrangement"
schemas:	[loan]
---

# arrears_arrangement

---

The **arrears_arrangement** is the property of a loan (debt) that describes how the borrower and lender are dealing with the unpaid capital or interest payments indicated in the **arrears_balance**. An arrears_arrangement does not necessarily require a positive arrears_balance as an arrangement may be reached between lender and borrower in anticipation of a future arrears situation eg. *Forbearance*. Forbearance is not an extremely well-defined concept within accounting standards. As such we have adopted the [forbearance definitions and categorisation adopted by the EBA][eba-forbearance-its] and used in the [Finrep ITS][finrep-its]. See also: [BBVA research paper on the topic][bbva-forbearance].

[eba-forbearance-its]: https://www.eba.europa.eu/implementing-technical-standard-supervisory-reporting-forbearance-and-non-performing-exposures
[bbva-forbearance]: https://www.bbvaresearch.com/wp-content/uploads/2017/12/2017-12-IFRS-9-Impact-on-forbearance-practices.pdf
[finrep-its]: https://eba.europa.eu/sites/default/documents/files/documents/10180/2321183/b67323ac-27fa-482d-926e-ae7ba3e90cb8/Annex%20III%20%28Annex%205%20%28FINREP%29%29.pdf

### temporary
This indicates cases where the lender has made a temporary concession to the borrower to assist them with their payments of the **arrears_balance**.
From [MLAR][mlar]:
> agreement with the borrower whereby monthly payments are either suspended or less than they would be on a fully commercial basis

### formal
This indicates that a formal arrangement has been agreed with the borrower to capitalise the loan with the view to decrease the **arrears_balance** with future payments.

### none
No temporary or formal arrangement or contact has been made with the borrower to "solve" the balance outstanding in the **arrears_balance**.

### possessed
Cases where the underlying collateral has been seized or taken into possession by the lender.

From [MLAR][mlar]:
> In possession: cases should be included here where the property is
F3.6/F4.6 taken in possession (through any method e.g. voluntary surrender, court
order etc). For development loans in particular, cases should also be
included where the appointment of a receiver and/or a manager has been
made, or where the security is being enforced in other ways (which may
or may not also involve the existence of arrears e.g. building finance case
with interest roll up, no arrears, but a current valuation is less than the
outstanding debt).


[mlar]: http://www.bankofengland.co.uk/pra/documents/regulatorydata/mlar/sup_chapter16_annex19bg_20120401.pdf

### modified_tnc
A modification of the previous terms and conditions of a contract that the debtor is considered unable to comply with due to its financial difficulties ("troubled debt") resulting in insufficient debt service ability and that would not  have  been  granted  had  the  debtor  not  been  experiencing  financial  difficulties (in relation to forbearance status).

### refinancing
A total or partial refinancing of a troubled debt contract, that would not have been granted had the debtor not been experiencing financial difficulties (in relation to forbearance status).

### interest_grace_period
Where the lender has provided a period before payment becomes due for interest not to be applied (as an arrangement) after a product has gone into arrears. This should not be confused with products where an initial/promotional interest-free period is granted. Those cases should be identified using the "reversion_date" and "reversion_rate" properties.
