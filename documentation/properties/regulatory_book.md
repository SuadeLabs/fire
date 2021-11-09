---
layout:     property
title:      "regulatory_book"
schemas:    [account, collateral, derivative_cash_flow, derivative, loan, security]
---

# regulatory_book

---

The type of **regulatory_book** is defined in Article 104 of the [CRR][crr]

The **trading_book** and **banking_book** enum values have extended definitions provided by the [BCBS 457][bcbs].

### trading_book
The [BCBS 457][bcbs] paper goes in to more detail but here is an exerpt:
> 25.2 Instruments comprise financial instruments, foreign exchange (FX), and commodities. A financial
> instrument is any contract that gives rise to both a financial asset of one entity and a financial
> liability or equity instrument of another entity. Financial instruments include primary financial
> instruments (or cash instruments) and derivative financial instruments. A financial asset is any
> asset that is cash, the right to receive cash or another financial asset or a commodity, or an equity
> instrument. A financial liability is the contractual obligation to deliver cash or another financial
> asset or a commodity. Commodities also include non-tangible (ie non-physical) goods such as
> electric power.
>
> 25.3 Banks may only include a financial instrument, instruments on FX or commodity in the trading
> book when there is no legal impediment against selling or fully hedging it.
> 25.4 Banks must fair value daily any trading book instrument and recognise any valuation change in
> the profit and loss (P&L) account.

### banking_book
Essentially defined as everything that is not in the trading_book.


---
[crr]: http://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013R0575
[bcbs]: https://www.bis.org/bcbs/publ/d457.htm
