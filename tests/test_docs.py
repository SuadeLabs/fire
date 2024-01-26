from bs4 import BeautifulSoup
import grequests
import markdown
import os
import unittest
from . import (
    SCHEMA_NAMES,
    all_properties,
    DOCS_DIR,
    DOC_NAMES,
    property_doc_name,
    schema_enum_registry,
)


class TestDocs(unittest.TestCase):
    def test_property_has_docs(self):
        """
        Ensure there are docs for every new attribute
        """
        exceptions = [
            "account_ids",
            "cb_haircut",
            "col",
            "comment",
            "contribution_amount",
            "contribution_text",
            "data",
            "delta",
            "derivative_id",
            "forward_rate",
            "gamma",
            "insolvency_rank",
            "leg",
            "links",
            "loan_id",
            "loan_ids",
            "next_exercise_date",
            "next_payment_amount",
            "next_receive_amount",
            "next_receive_date",
            "next_reset_date",
            "page",
            "payment_date",
            "report_type",
            "reset_date",
            "rho",
            "row",
            "settlement_type",
            "security_id",
            "theta",
            "title",
            "underlying_derivative_id",
            "underlying_issuer_id",
            "underlying_security_id",
            "underlying_strike",
            "values",
            "vega",
            "vol_adj_fx",
        ]

        properties = all_properties()
        self.assertTrue(properties)

        no_docs = []
        for p in properties:
            if p not in DOC_NAMES + exceptions:
                no_docs.append(p)

        self.assertFalse(
            no_docs, "No documenation found for properties: {}".format(no_docs)
        )
        for doc in DOC_NAMES:
            self.assertTrue(
                doc in properties, "No property found for documenation: {}".format(doc)
            )

    def test_enums_documented(self):
        """
        Each enum value should have a corresponding level 3 header (###) in the
        documentation markdown file.

        eg. ### enum_value
        """

        def error_msg(schema_name, value, enum):
            return (
                "Could not find a level-3 header (###) entry for "
                "{}:'{}' in {}.md.\n\n".format(schema_name, value, enum)
            )

        exceptions = [
            "country_code",  # TL;DR
            "currency_code",  # TL;DR
            "nace_code",  # TL;DR
            "interest_repayment_frequency",  # Same as repayment_frequency
            "reporting_relationship",  # same as relationship
        ]
        for schema_name in SCHEMA_NAMES:
            for enum, values in schema_enum_registry(schema_name).items():
                if enum in exceptions:
                    continue

                property_docs = property_doc_name(enum)

                if not property_docs:
                    raise FileNotFoundError(
                        f"Could not find documentation for: {schema_name} :: {enum}"
                    )  # noqa

                _file = os.path.join(DOCS_DIR, property_docs)

                for v in values:
                    with open(_file) as enum_doc:
                        assert "### {}".format(v) in enum_doc.read(), error_msg(
                            schema_name, v, enum
                        )  # noqa

    def test_urls_in_docs(s):
        def exception(request, exception):
            return f"{request} - {exception}"

        def async_requests(urls):
            results = grequests.map(
                (grequests.get(u) for u in urls), exception_handler=exception, size=100
            )
            return results

        urls = []

        for docname in DOC_NAMES:
            filename = os.path.join(DOCS_DIR, f"{docname}.md")
            with open(filename) as f:
                doc_html = markdown.markdown(f.read())
                soup = BeautifulSoup(doc_html, features="html.parser")
                links = soup.find_all("a")
                for link in links:
                    url = link.get("href")
                    if not url.startswith("http"):
                        raise ValueError(f"Invalid URL in {docname}: {url}")

                    urls.append(url)

        results = async_requests(urls)

        warns = []
        not_founds = []
        for resp in results:
            if not resp.ok:
                warns.append(f"failed {resp.status_code}: {resp.url}")
            if resp.status_code in [404]:
                not_founds.append(resp.url)

        if not_founds:
            raise ValueError(f"URLs not found: \n {not_founds}")

        print("=== Minor URL link warnings ===")
        for w in warns:
            print(w)
