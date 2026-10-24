unirate-api: Python client for the UniRate API
===============================================

``unirate-api`` is the official Python client for the `UniRate API
<https://unirateapi.com>`_ — a REST API for **real-time currency exchange
rates**, **currency conversion**, **historical rates**, and **EU/global VAT
rates**, covering 170+ currencies.

The client is a thin, typed wrapper over the HTTP API. Its only dependency is
`requests <https://requests.readthedocs.io/>`_, and it works on Python 3.7+.

.. code-block:: python

   from unirate import UnirateClient

   client = UnirateClient(api_key="YOUR_API_KEY")

   # 1 USD in EUR
   print(client.get_rate("USD", "EUR"))

   # Convert 100 USD to GBP
   print(client.convert("GBP", amount=100, from_currency="USD"))

Get a free API key at `unirateapi.com <https://unirateapi.com>`_ — no credit
card required. The same key works across all of the `UniRate client libraries
<https://unirateapi.com>`_ (Python, Node.js, Go, Rust, Java, Ruby, PHP, and
more).

.. toctree::
   :maxdepth: 2
   :caption: Contents

   installation
   quickstart
   api
   errors
   formats

Features
--------

- **Real-time exchange rates** between any supported currency pair.
- **Currency conversion** for arbitrary amounts.
- **Historical rates** and **time series** for a date or date range (Pro plan).
- **VAT rates** for all countries or a single country.
- **Multiple response formats**: JSON (default), XML, CSV, TSV, and JSONP.
- **Typed, documented methods** with clear exception classes.

Links
-----

- API homepage and free API key: `unirateapi.com <https://unirateapi.com>`_
- Source code: `GitHub <https://github.com/UniRate-API/unirate-api-python>`_
- Package: `PyPI <https://pypi.org/project/unirate-api/>`_

Indices and tables
-------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
