---
layout:     property
title:      "base_rate"
schemas:    [derivative]
---

# base_rate

---

# loan
The base rate set by the bank that offers the loan product, which typically follows the official central bank interest rate - but it is not guaranteed to do so. The base rate represents the basis of the repayment rate on the borrowed funds at the given date as agreed in the terms of the loan.

The [official interest rate][official] is the interest rate paid on commercial bank reserves by the central bank of an area or region.

```bash
├── FDTR
├── FESR
├── UKBRBASE
├── USTSR
├── ZERO
├── cert_dep
├── chf_libor
│   ├── chf_libor_10m
│   ├── chf_libor_11m
│   ├── chf_libor_12m
│   ├── chf_libor_1m
│   └── chf_libor_1w
│   └── chf_libor_2m
│   └── chf_libor_2w
│   └── chf_libor_3m
│   └── chf_libor_3w
│   └── chf_libor_4m
│   └── chf_libor_5m
│   └── chf_libor_6m
│   └── chf_libor_7m
│   └── chf_libor_8m
│   └── chf_libor_9m
│   └── chf_libor_on
├── cofi
│   ├── cofi_11th
│   ├── cofi_nm
│   └── cofi_other
├── cosi
├── eonia
├── estr
├── euribor
│   ├── euribor_10m
│   ├── euribor_11m
│   ├── euribor_12m
│   ├── euribor_1m
│   └── euribor_1w
│   └── euribor_2m
│   └── euribor_2w
│   └── euribor_3m
│   └── euribor_3w
│   └── euribor_4m
│   └── euribor_5m
│   └── euribor_6m
│   └── euribor_7m
│   └── euribor_8m
│   └── euribor_9m
│   └── euribor_on
├── eur_libor
│   ├── eur_libor_10m
│   ├── eur_libor_11m
│   ├── eur_libor_12m
│   ├── eur_libor_1m
│   └── eur_libor_1w
│   └── eur_libor_2m
│   └── eur_libor_2w
│   └── eur_libor_3m
│   └── eur_libor_3w
│   └── eur_libor_4m
│   └── eur_libor_5m
│   └── eur_libor_6m
│   └── eur_libor_7m
│   └── eur_libor_8m
│   └── eur_libor_9m
│   └── eur_libor_on
├── gbp_libor
│   ├── gbp_libor_10m
│   ├── gbp_libor_11m
│   ├── gbp_libor_12m
│   ├── gbp_libor_1m
│   └── gbp_libor_1w
│   └── gbp_libor_2m
│   └── gbp_libor_2w
│   └── gbp_libor_3m
│   └── gbp_libor_3w
│   └── gbp_libor_4m
│   └── gbp_libor_5m
│   └── gbp_libor_6m
│   └── gbp_libor_7m
│   └── gbp_libor_8m
│   └── gbp_libor_9m
│   └── gbp_libor_on
├── honia
├── jpy_libor
│   ├── jpy_libor_10m
│   ├── jpy_libor_11m
│   ├── jpy_libor_12m
│   ├── jpy_libor_1m
│   └── jpy_libor_1w
│   └── jpy_libor_2m
│   └── jpy_libor_2w
│   └── jpy_libor_3m
│   └── jpy_libor_3w
│   └── jpy_libor_4m
│   └── jpy_libor_5m
│   └── jpy_libor_6m
│   └── jpy_libor_7m
│   └── jpy_libor_8m
│   └── jpy_libor_9m
│   └── jpy_libor_on
├── mibor
│   ├── mibor_10m
│   ├── mibor_11m
│   ├── mibor_12m
│   ├── mibor_1m
│   └── mibor_1w
│   └── mibor_2m
│   └── mibor_2w
│   └── mibor_3m
│   └── mibor_3w
│   └── mibor_4m
│   └── mibor_5m
│   └── mibor_6m
│   └── mibor_7m
│   └── mibor_8m
│   └── mibor_9m
│   └── mibor_on
├── mta
├── multi_rate
│   ├── multi_rate_10m
│   ├── multi_rate_11m
│   ├── multi_rate_12m
│   ├── multi_rate_1m
│   └── multi_rate_1w
│   └── multi_rate_2m
│   └── multi_rate_2w
│   └── multi_rate_3m
│   └── multi_rate_3w
│   └── multi_rate_4m
│   └── multi_rate_5m
│   └── multi_rate_6m
│   └── multi_rate_7m
│   └── multi_rate_8m
│   └── multi_rate_9m
│   └── multi_rate_on
├── other
│   ├── other_10m
│   ├── other_11m
│   ├── other_12m
│   ├── other_1m
│   └── other_1w
│   └── other_2m
│   └── other_2w
│   └── other_3m
│   └── other_3w
│   └── other_4m
│   └── other_5m
│   └── other_6m
│   └── other_7m
│   └── other_8m
│   └── other_9m
│   └── other_on
├── prime
├── saron
├── sofr
│   ├── sofr_1m
│   ├── sofr_1y
│   ├── sofr_3m
│   ├── sofr_6m
│   └── sofr_other
├── sonia
├── sora
└── tbill
    ├── tbill_1y
    ├── tbill_3m
    ├── tbill_3y
    ├── tbill_5y
    ├── tbill_6m
    └── tbill_other
├── tona
├── usd_libor
│   ├── usd_libor_10m
│   ├── usd_libor_11m
│   ├── usd_libor_12m
│   ├── usd_libor_1m
│   └── usd_libor_1w
│   └── usd_libor_2m
│   └── usd_libor_2w
│   └── usd_libor_3m
│   └── usd_libor_3w
│   └── usd_libor_4m
│   └── usd_libor_5m
│   └── usd_libor_6m
│   └── usd_libor_7m
│   └── usd_libor_8m
│   └── usd_libor_9m
│   └── usd_libor_on
```

