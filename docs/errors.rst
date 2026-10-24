Error handling
==============

All client errors subclass :class:`unirate.exceptions.UnirateError`, so you can
catch everything from the client with a single ``except``:

.. code-block:: python

   from unirate import UnirateClient, UnirateError

   client = UnirateClient(api_key="YOUR_API_KEY")

   try:
       rate = client.get_rate("USD", "EUR")
   except UnirateError as exc:
       print(f"UniRate request failed: {exc}")

Exception classes
-----------------

The client maps HTTP status codes to specific exception types:

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Exception
     - HTTP status
     - Raised when
   * - ``AuthenticationError``
     - 401
     - The API key is missing or invalid.
   * - ``InvalidCurrencyError``
     - 404
     - A currency is unknown or no data is available.
   * - ``InvalidDateError``
     - 400
     - Request parameters are invalid (e.g. a bad date).
   * - ``RateLimitError``
     - 429
     - You have exceeded your plan's rate limit.
   * - ``APIError``
     - 503 / other
     - The service is unavailable or returned an error.
   * - ``UnirateError``
     - —
     - Base class; also wraps transport-level failures.

``APIError`` carries the ``status_code`` and (when available) the parsed
``response`` body as attributes:

.. code-block:: python

   from unirate.exceptions import APIError

   try:
       ...
   except APIError as exc:
       print(exc.status_code, exc.response)

Rate limits and plans
---------------------

A ``RateLimitError`` means you have hit your plan's quota. Historical and
time-series endpoints additionally require a Pro plan and will raise an
``AuthenticationError`` on the free tier. See the `UniRate API pricing
<https://unirateapi.com>`_ for current limits.
