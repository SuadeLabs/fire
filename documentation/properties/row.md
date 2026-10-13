---
layout:     property
title:      "row"
schemas:    [adjustment]
---

# row

---

The **row** attribute identifies the report row to which an adjustment applies and is a string field.

Together with `report_type` and `col`, this locates the reporting cell being adjusted. For an example of regulatory row codes, see [Regulation (EU) 2024/3117, Annex I, template C 01.00 (Own funds), page 21][reporting]. FIRE stores the row code as a string so leading zeroes are retained.

It is best to check with your software provider for a full list of applicable row codes by report (this list would be too long to enumerate here).

[reporting]: https://www.mfsa.mt/wp-content/uploads/2025/10/ITS-on-Supervisory-Reporting-Regulation-EU-2024_3117.pdf#page=21
