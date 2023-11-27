from text_to_speech import convert_text_to_speech
from translation import detect_and_translate

def translate_and_talk(text, target):
    detection = detect_and_translate(text, target)
    return convert_text_to_speech(detection)
