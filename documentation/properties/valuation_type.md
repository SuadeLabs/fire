---
layout:     property
title:      "valuation_type"
schemas:    [collateral, security]
---

# valuation_type

---

Methodology used in the determination of the collateral value.

For more information, refer to:
- https://www.ecfr.gov/current/title-12/chapter-VI/subchapter-B/part-614/subpart-F/section-614.4265
- https://www.federalreserve.gov/boarddocs/srletters/2010/sr1016a1.pdf
- AnaCredit Manual part 2, Chapter 9.4.6 https://www.banque-france.fr/fr/system/files/2023-08/banque_de_france_espace_declarants_anacredit_manual_part_ii_datasets_and_data_attributes_201905.en_.pdf/#page=231

# collateral

```bash
├── auto_val_model
├── broker_price
├── counterparty
├── creditor
├── desktop
├── full
├── limited
├── mtm
├── other
├── prospective_market_value
│   ├── as_completed
│   ├── as_is
│   └── as_stabilized
├── purchase_price
├── tav
└── third_party
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

### counterparty
Counterparty estimation - A valuation method whereby the valuation is carried out by the protection provider.

Reference: AnaCredit Reporting Manual Part II, chapter 9.4.6 Protection valuation approach

### creditor
Creditor valuation is a valuation method whereby the valuation is carried out by the creditor. The valuation may be undertaken by an external or staff appraiser who possesses the necessary qualifications, ability and experience to execute a valuation and who is not independent from the credit decision process.

Reference: AnaCredit Reporting Manual Part II, chapter 9.4.6 Protection valuation approach

### desktop
Desktop Appraisal - A property valuation that relies on publicly available data and records without a physical inspection of the property.

### full
Full Appraisal - A comprehensive property valuation that includes a physical inspection of both the interior and exterior of the property, along with detailed market analysis.

### limited
Limited Appraisal - A property valuation that includes a physical inspection but may have a more limited scope than a full appraisal, often focusing on specific aspects of the property.

### mtm
Mark-to-market is a valuation method whereby the protection value is based on unadjusted prices quoted at an exchange for identical assets and liabilities in an active market.

Reference: AnaCredit Reporting Manual Part II, chapter 9.4.6 Protection valuation approach

### other
Definition: Other type of valuation is any other type of valuation that is not included in the previous categories of valuation approaches. 

Reference: AnaCredit Reporting Manual Part II, chapter 9.4.6 Protection valuation approach

### prospective_mkt_value

Prospective Market Value - A valuation provided by an appraiser for a property interest related to a credit decision for a proposed development or renovation project, based on the condition of the property at a specified stage of its development or renovation.

### purchase_price
Purchase Price - The actual price paid for the property in a recent transaction, used as the basis for valuation.

### tav
Transaction Automated Valuation - An automated valuation that is specifically tied to a transaction, using transaction-specific data points to determine the property value.

### third_party
Third-party valuation is a valuation method in which the valuation is provided by an appraiser who is independent of the credit decision process.

Reference: AnaCredit Reporting Manual Part II, chapter 9.4.6 Protection valuation approach

# security

```bash
├── counterparty
├── creditor
├── mtm
├── other
└── third_party
```

### counterparty
Counterparty estimation - A valuation method whereby the valuation is carried out by the protection provider.

Reference: AnaCredit Reporting Manual Part II, chapter 9.4.6 Protection valuation approach

### creditor
Creditor valuation is a valuation method whereby the valuation is carried out by the creditor. The valuation may be undertaken by an external or staff appraiser who possesses the necessary qualifications, ability and experience to execute a valuation and who is not independent from the credit decision process.

Reference: AnaCredit Reporting Manual Part II, chapter 9.4.6 Protection valuation approach

### mtm
Mark-to-market is a valuation method whereby the protection value is based on unadjusted prices quoted at an exchange for identical assets and liabilities in an active market.

Reference: AnaCredit Reporting Manual Part II, chapter 9.4.6 Protection valuation approach

### other
Definition: Other type of valuation is any other type of valuation that is not included in the previous categories of valuation approaches. 

Reference: AnaCredit Reporting Manual Part II, chapter 9.4.6 Protection valuation approach

### third_party
Third-party valuation is a valuation method in which the valuation is provided by an appraiser who is independent of the credit decision process.

Reference: AnaCredit Reporting Manual Part II, chapter 9.4.6 Protection valuation approach

--- 