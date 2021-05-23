---
layout:		property
title:		"start_date"
schemas:	[account, collateral, customer, derivative_cash_flow, derivative, loan, security]
---

# start_date

---

The **start_date** represents the contractual date of commencement of the financial product. This may corresponds to:
    - the effective date for swap and option contracts,
    - the issue date of a security
    - the start date of a SFT
    - any other specific attribute which denotes the date at which a financial contract takes effect
It is in date-time format in accordance with the ISO 8601 standard (YYYY-MM-DDTHH:MM:SSZ).

See also [**date**][date] and [**issue_date**][issue_date]

---

[date]: 		https://github.com/suadelabs/fire/blob/master/documentation/properties/date.md
[issue_date]:       https://github.com/suadelabs/fire/blob/master/documentation/properties/issue_date.md