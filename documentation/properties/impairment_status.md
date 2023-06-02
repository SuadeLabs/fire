---
layout:		property
title:		"impairment_status"
schemas:	[account, loan, security, derivative]
---

# impairment_status

---

```bash
├── performing
│   ├── stage_1
│   │   ├── normal (aka pass)
│   │   └── watch (aka special mention)
│   └── stage_2
│       └── substandard
├── non_performing
│   └── stage_3
│       ├── doubtful
│       ├── loss
│       ├── in_litigation
│       └── pre_litigation
├── stage_1_normal
├── stage_1_watch
├── stage_1_substandard
├── stage_1_doubtful
├── stage_1_loss
├── stage_2_normal
├── stage_2_watch
├── stage_2_substandard
├── stage_2_doubtful
├── stage_2_loss
├── stage_3_normal
├── stage_3_watch
├── stage_3_substandard
├── stage_3_doubtful
└── stage_3_loss

```

> NOTE: due to ambiguities in definitions and differences in credit grade and risk stage models, unexpected combinations like IFRS "stage_1" and "doubtful" may be present in a firm's data. To avoid passing judgement on an internal model, we include all 15 combinations of stages and credit grades should firms choose to define their own hierarchy.

Under [IFRS9][ifrs9] accounting principles, impairment must be recognised in stages and this standard is being adopted globally. Historically, at the most granular level, agencies are largely adopting and documenting industry best practices. Some jurisdictions employ even more detailed assessments with 10 or more categories going in to more granular detail.

Further reading:
* [BCBS Insights: The identification and measurement of non-performing assets: a cross-country comparison][bcbs-i7]
* [US: Interagency Supervisory Guidance Addressing Certain Issues Related to Troubled Debt Restructurings ][sr13-17]
* [HKMA Loan classification system][hkma-lcs]
* [MAS 612][mas612]

Some agencies may also refer to *classified* loans as those that fall in substandard, doubtful and loss categories (occassionally watch/special mention as well).

### performing

### stage_1
**stage_1** assets are financial instruments that either have not deteriorated significantly in credit quality since initial recognition or have low credit risk. In this stage, financial institutions must recognise the expected credit losses that result from default events on a financial instrument that are possible within the 12 months after the reporting date.

### normal (pass)
HKMA LCS:
> This refers to loans where borrowers are current in meeting commitments and
full repayment of interest and principal is not in doubt.

MAS 612:
> This indicates that timely repayment of the outstanding credit facility is
not in doubt. Repayment is prompt and the credit facility does not exhibit any
potential weakness in repayment capability, business, cash flow or financial
position of the borrower.

### watch (special mention)
HKMA LCS:
> This refers to loans where borrowers are experiencing difficulties which may threaten the institution's position. Ultimate loss is not expected at this stage but could occur if adverse conditions persist. These loans exhibit one or more of the following characteristics:
a) early signs of liquidity problems such as delay in servicing loans;
b) inadequate loan information such as annual audited financial statements not obtained or available;
c) the condition of and control over collateral is questionable;
d) failure to obtain proper documentation or non-cooperation by the borrower or difficulty in keeping contact with him;
e) slowdown in business or adverse trend in the borrower's operations that
signals a potential weakness in the financial strength of the borrower but
which has not reached a point where servicing of the loan is jeopardised;
f) volatility in economic or market conditions which may in the future affect the borrower negatively;
g) poor performance in the industry in which the borrower operates;
h) the borrower or in the case of corporate borrowers, a key executive, is in ill health;
i) borrower is the subject of litigation which may have a significant impact on
his financial position; and/or
j) even if the loan in question is current, the borrower is having difficulty in servicing other loans (either from the institution concerned or from other
institutions).

MAS 612:
> this indicates that the credit facility exhibits potential weaknesses that, if not corrected in a timely manner, may adversely affect repayment by the borrower at a future date, and warrant close attention by a bank.  Characteristics of “special mention” credit facilities include the following:
(i) a declining trend in the operations of the borrower that signals a potential weakness in the financial position of the borrower, but not to the point that repayment is jeopardised;
(ii) economic and market conditions that may unfavourably affect the profitability and business of the borrower in the future.

