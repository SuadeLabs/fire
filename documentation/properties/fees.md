---
layout:		property
title:		"fees"
schemas:	[loan]
---

# fees

**fees** represents the associated amounts due surrounding a loan that need to be considered, for example when calculating current LTV.

This is a *monetary type* and as [it is impossible to squeeze infinitely many Real numbers into a finite number of bits][floats], we represent monetary types as integer numbers of cents/pence to reduce potential rounding errors. So $10.35 becomes 1035.
Don't forget to divide by 100 (or the relevant minor unit denomination) when presenting information to a user. The relevant minor unit denomination should be determined from the currency's corresponding ['E'][E] value.

References: [Rolling-up of fees, FCA Handbook][fca-fees]

---

[fca-fees]:  https://www.handbook.fca.org.uk/handbook/MCOB/4/6A.html
