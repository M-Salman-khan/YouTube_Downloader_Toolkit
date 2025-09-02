# 🎥 YouTube Downloader Toolkit (8K, 4K, 1080p, 480p, MP3) - [CLI Version]

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask Badge"/>
  <img src="https://img.shields.io/badge/yt--dlp-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="yt-dlp Badge"/>
  <img src="https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge&logo=ffmpeg&logoColor=white" alt="FFmpeg Badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License Badge"/>
</p>


A Python toolkit to download **YouTube videos and playlists** in different qualities (up to **8K**) or extract audio as MP3 using [yt-dlp](https://github.com/yt-dlp/yt-dlp).  

---

## 🚀 Features
- 📹 Download **single YouTube videos** or entire **playlists**.  
- 🎞️ Quality options:  
  - 1 → **Great Quality** (up to 8K)  
  - 2 → **Bestest Quality** (up to 4K)  
  - 3 → **Best Quality** (up to 1080p)  
  - 4 → **Good Quality** (up to 480p)  
  - 5 → **Audio only (MP3, 192kbps)**  
- 📂 Playlist videos are saved inside a folder named after the playlist.  
- 🔗 Automatic MP4 merging for video + audio.  
- 🎵 Audio extracted with FFmpeg in **MP3 format**.  

---

## 🗂 Folder Structure
```
YT_Downloader/
├── main.py
├── LICENSE
├── README.md
└── requirements.txt
```

---

## ✅ Requirements
- Python 3.7+  
- yt-dlp  
- FFmpeg (required for merging & audio extraction)  

Install dependencies:
```sh
pip install -r requirements.txt
```

>[!NOTE]
>Make sure **FFmpeg** is installed and available in your >system PATH.  

---

## ▶️ Usage
Run the main script:
```sh
python main.py
```

You’ll be prompted to enter the **YouTube video/playlist URL** and choose the quality option.  

---

## 💡 Output Examples

### Example 1: Single Video Download
```
Enter url of YT Video : https://youtu.be/Ky5i7NC4YgY
Enter 1 for great quality (upto 8k)
Enter 2 for Bestest quality (upto 4k)
Enter 3 for best quality (upto 1080p)
Enter 4 for good quality (upto 480p)
Enter 5 for audio

2
⚠️ If chosen quality is unavailable, the closest available will be downloaded.
[download] Destination: downloads/Muhabbat Gumshuda Meri 🎵❤️Original Sound Track - HUM MUSIC_720p.mp4
Downloaded video: Muhabbat Gumshuda Meri 🎵❤️Original Sound Track - HUM MUSIC
```

### Example 2: Playlist Download
```
Enter url of YT Video : https://www.youtube.com/playlist?list=...
Enter quality option (1–5): 3
⚠️ If chosen quality is unavailable, the closest available will be downloaded.
Downloaded playlist: My Playlist, 12 videos
```

### Example 3: Audio Only
```
Enter url of YT Video : https://youtu.be/xyz123
Enter 5 for audio
[download] Destination: downloads/Example Song_mp3.mp3
Downloaded video: Example Song
```

---

> [!NOTE]  
> - If the chosen resolution is **not available**, yt-dlp automatically picks the closest quality.  
> - Playlist downloads create a separate folder with the **playlist name**.  
> - MP3 audio is extracted at **192 kbps** by default (configurable in code).  
> - Make sure you have enough disk space for high-resolution videos (8K/4K).  

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).  

---

## 🙏 Credits
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) – The backend downloader  
- [FFmpeg](https://ffmpeg.org/) – Used for merging and audio extraction  
