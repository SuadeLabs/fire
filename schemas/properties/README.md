---
layout:		readme
title:		"Properties README"
---

# General Information

### Headers
Please make sure all property markdown files start with the following header:

> ---
> layout:			property
> title:			"name of the data item as it appears in the schemas (ie. lowercase)"
> schemas:			[a list of schemas where this data_item is used]
> ---

# Properties, names and values
A property in JSON notation is a name-value pair and list of properties is what makes up the "fields" in our schemas.

> *One property*
> {"name": value}
>
> *List of properties*
> {"name1": "value1", "name3": "value3", "name2": "value2"}

JSON is just text, so the formatting is purely visual, even the order (see above) does not matter. As things get more complicated however, it is considered best practice to format your JSON to look more human-friendly:

> {
>   "name1": "value1",
>   "name3": "value3",
>   "name2": "value2"
> }

You can visit: [http://jsonprettyprint.com/][http://jsonprettyprint.com/] to help with this formatting.

# Description

# Types
A **null** value means the value is unknown. Note that this is different from an empty or zero field.

An **integer** is a number without a fraction or exponent part.

> ex 1. 4
> ex 2. 26908289076124561671021

An **number** is a number with or without a fraction or exponent part.

> ex 1. 26908289076124561671021
> ex 2. 269082.89076124561671021

An **string** is a list of characters (except " or \ ) inside "quotes". You can think of a string as a word. Note that the "word" can also contain numbers (like your national insurance number). But also note that numbers represented as strings need to be converted back to numbers if you want to add or multiply them.

> ex 1. "sheep"
> ex 2. "AS546NB8"

A **boolean** is simple *true* or *false* flag. Note that the true/false flag is lowercase and not inside "quotes."

> ex 1. true
> ex 2. false

An **array** is a list of the other types, separated by commas and inside square brackets [ ].

> ex 1. [2, 235, 34634, 34]
> ex 2. ["sheep", "sheep_dog", "fox"]


null
The JSON null value.
object
A JSON object.

# Restrictions


