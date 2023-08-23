import joblib


class LoadModel:
    def get_model(self,model_path):
        return joblib.load(model_path)
    def get_models(self):
        toygar_model = self.get_model("models/toygar_model.joblib")
        troff_model = self.get_model("models/sinkaf_model.joblib")
        toygar_troff_model = self.get_model("models/toygar_sinkaf_model.joblib")
        return toygar_model,troff_model,toygar_troff_model
