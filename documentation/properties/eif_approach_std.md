---
layout:		property
title:		"eif_approach_std"
schemas:	[security]
---

# eif_approach_std

---

Describes which calculation approach the EIF will be used to derive EAD and risk weight:  LTA, MBA, FBA

REF:  OSFI BCAR Chapter 4, P146; 

## Security

```bash
├── lta
├── mba
├── fba

```
### lta
The "look-through approach" requires an institution to risk weight the underlying exposures of a fund as if the exposures were held directly by the institution. This is the most granular and risk-sensitive approach.

### mba
The "mandate-based approach" use the information contained in a fund's mandate or in the national regulations governing such investment funds

### fba
The "fall-back approach" would have the institution's equity investment in the fund is to be deducted from CET1 capital.
