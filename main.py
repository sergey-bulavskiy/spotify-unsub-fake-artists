import spotify_api


def ask_input(param_name):
    """ Simple function that asks user for input of specific parameter. """

    print('Enter ' + param_name + ':')
    return input(param_name + ': ')


def retrieve_credentials():
    """ Function that retrieves client credentials """
    client_id = ask_input('client_id')
    client_secret = ask_input('client_secret')
    return client_id, client_secret


def main():
    # TODO: Move to script args parameters
    client_id, client_secret = retrieve_credentials()

    spotify_api.authenticate(client_id=client_id, client_secret=client_secret)
    artists = spotify_api.get_user_followed_artists()

    # Careful, it will print out all 2k artists that you have.
    [print(a.id, a.name, a.genres) for a in artists]


if __name__ == "__main__":
    main()
