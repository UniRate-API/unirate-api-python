import requests
from typing import Dict, List, Union, Optional
from .exceptions import UnirateError

class UnirateClient:
    """
    Main client class for interacting with the Unirate API.
    """
    
    BASE_URL = "https://api.unirateapi.com"
    
    def __init__(
        self,
        api_key: str,
        timeout: int = 30
    ):
        """
        Initialize the Unirate client.

        Args:
            api_key (str): Your API key for authentication
            timeout (int, optional): Request timeout in seconds. Defaults to 30.
        """
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': f'unirate-python/{__import__("unirate").__version__}'
        })

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict] = None,
        json: Optional[Dict] = None
    ) -> Dict:
        """
        Make an HTTP request to the API.

        Args:
            method (str): HTTP method (GET, POST, etc.)
            endpoint (str): API endpoint
            params (dict, optional): Query parameters
            json (dict, optional): JSON body for POST requests

        Returns:
            dict: Response data

        Raises:
            UnirateError: If the API request fails
        """
        if params is None:
            params = {}
        
        # Add API key to all requests
        params['api_key'] = self.api_key

        try:
            response = self.session.request(
                method=method,
                url=f"{self.BASE_URL}/{endpoint.lstrip('/')}",
                params=params,
                json=json,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise UnirateError(f"API request failed: {str(e)}")

    def get_rate(
        self,
        from_currency: str,
        to_currency: str
    ) -> float:
        """
        Get the exchange rate between two currencies.

        Args:
            from_currency (str): Source currency code (e.g., "USD")
            to_currency (str): Target currency code (e.g., "EUR")

        Returns:
            float: Exchange rate

        Raises:
            UnirateError: If the request fails or currencies are invalid
        """
        params = {
            "from": from_currency.upper(),
            "to": to_currency.upper()
        }

        response = self._make_request("GET", "/api/rates", params=params)
        return float(response["rate"])

    def convert(
        self,
        amount: Union[int, float],
        from_currency: str,
        to_currency: str
    ) -> float:
        """
        Convert an amount from one currency to another.

        Args:
            amount (int or float): Amount to convert
            from_currency (str): Source currency code (e.g., "USD")
            to_currency (str): Target currency code (e.g., "EUR")

        Returns:
            float: Converted amount

        Raises:
            UnirateError: If the conversion fails
        """
        params = {
            "amount": amount,
            "from": from_currency.upper(),
            "to": to_currency.upper()
        }

        response = self._make_request("GET", "/api/convert", params=params)
        return float(response["result"])

    def get_supported_currencies(self) -> List[str]:
        """
        Get a list of supported currencies.

        Returns:
            list: List of currency codes

        Raises:
            UnirateError: If the request fails
        """
        response = self._make_request("GET", "/api/currencies")
        return response["currencies"] 