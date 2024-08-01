import lyricsgenius

def fetch_lyrics(song_title, artist_name, genius_token):
    genius = lyricsgenius.Genius(genius_token)
    song = genius.search_song(song_title, artist_name)
    return song.lyrics if song else None
