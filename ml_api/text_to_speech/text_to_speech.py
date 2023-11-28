import sieve
import shutil
from text_to_speech import convert_text_to_speech
from ..language import detect_and_translate

def convert_text_to_speech(text):
    """
    Converts text to speech using the ElevenLabs speech synthesis functionality in the 'sieve' library.

    The function takes a string of text and converts it into spoken words in an audio file format. 
    It uses predefined parameters for voice ID, stability, similarity boost, style, and speaker boost 
    to control the speech synthesis process.

    Parameters:
    - text (str): The text to be converted to speech.

    Returns:
    - str: The file path to the saved audio file containing the spoken version of the input text.

    Note:
    - The generated audio file is saved in the 'downloads' directory with the name 'output.mp3'.
    - The function uses the 'eleven_multilingual_v2' model for speech synthesis.
    """
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
    """
    Translates the given text into a target language and converts the translated text to speech.

    This function first translates the input text into the specified target language using the 
    'detect_and_translate' function. Then, it converts this translated text into speech using 
    the 'convert_text_to_speech' function.

    Parameters:
    - text (str): The text to be translated and converted to speech.
    - target (str): The target language code for translation.

    Returns:
    - str: The file path to the saved audio file containing the spoken version of the translated text.

    Note:
    - The function leverages 'detect_and_translate' for translation and 'convert_text_to_speech' for speech synthesis.
    """
    detection = detect_and_translate(text, target)
    return convert_text_to_speech(detection)
