import re
from config.configurator import Configurator


class KufurNet:
    def __init__(self):
        self.cfg = Configurator()
        self.black_starts = self.cfg.get_start_words()
        self.black_in = self.cfg.get_in_words()
        self.black_exact = self.cfg.get_exact_words()
        self.stop_words = self.cfg.get_stop_words()

    def analyze(self, text: dict):
        text = text["text"]
        words = self.get_words(text)
        if len(words):
            black_list = []
            for word in words:

                if word in self.black_exact:
                    black_list.append(word)
                    # print("Exact ->", word)
                    break
                for black in self.black_in:
                    if black in word:
                        black_list.append(word)
                        # print("In ->", word)
                        break
                for black in self.black_starts:
                    if word.startswith(black):
                        black_list.append(word)
                        # print("Starts ->", word)
                        break
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
