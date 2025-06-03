from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
import sys
import os
import re

# Get playlist URL from user input
try:
    playlist_url = input("Enter Playlist URL: ")
    ydl_opts = {'extract_flat': True, 'quiet': True}
    with YoutubeDL(ydl_opts) as ydl:
        p = ydl.extract_info(playlist_url, download=False)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

# Print minimal playlist information
print("Playlist Name : {}\nChannel Name  : {}\nTotal Videos  : {}".format(p['title'], p['uploader'], len(p['entries'])))

# Create a directory with the playlist name
playlist_dir = re.sub(r'[\\/*?:"<>|]', "_", p['title'].strip().replace(" ", "_"))
if not os.path.exists(playlist_dir):
    os.makedirs(playlist_dir)

# Get video URLs and indices from the playlist
videos = []
try:
    for i, entry in enumerate(p['entries'], start=1):
        videos.append((i, entry['url'], entry['title']))
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

print("Downloading Started...\n")

# Define the downloader function for 720p resolution
def downloader(videos):
    for seq_num, url, title in videos:
        # Sanitize title to avoid issues with special characters
        safe_title = re.sub(r'[\\/*?:"<>|]', "_", title)
        
        # Set the output template with sequence number and safe title
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Select the best 720p video and audio
            'merge_output_format': 'mp4',  # Ensure the output format is mp4 after merging video and audio
            'quiet': True,  # Suppress unnecessary output
            'outtmpl': os.path.join(playlist_dir, f"{seq_num:03d} - {safe_title}.%(ext)s"),
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                print(f"Downloaded: {safe_title}")
        except DownloadError as e:
            print(f"Failed to download {url}: {e}")

# Download videos in order
downloader(videos)

print("All downloads completed.")
