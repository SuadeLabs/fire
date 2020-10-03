---
layout:     property
title:      "leg_type"
schemas:    [derivative]
---

# leg_type
Payoff type of a derivative leg, which may be a stand-alone trade (e.g. fra, cap), or part of an instrument refered to in the derivative_type attibute (eg. vanilla_swap). The atribute is an enum with the following members:
- fixed: a leg with fixed amounts
- floating: a leg in the interest rate asset class with variable interest amounts referencing an underlying_index (e.g. USD_LIBOR_BBA) and an optional underlying index tenor (e.g. "3m").
- indexed: a leg in the fx, credit, equity and commodity asset class, with variable amounts which depend on the performance on an underlying security, issuer or index
- call: option leg in any asset class with variable amounts equal to max(underlying value - strike, 0)
- put: option leg in any asset class with variable amounts equal to max(strike - underlying value, 0)