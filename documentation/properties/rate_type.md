---
layout:		property
title:		"rate_type"
schemas:	[account, loan, security]
---

# rate_type

---

The **rate_type** property describes the nature of the interest rate being applied in the **rate** property. This is useful in determining future cash flows

```bash
├── fixed
├── fixed_to_fixed
├── fixed_to_float
├── step_up
├── variable
│   └── tracker
├── preferential
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
A **tracker** rate type is a sub-category of **variable** rate types and indicates a direct relationship between the interest rate and the **base_rate**[br]. For example **base_rate**[br] + 1%.

### preferential
A **preferential** rate type is often a temporary lower interest rate compared to what the bank would normally charge as an introductory offer or a reward for loyal customers.

### combined
Any mixture of the above

---
[mlar]: http://www.bankofengland.co.uk/pra/documents/regulatorydata/mlar/sup_chapter16_annex19bg_20120401.pdf
[br]: https://github.com/suadelabs/fire/blob/master/documentation/properties/base_rate.md
