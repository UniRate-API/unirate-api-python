"""
Unirate API Client
~~~~~~~~~~~~~~~~~

A Python client for the Unirate API.
"""

from .client import UnirateClient
from .exceptions import UnirateError

__version__ = "0.1.0"
__all__ = ["UnirateClient", "UnirateError"] 