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
├── cancelled_payout_agreed
├── audited
└── unaudited
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

### audited
Indicates profits that have been verified by persons independent of the firm that are responsible for the auditing of the firm’s accounts, as specified in condition (a) of Article 26 (2) of the CRR.

### unaudited
Indicates profits that have not been verified by persons independent of the firm that are responsible for the auditing of the firm’s accounts, thereby not meeting condition (a) of Article 26 (2) of the CRR.

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
    └── cancellable
├── cancelled
└── defaulted
```
### actual
This is a live loan.

### committed
This is a loan offer or commitment to a customer that a customer could draw down (typically also denoted as off balance sheet).

### cancellable
Indicates when an institution has the right to *unconditionally* cancel the commitment without notice to the obligor.  This is either commitment to an undrawn portion of a loan or revolving credit, or commitment to enter into another contract (off-balance sheet).

See definition from OSFI Chapter 4, P124:
> Commitments are arrangements that obligate an institution, at a client's request, to extend credit, purchase assets or issue credit substitutes. It includes any such arrangement that can be unconditionally cancelled by the institution at any time without prior notice to the obligor. It also includes any such arrangement that can be cancelled by the institution if the obligor fails to meet conditions set out in the facility documentation, including conditions that must be met by the obligor prior to any initial or subsequent drawdown under the arrangement. Counterparty risk weightings for OTC derivative transactions will not be subject to any specific ceiling. [Basel Framework, CRE 20.94]

See also [Basel CRE 20.94](https://www.bis.org/basel_framework/chapter/CRE/20.htm?tldate=20220101&inforce=20230101&published=20201126#:~:text=Off%2Dbalance%20sheet,any%20specific%20ceiling.):
> Off-balance sheet items will be converted into credit exposure equivalents through the use of credit conversion factors (CCF). In the case of commitments, the committed but undrawn amount of the exposure would be multiplied by the CCF. For these purposes, commitment means any contractual arrangement that has been offered by the bank and accepted by the client to extend credit, purchase assets or issue credit substitutes.43 It includes any such arrangement that can be unconditionally cancelled by the bank at any time without prior notice to the obligor. It also includes any such arrangement that can be cancelled by the bank if the obligor fails to meet conditions set out in the facility documentation, including conditions that must be met by the obligor prior to any initial or subsequent drawdown under the arrangement. Counterparty risk weightings for over-the-counter (OTC) derivative transactions will not be subject to any specific ceiling.

### cancelled
This is a loan that was committed but then later cancelled due to refusal by customer or expiry of offer.

### defaulted
This is a loan where the customer has defaulted or is non-performing.

## Security
```bash
├── paid_up
├── called_up
├── bankruptcy_remote
├── unsettled
    └── free_deliveries
└── non_operational
```

### paid_up
This indicates that capital has been [paid up][paidup] by the shareholders to the company that issued the shares.
When used in combination with the purpose attribute, 'default_fund', equates to prefunded default fund contributions.

### called_up
This indicates that capital has been [called up][calledup] by the company issuing the shares but has not been paid yet by the shareholders.
When used in combination with the purpose attribute, 'default_fund', equates to unfunded default fund contributions.

[paidup]: https://www.acra.gov.sg/how-to-guides/setting-up-a-local-company/share-capital
[calledup]: https://www.legislation.gov.uk/ukpga/2006/46/section/547?view=plain

### bankruptcy_remote
This indicates that the reporting institution has determined that the security will not be available to an entity’s creditors
in the event of the insolvency of that entity. When used in combination with the purpose attributes indicates that collateral
posted by the reporting institution to its counterparty as initial or variation margin, is held in a bankruptcy-remote manner,
and is therefore segregated from the counterparty's assets, as defined in Articles 276(1)(g) and 300(1) CRR.
When bankruptcy_remote is used in conjuction with the purpose 'custody', this indicates that the security held in custody will
not be available to the custodian's creditors in the event of the insolvency of the custodian.

### non_operational
This indicates that the security does not meet the requirements set in Article 8 of the [Liquidity Regulations][lcr]

### unsettled
This indicates that the transaction is still unsettled after its due delivery date. Under the Basel framework, this transaction would be in scope for the requirements defined under [the capital treatment of unsettled transactions and failed trades][CRE70]"

### free_deliveries

From [CRE70.10](https://www.bis.org/basel_framework/chapter/CRE/70.htm#:~:text=Capital%20requirements%20for%20non%2DDvP%20transactions%20(free%20deliveries)), free deliveries are a specific type of unsettled transaction. Indicates that cash is paid without receipt of the corresponding receivable  (securities, foreign currencies, gold, or commodities) or, conversely, deliverables were delivered without receipt of the corresponding cash payment (non-DvP, or free deliveries) expose firms to a risk of loss on the full amount of cash paid or deliverables delivered.


## Derivative
```bash
└── unsettled
    └── free_deliveries
```

### unsettled

This indicates that the transaction is still unsettled after its due delivery date. Under the Basel framework, this transaction would be in scope for the requirements defined under [the capital treatment of unsettled transactions and failed trades][CRE70]"

### free_deliveries

From [CRE70.10](https://www.bis.org/basel_framework/chapter/CRE/70.htm#:~:text=Capital%20requirements%20for%20non%2DDvP%20transactions%20(free%20deliveries)), free deliveries are a specific type of unsettled transaction. Indicates that cash is paid without receipt of the corresponding receivable  (securities, foreign currencies, gold, or commodities) or, conversely, deliverables were delivered without receipt of the corresponding cash payment (non-DvP, or free deliveries) expose firms to a risk of loss on the full amount of cash paid or deliverables delivered.

---
[lcr]:  http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0061
[reg-d]: https://www.ecfr.gov/cgi-bin/retrieveECFR?gp=&SID=fe8bd6e281e0788a9ba7efda92e96e2f&mc=true&n=pt12.2.204&r=PART&ty=HTML#se12.2.204_12
[CRE70]: https://www.bis.org/basel_framework/chapter/CRE/70.htm
