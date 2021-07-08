---
layout:		property
title:		"margin_period_of_risk"
schemas:	[agreement]
---

# margin_period_of_risk

The **margin_period_of_risk** attributre (expressed in business days) allows institutions to provide their own estimate of the margin period of risk (MPOR) used to calculate the maturity factor for margined transactions. (CRR Art 279c(1)(b)). 
- If left empty, the MPOR will be set to the regulatory floor defined in Art. 285(2) to (5), except for netting sets where the number of trades exceeds 5 000 at any point during the previous quarter, in which case a value of 20 business days shall be populated;
- Where an institution acts as a clearing member, resp. client to a clearing member, a value of 5 business days can be populated for its exposures to a client, resp. to the clearing member (a margin period of risk of at least 10 business days will be used for its exposures to a CCP and the field can be left empty);
If a number different from 5 or 20 is provided, the maturity factor will be calculated with that number, subject to the regulatory floor. 

---
[CRE52]: https://www.bis.org/basel_framework/chapter/CRE/52.htm?tldate=20201231&inforce=20220101