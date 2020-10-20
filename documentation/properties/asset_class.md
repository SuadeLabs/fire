---
layout:		property
title:		"asset_class"
schemas:	[derivative_cash_flow, derivative]
---

# asset_class

---

An [**asset class**][wiki] is a group of instruments which have similar financial characteristics and behave similarly in the marketplace. We can often break these instruments into those having to do with real assets and those having to do with financial assets. Often, assets within the same asset class are subject to the same laws and regulations; however, this is not always true. For instance, futures on an asset are often considered part of the same asset class as the underlying instrument but are subject to different regulations than the underlying instrument.

Primary asset classes are Foreign Exchange, Interest Rates, Credit, Equities, Commodities and Other

```bash
├── fx
├── ir
│   └── inflation
├── cr
│   ├── cr_index
│   └── cr_single
├── eq
│   ├── eq_index
│   └── eq_single
├── co
│   ├── metals
│   │    └── precious metals
│   │         ├── gold
│   │         ├── silver
│   │         ├── platinum
│   │         └── palladium
│   ├── energy
│   │    ├── oil
│   │    ├── gas
│   │    ├── coal
│   │    └── electricity
│   └── agri
│   │    ├── sugar
│   │    ├── coffee
│   │    └── corn
│   └── co_other
└── other
```


---

[wiki]: https://en.wikipedia.org/wiki/Asset_classes
