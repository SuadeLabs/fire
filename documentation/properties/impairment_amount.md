---
layout:		property  
title:		"impairment_amount"  
schemas:	[loan]  
---

# impairment_amount

---

Impairment refers to the amount of loss allowances that are held against or are allocated to the instrument on the reporting reference date. This data attribute applies to instruments subject to impairment under the applied accounting standard. Under IFRS, the accumulated impairment relates to the following amounts:

1. loss allowance at an amount equal to 12-month expected credit losses;
2. loss allowance at an amount equal to lifetime expected credit losses.

Under GAAP, the accumulated impairment relates to the following
amounts:

1.  loss allowance at an amount equal to general allowances;
2.  loss allowance at an amount equal to specific allowances.

From IAS 39 — [Impairment][impairdef]:

> A financial asset or group of assets is impaired, and impairment losses are recognised, only if there is objective evidence as a result of one or more events that occurred after the initial recognition of the asset. An entity is required to assess at each balance sheet date whether there is any objective evidence of impairment. If any such evidence exists, the entity is required to do a detailed impairment calculation to determine whether an impairment loss should be recognised. The amount of the loss is measured as the difference between the asset's carrying amount and the present value of estimated cash flows discounted at the financial asset's original effective interest rate.
> Assets that are individually assessed and for which no impairment exists are grouped with financial assets with similar credit risk statistics and collectively assessed for impairment.
> If, in a subsequent period, the amount of the impairment loss relating to a financial asset carried at amortised cost or a debt instrument carried as available-for-sale decreases due to an event occurring after the impairment was originally recognised, the previously recognised impairment loss is reversed through profit or loss. Impairments relating to investments in available-for-sale equity instruments are not reversed through profit or loss.

[impairdef]: http://www.iasplus.com/en/standards/ias/ias39 

For example, a loan is considered to be impaired when it is probable that not all of the related principal and interest payments will be collected. The **impairment_amount** for a loan is the allowance for loan impairments set aside by the firm that accounts for the event that the loan becomes impaired in the future.

An [impairment allowance][amountdef] can be based on the examination of individual receivables, or groups of similar types of receivables. The creditor can use any impairment measurement method that is practical for the creditor’s circumstances. When loans are aggregated for analysis purposes, you can use historical statistics to derive the estimated amount of impairment. The amount of impairment to recognize should be based on the present value of expected future cash flows, though a loan’s market price or the fair value of the related collateral can also be used. It is possible that there is no need to establish a reserve for an impaired loan if the value of the related collateral is at least as much as the recorded value of the loan.

[amountdef]: http://www.accountingtools.com/questions-and-answers/loan-impairment-accounting.html


