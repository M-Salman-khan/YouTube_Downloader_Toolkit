# Author: Salman Khan
# Social: instagram.com/khansalman.ig
# Website: m-salman-khan.web.app

'''Download all the pip from given below link
https://packaging.python.org/en/latest/tutorials/installing-packages'''

from pytube import YouTube
from pytube import Playlist
import sys
import os
import re

# Get playlist URL from user input
try:
    playlist_url = input("Enter Playlist URL: ")
    p = Playlist(playlist_url)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

try:
    playlist_title = p.title
    playlist_title_sanitized = re.sub(r'[<>:"/\\|?*]', '_', playlist_title)
    print("Playlist Name : {}\nChannel Name  : {}\nTotal Videos  : {}\nTotal Views   : {}".format(playlist_title, p.owner, p.length, p.views))
except Exception as e:
    print(f"Error retrieving playlist details: {e}")
    sys.exit(1)

# Create a directory with the playlist name
playlist_dir = playlist_title_sanitized
if not os.path.exists(playlist_dir):
    os.makedirs(playlist_dir)

# Get video URLs from the playlist
links = []
try:
    for url in p.video_urls:
        links.append(url)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)

print("Downloading Started...\n")

# Define the downloader function
def downloader(urls):
    for i, url in enumerate(urls):
        try:
            yt = YouTube(url)
            ys = yt.streams.get_highest_resolution()
            filename = ys.default_filename
            new_filename = f"{i+1:03d} - {filename}"
            ys.download(output_path=playlist_dir, filename=new_filename)
            print(f"{i+1}/{len(urls)} --> {new_filename} Downloaded")
        except Exception as e:
            print(f"Failed to download {url}: {e}")

# Download videos in order
downloader(links)

print("All downloads completed.")
