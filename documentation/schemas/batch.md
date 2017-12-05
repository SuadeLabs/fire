---
layout:		schema
title:		"batch"
---

# Batch Schema

---

FIRE schema for representing bulk collections of bank objects.

### Properties

Name | Type | Description
--- | --- | ---
name | A unique identifier for the data batch | string 
count | Number of records in this batch | integer 
data | An array of data items of a single type | array 
links | An array describing the page structure of the full data batch | array 
