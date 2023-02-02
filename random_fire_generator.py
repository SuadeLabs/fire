import argparse
import json
import iso3166
import logging
import random
import timeit
from datetime import datetime
from faker import Faker


fire_schemas = [
    "v1-dev/account.json",
    "v1-dev/curve.json",
    "v1-dev/customer.json",
    "v1-dev/derivative.json",
    "v1-dev/derivative_cash_flow.json",
    "v1-dev/guarantor.json",
    "v1-dev/issuer.json",
    "v1-dev/loan.json",
    "v1-dev/loan_transaction.json",
    "v1-dev/security.json",
]
WRITE_PATH = ""
fake = Faker()


def random_currency():
    return fake.currency_code()


def random_country():
    country_codes = [c[1] for c in iso3166.countries]
    return random.choice(country_codes)


def random_accounting_treatment():
    accounting_treatments = [
        "fv_designated",
        "fv_designated_mandatory",
        "held_for_trading",
        "held_for_hedge",
        "available_for_sale",
        "loans_and_recs",
        "held_to_maturity",
        "amortised_cost",
        "fv_oci",
    ]
    return random.choice(accounting_treatments)


def random_integer(min, max):
    return random.randrange(min, max)


def random_enum(enum_list):
    return random.choice(enum_list)


def random_word(n):
    return " ".join(fake.words(n))


def random_text(n):
    return fake.text(n)


def random_date():
    d = fake.date_time_between(start_date="-10y", end_date="+30y")
    return d.strftime("%Y-%m-%dT%H:%M:%SZ")


def insert(product, attr, attr_value):
    return product["data"][0].update({attr: attr_value})


def generate_random_fires(fire_schemas, n=100):
    """
    Given a list of fire product schemas (account, loan, derivative_cash_flow,
    security), generate random data and associated random relations (customer,
    issuer, collateral, etc.)

    TODO: add config to set number of products, min/max for dates etc.

    TODO: add relations
    """
    batches = []
    start_time = timeit.default_timer()

    for fire_schema in fire_schemas:
        f = open(fire_schema, "r")
        schema = json.load(f)
        data_type = fire_schema.split("/")[-1].split(".json")[0]
        data = generate_product_fire(schema, data_type, n)
        batches.append(data)

    end_time = timeit.default_timer() - start_time
    logging.warn(
        "Generating FIRE batches and writing to files"
        " took {} seconds".format(end_time)
    )
    # logging.warn(batches)
    return batches


def write_batches_to_files(batches):
    for b in batches:
        filename = "[" + str(b["date"]) + "] " + str(b["name"]) + ".json"
        f = open(filename.replace(" ", "_"), "w+")
        f.write(json.dumps(b, indent=2))
        f.close()


def include_embedded_schema_properties(schema):
    try:
        for i in range(len(schema["allOf"])):
            inherited_schema = schema["allOf"][i]["$ref"].split("/")[-1]
            f = open("v1-dev/" + inherited_schema, "r")
            inherited_schema = json.load(f)
            schema["properties"] = dict(
                schema["properties"].items() + inherited_schema["properties"].items()
            )

    except KeyError:
        pass

    return schema


def generate_product_fire(schema, data_type, n):
    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    batch = {
        "name": "Random_FIRE_{}s".format(schema["title"][:-7]),
        "date": now,
        "data": [],
    }

    schema = include_embedded_schema_properties(schema)
    schema_attrs = schema["properties"].keys()

    for i in range(n):
        p = {}
        batch["data"].append(p)
        for attr in schema_attrs:
            attr_obj = schema["properties"][attr]

            if attr == "id":
                attr_value = str(i)
                batch["data"][i].update({attr: attr_value})
                continue

            elif attr == "date":
                attr_value = now
                batch["data"][i].update({attr: attr_value})
                continue

            elif attr in ["currency_code", "facility_currency_code"]:
                attr_value = random_currency()
                continue

            elif attr in ["country_code", "risk_country_code"]:
                attr_value = random_country()
                continue

            elif attr == "accounting_treatment":
                attr_value = random_accounting_treatment()
                continue

            elif attr in ["isin_code" or "underlying_isin_code"]:
                attr_value = random_text(12)
                continue

            elif attr == "reporting_id":
                attr_value = random_text(20)
                continue

            else:
                try:
                    attr_type = schema["properties"][attr]["type"]
                except KeyError:
                    # logging.warn(
                    #     "Failed to determine attr type for {}".format(attr))
                    continue

                if attr_type == "number":
                    attr_value = random_integer(0, 500) / 100.0
                    batch["data"][i].update({attr: attr_value})
                    continue

                elif attr_type == "integer":
                    try:
                        attr_min = attr_obj["minimum"]
                    except KeyError:
                        attr_min = -10000
                    try:
                        attr_max = attr_obj["maximum"]
                    except KeyError:
                        attr_max = 100000

                    attr_value = random_integer(attr_min, attr_max)
                    batch["data"][i].update({attr: attr_value})
                    continue

                elif attr_type == "string":
                    try:
                        attr_enums = attr_obj["enum"]
                        attr_value = random_enum(attr_enums)

                    except KeyError:
                        try:
                            attr_format = attr_obj["format"]
                            if attr_format == "date-time":
                                attr_value = random_date()
                            else:
                                pass

                        except KeyError:
                            # logging.warn(
                            #     "Simple stringing {}".format(attr))
                            attr_value = random_word(1)

                    batch["data"][i].update({attr: attr_value})
                    continue

                elif attr_type == "boolean":
                    attr_value = random.choice([True, False])
                    batch["data"][i].update({attr: attr_value})
                    continue

                else:
                    # logging.warn(
                    #     "Failed to determine attr type for "
                    #     "{} {}".format(schema["title"][:-7], attr)
                    # )
                    continue

    # logging.warn(json.dumps(product))
    return batch


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate random FIRE data points.")
    parser.add_argument(
        "count",
        type=int,
        help="Integer number of FIRE data points to generate \
              for each data type",
    )
    args = parser.parse_args()

    write_batches_to_files(generate_random_fires(fire_schemas, args.count))
