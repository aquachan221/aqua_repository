import yt_dlp# type: ignore

def download_audio_m4a(url):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]',  # Ensure audio is in M4A format
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
download_audio_m4a("https://www.youtube.com/watch?v=dQw4w9WgXcQ")