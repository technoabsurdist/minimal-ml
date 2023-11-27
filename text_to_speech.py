import sieve
import shutil
from text_to_speech import convert_text_to_speech
from language import detect_and_translate

def convert_text_to_speech(text):
    voice_id = "21m00Tcm4TlvDq8ikWAM"
    stability = 0.5
    similarity_boost = 0.63
    style = 0
    use_speaker_boost = True
    model_id = "eleven_multilingual_v2"

    elevenlabs_speech_synthesis = sieve.function.get("sieve/elevenlabs_speech_synthesis")
    output = elevenlabs_speech_synthesis.run(text, voice_id, stability, similarity_boost, style, use_speaker_boost, model_id)
    destination_path = "downloads/output.mp3"
    shutil.copy(output.path, destination_path)
    return destination_path

def translate_and_talk(text, target):
    detection = detect_and_translate(text, target)
    return convert_text_to_speech(detection)
