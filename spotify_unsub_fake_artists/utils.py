from spotify_unsub_fake_artists.spotify_api import SpotifyArtist


def filter_artists_to_unsub(lastfm_artists: dict[str, int],
                            spotify_artists: list[SpotifyArtist],
                            maximum_playcount: int) -> list[SpotifyArtist]:
    """ Returns spotify artists which has less than 15 (including not-listened at all) playcount at lastfm."""

    # Altough it is a pretty normal case, unfollowing all artists is not the goal.
    if maximum_playcount <= 0:
        raise ValueError(f'Maximum playcount has incorrect value: {maximum_playcount}')

    return [artist for artist in spotify_artists if
            artist.name not in lastfm_artists
            or lastfm_artists[artist.name] <= maximum_playcount]
