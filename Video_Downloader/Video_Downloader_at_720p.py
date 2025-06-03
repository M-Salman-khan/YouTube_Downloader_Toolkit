from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
import sys
import os
import re

# Get video URL from user input
try:
    video_url = input("Enter Video URL: ")
    ydl_opts = {'quiet': True}
    with YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=False)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

# Print minimal video information
print("Video Title   : {}\nChannel Name  : {}".format(video_info['title'], video_info['uploader']))

# Create a directory to save the video
video_dir = "Downloaded_Videos"
if not os.path.exists(video_dir):
    os.makedirs(video_dir)

# Sanitize title to avoid issues with special characters
safe_title = re.sub(r'[\\/*?:"<>|]', "_", video_info['title'])

# Define the downloader function for 720p resolution
def download_video(video_url, title):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Select the best 720p video and audio
        'merge_output_format': 'mp4',  # Ensure the output format is mp4 after merging video and audio
        'quiet': True,  # Suppress unnecessary output
        'outtmpl': os.path.join(video_dir, f"{safe_title}.%(ext)s"),
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print(f"Downloading: {safe_title}")
    except DownloadError as e:
        print(f"Failed to download {video_url}: {e}")

# Download the video
download_video(video_url, safe_title)

print("Download completed.")
