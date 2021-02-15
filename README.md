# spotify-unsub-fake-artists
Script should unsub from artists that have been listened to less than 10 times. 

For spotify API communication library spotipy was used. (https://github.com/plamere/spotipy)

1. Authenticate in spotify.
2. Retrieve all followed artists from spotify (https://developer.spotify.com/documentation/web-api/reference/follow/get-followed/)
3. Retrieve all artists from last.fm library and filter out all that have > 10 playcount. (https://www.last.fm/api/show/library.getArtists)
4. Map rest of the artists to spotify ids. 
5. Unsub all of them via spotify api. (https://developer.spotify.com/documentation/web-api/reference/follow/unfollow-artists-users/)
