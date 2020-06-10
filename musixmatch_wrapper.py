import requests
import constants

track_search_base_url = "https://api.musixmatch.com/ws/1.1/track.search"
lyrics_search_base_url = 'https://api.musixmatch.com/ws/1.1/track.lyrics.get'


def fetch_lyrics(song, artist):
    track_id = get_song_id(artist, song)
    return get_lyrics_from_song_id(track_id)


def get_lyrics_from_song_id(track_id):
    lyrics_params = {
        'track_id': track_id,
        'apikey': constants.API_KEY}
    lyrics_response = requests.get(lyrics_search_base_url, params=lyrics_params)
    try:
        lyrics = lyrics_response.json()['message']['body']['lyrics']['lyrics_body']
    except:
        lyrics = "Nothing Found "
    return lyrics


def get_song_id(artist, song):
    params = {
        'q_track': song,
        'q_artist': artist,
        'f_lyrics_language': 'en',
        's_artist_rating': 'desc',
        's_track_rating': 'desc',
        'apikey': constants.API_KEY
    }
    song_info = requests.get(track_search_base_url, params=params)
    try:
        track_id = song_info.json()['message']['body']['track_list'][0]['track']['track_id']
    except:
        track_id = 0
    return track_id
