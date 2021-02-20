import pylast
from pylast import Artist


class LastfmClient(object):
    """ Represents Lastfm API client, using pylast to communicate with Lastfm API"""

    network: pylast.LastFMNetwork = None
    user: pylast.User = None
    library: pylast.Library = None

    def __init__(self, api_key, api_secret, username, plain_password):
        """ API Credentials can be retrieved here: https://www.last.fm/api/accounts """
        self.network = pylast.LastFMNetwork(
            api_key=api_key,
            api_secret=api_secret,
            username=username,
            password_hash=pylast.md5(plain_password)
        )

        self.user = self.network.get_user(username)
        self.library = pylast.Library(self.user, self.network)

    def get_users_followed_artists(self, limit: int = None) -> list[tuple[Artist, int]]:
        my_followed_artists = self.library.get_artists(limit=limit)

        return [(artist.item, artist.playcount) for artist in my_followed_artists]


if __name__ == "__main__":
    pass
