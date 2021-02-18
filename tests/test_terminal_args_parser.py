import unittest
from unittest import TestCase
from unittest.mock import patch
from spotify_unsub_fake_artists import args_helpers

expected_help_message = (
    f'usage: main.py  [-u | --username] <username>'
    f' [-p | --password] <password>'
    '\nScript requires lastfm credentials, both username and password is obligatory. '
    'please specify them like shown in usage above.')


class ArgsHelpersTests(TestCase):
    def test_empty_args_system_exits_with_code_2(self):
        with self.assertRaises(SystemExit) as err:
            args_helpers.parse_lastfm_credentials_from_args([])
        self.assertEqual(err.exception.code, 2)

    @patch('builtins.print')
    def test_empty_args_prints_help_message(self, mock_print):
        with self.assertRaises(SystemExit):
            args_helpers.parse_lastfm_credentials_from_args([])
        mock_print.assert_called_with(expected_help_message)

    def test_help_arg_system_exits_without_error_code(self):
        with self.assertRaises(SystemExit) as err:
            args_helpers.parse_lastfm_credentials_from_args(['-h'])
        self.assertEqual(None, err.exception.code)

    @patch('builtins.print')
    def test_help_arg_prints_out_help_message(self, mock_print):
        with self.assertRaises(SystemExit):
            args_helpers.parse_lastfm_credentials_from_args(['-h'])
        mock_print.assert_called_with(expected_help_message)

    @patch('builtins.print')
    def test_username_missing_raises(self, mock_print):
        with self.assertRaises(SystemExit):
            args_helpers.parse_lastfm_credentials_from_args(['-u', 'usrname'])
        mock_print.assert_called_with(expected_help_message)

    @patch('builtins.print')
    def test_password_missing_raises(self, mock_print):
        with self.assertRaises(SystemExit):
            args_helpers.parse_lastfm_credentials_from_args(['-p', 'pssw'])
        mock_print.assert_called_with(expected_help_message)

    def test_credentials_provided_correctly_returns(self):
        expected_username = 'some_username'
        expected_password = 'some_password'

        actual_username, actual_password = args_helpers. \
            parse_lastfm_credentials_from_args(["-u", f"{expected_username}",
                                                "-p", f"{expected_password}"])

        self.assertEqual(expected_username, actual_username)
        self.assertEqual(expected_password, actual_password)

    #TODO: Add tests for long parameter names.


if __name__ == '__main__':
    unittest.main()
