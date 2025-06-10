import yt_dlp  # type: ignore

def download_audio(url):
    # Step 1: Get available formats
    ydl = yt_dlp.YoutubeDL({'listformats': True})
    info_dict = ydl.extract_info(url, download=False)
    
    # Step 2: Check if M4A is available
    m4a_format = None
    for fmt in info_dict['formats']:
        if 'm4a' in fmt.get('ext', ''):
            m4a_format = fmt['format_id']
            break

    # Step 3: Set the format (M4A if available, otherwise MP3)
    ydl_opts = {
        'format': m4a_format if m4a_format else 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a' if m4a_format else 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
download_audio("")
#left off 177
#poop playlist