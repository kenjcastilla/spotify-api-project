import os
import requests
from pprint import pprint
from playlist_functions import _separate_section

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
#pprint(auth_response_data)

access_token = auth_response_data['access_token']

headers = {
    'Authorization': f'Bearer {access_token}'
}

# Base url for all Spotify API calls
BASE_URL = 'https://api.spotify.com/v1/'


def get_id():
    ta = input("Track or Artist? ")
    valid = ('track', '1', 'artist', '2')

    while ta.lower() not in valid:
        ta = input("Track or Artist? ")
    if ta in valid[0:2]:
        identifier = input("Enter Track ID here: ")
        # identifier = '7beF9ncmC9V1NzczO8pGvA'
        _get_track(identifier)
    else:
        identifier = input("Enter Artist ID here: ")
        # identifier = 14YzutUdMwS9yTnI0IFBaD
        _get_artist(identifier)


def _get_track(track_id):
    r = requests.get(f"{BASE_URL}tracks/{track_id}",
                     headers=headers)
    r = r.json()
    r2 = requests.get(f"{BASE_URL}audio-features",
                      headers=headers,
                      params={
                          'ids': track_id,
                      })
    r2 = r2.json()
    feats = r2['audio_features'][0]
    #pprint(r2)

    track_name = r['name']
    uri = r['uri']
    artists = []
    for i in range(0, len(r['artists'])):
        artists.append(r['artists'][i]['name'])
    artist = "/".join(artists)
    album = r['album']['name']
    popularity = r['popularity']
    tempo = feats['tempo']
    live = feats['liveness']
    time = feats['time_signature']
    print(f'Track: "{track_name}"\nArtist(s): {artist}\nAlbum: "{album}"\nURI: {uri}\nPopularity Score: {popularity}\n'
          f'Tempo: {tempo}\nLiveness: {live}\nTime Signature: {time}')

    print()
    _separate_section()


def _get_artist(artist_id):
    # GET artist album data from Spotify
    r = requests.get(f'{BASE_URL}artists/{artist_id}/albums',
                     headers=headers,
                     params={'include_groups': 'album',
                             'limit': 50})
    r = r.json()

    #print(r)

    # GETting the albums returns, along with tracks
    for alb in r['items']:
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

    _separate_section()


get_id()
while True:
    cont = input("Would you like to search again? (y/n) ")
    if cont.lower() in ['y', 'yes']:
        get_id()
    else:
        print("Thanks! Bye.")
        break
