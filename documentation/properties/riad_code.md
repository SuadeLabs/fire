---
layout:		property
title:		"riad_code"
schemas:	[customer, issuer, guarantor]
---

# riad_code

---

RIAD code is the unique counterparty identifier for all counterparties when reported from the NCBs to the ECB; 

## Structure

Every entity in RIAD needs to be identified with a unique RIAD Code. The first two digits of this RIAD
code represent the two digit ISO country code, i.e. the host. The second part of the RIAD Code is a freely
chosen string code that is owned by the national hub. 

For more information please see [BIS publication on RIAD:][riadbis]

[riadbis]: https://www.bis.org/ifc/publ/ifcb43_zi.pdf