from yt_dlp import YoutubeDL
def get_video(url,quality):
    if not url:
        print("Please provide URL first! ")
        return
    print("⚠️ If chosen quality is unavailable, the closest available will be downloaded.")
    if quality==1: video_format="bestvideo[ext=mp4][height<=4320p]+bestaudio[ext=m4a]/best[ext=mp4][height<=4320p]" #Upto 8k
    
    elif quality==2: video_format= "bestvideo[ext=mp4][height<=2160]+bestaudio[ext=m4a]/best[ext=mp4][height<=2160]" #Upto 2k

    elif quality==3: video_format= "bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4][height<=1080]" #Upto 1080p

    elif quality==4: video_format= "bestvideo[ext=mp4][height<=480]+bestaudio[ext=m4a]/best[ext=mp4][height<=480]" #Upto 480p
    
    elif quality==5: video_format= "bestaudio/best"

    else: print("Invalid quality option selected!")

    if "list" in url: download_path= "downloads/%(playlist_title)s/%(title)s_%(height)sp.%(ext)s"
    else: download_path= "downloads/%(title)s_%(height)sp.%(ext)s"
    ydl_opts={
        "outtmpl":download_path,
        "format":video_format,
        "merge_output_format": "mp4",
    }
    if quality==5:
        if "list" in url:
            download_path="downloads/%(playlist_title)s/%(title)s.%(ext)s"
        else:
            download_path= "downloads/%(title)s.%(ext)s"
        ydl_opts = {
        "outtmpl": download_path,
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",  # You can set 128, 192, 256, or 320 kbps
            }
            ],
        }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info=ydl.extract_info(url,download=True)
            if "entries" in info: print(f"Downloaded playlist: {info.get('title')}, {len(info['entries'])} videos")
            else: print(f"Downloaded video: {info.get('title')}")
    except Exception as e: print(f"❌ Error occured {str(e)}")

url=input("Enter url of YT Video : ")
quality=int(input("Enter 1 for great quality (upto 8k)\nEnter 2 for Bestest qualty (upto 4k) \nEnter 3 for best quality (upto 1080p)\nEnter 4 for good quality (upto 480p)\nEnter 5 for audio\n"))
get_video(url,quality)