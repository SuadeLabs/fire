---
layout:		schema
title:		"batch"
---

# Batch Schema

---

FIRE schema for representing bulk collections of bank objects.

### Properties

Name | Description | Type | Enum
--- | --- | --- | ---
name | <div class="enum-description">A unique identifier for the data batch</div> | string | - 
count | <div class="enum-description">Number of records in this batch</div> | integer | - 
data | <div class="enum-description">An array of data items of a single type</div> | array | - 
links | <div class="enum-description">An array describing the page structure of the full data batch</div> | array | - 
