from unirate import UnirateClient

def main():
    # Initialize the client with your API key
    client = UnirateClient('your-api-key-here')

    try:
        print('=== Basic Currency Operations ===')
        
        # Get current exchange rate
        rate = client.get_rate('USD', 'EUR')
        print(f'Current USD to EUR rate: {rate}')

        # Convert amount
        converted = client.convert(100, 'USD', 'EUR')
        print(f'100 USD = {converted} EUR')

        # Get supported currencies
        currencies = client.get_supported_currencies()
        print(f'Supported currencies: {", ".join(currencies[:10])}... ({len(currencies)} total)')

        print('\n=== Historical Data Operations ===')
        
        # Get historical rate for a specific date
        historical_rate = client.get_historical_rate('USD', 'EUR', '2024-01-01')
        print(f'USD to EUR rate on 2024-01-01: {historical_rate}')

        # Get all historical rates for a base currency on a specific date
        historical_rates = client.get_historical_rates('USD', '2024-01-01')
        print('USD rates on 2024-01-01:')
        for currency, rate in list(historical_rates.items())[:5]:
            print(f'  {currency}: {rate}')

        # Convert using historical rate
        historical_converted = client.convert_historical(100, 'USD', 'EUR', '2024-01-01')
        print(f'100 USD = {historical_converted} EUR (on 2024-01-01)')

        # Get time series data for a currency pair
        time_series = client.get_time_series('USD', 'EUR', '2024-01-01', '2024-01-07')
        print('USD to EUR time series (Jan 1-7, 2024):')
        for date, rate in time_series.items():
            print(f'  {date}: {rate}')

    except Exception as error:
        print(f'Error: {error}')

if __name__ == '__main__':
    main() 