import sys
import getopt


def parse_lastfm_credentials_from_args(argv):
    """ Function that parses input arguments, 
    and returns users name and password, 
    to authenticate on lastfm
    """

    CONST_USERNAME_SHORT = 'u'
    CONST_PASSWORD_SHORT = 'p'
    CONST_USERNAME_LONG = 'username'
    CONST_PASSWORD_LONG = 'password'
    lastfm_username = ''
    lastfm_password = ''
    help_string = (
        f'usage: main.py  [-{CONST_USERNAME_SHORT} | --{CONST_USERNAME_LONG}] <username>'
        f' [-{CONST_PASSWORD_SHORT} | --{CONST_PASSWORD_LONG}] <password>'
        '\nScript requires lastfm credentials, both username and password is obligatory. '
        'please specify them like shown in usage above.')

    def exit_with_help_message():
        print(help_string)
        sys.exit(2)

    try:
        opts, _ = getopt.getopt(argv, f'h{CONST_USERNAME_SHORT}:{CONST_PASSWORD_SHORT}:',
                                [f"{CONST_USERNAME_LONG}=", f"{CONST_PASSWORD_LONG}="])
    except getopt.GetoptError:
        exit_with_help_message()

    if len(opts) == 0:
        exit_with_help_message()

    for opt, arg in opts:
        if opt == '-h':
            print(help_string)
            sys.exit()
        elif opt in (f"-{CONST_USERNAME_SHORT}", f"-{CONST_USERNAME_LONG}"):
            lastfm_username = arg
        elif opt in (f"-{CONST_PASSWORD_SHORT}", f"-{CONST_PASSWORD_LONG}"):
            lastfm_password = arg

    if lastfm_password == '' or lastfm_password == '':
        exit_with_help_message()

    return lastfm_username, lastfm_password


if __name__ == "__main__":
    parse_lastfm_credentials_from_args(sys.argv[1:])
