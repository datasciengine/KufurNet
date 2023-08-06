import json


class Configurator:
    """

    """

    def __init__(self, path="config/config.json"):
        self.cfg = self.load_json(path)

    def get_stop_words(self):
        return self.load_txt(self.cfg["stop_words_path"])

    def get_black_words(self):
        return self.load_txt(self.cfg["black_words_path"])

    def get_start_words(self):
        return self.load_txt(self.cfg["starts_words_path"])

    def get_in_words(self):
        return self.load_txt(self.cfg["in_words_path"])

    def get_exact_words(self):
        return self.load_txt(self.cfg["exact_words_path"])

    @staticmethod
    def load_json(path, encoding="utf-8"):
        with open(path, encoding=encoding) as file:
            return json.load(file)

    @staticmethod
    def load_txt(path, encoding="utf-8"):
        with open(path, 'r', encoding=encoding) as f:
            return f.read().splitlines()
