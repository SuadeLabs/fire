---
layout:		property
title:		"mna_id"
schemas:	[derivative, derivative_cash_flow, security]
---

# mna_id

The **mna_id** is the unique identifier of the Master Netting Agreement the security/derivative falls under. Typically where used as derivatives collateral.

## Master Netting Agreement (MNA)
The **MNA** refers to the netting agreement defined in the [CRR][crr] Article 296:

2. The following conditions shall be fulfilled by all contractual netting agreements used by an institution for the purposes of determining exposure value in this Part:

> (a) the institution has concluded a contractual netting agreement with its counterparty which creates a single legal obligation, covering all included transactions, such that, in the event of default by the counterparty it would be entitled to receive or obliged to pay only the net sum of the positive and negative mark-to-market values of included individual transactions;

> (c) credit risk to each counterparty is aggregated to arrive at a single legal exposure across transactions with each counterparty. This aggregation shall be factored into credit limit purposes and internal capital purposes;

> (d) the contract shall not contain any clause which, in the event of default of a counterparty, permits a non-defaulting counterparty to make limited payments only, or no payments at all, to the estate of the defaulting party, even if the defaulting party is a net creditor (i.e. walk away clause).

---
[crr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013R0575
