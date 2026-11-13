---
layout:     property
title:      "derivative_id"
schemas:    [derivative_cash_flow]
---

# derivative_id

---

The **derivative_id** attribute links a derivative cash flow back to the derivative contract that generated it and is a string field.

The [FIRE derivative cash-flow schema, `derivative_id` property][schema] defines the link to the derivative that generated the cash flow. This is the institution's record identifier; it is not necessarily an EMIR unique trade identifier (UTI).

[schema]: https://github.com/SuadeLabs/fire/blob/master/schemas/derivative_cash_flow.json#:~:text=Unique%20identifier%20to%20the%20derivative%20to%20which%20this%20cash%20flow%20relates
