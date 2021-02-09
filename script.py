import requests, base64
from requests.auth import HTTPBasicAuth

# Simple function that asks user for input of specific parameter.
def ask_input(param_name):
    print('Enter ' + param_name + ':')
    return input(param_name + ': ')

# Function that retrieves client credentials 
def retrieve_credentials():
    client_id = ask_input('client_id')
    client_secret = ask_input('client_secret')
    return client_id, client_secret

# Function that asks for user credentials and then retrieves access token.
def request_access_token():
    payload = {'grant_type': 'client_credentials'}
    client_id, client_secret = retrieve_credentials()
    response = requests.post('https://accounts.spotify.com/api/token',
                auth=HTTPBasicAuth(client_id, client_secret),
                data=payload)
    return response.json().access_token


token = request_access_token()
