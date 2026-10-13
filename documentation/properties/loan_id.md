---
layout:     property
title:      "loan_id"
schemas:    [loan_cash_flow, loan_transaction]
---

# loan_id

---

The **loan_id** attribute identifies the loan to which a transaction or cash flow relates and is a string field.

FIRE uses `loan_id` as the institution's identifier for the linked loan record. A regulatory example of stable instrument identification is [AnaCredit Regulation (EU) 2016/867, Annex I, Template 1, points 2.1–2.2][anacredit], which defines the instrument record key and the scope within which contract and instrument identifiers must remain unique.

[anacredit]: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0867#:~:text=Each%20contract%20identifier%20must%20be%20unique
