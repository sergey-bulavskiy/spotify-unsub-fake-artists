import spotify_api, secrets_helpers


def main():
    yaml_content = open('../api_secrets.yaml').read()
    client_id, client_secret = secrets_helpers.read_spotify_secrets_from_yaml(yaml_content)

    spotify_api.authenticate(client_id=client_id, client_secret=client_secret)
    artists = spotify_api.get_user_followed_artists()

    # Careful, it will print out all 2k artists that you have.
    [print(a.id, a.name, a.genres) for a in artists]


if __name__ == "__main__":
    main()