### stage_2
**stage_2** assets are those which have experienced a significant change in the estimated default risk over the remaining expected life of the financial instrument. In this stage, financial institutions must recognise the expected credit losses that result from default events over the full lifetime of the financial instrument.
For stage 2 assets, interest revenue is also accrued on the gross carrying amount.

From the [Open Risk Manual][orm]:
> **Determination of Significant Increase in Credit Risk:**
	Determination of whether SICR has occurred or not is required at each reporting date
	The assessment must use the change in the Default Risk over the expected life of the financial instrument, hence specifically not the change in the amount of expected credit losses
    The comparison is between the Default Risk as estimated at the reporting date and the Default Risk at initial recognition (it is a relative assessment)
    The assessment must use Reasonable and Supportable Information (see below for examples)
    If an instrument initially deemed to be Low Credit Risk continues being assessed as such, it is deemed that there has been no significant increase

> **Risk Increase Indicators**
 	Risk Indicators the can establish whether there has been a significant increase in risk vary considerably depending on the nature of the borrower, the product type, internal management methods and external market resources.

> **Elements to Consider**
	Quantitative Elements: Scorecards or Risk Rating Systems after setting thresholds for determining what constitutes SICR in terms of the score or rating
    Qualitative Elements
    Backstop Indicators
    Low Credit Risk exception

> The following lists provide some examples:

> **Internal (Management) Indicators**
    Significant changes in internal price indicators of credit risk (the credit spread / premium that would be charged currently for similar risk)
    Other changes in the rates of terms of an existing financial instrument that would be significantly different if the instrument was newly originated
    Significant changes in external market indicators of credit risk for a particular financial instrument or similar financial instruments with the same expected life
    Changes in the entity’s credit management approach in relation to the financial instrument; ie based on emerging indicators of changes in the credit risk of the financial instrument, the entity’s credit risk management practice is expected to become more active or to be focused on managing the instrument, including the instrument becoming more closely monitored or controlled, or the entity specifically intervening with the borrower
    Expected changes in the loan documentation including an expected breach of contract that may lead to covenant waivers or amendments, interest payment holidays, interest rate step-ups, requiring additional collateral or guarantees, or other changes to the contractual framework of the instrument
    Past due information
    Significant increases in credit risk on other financial instruments of the same borrower.
    Significant changes in the expected performance and behaviour of the borrower, including changes in the payment status of borrowers in the group (for example, an increase in the expected number or extent of delayed contractual payments or significant increases in the expected number of credit card borrowers who are expected to approach or exceed their credit limit or who are expected to be paying the minimum monthly amount)
    A significant change in the quality of the guarantee provided by a shareholder (or an individual’s parents) if the shareholder (or parents) have an incentive and financial ability to prevent default by capital or cash infusion.
    Significant changes, such as reductions in financial support from a parent entity or other affiliate or an actual or expected significant change in the quality of credit enhancement, that are expected to reduce the borrower’s economic incentive to make scheduled contractual payments. Credit quality enhancements or support include the consideration of the financial condition of the guarantor and/or, for interests issued in securitisations, whether subordinated interests are expected to be capable of absorbing expected credit losses (for example, on the loans underlying the security).

