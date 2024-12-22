from utils.bert_model import BertModel
from utils.spacy_model import SpaCyModel


class NLPManager:
    def __init__(self, model_type="spacy"):
        if model_type == "spacy":
            self.model = SpaCyModel()
        elif model_type == "bert":
            self.model = BertModel()
        else:
            raise ValueError("Invalid model type. Choose 'spacy' or 'bert'.")

    def extract_intent(self, command):
        return self.model.extract_intent(command)

    def extract_entities(self, command):
        return self.model.extract_entities(command)
