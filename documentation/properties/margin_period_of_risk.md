---
layout:		property
title:		"margin_period_of_risk"
schemas:	[agreement]
---

# margin_period_of_risk

The **margin_period_of_risk** attribute (expressed in business days) allows institutions to provide their own estimate of the margin period of risk (MPOR) used to calculate the maturity factor for margined transactions. (CRR Art 279c(1)(b)). 

If left empty, the MPOR should be assumed to be equal to the regulatory floor defined in CRR Art. 285(2) of 5, 10 or 20 business days:
> 2. For transactions subject to daily re-margining and mark-to-market valuation, the margin period of risk used for the purpose of modelling the exposure value with margin agreements shall not be less than:  
> (a) 5 business days for netting sets consisting only of repurchase transactions, securities or commodities lending or borrowing transactions and margin lending transactions;  
> (b) 10 business days for all other netting sets.  
> 3. Points (a) and (b) of paragraph 2 shall be subject to the following exceptions:  
> (a) for all netting sets where the number of trades exceeds 5 000 at any point during a quarter, the margin period of risk for the following quarter shall not be less than 20 business days. This exception shall not apply to institutions' trade exposures;  
> (b) for netting sets containing one or more trades involving either illiquid collateral, or an OTC derivative that cannot be easily replaced, the margin period of risk shall not be less than 20 business days.  


---
[CRE52]: https://www.bis.org/basel_framework/chapter/CRE/52.htm?tldate=20201231&inforce=20220101
