## LyricalVideo
LyricalVideo is a Python-based tool for creating lyrical videos by syncing lyrics with video content. This tool extracts lyrics, generates synchronized subtitle files in SRT format, and embeds these subtitles into a video using FFmpeg. It's designed to help users create engaging and interactive lyrical videos for music tracks.

## Features
- Lyrics Fetching: Retrieve lyrics for a given song using the Genius API.
- Subtitle Synchronization: Manually sync lyrics with timestamps and convert them into SRT format.
- Video Integration: Embed synchronized subtitles into video files using FFmpeg.

## Prerequisites
# Python
Ensure you have Python 3.6 or higher installed. Python is used to run the scripts and manage dependencies.
https://www.python.org/downloads/

# FFmpeg
FFmpeg is a powerful tool used for video and audio processing. It is essential for adding subtitles to videos and handling various video formats.Follow the FFmpeg installation guide for instructions.
# Installation 
1. Windows
- Download FFmpeg
   1. Go to the FFmpeg download page.
   2. Click on the "Windows" logo and download a build from one of the provided links (e.g., "Windows builds by BtbN").
- Extract the files
  Extract the downloaded ZIP file to a directory of your choice (e.g., C:\ffmpeg).
- Add FFmpeg to System PATH
  1. Open the Start Menu and search for "Environment Variables".
  2. Click on "Edit the system environment variables".
  3. In the System Properties window, click on "Environment Variables".
  4. Under "System variables", find and select the "Path" variable, then click "Edit".
  5.Click "New" and add the path to the bin directory of the FFmpeg folder (e.g., C:\ffmpeg\bin).
  6. Click "OK" to close all dialogs.
- Verify Installation
-Open Command Prompt and type ffmpeg -version to check if FFmpeg is installed correctly.

2. macOS
- Install Homebrew (if not already installed):
  Open Terminal and run
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

- Install FFmpeg
In Terminal, run
brew install ffmpeg

- Verify Installation
Type ffmpeg -version in Terminal to ensure FFmpeg is installed.

3. Linux
- Install FFmpeg via Package Manager
  For Debian-based systems (e.g., Ubuntu), run:
sudo apt update
sudo apt install ffmpeg

- For Red Hat-based systems (e.g., Fedora), run:
sudo dnf install ffmpeg

- Verify Installation
Run ffmpeg -version in your terminal to check the installation.

# LyricsGenius
This project uses the Genius API to fetch lyrics for songs. The Genius API provides access to a vast database of song lyrics and metadata. Below are the steps to set up and use the Genius API to retrieve lyrics.
1. Create a Genius Account
To use the Genius API, you first need a Genius account. If you don't already have one, sign up at Genius.
2. Obtain an API Access Token
- Create a Developer Account
   1. Visit the Genius API Developer page.
   2.  Log in with your Genius account credentials.
- Register Your Application
   1. Click on "Create an API Client" or "Register Your Application."
   2. Fill out the required details
      - Application Name: Enter a name for your application.
      - Application Website URL: Provide a URL for your application (a placeholder URL is acceptable if you don’t have one).
      - OAuth Redirect URI: Use http://localhost:8000 if you don't have a specific URI.
    3. After registering, you will receive an Access Token.
3. Configure Your Environment
- Create a .env File
-- In the root directory of your project, create a file named .env and add your GENIUS_TOKEN
4. Install Required Python Packages
- Ensure you have the necessary Python packages installed:
pip install lyricsgenius python-dotenv

## Usage
1. Prepare your lyrics and video
- Edit the main.py file to specify the song title, artist name, input video path, and output video path.
2. Run the script
  - Execute the following command in your terminal:

      ```bash
      python main.py

  - This will fetch lyrics, create a subtitle file, and generate a video with embedded lyrics.

## Files
- main.py: Main script for processing lyrics and video.
- fetch_lyrics.py: Module for fetching lyrics from the Genius API.
- lyrics_timestamps.py: Module for cleaning lyrics and converting them to SRT format.
- create_video.py: Module for integrating subtitles into the video using FFmpeg.
- .env: Environment file for storing API tokens and other configurations.
- requirements.txt: List of Python dependencies.
- testcases.txt: List of testcases for the project functions.Each test case includes:
     - Function Name: The name of the function being tested.
     - Test Case Number: A unique identifier for the test case.
     - Input: The input values used for the test.
     - Expected Output: The expected result from the function.
## How to Run Testcases
- Ensure you have the necessary dependencies installed.
- Check the testcases.txt file for the specific test cases and expected results.
- Manually test each function according to the cases described.

For automated testing, consider implementing a test suite in a testing framework like unittest or pytest, which will read these test cases and validate the functionality.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License
This project is licensed under the MIT License. 

