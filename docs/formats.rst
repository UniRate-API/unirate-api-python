Response formats
================

By default every method parses the JSON response and returns native Python
types (``float``, ``dict``, ``list``). Pass a ``format`` argument to receive
the raw response body as a string instead. Supported values are ``"json"``
(default), ``"xml"``, ``"csv"``, and ``"tsv"``.

.. code-block:: python

   client.get_rate("USD", "EUR")                 # -> float
   client.get_rate("USD", "EUR", format="csv")   # -> str (CSV text)
   client.get_rate("USD", "EUR", format="xml")   # -> str (XML text)

When ``format`` is anything other than ``"json"``, the client returns the
response text unchanged — it does not attempt to parse it.

JSONP
-----

For ``json`` responses you may pass a ``callback`` name to wrap the payload in
a JSONP call, which is useful when serving the response directly to a browser:

.. code-block:: python

   client.get_rate("USD", "EUR", callback="handleRate")

See the `UniRate API documentation <https://unirateapi.com>`_ for the full
specification of each endpoint and its response shape.
