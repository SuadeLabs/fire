---
layout:		property
title:		"mtm_dirty"
schemas:	[security, derivative]
---

# mtm_dirty

---

The **dirty price** of a security/derivative is the price including any interest that has accrued since issue or the most recent coupon payment. This is to be compared to the clean price, which is the price of a security/derivative excluding the accrued interest.

> **Dirty Price = Clean Price + Accrued Interest**

The [Bank of England Handbook 20 - Basic Bond Analysis][boe] states:

> When a bond is bought or sold midway through a coupon period, a certain amount of coupon interest will have accrued. The coupon payment is always received by the person holding the bond at the time of the coupon payment (as the bond will then be registered in his name). Because he may not have held the bond throughout the coupon period, he will need to pay the previous holder some ‘compensation’ for the
amount of interest which accrued during his ownership. In order to calculate the accrued interest, we need to know the number of days in the accrued interest period, the number of days in the coupon period, and the money amount of the coupon payment. In most bond markets, accrued interest is calculated on the following basis:-

> ((Coupon interest) x (no. of days that have passed in coupon period))/(total no of days in the coupon period)

> Prices in the market are usually quoted on a clean basis (i.e. without accrued) but settled on a dirty basis (i.e. with accrued).

[boe]: http://www.bankofengland.co.uk/education/Documents/ccbs/handbooks/pdf/ccbshb20.pdf

See also [**mtm_clean**](https://github.com/suadelabs/fire/blob/master/documentation/properties/mtm_clean.md).

