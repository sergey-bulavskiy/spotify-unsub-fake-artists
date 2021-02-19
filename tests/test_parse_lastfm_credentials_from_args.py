import unittest
from unittest import TestCase
from unittest.mock import patch
from spotify_unsub_fake_artists import secrets_helpers

expected_help_message = (
    f'usage: main.py  [-u | --username] <username>'
    f' [-p | --password] <password>'
    '\nScript requires lastfm credentials, both username and password is obligatory. '
    'please specify them like shown in usage above.')

expected_username = 'some_username'
expected_password = 'some_password'


class ParseLastfmCredentialsFromArgsTests(TestCase):
    def test_empty_args_system_exits_with_code_2(self):
        with self.assertRaises(SystemExit) as err:
            secrets_helpers.parse_lastfm_credentials_from_args([])
        self.assertEqual(err.exception.code, 2)

    @patch('builtins.print')
    def test_empty_args_prints_help_message(self, mock_print):
        with self.assertRaises(SystemExit):
            secrets_helpers.parse_lastfm_credentials_from_args([])
        mock_print.assert_called_with(expected_help_message)

    def test_help_arg_system_exits_without_error_code(self):
        with self.assertRaises(SystemExit) as err:
            secrets_helpers.parse_lastfm_credentials_from_args(['-h'])
        self.assertEqual(None, err.exception.code)

    # TODO research ways to make parametrized tests.
    @patch('builtins.print')
    def test_help_arg_prints_out_help_message(self, mock_print):
        with self.assertRaises(SystemExit):
            secrets_helpers.parse_lastfm_credentials_from_args(['-h'])
        mock_print.assert_called_with(expected_help_message)

    @patch('builtins.print')
    def test_password_missing_raises_prints_help(self, mock_print):
        with self.assertRaises(SystemExit):
            secrets_helpers.parse_lastfm_credentials_from_args(
                ['-u', 'usrname'])
        mock_print.assert_called_with(expected_help_message)

    @patch('builtins.print')
    def test_username_missing_raises_prints_help(self, mock_print):
        with self.assertRaises(SystemExit):
            secrets_helpers.parse_lastfm_credentials_from_args(['-p', 'pssw'])
        mock_print.assert_called_with(expected_help_message)

    def test_short_credentials_provided_correctly_returns(self):
        actual_username, actual_password = secrets_helpers. \
            parse_lastfm_credentials_from_args(["-u", f"{expected_username}",
                                                "-p", f"{expected_password}"])

        self.assertEqual(expected_username, actual_username)
        self.assertEqual(expected_password, actual_password)

    def test_long_credentials_provided_correctly_returns(self):
        actual_username, actual_password = secrets_helpers. \
            parse_lastfm_credentials_from_args(["--username", f"{expected_username}",
                                                "--password", f"{expected_password}"])

        self.assertEqual(expected_username, actual_username)
        self.assertEqual(expected_password, actual_password)


if __name__ == '__main__':
    unittest.main()
