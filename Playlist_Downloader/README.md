# YouTube Playlist Downloader (720p)

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-brightgreen?logo=youtube)](https://github.com/yt-dlp/yt-dlp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A Python script to download all videos from a YouTube playlist at up to 720p resolution using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

---

## Features

- Downloads all videos from a YouTube playlist in order.
- Saves videos in a folder named after the playlist.
- Handles special characters in playlist and video titles.
- Downloads best available video/audio up to 720p and merges as MP4.
- Minimal, user-friendly command-line interface.

---

## Folder Structure

```
Playlist_Downloader/
├── Playlist_downloader_at_720p.py
├── README.md
└── requirements.txt
```

---

## Requirements

- Python 3.7+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

Install dependencies:
```sh
pip install -r requirements.txt
```

`requirements.txt`:
```
yt-dlp
```

---

## Usage

1. **Clone the repository:**
    ```sh
    git clone https://github.com/M-Salman-khan/YT_Playlist_Downloader.git
    cd Playlist_Downloader
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the downloader:**
    ```sh
    python playlist_downloader.py
    ```

4. **Enter the YouTube playlist URL** when prompted.

Videos will be saved in a folder named after the playlist.

---

## Example Output

```
Enter Playlist URL: https://www.youtube.com/playlist?list=...
Playlist Name : My Playlist
Channel Name  : Example Channel
Total Videos  : 12
Downloading Started...

Downloaded: 001 - First Video Title
Downloaded: 002 - Second Video Title
...
All downloads completed.
```

---

## Notes

- Only videos up to 720p will be downloaded.
- Filenames are sanitized to avoid issues with special characters.
- If a download fails, an error message will be displayed.

---

## License

MIT License

---

## Credits

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)