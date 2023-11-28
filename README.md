
<div align="center"> 
    <h1>Common ML Functionalities API</h1>
    <img src="./cover-image.png" height="200" width="200">
    <h4>
    Python package which provides useful and common interactions with ML functionalities <br /> such as detecting language, chatbots, 
    link transcriptions, audio enhancements, and much more.  
    </h4>

</div>

<br />
<br />

## Features

- **Translation (sieve/seamless_text2text)**: Translates text from a source language to a target language.
- **Youtube Link Transcription (langchain/youtube_transcripts)**: Transcribes audio from a given URL.
- **Detect Language (sieve)**: Identifies the language of the given text.
- **Text to Speech (sieve)**: Converts text into spoken words.
- **Translate and Talk (sieve)**: Translates text from one language to another and then converts the translated text to speech.
- **Youtube Video Download (sieve)**: Downloads a Youtube video in MP4 format given its URL.
- **Detect Language and Translate**: Detects the language of the text and translates it to a specified target language.
- **Audio Enhancement (sieve)**: Enhances the quality of an mp3 or wav file. 
- **Visual question answering (sieve/llava-vl-13b)**: Visual question answering with GPT-4 level capabilities.

## Setup

To set up the tool, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Install the required Python packages using: `pip install -r requirements.txt`
3. **Run the CLI**: Use the CLI with `python main.py [command]`. For help on commands, run `python main.py -h`.

## Usage

The CLI provides the following commands:

- `transcription`: Command for transcribing Youtube videos. Requires a URL argument.
- `translation`: Command for translating text. Requires text, source language, and target language arguments.
- `detect_language`: Command for detecting the language of text. Requires text argument.
- `detect_and_translate`: Command for detecting language and then translating text. Requires text and target language arguments.
- `text_to_speech`: Command for converting text to speech. Requires text argument.
- `translate_and_talk`: Command for translating and converting text to speech. Requires text and target language arguments.
- `youtube_download_mp4`: Command for downloading Youtube videos in MP4 format. Requires a URL argument.
- `audio_enhancement`: Command for enhancing the quality of an mp3 or wav file. 
- `visual question answer`: Command for visual question answering with GPT-4 level capabilities.

Each command can be used by running `python main.py [command]` followed by the necessary arguments. For specific details on each command and its required arguments, use `python main.py [command] -h`.
