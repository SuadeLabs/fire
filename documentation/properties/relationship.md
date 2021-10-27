---
layout:		property
title:		"relationship"
schemas:	[entity]
---

# relationship

---
The **relationship** is used to describe the link betweek two entities. There are two categories:
- The relationship between an entity (customer, issuer or guarantor) and it's ultimate parent. 
- The relationship between an entity (customer, issuer or guarantor) and the reporting_entity.

An entity can be a **parent_branch** or a **parent_subsidiary** of its ultimate parent.

If the entity and the reporting_entity are directly linked, the former can be a **branch**, **subsidiary**, **parent** or **head_office** of the latter.

If the entity and the reporting_entity are not directly linked, the former can be a **parent_subsidiary** or **parent_branch**.

### parent
Any undertaking which is not itself a subsidiary of another undertaking and/or effectively exercises a dominant influence over another undertaking. See first paragraph of subsidiary definition.


### head_office
It is a subcategory of parent that has control over one or many branch offices


### subsidiary
Controlling interests in other entities. More specifically, from Article 1(1) of the [Directive on Consolidated Accounts][dir-83-349]:

>1. A Member State shall require any undertaking governed by its national law to draw up consolidated accounts and a consolidated annual report if that undertaking (a parent undertaking):
(a) has a majority of the shareholders' or members' voting rights in another undertaking (a subsidiary undertaking); or
(b) has the right to appoint or remove a majority of the members of the administrative, management or supervisory body of another undertaking (a subsidiary undertaking) and is at the same time a shareholder in or member of that undertaking; or
(c) has the right to exercise a dominant influence over an undertaking (a subsidiary undertaking) of which it is a shareholder or member, pursuant to a contract entered into with that undertaking or to a provision in its memorandum or articles of association, where the law governing that subsidiary undertaking permits its being subject to such contracts or provisions. A Member State need not prescribe that a parent undertaking must be a shareholder in or member of its subsidiary undertaking. Those Member States the laws of which do not provide for such contracts or clauses shall not be required to apply this provision; or
(d) is a shareholder in or member of an undertaking, and:
(aa) a majority of the members of the administrative, management or supervisory bodies of that undertaking (a subsidiary undertaking) who have held office during the financial year, during the preceding financial year and up to the time when the consolidated accounts are drawn up, have been appointed solely as a result of the exercise of its voting rights; or
(bb) controls alone, pursuant to an agreement with other shareholders in or members of that undertaking (a subsidiary undertaking), a majority of shareholders' or members' voting rights in that undertaking. The Member States may introduce more detailed provisions concerning the form and contents of such agreements.
The Member States shall prescribe at least the arrangements referred to in (bb) above.
They may make the application of (aa) above dependent upon the holding's representing 20 % or more of the shareholders' or members' voting rights.
However, (aa) above shall not apply where another undertaking has the rights referred to in subparagraphs (a), (b) or (c) above with regard to that subsidiary undertaking.

### jv
Indicates subsidiaries or holdings where ownership is less than 50% or non-controlling.


### participation
[**DNB Reporting Manual**](https://www.dnb.nl/media/cvceu2pl/manual-monetary-reporting_tcm47-379376.pdf)
A holding is classified as participation equity if the reporting institution (the domestic banking business) holds an interest in the capital of a corporation (either domestic or foreign) that provides it with 10% or more of the voting rights.

This is in line with the criteria on influence and control described in BPM6 (Balance of Payments and International Investment Position Manual, edition 6).


### branch
From the [Capital Requirements Regulation][crr]:
> 'branch' means a place of business which forms a legally dependent part of an institution and which carries out directly all or some of the transactions inherent in the business of institutions;

IFRS does not explicitly define a branch, but in practise it has been noted as an extension to the parent company. 

From the IAS 21 definition of a foreign operation:
> Foreign operation is an entity that is a subsidiary, associate, joint
arrangement or branch of a reporting entity, the activities of which are based
or conducted in a country or currency other than those of the reporting entity

From IFRS 3:
> An integrated set of activities and assets that is capable of being conducted
and managed for the purpose of providing a return in the form of dividends,
lower costs or other economic benefits directly to investors or other owners,
members or participants

From Wikipedia [Branch Office][branch-wiki]:
A branch office is an outlet of a company or, more generally, an organization that – unlike a subsidiary – does not constitute a separate legal entity, while being physically separated from the organization's main office.


### parent_subsidiary
A subsidiary of the parent

### parent_branch
A branch of the parent

---
[dir-83-349]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:31983L0349
[branch-wiki]: https://en.wikipedia.org/wiki/Branch_office
[crr]: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32013R0575
