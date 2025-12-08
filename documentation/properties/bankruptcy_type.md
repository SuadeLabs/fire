---
layout:		property
title:		"bankruptcy_type"
schemas:	[customer, issuer, guarantor]
---

# bankruptcy_type

---

# Bankruptcy Type
The bankruptcy chapter of the borrower.

```bash
├── court_administration
├── insolvency
│   ├── chapter_7
│   ├── chapter_9
│   ├── chapter_11
│   ├── chapter_12
│   └── chapter_13
└── other
```

### chapter_7
[Chapter 7][chapter_7] of the Bankruptcy Code provides for "liquidation" - the sale of a debtor's nonexempt property and the distribution of the proceeds to creditors.

### chapter_9
[Chapter 9][chapter_9] of the Bankruptcy Code provides for reorganization of municipalities, which includes cities and towns, as well as villages, counties, taxing districts, municipal utilities, and school districts.

### chapter_11
[Chapter 11][chapter_11] of the Bankruptcy Code provides for reorganization, usually involving a corporation or partnership. A Chapter 11 debtor usually proposes a plan of reorganization to keep its business alive and pay creditors over time. People in business or individuals also can seek relief in Chapter 11.

### chapter_12
[Chapter 12][chapter_12] of the Bankruptcy Code provides for adjustment of debts of a "family farmer," or a "family fisherman" as those terms are defined in the U.S. Bankruptcy Code.

### chapter_13
[Chapter 13][chapter_13] of the Bankruptcy Code provides for adjustment of debts of an individual with regular income. Chapter 13 allows a debtor to keep property and pay debts over time, usually three to five years.

### court_administration
Any proceeding involving the intervention of a judicial body or similar aimed at reaching a refinancing agreement among the creditors, with the exception of any bankruptcy or insolvency proceedings.

### insolvency
Any proceeding involving the intervention of a judicial body or similar aimed at reaching a refinancing agreement among the creditors, with the exception of any bankruptcy or insolvency proceedings.

### other
Use this when the customer is understood to be bankrupt but where the exact bankruptcy chapter is unknown or does not meet another definition within the taxonomy.


---

[chapter_7]: https://www.uscourts.gov/court-programs/bankruptcy/bankruptcy-basics/chapter-7-bankruptcy-basics
[chapter_9]: https://www.uscourts.gov/court-programs/bankruptcy/bankruptcy-basics/chapter-9-bankruptcy-basics
[chapter_11]: https://www.uscourts.gov/court-programs/bankruptcy/bankruptcy-basics/chapter-11-bankruptcy-basics
[chapter_12]: https://www.uscourts.gov/court-programs/bankruptcy/bankruptcy-basics/chapter-12-bankruptcy-basics
[chapter_13]: https://www.uscourts.gov/court-programs/bankruptcy/bankruptcy-basics/chapter-13-bankruptcy-basics