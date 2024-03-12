---
layout:		property
title:		"cr_approach"
schemas:	[account, derivative, loan, security]
---
# cr_approach
Specifies the approved rwa calculation approach that is applied to the exposure for rwa calculations.  Specified for firms that are approved to have mixed calculation approaches
by the regulator.

---
### std
Standardized Approach
See [Basel CRE20-22](https://www.bis.org/basel_framework/chapter/CRE/20.htm)

### firb
Foundation Internal Model Approach
See [Basel CRE31 Foundation and advanced approaches](https://www.bis.org/basel_framework/chapter/CRE/30.htm?inforce=20230101&published=20200327#:~:text=and%20operational%20requirements.-,Foundation%20and%20advanced%20approaches,-30.32)

### airb
Advanced Internal Model Approach
See [Basel CRE31 Foundation and advanced approaches](https://www.bis.org/basel_framework/chapter/CRE/30.htm?inforce=20230101&published=20200327#:~:text=and%20operational%20requirements.-,Foundation%20and%20advanced%20approaches,-30.32)

### sec_sa
Securitisation Standardised Approach
See [Basel CRE41 Securitisation: Standardised Approach (SEC_SA)](https://www.bis.org/basel_framework/chapter/CRE/41.htm)

### sec_sa_lt
Securitisation Standardised Approach - Look-through Approach
For securitisation calculations, when the financial institution has full knowledge of the composition of the underlying exposures of pool at all time, the institution can apply the "look-through" approach to senior securitization exposures.
See [OSFI Chapter 7, P134 or Basel Framework, CRE 40.50][osfi-chapter-7]

### eif_lt
Equity Investments in Funds - Look-through Approach
The LTA requires a bank to risk weight the underlying exposures of a fund as if the exposures were held directly by the bank. This is the most granular and risk-sensitive approach. It must be used when:
(1) there is sufficient and frequent information provided to the bank regarding the underlying exposures of the fund; and
(2) such information is verified by an independent third party.
See [Basel CRE60 Equity Investments in Funds, CRE 60.2](https://www.bis.org/basel_framework/chapter/CRE/60.htm)

### eif_mba
Equity Investments in Funds - Mandate-based Approach
The second approach, the MBA, provides a method for calculating regulatory capital that can be used when the conditions for applying the LTA are not met.
Under the MBA banks may use the information contained in a fund's mandate or in the national regulations governing such investment funds.
See [Basel CRE60 Equity Investments in Funds, CRE 60.6](https://www.bis.org/basel_framework/chapter/CRE/60.htm)

### eif_fb
Equity Investmnets in Funds - Fall-back Approach
Where neither the LTA nor the MBA is feasible, banks are required to apply the FBA. The FBA applies a 1250% risk weight to the bank’s equity investment in the fund.
See [Basel CRE60 Equity investments in funds, CRE 60.8](https://www.bis.org/basel_framework/chapter/CRE/60.htm)

### sec_erba
Securitisation External-Ratings-Based Approach
See [Basel CRE42 Securitisation: External-Ratings-Based Approach (SEC_ERBA)](https://www.bis.org/basel_framework/chapter/CRE/42.htm)

---
[osfi-chapter-7]: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/capital-adequacy-requirements-car-2024-chapter-7-settlement-counterparty-risk
