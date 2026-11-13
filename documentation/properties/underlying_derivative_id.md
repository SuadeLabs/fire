---
layout:     property
title:      "underlying_derivative_id"
schemas:    [derivative]
---

# underlying_derivative_id

---

The **underlying_derivative_id** attribute identifies the derivative that is itself the underlying reference for the reported derivative and is a string field.

A swaption is an example of a derivative with another derivative as its underlying. [ESMA Guidelines for reporting under EMIR, Section 5.2, paragraph 411, page 191][emir] requires both option and underlying-swap characteristics in the report. FIRE uses this field to link to the underlying derivative record.

[emir]: https://www.esma.europa.eu/sites/default/files/library/esma74-362-2281_final_report_guidelines_emir_refit.pdf#page=192
