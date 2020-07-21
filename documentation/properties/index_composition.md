---
layout:     property
title:      "index_composition"
schemas:    [security]
---

# index_composition

---
The index_composition is an array of reference_id/weight providing a breakdown of index constituents.

## reference_id
A specific reference to a constituent in order to be able to establish a link in netting operations.

For **equity indices** we expect the reference_id to be an **ID** linking another security record.

## weight
Decimal value representing the proportion of a reference_id in the allocated index. We expect the sum of all weights to equal 1 but we do not enforce this validation.