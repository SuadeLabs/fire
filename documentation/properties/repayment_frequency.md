---
layout:		property
title:		"repayment_frequency"
schemas:	[loan]
---

# repayment_frequency

---

Repayment frequency of the loan refers to how often the repayments occur.

**The [FCA][repayment] defines 'Repayment Strategy' as:**

> "the means by which the customer intends to repay the outstanding capital and, where applicable, pay the interest accrued under the regulated mortgage contract, where all or part of that contract is an interest-only mortgage."

[repayment]: https://www.handbook.fca.org.uk/handbook/glossary/G2960.html

**[DIRECTIVE 2014/17/EU OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL][directive] (of 4 February 2014) on credit agreements for consumers relating to residential immovable property and amending Directives 2008/48/EC and 2013/36/EU and Regulation (EU) No 1093/2010 states:**

**Section ‘5. Frequency and number of payments’**:

* (1) Where payments are to be made on a regular basis, **the frequency of payments shall be indicated** (e.g. monthly). Where the frequency of payments will be irregular, this shall be clearly explained to the consumer.
* (2) The number of payments indicated shall cover the whole duration of the credit.

**Article 13: 1.** *Member States shall ensure that clear and comprehensible general information about credit agreements is made available by creditors or, where applicable, by tied credit intermediaries or their appointed representatives at all times on paper or on another durable medium or in electronic form. In addition, Member States may provide that general information is made available by non-tied credit intermediaries.*

*Such general information shall include at least the following*:

> "... (i) the range of different options available for reimbursing the credit to the creditor, **including the number, frequency and amount of the regular repayment instalments**;"

[directive]: http://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32014L0017

Valid enums:

### daily
once per 24 hour period

### weekly
once per 7 day period

### bi_weekly
once per 2 weeks

### monthly
once per calendar month

### bi_monthly
once per 2 months

### quarterly
once per 3 calendar months

### semi_annually
once per 6 calendar months

### annually
once per calendar year

### sesquiennially
once every 1 year and a half

### biennially
once every 2 years

### at_maturity
upon maturity of the product (end_date)
