---
layout:		property
title:		"repayment_type"
schemas:	[loan, security]
---

# repayment_type

---

The **repayment_type** property describes the repayment conditions of the loan. In short, the repayment type determines the contractual agreement the lender has made with the borrower regarding repayments:

## Loan
```bash
├── combined
├── interest_only
├── option_arm
├── other
└── repayment
```

### interest_only
The borrower will be meeting the [**accrued_interest**](https://github.com/suadelabs/fire/blob/master/documentation/properties/accrued_interest.md) amounts but not reducing the [**balance**](https://github.com/suadelabs/fire/blob/master/documentation/properties/balance.md) of the loan.

### repayment
The borrower will be paying the interest as well as the capital in an amortising manner such that the [**balance**](https://github.com/suadelabs/fire/blob/master/documentation/properties/balance.md) amount will be decreasing to zero over the life of the loan.

### combined
The borrower's repayment terms of the loan are a combination of **repayment** and **interest_only**. For example, the borrower typically has a **repayment** schedule but has an **interest_only** schedule during the summer.

### option_arm
A payment Option ARM is a nontraditional mortgage that allows the borrower to choose from a number of different payment options. For example, each month, the borrower may choose: a minimum payment option based on a ''start'' or introductory interest rate, an interest-only payment option based on the fully indexed interest rate, or a fully amortizing principal and interest payment option based on a 15-year or 30-year loan term, plus any required escrow payments. Payments on the minimum payment option can be less than the interest accruing on the loan, resulting in negative amortization. The interest-only option avoids negative amortization, but does not provide for principal amortization. After a specified number of years, or if the loan reaches a certain negative amortization cap, the required monthly payment amount is recast to require payments that will fully amortize the outstanding balance. Refer to [Federal Reserve FR Y-14M](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14M).

### other
The contractual terms do not specify a **repayment_type** and the borrower is free to pay the interest and/or capital on their own schedule. Credit cards and other credit facilities might have repayment_type = "other" characteristics. We use "other" here instead of "none" as it is assumed all loans are made under the premise of repayment.

## Security
```bash
├── other
├── pr2s
├── pr2s_abcp
├── pr2s_non_abcp
├── pro_rata
└── sequential
```

### sequential
Sequential amortisation

### pro_rata
Pro-rata amortisation

### pr2s
Pro-rata amortisation changing to sequential amortisation. Not compliant

### pr2s_abcp
Pro-rata amortisation changing to sequential amortisation. Compliant with STS criteria for on-balance sheet securitisations  (Article 26c (5) of Regulation (EU) 2017/2402).

### pr2s_non_abcp
Pro-rata amortisation changing to sequential amortisation. Compliant with STS criteria for non-ABCP transactions  (Guidelines on STS criteria for non-ABCP transactions and Article 21 (5) of Regulation (EU) 2017/2402

### other
Other amortisation system

See:
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02017R2402-20210409#:~:text=Losses%20shall%20be,forward%2Dlooking%20trigger.
