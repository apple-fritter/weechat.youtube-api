# YouTube Info

This WeeChat script fetches YouTube video information from URLs shared in a channel and posts the extracted details back to the channel. It utilizes the YouTube Data API to retrieve video information, ensuring accurate and reliable data extraction.

This project is intended to be a continuation of my deprecated repository, [weechat.youtube-info](https://github.com/apple-fritter/weechat.youtube-info).

## Requirements

- Python (2.7+ or 3.x)
- WeeChat
- `requests` library (`pip install requests`)
- YouTube Data API key (obtainable from Google Cloud Console)

## Installation

1. Install WeeChat if you haven't already. Refer to the official WeeChat documentation for installation instructions.
2. Install the `requests` library by running the following command:

```bash
pip install requests
```

3. Obtain a YouTube Data API key from the Google Cloud Console.
4. Download the `youtube_info.py` script file to your local machine.
5. Open the `youtube_info.py` script file and replace `"YOUR_API_KEY"` with your actual YouTube Data API key.
6. Open WeeChat and load the script by running the following command:

```bash
/script load /path/to/youtube_info.py
```

Replace `/path/to/youtube_info.py` with the actual path to the script file on your machine.

## Usage

1. Join a channel where users share YouTube URLs.
2. When a YouTube URL is posted in the channel, the script will automatically retrieve the video information using the YouTube Data API.
3. The extracted information includes the video's title, author, and duration, presented in a clean format.
4. The script will post the extracted information back to the channel for everyone to see and discuss.

## Flowchart
```
┌─ Start Program
│
├─ Join a channel
│
├─ Listen for messages
│   ├─ Is it a YouTube URL?
│   │   ├─ Yes
│   │   │   ├─ Fetch YouTube video details
│   │   │   │   ├─ Call YouTube API
│   │   │   │   │   ├─ Construct API request
│   │   │   │   │   ├─ Send API request
│   │   │   │   │   └─ Receive API response
│   │   │   │   │
│   │   │   │   └─ Extract video information from response
│   │   │   │
│   │   │   └─ Post video information to the channel
│   │   │
│   │   └─ No
│   │
│   └─ Continue listening for messages
│
└─ End Program
```

## Customization

You can customize the script behavior by modifying the following variables in the script:

- `API_KEY`: Replace `"YOUR_API_KEY"` with your actual YouTube Data API key obtained from the Google Cloud Console.

## Limitations

- The script requires a valid YouTube Data API key to access the API. Make sure to obtain a key from the Google Cloud Console and replace `"YOUR_API_KEY"` in the script with your actual key.
- The YouTube Data API has rate limits and usage quotas. Ensure your API key and usage comply with the API's terms and restrictions to avoid service interruptions.

## Contributing

Contributions to the script are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request or open an issue on the GitHub repository.
## IRC Meta

### WeeChat
- [weechat.ban-evasion-detection](https://github.com/apple-fritter/weechat.ban-evasion-detection): Detect and prevent ban evasion. (Python)
- [weechat.typo-aggregator](https://github.com/apple-fritter/weechat.typo-aggregator): Record misspelled words in a TSV (tab-separated values) file. (Python)
- [weechat.whois-aggregator](https://github.com/apple-fritter/weechat.whois-aggregator): Aggregate whois data in a rolling CSV file. (Python)
- (Deprecated) [weechat.youtube-info](https://github.com/apple-fritter/weechat.youtube-info): Extract video information from a YouTube URL and post it back to the channel. (Python)
- [weechat.youtube-api](https://github.com/apple-fritter/weechat.youtube-api): Extract video information from a YouTube URL and post it back to the channel. (Python)

### IRCcloud
- [irccloud-to-weechat](https://github.com/apple-fritter/irccloud-to-weechat): Convert IRC logs from IRCcloud format to Weechat format. (Rust)
- [irccloud-to-xchat](https://github.com/apple-fritter/irccloud-to-xchat): Convert IRC logs from IRCcloud format to XChat format. (Rust)

### X-Chat
- [xchat.channel-moderation](https://github.com/apple-fritter/xchat.channel-moderation): Moderate an IRC channel. (Python)
- [doppelganger](https://github.com/apple-fritter/doppelganger): X-Chat mIRC imposter. Fingerprint subversion. (Python bundle)

### Other
- [driftwood](https://github.com/apple-fritter/driftwood): A unified IRC log format definition. (Rust)

### IRC usage considerations
When working with any project involving IRC (Internet Relay Chat), it's important to keep the following considerations in mind to ensure a positive and respectful environment for all participants.

#### Philosophy of Use
Tailor your project's behavior and responses to align with the expected norms and conventions of IRC. Take into account the preferences and expectations of IRC users, ensuring that your project provides a seamless and familiar experience within the IRC ecosystem.

#### Foster a Positive and Inclusive Environment
Respect and adhere to the guidelines and policies of the IRC platform you are using. Familiarize yourself with the platform's rules regarding script usage, automation, and acceptable behavior. Comply with the platform's Terms of Service, and be mindful of any limitations or restrictions imposed by the platform. Strive to create an inclusive and welcoming environment where all users can engage respectfully and comfortably.

#### Respect the Rights and Dignity of Other Users
Maintain a polite and courteous demeanor in all interactions. Uphold the fundamental principles of respect, avoiding engagement in illegal, inappropriate, or offensive behavior. This includes refraining from using derogatory or inflammatory language, sharing explicit, triggering, or offensive content, engaging in harassment, or launching personal attacks. Obtain explicit consent before interacting with other users or sending automated responses. Respect the privacy of other users and avoid invading their personal space without their permission.

#### Respect the IRC Community and Channels
Avoid disrupting the normal flow of conversation within IRC channels. Ensure that your project's actions and responses do not cause unnecessary disruptions or inconvenience to other users. Implement mechanisms to prevent spamming or flooding the channel with excessive or irrelevant messages. Handle errors gracefully, preventing unintended behavior or disruptions to the IRC platform or the experiences of other users.

#### Ensure Compatibility
Consider the potential variations in behavior across different IRC platforms and clients. While aiming for compatibility, be aware that certain functionalities may not be available or consistent across all platforms. Test your project on multiple IRC platforms and clients to ensure compatibility and provide the best possible experience for users.

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

## License

These files released under the [MIT License](LICENSE).
