import secrets_helpers
import sys
import time
from spotify_api import SpotifyClient, SpotifyArtist
from lastfm_api import LastfmClient


def unsub_spotify_by_intersection_with_lastfm(lastfm_client, spotify_client, maximum_playcount):
    """ Function takes two lists of artists - spotify and lastfm ones, takes all spotify artists,
    which has less than 15 (including not-listened at all) artists and unsubs from them on spotify. """

    print('Downloading spotify artists...')
    start = time.perf_counter()
    spotify_artists: list[SpotifyArtist] = spotify_client.get_user_followed_artists()
    finish = time.perf_counter()
    print(f'Spotify artists downloaded in {finish - start:0.4f} seconds')

    # Might take a while without setting limit.
    print('Downloading lastfm artists, this may take a while.')
    start = time.perf_counter()
    lastfm_artists: dict[str, int] = lastfm_client.get_users_followed_artists()
    finish = time.perf_counter()
    print(f'Lastfm artists downloaded in {finish - start:0.4f} seconds')

    #TODO: Extract filtering part into external method and cover it with tests.
    artists_to_unfollow = [artist for artist in spotify_artists if
                           artist.name not in lastfm_artists
                           or lastfm_artists[artist.name] < maximum_playcount]
    print(f'Number of artists to unfollow: {len(artists_to_unfollow)}')
    answer = input('Continue ? (y - yes, any other symbol - no) ').strip()

    if answer == 'y':
        spotify_client.unfollow_spotify_artists(artists_to_unfollow)
    else:
        print('Exiting.')
        sys.exit()


def main():
    yaml_content = open('../api_secrets.yaml').read()
    client_id, client_secret = secrets_helpers.read_spotify_secrets_from_yaml(yaml_content)
    lastfm_username, lastfm_password = secrets_helpers.parse_lastfm_credentials_from_args(sys.argv[1:])
    lastfm_api_key, lastfm_api_secret = secrets_helpers.read_lastfm_secrets_from_yaml(yaml_content)

    lastfm_client = LastfmClient(lastfm_api_key, lastfm_api_secret, lastfm_username, lastfm_password)
    spotify_client = SpotifyClient(client_id, client_secret)

    unsub_spotify_by_intersection_with_lastfm(lastfm_client, spotify_client, maximum_playcount=15)


if __name__ == "__main__":
    main()
