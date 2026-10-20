---
layout:     property
title:      "capital_tier"
schemas:    [account, security]
---

# capital_tier

```bash
├── tier_1
├── ce_tier_1
├── ce_tier_1_ineligible
├── add_tier_1
│   └── add_tier_1_indirect
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

Capital tier of an instrument under the applicable regulatory framework. For banks,
[Basel Framework CAP10.1–10.3][basel-capital] distinguishes Common Equity Tier 1
(CET1), Additional Tier 1 (AT1) and Tier 2 capital. In the EU, the corresponding
rules are in [Regulation (EU) No 575/2013 (CRR), Part Two][crr-own-funds], as amended.

The property also supports insurance own-fund classifications and historical
banking classifications. **Basic** and **ancillary** own funds are distinctions
under [Solvency II, Articles 88–94][solvency-own-funds]; CRR does not subdivide bank
Tier 2 capital into these categories. Banking Tier 3 is a historical category,
as explained below. Classify the instrument under the relevant framework rather
than treating similarly named banking and insurance tiers as interchangeable.

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
capital instruments. See [CRR Article 25][crr-tier-1] and
[Basel Framework CAP10.1–10.3][basel-capital].

### ce_tier_1
Securities classed as common equity tier 1 (CET1) capital instruments.
As set out in [CRR Article 26][crr-cet1-items], these are  capital instruments,
provided that the conditions laid down in [CRR Article 28][crr-cet1-instruments] or, where applicable,
[Article 29][crr-mutual-cet1] are met.

### ce_tier_1_ineligible
Capital instruments which do not meet the condition in points (b), (l) and (m) of [CRR Article 28(1)][crr-cet1-instruments]. Conditions in those points reflect different situations of the capital which are reversible, and thus the amount reported here can be eligible in subsequent periods.

### add_tier_1
Securities classed as additional tier 1 capital instruments.
As set out in [CRR Article 51][crr-at1-items], these are capital instruments, where the
conditions laid down in [Article 52(1)][crr-at1-instruments] are met.

### add_tier_1_indirect
Indirect holdings of securities classed as additional tier 1 capital instruments where the condition set out in point (b)(ii) of [CRR Article 52(1)][crr-at1-instruments] is met.

### tier_2
Securities classed as Tier 2 capital instruments.
For banks, [CRR Article 62][crr-tier2-items] identifies Tier 2 items, including
capital instruments and subordinated loans meeting [Article 63][crr-tier2-instruments].
See also [Basel Framework CAP10, “Tier 2 capital”][basel-tier2].

### anc_tier_2
Ancillary own funds classified as Tier 2 under Solvency II. These are callable loss-absorbing items, such as eligible uncalled capital or guarantees, meeting the Tier 2 criteria. See [Directive 2009/138/EC, Articles 89 and 94(2)][solvency-own-funds] and [EIOPA’s Article 94 text][solvency-classification].

### bas_tier_2
Basic own funds classified as Tier 2 under Solvency II, meeting the applicable subordination and other classification criteria. Basic own funds comprise the excess of assets over liabilities, subject to adjustments, and subordinated liabilities. See [Directive 2009/138/EC, Articles 88 and 94(2)][solvency-own-funds].

### cet1_grandfathered
Instruments which are considered as grandfathered
as CET1 Capital, in that they no longer meet the tighter restrictions
introduced  in the CRR\CRR2 regulation for CET1 capital, but are still included
in transitional arrangements.

Under the historical transitional provisions of [CRR Article 484(3)][crr-grandfathering] this is capital within the meaning
of Article 22 of Directive 86/635/EEC, that qualified as original own funds
under the national transposition measures for point (a) of Article 57 of
Directive 2006/48/EC notwithstanding that the conditions laid down in
Article 28 or, where applicable, Article 29 of the CRR Regulation are not met.

### at1_grandfathered
Instruments which are considered as grandfathered
as additional tier 1 capital, in that they no longer meet the tighter
restrictions introduced  in the CRR\CRR2 regulation for additional tier 1
capital, but are still included in transitional arrangements.

Under the historical transitional provisions of [CRR Article 484(4)][crr-grandfathering] this is instruments that qualified
as original own funds under national transposition measures for point (ca)
of Article 57 and Article 154(8) and (9) of Directive 2006/48/EC
notwithstanding that the conditions laid down in Article 52 of this Regulation
are not met.

### t2_grandfathered
Instruments which are considered as grandfathered
as tier 2 capital, in that they no longer meet the tighter
restrictions introduced  in the CRR\CRR2 regulation for tier 2
capital, but are still included in transitional arrangements.

Under the historical transitional provisions of [CRR Article 484(5)][crr-grandfathering] this is instruments that qualified
under national transposition measures for points (e), (f), (g) or (h) of
Article 57 of Directive 2006/48/EC shall qualify as Tier 2 items,
notwithstanding that those items are not included in Article 62 of this
Regulation or that the conditions laid down in Article 63 of this
Regulation are not met.

### tier_3
Capital classified as Tier 3 under the applicable framework:

- **Historical banking framework:** short-term subordinated debt permitted, at national supervisory discretion and subject to limits, to meet part of the capital requirement for market risk. See [Basel II, paragraphs 49(xiii)–49(xiv)][basel2-tier3]. Banking Tier 3 was abolished by [Basel III, introductory paragraph 9][basel3-tier3]; it is not a current Basel III/CRR own-funds category.
- **Solvency II:** basic or ancillary own-fund items that do not qualify for Tier 1 or Tier 2. See [Directive 2009/138/EC, Article 94(3)][solvency-own-funds].


### anc_tier_3
Ancillary own funds classified as Tier 3 under Solvency II because they do not meet the Tier 2 criteria. See [Directive 2009/138/EC, Articles 89 and 94(3)][solvency-own-funds].

### bas_tier_3
Basic own funds classified as Tier 3 under Solvency II because they do not meet the Tier 1 or Tier 2 criteria. See [Directive 2009/138/EC, Articles 88 and 94(3)][solvency-own-funds].

[solvency-own-funds]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32009L0138#:~:text=Classification%20into%20tiers
[solvency-classification]: https://www.eiopa.europa.eu/rulebook/solvency-ii-single-rulebook/article-2182_en

[basel-capital]: https://www.bis.org/committees/bcbs/basel-framework/standard/cap?allChapters=true#:~:text=10.1
[basel-tier2]: https://www.bis.org/committees/bcbs/basel-framework/standard/cap?allChapters=true#:~:text=Tier%202%20capital
[basel2-tier3]: https://www.bis.org/publications/200606-standards-basel-ii-international-convergence-capital-measurement-and-capital-standards-revised-framework.pdf
[basel3-tier3]: https://www.bis.org/publ/bcbs189.pdf
[crr-own-funds]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0575#:~:text=Own%20funds
[crr-tier-1]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0575#:~:text=Article%2025
[crr-cet1-items]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0575#:~:text=Article%2026
[crr-cet1-instruments]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0575#:~:text=Article%2028
[crr-mutual-cet1]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0575#:~:text=Article%2029
[crr-at1-items]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0575#:~:text=Article%2051
[crr-at1-instruments]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0575#:~:text=Article%2052
[crr-tier2-items]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0575#:~:text=Article%2062
[crr-tier2-instruments]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0575#:~:text=Article%2063
[crr-grandfathering]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0575#:~:text=Article%20484
