import sieve
from variables import language_codes, language_mapping

def translate(original_text, source, target):
    if source not in language_codes or target not in language_codes:
        return "Not valid Source or Target language" 
    seamless_text2text = sieve.function.get("sieve/seamless_text2text")
    output = seamless_text2text.run(original_text, source, target)
    return output

def detect_and_translate(original_text, target):
    result_detected = detect(original_text)
    source_detected = language_mapping[result_detected['language_code']]

    output = translate(original_text, source_detected, target) 
    return output

def detect(text):
    langid = sieve.function.get("sieve/langid")
    output = langid.run(text)
    return output