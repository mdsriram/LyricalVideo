import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


import unittest
import os
from unittest.mock import patch
from src.create_video import create_video

class TestCreateVideo(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.input_video = "input_video/sample_video.mp4"
        cls.srt_file = "synced_lyrics.srt"
        cls.output_video = "output_video/test_output_video.mp4"
        
        # Create dummy video and SRT files for testing
        os.makedirs('input_video', exist_ok=True)
        os.makedirs('output_video', exist_ok=True)
        
        with open(cls.input_video, 'wb') as f:
            f.write(b'\0')  # Create a dummy binary file
        
        with open(cls.srt_file, 'w', encoding='utf-8') as f:
            f.write("1\n00:00:00,000 --> 00:00:05,000\nTest subtitle\n")
    
    @patch('subprocess.run')
    def test_create_video(self, mock_subprocess):
        mock_subprocess.return_value = None  # Mock successful execution
         #Call the function to test
        create_video(self.input_video, self.srt_file, self.output_video)
        
        # Check if subprocess.run was called with the correct arguments
        expected_command = [
            'ffmpeg', 
            '-i', self.input_video, 
            '-vf', f'subtitles={self.srt_file}:force_style=\'FontName=Arial,FontSize=24\'', 
            '-c:v', 'libx264', 
            '-c:a', 'copy', 
            self.output_video
        ]
        mock_subprocess.assert_called_once_with(expected_command, check=True)
    
    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.input_video):
            os.remove(cls.input_video)
        if os.path.exists(cls.srt_file):
            os.remove(cls.srt_file)
        if os.path.exists(cls.output_video):
                os.remove(cls.output_video)
        if os.path.isdir('input_video'):
            os.rmdir('input_video')
        if os.path.isdir('output_video'):
            os.rmdir('output_video')

if __name__ == "__main__":
    unittest.main()
