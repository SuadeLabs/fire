---
layout: readme
title: "FIRE FAQs"
---

### Is FIRE a data model for my database?
No. The FIRE Data Format is designed to define the format and definition for the transmission of data rather than the storage of that data. Financial institution data as a whole lends itself naturally to a relational data model.
Depending on the use-case, FIRE data might be better stored in a non-relational or denormalised form.

### Given that FIRE is not a data model recipe, why do you have multiple schemas and relational ids that suggests an underlying relational table design?
The reason for separating data into "normalised" components is many: 
* To reduce redundant information and the amount of data going down the wire. If you are transmitting information on customers and products, doing so in multiple schemas will be less data than having customer information repeated as additional fields in every product schema.
* To remove possibility for errors and inconsistencies in data. Again, if we had customer information fields in our loan schema you could get two loans with the same customer_id but different credit_impaired statuses.
* By segregating schemas, it also allows entities (like customers or collateral) to be added independently (without a loan, for example). It also allows for transmitting of product data without customer data which can be particularly useful where data protection and security concerns might exist for different confidentiality levels of data.
