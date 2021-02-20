import secrets_helpers
import sys
from pylast import Artist as LastfmArtist
from spotify_api import SpotifyClient, SpotifyArtist
from lastfm_api import LastfmClient


def intersect_spotify_lastfm_artists(spotify_artists: list[SpotifyArtist],
                                     lastfm_artists: list[LastfmArtist]) -> list[SpotifyArtist]:
    lastfm_artist_names = [artist.name for artist in lastfm_artists]
    return [artist for artist in spotify_artists if artist.name in lastfm_artist_names]


def main():
    yaml_content = open('../api_secrets.yaml').read()
    client_id, client_secret = secrets_helpers.read_spotify_secrets_from_yaml(yaml_content)
    lastfm_username, lastfm_password = secrets_helpers.parse_lastfm_credentials_from_args(sys.argv[1:])
    lastfm_api_key, lastfm_api_secret = secrets_helpers.read_lastfm_secrets_from_yaml(yaml_content)

    lastfm_client = LastfmClient(lastfm_api_key, lastfm_api_secret, lastfm_username, lastfm_password)
    spotify_client = SpotifyClient(client_id, client_secret)

    spotify_artists = spotify_client.get_user_followed_artists()
    # Might take a while without setting limit.
    lastfm_artists = lastfm_client.get_users_followed_artists()

    filtered_lastfm_artists = [artist for artist, playcount in lastfm_artists if playcount < 15]

    spotify_artists_filtered_by_playcount = intersect_spotify_lastfm_artists(spotify_artists,
                                                                             filtered_lastfm_artists)

    ids_to_unfollow = [artist.id for artist in spotify_artists_filtered_by_playcount]
    ids_chunked = [ids_to_unfollow[i:i + 50] for i in range(0, len(ids_to_unfollow), 50)]

    # If we send all hundreds of ids to spotify client, it will
    # fall due to TooManyRequests.
    for chunk in ids_chunked:
        spotify_client.unfollow_artists(chunk)


if __name__ == "__main__":
    main()
