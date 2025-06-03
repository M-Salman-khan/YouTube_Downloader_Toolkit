# YouTube Video Downloader (720p)

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-brightgreen?logo=youtube)](https://github.com/yt-dlp/yt-dlp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple Python script to download a single YouTube video at up to 720p resolution using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

---

## Features

- Downloads a single YouTube video at up to 720p.
- Saves videos in a `Downloaded_Videos` folder.
- Handles special characters in video titles.
- Minimal, user-friendly command-line interface.

---

## Folder Structure

```
Video_Downloader/
├── video_downloader.py
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
    cd Video_Downloader
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the downloader:**
    ```sh
    python video_downloader.py
    ```

4. **Enter the YouTube video URL** when prompted.

The video will be saved in the `Downloaded_Videos` folder.

---

## Example Output

```
Enter Video URL: https://www.youtube.com/watch?v=...
Video Title   : Example Video Title
Channel Name  : Example Channel
Downloading: Example Video Title
Download completed.
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