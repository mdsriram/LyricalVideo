import subprocess

def extract_audio_from_video(input_video, output_audio):
    command = [
        'ffmpeg',
        '-i', input_video,     # Input video file
        '-q:a', '0',           # Quality for audio
        '-map', 'a',           # Select audio stream
        output_audio           # Output audio file
    ]
    subprocess.run(command, check=True)

#input_video = r"C:\Desktop\Lyricalvideo\input_video.mp4"
#output_audio = r"C:\Desktop\Lyricalvideo\lyrical_audio.mp3"

##extract_audio_from_video(input_video, output_audio)
#