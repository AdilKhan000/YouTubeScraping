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

Or to get the codes based on specific keyword
Usage

```bash
python getID.py --output-file <output_file> --keyword <keyword> --maxResults <Maximum outputs>
```

Example Command:

```bash
python getID.py --output-file Kannada.txt --keyword "Kannada Travel vlog" --maxResults 50
```
