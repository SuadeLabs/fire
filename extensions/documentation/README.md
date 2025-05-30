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

# Extensions to the FiRe schemas

The extensions directory contains extra properties, which are regarded as too jurisdiction- or regulation-specific to include in the core FiRe schemas. A lot of these properties will be irrelevant to certain users.

Every property in each of the extended schemas contains a `jurisdictions` array which lists the jurisdictions this property is relevant to. Users of the extended FiRe schemas are expected to only use properties that apply to their jurisdictions.
