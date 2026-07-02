class LanguageManager:
    def __init__(self):
        self.language = "fr"

    def set_language(self, lang):
        self.language = lang

    def get_language(self):
        return self.language