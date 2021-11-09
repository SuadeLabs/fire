---
layout:		property
title:		"margin_frequency"
schemas:	[agreement]
---

# margin_frequency

```bash
├── daily
│   └── daily_settled
├── weekly
├── bi_weekly
└── monthly
```

In a credit support annex, the **margin_frequency** is the periodic timescale at which variation margin is exchanged.
In the [Margin Requirements for non-cleared derivatives][bcbs_317], a *sufficient* frequency for exchanging variation margin is defined as **daily**.
In the [CRR][CRR], the **margin_frequency** is used in Article 285 in order to derive the margin period of risk.

### daily
Margining occurs on a daily basis.

### daily_settled
Margining occurs on a daily basis and is also settled daily. (like when facing a ccp)

### weekly
Margining occurs on a weekly basis.

### bi_weekly
Margining occurs on a bi_weekly basis.

### monthly
Margining occurs on a monthly basis.


---
[bcbs_317]: https://www.bis.org/bcbs/publ/d317.pdf
[CRR]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02013R0575-20191225
