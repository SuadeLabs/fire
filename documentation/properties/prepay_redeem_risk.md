---
layout:     property
title:      "prepay_redeem_risk "
schemas:    [account, loan, security]
---

# prepay_redeem_risk 

---

The **prepay_redeem_risk** property represents two estimates that could either be used for assets or liabillities. It covers both asset-side prepayments (via CPR) and liability-side early redemptions (via ERR)

A conditional prepayment rate (CPR) is an estimate of the percentage of a loan pool’s principal that is likely to be paid off prematurely. CPR is expressed as an annual percentage rate. 

Early redemption risk (ERR) is the risk that depositors withdraw funds before contractual maturity, altering a bank's expected cash flows and interest rate exposure

This attribute is represented as a percentage, and should be recorded as a decimal/float such that 1.5% is 0.015.

---

ref: https://www.bis.org/publications/interest-rate-risk-banking-book-additional-pillar-2-guidance_0.pdf