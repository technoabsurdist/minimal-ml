# Common ML Usecases API 

API that provides some useful and common interactions with state-of-the-art ML models (e.g., `chat-gpt4`, `youtube_transcription`, )
using Sieve, Langchain and more. 

## Features

- **Translation (sieve/seamless_text2text)**: Translates text from a source language to a target language. <br />
- **Youtube Link Transcription (langchain/youtube_transcripts)**: Transcribes audio from a given URL. <br />
- **Detect Language**: Identifies the language of the given text. <br />
- **Text to Speech**: Converts text into spoken words. <br />
- **Translate and Talk**: Translates text from one language to another and then converts the translated text to speech. <br />
- **Youtube Video Download (MP4)**: Downloads a Youtube video in MP4 format given its URL. <br />
- **Detect Language and Translate**: Detects the language of the text and translates it to a specified target language. <br />

## Setup

To set up the server, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine. <br />
2. **Install Dependencies**: Install the required Python packages using: `pip install -r requirements.txt` <br />
3. **Run server**: Run server with `python main.py` <br />

## Endpoints

The API provides the following endpoints:

- `/transcription`: POST method for transcribing Youtube videos. <br />
- `/translation`: POST method for translating text. <br />
- `/detect_language`: POST method for detecting the language of text. <br />
- `/detect_and_translate`: POST method for detecting language and then translating text. <br />
- `/text_to_speech`: POST method for converting text to speech. <br />
- `/translate_and_talk`: POST method for translating and converting text to speech. <br />
- `/youtube_download_mp4`: POST method for downloading Youtube videos in MP4 format. <br />