import sieve 
from variables import language_codes

def translate(original_text, source, target):
    if source not in language_codes or target not in language_codes:
        return "Not valid Source or Target language" 
    seamless_text2text = sieve.function.get("sieve/seamless_text2text")
    output = seamless_text2text.run(original_text, source, target)
    if not output:
        return "Error in generation."
    return output


