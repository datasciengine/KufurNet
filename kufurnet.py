import re
from configurator import Configurator
from load_model import LoadModel
from profanityfilter import ProfanityFilter


class KufurNet:
    def __init__(self):
        self.cfg = Configurator()
        self.black_starts = self.cfg.get_start_words()
        self.black_in = self.cfg.get_in_words()
        self.black_exact = self.cfg.get_exact_words()
        self.stop_words = self.cfg.get_stop_words()

    def ml_analyze(self, text: str):
        models = LoadModel().get_models()
        threshold = 1  # Eşik değeri
        profanity_filter = ProfanityFilter(models, threshold)

        prediction = profanity_filter.predict(text)
        print(prediction)

        return prediction

    def filter_analyze(self, text: str):

        words = self.get_words(text)
        if len(words):
            black_list = []
            for word in words:
                if word in self.black_exact:
                    black_list.append(word)
                for black in self.black_in:
                    if black in word:
                        black_list.append(word)
                for black in self.black_starts:
                    if word.startswith(black):
                        black_list.append(word)
            return len(black_list) > 0, round((len(black_list) / len(words)), 2), black_list

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

    def validate_input(self, input_message):

        if not isinstance(input_message, dict):
            raise TypeError(f"Input message should be dict but you gave {type(input_message)} type.")

        if "text" not in input_message.keys():
            raise KeyError(f"Input message does not contain key variable as 'text'.")

        if len(input_message.keys()) != 1:
            raise ValueError(f"Length of item should be 1, but you gave {len(input_message.keys())}.")

        if len(input_message["text"]) <= 2:
            raise ValueError(
                f"Please check min character constraint in the message. Lower limit is 2 char. Your message has {len(input_message['text'])} char.")

        if len(input_message["text"]) >= 200:
            raise ValueError(
                f"Please check max character constraint in the message. Upper limit is 200 char. Your message has {len(input_message['text'])} char.")
