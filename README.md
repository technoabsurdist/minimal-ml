
<div align="center"> 
    <h1>Minimal ML</h1>
    <img src="./cover-image.png" height="200" width="200">
    <h4>
    Python package which provides useful and common interactions with ML functionalities <br /> such as detecting language, chatbots, 
    link transcriptions, audio enhancements, and much more.  
    </h4>
    <h5>Powered by <a href="https://www.sievedata.com/">Sieve</a>, <a href="https://www.langchain.com/">Langchain</a></h5>

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
pip install minimalml

2. **Import in Your Project**: Import the required functionalities in your Python project:
```python
from minimalml.translation import translate
from minimalml.text_to_speech import convert_text_to_speech
# ... other imports as needed
```

<br />

## Usage

The package offers a range of functionalities that can be easily integrated into Python projects. Here are some of the features and how to use them:

<br />

**Translation**: Use `translate(original_text, source_language, target_language)` to translate text. <br />
```python
from minimalml.language import translate

translated_text = translate("Hello, world!", "en", "es")
print(translated_text)
```
<br />

**Youtube Link Transcription**: Use `yb_transcript(url)` to get transcriptions of YouTube videos. <br />
```python
from minimalml.yb import yb_transcript

transcript = yb_transcript("https://www.youtube.com/watch?v=example")
print("Transcript:", transcript)
```
<br />

**Detect Language**: Use `detect(text)` to identify the language of a given text. <br />
```python
from minimalml.language import detect

language_code = detect("Ceci est un texte en français.")
print(f"The detected language code is: {language_code}")
```
<br />

**Text to Speech**: Use `convert_text_to_speech(text)` to convert text into speech. <br />
```python
from minimalml.text_to_speech import convert_text_to_speech

audio_file_path = convert_text_to_speech("Hello, this is a test.")
print(f"Audio file saved at: {audio_file_path}")
```
<br />

**Translate and Talk**: Use `translate_and_talk(text, target_language)` to translate and convert text to speech. <br />
```python
from minimalml.text_to_speech import translate_and_talk

audio_file_path = translate_and_talk("This is a test.", "es")
print(f"Translated and converted to speech, file saved at: {audio_file_path}")
```
<br />

**Youtube Video Download**: Use `yb_download(url)` to download YouTube videos. <br />
```python
from minimalml.yb import yb_download

video_path = yb_download("https://www.youtube.com/watch?v=example")
print(f"Video downloaded at: {video_path}")
```
<br />

**Detect Language and Translate**: Combine detect and translate for detecting and translating text. <br />
```python
from minimalml.language import detect_and_translate

translated_text = detect_and_translate("Bonjour le monde!", "en")
print(translated_text)
```
<br />

**Audio Enhancement**: Use `enhance_audio(audio_url, speed_boost, steps)` for audio enhancement. <br />
```python
from minimalml.audio import enhance_audio

enhanced_audio_path = enhance_audio("http://example.com/audio.mp3", True, 50)
print(f"Enhanced audio saved at: {enhanced_audio_path}")
```
<br />

**Visual question answering**: Use `visual_question_answering(image_url, prompt)` for visual Q&A. <br /> 
```python
from minimalml.visual import visual_question_answering

answer = visual_question_answering("http://example.com/image.jpg", "What is depicted in this image?")
print(answer)
```
<br />


## Contributing!
Please consider contributing to this young and humble project! 
Email any questions at andere.emi@gmail.com
