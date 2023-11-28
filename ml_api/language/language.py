import sieve
from ..variables import language_codes, language_mapping

def translate(original_text, source, target):
    """
    Translates text from a source language to a target language.

    Utilizes the 'sieve' library's seamless_text2text function for translation.
    The function checks if the source and target languages are valid based on a predefined list of language codes.

    Parameters:
    - original_text (str): The text to be translated.
    - source (str): The source language code.
    - target (str): The target language code.

    Returns:
    - str: The translated text if source and target languages are valid, otherwise a not valid language error message.

    Note:
    - The language codes should be part of the predefined 'language_codes' list.
    """
    if source not in language_codes or target not in language_codes:
        return "Not valid Source or Target language"
    seamless_text2text = sieve.function.get("sieve/seamless_text2text")
    return seamless_text2text.run(original_text, source, target)

def detect_and_translate(original_text, target):
    """
    Detects the language of the given text and translates it to a target language.

    First, the function detects the language of the original text. Then, it translates the text 
    to the specified target language using the 'translate' function.

    Parameters:
    - original_text (str): The text for which the language is to be detected and then translated.
    - target (str): The target language code for translation.

    Returns:
    - str: The translated text into the target language.

    Note:
    - The function relies on the 'detect' and 'translate' functions.
    """
    result_detected = detect(original_text)
    source_detected = language_mapping[result_detected['language_code']]
    return translate(original_text, source_detected, target) 

def detect(text):
    """
    Detects the language of a given piece of text.

    Uses the 'sieve' library's langid function to identify the language of the input text.

    Parameters:
    - text (str): The text whose language needs to be detected.

    Returns:
    - dict: A dictionary with the detected language code.
    
    Note:
    - The returned dictionary includes the language code under the key 'language_code'.
    """
    langid = sieve.function.get("sieve/langid")
    return langid.run(text)
