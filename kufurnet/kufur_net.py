import re
from kufurnet.configurator import Configurator


class KufurNet:
    def __init__(self):
        self.cfg = Configurator()
        self.black_words = self.cfg.get_black_words()
        self.stop_words = self.cfg.get_stop_words()

    def get_swears(self, comment: dict):
        comment = comment["comment"]
        words = self.get_comment_words(comment)
        black_list = []
        for word in words:
            if word in self.black_words:
                black_list.append(word)

        len_words = len(words)
        len_blacks = len(black_list)

        swear_score = round((len_blacks / len_words), 2)
        if swear_score > 0:
            return {
                "Offensive": True,
                "Score": swear_score,
                "BlackList": black_list
            }
        return {
            "Offensive": False,
            "Score": 0,
            "BlackList": []
        }

    def get_comment_words(self, comment):
        comment = re.sub(r'[^\w\s]', '', comment)
        comment = comment.replace("  ", " ")
        words = comment.split(" ")
        words = [word for word in words if len(word) > 1]
        return [word for word in words if word not in self.stop_words]

    def get_json_comment(self,json_data,comment_id):
        return json_data[comment_id]["Comment"]

    def get_swears_1(self, comment_data: dict):
        result = {}
        for key, comment in comment_data.items():
            words = self.get_comment_words(comment["text"])
            black_list = []
            for word in words:
                if word in self.black_words:
                    black_list.append(word)

            len_words = len(words)
            len_blacks = len(black_list)

            swear_score = round((len_blacks / len_words), 2)
            if swear_score > 0:
                result[key] = {
                    "text": comment["text"],  # text alanını sonuçlara ekliyoruz
                    "Offensive": True,
                    "Score": swear_score,
                    "BlackList": black_list
                }
            else:
                result[key] = {
                    "text": comment["text"],  # text alanını sonuçlara ekliyoruz
                    "Offensive": False,
                    "Score": 0,
                    "BlackList": []
                }
        return result
