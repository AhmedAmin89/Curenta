from transformers import pipeline
from utils.model import NLPModel


class BertModel(NLPModel):

    def __init__(self):
        self.transformers_pipeline = pipeline("ner",
                                              model="dslim/bert-base-NER")

    def extract_intent(self, command):
        for intent, patterns in self.INTENT_PATTERNS.items():
            if any(pattern in command.lower() for pattern in patterns):
                return intent
        return None

    def extract_entities(self, command):
        doc = self.transformers_pipeline(command)
        entities = {}
        for ent in doc:
            if ent['entity'] == "B-PER":
                entities.setdefault("name", ent['word'])

        if "male" in command.lower() or "female" in command.lower():
            entities[
                "gender"] = "male" if "male" in command.lower() else "female"
        if "diabetes" in command.lower():
            entities["condition"] = "diabetes"

        return entities