### FDTR
The base rate is tied to the Federal Reserve's target rate for the federal funds rate. This is the interest rate that banks charge each other for overnight loans of federal funds.

### FESR
The base rate is tied to the Federal Funds Effective Swap Rate.

### UKBRBASE
The base rate is linked to the Bank of England's base rate, which is the interest rate that the Bank of England charges banks for secured overnight lending.

### USTSR
The base rate is tied to the US Treasury Security Interest Rate.

### ZERO
The base rate is set to zero, indicating that the loan's interest rate is not tied to any external benchmark rate.

### bbsw
Bank Bill Swap Rate (BBSW) where the tenor is unknown. Refer to: https://www.rba.gov.au/mkt-operations/resources/interest-rate-benchmark-reform.html

### bbsw_3m
3 month Bank Bill Swap Rate (BBSW). Refer to: https://www.rba.gov.au/mkt-operations/resources/interest-rate-benchmark-reform.html

### chf_libor
CHF Libor was the reference interest rate for many financial instruments denominated in Swiss Francs

### chf_libor_10m
10 month CHF Libor reference interest rate

### chf_libor_11m
11 month CHF Libor reference interest rate

### chf_libor_12m
12 month CHF Libor reference interest rate

### chf_libor_1m
1 month CHF Libor reference interest rate

### chf_libor_1w
1 week CHF Libor reference interest rate

### chf_libor_2m
2 month CHF Libor reference interest rate

### chf_libor_2w
2 week CHF Libor reference interest rate

### chf_libor_3m
3 month CHF Libor reference interest rate

### chf_libor_3w
3 week CHF Libor reference interest rate

### chf_libor_4m
4 month CHF Libor reference interest rate

### chf_libor_5m
5 month CHF Libor reference interest rate

### chf_libor_6m
6 month CHF Libor reference interest rate

### chf_libor_7m
7 month CHF Libor reference interest rate

### chf_libor_8m
8 month CHF Libor reference interest rate

