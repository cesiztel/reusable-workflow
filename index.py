import requests


def get_transactions():
    url = "https://rfw8tqhtub.execute-api.eu-west-2.amazonaws.com/prod"
    endpoint = "/transactions"

    response = requests.get(url + endpoint)
    print(response.json())


get_transactions()
