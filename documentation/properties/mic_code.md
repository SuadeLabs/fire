---
layout:		property
title:		"mic_code"
schemas:	[security, derivative]
---

# mic_code

---

The [Market Identifier Code][mic] falls under [International Standards Organisation 10383][iso10383] and is used to identify entities such as exchanges, trading platforms, regulated or non-regulated markets and trade reporting facilities as sources of prices and related information. For the purpose of [MIFID II Transaction Reporting][rts] the MIC code will identify the venue where the transaction was executed. 

[MIFID II Transaction Reporting][rts] states that the [segment  MIC code][mic] (i.e the MIC that identifies the segment of one of the above entities) can be used for transactions executed on a trading venue, Systematic Internaliser (SI) (as defined in Article 4(1)(20) of [Directive 2014/65/EU;][mifid]) or organised trading platform outside of the Union. Where a segment MIC does not exist, an [operating MIC][mic] can be used. 

Under [MIFIR transaction reporting rules][rts], firms should use the MIC code XOFF for financial instruments admitted to trading, or traded on a trading venue or for which a request for admission was made, where the transaction on that financial instrument is not executed on a trading venue, SI or organised trading platform outside of the Union, or where an investment firm does not know it is trading with another investment firm acting as an SI.

Alternatively firms should use the MIC code XXXX for financial instruments that are not admitted to trading or traded on a trading venue or for which no request for admission has been made and that are not traded on an organised trading platform outside of the Union but where the underlying is admitted to trading or traded on a trading venue.

---

[iso10383]: https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.pdf 
[mic]: https://www.iso20022.org/market-identifier-codes
[rts]: https://eur-lex.europa.eu/legal-content/EN/TXT/?toc=OJ:L:2017:087:TOC&uri=uriserv:OJ.L_.2017.087.01.0449.01.ENG
[mifid]: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32014L0065
