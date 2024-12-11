---
layout:     property
title:      "netting_restriction"
schemas:    [agreement]
---

# netting_restriction

By default, **netting_restriction** is not populated when netting is recognized and the agreement is risk-reducing as per CRR Articles 295 to 298.
When netting recognition does not aplly to the agreement, **netting_restriction** specifies the nature of the non-recognition:

### national_supervision
The national supervisor is not satisfied that the netting is enforceable under the laws of each of the relevant jurisdictions (after consultation with other relevant supervisors, when necessary). Thus,if any of these supervisors is dissatisfied about enforceability under its laws, the netting contract or agreement will not meet this condition and neither counterparty could obtain supervisory benefit.

### no_set_off_right
SFTs will not meet the condition allowable to net the cash payable and receivable if the mna_id does not include the legally enforceable right to offset or where there is no intent to settle on a net basis or simultaneously. Therefore the SFT payable and receivable cashflows will be reported gross if no_set_off_right is applied under netting_restriction. Further detail is available under [Article 429b(4) of CRR][settlement-rights]

### restrictive_covenant
The netting contract contains clauses which, in the event of default of a counterparty, permits a non-defaulting counterparty to make limited payments only, or no payments at all, to the estate of the defaulting party, even if the defaulting party is a net creditor.

[settlement-rights]: https://www.prarulebook.co.uk/pra-rules/leverage-ratio-crr/3-leverage-ratio-part-seven-crr/article-429b-calculation-of-the-exposure-value-of-assets/05-12-2024?p=1
