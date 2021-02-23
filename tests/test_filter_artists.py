from unittest import TestCase

from spotify_unsub_fake_artists.spotify_api import SpotifyArtist
from spotify_unsub_fake_artists.utils import filter_artists_to_unsub

bob_dylan = SpotifyArtist(name='Bob Dylan', spotify_id='')
mac_miller = SpotifyArtist(name='Mac Miller', spotify_id='')
spotify_artists = [bob_dylan, mac_miller]
lastfm_artists: dict[str, int] = {'Bob Dylan': 1, 'Mac Miller': 100}


class TestFilterArtists(TestCase):
    def test_empty_input_empty_output(self):
        result = filter_artists_to_unsub({}, [], 15)

        self.assertEqual(0, len(result))

    def test_spotify_artists_empty_returns_empty_list(self):
        result = filter_artists_to_unsub({'Bob Dylan': 1, 'Mac Miller': 100}, [], 15)

        self.assertEqual(0, len(result))

    def test_maximum_playcount_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as err:
            filter_artists_to_unsub(lastfm_artists, spotify_artists, 0)

    def test_filter_one_positive_case(self):
        result = filter_artists_to_unsub(lastfm_artists, spotify_artists, 15)

        self.assertEqual(1, len(result))
        self.assertTrue(bob_dylan in result)
        self.assertTrue(mac_miller not in result)

    def test_filter_all_cases_positive(self):
        result = filter_artists_to_unsub(lastfm_artists, spotify_artists, 100)

        self.assertEqual(2, len(result))
        self.assertTrue(bob_dylan in result)
        self.assertTrue(mac_miller in result)

    def test_spotify_artist_not_in_lastfm_returns_artist(self):
        result = filter_artists_to_unsub({}, spotify_artists, 1)

        self.assertEqual(2, len(result))
        self.assertTrue(bob_dylan in result)
        self.assertTrue(mac_miller in result)
