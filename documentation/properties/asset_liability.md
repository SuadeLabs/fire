---
layout:     property
title:      "asset_liability"
schemas:    [account, derivative, derivative cash flow, loan, security]
---

# asset_liability

---

## account
An account is either an **asset**,  a **liability**, an **equity** or **pnl** (Profit & Loss) from the firm's point of view.

### asset
An account is considered an [**asset**][asset] if it is a present economic resource controlled by the entity as a result of
past event. For example, a [loan] [loan] is an asset from the issuing entity's point of view, as the issuing entity expects inflows of economic benefits as a result of issuing a loan, as the account holder pays interest and penalties (if applicable).

### liability
An account is considered a [**liability**][liability] if it is a present obligation of the entity to transfer an economic resource
as a result of past events. For example, a [savings account][savings account] is a liability from the issuing entity's point of view, as the issuing entity expects the issuance of a savings account to lead to an outflow of future economic benefits from the entity, as the issuer pays interest on the funds in the account to the account holder.

### equity
An account is considered an [**equity**][equity] if it represents a residual interest in the firm's assets after all of its liabilities have been deducted. For example, a firm may allocate certain amounts of its profits to a [reserve][reserve] account for specific purposes (e.g. a revaluation reserve or a share plan reserve). This reserve account would be recognised as equity on the firm's balance sheet. Equity is typically split in to two types of accounts, capital and reserves.

An account is considered [Profit and Loss (**pnl**)][pnl] if it represents income or expenses attributable to the firm over the period defined by the start and end dates.

[asset]: http://www.ifrs.org/-/media/project/conceptual-framework/exposure-draft/published-documents/ed-conceptual-framework.pdf
[liability]: http://www.ifrs.org/-/media/project/conceptual-framework/exposure-draft/published-documents/ed-conceptual-framework.pdf
[loan]: https://en.wikipedia.org/wiki/Loan
[savings account]: https://en.wikipedia.org/wiki/Savings_account
[equity]: https://www.ifrs.org/-/media/project/conceptual-framework/exposure-draft/published-documents/ed-conceptual-framework.pdf
[reserve]: https://en.wikipedia.org/wiki/Reserve_(accounting)
---

## derivative
[Derivatives][derivatives] can be either a financial **asset** or a financial **liability** on a firm's balance sheet.

## asset
A derivative is an **asset** on the firm's balance sheet if it has a positive value with regard to the underlying variable (rate, price, or index).

## liability
A derivative is a **liability** on the firm's balance sheet if it has a negative value with regard to the underlying variable (rate, price, or index).

[derivatives]: http://www.iasplus.com/en-gb/standards/ias/ias39

---

## derivative_cash_flow
A derivative cash flow is where two parties exchange cash flows (or assets) derived from an underlying reference index, security or financial instrument. This will represent either an **asset** or a **liability** on the firm's balance sheet.

Another term for this exchange is a 'swap'. ([Swaps][swaps] are contracts to exchange cash flows as of a specified date or a series of specified dates based on a notional amount and two different underlying financial instruments. Many times a swap will occur because one party has a comparative advantage in one area such as borrowing funds under variable interest rates, while another party can borrow more freely as the fixed rate.)

[swaps]: https://en.wikipedia.org/wiki/Swap_(finance)

A derivative cash flow exchange (swap) that results in a net positive value after the transaction with regard to the underlying reference index, security or financial instrument is an **asset** on the firm's balance sheet.

A derivative cash flow exchange (swap) that results in a net negative value after the transaction with regard to the underlying reference index, security or financial instrument is a **liability** on the firm's balance sheet.

---

## loan
A loan is either an **asset** or a **liability** for a firm that offers a loan.

### asset
A loan is an [**asset**][asset] on a firm's balance sheet when future economic benefits are expected to flow to the firm as a result of issuing the loan. For example, a mortgage offered by a bank is an asset on the bank's balance sheet as repayments are expected in the future.

### liability
A loan is a [**liability**][liability] on a firm's balance sheet if future economic benefits are expected to flow out of the firm. For example, if a bank has a mortgage loan on its balance sheet, and repayments are made which are greater than the required repayments, then the bank expects to return the overpayments to the borrower leading to an outflow of future economic benefits.

[asset]: https://cdn.ifrs.org/content/dam/ifrs/supporting-implementation/smes/module-11.pdf
[liability]: https://cdn.ifrs.org/content/dam/ifrs/supporting-implementation/smes/module-11.pdf

---

## security
A security is valued using either...

1.  [amortised cost][amortisation]: amortised cost is calculated using the effective interest method. The effective interest rate is the rate that exactly discounts estimated future cash payments or receipts through the expected life of the financial instrument to the net carrying amount of the financial asset or liability. Financial assets that are not carried at fair value though profit and loss are subject to an [impairment test][impairment test]. If expected life cannot be determined reliably, then the contractual life is used;

2. [fair value][fair value]: the amount for which an asset could be exchanged, or a liability settled, between knowledgeable, willing parties in an arm's length transaction.

[amortisation]: https://www.iasplus.com/en-gb/standards/ias/ias39
[impairment test]: https://www.iasplus.com/en-gb/standards/ias/ias36
[fair value]: http://www.iasplus.com/en-gb/standards/ias/ias39

If the valuation leads to expected outflows of economic benefits, then the security is a **liability** on the firm's balance sheet. For example if an [equity security][equity security] was purchased by a firm expecting to receieve future inflows of economic benefits through dividend payments, but a market downturn caused a negative fluctuation in dividend payments, the security may have cost more than its expected future value in terms of economic benefit flows and becomes a **liability** on the firm's balance sheet.

If the valuation leads to expected inflows of economic benefits, then the security is an **asset** on the firm's balance sheet. For example, if an [asset backed security][asset backed security] (e.g. collateralised mortgage obligation) was purchased by a firm expecting to receieve future inflows of economic benefits through repayments of those mortgages, and the security was purchased at a value lower than the expected income from those mortgage repayments over the lifetime of the security, then the security will have a net positive fair value and be an **asset** on the firm's balance sheet.

If the security comes from own funds, it will then be classified as **equity**

[equity security]: http://www.iasplus.com/en-gb/standards/ias/ias39
[asset backed security]: http://www.iasplus.com/en-gb/standards/ias/ias39


---

### pnl
**pnl** is used to identify non-balance sheet information relevant for the firm's Profit & Loss financial statements