> **External (Market) Indicators**
    Credit spreads
    Credit default swap prices for the borrower
    Length of time (duration) or the extent (degree) to which the fair value of a financial asset is less then the amortized cost
    Other market information related to the borrower
    Significant change in the value of the collateral supporting the obligation or in the quality of third-party guarantees or credit enhancements, which are expected to reduce the borrower’s economic incentive to make scheduled contractual payments or to otherwise have an effect on the probability of a default occurring. For example, if the value of collateral declines because house prices decline, borrowers in some jurisdictions have a greater incentive to default on their mortgages.
    Actual or expected significant downgrade in an external credit rating
    Existing or forecast adverse changes in business, financial or economic conditions that are expected to cause a significant change in the borrower’s ability to meet its debt obligations, such as an actual or expected increase in interest rates or an actual or expected significant increase in unemployment rates
    An actual or expected significant adverse change in the regulatory, economic, or technological environment of the borrower that results in a significant change in the borrower’s ability to meet its debt obligations, such as a decline in the demand for the borrower’s sales product because of a shift in technology.
    Actual or expected significant internal credit rating downgrade or decrease (worsening) in behavioural scoring used to assess credit risk internally
    Actual or expected significant change in the operating results of the borrower. Examples include actual or expected declining revenues or margins, increasing operating risks, working capital deficiencies, decreasing asset quality, increased balance sheet leverage, liquidity, management problems or changes in the scope of business or organisational structure (such as the discontinuance of a segment of the business) that results in a significant change in the borrower’s ability to meet its debt obligations.

> **Example**
	For the purpose of the EBA 2018 EU-Wide Stress Test projections banks shall, as a backstop, assume that Stage 1 assets which experience a threefold increase of annual point-in-time PD compared to the corresponding value at initial recognition (i.e. a 200% relative increase) undergo a significant increase in credit risk (SICR) and hence become Stage 2. Notably the backstop is defined with reference to the annual PD, not the lifetime PD.

### substandard
HKMA LCS:
> This refers to loans where borrowers are displaying a definable weakness that is likely to jeopardise repayment. The institution is relying heavily on available security. This would include loans where some loss of principal or interest is possible after taking account of the "net realisable value" of security, and rescheduled loans where concessions have been made to a customer on interest or principal such as to render the loan "non-commercial" to the bank. These loans exhibit one or more of the following characteristics:
a) repayment of principal and/or interest has been overdue for more than three months and the net realisable value of security is insufficient to cover the payment of principal and accrued interest;
b) even where principal and accrued interest are fully secured, a "substandard" classification will usually be justified where repayment of principal and/or interest is overdue* for more than 12 months;
c) in the case of unsecured or partially secured loans, a “substandard” classification may also be justified, even if the overdue period is less than three months, where other significant deficiencies are present which threaten the borrower’s business, cash flow and payment capability. These include:
* credit history or performance record is not satisfactory;
* labour disputes or unresolved management problems which may affect the business, production or profitability of the borrower;
* increased borrowings not in proportion with the borrower's business;
* the borrower experiencing difficulties in repaying obligations to other creditors;

MAS 612:
>  this indicates that the credit facility exhibits definable weaknesses, either in respect of the business, cash flow or financial position of the borrower that may jeopardise repayment on existing terms. Characteristics of “substandard” credit facilities include the following:
(i) inability of the borrower to meet contractual repayment terms of the credit facility;
(ii) unfavourable economic and market conditions or operating problems that would affect the profitability and business of the borrower in the future;
(iii) weak financial condition or the inability of the borrower to generate sufficient cash flow to service the payments;
(iv) difficulties experienced by the borrower in repaying other credit facilities granted by the same bank, or by other financial institutions (where such information is available);
(v) breach of any key financial covenants by the borrower.
A bank shall assess the severity of each weakness exhibited by the credit facility and consider whether the weakness, when considered singly and in combination with other weaknesses, would adversely affect the repayment ability of the borrower.

### non_performing

### stage_3
**stage_3** assets are those which whose credit quality has detiorated to the extent that they show objective evidence of a credit loss event. Practically, these would have been those assets which, under the previous IAS 39 accounting standards would have been considered impairment allowances. In this stage, financial institutions must also recognise the expected credit losses that result from default events over the full lifetime of the financial instrument.
Furthermore, interest revenue should also be accrued on the *net* carrying amount.

