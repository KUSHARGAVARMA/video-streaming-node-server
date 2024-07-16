import yt_dlp

SAVE_PATH = "./src"  # Save to the src directory
link = "https://www.youtube.com/watch?v=eeDp4RbdX1I"

ydl_opts = {
    'outtmpl': f'{SAVE_PATH}/%(title)s.%(ext)s',
    'format': 'mp4'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print('Video downloaded successfully!')
