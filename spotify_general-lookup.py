import os
import requests
from pprint import pprint

# Assign environment variable values to local variables
CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'

# Request authorization token from Spotify by sending credentials
auth_response = requests.post(
    AUTH_URL,
    {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
)

auth_response_data = auth_response.json()
pprint(auth_response_data)

access_token = auth_response_data['access_token']

headers = {
    'Authorization': f'Bearer {access_token}'
}

# Base url for all Spotify API calls
BASE_URL = 'https://api.spotify.com/v1/'

track_id = ''

artist_id = '14YzutUdMwS9yTnI0IFBaD'

# Get artist album data from Spotify
r = requests.get(f'{BASE_URL}artists/{artist_id}/albums',
                 headers=headers,
                 params={'include_groups': 'album',
                         'limit': 50})
r = r.json()

print(r)

# GETting the albums returns, along with tracks
for alb in r['items']:
    # Print album information
    print(f"Title: {alb['name']}\nReleased: {alb['release_date']}\nType: {alb['type']}\nID: {alb['id']}\nTracks:")
    # Call to API to GET more album info by Album ID
    r2 = requests.get(f"{BASE_URL}albums/{alb['id']}",
                      headers=headers)
    r2 = r2.json()
    # Retrieve tracks from album info, and print them out
    tracks = r2['tracks']['items']
    for track in tracks:
        print(f"\t--{track['name']}")
    print()

