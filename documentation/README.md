---
layout:		readme
title:		"README"
---

# General Information
This is an introduction for people new to JSON, if you are already familiar with JSON schemas already, move along now, nothing to see here.

### Headers
Please make sure all property markdown files start with the following header:

```markdown
--- 
layout:			property
title:			"name of the data item as it appears in the schemas (ie. lowercase)"
schemas:		[a list of schemas where this data_item is used]
---
```

# JSON
JSON is short for "Javascript Object Notation" and defines the format for an "object." An object in programming terms can be a variable, data structure or a function (basically anything). More commonly, in Object-Oriented programming an object typically refers to an Instance of a Class. That is to say, a specific description of something more general. Like a Goat being an instance of the Class "Animal." 

For our purposes, we can just consider JSON to be the data and a JSON-schema to just define the format for that data, ie. what it needs to *look like* so the computer can understand where things are when it receives it.

### Properties, names and values
A property in JSON notation is a name-value pair and list of properties is what makes up the data in our schemas. What you would normally call a "field" (like interest_rate) is the *name of the property* and what we might call an attribute is the *value of the property*.

**One property**
```javascript
{"name": value}
```

**List of properties**
```javascript
{"name1": "value1", "name3": "value3", "name2": "value2"}
```

JSON is just text, so the formatting is purely visual, even the order (see above) does not matter. As things get more complicated however, it is considered best practice to format your JSON to look more human-friendly:

```javascript
{
  "name1": "value1",
  "name3": "value3",
  "name2": "value2"
}
```

You can visit: [http://jsonprettyprint.com/](http://jsonprettyprint.com/) to help with this formatting.


# JSON-Schema
While any data sent/received in JSON format will always look like the above, we need a way to make sure it is what we are expecting. For this we define a JSON-Schema which basically describes what the JSON formatted data should look like.

### Description
What if we want to add a little more information to describe our property? This is where the "description" parameter comes in. We add some curly brackets where the "value" is supposed to be and add a description as so: 

```javascript
{"name": {"description": "A little blurb about this property"} }
```

*or*

```javascript
{
  "name": {
   "description": "A little blurb about this property"
  }
}
```

### Types
Now that we have described our property value, let's go a step further and narrow it down to a specific type. Is it a number, a word, a list? The "type" parameter allows us to specify exactly this. So now our schema would look something like this:

```javascript
{
  "name": {
   "description": "A little blurb about this property",
   "type": "number"
  }
}
```

JSON has 7 standard types that we can use:

A **null** value means the value is unknown. Note that this is different from an empty or zero field. If the field is empty, undefined or does not exist, then it can simply be omitted (unless it is indicated as being "required" in which case you should provide a suitable default value).

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

An **object** is a JSON object, or in other words, the thing we are defining. So this allows for nesting of objects within objects. This is valid JSON, but adds time and complexity in the decoding/parsing process so generally should be avoided.

```javascript
{
  "farm_id": "E2G2K3LSJENJ4J3K10H",
  "animals": {
    "goat": 2,
    "sheep": 7,
    "sheep_dog": 1
  },
  "farm_owner": "peter"
}
```

### Formats
How would you represent a date value like 31 August 2014? 
- We could make use of a string type: "31 August 2014" but then "Aug 31 2014" would also be valid and we would have trouble ordering our data by date.
- We could accept an integer type: 31082014 but then 1235 would also be a valid integer. And even if we restricted it to 8-digits, we would have to remember to make sure single digit months have a leading zeros and still this doesn't tell us if it is 31 August 2014 or 14 February 8013.

You get the idea, sometimes we need more information. This is where the **format** parameter comes in. 

The following is the list of the formats specified in the JSON Schema specification:

- "date-time": Date representation, as defined by RFC 3339, section 5.6.
- "email": Internet email address, see RFC 5322, section 3.4.1.
- "hostname": Internet host name, see RFC 1034, section 3.1.
- "ipv4": IPv4 address, according to dotted-quad ABNF syntax as defined in RFC 2673, section 3.2.
- "ipv6": IPv6 address, as defined in RFC 2373, section 2.2.
- "uri": A universal resource identifier (URI), according to RFC3986.

The one we use most commonly from this is the **"date-time"** format and it basically means your dates and timestamps need to be a valid string but also look like this: YYYY-MM-DDTHH:MM:SSZ in accordance with ISO 8601. 

So for our example, if this is your schema:
```javascript
{"animal_birthday": {
  "description": "The recorded birthday for the animal.",
  "type": "string",
  "format": "date-time"
  }
}
```
then this would be a valid input:
```javascript
{"animal_birthday": "1995-06-07T13:00:00Z"}
```



<!-- ### Restrictions
Once we have defined the name and type of our  -->

