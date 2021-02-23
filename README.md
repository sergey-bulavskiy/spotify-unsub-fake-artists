# spotify-unsub-fake-artists
Script should unsub from artists that have been listened quite a few times, or have not been listened at all. 

For Spotify API communication library spotipy was used. (https://github.com/plamere/spotipy)
For Lastfm API communication, pylast was used. (https://github.com/pylast/pylast)

1. Authenticate in spotify.
2. Authenticate in lastfm.
3. Retrieve all followed artists from spotify (https://developer.spotify.com/documentation/web-api/reference/follow/get-followed/)
4. Retrieve all artists from last.fm library and filter out all that have > 10 playcount. (https://www.last.fm/api/show/library.getArtists)
5. Map rest of the artists to spotify ids. (additionally check that if artist does not have any history on lastfm, probably it should be unfollowed, as right now everything listened on spotify is being scrobbled)
6. Unsub all of them via spotify api. (https://developer.spotify.com/documentation/web-api/reference/follow/unfollow-artists-users/)


Spotify and Lastfm API credentials (ids and secrets should be specified in [api_secrets.yaml](https://github.com/sergey-bulavskiy/spotify-unsub-fake-artists/blob/main/api_secrets.yaml)).

Script could be ran with `py (in case of python3) main.py -u <lastfm_username> -p <lastfm_password>`
