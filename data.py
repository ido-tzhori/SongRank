import requests
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret =os.getenv("CLIENT_SECRET")

def get_access_token(client_id, client_secret):
    # Define the endpoint
    token_url = 'https://accounts.spotify.com/api/token'
    # Define the headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    # Define the payload
    payload = {
        'grant_type': 'client_credentials',
    }
    # Create a tuple of the client ID and secret
    client_creds = (client_id, client_secret)
    # Make the POST request
    response = requests.post(token_url, headers=headers, data=payload, auth=client_creds)
    # Check if the request was successful
    if response.status_code != 200:
        print("Error:", response.json())
        return None

    # Return the access token
    token_data = response.json()
    return token_data['access_token']

access_token = get_access_token(client_id, client_secret)
print("Access Token:", access_token)


