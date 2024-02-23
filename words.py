import json

LANGUAGES = ["nl", "fr", "hu", 'zn_CH']


class Deck():
    
    def __init__(self, dir="test.json"):
        self._words = []
        raw = {}
        with open(dir, 'r') as f:
            raw = json.load(f)
        for x in raw.keys():
            w = Word(x, raw[x][LANGUAGES[0]], raw[x][LANGUAGES[1]], raw[x][LANGUAGES[2]])
            self._words.append(w)

    def add_word_man(self, en, nl, fr, hu, zn_CH):
        ...


class Word():
    
    def __init__(self, en, nl, fr, hu, zn_CH):
        self._en = en
        self._nl = nl
        self._fr = fr
        self._hu = hu
        self._zn_CH = zn_CH

    def get_en(self):
        return self._en
    
    def get_nl(self):
        return self._nl
    
    def get_fr(self):
        return self._fr
    
    def get_hu(self):
        return self._hu
    
    def get_zn_CH(self):
        return self._hu

    # set specific translations individually
    def set_en(self,word):
        self._en = word
    
    def set_nl(self,word):
        self._nl = word
     
    def set_fr(self,word):
        self._fr = word
    
    def set_hu(self,word):
        self._hu = word
    
    def set_zn_CH(self,word):
        self._zn_CH = word
    
d = Deck()