from spotify_wrapper import fetch_songs_list
from musixmatch_wrapper import fetch_lyrics
from pprint import pprint
if __name__ == '__main__':
    list_of_songs = fetch_songs_list('sandeepjswl123')
    for song_info in list_of_songs:
        lyrics = fetch_lyrics(song_info[0], song_info[1])
        pprint(lyrics)