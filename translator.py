from googletrans import Translator, constants

class MyTranslator:
    _defaultOriginLanguage = None
    _approvedLanguages = None

    def __init__(self, defaultOriginLanguage="fr", approvedLanguages=["en", "fr", "hun", "nl", "ch"]):
        self._defaultOriginLanguage = defaultOriginLanguage
        self._approvedLanguages = approvedLanguages

    def set_default_origin_language(language):
        if language in _approvedLanguages:
            _defaultOriginLanguage = language
        else:
            print(f("Err: Invalid language"))

    def translate_word(word):
        pass