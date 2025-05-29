---
layout:     property
title:      "repurchase_status"
schemas:    [loan]
---

# repurchase_status

---

```bash
├── complete_no_repurchase
├── complete_repurchased
└── in_process
```

Indicates the current status of any repurchase request for the loan. This field tracks whether a repurchase request has been made, is pending review, has been approved, or has been rejected.

### complete_no_repurchase

The repurchase process has been completed and the decision was made not to repurchase the loan. This is a final status indicating the loan will remain in its current state.

### complete_repurchased

The repurchase process has been completed and the loan has been successfully repurchased. This is a final status indicating the loan has been returned to the original holder.

### in_process

The repurchase request is currently being processed. This status indicates that a repurchase request has been made and is actively being reviewed or executed. 