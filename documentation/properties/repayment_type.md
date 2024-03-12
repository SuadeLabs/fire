---
layout:		property
title:		"repayment_type"
schemas:	[loan]
---

# repayment_type

---

The **repayment_type** property describes the repayment conditions of the loan. In short, the repayment type determines the contractual agreement the lender has made with the borrower regarding repayments:

### interest_only
The borrower will be meeting the [**accrued_interest**](https://github.com/suadelabs/fire/blob/master/documentation/properties/accrued_interest.md) amounts but not reducing the [**balance**](https://github.com/suadelabs/fire/blob/master/documentation/properties/balance.md) of the loan.

### repayment
The borrower will be paying the interest as well as the capital in an amortising manner such that the [**balance**](https://github.com/suadelabs/fire/blob/master/documentation/properties/balance.md) amount will be decreasing to zero over the life of the loan.

### combined
The borrower's repayment terms of the loan are a combination of **repayment** and **interest_only**. For example, the borrower typically has a **repayment** schedule but has an **interest_only** schedule during the summer.

### other
The contractual terms do not specify a **repayment_type** and the borrower is free to pay the interest and/or capital on their own schedule. Credit cards and other credit facilities might have repayment_type = "other" characteristics. We use "other" here instead of "none" as it is assumed all loans are made under the premise of repayment.


# Security

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
