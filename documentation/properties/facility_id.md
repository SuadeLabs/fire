---
layout:     property
title:      "facility_id"
schemas:    [loan, account]
---

# facility_id

---

Represents the identifier used to group transactional information for an individual instrument within a parent_facility_id.
Where a parent_facility_id contains multiple instruments, facility_id is used to group the transactions belonging to each individual instrument within the parent facility.
facility_id is only required where it is necessary to distinguish or group transactional data for reporting purposes. It is not required where the information is already provided at an aggregated level or where no additional instrument-level grouping is necessary
---