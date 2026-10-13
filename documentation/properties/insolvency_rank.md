---
layout:     property
title:      "insolvency_rank"
schemas:    [account, derivative, security]
---

# insolvency_rank

---

The **insolvency_rank** attribute captures the priority of a claim or instrument in the applicable insolvency hierarchy and is a positive integer.

This is a legal ordering concept. [Bank Recovery and Resolution Directive 2014/59/EU, Article 108 (Ranking in insolvency hierarchy)][brrd-eur-lex] addresses creditor ranking in bank insolvency. FIRE stores the rank as understood under the applicable national legal framework; the numeric representation is a FIRE convention.

Read the [EUR-Lex consolidated text (14 November 2024)][brrd-eur-lex] or the corresponding [EBA Single Rulebook entry][brrd].

[brrd]: https://www.eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/14050
[brrd-eur-lex]: https://eur-lex.europa.eu/eli/dir/2014/59/2024-11-14/eng#:~:text=Ranking%20in%20insolvency%20hierarchy
