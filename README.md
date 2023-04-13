# Spotify API Project
Utilizing Spotify's API to gain insight on habits, analyze data, and practice querying APIs.

WARNING: If you don't have a Spotify account, then cloning and running won't work the way you want it to. You can still observe findings in the notebooks, but you need your own Spotify credentials to play around with the functions in the .py files. I used environment variables for my credentials (as seen in [playlist_functions.py](playlist_functions.py) and [general-lookup.py](general-lookup.py)).

To use:

1. **Add a .env file** with environment variables SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_PROFILE_EMAIL, SPOTIFY_PROFILE_PASSWORD, SPOTIFY_PROFILE_USERNAME, and TOP_TRACKS_PLAYLIST. **This is mandatory for the functionality of the project.**

2. Run [main.py](main.py). Comment out whichever functions you don't want to use.

3. Observe [track-habits.ipynb](track-habits.ipynb), and run all cells 


Be sure to check your own Spotify library to see the changes if you update your playlist of top tracks!
