import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from unittest.mock import patch, MagicMock
from src.fetch_lyrics import fetch_lyrics

class TestFetchLyrics(unittest.TestCase):

    @patch('lyricsgenius.Genius')
    def test_fetch_lyrics(self, MockGenius):
        # Create a mock Genius object and mock search_song method
        mock_genius = MockGenius.return_value
        mock_song = MagicMock()
        mock_song.lyrics = "Test lyrics"
        mock_genius.search_song.return_value = mock_song

        genius_token = "fake_token"
        song_title = "Test Song"
        artist_name = "Test Artist"
        
        lyrics = fetch_lyrics(song_title, artist_name, genius_token)
        self.assertEqual(lyrics, "Test lyrics")

    @patch('lyricsgenius.Genius')
    def test_fetch_lyrics_no_song(self, MockGenius):
        mock_genius = MockGenius.return_value
        mock_genius.search_song.return_value = None

        genius_token = "fake_token"
        song_title = "Nonexistent Song"
        artist_name = "Nonexistent Artist"
        
        lyrics = fetch_lyrics(song_title, artist_name, genius_token)
        self.assertIsNone(lyrics)

if __name__ == "__main__":
    unittest.main()
