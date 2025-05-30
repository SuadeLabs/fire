---
layout:     property
title:      "foreclosure_status"
schemas:    [loan]
---

# foreclosure_status

---

Indication of the status of a foreclosure.

For additional details refer to: https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14M


```bash
├── post_sale
│   └── post_sale_susp
├── pre_sale
│   └── pre_sale_susp
└── reo
    └── reo_susp
```

### post_sale
A loan where the bank has obtained title at foreclosure sale, but the property is not yet actively being marketed. Typically this will include loans that are in redemption or being repaired.

### post_sale_susp
A loan where the bank has obtained title at foreclosure sale, but the property is not yet actively being marketed and the foreclosure activities are suspended. Typically this will include loans that are in redemption or being repaired.

### pre_sale
A mortgage that has been referred to an attorney for loss mitigation proceedings but has not yet gone to foreclosure sale.

### pre_sale_susp
A mortgage that has been referred to an attorney for loss mitigation proceedings but has not yet gone to foreclosure sale and the foreclosure activities are suspended.

### reo
A mortgage where the bank has obtained title at foreclosure sale and the property is on the market and available for sale. Also used where the bank has obtained title but the availability for sale is not known.

### reo_susp
A mortgage where the bank has obtained title at foreclosure sale, the property is on the market and available for sale but the foreclosure activities are suspended. Also used where the bank has obtained title but the availability for sale is not known.

--- 