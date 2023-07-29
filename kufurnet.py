import re
from config.configurator import Configurator


class KufurNet:
    def __init__(self):
        self.cfg = Configurator()
        self.black_words = self.cfg.get_black_words()
        self.stop_words = self.cfg.get_stop_words()

    def analyze(self, text: dict):
        text = text["text"]
        words = self.get_words(text)
        if len(words):
            black_list = []
            for word in words:
                if word in self.black_words:
                    black_list.append(word)

            return {
                "status": True,
                "result": {
                    "is_black": len(black_list) > 0,
                    "black_score": round((len(black_list) / len(words)), 2),
                    "black_list": black_list
                }
            }
        return {
            "status": True,
            "result": {
                "is_black": False,
                "black_score": 0,
                "black_list": []
            }
        }

    def get_words(self, text):

        text = text.replace(",", " ")
        text = text.replace("'", " ")
        text = text.replace('.', " ")

        text = re.sub(r'[^\w\s]', '', text.lower())  # remove puncts.

        text = text.replace("  ", " ")
        text = text.replace("   ", " ")
        words = text.split(" ")
        words = [word for word in words if len(word) > 1]
        return [word for word in words if word not in self.stop_words]
