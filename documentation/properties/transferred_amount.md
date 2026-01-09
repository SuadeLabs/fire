---
layout:		property
title:		"transferred_amount"
schemas:	[loan]
---

# transferred_amount

Transferred amount of the economic ownership of the financial asset.

From [AnaCredit Manual part 2: 4.4.3 Transferred amount][transferred-amount]:  
> This data attribute captures the part of the outstanding nominal amount that has been transferred to another creditor. Please note that this data attribute refers to the amount transferred to third parties rather than amounts acquired from third parties. This data attribute is primarily relevant in the case of transferred instruments, and in particular transferred as part of a traditional securitisation scheme. 
>
>Transferred instruments are those that have been granted or acquired by the observed agent and legally transferred (sold) to third parties but are still subject to reporting agent because it retains the servicing rights of the instrument, regardless of whether the amount reported is in the balance sheet of the observed agent (i.e. regardless of whether the instrument is entirely or partially recognised in the balance sheet).
> 
>Regarding instruments that are fully transferred (sold) to a third party and are no longer serviced by the observed agent, the observed agent does not report such instruments to AnaCredit any longer after the transfer date, irrespective of whether or not the transfer date is a quarter-end date. However, in the case of transferred instruments for which a write-off has occurred, the observed agent reports such instruments until at least the quarter-end date of the quarter in which the transfer takes place.
---
[transferred-amount]: https://www.ecb.europa.eu/pub/pdf/other/AnaCredit_Manual_Part_II_Datasets_and_data_attributes_201905~cc9f4ded23.en.pdf#page=85