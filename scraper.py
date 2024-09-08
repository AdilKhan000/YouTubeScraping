import os
import yt_dlp
import argparse

# Function to download audio and subtitles based on default settings (no language provided)
def download_audio_and_default_subtitle(video_code, audio_format='mp3', subtitle_format='srt'):
    base_url = "https://www.youtube.com/watch?v="
    video_url = base_url + video_code
    
    output_dir = os.path.join('parsed_Content', video_code)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts_info = {
        'quiet': True,
        'skip_download': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        language = info_dict.get('language')

    # Default to 'en' (English) if language is not detected
    if not language:
        language = 'en'

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, f'{video_code}.%(ext)s'),
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
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Function to download audio and subtitles based on the provided language
def download_audio_and_specified_subtitle(video_code, language, audio_format='mp3', subtitle_format='srt'):
    base_url = "https://www.youtube.com/watch?v="
    video_url = base_url + video_code
    
    output_dir = os.path.join('parsed_Content', video_code)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, f'{video_code}.%(ext)s'),
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
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }

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

# Function to process each video code from the file based on language input
def process_video_codes_from_file(file_path, language=None):
    with open(file_path, 'r') as file:
        video_codes = [line.strip() for line in file if line.strip()]

    for video_code in video_codes:
        print(f"Processing video: {video_code}")
        if language:
            download_audio_and_specified_subtitle(video_code, language, audio_format='mp3', subtitle_format='srt')
        else:
            download_audio_and_default_subtitle(video_code, audio_format='mp3', subtitle_format='srt')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Download audio and subtitles from YouTube videos.")
    
    # Arguments for input file and subtitle language
    parser.add_argument('--input-file', type=str, required=True, help='Path to the file containing video codes.')
    parser.add_argument('--language', type=str, help='Subtitle language code (e.g., en, kn, hi). Defaults to the original setting.')
    
    args = parser.parse_args()

    # Ensure the parsed_Content directory exists
    if not os.path.exists('parsed_Content'):
        os.makedirs('parsed_Content')
    
    # Process video codes based on the provided arguments
    process_video_codes_from_file(args.input_file, args.language)
