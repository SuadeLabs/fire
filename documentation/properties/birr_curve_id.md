---
layout:     property
title:      "birr_curve_id"
schemas:    [customer, issuer, guarantor]

---

# birr_curve_id

---

The **birr_curve_id** represents the unique identifier of a curve containing historical Borrower Internal Risk Ratings (BIRR) for an entity. The referenced curve must be of type 'risk_rating'.

This property allows for tracking the historical evolution of an entity's internal risk assessment over time, providing a complete view of how the entity's creditworthiness has changed.

### Example
```json
{
    "id": "entity123",
    "date": "2024-03-20T00:00:00Z",
    "birr_curve_id": "curve456",
    "name": "Example Corporation"
}
```

In this example, the entity is linked to a curve with ID "curve456" that contains its historical BIRR values. The curve would contain entries like:

```json
{
    "id": "curve456",
    "type": "risk_rating",
    "values": [
        {
            "reference": "1m",
            "value": "A"
        },
        {
            "reference": "2m",
            "value": "A-"
        },
        {
            "reference": "3m",
            "value": "B+"
        }
    ]
}
```

### Related Properties
- [birr_id](https://raw.githubusercontent.com/SuadeLabs/fire/master/documentation/properties/birr_id.md) - The current BIRR identifier