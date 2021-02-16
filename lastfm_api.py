import pylast

# TODO: implement input via console.

# can be retrieved here: https://www.last.fm/api/accounts
API_KEY = ''
API_SECRET = ''

username = ''
# use of real password somehow.
password_hash = pylast.md5('')

network = pylast.LastFMNetwork(
    api_key = API_KEY,
    api_secret = API_SECRET,
    username = username,
    password_hash = password_hash
)

user = network.get_user(username)

library = pylast.Library(user, network)

my_followed_artists = library.get_artists(limit=None)
my_followed_artists = [artist for artist in my_followed_artists if artist.playcount < 5]

[print(artist.item, 'playcount: ', artist.playcount) for artist in my_followed_artists]
