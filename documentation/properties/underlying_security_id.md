---
layout:     property
title:      "underlying_security_id"
schemas:    [derivative]
---

# underlying_security_id

---

The **underlying_security_id** attribute identifies the security that serves as the underlying reference for the derivative and is a string field.

See [ESMA Guidelines for reporting under EMIR, Section 4.16, paragraph 246, page 160][emir] for identification of an underlying asset by ISIN. FIRE stores the institution's identifier for the underlying security separately from the derivative's own identifier; an external reporting code may be obtained from the linked security record.

[emir]: https://www.esma.europa.eu/sites/default/files/library/esma74-362-2281_final_report_guidelines_emir_refit.pdf#page=161
