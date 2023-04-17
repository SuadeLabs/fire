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
See [OSFI Chapter 7, P134 or Basel Framework, CRE 40.50](https://www.osfi-bsif.gc.ca/Eng/fi-if/rg-ro/gdn-ort/gl-ld/Pages/CAR22_chpt6.aspx#ToC6.6.5)

### sec_erba
Securitisation External-Ratings-Based Approach
See [Basel CRE42 Securitisation: External-Ratings-Based Approach (SEC_ERBA)](https://www.bis.org/basel_framework/chapter/CRE/42.htm)
