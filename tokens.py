from dotenv import load_dotenv
from os import getenv
import requests
from urllib.parse import urlencode
import secrets
import string
import base64
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


# Retrieve credentials from .env file
load_dotenv()
CLIENT_ID = getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = getenv('SPOTIFY_CLIENT_SECRET')
PROFILE_EMAIL = getenv('SPOTIFY_PROFILE_EMAIL')
PROFILE_PASSWORD = getenv('SPOTIFY_PROFILE_PASSWORD')


def get_access_token():
    """
    Getting access token from Spotify which will allow us to query API.
        Step 1) Retrieve authorization code.
        Step 2) Get access token using authorization code and scope parameters.
    :return: access_token
    """

    # Step 1
    state = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(15))
    scope = 'playlist-read-private playlist-modify-private playlist-modify-public user-top-read user-library-modify ' \
            'user-library-read '
    params = {
        'grant_type': 'client_credentials',
        'client_id': getenv('SPOTIFY_CLIENT_ID'),
        'response_type': 'code',
        'redirect_uri': 'http://localhost:7777/callback',
        'state': state,
        'scope': scope
    }

    authorize_url = "https://accounts.spotify.com/authorize?" + urlencode(params)
    service = Service(executable_path="/opt/homebrew/Caskroom/chromedriver/112.0.5615.49/chromedriver")
    with webdriver.Chrome(service=service) as driver:
        driver.get(authorize_url)  # Opens Spotify login page for authorization
        my_current_url = driver.current_url  # Save URL to check for page redirect later
        login_username = driver.find_element(By.ID, 'login-username')
        login_password = driver.find_element(By.ID, 'login-password')
        login_button = driver.find_element(By.ID, 'login-button')
        login_username.send_keys(PROFILE_EMAIL)  # Enter Spotify email
        login_password.send_keys(PROFILE_PASSWORD)  # Enter Spotify password
        login_button.click()  # Click LOGIN button
        wait = WebDriverWait(driver, 10)
        wait.until(lambda d: d.current_url != my_current_url)  # Wait for current URL to change
        my_current_url = driver.current_url  # Grab URL after redirect (after clicking LOGIN button)
        # print(my_current_url)

    # Retrieve authorization code from redirect  URL
    beg = my_current_url.index('code') + 5
    end = my_current_url.rindex('&')
    code = my_current_url[beg:end]
    print('code: ', code)

    # Step 2
    base_url = 'https://accounts.spotify.com/api/token'
    encoded = base64.b64encode(CLIENT_ID.encode() + b':' + CLIENT_SECRET.encode()).decode("utf-8")
    headers = {'Authorization': f'Basic {encoded}',
               'Content-Type': 'application/x-www-form-urlencoded'
               }
    params = {'grant_type': 'authorization_code',
              'code': code,
              'redirect_uri': 'http://localhost:7777/callback'}

    r = requests.post(base_url,
                      headers=headers,
                      params=params)

    # print(r.json())

    return r.json()['access_token']


get_access_token()
