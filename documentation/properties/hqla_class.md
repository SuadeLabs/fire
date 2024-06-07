---

layout:     property
title:      "hqla_class"
schemas:    [security]

---

# hqla_class

---

The **hqla_class** of a security product is the classification of the security with regard to specified levels of high-quality liquid assets (HQLA) as defined in [Basel III regulation][breg] as part of The Liquidity Coverage Ratio (LCR) and liquidity risk monitoring tools key reforms:

> The objective of the LCR is to promote the short-term resilience of the liquidity risk profile of banks. It does this by ensuring that banks have an adequate stock of unencumbered high-quality liquid assets (HQLA) that can be converted easily and immediately in private markets into cash to meet their liquidity needs for a 30 calendar day liquidity stress scenario. The LCR will improve the banking sector’s ability to absorb shocks arising from financial and economic stress, whatever the source, thus reducing the risk of spillover from the financial sector to the real economy.

```bash
├── i
│   └── i_non_op
├── iia
│   └── iia_non_op
├── iib
│   └── iib_non_op
├── ineligible
│   └── ineligible_non_op
└── exclude
```

### i
Some examples of Level 1 Assets are:
- Coins and bank notes
- Qualifying marketable securities from sovereigns, central banks, public sector entities and multilateral development banks
- Qualifying central bank reserves
- Domestic sovereign or central bank debt for non-0% risk-weighted sovereigns

### i_non_op
Level 1 Assets that do not meet all operational requirements for a liquid asset, as defined in [LCR][lcr] Article 8.

### iia
Some examples of Level 2A Assets are:
- Sovereign, central bank, multilateral development banks, and public sector entity assets qualifying for 20% risk weighting
- Qualifying corporate debt securities rated AA- or higher
- Qualifying covered bonds rated AA- or higher

### iia_non_op
Level 2A Assets that do not meet all operational requirements for a liquid asset, as defined in [LCR][lcr] Article 8.

### iib
Some examples of Level 2B Assets are:
- Qualifying residential mortgage backed securities
- Qualifying corporate debt securities rated between A+ and BBB-
- Qualifying common equity shares

### iib_non_op
Level 2B Assets that do not meet all operational requirements for a liquid asset, as defined in [LCR][lcr] Article 8.

### ineligible
Assets that do not qualify for any of the HQLA classes set out in Chapter 2 of the LCR Regulation (or otherwise deemed ineligible by the firm or it's national supervisor) should be classified as **ineligible**.

### ineligible_non_op
Ineligible Assets that do not meet all operational requirements for a liquid asset, as defined in [LCR][lcr] Article 8.

### exclude
The exclude identifier is used to provide a manual override to exclude certain securities from an HQLA report for *credit enhancement or for operational reasons* according to [LCR][lcr] Article 8 and in particular:
> Assets used to provide credit enhancement in structured transactions or to cover operational costs of the credit institutions shall not be deemed as readily accessible to a credit institution.


---

[breg]: http://www.bis.org/publ/bcbs238.pdf
[lcr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0061
