class MixinChangeLanguage:
    def __init__(self):
        self.__language = 'EN'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        raise AttributeError("property 'language' of 'KeyBoard' object has no setter")
