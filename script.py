from typing import List
import spotipy
from spotipy import client
from spotipy.oauth2 import SpotifyOAuth


class SpotifyArtist(object):
    """ Class representing spotify artist objects. Not all fields presented. \n
        ref: https://developer.spotify.com/documentation/web-api/reference/#object-artistobject """

    def __init__(self, genres: list[str], id: str, name: str) -> None:
        self.genres = genres
        self.id = id
        self.name = name


# Simple function that asks user for input of specific parameter.
def ask_input(param_name):
    print('Enter ' + param_name + ':')
    return input(param_name + ': ')

# Function that retrieves client credentials


def retrieve_credentials():
    client_id = ask_input('client_id')
    client_secret = ask_input('client_secret')
    return client_id, client_secret


client_id, client_secret = retrieve_credentials()

# TODO: Add check that token is expired, and then - authenticate.
spotify_client = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                           client_secret=client_secret,
                                                           redirect_uri="https://spotify.com",
                                                           open_browser=False,
                                                           scope='user-follow-read'))


resp = spotify_client.current_user_followed_artists(50)

# TODO: Move to methods and add handling of paging.
spotify_followed_artists = []
for artist in resp["artists"]["items"]:
    spotify_followed_artists.append(
        SpotifyArtist(artist["genres"],
                      artist["id"],
                      artist["name"]))

[print(a.id, a.name, a.genres) for a in spotify_followed_artists]
