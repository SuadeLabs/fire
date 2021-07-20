---
layout: readme
title: Guiding Principles
---

# Guiding principles
The guiding principles are composed of:
* [Project principles](#project-principles)
* [Schema design principles](#schema-design-principles)

## Project principles
The FIRE project should be:

### Easy to understand
FIRE should be easy to read, understand and explain for non-technical users. The reason for this is that (like any data specification for a complex, regulated industry) FIRE contains a great deal of embedded subject matter expertise needs to be evaluated and updated by specialists in finance, regulatory policy, accounting and law. Similarly, as FIRE will be implemented and used by developers, who may not necessarily have the same level of subject matter expertise, it should not require a great deal of financial or regulatory knowledge to understand the general concepts for use.

### Easy to use 
FIRE should be easy to implement and should require drastic and fundamental changes to how financial institutions identify, conceptualize, create, store and manage their data. This is why the schemas attributes will look familiar to those associated with traditional relational tables and financial data models. Despite a relational look and feel, as JSON objects, FIRE data can be easily used with NoSQL or Graph databases. 

### Free, open and collaborative
This should be a given but is unfortunately not very common in the financial industry as enterprise software vendors are keen to create lock-in to their systems and platforms with closed and proprietary data models and formats. As such, FIRE carries an open-source [Apache 2.0 License][license] and is publicly accessible on Github for easy integration with other IT systems.


## Schema design principles
The FIRE Data schema specifications should respect the following 3 schema design principles. Note that the terms data attributes and schema properties are interchangeably used.

### 1. Data attributes should always be true
Schema properties (data attributes) should be self-evident truths and not depend on the application for which they will be used. In the same way that your date of birth doesn't change depending on who's asking, properties should follow the same philosophy. Practically, this means data should not be dependent on the intended computation, visualisation, report or application. Data should simply represent a labelling of a contract or entity based on purely legal definitions. As such, every pull request requires a corresponding, documented, legal reference, preferably to a currently in-force financial regulation.

### 2. Data attributes should be atomic
Schema properties should uniquely describe the data. Properties should be fundamental, atomic units of measurement. One property should not be derivable from other properties. Similar to the "flags" problem, schema properties should not have embedded logic. This was often done with legacy systems for performance reasons when databases were fast, CPUs slow and memory expensive, but today, most applications are I/O bound. You may still choose to store secondary or derived data, but this is the concern of the application and its specific goals rather than the underlying fundamental data.

eg. It would be unwise to have a loan balance in original currency and USD. This inevitably leads to data of the form:

| **balance** | **original ccy** | **in USD** |
|-------------|------------------|------------|
| 100         | EUR              | 120        |
| 100         | USD              | 90         |
| 100         | EUR              | 130        |

> Can you spot the problem?

Better is to just have an original currency and an exchange rate.

### 3. Data attributes should be consistent
Schema properties should try to avoid logical inconsistencies. In other words, one schema property should not contradict another. This is a common occurrence in legacy systems where schemas were updated without a big picture consideration. This typically manifests itself in the form of flags

eg. There should not be a security type titled "government_bond" and a "issuer-type-is-government" flag. 

This might seem ok:

| **security type** | **issuer-type-is-govt** |
|-------------------|-------------------------|
| government_bond   | Y                       |

This has the potential to create contradictory data of the nature:

| **security type** | **issuer-type-is-govt** |
|-------------------|-------------------------|
| government_bond   | N                       |

Better would be:

| **security type** | **issuer-type-is-govt** |
|-------------------|-------------------------|
| bond              | Y                       |

Even better would be:

| **security type** | **issuer type** |
|-------------------|-----------------|
| bond              | government      |

Why? Because flags are limiting and can still lead to inconsistencies:

| **security type** | **issuer-type-is-govt** | **issuer-type-is-retail** |
|-------------------|-------------------------|---------------------------|
| bond              | Y                       | Y                         |


---
[license]:  https://github.com/suadelabs/fire/LICENSE
