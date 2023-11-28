# Import functions from language.py so they can be accessed directly from the package
from .language import translate, detect_and_translate, detect

# Optionally, you can expose the language codes and mappings if needed
from ..variables import language_codes, language_mapping

# This allows users of your package to do something like:
# from language_utils.language import translate
