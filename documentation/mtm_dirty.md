---
layout:		property
title:		"mtm_dirty"
schemas:	[security, derivative]
---

# mtm_dirty
The price of a [security/derivative] is the present value of its future cash-flows. To avoid the impact of the next coupon payment on the price of a [security/derivative], this cash flow is excluded from the price of the [security/derivative] and is called the accrued interest. In finance, the **dirty price** is the price of a [security/derivative] including any interest that has accrued since issue of the most recent coupon payment. This is to be compared with the clean price, which is the price of a [security/derivative] excluding the accrued interest.

> **Dirty Price = Clean Price + Accrued Interest**

(Source: https://en.wikipedia.org/wiki/Dirty_price)

Bank of England Handbook 20 - [Basic Bond Analysis][boe] (dirty/clean prices with regards to a bond product):

> When a bond is bought or sold midway through a coupon period, a certain amount of
coupon interest will have accrued. The coupon payment is always received by the
person holding the bond at the time of the coupon payment (as the bond will then be
registered in his name). Because he may not have held the bond throughout the
coupon period, he will need to pay the previous holder some ‘compensation’ for the
amount of interest which accrued during his ownership. In order to calculate the
accrued interest, we need to know the number of days in the accrued interest period,
the number of days in the coupon period, and the money amount of the coupon
payment. In most bond markets, accrued interest is calculated on the following
basis:-

> ((Coupon interest) x (no. of days that have passed in coupon period))/(total no of days in the coupon period)

> Prices in the market are usually quoted on a clean basis (i.e. without accrued) but
settled on a dirty basis (i.e. with accrued).

[boe]: http://www.bankofengland.co.uk/education/Documents/ccbs/handbooks/pdf/ccbshb20.pdf
