---
layout:		schema
title:		"entity"
---

# Entity Schema

---

Data schema to define a person or legal entity.

### Properties

Name | Type | Description
--- | --- | ---
id | The unique identifier for the person or legal entity within the financial institution. | string 
date | YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. | string 
boe_industry_code | Bank of England industry code. | string 
boe_sector_code | Bank of England sector code. | string 
country_code | The person or entity country of residence. Two-letter country code as defined according to ISO 3166-1. | undefined 
credit_impaired | Flag to determine if the entity credit quality is impaired. | boolean 
cqs_standardised | The credit quality step for standardised approach. | integer 
cqs_irb | The credit quality step for internal ratings based approach. | integer 
intra_group | Flag to indicate that this should be considered an intra-group entity. | boolean 
lei_code | The LEI code for the legal entity (for corporates). | string 
legal_entity_name | The official legal name of the entity. | string 
name | The name of the person or legal entity to be used for display and reference purposes. | string 
parent_id | The unique identifier for the ultimate parent of the person or legal entity. | string 
parent_name | The name of the ultimate parent of person or legal entity to be used for display and reference purposes. | string 
risk_country_code | Two-letter country code describing where the risk for the security resides. In accordance with ISO 3166-1 | undefined 
sic_code | The UK SIC 2007 standard industry and sector classification. | integer 
sources | Identifiers for data sources. Useful for analytics and MI purposes. | array 
type | The designated financial or legal entity category this person or legal entity falls under | string 
