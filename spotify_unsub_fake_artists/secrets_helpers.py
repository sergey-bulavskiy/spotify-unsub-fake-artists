import sys
import getopt
import yaml


def read_secrets_from_yaml(yaml_content, root_node_name, id_key_name, secret_key_name):
    """ Reads yaml_content and searches for root node, and two child nodes inside.
        Simple and stupid, but does the job. """

    """
    Altough name of yaml file is hardcoded, highly unlikely that this script will contain
    any other yaml files.
    """
    api_secrets_yaml_string = 'Error occured while reading api_secrets.yaml file:'
    correct_yaml_structure_string = (""" Correct structure of api_secrets.py file is: 
            spotify:
                client_id: '<client_id>'
                client_secret: '<client_secret>'
            lastfm:
                api_key: '<api_key>'
                api_secret: '<api_secret>'
            """)

    def try_get(yaml_node, node_name):
        if node_name not in yaml_node:
            print(f'Node {node_name} could not be found in yaml')
            sys.exit(2)
        return yaml_node.get(node_name)

    secrets = yaml.load(yaml_content, Loader=yaml.BaseLoader)

    if secrets is None:
        print(api_secrets_yaml_string)
        print('Seems like yaml file is empty or not yaml.')
        print(correct_yaml_structure_string)
        sys.exit(2)

    base_node = try_get(secrets, root_node_name)
    id_key = try_get(base_node, id_key_name)
    secret_key = try_get(base_node, secret_key_name)
    return id_key, secret_key


def read_lastfm_secrets_from_yaml(yaml_content):
    return read_secrets_from_yaml(yaml_content, 'lastfm', 'api_key', 'api_secret')


def read_spotify_secrets_from_yaml(yaml_content):
    return read_secrets_from_yaml(yaml_content, 'spotify', 'client_id', 'client_secret')


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
        elif opt in (f"-{CONST_USERNAME_SHORT}", f"--{CONST_USERNAME_LONG}"):
            lastfm_username = arg
        elif opt in (f"-{CONST_PASSWORD_SHORT}", f"--{CONST_PASSWORD_LONG}"):
            lastfm_password = arg

    if lastfm_username == '' or lastfm_password == '':
        exit_with_help_message()

    return lastfm_username, lastfm_password


if __name__ == "__main__":
    parse_lastfm_credentials_from_args(sys.argv[1:])
