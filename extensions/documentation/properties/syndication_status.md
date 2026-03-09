---
layout:     property
title:      "syndication_status"
schemas:    [loan]
---

# syndication_status

---

Specifies the execution status of the syndication agreement for the loan, indicating whether the commitment is unsigned, partially signed, or fully closed and settled among participants.

```bash
├── closed_not_settled
├── closed_settled
├── dual_signed
└── single_signed
```

### closed_not_settled
Loan documents are fully executed but participant funding/execution is still pending.

### closed_settled
Loan documents are fully executed and binding, with post-closing sell-down to all participants complete.

### dual_signed
Syndication agreement signed by both the lead institution and the borrower.

### single_signed
Syndication agreement signed only by the lead institution.

--- 