# Import necessary dependencies
import requests
import json
import os
import numpy as np
from pprint import pprint

# Access token from https://developer.spotify.com/console/get-current-user-top-artists-and-tracks
access_token = 'BQBWv5ISaHwxP_Ue8iM9hPfWRKZ4C7n5PXX3lFuD8Af8cq5HGlg4smdgz9u3HvrUMBo7m_56z91O6JwqUKbCPfbKdI7H8EenrX6K1bbNJF6toJu-zKTHP7fEevZZr7jsHZKsroLJ_qOsUIPjorVaRW_fmcJ_ZMPK_W3Om2nCQHKW6v4iNikro__-XPkB3RgfApSaQbOwpXVTPB7tKB1MSdC9iVblpsOBdysXB_aBDbNzHA'

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
