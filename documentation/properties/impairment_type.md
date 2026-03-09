---
layout:		property
title:		"impairment_type"
schemas:	[account, loan, security]
---

# impairment_type

---

Under [IAS 39][ias], a financial asset or group of assets is impaired, and impairment losses are recognised, only if there is objective evidence as a result of one or more events that occurred after the initial recognition of the asset. An entity is required to assess at each balance sheet date whether there is any objective evidence of impairment. If any such evidence exists, the entity is required to do a detailed impairment calculation to determine whether an impairment loss should be recognised. The amount of the loss is measured as the difference between the asset's carrying amount and the present value of estimated cash flows discounted at the financial asset's original effective interest rate.

Assets that are individually assessed and for which no impairment exists are grouped with financial assets with similar credit risk statistics and collectively assessed for impairment.

If, in a subsequent period, the amount of the impairment loss relating to a financial asset carried at amortised cost or a debt instrument carried as available-for-sale decreases due to an event occurring after the impairment was originally recognised, the previously recognised impairment loss is reversed through profit or loss. Impairments relating to investments in available-for-sale equity instruments are not reversed through profit or loss.

Assets that can be impaired include land, buildings, machinery and equipment, loan portfolio, investment property, goodwill, intangible assets, investments in subsidiaries, associates and joint ventures

With regards to loans, there are three categories they can fall into:

```bash
├── collective
│   ├── collective_formal
│   └── collective_internal
├── individual
│   ├── individual_formal
│   └── individual_internal
└── write_off
```

### collective
To be used if the instrument is subject to impairment in accordance with an applied accounting standard and is collectively assessed for impairment by being grouped together with instruments with similar credit risk characteristics.

### individual
To be used if the instrument is subject to impairment in accordance with an applied accounting standard and is individually assessed for impairment.


The suffix of both collective and invidudual into either formal or internal relates to whether the debt has been formally reduced/removed or not as below (Please see [Appendix 1 of Resident office returns under CBI][ror]):

### collective_formal
To be used if the instrument is subject to impairment in accordance with an applied accounting standard and is collectively assessed for impairment by being grouped together with instruments with similar credit risk characteristics.
This represents formal debt forgiveness where the borrower legal obligation is reduced/removed

### collective_internal
To be used if the instrument is subject to impairment in accordance with an applied accounting standard and is collectively assessed for impairment by being grouped together with instruments with similar credit risk characteristics.
Internal accounting write-off or provisioning decision without extinguishing legal repayment obligation.

### individual_formal
To be used if the instrument is subject to impairment in accordance with an applied accounting standard and is individually assessed for impairment.
This represents formal debt forgiveness where the borrower legal obligation is reduced/removed

### individual_internal
To be used if the instrument is subject to impairment in accordance with an applied accounting standard and is individually assessed for impairment.
Internal accounting write-off or provisioning decision without extinguishing legal repayment obligation.

### write_off
Write-offs relate to amounts where the lender has no expectation of ever being able to recover value from the collateral or otherwise. It can relate to a financial asset in its entirety or to a portion of it. For example, an entity plans to enforce the collateral on a financial asset and expects to recover no more than 30 per cent of the financial asset from the collateral. If the entity has no reasonable prospects of recovering any further cash flows from the financial asset, it should write off the remaining 70 per cent of the financial asset.


[ias]: https://www.iasplus.com/en/standards/ias/ias39
[ror]: https://www.centralbank.ie/docs/default-source/statistics/statistical-reporting-requirements/credit-institutions/rs2-rv2-and-rc2/notes-on-compilation-2022-(rs3-rv3-rc3)_v.1.2_final.pdf?sfvrsn=ea83991d_8
