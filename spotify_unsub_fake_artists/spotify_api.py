import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyArtist(object):
    """ Class representing spotify artist objects. Not all fields presented. \n
        ref: https://developer.spotify.com/documentation/web-api/reference/#object-artistobject """

    def __init__(self, genres: list[str], id: str, name: str) -> None:
        self.genres = genres
        self.id = id
        self.name = name


class SpotifyClient(object):
    """ Represents spotify API client, using spotipy to communicate with Spotify API. """

    spotify_client: spotipy.Spotify = None

    def __init__(self, client_id: str, client_secret: str):
        """ Should be called before all other interactions with api. """
        self.spotify_client = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                                        client_secret=client_secret,
                                                                        redirect_uri="https://spotify.com",
                                                                        open_browser=False,
                                                                        scope='user-follow-read'))

    def get_user_followed_artists(self):
        """ Downloads all artists followed by current user. """

        spotify_artists = []
        response = self.spotify_client.current_user_followed_artists(50)['artists']

        while response['next']:
            spotify_artists.extend(map(
                lambda json_artist:
                SpotifyArtist(
                    json_artist["genres"],
                    json_artist["id"],
                    json_artist["name"]),
                response['items']))

            response = self.spotify_client.next(response)['artists']
        return spotify_artists

    def unfollow_artists(self, ids: list[str]):
        """ Unfollow artists with given ids. """
        self.spotify_client.user_unfollow_artists(ids)


if __name__ == "__main__":
    pass
