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
├── non_sts
│   ├── non_sts_traditional
│   └── non_sts_synthetic
└──  pass_through

```

### sts
**STS securitisation**, or ‘simple, transparent and standardised securitisation’ means a securitisation that meets the requirements set out in Article 18 of Regulation (EU) 2017/2402. See [definitions](https://www.eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/101073) and [criteria for STS securitisations qualifying for differentiated capital treatment](https://www.eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/101074).

### sts_traditional
**Traditional** securitization is a structure where the cash flow from an underlying pool of exposures is used to service at least two different stratified risk positions or tranches reflecting different degrees of credit risk. Payments to the investors depend upon the performance of the specified underlying exposures, as opposed to being derived from an obligation of the entity originating those exposures.
See [OSFI Chapter 6, P5](https://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/CAR22_chpt6.aspx#ToC6.6.5)

### sts_synthetic
**Synthetic** securitization is a structure with at least two different stratified risk positions or tranches that reflect different degrees of credit risk where credit risk of an underlying pool of exposures is transferred, in whole or in part, through the use of funded (e.g. credit-linked notes) or unfunded (e.g. credit default swaps) credit derivatives or guarantees that serve to hedge the credit risk of the portfolio. 
See [OSFI Chapter 6, P6](https://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/CAR22_chpt6.aspx#ToC6.6.5)

### non_sts
**Non STS securitisation** means a securitisation that does not meet the requirements set out in Article 18 of Regulation (EU) 2017/2402. See [definitions](https://www.eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/101073) and [criteria for STS securitisations qualifying for differentiated capital treatment](https://www.eba.europa.eu/regulation-and-policy/single-rulebook/interactive-single-rulebook/101074).

### non_sts_traditional
**Traditional** securitization is a structure where the cash flow from an underlying pool of exposures is used to service at least two different stratified risk positions or tranches reflecting different degrees of credit risk. Payments to the investors depend upon the performance of the specified underlying exposures, as opposed to being derived from an obligation of the entity originating those exposures.
See [OSFI Chapter 6, P5](https://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/CAR22_chpt6.aspx#ToC6.6.5)

### non_sts_synthetic
**Synthetic** securitization is a structure with at least two different stratified risk positions or tranches that reflect different degrees of credit risk where credit risk of an underlying pool of exposures is transferred, in whole or in part, through the use of funded (e.g. credit-linked notes) or unfunded (e.g. credit default swaps) credit derivatives or guarantees that serve to hedge the credit risk of the portfolio. 
See [OSFI Chapter 6, P6](https://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/CAR22_chpt6.aspx#ToC6.6.5)

### pass_through
**Pass-through** security; a security created when one or more mortgage holders form a collection (pool) of mortgages and sells shares or participation certificates in the pool. The cash flow from the collateral pool is "passed through" to the security holder as monthly payments of principal, interest, and prepayments.
