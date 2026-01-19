---
layout:     property
title:      "interest_only_end_date"
schemas:    [loan]
---

# interest_only_end_date

The **interest_only_end_date** is the date on which the interest-only period ends. Interest-only instruments are those for which, for a contractually set period, only the interest on the principal balance is paid, with the principal balance remaining unchanged.

Reference: [AnaCredit Reporting Manual Part II , section 3.4.10, End Date of the Interest-Only Period](<https://www.ecb.europa.eu/pub/pdf/other/AnaCredit_Manual_Part_II_Datasets_and_data_attributes_201905~cc9f4ded23.en.pdf>)

When reporting the End Date of the Interest-Only Period, we capture the final day of the interest-only phase:
•	If a loan is currently in an interest-only period, report the future end date 
•	If a loan is no longer in an interest-only period, report the most recent past end date