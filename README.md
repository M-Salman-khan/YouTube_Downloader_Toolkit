# YouTube Downloader Toolkit (720p)

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-latest-brightgreen?logo=youtube)](https://github.com/yt-dlp/yt-dlp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A Python toolkit to download single videos or entire playlists from YouTube at up to 720p resolution using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

---

## 🚀 Projects Included

### 1. 📥 YouTube Video Downloader
- Downloads a **single YouTube video** at up to 720p.
- Saves videos in the `Downloaded_Videos` folder.
- Minimal user prompts and automatic filename sanitization.

File: `Video_Downloader/Video_Downloader_at_720p.py`

### 2. 📥 YouTube Playlist Downloader
- Downloads all videos from a **YouTube playlist**, in order.
- Saves them in a folder named after the playlist.
- Includes title sanitization and MP4 merging.

File: `Playlist_Downloader/Playlist_downloader_at_720p.py`

---

## 🗂 Folder Structure

```
YT_Playlist_Downloader/
├── Playlist_Downloader/
│   ├── LICENSE
│   ├── Playlist_downloader_at_720p.py
│   ├── README.md
│   └── requirements.txt
│
├── Video_Downloader/
│   ├── LICENSE
│   ├── README.md
│   ├── requirements.txt
│   └── Video_Downloader_at_720p.py
│
├── LICENSE
└── README.md
```

---

## ✅ Requirements

- Python 3.7+
- yt-dlp

Install dependencies:
```sh
pip install -r requirements.txt
```

Example `requirements.txt`:
```
yt-dlp
```

---

## ▶️ Usage

### Run Single Video Downloader
```sh
cd Video_Downloader
python Video_Downloader_at_720p.py
```
You’ll be prompted to enter the **YouTube video URL**.

### Run Playlist Downloader
```sh
cd Playlist_Downloader
python Playlist_downloader_at_720p.py
```
You’ll be prompted to enter the **YouTube playlist URL**.

---

## 💡 Output Examples

### Video Downloader
```
Enter Video URL: https://www.youtube.com/watch?v=...
Video Title   : Example Title
Channel Name  : Example Channel
Downloading: Example Title
Download completed.
```

### Playlist Downloader
```
Enter Playlist URL: https://www.youtube.com/playlist?list=...
Playlist Name : My Playlist
Channel Name  : Example Channel
Total Videos  : 10
Downloading Started...

Downloaded: 001 - Video Title
...
All downloads completed.
```

---

## ⚠️ Notes

- Downloads are capped at **720p** for video quality.
- Filenames are sanitized to avoid filesystem issues.
- Errors (e.g. unavailable video) are caught and printed.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Credits

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for the powerful downloading backend.
