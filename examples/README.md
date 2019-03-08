---
layout: readme
title: FIRE data examples
---

## Individual element examples
# Account examples
* [current_account](current_account.json)
* [current_account_with_guarantee](current_account_with_guarantee.json)
* [savings_account](savings_account.json)
* [savings_account_with_notice](savings_account_with_notice.json)
* [time_deposit_1year](time_deposit_1year.json)
* [time_deposit_1year_with_6_month_withdrawal_option](time_deposit_1year_with_6_month_withdrawal_option.json)

# Agreement examples
* [master_netting_agreement_with_csa](master_netting_agreement_with_csa.json)
* [master_netting_agreement_without_csa](master_netting_agreement_without_csa.json)

# Derivative examples
* [derivative_with_initial_margin](derivative_with_initial_margin.json)

# Security examples
* [variation_margin_cash_posted](variation_margin_cash_posted.json)
* [variation_margin_cash_received](variation_margin_cash_received.json)
* [variation_margin_bond_posted](variation_margin_bond_posted.json)
* [variation_margin_bond_received](variation_margin_bond_received.json)

## Test case examples
# Derivatives with Variation Margin (VM)
* [Gross receivables with VM received](derivative_receivables_with_vm_received.json)

> 2 Derivatives: one is receivable at 200 GBP and the other payable at 100 GBP so the overall gross position is +100 GBP.

> 1 Security: 50 GBP cash collateral received as variation margin.

> Note the derivatives and the security are linked through the mna_id which matches the agreement id.

* [Gross payables with VM posted/given](derivative_payables_with_vm_posted.json)

> 2 Derivatives: one is payable at 200 GBP and the other receivable at 100 GBP so the overall gross position is -100 GBP.

> 1 Security: 50 GBP cash collateral posted as variation margin.

> Note the derivatives and the security are linked through the mna_id which matches the agreement id.

# Derivatives with Initial Margin (IM)
* [Derivatives facing credit institution](derivative_with_im_facing_ci.json)

> Note IM is directly populated on the derivative schema.

* [Derivatives facing central clearing party (CCP)](derivative_with_im_facing_ccp.json)

> Note IM is directly populated on the derivative schema.

# Non-margined derivatives
* [in-the-money derivatives](derivative_unmargined_itm.json)

> 2 Derivatives with positive mtm.
> Note the MNA does not have the "credit_support_type" property.

* [out-of-the-money derivatives](derivative_unmargined_otm.json)

> 2 Derivatives with negative mtm.
> Note the MNA does not have the "credit_support_type" property.

# Non-derivatives IM posted to a CCP (e.g. RepoClear)
* [collateral posted to ccp on non-derivatives](security_collateral_posted_ccp_non_deriv.json)

> Security has "purpose" = "collateral" which signals it is not linked to derivative transactions.
