Installation
============

Install from PyPI with ``pip``:

.. code-block:: console

   $ pip install unirate-api

The package supports Python 3.7 and newer. Its only runtime dependency is
`requests <https://requests.readthedocs.io/>`_ (>= 2.25.0).

Getting an API key
------------------

Every request needs an API key. Create a free account at
`unirateapi.com <https://unirateapi.com>`_ — the free tier includes real-time
rates, conversion, the supported-currency list, and VAT rates, with no credit
card required.

Keep your key out of source control. A common pattern is to read it from an
environment variable:

.. code-block:: python

   import os
   from unirate import UnirateClient

   client = UnirateClient(api_key=os.environ["UNIRATE_API_KEY"])

Verifying the installation
--------------------------

.. code-block:: python

   from unirate import UnirateClient

   client = UnirateClient(api_key="YOUR_API_KEY")
   currencies = client.get_supported_currencies()
   print(f"{len(currencies)} currencies supported")

If this prints a count without raising, the client is installed and your key
works. See :doc:`errors` for how failures are reported.
