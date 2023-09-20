---
layout:     property
title:      "capital_tier"
schemas:    [account, security]
---

# capital_tier

```bash
├── tier_1
├── ce_tier_1
├── add_tier_1
├── cet1_grandfathered
├── at1_grandfathered
├── tier_2
├── anc_tier_2
├── bas_tier_2
├── t2_grandfathered
├── tier_3
├── anc_tier_3
└── bas_tier_3
```

Capital tier of an instrument in accordance with CRR2 regulation
(REGULATION (EU) No 575/2013 AS AMENDED BY REGULATION (EU) 2019/876 (CRR2) ).

Note that this includes 'grandfathered capital' which is capital which would
have been classified in capital tiers under Basel 2 regulations, rules but are
no longer eligible due to the tighter rules under Basel3 currently
reflected in CRR and CRR2 (and  hence they are ‘grandfathered’ and dealt
with in a special way by transitional arrangements during  a transitional
period).

The fields here are listed in a flat structure as they are mutually exclusive.

### tier_1
Securities classed as tier 1 capital instruments, these include securities
classed as common equity tier 1 and securities classed as additional tier 1
capital instruments.

### ce_tier_1
Securities classed as common equity tier 1 (CET1) capital instruments.
As set out in CRR Article 26, these are  capital instruments,
provided that the conditions laid down in CRR Article 28 or, where applicable,
Article 29 are met.

### add_tier_1
Securities classed as additional tier 1 capital instruments.
As set out in CRR Article 51, these are capital instruments, where the
conditions laid down in Article 52(1) are met.

### tier_2
Securities classed as Tier 2 capital instruments.
As set out in CRR Article 62 these are capital instruments where the
conditions laid down in Article 63 are met.

### anc_tier_2
*Needs definition*

### bas_tier_2
*Needs definition*

### cet1_grandfathered
Instruments which are considered as grandfathered
as CET1 Capital, in that they no longer meet the tighter restrictions
introduced  in the CRR\CRR2 regulation for CET1 capital, but are still included
in transitional arrangements.

According to CRR2 Regulation Article 484(3) this is capital within the meaning
of Article 22 of Directive 86/635/EEC, that qualified as original own funds
under the national transposition measures for point (a) of Article 57 of
Directive 2006/48/EC notwithstanding that the conditions laid down in
Article 28 or, where applicable, Article 29 of the CRR Regulation are not met.

### at1_grandfathered
Instruments which are considered as grandfathered
as additional tier 1 capital, in that they no longer meet the tighter
restrictions introduced  in the CRR\CRR2 regulation for additional tier 1
capital, but are still included in transitional arrangements.

According to CRR2 Regulation Article 484(4) this is instruments that qualified
as original own funds under national transposition measures for point (ca)
of Article 57 and Article 154(8) and (9) of Directive 2006/48/EC
notwithstanding that the conditions laid down in Article 52 of this Regulation
are not met.

### t2_grandfathered
Instruments which are considered as grandfathered
as tier 2 capital, in that they no longer meet the tighter
restrictions introduced  in the CRR\CRR2 regulation for tier 2
capital, but are still included in transitional arrangements.

According to CRR2 Regulation Article 484(5) this is instruments that qualified
under national transposition measures for points (e), (f), (g) or (h) of
Article 57 of Directive 2006/48/EC shall qualify as Tier 2 items,
notwithstanding that those items are not included in Article 62 of this
Regulation or that the conditions laid down in Article 63 of this
Regulation are not met.

### tier_3
*Needs definition*


### anc_tier_3
*Needs definition*

### bas_tier_3
*Needs definition*
