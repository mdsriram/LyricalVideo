import os
from dotenv import load_dotenv
from src.fetch_lyrics import fetch_lyrics
from src.srt_creator import clean_lyrics, convert_lyrics_to_srt
from src.create_video import create_video

# Load environment variables from .env file
load_dotenv()

# Access environment variables
genius_token = os.getenv('GENIUS_TOKEN')

def main(song_title, artist_name, genius_token, input_video, output_video):
    # Fetch lyrics
    lyrics = fetch_lyrics(song_title, artist_name, genius_token)
    if not lyrics:
        print("Lyrics not found.")
        return
    
    # Clean the lyrics
    cleaned_lyrics = clean_lyrics(lyrics)
    
    # Manually provide the timestamps for each line (start_time, end_time, line)
    lyrics_with_timestamps = [
        (0.00, 5.00, "Thumbi penne kothiyille neril kaanaan"),
        (5.00, 10.00, "Vanittunde en velipennu"),
        (10.00, 15.00, "Kavilathunde kannadi thundu"),
        (15.00, 20.00, "Chundathunde chingara chundu"),
        (20.00, 25.00, "Neela kaayalupol thonum omal kannanu"),
        (25.00, 30.00, "Mudi kaarmukilum tholkum naadan chelaanu"),
        (30.00, 35.00, "Konde poraam pennalle ponnona kaalathu"),
        (35.00, 40.00, "Kannum nenjum kannaale nee kaanum nerathu"),
        (40.00, 45.00, "Thanka thaamarapol poonthen chinthum nenjanu"),
        (45.00, 50.00, "Chella thaarakalum pennum pande koottaannu")
     
    ]

    # Convert lyrics to SRT format
    srt_content = convert_lyrics_to_srt(lyrics_with_timestamps) 
    srt_file = "synced_lyrics.srt"

    # Write SRT file with UTF-8 encoding
    with open(srt_file, 'w', encoding='utf-8') as file:
        file.write(srt_content)
    
    # Create video with lyrics
    create_video(input_video.replace("\\", "/"), srt_file.replace("\\", "/"), output_video.replace("\\", "/"))
    print(f"Video created: {output_video}")

if __name__ == "__main__":
    # Define your variables here or fetch from environment variables
    SONG_TITLE = "Thumbi Penne"
    ARTIST_NAME = "Siddharth Menon"
    INPUT_VIDEO = r"C:\Desktop\Lyricalvideo\input_video.mp4"
    OUTPUT_VIDEO = r"C:\Desktop\Lyricalvideo\lyrical_video_with_subs.mp4"
    
    # Check if the Genius token is available
    if genius_token is None:
        print("GENIUS_TOKEN is not set. Please check your .env file.")
    else:
        main(SONG_TITLE, ARTIST_NAME, genius_token, INPUT_VIDEO, OUTPUT_VIDEO)
