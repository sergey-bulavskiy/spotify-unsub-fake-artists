import unittest
from unittest import TestCase
from unittest.mock import patch
from spotify_unsub_fake_artists import secrets_helpers


class ReadSecretsFromYamlTests(TestCase):
    def test_read_correct_yaml_return_correct_values(self):
        yaml_content = ("""
        spotify:
            client_id: 'some_client_id'
            client_secret: 'some_client_secret'
        lastfm:
            api_key: 'some_api_key'
            api_secret: 'some_api_secret'
        """)

        client_id, client_secret = secrets_helpers.read_secrets_from_yaml(
            yaml_content, 'spotify', 'client_id', 'client_secret')

        self.assertEqual('some_client_id', client_id)
        self.assertEqual('some_client_secret', client_secret)

    def test_read_yaml_empty_file_raises_exit(self):
        yaml_content = """ """

        with self.assertRaises(SystemExit):
            secrets_helpers.read_secrets_from_yaml(
                yaml_content, 'spotify', 'client_id', 'client_secret')

    @patch('builtins.print')
    def test_read_yaml_root_node_not_found_raises_exit(self, mock_print):
        yaml_content = """         
                lastfm:
                    api_key: 'some_api_key'
                    api_secret: 'some_api_secret'
            """

        with self.assertRaises(SystemExit):
            secrets_helpers.read_secrets_from_yaml(
                yaml_content, 'spotify', 'client_id', 'client_secret')

        mock_print.assert_called_with('Node spotify could not be found in yaml')

    @patch('builtins.print')
    def test_read_yaml_child_node_not_found_raises_exit(self, mock_print):
        yaml_content = """         
                        lastfm:
                            api_secret: 'some_api_secret'
                    """
        with self.assertRaises(SystemExit):
            secrets_helpers.read_secrets_from_yaml(
                yaml_content, 'lastfm', 'api_key', 'api_secret')

        mock_print.assert_called_with('Node api_key could not be found in yaml')


if __name__ == '__main__':
    unittest.main()
