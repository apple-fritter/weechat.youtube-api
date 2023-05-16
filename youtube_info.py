import weechat
import re
import subprocess
import requests

# YouTube Data API endpoint and API key
API_ENDPOINT = "https://www.googleapis.com/youtube/v3/videos"
API_KEY = "YOUR_API_KEY"

# Regular expression pattern for extracting video ID from YouTube URL
VIDEO_ID_PATTERN = r"youtube\.com/watch\?v=([^\s&]+)"

def fetch_youtube_info(data, buffer, date, tags, displayed, highlight, prefix, message):
    # Check if the message contains a YouTube URL
    match = re.search(VIDEO_ID_PATTERN, message)
    if match:
        video_id = match.group(1)

        # Send API request to retrieve video information
        params = {
            "part": "snippet,contentDetails",
            "id": video_id,
            "key": API_KEY
        }
        response = requests.get(API_ENDPOINT, params=params)
        video_data = response.json()

        if "items" in video_data:
            video_info = video_data["items"][0]["snippet"]

            # Extract video information
            video_title = video_info["title"]
            video_author = video_info["channelTitle"]
            video_duration = video_data["items"][0]["contentDetails"]["duration"]

            # Post the extracted information back to the channel
            weechat.command(buffer, "/say [YouTube Info] Title: {} | Author: {} | Duration: {}".format(
                video_title, video_author, video_duration))
        else:
            # Unable to retrieve video information
            weechat.command(buffer, "/say [YouTube Info] Failed to retrieve video information.")

    return weechat.WEECHAT_RC_OK

if __name__ == "__main__":
    weechat.register("youtube_info", "Your Name", "1.0", "MIT", "Fetch YouTube info from URLs", "", "")

    # Hook the message processing event
    weechat.hook_print("", "irc_privmsg", "", 1, "fetch_youtube_info", "")

    weechat.prnt("", "YouTube info script loaded.")
