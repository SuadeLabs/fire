---
layout:     property
title:      "transmission_indicator"
schemas:    [security, derivative]
---

# transmission_indicator

Some firms do not execute client orders for financial instruments but rather they transmit them to another firm to be executed. The purpose of this property is to indicate that there was a transmission within a chain to another investment firm that did not meet the conditions of Article 4 of [Commission Delegated Regulation (EU) 2017/590][rts]. 

### true
This indicates that the conditions set out in Article 4 of [Commission Delegated Regulation (EU) 2017/590][rts] were not met. For example, Article 4 requires details such as the identification code of the financial instrument to be transferred to the receiving investment firm. 

### false
This field should be populated in all other circumstances. For example, this field may be populated by a firms who is executing a trade directly on a trading venue.

---


[rts]: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32017R0590

