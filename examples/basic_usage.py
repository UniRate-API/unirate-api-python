from unirate import UnirateClient, UnirateError

def main():
    # Initialize the client
    client = UnirateClient(api_key="your-api-key-here")

    try:
        # Get current exchange rate
        rate = client.get_rate("USD", "EUR")
        print(f"Current USD to EUR rate: {rate}")

        # Convert an amount
        amount = 100
        converted = client.convert(amount, "USD", "EUR")
        print(f"{amount} USD = {converted} EUR")

        # Get supported currencies
        currencies = client.get_supported_currencies()
        print("\nSupported currencies:", currencies)

    except UnirateError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 