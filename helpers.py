import os
import requests


def lookup(symbol):

    # Contact External API
    try:
        api_key = os.environ.get("API_KEY")
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

    # Parse the response
    # try:
    #     quote = response.json()
    #     # symbol = quote
    #     # price = quote[]
    #     return {
    #         "name": quote["name"],
    #         "status": quote["status"]
    #     }
    #
    # except (KeyError, TypeError, ValueError):
    #     return None
