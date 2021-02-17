import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyArtist(object):
    """ Class representing spotify artist objects. Not all fields presented. \n
        ref: https://developer.spotify.com/documentation/web-api/reference/#object-artistobject """

    def __init__(self, genres: list[str], id: str, name: str) -> None:
        self.genres = genres
        self.id = id
        self.name = name

spotify_client = None

def authenticate(client_id, client_secret):
    """ Should be called before all other interactions with api."""
    global spotify_client
    spotify_client = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                               client_secret=client_secret,
                                                               redirect_uri="https://spotify.com",
                                                               open_browser=False,
                                                               scope='user-follow-read'))


def get_user_followed_artists():
    """ Downloads all artists followed by current user """

    # TODO: check that api is authenticated somehow.
    if (spotify_client is None):
        raise Exception(
            'Spotify client is not authenticated, please call .authenticate with correctly specified credentials')

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
