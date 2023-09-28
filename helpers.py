import os
import requests


def lookup(symbol):

    api_key = os.environ.get("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    # Contact External API
    try:
        url = "https://www.alphavantage.co/query"

        querystring = {
                       "function": "GLOBAL_QUOTE",
                       "symbol": f"{symbol}",
                       "datatype": "json",
                       "output_size": "compact",
                       "apikey": f"{api_key}"}

        response = requests.get(url, params=querystring)

        return response.json()

    except requests.RequestException:
        return None


