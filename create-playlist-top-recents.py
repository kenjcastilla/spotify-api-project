# Import necessary dependencies
import requests
import json
import os
import numpy as np
from pprint import pprint
from tokens import token_top_tracks

# Access token from https://developer.spotify.com/console/get-current-user-top-artists-and-tracks
access_token = token_top_tracks

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
r = requests.post(f'{BASE_URL}users/kencastilla/playlists',
                  data=data,
                  headers=headers,
                  )
r = r.json()

pprint(r)

"""
tracks_id = []
pos = 1
# Add each track id to a list
for item in r['items']:
    track_id = item['id']
    tracks_id.append(track_id)
    pos+=1
"""
