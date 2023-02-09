---
layout:     property
title:      "last_drawdown_date"
schemas:    [account, loan]
---

# last_drawdown_date

---

The date on which the last drawdown occurred for this account (ie. overdraft).

Relevant for determining "transactors" as per the Basel Framework 20.66:
> "Transactors" are obligors in relation to facilities such as credit cards and charge cards where the balance has been repaid in full at each scheduled repayment date for the previous 12 months. Obligors in relation to overdraft facilities would also be considered as transactors if there has been no drawdown over the previous 12 months.

Relevant for determining "transactors" as per OSFI BCAR Framework Chapter 4 P 84:
> Transactors are obligors in relation to facilities such as credit cards and charge cards with an interest free grace period, where the accrued interest over the previous 12 months is less than $50, or obligors in relation to overdraft facilities or lines of credit would also be considered as transactors if there has been no drawdowns over the previous 12 months
