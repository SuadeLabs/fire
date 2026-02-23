---
layout:		property
title:		"arrears_arrangement"
schemas:	[account, loan, security]
---

# arrears_arrangement

---

The **arrears_arrangement** is the property of a loan or debt security that describes how the borrower/issuer and lender/holder are dealing with the unpaid capital or interest (coupon) payments indicated in the **arrears_balance**. An arrears_arrangement does not necessarily require a positive arrears_balance as an arrangement may be reached in anticipation of a future arrears situation eg. *Forbearance*. Forbearance is not an extremely well-defined concept within accounting standards. As such we have adopted the [forbearance definitions and categorisation adopted by the EBA][eba-forbearance-its] and used in the [Finrep ITS][finrep-its]. See also: [BBVA research paper on the topic][bbva-forbearance].

[eba-forbearance-its]: https://www.eba.europa.eu/implementing-technical-standard-supervisory-reporting-forbearance-and-non-performing-exposures
[bbva-forbearance]: https://www.bbvaresearch.com/wp-content/uploads/2017/12/2017-12-IFRS-9-Impact-on-forbearance-practices.pdf
[finrep-its]: https://eba.europa.eu/sites/default/documents/files/documents/10180/2321183/b67323ac-27fa-482d-926e-ae7ba3e90cb8/Annex%20III%20%28Annex%205%20%28FINREP%29%29.pdf

```bash
├── formal
├── interest_grace_period
├── mi_claim_adv
├── modified_tnc
│   ├── prin_def_rate
│   ├── prin_def_rate_term
│   ├── prin_def_term
│   ├── principal_defer
│   ├── principal_forgive
│   ├── rate_prin_forgive
│   ├── rate_red_frozen
│   ├── rate_term
│   ├── rate_term_prin_forgive
│   ├── recap
│   ├── renewal
│   ├── term_ext
│   ├── term_prin_forgive
│   └── term_recap
├── none
├── possessed
│   └── reo
├── refinancing
├── settlement
├── short_sale
└── temporary
```

### formal
This indicates that a formal arrangement has been agreed with the borrower to capitalise the loan with the view to decrease the **arrears_balance** with future payments.

### interest_grace_period
A temporary arrangement where the borrower is allowed to make reduced or no payments for a specified period, with the deferred amounts added to the loan balance.

### mi_claim_adv
A MI Claim Advance (Mortgage Insurance) is a pre-claim payment from the mortgage insurance company to assist borrowers facing mortgage delinquencies. It can help borrowers catch up on payments, buy down the mortgage rate, or receive a wage subsidy, ultimately preventing foreclosure.

### modified_tnc
A modification of the previous terms and conditions of a contract that the debtor is considered unable to comply with due to its financial difficulties ("troubled debt") resulting in insufficient debt service ability and that would not have been granted had the debtor not been experiencing financial difficulties (in relation to forbearance status).

### none
No temporary or formal arrangement or contact has been made with the borrower to "solve" the balance outstanding in the **arrears_balance**.

### possessed
Cases where the underlying collateral has been seized or taken into possession by the lender.

From [MLAR][mlar]:
> In possession: cases should be included here where the property is
F3.6/F4.6 taken in possession (through any method e.g. voluntary surrender, court
order etc). For development loans in particular, cases should also be
included where the appointment of a receiver and/or a manager has been
made, or where the security is being enforced in other ways (which may
or may not also involve the existence of arrears e.g. building finance case
with interest roll up, no arrears, but a current valuation is less than the
outstanding debt).

### prin_def_rate
A combination of [principal_defer] and [rate_red_frozen]

### prin_def_rate_term
A combination of [principal_defer], [term_ext] and [rate_red_frozen]

### prin_def_term
A combination of [principal_defer] and [term_ext]

### principal_defer
When the modification results in deferred principal and includes when principal write-downs occur.

### principal_forgive
When the modification results in principal forgiveness.

### rate_prin_forgive
A combination of [rate_red_frozen] and [principal_forgive]

### rate_red_frozen
When the modification results in an interest rate reduction or if the interest rate was frozen at a lower rate than if allowed to adjust (for ARMs).

### rate_term
A combination of [rate_red_frozen] and [term_ext]

### rate_term_prin_forgive
A combination of [rate_red_frozen], [term_ext] and [principal_forgive]

### recap
When the modification results in recapitalization. Recapitalization referes to instances where accrued and/or deferred principal, interest, servicing advances, expenses, fees, etc. are capitalized into the unpaid principal balance of the modified loan.

### refinancing
The loan has been refinanced with a new loan, either with the same or a different lender, effectively replacing the original loan terms.

### renewal
Loans that have been renewed and contract terms have changed and the borrower does not meet the current BHC or IHC or SLHC credit standards. This is when the borrower has entered into a new contractual obligation with the lender and the HELOC terms have changed.

### reo
Real estate owned (REO) refers to a lender-owned property that is not sold at a foreclosure auction. Properties become REO when owners default and the bank repossesses them and tries to sell them. The lender, which is often a bank, takes ownership of a foreclosed property when it fails to sell at the amount sought to cover the loan. Refer to https://www.investopedia.com/terms/r/realestateowned.asp.

### settlement
Settlement is an agreement to accept as payment in full of the debt an amount that is less than what is contractually owed. Institutions sometimes negotiate settlement agreements with borrowers who are unable to service their unsecured open-end credit. In a settlement arrangement, the institution forgives a portion of the amount owed. In exchange, the borrower agrees to pay the remaining balance either in a lump- sum payment or by amortizing the balance over a several month period.

Settlement programs are another type of workout program in which the bank agrees to accept less than the full balance due from a borrower in full satisfaction of the debt. As with any other workout program, collectors should determine the borrower's ability to repay under the settlement terms.

### short_sale
A short sale is a type of loss mitigation where the property is sold by the borrower for less than is owed on the mortgage.

### temporary
This indicates cases where the lender has made a temporary concession to the borrower to assist them with their payments of the **arrears_balance**.
From [MLAR][mlar]:
> agreement with the borrower whereby monthly payments are either suspended or less than they would be on a fully commercial basis

### term_ext
When the modification results in a term extension.

### term_prin_forgive
A combination of [term_ext] and [principal_forgive]

### term_recap
A combination of [term_ext] and [recap]

[mlar]: http://www.bankofengland.co.uk/pra/documents/regulatorydata/mlar/sup_chapter16_annex19bg_20120401.pdf 