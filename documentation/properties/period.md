---
layout: property
title: "period"
schemas:  [exchange_rate]
---

# period

---



# Exchange Rate

The period corresponds to the methodology and period over which the excange rate has been calculated. This assumes that the current **date** is the end of the period. So *avg_3m* can be understood as the average rate over the past 3 months.

If period is blank, it can be assumed the that rate corresponds to the current spot rate (ie. no period). The spot rate is the reference rate that corresponds to the exchange rate on the provided **date**. Reference rates are rates determined by the firm or the relevant central bank for a given date for reporting purposes. (e.g. [ECB EUR Reference Rates][ecb-ref-rates], [BoE Reference Rates][boe-ref-rates]). If **type** is left blank that it can be assumed to be the spot rate for the given **date** of the data.


```bash
├── avg_1m
├── avg_3m
├── avg_6m
├── avg_12m
└── avg_ytd
```


### avg_1m
The average rate over the past month.

### avg_3m
The average rate over the past 3 months.

### avg_6m
The average rate over the past 6 months.

### avg_12m
The average rate over the past 12 months.

### avg_ytd
The average rate since the start of the current calendar year.


---

[ecb-ref-rates]: https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html
[boe-ref-rates]: https://www.bankofengland.co.uk/statistics/exchange-rates
