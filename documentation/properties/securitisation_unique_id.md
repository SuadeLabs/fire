---
layout:		property
title:		"securitisation_unique_id"
schemas:	[security]
---

# securitisation_unique_id

---
The **securitisation_unique_id** is the regulatory unique identifier of a securitisation, as defined in [Article 11 of Commission Delegated Regulation (EU) 2020/1224](https://eur-lex.europa.eu/eli/reg_del/2020/1224/oj/eng). It is populated on the securitisation transaction record (`type` = securitisation or re_securitisation) and is not expected on the tranche records.

It is composed of the following elements, in this order, with no separators (27 characters):

1. the Legal Entity Identifier (20 characters) of the reporting entity designated under Article 7(2) of Regulation (EU) 2017/2402, which is usually the originator, sponsor or SSPE and not necessarily the institution submitting the data;
2. the letter `A` for an ABCP securitisation or `N` for a non-ABCP securitisation;
3. the four-digit year in which the first securities of the securitisation (or, for ABCP, of the ABCP programme) were issued;
4. `01`, or where several securitisations share elements 1 to 3, a two-digit sequential number in the order in which information about each was made available.

The identifier cannot be amended by the reporting entity once assigned. It is reported by originators, sponsors and investors alike, for example in column 0015 of COREP templates C 14.00 and C 14.01.

Example: `ABCDEF1234567890XY12N202401`.

This attribute differs from [securitisation_id](securitisation_id.md), which is the institution's internal code linking the transaction to its tranches.