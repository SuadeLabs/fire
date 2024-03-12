---
layout:     property
title:      "securitisation_type"
schemas:    [security]
---

# securitisation_type

---

The type of securitisation with regards to common regulatory classifications.

```bash
├── sts
│   ├── sts_traditional
│   └── sts_synthetic
├── sythetic
├── traditional
└── pass_through

```

### sts
**STS securitisation**, or ‘simple, transparent and standardised securitisation’ means a securitisation that meets the requirements set out in Article 18 of Regulation (EU) 2017/2402. See [definitions](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32013R0575) and [criteria for STS securitisations qualifying for differentiated capital treatment](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32013R0575).

### sts_traditional
**Traditional** securitization is a structure where the cash flow from an underlying pool of exposures is used to service at least two different stratified risk positions or tranches reflecting different degrees of credit risk. Payments to the investors depend upon the performance of the specified underlying exposures, as opposed to being derived from an obligation of the entity originating those exposures.
See [OSFI Chapter 6, P5][osfi-chapter-6]

### sts_synthetic
**Synthetic** securitization is a structure with at least two different stratified risk positions or tranches that reflect different degrees of credit risk where credit risk of an underlying pool of exposures is transferred, in whole or in part, through the use of funded (e.g. credit-linked notes) or unfunded (e.g. credit default swaps) credit derivatives or guarantees that serve to hedge the credit risk of the portfolio.
See [OSFI Chapter 6, P6][osfi-chapter-6]

### traditional
**Non STS securitisation** means a securitisation that does not meet the requirements set out in Article 18 of Regulation (EU) 2017/2402. See [definitions](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32013R0575) and [criteria for STS securitisations qualifying for differentiated capital treatment](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32013R0575).

**Traditional** securitization is a structure where the cash flow from an underlying pool of exposures is used to service at least two different stratified risk positions or tranches reflecting different degrees of credit risk. Payments to the investors depend upon the performance of the specified underlying exposures, as opposed to being derived from an obligation of the entity originating those exposures.
See [OSFI Chapter 6, P5][osfi-chapter-6]

### synthetic
**Synthetic** (non-STS) securitization is a structure with at least two different stratified risk positions or tranches that reflect different degrees of credit risk where credit risk of an underlying pool of exposures is transferred, in whole or in part, through the use of funded (e.g. credit-linked notes) or unfunded (e.g. credit default swaps) credit derivatives or guarantees that serve to hedge the credit risk of the portfolio.
See [OSFI Chapter 6, P6][osfi-chapter-6]

### pass_through
**Pass-through** security; a security created when one or more mortgage holders form a collection (pool) of mortgages and sells shares or participation certificates in the pool. The cash flow from the collateral pool is "passed through" to the security holder as monthly payments of principal, interest, and prepayments.

---
[osfi-chapter-6]: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/capital-adequacy-requirements-car-2024-chapter-6-securitization
