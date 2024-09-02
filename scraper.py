import os
import yt_dlp

# Function to download audio and subtitles from a YouTube video
def download_audio_and_subtitle(video_code, audio_format='mp3', subtitle_format='srt'):
    # Construct the YouTube video URL
    base_url = "https://www.youtube.com/watch?v="
    video_url = base_url + video_code
    
    # Create a folder named after the video code
    output_dir = os.path.join('parsed_Content', video_code)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Initialize yt-dlp options for extracting video information
    ydl_opts_info = {
        'quiet': True,
        'skip_download': True,
    }
    
    # Get video information to determine the language
    with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        # Extract the language code (default language of the video)
        language = info_dict.get('language')
    
    # If language is not detected, fallback to 'en' (English)
    if not language:
        language = 'en'
    
    # Set the yt-dlp options for downloading subtitles and audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, f'{video_code}.%(ext)s'),  # Save files in the created folder with video_code as filename
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio_format,
            'preferredquality': '192',
        }],
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': [language],
        'subtitlesformat': subtitle_format,
        'convertsubs': subtitle_format,
        'logger': MyLogger(),  # Custom logger (optional)
        'progress_hooks': [my_hook],  # Custom progress hook (optional)
    }

    # Download the audio and subtitle files
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Custom logger class for yt-dlp
class MyLogger:
    def debug(self, msg):
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        print(msg)

    def warning(self, msg):
        print(msg)

    def error(self, msg):
        print(msg)

# Custom progress hook function
def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')

# Function to process each video code from the file
def process_video_codes_from_file(file_path):
    # Read video codes from the file
    with open(file_path, 'r') as file:
        video_codes = [line.strip() for line in file if line.strip()]

    # Loop through each video code and download audio and subtitles
    for video_code in video_codes:
        print(f"Processing video: {video_code}")
        download_audio_and_subtitle(video_code, audio_format='mp3', subtitle_format='srt')

if __name__ == '__main__':
    if not os.path.exists('parsed_Content'):
        os.makedirs('parsed_Content')
    # Specify the path to the file containing video codes
    video_codes_file = 'video_ids.txt'
    
    # Call the function to process video codes
    process_video_codes_from_file(video_codes_file)
