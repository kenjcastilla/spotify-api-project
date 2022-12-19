import requests
import json
from tokens import token_remove_tracks, token_get_playlist, token_create, token_add_tracks, \
    token_top_artists, token_top_tracks
from pprint import pprint

# Base url for all Spotify API calls
BASE_URL = 'https://api.spotify.com/v1/'


# Get user's top tracks
def get_top_tracks(limit: int = 50):
    print('TOP TRACKS\n\n')
    headers = {
        'Authorization': f'Bearer {token_top_tracks}',
        'Content-Type': 'application/json',
    }
    r = requests.get(f'{BASE_URL}me/top/tracks',
                     headers=headers,
                     params={
                         'limit': limit,
                         'time_range': 'short_term',
                     })
    r = r.json()

    uris = []
    pos = 1
    for item in r['items']:
        track_name = item['name']
        uri = item['uri']
        uris.append(uri)
        artists = []
        for i in range(0, len(item['artists'])):
            artists.append(item['artists'][i]['name'])
        artist = "/".join(artists)
        album = item['album']['name']
        print(f'{pos})\n\tTrack: "{track_name}"\n\tArtist(s): {artist}\n\tAlbum: "{album}"\n\tURI: {uri}\n')
        _separate_section()
        pos += 1

    tracks = ','.join(uris)
    print(tracks, '\n')
    _separate_section()
    return uris


# Get playlist
def get_playlist():
    print('PLAYLIST\n')
    headers = {
        'Authorization': f'Bearer {token_get_playlist}',
        'Content-Type': 'application/json',
    }
    playlist_id = '5ZxRxpARcooxJGQHHu0gkB'
    query = f'{BASE_URL}playlists/{playlist_id}'
    r = requests.get(query,
                     headers=headers,
                     )
    r = r.json()
    #print(r, width=2)

    snapshot_id = r['snapshot_id']
    uris = []
    names = []
    pos = 1
    for item in r['tracks']['items']:
        #pprint(item, width=2)
        uri = item['track']['uri']
        uris.append(uri)
        name = item['track']['name']
        names.append(name)
        pos += 1

    tracks_uri = ','.join(uris)
    print(tracks_uri, '\n')
    _separate_section()

    return uris, names, snapshot_id


# Remove all tracks from playlist
def remove_from_playlist():
    print('REMOVE FROM PLAYLIST\n\n')
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token_remove_tracks}',
    }
    playlist_id = '5ZxRxpARcooxJGQHHu0gkB'

    url = f'{BASE_URL}playlists/{playlist_id}/tracks'

    playlist = get_playlist()
    tracks_uri = playlist[0]
    uris = []
    for uri in tracks_uri:
        uris.append({'uri': uri})
    snapshot_id = playlist[2]
    data = json.dumps({
        'tracks': uris,
        'snapshot_id': snapshot_id
    })
    pprint(data)
    r = requests.delete(url,
                        data=data,
                        headers=headers,
                        )
    r = r.json()
    print(r)


# Add user's top tracks to playlist
def add_to_playlist():
    playlist_id = '5ZxRxpARcooxJGQHHu0gkB'
    url = f'{BASE_URL}playlists/{playlist_id}/tracks'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token_add_tracks}',
        'Content-Length': '50',
    }
    data = json.dumps({'uris': get_top_tracks()})

    r = requests.post(url,
                      data=data,
                      headers=headers,
                      )
    r = r.json()
    print('ADD TO PLAYLIST\n')
    #print(r, '\n')

    _separate_section()


# Shows which tracks are no longer in playlist
def not_in_new(old, new):
    print('NO LONGER IN TOP RECENTS:\n\t')
    indices = []
    for uri in old[0]:
        if uri not in new[0]:
            i = indices.append(new[0].index(uri))
            print(f'\t{new[1][i]}\n')
    """for track in old:
        if track in new:
            print(f'{track}\n')"""
    _separate_section()


def _separate_section():
    """
    Separates console outputs by printing a dashed line
    """
    print('--------------------------------------------------------------------------------------\n')


