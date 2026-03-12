---
layout:     property
title:      "securitisation_type"
schemas:    [security]
---

# securitisation_type

---
The type of securitisation with regards to common regulatory classifications. There are 5 main types of securitisations:
### traditional
‘traditional securitisation’: involves the transfer of the economic interest in the exposures being securitised through the transfer of ownership of those exposures from the originator to an SSPE or through sub-participation by an SSPE, where the securities issued do not represent payment obligations of the originator; the cash flow from the underlying pool of exposures is used to service at least two different stratified risk positions or tranches reflecting different degrees of credit risk. Payments to the investors depend upon the performance of the specified underlying exposures, as opposed to being derived from an obligation of the entity originating those exposures

### synthetic
‘synthetic securitisation’ the transfer of risk is achieved by the use of credit derivatives or guarantees, and the exposures being securitised remain exposures of the originator;

### abcp_programme
Asset-backed commercial paper programme:  a programme of securitisations the securities issued by which predominantly take the form of asset-backed commercial paper with an original maturity of one year or less;

### abcp_transaction
Asset-backed commercial paper transaction: a securitisation within an ABCP programme

### npe
A traditionional securitisation backed by a pool of non-performing exposures the nominal value of which makes up not less than 90 % of the entire pool’s nominal value at the time of origination and at any later time where assets are added to or removed from the underlying pool due to replenishment, restructuring or any other relevant reason. 

### npe_qualifying
A traditional NPE securitisation where the non-refundable purchase price discount is at least 50 % of the outstanding amount of the underlying exposures at the time they were transferred to the SSPE.

### sts
Each type of securitisation can be eligible to the Simple, Transparent and Standardised status (STS) when meeting the requirements of Article 18 of Regulation (EU) 2017/2402. (https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32013R0575)

### sts_traditional
### sts_synthetic
### sts_abcp_programme
### sts_abcp_transaction
### sts_npe
### sts_npe_qualifying

### sts_q
STS securitisations which qualify for a preferential ("differentiated") capital treatment under Art. 243 (ABCP and traditional securitisation) or art. 270 (synthetic securitisation).
### sts_q_traditional
### sts_q_synthetic
### sts_q_abcp_programme
### sts_q_abcp_transaction
### sts_q_npe
### sts_q_npe_qualifying


```bash
├── abcp_programme
├── abcp_transaction
├── npe_non_qualifying
├── npe_qualifying
├── sythetic
├── traditional
├── pass_through
├── sts (sts_traditional)
│  ├── sts_abcp_programme
│  ├── sts_abcp_transaction
│  ├── sts_npe
│  ├── sts_npe_qualifying
│  ├── sts_traditional
│  └── sts_synthetic
├── sts_q (sts_q_traditional)
   ├── sts_q_abcp_programme
   ├── sts_q_abcp_transaction
   ├── sts_q_npe
   ├── sts_q_npe_qualifying
   ├── sts_q_traditional
   └── sts_q_synthetic

```
Remarks: **sts** and **sts_q** do not refer to any of the 5 basic securitisation types; they can therefore by used for **sts_traditional** and **sts_q_traditional**

### pass_through
**Pass-through** security; a security created when one or more mortgage holders form a collection (pool) of mortgages and sells shares or participation certificates in the pool. The cash flow from the collateral pool is "passed through" to the security holder as monthly payments of principal, interest, and prepayments.

https://eur-lex.europa.eu/legal-content/en/TXT/?uri=CELEX%3A02013R0575-20260101#art_242:~:text=%E2%96%BCM13-,Article%20269a,-Treatment%20of%20non

---
[osfi-chapter-6]: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/capital-adequacy-requirements-car-2024-chapter-6-securitization
