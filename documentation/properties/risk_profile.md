---
layout:		property
title:		"risk_profile"
schemas:	[customer]
---

# risk_profile

---

The **risk_profile** also know as investor profile defines a numerical scale to represent the customer's willingness and/or capacity to take on financial risk.

As described in this [Article from the CFA Institute][cfa_institute]:

> Current regulations reflect the complexity surrounding risk profiling, with many generally vague as to what factors influence a risk profile. Current regulatory guidance also differs among countries

Note the differences in the definitions of investment profiles in Article 25 (2) of [MIFID II][mifid_ii], and [US FINRA Rule 2111][us_finra_2011].

The scale is based on an internal assessment made by the reporting intitution. It is presented in ascendant order from 1 to 10. However, the reporting instituion does not need to define 10 different risk profiles. This means:

If the reporting instituion has defined 5 different profiles for their investors, a **risk_profile** of 1 will represent the most conservative investors, while a **risk_profile** of 5 will represent the most risky ones.

---
[cfa_institute]: https://www.cfainstitute.org/-/media/documents/article/rf-brief/rfbr-v1-n1-1-pdf.ashx
[mifid_ii]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32014L0065
[us_finra_2011]: https://www.finra.org/rules-guidance/rulebooks/finra-rules/2111
