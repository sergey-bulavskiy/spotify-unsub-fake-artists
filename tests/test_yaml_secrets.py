import unittest
from spotify_unsub_fake_artists import secrets_helpers


class MyTestCase(unittest.TestCase):
    def test_something(self):
        yaml_content = ("""
        spotify:
            client_id: 'some_client_id'
            client_secret: 'some_client_secret'
        lastfm:
            api_key: 'some_api_key'
            api_secret: 'some_api_secret'
        """)

        client_id, client_secret = secrets_helpers.read_spotify_secrets_from_yaml(yaml_content)
        self.assertEqual('some_client_id', client_id)
        self.assertEqual('some_client_secret', client_secret)

        #TODO add some negative tests


if __name__ == '__main__':
    unittest.main()
