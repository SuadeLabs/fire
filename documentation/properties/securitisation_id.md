---
layout:		property
title:		"securitisation_id"
schemas:	[security]
---

# securitisation_id


---
The **securitisation_id** is the internal (alpha-numerical) code used by the institution to identify a securitisation. It must be populated on the securitisation transaction record (`type` = securitisation or re_securitisation) and on every tranche record of that securitisation, so that tranches can be linked to their transaction.

The code should be that used for the legal registration of the securitisation transaction or, if not available, the name by which the securitisation transaction is known in the market, or within the institution in case of an internal or private securitisation. Where the International Securities Identification Number (ISIN) is available (i.e. for public transactions), the characters that are common to all tranches of the securitisation may be used.

The regulatory identifier defined in Article 11 of Commission Delegated Regulation (EU) 2020/1224 is reported separately in [securitisation_unique_id](./securitisation_unique_id.md).