# 🎥 YouTube Downloader Toolkit (8K, 4K, 1080p, 480p, MP3)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask Badge"/>
  <img src="https://img.shields.io/badge/yt--dlp-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="yt-dlp Badge"/>
  <img src="https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white" alt="FFmpeg Badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License Badge"/>
</p>

A **Python Flask web app** to download **YouTube videos and playlists** in multiple qualities (up to 8K) or extract audio as MP3 using [yt-dlp](https://github.com/yt-dlp/yt-dlp).  

---

## 🚀 Features
- 📹 Download **single videos** or **entire playlists** from YouTube.
- 🎞️ Quality options:
  - 1 → **8K**
  - 2 → **4K**
  - 3 → **1080p**
  - 4 → **480p**
  - 5 → **Audio only (MP3, 192 kbps)**
- 📂 Playlist videos are stored in a folder named after the playlist and can be downloaded as a ZIP.
- 🔗 Automatic MP4 merging for video + audio.
- 🎵 Audio extracted to **MP3** with FFmpeg.
- 💾 Files are automatically cleaned up after download (for single videos), or playlist folders are deleted after zipping.

---

## 🗂 Folder Structure
```
YT_Downloader/
├── main.py
├── templates/
│   └── index.html
├── downloads/
├── LICENSE
├── README.md
└── requirements.txt
```

---

## ✅ Requirements
- Python 3.7+
- Flask
- yt-dlp
- FFmpeg (for merging and audio extraction)

Install dependencies:
```bash
pip install -r requirements.txt
```
>[!WARNING]
>  Make sure **FFmpeg** is installed and available in your system PATH.

---

## ▶️ Usage

1. Run the Flask app:

```bash
python main.py
```

2. Open the browser at `http://127.0.0.1:5000/`.

3. Paste the YouTube video or playlist URL.

4. Choose your desired quality:

| Value | Quality |
|-------|---------|
| 1     | 8K      |
| 2     | 4K      |
| 3     | 1080p   |
| 4     | 480p    |
| 5     | Audio (MP3) |

5. Click **Download**.  

- Single videos will download immediately.  
- Playlists will be zipped and sent for download.  
- Audio-only downloads will be extracted to MP3 at 192 kbps.


---
## 👀 Demo (Screenshot)
![App Screenshot](.github/assets/Screenshot%202025-08-31%20141105.png)


---

>[!NOTE]
>- yt-dlp automatically chooses the closest available quality if the selected one isn’t available.
>- Playlists are downloaded to a folder named after the playlist; the folder is deleted after zipping.
>- MP3 extraction is done with FFmpeg at **192 kbps** by default.
>- Ensure you have enough disk space for high-resolution video downloads (especially 8K/4K).

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Credits
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) – Video/audio downloader backend  
- [FFmpeg](https://ffmpeg.org/) – Audio extraction and video merging  
- [Flask](https://flask.palletsprojects.com/) – Web framework