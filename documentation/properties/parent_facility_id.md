---
layout:     property
title:      "parent_facility_id"
schemas:    [loan, account]
---

# parent facility_id

---

Represents the identifier of a facility created under a loan contract or agreement.
A loan contract or agreement can contain one or multiple facilities. Each facility can contain one or multiple instruments and can be associated with one or multiple counterparties.
Accordingly:
One loan contract or agreement can contain one or multiple parent_facility_id values.
One parent_facility_id can contain one or multiple instruments.
One parent_facility_id can be associated with one or multiple counterparties.
A shared facility may therefore have the same parent_facility_id reported for multiple counterparties.
A linked facility can have multiple instruments reported under the same parent_facility_id.
---