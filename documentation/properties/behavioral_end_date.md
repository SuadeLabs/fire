---
layout:		property
title:		"behavioral_end_date"
schemas:	[account, loan]
---

# behavioral_end_date

---

The **behavioral_end_date** property represents the weighted average maturity date of as defined in the [Federal Reserve Y-14 Q&As][fed_definition] which includes behavioral assumptions.

> "The Weighted Average Life of Loans should reflect the current position, the impact of new business activity, as well as the impact of behavioral assumptions such as prepayments or defaults, based on the expected remaining lives, inclusive of behavioral assumptions as of month-end. It should reflect the weighted average of time to principal actual repayment (as modeled) for all positions in the segment, rounded to the nearest monthly term."

This is also relevant for UK, European behavioral assumptions for liquiduity run-off analysis.

It is in date-time format in accordance with the ISO 8601 standard (YYYY-MM-DDTHH:MM:SSZ).

---

[fed_definition]: https://www.federalreserve.gov/publications/fr-y-14-qas/fr-y-14-qas-fr-y-14q.htm#:~:text=Weighted%20Average%20Life

