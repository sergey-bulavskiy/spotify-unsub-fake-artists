import sys
import time
from spotify_api import SpotifyClient, SpotifyArtist
from lastfm_api import LastfmClient
import secrets_helpers
from spotify_unsub_fake_artists.utils import filter_artists_to_unsub

CONST_MAXIMUM_PLAYCOUNT = 15
""" Const that represents maximum playcount by which
 spotify artists should be filtered and unfollowed. """


def main():
    yaml_content = open('../api_secrets.yaml').read()
    client_id, client_secret = secrets_helpers.read_spotify_secrets_from_yaml(yaml_content)
    lastfm_username, lastfm_password = secrets_helpers.parse_lastfm_credentials_from_args(sys.argv[1:])
    lastfm_api_key, lastfm_api_secret = secrets_helpers.read_lastfm_secrets_from_yaml(yaml_content)

    lastfm_client = LastfmClient(lastfm_api_key, lastfm_api_secret, lastfm_username, lastfm_password)
    spotify_client = SpotifyClient(client_id, client_secret)

    print('Downloading spotify artists...')
    start = time.perf_counter()
    spotify_artists: list[SpotifyArtist] = spotify_client.get_user_followed_artists()
    finish = time.perf_counter()
    print(f'Spotify artists downloaded in {finish - start:0.4f} seconds')

    print('Downloading lastfm artists, this may take a while.')
    start = time.perf_counter()
    # Might take a while without setting limit.
    lastfm_artists: dict[str, int] = lastfm_client.get_users_followed_artists()
    finish = time.perf_counter()
    print(f'Lastfm artists downloaded in {finish - start:0.4f} seconds')

    artists_to_unfollow = filter_artists_to_unsub(lastfm_artists, spotify_artists, CONST_MAXIMUM_PLAYCOUNT)

    print(f'Number of artists to unfollow: {len(artists_to_unfollow)}')
    answer = input('Continue ? (y - yes, any other symbol - no) ').strip()

    if answer == 'y':
        spotify_client.unfollow_spotify_artists(artists_to_unfollow)
    else:
        print('Exiting.')
        sys.exit()


if __name__ == "__main__":
    main()
