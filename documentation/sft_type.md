 ---

layout:     property
title:      "sft_type"
schemas:    [security]

---


# sft_type
The **sft_type** is used when describing securities financing transactions using the security schema. Securities Financing Transactions (SFTs) allow market partcipants to access secured funding, through the temporary exchange of assets as a guarantee for a funding transaction. 

```bash
├── margin_loan
├── repo
│   ├── bond_loan
│   ├── stock_loan
│   └── sell_buy_back
└── rev_repo
    ├── bond_borrow
    ├── stock_borrow
    └── buy_sell_back
```

**ex.**
> A bank does 6 security deals:
> - deal #1 - bank executes a repo transaction and lends a covered bond worth 100 in exchange for 90 in cash
> - deal #2 - bank executes a collateral swap transaction and lends a portfolio of shares worth 100 in exchange for 1 share worth 45 and one index linked gilt worth 50
> - deal #3 - bank issues commercial paper at par and receives 100 from investors
> - deal #4 - bank executes a reverse repo transaction and borrows a bond worth 100 in exchange for 90 in cash
> - deal #5 - bank is holding 50 of cash
> - deal #6 - bank is holding 50 worth of auto ABS


| id | deal_id | date     | start_date | end_date | value_date | mtm_dirty | sft_type     | type              | movement | asset_liability |
|----|---------|----------|------------|----------|------------|-----------|--------------|-------------------|----------|-----------------|
| 1  | 1       | 18/08/16 | 18/08/16   | 17/10/16 | 18/08/16   | -100      | repo         | covered_bond      | asset    | asset           |
| 2  | 1       | 18/08/16 | 18/08/16   | 17/10/16 | 18/08/16   | 90        | repo         | covered_bond      | cash     | liability       |
| 3  | 2       | 18/08/16 | 13/08/16   | 12/09/16 | 18/08/16   | -100      | stock_loan   | share_agg         | asset    | asset           |
| 4  | 2       | 18/08/16 | 17/08/16   | 16/09/16 | 18/08/16   | 50        | stock_borrow | share             | asset    | liability       |
| 5  | 2       | 18/08/16 | 12/08/16   | 11/10/16 | 18/08/16   | 45        | bond_borrow  | index_linked_gilt | asset    | liability       |
| 6  | 3       | 18/08/16 | 18/08/16   | 17/09/16 | 18/08/16   | -100      |              | debt_issue        | asset    | asset           |
| 7  | 3       | 18/08/16 | 13/08/16   | 12/09/16 | 18/08/16   | 100       |              | debt_issue        | cash     | liability       |
| 8  | 4       | 18/08/16 | 21/08/16   | 20/09/16 | 18/08/16   | 100       | rev_repo     | bond              | asset    | liability       |
| 9  | 4       | 18/08/16 | 21/08/16   | 20/09/16 | 18/08/16   | -90       | rev_repo     | bond              | cash     | asset           |
| 10 | 5       | 18/08/16 | 16/08/16   | 15/09/16 | 18/08/16   | 50        |              | cash              | cash     | asset           |
| 11 | 6       | 18/08/16 | 16/08/16   | 15/09/16 | 18/08/16   | 50        |              | abs_auto          | asset    | asset           |
