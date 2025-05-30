---
layout:     property
title:      "base_rate"
schemas:    [account, derivative, loan, security]
---

# base_rate

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

# loan
The base rate set by the bank that offers the loan product, which typically follows the official central bank interest rate - but it is not guaranteed to do so. The base rate represents the basis of the repayment rate on the borrowed funds at the given date as agreed in the terms of the loan.

The [official interest rate][official] is the interest rate paid on commercial bank reserves by the central bank of an area or region.

```bash
├── FDTR
├── UKBRBASE
├── ZERO
├── cert_dep
├── cofi
│   ├── cofi_11th
│   ├── cofi_nm
│   └── cofi_other
├── cosi
├── mta
├── other
├── prime
├── sofr
│   ├── sofr_1m
│   ├── sofr_1y
│   ├── sofr_3m
│   ├── sofr_6m
│   └── sofr_other
└── tbill
    ├── tbill_1y
    ├── tbill_3m
    ├── tbill_3y
    ├── tbill_5y
    ├── tbill_6m
    └── tbill_other
```

### FDTR
The base rate is tied to the Federal Reserve's target rate for the federal funds rate. This is the interest rate that banks charge each other for overnight loans of federal funds.

### UKBRBASE
The base rate is linked to the Bank of England's base rate, which is the interest rate that the Bank of England charges banks for secured overnight lending.

### ZERO
The base rate is set to zero, indicating that the loan's interest rate is not tied to any external benchmark rate.

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

### mta
The Monthly Treasury Average (MTA) is also known as the 12-month moving average of one-year constant maturity Treasury (1-year CMT) bonds.

### other
A base rate other than one defined within the taxonomy.

### prime
Prime is one of several base rates used by banks to price short-term business loans. Refer to https://www.federalreserve.gov/releases/h15/.

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

---

# security
The **base rate** represents the [basis][basis] of the [**rate**][ir] on the [**balance**][balance] at the given [**date**][date] as agreed in the terms of the financial product.

Basis can be defined as "the difference between the spot price of a given cash market asset and the price of its related futures contract." Therefore, the base rate can be viewed as the time value of the money referred to in the financial product and the difference between the interest rate and the base rate can be viewed as the [yield spread][ys] of the financial product over a defined index.

In practice, the base rate conveys the information that the interest rate is directly or indirectly linked to another rate or index. For the purposes of consistency, the relevant Bloomberg Index ticker is used with "ZERO" used to indicate that there is no related base rate used for the determination of the interest rate.

### FDTR
Fed funds rate

### UKBRBASE
UK BoE base rate

### ZERO
0

---

[date]: https://github.com/suadelabs/fire/blob/master/documentation/properties/date.md
[basis]: https://en.wikipedia.org/wiki/Basis_trading
[ir]: https://github.com/suadelabs/fire/blob/master/documentation/properties/rate.md
[balance]: https://github.com/suadelabs/fire/blob/master/documentation/properties/balance.md
[ys]: https://en.wikipedia.org/wiki/Yield_spread
