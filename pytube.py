# Download viedo from Youtube
# First make sure in your system pip install
# Then insure that PyTube installed, if not then run pip install PyTube in your terminal

from pytube import YouTube

# Set the URL of the YouTube video you want to download
video_url = "WWW"

# Create a YouTube object
youtube = YouTube(video_url)

# Get the first stream with the "progressive" flag and highest resolution
video = youtube.streams.filter(progressive=True).order_by('resolution').desc().first()

# Set the path where you want to save the video
save_path = "XXX/"

# Download the video
video.download(save_path)

print("Video download complete.")