### chf_libor_9m
9 month CHF Libor reference interest rate

### chf_libor_on
Overnight CHF Libor reference interest rate

### cert_dep
Rate based on a certificate of deposit rate.

### cofi
The Federal Cost of Funds Index (COFI) is used as a benchmark for some types of mortgage loans and securities. It is calculated as the sum of the monthly average interest rates for marketable Treasury bills and for marketable Treasury notes, divided by two, and rounded to three decimal places. Refer to https://www.freddiemac.com/research/datasets/cofi.

#### cofi_11th
The Federal Home Loan Mortgage Corporation ("Freddie Mac") is the administrator and publisher of the Enterprise 11th District COFI Replacement Index and Enterprise 11th District COFI Institutional Replacement Index (each a "Replacement Index", collectively the "Replacement Indices") which are being made available for financial instruments owned or guaranteed by Freddie Mac or Fannie Mae (the "GSEs") that are indexed to the 11th District Monthly Weighted Average Cost of Funds Index ("COFI"), an index calculated and published by the Federal Home Loan Bank of San Francisco. The Federal Home Loan Bank of San Francisco will discontinue the calculation and publication of the 11th District Monthly Weighted Average Cost of Funds Index after the announcement of the December 2021 COFI in January 2022. Refer to https://www.freddiemac.com/research/indices/COFI-enterprise-replacement.

#### cofi_nm
The Federal Cost of Funds Index (COFI) is used as a benchmark for some types of mortgage loans and securities. It is calculated as the sum of the monthly average interest rates for marketable Treasury bills and for marketable Treasury notes, divided by two, and rounded to three decimal places. Refer to https://www.freddiemac.com/research/datasets/cofi.

#### cofi_other
COFI other than the national monthly index or 11th district. 

The Federal Cost of Funds Index (COFI) is used as a benchmark for some types of mortgage loans and securities. It is calculated as the sum of the monthly average interest rates for marketable Treasury bills and for marketable Treasury notes, divided by two, and rounded to three decimal places. Refer to https://www.freddiemac.com/research/datasets/cofi.

### cosi
The Cost of Savings Index (COSI) is a popular index used for calculating the interest rate of certain adjustable-rate mortgages (ARMs). Officially known as the Wells Fargo Cost of Savings Index, it is based on the interest rates that Wells Fargo Bank pays to individuals on certificates of deposit (CDs). Refer to https://www.wellsfargo.com/mortgage/manage-account/cost-of-savings-index/.

### eonia
Euro OverNight Index Average (EONIA) was the interbank overnight lending reference rate for the euro

### estr
Euro short-term rate (€STR)

### eur_libor
Euro LIBOR was the London Interbank Offered Rate (LIBOR) denominated in euros

### eur_libor_10m
10 month EUR Libor reference interest rate

### eur_libor_11m
11 month EUR Libor reference interest rate

### eur_libor_12m
12 month EUR Libor reference interest rate

### eur_libor_1m
1 month EUR Libor reference interest rate

### eur_libor_1w
1 week EUR Libor reference interest rate

### eur_libor_2m
2 month EUR Libor reference interest rate

### eur_libor_2w
2 week EUR Libor reference interest rate

### eur_libor_3m
3 month EUR Libor reference interest rate

### eur_libor_3w
3 week EUR Libor reference interest rate

### eur_libor_4m
4 month EUR Libor reference interest rate

### eur_libor_5m
5 month EUR Libor reference interest rate

### eur_libor_6m
6 month EUR Libor reference interest rate

### eur_libor_7m
7 month EUR Libor reference interest rate

### eur_libor_8m
8 month EUR Libor reference interest rate

### eur_libor_9m
9 month EUR Libor reference interest rate

### eur_libor_on
Overnight EUR Libor reference interest rate

### euribor
Euro Interbank Offered Rate (Euribor) where the tenor is unknown

### euribor_10m
10 month Euribor reference interest rate

