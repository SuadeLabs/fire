---
layout:     property
title:      "orig_imp_status"
schemas:    [loan]
---

# orig_imp_status

---

The impairment_status at origination.

```bash
├── performing
│   ├── stage_1
│   │   ├── normal (aka pass)
│   │   └── watch (aka special mention)
│   └── stage_2
│       └── substandard
├── non_performing
│   └── stage_3
│       ├── doubtful
│       ├── loss
│       ├── in_litigation
│       └── pre_litigation
├── stage_1_normal
├── stage_1_watch
├── stage_1_substandard
├── stage_1_doubtful
├── stage_1_loss
├── stage_2_normal
├── stage_2_watch
├── stage_2_substandard
├── stage_2_doubtful
├── stage_2_loss
├── stage_3_normal
├── stage_3_watch
├── stage_3_substandard
├── stage_3_doubtful
└── stage_3_loss

```

--- 