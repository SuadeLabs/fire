---
layout:     property
title:      "birr_curve_id"
schemas:    [customer, issuer, guarantor]

---

# birr_curve_id

---

The **birr_curve_id** represents the unique identifier of a curve containing historical Borrower Internal Risk Ratings (BIRR) for an entity. The referenced curve must be of type 'risk_rating'.

This property allows for tracking the historical evolution of an entity's internal risk assessment over time, providing a complete view of how the entity's creditworthiness has changed. Each value in the curve represents a specific BIRR identifier that was assigned to the entity at that point in time.

### Example
```json
{
    "id": "entity123",
    "date": "2024-03-20T00:00:00Z",
    "birr_curve_id": "curve456",
    "name": "Example Corporation"
}
```

In this example, the entity is linked to a curve with ID "curve456" that contains its historical BIRR identifiers. The curve would contain entries like:

```json
{
    "id": "curve456",
    "type": "risk_rating",
    "values": [
        {
            "reference": "1m",
            "value": "BIRR-2024-02-A1"
        },
        {
            "reference": "2m",
            "value": "BIRR-2024-01-A2"
        },
        {
            "reference": "3m",
            "value": "BIRR-2023-12-B1"
        }
    ]
}
```

Each value in the curve is a BIRR identifier that corresponds to the entity's risk rating at that specific point in time. These identifiers should match the format used in the [birr_id](https://raw.githubusercontent.com/SuadeLabs/fire/master/documentation/properties/birr_id.md) property.

### Related Properties
- [birr_id](https://raw.githubusercontent.com/SuadeLabs/fire/master/documentation/properties/birr_id.md) - The current BIRR identifier