### euribor_11m
11 month Euribor reference interest rate

### euribor_12m
12 month Euribor reference interest rate

### euribor_1m
1 month EURLibor reference interest rate

### euribor_1w
1 week CHF Libor reference interest rate

### euribor_2m
2 month Euribor reference interest rate

### euribor_2w
2 week Euribor reference interest rate

### euribor_3m
3 month Euribor reference interest rate

### euribor_3w
3 week Euribor reference interest rate

### euribor_4m
4 month Euribor reference interest rate

### euribor_5m
5 month Euribor reference interest rate

### euribor_6m
6 month Euribor reference interest rate

### euribor_7m
7 month Euribor reference interest rate

### euribor_8m
8 month Euribor reference interest rate

### euribor_9m
9 month Euribor reference interest rate

### euribor_on
Overnight Euribor reference interest rate

### gbp_libor
GBP LIBOR was the London Interbank Offered Rate (LIBOR) for pounds sterling

### gbp_libor_10m
10 month GBP Libor reference interest rate

### gbp_libor_11m
11 month GBP Libor reference interest rate

### gbp_libor_12m
12 month GBP Libor reference interest rate

### gbp_libor_1m
1 month GBP Libor reference interest rate

### gbp_libor_1w
1 week GBP Libor reference interest rate

### gbp_libor_2m
2 month GBP Libor reference interest rate

### gbp_libor_2w
2 week GBP Libor reference interest rate

### gbp_libor_3m
3 month GBP Libor reference interest rate

### gbp_libor_3w
3 week GBP Libor reference interest rate

### gbp_libor_4m
4 month GBP Libor reference interest rate

### gbp_libor_5m
5 month GBP Libor reference interest rate

### gbp_libor_6m
6 month GBP Libor reference interest rate

### gbp_libor_7m
7 month GBP Libor reference interest rate

### gbp_libor_8m
8 month GBP Libor reference interest rate

### gbp_libor_9m
9 month GBP Libor reference interest rate

### gbp_libor_on
Overnight GBP Libor reference interest rate

### honia
Hong Kong Dollar Overnight Index Average (HONIA)

### jpy_libor
JPY LIBOR was the London Interbank Offered Rate (LIBOR) for Japanese yen

### jpy_libor_10m
10 month JPY Libor reference interest rate

### jpy_libor_11m
11 month JPY Libor reference interest rate

### jpy_libor_12m
12 month JPY Libor reference interest rate

### jpy_libor_1m
1 month JPY Libor reference interest rate

### jpy_libor_1w
1 week JPY Libor reference interest rate

### jpy_libor_2m
2 month JPY Libor reference interest rate

### jpy_libor_2w
2 week JPY Libor reference interest rate

### jpy_libor_3m
3 month JPY Libor reference interest rate

### jpy_libor_3w
3 week JPY Libor reference interest rate

### jpy_libor_4m
4 month JPY Libor reference interest rate

### jpy_libor_5m
5 month JPY Libor reference interest rate

### jpy_libor_6m
6 month JPY Libor reference interest rate

### jpy_libor_7m
7 month JPY Libor reference interest rate

### jpy_libor_8m
8 month JPY Libor reference interest rate

### jpy_libor_9m
9 month JPY Libor reference interest rate

### jpy_libor_on
Overnight JPY Libor reference interest rate

### mibor
Mumbai Interbank Offered Rate (MIBOR)

### mibor_10m
10 month MIBOR reference interest rate

### mibor_11m
11 month MIBOR reference interest rate

### mibor_12m
12 month MIBOR reference interest rate

### mibor_1m
1 month MIBOR reference interest rate

### mibor_1w
1 week MIBOR reference interest rate

### mibor_2m
2 month MIBOR reference interest rate

### mibor_2w
2 week MIBOR reference interest rate

### mibor_3m
3 month MIBOR reference interest rate

### mibor_3w
3 week MIBOR reference interest rate

