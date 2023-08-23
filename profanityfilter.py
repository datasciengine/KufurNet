import numpy as np


class ProfanityFilter:
    def __init__(self, models, threshold=0.5):
        self.models = models
        self.weights = weights = [1, 1, 1]
        self.weights = weights if weights else np.ones(len(models))
        self.threshold = threshold

    def predict_single(self, text):
        predictions = []
        for model in self.models:
            prediction = model.predict([text])[0]
            predictions.append(prediction)
        combined_prediction = np.dot(predictions, self.weights)

        final_label = 1 if combined_prediction >= self.threshold else 0
        return final_label

    def predict(self, text):
        return self.predict_single(text)
