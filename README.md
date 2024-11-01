# Python Playlist Downloader

This Python script allows you to download all videos from a given playlist URL on YouTube. It saves the videos to your local directory, making playlists available offline anytime.

## Author

- **Name**: M. Salman Khan
- **Instagram**: [khansalman.ig](https://instagram.com/khansalman.ig)
- **Website**: [m-salman-khan.web.app](https://m-salman-khan.web.app)

## Features

- Downloads all videos from a specified playlist.
- Saves downloaded videos to a chosen folder on your device.
- Provides status updates on each download’s progress.

## Requirements

- **Python 3.x**: Ensure Python is installed on your system. You can check your version by running:
  ```bash
  python --version
  ```
- **pip**: Python package manager, typically included with Python installations.
- **FFmpeg**: Required for video processing.

## Installation

### Step 1: Clone the Repository

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/playlist-downloader.git
   ```
2. Navigate to the project directory:
   ```bash
   cd playlist-downloader
   ```

### Step 2: Install Dependencies

Install Python dependencies:
```bash
pip install -r requirements.txt
```

### Step 3: Install FFmpeg (for Windows)

You can install FFmpeg on Windows easily using Chocolatey, a Windows package manager.

1. Install [Chocolatey](https://chocolatey.org/install) if you haven’t already.
2. Once Chocolatey is set up, open a new command prompt (with administrator privileges) and run:
   ```bash
   choco install ffmpeg
   ```
3. After installation, verify FFmpeg by running:
   ```bash
   ffmpeg -version
   ```

For other operating systems, refer to [FFmpeg's official installation guide](https://ffmpeg.org/download.html).

## Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. Enter the URL of the playlist you want to download when prompted.
3. The videos will begin downloading to the specified directory.

## Note

- This script is for personal use only. Be sure to respect YouTube’s terms of service regarding downloading videos.

## Contributing

Feel free to open issues or submit pull requests to improve the script or add new features!
