def get_rates():
    import requests

    params = (("apikey", "b72675e0-620f-11ec-9f73-1723fd0ed4bc"),)
    response = requests.get(
        "https://freecurrencyapi.net/api/v2/latest", params=params
    )
    return response
