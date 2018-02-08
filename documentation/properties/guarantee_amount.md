---
layout:     property
title:      "guarantee_amount"
schemas:    [account]
---

# guarantee_amount

---

The **guarantee_amount** is the amount covered for the deposit account under the corresponding [**guarantee_scheme**][gscheme]. Firms should ensure that this number corresponds to Member State requirement "that the coverage level for the aggregate deposits of each depositor is EUR 100 000 in the event of deposits being unavailable." [&#185;][1]

So if a customer has multiple accounts protected under the same guarantee scheme, the sum of the guarantee amounts in each of those accounts should equal EUR 100 000 or the national equivalent.

---

[1]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32014L0049
[gscheme]: https://github.com/suadelabs/fire/blob/master/documentation/properties/guarantee_scheme.md
