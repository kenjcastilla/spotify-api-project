# Import necessary dependencies
import requests
import json
from dotenv import load_dotenv
from os import getenv
from pprint import pprint
from tokens import get_access_token

access_token = get_access_token()

load_dotenv()
SPOTIFY_USERNAME = getenv(SPOTIFY_PROFILE_USERNAME)

headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Base url for all Spotify API calls
BASE_URL = 'https://api.spotify.com/v1/'

# Create playlist
data = json.dumps({
                    'name': 'top tracks short-term',
                    'description': 'generated using python and spotify official api',
                    'public': False
})
r = requests.post(f'{BASE_URL}users/{SPOTIFY_USERNAME}/playlists',
                  data=data,
                  headers=headers,
                  )
r = r.json()

pprint(r)
