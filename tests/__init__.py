import os


HOME = os.path.realpath(".")
SCHEMAS_DIR = os.path.join(HOME, 'v1-dev')
DOCS_DIR = os.path.join(HOME, "documentation", "properties")

_, _, filenames = next(os.walk(SCHEMAS_DIR), (None, None, []))
SCHEMA_FILES = [f for f in filenames if f.endswith(".json")]
SCHEMA_NAMES = [f.split(".json")[0] for f in SCHEMA_FILES]

_, _, filenames = next(os.walk(DOCS_DIR), (None, None, []))
DOC_FILES = [f for f in filenames if f.endswith(".md")]
DOC_NAMES = [f.split(".md")[0] for f in DOC_FILES]
