---
layout:		property
title:		"lei_code"
schemas:	[entity]
---

# lei_code

---

According to the [Legal Entity Identifier Regulatory Oversight Committee][web], the Legal Entity Identifier (LEI) is a 20-character reference code to uniquely identify legally distinct entities that engage in financial transactions and associated reference data. Two fundamental principles of the LEI code are:

- Uniqueness: an LEI is assigned to a unique entity. Once assigned to an entity, and even if this entity has for instance ceased to exist, a code should never be assigned to another entity.
- Exclusivity: a legal entity that has obtained an LEI cannot obtain another one. Entities may port the maintenance of their LEI from one operator to another. The LEI remains unchanged in the process.

You will find below information on the structure of LEI codes, the components of the reference data associated to each LEI and the definition of entities eligible to obtain an LEI.

Entities who wish to obtain an LEI should consult the page, [How to Obtain an LEI][lei2]. The GLEIF publishes a centralised data base of LEIs.

[web]: https://www.leiroc.org/lei.htm
[lei2]: https://www.leiroc.org/lei/how.htm

### Structure of the LEI code

The LEI definition currently relies on a standard published by the International Organisation for Standardisation (ISO) on 30 May 2012 [(ISO 17442:2012, Financial Services - Legal Entity Identifier (LEI))][isolink]

The number allocation scheme was further specified in Annex 2 of the Financial Stability Board's third progress note on the Global LEI Initiative on 24 October 2012:

- Characters 1-4: A four character prefix allocated uniquely to each Local Operating Unit (LOU) issuing LEIs. This prefix identifies (except for LEIs issued before 30 November 2012) the LOU that first issued the LEI and contributes to avoiding that different LOUs would assign the same LEI. However, the entity might have subsequently ported the maintenance of its LEI to a different LOU. Use the GLEIF search function to check which LOU is maintaining an LEI ("Managing LOU" field) and go to this LOU's website to update the reference data of the entity or certify that it is still up-to-date.
- Characters 5-6: Two reserved characters set to zero.
- Characters 7-18: Entity-specific part of the code generated and assigned by LOUs according to transparent, sound and robust allocation policies.
- Characters 19-20: Two check digits as described in the ISO 17442 standards. The check digit scheme follows ISO/IEC 7064 (MOD 97-10) and contributes to avoiding typing errors.

[isolink]: http://www.iso.org/iso/catalogue_detail?csnumber=59771

### Entities eligible for an LEI

[ISO 17442:2012]][isolink] states that the ISO standard "specifies the elements of an unambiguous Legal Entity Identifier scheme to identify the legal entities relevant to any financial transaction".

The term "legal entities" includes, but is not limited to, unique parties that are legally or financially responsible for the performance of financial transactions or have the legal right in their jurisdiction to enter independently into legal contracts, regardless of whether they are incorporated or constituted in some other way (e.g. trust, partnership, contractual). It excludes natural persons, but includes governmental organizations and supranationals." [¹](http://www.iso.org/iso/catalogue_detail?csnumber=59771)

Individuals acting in a business capacity are eligible to an LEI under certain conditions described by the ROC on [30 September 2015][leiroc].

A policy document published by the ROC on 11 July 2016 sets forth the policy design, definitions, and conditions for issuance of LEIs for international branches (also known as foreign branches). Implementation is expected to start in early 2017, subject to ROC concurrence with an appropriate framework being established to ensure that the conditions described in this document are met.

[leiroc]: https://www.leiroc.org/publications/gls/lou_20150930-1.pdf

### Reference data

As specified in [ISO 17442:2012][isolink], the reference data stored in the LEI data base for each entity includes:

- The official name of the legal entity;
- The address of the headquarters of the legal entity;
- The address of legal formation;
- The date of the first LEI assignment;
- The date of last update of the LEI;
- The date of expiry, if applicable;
- For entities with a date of expiry, the reason for the expiry should be recorded, and if applicable, the LEI of the entity that acquired the expired entity;
- The official business registry where the foundation of the legal entity is mandated to be recorded on formation of the entity, where applicable;
- The reference in the official business registry to the registered entity, where applicable.

The ROC adopted a common data format (CDF) in 2014 defining with more granularity the content of an LEI record.

Beyond the "level 1" "business card" information described above and already collected by the Global LEI System, the objective is to progressively extend the reference data to "level 2" data on relationships among entities. As a first step, the ROC established in December 2014 a task force to develop a proposal for collecting in the Global LEI System information on the direct and ultimate parents of legal entities. A public consultation was launched on 7 September 2015 on this topic. Phased implementation of such information is expected to begin in 2016.

