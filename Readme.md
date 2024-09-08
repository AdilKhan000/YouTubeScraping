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

| **1-10** | **Category**     |
| -------- | ---------------- |
| 1        | Film & Animation |
| 2        | Autos & Vehicles |
| 3        | (unassigned)     |
| 4        | (unassigned)     |
| 5        | (unassigned)     |
| 6        | (unassigned)     |
| 7        | (unassigned)     |
| 8        | (unassigned)     |
| 9        | (unassigned)     |
| 10       | Music            |

| **11-20** | **Category**    |
| --------- | --------------- |
| 11        | (unassigned)    |
| 12        | (unassigned)    |
| 13        | (unassigned)    |
| 14        | (unassigned)    |
| 15        | Pets & Animals  |
| 16        | (unassigned)    |
| 17        | Sports          |
| 18        | Short Movies    |
| 19        | Travel & Events |
| 20        | Gaming          |

| **21-30** | **Category**            |
| --------- | ----------------------- |
| 21        | Videoblogging           |
| 22        | People & Blogs          |
| 23        | Comedy                  |
| 24        | Entertainment (general) |
| 25        | News & Politics         |
| 26        | Howto & Style           |
| 27        | Education               |
| 28        | Science & Technology    |
| 29        | Nonprofits & Activism   |
| 30        | Movies                  |

| **31-44** | **Category**     |
| --------- | ---------------- |
| 31        | Anime/Animation  |
| 32        | Action/Adventure |
| 33        | Classics         |
| 34        | Comedy           |
| 35        | Documentary      |
| 36        | Drama            |
| 37        | Family           |
| 38        | Foreign          |
| 39        | Horror           |
| 40        | Sci-Fi/Fantasy   |
| 41        | Thriller         |
| 42        | Shorts           |
| 43        | Shows            |

(TV shows?)
44 | Trailers

####Or to get the codes based on specific keyword
Usage

```bash
python getID.py --output-file <output_file> --keyword <keyword> --maxResults <Maximum outputs>
```

Example Command:

```bash
python getID.py --output-file Kannada.txt --keyword "Kannada Travel vlog" --maxResults 50
```
