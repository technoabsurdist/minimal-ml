from flask import Flask, request, jsonify
from detect_language import detect
from text_to_speech import convert_text_to_speech
from translate_and_talk import translate_and_talk
from translation import detect_and_translate, translate
import interfaces
from yb import yb_download, yb_transcript

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/transcription', methods=['POST'])
def transcription():
    try:
        request_data = interfaces.TranslationRequest(**request.json)
    except ValueError as e:
        return {"error": str(e)}, 400

    result = yb_transcript(request_data.url)
    return result, 200

@app.route('/translation', methods=['POST'])
def translation():
    try:
        request_data = interfaces.TranslationRequest(**request.json)
    except ValueError as e:
        return {"error": str(e)}, 400

    result = translate(request_data.text, request_data.source, request_data.target)
    return result, 200

@app.route('/detect_language', methods=['POST'])
def detect_language():
    try:
        request_data = interfaces.DetectLanguageRequest(**request.json)
    except ValueError as e:
        return {"error": str(e)}, 400
    
    result = detect(request_data.text)
    return result, 200

@app.route('/detect_and_translate', methods=['POST'])
def translate_with_detect():
    try:
        request_data = interfaces.DetectAndTranslateRequest(**request.json)
    except ValueError as e:
        return {"error": str(e)}, 400
 
    result = detect_and_translate(request_data.text, request_data.target)
    return result, 200
    
@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():
    try:
        request_data = interfaces.TextToSpeechRequest(**request.json)
    except ValueError as e:
        return {"error": str(e)}, 400

    result = convert_text_to_speech(request_data.text)
    return result, 200

@app.route('/translate_and_talk', methods=['POST'])
def translate_and_speech():
    try:
        request_data = interfaces.TranslateToSpeechRequest(**request.json)
    except ValueError as e:
        return {"error": str(e)}, 400

    result = translate_and_talk(request_data.text, request_data.target)
    return result, 200

@app.route('/youtube_download_mp4', methods=['POST'])
def youtube_download_mp4():
    try:
        request_data = interfaces.YoutubeDownloadRequest(**request.json)
    except ValueError as e:
        return {"error": str(e)}, 400

    result = yb_download(request_data.url)
    return result, 200

if __name__ == '__main__':
    app.run(debug=True)
