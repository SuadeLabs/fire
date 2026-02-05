---
layout:     property
title:      "orig_rate_type"
schemas:    [loan, account, security]
---

# orig_rate_type


The rate_type at origination.

## Loan and account 
```bash
├── combined
├── fixed
├── tracker
└── variable
```

### combined
Combined Rate - A hybrid rate structure that combines elements of different rate types. This could include a combination of fixed and variable components, or other rate structures that don't fit into the standard categories.

### fixed
Fixed Rate - The interest rate remains constant throughout the life of the loan. The rate is set at origination and does not change, providing predictable payment amounts for the borrower.

### tracker
Tracker Rate - The interest rate is directly linked to a specific benchmark rate, typically moving in lockstep with changes to that rate. The rate tracks the benchmark rate with a fixed margin above or below it.

### variable
Variable Rate - The interest rate can change over time based on market conditions or other factors. Unlike a tracker rate, the changes may not be directly proportional to changes in a benchmark rate.


## Security


```bash
├── fixed
├── fixed_to_fixed
├── fixed_to_float
├── step_up
├── variable
│   └── tracker
└── combined
```

### fixed
A **fixed** rate type that is not expected to change. For example as defined in the [Bank of England's Mortgage Lending & Administration Report (MLAR)][mlar] Definitions:
> means the rate of interest is fixed for a stated period. It should also include any products with a 'capped rate' (i.e. subject to a guaranteed maximum rate) and any products that are 'collared loans' (i.e. subject to a minimum and a maximum rate). Annual review or stabilised payment loans should be excluded (since the purpose is merely to smooth cash flow on variable rate loans);

### fixed_to_fixed
A **fixed-to-fixed** rate type is where the interest rate is fixed for a set period, then resets to a new fixed rate at scheduled intervals.

### fixed_to_float
A **fixed-to-floating** rate type is where the interest rate is initially fixed for a defined period and then converts to a floating rate that varies based on a market benchmark.

### step_up
A **step-up** rate type is where the interest rate increases (or "steps up") at predefined intervals.

### variable
A **variable** rate which may be subject to change. For example as defined in the [Bank of England's Mortgage Lending & Administration Report (MLAR)][mlar] Definitions:
> includes all other interest rate bases (i.e. other than those defined above as 'fixed') applying to particular products, including those at, or at a discount or premium to, one of the firm's administered lending rates; those linked to Libor (or other market rate); those linked to an index (e.g. FTSE) etc. However if any such loan products are subject to a 'capped rate', then treat as 'fixed'.

### tracker
A **tracker** rate type is a sub-category of **variable** rate types and indicates a direct relationship between the interest rate and the [**base_rate**][br]. For example [**base_rate**][br] + 1%.

### combined
Any mixture of the above

---
[mlar]: http://www.bankofengland.co.uk/pra/documents/regulatorydata/mlar/sup_chapter16_annex19bg_20120401.pdf
[br]: https://suade.org/fire/book/documentation/properties/base_rate.html

