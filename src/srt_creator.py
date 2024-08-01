import re
from datetime import timedelta

def seconds_to_srt_time(seconds):
    """
    Convert seconds to SRT time format (HH:MM:SS,MS).
    Args:
        seconds (float): The time in seconds.
    Returns:
        str: The time formatted for SRT (HH:MM:SS,MS).
    """
    milliseconds = int((seconds - int(seconds)) * 1000)
    time_str = str(timedelta(seconds=int(seconds)))
    if len(time_str) < 8:
        time_str = '0' * (8 - len(time_str)) + time_str
    return f"{time_str},{milliseconds:03}"

def clean_lyrics(lyrics):
    """
    Clean the lyrics by removing unwanted lines and trimming extra spaces.
    Args:
        lyrics (str): Raw lyrics of the song.
    Returns:
        str: Cleaned lyrics.
    """
    cleaned_lines = []
    for line in lyrics.split('\n'):
        if any(keyword in line for keyword in ["Contributor", "Lyrics", "Embed"]):
            continue
        if len(line.strip()) > 0:
            cleaned_lines.append(line.strip())
    cleaned_lyrics = '\n'.join(cleaned_lines)
    return cleaned_lyrics

def convert_lyrics_to_srt(lyrics_with_timestamps):
    """
    Convert lyrics with timestamps to SRT format.
    Args:
        lyrics_with_timestamps (list of tuples): List of tuples with (start_time, end_time, line).
    Returns:
        str: SRT formatted string.
    """
    if not lyrics_with_timestamps:
        return "No lyrics provided."

    srt_content = ""
    for i, (start_time, end_time, line) in enumerate(lyrics_with_timestamps):
        srt_content += f"{i + 1}\n"
        srt_content += f"{seconds_to_srt_time(start_time)} --> {seconds_to_srt_time(end_time)}\n"
        srt_content += f"{line.strip()}\n\n"

    return srt_content

