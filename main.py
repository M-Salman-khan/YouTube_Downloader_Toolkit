from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
import sys
import os

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
playlist_dir = p['title'].strip().replace(" ", "_")
if not os.path.exists(playlist_dir):
    os.makedirs(playlist_dir)

# Get video URLs from the playlist
links = []
try:
    for entry in p['entries']:
        links.append(entry['url'])
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

print("Downloading Started...\n")

# Define the downloader function
def downloader(urls):
    ydl_opts = {
        'outtmpl': os.path.join(playlist_dir, '%(playlist_index)03d - %(title)s.%(ext)s'),
        'quiet': True  # Suppress unnecessary output
    }
    with YoutubeDL(ydl_opts) as ydl:
        for i, url in enumerate(urls):
            try:
                info = ydl.extract_info(url, download=True)
                print(f"Downloading: {info['title']}")
            except DownloadError as e:
                print(f"Failed to download {url}: {e}")

# Download videos in order
downloader(links)

print("All downloads completed.")
