---
layout:		property
title:		"encumbrance_amount"
schemas:	[account, loan, collateral]
---

# encumbrance_amount

---

The **encumbrance_amount** is used in reference to products or entities where an encumbrance can be described as a claim, right to, interest in, or legal liability that diminishes its value. Encumbrances are typically used in reference to real property or assets to reflect liabilities where part or whole of the property or asset has been used as collateral, security or pledged by a borrower to a lender.

The *amount* here refers to the carrying amount or accounting value for the encumbrance. It is a positive integer number of cents. [See issue](https://github.com/suadelabs/fire/issues/12)

### EBA
Asset Encumbrance has become a regulatory requirement in its own right and in the EBA's 2013 [public hearing][eba-pres] they describe:
> an asset is considered encumbered if it has been pledged or if it is subject to any form of arrangement to secure, collateralise or credit enhance any transaction from which it cannot be freely withdrawn.

The 2015 [Report on Asset Encumbrance][eba-report] refers to asset encumbrance as: "balance sheet liabilities for which collateral was posted by institutions" and states that common sources of asset encumbrance come from repos, covered bonds and OTC derivatives.

*Repos* are tricky in this regard and under the standard [GMRA][gmra] definitions, legal title passes to the buyer (as a sale of the asset) with an agreement to repurchase at a later date. So technically, under this definition, there is no legal encumbrance on the *asset* but contractually on the cash or value arising from the sale of that asset.

### LCR
For Assests, the [LCR Regulation][lcr] has this to say about encumbrance:

> **LCR - Article 7.2**
> The assets shall be a property, right, entitlement or interest held by a credit institution and free from any encumbrance. For those purposes, an asset shall be deemed to be unencumbered where the credit institution is not subject to any legal, contractual, regulatory or other restriction preventing it from liquidating, selling, transferring, assigning or, generally, disposing of such asset via active outright sale or repurchase agreement within the following 30 calendar days. The following assets shall be deemed to be unencumbered:
>
>(a) assets included in a pool which are available for immediate use as collateral to obtain additional funding under committed but not yet funded credit lines available to the credit institution. This shall include assets placed by a credit institution with the central institution in a cooperative network or institutional protection scheme. Credit institutions shall assume that assets in the pool are encumbered in order of increasing liquidity on the basis of the liquidity classification set out in Chapter 2, starting with assets ineligible for the liquidity buffer;
>
>(b) assets that the credit institution has received as collateral for credit risk mitigation purposes in reverse repo or securities financing transactions and that the credit institution may dispose of.

Encumbrances are also sometimes used for account management purposes to denote future payments or commitments prior to expenditure to avoid overspending. In these cases, it should be checked that the commitment is a legal liability.

See also [**encumbrance_type**][encumbrance_type].

Further reading:
[BIS CGFS Paper No. 49][biscgfs49]

---

[eba-pres]: https://www.eba.europa.eu/implementing-technical-standard-supervisory-reporting-asset-encumbrance
[eba-report]:  https://www.eba.europa.eu/sites/default/files/document_library/Risk%20Analysis%20and%20Data/Risk%20Assessment%20Reports/2022/1036110/Report%20on%20Asset%20Encumbrance%202022.pdf
[gmra]: https://www.icmagroup.org/market-practice-and-regulatory-policy/repo-and-collateral-markets/icma-ercc-publications/frequently-asked-questions-on-repo/19-what-is-the-gmra/#:~:text=GMRA%20is%20the%20acronym%20for,and%20repo%20markets%20in%20Europe.global-master-repurchase-agreement-gmra/
[lcr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32015R0061
[encumbrance_type]: https://github.com/suadelabs/fire/blob/master/documentation/properties/encumbrance_type.md
[biscgfs49]: http://www.bis.org/publ/cgfs49.pdf