### doubtful
HKMA LCS:
> This refers to loans where collection in full is improbable and the institution expects to sustain a loss of principal and/or interest after taking account of the net realisable value of security. Doubtful loans exhibit one or more of the following characteristics:
a) repayment of principal and/or interest has been overdue for more than six months and the net realisable value of security is insufficient to cover the payment of principal and accrued interest; and/or
b) in the case of unsecured or partially secured loans, a shorter overdue period may also justify a “doubtful” classification if other serious  deficiencies, such as default, death, bankruptcy or liquidation of the borrower, are detected or if the borrower’s whereabouts are unknown.

MAS 612:
> this indicates that the outstanding credit facility exhibits more severe weaknesses than those in a “substandard” credit facility, such that the prospect of full recovery of the outstanding credit facility is questionable and the prospect of a loss is high, but the exact amount remains undeterminable as yet. Consumer loans past due for 120 days or more, but less than 180 days fall under this classification.

### loss
HKMA LCS:
> This refers to loans which are considered uncollectible after exhausting all collection efforts such as realisation of collateral, institution of legal proceedings, etc.

MAS 612:
> this indicates that the outstanding credit facility is not collectable, and little or nothing can be done to recover the outstanding amount from any collateral or from the assets of the borrower generally. Consumer loans past due for 180 days or more fall under this classification.

### in_litigation
From Annex 5, FINREP ITS: An exposure shall be ‘in litigation status’ where legal action against the debtor has formally been taken. This comprises cases where a court of law confirmed that formal judiciary proceedings have occurred or the judiciary system has been notified of the intention to commence legal proceedings. [eba-680]

### pre_litigation
From Annex 5, FINREP ITS: An exposure shall be ‘in pre-litigation status’ where the debtor has been formally notified that the institution will take legal action against the debtor within a defined time period, unless certain contractual or other payment obligations are met. That shall also include cases where the contract has been terminated by the reporting institution because the debtor is in formal breach of the terms and conditions of the contract and the debtor has been notified accordingly, but no legal action against the debtor has formally been taken by the institution yet. [eba-680]

### stage_1_normal
*Included for completeness, not recommended to use*

### stage_1_watch
*Included for completeness, not recommended to use*

### stage_1_substandard
*Included for completeness, not recommended to use*

### stage_1_doubtful
*Included for completeness, not recommended to use*

### stage_1_loss
*Included for completeness, not recommended to use*

### stage_2_normal
*Included for completeness, not recommended to use*

### stage_2_watch
*Included for completeness, not recommended to use*

### stage_2_substandard
*Included for completeness, not recommended to use*

### stage_2_doubtful
*Included for completeness, not recommended to use*

### stage_2_loss
*Included for completeness, not recommended to use*

### stage_3_normal
*Included for completeness, not recommended to use*

### stage_3_watch
*Included for completeness, not recommended to use*

### stage_3_substandard
*Included for completeness, not recommended to use*

### stage_3_doubtful
*Included for completeness, not recommended to use*

### stage_3_loss
*Included for completeness, not recommended to use*



[ifrs9]: https://www.iasplus.com/en-gb/standards/ifrs-en-gb/ifrs9
[orm]: https://www.openriskmanual.org/wiki/Significant_Increase_in_Credit_Risk
[hkma-lcs]: https://www.hkma.gov.hk/media/eng/doc/key-functions/banking-stability/banking-policy-and-supervision/regulatory-framework/ma(bs)2aci(app2)_e.pdf
[sr13-17]: https://www.fdic.gov/regulations/resources/director/college/ny/materials/2012-loans.pdf
[mas612]: https://www.mas.gov.sg/-/media/MAS/Notices/PDF/MAS-Notice-612-effective-1-Jan-2018.pdf
[bcbs-i7]: https://www.bis.org/fsi/publ/insights7.pdf
[eba-680]: https://www.eba.europa.eu/sites/default/documents/files/documents/10180/2321183/9498635b-c1c1-4f5a-91f2-d676472da3ad/Draft%20final%20report%20on%20ITS%20amending%20ITS%20Rep%20FINREP.pdf?retry=1
