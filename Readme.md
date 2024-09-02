YouTube Video ID Generator and Subtitle Downloader
This repository contains two Python scripts: one for generating YouTube video IDs based on specific categories and regions, and another for downloading subtitles (auto-generated or available) for those videos.

Prerequisites
Ensure that Python 3.x is installed on your system.

Install the required dependencies by running:

pip install google-api-python-client youtube-dl
or using requirements.txt:

pip install -r requirements.txt
Contents of requirements.txt:

google-api-python-client
youtube-dl

1. YouTube Video ID Generator
   This script fetches video IDs from YouTube based on categories, regions, and charts. It can fetch more than 200 videos using pagination and appends the video IDs to a text file.

Usage

python getID.py --output-file <output_file> --regionCode <region_code> --videoCategoryId <category_ids>
Example Command:

python getID.py --output-file video_ids.txt --regionCode US --videoCategoryId 10,24,17
Options:
Argument Description Example
--output-file File where the video IDs will be saved (appended if the file already exists). video_ids.txt
--regionCode Region code to filter videos by country. Default is US. You can use any ISO 3166-1 alpha-2 country code. US, IN
--videoCategoryId Comma-separated list of video categories to retrieve. Below is a list of available category IDs. You can specify one or multiple categories. 10,17,22
--maxResults Maximum number of results per page. YouTube API limits this to 50. The script automatically handles pagination to fetch more results. 50
--part Part of the video resource to retrieve. Default is snippet. snippet
Video Categories
ID Category ID Category
2 Autos & Vehicles 28 Science & Technology
1 Film & Animation 29 Nonprofits & Activism
10 Music 30 Movies
15 Pets & Animals 31 Anime/Animation
17 Sports 32 Action/Adventure
18 Short Movies 33 Classics
19 Travel & Events 34 Comedy
20 Gaming 35 Documentary
21 Videoblogging 36 Drama
22 People & Blogs 37 Family
23 Comedy 38 Foreign
24 Entertainment 39 Horror
25 News & Politics 40 Sci-Fi/Fantasy
26 Howto & Style 41 Thriller
27 Education 42 Shorts
28 Science & Technology 43 Shows
29 Nonprofits & Activism 44 Trailers
Notes:
Multiple Categories: You can provide multiple categories separated by commas (e.g., 10,17,22 for Music, Sports, and People & Blogs).
Pagination: The script uses nextPageToken to fetch more than 200 video IDs.
File Append: The video IDs are appended to the specified output file to avoid overwriting existing data.

2. YouTube Subtitle Downloader
   This script downloads subtitles (either manually uploaded or auto-generated) for videos from YouTube using their video IDs.

Usage

python scraper.py

Language Detection: The script automatically detects the video’s language and fetches subtitles accordingly (e.g., Hindi for Hindi videos, English for English videos).
Auto-Generated Subtitles: It also supports downloading auto-generated subtitles by using the --write-auto-subs flag.
Subtitle Format: You can specify the subtitle format (e.g., SRT or VTT) using the --sub-format option.
How to Run
Step 1: Generate YouTube Video IDs
To generate a list of YouTube video IDs based on your desired categories and regions, run the following command:

bash
Copy code
python getID.py --output-file video_ids.txt --regionCode IN --videoCategoryId 10,24,17
This command will save the video IDs from categories Music (10), Entertainment (24), and Sports (17) in India (regionCode=IN) to the video_ids.txt file.
Step 2: Download Subtitles for the Videos
Once the video IDs are saved in the video_ids.txt file, you can download subtitles for these videos by running:

python scraper.py
This command will download the subtitles and save them in the subtitles/ directory.
