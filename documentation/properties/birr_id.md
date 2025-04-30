---
layout: property
title: "birr_id"
schemas: [customer, issuer, guarantor]
---

# birr_id

---

The unique identifier of the Borrower Internal Risk Rating (BIRR).

The Borrower Internal Risk Rating represents an internally assigned risk assessment for a customer, based on their creditworthiness and financial stability. It is used to evaluate the likelihood of default across different exposures and lending decisions, considering factors such as historical repayment behavior, financial statements, and market conditions.

This "id" is designed to link to a corresponding "id" in the risk_rating schema.

### Requirement for Internal Ratings under IRB
Under the IRB approach, institutions are required to assign a borrower-level internal risk rating to each obligor, forming the basis for the probability of default (PD) used in regulatory capital calculations. This requirement applies to all corporate, sovereign, and bank counterparties, regardless of product type.

> “Institutions must assign to each obligor a rating reflecting the obligor’s likelihood of default. This rating shall form the basis for determining the obligor’s PD estimate.”
> - OSFI CAR Chapter 5, para 94; Basel II, para 415
As such, when a bond is held in the banking book (subject to credit risk capital under IRB), the issuer of the bond is the credit-risk-bearing counterparty, and must be assigned a risk rating.

### Terminology: Why We Refer to It as a BIRR
While the term BIRR (Borrower Internal Risk Rating) is most commonly associated with facilities such as loans or credit lines, the concept is applicable to any obligor-level credit exposure, including bonds.

Using the term BIRR for issuer exposures is justified because:

The conceptual framework is identical — a forward-looking, obligor-level risk assessment used to derive PD.
The regulatory requirement to assign an internal rating at the obligor level does not distinguish between loans and securities.
In essence: “BIRR” = any internal counterparty rating tied to a PD under IRB — whether the exposure arises from a loan, bond, or other credit instrument.

Thus, in the context of IRB-compliant modeling, the issuer rating used for PD assignment serves the same regulatory and risk purpose as a traditional BIRR, and can justifiably be referred to as such in documentation and systems.

---
[osfi bd]: https://www.osfi-bsif.gc.ca/en/data-forms/reporting-returns/filing-financial-returns/financial-reporting-instructions/irb-credit-data-retail-portfolio-part-1-bd
[osfi bb]: https://www.osfi-bsif.gc.ca/en/data-forms/reporting-returns/filing-financial-returns/financial-reporting-instructions/irb-credit-data-wholesale-portfolio-part-1-bb
