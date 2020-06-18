---
layout:		property
title:		"margin_frequency"
schemas:	[agreement]
---

# margin_frequency

In a credit support annex, the **margin_frequency** is the periodic timescale at which variation margin is exchanged. Can be one of the following values:
    - "daily", "weekly", "daily_settled"
Cleared derivatives which are settled daily can be flagged as daily_settled."

## Magin frequency in regulation

In the [Margin Requirements for non-cleared derivatives][bcbs_317], a **sufficient** frequency for exchanging variation margin is defined as **daily**.
In the [CRR][CRR], the **margin_frequency** is used in Article 285 in order to derive the margin period of risk.

---
[bcbs_317]: https://www.bis.org/bcbs/publ/d317.pdf
[CRR]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02013R0575-20191225