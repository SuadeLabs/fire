---
layout:		property
title:		"country_code"
schemas:	[account, collateral, customer, loan]
---

# country_code

---

The **country_code** represents location, registration, jurisdiction or country of domicile of the product, customer or collateral (booking location). This reflects where product or entity is from an operational standpoint rather than a legal point of view (although in many cases it is the same).

Countries are represented as 2-letter codes in accordance with [ISO 3166-1][iso3166].
Exceptionally, due to inconsistent regulatory treatment granularity, [ISO-3611-2][iso3166-2] codes have been added, for example to distinguish between the 7 different emirates.

### Member States
EU Regulations often refer to *Member States* which refers to European Economic Area (EEA) countries as clarified by the EBA in [this Q&A][member-state-qa].

For the avoidance of doubt, the EEA list is:
Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden and the UK which comprise the list of EU Members and also Iceland, Liechtenstein and Norway who are part of the single market but not part of the EU.

The notable exception here is Switzerland (CH).

```python
EU_MEMBERS = [BE, BG, CZ, DK, DE, EE, IE, ES, FR, GB, GR, HR, IT, CY, LV, LT, LU, HU, MT, NL, AT, PL, PT, RO, SI, SK, FI, SE]

EEA_MEMBERS = EU_MEMBERS + [IS, LI, NO]
```

See also [**risk_country_code**][rcc].

---

[end]: https://github.com/suadelabs/fire/blob/master/documentation/properties/end_date.md
[iso3166]: https://en.wikipedia.org/wiki/ISO_3166-1
[member-state-qa]: https://www.eba.europa.eu/single-rule-book-qa/-/qna/view/publicId/2013_233
[rcc]: https://github.com/suadelabs/fire/blob/master/documentation/properties/risk_country_code.md
[iso3166-2]: https://en.wikipedia.org/wiki/ISO_3166-2
