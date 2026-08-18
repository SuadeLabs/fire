---
layout:     property
title:      "contribution_amount"
schemas:    [adjustment]
---

# contribution_amount

---

The **contribution_amount** reflects the amount that the adjustment contributes to to the reportable value (in a report/cell). If a currency_code is present, this amount is taken to be monetary in minor currency of the corresponding currency. If no currency code is present, this amount is taken as-is and assumed to be non-monetary (e.g. a percentage or risk weight). Implementation of contributions may differ, but are typically  additive so that multiple contributions can be aggregated.
