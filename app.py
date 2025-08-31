from yt_dlp import YoutubeDL
import os, shutil
from flask import Flask,render_template,request,send_file
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",title="Home - Page")

@app.route("/download_video",methods=["GET"])
def getVideo():
    url=request.args.get("url")
    quality=int(request.args.get("quality"))

    if not url: print("Please provide a valid url!")
    print("⚠️ If chosen quality is unavailable, the closest available will be downloaded.")
    if quality==1: video_format="bestvideo[ext=mp4][height<=4320p]+bestaudio[ext=m4a]/best[ext=mp4][height<=4320p]" #Upto 8k
    
    elif quality==2: video_format= "bestvideo[ext=mp4][height<=2160]+bestaudio[ext=m4a]/best[ext=mp4][height<=2160]" #Upto 2k

    elif quality==3: video_format= "bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4][height<=1080]" #Upto 1080p

    elif quality==4: video_format= "bestvideo[ext=mp4][height<=480]+bestaudio[ext=m4a]/best[ext=mp4][height<=480]" #Upto 480p
    
    elif quality==5: video_format= "bestaudio/best"

    else: return "Invalid quality option selected!",400

    if "list" in url: download_path= "downloads/%(playlist_title)s/%(title)s_%(height)sp.%(ext)s"
    else: download_path= "downloads/%(title)s_%(height)sp.%(ext)s"
    ydl_opts={
        "outtmpl":download_path,
        "format":video_format,
        "merge_output_format": "mp4"
    }
    if quality==5:
        if "list" in url: download_path="downloads/%(playlist_title)s/%(title)s.%(ext)s"
        else: download_path= "downloads/%(title)s.%(ext)s"
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
            if "entries" in info:
                playlist_title=info.get("title","playlist")
                folder_path=os.path.join("downloads",playlist_title)

                zip_filename=f"{folder_path}.zip"
                shutil.make_archive(folder_path,"zip",folder_path)
                
                if os.path.exists(folder_path):
                    shutil.rmtree(folder_path)
                
                return send_file(zip_filename,as_attachment=True),200
            else: 
                if "requested_downloads" in info:
                    filename=info["requested_downloads"][0]["filepath"]
                else:
                    filename=ydl.prepare_filename(info)
                return send_file(filename,as_attachment=True),200
    except Exception as e: return f"❌ Error occured {str(e)}",500
if __name__=="__main__":
    app.run(debug=True)