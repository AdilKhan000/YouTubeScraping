import os
import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the API key and other constants
API_KEY = 'INSERTYOURAPIKEY'
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CHARTS = ['mostPopular']  # Available chart options; you can expand this list
MAX_RESULTS_PER_CALL = 50  # Maximum number of results per API call (YouTube limits this to 50)
MAX_TOTAL_RESULTS = 1000  # Target total number of results

# Function to get the YouTube API service
def get_youtube_service():
    return build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)

# Function to fetch a list of video IDs and save them to a file
def fetch_video_ids(youtube, output_file, **kwargs):
    video_ids = []
    page_token = None

    while len(video_ids) < MAX_TOTAL_RESULTS:
        request = youtube.videos().list(
            part=kwargs.get('part', 'snippet'),
            chart=kwargs.get('chart', 'mostPopular'),
            regionCode=kwargs.get('regionCode', 'US'),
            videoCategoryId=kwargs.get('videoCategoryId', '0'),
            maxResults=min(MAX_RESULTS_PER_CALL, MAX_TOTAL_RESULTS - len(video_ids)),
            pageToken=page_token
        )

        response = request.execute()
        video_ids.extend([item['id'] for item in response.get('items', [])])

        # Check for the next page token
        page_token = response.get('nextPageToken')
        if not page_token:
            break  # Exit if there are no more pages

    # Append video IDs to the output file
    with open(output_file, 'a') as f:
        for video_id in video_ids:
            f.write(video_id + '\n')

    print(f"Fetched {len(video_ids)} video IDs and appended to {output_file}")

def fetch_videos_for_different_categories(youtube, output_file, categories, region_code):
    for category_id in categories:
        print(f"Fetching videos for category ID {category_id}...")
        fetch_video_ids(
            youtube,
            output_file=output_file,
            chart='mostPopular',  # You can modify this to fetch different types of videos
            regionCode=region_code,
            videoCategoryId=category_id,
            maxResults=MAX_RESULTS_PER_CALL
        )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Define command-line arguments
    parser.add_argument('--output-file', type=str, required=True, help='File to save video IDs')
    parser.add_argument('--part', type=str, default='snippet', help='Comma-separated list of video resource properties to retrieve')
    parser.add_argument('--chart', type=str, choices=CHARTS, default='mostPopular', help='Chart to retrieve (mostPopular)')
    parser.add_argument('--regionCode', type=str, default='US', help='ISO 3166-1 alpha-2 country code to filter videos by region')
    parser.add_argument('--videoCategoryId', type=str, help='Comma-separated video category IDs to filter results by category')
    parser.add_argument('--maxResults', type=int, default=50, help='Maximum number of results per page')

    args = parser.parse_args()

    # Initialize YouTube service
    youtube_service = get_youtube_service()

    # Fetch videos for multiple categories
    categories = args.videoCategoryId.split(',') if args.videoCategoryId else ['0']  # Default to category ID '0'
    fetch_videos_for_different_categories(
        youtube_service,
        output_file=args.output_file,
        categories=categories,
        region_code=args.regionCode
    )
