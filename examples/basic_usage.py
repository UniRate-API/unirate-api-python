from unirate import UnirateClient

def main():
    # Initialize the client with your API key
    client = UnirateClient('your-api-key-here')

    try:
        print('=== Basic Currency Operations ===')
        
        # Get current exchange rate
        rate = client.get_rate('USD', 'EUR')
        print(f'Current USD to EUR rate: {rate}')
        
        # Get all rates for a base currency
        all_rates = client.get_rate('USD')
        print(f'USD rates for all currencies (showing first 5):')
        for currency, rate in list(all_rates.items())[:5]:
            print(f'  {currency}: {rate}')

        # Convert amount (note: to_currency is now first parameter)
        converted = client.convert('EUR', 100, 'USD')
        print(f'100 USD = {converted} EUR')

        # Get supported currencies
        currencies = client.get_supported_currencies()
        print(f'Supported currencies: {", ".join(currencies[:10])}... ({len(currencies)} total)')

        print('\n=== Historical Data Operations ===')
        
        # Get historical rate for a specific date
        historical_rate = client.get_historical_rate('2024-01-01', from_currency='USD', to_currency='EUR')
        print(f'USD to EUR rate on 2024-01-01: {historical_rate}')

        # Get all historical rates for a base currency on a specific date
        historical_rates = client.get_historical_rates('2024-01-01', base_currency='USD')
        print('USD rates on 2024-01-01 (showing first 5):')
        for currency, rate in list(historical_rates.items())[:5]:
            print(f'  {currency}: {rate}')

        # Convert using historical rate
        historical_converted = client.convert_historical(100, 'USD', 'EUR', '2024-01-01')
        print(f'100 USD = {historical_converted} EUR (on 2024-01-01)')

        # Get time series data for multiple currencies
        time_series = client.get_time_series('2024-01-01', '2024-01-07', 
                                           base_currency='USD', 
                                           currencies=['EUR', 'GBP'])
        print('USD time series (Jan 1-7, 2024):')
        for date, rates in list(time_series.items())[:3]:
            print(f'  {date}: EUR={rates.get("EUR", "N/A")}, GBP={rates.get("GBP", "N/A")}')

        print('\n=== New Features ===')
        
        # Get historical data limits
        limits = client.get_historical_limits()
        print('Historical data limits:')
        print(f'  Total currencies: {limits.get("total_currencies", "N/A")}')
        if 'currencies' in limits:
            for currency, info in list(limits['currencies'].items())[:3]:
                print(f'  {currency}: {info.get("earliest_date", "N/A")} to {info.get("latest_date", "N/A")}')

        # Get VAT rates for all countries
        vat_rates = client.get_vat_rates()
        print(f'VAT rates for all countries (total: {vat_rates.get("total_countries", "N/A")}):')
        if 'vat_rates' in vat_rates:
            for country, info in list(vat_rates['vat_rates'].items())[:5]:
                print(f'  {info.get("country_name", country)}: {info.get("vat_rate", "N/A")}%')

        # Get VAT rate for a specific country
        germany_vat = client.get_vat_rates('DE')
        if 'vat_data' in germany_vat:
            vat_info = germany_vat['vat_data']
            print(f'Germany VAT rate: {vat_info.get("vat_rate", "N/A")}%')

        print('\n=== Format Examples ===')
        
        # Get rates in CSV format
        csv_rates = client.get_rate('USD', 'EUR', format='csv')
        print('CSV format example:')
        print(csv_rates[:100] + '...' if len(csv_rates) > 100 else csv_rates)
        
        # Get currencies in XML format
        xml_currencies = client.get_supported_currencies(format='xml')
        print('XML format example:')
        print(xml_currencies[:100] + '...' if len(xml_currencies) > 100 else xml_currencies)

    except Exception as error:
        print(f'Error: {error}')

if __name__ == '__main__':
    main() 