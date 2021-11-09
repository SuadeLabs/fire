---
layout:     property
title:      "leg_type"
schemas:    [derivative]
---

# leg_type
Payoff type of a derivative leg, which may be a stand-alone trade (e.g. fra, cap), or part of an instrument refered to in the derivative_type attibute (eg. vanilla_swap). The atribute is an enum with the following members:

### fixed
the leg cash flows are fixed amounts

### floating
cashflows are floating interest amount linked to a rate index ((e.g. USD_LIBOR_BBA) populated in the underlying_index attribute; the notional amount is fixed (not indexed). Used only for the interest rate asset class.

### indexed
cashflows are linked to the performance/price variation of an underlying index (e.g inflation, equity index, security price, etc.) for transactions in all asset classes

### call
option leg in any asset class with variable amounts equal to max(underlying value - strike, 0)

### put
option leg in any asset class with variable amounts equal to max(strike - underlying value, 0)