### mibor_4m
4 month MIBOR reference interest rate

### mibor_5m
5 month MIBOR reference interest rate

### mibor_6m
6 month MIBOR reference interest rate

### mibor_7m
7 month MIBOR reference interest rate

### mibor_8m
8 month MIBOR reference interest rate

### mibor_9m
9 month MIBOR reference interest rate

### mibor_on
Overnight MIBOR reference interest rate

### mta
The Monthly Treasury Average (MTA) is also known as the 12-month moving average of one-year constant maturity Treasury (1-year CMT) bonds.

### multi_rate
Instruments using multiple reference rates used for the calculation of the actual interest rate

### multi_rate_10m
10 month multi rate reference interest rates

### multi_rate_11m
11 month multi rate reference interest rates

### multi_rate_12m
12 month multi rate reference interest rates

### multi_rate_1m
1 month multi rate reference interest rates

### multi_rate_1w
1 week multi rate reference interest rates

### multi_rate_2m
2 month multi rate reference interest rates

### multi_rate_2w
2 week multi rate reference interest rates

### multi_rate_3m
3 month multi rate reference interest rates

### multi_rate_3w
3 week multi rate reference interest rates

### multi_rate_4m
4 month multi rate reference interest rates

### multi_rate_5m
5 month multi rate reference interest rates

### multi_rate_6m
6 month multi rate reference interest rates

### multi_rate_7m
7 month multi rate reference interest rates

### multi_rate_8m
8 month multi rate reference interest rates

### multi_rate_9m
9 month multi rate reference interest rates

### multi_rate_on
Overnight multi rate reference interest rates

### other
A base rate other than one defined within the taxonomy.

### other_10m
10 month other reference interest rate

### other_11m
11 month other reference interest rate

### other_12m
12 month other reference interest rate

### other_1m
1 month other reference interest rate

### other_1w
1 week other reference interest rate

### other_2m
2 month other reference interest rate

### other_2w
2 week other reference interest rate

### other_3m
3 month other reference interest rate

### other_3w
3 week other reference interest rate

### other_4m
4 month other reference interest rate

### other_5m
5 month other reference interest rate

### other_6m
6 month other reference interest rate

### other_7m
7 month other reference interest rate

### other_8m
8 month other reference interest rate

### other_9m
9 month other reference interest rate

### other_on
Overnight other reference interest rate

### pboc
People’s Bank of China (PBOC) benchmark interest rate, where the specific rate or tenor is unknown

### prime
Prime is one of several base rates used by banks to price short-term business loans. Refer to https://www.federalreserve.gov/releases/h15/.

### saron
Swiss Average Rate Overnight (SARON)

### sofr
Secured Overnight Financing Rate (SOFR) where the tenor is unknown.

#### sofr_1m
1 month Secured Overnight Financing Rate (SOFR).

#### sofr_1y
1 year Secured Overnight Financing Rate (SOFR).

#### sofr_3m
3 month Secured Overnight Financing Rate (SOFR).

#### sofr_6m
6 month Secured Overnight Financing Rate (SOFR).

#### sofr_other
Secured Overnight Financing Rate (SOFR) where the tenor is known.

### sonia
The Sterling Overnight Index Average (SONIA)

### sora
The Singapore Overnight Rate Average (SORA) 

### tbill
Treasury bill rate with an unknown tenor. Refer to https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_bill_rates.

#### tbill_1y
1 year treasury bill rate. Refer to https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_bill_rates.

#### tbill_3m
3 month treasury bill rate. Refer to https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_bill_rates.

#### tbill_3y
3 year treasury bill rate. Refer to https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_bill_rates.

#### tbill_5y
5 year treasury bill rate. Refer to https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_bill_rates.

#### tbill_6m
6 month treasury bill rate. Refer to https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_bill_rates.

#### tbill_other
Treasury bill rate with another tenor. Refer to https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_bill_rates.

