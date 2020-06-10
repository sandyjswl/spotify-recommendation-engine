import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_songs_from_playlists(playlist_id):
    response = sp.playlist_tracks(playlist_id,
                                  offset=0,
                                  fields='items.track.id,total')
    return response['items']


def extracts_songs_info(songs_from_playlist):
    songs_list = []
    for song in songs_from_playlist:
        id = song['track']['id']
        res = sp.track(id)

        album_name = (res['album']['name'])
        artist_name = (res['album']['artists'][0]['name'])
        songs_name = (res['name'])
        songs_list.append((songs_name, artist_name, album_name))
        print(songs_name, artist_name, album_name)
    return songs_list


def fetch_songs_list(username):
    all_playlists = sp.user_playlists(username)
    playlist_uri = all_playlists['items'][0]['uri']
    songs_from_playlist = get_songs_from_playlists(playlist_uri)
    list_of_songs = extracts_songs_info(songs_from_playlist)
    return list_of_songs
