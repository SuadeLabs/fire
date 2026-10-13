---
layout:     property
title:      "account_ids"
schemas:    [collateral]
---

# account_ids

---

The **account_ids** attribute records the internal identifiers of the account positions secured by, or otherwise linked to, a collateral item and is an array of strings.

Prudential datasets need stable identifiers to link collateral to exposures. [AnaCredit Regulation (EU) 2016/867, Annex I, Template 1, points 2.1–2.2][anacredit] specifies the instrument record key and prohibits reuse of contract and instrument identifiers within their respective scopes. FIRE uses internal account identifiers as an array because one collateral object may relate to several accounts.

[anacredit]: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0867#:~:text=Each%20contract%20identifier%20must%20be%20unique
