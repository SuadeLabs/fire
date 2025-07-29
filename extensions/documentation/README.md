---
layout:		readme
title:		"Introduction"
---

# General Information
This guide assumes you have already read and understood the main documentation for the fire schemas.

### Headers
Please make sure all property markdown files in documentation/properties/ folder start with the following header:

```

---
layout:			property
title:			"name of the data item as it appears in the schemas (ie. lowercase)"
schemas:		[a list of schemas where this data_item is used]
---

```

# Extensions to the FIRE schemas

In a nutshell, extensions are exactly how they sound, extended lists of properties or attributes for each standard FIRE schema. So the loan extensions schema is just like adding a list of new properties to the loan schema, but they are *optional*. This makes the extensions rigorous, but not cumbersome to users to whom the properties are not relevant. 

As you will see, the extensions are long, varied and often very niche data elements relevant only to certain jurisdictions or specific domains. As such, each element in the extensions schemas is accompanied by a "jursdiction" list in order to better assess relevance.

It is possible that a property in the extension schema might get *upgraded* to the main schema in the event that it is deemed more significant. Additionally, as extensions are niche attributes for very specific use cases, they may not have the same degree of backwards compatibility of the primary FIRE schemas. Any deprecations will of course be flagged and supported as indicated in the release notes.

### Extension contributions
How do I know if something goes in the extension schema or the main schema? Well there are some rules:
1. Extension properties must still be unique within the wider context. A property cannot be both in the extension schema and a standard FIRE schema.
2. Extension properties must be documented just like regular properties, just in this folder.
3. Extension properties must have the jurisdiction array included.
4. If a contribution is to an existing FIRE schema property (like extending an enum granularity), even if it is jurisdiction-specific, it should be included in the main property, not as an extension.

