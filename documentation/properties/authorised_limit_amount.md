---
layout:     property
title:      "authorised_limit_amount"
schemas:    [account, loan]
---

# authorised_limit_amount

---
The authorised limit amount represents the total credit limit authorised at a consolidated level. It applies in cases where a limit is shared across multiple borrowers, multiple product types, or both.

This attribute cannot be derived from limit_amount or orig_limit_amount, as those fields reflect instrument-level limits only.

For the Canadian region, the authorised limit amount is required to determine whether transactions qualify for inclusion in the BF or BG schedules. It is used as a reporting filter to support aggregation of authorised limits across parent corporations.


---