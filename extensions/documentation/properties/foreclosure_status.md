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
├── none
├── in_foreclosure_presale
├── post_sale_redemption
└── reo
```

### none
No Foreclosure - The property is not in any stage of the foreclosure process. This status applies to loans that are current or in other stages of delinquency management.

### in_foreclosure_presale
In Foreclosure Pre-Sale - The property is in the active foreclosure process but has not yet been sold at auction. This includes the period from the initiation of foreclosure proceedings up to the foreclosure sale date.

### post_sale_redemption
Post-Sale Redemption - The property has been sold at foreclosure auction, but the borrower still has the right to redeem the property by paying the full amount owed within a specified redemption period, as allowed by state law.

### reo
Real Estate Owned - The property has completed the foreclosure process and is now owned by the lender. This status applies after the foreclosure sale has been completed and any redemption period has expired without the borrower redeeming the property.

--- 