Quickstart
==========

This page walks through the free-tier features. Grab an API key from
`unirateapi.com <https://unirateapi.com>`_ first, then create a client:

.. code-block:: python

   from unirate import UnirateClient

   client = UnirateClient(api_key="YOUR_API_KEY")

You can pass a custom request ``timeout`` (seconds) if you need to:

.. code-block:: python

   client = UnirateClient(api_key="YOUR_API_KEY", timeout=10)

Exchange rates
--------------

Get the rate for a single pair:

.. code-block:: python

   rate = client.get_rate("USD", "EUR")
   print(rate)  # e.g. 0.92

Omit the target currency to get every rate for a base currency as a ``dict``:

.. code-block:: python

   all_rates = client.get_rate("USD")
   print(all_rates["JPY"])

Currency conversion
-------------------

Convert an amount from one currency to another:

.. code-block:: python

   result = client.convert("GBP", amount=100, from_currency="USD")
   print(result)  # 100 USD worth of GBP

Supported currencies
--------------------

.. code-block:: python

   currencies = client.get_supported_currencies()
   print("USD" in currencies, "EUR" in currencies)

VAT rates
---------

Fetch VAT rates for every country, or a single country by its two-letter code:

.. code-block:: python

   all_vat = client.get_vat_rates()
   germany = client.get_vat_rates(country="DE")

Historical data (Pro plan)
--------------------------

Historical rates, historical conversion, and time series require a Pro plan;
on the free tier they return an authorization error. See the `pricing page
<https://unirateapi.com>`_ for details.

.. code-block:: python

   # Requires a Pro plan
   rate = client.get_historical_rate("2024-01-01", from_currency="USD",
                                      to_currency="EUR")

   series = client.get_time_series("2024-01-01", "2024-01-31",
                                   base_currency="USD",
                                   currencies=["EUR", "GBP"])

Response formats
----------------

Every method returns parsed JSON by default. Pass ``format="csv"`` (or
``"xml"`` / ``"tsv"``) to get the raw response text instead. See
:doc:`formats`.

.. code-block:: python

   csv_text = client.get_rate("USD", "EUR", format="csv")
