
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


<br />

## Setup

To set up the package, follow these steps:

1. **Install the Package**: Install this package using pip:
pip install ml_api

2. **Import in Your Project**: Import the required functionalities in your Python project:
```python
from ml_api.translation import translate
from ml_api.text_to_speech import convert_text_to_speech
# ... other imports as needed
```

<br />

## Usage

The package offers a range of functionalities that can be easily integrated into Python projects. Here are some of the features and how to use them:

**Translation**: Use `translate(original_text, source_language, target_language)` to translate text. <br />
**Youtube Link Transcription**: Use `yb_transcript(url)` to get transcriptions of YouTube videos. <br />
**Detect Language**: Use `detect(text)` to identify the language of a given text. <br />
**Text to Speech**: Use `convert_text_to_speech(text)` to convert text into speech. <br />
**Translate and Talk**: Use `translate_and_talk(text, target_language)` to translate and convert text to speech. <br />
**Youtube Video Download**: Use `yb_download(url)` to download YouTube videos. <br />
**Detect Language and Translate**: Combine detect and translate for detecting and translating text. <br />
**Audio Enhancement**: Use `enhance_audio(audio_url, speed_boost, steps)` for audio enhancement. <br />
**Visual question answering**: Use `visual_question_answering(image_url, prompt)` for visual Q&A. <br /> 

Each function can be directly used in your Python code after importing the respective module from the ml_api package. <br />

<br />

## Contributing!
Please consider contributing to this young and humble project! 
Email any questions at andere.emi@gmail.com