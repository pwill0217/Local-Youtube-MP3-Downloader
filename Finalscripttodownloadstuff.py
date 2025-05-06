import yt_dlp

# Open the file where the YouTube links were saved
with open("youtube_links.txt", "r") as file:
    # Read each line (each link)
    links = file.readlines()

# Clean up the links (remove any extra newlines or spaces)
links = [link.strip() for link in links]

# Configure yt-dlp options for audio extraction and conversion to MP3
ydl_opts = {
    'format': 'bestaudio/best',  # Select the best audio format available
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',  # Correct key for FFmpeg audio extraction
        'preferredcodec': 'mp3',  # Convert to MP3
    }],
    'outtmpl': '%(title)s.%(ext)s',  # Save the file with the title of the video
}

# Iterate through the list of links and download the audio
for link in links:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])  # Download the audio for each link
