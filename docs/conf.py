"""Sphinx configuration for the unirate-api Python client documentation.

The build only needs Sphinx + the Furo theme. ``requests`` is mocked via
``autodoc_mock_imports`` so autodoc can import the package from source without
installing any runtime dependency.
"""

import os
import sys
from datetime import datetime

# Make the ``unirate`` package importable from the repository root so autodoc
# can read the live docstrings without installing the package.
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = "unirate-api"
author = "UniRate API"
copyright = f"{datetime.now():%Y}, UniRate API"

# Keep in sync with unirate/__init__.py
release = "1.0.0"
version = "1.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # Google-style docstrings
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

# Mock the only third-party import so the doc build pulls no runtime deps.
autodoc_mock_imports = ["requests"]

autodoc_member_order = "bysource"
autodoc_typehints = "description"

napoleon_google_docstring = True
napoleon_numpy_docstring = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- HTML output -------------------------------------------------------------

html_theme = "furo"
html_title = "unirate-api (Python)"
html_baseurl = "https://unirate-api-python.readthedocs.io/"

# Dofollow homepage links rendered through the theme chrome.
html_theme_options = {
    "source_repository": "https://github.com/UniRate-API/unirate-api-python/",
    "source_branch": "main",
    "source_directory": "docs/",
    "footer_icons": [
        {
            "name": "UniRate API",
            "url": "https://unirateapi.com",
            "html": "unirateapi.com",
            "class": "",
        },
    ],
}

# A banner link to the API homepage on every page.
html_theme_options["announcement"] = (
    'Powered by the <a href="https://unirateapi.com">UniRate API</a> &mdash; '
    'free real-time currency exchange &amp; VAT rates.'
)
