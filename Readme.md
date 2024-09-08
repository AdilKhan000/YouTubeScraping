# YouTube Video ID Generator and Subtitle Downloader

This repository contains two Python scripts: one for generating YouTube video IDs based on specific categories and regions, and another for downloading subtitles (auto-generated or available) and audio of these videos.
This can be used to generate training data for Machine Learning.

## Prerequisites

Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### 1. YouTube Video code Generator

This script fetches video codes from YouTube based on categories, regions, and charts. It can fetch more than 200 videos using pagination and appends the video codes to a text file.

Usage

```bash
python getID.py --output-file <output_file> --regionCode <region_code> --videoCategoryId <category_ids>
```

Example Command:

```bash
python getID.py --output-file video_ids.txt --regionCode US --videoCategoryId 10,24,17
```

## Content Categories

| **1-10** | **Category**            |
| -------- | ----------------------- |
| 1        | Film & Animation        |
| 2        | Autos & Vehicles        |
| 10       | Music                   |
| 15       | Pets & Animals          |
| 16       | (unassigned)            |
| 17       | Sports                  |
| 18       | Short Movies            |
| 19       | Travel & Events         |
| 20       | Gaming                  |
| 21       | Videoblogging           |
| 22       | People & Blogs          |
| 23       | Comedy                  |
| 24       | Entertainment (general) |
| 25       | News & Politics         |
| 26       | Howto & Style           |
| 27       | Education               |
| 28       | Science & Technology    |
| 29       | Nonprofits & Activism   |
| 30       | Movies                  |
| 31       | Anime/Animation         |
| 32       | Action/Adventure        |
| 33       | Classics                |
| 34       | Comedy                  |
| 35       | Documentary             |
| 36       | Drama                   |
| 37       | Family                  |
| 38       | Foreign                 |
| 39       | Horror                  |
| 40       | Sci-Fi/Fantasy          |
| 41       | Thriller                |
| 42       | Shorts                  |
| 43       | Shows                   |
| 44       | Trailers                |

####Or to get the codes based on specific keyword
Usage

```bash
python getID.py --output-file <output_file> --keyword <keyword> --maxResults <Maximum outputs>
```

Example Command:

```bash
python getID.py --output-file Kannada.txt --keyword "Kannada Travel vlog" --maxResults 50
```

### 2. YouTube Subtitle and Audio Downloader

This script downloads subtitles (either manually uploaded or auto-generated) and audio for videos from YouTube using their video IDs. It also supports specifying subtitle language and uses default settings if not provided.

Usage

```bash
python scraper.py --input-file <video_ids_file> --lang <subtitle_language>
```

Example Command:

```bash
python scraper.py --input-file video_ids.txt --lang kn
```

This command downloads audio and Kannada subtitles (kn) for the videos listed in video_ids.txt. If no language is specified, the script defaults to auto-detected subtitles
