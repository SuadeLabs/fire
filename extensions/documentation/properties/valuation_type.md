---
layout:     property
title:      "valuation_type"
schemas:    [collateral]
---

# valuation_type

---

Methodology used in the determination of the collateral value.

For more information, refer to:
- https://www.ecfr.gov/current/title-12/chapter-VI/subchapter-B/part-614/subpart-F/section-614.4265
- https://www.federalreserve.gov/boarddocs/srletters/2010/sr1016a1.pdf

```bash
├── auto_val_model
├── broker_price
├── desktop
├── full
├── limited
├── prospective_market_value
│   ├── as_completed
│   ├── as_is
│   └── as_stabilized
├── purchase_price
└── tav
```

### as_completed

The prospective market value of the property as of the date construction or renovation is expected to be completed, assuming all proposed improvements are finished according to the plans and specifications.

### as_is

The prospective market value of the property in its actual physical condition, use, and zoning as of the appraisal’s effective date, reflecting any deductions or discounts for incomplete construction, non-market leases, or other existing conditions.

### as_stabilized

The prospective market value of the property as of the date it is projected to achieve stabilized occupancy, representing the point when the property reaches typical market-level performance after lease-up or renovation.

### auto_val_model
Automated Valuation Model (AVM) - A computer-driven mathematical model that uses property characteristics, location, and market conditions to determine property values without a physical inspection.

### broker_price
Broker Price Opinion (BPO) - A professional estimate of a property's value provided by a real estate broker or agent, typically based on comparable sales and market analysis.

### desktop
Desktop Appraisal - A property valuation that relies on publicly available data and records without a physical inspection of the property.

### full
Full Appraisal - A comprehensive property valuation that includes a physical inspection of both the interior and exterior of the property, along with detailed market analysis.

### limited
Limited Appraisal - A property valuation that includes a physical inspection but may have a more limited scope than a full appraisal, often focusing on specific aspects of the property.

### prospective_market_value

Prospective Market Value - A valuation provided by an appraiser for a property interest related to a credit decision for a proposed development or renovation project, based on the condition of the property at a specified stage of its development or renovation.

### purchase_price
Purchase Price - The actual price paid for the property in a recent transaction, used as the basis for valuation.

### tav
Transaction Automated Valuation - An automated valuation that is specifically tied to a transaction, using transaction-specific data points to determine the property value.

--- 