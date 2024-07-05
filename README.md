# Playlist Downloader

This Python script downloads all videos from a YouTube playlist and saves them to a directory named after the playlist. The script uses the `pytube` library to handle video downloading.

## Author

- **Name**: Salman Khan
- **Instagram**: [khansalman.ig](https://instagram.com/khansalman.ig)
- **Website**: [m-salman-khan.web.app](https://m-salman-khan.web.app)

## Requirements

Ensure you have `pytube` installed before running the script. If not, you can install it using pip:

```sh
pip install pytube
```

For more information on installing Python packages, visit the [official documentation](https://packaging.python.org/en/latest/tutorials/installing-packages).

## Usage

1. Clone or download the script to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using Python:

   ```sh
   python Playlist_downloader.py
   ```

5. When prompted, enter the URL of the YouTube playlist you want to download.
6. The script will create a directory named after the playlist (with any illegal characters sanitized) and download all videos in the highest available resolution to this directory.

## How It Works

1. The script prompts the user to enter the URL of a YouTube playlist.
2. It retrieves the playlist details and creates a directory named after the playlist.
3. It collects all video URLs from the playlist.
4. It downloads each video in the highest available resolution, saving them in the previously created directory with filenames numbered in the order of their appearance in the playlist.
5. The script prints the progress and completion status for each video download.

## Example

```sh
Enter Playlist URL: https://www.youtube.com/playlist?list=PL1234567890
Playlist Name : Example Playlist
Channel Name  : Example Channel
Total Videos  : 10
Total Views   : 100000

Downloading Started...

1/10 --> 001 - video1.mp4 Downloaded
2/10 --> 002 - video2.mp4 Downloaded
...
10/10 --> 010 - video10.mp4 Downloaded

All downloads completed.
```

## Notes

- Ensure you have a stable internet connection during the download process.
- If the playlist contains a large number of videos, the download process might take a significant amount of time.

## Troubleshooting

- If you encounter errors, ensure you have installed all required dependencies.
- Check your internet connection if downloads are failing.
- Ensure the provided playlist URL is correct and accessible.

## License

This project is open-source and available under the [MIT License](LICENSE).
