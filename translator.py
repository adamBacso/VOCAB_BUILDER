from googletrans import Translator, constants


class MyTranslator:
    gTranslator = Translator()

    DEFAULT_LANGUAGE = "fr"

    DEFAULT_LANGUAGES = ["en", "fr", "hu", "nl", "zh-CN"]


    def __init__(self, defaultOriginLanguage="xx", approvedLanguages=[]):

        if defaultOriginLanguage == "xx":
            self._defaultOriginLanguage = self.DEFAULT_LANGUAGE
        else:
            self._defaultOriginLanguage = defaultOriginLanguage
        
        if approvedLanguages == []:
            self._activeLanguages = self.DEFAULT_LANGUAGES
        else:
            self._activeLanguages = approvedLanguages
    

    def display_languages(self):

        for i in range(len(self._activeLanguages)):
            print(i+f(". ")+self._activeLanguages[i])

    def add_language(self):
        self._activeLanguagesappend(language)
    
    def remove_approved_language(self, language):
        if language in self._activeLanguages:
            self._activeLanguages.remove(language)
        else:
            print(f("Err: target language not an active language."))
            self.display_languages()

    def set_default_origin_language(self, language=None):
        if language==None:
            lanugage = self._defaultOriginLanguage

        if language in self._activeLanguages:
            self._defaultOriginLanguage = language
        else:
            print(f("Err: Invalid language"))

    """
    Postcondition: returns an array of strings in the order of _activeLanguages
    """
    def translate_word(self, word):
        translations = []
        language = self.gTranslator.detect(word).lang
        for lang in self._activeLanguages:
            if lang != language:
                translations.append(self.gTranslator.translate(word,lang,language).text)
            else:
                translations.append(word)
        return translations