[official]: http://www.bankofengland.co.uk/statistics/pages/iadb/notesiadb/wholesale_baserate.aspx

### tona
 Tokyo Overnight Average Rate (TONA)

### usd_libor
USD LIBOR was the London Interbank Offered Rate (LIBOR) for US dollars

### usd_libor_10m
10 month USD Libor reference interest rate

### usd_libor_11m
11 month USD Libor reference interest rate

### usd_libor_12m
12 month USD Libor reference interest rate

### usd_libor_1m
1 month USD Libor reference interest rate

### usd_libor_1w
1 week USD Libor reference interest rate

### usd_libor_2m
2 month USD Libor reference interest rate

### usd_libor_2w
2 week USD Libor reference interest rate

### usd_libor_3m
3 month USD Libor reference interest rate

### usd_libor_3w
3 week USD Libor reference interest rate

### usd_libor_4m
4 month USD Libor reference interest rate

### usd_libor_5m
5 month USD Libor reference interest rate

### usd_libor_6m
6 month USD Libor reference interest rate

### usd_libor_7m
7 month USD Libor reference interest rate

### usd_libor_8m
8 month USD Libor reference interest rate

### usd_libor_9m
9 month USD Libor reference interest rate

### usd_libor_on
Overnight USD Libor reference interest rate


---

# security
The **base rate** represents the [basis][basis] of the [**rate**][ir] on the [**balance**][balance] at the given [**date**][date] as agreed in the terms of the financial product.

Basis can be defined as "the difference between the spot price of a given cash market asset and the price of its related futures contract." Therefore, the base rate can be viewed as the time value of the money referred to in the financial product and the difference between the interest rate and the base rate can be viewed as the [yield spread][ys] of the financial product over a defined index.

In practice, the base rate conveys the information that the interest rate is directly or indirectly linked to another rate or index. For the purposes of consistency, the relevant Bloomberg Index ticker is used with "ZERO" used to indicate that there is no related base rate used for the determination of the interest rate.

---

[date]: https://github.com/suadelabs/fire/blob/master/documentation/properties/date.md
[basis]: https://en.wikipedia.org/wiki/Basis_trading
[ir]: https://github.com/suadelabs/fire/blob/master/documentation/properties/rate.md
[balance]: https://github.com/suadelabs/fire/blob/master/documentation/properties/balance.md
[ys]: https://en.wikipedia.org/wiki/Yield_spread

---


# account
The base rate set by the bank that offers the account facility, which typically follows the official central bank interest rate - but it is not guaranteed to do so. The base rate represents the basis of the rate on the balance at the given date as agreed in the terms of the account.

The [official interest rate][official] is the interest rate paid on commercial bank reserves by the central bank of an area or region.

[official]: http://www.bankofengland.co.uk/statistics/pages/iadb/notesiadb/wholesale_baserate.aspx


---

# derivative
The **base rate** represents the [basis][basis] of the [**rate**][ir] on the [**balance**][balance] at the given [**date**][date] as agreed in the terms of the financial product.

Basis can be defined as "the difference between the spot price of a given cash market asset and the price of its related futures contract." Therefore, the base rate can be viewed as the time value of the money referred to in the financial product and the difference between the interest rate and the base rate can be viewed as the [yield spread][ys] of the financial product over a defined index.

In practice, the base rate conveys the information that the interest rate is directly or indirectly linked to another rate or index. For the purposes of consistency, the relevant Bloomberg Index ticker is used with "ZERO" used to indicate that there is no related base rate used for the determination of the interest rate.

[date]: https://github.com/suadelabs/fire/blob/master/documentation/properties/date.md
[basis]: https://en.wikipedia.org/wiki/Basis_trading
[ir]: https://github.com/suadelabs/fire/blob/master/documentation/properties/rate.md
[balance]: https://github.com/suadelabs/fire/blob/master/documentation/properties/balance.md
[ys]: https://en.wikipedia.org/wiki/Yield_spread

---