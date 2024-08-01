import subprocess

def create_video(input_video, srt_file, output_video):
    command = [
        'ffmpeg', 
        '-i', input_video, 
        '-vf', f'subtitles={srt_file}:force_style=\'FontName=Arial,FontSize=24\'', # Add subtitles
        '-c:v', 'libx264', 
        '-c:a', 'copy', 
        output_video
    ]
    subprocess.run(command, check=True)
