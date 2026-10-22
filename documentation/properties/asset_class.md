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

### fx
Derivatives whose underlying risk is the exchange rate between currencies, such as currency forwards, swaps and options. See the [BIS OTC derivatives asset classes][bis-otc].

### ir
Derivatives linked to interest rates or interest-bearing instruments, such as interest rate swaps, forward rate agreements and interest rate options. See the [BIS OTC derivatives asset classes][bis-otc].

### inflation
Derivatives with payments linked to changes in a price index or inflation rate. FIRE groups these under **ir**. The [ECB explanation of inflation-linked swaps][ecb-inflation] describes exchanging fixed payments for inflation-linked payments.

### cr
Derivatives transferring credit risk relating to a reference entity or group of entities, such as credit default swaps. See the [BIS OTC derivatives asset classes][bis-otc].

### cr_index
Credit derivatives referencing an index of multiple reference entities, rather than one entity. See the [BIS definitions of credit derivatives][bis-otc].

### cr_single
Credit derivatives referencing a single entity, such as a single-name credit default swap. See the [BIS definitions of credit derivatives][bis-otc].

### eq
Derivatives linked to equity prices or returns, including individual shares and equity indices. See the [BIS OTC derivatives asset classes][bis-otc].

### eq_index
Equity derivatives referencing a share-price index. See the [BIS definitions of equity derivatives][bis-otc].

### eq_single
Equity derivatives referencing the shares of a single issuer. See the [BIS definitions of equity derivatives][bis-otc].

### co
Derivatives linked to commodity prices or indices. FIRE subdivides this category into metals, energy, agricultural and other commodities. The commodity names below are described in [Regulation (EU) 2017/585, Annex, Table 2][commodity-taxonomy].

### metals
Commodity derivatives referencing [metals, including base and precious metals][commodity-taxonomy].

### precious_metals
Commodity derivatives referencing [precious metals][commodity-taxonomy].

### gold
Commodity derivatives referencing [gold][commodity-taxonomy].

### silver
Commodity derivatives referencing [silver][commodity-taxonomy].

### platinum
Commodity derivatives referencing [platinum][commodity-taxonomy].

### palladium
Commodity derivatives referencing [palladium][commodity-taxonomy].

### energy
Commodity derivatives referencing [energy commodities][commodity-taxonomy].

### oil
Commodity derivatives referencing [oil][commodity-taxonomy].

### gas
Commodity derivatives referencing [natural gas][commodity-taxonomy].

### coal
Commodity derivatives referencing [coal][commodity-taxonomy].

### electricity
Commodity derivatives referencing [electricity][commodity-taxonomy].

### agri
Commodity derivatives referencing [agricultural commodities][commodity-taxonomy].

### sugar
Commodity derivatives referencing [sugar][commodity-taxonomy].

### coffee
Commodity derivatives referencing [coffee][commodity-taxonomy].

### corn
Commodity derivatives referencing [corn (maize)][commodity-taxonomy].

### co_other
Commodity derivatives whose underlying commodity does not fall within the metals, energy or agricultural categories in this hierarchy.

### other
Derivatives whose underlying asset class does not fall within the foreign exchange, interest rate, credit, equity or commodity categories above.


---

[wiki]: https://en.wikipedia.org/wiki/Asset_classes

[bis-otc]: https://data.bis.org/topics/OTC_DER
[ecb-inflation]: https://www.ecb.europa.eu/pub/pdf/other/mb200309_focus04.en.pdf
[commodity-taxonomy]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017R0585#:~:text=Table%202
