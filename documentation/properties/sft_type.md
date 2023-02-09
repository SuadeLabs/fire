---
layout:     property
title:      "sft_type"
schemas:    [security]
---

# sft_type

---

The **sft_type** is used when describing securities financing transactions using the security schema. Securities Financing Transactions (SFTs) allow market partcipants to access secured funding, through the temporary exchange of assets as a guarantee for a funding transaction.

[SFT Regulation][sftr] Article 3(11):
> 'securities financing transaction' or 'SFT' means:
> (a) a repurchase transaction;
> (b) securities or commodities lending and securities or commodities borrowing;
> (c) a buy-sell back transaction or sell-buy back transaction;
> (d) a margin lending transaction;


```bash
├── repo
├── rev_repo
├── lending
│   ├── bond_loan
│   ├── stock_loan
│   └── sell_buy_back
├── borrowing
│   ├── bond_borrow
│   ├── stock_borrow
│   └── buy_sell_back
├── margin_loan
└── term_funding_scheme
```


### sec_lending, sec_borrowing
[SFT Regulation][sftr] Article 3(7):
> 'securities or commodities lending' or 'securities or commodities borrowing' means a transaction by which a counterparty transfers securities or commodities subject to a commitment that the borrower will return equivalent securities or commodities on a future date or when requested to do so by the transferor, that transaction being considered as securities or commodities lending for the counterparty transferring the securities or commodities and being considered as securities or commodities borrowing for the counterparty to which they are transferred;

### buy_sell_back
### sell_buy_back
[SFT Regulation][sftr] Article 3(8):
> 'buy-sell back transaction' or 'sell-buy back transaction' means a transaction by which a counterparty buys or sells securities, commodities, or guaranteed rights relating to title to securities or commodities, agreeing, respectively, to sell or to buy back securities, commodities or such guaranteed rights of the same description at a specified price on a future date, that transaction being a buy-sell back transaction for the counterparty buying the securities, commodities or guaranteed rights, and a sell-buy back transaction for the counterparty selling them, such buy-sell back transaction or sell-buy back transaction not being governed by a repurchase agreement or by a reverse-repurchase agreement within the meaning of point (9);

### repo
### rev_repo
[SFT Regulation][sftr] Article 3(9):
> 'repurchase transaction' means a transaction governed by an agreement by which a counterparty transfers securities, commodities, or guaranteed rights relating to title to securities or commodities where that guarantee is issued by a recognised exchange which holds the rights to the securities or commodities and the agreement does not allow a counterparty to transfer or pledge a particular security or commodity to more than one counterparty at a time, subject to a commitment to repurchase them, or substituted securities or commodities of the same description at a specified price on a future date specified, or to be specified, by the transferor, being a repurchase agreement for the counterparty selling the securities or commodities and a reverse repurchase agreement for the counterparty buying them;

### margin_loan
[SFT Regulation][sftr] Article 3(10):
> 'margin lending transaction' means a transaction in which a counterparty extends credit in connection with the purchase, sale, carrying or trading of securities, but not including other loans that are secured by collateral in the form of securities;

### term_funding_scheme
Under the term funding scheme (TFS), participating banks and building societies were able to borrow funds from the Bank of England at a rate close to Bank Rate for up to four years. More information [here][tfs].

Note that ECB equivalent of TFS is the Targeted longer-term refinancing operations ([TLTRO][tltro]).

[tfs]: https://www.bankofengland.co.uk/markets/market-notices/2020/term-funding-scheme-market-notice-mar-2020
[tltro]: https://www.ecb.europa.eu/mopo/implement/omo/tltro/html/index.en.html 

### bond_borrow
### bond_loan
### stock_borrow
### stock_loan
*Needs definition*


**example**
> A bank does 6 security deals:
> - deal #1 - bank executes a repo transaction and lends a covered bond worth 100 in exchange for 90 in cash
> - deal #2 - bank executes a collateral swap transaction and lends a portfolio of shares worth 100 in exchange for 1 share worth 45 and one index linked gilt worth 50
> - deal #3 - bank executes a reverse repo transaction and borrows a bond worth 100 in exchange for 90 in cash
> - deal #4 - bank is holding 50 of cash
> - deal #5 - bank is holding 50 worth of auto ABS


| id | deal_id | date     | start_date | end_date | value_date | mtm_dirty | sft_type     | type              | movement   | asset_liability |
|----|---------|----------|------------|----------|------------|-----------|--------------|-------------------|------------|-----------------|
| 1  | 1       | 18/08/16 | 18/08/16   | 17/10/16 | 18/08/16   | -100      | repo         | covered_bond      | asset      | asset           |
| 2  | 1       | 18/08/16 | 18/08/16   | 17/10/16 | 18/08/16   | 90        | repo         | covered_bond      | cash       | liability       |
| 3  | 2       | 18/08/16 | 13/08/16   | 12/09/16 | 18/08/16   | -100      | stock_loan   | share_agg         | asset      | asset           |
| 4  | 2       | 18/08/16 | 17/08/16   | 16/09/16 | 18/08/16   | 50        | stock_borrow | share             | asset      | liability       |
| 5  | 2       | 18/08/16 | 12/08/16   | 11/10/16 | 18/08/16   | 45        | bond_borrow  | index_linked_gilt | asset      | liability       |
| 5  | 3       | 18/08/16 | 21/08/16   | 20/09/16 | 18/08/16   | 100       | rev_repo     | bond              | asset      | liability       |
| 7  | 3       | 18/08/16 | 21/08/16   | 20/09/16 | 18/08/16   | -90       | rev_repo     | bond              | cash       | asset           |
| 8  | 4       | 18/08/16 | 16/08/16   | 15/09/16 | 18/08/16   | 50        |              | cash              | cash       | asset           |
| 9  | 5       | 18/08/16 | 16/08/16   | 15/09/16 | 18/08/16   | 50        |              | abs_auto          | asset      | asset           |

[sftr]: http://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32015R2365&qid=1466153681918
