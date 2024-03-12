---
layout:		readme
title:		"Home"
---

![logo-fire-red](https://github.com/SuadeLabs/fire/assets/12458414/9aa87ab9-6fbd-4f1f-8e2f-146dddf92229)

# Financial Regulatory (FIRE) Data Standard

---
![Build Status](https://github.com/SuadeLabs/fire/actions/workflows/ci-pipeline.yml/badge.svg)
[![Project Website](https://img.shields.io/badge/website-fire-red.svg)][fire]
[![Apache 2.0 License](https://img.shields.io/badge/LICENSE-Apache_2.0-yellow.svg)][license]
[![Join the chat at https://gitter.im/SuadeLabs/fire](https://badges.gitter.im/SuadeLabs/fire.svg)][gitter]
[![Contributor Guidelines](https://img.shields.io/badge/contributor-guidelines-lightgrey.svg)][contributing]

### What is the FIRE data standard?
The Financial Regulatory Data Standard (FIRE) defines a common specification for the transmission of granular data between regulatory systems in finance. Regulatory data refers to the data that underlies regulatory submissions, requirements, calculations and is used for policy, monitoring and supervision purposes.

The FIRE data schemas and code samples are licensed under the [Apache 2.0 License][apache] which has been chosen for being open, permissive and already widely accepted within the financial sector (think Hadoop, Cassandra, ActiveMQ).

The FIRE data standard is supported by the [European Commission][euc], the [Open Data Institute][odi] and the [Open Data Incubator for Europe][odine] via the Horizon 2020 funding programme.


<div class="image-group" style="width:100%; height:auto; margin:25px; text-align:center; background-color: white">
    <a href="http://ec.europa.eu/index_en.htm" target="_blank">
        <img src="./documentation/images/eu_commission.png" width="30%"/>
    </a>
    <a href="http://opendata.institute/" target="_blank">
        <img src="./documentation/images/odi.png" width="30%"/>
    </a>
    <a href="https://opendataincubator.eu/" target="_blank">
        <img src="./documentation/images/odine.png" width="30%"/>
    </a>
</div>

---

Please see the [contributing guidelines][contributing] and [guiding principles][guiding-principles] if you would like to contribute to this project.

### Random FIRE Data Generator
Included is a [random data generator][random-fire] which will generate data in line with the FIRE schema, but not necessarily realistic. (eg. You might get a loan with a balance of 10 but accrued interest of 1 million)

### Testing
You can run tests locally via `./run_tests.sh` or view the [CI test results here][travis-ci]


---
[fire]:         https://suade.org/fire/
[license]:      https://github.com/SuadeLabs/fire/blob/master/LICENSE
[gitter]:       https://gitter.im/SuadeLabs/fire
[contributing]: https://github.com/SuadeLabs/fire/blob/master/CONTRIBUTING.md
[guiding-principles]: https://github.com/SuadeLabs/fire/blob/master/guiding_principles.md
[apache]:	http://www.apache.org/licenses/LICENSE-2.0
[euc]:		http://ec.europa.eu/index_en.htm
[odi]:		http://opendata.institute/
[odine]:	https://opendataincubator.eu/
[random-fire]:      https://github.com/SuadeLabs/fire/blob/master/random_fire_generator.py
[travis-ci]:        https://travis-ci.org/github/SuadeLabs/fire
