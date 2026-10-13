---
layout:     property
title:      "loan_ids"
schemas:    [collateral]
---

# loan_ids

---

The **loan_ids** attribute records the identifiers of the loans secured by, or associated with, the collateral item and is an array of strings.

This relationship key links collateral to one or more protected loans. [AnaCredit Regulation (EU) 2016/867, Annex I, Template 2, points 8.1–8.2][anacredit] similarly records instrument-protection combinations using both instrument and protection identifiers. FIRE stores the linked loan identifiers in this array.

[anacredit]: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0867#:~:text=The%20level%20of%20granularity%20for%20the%20instrument%2Dprotection%20received%20data
