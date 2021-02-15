import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyArtist(object):
    """ Class representing spotify artist objects. Not all fields presented. \n
        ref: https://developer.spotify.com/documentation/web-api/reference/#object-artistobject """

    def __init__(self, genres: list[str], id: str, name: str) -> None:
        self.genres = genres
        self.id = id
        self.name = name


def ask_input(param_name):
    """ Simple function that asks user for input of specific parameter. """

    print('Enter ' + param_name + ':')
    return input(param_name + ': ')


def retrieve_credentials():
    """ Function that retrieves client credentials """
    client_id = ask_input('client_id')
    client_secret = ask_input('client_secret')
    return client_id, client_secret


client_id, client_secret = retrieve_credentials()
spotify_client = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                           client_secret=client_secret,
                                                           redirect_uri="https://spotify.com",
                                                           open_browser=False,
                                                           scope='user-follow-read'))


def get_user_followed_artists():
    """ Downloads all artists followed by current user """

    spotify_artists = []
    response = spotify_client.current_user_followed_artists(50)['artists']

    while response['next']:
        spotify_artists.extend(map(
            lambda json_artist:
            SpotifyArtist(
                json_artist["genres"],
                json_artist["id"],
                json_artist["name"]),
                response['items']))

        response = spotify_client.next(response)['artists']

    return spotify_artists


artists = get_user_followed_artists()

# Careful, it will print out all 2k artists that you have!!!
[print(a.id, a.name, a.genres) for a in artists]
