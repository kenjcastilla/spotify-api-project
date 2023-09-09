from tokens import get_access_token
from playlist_functions import get_top_tracks, get_playlist, remove_from_playlist, add_to_playlist, not_in_new

token = ''
token = get_access_token()

get_top_tracks(token, 50)

old = get_playlist(token)

remove_from_playlist(token)
#
add_to_playlist(token)
#
new = get_playlist(token)
#
not_in_new(old, new)
