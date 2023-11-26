from pydantic import BaseModel
from flask import Flask, request, jsonify
from translation import translate
from interfaces import TranslationRequest
from yb_transcription import yb_transcript

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/transcription', methods=['POST'])
def transcription():
    try:
        request_data = TranslationRequest(**request.json)
    except ValueError as e:
        return {"error": str(e)}, 400

    result = yb_transcript(request_data.url)
    return result

@app.route('/translation', methods=['POST'])
def translation():
    try:
        request_data = TranslationRequest(**request.json)
    except ValueError as e:
        return {"error": str(e)}, 400

    result = translate(request_data.text, request_data.source, request_data.target)
    return result

if __name__ == '__main__':
    app.run(debug=True)