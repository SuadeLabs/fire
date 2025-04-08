import asyncio
import os
import unittest

import httpx
import markdown
import re
import pytest
from bs4 import BeautifulSoup

from . import (
    DOC_NAMES,
    DOCS_DIR,
    SCHEMA_NAMES,
    all_properties,
    property_doc_name,
    schema_enum_registry,
    schema_properties
)


MISSING_DOCS = [
            "account_ids",
            "cb_haircut",
            "col",
            "comment",
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
            # DO NOT ADD TO THIS LIST, ADD DOCUMENTATION!
        ]


def get_schema_refs_in_doc(docname):
    regex = r"schemas:\s+\[(.*?)\]"  # capture what is in the brackets

    filename = os.path.join(DOCS_DIR, f"{docname}.md")
    with open(filename) as f:
        for line in f.readlines():
            schema_refs = re.findall(regex, line)
            if schema_refs:
                return schema_refs[0].split(", ")

class TestDocs(unittest.TestCase):
    def test_property_has_docs(self):
        """
        Ensure there are docs for every new attribute
        """


        properties = all_properties()
        self.assertTrue(properties)

        no_docs = []
        for p in properties:
            if p not in DOC_NAMES + MISSING_DOCS:
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

    def test_urls_in_docs(self):
        async def async_requests(urls):
            async with httpx.AsyncClient(timeout=60) as client:
                responses = (client.get(url) for url in urls)
                results = await asyncio.gather(*responses, return_exceptions=True)

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

        results = asyncio.run(async_requests(urls))

        warns = []
        not_founds = []
        for response in results:
            if isinstance(response, httpx.HTTPError):
                warns.append(f"failed {response!s}: {response.request.url!s}")
            else:
                if not response.is_success:
                    warns.append(f"failed {response.status_code}: {response.url!s}")

                if response.status_code in (404,):
                    not_founds.append(str(response.url))

        print("\n=== Minor URL link warnings ===\n")
        for w in warns:
            print(w)

        assert not not_founds, f"URLs not found: \n {not_founds}"

    def test_docs_ref_correct_schemas(self):
        """
        Each doc should list the relevant schemas for that property.

        Check this exists and is correct.

        The syntax should be (on one line): "schemas: [x, y, z]"
        """
        for docname in DOC_NAMES:
            schema_refs = get_schema_refs_in_doc(docname)
            if schema_refs:
                # check no dupes
                assert len(schema_refs) == len(set(schema_refs)), f"Duplicate schema refs found for {docname}"

                for schema_name in schema_refs:
                    # Here we check the schemas found are real schemas
                    assert schema_name in SCHEMA_NAMES, f"Failed for {docname}.md"

                    # Here we check that the property is in the schema it says it is in
                    err_msg = f"Property: {docname} not found in {schema_name}"
                    assert docname in schema_properties(f"{schema_name}.json"), err_msg

            if not schema_refs:
                # Fail if no schema refs found at all
                raise AssertionError(f"No schema references found for doc: {docname}")

    def test_schemas_are_correctly_referenced_in_docs(self):
        """
        Here we check the reverse of the above, that schema properties are correctly documented
        with references in their docs.

        We skip abstract or inherited schemas as these are checked in child schemas. e.g. customer
        for entity
        """
        dont_check = [
            "batch",
            "common",
            "example",
            "entity",
        ]
        for schema_name in SCHEMA_NAMES:
            if schema_name in dont_check:
                continue

            for prop in schema_properties(f"{schema_name}.json"):
                if prop in MISSING_DOCS:
                    continue

                schema_refs = get_schema_refs_in_doc(prop)
                assert schema_name in schema_refs, f"{schema_name} not found for doc: {prop}"

    @pytest.mark.skip("This syntax rule has 501 transgressions, will take some fixing")
    def test_referenced_schemas_have_a_section_in_docs(self):
        """
        If a doc pertains to multiple schemas, each schema should have its own section in the docs
        identifiable with a level 1 header in markdown (#)
        """
        for docname in DOC_NAMES:
            schema_refs = get_schema_refs_in_doc(docname)
            if len(schema_refs) > 1:
                filename = os.path.join(DOCS_DIR, f"{docname}.md")
                with open(filename) as doc:
                    for schema_ref in schema_refs:
                        assert re.match(f"# {schema_ref}", doc.read()), f"No level-1 header (section) found in {docname} for {schema_ref}"
