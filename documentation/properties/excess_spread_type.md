---
layout:     property
title:      "excess_spread_type"
schemas:    [security]
---

# excess_spread_type

---

Excess spread or *Synthetic Excess Spread* is defined in the [Securitisation Regulations Article 2 (29)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02017R2402-20210409#:~:text=%E2%80%98synthetic%20excess%20spread%E2%80%99%20means%20the%20amount%20that%2C%20according%20to%20the%20documentation%20of%20a%20synthetic%20securitisation%2C%20is%20contractually%20designated%20by%20the%20originator%20to%20absorb%20losses%20of%20the%20securitised%20exposures%20that%20might%20occur%20before%20the%20maturity%20date%20of%20the%20transaction%3B):

> ‘synthetic excess spread’ means the amount that, according to the documentation of a synthetic securitisation, is contractually designated by the originator to absorb losses of the securitised exposures that might occur before the maturity date of the transaction;


### fixed
> Fixed excess spread: the amount of excess spread that the originator commits to use as credit enhancement at each payment period is pre-determined in the contract, usually expressed as a fixed percentage of the total outstanding portfolio balance, e.g. 30 basis points of the outstanding portfolio balance. The excess spread is, under this scenario, a contractually committed credit enhancement buffer, within which losses will be absorbed before impacting any more senior position, and is therefore due to the lack of calculation of any excess amount no excess spread in the strict sense of the term;

From the [EBA draft RTS on determining the exposure of synthetic excess spread][draft-rts]:
> Use-It-Or-Lose-It (UIOLI) mechanisms. UIOLI mechanisms imply that the amount designated to absorb losses is periodically offset with the amount of losses realised at each period, and that the amount that is not used for loss absorption in a particular period is no longer available for loss compensation in future periods. Because of the lower loss absorbing capacity of UIOLI mechanisms in comparison with trapped mechanisms, and the circumstance that this lower loss absorbing capacity also depends on the distribution of the losses throughout the life of the transaction 3 , these RTS specify an adjustment to the calculation applicable to trapped mechanisms in case of the application of the simplified model approach. This adjustment is not needed in the case of the full model approach because it already accounts for the lower loss absorbing capacity of UIOLI SES within the differentiated modelling of periodical cash flows and loss amounts for all periods throughout the maturity of a transaction.

> Use-it-or-lose-it mechanism: during each payment period, excess spread may be used to cover credit losses materialising during that period. Excess spread not used for that purpose during the payment period is returned to the originator;

From the [Securitisation Regulation Article 26e](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02017R2402-20210409#:~:text=The%20originator%20may%20commit,returned%20to%20the%20originator%3B)

> The originator may commit synthetic excess spread, which shall be available as credit enhancement for the investors, where all of the following conditions are met:
> (a) the amount of the synthetic excess spread that the originator commits to using as credit enhancement at each payment period is specified in the transaction documentation and expressed as a fixed percentage of the total outstanding portfolio balance at the start of the relevant payment period (fixed synthetic excess spread);
> (b) the synthetic excess spread which is not used to cover credit losses that materialise during each payment period shall be returned to the originator;

### fixed_trapped
Similar to **fixed** above, but without condition (b) as defined in the [EBA draft RTS on determining the exposure of synthetic excess spread][draft-rts]:

> Trapped mechanisms. In trapped mechanisms, the amount designated by the originator institution to absorb losses is periodically offset with the amount of losses realised at each period; the amount not used for loss absorption in that period cumulates in a separate account and is still available for loss absorption in future periods. Because of that, these draft RTS specify that its exposure value should be the total losses expected to be covered during the entire life of the transaction. To calculate those losses two methodologies would be possible: a full model approach, similar to the approach recommended in the EBA Report on SRT for the SRT assessment2 , or a simplified model approach, which would only model the remaining weighted average life (WAL) of the underlying portfolio and would multiply it by the SES designated for the next period.

From the [Discussion Paper on Significant Risk Transfers for Securitisations][discussion-paper]

> Trap mechanism: during each payment period, excess spread not consumed to cover losses materialising during that period is set aside to create a ledger (spread account) that cumulates over time and remains available to absorb losses when these materialise. Spread may cumulate in a ledger for the entire life of the transaction, it may alternatively start cumulating as a given performance trigger is activated, from the date of a call option or may be cumulated to reach different target levels depending on agreed triggers

### variable
Slightly more complex than the fixed approach, variable excess spread is determined by a formula or other dynamic method.
From the [EBA draft RTS on determining the exposure of synthetic excess spread][draft-rts]:
> based on the expected income of the securitised exposures or on the outstanding amount of those securitised exposures, or on another reference related to the securitised exposures, as the amounts that originator institutions estimate to be available for the absorption of losses in the respective future period for which the synthetic excess spread amount is being determined

From the [Discussion Paper on Significant Risk Transfers for Securitisations][discussion-paper]
> Variable excess spread: mostly to replicate the functioning of a traditional securitisation transaction, excess spread is defined in a contract by means of formulae, resulting in a variable amount of excess spread at each payment period. Such formulae can be defined as the portfolio income that, at each payment period, exceeds the costs of the securitisation transaction, among others including the cost of credit protection, the spread paid on the senior tranche, or an equivalent funding cost whenever the senior tranche is retained by the originator, servicing costs and all other relevant costs

### variable_trapped
See *variable* and *trapped* as referenced above.

### none
No excess spread mechanism built in to the securitisation.


---
[draft-rts]: https://www.eba.europa.eu/sites/default/files/document_library/Publications/Consultations/2022/Consultation%20on%20draft%20RTS%20on%20the%20determination%20by%20originator%20institutions%20of%20the%20exposure%20value%20of%20SES%20in%20securitisations/1037741/CP%20on%20draft%20RTS%20on%20calculation%20of%20exposure%20value%20of%20SES.pdf

[discussion-paper]: https://www.eba.europa.eu/sites/default/files/documents/10180/1963391/228098e3-29ba-473f-9e4c-680ce32e1869/Discussion%20Paper%20on%20the%20Significant%20Risk%20Transfer%20in%20Securitisation%20%28EBA-DP-2017-03%29.pdf
