import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from src.srt_creator import clean_lyrics

class TestSrtCreator(unittest.TestCase):
    def test_clean_lyrics(self):
        raw_lyrics = """
        Contributor: John Doe
        Lyrics by: Jane Doe

        Verse 1
        Some lyrics here

        Chorus
        Some more lyrics here

        Embed: http://example.com
        """
        cleaned = clean_lyrics(raw_lyrics)
        expected = "Verse 1\nSome lyrics here\n\nChorus\nSome more lyrics here"
        self.assertEqual(cleaned, expected)

if __name__ == "__main__":
    unittest.main()
