---
layout:     property
title:      "repurchase_status"
schemas:    [loan]
---

# repurchase_status

---

```bash
├── complete_no_repurchased
├── complete_repurchased
├── in_process
└── initiated
```

Indicates the current status of any repurchase request for the loan. This field tracks whether a repurchase request has been made, is pending review, has been approved, or has been rejected.

### complete_no_repurchased
A request was been made for repurchase of the loan by the counterparty and has concluded with the property not being repurchased.

### complete_repurchased
A request was been made for repurchase of the loan by the counterparty and has concluded with the property being repurchased.

### in_process
A request has been made for repurchase of the loan by the counterparty. This include both loans where repurchase is being finalized and loans where agreement to repurchase has not yet occurred.

### initiated
The bank voluntarily initiated a repurchase. 