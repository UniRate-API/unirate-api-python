# Unirate API Client

Official Python client for the Unirate API. This library provides a simple and intuitive way to interact with the Unirate currency conversion service.

## Installation

```bash
pip install unirate-api
```

## Quick Start

```python
from unirate import UnirateClient

# Initialize the client
client = UnirateClient(api_key="your-api-key")

# Get current exchange rate
rate = client.get_rate("USD", "EUR")
print(f"Current USD to EUR rate: {rate}")

# Convert amount
converted = client.convert(amount=100, from_currency="USD", to_currency="EUR")
print(f"100 USD = {converted} EUR")

# Get supported currencies
currencies = client.get_supported_currencies()
print("Supported currencies:", currencies)
```

## Features

- Simple and intuitive API
- Real-time currency conversion
- Support for multiple currency pairs
- Comprehensive error handling

## Documentation

For detailed documentation, please visit our [documentation site](https://unirateapi.com/apidocs/).

## Authentication

To use this client, you'll need an API key. You can obtain one by registering at [Unirate](https://unirateapi.com).

## Error Handling

The client includes comprehensive error handling:

```python
from unirate.exceptions import UnirateError

try:
    rate = client.get_rate("INVALID", "EUR")
except UnirateError as e:
    print(f"An error occurred: {e}")
```

## Available Methods

### Get Exchange Rate
```python
rate = client.get_rate("USD", "EUR")
```

### Convert Amount
```python
converted = client.convert(100, "USD", "EUR")
```

### Get Supported Currencies
```python
currencies = client.get_supported_currencies()
```