---
layout:		property
title:		"status"
schemas:	[account, customer, loan, security]
---

# status

---

The **status** property indicates the current state of the financial product. A product can be active, cancelled, defaulted, committed etc. This is generally used to differentiate potential offers committed by the institution (lending decision taken) but not yet accepted by a customer. The status could also indicate liabilities which have been cancelled but are still being held within the dataset (until maturity or otherwise).

## Account

```bash
├── active
├── transactional
├── other
├── cancelled
└── cancelled_payout_agreed
```
### active
The account is active and in use by the customer.

### transactional
The account is active in a transactional way, *transactional* being defined in accordance with the [Liquidity Regulations][lcr]:
> LCR Article 24(3):
> For the purposes of paragraph 1(b) a retail deposit shall be considered
> as being held in a transactional account where salaries, income or
> transactions are regularly credited and debited respectively against
> that account.

For US accounts, transactional is defined in [Regulation D][reg-d]:
> Transaction accounts are defined in section 19 of the FRA and in Regulation D as an account from which the depositor or account holder is permitted to "make transfers or withdrawals by negotiable or transferable instrument, payment order of withdrawal, telephone transfer, or other similar device for the purpose of making payments or transfers to third persons or others...." Demand deposits, negotiable order of withdrawal (NOW) accounts, and share draft accounts are all included in the definition of "transaction account." "Time deposits" and "savings deposits," discussed further below, are excluded from the Regulation D definition of transaction account. See the definition of "transaction accounts" in section 204.2(e) of Regulation D.

### cancelled
The account has been cancelled but funds will be rolled-over in to another account on the [**end_date**](https://github.com/SuadeLabs/fire/blob/master/documentation/properties/end_date.md).

### cancelled_payout_agreed
The account has been cancelled and the funds are known to be leaving the financial institution.

### other
Any other status


## Customer

```bash
└── established
```
### established
The reporting institution has determined that the counterparty is part of an established relationship in accordance with the [Liquidity Regulations][lcr] Article 24 (2).


## Loan
```bash
├── actual
├── committed
├── cancelled
└── defaulted
```
### actual
This is a live loan.

### committed
This is a loan offer or commitment to a customer that a customer could draw down (typically also denoted as off balance sheet).

### cancelled
This is a loan that was committed but then later cancelled due to refusal by customer or expiry of offer.

### defaulted
This is a loan where the customer has defaulted or is non-performing.

## Security
```bash
├── paid_up
├── called_up
├── bankruptcy_remote
└── non_operational
```

### paid_up
This indicates that capital has been [paid up][paidup] by the shareholders to the company that issued the shares.
When used in combination with the purpose attribute, 'default_fund', equates to prefunded default fund contributions.

### called_up
This indicates that capital has been [called up][calledup] by the company issuing the shares but has not been paid yet by the shareholders.
When used in combination with the purpose attribute, 'default_fund', equates to unfunded default fund contributions.

[paidup]: https://www.investopedia.com/terms/p/paidupcapital.asp
[calledup]: https://www.investopedia.com/ask/answers/073015/what-difference-between-calledup-share-capital-and-paidup-share-capital.asp

### bankruptcy_remote
This indicates that the reporting institution has determined that the security will not be available to an entity’s creditors
in the event of the insolvency of that entity. When used in combination with the purpose attributes indicates that collateral
posted by the reporting institution to its counterparty as initial or variation margin, is held in a bankruptcy-remote manner,
and is therefore segregated from the counterparty's assets, as defined in Articles 276(1)(g) and 300(1) CRR.
When bankruptcy_remote is used in conjuction with the purpose 'custody', this indicates that the security held in custody will
not be available to the custodian's creditors in the event of the insolvency of the custodian.

### non_operational
This indicates that the security does not meet the requirements set in Article 8 of the [Liquidity Regulations][lcr]

---
[lcr]:  http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0061
[reg-d]: https://www.ecfr.gov/cgi-bin/retrieveECFR?gp=&SID=fe8bd6e281e0788a9ba7efda92e96e2f&mc=true&n=pt12.2.204&r=PART&ty=HTML#se12.2.204_12