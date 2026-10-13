---
layout:     property
title:      "underlying_strike"
schemas:    [derivative]
---

# underlying_strike

---

The **underlying_strike** attribute is the strike price used to compare the underlying value with the option terms on exercise and is a numeric field.

Strike is a contractual option term. For a regulatory example, [ESMA Guidelines for reporting under EMIR, Section 5.2.1, Table 28, page 193][emir] reports the strike separately in field 2.134 for a swaption. FIRE stores the strike directly as a numeric value.

[emir]: https://www.esma.europa.eu/sites/default/files/library/esma74-362-2281_final_report_guidelines_emir_refit.pdf#page=194
